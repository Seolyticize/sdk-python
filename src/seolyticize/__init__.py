"""Seolyticize: the API client, and on-site helpers in :mod:`seolyticize.site`."""

from ._client import DEFAULT_BASE_URL, VERSION, Seolyticize
from ._tools import TOOL_COUNT
from .errors import (
    AuthenticationError,
    NetworkError,
    NotFoundError,
    PermissionError,
    RateLimitError,
    RefusedError,
    SeolyticizeError,
    ServerError,
    ValidationError,
)

__version__ = VERSION
__all__ = [
    "Seolyticize",
    "DEFAULT_BASE_URL",
    "TOOL_COUNT",
    "SeolyticizeError",
    "ValidationError",
    "AuthenticationError",
    "PermissionError",
    "NotFoundError",
    "RefusedError",
    "RateLimitError",
    "ServerError",
    "NetworkError",
]
