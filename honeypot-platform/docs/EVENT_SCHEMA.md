# Event Schema v2

All telemetry producers emit schema version `2`.

## Required envelope
- `schema_version: 2`
- `event_id`, `ts`
- `honeypot_id`, `session_id`, `agent_id`
- `event_name` (lowercase dotted)
- `action` (optional, hub-derived UI headline; `event_name` remains canonical)
- `component`
- `classification`, `decision`, `artifacts`

`pack_id` may still appear from transitional emitters but should be normalized to `honeypot_id` by downstream consumers.

## Event examples

### `http.request`
```json
{"schema_version":2,"event_name":"http.request","component":"sensor.http_proxy","honeypot_id":"example","session_id":"...","agent_id":"host","request":{"path":"/"}}
```

### `egress.response`
```json
{"schema_version":2,"event_name":"egress.response","component":"sensor.egress_proxy","response":{"status_code":200},"artifacts":[{"kind":"egress.response_body","sha256":"...","size":123,"mime":"application/octet-stream","storage_ref":"blobs/ab/...","meta":{"url":"https://example.com/payload"}}]}
```

### `fs.write`
```json
{"schema_version":2,"event_name":"fs.write","component":"sensor.fsmon","classification":{"verdict":"postex","tags":["fs_change"],"indicators":["/var/www/html/shell.php"]}}
```

### `pcap.segment`
```json
{"schema_version":2,"event_name":"pcap.segment","component":"sensor.pcap","artifacts":[{"kind":"pcap_segment","storage_ref":"blobs/ab/..."}]}
```

### `falco.alert`
```json
{"schema_version":2,"event_name":"falco.alert","component":"sensor.falco","classification":{"verdict":"alert","tags":["falco"]},"falco":{"rule":"..."}}
```

### `runtime.ca_install`
```json
{"schema_version":2,"event_name":"runtime.ca_install","component":"runtime.compose","runtime":{"service":"web","exit_code":0}}
```
