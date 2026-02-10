from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import json
import re
import subprocess


@dataclass
class DownAllResult:
    projects_found: list[str]
    projects_stopped: list[str]
    projects_failed: list[str]
    stray_projects_cleaned: list[str]


def _sanitize_project_name(value: str) -> str:
    sanitized = re.sub(r"[^a-z0-9_-]", "-", value.lower()).strip("-_")
    return sanitized or "hoho"


def _run_cmd(cmd: list[str]) -> tuple[int, str, str]:
    proc = subprocess.run(cmd, capture_output=True, text=True)
    return proc.returncode, proc.stdout, proc.stderr


def _run_action(cmd: list[str], *, dry_run: bool) -> int:
    print("$ " + " ".join(cmd))
    if dry_run:
        return 0
    proc = subprocess.run(cmd)
    return proc.returncode


def _list_compose_projects() -> set[str]:
    projects: set[str] = set()
    rc, stdout, _ = _run_cmd(["docker", "compose", "ls", "--format", "json"])
    if rc == 0 and stdout.strip():
        try:
            payload = json.loads(stdout)
            if isinstance(payload, list):
                for entry in payload:
                    if not isinstance(entry, dict):
                        continue
                    name = entry.get("Name") or entry.get("name")
                    if isinstance(name, str) and name.startswith("hoho-"):
                        projects.add(name)
        except json.JSONDecodeError:
            pass
    return projects


def _list_projects_by_label() -> set[str]:
    projects: set[str] = set()
    cmd = [
        "docker",
        "ps",
        "-a",
        "--filter",
        "label=com.docker.compose.project",
        "--format",
        "{{.Label \"com.docker.compose.project\"}}",
    ]
    rc, stdout, _ = _run_cmd(cmd)
    if rc != 0:
        return projects

    for line in stdout.splitlines():
        project = line.strip()
        if project.startswith("hoho-"):
            projects.add(project)
    return projects


def _remove_stray_project(project_name: str, *, remove_volumes: bool, dry_run: bool) -> bool:
    failed = False

    rc, stdout, _ = _run_cmd(
        ["docker", "ps", "-a", "--filter", f"label=com.docker.compose.project={project_name}", "-q"]
    )
    container_ids = [item for item in stdout.split() if item]
    if rc == 0 and container_ids:
        cmd = ["docker", "rm", "-f", *container_ids]
        if _run_action(cmd, dry_run=dry_run) != 0:
            failed = True

    rc, stdout, _ = _run_cmd(
        ["docker", "network", "ls", "-q", "--filter", f"label=com.docker.compose.project={project_name}"]
    )
    network_ids = [item for item in stdout.split() if item]
    if rc == 0 and network_ids:
        cmd = ["docker", "network", "rm", *network_ids]
        if _run_action(cmd, dry_run=dry_run) != 0:
            failed = True

    if remove_volumes:
        rc, stdout, _ = _run_cmd(
            ["docker", "volume", "ls", "-q", "--filter", f"label=com.docker.compose.project={project_name}"]
        )
        volume_ids = [item for item in stdout.split() if item]
        if rc == 0 and volume_ids:
            cmd = ["docker", "volume", "rm", *volume_ids]
            if _run_action(cmd, dry_run=dry_run) != 0:
                failed = True

    return not failed


def down_all(
    repo_root: Path,
    *,
    remove_volumes: bool = False,
    dry_run: bool = False,
    include_stale: bool = True,
) -> DownAllResult:
    """
    Stops/removes all hoho honeypot compose projects.
    Primary source of truth: deploy/compose/<honeypot_id>/docker-compose.yml.
    Secondary (stale) cleanup: docker compose ls + docker labels.
    """
    compose_files = sorted((repo_root / "deploy" / "compose").glob("*/docker-compose.yml"))

    projects_found: list[str] = []
    projects_stopped: list[str] = []
    projects_failed: list[str] = []
    stray_projects_cleaned: list[str] = []

    handled_projects: set[str] = set()

    for compose_file in compose_files:
        honeypot_id = compose_file.parent.name
        project_name = _sanitize_project_name(f"hoho-{honeypot_id}")

        projects_found.append(project_name)
        handled_projects.add(project_name)

        cmd = ["docker", "compose", "-p", project_name, "-f", str(compose_file), "down", "--remove-orphans"]
        if remove_volumes:
            cmd.append("--volumes")

        rc = _run_action(cmd, dry_run=dry_run)
        if rc == 0:
            projects_stopped.append(project_name)
        else:
            projects_failed.append(project_name)

    if include_stale:
        stale_projects = _list_compose_projects() | _list_projects_by_label()
        for project_name in sorted(stale_projects):
            if not project_name.startswith("hoho-"):
                continue
            if project_name in handled_projects:
                continue

            if _remove_stray_project(project_name, remove_volumes=remove_volumes, dry_run=dry_run):
                stray_projects_cleaned.append(project_name)
            else:
                projects_failed.append(project_name)

    return DownAllResult(
        projects_found=projects_found,
        projects_stopped=projects_stopped,
        projects_failed=projects_failed,
        stray_projects_cleaned=stray_projects_cleaned,
    )
