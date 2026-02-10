# sensor-http-proxy

Mitmproxy reverse-proxy sensor emitting canonical events and request-body artifacts.

## Runtime Environment Variables
- `UPSTREAM` (default: `http://upstream:80`): reverse proxy target.
- `PROXY_LISTEN_HOST` (default: `0.0.0.0`): bind host for mitmproxy.
- `PROXY_LISTEN_PORT` (default: `8080`): bind port for mitmproxy.
- `PROXY_KEEP_HOST_HEADER` (default: `true`): when truthy (`1`, `true`, `yes`, `on`, case-insensitive), pass the incoming `Host` header upstream.
- `PROXY_EXTRA_ARGS` (default: empty): raw extra CLI args appended to `mitmdump`.

## Redirect Troubleshooting
If clients are redirected to an internal name like `http://web:8088/...`, the upstream app is generating redirects based on the rewritten `Host` header.

This sensor enables mitmproxy `keep_host_header` by default so the upstream sees the original host/port from the client request. To intentionally disable this behavior, set `PROXY_KEEP_HOST_HEADER=false`.
