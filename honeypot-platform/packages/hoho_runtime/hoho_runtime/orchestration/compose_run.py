import subprocess
from pathlib import Path


def run_compose(compose_file: Path) -> int:
    return subprocess.call(["docker", "compose", "-f", str(compose_file), "up"])
