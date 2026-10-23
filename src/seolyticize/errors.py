"""What the API said when it said no, as classes a caller can branch on."""

from __future__ import annotations

from typing import Optional


class SeolyticizeError(Exception):
    """Any failure. ``code`` is stable — branch on it, not on the message."""

    def __init__(
        self,
        message: str,
        *,
        status: Optional[int] = None,
        code: Optional[str] = None,
        next: Optional[str] = None,
        request_id: Optional[str] = None,
        tool: Optional[str] = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.status = status
        self.code = code
        #: The call or step that fixes it, when the server named one.
        self.next = next
        #: Quote this when asking for help: it matches the server's log line.
        self.request_id = request_id
        self.tool = tool

    def __str__(self) -> str:
        parts = [self.message]
        if self.code:
            parts.append(f"(code: {self.code})")
        if self.next:
            parts.append(f"Next: {self.next}")
        return " ".join(parts)


class ValidationError(SeolyticizeError):
    """400: the input did not match the tool's schema."""


class AuthenticationError(SeolyticizeError):
    """401: no key, or one that is unknown, expired or revoked."""


class PermissionError(SeolyticizeError):  # noqa: A001 — mirrors the API's word
    """403: the key's role or reach does not allow this tool or client."""


class NotFoundError(SeolyticizeError):
    """404: no tool by that name."""


class RefusedError(SeolyticizeError):
    """422: a valid request the product declined; ``message`` says why, ``next`` what to do."""


class RateLimitError(SeolyticizeError):
    """429: too many requests; ``retry_after`` is how long to wait, in seconds."""

    def __init__(self, message: str, *, retry_after: Optional[float] = None, **kwargs) -> None:
        super().__init__(message, **kwargs)
        self.retry_after = retry_after


class ServerError(SeolyticizeError):
    """5xx: the request failed on the server. A write may or may not have happened."""


class NetworkError(SeolyticizeError):
    """No response arrived at all."""


def error_for_status(status: int, message: str, **kwargs) -> SeolyticizeError:
    kinds = {400: ValidationError, 401: AuthenticationError, 403: PermissionError, 404: NotFoundError, 422: RefusedError}
    if status == 429:
        return RateLimitError(message, status=status, **kwargs)
    if status >= 500:
        return ServerError(message, status=status, **kwargs)
    return kinds.get(status, SeolyticizeError)(message, status=status, **kwargs)
