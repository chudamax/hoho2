import json
import os
import sys
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path
from urllib import request

HONEYPOT_ID = os.getenv("HOHO_HONEYPOT_ID", os.getenv("HOHO_PACK_ID", "unknown-pack"))
SESSION_ID = os.getenv("HOHO_SESSION_ID", "unknown-session")
AGENT_ID = os.getenv("HOHO_AGENT_ID", "unknown-agent")
ROOT = Path(os.getenv("HOHO_STORAGE_ROOT", "/artifacts"))
EVENTS_PATH = ROOT / HONEYPOT_ID / "index" / "events.jsonl"
ONLY_PROJECT = os.getenv("HOHO_FALCO_ONLY_PROJECT", "true").strip().lower() in {"1", "true", "yes", "on"}
PROJECT = os.getenv("HOHO_FALCO_PROJECT", "")
ONLY_SERVICES = {s for s in os.getenv("HOHO_FALCO_ONLY_SERVICES", "").split(",") if s}
ENFORCE_ENABLED = os.getenv("HOHO_FALCO_ENFORCE_ENABLED", "false").strip().lower() in {"1", "true", "yes", "on"}
ENFORCE_PRIORITIES = {x for x in os.getenv("HOHO_FALCO_ENFORCE_MATCH_PRIORITIES", "Critical,Error").split(",") if x}
ENFORCE_RULES = {x for x in os.getenv("HOHO_FALCO_ENFORCE_MATCH_RULES", "").split(",") if x}
ENFORCE_ACTION = os.getenv("HOHO_FALCO_ENFORCE_ACTION", "stop_container")
ENFORCE_COOLDOWN_SECONDS = int(os.getenv("HOHO_FALCO_ENFORCE_COOLDOWN_SECONDS", "60"))
DOCKER_SOCK = "/host/var/run/docker.sock"
_last_enforce = {}


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def append_event(event: dict) -> None:
    EVENTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    with EVENTS_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event) + "\n")


def docker_api(path: str, method: str = "GET"):
    opener = request.build_opener(request.ProxyHandler({}))
    opener.add_handler(request.HTTPHandler())
    url = f"http://localhost{path}"
    req = request.Request(url, method=method)
    req.add_header("Host", "docker")
    return opener.open(req, timeout=3)


def docker_request(path: str, method: str = "GET"):
    import http.client

    conn = http.client.HTTPConnection("localhost")
    conn.sock = __import__("socket").socket(__import__("socket").AF_UNIX, __import__("socket").SOCK_STREAM)
    conn.sock.connect(DOCKER_SOCK)
    conn.request(method, path)
    resp = conn.getresponse()
    data = resp.read()
    conn.close()
    return resp.status, data


def inspect_container(container_id: str) -> dict:
    status, body = docker_request(f"/containers/{container_id}/json")
    if status >= 400:
        return {}
    try:
        return json.loads(body.decode("utf-8"))
    except Exception:
        return {}


def stop_container(container_id: str) -> bool:
    status, _ = docker_request(f"/containers/{container_id}/stop?t=5", method="POST")
    return status < 400


def list_project_containers(project: str) -> list[str]:
    status, body = docker_request("/containers/json")
    if status >= 400:
        return []
    items = json.loads(body.decode("utf-8"))
    out = []
    for item in items:
        labels = item.get("Labels", {})
        if labels.get("com.docker.compose.project") == project:
            out.append(item.get("Id", ""))
    return [x for x in out if x]


def extract_container_id(alert: dict) -> str:
    fields = alert.get("output_fields", {}) or {}
    container_id = fields.get("container.id")
    if not container_id or container_id == "<NA>":
        return ""
    return str(container_id)


def should_keep(alert: dict):
    container_id = extract_container_id(alert)
    if not container_id:
        return False, "", ""
    inspect = inspect_container(container_id)
    labels = inspect.get("Config", {}).get("Labels", {}) if inspect else {}
    project = labels.get("com.docker.compose.project", "")
    service = labels.get("com.docker.compose.service", "")
    if ONLY_PROJECT and PROJECT and project != PROJECT:
        return False, project, service
    if ONLY_SERVICES and service not in ONLY_SERVICES:
        return False, project, service
    return True, project, service


