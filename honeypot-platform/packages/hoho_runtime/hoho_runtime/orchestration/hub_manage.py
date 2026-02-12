import subprocess
from pathlib import Path


def _compose_base_cmd(compose_file: Path, env_file: Path | None) -> list[str]:
    cmd = ["docker", "compose"]
    if env_file is not None:
        cmd.extend(["--env-file", str(env_file)])
    cmd.extend(["-f", str(compose_file)])
    return cmd


def hub_up(repo_root: Path, env_file: Path | None) -> int:
    compose_file = repo_root / "hub" / "docker-compose.yml"
    cmd = _compose_base_cmd(compose_file, env_file)
    cmd.extend(["up", "-d", "--build"])
    return subprocess.call(cmd)


def hub_down(repo_root: Path, env_file: Path | None) -> int:
    compose_file = repo_root / "hub" / "docker-compose.yml"
    cmd = _compose_base_cmd(compose_file, env_file)
    cmd.append("down")
    return subprocess.call(cmd)


def hub_logs(repo_root: Path, env_file: Path | None) -> int:
    compose_file = repo_root / "hub" / "docker-compose.yml"
    cmd = _compose_base_cmd(compose_file, env_file)
    cmd.extend(["logs", "-f", "--tail=200"])
    return subprocess.call(cmd)
