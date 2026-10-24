"""Server-side collection for the cookieless analytics, in any Python web stack.

Reports page views from the server, for the visitors that never run the
browser tag — AI assistants such as ChatGPT-User, Claude-User and
Perplexity-User above all — or for a site that would rather not run a tag.
Needs the site's server key from ``issue_server_collect_key``: with it the
report may carry the visitor's address and user agent instead of the
server's, which Seolyticize hashes under a daily salt and never stores.

What leaves the site is the least the report needs: the path with only the
campaign tags (every other query parameter is stripped here), the referrer's
origin, the visitor's address, user agent and country. Bots are dropped here
before anything is sent.

- :class:`Collector` — ``track(...)`` one page view; sends in the background.
  ``track_for_visit(...)`` reports an event for the visitor in front of you and
  returns the visit's token; ``track_later(token, ...)`` credits an event that
  happens afterwards (a payment confirmed by webhook, a trial that converts
  next week) to that visit. Keep the token on your server with the account or
  order — never in a cookie or a page.
- :class:`WSGICollector` — wraps a WSGI app (Flask: ``app.wsgi_app = WSGICollector(app.wsgi_app, collector)``).
- :class:`ASGICollector` — wraps an ASGI app (FastAPI, Starlette).
- :func:`django_middleware` — a Django middleware class for ``MIDDLEWARE``.
"""

from __future__ import annotations

import json
import queue
import re
import threading
import urllib.error
import urllib.request
from typing import Any, Callable, Dict, Iterable, List, Optional, Tuple
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

DEFAULT_COLLECT_URL = "https://seolyticize.com/api/collect"
DEFAULT_ALLOWED_PARAMS = ("utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content")

# The AI assistants that read pages on somebody's behalf; kept in step with
# the server, which decides how each is reported.
_AGENT = re.compile(r"chatgpt-user|claude-user|perplexity-user|mistralai-user", re.I)
_BOT = re.compile(
    "|".join(
        [
            r"bot\b",
            "crawl",
            "spider",
            "slurp",
            "mediapartners",
            "facebookexternalhit",
            "embedly",
            "whatsapp",
            "headless",
            "phantomjs",
            "selenium",
            "webdriver",
            "puppeteer",
            "playwright",
            "lighthouse",
            "pagespeed",
            "gtmetrix",
            "pingdom",
            "uptime",
            "monitor",
            "preview",
            "prerender",
            "curl/",
            "wget/",
            "httpie",
            "python-requests",
            "python-urllib",
            "aiohttp",
            "httpx",
            "go-http-client",
            "java/",
            "okhttp",
            "apache-httpclient",
            "node-fetch",
            "undici",
            "axios/",
            "libwww",
            "scrapy",
            "feedfetcher",
        ]
    ),
    re.I,
)


def classify_agent(user_agent: str, signature_agent: Optional[str] = None) -> str:
    """``"person"``, ``"agent"`` (an AI assistant reading for someone) or ``"bot"``."""
    if signature_agent and re.search(r"chatgpt\.com", signature_agent, re.I):
        return "agent"
    if _AGENT.search(user_agent or ""):
        return "agent"
    if len(user_agent or "") < 20:
        return "bot"
    if _BOT.search(re.sub("cubot", "", user_agent, flags=re.I)):
        return "bot"
    return "person"


def strip_query(url: str, allowed: Iterable[str] = DEFAULT_ALLOWED_PARAMS) -> str:
    """The URL with only the allowed query parameters and no fragment."""
    keep = {name.lower() for name in allowed}
    parts = urlsplit(url)
    query = [(k, v) for k, v in parse_qsl(parts.query, keep_blank_values=True) if k.lower() in keep]
    return urlunsplit((parts.scheme, parts.netloc, parts.path or "/", urlencode(query), ""))


def _pattern(patterns: Optional[Iterable[str]]) -> Optional["re.Pattern[str]"]:
    parts = [re.escape(p.strip()).replace(r"\*", ".*") for p in (patterns or []) if p.strip()]
    return re.compile("^(?:" + "|".join(parts) + ")$") if parts else None


