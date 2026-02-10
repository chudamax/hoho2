# Storage Layout

## Root Structure
Default root is `./run/artifacts`.

### Simple mode (no run id)
Used by low-interaction runtime and `hoho render-compose` without `--run-id`.

```text
<root>/<pack_id>/
  index/events.jsonl
  blobs/<sha256_prefix>/<sha256>
  objects/<event_id>/<kind>/<filename>
```

### Run mode (isolated instances)
Used by `hoho run` for high-interaction packs by default, and by `hoho render-compose --run-id <id>`.

```text
<root>/runs/<run_id>/<pack_id>/
  index/events.jsonl
  blobs/<sha256_prefix>/<sha256>
  objects/<event_id>/<kind>/<filename>
```

Each run gets a unique `<run_id>` directory, so concurrent stacks do not interleave artifacts. Cleanup is straightforward: remove one `runs/<run_id>` directory.

## Blob Dedupe
Blobs are keyed by SHA256 and written once. Repeated payloads map to existing blob paths. `storage_ref` values in events point to the stable blob or object location.

## Event File
`events.jsonl` is append-only and stores one JSON object per line for easy stream processing.

## Object Materialization
`objects/` is reserved for per-event extracted files or metadata sidecars when operators need easier browsing than raw blob references.
