import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

PACK_ID = os.getenv("HOHO_PACK_ID", "unknown-pack")
ROOT = Path(os.getenv("HOHO_STORAGE_ROOT", "/artifacts"))


def _now():
    return datetime.now(timezone.utc).isoformat()


def _append_event(ev: dict):
    p = ROOT / PACK_ID / "index" / "events.jsonl"
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("a", encoding="utf-8") as f:
        f.write(json.dumps(ev) + "\n")


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
        digest = hashlib.sha256(body).hexdigest() if body else None

        if body:
            bp = ROOT / PACK_ID / "blobs" / digest[:2] / digest
            bp.parent.mkdir(parents=True, exist_ok=True)
            if not bp.exists():
                bp.write_bytes(body)

        peername = _peername(flow)
        src_ip = peername[0] if peername else None
        src_port = peername[1] if peername else None

        ev = {
            "schema_version": 1,
            "event_id": flow.id,
            "ts": _now(),
            "pack_id": PACK_ID,
            "interaction": "high",
            "component": "sensor.http_proxy",
            "src": {
                "ip": src_ip,
                "port": src_port,
                "forwarded_for": _forwarded_for_values(req),
                "user_agent": req.headers.get("User-Agent"),
            },
            "proto": "http",
            "http": {"host": req.headers.get("Host")},
            "request": {
                "method": req.method,
                "path": req.path,
                "query": dict(req.query),
                "headers_redacted": {
                    k: ("<redacted>" if k.lower() in ["authorization", "cookie"] else v)
                    for k, v in req.headers.items()
                },
                "content_type": req.headers.get("Content-Type"),
                "content_length": len(body),
            },
            "response": {
                "status_code": resp.status_code if resp else None,
                "bytes_sent": len(resp.raw_content or b"") if resp else 0,
                "profile": None,
            },
            "classification": {"verdict": "unknown", "tags": [], "indicators": []},
            "decision": {
                "truncated": False,
                "oversized": False,
                "rate_limited": False,
                "dropped": False,
            },
            "artifacts": (
                [
                    {
                        "kind": "request_body",
                        "sha256": digest,
                        "size": len(body),
                        "mime": req.headers.get("Content-Type", "application/octet-stream"),
                        "storage_ref": f"blobs/{digest[:2]}/{digest}",
                        "meta": {},
                    }
                ]
                if body
                else []
            ),
        }
        _append_event(ev)
    except Exception as exc:  # noqa: BLE001
        _log_error(str(exc))
