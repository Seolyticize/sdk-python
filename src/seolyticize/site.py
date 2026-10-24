"""On-site helpers: what a website itself needs, in Django, Flask, FastAPI or anything.

- :func:`analytics_tag` — the cookieless analytics ``<script>`` for your templates.
- :func:`indexnow_key_response` — the body and headers to serve your IndexNow key file.
- :func:`notify_deploy` — call after each deploy; changed pages go to IndexNow.
- :func:`track_event` — send a pageview or custom event from your server.

For page views reported from the server with the visitor's own address and
user agent (and AI assistants counted), see :mod:`seolyticize.collect`.
"""

from __future__ import annotations

import json
import urllib.request
from html import escape
from typing import Any, Dict, Iterable, Optional, Tuple

DEFAULT_BASE_URL = "https://seolyticize.com"


def analytics_tag(
    site_key: str,
    *,
    exclude: Optional[Iterable[str]] = None,
    include: Optional[Iterable[str]] = None,
    track: Optional[Iterable[str]] = None,
    base_url: str = DEFAULT_BASE_URL,
) -> str:
    """The analytics tag, HTML-escaped, for the ``<head>`` of every page.

    ``exclude=["/app/*", "/verify"]`` keeps paths from ever being reported;
    ``track=["outbound", "downloads"]`` records those clicks as events.
    Mark it safe in your template engine (``|safe`` in Django or Jinja).
    """
    attrs = {"defer": None, "data-site": site_key, "src": f"{base_url.rstrip('/')}/a.js"}
    if exclude:
        attrs["data-exclude"] = ",".join(exclude)
    if include:
        attrs["data-include"] = ",".join(include)
    if track:
        attrs["data-track"] = " ".join(track)
    rendered = " ".join(name if value is None else f'{name}="{escape(value, quote=True)}"' for name, value in attrs.items())
    return f"<script {rendered}></script>"


def indexnow_key_response(key: str) -> Tuple[str, Dict[str, str]]:
    """The body and headers to serve at ``/<key>.txt``. In Django::

        def indexnow(request):
            body, headers = indexnow_key_response(KEY)
            return HttpResponse(body, headers=headers)

        urlpatterns = [path(f"{KEY}.txt", indexnow), ...]

    In Flask: ``return indexnow_key_response(KEY)`` from a ``/<KEY>.txt`` route.
    """
    return key, {"Content-Type": "text/plain; charset=utf-8", "Cache-Control": "public, max-age=3600"}


def _post(url: str, body: Dict[str, Any], timeout: float) -> Dict[str, Any]:
    request = urllib.request.Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        method="POST",
        headers={"content-type": "application/json", "user-agent": "seolyticize-python-site/0.4.0"},
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        text = response.read().decode("utf-8")
        return json.loads(text) if text else {}


def notify_deploy(hook_url: str, urls: Optional[Iterable[str]] = None, *, timeout: float = 120.0) -> Dict[str, Any]:
    """Tells Seolyticize a deploy finished (the URL from ``create_deploy_hook``).

    Without ``urls`` the sitemap is compared with the last deploy's and the new
    and changed pages go to IndexNow; with them, exactly those are sent.
    """
    return _post(hook_url, {"urls": list(urls)} if urls is not None else {}, timeout)


def track_event(
    site_key: str,
    url: str,
    name: str = "pageview",
    *,
    referrer: Optional[str] = None,
    props: Optional[Dict[str, Any]] = None,
    base_url: str = DEFAULT_BASE_URL,
    timeout: float = 10.0,
) -> None:
    """Sends one event to ``/api/collect`` from a server.

    Every event sent from one server address counts as one visitor; send from
    the browser where you can. Only the path and ``utm_*`` tags of ``url`` are kept.
    """
    body: Dict[str, Any] = {"k": site_key, "n": name, "u": url}
    if referrer:
        body["r"] = referrer
    if props:
        body["p"] = props
    _post(f"{base_url.rstrip('/')}/api/collect", body, timeout)
