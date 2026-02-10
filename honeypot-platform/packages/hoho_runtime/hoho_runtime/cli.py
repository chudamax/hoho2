import argparse
import json
from hoho_core.schema.validate import load_pack, validate_pack
from hoho_runtime.server.http import run_low_http
from hoho_runtime.orchestration.compose_render import render_compose
from hoho_runtime.orchestration.compose_run import run_compose


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
    out = render_compose(pack, args.output)
    print(out)


def cmd_run(args):
    pack = load_pack(args.pack)
    if pack["metadata"]["interaction"] == "low":
        run_low_http(pack)
    else:
        compose_file = render_compose(pack)
        if args.no_up:
            print(compose_file)
        else:
            raise SystemExit(run_compose(compose_file))


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
    p_run.set_defaults(func=cmd_run)

    p_rc = sub.add_parser("render-compose")
    p_rc.add_argument("pack")
    p_rc.add_argument("-o", "--output", default=None)
    p_rc.set_defaults(func=cmd_render_compose)

    p_ex = sub.add_parser("explain")
    p_ex.add_argument("pack")
    p_ex.set_defaults(func=cmd_explain)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
