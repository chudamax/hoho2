import json
import os
from pathlib import Path
from datetime import datetime, timezone
import hashlib

PACK_ID = os.getenv("HOHO_PACK_ID", "unknown-pack")
ROOT = Path(os.getenv("HOHO_STORAGE_ROOT", "/artifacts"))


def _now():
    return datetime.now(timezone.utc).isoformat()


def _append_event(ev: dict):
    p = ROOT / PACK_ID / "index" / "events.jsonl"
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("a", encoding="utf-8") as f:
        f.write(json.dumps(ev) + "\n")


def response(flow):
    req = flow.request
    resp = flow.response
    body = req.raw_content or b""
    digest = hashlib.sha256(body).hexdigest() if body else None
    if body:
        bp = ROOT / PACK_ID / "blobs" / digest[:2] / digest
        bp.parent.mkdir(parents=True, exist_ok=True)
        if not bp.exists():
            bp.write_bytes(body)
    ev = {
        "schema_version": 1,
        "event_id": flow.id,
        "ts": _now(),
        "pack_id": PACK_ID,
        "interaction": "high",
        "component": "sensor.http_proxy",
        "src": {"ip": req.remote_conn.address[0] if req.remote_conn.address else None, "port": req.remote_conn.address[1] if req.remote_conn.address else None, "forwarded_for": [], "user_agent": req.headers.get("User-Agent")},
        "proto": "http",
        "request": {"method": req.method, "path": req.path, "query": dict(req.query), "headers_redacted": {k: ("<redacted>" if k.lower() in ["authorization","cookie"] else v) for k,v in req.headers.items()}, "content_type": req.headers.get("Content-Type"), "content_length": len(body)},
        "response": {"status_code": resp.status_code if resp else None, "bytes_sent": len(resp.raw_content or b"") if resp else 0, "profile": None},
        "classification": {"verdict": "unknown", "tags": [], "indicators": []},
        "decision": {"truncated": False, "oversized": False, "rate_limited": False, "dropped": False},
        "artifacts": ([{"kind": "request_body", "sha256": digest, "size": len(body), "mime": req.headers.get("Content-Type", "application/octet-stream"), "storage_ref": f"blobs/{digest[:2]}/{digest}", "meta": {}}] if body else []),
    }
    _append_event(ev)