def should_enforce(alert: dict) -> bool:
    if not ENFORCE_ENABLED:
        return False
    rule = str(alert.get("rule", ""))
    priority = str(alert.get("priority", ""))
    if ENFORCE_RULES and rule in ENFORCE_RULES:
        return True
    if priority in ENFORCE_PRIORITIES:
        return True
    return False


def maybe_enforce(alert: dict, project: str, service: str) -> dict | None:
    if not should_enforce(alert):
        return None
    container_id = extract_container_id(alert)
    if not container_id:
        return None

    key = (ENFORCE_ACTION, container_id, project)
    now = time.time()
    last = _last_enforce.get(key, 0)
    if now - last < ENFORCE_COOLDOWN_SECONDS:
        return None
    _last_enforce[key] = now

    result = {"ok": False, "targets": []}
    if ENFORCE_ACTION in {"stop_container", "stop_service"}:
        result["targets"] = [container_id]
        result["ok"] = stop_container(container_id)
    elif ENFORCE_ACTION == "stop_stack" and project:
        targets = list_project_containers(project)
        result["targets"] = targets
        result["ok"] = all(stop_container(cid) for cid in targets) if targets else False
    return result


def make_base_event(alert: dict) -> dict:
    rule = str(alert.get("rule", "unknown"))
    priority = str(alert.get("priority", "Notice"))
    tags = ["falco", f"priority:{priority}", f"rule:{rule}"] + [str(t) for t in (alert.get("tags") or [])]
    return {
        "schema_version": 2,
        "event_id": f"falco-{uuid.uuid4().hex}",
        "ts": now_iso(),
        "honeypot_id": HONEYPOT_ID,
        "session_id": SESSION_ID,
        "agent_id": AGENT_ID,
        "event_name": "falco.alert",
        "component": "sensor.falco",
        "proto": "runtime",
        "classification": {"verdict": "alert", "tags": tags, "indicators": [rule]},
        "decision": {"truncated": False, "oversized": False, "rate_limited": False, "dropped": False},
        "artifacts": [],
        "falco": {
            "time": alert.get("time"),
            "rule": rule,
            "priority": priority,
            "source": alert.get("source"),
            "output": alert.get("output"),
            "output_fields": alert.get("output_fields", {}),
            "tags": alert.get("tags", []),
        },
    }


def main() -> int:
    for raw in sys.stdin:
        line = raw.strip()
        if not line:
            continue
        try:
            alert = json.loads(line)
        except Exception:
            print(f"[falco-forwarder] failed to parse alert line: {line[:300]}", file=sys.stderr)
            continue

        keep, project, service = should_keep(alert)
        if not keep:
            continue

        ev = make_base_event(alert)
        # Stamp static context here (no Falco append_output needed)
        ev["falco"]["output_fields"] = ev["falco"].get("output_fields", {}) or {}
        ev["falco"]["output_fields"].update(
            {
                "honeypot_id": HONEYPOT_ID,
                "sensor": "falco",
            }
        )
        ev["classification"]["tags"].extend([f"compose_project:{project}", f"compose_service:{service}"])
        append_event(ev)

        enforce_result = maybe_enforce(alert, project=project, service=service)
        if enforce_result is not None:
            append_event(
                {
                    **ev,
                    "event_id": f"falco-enforce-{uuid.uuid4().hex}",
                    "event_name": "falco.enforcement",
                    "classification": {
                        "verdict": "enforcement",
                        "tags": ["falco", "enforcement", f"action:{ENFORCE_ACTION}"],
                        "indicators": ev["classification"]["indicators"],
                    },
                    "falco_enforcement": {
                        "action": ENFORCE_ACTION,
                        "ok": enforce_result.get("ok", False),
                        "targets": enforce_result.get("targets", []),
                    },
                }
            )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
