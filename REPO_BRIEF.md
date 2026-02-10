# Repository Brief: hoho2

_Generated 2026-02-10 11:24 UTC_

## Quick Facts
- **Branch:** main
- **Commit:** 002af03 (2026-02-10 12:05:16 +0100)
- **Total commits:** 3
- **Files scanned:** 65
- **Text files embedded (after filters):** 65

## Language & LOC Overview (approx.)
- **python** — files: 32 (49.2%), LOC: 621
- **md** — files: 15 (23.1%), LOC: 222
- **other** — files: 6 (9.2%), LOC: 229
- **yaml** — files: 4 (6.2%), LOC: 121
- **bash** — files: 4 (6.2%), LOC: 50
- **json** — files: 2 (3.1%), LOC: 37
- **toml** — files: 2 (3.1%), LOC: 26

## Directory Tree (depth ≤ 10)

```text
- .gitignore
- honeypot-platform
  - docs
    - ARCHITECTURE.md
    - DEPLOYMENT.md
    - DSL_REFERENCE.md
    - EVENT_SCHEMA.md
    - PACK_SPEC.md
    - README.md
    - SECURITY.md
    - SENSORS.md
    - STORAGE_LAYOUT.md
  - scripts
    - check_docs.sh
  - deploy
    - compose
      - README.md
  - packages
    - hoho_core
      - pyproject.toml
    - hoho_runtime
  - packs
    - high
      - example_wp_stack.yaml
    - low
      - example_upload_sink.yaml
      - example_web.yaml
  - sensors
    - fsmon
      - Dockerfile
      - entrypoint.sh
    - http_proxy
    - pcap
      - example-wp-stack
        - docker-compose.yml
      - hoho_core
        - __init__.py
        - version.py
      - hoho_runtime
        - cli.py
        - config.py
      - fsmon
        - fsmon.py
        - rules.schema.json
      - proxy
        - capture_addon.py
        - dsl
          - __init__.py
          - actions.py
          - engine.py
          - matchers.py
          - templates.py
        - model
          - artifact.py
          - event.py
        - schema
          - pack_v1.json
          - validate.py
        - storage
          - base.py
          - fs.py
        - utils
          - filenames.py
          - hashing.py
          - jsonl.py
          - redact.py
          - time.py
        - orchestration
          - compose_render.py
          - compose_run.py
        - server
          - http.py
          - tcp.py
  - run
    - artifacts
      - example-upload-sink
        - index
          - events.jsonl
      - example-web
```

## Recent Commits
- 002af03 | 2026-02-10 | Merge pull request #1 from chudamax/codex/create-yaml-first-honeypot-platform
- d757b05 | 2026-02-10 | Remove generated artifact blob from repository
- c6f004d | 2026-02-10 | Initial commit

## Files (embedded, trimmed)
> Secret-looking lines are redacted by default. Large files are truncated to stay within budgets.

### `.gitignore`  _(~4.6 KB; showing ≤800 lines)_
```
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[codz]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py.cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# UV
#   Similar to Pipfile.lock, it is generally recommended to include uv.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#uv.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock
#poetry.toml

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#   pdm recommends including project-wide configuration in pdm.toml, but excluding .pdm-python.
#   https://pdm-project.org/en/latest/usage/project/#working-with-version-control
#pdm.lock
#pdm.toml
.pdm-python
.pdm-build/

# pixi
#   Similar to Pipfile.lock, it is generally recommended to include pixi.lock in version control.
#pixi.lock
#   Pixi creates a virtual environment in the .pixi directory, just like venv module creates one
#   in the .venv directory. It is recommended not to include this directory in version control.
.pixi

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.envrc
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/

# Abstra
# Abstra is an AI-powered process automation framework.
# Ignore directories containing user credentials, local state, and settings.
# Learn more at https://abstra.io/docs
.abstra/

# Visual Studio Code
#  Visual Studio Code specific template is maintained in a separate VisualStudioCode.gitignore 
#  that can be found at https://github.com/github/gitignore/blob/main/Global/VisualStudioCode.gitignore
#  and can be added to the global gitignore or merged into this file. However, if you prefer, 
#  you could uncomment the following to ignore the entire vscode folder
# .vscode/

# Ruff stuff:
.ruff_cache/

# PyPI configuration file
.pypirc

# Cursor
#  Cursor is an AI-powered code editor. `.cursorignore` specifies files/directories to
#  exclude from AI features like autocomplete and code analysis. Recommended for sensitive data
#  refer to https://docs.cursor.com/context/ignore-files
.cursorignore
.cursorindexingignore

# Marimo
marimo/_static/
marimo/_lsp/
__marimo__/
```

### `honeypot-platform/deploy/compose/README.md`  _(~0.1 KB; showing ≤800 lines)_
```md
# Rendered Compose Output

`hoho render-compose` writes generated Compose bundles into this tree by pack identifier.
```

### `honeypot-platform/deploy/compose/example-wp-stack/docker-compose.yml`  _(~0.8 KB; showing ≤800 lines)_
```yaml
version: "3.9"
services:
  web:
    image: "nginx:alpine"
    ports:
      - 8088:80
    volumes:
      - webdata:/var/www/html
    networks:
      - frontend
  proxy-sensor:
    image: "hoho/sensor-http-proxy:latest"
    environment:
      HOHO_PACK_ID: example-wp-stack
      HOHO_STORAGE_BACKEND: filesystem
      HOHO_STORAGE_ROOT: /artifacts
    volumes:
      - artifacts:/artifacts
  fsmon-sensor:
    image: "hoho/sensor-fsmon:latest"
    environment:
      HOHO_PACK_ID: example-wp-stack
      HOHO_STORAGE_BACKEND: filesystem
      HOHO_STORAGE_ROOT: /artifacts
    volumes:
      - artifacts:/artifacts
  pcap-sensor:
    image: "hoho/sensor-pcap:latest"
    environment:
      HOHO_PACK_ID: example-wp-stack
      HOHO_STORAGE_BACKEND: filesystem
      HOHO_STORAGE_ROOT: /artifacts
    volumes:
      - artifacts:/artifacts
volumes:
  artifacts:
```

### `honeypot-platform/docs/ARCHITECTURE.md`  _(~1.2 KB; showing ≤800 lines)_
```md
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
```

