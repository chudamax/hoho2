import gzip
import random
import time
from hoho_core.dsl.templates import render_template


def run_action(action: dict, state: dict, req: dict, store) -> None:
    if "emit_event" in action:
        data = action["emit_event"]
        state["classification"]["verdict"] = data.get("verdict", state["classification"]["verdict"])
        state["classification"]["tags"].extend(data.get("tags", []))
        state["classification"]["indicators"].extend(data.get("indicators", []))
    elif "store_body" in action:
        data = req.get("body", b"")
        conf = action["store_body"]
        if conf.get("gzip"):
            data = gzip.compress(data)
            mime = "application/gzip"
        else:
            mime = req.get("content_type") or "application/octet-stream"
        art = store.put_blob(data, mime=mime)
        state["artifacts"].append({"kind": conf.get("kind", "request_body"), **art, "meta": {}})
    elif "delay" in action:
        conf = action["delay"]
        base = int(conf.get("ms", 0))
        jitter = int(conf.get("jitterMs", 0))
        time.sleep(max(0, (base + random.randint(-jitter, jitter)) / 1000))
    elif "respond" in action:
        state["respond"] = action["respond"]
    elif "drop" in action:
        state["decision"]["dropped"] = True
