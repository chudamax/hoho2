# Architecture

## Component Overview
The platform is split into a shared core package (`hoho_core`), a runtime package (`hoho_runtime`), sensor images, and YAML packs.

Text diagram:

- Operator writes `packs/*.yaml`.
- `hoho validate` checks the pack against JSONSchema and semantic constraints.
- `hoho run` starts low-interaction HTTP/TCP emulation or renders/runs high-interaction Compose stacks.
- Runtime and sensors write canonical JSONL events plus content-addressed blobs under a shared artifact root.

## Pack to Runtime Flow
Low-interaction packs define listen endpoints and behavior rules. The runtime parses request metadata, evaluates matchers, executes safe actions, selects a response, and emits one canonical event per request.

High-interaction packs define stack services and sensor attachments. Compose rendering injects sensor containers and shared `/artifacts` volume mounts.

## Telemetry and Storage Flow
1. Request/flow/file/pcap segment observed.
2. Metadata sanitized and redacted.
3. Blob content hashed and written to `blobs/<prefix>/<sha256>`.
4. Event record appended to `index/events.jsonl` with artifact references.
5. Optional object materialization can be added under `objects/<event_id>/...` in future versions.
