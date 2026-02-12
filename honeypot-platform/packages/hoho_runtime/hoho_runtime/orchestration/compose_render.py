from copy import deepcopy
from pathlib import Path, PurePosixPath
import re
import shutil

import yaml

from hoho_runtime.config import DEFAULT_STORAGE_ROOT


SENSOR_IMAGES = {
    "proxy": "hoho/sensor-http-proxy:latest",
    "fsmon": "hoho/sensor-fsmon:latest",
    "pcap": "hoho/sensor-pcap:latest",
    "egress_proxy": "hoho/sensor-egress-proxy:latest",
    "falco": "hoho/sensor-falco:latest",
}


def _as_list(value) -> list:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def _collect_service_networks(service: dict) -> list[str]:
    networks = service.get("networks", [])
    if isinstance(networks, list):
        return [n for n in networks if isinstance(n, str)]
    if isinstance(networks, dict):
        return [n for n in networks.keys() if isinstance(n, str)]
    return []


def _parse_mount(volume_entry):
    if isinstance(volume_entry, str):
        parts = volume_entry.split(":")
        if len(parts) < 2:
            return None
        source = parts[0]
        target = parts[1]
        return {"source": source, "target": target, "raw": volume_entry}

    if isinstance(volume_entry, dict):
        source = volume_entry.get("source")
        target = volume_entry.get("target")
        if source and target:
            return {"source": source, "target": target, "raw": volume_entry}
    return None


def _find_covering_mount(service: dict, watch_path: str):
    watch = str(PurePosixPath(watch_path))
    best_mount = None
    best_len = -1
    for volume in _as_list(service.get("volumes", [])):
        parsed = _parse_mount(volume)
        if not parsed:
            continue
        target = str(PurePosixPath(parsed["target"]))
        if watch == target or watch.startswith(f"{target}/"):
            if len(target) > best_len:
                best_mount = parsed
                best_len = len(target)
    return best_mount


def _named_volume_source(source: str) -> bool:
    return not source.startswith("/") and not source.startswith(".")


def _collect_named_volumes(services: dict) -> set[str]:
    named = set()
    for service in services.values():
        for volume in _as_list(service.get("volumes", [])):
            parsed = _parse_mount(volume)
            if parsed and _named_volume_source(parsed["source"]):
                named.add(parsed["source"])
    return named


def _as_bool(value, default: bool = False) -> bool:
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in {"1", "true", "yes", "on"}
    return bool(value)


def _storage_env(pack_id: str) -> dict:
    return {
        "HOHO_PACK_ID": pack_id,
        "HOHO_STORAGE_BACKEND": "filesystem",
        "HOHO_STORAGE_ROOT": "/artifacts",
    }


def _low_runtime_service(pack: dict, artifacts_bind_mount: str, honeypot_dir: Path) -> dict:
    listen = _as_list(pack.get("listen", []))
    ports = []
    for entry in listen:
        if not isinstance(entry, dict):
            continue
        port = entry.get("port")
        if port is None:
            continue
        ports.append(f"{int(port)}:{int(port)}")

    return {
        "image": "hoho/low-runtime:latest",
        "environment": {
            **_storage_env(pack["metadata"]["id"]),
            "HOHO_PACK_PATH": "/honeypot/honeypot.yaml",
        },
        "volumes": [
            artifacts_bind_mount,
            f"{honeypot_dir.resolve()}:/honeypot:ro",
        ],
        "ports": ports,
    }




def _sanitize_name(value: str) -> str:
    sanitized = re.sub(r"[^a-z0-9_-]", "-", value.lower()).strip("-_")
    return sanitized or "hoho"


def _inject_egress_proxy_env(service: dict, service_names: list[str], port: int, set_env_bundles: bool):
    env = service.setdefault("environment", {})
    proxy_url = f"http://egress:{port}"
    no_proxy = ",".join(["localhost", "127.0.0.1", *service_names])

    env["HTTP_PROXY"] = proxy_url
    env["HTTPS_PROXY"] = proxy_url
    env["NO_PROXY"] = no_proxy
    env["http_proxy"] = proxy_url
    env["https_proxy"] = proxy_url
    env["no_proxy"] = no_proxy

    if set_env_bundles:
        env["SSL_CERT_FILE"] = "/hoho/ca/egress-ca.crt"
        env["REQUESTS_CA_BUNDLE"] = "/hoho/ca/egress-ca.crt"
        env["CURL_CA_BUNDLE"] = "/hoho/ca/egress-ca.crt"
        env["NODE_EXTRA_CA_CERTS"] = "/hoho/ca/egress-ca.crt"


