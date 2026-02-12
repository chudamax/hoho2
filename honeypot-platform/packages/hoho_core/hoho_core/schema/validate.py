import json
from pathlib import Path

import yaml
from jsonschema import ValidationError, validate


def load_pack(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    suffix = Path(path).suffix.lower()
    try:
        if suffix == ".json":
            data = json.loads(text)
        elif suffix in {".yaml", ".yml"}:
            data = yaml.safe_load(text)
        else:
            raise ValueError(f"unsupported pack format '{suffix}', expected .json, .yaml, or .yml")
    except (json.JSONDecodeError, yaml.YAMLError) as exc:
        raise ValueError(f"pack parsing error: {exc}") from exc

    if not isinstance(data, dict):
        raise ValueError("pack parsing error: top-level document must be an object")
    return data


def _load_schema() -> dict:
    schema_path = Path(__file__).with_name("pack_v1.json")
    return json.loads(schema_path.read_text(encoding="utf-8"))


def _format_schema_error(exc: ValidationError) -> str:
    path = ".".join(str(part) for part in exc.path)
    if path:
        return f"schema error at {path}: {exc.message}"
    return f"schema error: {exc.message}"


def validate_pack(pack: dict) -> list[str]:
    out: list[str] = []

    try:
        validate(instance=pack, schema=_load_schema())
    except ValidationError as exc:
        out.append(_format_schema_error(exc))
        return out

    interaction = pack.get("metadata", {}).get("interaction")
    if interaction == "low" and "behaviors" not in pack:
        out.append("semantic error: low interaction pack requires behaviors")
    if interaction == "high" and "stack" not in pack:
        out.append("semantic error: high interaction pack requires stack")

    services = pack.get("stack", {}).get("services", {})
    service_names = set(services.keys()) if isinstance(services, dict) else set()
    if interaction == "low":
        service_names.add("honeypot")

    for sensor in pack.get("sensors", []):
        sensor_name = sensor.get("name", "<unnamed>")
        sensor_type = sensor.get("type")
        attach = sensor.get("attach", {})

        if sensor_type in {"fsmon", "proxy", "pcap"}:
            target_service = attach.get("service")
            if target_service and target_service not in service_names:
                out.append(
                    f"semantic error: {sensor_type} sensor '{sensor_name}' attaches to unknown service '{target_service}'"
                )

        if sensor_type == "egress_proxy":
            attached_services = attach.get("services", [])
            for service_name in attached_services:
                if service_name not in service_names:
                    out.append(
                        f"semantic error: egress_proxy sensor '{sensor_name}' attaches to unknown service '{service_name}'"
                    )

    return out
