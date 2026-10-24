"""The client: one call() for any tool, and a typed method per tool on top."""

from __future__ import annotations

import json
import os
import random
import time
import urllib.error
import urllib.request
from typing import Any, Callable, Dict, Optional

from ._tools import READ_ONLY_TOOLS, Tools
from .errors import NetworkError, RateLimitError, SeolyticizeError, error_for_status

DEFAULT_BASE_URL = "https://seolyticize.com"
VERSION = "0.3.0"


class Seolyticize(Tools):
    """A Seolyticize API client.

    >>> client = Seolyticize()  # reads SEOLYTICIZE_API_KEY
    >>> client.get_next_steps(client_id="client_…")

    Every tool is a method (``client.onboard_site(domain="example.com")``), and
    ``client.call("tool_name", {...})`` reaches tools newer than this SDK.
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        *,
        base_url: Optional[str] = None,
        timeout: float = 60.0,
        max_retries: int = 2,
        max_retry_after: float = 60.0,
        sleep: Callable[[float], None] = time.sleep,
    ) -> None:
        key = api_key or os.environ.get("SEOLYTICIZE_API_KEY")
        if not key:
            raise SeolyticizeError(
                "An API key is required: pass api_key or set SEOLYTICIZE_API_KEY.",
                code="no_api_key",
            )
        self.api_key = key
        self.base_url = (base_url or os.environ.get("SEOLYTICIZE_BASE_URL") or DEFAULT_BASE_URL).rstrip("/")
        self.timeout = timeout
        self.max_retries = max_retries
        self.max_retry_after = max_retry_after
        self._sleep = sleep
        #: The X-RateLimit-* headers from the latest response.
        self.last_rate_limit: Dict[str, Optional[int]] = {}

    # -- requests ----------------------------------------------------------

    def _request(self, method: str, path: str, body: Optional[Dict[str, Any]], tool: Optional[str], retry_transient: bool) -> Any:
        data = None if body is None else json.dumps(body).encode("utf-8")
        attempt = 0
        while True:
            request = urllib.request.Request(
                self.base_url + path,
                data=data,
                method=method,
                headers={
                    "authorization": f"Bearer {self.api_key}",
                    "content-type": "application/json",
                    "accept": "application/json",
                    "user-agent": f"seolyticize-python/{VERSION}",
                },
            )
            try:
                with urllib.request.urlopen(request, timeout=self.timeout) as response:
                    self._remember_rate(response.headers)
                    payload = json.loads(response.read().decode("utf-8") or "{}")
                    return payload.get("data", payload)
            except urllib.error.HTTPError as failure:
                self._remember_rate(failure.headers)
                status = failure.code
                details = _details(failure)
                retry_after = _float(failure.headers.get("retry-after"))
                can_retry = attempt < self.max_retries
                if status == 429 and can_retry and (retry_after or 0) <= self.max_retry_after:
                    self._sleep(retry_after if retry_after is not None else _backoff(attempt))
                    attempt += 1
                    continue
                if status >= 500 and retry_transient and can_retry:
                    self._sleep(_backoff(attempt))
                    attempt += 1
                    continue
                extra = {"retry_after": retry_after} if status == 429 else {}
                raise error_for_status(status, details["message"], code=details["code"], next=details["next"], request_id=details["request_id"], tool=tool, **extra) from None
            except (urllib.error.URLError, TimeoutError, ConnectionError) as failure:
                if retry_transient and attempt < self.max_retries:
                    self._sleep(_backoff(attempt))
                    attempt += 1
                    continue
                raise NetworkError(f"No response from {self.base_url}: {failure}", tool=tool) from None

    def _remember_rate(self, headers: Any) -> None:
        if headers is None:
            return
        self.last_rate_limit = {
            "limit": _int(headers.get("x-ratelimit-limit")),
            "remaining": _int(headers.get("x-ratelimit-remaining")),
            "reset_seconds": _int(headers.get("x-ratelimit-reset")),
        }

    # -- public ------------------------------------------------------------

    def call(self, tool: str, input: Optional[Dict[str, Any]] = None) -> Any:
        """Calls any tool by name with a JSON-shaped input (camelCase keys, as the API takes them)."""
        # A tool this SDK has never heard of may be a write; it is not retried
        # on server errors, since repeating a write could do it twice.
        return self._request("POST", f"/api/v1/tools/{tool}", input or {}, tool, tool in READ_ONLY_TOOLS)

    def list_tools(self, group: Optional[str] = None) -> Dict[str, Any]:
        """The tools this key may call, with their schemas; ``group`` narrows to one job (onboarding, weekly, technical, research, reporting)."""
        query = f"?group={group}" if group else ""
        return self._request("GET", f"/api/v1/tools{query}", None, None, True)


def _details(failure: urllib.error.HTTPError) -> Dict[str, Optional[str]]:
    try:
        body = json.loads(failure.read().decode("utf-8") or "{}")
    except Exception:  # an HTML error page from a proxy
        body = {}
    text = lambda value: value if isinstance(value, str) and value else None  # noqa: E731
    return {
        "message": text(body.get("error")) or f"HTTP {failure.code}",
        "code": text(body.get("code")),
        "next": text(body.get("next")),
        "request_id": text(body.get("requestId")) or failure.headers.get("x-request-id"),
    }


def _backoff(attempt: int) -> float:
    return min(8.0, 0.5 * (2**attempt)) * (0.5 + random.random() / 2)


def _int(value: Optional[str]) -> Optional[int]:
    try:
        return int(value) if value is not None else None
    except ValueError:
        return None


def _float(value: Optional[str]) -> Optional[float]:
    try:
        return float(value) if value is not None else None
    except ValueError:
        return None
