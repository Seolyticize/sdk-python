import asyncio
import json
import unittest

from seolyticize.collect import (
    ASGICollector,
    Collector,
    WSGICollector,
    address_from,
    classify_agent,
    is_page_request,
    strip_query,
)

CHROME = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
)


class Recorder:
    def __init__(self, status=202):
        self.calls = []
        self.status = status

    def __call__(self, url, data, headers, timeout):
        self.calls.append((url, json.loads(data), headers))
        return self.status


def collector(sent, **options):
    return Collector("site_key_0123456789", "slyc_secret", background=False, send=sent, **options)


class ClassifyTests(unittest.TestCase):
    def test_agents_bots_and_people(self):
        self.assertEqual(classify_agent("Mozilla/5.0 (compatible; ChatGPT-User/1.0; +https://openai.com/bot)"), "agent")
        self.assertEqual(classify_agent(CHROME, '"https://chatgpt.com"'), "agent")
        self.assertEqual(classify_agent("Mozilla/5.0 (compatible; Googlebot/2.1)"), "bot")
        self.assertEqual(classify_agent("python-requests/2.32"), "bot")
        self.assertEqual(classify_agent(CHROME), "person")

    def test_strip_query_keeps_only_campaign_tags(self):
        self.assertEqual(
            strip_query("https://shop.example/p?utm_source=news&email=a%40b.com#top"),
            "https://shop.example/p?utm_source=news",
        )

    def test_page_requests(self):
        self.assertTrue(is_page_request("GET", {"accept": "text/html"}))
        self.assertFalse(is_page_request("POST", {"accept": "text/html"}))
        self.assertFalse(is_page_request("GET", {"accept": "text/html", "sec-purpose": "prefetch"}))
        self.assertFalse(is_page_request("GET", {"sec-fetch-dest": "image"}))

    def test_address_from_proxy_headers(self):
        self.assertEqual(address_from({"x-forwarded-for": "203.0.113.2, 10.0.0.1"}), "203.0.113.2")
        self.assertIsNone(address_from({}))


class TrackTests(unittest.TestCase):
    def test_sends_the_visitor_with_the_server_key(self):
        sent = Recorder()
        collector(sent).track(
            "https://shop.example/pricing?utm_campaign=autumn&session=abc",
            referrer="https://www.google.com/search?q=private",
            user_agent=CHROME,
            ip="198.51.100.7",
            country="GB",
        )
        url, body, headers = sent.calls[0]
        self.assertEqual(url, "https://seolyticize.com/api/collect")
        self.assertEqual(headers["authorization"], "Bearer slyc_secret")
        self.assertEqual(
            body,
            {
                "k": "site_key_0123456789",
                "n": "pageview",
                "u": "https://shop.example/pricing?utm_campaign=autumn",
                "r": "https://www.google.com/",
                "ua": CHROME,
                "ip": "198.51.100.7",
                "c": "GB",
            },
        )

    def test_drops_bots_excluded_paths_and_people_in_agents_mode(self):
        sent = Recorder()
        c = collector(sent, exclude=["/admin/*"])
        c.track("https://shop.example/", user_agent="curl/8.4.0")
        c.track("https://shop.example/admin/users", user_agent=CHROME)
        self.assertEqual(sent.calls, [])
        agents = collector(sent, only="agents")
        agents.track("https://shop.example/", user_agent=CHROME)
        self.assertEqual(sent.calls, [])
        agents.track("https://shop.example/", user_agent="Mozilla/5.0 (compatible; Claude-User/1.0)")
        self.assertEqual(len(sent.calls), 1)

    def test_never_raises_and_reports_a_refused_key(self):
        errors = []
        c = Collector("site_key_0123456789", "slyc_wrong", background=False, send=Recorder(401), on_error=errors.append)
        c.track("https://shop.example/", user_agent=CHROME)
        self.assertEqual(len(errors), 1)


