#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import re
import shutil
from pathlib import Path

LEVELS = ("high", "low")
HONEYPOT_FILE = "honeypot.yaml"
README_FILE = "README.md"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def extract_metadata_id(yaml_text: str) -> str | None:
    metadata_match = re.search(r"^metadata:\s*\n([\s\S]*?)(?=^\S|\Z)", yaml_text, flags=re.M)
    if not metadata_match:
        return None
    md_block = metadata_match.group(1)
    id_match = re.search(r"^\s+id:\s*([\w.-]+)\s*$", md_block, flags=re.M)
    return id_match.group(1) if id_match else None


def find_pack_asset_roots(yaml_text: str, level: str) -> set[Path]:
    roots: set[Path] = set()
    prefix = f"./packs/{level}/"
    for match in re.finditer(r"([\"']?)(\./packs/(high|low)/[^\s\"']+)\1", yaml_text):
        value = match.group(2)
        if not value.startswith(prefix):
            continue
        rel = value[len(prefix) :]
        first = rel.split("/", 1)[0]
        if first:
            roots.add(Path(first))
    return roots


def rewrite_pack_paths(yaml_text: str, level: str) -> str:
    return yaml_text.replace(f"./packs/{level}/", "./")


def copy_file_if_missing(src: Path, dst: Path, warnings: list[str]) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        if sha256_file(src) != sha256_file(dst):
            warnings.append(f"conflict kept existing file: {dst}")
        return
    shutil.copy2(src, dst)


def merge_tree(src_root: Path, dst_root: Path, warnings: list[str]) -> None:
    for src in src_root.rglob("*"):
        rel = src.relative_to(src_root)
        dst = dst_root / rel
        if src.is_dir():
            dst.mkdir(parents=True, exist_ok=True)
        else:
            copy_file_if_missing(src, dst, warnings)


def migrate_level(repo_root: Path, level: str, dry_run: bool) -> tuple[int, list[str]]:
    packs_root = repo_root / "packs" / level
    honeypots_root = repo_root / "honeypots" / level
    honeypots_root.mkdir(parents=True, exist_ok=True)

    warnings: list[str] = []
    migrated = 0

    for pack_file in sorted(packs_root.glob("*.yaml")):
        yaml_text = pack_file.read_text(encoding="utf-8")
        honeypot_id = extract_metadata_id(yaml_text)
        if not honeypot_id:
            warnings.append(f"skipped (missing metadata.id): {pack_file}")
            continue

        target_dir = honeypots_root / honeypot_id
        target_dir.mkdir(parents=True, exist_ok=True)

        merge_candidates = [repo_root / "honeypots" / honeypot_id, repo_root / "honeypots" / level / honeypot_id]
        for candidate in merge_candidates:
            if candidate.is_dir():
                merge_tree(candidate, target_dir, warnings)

        for asset_root in sorted(find_pack_asset_roots(yaml_text, level)):
            src_asset = packs_root / asset_root
            dst_asset = target_dir / asset_root
            if not src_asset.exists():
                warnings.append(f"referenced asset missing: {src_asset}")
                continue
            if src_asset.is_dir():
                merge_tree(src_asset, dst_asset, warnings)
            else:
                copy_file_if_missing(src_asset, dst_asset, warnings)

        target_pack = target_dir / HONEYPOT_FILE
        rewritten = rewrite_pack_paths(yaml_text, level)
        if target_pack.exists() and target_pack.read_text(encoding="utf-8") != rewritten:
            warnings.append(f"overwrite canonical {HONEYPOT_FILE} from pack source: {target_pack}")
        if not dry_run:
            target_pack.write_text(rewritten, encoding="utf-8")

        readme = target_dir / README_FILE
        if not readme.exists() and not dry_run:
            readme.write_text(
                f"# {honeypot_id}\n\nMigrated honeypot. Document setup, run steps, and reset procedures here.\n",
                encoding="utf-8",
            )

        migrated += 1

    return migrated, warnings


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    total = 0
    warnings: list[str] = []

    for level in LEVELS:
        migrated, level_warnings = migrate_level(repo_root, level, args.dry_run)
        total += migrated
        warnings.extend(level_warnings)

    print(f"[migrate] mode={'dry-run' if args.dry_run else 'apply'} migrated_packs={total}")
    if warnings:
        print("[migrate] warnings:")
        for item in warnings:
            print(f"  - {item}")


if __name__ == "__main__":
    main()
