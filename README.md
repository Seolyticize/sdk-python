# Seolyticize for Python

Every [Seolyticize](https://seolyticize.com) API tool as a method, and on-site helpers for analytics, IndexNow and deploys. Standard library only, Python 3.9+.

```sh
pip install "git+https://github.com/Seolyticize/sdk-python"
```

## Quick start

```python
from seolyticize import Seolyticize

client = Seolyticize()  # reads SEOLYTICIZE_API_KEY

# Onboard a site: one call returns everything to deploy.
manifest = client.onboard_site(domain="example.com", framework="html")
# …deploy manifest["files"] and the analytics snippet, then:
checklist = client.verify_site(client_id=manifest["clientId"])

# The weekly loop.
for item in client.get_next_steps(client_id=manifest["clientId"])["weekly"]:
    print(item["tool"], item["why"])
```

Arguments are keyword-only and snake_case (`client_id`, `crawl_id`); Python keywords get an underscore (`from_`). Tools newer than this package are reachable with `client.call("tool_name", {"camelCase": "input"})`. `client.list_tools(group="onboarding")` lists what your key may call, with schemas.

## Errors

```python
from seolyticize import RefusedError, RateLimitError

try:
    client.connect_search_console_service_account(client_id="client_…")
except RefusedError as error:
    print(error.code)        # "search_console_no_access" — branch on this
    print(error.next)        # what to do next
    print(error.request_id)  # quote it when asking for help
```

`ValidationError` (400), `AuthenticationError` (401), `PermissionError` (403), `NotFoundError` (404), `RefusedError` (422), `RateLimitError` (429), `ServerError` (5xx), `NetworkError` — all subclasses of `SeolyticizeError`. 429s are retried after `Retry-After`; server and network errors are retried only for read-only tools, since a write that failed may already have happened.

## On your site

```python
from seolyticize.site import analytics_tag, indexnow_key_response, notify_deploy, track_event

analytics_tag("SITE_KEY", exclude=["/account/*", "/verify"])  # the <script> for your <head>
body, headers = indexnow_key_response("KEY")                   # serve at /KEY.txt
notify_deploy("https://seolyticize.com/api/v1/hooks/deploy/dh_…")  # after each deploy
track_event("SITE_KEY", "https://example.com/pricing", name="Signup")  # server-side event
```

Docs: [seolyticize.com/docs/python-sdk](https://seolyticize.com/docs/python-sdk) · Agent quick start: [seolyticize.com/AGENTS.md](https://seolyticize.com/AGENTS.md)

The tool methods are generated from the same registry that runs the API. License: MIT.
