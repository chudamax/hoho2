import json
from pathlib import Path

from jsonschema import ValidationError, validate


_EVENT_SCHEMA_V2: dict | None = None


def _load_event_schema() -> dict:
    global _EVENT_SCHEMA_V2
    if _EVENT_SCHEMA_V2 is None:
        schema_path = Path(__file__).with_name("event_v2.json")
        _EVENT_SCHEMA_V2 = json.loads(schema_path.read_text(encoding="utf-8"))
    return _EVENT_SCHEMA_V2


def validate_event(event: dict) -> list[str]:
    try:
        validate(instance=event, schema=_load_event_schema())
    except ValidationError as exc:
        path = ".".join(str(p) for p in exc.path)
        return [f"schema error at {path}: {exc.message}" if path else f"schema error: {exc.message}"]
    return []
