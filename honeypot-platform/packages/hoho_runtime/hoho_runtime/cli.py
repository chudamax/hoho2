import argparse
import json
import re
import shutil
from pathlib import Path

from hoho_core.schema.validate import load_pack, validate_pack
from hoho_runtime.config import DEFAULT_STORAGE_ROOT
from hoho_runtime.orchestration.compose_down_all import down_all
from hoho_runtime.orchestration.compose_render import render_compose
from hoho_runtime.orchestration.compose_run import run_compose
from hoho_runtime.server.http import run_low_http


def _sanitize_name(value: str) -> str:
    sanitized = re.sub(r"[^a-z0-9_-]", "-", value.lower()).strip("-_")
    return sanitized or "hoho"


def _warn_if_run_id_used(run_id: str | None) -> None:
    if run_id:
        print("WARNING: --run-id is deprecated and ignored; Simple Layout v1 always overwrites by honeypot_id.")


def _guess_project_root(pack_path: Path) -> Path:
    return _resolve_repo_root(pack_path.parent)


def _resolve_repo_root(start: Path) -> Path:
    candidates: list[Path] = [start, *start.parents]

    for candidate in candidates:
        compose_dir = candidate / "deploy" / "compose"
        if compose_dir.is_dir() or (compose_dir / "README.md").exists():
            return candidate

        nested_root = candidate / "honeypot-platform"
        nested_compose_dir = nested_root / "deploy" / "compose"
        if nested_compose_dir.is_dir() or (nested_compose_dir / "README.md").exists():
            return nested_root

    for candidate in candidates:
        if (candidate / "packs").is_dir():
            return candidate

    return start


def _compose_output_dir(honeypot_id: str, output: str | None, project_root: Path) -> str:
    if output:
        return output
    return str(project_root / "deploy" / "compose" / honeypot_id)


def _resolve_storage_root(pack: dict, artifacts_root_arg: str | None, project_root: Path) -> Path:
    storage_value = artifacts_root_arg or pack.get("storage", {}).get("root", DEFAULT_STORAGE_ROOT)
    storage_root = Path(storage_value).expanduser()
    if not storage_root.is_absolute():
        storage_root = project_root / storage_root
    return storage_root.resolve()


def _prepare_artifacts_root(storage_root: Path, honeypot_id: str) -> Path:
    artifacts_dir = storage_root / honeypot_id
    shutil.rmtree(artifacts_dir, ignore_errors=True)
    artifacts_dir.mkdir(parents=True, exist_ok=True)
    return artifacts_dir


def cmd_validate(args):
    pack = load_pack(args.pack)
    errors = validate_pack(pack)
    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        raise SystemExit(1)
    print("valid")


def cmd_render_compose(args):
    pack_path = Path(args.pack).expanduser().resolve()
    project_root = _guess_project_root(pack_path)

    pack = load_pack(str(pack_path))
    errors = validate_pack(pack)
    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        raise SystemExit(1)

    honeypot_id = pack["metadata"]["id"]
    _warn_if_run_id_used(args.run_id)
    out_dir = _compose_output_dir(honeypot_id, args.output, project_root=project_root)
    storage_root = _resolve_storage_root(pack, args.artifacts_root, project_root)
    out = render_compose(pack, out_dir=out_dir, artifacts_root=str(storage_root))
    print(out)


def cmd_run(args):
    pack_path = Path(args.pack).expanduser().resolve()
    project_root = _guess_project_root(pack_path)
    pack = load_pack(str(pack_path))
    storage_root = _resolve_storage_root(pack, args.artifacts_root, project_root)

    if pack["metadata"]["interaction"] == "low":
        pack.setdefault("storage", {})["root"] = str(storage_root)
        run_low_http(pack)
    else:
        honeypot_id = pack["metadata"]["id"]
        _warn_if_run_id_used(args.run_id)
        out_dir = _compose_output_dir(honeypot_id, args.output, project_root=project_root)

        artifacts_host_path = _prepare_artifacts_root(storage_root, honeypot_id)
        compose_file = render_compose(pack, out_dir=out_dir, artifacts_root=str(storage_root))
        project_name = _sanitize_name(f"hoho-{honeypot_id}")

        print(
            json.dumps(
                {
                    "honeypot_id": honeypot_id,
                    "artifacts_host_path": str(artifacts_host_path),
                    "compose_file": str(compose_file.resolve()),
                    "project_name": project_name,
                }
            )
        )

        if args.no_up:
            print(compose_file)
        else:
            raise SystemExit(run_compose(compose_file, project_name=project_name, pack=pack, artifacts_root=storage_root))


def cmd_explain(args):
    pack = load_pack(args.pack)
    plan = {
        "honeypot_id": pack["metadata"]["id"],
        "interaction": pack["metadata"]["interaction"],
        "listen": pack.get("listen", []),
        "limits": pack.get("limits", {}),
        "storage_root": pack.get("storage", {}).get("root", "./run/artifacts"),
        "sensors": pack.get("sensors", []),
    }
    print(json.dumps(plan, indent=2))


def cmd_down_all(args):
    repo_root = _resolve_repo_root(Path.cwd())
    result = down_all(
        repo_root,
        remove_volumes=args.volumes,
        dry_run=args.dry_run,
        include_stale=args.include_stale,
    )

    print(
        "found "
        f"{len(result.projects_found)} projects, "
        f"stopped {len(result.projects_stopped)}, "
        f"failed {len(result.projects_failed)}, "
        f"cleaned stale {len(result.stray_projects_cleaned)}"
    )

    if result.projects_failed:
        raise SystemExit(2)


def main():
    parser = argparse.ArgumentParser(prog="hoho")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_val = sub.add_parser("validate")
    p_val.add_argument("pack")
    p_val.set_defaults(func=cmd_validate)

    p_run = sub.add_parser("run")
    p_run.add_argument("pack")
    p_run.add_argument("--no-up", action="store_true")
    p_run.add_argument("--run-id", default=None)
    p_run.add_argument("--artifacts-root", default=None)
    p_run.add_argument("-o", "--output", default=None)
    p_run.set_defaults(func=cmd_run)

    p_rc = sub.add_parser("render-compose")
    p_rc.add_argument("pack")
    p_rc.add_argument("-o", "--output", default=None)
    p_rc.add_argument("--run-id", default=None)
    p_rc.add_argument("--artifacts-root", default=None)
    p_rc.set_defaults(func=cmd_render_compose)

    p_ex = sub.add_parser("explain")
    p_ex.add_argument("pack")
    p_ex.set_defaults(func=cmd_explain)

    p_down_all = sub.add_parser("down-all")
    p_down_all.add_argument("--volumes", action="store_true")
    p_down_all.add_argument("--dry-run", action="store_true")
    p_down_all.add_argument("--include-stale", action=argparse.BooleanOptionalAction, default=True)
    p_down_all.set_defaults(func=cmd_down_all)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