def _referrer_origin(referrer: Optional[str]) -> Optional[str]:
    if not referrer:
        return None
    parts = urlsplit(referrer)
    if parts.scheme not in ("http", "https") or not parts.netloc:
        return None
    return f"{parts.scheme}://{parts.netloc}/"


def is_page_request(method: str, headers: Dict[str, str]) -> bool:
    """A GET for HTML that nobody prefetched. ``headers`` keys are lower case."""
    if method.upper() not in ("GET", "HEAD"):
        return False
    purpose = f"{headers.get('purpose', '')} {headers.get('sec-purpose', '')}"
    if re.search("prefetch|prerender", purpose, re.I):
        return False
    dest = headers.get("sec-fetch-dest")
    if dest and dest != "document":
        return False
    accept = headers.get("accept", "")
    return accept == "" or "text/html" in accept or "*/*" in accept


def address_from(headers: Dict[str, str]) -> Optional[str]:
    """The visitor's address from Cloudflare's header, X-Real-IP, or the first X-Forwarded-For entry."""
    direct = headers.get("cf-connecting-ip") or headers.get("x-real-ip")
    if direct:
        return direct.strip()
    forwarded = headers.get("x-forwarded-for")
    if forwarded:
        first = forwarded.split(",")[0].strip()
        return first or None
    return None


