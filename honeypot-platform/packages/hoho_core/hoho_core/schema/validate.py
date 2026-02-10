import json


def load_pack(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise ValueError(f"pack parsing error: only JSON-compatible YAML is supported in this environment ({exc})")


def validate_pack(pack: dict) -> list[str]:
    out: list[str] = []
    if pack.get("apiVersion") != "hoho.dev/v1":
        out.append("apiVersion must be hoho.dev/v1")
    if pack.get("kind") != "HoneypotPack":
        out.append("kind must be HoneypotPack")

    md = pack.get("metadata", {})
    for req in ["id", "name", "interaction", "description"]:
        if not md.get(req):
            out.append(f"metadata.{req} is required")
    if md.get("interaction") not in {"low", "high"}:
        out.append("metadata.interaction must be low or high")

    interaction = md.get("interaction")
    if interaction == "low" and "behaviors" not in pack:
        out.append("low interaction pack requires behaviors")
    if interaction == "high" and "stack" not in pack:
        out.append("high interaction pack requires stack")
    return out