def render_compose(
    pack: dict,
    out_dir: str | None = None,
    artifacts_root: str | None = None,
    honeypot_dir: str | Path | None = None,
) -> Path:
    pack_id = pack["metadata"]["id"]
    interaction = pack.get("metadata", {}).get("interaction")
    root = Path(out_dir or f"./deploy/compose/{pack_id}")
    shutil.rmtree(root, ignore_errors=True)
    root.mkdir(parents=True, exist_ok=True)

    runtime_root = root / "runtime"
    runtime_dir = runtime_root / "ca"
    runtime_dir.mkdir(parents=True, exist_ok=True)
    falco_runtime_dir = runtime_root / "falco"
    falco_runtime_dir.mkdir(parents=True, exist_ok=True)
    install_script = runtime_dir / "install-ca.sh"
    install_script.write_text(
        """#!/usr/bin/env sh
set -eu

cert_path=${1:-/hoho/ca/egress-ca.crt}
if [ ! -f \"$cert_path\" ]; then
    echo \"CA cert not found: $cert_path\" >&2
    exit 1
fi

if ! command -v update-ca-certificates >/dev/null 2>&1 && ! command -v update-ca-trust >/dev/null 2>&1; then
    if command -v apt-get >/dev/null 2>&1; then
        apt-get update >/dev/null 2>&1 || true
        apt-get install -y ca-certificates >/dev/null 2>&1 || true
    elif command -v apk >/dev/null 2>&1; then
        apk add --no-cache ca-certificates >/dev/null 2>&1 || true
    elif command -v dnf >/dev/null 2>&1; then
        dnf install -y ca-certificates >/dev/null 2>&1 || true
    elif command -v yum >/dev/null 2>&1; then
        yum install -y ca-certificates >/dev/null 2>&1 || true
    fi
fi

if command -v update-ca-certificates >/dev/null 2>&1; then
    mkdir -p /usr/local/share/ca-certificates
    cp "$cert_path" /usr/local/share/ca-certificates/hoho-egress-ca.crt
    update-ca-certificates || true
fi

if command -v update-ca-trust >/dev/null 2>&1; then
    mkdir -p /etc/pki/ca-trust/source/anchors
    cp "$cert_path" /etc/pki/ca-trust/source/anchors/hoho-egress-ca.crt
    update-ca-trust extract || true
fi

if [ -n "${HOHO_TRUST_EXTRA_COMMANDS:-}" ]; then
    printf '%s\n' "${HOHO_TRUST_EXTRA_COMMANDS}" | while IFS= read -r cmd; do
        [ -n "$cmd" ] || continue
        sh -c "$cmd" || true
    done
fi

exit 0
""",
        encoding="utf-8",
    )

    storage_root = Path(artifacts_root or pack.get("storage", {}).get("root", DEFAULT_STORAGE_ROOT))
    storage_root.mkdir(parents=True, exist_ok=True)
    artifacts_bind_mount = f"{storage_root.resolve()}:/artifacts"

    if interaction == "low":
        if honeypot_dir is None:
            raise ValueError("low interaction compose rendering requires honeypot_dir")
        services = {"honeypot": _low_runtime_service(pack, artifacts_bind_mount, Path(honeypot_dir))}
    else:
        services = deepcopy(pack.get("stack", {}).get("services", {}))

    valid_attach_services = set(services.keys())
    networks_used: set[str] = set()
    network_defs: dict[str, dict] = {}

    for service in services.values():
        networks_used.update(_collect_service_networks(service))

    for sensor in pack.get("sensors", []):
        sname = sensor["name"]
        stype = sensor["type"]
        attach = sensor.get("attach", {})
        config = sensor.get("config", {})

        sensor_service = {
            "image": SENSOR_IMAGES.get(stype, "busybox:latest"),
            "environment": _storage_env(pack_id),
            "volumes": [artifacts_bind_mount],
        }

        if stype == "fsmon":
            target_service_name = attach.get("service")
            target_service = services.get(target_service_name)
            if not target_service:
                raise ValueError(f"fsmon sensor '{sname}' attaches to unknown service '{target_service_name}'")

            watch_paths = _as_list(config.get("watch", []))
            if not watch_paths:
                raise ValueError(f"fsmon sensor '{sname}' requires config.watch")

            allow_globs = _as_list(config.get("allow_globs"))
            deny_globs = _as_list(config.get("deny_globs"))
            sensor_service["environment"].update(
                {
                    "FSMON_WATCH": ",".join(watch_paths),
                    "FSMON_ALLOW": ",".join(allow_globs) if allow_globs else "*",
                    "FSMON_DENY": ",".join(deny_globs),
                }
            )
            if config.get("max_bytes") is not None:
                sensor_service["environment"]["FSMON_MAX_BYTES"] = str(config["max_bytes"])

            seen_mounts = set()
            for watch_path in watch_paths:
                mount = _find_covering_mount(target_service, watch_path)
                if not mount:
                    raise ValueError(
                        f"fsmon watch path {watch_path} is not backed by a named volume/bind mount in service {target_service_name}; "
                        "sidecar can't see container rootfs"
                    )
                mount_key = (mount["source"], mount["target"])
                if mount_key in seen_mounts:
                    continue
                seen_mounts.add(mount_key)
                sensor_service["volumes"].append(f"{mount['source']}:{mount['target']}")

            target_networks = _collect_service_networks(target_service)
            if target_networks:
                sensor_service["networks"] = target_networks
                networks_used.update(target_networks)

        elif stype == "proxy":
            target_service_name = attach.get("service")
            target_service = services.get(target_service_name)
            if not target_service:
                raise ValueError(f"proxy sensor '{sname}' attaches to unknown service '{target_service_name}'")
            upstream = config.get("upstream")
            if not upstream:
                raise ValueError(f"proxy sensor '{sname}' requires config.upstream")

            listen_port = int(config.get("listen_port", 8080))
            listen_host = str(config.get("listen_host", "0.0.0.0"))
            keep_host_header = _as_bool(config.get("keep_host_header"), default=True)
            sensor_service["environment"].update(
                {
                    "UPSTREAM": upstream,
                    "PROXY_LISTEN_PORT": str(listen_port),
                    "PROXY_LISTEN_HOST": listen_host,
                    "PROXY_KEEP_HOST_HEADER": "true" if keep_host_header else "false",
                }
            )

            target_networks = _collect_service_networks(target_service)
            if target_networks:
                sensor_service["networks"] = target_networks
                networks_used.update(target_networks)

            moved_ports = _as_list(target_service.get("ports", []))
            if moved_ports:
                proxy_ports = []
                for port in moved_ports:
                    if isinstance(port, str) and ":" in port:
                        host_port = port.rsplit(":", 1)[0]
                        proxy_ports.append(f"{host_port}:{listen_port}")
                    else:
                        proxy_ports.append(port)
                sensor_service["ports"] = proxy_ports
                target_service["ports"] = []

        elif stype == "pcap":
            target_service_name = attach.get("service")
            target_network = attach.get("network")
            if target_service_name:
                if target_service_name not in valid_attach_services:
                    raise ValueError(f"pcap sensor '{sname}' attaches to unknown service '{target_service_name}'")
                sensor_service["network_mode"] = f"service:{target_service_name}"
            elif target_network:
                sensor_service["networks"] = [target_network]
                networks_used.add(target_network)

            sensor_service["cap_add"] = ["NET_ADMIN", "NET_RAW"]
            if config.get("rotate_seconds") is not None:
                sensor_service["environment"]["PCAP_ROTATE_SECONDS"] = str(config["rotate_seconds"])
            if config.get("rotate_count") is not None:
                sensor_service["environment"]["PCAP_ROTATE_COUNT"] = str(config["rotate_count"])
            if config.get("interface") is not None:
                sensor_service["environment"]["PCAP_INTERFACE"] = str(config["interface"])

        elif stype == "falco":
            if interaction != "high":
                raise ValueError("falco sensor is only supported for high interaction honeypots")

            mode = str(config.get("mode", "privileged"))
            engine = str(config.get("engine", "modern_ebpf"))
            priority_min = str(config.get("priority_min", "Warning"))
            append_fields = _as_list(config.get("append_fields", []))
            any_exec = _as_bool(config.get("any_exec"), default=False)
            enforce = config.get("enforce", {})
            enforce_enabled = _as_bool(enforce.get("enabled"), default=False)
            enforce_priorities = _as_list(enforce.get("match_priorities", ["Critical", "Error"]))
            enforce_rules = _as_list(enforce.get("match_rules", []))
            enforce_action = str(enforce.get("action", "stop_container"))
            cooldown_seconds = int(enforce.get("cooldown_seconds", 60))

            project_name = _sanitize_name(f"hoho-{pack_id}")
            attach_services = _as_list(attach.get("services", []))
            for attach_service_name in attach_services:
                if attach_service_name not in valid_attach_services:
                    raise ValueError(f"falco sensor '{sname}' attaches to unknown service '{attach_service_name}'")

            default_rules = ["/app/rules/hoho_rules.yaml"]
            if any_exec:
                default_rules.append("/app/rules/hoho_any_exec.yaml")

            sensor_service["environment"].update(
                {
                    "FALCO_PRIORITY_MIN": priority_min,
                    "FALCO_ENGINE": engine,
                    "FALCO_RULES": ",".join(default_rules),
                    "HOHO_FALCO_PROJECT": project_name,
                    "HOHO_FALCO_ONLY_PROJECT": "true",
                    "HOHO_FALCO_APPEND_FIELDS": ",".join(str(f) for f in append_fields if f),
                    "HOHO_FALCO_ENFORCE_ENABLED": "true" if enforce_enabled else "false",
                    "HOHO_FALCO_ENFORCE_MATCH_PRIORITIES": ",".join(str(x) for x in enforce_priorities),
                    "HOHO_FALCO_ENFORCE_MATCH_RULES": ",".join(str(x) for x in enforce_rules),
                    "HOHO_FALCO_ENFORCE_ACTION": enforce_action,
                    "HOHO_FALCO_ENFORCE_COOLDOWN_SECONDS": str(cooldown_seconds),
                }
            )
            if attach_services:
                sensor_service["environment"]["HOHO_FALCO_ONLY_SERVICES"] = ",".join(attach_services)

            custom_rules = []
            for rule_path in _as_list(config.get("rules", [])):
                if not isinstance(rule_path, str) or not rule_path:
                    continue
                if rule_path.startswith("runtime/falco/"):
                    continue
                if rule_path.startswith("./"):
                    rule_src = (Path(honeypot_dir) / rule_path).resolve() if honeypot_dir else None
                    if rule_src and rule_src.is_file():
                        dst = falco_runtime_dir / rule_src.name
                        shutil.copy2(rule_src, dst)
                        custom_rules.append(f"/runtime/falco/{dst.name}")
                else:
                    custom_rules.append(rule_path)

            rules_all = [*default_rules, *custom_rules]
            sensor_service["environment"]["FALCO_RULES"] = ",".join(rules_all)

            sensor_service["volumes"].extend(
                [
                    f"{falco_runtime_dir.resolve()}:/runtime/falco:ro",
                    "/sys/kernel/tracing:/sys/kernel/tracing:ro",
                    "/proc:/host/proc:ro",
                    "/etc:/host/etc:ro",
                    "/var/run/docker.sock:/host/var/run/docker.sock",
                ]
            )

            if mode == "privileged":
                sensor_service["privileged"] = True
            sensor_service["network_mode"] = "host"
        elif stype == "egress_proxy":
            attach_services = _as_list(attach.get("services", []))
            for attach_service_name in attach_services:
                if attach_service_name not in valid_attach_services:
                    raise ValueError(
                        f"egress_proxy sensor '{sname}' attaches to unknown service '{attach_service_name}'"
                    )

            listen_host = str(config.get("listen_host", "0.0.0.0"))
            listen_port = int(config.get("listen_port", 3128))
            force_egress = _as_bool(config.get("force_egress_via_proxy"), default=True)

            tls_mitm = config.get("tls_mitm", {})
            tls_mitm_enabled = _as_bool(tls_mitm.get("enabled"), default=False)
            install_trust = tls_mitm.get("install_trust", {})
            set_env_bundles = _as_bool(install_trust.get("also_set_env_bundles"), default=True)
            extra_commands = _as_list(install_trust.get("extra_commands", []))

            capture = config.get("capture", {})
            capture_enabled = _as_bool(capture.get("enabled"), default=True)
            capture_bodies = str(capture.get("bodies", "*"))
            capture_max_bytes = int(capture.get("max_bytes", 52428800))
            capture_store_ok_only = _as_bool(capture.get("store_ok_only"), default=True)
            capture_min_bytes = int(capture.get("min_bytes", 1))
            redact_headers = _as_list(capture.get("redact_headers", ["Authorization", "Cookie"]))

            sensor_service["environment"].update(
                {
                    "PROXY_LISTEN_HOST": listen_host,
                    "PROXY_LISTEN_PORT": str(listen_port),
                    "PROXY_STACK_ID": pack_id,
                    "PROXY_TLS_MITM_ENABLED": "true" if tls_mitm_enabled else "false",
                    "PROXY_CA_CERT_PATH": "/runtime/ca/egress-ca.crt",
                    "PROXY_CA_KEY_PATH": "/runtime/ca/egress-ca.key",
                    "PROXY_MITM_BUNDLE_PATH": "/runtime/ca/mitmproxy-ca.pem",
                    "PROXY_MITM_CERT_PATH": "/runtime/ca/mitmproxy-ca-cert.pem",
                    "PROXY_CAPTURE_ENABLED": "true" if capture_enabled else "false",
                    "PROXY_CAPTURE_BODIES": capture_bodies,
                    "PROXY_CAPTURE_MAX_BYTES": str(capture_max_bytes),
                    "PROXY_CAPTURE_STORE_OK_ONLY": "true" if capture_store_ok_only else "false",
                    "PROXY_CAPTURE_MIN_BYTES": str(capture_min_bytes),
                    "PROXY_REDACT_HEADERS": ",".join(redact_headers),
                }
            )
            sensor_service["volumes"].append(f"{(root / 'runtime').resolve()}:/runtime:ro")
            sensor_service["volumes"].append(f"{(root / 'runtime' / 'ca').resolve()}:/runtime/ca:ro")
            sensor_service["volumes"].append(f"{(storage_root / pack_id).resolve()}:/artifacts/{pack_id}")

            all_service_names = sorted([name for name in services.keys() if name != sname])
            for attach_service_name in attach_services:
                attach_service = services[attach_service_name]
                _inject_egress_proxy_env(attach_service, all_service_names, listen_port, set_env_bundles)
                if tls_mitm_enabled:
                    if extra_commands:
                        attach_service.setdefault("environment", {})["HOHO_TRUST_EXTRA_COMMANDS"] = "\n".join(
                            str(cmd) for cmd in extra_commands
                        )
                    attach_service.setdefault("volumes", []).extend(
                        [
                            f"{(root / 'runtime' / 'ca' / 'install-ca.sh').resolve()}:/hoho/ca/install-ca.sh:ro",
                            f"{(root / 'runtime' / 'ca' / 'egress-ca.crt').resolve()}:/hoho/ca/egress-ca.crt:ro",
                        ]
                    )

            sensor_service["networks"] = list(networks_used)
            #networks_used.update({"hp_internal", "hp_external", "frontend"})
            
            if force_egress:
                network_defs["hp_internal"] = {"internal": True}
                network_defs["hp_external"] = {}
                sensor_service["networks"] = ["hp_internal", "hp_external"]
                networks_used.update({"hp_internal", "hp_external"})

                for attach_service_name in attach_services:
                    services[attach_service_name]["networks"] = ["hp_internal"]

        services[sname] = sensor_service

    compose = {"services": services}

    named_volumes = sorted(_collect_named_volumes(services))
    if named_volumes:
        compose["volumes"] = {volume_name: {} for volume_name in named_volumes}

    if networks_used or network_defs:
        compose["networks"] = {name: network_defs.get(name, {}) for name in sorted(networks_used | set(network_defs.keys()))}

    out = root / "docker-compose.yml"
    out.write_text(yaml.safe_dump(compose, sort_keys=False), encoding="utf-8")
    return out
