from typing import Mapping

DEFAULT_REDACT_HEADERS = {"authorization", "cookie"}


def redact_headers(headers: Mapping[str, str], redact_list: list[str] | None = None) -> dict[str, str]:
    targets = {h.lower() for h in (redact_list or [])} | DEFAULT_REDACT_HEADERS
    out: dict[str, str] = {}
    for k, v in headers.items():
        out[k] = "<redacted>" if k.lower() in targets else v
    return out