### `honeypot-platform/docs/DEPLOYMENT.md`  _(~0.8 KB; showing ≤800 lines)_
```md
# Deployment

## Quickstart: Low-Interaction Pack
1. Validate pack:
   - `hoho validate packs/low/example_web.yaml`
2. Run runtime:
   - `hoho run packs/low/example_web.yaml`
3. Send traffic to configured listen port.
4. Inspect `run/artifacts/<pack_id>/index/events.jsonl` and `blobs/`.

## Quickstart: High-Interaction Pack
1. Validate pack.
2. Render compose bundle:
   - `hoho render-compose packs/high/example_wp_stack.yaml`
3. Optionally start stack:
   - `docker compose -f deploy/compose/example-wp-stack/docker-compose.yml up`

## Recommended Isolation
- Use dedicated network segments for honeypot exposure.
- Restrict outbound egress from honeypot and sensor networks.
- Run with non-privileged users wherever possible.
- Mount artifact storage on isolated volumes with monitoring.
```

### `honeypot-platform/docs/DSL_REFERENCE.md`  _(~1.0 KB; showing ≤800 lines)_
```md
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
```

### `honeypot-platform/docs/EVENT_SCHEMA.md`  _(~1.2 KB; showing ≤800 lines)_
```md
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
```

### `honeypot-platform/docs/PACK_SPEC.md`  _(~1.1 KB; showing ≤800 lines)_
```md
# Pack Specification (v1)

## Common Top-Level Fields
- `apiVersion`: must be `hoho.dev/v1`.
- `kind`: must be `HoneypotPack`.
- `metadata`: includes `id`, `name`, `interaction`, `tags`, and `description`.
- `storage`: currently `backend: filesystem` and `root` path.
- `limits`: `max_body_bytes`, `max_upload_bytes`, and `max_artifacts_per_request`.
- `telemetry`: `emit_events`, `redact_headers`, and optional query redaction list.

## Low-Interaction Fields
- `listen`: list of `{host, port}` entries.
- `responses`: optional reusable response templates.
- `behaviors`: ordered rules with `name`, `match`, `actions`, and optional `respond`.

## High-Interaction Fields
- `stack.runtime`: `compose` for v1.
- `stack.services`: compose-like service map (`image/build`, environment, volumes, networks, ports).
- `sensors`: shared sensor descriptors with `name`, `type`, `config`, and `attach` mapping.
- `expose`: optional shortcut metadata for published ports.

## Validation Rules
Schema validation enforces required fields and interaction mode options. Semantic checks ensure low packs include behaviors and high packs include a stack section.
```

### `honeypot-platform/docs/README.md`  _(~0.2 KB; showing ≤800 lines)_
```md
# Honeypot Platform Documentation

This directory contains architecture, specification, sensor, storage, deployment, and security guidance for the YAML-first honeypot platform.
```

### `honeypot-platform/docs/SECURITY.md`  _(~0.7 KB; showing ≤800 lines)_
```md
# Security

## Core Safety Statement
Captured payloads are treated as opaque bytes. The platform never executes, imports, or opens uploaded content as code.

## Safe Malware Handling
- Keep artifacts in isolated storage.
- Do not double-click or run captured binaries/scripts.
- Use offline analysis environments with strict controls.
- Preserve hashes and metadata for chain-of-custody.

## Network and Host Isolation
- Place honeypots in dedicated VLAN/VPC segments.
- Enforce firewall egress controls.
- Limit sensor and runtime privileges.
- Keep host patching and logging up to date.

## Operational Hardening
- Enable strict size limits to reduce resource abuse.
- Redact sensitive headers by default.
- Avoid shelling out with untrusted input.
```

### `honeypot-platform/docs/SENSORS.md`  _(~1.2 KB; showing ≤800 lines)_
```md
# Sensors

## Shared Contract
All sensors read common environment variables:
- `HOHO_PACK_ID`
- `HOHO_STORAGE_BACKEND=filesystem`
- `HOHO_STORAGE_ROOT=/artifacts`
- `HOHO_EMIT_EVENTS=1`
- `HOHO_REDACT_HEADERS=[REDACTED]

All sensors append canonical events to `<root>/<pack_id>/index/events.jsonl` and write artifacts as content-addressed blobs.

## HTTP Proxy Sensor
- Built on mitmproxy reverse mode (`--mode reverse:<upstream>`).
- Captures request/response metadata and request body artifacts.
- Supports deployment as sidecar in front of a target web service.

Compose snippet:
```yaml
proxy-sensor:
  image: hoho/sensor-http-proxy:latest
  environment:
    HOHO_PACK_ID: example
  volumes: ["artifacts:/artifacts"]
```

## Filesystem Monitor Sensor
- Watches configured directories for create/modify events.
- Applies allow/deny glob filters.
- Stores changed file content up to a cap and records preview text.

## PCAP Sensor
- Uses tcpdump with rotation controls (`-G`, `-W`, optional `-C`).
- Stores rotated pcap files as blob artifacts and emits `pcap_segment` events.

## Operational Notes
Disk usage can grow quickly from uploads and pcap segments. Use external rotation, retention cleanup, and dedicated storage volumes.
```

### `honeypot-platform/docs/STORAGE_LAYOUT.md`  _(~0.6 KB; showing ≤800 lines)_
```md
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
```

### `honeypot-platform/packages/hoho_core/README.md`  _(~0.1 KB; showing ≤800 lines)_
```md
# hoho_core

Shared core primitives for pack validation, event modeling, DSL evaluation, and filesystem artifact storage.
```

### `honeypot-platform/packages/hoho_core/hoho_core/__init__.py`  _(~0.1 KB; showing ≤800 lines)_
```python
from .version import __version__

__all__ = ["__version__"]
```

### `honeypot-platform/packages/hoho_core/hoho_core/dsl/__init__.py`  _(~0.1 KB; showing ≤800 lines)_
```python
from .engine import evaluate_rules

__all__ = ["evaluate_rules"]
```

### `honeypot-platform/packages/hoho_core/hoho_core/dsl/actions.py`  _(~1.3 KB; showing ≤800 lines)_
```python
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
```

### `honeypot-platform/packages/hoho_core/hoho_core/dsl/engine.py`  _(~0.6 KB; showing ≤800 lines)_
```python
from hoho_core.dsl.matchers import match_rule
from hoho_core.dsl.actions import run_action


def evaluate_rules(behaviors: list[dict], req: dict, store, event: dict) -> dict:
    state = {
        "classification": event["classification"],
        "decision": event["decision"],
        "artifacts": event["artifacts"],
        "respond": None,
    }
    for rule in behaviors:
        if match_rule(rule, req):
            for action in rule.get("actions", []):
                run_action(action, state, req, store)
            if rule.get("respond"):
                state["respond"] = rule["respond"]
            break
    return state
