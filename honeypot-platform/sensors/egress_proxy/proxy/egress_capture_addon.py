import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

PACK_ID = os.getenv("HOHO_PACK_ID", "unknown-pack")
ROOT = Path(os.getenv("HOHO_STORAGE_ROOT", "/artifacts"))
CAPTURE_ENABLED = os.getenv("PROXY_CAPTURE_ENABLED", "true").lower() in {"1", "true", "yes", "on"}
CAPTURE_BODIES = os.getenv("PROXY_CAPTURE_BODIES", "*")
CAPTURE_MAX_BYTES = int(os.getenv("PROXY_CAPTURE_MAX_BYTES", "52428800"))
CAPTURE_STORE_OK_ONLY = os.getenv("PROXY_CAPTURE_STORE_OK_ONLY", "true").lower() in {"1", "true", "yes", "on"}
CAPTURE_MIN_BYTES = int(os.getenv("PROXY_CAPTURE_MIN_BYTES", "1"))
REDACT_HEADERS = {h.strip().lower() for h in os.getenv("PROXY_REDACT_HEADERS", "Authorization,Cookie").split(",") if h.strip()}


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _events_path() -> Path:
    return ROOT / PACK_ID / "index" / "events.jsonl"


def _append_event(ev: dict) -> None:
    path = _events_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(ev) + "\n")


def _redact(headers) -> dict:
    out = {}
    for k, v in headers.items(multi=True):
        out[k] = "<redacted>" if k.lower() in REDACT_HEADERS else v
    return out


def _guess_filename(flow_id: str, url: str, headers, digest: str) -> str:
    content_disp = headers.get("Content-Disposition", "")
    marker = "filename="
    if marker in content_disp:
        candidate = content_disp.split(marker, 1)[1].strip().strip('"\'')
        if candidate:
            return candidate

    path = urlparse(url).path
    tail = Path(path).name
    if tail:
        return tail
    return f"{digest[:32] if digest else flow_id}.bin"


def response(flow):
    req = flow.request
    resp = flow.response
    event_id = flow.id

    body = (resp.raw_content or b"") if resp else b""
    total_bytes = len(body)
    should_store = CAPTURE_ENABLED and CAPTURE_BODIES == "*"
    if CAPTURE_STORE_OK_ONLY and resp is not None:
        should_store = should_store and (200 <= resp.status_code <= 399)
    should_store = should_store and total_bytes >= CAPTURE_MIN_BYTES

    artifacts = []
    if should_store:
        stored = body[:CAPTURE_MAX_BYTES]
        digest = hashlib.sha256(stored).hexdigest()
        truncated = len(stored) < total_bytes

        blob_path = ROOT / PACK_ID / "blobs" / digest[:2] / digest
        blob_path.parent.mkdir(parents=True, exist_ok=True)
        if not blob_path.exists():
            blob_path.write_bytes(stored)

        filename = _guess_filename(event_id, req.pretty_url, resp.headers if resp else {}, digest)
        obj_path = ROOT / PACK_ID / "objects" / event_id / "egress.response" / filename
        obj_path.parent.mkdir(parents=True, exist_ok=True)
        if not obj_path.exists():
            obj_path.symlink_to(blob_path)

        artifacts.append(
            {
                "kind": "egress.response_body",
                "sha256": digest,
                "bytes_captured": len(stored),
                "bytes_total": total_bytes,
                "truncated": truncated,
                "filename_guess": filename,
                "url": req.pretty_url,
                "storage_ref": f"blobs/{digest[:2]}/{digest}",
            }
        )

    ev = {
        "schema_version": 1,
        "event_id": event_id,
        "ts": _now(),
        "pack_id": PACK_ID,
        "interaction": "high",
        "kind": "sensor.egress_proxy.http",
        "component": "sensor.egress_proxy",
        "request": {
            "method": req.method,
            "url": req.pretty_url,
            "headers_redacted": _redact(req.headers),
        },
        "response": {
            "status_code": resp.status_code if resp else None,
            "headers_redacted": _redact(resp.headers) if resp else {},
            "bytes": total_bytes,
        },
        "artifacts": artifacts,
    }
    _append_event(ev)
