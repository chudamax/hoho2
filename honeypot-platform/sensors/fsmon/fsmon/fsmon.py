import fnmatch
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

PACK_ID = os.getenv("HOHO_PACK_ID", "unknown-pack")
ROOT = Path(os.getenv("HOHO_STORAGE_ROOT", "/artifacts"))
WATCH_DIRS = os.getenv("FSMON_WATCH", "/watched").split(",")
MAX_BYTES = int(os.getenv("FSMON_MAX_BYTES", "262144"))
ALLOW = [x for x in os.getenv("FSMON_ALLOW", "*").split(",") if x]
DENY = [x for x in os.getenv("FSMON_DENY", "").split(",") if x]


def now():
    return datetime.now(timezone.utc).isoformat()


def allow_path(path: str) -> bool:
    if any(fnmatch.fnmatch(path, pat) for pat in DENY):
        return False
    return any(fnmatch.fnmatch(path, pat) for pat in ALLOW)


def append_event(event):
    p = ROOT / PACK_ID / "index" / "events.jsonl"
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event) + "\n")


class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        self._process(event)

    def on_created(self, event):
        self._process(event)

    def _process(self, event):
        if event.is_directory or not allow_path(event.src_path):
            return
        path = Path(event.src_path)
        try:
            data = path.read_bytes()[:MAX_BYTES]
        except Exception:
            return
        digest = hashlib.sha256(data).hexdigest()
        bp = ROOT / PACK_ID / "blobs" / digest[:2] / digest
        bp.parent.mkdir(parents=True, exist_ok=True)
        if not bp.exists():
            bp.write_bytes(data)
        ev = {
            "schema_version": 1,
            "event_id": f"fs-{int(datetime.now().timestamp()*1000)}",
            "ts": now(),
            "pack_id": PACK_ID,
            "interaction": "high",
            "component": "sensor.fsmon",
            "src": {"ip": None, "port": None, "forwarded_for": [], "user_agent": None},
            "proto": "tcp",
            "request": {},
            "response": {"status_code": None, "bytes_sent": 0, "profile": None},
            "classification": {"verdict": "postex", "tags": ["fs_change"], "indicators": [str(path)]},
            "decision": {"truncated": len(data) >= MAX_BYTES, "oversized": False, "rate_limited": False, "dropped": False},
            "artifacts": [{"kind": "fs_write", "sha256": digest, "size": len(data), "mime": "application/octet-stream", "storage_ref": f"blobs/{digest[:2]}/{digest}", "meta": {"path": str(path), "preview": data[:128].decode('utf-8', errors='ignore')}}],
        }
        append_event(ev)


if __name__ == "__main__":
    observer = Observer()
    handler = Handler()
    for d in WATCH_DIRS:
        Path(d).mkdir(parents=True, exist_ok=True)
        observer.schedule(handler, d, recursive=True)
    observer.start()
    observer.join()