```

### `honeypot-platform/packages/hoho_core/hoho_core/dsl/matchers.py`  _(~1.6 KB; showing ≤800 lines)_
```python
import fnmatch
import re


def _match_value(value: str, cond: dict) -> bool:
    if "equals" in cond:
        return value == cond["equals"]
    if "contains" in cond:
        return cond["contains"] in value
    if "regex" in cond:
        return re.search(cond["regex"], value or "") is not None
    if cond.get("exists") is True:
        return bool(value)
    return False


def match_rule(rule: dict, req: dict) -> bool:
    m = rule.get("match", {})
    method = m.get("method")
    if method:
        allowed = method if isinstance(method, list) else [method]
        if req.get("method") not in allowed:
            return False
    if "path" in m and req.get("path") != m["path"]:
        return False
    if "pathGlob" in m and not fnmatch.fnmatch(req.get("path", ""), m["pathGlob"]):
        return False
    if "pathRegex" in m and re.search(m["pathRegex"], req.get("path", "")) is None:
        return False
    for hk, cond in m.get("headers", {}).items():
        if not _match_value(req.get("headers", {}).get(hk, ""), cond):
            return False
    for qk, cond in m.get("query", {}).items():
        if not _match_value(req.get("query", {}).get(qk, ""), cond):
            return False
    body = req.get("body", b"")
    body_text = body.decode("utf-8", errors="ignore")
    body_match = m.get("body", {})
    if "contains" in body_match and body_match["contains"] not in body_text:
        return False
    if "regex" in body_match and re.search(body_match["regex"], body_text) is None:
        return False
    if "contentTypeContains" in m and m["contentTypeContains"] not in req.get("content_type", ""):
        return False
    return True
```

### `honeypot-platform/packages/hoho_core/hoho_core/dsl/templates.py`  _(~0.4 KB; showing ≤800 lines)_
```python
from hoho_core.utils.time import utc_iso


def render_template(template: str, ctx: dict) -> str:
    out = template
    replacements = {
        "${req.method}": ctx.get("req", {}).get("method", ""),
        "${req.path}": ctx.get("req", {}).get("path", ""),
        "${now.iso}": utc_iso(),
    }
    for key, value in replacements.items():
        out = out.replace(key, str(value))
    return out
```

### `honeypot-platform/packages/hoho_core/hoho_core/model/__init__.py`  _(~0.1 KB; showing ≤800 lines)_
```python
from .event import build_base_event
from .artifact import ArtifactRef

__all__ = ["build_base_event", "ArtifactRef"]
```

### `honeypot-platform/packages/hoho_core/hoho_core/model/artifact.py`  _(~0.4 KB; showing ≤800 lines)_
```python
from dataclasses import dataclass, field


@dataclass
class ArtifactRef:
    kind: str
    sha256: str
    size: int
    mime: str
    storage_ref: str
    meta: dict = field(default_factory=dict)

    def as_dict(self) -> dict:
        return {
            "kind": self.kind,
            "sha256": self.sha256,
            "size": self.size,
            "mime": self.mime,
            "storage_ref": self.storage_ref,
            "meta": self.meta,
        }
```

### `honeypot-platform/packages/hoho_core/hoho_core/model/event.py`  _(~0.8 KB; showing ≤800 lines)_
```python
import uuid
from hoho_core.utils.time import utc_iso


def build_base_event(pack_id: str, interaction: str, component: str, proto: str) -> dict:
    return {
        "schema_version": 1,
        "event_id": str(uuid.uuid4()),
        "ts": utc_iso(),
        "pack_id": pack_id,
        "interaction": interaction,
        "component": component,
        "src": {"ip": None, "port": None, "forwarded_for": [], "user_agent": None},
        "proto": proto,
        "request": {},
        "response": {"status_code": None, "bytes_sent": 0, "profile": None},
        "classification": {"verdict": "unknown", "tags": [], "indicators": []},
        "decision": {"truncated": False, "oversized": False, "rate_limited": False, "dropped": False},
        "artifacts": [],
    }
```

### `honeypot-platform/packages/hoho_core/hoho_core/schema/__init__.py`  _(~0.1 KB; showing ≤800 lines)_
```python
from .validate import validate_pack

__all__ = ["validate_pack"]
```

### `honeypot-platform/packages/hoho_core/hoho_core/schema/pack_v1.json`  _(~0.9 KB; showing ≤800 lines)_
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": ["apiVersion", "kind", "metadata"],
  "properties": {
    "apiVersion": {"const": "hoho.dev/v1"},
    "kind": {"const": "HoneypotPack"},
    "metadata": {
      "type": "object",
      "required": ["id", "name", "interaction", "description"],
      "properties": {
        "id": {"type": "string", "minLength": 1},
        "name": {"type": "string"},
        "interaction": {"enum": ["low", "high"]},
        "tags": {"type": "array", "items": {"type": "string"}},
        "description": {"type": "string"}
      }
    },
    "storage": {"type": "object"},
    "limits": {"type": "object"},
    "telemetry": {"type": "object"},
    "listen": {"type": "array"},
    "responses": {"type": "object"},
    "behaviors": {"type": "array"},
    "stack": {"type": "object"},
    "sensors": {"type": "array"}
  }
}
```

### `honeypot-platform/packages/hoho_core/hoho_core/schema/validate.py`  _(~1.1 KB; showing ≤800 lines)_
```python
import json


def load_pack(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise ValueError(f"pack parsing error: only JSON-compatible YAML is supported in this environment ({exc})")


def validate_pack(pack: dict) -> list[str]:
    out: list[str] = []
    if pack.get("apiVersion") != "hoho.dev/v1":
        out.append("apiVersion must be hoho.dev/v1")
    if pack.get("kind") != "HoneypotPack":
        out.append("kind must be HoneypotPack")

    md = pack.get("metadata", {})
    for req in ["id", "name", "interaction", "description"]:
        if not md.get(req):
            out.append(f"metadata.{req} is required")
    if md.get("interaction") not in {"low", "high"}:
        out.append("metadata.interaction must be low or high")

    interaction = md.get("interaction")
    if interaction == "low" and "behaviors" not in pack:
        out.append("low interaction pack requires behaviors")
    if interaction == "high" and "stack" not in pack:
        out.append("high interaction pack requires stack")
    return out
```

### `honeypot-platform/packages/hoho_core/hoho_core/storage/__init__.py`  _(~0.1 KB; showing ≤800 lines)_
```python
from .base import ArtifactStore
from .fs import FilesystemArtifactStore

__all__ = ["ArtifactStore", "FilesystemArtifactStore"]
```

