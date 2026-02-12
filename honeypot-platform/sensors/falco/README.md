# Falco Sensor

Falco sensor runs Falco with JSON + program output and forwards alerts into Hoho canonical events under `index/events.jsonl`.

## Environment
- `HOHO_PACK_ID`
- `HOHO_STORAGE_BACKEND=filesystem`
- `HOHO_STORAGE_ROOT=/artifacts`
- `FALCO_PRIORITY_MIN`
- `FALCO_RULES`
- `HOHO_FALCO_ONLY_PROJECT`
- `HOHO_FALCO_PROJECT`
- `HOHO_FALCO_ONLY_SERVICES`
- `HOHO_FALCO_ENFORCE_*`
