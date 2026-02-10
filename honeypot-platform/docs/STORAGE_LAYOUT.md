# Storage Layout

## Root Structure
Default root is `./run/artifacts`.

```text
<root>/<pack_id>/
  index/events.jsonl
  blobs/<sha256_prefix>/<sha256>
  objects/<event_id>/<kind>/<filename>
```

## Blob Dedupe
Blobs are keyed by SHA256 and written once. Repeated payloads map to existing blob paths. `storage_ref` values in events point to the stable blob or object location.

## Event File
`events.jsonl` is append-only and stores one JSON object per line for easy stream processing.

## Object Materialization
`objects/` is reserved for per-event extracted files or metadata sidecars when operators need easier browsing than raw blob references.