### `honeypot-platform/packages/hoho_core/hoho_core/storage/base.py`  _(~0.3 KB; showing ≤800 lines)_
```python
from abc import ABC, abstractmethod


class ArtifactStore(ABC):
    @abstractmethod
    def put_blob(self, data: bytes, mime: str = "application/octet-stream") -> dict:
        raise NotImplementedError

    @abstractmethod
    def append_event(self, pack_id: str, event: dict) -> None:
        raise NotImplementedError
```

### `honeypot-platform/packages/hoho_core/hoho_core/storage/fs.py`  _(~1.0 KB; showing ≤800 lines)_
```python
from pathlib import Path
from hoho_core.storage.base import ArtifactStore
from hoho_core.utils.hashing import sha256_bytes
from hoho_core.utils.jsonl import append_jsonl


class FilesystemArtifactStore(ArtifactStore):
    def __init__(self, root: str, pack_id: str):
        self.root = Path(root)
        self.pack_id = pack_id
        self.pack_root = self.root / pack_id

    def put_blob(self, data: bytes, mime: str = "application/octet-stream") -> dict:
        digest = sha256_bytes(data)
        prefix = digest[:2]
        blob_path = self.pack_root / "blobs" / prefix / digest
        blob_path.parent.mkdir(parents=True, exist_ok=True)
        if not blob_path.exists():
            blob_path.write_bytes(data)
        return {
            "sha256": digest,
            "size": len(data),
            "mime": mime,
            "storage_ref": str(blob_path.relative_to(self.pack_root)),
        }

    def append_event(self, pack_id: str, event: dict) -> None:
        append_jsonl(self.root / pack_id / "index" / "events.jsonl", event)
```

### `honeypot-platform/packages/hoho_core/hoho_core/utils/__init__.py`  _(~0.0 KB; showing ≤800 lines)_
```python

```

### `honeypot-platform/packages/hoho_core/hoho_core/utils/filenames.py`  _(~0.1 KB; showing ≤800 lines)_
```python
import re


def safe_filename(name: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]", "_", name)
```

### `honeypot-platform/packages/hoho_core/hoho_core/utils/hashing.py`  _(~0.1 KB; showing ≤800 lines)_
```python
import hashlib


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()
```

### `honeypot-platform/packages/hoho_core/hoho_core/utils/jsonl.py`  _(~0.2 KB; showing ≤800 lines)_
```python
import json
from pathlib import Path


def append_jsonl(path: Path, record: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, separators=(",", ":")) + "\n")
```

### `honeypot-platform/packages/hoho_core/hoho_core/utils/redact.py`  _(~0.4 KB; showing ≤800 lines)_
```python
from typing import Mapping

DEFAULT_REDACT_HEADERS =[REDACTED]


def redact_headers(headers: Mapping[str, str], redact_list: list[str] | None = None) -> dict[str, str]:
    targets = {h.lower() for h in (redact_list or [])} | DEFAULT_REDACT_HEADERS
    out: dict[str, str] = {}
    for k, v in headers.items():
        out[k] = "<redacted>" if k.lower() in targets else v
    return out
```

### `honeypot-platform/packages/hoho_core/hoho_core/utils/time.py`  _(~0.1 KB; showing ≤800 lines)_
```python
from datetime import datetime, timezone


def utc_iso() -> str:
    return datetime.now(timezone.utc).isoformat()
```

### `honeypot-platform/packages/hoho_core/hoho_core/version.py`  _(~0.0 KB; showing ≤800 lines)_
```python
__version__ = "0.1.0"
```

### `honeypot-platform/packages/hoho_core/pyproject.toml`  _(~0.2 KB; showing ≤800 lines)_
```toml
[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "hoho-core"
version = "0.1.0"

[tool.setuptools.packages.find]
where = ["."]
include = ["hoho_core*"]
```

### `honeypot-platform/packages/hoho_runtime/README.md`  _(~0.1 KB; showing ≤800 lines)_
```md
# hoho_runtime

CLI and runtime components for low-interaction serving and high-interaction compose orchestration.
```

### `honeypot-platform/packages/hoho_runtime/hoho_runtime/__init__.py`  _(~0.0 KB; showing ≤800 lines)_
```python

```

### `honeypot-platform/packages/hoho_runtime/hoho_runtime/cli.py`  _(~2.1 KB; showing ≤800 lines)_
```python
import argparse
import json
from hoho_core.schema.validate import load_pack, validate_pack
from hoho_runtime.server.http import run_low_http
from hoho_runtime.orchestration.compose_render import render_compose
from hoho_runtime.orchestration.compose_run import run_compose


def cmd_validate(args):
    pack = load_pack(args.pack)
    errors = validate_pack(pack)
    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        raise SystemExit(1)
    print("valid")


def cmd_render_compose(args):
    pack = load_pack(args.pack)
    out = render_compose(pack, args.output)
    print(out)


def cmd_run(args):
    pack = load_pack(args.pack)
    if pack["metadata"]["interaction"] == "low":
        run_low_http(pack)
    else:
        compose_file = render_compose(pack)
        if args.no_up:
            print(compose_file)
        else:
            raise SystemExit(run_compose(compose_file))


def cmd_explain(args):
    pack = load_pack(args.pack)
    plan = {
        "pack_id": pack["metadata"]["id"],
        "interaction": pack["metadata"]["interaction"],
        "listen": pack.get("listen", []),
        "limits": pack.get("limits", {}),
        "storage_root": pack.get("storage", {}).get("root", "./run/artifacts"),
        "sensors": pack.get("sensors", []),
    }
    print(json.dumps(plan, indent=2))


def main():
    parser = argparse.ArgumentParser(prog="hoho")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_val = sub.add_parser("validate")
    p_val.add_argument("pack")
    p_val.set_defaults(func=cmd_validate)

    p_run = sub.add_parser("run")
    p_run.add_argument("pack")
    p_run.add_argument("--no-up", action="store_true")
    p_run.set_defaults(func=cmd_run)

    p_rc = sub.add_parser("render-compose")
    p_rc.add_argument("pack")
    p_rc.add_argument("-o", "--output", default=None)
    p_rc.set_defaults(func=cmd_render_compose)

    p_ex = sub.add_parser("explain")
    p_ex.add_argument("pack")
    p_ex.set_defaults(func=cmd_explain)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
```

### `honeypot-platform/packages/hoho_runtime/hoho_runtime/config.py`  _(~0.2 KB; showing ≤800 lines)_
```python
DEFAULT_STORAGE_ROOT = "./run/artifacts"
DEFAULT_LIMITS = {
    "max_body_bytes": 1048576,
    "max_upload_bytes": 10485760,
    "max_artifacts_per_request": 5,
}
```

