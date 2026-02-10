from pathlib import Path


def _to_yaml(obj, indent=0):
    sp = "  " * indent
    if isinstance(obj, dict):
        lines = []
        for k, v in obj.items():
            if isinstance(v, (dict, list)):
                lines.append(f"{sp}{k}:")
                lines.append(_to_yaml(v, indent + 1))
            else:
                if isinstance(v, str) and any(c in v for c in [":", "#", "{"]):
                    v = f'"{v}"'
                lines.append(f"{sp}{k}: {v}")
        return "\n".join(lines)
    if isinstance(obj, list):
        lines = []
        for item in obj:
            if isinstance(item, (dict, list)):
                lines.append(f"{sp}-")
                lines.append(_to_yaml(item, indent + 1))
            else:
                lines.append(f"{sp}- {item}")
        return "\n".join(lines)
    return f"{sp}{obj}"


def render_compose(pack: dict, out_dir: str | None = None) -> Path:
    pack_id = pack["metadata"]["id"]
    root = Path(out_dir or f"./deploy/compose/{pack_id}")
    root.mkdir(parents=True, exist_ok=True)
    services = dict(pack.get("stack", {}).get("services", {}))

    for sensor in pack.get("sensors", []):
        sname = sensor["name"]
        stype = sensor["type"]
        image_map = {
            "proxy": "hoho/sensor-http-proxy:latest",
            "fsmon": "hoho/sensor-fsmon:latest",
            "pcap": "hoho/sensor-pcap:latest",
        }
        services[sname] = {
            "image": image_map.get(stype, "busybox:latest"),
            "environment": {
                "HOHO_PACK_ID": pack_id,
                "HOHO_STORAGE_BACKEND": "filesystem",
                "HOHO_STORAGE_ROOT": "/artifacts",
            },
            "volumes": ["artifacts:/artifacts"],
        }
    compose = {"version": "3.9", "services": services, "volumes": {"artifacts": {}}}
    out = root / "docker-compose.yml"
    out.write_text(_to_yaml(compose) + "\n", encoding="utf-8")
    return out
