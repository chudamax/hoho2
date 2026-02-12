import os
from pathlib import Path
from urllib.parse import urlparse

from hoho_core.model.event import build_base_event
from hoho_core.storage.fs import FilesystemArtifactStore
from hoho_core.utils.redact import redact_headers

HONEYPOT_ID = os.getenv("HOHO_HONEYPOT_ID", os.getenv("HOHO_PACK_ID", "unknown-pack"))
SESSION_ID = os.getenv("HOHO_SESSION_ID", "unknown-session")
AGENT_ID = os.getenv("HOHO_AGENT_ID", "unknown-agent")
ROOT = Path(os.getenv("HOHO_STORAGE_ROOT", "/artifacts"))
STORE = FilesystemArtifactStore(str(ROOT), HONEYPOT_ID)
CAPTURE_ENABLED = os.getenv("PROXY_CAPTURE_ENABLED", "true").lower() in {"1", "true", "yes", "on"}
CAPTURE_BODIES = os.getenv("PROXY_CAPTURE_BODIES", "*")
CAPTURE_MAX_BYTES = int(os.getenv("PROXY_CAPTURE_MAX_BYTES", "52428800"))
CAPTURE_STORE_OK_ONLY = os.getenv("PROXY_CAPTURE_STORE_OK_ONLY", "true").lower() in {"1", "true", "yes", "on"}
CAPTURE_MIN_BYTES = int(os.getenv("PROXY_CAPTURE_MIN_BYTES", "1"))
REDACT_HEADERS = [h.strip() for h in os.getenv("PROXY_REDACT_HEADERS", "Authorization,Cookie").split(",") if h.strip()]


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

    ev = build_base_event(
        honeypot_id=HONEYPOT_ID,
        component="sensor.egress_proxy",
        proto="http",
        session_id=SESSION_ID,
        agent_id=AGENT_ID,
        event_name="egress.response",
    )
    ev["event_id"] = event_id
    ev["request"] = {
        "method": req.method,
        "url": req.pretty_url,
        "headers_redacted": redact_headers(dict(req.headers.items(multi=True)), REDACT_HEADERS),
    }
    ev["response"] = {
        "status_code": resp.status_code if resp else None,
        "headers_redacted": redact_headers(dict(resp.headers.items(multi=True)), REDACT_HEADERS) if resp else {},
        "bytes": total_bytes,
    }
    ev["egress"] = {"capture_enabled": CAPTURE_ENABLED}

    if should_store:
        stored = body[:CAPTURE_MAX_BYTES]
        blob = STORE.put_blob(stored)
        truncated = len(stored) < total_bytes
        filename = _guess_filename(event_id, req.pretty_url, resp.headers if resp else {}, blob["sha256"])
        obj_path = ROOT / HONEYPOT_ID / "objects" / event_id / "egress.response" / filename
        blob_path = ROOT / HONEYPOT_ID / blob["storage_ref"]
        obj_path.parent.mkdir(parents=True, exist_ok=True)
        if not obj_path.exists():
            obj_path.symlink_to(blob_path)
        ev["artifacts"] = [
            {
                "kind": "egress.response_body",
                **blob,
                "meta": {
                    "bytes_total": total_bytes,
                    "truncated": truncated,
                    "filename_guess": filename,
                    "url": req.pretty_url,
                },
            }
        ]
        ev["decision"]["truncated"] = truncated

    STORE.append_event(HONEYPOT_ID, ev)