### `honeypot-platform/packages/hoho_runtime/hoho_runtime/orchestration/__init__.py`  _(~0.0 KB; showing ≤800 lines)_
```python

```

### `honeypot-platform/packages/hoho_runtime/hoho_runtime/orchestration/compose_render.py`  _(~1.9 KB; showing ≤800 lines)_
```python
from pathlib import Path


def _to_yaml(obj, indent=0):
    sp = "  " * indent
    if isinstance(obj, dict):
        lines = []
        for k, v in obj.items():
            if isinstance(v, (dict, list)):
                lines.append(f"{sp}{k}:")
                lines.append(_to_yaml(v, indent + 1))
            else:
                if isinstance(v, str) and any(c in v for c in [":", "#", "{"]):
                    v = f'"{v}"'
                lines.append(f"{sp}{k}: {v}")
        return "\n".join(lines)
    if isinstance(obj, list):
        lines = []
        for item in obj:
            if isinstance(item, (dict, list)):
                lines.append(f"{sp}-")
                lines.append(_to_yaml(item, indent + 1))
            else:
                lines.append(f"{sp}- {item}")
        return "\n".join(lines)
    return f"{sp}{obj}"


def render_compose(pack: dict, out_dir: str | None = None) -> Path:
    pack_id = pack["metadata"]["id"]
    root = Path(out_dir or f"./deploy/compose/{pack_id}")
    root.mkdir(parents=True, exist_ok=True)
    services = dict(pack.get("stack", {}).get("services", {}))

    for sensor in pack.get("sensors", []):
        sname = sensor["name"]
        stype = sensor["type"]
        image_map = {
            "proxy": "hoho/sensor-http-proxy:latest",
            "fsmon": "hoho/sensor-fsmon:latest",
            "pcap": "hoho/sensor-pcap:latest",
        }
        services[sname] = {
            "image": image_map.get(stype, "busybox:latest"),
            "environment": {
                "HOHO_PACK_ID": pack_id,
                "HOHO_STORAGE_BACKEND": "filesystem",
                "HOHO_STORAGE_ROOT": "/artifacts",
            },
            "volumes": ["artifacts:/artifacts"],
        }
    compose = {"version": "3.9", "services": services, "volumes": {"artifacts": {}}}
    out = root / "docker-compose.yml"
    out.write_text(_to_yaml(compose) + "\n", encoding="utf-8")
    return out
```

### `honeypot-platform/packages/hoho_runtime/hoho_runtime/orchestration/compose_run.py`  _(~0.2 KB; showing ≤800 lines)_
```python
import subprocess
from pathlib import Path


def run_compose(compose_file: Path) -> int:
    return subprocess.call(["docker", "compose", "-f", str(compose_file), "up"])
```

### `honeypot-platform/packages/hoho_runtime/hoho_runtime/server/__init__.py`  _(~0.0 KB; showing ≤800 lines)_
```python

```

### `honeypot-platform/packages/hoho_runtime/hoho_runtime/server/http.py`  _(~2.8 KB; showing ≤800 lines)_
```python
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs
from hoho_core.dsl.engine import evaluate_rules
from hoho_core.model.event import build_base_event
from hoho_core.storage.fs import FilesystemArtifactStore
from hoho_core.utils.redact import redact_headers


class LowInteractionHandler(BaseHTTPRequestHandler):
    pack = None
    store = None

    def _handle(self):
        length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(length) if length else b""
        parsed = urlparse(self.path)
        req = {
            "method": self.command,
            "path": parsed.path,
            "query": {k: v[0] for k, v in parse_qs(parsed.query).items()},
            "headers": {k: v for k, v in self.headers.items()},
            "body": body,
            "content_type": self.headers.get("Content-Type", ""),
        }
        event = build_base_event(self.pack["metadata"]["id"], "low", "runtime.http", "http")
        event["src"]["ip"] = self.client_address[0]
        event["src"]["port"] = self.client_address[1]
        event["src"]["user_agent"] = self.headers.get("User-Agent")
        event["request"] = {
            "method": self.command,
            "path": parsed.path,
            "query": req["query"],
            "headers_redacted": redact_headers(req["headers"], self.pack.get("telemetry", {}).get("redact_headers")),
            "content_type": req["content_type"],
            "content_length": len(body),
        }
        state = evaluate_rules(self.pack.get("behaviors", []), req, self.store, event)
        resp = state.get("respond") or {"status": 404, "headers": {}, "body": "not found"}
        self.send_response(resp.get("status", 200))
        for k, v in resp.get("headers", {}).items():
            self.send_header(k, v)
        self.end_headers()
        body_out = resp.get("body", "").encode()
        self.wfile.write(body_out)
        event["response"]["status_code"] = resp.get("status", 200)
        event["response"]["bytes_sent"] = len(body_out)
        self.store.append_event(self.pack["metadata"]["id"], event)

    do_GET = _handle
    do_POST = _handle
    do_PUT = _handle
    do_DELETE = _handle


def run_low_http(pack: dict) -> None:
    listen = (pack.get("listen") or [{"host": "0.0.0.0", "port": 8080}])[0]
    store = FilesystemArtifactStore(pack.get("storage", {}).get("root", "./run/artifacts"), pack["metadata"]["id"])
    handler = type("BoundHandler", (LowInteractionHandler,), {"pack": pack, "store": store})
    server = ThreadingHTTPServer((listen.get("host", "0.0.0.0"), int(listen.get("port", 8080))), handler)
    print(json.dumps({"status": "listening", "host": listen.get("host", "0.0.0.0"), "port": listen.get("port", 8080)}))
    server.serve_forever()
```

### `honeypot-platform/packages/hoho_runtime/hoho_runtime/server/tcp.py`  _(~0.4 KB; showing ≤800 lines)_
```python
import socket
import threading


def run_tcp_banner(host: str, port: int, banner: str) -> None:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(5)

    def loop():
        while True:
            conn, _ = sock.accept()
            conn.sendall(banner.encode())
            conn.close()

    threading.Thread(target=loop, daemon=True).start()
```

### `honeypot-platform/packages/hoho_runtime/pyproject.toml`  _(~0.3 KB; showing ≤800 lines)_
```toml
[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "hoho-runtime"
version = "0.1.0"
dependencies = ["hoho-core"]

[project.scripts]
hoho = "hoho_runtime.cli:main"

[tool.setuptools.packages.find]
where = ["."]
include = ["hoho_runtime*"]
```

