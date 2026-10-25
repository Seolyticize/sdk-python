# Seolyticize for Python

Every [Seolyticize](https://seolyticize.com) API tool (about 500 in 0.4.0) as a method, and on-site helpers for analytics, IndexNow and deploys. Standard library only, Python 3.9+.

```sh
pip install seolyticize
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

Paid research (any domain, the AI answer index, Maps, AI Mode beside rank) takes `max_cost_micros`. Quote the exact call first:

```python
args = {"clientId": client_id, "target": "rival.com/blog/", "change": "new"}
quote = client.estimate_cost(tool="get_ranked_keywords", arguments=args)
ranked = client.get_ranked_keywords(
    client_id=client_id, target="rival.com/blog/", change="new",
    max_cost_micros=quote["estimatedMaxMicros"],
)

# Free reads over stored data:
pages = client.get_landing_pages(client_id=client_id, tracker_id=tracker_id)
grid = client.get_local_visibility(client_id=client_id, location_id=location_id, term="emergency plumber")
redirects = client.plan_redirect_map(client_id=client_id, old_crawl_id=old_crawl_id, format_="csv")
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

### Server-side collection

Reports page views from the server — above all the AI assistants (ChatGPT-User, Claude-User, Perplexity-User) that read pages without running the browser tag. Needs the server key from `issue_server_collect_key`; keep it in the environment.

```python
import os
from seolyticize.collect import ASGICollector, Collector, WSGICollector, django_middleware

collector = Collector("SITE_KEY", os.environ["SEOLYTICIZE_SERVER_KEY"],
                      exclude=["/admin/*", "/api/*"],
                      only="agents")  # with the browser tag installed too; "all" without it

app.wsgi_app = WSGICollector(app.wsgi_app, collector)      # Flask
app = ASGICollector(app, collector)                         # FastAPI / Starlette
SeolyticizeMiddleware = django_middleware(collector)        # Django: add to MIDDLEWARE
```

Only the path and `utm_*` parameters (change with `allow_params`), the referrer's origin, the visitor's address, user agent and country are sent; Seolyticize hashes the address and user agent under a daily salt and stores neither. Bots are dropped before anything is sent. Reports go out on a background thread and never raise.

To credit orders to the visit they came from, send a reference from the checkout — the tag's `seolyticize('event', 'Checkout', {ref: cartId})`, or `collector.track(checkout_url, name="Checkout", props={"ref": cart_id}, user_agent=…, ip=…)` with the visitor's own agent and address so it joins their visit — and put the same value in the order's metadata as `seolyticize_ref` (Stripe metadata, a Shopify cart attribute, Paddle `custom_data`).

A conversion that happens after the visit — a payment confirmed by webhook, a trial that converts next week — is credited to the visit by its token. Ask for it while the visitor is there and keep it on your server with the account (never in a cookie or the page); the token lasts 35 days:

```python
visit = collector.track_for_visit(request.url, "Signup", user_agent=ua, ip=ip)  # returns the token
account.seolyticize_visit = visit
# ...days later, from the payment webhook:
collector.track_later(account.seolyticize_visit, "Top-up", props={"value": 25})
```

Docs: [seolyticize.com/docs/python-sdk](https://seolyticize.com/docs/python-sdk) · Agent quick start: [seolyticize.com/AGENTS.md](https://seolyticize.com/AGENTS.md)

The tool methods are generated from the same registry that runs the API. License: MIT.
