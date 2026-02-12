import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs
from hoho_core.dsl.engine import evaluate_rules
from hoho_core.model.event import build_base_event
from hoho_core.storage.fs import FilesystemArtifactStore
from hoho_core.utils.redact import redact_headers


class LowInteractionHandler(BaseHTTPRequestHandler):
    pack = None
    store = None

    def _handle(self):
        length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(length) if length else b""
        parsed = urlparse(self.path)
        req = {
            "method": self.command,
            "path": parsed.path,
            "query": {k: v[0] for k, v in parse_qs(parsed.query).items()},
            "headers": {k: v for k, v in self.headers.items()},
            "body": body,
            "content_type": self.headers.get("Content-Type", ""),
        }
        event = build_base_event(
            honeypot_id=self.pack["metadata"]["id"],
            component="runtime.http",
            proto="http",
            session_id=os.getenv("HOHO_SESSION_ID", "unknown-session"),
            agent_id=os.getenv("HOHO_AGENT_ID", "unknown-agent"),
            event_name="http.request",
        )
        event["src"]["ip"] = self.client_address[0]
        event["src"]["port"] = self.client_address[1]
        event["src"]["user_agent"] = self.headers.get("User-Agent")
        event["request"] = {
            "method": self.command,
            "path": parsed.path,
            "query": req["query"],
            "headers_redacted": redact_headers(req["headers"], self.pack.get("telemetry", {}).get("redact_headers")),
            "content_type": req["content_type"],
            "content_length": len(body),
        }
        state = evaluate_rules(self.pack.get("behaviors", []), req, self.store, event)
        resp = state.get("respond") or {"status": 404, "headers": {}, "body": "not found"}
        self.send_response(resp.get("status", 200))
        for k, v in resp.get("headers", {}).items():
            self.send_header(k, v)
        self.end_headers()
        body_out = resp.get("body", "").encode()
        self.wfile.write(body_out)
        event["response"]["status_code"] = resp.get("status", 200)
        event["response"]["bytes_sent"] = len(body_out)
        self.store.append_event(self.pack["metadata"]["id"], event)

    do_GET = _handle
    do_POST = _handle
    do_PUT = _handle
    do_DELETE = _handle


def run_low_http(pack: dict) -> None:
    listen = (pack.get("listen") or [{"host": "0.0.0.0", "port": 8080}])[0]
    store = FilesystemArtifactStore(pack.get("storage", {}).get("root", "./run/artifacts"), pack["metadata"]["id"])
    handler = type("BoundHandler", (LowInteractionHandler,), {"pack": pack, "store": store})
    server = ThreadingHTTPServer((listen.get("host", "0.0.0.0"), int(listen.get("port", 8080))), handler)
    print(json.dumps({"status": "listening", "host": listen.get("host", "0.0.0.0"), "port": listen.get("port", 8080)}))
    server.serve_forever()
