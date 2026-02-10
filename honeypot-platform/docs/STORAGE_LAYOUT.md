# Storage Layout

Default root is `./run/artifacts`.

Simple Layout v1 stores data in a single stable directory per honeypot:

```text
<root>/<honeypot_id>/
  index/events.jsonl
  blobs/<sha256_prefix>/<sha256>
  objects/<event_id>/<kind>/<filename>
```

There is no run-isolated `runs/` subtree. A new run for the same honeypot overwrites the previous artifact tree.

## Operational warning
- Do not run two copies of the same honeypot concurrently.
- Clear `<root>/<honeypot_id>/` before starting a new run when you need a clean capture session.