### `honeypot-platform/packs/high/example_wp_stack.yaml`  _(~1.0 KB; showing ≤800 lines)_
```yaml
{
  "apiVersion": "hoho.dev/v1",
  "kind": "HoneypotPack",
  "metadata": {
    "id": "example-wp-stack",
    "name": "Example High-Interaction Web Stack",
    "interaction": "high",
    "tags": ["web", "stack"],
    "description": "Generic web stack placeholder with shared sensors."
  },
  "storage": {"backend": "filesystem", "root": "./run/artifacts"},
  "telemetry": [REDACTED]
  "stack": {
    "runtime": "compose",
    "services": {
      "web": {
        "image": "nginx:alpine",
        "ports": ["8088:80"],
        "volumes": ["webdata:/var/www/html"],
        "networks": ["frontend"]
      }
    }
  },
  "sensors": [
    {"name": "proxy-sensor", "type": "proxy", "config": {"upstream": "http://web:80"}, "attach": {"service": "web"}},
    {"name": "fsmon-sensor", "type": "fsmon", "config": {"watch": ["/var/www/html"]}, "attach": {"service": "web"}},
    {"name": "pcap-sensor", "type": "pcap", "config": {"interface": "any"}, "attach": {"network": "frontend"}}
  ]
}
```

### `honeypot-platform/packs/low/example_upload_sink.yaml`  _(~1.0 KB; showing ≤800 lines)_
```yaml
{
  "apiVersion": "hoho.dev/v1",
  "kind": "HoneypotPack",
  "metadata": {
    "id": "example-upload-sink",
    "name": "Upload Sink Honeypot",
    "interaction": "low",
    "tags": ["upload", "api"],
    "description": "Accepts multipart and stores uploads as artifacts."
  },
  "storage": {"backend": "filesystem", "root": "./run/artifacts"},
  "limits": {"max_body_bytes": 2097152, "max_upload_bytes": 10485760, "max_artifacts_per_request": 5},
  "telemetry": [REDACTED]
  "listen": [{"host": "0.0.0.0", "port": 8081}],
  "behaviors": [
    {
      "name": "upload-api",
      "match": {"method": "POST", "path": "/api/upload", "contentTypeContains": "multipart/form-data"},
      "actions": [
        {"emit_event": {"verdict": "upload", "tags": ["multipart"], "indicators": ["file-upload"]}},
        {"store_body": {"kind": "request_body", "gzip": true}},
        {"respond": {"status": 201, "headers": {"Content-Type": "application/json"}, "body": "{\"ok\":true,\"id\":\"fake-123\"}"}}
      ]
    }
  ]
}
```

### `honeypot-platform/packs/low/example_web.yaml`  _(~1.2 KB; showing ≤800 lines)_
```yaml
{
  "apiVersion": "hoho.dev/v1",
  "kind": "HoneypotPack",
  "metadata": {
    "id": "example-web",
    "name": "Example Web Honeypot",
    "interaction": "low",
    "tags": ["web", "probe"],
    "description": "Basic web decoy with fake server banner."
  },
  "storage": {"backend": "filesystem", "root": "./run/artifacts"},
  "limits": {"max_body_bytes": 1048576, "max_upload_bytes": 10485760, "max_artifacts_per_request": 3},
  "telemetry": [REDACTED]
  "listen": [{"host": "0.0.0.0", "port": 8088}],
  "behaviors": [
    {
      "name": "root-page",
      "match": {"method": "GET", "path": "/"},
      "actions": [{"emit_event": {"verdict": "probe", "tags": ["landing"], "indicators": []}}],
      "respond": {"status": 200, "headers": {"Content-Type": "text/html", "Server": "Apache/2.4.41"}, "body": "<html><body><h1>It works</h1></body></html>"}
    },
    {
      "name": "admin-probe",
      "match": {"pathGlob": "/admin*"},
      "actions": [{"emit_event": {"verdict": "exploit", "tags": ["admin-probe"], "indicators": ["admin-path"]}}],
      "respond": {"status": 403, "headers": {"Content-Type": "text/plain"}, "body": "forbidden"}
    }
  ]
}
```

### `honeypot-platform/run/artifacts/example-upload-sink/index/events.jsonl`  _(~1.1 KB; showing ≤800 lines)_
```
{"schema_version":1,"event_id":"61dfc609-6a77-4a20-8697-1fae4c7a97cc","ts":"2026-02-10T10:59:45.779097+00:00","pack_id":"example-upload-sink","interaction":"low","component":"runtime.http","src":{"ip":"127.0.0.1","port":58474,"forwarded_for":[],"user_agent":"curl/8.5.0"},"proto":"http","request":{"method":"POST","path":"/api/upload","query":{},"headers_redacted":{"Host":"127.0.0.1:8081","User-Agent":"curl/8.5.0","Accept":"*/*","Content-Length":"335","Content-Type":"multipart/form-data; boundary=------------------------lJfSta67QKjFM4bQe7rGeN"},"content_type":"multipart/form-data; boundary=------------------------lJfSta67QKjFM4bQe7rGeN","content_length":335},"response":{"status_code":201,"bytes_sent":27,"profile":null},"classification":{"verdict":"upload","tags":["multipart"],"indicators":["file-upload"]},"decision":{"truncated":false,"oversized":false,"rate_limited":false,"dropped":false},"artifacts":[{"kind":"request_body","sha256":"1a939cffc5e1f8abf5bbda975b4b012eb5f2543f455261dce84aa611d2479073","size":230,"mime":"application/gzip","storage_ref":"blobs/1a/1a939cffc5e1f8abf5bbda975b4b012eb5f2543f455261dce84aa611d2479073","meta":{}}]}
```

