from pathlib import Path
from hoho_core.storage.base import ArtifactStore
from hoho_core.utils.hashing import sha256_bytes
from hoho_core.utils.jsonl import append_jsonl


class FilesystemArtifactStore(ArtifactStore):
    def __init__(self, root: str, pack_id: str):
        self.root = Path(root)
        self.pack_id = pack_id
        self.pack_root = self.root / pack_id

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

    def append_event(self, pack_id: str, event: dict) -> None:
        append_jsonl(self.root / pack_id / "index" / "events.jsonl", event)
