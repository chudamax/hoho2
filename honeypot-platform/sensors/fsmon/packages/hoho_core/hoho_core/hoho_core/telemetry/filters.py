import json
import re
from typing import Any


def _iter_values(obj: Any, parts: list[str]) -> list[Any]:
    if not parts:
        return [obj]
    if isinstance(obj, list):
        out: list[Any] = []
        for item in obj:
            out.extend(_iter_values(item, parts))
        return out
    if not isinstance(obj, dict):
        return []
    key = parts[0]
    if key not in obj:
        return []
    return _iter_values(obj[key], parts[1:])


def _match_condition(event: dict, cond: dict) -> bool:
    if "all" in cond:
        return all(_match_condition(event, c) for c in cond.get("all", []))
    if "any" in cond:
        return any(_match_condition(event, c) for c in cond.get("any", []))

    field = cond.get("field")
    if not field:
        return False
    values = _iter_values(event, str(field).split("."))

    if "exists" in cond:
        return bool(values) is bool(cond["exists"])
    if not values:
        return False

    for value in values:
        if "eq" in cond and value == cond["eq"]:
            return True
        if "neq" in cond and value != cond["neq"]:
            return True
        if "in" in cond and value in cond["in"]:
            return True
        if "contains" in cond and str(cond["contains"]) in str(value):
            return True
        if "regex" in cond and re.search(str(cond["regex"]), str(value)):
            return True
        if "gte" in cond:
            try:
                if value >= cond["gte"]:
                    return True
            except TypeError:
                pass
        if "lte" in cond:
            try:
                if value <= cond["lte"]:
                    return True
            except TypeError:
                pass
    return False


def parse_filter_config(config: dict | None) -> list[dict]:
    if not config:
        return []
    if isinstance(config, list):
        return config
    return []


def load_rules_from_env(env_key: str) -> list[dict]:
    raw = __import__("os").getenv(env_key, "")
    if not raw.strip():
        return []
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError:
        return []
    return parse_filter_config(parsed)


def should_keep(event: dict, rules: list[dict]) -> tuple[bool, str | None]:
    for rule in rules:
        when = rule.get("when")
        matched = True if when is None else _match_condition(event, when)
        if not matched:
            continue
        action = str(rule.get("action", "keep")).lower()
        return action != "drop", rule.get("name")
    return True, None