### `honeypot-platform/run/artifacts/example-web/index/events.jsonl`  _(~3.5 KB; showing ≤800 lines)_
```
{"schema_version":1,"event_id":"33fc0764-0135-47cb-b35e-592d0e51d345","ts":"2026-02-10T11:18:36.099237+00:00","pack_id":"example-web","interaction":"low","component":"runtime.http","src":{"ip":"192.168.0.59","port":60372,"forwarded_for":[],"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"},"proto":"http","request":{"method":"GET","path":"/","query":{},"headers_redacted":{"Host":"192.168.0.21:8088","Connection":"keep-alive","DNT":"1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate","Accept-Language":"en,ru;q=0.9,en-US;q=0.8,zh-CN;q=0.7,zh;q=0.6","Cookie":"<redacted>"},"content_type":"","content_length":0},"response":{"status_code":200,"bytes_sent":43,"profile":null},"classification":{"verdict":"probe","tags":["landing"],"indicators":[]},"decision":{"truncated":false,"oversized":false,"rate_limited":false,"dropped":false},"artifacts":[]}
{"schema_version":1,"event_id":"0663755a-c94c-49fe-b8cc-0f763f513cfe","ts":"2026-02-10T11:18:36.132115+00:00","pack_id":"example-web","interaction":"low","component":"runtime.http","src":{"ip":"192.168.0.59","port":51292,"forwarded_for":[],"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"},"proto":"http","request":{"method":"GET","path":"/favicon.ico","query":{},"headers_redacted":{"Host":"192.168.0.21:8088","Connection":"keep-alive","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36","DNT":"1","Accept":"image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8","Referer":"http://192.168.0.21:8088/","Accept-Encoding":"gzip, deflate","Accept-Language":"en,ru;q=0.9,en-US;q=0.8,zh-CN;q=0.7,zh;q=0.6","Cookie":"<redacted>"},"content_type":"","content_length":0},"response":{"status_code":404,"bytes_sent":9,"profile":null},"classification":{"verdict":"unknown","tags":[],"indicators":[]},"decision":{"truncated":false,"oversized":false,"rate_limited":false,"dropped":false},"artifacts":[]}
{"schema_version":1,"event_id":"84899a61-e277-4e42-aa42-3880b5e0af30","ts":"2026-02-10T11:18:39.064558+00:00","pack_id":"example-web","interaction":"low","component":"runtime.http","src":{"ip":"192.168.0.59","port":52784,"forwarded_for":[],"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"},"proto":"http","request":{"method":"GET","path":"/","query":{},"headers_redacted":{"Host":"192.168.0.21:8088","Connection":"keep-alive","DNT":"1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate","Accept-Language":"en,ru;q=0.9,en-US;q=0.8,zh-CN;q=0.7,zh;q=0.6","Cookie":"<redacted>"},"content_type":"","content_length":0},"response":{"status_code":200,"bytes_sent":43,"profile":null},"classification":{"verdict":"probe","tags":["landing"],"indicators":[]},"decision":{"truncated":false,"oversized":false,"rate_limited":false,"dropped":false},"artifacts":[]}
```

### `honeypot-platform/scripts/check_docs.sh`  _(~0.6 KB; showing ≤800 lines)_
```bash
#!/usr/bin/env bash
set -euo pipefail

DOCS=(
  docs/ARCHITECTURE.md
  docs/PACK_SPEC.md
  docs/DSL_REFERENCE.md
  docs/EVENT_SCHEMA.md
  docs/SENSORS.md
  docs/STORAGE_LAYOUT.md
  docs/DEPLOYMENT.md
  docs/SECURITY.md
)

MIN_LINES=12

for d in "${DOCS[@]}"; do
  [[ -f "$d" ]] || { echo "missing: $d"; exit 1; }
  lines=$(wc -l < "$d")
  (( lines >= MIN_LINES )) || { echo "too short: $d ($lines < $MIN_LINES)"; exit 1; }
  rg -q '^# ' "$d" || { echo "missing title heading: $d"; exit 1; }
  sec_count=$(rg -c '^## ' "$d")
  (( sec_count >= 2 )) || { echo "need at least 2 sections: $d"; exit 1; }
  echo "ok: $d"
done
```

### `honeypot-platform/sensors/fsmon/Dockerfile`  _(~0.2 KB; showing ≤800 lines)_
```
FROM python:3.11-slim
WORKDIR /app
COPY fsmon/fsmon.py /app/fsmon.py
COPY fsmon/rules.schema.json /app/rules.schema.json
COPY entrypoint.sh /entrypoint.sh
RUN pip install --no-cache-dir watchdog && chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
```

### `honeypot-platform/sensors/fsmon/README.md`  _(~0.1 KB; showing ≤800 lines)_
```md
# sensor-fsmon

Inotify-style filesystem monitor (implemented through watchdog in Python) for create/modify capture.
```

### `honeypot-platform/sensors/fsmon/entrypoint.sh`  _(~0.1 KB; showing ≤800 lines)_
```bash
#!/usr/bin/env sh
set -eu
exec python /app/fsmon.py
```

### `honeypot-platform/sensors/fsmon/fsmon/fsmon.py`  _(~2.8 KB; showing ≤800 lines)_
```python
import fnmatch
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

PACK_ID = os.getenv("HOHO_PACK_ID", "unknown-pack")
ROOT = Path(os.getenv("HOHO_STORAGE_ROOT", "/artifacts"))
WATCH_DIRS = os.getenv("FSMON_WATCH", "/watched").split(",")
MAX_BYTES = int(os.getenv("FSMON_MAX_BYTES", "262144"))
ALLOW = [x for x in os.getenv("FSMON_ALLOW", "*").split(",") if x]
DENY = [x for x in os.getenv("FSMON_DENY", "").split(",") if x]


def now():
    return datetime.now(timezone.utc).isoformat()


def allow_path(path: str) -> bool:
    if any(fnmatch.fnmatch(path, pat) for pat in DENY):
        return False
    return any(fnmatch.fnmatch(path, pat) for pat in ALLOW)


def append_event(event):
    p = ROOT / PACK_ID / "index" / "events.jsonl"
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event) + "\n")


class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        self._process(event)

    def on_created(self, event):
        self._process(event)

    def _process(self, event):
        if event.is_directory or not allow_path(event.src_path):
            return
        path = Path(event.src_path)
        try:
            data = path.read_bytes()[:MAX_BYTES]
        except Exception:
            return
        digest = hashlib.sha256(data).hexdigest()
        bp = ROOT / PACK_ID / "blobs" / digest[:2] / digest
        bp.parent.mkdir(parents=True, exist_ok=True)
        if not bp.exists():
            bp.write_bytes(data)
        ev = {
            "schema_version": 1,
            "event_id": f"fs-{int(datetime.now().timestamp()*1000)}",
            "ts": now(),
            "pack_id": PACK_ID,
            "interaction": "high",
            "component": "sensor.fsmon",
            "src": {"ip": None, "port": None, "forwarded_for": [], "user_agent": None},
            "proto": "tcp",
            "request": {},
            "response": {"status_code": None, "bytes_sent": 0, "profile": None},
            "classification": {"verdict": "postex", "tags": ["fs_change"], "indicators": [str(path)]},
            "decision": {"truncated": len(data) >= MAX_BYTES, "oversized": False, "rate_limited": False, "dropped": False},
            "artifacts": [{"kind": "fs_write", "sha256": digest, "size": len(data), "mime": "application/octet-stream", "storage_ref": f"blobs/{digest[:2]}/{digest}", "meta": {"path": str(path), "preview": data[:128].decode('utf-8', errors='ignore')}}],
        }
        append_event(ev)


if __name__ == "__main__":
    observer = Observer()
    handler = Handler()
    for d in WATCH_DIRS:
        Path(d).mkdir(parents=True, exist_ok=True)
        observer.schedule(handler, d, recursive=True)
    observer.start()
    observer.join()
```

