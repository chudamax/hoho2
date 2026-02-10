import uuid
from hoho_core.utils.time import utc_iso


def build_base_event(pack_id: str, interaction: str, component: str, proto: str) -> dict:
    return {
        "schema_version": 1,
        "event_id": str(uuid.uuid4()),
        "ts": utc_iso(),
        "pack_id": pack_id,
        "interaction": interaction,
        "component": component,
        "src": {"ip": None, "port": None, "forwarded_for": [], "user_agent": None},
        "proto": proto,
        "request": {},
        "response": {"status_code": None, "bytes_sent": 0, "profile": None},
        "classification": {"verdict": "unknown", "tags": [], "indicators": []},
        "decision": {"truncated": False, "oversized": False, "rate_limited": False, "dropped": False},
        "artifacts": [],
    }
