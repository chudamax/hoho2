import os
from pathlib import Path

from hoho_core.storage.base import ArtifactStore
from hoho_core.telemetry.filters import load_rules_from_env, should_keep
from hoho_core.utils.hashing import sha256_bytes
from hoho_core.utils.jsonl import append_jsonl


class FilesystemArtifactStore(ArtifactStore):
    def __init__(self, root: str, honeypot_id: str):
        self.root = Path(root)
        self.honeypot_id = honeypot_id
        self.pack_root = self.root / honeypot_id
        self._emit_rules = load_rules_from_env("HOHO_EMIT_FILTERS_JSON")
        self._debug_drops = os.getenv("HOHO_EMIT_FILTERS_DEBUG", "false").lower() in {"1", "true", "yes", "on"}

    def put_blob(self, data: bytes, mime: str = "application/octet-stream") -> dict:
        digest = sha256_bytes(data)
        prefix = digest[:2]
        blob_path = self.pack_root / "blobs" / prefix / digest
        blob_path.parent.mkdir(parents=True, exist_ok=True)
        if not blob_path.exists():
            blob_path.write_bytes(data)
        return {
            "sha256": digest,
            "size": len(data),
            "mime": mime,
            "storage_ref": str(blob_path.relative_to(self.pack_root)),
        }

    def append_event(self, honeypot_id: str, event: dict) -> None:
        keep, rule = should_keep(event, self._emit_rules)
        if not keep:
            if self._debug_drops:
                append_jsonl(
                    self.root / honeypot_id / "index" / "events.jsonl",
                    {"event_name": "telemetry.drop", "reason": rule, "ts": event.get("ts")},
                )
            return
        append_jsonl(self.root / honeypot_id / "index" / "events.jsonl", event)