### `honeypot-platform/sensors/fsmon/fsmon/rules.schema.json`  _(~0.3 KB; showing ≤800 lines)_
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "watch": {"type": "array", "items": {"type": "string"}},
    "allow_globs": {"type": "array", "items": {"type": "string"}},
    "deny_globs": {"type": "array", "items": {"type": "string"}}
  }
}
```

### `honeypot-platform/sensors/http_proxy/Dockerfile`  _(~0.2 KB; showing ≤800 lines)_
```
FROM python:3.11-slim
WORKDIR /app
COPY proxy/capture_addon.py /app/capture_addon.py
COPY entrypoint.sh /entrypoint.sh
RUN pip install --no-cache-dir mitmproxy PyYAML jsonschema && chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
```

### `honeypot-platform/sensors/http_proxy/README.md`  _(~0.1 KB; showing ≤800 lines)_
```md
# sensor-http-proxy

Mitmproxy reverse-proxy sensor emitting canonical events and request-body artifacts.
```

### `honeypot-platform/sensors/http_proxy/entrypoint.sh`  _(~0.1 KB; showing ≤800 lines)_
```bash
#!/usr/bin/env sh
set -eu
: "${UPSTREAM:=http://upstream:80}"
exec mitmdump --mode "reverse:${UPSTREAM}" -s /app/capture_addon.py
```

### `honeypot-platform/sensors/http_proxy/proxy/capture_addon.py`  _(~2.1 KB; showing ≤800 lines)_
```python
import json
import os
from pathlib import Path
from datetime import datetime, timezone
import hashlib

PACK_ID = os.getenv("HOHO_PACK_ID", "unknown-pack")
ROOT = Path(os.getenv("HOHO_STORAGE_ROOT", "/artifacts"))


def _now():
    return datetime.now(timezone.utc).isoformat()


def _append_event(ev: dict):
    p = ROOT / PACK_ID / "index" / "events.jsonl"
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("a", encoding="utf-8") as f:
        f.write(json.dumps(ev) + "\n")


def response(flow):
    req = flow.request
    resp = flow.response
    body = req.raw_content or b""
    digest = hashlib.sha256(body).hexdigest() if body else None
    if body:
        bp = ROOT / PACK_ID / "blobs" / digest[:2] / digest
        bp.parent.mkdir(parents=True, exist_ok=True)
        if not bp.exists():
            bp.write_bytes(body)
    ev = {
        "schema_version": 1,
        "event_id": flow.id,
        "ts": _now(),
        "pack_id": PACK_ID,
        "interaction": "high",
        "component": "sensor.http_proxy",
        "src": {"ip": req.remote_conn.address[0] if req.remote_conn.address else None, "port": req.remote_conn.address[1] if req.remote_conn.address else None, "forwarded_for": [], "user_agent": req.headers.get("User-Agent")},
        "proto": "http",
        "request": [REDACTED]
        "response": {"status_code": resp.status_code if resp else None, "bytes_sent": len(resp.raw_content or b"") if resp else 0, "profile": None},
        "classification": {"verdict": "unknown", "tags": [], "indicators": []},
        "decision": {"truncated": False, "oversized": False, "rate_limited": False, "dropped": False},
        "artifacts": ([{"kind": "request_body", "sha256": digest, "size": len(body), "mime": req.headers.get("Content-Type", "application/octet-stream"), "storage_ref": f"blobs/{digest[:2]}/{digest}", "meta": {}}] if body else []),
    }
    _append_event(ev)
```

### `honeypot-platform/sensors/pcap/Dockerfile`  _(~0.2 KB; showing ≤800 lines)_
```
FROM alpine:3.20
RUN apk add --no-cache tcpdump bash coreutils
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
```

### `honeypot-platform/sensors/pcap/README.md`  _(~0.1 KB; showing ≤800 lines)_
```md
# sensor-pcap

Tcpdump wrapper with rotated capture files stored as blob artifacts plus pcap segment events.
```

### `honeypot-platform/sensors/pcap/entrypoint.sh`  _(~1.3 KB; showing ≤800 lines)_
```bash
#!/usr/bin/env bash
set -euo pipefail
PACK_ID="${HOHO_PACK_ID:-unknown-pack}"
ROOT="${HOHO_STORAGE_ROOT:-/artifacts}"
ROTATE_SECONDS="${PCAP_ROTATE_SECONDS:-60}"
ROTATE_COUNT="${PCAP_ROTATE_COUNT:-10}"
OUT_DIR="${ROOT}/${PACK_ID}/pcap"
mkdir -p "$OUT_DIR" "${ROOT}/${PACK_ID}/index"

tcpdump -i any -w "${OUT_DIR}/segment-%Y%m%d-%H%M%S.pcap" -G "$ROTATE_SECONDS" -W "$ROTATE_COUNT" || true
for f in "$OUT_DIR"/*.pcap; do
  [ -f "$f" ] || continue
  sha=$(sha256sum "$f" | awk '{print $1}')
  bdir="${ROOT}/${PACK_ID}/blobs/${sha:0:2}"
  mkdir -p "$bdir"
  cp "$f" "$bdir/$sha"
  printf '{"schema_version":1,"event_id":"pcap-%s","ts":"%s","pack_id":"%s","interaction":"high","component":"sensor.pcap","src":{"ip":null,"port":null,"forwarded_for":[],"user_agent":null},"proto":"tcp","request":{},"response":{"status_code":null,"bytes_sent":0,"profile":null},"classification":{"verdict":"probe","tags":["pcap_segment"],"indicators":[]},"decision":{"truncated":false,"oversized":false,"rate_limited":false,"dropped":false},"artifacts":[{"kind":"pcap_segment","sha256":"%s","size":%s,"mime":"application/vnd.tcpdump.pcap","storage_ref":"blobs/%s/%s","meta":{"source":"%s"}}]}\n' "$(date +%s)" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$PACK_ID" "$sha" "$(wc -c < "$f")" "${sha:0:2}" "$sha" "$f" >> "${ROOT}/${PACK_ID}/index/events.jsonl"
done
```
