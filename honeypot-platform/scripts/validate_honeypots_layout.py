#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

LEVELS = ("high", "low")


def extract_metadata_id(yaml_text: str) -> str | None:
    metadata_match = re.search(r"^metadata:\s*\n([\s\S]*?)(?=^\S|\Z)", yaml_text, flags=re.M)
    if not metadata_match:
        return None
    md_block = metadata_match.group(1)
    id_match = re.search(r"^\s+id:\s*([\w.-]+)\s*$", md_block, flags=re.M)
    return id_match.group(1) if id_match else None


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    errors: list[str] = []

    honeypots_root = repo_root / "honeypots"
    for level in LEVELS:
        level_root = honeypots_root / level
        if not level_root.is_dir():
            errors.append(f"missing level directory: {level_root.relative_to(repo_root)}")
            continue

        for hp_dir in sorted(p for p in level_root.iterdir() if p.is_dir()):
            pack_file = hp_dir / "honeypot.yaml"
            readme_file = hp_dir / "README.md"

            if not pack_file.is_file():
                errors.append(f"missing honeypot.yaml: {hp_dir.relative_to(repo_root)}")
                continue
            if not readme_file.is_file():
                errors.append(f"missing README.md: {hp_dir.relative_to(repo_root)}")

            yaml_text = pack_file.read_text(encoding="utf-8")
            metadata_id = extract_metadata_id(yaml_text)
            if metadata_id != hp_dir.name:
                errors.append(
                    f"metadata.id mismatch in {pack_file.relative_to(repo_root)}: metadata.id={metadata_id!r}, folder={hp_dir.name!r}"
                )

            for match in re.finditer(r"([\"'])([^\"']*\.\./[^\"']*)\1", yaml_text):
                value = match.group(2)
                resolved = (hp_dir / value).resolve()
                try:
                    resolved.relative_to(hp_dir.resolve())
                except ValueError:
                    errors.append(f"path escapes honeypot directory in {pack_file.relative_to(repo_root)}: {value}")

    if errors:
        print("layout validation failed:")
        for error in errors:
            print(error)
        return 1

    print("honeypots layout validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
