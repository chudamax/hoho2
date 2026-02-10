import json
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
    _append_event(storage_pack_root, event)


def _wait_for_ca_cert(ca_path: Path, timeout_seconds: int = 30, poll_seconds: float = 1.0) -> bool:
    deadline = time.time() + timeout_seconds
    while time.time() < deadline:
        if ca_path.exists() and ca_path.stat().st_size > 0:
            return True
        time.sleep(poll_seconds)
    return False


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
    cmd = ["docker", "compose"]
    if project_name:
        cmd.extend(["-p", project_name])
    cmd.extend(["-f", str(compose_file), "up", "-d"])
    rc = subprocess.call(cmd)
    if rc != 0 or not pack or not artifacts_root:
        return rc

    pack_id = pack.get("metadata", {}).get("id", "unknown-pack")
    storage_pack_root = artifacts_root / pack_id

    for sensor in pack.get("sensors", []):
        if sensor.get("type") != "egress_proxy":
            continue
        tls_mitm = sensor.get("config", {}).get("tls_mitm", {})
        if not bool(tls_mitm.get("enabled", False)):
            continue
        install_trust = tls_mitm.get("install_trust", {})
        if not bool(install_trust.get("enabled", True)):
            continue

        ca_path = storage_pack_root / "ca" / "egress-ca.crt"
        if not _wait_for_ca_cert(ca_path):
            for service in sensor.get("attach", {}).get("services", []):
                _emit_ca_install_event(
                    storage_pack_root=storage_pack_root,
                    pack_id=pack_id,
                    service_name=service,
                    kind="system.ca_install.failed",
                    exit_code=1,
                    stderr_snippet=f"timed out waiting for CA certificate at {ca_path}",
                )
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
