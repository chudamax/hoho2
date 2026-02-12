import os
from pathlib import Path


def loadenv(path: Path, *, override: bool = False) -> dict[str, str]:
    loaded: dict[str, str] = {}

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        if not key:
            continue

        loaded[key] = value
        if override or key not in os.environ:
            os.environ[key] = value

    return loaded