class Collector:
    """Reports page views to Seolyticize from the server.

    ``only="agents"`` reports AI assistants alone — use it when the browser tag
    is installed too, or every person is counted twice. Sending happens on a
    background thread (``background=False`` sends inline, for tests and
    scripts), so a slow network never holds up a page.
    """

    def __init__(
        self,
        site_key: str,
        server_key: str,
        *,
        endpoint: str = DEFAULT_COLLECT_URL,
        exclude: Optional[Iterable[str]] = None,
        include: Optional[Iterable[str]] = None,
        allow_params: Iterable[str] = DEFAULT_ALLOWED_PARAMS,
        only: str = "all",
        timeout: float = 2.0,
        background: bool = True,
        on_error: Optional[Callable[[Exception], None]] = None,
        send: Optional[Callable[[str, bytes, Dict[str, str], float], int]] = None,
        request: Optional[Callable[[str, bytes, Dict[str, str], float], Tuple[int, bytes]]] = None,
    ):
        self.site_key = site_key
        self.server_key = server_key
        self.endpoint = endpoint
        self.allow_params = list(allow_params)
        self.only = only
        self.timeout = timeout
        self.on_error = on_error
        self._exclude = _pattern(exclude)
        self._include = _pattern(include)
        self._send = send or _urlopen_send
        # For the calls whose answer is read (the visit token): status and body.
        self._request = request or _urlopen_request
        self._queue: Optional["queue.Queue[bytes]"] = None
        if background:
            self._queue = queue.Queue(maxsize=1000)
            threading.Thread(target=self._drain, daemon=True, name="seolyticize-collect").start()

    def reports(self, path: str) -> bool:
        value = path[:-1] if len(path) > 1 and path.endswith("/") else path
        if self._exclude and self._exclude.match(value):
            return False
        return not self._include or bool(self._include.match(value))

    def payload(
        self,
        url: str,
        *,
        referrer: Optional[str] = None,
        user_agent: Optional[str] = None,
        ip: Optional[str] = None,
        country: Optional[str] = None,
        client_hints: Optional[str] = None,
        signature_agent: Optional[str] = None,
        name: str = "pageview",
        props: Optional[Dict[str, Any]] = None,
        everyone: bool = False,
    ) -> Optional[Dict[str, Any]]:
        """What would be sent for this page view, or None when nothing would be.

        ``everyone`` ignores ``only="agents"``: an event a visit token is asked
        for is sent for people too.
        """
        if not self.reports(urlsplit(url).path or "/"):
            return None
        kind = classify_agent(user_agent or "", signature_agent)
        if kind == "bot" or (not everyone and self.only == "agents" and kind != "agent"):
            return None
        body: Dict[str, Any] = {
            "k": self.site_key,
            "n": name,
            "u": strip_query(url, self.allow_params),
            "ua": (user_agent or "")[:1024],
        }
        origin = _referrer_origin(referrer)
        if origin:
            body["r"] = origin
        if ip:
            body["ip"] = ip[:64]
        if country:
            body["c"] = country[:2]
        if client_hints:
            body["h"] = client_hints[:512]
        if signature_agent:
            body["sa"] = signature_agent[:256]
        if props:
            body["p"] = props
        return body

    def track(self, url: str, **fields: Any) -> None:
        """Reports one page view (or, with ``name``, a custom event). Never raises."""
        try:
            body = self.payload(url, **fields)
            if body is None:
                return
            data = json.dumps(body).encode("utf-8")
            if self._queue is not None:
                try:
                    self._queue.put_nowait(data)
                except queue.Full:
                    pass  # Dropping a page view beats growing without bound.
            else:
                self._post(data)
        except Exception as error:  # noqa: BLE001 — a report must never break a page
            if self.on_error:
                self.on_error(error)

    def _headers(self) -> Dict[str, str]:
        return {
            "content-type": "application/json",
            "authorization": f"Bearer {self.server_key}",
            "user-agent": "seolyticize-python-collect/0.1.0",
        }

    def track_for_visit(self, url: str, name: str, **fields: Any) -> Optional[str]:
        """Reports an event for the visitor in front of you — a sign-up, a
        checkout started — and returns that visit's token, or None when none
        was issued (a bot, an agent, an excluded path, a failure). Sent inline,
        whatever ``only`` says. Never raises."""
        try:
            body = self.payload(url, name=name, everyone=True, **fields)
            if body is None:
                return None
            status, answer = self._request(
                self.endpoint, json.dumps(body).encode("utf-8"), self._headers(), self.timeout
            )
            if status == 401:
                raise RuntimeError("Seolyticize refused the server key. Issue a new one.")
            if status != 202 or not answer:
                return None
            visit = json.loads(answer.decode("utf-8")).get("visit")
            return visit if isinstance(visit, str) else None
        except Exception as error:  # noqa: BLE001 — a report must never break a page
            if self.on_error:
                self.on_error(error)
            return None

    def track_later(
        self,
        visit: str,
        name: str,
        *,
        props: Optional[Dict[str, Any]] = None,
        url: Optional[str] = None,
    ) -> bool:
        """Credits an event that happened after the visit — a top-up confirmed
        by webhook, a trial converting — to the visit ``visit`` names. ``props``
        may carry ``value``, which a goal without a fixed worth sums. Sent
        inline. Returns True when credited; never raises."""
        try:
            body: Dict[str, Any] = {"k": self.site_key, "n": name, "visit": visit}
            if url:
                body["u"] = strip_query(url, self.allow_params)
            if props:
                body["p"] = props
            status, _ = self._request(
                self.endpoint, json.dumps(body).encode("utf-8"), self._headers(), self.timeout
            )
            if status == 202:
                return True
            # 410: the token outlived its 35 days; 404: its visit was not
            # found; 400: not a token for this site.
            raise RuntimeError(f"Seolyticize did not credit the event (HTTP {status}).")
        except Exception as error:  # noqa: BLE001
            if self.on_error:
                self.on_error(error)
            return False

    def _post(self, data: bytes) -> None:
        try:
            status = self._send(self.endpoint, data, self._headers(), self.timeout)
            if status == 401:
                raise RuntimeError("Seolyticize refused the server key. Issue a new one.")
        except Exception as error:  # noqa: BLE001
            if self.on_error:
                self.on_error(error)

    def _drain(self) -> None:
        assert self._queue is not None
        while True:
            self._post(self._queue.get())

    def track_wsgi(self, environ: Dict[str, Any], status: int) -> None:
        """Reports a finished WSGI request, if it was a successful page view."""
        headers = {
            key[5:].replace("_", "-").lower(): str(value)
            for key, value in environ.items()
            if key.startswith("HTTP_")
        }
        if not (200 <= status < 300) or not is_page_request(environ.get("REQUEST_METHOD", "GET"), headers):
            return
        host = headers.get("x-forwarded-host") or headers.get("host") or environ.get("SERVER_NAME", "localhost")
        scheme = (headers.get("x-forwarded-proto") or environ.get("wsgi.url_scheme", "https")).split(",")[0]
        path = environ.get("PATH_INFO", "/") or "/"
        query = environ.get("QUERY_STRING", "")
        url = f"{scheme}://{host.split(',')[0].strip()}{path}" + (f"?{query}" if query else "")
        self.track(
            url,
            referrer=headers.get("referer"),
            user_agent=headers.get("user-agent"),
            ip=address_from(headers) or environ.get("REMOTE_ADDR"),
            country=headers.get("cf-ipcountry"),
            client_hints=headers.get("sec-ch-ua"),
            signature_agent=headers.get("signature-agent"),
        )


