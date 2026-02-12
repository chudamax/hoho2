# Event Schema v1

## Required Core Fields
Every event includes:
- identity: `schema_version`, `event_id`, `ts`, `pack_id`
- mode: `interaction`, `component`, `proto`
- source: `src` (`ip`, `port`, `forwarded_for`, `user_agent`)
- request/response objects when applicable
- classification (`verdict`, `tags`, `indicators`)
- decision flags (`truncated`, `oversized`, `rate_limited`, `dropped`)
- artifact list with `kind`, hash, size, mime, and `storage_ref`

## Example: Low HTTP Upload
```json
{"schema_version":1,"pack_id":"example-upload-sink","component":"runtime.http","classification":{"verdict":"upload","tags":["multipart"],"indicators":["file-upload"]}}
```

## Example: Proxy Flow
```json
{"schema_version":1,"pack_id":"example-wp-stack","component":"sensor.http_proxy","proto":"http","response":{"status_code":200}}
```

## Example: Filesystem Change
```json
{"schema_version":1,"component":"sensor.fsmon","classification":{"verdict":"postex","tags":["fs_change"],"indicators":["/var/www/html/index.php"]}}
```

## Example: PCAP Rotation
```json
{"schema_version":1,"component":"sensor.pcap","artifacts":[{"kind":"pcap_segment","storage_ref":"blobs/ab/abcdef..."}]}
```


## Example: Falco Alert
```json
{"schema_version":1,"component":"sensor.falco","proto":"runtime","classification":{"verdict":"alert","tags":["falco","priority:Error","rule:Hoho Shell Spawned in Container"]},"falco":{"rule":"Hoho Shell Spawned in Container","priority":"Error","output_fields":{"proc.cmdline":"/bin/sh","container.id":"abcd1234"}}}
```
