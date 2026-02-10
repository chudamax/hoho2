import subprocess
from pathlib import Path


def run_compose(compose_file: Path, project_name: str | None = None) -> int:
    cmd = ["docker", "compose"]
    if project_name:
        cmd.extend(["-p", project_name])
    cmd.extend(["-f", str(compose_file), "up", "-d"])
    return subprocess.call(cmd)
