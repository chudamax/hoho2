from dataclasses import dataclass, field


@dataclass
class ArtifactRef:
    kind: str
    sha256: str
    size: int
    mime: str
    storage_ref: str
    meta: dict = field(default_factory=dict)

    def as_dict(self) -> dict:
        return {
            "kind": self.kind,
            "sha256": self.sha256,
            "size": self.size,
            "mime": self.mime,
            "storage_ref": self.storage_ref,
            "meta": self.meta,
        }
