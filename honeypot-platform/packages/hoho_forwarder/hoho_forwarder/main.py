import json
import os
import time
from pathlib import Path

import requests

from hoho_core.telemetry.filters import load_rules_from_env, should_keep


def _iter_artifact_shas(event: dict) -> list[str]:
    return [a.get("sha256") for a in event.get("artifacts", []) if isinstance(a, dict) and a.get("sha256")]


def main() -> int:
    root = Path(os.getenv("HOHO_STORAGE_ROOT", "/artifacts"))
    honeypot_id = os.getenv("HOHO_HONEYPOT_ID", os.getenv("HOHO_PACK_ID", "unknown-pack"))
    hub_url = os.getenv("HOHO_HUB_URL", "").rstrip("/")
    token = os.getenv("HOHO_HUB_TOKEN", "")
    if not hub_url:
        print("[forwarder] HOHO_HUB_URL missing; exiting")
        return 0

    events_path = root / honeypot_id / "index" / "events.jsonl"
    cursor_path = root / honeypot_id / "index" / "forwarder.cursor"
    rules = load_rules_from_env("HOHO_FORWARD_FILTERS_JSON")
    headers = {"Authorization": f"Bearer {token}"} if token else {}

    offset = int(cursor_path.read_text().strip() or "0") if cursor_path.exists() else 0
    while True:
        events_path.parent.mkdir(parents=True, exist_ok=True)
        events_path.touch(exist_ok=True)
        with events_path.open("r", encoding="utf-8") as f:
            f.seek(offset)
            for line in f:
                offset = f.tell()
                try:
                    event = json.loads(line)
                except json.JSONDecodeError:
                    continue
                keep, _ = should_keep(event, rules)
                if not keep:
                    continue

                for sha in _iter_artifact_shas(event):
                    head = requests.head(f"{hub_url}/api/v1/blobs/{sha}", headers=headers, timeout=5)
                    if head.status_code == 404:
                        blob_path = root / honeypot_id / "blobs" / sha[:2] / sha
                        if blob_path.exists():
                            requests.put(
                                f"{hub_url}/api/v1/blobs/{sha}",
                                data=blob_path.read_bytes(),
                                headers=headers,
                                timeout=20,
                            )
                requests.post(f"{hub_url}/api/v1/events", json=event, headers=headers, timeout=5)
                cursor_path.write_text(str(offset), encoding="utf-8")
        time.sleep(1)


if __name__ == "__main__":
    raise SystemExit(main())
