from abc import ABC, abstractmethod


class ArtifactStore(ABC):
    @abstractmethod
    def put_blob(self, data: bytes, mime: str = "application/octet-stream") -> dict:
        raise NotImplementedError

    @abstractmethod
    def append_event(self, pack_id: str, event: dict) -> None:
        raise NotImplementedError
