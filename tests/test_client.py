import json
import threading
import unittest
from http.server import BaseHTTPRequestHandler, HTTPServer

from seolyticize import RefusedError, Seolyticize, ServerError
from seolyticize.site import analytics_tag, indexnow_key_response, notify_deploy


class Fake:
    """A local stand-in for the API: records requests, answers from a script."""

    def __init__(self):
        self.requests = []
        self.answers = []
        fake = self

        class Handler(BaseHTTPRequestHandler):
            def log_message(self, *args):
                pass

            def _answer(self):
                length = int(self.headers.get("content-length") or 0)
                body = json.loads(self.rfile.read(length) or b"null") if length else None
                fake.requests.append((self.command, self.path, dict(self.headers), body))
                status, payload, headers = fake.answers.pop(0) if fake.answers else (200, {"data": {}}, {})
                self.send_response(status)
                for key, value in headers.items():
                    self.send_header(key, value)
                self.send_header("content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(payload).encode())

            do_GET = do_POST = _answer

        self.server = HTTPServer(("127.0.0.1", 0), Handler)
        threading.Thread(target=self.server.serve_forever, daemon=True).start()
        self.url = f"http://127.0.0.1:{self.server.server_port}"

    def client(self):
        return Seolyticize("sk_seo_test", base_url=self.url, sleep=lambda _s: None)


class ClientTests(unittest.TestCase):
    def setUp(self):
        self.fake = Fake()

    def tearDown(self):
        self.fake.server.shutdown()

    def test_typed_method_sends_camel_case_and_drops_unset(self):
        self.fake.answers.append((200, {"data": {"pagesCrawled": 10}}, {}))
        result = self.fake.client().get_audit_summary(client_id="client_1")
        self.assertEqual(result, {"pagesCrawled": 10})
        method, path, headers, body = self.fake.requests[0]
        self.assertEqual((method, path), ("POST", "/api/v1/tools/get_audit_summary"))
        self.assertEqual(body, {"clientId": "client_1"})
        self.assertEqual(headers["Authorization"], "Bearer sk_seo_test")

    def test_reserved_names_get_an_underscore(self):
        self.fake.client().export_search_console_data(client_id="c", from_="2026-10-01", to="2026-10-20")
        self.assertEqual(self.fake.requests[0][3], {"clientId": "c", "from": "2026-10-01", "to": "2026-10-20"})

    def test_refusal_carries_code_next_and_request_id(self):
        self.fake.answers.append((422, {"error": "Not yet.", "code": "search_console_no_access", "next": "verify_site", "requestId": "req_1"}, {}))
        with self.assertRaises(RefusedError) as caught:
            self.fake.client().connect_search_console_service_account(client_id="c")
        error = caught.exception
        self.assertEqual((error.status, error.code, error.next, error.request_id), (422, "search_console_no_access", "verify_site", "req_1"))

    def test_a_4xx_refusal_as_data_reads_like_the_old_200(self):
        declined = {"ok": False, "refused": "not-connected", "data": {"refused": "not-connected"}}
        self.fake.answers.append((409, declined, {}))
        self.assertEqual(self.fake.client().get_next_steps(client_id="c"), {"refused": "not-connected"})
        self.assertEqual(len(self.fake.requests), 1)

    def test_rate_limit_is_retried(self):
        self.fake.answers.append((429, {"error": "Slow down", "code": "rate_limited"}, {"Retry-After": "1"}))
        self.fake.answers.append((200, {"data": {"ok": True}}, {}))
        self.assertEqual(self.fake.client().get_next_steps(client_id="c"), {"ok": True})
        self.assertEqual(len(self.fake.requests), 2)

    def test_a_slow_call_is_collected_under_its_key(self):
        queued = {"ok": True, "outcome": "queued", "idempotencyKey": "async_k1", "pollAfterSeconds": 5}
        self.fake.answers.append((202, queued, {}))
        self.fake.answers.append((409, {"error": "Still running", "code": "in_progress"}, {}))
        self.fake.answers.append((200, {"data": {"done": True}}, {}))
        self.assertEqual(self.fake.client().call("start_crawl", {"clientId": "c"}), {"done": True})
        self.assertEqual(len(self.fake.requests), 3)
        self.assertNotIn("Idempotency-Key", self.fake.requests[0][2])
        self.assertEqual(self.fake.requests[2][2].get("Idempotency-Key"), "async_k1")
        self.assertEqual(self.fake.requests[2][3], {"clientId": "c"})

    def test_a_write_is_not_repeated_after_a_server_error(self):
        self.fake.answers.append((500, {"error": "Failed", "code": "internal_error"}, {}))
        with self.assertRaises(ServerError):
            self.fake.client().create_client(name="A", domain="a.com")
        self.assertEqual(len(self.fake.requests), 1)

    def test_list_tools_by_group(self):
        self.fake.client().list_tools(group="onboarding")
        self.assertEqual(self.fake.requests[0][:2], ("GET", "/api/v1/tools?group=onboarding"))


class SiteTests(unittest.TestCase):
    def test_analytics_tag(self):
        tag = analytics_tag("abc123", exclude=["/app/*", "/verify"], track=["outbound"])
        for part in ('data-site="abc123"', 'data-exclude="/app/*,/verify"', 'data-track="outbound"', 'src="https://seolyticize.com/a.js?v=2"', " defer "):
            self.assertIn(part, tag)
        self.assertNotIn('"><x', analytics_tag('"><x'))

    def test_indexnow_key_response(self):
        body, headers = indexnow_key_response("k123")
        self.assertEqual(body, "k123")
        self.assertTrue(headers["Content-Type"].startswith("text/plain"))

    def test_notify_deploy(self):
        fake = Fake()
        try:
            fake.answers.append((200, {"submitted": 1}, {}))
            self.assertEqual(notify_deploy(fake.url, ["https://a.com/x"]), {"submitted": 1})
            self.assertEqual(fake.requests[0][3], {"urls": ["https://a.com/x"]})
        finally:
            fake.server.shutdown()


if __name__ == "__main__":
    unittest.main()
