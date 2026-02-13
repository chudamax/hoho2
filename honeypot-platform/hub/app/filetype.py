import logging
import mimetypes
from pathlib import Path

logger = logging.getLogger(__name__)

try:
    import magic
except Exception:  # pragma: no cover - optional dependency behavior
    magic = None


def detect_blob(path: Path, *, max_bytes: int = 262144) -> dict[str, str | None]:
    with path.open("rb") as handle:
        buf = handle.read(max(1, max_bytes))

    detected_mime: str | None = None
    detected_desc: str | None = None

    if magic is not None:
        try:
            detected_mime = magic.from_buffer(buf, mime=True)
            detected_desc = magic.from_buffer(buf, mime=False)
        except Exception as exc:  # pragma: no cover - defensive fallback
            logger.warning("filetype detection failed for %s: %s", path, exc)

    if not detected_mime:
        guessed_mime = mimetypes.guess_type(str(path))[0]
        detected_mime = guessed_mime or "application/octet-stream"
    if not detected_desc:
        detected_desc = "data"

    guessed_ext = mimetypes.guess_extension(detected_mime or "")
    if guessed_ext and guessed_ext.startswith("."):
        guessed_ext = guessed_ext[1:]

    return {
        "detected_mime": detected_mime,
        "detected_desc": detected_desc,
        "guessed_ext": guessed_ext,
    }