def _urlopen_send(url: str, data: bytes, headers: Dict[str, str], timeout: float) -> int:
    request = urllib.request.Request(url, data=data, method="POST", headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return int(response.status)
    except urllib.error.HTTPError as error:
        return int(error.code)


def _urlopen_request(
    url: str, data: bytes, headers: Dict[str, str], timeout: float
) -> Tuple[int, bytes]:
    request = urllib.request.Request(url, data=data, method="POST", headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return int(response.status), response.read(4096)
    except urllib.error.HTTPError as error:
        return int(error.code), b""


class WSGICollector:
    """WSGI middleware: reports each successful page view after it is served."""

    def __init__(self, app: Callable[..., Iterable[bytes]], collector: Collector):
        self.app = app
        self.collector = collector

    def __call__(self, environ: Dict[str, Any], start_response: Callable[..., Any]) -> Iterable[bytes]:
        seen: List[int] = []

        def recording_start(status: str, headers: List[Any], exc_info: Any = None) -> Any:
            try:
                seen.append(int(status.split(" ", 1)[0]))
            except ValueError:
                pass
            return start_response(status, headers, exc_info) if exc_info else start_response(status, headers)

        result = self.app(environ, recording_start)
        if seen:
            self.collector.track_wsgi(environ, seen[0])
        return result


class ASGICollector:
    """ASGI middleware (FastAPI, Starlette): reports each successful page view."""

    def __init__(self, app: Callable[..., Any], collector: Collector):
        self.app = app
        self.collector = collector

    async def __call__(self, scope: Dict[str, Any], receive: Callable[..., Any], send: Callable[..., Any]) -> None:
        if scope.get("type") != "http":
            await self.app(scope, receive, send)
            return
        status: List[int] = []

        async def recording_send(message: Dict[str, Any]) -> None:
            if message.get("type") == "http.response.start":
                status.append(int(message.get("status", 0)))
            await send(message)

        await self.app(scope, receive, recording_send)
        if status:
            environ = _environ_from_scope(scope)
            self.collector.track_wsgi(environ, status[0])


def _environ_from_scope(scope: Dict[str, Any]) -> Dict[str, Any]:
    environ: Dict[str, Any] = {
        "REQUEST_METHOD": scope.get("method", "GET"),
        "PATH_INFO": scope.get("path", "/"),
        "QUERY_STRING": (scope.get("query_string") or b"").decode("latin-1"),
        "wsgi.url_scheme": scope.get("scheme", "https"),
    }
    client = scope.get("client")
    if client:
        environ["REMOTE_ADDR"] = client[0]
    for raw_name, raw_value in scope.get("headers", []):
        name = raw_name.decode("latin-1").upper().replace("-", "_")
        environ[f"HTTP_{name}"] = raw_value.decode("latin-1")
    return environ


def django_middleware(collector: Collector) -> type:
    """A Django middleware class reporting through ``collector``::

        # settings.py
        SEOLYTICIZE = Collector(SITE_KEY, os.environ["SEOLYTICIZE_SERVER_KEY"])
        # middleware.py
        SeolyticizeMiddleware = django_middleware(settings.SEOLYTICIZE)
        # MIDDLEWARE = [..., "myapp.middleware.SeolyticizeMiddleware"]
    """

    class SeolyticizeMiddleware:
        def __init__(self, get_response: Callable[[Any], Any]):
            self.get_response = get_response

        def __call__(self, request: Any) -> Any:
            response = self.get_response(request)
            collector.track_wsgi(request.META, int(getattr(response, "status_code", 0)))
            return response

    return SeolyticizeMiddleware
