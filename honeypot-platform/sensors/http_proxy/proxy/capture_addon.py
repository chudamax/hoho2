import os
import sys
from pathlib import Path

from hoho_core.model.event import build_base_event
from hoho_core.storage.fs import FilesystemArtifactStore
from hoho_core.utils.redact import redact_headers

HONEYPOT_ID = os.getenv("HOHO_HONEYPOT_ID", os.getenv("HOHO_PACK_ID", "unknown-pack"))
SESSION_ID = os.getenv("HOHO_SESSION_ID", "unknown-session")
AGENT_ID = os.getenv("HOHO_AGENT_ID", "unknown-agent")
ROOT = Path(os.getenv("HOHO_STORAGE_ROOT", "/artifacts"))
STORE = FilesystemArtifactStore(str(ROOT), HONEYPOT_ID)


def _log_error(message: str):
    print(f"capture_addon error: {message}", file=sys.stderr)


def _peername(flow):
    client_conn = getattr(flow, "client_conn", None)
    if not client_conn:
        return None
    peername = getattr(client_conn, "peername", None)
    if isinstance(peername, tuple) and len(peername) >= 2:
        return peername
    return None


def _forwarded_for_values(req) -> list[str]:
    header_val = req.headers.get("X-Forwarded-For", "")
    if not header_val:
        return []
    return [v.strip() for v in header_val.split(",") if v.strip()]


def response(flow):
    try:
        req = flow.request
        resp = flow.response
        body = req.raw_content or b""

        peername = _peername(flow)
        src_ip = peername[0] if peername else None
        src_port = peername[1] if peername else None

        ev = build_base_event(
            honeypot_id=HONEYPOT_ID,
            component="sensor.http_proxy",
            proto="http",
            session_id=SESSION_ID,
            agent_id=AGENT_ID,
            event_name="http.request",
        )
        ev["event_id"] = flow.id
        ev["src"] = {
            "ip": src_ip,
            "port": src_port,
            "forwarded_for": _forwarded_for_values(req),
            "user_agent": req.headers.get("User-Agent"),
        }
        ev["http"] = {"host": req.headers.get("Host")}
        ev["request"] = {
            "method": req.method,
            "path": req.path,
            "query": dict(req.query),
            "headers_redacted": redact_headers(dict(req.headers.items(multi=True))),
            "content_type": req.headers.get("Content-Type"),
            "content_length": len(body),
        }
        ev["response"] = {
            "status_code": resp.status_code if resp else None,
            "bytes_sent": len(resp.raw_content or b"") if resp else 0,
            "profile": None,
        }
        if body:
            blob = STORE.put_blob(body, mime=req.headers.get("Content-Type", "application/octet-stream"))
            ev["artifacts"] = [{"kind": "request_body", **blob, "meta": {}}]
        STORE.append_event(HONEYPOT_ID, ev)
    except Exception as exc:  # noqa: BLE001
        _log_error(str(exc))
