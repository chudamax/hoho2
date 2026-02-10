# DSL Reference

## Matchers
Supported matcher keys in `match`:
- `method`, `path`, `pathGlob`, `pathRegex`
- `headers` and `query` condition maps (`equals`, `contains`, `regex`, `exists`)
- `body` (`contains`, `regex`, optional max byte guard)
- `contentTypeContains`

## Actions
Supported actions:
- `emit_event` for classification values.
- `store_body` to persist request body blobs (optional gzip).
- `store_multipart` (specified in schema; can be expanded in runtime).
- `delay` with optional jitter.
- `set_var` for session/global value templates (future extension target).
- `respond` to construct response.
- `drop` for close/timeout simulation.

## Response and Template Model
Responses support `status`, `headers`, `body`, and `bodyFile`. Template syntax is intentionally minimal (`${req.method}`, `${req.path}`, `${now.iso}`) and does not execute code.

## Safety and Limits
The DSL never runs user-provided code. Size limits and truncation decisions should be recorded in `decision` flags whenever request or artifact size guards are crossed.
