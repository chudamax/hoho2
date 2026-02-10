import json
import os
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _append_event(storage_pack_root: Path, event: dict) -> None:
    events_path = storage_pack_root / "index" / "events.jsonl"
    events_path.parent.mkdir(parents=True, exist_ok=True)
    with events_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event) + "\n")


def ensure_pack_eventlog(artifacts_pack_root: Path) -> Path:
    """
    Ensure <root>/index/events.jsonl exists and is writable by current user.
    Returns the path to events.jsonl.
    """
    index_path = artifacts_pack_root / "index"
    index_path.mkdir(parents=True, exist_ok=True)

    events_path = index_path / "events.jsonl"
    try:
        fd = os.open(events_path, os.O_CREAT | os.O_APPEND | os.O_WRONLY, 0o666)
    except OSError as exc:
        raise SystemExit(
            "[hoho] ERROR: unable to create/open events log before startup: "
            f"{events_path} ({exc}). Fix ownership and retry, e.g. `sudo chown -R "
            f"$USER:$USER {artifacts_pack_root}`."
        ) from exc

    try:
        os.fchmod(fd, 0o666)
    finally:
        os.close(fd)

    if not os.access(events_path, os.W_OK):
        owner_uid = events_path.stat().st_uid
        owner_gid = events_path.stat().st_gid
        current_uid = os.getuid()
        current_gid = os.getgid()
        raise SystemExit(
            "[hoho] ERROR: events log is not writable before startup: "
            f"{events_path} (owner={owner_uid}:{owner_gid}, current={current_uid}:{current_gid}). "
            "Fix ownership and retry, e.g. `sudo chown -R $USER:$USER "
            f"{artifacts_pack_root}`."
        )

    return events_path


def _emit_ca_install_event(
    *,
    storage_pack_root: Path,
    pack_id: str,
    service_name: str,
    kind: str,
    exit_code: int | None = None,
    stderr_snippet: str | None = None,
) -> None:
    event = {
        "schema_version": 1,
        "event_id": f"ca-install-{service_name}-{int(time.time() * 1000)}",
        "ts": _now_iso(),
        "pack_id": pack_id,
        "interaction": "high",
        "component": "runtime.compose",
        "kind": kind,
        "service": service_name,
    }
    if exit_code is not None:
        event["exit_code"] = exit_code
    if stderr_snippet:
        event["stderr_snippet"] = stderr_snippet
    try:
        _append_event(storage_pack_root, event)
    except OSError as exc:
        print(f"[hoho] WARN: cannot append to events.jsonl: {exc}")




def _bool_enabled(value: object, default: bool = False) -> bool:
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return bool(value)
    return str(value).strip().lower() in {"1", "true", "yes", "on"}

def _run_ca_install(
    *,
    compose_file: Path,
    project_name: str | None,
    service_name: str,
    storage_pack_root: Path,
    pack_id: str,
) -> None:
    cmd = ["docker", "compose"]
    if project_name:
        cmd.extend(["-p", project_name])
    cmd.extend(["-f", str(compose_file), "exec", "-T", service_name, "sh", "/hoho/ca/install-ca.sh", "/hoho/ca/egress-ca.crt"])
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode == 0:
        _emit_ca_install_event(
            storage_pack_root=storage_pack_root,
            pack_id=pack_id,
            service_name=service_name,
            kind="system.ca_install.succeeded",
        )
        return

    stderr = (proc.stderr or "").strip()
    _emit_ca_install_event(
        storage_pack_root=storage_pack_root,
        pack_id=pack_id,
        service_name=service_name,
        kind="system.ca_install.failed",
        exit_code=proc.returncode,
        stderr_snippet=stderr[:500],
    )


def run_compose(
    compose_file: Path,
    project_name: str | None = None,
    *,
    pack: dict | None = None,
    artifacts_root: Path | None = None,
) -> int:
    if pack and artifacts_root:
        pack_id = pack.get("metadata", {}).get("id", "unknown-pack")
        storage_pack_root = artifacts_root / pack_id
        storage_pack_root.mkdir(parents=True, exist_ok=True)
        (storage_pack_root / "ca").mkdir(parents=True, exist_ok=True)
        ensure_pack_eventlog(storage_pack_root)

    cmd = ["docker", "compose"]
    if project_name:
        cmd.extend(["-p", project_name])
    #cmd.extend(["-f", str(compose_file), "up", "-d"])
    cmd.extend(["-f", str(compose_file), "up"])
    rc = subprocess.call(cmd)
    if rc != 0 or not pack or not artifacts_root:
        return rc

    pack_id = pack.get("metadata", {}).get("id", "unknown-pack")
    storage_pack_root = artifacts_root / pack_id

    for sensor in pack.get("sensors", []):
        if sensor.get("type") != "egress_proxy":
            continue
        tls_mitm = sensor.get("config", {}).get("tls_mitm", {})
        if not _bool_enabled(tls_mitm.get("enabled", False)):
            continue
        install_trust = tls_mitm.get("install_trust", {})
        if not _bool_enabled(install_trust.get("enabled", True), default=True):
            continue
        ca_install = tls_mitm.get("ca_install", {})
        if not _bool_enabled(ca_install.get("enabled", True), default=True):
            continue
        if str(ca_install.get("mode", "auto")).strip().lower() == "off":
            continue

        for service in sensor.get("attach", {}).get("services", []):
            _run_ca_install(
                compose_file=compose_file,
                project_name=project_name,
                service_name=service,
                storage_pack_root=storage_pack_root,
                pack_id=pack_id,
            )

    return rc
