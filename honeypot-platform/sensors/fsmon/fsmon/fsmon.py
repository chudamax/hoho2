import fnmatch
import os
from pathlib import Path

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from hoho_core.model.event import build_base_event
from hoho_core.storage.fs import FilesystemArtifactStore

HONEYPOT_ID = os.getenv("HOHO_HONEYPOT_ID", os.getenv("HOHO_PACK_ID", "unknown-pack"))
SESSION_ID = os.getenv("HOHO_SESSION_ID", "unknown-session")
AGENT_ID = os.getenv("HOHO_AGENT_ID", "unknown-agent")
ROOT = Path(os.getenv("HOHO_STORAGE_ROOT", "/artifacts"))
WATCH_DIRS = os.getenv("FSMON_WATCH", "/watched").split(",")
MAX_BYTES = int(os.getenv("FSMON_MAX_BYTES", "262144"))
ALLOW = [x for x in os.getenv("FSMON_ALLOW", "*").split(",") if x]
DENY = [x for x in os.getenv("FSMON_DENY", "").split(",") if x]
STORE = FilesystemArtifactStore(str(ROOT), HONEYPOT_ID)


def allow_path(path: str) -> bool:
    if any(fnmatch.fnmatch(path, pat) for pat in DENY):
        return False
    return any(fnmatch.fnmatch(path, pat) for pat in ALLOW)


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

        blob = STORE.put_blob(data)
        ev = build_base_event(
            honeypot_id=HONEYPOT_ID,
            component="sensor.fsmon",
            proto="fs",
            session_id=SESSION_ID,
            agent_id=AGENT_ID,
            event_name="fs.write",
        )
        ev["classification"] = {"verdict": "postex", "tags": ["fs_change"], "indicators": [str(path)]}
        ev["decision"]["truncated"] = len(data) >= MAX_BYTES
        ev["artifacts"] = [
            {
                "kind": "fs_write",
                **blob,
                "meta": {"path": str(path), "preview": data[:128].decode("utf-8", errors="ignore")},
            }
        ]
        STORE.append_event(HONEYPOT_ID, ev)


if __name__ == "__main__":
    observer = Observer()
    handler = Handler()
    for d in WATCH_DIRS:
        Path(d).mkdir(parents=True, exist_ok=True)
        observer.schedule(handler, d, recursive=True)
    observer.start()
    observer.join()
