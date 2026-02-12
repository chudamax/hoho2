import json
import os

from hoho_core.schema.validate import load_pack, validate_pack
from hoho_runtime.server.http import run_low_http


def main() -> None:
    pack_path = os.environ.get("HOHO_PACK_PATH", "/honeypot/honeypot.yaml")
    storage_root = os.environ.get("HOHO_STORAGE_ROOT", "/artifacts")

    pack = load_pack(pack_path)
    errors = validate_pack(pack)
    if errors:
        raise SystemExit("; ".join(errors))

    pack.setdefault("storage", {})["root"] = storage_root
    listen = (pack.get("listen") or [{"port": 8080}])[0]
    listen["host"] = "0.0.0.0"

    print(
        json.dumps(
            {
                "status": "ready",
                "component": "low_runtime",
                "pack_id": pack["metadata"]["id"],
                "pack_path": pack_path,
                "storage_root": storage_root,
                "listen_port": int(listen.get("port", 8080)),
            }
        )
    )
    run_low_http(pack)


if __name__ == "__main__":
    main()
