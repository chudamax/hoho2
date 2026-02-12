import uuid
from hoho_core.utils.time import utc_iso


def build_base_event(
    honeypot_id: str,
    component: str,
    proto: str,
    session_id: str,
    agent_id: str,
    event_name: str,
) -> dict:
    return {
        "schema_version": 2,
        "event_id": str(uuid.uuid4()),
        "ts": utc_iso(),
        "honeypot_id": honeypot_id,
        "session_id": session_id,
        "agent_id": agent_id,
        "event_name": event_name,
        "component": component,
        "src": {"ip": None, "port": None, "forwarded_for": [], "user_agent": None},
        "proto": proto,
        "request": {},
        "response": {"status_code": None, "bytes_sent": 0, "profile": None},
        "classification": {"verdict": "unknown", "tags": [], "indicators": []},
        "decision": {"truncated": False, "oversized": False, "rate_limited": False, "dropped": False},
        "artifacts": [],
    }
