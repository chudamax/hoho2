import argparse
import json
import re
import secrets
from datetime import datetime, timezone
from pathlib import Path

from hoho_core.schema.validate import load_pack, validate_pack
from hoho_runtime.config import DEFAULT_STORAGE_ROOT
from hoho_runtime.orchestration.compose_render import render_compose
from hoho_runtime.orchestration.compose_run import run_compose
from hoho_runtime.server.http import run_low_http


def _sanitize_name(value: str) -> str:
    sanitized = re.sub(r"[^a-z0-9_-]", "-", value.lower()).strip("-_")
    return sanitized or "hoho"


def _generate_run_id() -> str:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    return f"{timestamp}-{secrets.token_hex(3)}"


def _compose_output_dir(pack_id: str, run_id: str | None, output: str | None) -> str | None:
    if output:
        return output
    if run_id:
        return str(Path("./deploy/compose") / pack_id / run_id)
    return None


def cmd_validate(args):
    pack = load_pack(args.pack)
    errors = validate_pack(pack)
    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        raise SystemExit(1)
    print("valid")


def cmd_render_compose(args):
    pack = load_pack(args.pack)
    errors = validate_pack(pack)
    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        raise SystemExit(1)

    pack_id = pack["metadata"]["id"]
    out_dir = _compose_output_dir(pack_id, args.run_id, args.output)
    out = render_compose(pack, out_dir=out_dir, run_id=args.run_id, artifacts_root=args.artifacts_root)
    print(out)


def cmd_run(args):
    pack = load_pack(args.pack)
    if pack["metadata"]["interaction"] == "low":
        run_low_http(pack)
    else:
        pack_id = pack["metadata"]["id"]
        run_id = args.run_id or _generate_run_id()
        out_dir = _compose_output_dir(pack_id, run_id, args.output)
        compose_file = render_compose(pack, out_dir=out_dir, run_id=run_id, artifacts_root=args.artifacts_root)

        storage_root = Path(args.artifacts_root or pack.get("storage", {}).get("root", DEFAULT_STORAGE_ROOT))
        artifacts_host_path = (storage_root / "runs" / run_id).resolve() / pack_id
        project_name = _sanitize_name(f"hoho-{pack_id}-{run_id}")

        print(
            json.dumps(
                {
                    "pack_id": pack_id,
                    "run_id": run_id,
                    "artifacts_host_path": str(artifacts_host_path),
                    "compose_file": str(compose_file.resolve()),
                    "project_name": project_name,
                }
            )
        )

        if args.no_up:
            print(compose_file)
        else:
            raise SystemExit(run_compose(compose_file, project_name=project_name))


def cmd_explain(args):
    pack = load_pack(args.pack)
    plan = {
        "pack_id": pack["metadata"]["id"],
        "interaction": pack["metadata"]["interaction"],
        "listen": pack.get("listen", []),
        "limits": pack.get("limits", {}),
        "storage_root": pack.get("storage", {}).get("root", "./run/artifacts"),
        "sensors": pack.get("sensors", []),
    }
    print(json.dumps(plan, indent=2))


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

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