class MiddlewareTests(unittest.TestCase):
    def environ(self, path="/found"):
        return {
            "REQUEST_METHOD": "GET",
            "PATH_INFO": path,
            "QUERY_STRING": "",
            "wsgi.url_scheme": "https",
            "HTTP_HOST": "shop.example",
            "HTTP_ACCEPT": "text/html",
            "HTTP_USER_AGENT": CHROME,
            "REMOTE_ADDR": "203.0.113.5",
        }

    def test_wsgi_reports_successful_pages_only(self):
        sent = Recorder()

        def app(environ, start_response):
            status = "200 OK" if environ["PATH_INFO"] == "/found" else "404 Not Found"
            start_response(status, [("content-type", "text/html")])
            return [b"ok"]

        wrapped = WSGICollector(app, collector(sent))
        wrapped(self.environ("/missing"), lambda status, headers: None)
        wrapped(self.environ("/found"), lambda status, headers: None)
        self.assertEqual(len(sent.calls), 1)
        self.assertEqual(sent.calls[0][1]["u"], "https://shop.example/found")
        self.assertEqual(sent.calls[0][1]["ip"], "203.0.113.5")

    def test_asgi_reports_from_the_scope(self):
        sent = Recorder()

        async def app(scope, receive, send):
            await send({"type": "http.response.start", "status": 200, "headers": []})
            await send({"type": "http.response.body", "body": b"ok"})

        async def noop(message):
            return None

        scope = {
            "type": "http",
            "method": "GET",
            "path": "/docs",
            "query_string": b"utm_source=x&secret=1",
            "scheme": "https",
            "client": ("203.0.113.8", 5000),
            "headers": [(b"host", b"shop.example"), (b"accept", b"text/html"), (b"user-agent", CHROME.encode())],
        }
        asyncio.run(ASGICollector(app, collector(sent))(scope, None, noop))
        self.assertEqual(sent.calls[0][1]["u"], "https://shop.example/docs?utm_source=x")
        self.assertEqual(sent.calls[0][1]["ip"], "203.0.113.8")


class Answering:
    """A fake transport that answers with a status and a body."""

    def __init__(self, status=202, body=b""):
        self.calls = []
        self.status = status
        self.body = body

    def __call__(self, url, data, headers, timeout):
        self.calls.append((url, json.loads(data), headers))
        return self.status, self.body


class VisitTokenTests(unittest.TestCase):
    def test_an_event_for_the_visitor_returns_the_token(self):
        answer = Answering(body=json.dumps({"visit": "v1.abc.def"}).encode())
        c = Collector("site_key_0123456789", "slyc_secret", background=False, request=answer, only="agents")
        token = c.track_for_visit(
            "https://shop.example/signup", "Signup", user_agent=CHROME, ip="198.51.100.7"
        )
        self.assertEqual(token, "v1.abc.def")
        self.assertEqual(answer.calls[0][1]["n"], "Signup")
        self.assertEqual(answer.calls[0][1]["ip"], "198.51.100.7")
        self.assertEqual(answer.calls[0][2]["authorization"], "Bearer slyc_secret")

    def test_no_token_for_a_bot_or_when_none_was_issued(self):
        answer = Answering()
        c = Collector("site_key_0123456789", "slyc_secret", background=False, request=answer)
        self.assertIsNone(c.track_for_visit("https://shop.example/", "Signup", user_agent="curl/8"))
        self.assertEqual(answer.calls, [])
        self.assertIsNone(c.track_for_visit("https://shop.example/", "Signup", user_agent=CHROME))

    def test_a_later_event_carries_the_token_and_no_visitor(self):
        answer = Answering()
        c = Collector("site_key_0123456789", "slyc_secret", background=False, request=answer)
        self.assertTrue(c.track_later("v1.abc.def", "Top-up", props={"value": 25}))
        self.assertEqual(
            answer.calls[0][1],
            {"k": "site_key_0123456789", "n": "Top-up", "visit": "v1.abc.def", "p": {"value": 25}},
        )

    def test_an_expired_token_is_reported_not_raised(self):
        errors = []
        c = Collector(
            "site_key_0123456789",
            "slyc_secret",
            background=False,
            request=Answering(status=410),
            on_error=errors.append,
        )
        self.assertFalse(c.track_later("v1.old.token", "Top-up"))
        self.assertEqual(len(errors), 1)


if __name__ == "__main__":
    unittest.main()
