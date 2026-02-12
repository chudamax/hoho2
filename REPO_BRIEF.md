# Repository Brief: hoho2

_Generated 2026-02-12 15:19 UTC_

## Quick Facts
- **Branch:** main
- **Commit:** 800e43c (2026-02-12 16:13:31 +0100)
- **Total commits:** 68
- **Files scanned:** 125
- **Text files embedded (after filters):** 123

## Language & LOC Overview (approx.)
- **python** — files: 49 (39.8%), LOC: 3134
- **md** — files: 32 (26.0%), LOC: 8266
- **yaml** — files: 11 (8.9%), LOC: 759
- **bash** — files: 11 (8.9%), LOC: 317
- **other** — files: 9 (7.3%), LOC: 310
- **html** — files: 5 (4.1%), LOC: 19
- **json** — files: 3 (2.4%), LOC: 681
- **toml** — files: 3 (2.4%), LOC: 48

## Directory Tree (depth ≤ 10)

```text
- .gitignore
- AGENTS.md
- REPO_BRIEF.md
- honeypot-platform
  - docs
    - ARCHITECTURE.md
    - DEPLOYMENT.md
    - DIRECTORY_LAYOUT.md
    - DSL_REFERENCE.md
    - EVENT_SCHEMA.md
    - HUB.md
    - PACK_SPEC.md
    - README.md
    - SECURITY.md
    - SENSORS.md
    - STORAGE_LAYOUT.md
    - TELEMETRY_FILTERS.md
    - TELEMETRY_FORWARDING.md
  - hub
    - Dockerfile
    - docker-compose.yml
  - scripts
    - build_sensors.sh
    - check_docs.sh
    - check_layout.sh
    - migrate_honeypots_layout.py
    - validate_honeypots_layout.py
  - deploy
    - compose
      - README.md
    - runbooks
      - high-interaction-honeypot-from-cve.md
      - low-interaction-honeypot-from-cve.md
    - app
      - db.py
      - main.py
  - packages
    - hoho_core
      - pyproject.toml
    - hoho_forwarder
    - hoho_runtime
  - runtimes
    - low_runtime
      - Dockerfile
  - sensors
    - egress_proxy
      - entrypoint.sh
    - falco
      - forwarder.py
    - fsmon
    - http_proxy
    - pcap
  - honeypots
    - high
      - cve-2017-12629_solr_rce
        - README.md
        - honeypot.yaml
        - reset.sh
      - cve-2020-25213_wp_file_upload
      - cve-2021-41773_42013_apache_rce
      - example-wp-stack
    - low
      - cve-2021-41773_apache-2-4-49-2-4-50-traversal-rce
      - example-upload-sink
      - example-web
      - templates
        - event.html
        - events.html
        - index.html
        - sessions.html
      - hoho_core
        - MANIFEST.in
        - __init__.py
        - version.py
      - hoho_forwarder
        - main.py
      - hoho_runtime
        - cli.py
        - config.py
        - env.py
      - proxy
        - egress_capture_addon.py
        - gen_ca.py
      - rules
        - hoho_any_exec.yaml
        - hoho_rules.yaml
      - fsmon
        - fsmon.py
        - rules.schema.json
        - capture_addon.py
        - falco
          - custom_rules.yaml
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
          - event_v2.json
          - pack_v1.json
          - validate.py
          - validate_event.py
        - storage
          - base.py
          - fs.py
        - telemetry
          - filters.py
        - utils
          - filenames.py
          - hashing.py
          - jsonl.py
          - redact.py
          - time.py
        - container
          - low_runtime.py
        - orchestration
          - ca_pregen.py
          - compose_down_all.py
          - compose_render.py
          - compose_run.py
        - server
          - http.py
          - tcp.py
        - cve-2021-41773_42013
          - cgi-bin
            - health.sh
          - htdocs
            - index.html
```

## Recent Commits
- 800e43c | 2026-02-12 | Merge pull request #21 from chudamax/codex/add-global-.env-for-telemetry-forwarding
- e05a298 | 2026-02-12 | Add global .env loading for telemetry forwarding
- 7a77db2 | 2026-02-12 | up
- ebf9abd | 2026-02-12 | up
- 425f07b | 2026-02-12 | up
- 735b926 | 2026-02-12 | Merge pull request #20 from chudamax/codex/implement-telemetry-v2-with-event-contracts
- 7658593 | 2026-02-12 | Implement telemetry v2 contracts, filtering, forwarder, and hub scaffolding
- 4a43fb9 | 2026-02-12 | falcon is working
- dd60f89 | 2026-02-12 | Merge pull request #19 from chudamax/codex/move-falco-rules-to-yaml-and-fix-startup-errors
- 1925c7a | 2026-02-12 | Move Falco defaults into image rules and fix startup args

## Files (embedded, trimmed)
> Secret-looking lines are redacted by default. Large files are truncated to stay within budgets.

### `.gitignore`  _(~4.9 KB; showing ≤800 lines)_
```
artifacts/
run/
deploy/
honeypot-platform/sensors/*/packages/

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

# Generated compose/runtime outputs
honeypot-platform/deploy/compose/*
!honeypot-platform/deploy/compose/README.md
honeypot-platform/run/artifacts/**

honeypot-platform/deploy/compose/**/runtime/ca/**

honeypot-platform/.env
honeypot-platform/.env.*
!honeypot-platform/.env.example
```

### `AGENTS.md`  _(~3.4 KB; showing ≤800 lines)_
```md
# AGENTS.md (repo root)

## Honeypot layout (Unified Layout v2)
Authoritative spec: `honeypot-platform/docs/DIRECTORY_LAYOUT.md`.

MUST:
- Always use `honeypot_id == metadata.id`.
- Create honeypots only at:
  - `honeypot-platform/honeypots/low/<honeypot_id>/honeypot.yaml`
  - `honeypot-platform/honeypots/high/<honeypot_id>/honeypot.yaml`
- Create docs only at `honeypot-platform/honeypots/{low,high}/<honeypot_id>/README.md`.
- Keep YAML-referenced local paths relative and inside the same honeypot folder.
- Artifacts always go to `honeypot-platform/run/artifacts/<honeypot_id>/...`.
- Compose output always goes to `honeypot-platform/deploy/compose/<honeypot_id>/docker-compose.yml`.

MUST NOT:
- Do not create `honeypot-platform/run/artifacts/<runs-subtree>/**` (no run-id subtrees).
- Do not create non-canonical honeypot folders (example forbidden: `honeypots/high/2021-41773_42013/`).
- Do not add new honeypot YAML definitions under `honeypot-platform/packs/`.

## Deprecated compatibility
- `honeypot-platform/packs/{low,high}/*.yaml` may still be invoked by CLI for one compatibility window.
- CLI should emit deprecation warnings for `packs/` paths.

## Docs that must be consulted (before implementing or changing honeypots)
- Spec + schema rules: `honeypot-platform/docs/PACK_SPEC.md`
- Sensor behavior + env contracts: `honeypot-platform/docs/SENSORS.md`
- Storage layout + overwrite semantics: `honeypot-platform/docs/STORAGE_LAYOUT.md`
- Deployment notes: `honeypot-platform/docs/DEPLOYMENT.md`
- Compose output notes (incl. egress CA paths): `honeypot-platform/deploy/compose/README.md`

## Runbooks (follow exactly)
Low-interaction:
- Always read: `honeypot-platform/docs/runbooks/low-interaction-honeypot-from-cve.md`

High-interaction:
- Always read: `honeypot-platform/docs/runbooks/high-interaction-honeypot-from-cve.md`

## High-interaction capture baseline (recommended)
For “high” stacks, default to maximum visibility:
- `http_proxy` (reverse proxy) for inbound request/response metadata and request body capture.
- `egress_proxy` (forward proxy) to capture **outbound** downloads (post-exploitation stage).
- `fsmon` to capture file writes in shared mounted paths.
- `pcap` for ground-truth network capture.

## Egress proxy sensor guidance (important)
Use `egress_proxy` when you want to capture attacker tooling fetched by the compromised container(s):
- It emits `sensor.egress_proxy.http` events.
- It can store response bodies as artifacts (`egress.response_body`) and also materialize symlinks under:
  `run/artifacts/<honeypot_id>/objects/<event_id>/egress.response/<filename>`
- With TLS MITM enabled, `hoho run` pre-generates a runtime CA under:
  `deploy/compose/<honeypot_id>/runtime/ca/`
  and the egress proxy exports the CA cert to:
  `run/artifacts/<honeypot_id>/ca/egress-ca.crt`
- If `tls_mitm.install_trust.enabled: true`, runtime executes `/hoho/ca/install-ca.sh` in attached services and emits:
  `system.ca_install.succeeded` / `system.ca_install.failed` events.

## Working reference honeypots (golden examples)
High-interaction:
- `honeypot-platform/honeypots/high/cve-2021-41773_42013_apache_rce/honeypot.yaml`

Low-interaction:
- `honeypot-platform/honeypots/low/cve-2021-41773_apache-2-4-49-2-4-50-traversal-rce/honeypot.yaml`

## Operational commands (stop/cleanup)
- Stop everything: `hoho down-all` (optionally `--volumes`)
- Per-honeypot manual stop:
  `docker compose -p "hoho-<honeypot_id>" -f deploy/compose/<honeypot_id>/docker-compose.yml down -v`
```

### `REPO_BRIEF.md`  _(~230.0 KB; showing ≤800 lines)_
```md
# Repository Brief: hoho2

_Generated 2026-02-12 13:24 UTC_

## Quick Facts
- **Branch:** main
- **Commit:** 735b926 (2026-02-12 14:16:27 +0100)
- **Total commits:** 63
- **Files scanned:** 123
- **Text files embedded (after filters):** 122

## Language & LOC Overview (approx.)
- **python** — files: 48 (39.3%), LOC: 3047
- **md** — files: 32 (26.2%), LOC: 7427
- **yaml** — files: 11 (9.0%), LOC: 755
- **bash** — files: 11 (9.0%), LOC: 295
- **other** — files: 9 (7.4%), LOC: 292
- **html** — files: 5 (4.1%), LOC: 19
- **json** — files: 3 (2.5%), LOC: 681
- **toml** — files: 3 (2.5%), LOC: 48

## Directory Tree (depth ≤ 10)

```text
- .gitignore
- AGENTS.md
- REPO_BRIEF.md
- honeypot-platform
  - docs
    - ARCHITECTURE.md
    - DEPLOYMENT.md
    - DIRECTORY_LAYOUT.md
    - DSL_REFERENCE.md
    - EVENT_SCHEMA.md
    - HUB.md
    - PACK_SPEC.md
    - README.md
    - SECURITY.md
    - SENSORS.md
    - STORAGE_LAYOUT.md
    - TELEMETRY_FILTERS.md
    - TELEMETRY_FORWARDING.md
  - hub
    - Dockerfile
    - docker-compose.yml
  - scripts
    - build_sensors.sh
    - check_docs.sh
    - check_layout.sh
    - migrate_honeypots_layout.py
    - validate_honeypots_layout.py
  - deploy
    - compose
      - README.md
    - runbooks
      - high-interaction-honeypot-from-cve.md
      - low-interaction-honeypot-from-cve.md
    - app
      - db.py
      - main.py
  - packages
    - hoho_core
      - pyproject.toml
    - hoho_forwarder
    - hoho_runtime
  - runtimes
    - low_runtime
      - Dockerfile
  - sensors
    - egress_proxy
      - entrypoint.sh
    - falco
      - forwarder.py
    - fsmon
    - http_proxy
    - pcap
  - honeypots
    - high
      - cve-2017-12629_solr_rce
        - README.md
        - honeypot.yaml
        - reset.sh
      - cve-2020-25213_wp_file_upload
      - cve-2021-41773_42013_apache_rce
      - example-wp-stack
    - low
      - cve-2021-41773_apache-2-4-49-2-4-50-traversal-rce
      - example-upload-sink
      - example-web
      - templates
        - event.html
        - events.html
        - index.html
        - sessions.html
      - hoho_core
        - MANIFEST.in
        - __init__.py
        - version.py
      - hoho_forwarder
        - main.py
      - hoho_runtime
        - cli.py
        - config.py
      - proxy
        - egress_capture_addon.py
        - gen_ca.py
      - rules
        - hoho_any_exec.yaml
        - hoho_rules.yaml
      - fsmon
        - fsmon.py
        - rules.schema.json
        - capture_addon.py
        - falco
          - custom_rules.yaml
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
          - event_v2.json
          - pack_v1.json
          - validate.py
          - validate_event.py
        - storage
          - base.py
          - fs.py
        - telemetry
          - filters.py
        - utils
          - filenames.py
          - hashing.py
          - jsonl.py
          - redact.py
          - time.py
        - container
          - low_runtime.py
        - orchestration
          - ca_pregen.py
          - compose_down_all.py
          - compose_render.py
          - compose_run.py
        - server
          - http.py
          - tcp.py
        - cve-2021-41773_42013
          - cgi-bin
            - health.sh
          - htdocs
            - index.html
```

## Recent Commits
- 735b926 | 2026-02-12 | Merge pull request #20 from chudamax/codex/implement-telemetry-v2-with-event-contracts
- 7658593 | 2026-02-12 | Implement telemetry v2 contracts, filtering, forwarder, and hub scaffolding
- 4a43fb9 | 2026-02-12 | falcon is working
- dd60f89 | 2026-02-12 | Merge pull request #19 from chudamax/codex/move-falco-rules-to-yaml-and-fix-startup-errors
- 1925c7a | 2026-02-12 | Move Falco defaults into image rules and fix startup args
- 982f536 | 2026-02-12 | up
- 6f711d7 | 2026-02-12 | Merge pull request #18 from chudamax/codex/add-falco-sensor-for-runtime-telemetry
- 1a4e5dd | 2026-02-12 | Add falco sensor integration with compose rendering and docs
- 4d26738 | 2026-02-12 | up
- 1fdd0df | 2026-02-12 | Merge pull request #17 from chudamax/codex/containerize-low-interaction-honeypots

## Files (embedded, trimmed)
[REDACTED]

### `.gitignore`  _(~4.8 KB; showing ≤800 lines)_
```
artifacts/
run/
deploy/

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

# Generated compose/runtime outputs
honeypot-platform/deploy/compose/*
!honeypot-platform/deploy/compose/README.md
honeypot-platform/run/artifacts/**

honeypot-platform/deploy/compose/**/runtime/ca/**
```

### `AGENTS.md`  _(~3.4 KB; showing ≤800 lines)_
```md
# AGENTS.md (repo root)

## Honeypot layout (Unified Layout v2)
Authoritative spec: `honeypot-platform/docs/DIRECTORY_LAYOUT.md`.

MUST:
- Always use `honeypot_id == metadata.id`.
- Create honeypots only at:
  - `honeypot-platform/honeypots/low/<honeypot_id>/honeypot.yaml`
  - `honeypot-platform/honeypots/high/<honeypot_id>/honeypot.yaml`
- Create docs only at `honeypot-platform/honeypots/{low,high}/<honeypot_id>/README.md`.
- Keep YAML-referenced local paths relative and inside the same honeypot folder.
- Artifacts always go to `honeypot-platform/run/artifacts/<honeypot_id>/...`.
- Compose output always goes to `honeypot-platform/deploy/compose/<honeypot_id>/docker-compose.yml`.

MUST NOT:
- Do not create `honeypot-platform/run/artifacts/<runs-subtree>/**` (no run-id subtrees).
- Do not create non-canonical honeypot folders (example forbidden: `honeypots/high/2021-41773_42013/`).
- Do not add new honeypot YAML definitions under `honeypot-platform/packs/`.

## Deprecated compatibility
- `honeypot-platform/packs/{low,high}/*.yaml` may still be invoked by CLI for one compatibility window.
- CLI should emit deprecation warnings for `packs/` paths.

## Docs that must be consulted (before implementing or changing honeypots)
- Spec + schema rules: `honeypot-platform/docs/PACK_SPEC.md`
- Sensor behavior + env contracts: `honeypot-platform/docs/SENSORS.md`
- Storage layout + overwrite semantics: `honeypot-platform/docs/STORAGE_LAYOUT.md`
- Deployment notes: `honeypot-platform/docs/DEPLOYMENT.md`
- Compose output notes (incl. egress CA paths): `honeypot-platform/deploy/compose/README.md`

## Runbooks (follow exactly)
Low-interaction:
- Always read: `honeypot-platform/docs/runbooks/low-interaction-honeypot-from-cve.md`

High-interaction:
- Always read: `honeypot-platform/docs/runbooks/high-interaction-honeypot-from-cve.md`

## High-interaction capture baseline (recommended)
For “high” stacks, default to maximum visibility:
- `http_proxy` (reverse proxy) for inbound request/response metadata and request body capture.
- `egress_proxy` (forward proxy) to capture **outbound** downloads (post-exploitation stage).
- `fsmon` to capture file writes in shared mounted paths.
- `pcap` for ground-truth network capture.

## Egress proxy sensor guidance (important)
Use `egress_proxy` when you want to capture attacker tooling fetched by the compromised container(s):
- It emits `sensor.egress_proxy.http` events.
- It can store response bodies as artifacts (`egress.response_body`) and also materialize symlinks under:
  `run/artifacts/<honeypot_id>/objects/<event_id>/egress.response/<filename>`
- With TLS MITM enabled, `hoho run` pre-generates a runtime CA under:
  `deploy/compose/<honeypot_id>/runtime/ca/`
  and the egress proxy exports the CA cert to:
  `run/artifacts/<honeypot_id>/ca/egress-ca.crt`
- If `tls_mitm.install_trust.enabled: true`, runtime executes `/hoho/ca/install-ca.sh` in attached services and emits:
  `system.ca_install.succeeded` / `system.ca_install.failed` events.

## Working reference honeypots (golden examples)
High-interaction:
- `honeypot-platform/honeypots/high/cve-2021-41773_42013_apache_rce/honeypot.yaml`

Low-interaction:
- `honeypot-platform/honeypots/low/cve-2021-41773_apache-2-4-49-2-4-50-traversal-rce/honeypot.yaml`

## Operational commands (stop/cleanup)
- Stop everything: `hoho down-all` (optionally `--volumes`)
- Per-honeypot manual stop:
  `docker compose -p "hoho-<honeypot_id>" -f deploy/compose/<honeypot_id>/docker-compose.yml down -v`
```

### `REPO_BRIEF.md`  _(~205.2 KB; showing ≤800 lines)_
```md
# Repository Brief: hoho2

_Generated 2026-02-12 12:38 UTC_

## Quick Facts
- **Branch:** main
- **Commit:** 4a43fb9 (2026-02-12 12:37:54 +0000)
- **Total commits:** 61
- **Files scanned:** 104
- **Text files embedded (after filters):** 104

## Language & LOC Overview (approx.)
- **python** — files: 41 (39.4%), LOC: 2638
- **md** — files: 29 (27.9%), LOC: 7222
- **bash** — files: 11 (10.6%), LOC: 292
- **yaml** — files: 10 (9.6%), LOC: 745
- **other** — files: 8 (7.7%), LOC: 287
- **json** — files: 2 (1.9%), LOC: 505
- **toml** — files: 2 (1.9%), LOC: 36
- **html** — files: 1 (1.0%), LOC: 12

## Directory Tree (depth ≤ 10)

```text
- .gitignore
- AGENTS.md
- REPO_BRIEF.md
- honeypot-platform
  - docs
    - ARCHITECTURE.md
    - DEPLOYMENT.md
    - DIRECTORY_LAYOUT.md
    - DSL_REFERENCE.md
    - EVENT_SCHEMA.md
    - PACK_SPEC.md
    - README.md
    - SECURITY.md
    - SENSORS.md
    - STORAGE_LAYOUT.md
  - scripts
    - build_sensors.sh
    - check_docs.sh
    - check_layout.sh
    - migrate_honeypots_layout.py
    - validate_honeypots_layout.py
  - deploy
    - compose
      - README.md
    - runbooks
      - high-interaction-honeypot-from-cve.md
      - low-interaction-honeypot-from-cve.md
  - packages
    - hoho_core
      - pyproject.toml
    - hoho_runtime
  - runtimes
    - low_runtime
      - Dockerfile
  - sensors
    - egress_proxy
      - entrypoint.sh
    - falco
      - forwarder.py
    - fsmon
    - http_proxy
    - pcap
  - honeypots
    - high
      - cve-2017-12629_solr_rce
        - README.md
        - honeypot.yaml
        - reset.sh
      - cve-2020-25213_wp_file_upload
      - cve-2021-41773_42013_apache_rce
      - example-wp-stack
    - low
      - cve-2021-41773_apache-2-4-49-2-4-50-traversal-rce
      - example-upload-sink
      - example-web
      - hoho_core
        - MANIFEST.in
        - __init__.py
        - version.py
      - hoho_runtime
        - cli.py
        - config.py
      - proxy
        - egress_capture_addon.py
        - gen_ca.py
      - rules
        - hoho_any_exec.yaml
        - hoho_rules.yaml
      - fsmon
        - fsmon.py
        - rules.schema.json
        - capture_addon.py
        - falco
          - custom_rules.yaml
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
        - container
          - low_runtime.py
        - orchestration
          - ca_pregen.py
          - compose_down_all.py
          - compose_render.py
          - compose_run.py
        - server
          - http.py
          - tcp.py
        - cve-2021-41773_42013
          - cgi-bin
            - health.sh
          - htdocs
            - index.html
```

## Recent Commits
- 4a43fb9 | 2026-02-12 | falcon is working
- dd60f89 | 2026-02-12 | Merge pull request #19 from chudamax/codex/move-falco-rules-to-yaml-and-fix-startup-errors
- 1925c7a | 2026-02-12 | Move Falco defaults into image rules and fix startup args
- 982f536 | 2026-02-12 | up
- 6f711d7 | 2026-02-12 | Merge pull request #18 from chudamax/codex/add-falco-sensor-for-runtime-telemetry
- 1a4e5dd | 2026-02-12 | Add falco sensor integration with compose rendering and docs
- 4d26738 | 2026-02-12 | up
- 1fdd0df | 2026-02-12 | Merge pull request #17 from chudamax/codex/containerize-low-interaction-honeypots
- d005368 | 2026-02-12 | Containerize low interaction runtime and enable sensors via compose
- 748828b | 2026-02-12 | up

## Files (embedded, trimmed)
[REDACTED]

### `.gitignore`  _(~4.8 KB; showing ≤800 lines)_
```
artifacts/
run/
deploy/

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
```
<!-- trimmed: file exceeded per-file limits -->

### `honeypot-platform/deploy/compose/README.md`  _(~1.2 KB; showing ≤800 lines)_
```md
# Compose output directory

By default, `hoho` writes compose bundles under `<project_root>/deploy/compose/<honeypot_id>/`.

When `-o/--output` is not provided, the CLI discovers `project_root` by walking up from the honeypot definition path and selecting:
1. the first ancestor containing `deploy/compose` (or `deploy/compose/README.md`),
2. otherwise the first ancestor containing `honeypots/` or `packs/`,
3. otherwise the definition file's parent directory.

If `-o/--output` is provided, `hoho` keeps existing behavior and uses that path as given.


## Runtime egress MITM CA

For high-interaction stacks using the egress proxy with TLS MITM + CA install enabled, `hoho run` now pre-generates (or reuses) a host-side runtime CA before `docker compose up`:

- `deploy/compose/<honeypot_id>/runtime/ca/egress-ca.crt`
- `deploy/compose/<honeypot_id>/runtime/ca/egress-ca.key`
- `deploy/compose/<honeypot_id>/runtime/ca/mitmproxy-ca.pem` (combined cert + key)
- `deploy/compose/<honeypot_id>/runtime/ca/mitmproxy-ca-cert.pem` (cert only)

Attached services mount `runtime/ca/egress-ca.crt` at `/hoho/ca/egress-ca.crt`, and the egress proxy mounts `runtime/ca` and uses those files in custom CA mode so all services trust and interception use the same CA material.
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

### `honeypot-platform/docs/DEPLOYMENT.md`  _(~1.7 KB; showing ≤800 lines)_
```md
# Deployment

## Quickstart (low + high)
1. Validate honeypot:
   - `hoho validate honeypots/{low,high}/<honeypot_id>/honeypot.yaml`
2. Render compose:
   - `hoho render-compose honeypots/{low,high}/<honeypot_id>/honeypot.yaml`
3. Start stack:
   - `hoho run honeypots/{low,high}/<honeypot_id>/honeypot.yaml`
4. Inspect artifacts:
   - `run/artifacts/<honeypot_id>/index/events.jsonl`
   - `run/artifacts/<honeypot_id>/blobs/`

## Global .env for telemetry forwarding
- Global environment file path: `honeypot-platform/.env`
- Recommended bootstrap:
  - `cp honeypot-platform/.env.example honeypot-platform/.env`
- Variables:
  - `HOHO_HUB_URL`
  - `HOHO_HUB_TOKEN`

`hoho` auto-loads `honeypot-platform/.env` by default and also passes it to Docker Compose with `--env-file` so `${HOHO_HUB_URL}` and `${HOHO_HUB_TOKEN}` interpolate consistently.

Override examples:
- `hoho --env-file /path/to/custom.env run honeypots/high/<honeypot_id>/honeypot.yaml`
- `hoho --no-env run honeypots/high/<honeypot_id>/honeypot.yaml`

## Low interaction runtime mode
- `hoho run` defaults to `--mode container` for both low and high interaction honeypots.
- For low-interaction debugging only, host mode is still available:
  - `hoho run honeypots/low/<honeypot_id>/honeypot.yaml --mode host`

## Multi-honeypot operation
- Each run uses compose project name `hoho-<honeypot_id>`.
- Multiple honeypots can run in parallel when `honeypot_id` differs.
- Keep only one active stack per `honeypot_id`.

## Notes
- `deploy/compose/**` is generated and should not be committed.
- `run/artifacts/<honeypot_id>/` is overwritten for each new run of the same honeypot.
- `HOHO_PACK_ID` remains the runtime env variable name and aliases `honeypot_id`.
```

### `honeypot-platform/docs/DIRECTORY_LAYOUT.md`  _(~1.9 KB; showing ≤800 lines)_
```md
# DIRECTORY_LAYOUT.md

## Canonical Layout (one honeypot = one folder)

All honeypot source-of-truth files live together under:

- `honeypot-platform/honeypots/high/<honeypot_id>/`
- `honeypot-platform/honeypots/low/<honeypot_id>/`

Each honeypot folder must contain:
- `honeypot.yaml`
- `README.md`

Optional supporting assets referenced by `honeypot.yaml` must stay inside the same folder.

## Deprecated layout

`honeypot-platform/packs/` is deprecated. Existing files may be kept temporarily for compatibility, but new honeypot definitions must not be added there.

## Generated output (never committed)
- Compose: `honeypot-platform/deploy/compose/<honeypot_id>/docker-compose.yml` (overwritten)
- Artifacts: `honeypot-platform/run/artifacts/<honeypot_id>/**` (overwritten)

## MUST rules
- MUST use `honeypot_id` as the only filesystem identifier.
- MUST set `metadata.id == <honeypot_id>` in `honeypot.yaml`.
- MUST keep docs in `honeypots/{low,high}/<honeypot_id>/README.md`.
- MUST keep referenced local file paths relative and inside the same honeypot folder.
- MUST render compose to `deploy/compose/<honeypot_id>/docker-compose.yml`.
- MUST write artifacts to `run/artifacts/<honeypot_id>/...`.

## MUST NOT rules
- MUST NOT create `run/artifacts/<runs-subtree>/**`.
- MUST NOT create non-canonical honeypot folders (example forbidden: `honeypots/high/2021-41773_42013/`).
- MUST NOT commit generated compose files under `honeypots/**`.
- MUST NOT add new honeypot YAML files under `packs/`.

## Compatibility invocation styles
- `hoho run honeypot-platform/honeypots/high/<id>`
- `hoho run honeypot-platform/honeypots/high/<id>/honeypot.yaml`
- `hoho run honeypot-platform/packs/high/<old>.yaml` (supported with deprecation warning)

## Overwrite warning
Simple layout has no run isolation. Running the same `honeypot_id` again overwrites `deploy/compose/<honeypot_id>/` and `run/artifacts/<honeypot_id>/`.
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

### `honeypot-platform/docs/EVENT_SCHEMA.md`  _(~1.6 KB; showing ≤800 lines)_
```md
# Event Schema v2

All telemetry producers emit schema version `2`.

## Required envelope
- `schema_version: 2`
- `event_id`, `ts`
- `honeypot_id`, `session_id`, `agent_id`
- `event_name` (lowercase dotted)
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
```

### `honeypot-platform/docs/HUB.md`  _(~0.7 KB; showing ≤800 lines)_
```md
# HOHO Hub

Hub lives under `honeypot-platform/hub/` and provides:
- ingest APIs for events/blobs
- lightweight HTML pages for browsing honeypots/sessions/events
- blob downloads by sha256

## Global .env
Use the shared env file at `honeypot-platform/.env` for hub + honeypot forwarding.

Required vars:
- `HOHO_HUB_URL`
- `HOHO_HUB_TOKEN`

Create it from template:
```bash
cp honeypot-platform/.env.example honeypot-platform/.env
```

Run hub from repo root:
```bash
docker compose --env-file honeypot-platform/.env \
  -f honeypot-platform/hub/docker-compose.yml up --build
```

[REDACTED]
```

### `honeypot-platform/docs/PACK_SPEC.md`  _(~2.1 KB; showing ≤800 lines)_
```md
# Honeypot Specification (v1)

> Historical name: "Pack Spec". Terminology now prefers **honeypot**.

## File + location
- Canonical file name: `honeypot.yaml`.
- Canonical path: `honeypots/{high,low}/<honeypot_id>/honeypot.yaml`.
- YAML is the standard format (`.yaml` / `.yml`). JSON input is still accepted by CLI when provided directly.

## Common top-level fields
- `apiVersion`: `hoho.dev/v1`
- `kind`: `HoneypotPack`
- `metadata`: includes `id`, `name`, `interaction`, `tags`, `description`
- `storage`: currently `backend: filesystem` + `root`
- `limits`: request/body/artifact limits
- `telemetry`: event emission + redaction controls
- `sensors`: optional for both low and high interaction honeypots

## Layout constraints
- `metadata.id` MUST match the folder name `<honeypot_id>`.
- Local relative paths in YAML must resolve inside the same honeypot folder.

## Low-interaction fields
- `listen`
- `responses` (optional)
- `behaviors`
- optional `sensors` that attach to the implicit runtime service named `honeypot`

## High-interaction fields
- `stack.runtime`
- `stack.services`
- optional `sensors`
  - includes high-interaction sensor type `falco` for runtime process telemetry and optional enforcement

## Validation rules
Schema validation runs first, then semantic checks:
- low interaction honeypots require `behaviors`
- high interaction honeypots require `stack`
- sensor attachment targets must exist:
  - high: targets must exist in `stack.services`
  - low: implicit service name `honeypot` is valid for sensor attachments

## Env compatibility note
Existing env naming is retained for compatibility:
- `HOHO_PACK_ID == honeypot_id`


## Falco sensor config (high only)
Supported keys under `sensors[].config` for `type: falco` include: `mode`, `engine`, `priority_min`, `rules`, `append_fields`, `any_exec`, and `enforce` (`enabled`, `match_priorities`, `match_rules`, `action`, `cooldown_seconds`).

Default rules are bundled in the Falco sensor image and always loaded first from `/app/rules/hoho_rules.yaml`.
Setting `any_exec: true` also loads `/app/rules/hoho_any_exec.yaml`.
Use `rules` to add custom rule files/overrides that load after these defaults.
```

### `honeypot-platform/docs/README.md`  _(~0.2 KB; showing ≤800 lines)_
```md
# Honeypot Platform Documentation

This directory contains architecture, honeypot specification, sensor, storage, deployment, and security guidance.

Primary layout reference: `docs/DIRECTORY_LAYOUT.md`.
```

### `honeypot-platform/docs/SECURITY.md`  _(~1.5 KB; showing ≤800 lines)_
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


## Egress Proxy + TLS MITM Safety
- Captured response bodies (including binaries) are untrusted and must be handled as malware-grade content.
- The generated MITM CA is honeypot-only; never reuse it in production or on analyst workstations.
[REDACTED]


## Falco sensor privilege model
- `falco` sensor currently uses privileged container mode and host mounts (including Docker socket) for runtime visibility and optional enforcement.
- Deploy this mode only on isolated honeypot hosts/VPCs dedicated to deception workloads.
- Treat Falco + Docker API access as high trust: do not co-locate with production workloads or analyst desktops.
```

### `honeypot-platform/docs/SENSORS.md`  _(~4.5 KB; showing ≤800 lines)_
```md
# Sensors

## Shared Contract
All sensors read common environment variables:
- `HOHO_PACK_ID` (legacy name; value equals `honeypot_id`)
- `HOHO_STORAGE_BACKEND=filesystem`
- `HOHO_STORAGE_ROOT=/artifacts`

`/artifacts` is a sensor/container mountpoint mapped to host `<storage.root>`.

Sensors append canonical events to `<root>/<honeypot_id>/index/events.jsonl` and write artifacts as content-addressed blobs.

## Attach model for low and high
- High interaction: attach to named services in `stack.services`.
- Low interaction: attach to the implicit runtime service named `honeypot`.

Example (low + sensors):
```yaml
sensors:
  - name: proxy-sensor
    type: proxy
    attach:
      service: honeypot
    config:
      upstream: http://honeypot:8088
  - name: pcap-sensor
    type: pcap
    attach:
      service: honeypot
```

## HTTP Proxy Sensor
- Built on mitmproxy reverse mode (`--mode reverse:<upstream>`).
- Captures request/response metadata and request body artifacts.
- Renderer joins proxy to attached service networks and applies fronting behavior:
  - Attached service published ports are removed.
  - Proxy publishes the same host ports to `listen_port` (default `8080`).

Runtime env used by renderer:
- `UPSTREAM` (required)
- `PROXY_LISTEN_PORT` (defaults to `8080`)
- `PROXY_LISTEN_HOST` (defaults to `0.0.0.0`)
- `PROXY_KEEP_HOST_HEADER` (`true`/`false`, defaults to `true`)

## Filesystem Monitor Sensor
- Watches configured directories for create/modify events.
- Applies allow/deny glob filters.
- Stores changed file content up to a cap and records preview text.

Runtime env used by renderer:
- `FSMON_WATCH` (comma-separated absolute paths)
- `FSMON_ALLOW` (comma-separated globs, defaults to `*`)
- `FSMON_DENY` (comma-separated globs)
- `FSMON_MAX_BYTES` (optional)

Important: fsmon cannot inspect a target container root filesystem directly. Watch paths must be backed by mounts shared with the fsmon sidecar.

## PCAP Sensor
- Uses tcpdump with rotation controls.
- Sidecar mode (`attach.service`) uses `network_mode: service:<target>`.
- Network mode (`attach.network`) joins the named network.
- Renderer adds required capabilities:
  - `NET_ADMIN`
  - `NET_RAW`
- Output is written under the honeypot artifacts tree (for example `run/artifacts/<honeypot_id>/...`).

Runtime env used by renderer:
- `PCAP_ROTATE_SECONDS`
- `PCAP_ROTATE_COUNT`
- `PCAP_INTERFACE`

## Egress Proxy Sensor
- Runs mitmproxy in explicit forward-proxy mode.
- Emits `sensor.egress_proxy.http` per flow with request/response metadata and redacted headers.
- Supports response-body capture with `capture.bodies: "*"` (default) or metadata-only with `"none"`.
- Persists mitmproxy confdir under artifacts (`run/artifacts/<id>/mitmproxy-conf/`).
- With `tls_mitm.enabled: true`, `hoho run` generates a runtime CA in compose runtime dir before startup.
- Runtime can execute `/hoho/ca/install-ca.sh` in attached services and emits `system.ca_install.succeeded` / `system.ca_install.failed` events.

## Operational Notes
Disk usage can grow quickly from uploads and pcap segments. Use external rotation, retention cleanup, and dedicated storage volumes.


## Falco Sensor
- High-interaction runtime behavior telemetry via Falco (process execution, shells, downloaders, network tools, interpreters).
- Renderer starts `falco-sensor` as privileged (MVP) with Modern eBPF engine by default.
- Default Hoho Falco rules are shipped in the image under `/app/rules/hoho_rules.yaml`.
- `any_exec: true` appends an additional noisy default rules file from `/app/rules/hoho_any_exec.yaml`.
- Falco writes one-line JSON alerts to a long-running forwarder via `program_output`.
- Forwarder emits `sensor.falco` canonical events to `<storage.root>/<honeypot_id>/index/events.jsonl`.
- Alerts are scoped to this compose stack by checking Docker labels (`com.docker.compose.project == hoho-<honeypot_id>`), with optional `attach.services` filtering.
- `sensors[].config.rules` adds extra rule files/overrides loaded after image defaults.
- Optional enforcement can stop offending container/service/stack and emit a corresponding enforcement event.
- Required mounts include `/sys/kernel/tracing`, `/proc`, `/etc`, and docker socket (`/var/run/docker.sock`) from host.

## Telemetry v2 additions
- All sensors emit `schema_version: 2` with `honeypot_id`, `session_id`, `agent_id`, and `event_name`.
- Runtime injects `HOHO_SESSION_ID`, `HOHO_AGENT_ID`, `HOHO_EMIT_FILTERS_JSON`, and `HOHO_FORWARD_FILTERS_JSON` into services/sensors.
[REDACTED]
```

### `honeypot-platform/docs/STORAGE_LAYOUT.md`  _(~0.5 KB; showing ≤800 lines)_
```md
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
```

### `honeypot-platform/docs/TELEMETRY_FILTERS.md`  _(~0.8 KB; showing ≤800 lines)_
```md
# Telemetry Filters

Rules are ordered and first-match wins. If no rule matches, the default action is `keep`.

Supported operators: `eq`, `neq`, `in`, `contains`, `regex`, `gte`, `lte`, `exists`.

Example:
```yaml
telemetry:
  filters:
    emit:
      - name: drop_noise
        when:
          all:
            - field: event_name
              eq: http.request
            - field: request.path
              in: ["/favicon.ico", "/robots.txt"]
        action: drop
    forward:
      - name: keep_interesting
        when:
          any:
            - field: classification.verdict
              in: ["exploit", "postex", "alert", "enforcement"]
            - field: response.status_code
              gte: 400
        action: keep
      - name: drop_rest
        action: drop
```
```

### `honeypot-platform/docs/TELEMETRY_FORWARDING.md`  _(~0.9 KB; showing ≤800 lines)_
```md
# Telemetry Forwarding

When `telemetry.forwarding.enabled: true`, compose adds `telemetry-forwarder`.

The forwarder:
- tails `run/artifacts/<honeypot_id>/index/events.jsonl`
- uploads missing blobs (`HEAD` then `PUT /api/v1/blobs/{sha}`)
- posts events to `POST /api/v1/events`
- persists cursor at `index/forwarder.cursor`

## Global .env
Use one shared env file at `honeypot-platform/.env`.

Variables:
- `HOHO_HUB_URL`
- `HOHO_HUB_TOKEN`
- `HOHO_FORWARD_FILTERS_JSON`

Template:
```bash
cp honeypot-platform/.env.example honeypot-platform/.env
```

`hoho` automatically loads `honeypot-platform/.env` and forwards it to docker compose with `--env-file` by default.

Override with:
```bash
hoho --env-file /path/to/custom.env run honeypots/high/<honeypot_id>/honeypot.yaml
```

## Pack contract example
```yaml
telemetry:
  forwarding:
    enabled: true
    hub_url: "${HOHO_HUB_URL}"
    token_env: "HOHO_HUB_TOKEN"
```
```

### `honeypot-platform/docs/runbooks/high-interaction-honeypot-from-cve.md`  _(~1.5 KB; showing ≤800 lines)_
```md
# Runbook: high-interaction honeypot from CVE

## Required layout
- Honeypot folder: `honeypot-platform/honeypots/high/<honeypot_id>/`
- Definition: `honeypot-platform/honeypots/high/<honeypot_id>/honeypot.yaml`
- Docs: `honeypot-platform/honeypots/high/<honeypot_id>/README.md`
- Optional assets/scripts: under same honeypot folder
- Compose output: `honeypot-platform/deploy/compose/<honeypot_id>/docker-compose.yml`
- Artifacts: `honeypot-platform/run/artifacts/<honeypot_id>/...`

## Workflow
1. Research target CVE and vulnerable stack.
2. Build `honeypot.yaml` under `honeypots/high/<honeypot_id>/`.
3. Add sensors for proxy/fsmon/pcap (plus egress_proxy when needed). 
4. When configuring fsmon watch_paths, always include common world-writable temp locations (/tmp, /var/tmp) plus the app's most likely writable/content directories
5. Write `README.md` (+ `reset.sh` if useful).
6. Validate, render compose, and run.

## Validation and run
```bash
PYTHONPATH=honeypot-platform/packages/hoho_core:honeypot-platform/packages/hoho_runtime \
  python -m hoho_runtime.cli validate honeypot-platform/honeypots/high/<honeypot_id>/honeypot.yaml

PYTHONPATH=honeypot-platform/packages/hoho_core:honeypot-platform/packages/hoho_runtime \
  python -m hoho_runtime.cli render-compose honeypot-platform/honeypots/high/<honeypot_id>/honeypot.yaml

PYTHONPATH=honeypot-platform/packages/hoho_core:honeypot-platform/packages/hoho_runtime \
  python -m hoho_runtime.cli run honeypot-platform/honeypots/high/<honeypot_id>
```
```

### `honeypot-platform/docs/runbooks/low-interaction-honeypot-from-cve.md`  _(~1.0 KB; showing ≤800 lines)_
```md
# Runbook: low-interaction honeypot from CVE

## Required layout
- Honeypot folder: `honeypot-platform/honeypots/low/<honeypot_id>/`
- Definition: `honeypot-platform/honeypots/low/<honeypot_id>/honeypot.yaml`
- Docs: `honeypot-platform/honeypots/low/<honeypot_id>/README.md`
- Compose output: `honeypot-platform/deploy/compose/<honeypot_id>/docker-compose.yml`
- Artifacts: `honeypot-platform/run/artifacts/<honeypot_id>/...`

## Workflow
1. Research CVE protocol surface and request patterns.
2. Implement `honeypot.yaml` at `honeypots/low/<honeypot_id>/`.
3. Document operation in `README.md`.
4. Validate and run.

## Validation and run
```bash
PYTHONPATH=honeypot-platform/packages/hoho_core:honeypot-platform/packages/hoho_runtime \
  python -m hoho_runtime.cli validate honeypot-platform/honeypots/low/<honeypot_id>/honeypot.yaml

PYTHONPATH=honeypot-platform/packages/hoho_core:honeypot-platform/packages/hoho_runtime \
  python -m hoho_runtime.cli run honeypot-platform/honeypots/low/<honeypot_id>
```
```

### `honeypot-platform/honeypots/high/cve-2017-12629_solr_rce/README.md`  _(~1.2 KB; showing ≤800 lines)_
```md
# High-Interaction Honeypot: Apache Solr CVE-2017-12629

## Honeypot ID
- `honeypot_id`: `cve-2017-12629_solr_rce`
- Pack YAML: `honeypot-platform/packs/high/cve-2017-12629_solr_rce.yaml`

## Run
From `honeypot-platform/`:

```bash
hoho validate packs/high/cve-2017-12629_solr_rce.yaml
hoho run packs/high/cve-2017-12629_solr_rce.yaml
```

Manual compose flow:

```bash
hoho render-compose packs/high/cve-2017-12629_solr_rce.yaml
docker compose -f deploy/compose/cve-2017-12629_solr_rce/docker-compose.yml up -d
```

## Stop

```bash
docker compose -p hoho-cve-2017-12629_solr_rce -f deploy/compose/cve-2017-12629_solr_rce/docker-compose.yml down -v
```

## Artifacts
Artifacts are always written to:

- `honeypot-platform/run/artifacts/cve-2017-12629_solr_rce/`

Simple Layout v1 intentionally overwrites this folder for each new run.

## Notes
- The stack runs Solr 7.1 (`solr-precreate gettingstarted`) and fronts it with the reverse proxy sensor.
- Captures include inbound request metadata/body (`proxy`), filesystem writes under `/var/solr` (`fsmon`), packet traces (`pcap`), and outbound downloads (`egress_proxy`).

## One-command reset
Use:

```bash
./honeypot-platform/honeypots/high/cve-2017-12629_solr_rce/reset.sh
```
```

### `honeypot-platform/honeypots/high/cve-2017-12629_solr_rce/honeypot.yaml`  _(~1.7 KB; showing ≤800 lines)_
```yaml
apiVersion: hoho.dev/v1
kind: HoneypotPack
metadata:
  id: cve-2017-12629_solr_rce
  name: cve-2017-12629_solr_rce
  interaction: high
  tags:
    - web
    - apache-solr
    - cve-2017-12629
    - rce
  description: Apache Solr 7.1.0 high-interaction stack with DIH-oriented telemetry capture for CVE-2017-12629.
storage:
  backend: filesystem
  root: ./run/artifacts
telemetry:
  emit_events: true
  redact_headers:
[REDACTED]
    - Cookie
stack:
  runtime: compose
  services:
    solr:
      image: solr:7.0.1
      command:
        - solr-precreate
        - gettingstarted
      ports:
        - 8097:8983
      volumes:
        - solrdata:/var/solr
        - tmpdata:/tmp
      networks:
        - frontend
sensors:
  - name: proxy-sensor
    type: proxy
    config:
      upstream: http://solr:8983
      listen_port: 8080
      keep_host_header: true
    attach:
      service: solr
  - name: fsmon-sensor
    type: fsmon
    config:
      watch:
        - /var/solr
        - /tmp
      allow_globs:
        - "**"
      deny_globs:
        - "**/*.log"
      max_bytes: 524288
    attach:
      service: solr
  - name: pcap-sensor
    type: pcap
    config:
      interface: any
      rotate_seconds: 60
      rotate_count: 20
    attach:
      service: proxy-sensor
  - name: egress
    type: egress_proxy
    attach:
      services: ["solr"]
    config:
      listen_host: "0.0.0.0"
      listen_port: 3128
      force_egress_via_proxy: false
      tls_mitm:
        enabled: true
        install_trust:
          also_set_env_bundles: true
          extra_commands: []
      capture:
        enabled: true
        bodies: "*"
        max_bytes: 52428800
        store_ok_only: true
        min_bytes: 1
        redact_headers: [REDACTED]
```

### `honeypot-platform/honeypots/high/cve-2017-12629_solr_rce/reset.sh`  _(~0.8 KB; showing ≤800 lines)_
```bash
#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$(cd "${SCRIPT_DIR}/../../.." && pwd)"
HONEYPOT_ID="cve-2017-12629_solr_rce"
PACK="${ROOT_DIR}/packs/high/${HONEYPOT_ID}.yaml"
ARTIFACT_DIR="${ROOT_DIR}/run/artifacts/${HONEYPOT_ID}"
COMPOSE_DIR="${ROOT_DIR}/deploy/compose/${HONEYPOT_ID}"
COMPOSE_FILE="${COMPOSE_DIR}/docker-compose.yml"
PROJECT_NAME="hoho-${HONEYPOT_ID}"

if [ -f "${COMPOSE_FILE}" ]; then
  docker compose -p "${PROJECT_NAME}" -f "${COMPOSE_FILE}" down -v || true
fi

rm -rf "${ARTIFACT_DIR}" "${COMPOSE_DIR}"

(
  cd "${ROOT_DIR}"
  PYTHONPATH="packages/hoho_core:packages/hoho_runtime" python -m hoho_runtime.cli render-compose "${PACK}"
)

docker compose -p "${PROJECT_NAME}" -f "${COMPOSE_FILE}" up -d

echo "honeypot_id=${HONEYPOT_ID}"
echo "artifacts=run/artifacts/${HONEYPOT_ID}/"
```

### `honeypot-platform/honeypots/high/cve-2020-25213_wp_file_upload/README.md`  _(~0.1 KB; showing ≤800 lines)_
```md
# cve-2020-25213_wp_file_upload

Migrated honeypot. Document setup, run steps, and reset procedures here.
```

### `honeypot-platform/honeypots/high/cve-2020-25213_wp_file_upload/honeypot.yaml`  _(~3.7 KB; showing ≤800 lines)_
```yaml
apiVersion: hoho.dev/v1
kind: HoneypotPack
metadata:
  id: cve-2020-25213_wp_file_upload
  name: cve-2020-25213
  interaction: high
  tags:
    - web
    - stack
    - wordpress
  description: WordPress + MariaDB high-interaction stack with fsmon, proxy, and pcap sidecars.
storage:
  backend: filesystem
  root: ./run/artifacts
telemetry:
  emit_events: true
  redact_headers:
[REDACTED]
    - Cookie
  forwarding:
    enabled: true
    hub_url: "${HOHO_HUB_URL}"
    token_env: "HOHO_HUB_TOKEN"
stack:
  runtime: compose
  services:
    db:
      image: mariadb:11
      environment:
        MARIADB_DATABASE: wordpress
        MARIADB_USER: wordpress
        MARIADB_PASSWORD: wordpress
        MARIADB_ROOT_PASSWORD: rootpass
      volumes:
        - dbdata:/var/lib/mysql
      networks:
        - frontend
    web:
      image: funway/cve-2020-25213
      depends_on:
        - db
      environment:
        WORDPRESS_DB_HOST: db:3306
        WORDPRESS_DB_USER: wordpress
        WORDPRESS_DB_PASSWORD: wordpress
        WORDPRESS_DB_NAME: wordpress
      ports:
        - 8088:80
      volumes:
        - webdata:/var/www/html
      networks:
        - frontend
sensors:
  - name: proxy-sensor
    type: proxy
    config:
      upstream: http://web:80
      listen_port: 8080
    attach:
      service: web
  - name: fsmon-sensor
    type: fsmon
    config:
      watch:
        - /var/www/html
        - /var/www/html/wp-content/uploads
      allow_globs:
        - "**"
      deny_globs:
        - "**/cache/**"
      max_bytes: 262144
    attach:
      service: web
  - name: pcap-sensor
    type: pcap
    config:
      interface: any
      rotate_seconds: 60
      rotate_count: 10
    attach:
      service: web
  - name: egress
    type: egress_proxy
    attach:
      services: ["web"]    # list of stack service names to proxy egress for
    config:
      listen_host: "0.0.0.0"
      listen_port: 3128

      force_egress_via_proxy: false

      tls_mitm:
        enabled: true
        install_trust:
          also_set_env_bundles: true  # SSL_CERT_FILE/REQUESTS_CA_BUNDLE/CURL_CA_BUNDLE/NODE_EXTRA_CA_CERTS
          extra_commands: []          # optional extra per-image commands

      capture:
        enabled: true
        bodies: "*"                # DEFAULT: capture all response bodies
        max_bytes: 52428800        # 50MB cap per response
        store_ok_only: true        # default true (2xx/3xx)
        min_bytes: 1               # default 1 (set higher if you want to reduce noise)
        redact_headers: [REDACTED]
  - name: falco-sensor
    type: falco
    attach:
      services: ["web"]          # stack service(s) to scope on (optional but recommended)
    config:
      # Falco runtime mode (renderer supports "privileged"; runs with host net + mounts)
      mode: privileged

      # Falco engine (default is modern_ebpf)
      engine: modern_ebpf

      # Minimum Falco priority to emit
      priority_min: Warning

      # If true, default rules become more "any exec" noisy (good for RCE labs)
      any_exec: true

      # Extra fields appended into emitted events (comma-joined list)
      append_fields:
        - honeypot_id=cve-2021-41773_42013_apache_rce
        - sensor=falco

      # Optional: add your own rules files.
      # Defaults are always loaded from /app/rules/hoho_rules.yaml in the Falco image,
      # then custom files from this honeypot are appended after defaults.
      rules:
        - ./falco/custom_rules.yaml

      # Optional enforcement (OFF by default)
      enforce:
        enabled: false
        match_priorities: ["Critical", "Error"]
        match_rules: []
        action: stop_container       # stop_container | stop_service | stop_stack
        cooldown_seconds: 60
```

### `honeypot-platform/honeypots/high/cve-2021-41773_42013_apache_rce/README.md`  _(~0.9 KB; showing ≤800 lines)_
```md
# High-Interaction Honeypot: CVE-2021-41773 / CVE-2021-42013

## Honeypot ID
- `honeypot_id`: `cve-2021-41773_42013`
- Pack YAML: `honeypot-platform/packs/high/cve-2021-41773_42013.yaml`

## Run
From `honeypot-platform/`:

```bash
hoho validate packs/high/cve-2021-41773_42013.yaml
hoho run packs/high/cve-2021-41773_42013.yaml
```

Manual compose flow:

```bash
hoho render-compose packs/high/cve-2021-41773_42013.yaml
docker compose -f deploy/compose/cve-2021-41773_42013/docker-compose.yml up -d
```

## Stop

```bash
docker compose -p hoho-cve-2021-41773_42013 -f deploy/compose/cve-2021-41773_42013/docker-compose.yml down -v
```

## Artifacts
Artifacts are always written to:

- `honeypot-platform/run/artifacts/cve-2021-41773_42013/`

Simple Layout v1 intentionally overwrites this folder for each new run.

## One-command reset
Use:

```bash
./honeypot-platform/honeypots/high/cve-2021-41773_42013/reset.sh
```
```

### `honeypot-platform/honeypots/high/cve-2021-41773_42013_apache_rce/cve-2021-41773_42013/cgi-bin/health.sh`  _(~0.1 KB; showing ≤800 lines)_
```bash
#!/bin/sh
echo "Content-Type: text/plain"
echo ""
echo "ok"
```

### `honeypot-platform/honeypots/high/cve-2021-41773_42013_apache_rce/cve-2021-41773_42013/htdocs/index.html`  _(~0.3 KB; showing ≤800 lines)_
```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Apache HTTP Server Test Page</title>
  </head>
  <body>
    <h1>It works!</h1>
    <p>Apache httpd service is online.</p>
    <p>Build profile: 2.4.49-compatible layout for research capture.</p>
  </body>
</html>
```

### `honeypot-platform/honeypots/high/cve-2021-41773_42013_apache_rce/falco/custom_rules.yaml`  _(~0.2 KB; showing ≤800 lines)_
```yaml
# Optional per-honeypot Falco overrides loaded after image defaults.
# Example disabled rule override:
# - rule: Hoho Any Exec in Container
#   enabled: false
```

### `honeypot-platform/honeypots/high/cve-2021-41773_42013_apache_rce/honeypot.yaml`  _(~3.4 KB; showing ≤800 lines)_
```yaml
apiVersion: hoho.dev/v1
kind: HoneypotPack
metadata:
  id: cve-2021-41773_42013_apache_rce
  name: cve-2021-41773_42013_apache_rce
  interaction: high
  tags:
    - web
    - apache
    - cve-2021-41773
    - cve-2021-42013
  description: Apache httpd 2.4.49/2.4.50 high-interaction stack with traversal/RCE-oriented telemetry capture.
storage:
  backend: filesystem
  root: ./run/artifacts
telemetry:
  emit_events: true
  redact_headers:
[REDACTED]
    - Cookie
stack:
  runtime: compose
  services:
    apache:
      image: blueteamsteve/cve-2021-41773:with-cgid
      ports:
        - 8096:80
      volumes:
        - ./cve-2021-41773_42013/htdocs:/usr/local/apache2/htdocs
        - ./cve-2021-41773_42013/cgi-bin:/usr/local/apache2/cgi-bin
        - tmpdata:/tmp
      networks:
        - frontend
        - hp_internal
        - hp_external
sensors:
  - name: proxy-sensor
    type: proxy
    config:
      upstream: http://apache:80
      listen_port: 8080
    attach:
      service: apache
  - name: fsmon-sensor
    type: fsmon
    config:
      watch:
        - /usr/local/apache2/htdocs
        - /usr/local/apache2/cgi-bin
        - /tmp
      allow_globs:
        - "**"
      deny_globs:
        - "**/*.log"
      max_bytes: 524288
    attach:
      service: apache
  - name: pcap-sensor
    type: pcap
    config:
      interface: any
      rotate_seconds: 60
      rotate_count: 20
    attach:
      service: apache
  - name: egress
    type: egress_proxy
    attach:
      services: ["apache"]    # list of stack service names to proxy egress for
    config:
      listen_host: "0.0.0.0"
      listen_port: 3128

      force_egress_via_proxy: false

      tls_mitm:
        enabled: true
        install_trust:
          also_set_env_bundles: true  # SSL_CERT_FILE/REQUESTS_CA_BUNDLE/CURL_CA_BUNDLE/NODE_EXTRA_CA_CERTS
          extra_commands: []          # optional extra per-image commands

      capture:
        enabled: true
        bodies: "*"                # DEFAULT: capture all response bodies
        max_bytes: 52428800        # 50MB cap per response
        store_ok_only: true        # default true (2xx/3xx)
        min_bytes: 1               # default 1 (set higher if you want to reduce noise)
        redact_headers: [REDACTED]
  - name: falco-sensor
    type: falco
    attach:
      services: ["apache"]          # stack service(s) to scope on (optional but recommended)
    config:
      # Falco runtime mode (renderer supports "privileged"; runs with host net + mounts)
      mode: privileged

      # Falco engine (default is modern_ebpf)
      engine: modern_ebpf

      # Minimum Falco priority to emit
      priority_min: Warning

      # If true, default rules become more "any exec" noisy (good for RCE labs)
      any_exec: true

      # Extra fields appended into emitted events (comma-joined list)
      append_fields:
        - honeypot_id=cve-2021-41773_42013_apache_rce
        - sensor=falco

      # Optional: add your own rules files.
      # Defaults are always loaded from /app/rules/hoho_rules.yaml in the Falco image,
      # then custom files from this honeypot are appended after defaults.
      rules:
        - ./falco/custom_rules.yaml

      # Optional enforcement (OFF by default)
      enforce:
        enabled: false
        match_priorities: ["Critical", "Error"]
        match_rules: []
        action: stop_container       # stop_container | stop_service | stop_stack
        cooldown_seconds: 60
```

### `honeypot-platform/honeypots/high/cve-2021-41773_42013_apache_rce/reset.sh`  _(~0.8 KB; showing ≤800 lines)_
```bash
#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$(cd "${SCRIPT_DIR}/../../.." && pwd)"
HONEYPOT_ID="cve-2021-41773_42013"
PACK="${ROOT_DIR}/packs/high/${HONEYPOT_ID}.yaml"
ARTIFACT_DIR="${ROOT_DIR}/run/artifacts/${HONEYPOT_ID}"
COMPOSE_DIR="${ROOT_DIR}/deploy/compose/${HONEYPOT_ID}"
COMPOSE_FILE="${COMPOSE_DIR}/docker-compose.yml"
PROJECT_NAME="hoho-${HONEYPOT_ID}"

if [ -f "${COMPOSE_FILE}" ]; then
  docker compose -p "${PROJECT_NAME}" -f "${COMPOSE_FILE}" down -v || true
fi

rm -rf "${ARTIFACT_DIR}" "${COMPOSE_DIR}"

(
  cd "${ROOT_DIR}"
  PYTHONPATH="packages/hoho_core:packages/hoho_runtime" python -m hoho_runtime.cli render-compose "${PACK}"
)

docker compose -p "${PROJECT_NAME}" -f "${COMPOSE_FILE}" up -d

echo "honeypot_id=${HONEYPOT_ID}"
echo "artifacts=run/artifacts/${HONEYPOT_ID}/"
```

### `honeypot-platform/honeypots/high/example-wp-stack/README.md`  _(~0.1 KB; showing ≤800 lines)_
```md
# example-wp-stack

Migrated honeypot. Document setup, run steps, and reset procedures here.
```

### `honeypot-platform/honeypots/high/example-wp-stack/honeypot.yaml`  _(~1.6 KB; showing ≤800 lines)_
```yaml
apiVersion: hoho.dev/v1
kind: HoneypotPack
metadata:
  id: example-wp-stack
  name: Example High-Interaction WordPress Stack
  interaction: high
  tags:
    - web
    - stack
    - wordpress
  description: WordPress + MariaDB high-interaction stack with fsmon, proxy, and pcap sidecars.
storage:
  backend: filesystem
  root: ./run/artifacts
telemetry:
  emit_events: true
  redact_headers:
[REDACTED]
    - Cookie
stack:
  runtime: compose
  services:
    db:
      image: mariadb:11
      environment:
        MARIADB_DATABASE: wordpress
        MARIADB_USER: wordpress
        MARIADB_PASSWORD: wordpress
        MARIADB_ROOT_PASSWORD: rootpass
      volumes:
        - dbdata:/var/lib/mysql
      networks:
        - frontend
    web:
      image: wordpress:6-apache
      depends_on:
        - db
      environment:
        WORDPRESS_DB_HOST: db:3306
        WORDPRESS_DB_USER: wordpress
        WORDPRESS_DB_PASSWORD: wordpress
        WORDPRESS_DB_NAME: wordpress
      ports:
        - 8088:80
      volumes:
        - webdata:/var/www/html
      networks:
        - frontend
sensors:
  - name: proxy-sensor
    type: proxy
    config:
      upstream: http://web:80
      listen_port: 8080
    attach:
      service: web
  - name: fsmon-sensor
    type: fsmon
    config:
      watch:
        - /var/www/html
        - /var/www/html/wp-content/uploads
      allow_globs:
        - "**"
      deny_globs:
        - "**/cache/**"
      max_bytes: 262144
    attach:
      service: web
  - name: pcap-sensor
    type: pcap
    config:
      interface: any
      rotate_seconds: 60
      rotate_count: 10
    attach:
      service: proxy-sensor
```

### `honeypot-platform/honeypots/low/cve-2021-41773_apache-2-4-49-2-4-50-traversal-rce/README.md`  _(~3.2 KB; showing ≤800 lines)_
```md
# Apache httpd 2.4.49/2.4.50 Traversal + RCE (low-interaction)

## CVE profile
- **Primary CVEs:** CVE-2021-41773 (path traversal / file read) and CVE-2021-42013 (incomplete fix bypass, enabling traversal and CGI RCE patterns).
- **Product:** Apache HTTP Server (`httpd`) 2.4.49 and 2.4.50.
- **Vulnerability family:** Path normalization bypass with traversal into sensitive filesystem paths; when CGI is enabled, traversal to shell binaries can be used for command execution attempts.
- **Exposed surface:** HTTP on common web ports, especially paths under `/cgi-bin/` and sometimes `/icons/` with encoded traversal segments.
- **Attacker objectives:**
[REDACTED]
  - Reach CGI-capable executable paths (for example shell entrypoints) and send command-style bodies.

## Transcript-derived request patterns emulated

### Primary probes
1. **Traversal file-read probe (`GET`)**
   - Distinctive structure: [REDACTED]
[REDACTED]

2. **Traversal-to-CGI RCE probe (`POST`)**
   - Distinctive structure: encoded traversal path ending in `bin/sh` under `/cgi-bin/`.
   - Emulated by behavior `cgi-rce-binsh-probe`.
   - Request body is stored as compressed artifact for analysis.

3. **Double-encoded traversal normalization probe (`GET`)**
   - Distinctive structure: double-encoded dot segments (`%%32%65` style) plus sensitive target path.
   - Emulated by behavior `traversal-normalization-probe`.

### Secondary follow-up
- `GET /` landing probe with Apache-like banner and “It works!” response.

### Negative matching intent
- The pack does **not** match only on user-agent.
- The pack does **not** require exact payload command strings.
- Matching focuses on stable path/encoding traits to avoid overfitting.

## Telemetry contract
- Global tags in metadata:
  - `cve:2021-41773`
  - `cve:2021-42013`
  - `product:apache-httpd`
  - `technique:path-traversal`
  - `technique:rce`
- Verdicts emitted: `probe`, `exploit`, `unknown`.
- Indicators used:
  - `file-read-probe`
  - `cgi-bin-sh-exec`
  - `double-encoded-dot-segments`
- Header redaction: [REDACTED]
- Body capture: enabled for `POST` CGI RCE probe (`store_body` with gzip).

## How to run
From the repository root:

```bash
python -m hoho_runtime.cli validate honeypot-platform/packs/low/cve-2021-41773_apache-2-4-49-2-4-50-traversal-rce.yaml
PYTHONPATH=honeypot-platform/packages/hoho_core:honeypot-platform/packages/hoho_runtime \
  python -m hoho_runtime.cli run honeypot-platform/packs/low/cve-2021-41773_apache-2-4-49-2-4-50-traversal-rce.yaml
```

## Harmless test requests

```bash
curl -i http://127.0.0.1:8088/
curl -i "http: [REDACTED]
curl -i -X POST "http://127.0.0.1:8088/cgi-bin/.%2e/%2e%2e/%2e%2e/%2e%2e/bin/sh" -d "echo test"
```

## Known limitations
- This is behavioral emulation only; no real Apache parser, CGI runtime, or filesystem access exists.
- Only selected transcript patterns are emulated; many variants may hit the default `404`/`unknown` rule.
- Response bodies are intentionally minimal to avoid acting as a real vulnerable target.
```

### `honeypot-platform/honeypots/low/cve-2021-41773_apache-2-4-49-2-4-50-traversal-rce/honeypot.yaml`  _(~3.5 KB; showing ≤800 lines)_
```yaml
apiVersion: hoho.dev/v1
kind: HoneypotPack
metadata:
  id: cve-2021-41773_apache-2-4-49-2-4-50-traversal-rce
  name: Apache httpd 2.4.49/2.4.50 Traversal + RCE (low)
  interaction: low
  tags:
    - cve
    - cve:2021-41773
    - cve:2021-42013
    - product:apache-httpd
    - technique:path-traversal
    - technique:rce
  description: >
    Low-interaction emulation for Apache httpd 2.4.49/2.4.50 path traversal and
    CGI RCE probe traffic. Captures exploit attempts and returns plausible
    Apache-style responses without running vulnerable software.
storage:
  backend: filesystem
  root: ./run/artifacts
limits:
  max_body_bytes: 1048576
  max_upload_bytes: 10485760
  max_artifacts_per_request: 5
telemetry:
  emit_events: true
  redact_headers:
[REDACTED]
    - Cookie
listen:
  - host: 0.0.0.0
    port: 8088
behaviors:
  - name: [REDACTED]
    match:
      method: GET
      pathRegex: [REDACTED]
    actions:
      - emit_event:
          verdict: exploit
          tags:
            - cve:2021-41773
            - cve:2021-42013
            - product:apache-httpd
            - technique:path-traversal
          indicators:
            - file-read-probe
      - delay:
          ms: 120
          jitterMs: 80
    respond:
      status: 200
      headers:
        Content-Type: text/plain
        Server: Apache/2.4.49 (Unix)
      body: "root:x:0:0:root:/root:/bin/bash\nwww-data:x:33:33:www-data:/var/www:/usr/sbin/nologin\n"

  - name: cgi-rce-binsh-probe
    match:
      method: POST
      pathRegex: "^/cgi-bin/.*(%2e|\\.){1,2}(%2f|/).*(bin/sh)$"
    actions:
      - emit_event:
          verdict: exploit
          tags:
            - cve:2021-41773
            - cve:2021-42013
            - product:apache-httpd
            - technique:rce
          indicators:
            - cgi-bin-sh-exec
      - store_body:
          kind: request_body
          gzip: true
      - delay:
          ms: 180
          jitterMs: 120
    respond:
      status: 200
      headers:
        Content-Type: text/plain
        Server: Apache/2.4.50 (Unix)
      body: "Status: 200\nContent-Type: text/plain\n\n"

  - name: traversal-normalization-probe
    match:
      method: GET
      pathRegex: [REDACTED]
    actions:
      - emit_event:
          verdict: exploit
          tags:
            - cve:2021-42013
            - product:apache-httpd
            - technique:path-traversal
          indicators:
            - double-encoded-dot-segments
      - delay:
          ms: 140
          jitterMs: 90
    respond:
      status: 403
      headers:
        Content-Type: text/html
        Server: Apache/2.4.50 (Unix)
      body: "<html><body><h1>403 Forbidden</h1></body></html>"

  - name: server-root
    match:
      method: GET
      path: /
    actions:
      - emit_event:
          verdict: probe
          tags:
            - product:apache-httpd
            - landing
          indicators: []
    respond:
      status: 200
      headers:
        Content-Type: text/html
        Server: Apache/2.4.49 (Unix)
      body: "<html><body><h1>It works!</h1></body></html>"

  - name: default
    match:
      pathGlob: "/*"
    actions:
      - emit_event:
          verdict: unknown
          tags:
            - product:apache-httpd
          indicators: []
    respond:
      status: 404
      headers:
        Content-Type: text/plain
        Server: Apache/2.4.49 (Unix)
      body: "Not Found"
```

### `honeypot-platform/honeypots/low/example-upload-sink/README.md`  _(~0.1 KB; showing ≤800 lines)_
```md
# example-upload-sink

Migrated honeypot. Document setup, run steps, and reset procedures here.
```

### `honeypot-platform/honeypots/low/example-upload-sink/honeypot.yaml`  _(~1.0 KB; showing ≤800 lines)_
```yaml
apiVersion: hoho.dev/v1
kind: HoneypotPack
metadata:
  id: example-upload-sink
  name: Upload Sink Honeypot
  interaction: low
  tags:
    - upload
    - api
  description: Accepts multipart and stores uploads as artifacts.
storage:
  backend: filesystem
  root: ./run/artifacts
limits:
  max_body_bytes: 2097152
  max_upload_bytes: 10485760
  max_artifacts_per_request: 5
telemetry:
  emit_events: true
  redact_headers:
[REDACTED]
    - Cookie
listen:
  - host: 0.0.0.0
    port: 8081
behaviors:
  - name: upload-api
    match:
      method: POST
      path: /api/upload
      contentTypeContains: multipart/form-data
    actions:
      - emit_event:
          verdict: upload
          tags:
            - multipart
          indicators:
            - file-upload
      - store_body:
          kind: request_body
          gzip: true
      - respond:
          status: 201
          headers:
            Content-Type: application/json
          body: '{"ok":true,"id":"fake-123"}'
```

### `honeypot-platform/honeypots/low/example-web/README.md`  _(~0.1 KB; showing ≤800 lines)_
```md
# example-web

Migrated honeypot. Document setup, run steps, and reset procedures here.
```

### `honeypot-platform/honeypots/low/example-web/honeypot.yaml`  _(~1.4 KB; showing ≤800 lines)_
```yaml
apiVersion: hoho.dev/v1
kind: HoneypotPack
metadata:
  id: example-web
  name: Example Web Honeypot
  interaction: low
  tags:
    - web
    - probe
  description: Basic web decoy with fake server banner.
storage:
  backend: filesystem
  root: ./run/artifacts
limits:
  max_body_bytes: 1048576
  max_upload_bytes: 10485760
  max_artifacts_per_request: 3
telemetry:
  emit_events: true
  redact_headers:
[REDACTED]
    - Cookie
listen:
  - host: 0.0.0.0
    port: 8088
behaviors:
  - name: root-page
    match:
      method: GET
      path: /
    actions:
      - emit_event:
          verdict: probe
          tags:
            - landing
          indicators: []
    respond:
      status: 200
      headers:
        Content-Type: text/html
        Server: Apache/2.4.41
      body: "<html><body><h1>It works</h1></body></html>"
  - name: admin-probe
    match:
      pathGlob: /admin*
    actions:
      - emit_event:
          verdict: exploit
          tags:
            - admin-probe
          indicators:
            - admin-path
    respond:
      status: 403
      headers:
        Content-Type: text/plain
      body: forbidden

sensors:
  - name: proxy-sensor
    type: proxy
    config:
      upstream: http://honeypot:8088
      listen_port: 8080
    attach:
      service: honeypot
  - name: pcap-sensor
    type: pcap
    config:
      interface: any
      rotate_seconds: 60
      rotate_count: 10
    attach:
      service: honeypot
```

### `honeypot-platform/hub/Dockerfile`  _(~0.2 KB; showing ≤800 lines)_
```
FROM python:3.11-slim
WORKDIR /app
COPY app /app/app
RUN pip install --no-cache-dir fastapi uvicorn jinja2
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### `honeypot-platform/hub/app/db.py`  _(~2.2 KB; showing ≤800 lines)_
```python
import json
import sqlite3
from pathlib import Path


class HubDB:
    def __init__(self, path: Path):
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(str(path), check_same_thread=False)
        self.conn.execute(
            """
            create table if not exists events(
              event_id text primary key,
              honeypot_id text,
              session_id text,
              ts text,
              event_name text,
              component text,
              verdict text,
              tags text,
              raw_json text
            )
            """
        )
        self.conn.execute(
            """
            create table if not exists sessions(
              honeypot_id text,
              session_id text,
              agent_id text,
              started_ts text,
              last_seen_ts text,
              primary key(honeypot_id, session_id)
            )
            """
        )
        self.conn.commit()

    def insert_event(self, event: dict):
        tags = event.get("classification", {}).get("tags", [])
        self.conn.execute(
            "insert or replace into events(event_id,honeypot_id,session_id,ts,event_name,component,verdict,tags,raw_json) values(?,?,?,?,?,?,?,?,?)",
            (
                event.get("event_id"),
                event.get("honeypot_id") or event.get("pack_id"),
                event.get("session_id"),
                event.get("ts"),
                event.get("event_name"),
                event.get("component"),
                event.get("classification", {}).get("verdict"),
                json.dumps(tags),
                json.dumps(event),
            ),
        )
        self.conn.execute(
            "insert into sessions(honeypot_id,session_id,agent_id,started_ts,last_seen_ts) values(?,?,?,?,?) "
            "on conflict(honeypot_id,session_id) do update set last_seen_ts=excluded.last_seen_ts",
            (
                event.get("honeypot_id") or event.get("pack_id"),
                event.get("session_id"),
                event.get("agent_id"),
                event.get("ts"),
                event.get("ts"),
            ),
        )
        self.conn.commit()
```

### `honeypot-platform/hub/app/main.py`  _(~3.4 KB; showing ≤800 lines)_
```python
import hashlib
import json
import os
from pathlib import Path

from fastapi import FastAPI, Header, HTTPException, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

from .db import HubDB

DATA = Path(os.getenv("HOHO_HUB_DATA", "./data"))
BLOBS = DATA / "blobs"
TOKEN =[REDACTED]
DB = HubDB(DATA / "hub.db")
app = FastAPI()
templates = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))


def _auth(authorization: [REDACTED]
    if not TOKEN: [REDACTED]
        return
    bearer =[REDACTED]
    if bearer !=[REDACTED]
        raise HTTPException(status_code=401, detail="unauthorized")


@app.put("/api/v1/blobs/{sha}")
async def put_blob(sha: str, request: Request, authorization: str | None =[REDACTED]
[REDACTED]
    data = await request.body()
    if hashlib.sha256(data).hexdigest() != sha:
        raise HTTPException(status_code=400, detail="sha mismatch")
    p = BLOBS / sha[:2] / sha
    p.parent.mkdir(parents=True, exist_ok=True)
    if not p.exists():
        p.write_bytes(data)
    return {"ok": True}


@app.head("/api/v1/blobs/{sha}")
def head_blob(sha: str):
    p = BLOBS / sha[:2] / sha
    if not p.exists():
        raise HTTPException(status_code=404)
    return {}


@app.post("/api/v1/events")
def post_event(event: dict, authorization: str | None =[REDACTED]
[REDACTED]
    if "honeypot_id" not in event and "pack_id" in event:
        event["honeypot_id"] = event["pack_id"]
    DB.insert_event(event)
    return {"ok": True}


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    rows = DB.conn.execute("select distinct honeypot_id from events order by honeypot_id").fetchall()
    return templates.TemplateResponse("index.html", {"request": request, "rows": rows})


@app.get("/honeypots/{honeypot_id}", response_class=HTMLResponse)
def sessions(request: Request, honeypot_id: str):
    rows = DB.conn.execute("select session_id, agent_id, started_ts, last_seen_ts from sessions where honeypot_id=? order by last_seen_ts desc", (honeypot_id,)).fetchall()
    return templates.TemplateResponse("sessions.html", {"request": request, "honeypot_id": honeypot_id, "rows": rows})


@app.get("/honeypots/{honeypot_id}/sessions/{session_id}", response_class=HTMLResponse)
def events(request: Request, honeypot_id: str, session_id: str):
    rows = DB.conn.execute("select event_id, ts, event_name, component, verdict from events where honeypot_id=? and session_id=? order by ts desc", (honeypot_id, session_id)).fetchall()
    return templates.TemplateResponse("events.html", {"request": request, "honeypot_id": honeypot_id, "session_id": session_id, "rows": rows})


@app.get("/events/{event_id}", response_class=HTMLResponse)
def event_detail(request: Request, event_id: str):
    row = DB.conn.execute("select raw_json from events where event_id=?", (event_id,)).fetchone()
    event = json.loads(row[0]) if row else {}
    return templates.TemplateResponse("event.html", {"request": request, "event": event})


@app.get("/blobs/{sha}")
def download_blob(sha: str):
    p = BLOBS / sha[:2] / sha
    if not p.exists():
        raise HTTPException(status_code=404)
    return FileResponse(str(p), filename=sha)
```

### `honeypot-platform/hub/app/templates/event.html`  _(~0.0 KB; showing ≤800 lines)_
```html
<h1>Event</h1><pre>{{event}}</pre>
```

### `honeypot-platform/hub/app/templates/events.html`  _(~0.2 KB; showing ≤800 lines)_
```html
<h1>Events {{honeypot_id}}/{{session_id}}</h1>
<ul>{% for r in rows %}<li><a href="/events/{{r[0]}}">{{r[1]}} {{r[2]}} {{r[3]}} {{r[4]}}</a></li>{% endfor %}</ul>
```

### `honeypot-platform/hub/app/templates/index.html`  _(~0.1 KB; showing ≤800 lines)_
```html
<h1>Honeypots</h1>
<ul>{% for row in rows %}<li><a href="/honeypots/{{row[0]}}">{{row[0]}}</a></li>{% endfor %}</ul>
```

### `honeypot-platform/hub/app/templates/sessions.html`  _(~0.2 KB; showing ≤800 lines)_
```html
<h1>{{honeypot_id}} sessions</h1>
<ul>{% for r in rows %}<li><a href="/honeypots/{{honeypot_id}}/sessions/{{r[0]}}">{{r[0]}}</a> ({{r[1]}})</li>{% endfor %}</ul>
```

### `honeypot-platform/hub/docker-compose.yml`  _(~0.2 KB; showing ≤800 lines)_
```yaml
services:
  hub:
    build: .
    ports:
      - "8000:8000"
    environment:
      - HOHO_HUB_DATA=/data
      - HOHO_HUB_TOKEN=${HOHO_HUB_TOKEN:-changeme-please-override}
    volumes:
      - ./data:/data
```

### `honeypot-platform/packages/hoho_core/README.md`  _(~0.1 KB; showing ≤800 lines)_
```md
# hoho_core

Shared core primitives for pack validation, event modeling, DSL evaluation, and filesystem artifact storage.
```

### `honeypot-platform/packages/hoho_core/hoho_core/MANIFEST.in`  _(~0.0 KB; showing ≤800 lines)_
```
recursive-include hoho_core/schema *.json
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

### `honeypot-platform/packages/hoho_core/hoho_core/model/event.py`  _(~0.9 KB; showing ≤800 lines)_
```python
import uuid
from hoho_core.utils.time import utc_iso


def build_base_event(
    honeypot_id: str,
    component: str,
    proto: str,
    session_id: str,
    agent_id: str,
    event_name: str,
) -> dict:
    return {
        "schema_version": 2,
        "event_id": str(uuid.uuid4()),
        "ts": utc_iso(),
        "honeypot_id": honeypot_id,
        "session_id": session_id,
        "agent_id": agent_id,
        "event_name": event_name,
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
from .validate import load_pack, validate_pack
from .validate_event import validate_event

__all__ = ["load_pack", "validate_pack", "validate_event"]
```

### `honeypot-platform/packages/hoho_core/hoho_core/schema/event_v2.json`  _(~2.1 KB; showing ≤800 lines)_
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": [
    "schema_version",
    "event_id",
    "ts",
    "honeypot_id",
    "session_id",
    "agent_id",
    "event_name",
    "component",
    "classification",
    "decision",
    "artifacts"
  ],
  "properties": {
    "schema_version": {"const": 2},
    "event_id": {"type": "string", "minLength": 1},
    "ts": {"type": "string", "minLength": 1},
    "honeypot_id": {"type": "string", "minLength": 1},
    "session_id": {"type": "string", "minLength": 1},
    "agent_id": {"type": "string", "minLength": 1},
    "event_name": {"type": "string", "pattern": "^[a-z0-9]+(\\.[a-z0-9_]+)+$"},
    "component": {"type": "string", "minLength": 1},
    "proto": {"type": "string"},
    "src": {"type": "object"},
    "request": {"type": "object"},
    "response": {"type": "object"},
    "classification": {
      "type": "object",
      "required": ["verdict", "tags", "indicators"],
      "properties": {
        "verdict": {"type": "string"},
        "tags": {"type": "array", "items": {"type": "string"}},
        "indicators": {"type": "array", "items": {"type": "string"}}
      },
      "additionalProperties": true
    },
    "decision": {
      "type": "object",
      "required": ["truncated", "oversized", "rate_limited", "dropped"],
      "properties": {
        "truncated": {"type": "boolean"},
        "oversized": {"type": "boolean"},
        "rate_limited": {"type": "boolean"},
        "dropped": {"type": "boolean"}
      },
      "additionalProperties": true
    },
    "artifacts": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["kind", "sha256", "size", "mime", "storage_ref", "meta"],
        "properties": {
          "kind": {"type": "string"},
          "sha256": {"type": "string", "minLength": 64, "maxLength": 64},
          "size": {"type": "integer", "minimum": 0},
          "mime": {"type": "string"},
          "storage_ref": {"type": "string", "minLength": 1},
          "meta": {"type": "object"}
        },
        "additionalProperties": true
      }
    }
  },
  "additionalProperties": true
}
```

### `honeypot-platform/packages/hoho_core/hoho_core/schema/pack_v1.json`  _(~15.0 KB; showing ≤800 lines)_
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": [
    "apiVersion",
    "kind",
    "metadata"
  ],
  "properties": {
    "apiVersion": {
      "const": "hoho.dev/v1"
    },
    "kind": {
      "const": "HoneypotPack"
    },
    "metadata": {
      "type": "object",
      "required": [
        "id",
        "name",
        "interaction",
        "description"
      ],
      "properties": {
        "id": {
          "type": "string",
          "minLength": 1
        },
        "name": {
          "type": "string",
          "minLength": 1
        },
        "interaction": {
          "enum": [
            "low",
            "high"
          ]
        },
        "tags": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "description": {
          "type": "string",
          "minLength": 1
        }
      },
      "additionalProperties": true
    },
    "storage": {
      "type": "object"
    },
    "limits": {
      "type": "object"
    },
    "telemetry": {
      "type": "object",
      "properties": {
        "emit_events": {
          "type": "boolean"
        },
        "redact_headers": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "filters": {
          "type": "object",
          "properties": {
            "emit": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/filter_rule"
              }
            },
            "forward": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/filter_rule"
              }
            }
          },
          "additionalProperties": false
        },
        "forwarding": {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "boolean"
            },
            "hub_url": {
              "type": "string",
              "minLength": 1
            },
            "token_env": {
              "type": "string",
              "minLength": 1
            }
          },
          "additionalProperties": false
        }
      },
      "additionalProperties": true
    },
    "listen": {
      "type": "array"
    },
    "responses": {
      "type": "object"
    },
    "behaviors": {
      "type": "array"
    },
    "stack": {
      "type": "object",
      "properties": {
        "runtime": {
          "type": "string"
        },
        "services": {
          "type": "object",
          "additionalProperties": {
            "type": "object",
            "properties": {
              "volumes": {
                "type": "array",
                "items": {
                  "oneOf": [
                    {
                      "type": "string"
                    },
                    {
                      "type": "object"
                    }
                  ]
                }
              },
              "networks": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "ports": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              }
            },
            "additionalProperties": true
          }
        }
      },
      "additionalProperties": true
    },
    "sensors": {
      "type": "array",
      "items": {
        "type": "object",
        "required": [
          "name",
          "type",
          "attach"
        ],
        "properties": {
          "name": {
            "type": "string",
            "minLength": 1
          },
          "type": {
            "enum": [
              "fsmon",
              "proxy",
              "pcap",
              "egress_proxy",
              "falco"
            ]
          },
          "attach": {
            "type": "object",
            "properties": {
              "service": {
                "type": "string",
                "minLength": 1
              },
              "network": {
                "type": "string",
                "minLength": 1
              },
              "services": {
                "type": "array",
                "minItems": 1,
                "items": {
                  "type": "string",
                  "minLength": 1
                }
              }
            },
            "additionalProperties": false
          },
          "config": {
            "oneOf": [
              {
                "type": "object",
                "required": [
                  "watch"
                ],
                "properties": {
                  "watch": {
                    "type": "array",
                    "minItems": 1,
                    "items": {
                      "type": "string",
                      "minLength": 1
                    }
                  },
                  "allow_globs": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    }
                  },
                  "deny_globs": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    }
                  },
                  "max_bytes": {
                    "type": "integer",
                    "minimum": 1
                  }
                },
                "additionalProperties": false
              },
              {
                "type": "object",
                "required": [
                  "upstream"
                ],
                "properties": {
                  "upstream": {
                    "type": "string",
                    "minLength": 1
                  },
                  "listen_port": {
                    "type": "integer",
                    "minimum": 1
                  }
                },
                "additionalProperties": false
              },
              {
                "type": "object",
                "properties": {
                  "interface": {
                    "type": "string",
                    "minLength": 1
                  },
                  "rotate_seconds": {
                    "type": "integer",
                    "minimum": 1
                  },
                  "rotate_count": {
                    "type": "integer",
                    "minimum": 1
                  }
                },
                "additionalProperties": false
              },
              {
                "type": "object",
                "properties": {
                  "listen_host": {
                    "type": "string",
                    "minLength": 1
                  },
                  "listen_port": {
                    "type": "integer",
                    "minimum": 1
                  },
                  "force_egress_via_proxy": {
                    "type": "boolean"
                  },
                  "tls_mitm": {
                    "type": "object",
                    "properties": {
                      "enabled": {
                        "type": "boolean"
                      },
                      "install_trust": {
                        "type": "object",
                        "properties": {
                          "also_set_env_bundles": {
                            "type": "boolean"
                          },
                          "extra_commands": {
                            "type": "array",
                            "items": {
                              "type": "string"
                            }
                          }
                        },
                        "additionalProperties": false
                      }
                    },
                    "additionalProperties": false
                  },
                  "capture": {
                    "type": "object",
                    "properties": {
                      "enabled": {
                        "type": "boolean"
                      },
                      "bodies": {
                        "enum": [
                          "*",
                          "none"
                        ]
                      },
                      "max_bytes": {
                        "type": "integer",
                        "minimum": 1
                      },
                      "store_ok_only": {
                        "type": "boolean"
                      },
                      "min_bytes": {
                        "type": "integer",
                        "minimum": 0
                      },
                      "redact_headers": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      }
                    },
                    "additionalProperties": false
                  }
                },
                "additionalProperties": false
              },
              {
                "type": "object",
                "properties": {
                  "mode": {
                    "enum": [
                      "privileged",
                      "least_privileged"
                    ]
                  },
                  "engine": {
                    "enum": [
                      "modern_ebpf",
                      "kmod",
                      "ebpf"
                    ]
                  },
                  "priority_min": {
                    "enum": [
                      "Debug",
                      "Informational",
                      "Notice",
                      "Warning",
                      "Error",
                      "Critical",
                      "Emergency"
                    ]
                  },
                  "rules": {
                    "type": "array",
                    "items": {
                      "type": "string",
                      "minLength": 1
                    }
                  },
                  "append_fields": {
                    "type": "array",
                    "items": {
                      "type": "string",
                      "minLength": 1
                    }
                  },
                  "any_exec": {
                    "type": "boolean"
                  },
                  "enforce": {
                    "type": "object",
                    "properties": {
                      "enabled": {
                        "type": "boolean"
                      },
                      "match_priorities": {
                        "type": "array",
                        "items": {
                          "type": "string",
                          "minLength": 1
                        }
                      },
                      "match_rules": {
                        "type": "array",
                        "items": {
                          "type": "string",
                          "minLength": 1
                        }
                      },
                      "action": {
                        "enum": [
                          "stop_container",
                          "stop_service",
                          "stop_stack"
                        ]
                      },
                      "cooldown_seconds": {
                        "type": "integer",
                        "minimum": 0
                      }
                    },
                    "additionalProperties": false
                  }
                },
                "additionalProperties": false
              }
            ]
          }
        },
        "allOf": [
          {
            "if": {
              "properties": {
                "type": {
                  "const": "fsmon"
                }
              },
              "required": [
                "type"
              ]
            },
            "then": {
              "required": [
                "config"
              ],
              "properties": {
                "config": {
                  "type": "object",
                  "required": [
                    "watch"
                  ]
                },
                "attach": {
                  "type": "object",
                  "required": [
                    "service"
                  ]
                }
              }
            }
          },
          {
            "if": {
              "properties": {
                "type": {
                  "const": "proxy"
                }
              },
              "required": [
                "type"
              ]
            },
            "then": {
              "required": [
                "config"
              ],
              "properties": {
                "config": {
                  "type": "object",
                  "required": [
                    "upstream"
                  ]
                },
                "attach": {
                  "type": "object",
                  "required": [
                    "service"
                  ]
                }
              }
            }
          },
          {
            "if": {
              "properties": {
                "type": {
                  "const": "egress_proxy"
                }
              },
              "required": [
                "type"
              ]
            },
            "then": {
              "required": [
                "config"
              ],
              "properties": {
                "attach": {
                  "type": "object",
                  "required": [
                    "services"
                  ]
                }
              }
            }
          },
          {
            "if": {
              "properties": {
                "type": {
                  "const": "falco"
                }
              },
              "required": [
                "type"
              ]
            },
            "then": {
              "required": [
                "config"
              ]
            }
          }
        ],
        "additionalProperties": true
      }
    }
  },
  "additionalProperties": true,
  "$defs": {
    "filter_condition": {
      "type": "object",
      "properties": {
        "all": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/filter_condition"
          }
        },
        "any": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/filter_condition"
          }
        },
        "field": {
          "type": "string"
        },
        "eq": {},
        "neq": {},
        "in": {
          "type": "array"
        },
        "contains": {
          "type": "string"
        },
        "regex": {
          "type": "string"
        },
        "gte": {},
        "lte": {},
        "exists": {
          "type": "boolean"
        }
      },
      "additionalProperties": true
    },
    "filter_rule": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "when": {
          "$ref": "#/$defs/filter_condition"
        },
        "action": {
          "enum": [
            "keep",
            "drop"
          ]
        }
      },
      "required": [
        "action"
      ],
      "additionalProperties": false
    }
  }
}
```

### `honeypot-platform/packages/hoho_core/hoho_core/schema/validate.py`  _(~3.8 KB; showing ≤800 lines)_
```python
import json
from pathlib import Path

import yaml
from jsonschema import ValidationError, validate


def load_pack(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    suffix = Path(path).suffix.lower()
    try:
        if suffix == ".json":
            data = json.loads(text)
        elif suffix in {".yaml", ".yml"}:
            data = yaml.safe_load(text)
        else:
            raise ValueError(f"unsupported pack format '{suffix}', expected .json, .yaml, or .yml")
    except (json.JSONDecodeError, yaml.YAMLError) as exc:
        raise ValueError(f"pack parsing error: {exc}") from exc

    if not isinstance(data, dict):
        raise ValueError("pack parsing error: top-level document must be an object")
    return data


def _load_schema() -> dict:
    schema_path = Path(__file__).with_name("pack_v1.json")
    return json.loads(schema_path.read_text(encoding="utf-8"))


def _format_schema_error(exc: ValidationError) -> str:
    path = ".".join(str(part) for part in exc.path)
    if path:
        return f"schema error at {path}: {exc.message}"
    return f"schema error: {exc.message}"


def validate_pack(pack: dict) -> list[str]:
    out: list[str] = []

    try:
        validate(instance=pack, schema=_load_schema())
    except ValidationError as exc:
        out.append(_format_schema_error(exc))
        return out

    interaction = pack.get("metadata", {}).get("interaction")
    if interaction == "low" and "behaviors" not in pack:
        out.append("semantic error: low interaction pack requires behaviors")
    if interaction == "high" and "stack" not in pack:
        out.append("semantic error: high interaction pack requires stack")


    telemetry = pack.get("telemetry", {}) if isinstance(pack.get("telemetry", {}), dict) else {}
    forwarding = telemetry.get("forwarding", {}) if isinstance(telemetry.get("forwarding", {}), dict) else {}
    if forwarding.get("enabled") and not forwarding.get("hub_url"):
        out.append("semantic error: telemetry.forwarding.enabled requires telemetry.forwarding.hub_url")
    if forwarding.get("enabled") and not forwarding.get("token_env"):
        out.append("semantic error: telemetry.forwarding.enabled requires telemetry.forwarding.token_env")

    services = pack.get("stack", {}).get("services", {})
    service_names = set(services.keys()) if isinstance(services, dict) else set()
    if interaction == "low":
        service_names.add("honeypot")

    for sensor in pack.get("sensors", []):
        sensor_name = sensor.get("name", "<unnamed>")
        sensor_type = sensor.get("type")
        attach = sensor.get("attach", {})

        if sensor_type in {"fsmon", "proxy", "pcap"}:
            target_service = attach.get("service")
            if target_service and target_service not in service_names:
                out.append(
                    f"semantic error: {sensor_type} sensor '{sensor_name}' attaches to unknown service '{target_service}'"
                )

        if sensor_type == "falco":
            if interaction != "high":
                out.append(f"semantic error: falco sensor '{sensor_name}' requires metadata.interaction=high")
            attached_services = attach.get("services", [])
            for service_name in attached_services:
                if service_name not in service_names:
                    out.append(
                        f"semantic error: falco sensor '{sensor_name}' attaches to unknown service '{service_name}'"
                    )

        if sensor_type == "egress_proxy":
            attached_services = attach.get("services", [])
            for service_name in attached_services:
                if service_name not in service_names:
                    out.append(
                        f"semantic error: egress_proxy sensor '{sensor_name}' attaches to unknown service '{service_name}'"
                    )

    return out
```

### `honeypot-platform/packages/hoho_core/hoho_core/schema/validate_event.py`  _(~0.7 KB; showing ≤800 lines)_
```python
import json
from pathlib import Path

from jsonschema import ValidationError, validate


_EVENT_SCHEMA_V2: dict | None = None


def _load_event_schema() -> dict:
    global _EVENT_SCHEMA_V2
    if _EVENT_SCHEMA_V2 is None:
        schema_path = Path(__file__).with_name("event_v2.json")
        _EVENT_SCHEMA_V2 = json.loads(schema_path.read_text(encoding="utf-8"))
    return _EVENT_SCHEMA_V2


def validate_event(event: dict) -> list[str]:
    try:
        validate(instance=event, schema=_load_event_schema())
    except ValidationError as exc:
        path = ".".join(str(p) for p in exc.path)
        return [f"schema error at {path}: {exc.message}" if path else f"schema error: {exc.message}"]
    return []
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

### `honeypot-platform/packages/hoho_core/hoho_core/storage/fs.py`  _(~1.6 KB; showing ≤800 lines)_
```python
import os
from pathlib import Path

from hoho_core.storage.base import ArtifactStore
from hoho_core.telemetry.filters import load_rules_from_env, should_keep
from hoho_core.utils.hashing import sha256_bytes
from hoho_core.utils.jsonl import append_jsonl


class FilesystemArtifactStore(ArtifactStore):
    def __init__(self, root: str, honeypot_id: str):
        self.root = Path(root)
        self.honeypot_id = honeypot_id
        self.pack_root = self.root / honeypot_id
        self._emit_rules = load_rules_from_env("HOHO_EMIT_FILTERS_JSON")
        self._debug_drops = os.getenv("HOHO_EMIT_FILTERS_DEBUG", "false").lower() in {"1", "true", "yes", "on"}

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

    def append_event(self, honeypot_id: str, event: dict) -> None:
        keep, rule = should_keep(event, self._emit_rules)
        if not keep:
            if self._debug_drops:
                append_jsonl(
                    self.root / honeypot_id / "index" / "events.jsonl",
                    {"event_name": "telemetry.drop", "reason": rule, "ts": event.get("ts")},
                )
            return
        append_jsonl(self.root / honeypot_id / "index" / "events.jsonl", event)
```

### `honeypot-platform/packages/hoho_core/hoho_core/telemetry/__init__.py`  _(~0.1 KB; showing ≤800 lines)_
```python
from .filters import load_rules_from_env, parse_filter_config, should_keep

__all__ = ["load_rules_from_env", "parse_filter_config", "should_keep"]
```

### `honeypot-platform/packages/hoho_core/hoho_core/telemetry/filters.py`  _(~2.5 KB; showing ≤800 lines)_
```python
import json
import re
from typing import Any


def _iter_values(obj: Any, parts: list[str]) -> list[Any]:
    if not parts:
        return [obj]
    if isinstance(obj, list):
        out: list[Any] = []
        for item in obj:
            out.extend(_iter_values(item, parts))
        return out
    if not isinstance(obj, dict):
        return []
    key = parts[0]
    if key not in obj:
        return []
    return _iter_values(obj[key], parts[1:])


def _match_condition(event: dict, cond: dict) -> bool:
    if "all" in cond:
        return all(_match_condition(event, c) for c in cond.get("all", []))
    if "any" in cond:
        return any(_match_condition(event, c) for c in cond.get("any", []))

    field = cond.get("field")
    if not field:
        return False
    values = _iter_values(event, str(field).split("."))

    if "exists" in cond:
        return bool(values) is bool(cond["exists"])
    if not values:
        return False

    for value in values:
        if "eq" in cond and value == cond["eq"]:
            return True
        if "neq" in cond and value != cond["neq"]:
            return True
        if "in" in cond and value in cond["in"]:
            return True
        if "contains" in cond and str(cond["contains"]) in str(value):
            return True
        if "regex" in cond and re.search(str(cond["regex"]), str(value)):
            return True
        if "gte" in cond:
            try:
                if value >= cond["gte"]:
                    return True
            except TypeError:
                pass
        if "lte" in cond:
            try:
                if value <= cond["lte"]:
                    return True
            except TypeError:
                pass
    return False


def parse_filter_config(config: dict | None) -> list[dict]:
    if not config:
        return []
    if isinstance(config, list):
        return config
    return []


def load_rules_from_env(env_key: str) -> list[dict]:
    raw = __import__("os").getenv(env_key, "")
    if not raw.strip():
        return []
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError:
        return []
    return parse_filter_config(parsed)


def should_keep(event: dict, rules: list[dict]) -> tuple[bool, str | None]:
    for rule in rules:
        when = rule.get("when")
        matched = True if when is None else _match_condition(event, when)
        if not matched:
            continue
        action = str(rule.get("action", "keep")).lower()
        return action != "drop", rule.get("name")
    return True, None
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

### `honeypot-platform/packages/hoho_core/pyproject.toml`  _(~0.4 KB; showing ≤800 lines)_
```toml
[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "hoho-core"
version = "0.1.0"
dependencies = [
  "PyYAML",
  "jsonschema"
]

[tool.setuptools.packages.find]
where = ["."]
include = ["hoho_core*"]

[tool.setuptools]
include-package-data = true

[tool.setuptools.package-data]
hoho_core = ["schema/*.json"]
```

### `honeypot-platform/packages/hoho_forwarder/hoho_forwarder/__init__.py`  _(~0.0 KB; showing ≤800 lines)_
```python

```

### `honeypot-platform/packages/hoho_forwarder/hoho_forwarder/main.py`  _(~2.4 KB; showing ≤800 lines)_
```python
import json
import os
import time
from pathlib import Path

import requests

from hoho_core.telemetry.filters import load_rules_from_env, should_keep


def _iter_artifact_shas(event: dict) -> list[str]:
    return [a.get("sha256") for a in event.get("artifacts", []) if isinstance(a, dict) and a.get("sha256")]


def main() -> int:
    root = Path(os.getenv("HOHO_STORAGE_ROOT", "/artifacts"))
    honeypot_id = os.getenv("HOHO_HONEYPOT_ID", os.getenv("HOHO_PACK_ID", "unknown-pack"))
    hub_url = os.getenv("HOHO_HUB_URL", "").rstrip("/")
    token =[REDACTED]
    if not hub_url:
        print("[forwarder] HOHO_HUB_URL missing; exiting")
        return 0

    events_path = root / honeypot_id / "index" / "events.jsonl"
    cursor_path = root / honeypot_id / "index" / "forwarder.cursor"
    rules = load_rules_from_env("HOHO_FORWARD_FILTERS_JSON")
    headers =[REDACTED]

    offset = int(cursor_path.read_text().strip() or "0") if cursor_path.exists() else 0
    while True:
        events_path.parent.mkdir(parents=True, exist_ok=True)
        events_path.touch(exist_ok=True)
        with events_path.open("r", encoding="utf-8") as f:
            f.seek(offset)
            for line in f:
                offset = f.tell()
                try:
                    event = json.loads(line)
                except json.JSONDecodeError:
                    continue
                keep, _ = should_keep(event, rules)
                if not keep:
                    continue

                for sha in _iter_artifact_shas(event):
                    head = requests.head(f"{hub_url}/api/v1/blobs/{sha}", headers=headers, timeout=5)
                    if head.status_code == 404:
                        blob_path = root / honeypot_id / "blobs" / sha[:2] / sha
                        if blob_path.exists():
                            requests.put(
                                f"{hub_url}/api/v1/blobs/{sha}",
                                data=blob_path.read_bytes(),
                                headers=headers,
                                timeout=20,
                            )
                requests.post(f"{hub_url}/api/v1/events", json=event, headers=headers, timeout=5)
                cursor_path.write_text(str(offset), encoding="utf-8")
        time.sleep(1)


if __name__ == "__main__":
    raise SystemExit(main())
```

### `honeypot-platform/packages/hoho_forwarder/pyproject.toml`  _(~0.2 KB; showing ≤800 lines)_
```toml
[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "hoho-forwarder"
version = "0.1.0"
dependencies = ["requests"]

[tool.setuptools.packages.find]
where = ["."]
include = ["hoho_forwarder*"]
```

### `honeypot-platform/packages/hoho_runtime/README.md`  _(~0.3 KB; showing ≤800 lines)_
```md
# hoho_runtime

CLI and runtime components for low-interaction serving and high-interaction compose orchestration.

## CLI quick reference

```bash
# Stop and remove all honeypots
hoho down-all

# Also remove project volumes
hoho down-all --volumes

# Preview cleanup commands only
hoho down-all --dry-run
```
```

### `honeypot-platform/packages/hoho_runtime/hoho_runtime/__init__.py`  _(~0.0 KB; showing ≤800 lines)_
```python

```

### `honeypot-platform/packages/hoho_runtime/hoho_runtime/cli.py`  _(~13.8 KB; showing ≤800 lines)_
```python
import argparse
import json
import os
import re
import shutil
import socket
import uuid
from pathlib import Path

from datetime import datetime, timezone

from hoho_core.schema.validate import load_pack, validate_pack
from hoho_runtime.config import DEFAULT_STORAGE_ROOT
from hoho_runtime.env import loadenv
from hoho_runtime.orchestration.compose_down_all import down_all
from hoho_runtime.orchestration.compose_render import render_compose
from hoho_runtime.orchestration.compose_run import run_compose
from hoho_runtime.orchestration.ca_pregen import EgressCAError, ensure_egress_ca
from hoho_runtime.server.http import run_low_http

HONEYPOTS_DIRNAME = "honeypots"
LEVEL_DIRS = ("high", "low")
HONEYPOT_FILE = "honeypot.yaml"


def _sanitize_name(value: str) -> str:
    sanitized = re.sub(r"[^a-z0-9_-]", "-", value.lower()).strip("-_")
    return sanitized or "hoho"


def _warn_if_run_id_used(run_id: str | None) -> None:
    if run_id:
        print("WARNING: --run-id is deprecated and ignored; Simple Layout v1 always overwrites by honeypot_id.")


def _guess_project_root(pack_path: Path) -> Path:
    return _resolve_repo_root(pack_path.parent)


def _resolve_repo_root(start: Path) -> Path:
    candidates: list[Path] = [start, *start.parents]

    for candidate in candidates:
        compose_dir = candidate / "deploy" / "compose"
        if compose_dir.is_dir() or (compose_dir / "README.md").exists():
            return candidate

        nested_root = candidate / "honeypot-platform"
        nested_compose_dir = nested_root / "deploy" / "compose"
        if nested_compose_dir.is_dir() or (nested_compose_dir / "README.md").exists():
            return nested_root

    for candidate in candidates:
        if (candidate / "packs").is_dir() or (candidate / HONEYPOTS_DIRNAME).is_dir():
            return candidate

    return start


def _resolve_pack_arg(raw_arg: str, cwd: Path) -> Path:
    raw_path = Path(raw_arg).expanduser()
    candidate = raw_path if raw_path.is_absolute() else (cwd / raw_path)

    if candidate.is_file():
        pack_path = candidate.resolve()
        if pack_path.suffix.lower() not in {".yaml", ".yml", ".json"}:
            raise SystemExit(f"ERROR: expected yaml/json file, got: {raw_arg}")
        _warn_if_deprecated_packs_path(pack_path)
        return pack_path

    if candidate.is_dir():
        pack_path = (candidate / HONEYPOT_FILE)
        if not pack_path.is_file():
            raise SystemExit(f"ERROR: directory '{raw_arg}' does not contain {HONEYPOT_FILE}")
        _warn_if_deprecated_packs_path(pack_path.resolve())
        return pack_path.resolve()

    return _resolve_honeypot_id(raw_arg, cwd)


def _resolve_honeypot_id(honeypot_id: str, cwd: Path) -> Path:
    repo_root = _resolve_repo_root(cwd)
    honeypots_root = repo_root / HONEYPOTS_DIRNAME
    matches: list[Path] = []

    for level in LEVEL_DIRS:
        candidate = honeypots_root / level / honeypot_id / HONEYPOT_FILE
        if candidate.is_file():
            matches.append(candidate.resolve())

    if not matches:
        raise SystemExit(
            "ERROR: unable to resolve honeypot input. "
            "Provide a honeypot directory, honeypot YAML path, or an existing honeypot id under honeypots/{high,low}."
        )

    if len(matches) > 1:
        raise SystemExit(
            f"ERROR: honeypot id '{honeypot_id}' exists in multiple interaction levels: "
            f"{', '.join(str(match.parent) for match in matches)}. Please pass an explicit path."
        )

    return matches[0]


def _warn_if_deprecated_packs_path(pack_path: Path) -> None:
    parts = set(pack_path.parts)
    if "packs" in parts:
        print(
            f"WARNING: Deprecated path: {pack_path}. "
            "Use honeypots/{high,low}/<honeypot_id>/honeypot.yaml instead."
        )


def _compose_output_dir(honeypot_id: str, output: str | None, project_root: Path) -> str:
    if output:
        return output
    return str(project_root / "deploy" / "compose" / honeypot_id)


def _resolve_storage_root(pack: dict, artifacts_root_arg: str | None, project_root: Path) -> Path:
    storage_value = artifacts_root_arg or pack.get("storage", {}).get("root", DEFAULT_STORAGE_ROOT)
    storage_root = Path(storage_value).expanduser()
    if not storage_root.is_absolute():
        storage_root = project_root / storage_root
    return storage_root.resolve()


def _prepare_artifacts_root(storage_root: Path, honeypot_id: str) -> Path:
    artifacts_dir = storage_root / honeypot_id
    shutil.rmtree(artifacts_dir, ignore_errors=True)
    artifacts_dir.mkdir(parents=True, exist_ok=True)
    return artifacts_dir






def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()




def _resolve_env_file_arg(env_file_arg: str | None, cwd: Path) -> Path | None:
    if not env_file_arg:
        return None
    env_file = Path(env_file_arg).expanduser()
    if not env_file.is_absolute():
        env_file = (cwd / env_file).resolve()
    return env_file


def _load_global_env(args: argparse.Namespace, repo_root: Path) -> Path | None:
    if getattr(args, "no_env", False):
        return None

    env_file = _resolve_env_file_arg(getattr(args, "env_file", None), Path.cwd())
    if env_file is None:
        env_file = repo_root / ".env"

    if env_file.is_file():
        loadenv(env_file, override=getattr(args, "env_override", False))

    return env_file


def _require_forwarding_env(pack: dict) -> None:
    telemetry = pack.get("telemetry", {})
    forwarding = telemetry.get("forwarding", {}) if isinstance(telemetry, dict) else {}
    if not _bool_enabled(forwarding.get("enabled"), default=False):
        return

    token_env = str(forwarding.get("token_env", "")).strip()
    hub_url = str(forwarding.get("hub_url", "")).strip()

    missing: list[str] = []
    if hub_url.startswith("${") and hub_url.endswith("}"):
        hub_url_env = hub_url[2:-1]
        if hub_url_env and not os.environ.get(hub_url_env):
            missing.append(hub_url_env)
    elif not hub_url:
        missing.append("telemetry.forwarding.hub_url")

    if token_env and not os.environ.get(token_env):
        missing.append(token_env)

    if missing:
        raise SystemExit(
            "ERROR: telemetry forwarding is enabled but required environment values are missing: "
            + ", ".join(missing)
        )

def _session_metadata(honeypot_id: str) -> dict:
    return {
        "honeypot_id": honeypot_id,
        "session_id": str(uuid.uuid4()),
        "agent_id": os.getenv("HOHO_AGENT_ID", socket.gethostname()),
        "started_ts": _utc_now(),
    }


def _write_session_metadata(artifacts_dir: Path, session: dict) -> None:
    index_dir = artifacts_dir / "index"
    index_dir.mkdir(parents=True, exist_ok=True)
    (index_dir / "session.json").write_text(json.dumps(session, indent=2), encoding="utf-8")

def _find_egress_proxy_sensor(pack: dict) -> dict | None:
    for sensor in pack.get("sensors", []):
        if sensor.get("type") == "egress_proxy":
            return sensor
    return None


def _runtime_ca_required(sensor: dict | None) -> bool:
    if not sensor:
        return False
    config = sensor.get("config", {})
    tls_mitm = config.get("tls_mitm", {})
    return _bool_enabled(tls_mitm.get("enabled", False), default=False)


def _bool_enabled(value: object, default: bool = False) -> bool:
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return bool(value)
    return str(value).strip().lower() in {"1", "true", "yes", "on"}

def cmd_validate(args):
    pack_path = _resolve_pack_arg(args.pack, Path.cwd())
    pack = load_pack(str(pack_path))
    errors = validate_pack(pack)
    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        raise SystemExit(1)
    print("valid")


def cmd_render_compose(args):
    pack_path = _resolve_pack_arg(args.pack, Path.cwd())
    project_root = _guess_project_root(pack_path)

    pack = load_pack(str(pack_path))
    errors = validate_pack(pack)
    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        raise SystemExit(1)

    honeypot_id = pack["metadata"]["id"]
    _warn_if_run_id_used(args.run_id)
    out_dir = _compose_output_dir(honeypot_id, args.output, project_root=project_root)
    _require_forwarding_env(pack)
    storage_root = _resolve_storage_root(pack, args.artifacts_root, project_root)
    session = _session_metadata(honeypot_id)
    out = render_compose(
        pack,
        out_dir=out_dir,
        artifacts_root=str(storage_root),
        honeypot_dir=pack_path.parent,
        session_id=session["session_id"],
        agent_id=session["agent_id"],
    )
    print(out)


def cmd_run(args):
    pack_path = _resolve_pack_arg(args.pack, Path.cwd())
    project_root = _guess_project_root(pack_path)
    pack = load_pack(str(pack_path))
    errors = validate_pack(pack)
    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        raise SystemExit(1)

    _require_forwarding_env(pack)
    storage_root = _resolve_storage_root(pack, args.artifacts_root, project_root)
    interaction = pack["metadata"]["interaction"]

    if args.mode == "host":
        if interaction != "low":
            raise SystemExit("ERROR: --mode host is only supported for low interaction honeypots")
        pack.setdefault("storage", {})["root"] = str(storage_root)
        run_low_http(pack)
        return

    honeypot_id = pack["metadata"]["id"]
    _warn_if_run_id_used(args.run_id)
    out_dir = _compose_output_dir(honeypot_id, args.output, project_root=project_root)

    artifacts_host_path = _prepare_artifacts_root(storage_root, honeypot_id)
    session = _session_metadata(honeypot_id)
    _write_session_metadata(artifacts_host_path, session)
    compose_file = render_compose(
        pack,
        out_dir=out_dir,
        artifacts_root=str(storage_root),
        honeypot_dir=pack_path.parent,
        session_id=session["session_id"],
        agent_id=session["agent_id"],
    )
    compose_root = compose_file.parent
    runtime_ca_dir = compose_root / "runtime" / "ca"
    egress_sensor = _find_egress_proxy_sensor(pack)
    if _runtime_ca_required(egress_sensor):
        try:
            ensure_egress_ca(runtime_ca_dir, common_name=f"hoho-egress-ca-{honeypot_id}")
        except EgressCAError as exc:
            raise SystemExit(f"[hoho] ERROR: failed to prepare runtime egress CA: {exc}") from exc
    project_name = _sanitize_name(f"hoho-{honeypot_id}")

    print(
        json.dumps(
            {
                "honeypot_id": honeypot_id,
                "artifacts_host_path": str(artifacts_host_path),
                "compose_file": str(compose_file.resolve()),
                "project_name": project_name,
                "mode": args.mode,
                "session_id": session["session_id"],
                "agent_id": session["agent_id"],
            }
        )
    )

    if args.no_up:
        print(compose_file)
    else:
        raise SystemExit(run_compose(
            compose_file,
            project_name=project_name,
            pack=pack,
            artifacts_root=storage_root,
            session_id=session["session_id"],
            agent_id=session["agent_id"],
            env_file=getattr(args, "_resolved_env_file", None),
        ))


def cmd_explain(args):
    pack_path = _resolve_pack_arg(args.pack, Path.cwd())
    pack = load_pack(str(pack_path))
    plan = {
        "honeypot_id": pack["metadata"]["id"],
        "interaction": pack["metadata"]["interaction"],
        "listen": pack.get("listen", []),
        "limits": pack.get("limits", {}),
        "storage_root": pack.get("storage", {}).get("root", "./run/artifacts"),
        "sensors": pack.get("sensors", []),
    }
    print(json.dumps(plan, indent=2))


def cmd_down_all(args):
    repo_root = _resolve_repo_root(Path.cwd())
    result = down_all(
        repo_root,
        remove_volumes=args.volumes,
        dry_run=args.dry_run,
        include_stale=args.include_stale,
    )

    print(
        "found "
        f"{len(result.projects_found)} projects, "
        f"stopped {len(result.projects_stopped)}, "
        f"failed {len(result.projects_failed)}, "
        f"cleaned stale {len(result.stray_projects_cleaned)}"
    )

    if result.projects_failed:
        raise SystemExit(2)


def main():
    parser = argparse.ArgumentParser(prog="hoho")
    parser.add_argument("--env-file", default=None)
    parser.add_argument("--no-env", action="store_true")
    parser.add_argument("--env-override", action="store_true")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_val = sub.add_parser("validate")
    p_val.add_argument("pack")
    p_val.set_defaults(func=cmd_validate)

    p_run = sub.add_parser("run")
    p_run.add_argument("pack")
    p_run.add_argument("--no-up", action="store_true")
    p_run.add_argument("--run-id", default=None)
    p_run.add_argument("--artifacts-root", default=None)
    p_run.add_argument("--mode", choices=["container", "host"], default="container")
    p_run.add_argument("-o", "--output", default=None)
    p_run.set_defaults(func=cmd_run)

    p_rc = sub.add_parser("render-compose")
    p_rc.add_argument("pack")
    p_rc.add_argument("-o", "--output", default=None)
    p_rc.add_argument("--run-id", default=None)
    p_rc.add_argument("--artifacts-root", default=None)
    p_rc.set_defaults(func=cmd_render_compose)

    p_ex = sub.add_parser("explain")
    p_ex.add_argument("pack")
    p_ex.set_defaults(func=cmd_explain)

    p_down_all = sub.add_parser("down-all")
    p_down_all.add_argument("--volumes", action="store_true")
    p_down_all.add_argument("--dry-run", action="store_true")
    p_down_all.add_argument("--include-stale", action=argparse.BooleanOptionalAction, default=True)
    p_down_all.set_defaults(func=cmd_down_all)

    args = parser.parse_args()
    repo_root = _resolve_repo_root(Path.cwd())
    args._resolved_env_file = _load_global_env(args, repo_root)
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

### `honeypot-platform/packages/hoho_runtime/hoho_runtime/container/__init__.py`  _(~0.0 KB; showing ≤800 lines)_
```python

```

### `honeypot-platform/packages/hoho_runtime/hoho_runtime/container/low_runtime.py`  _(~1.0 KB; showing ≤800 lines)_
```python
import json
import os

from hoho_core.schema.validate import load_pack, validate_pack
from hoho_runtime.server.http import run_low_http


def main() -> None:
    pack_path = os.environ.get("HOHO_PACK_PATH", "/honeypot/honeypot.yaml")
    storage_root = os.environ.get("HOHO_STORAGE_ROOT", "/artifacts")

    pack = load_pack(pack_path)
    errors = validate_pack(pack)
    if errors:
        raise SystemExit("; ".join(errors))

    pack.setdefault("storage", {})["root"] = storage_root
    listen = (pack.get("listen") or [{"port": 8080}])[0]
    listen["host"] = "0.0.0.0"

    print(
        json.dumps(
            {
                "status": "ready",
                "component": "low_runtime",
                "pack_id": pack["metadata"]["id"],
                "pack_path": pack_path,
                "storage_root": storage_root,
                "listen_port": int(listen.get("port", 8080)),
            }
        )
    )
    run_low_http(pack)


if __name__ == "__main__":
    main()
```

### `honeypot-platform/packages/hoho_runtime/hoho_runtime/env.py`  _(~0.6 KB; showing ≤800 lines)_
```python
import os
from pathlib import Path


def loadenv(path: Path, *, override: bool = False) -> dict[str, str]:
    loaded: dict[str, str] = {}

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        if not key:
            continue

        loaded[key] = value
        if override or key not in os.environ:
            os.environ[key] = value

    return loaded
```

### `honeypot-platform/packages/hoho_runtime/hoho_runtime/orchestration/__init__.py`  _(~0.0 KB; showing ≤800 lines)_
```python

```

### `honeypot-platform/packages/hoho_runtime/hoho_runtime/orchestration/ca_pregen.py`  _(~5.2 KB; showing ≤800 lines)_
```python
from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path


class EgressCAError(RuntimeError):
    """Raised when host-side egress CA generation fails."""


def _set_private_key_mode(path: Path) -> None:
    # Best-effort (some FS / platforms ignore chmod).
    try:
        os.chmod(path, 0o600)
    except OSError:
        return


def _run_openssl(args: list[str], *, cwd: Path) -> subprocess.CompletedProcess[str]:
    cmd = ["openssl", *args]
    try:
        proc = subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True)
    except FileNotFoundError as exc:
        raise EgressCAError("openssl is required to pre-generate runtime egress CA but was not found") from exc

    if proc.returncode != 0:
        stderr = (proc.stderr or "").strip()
        raise EgressCAError(f"openssl command failed ({' '.join(cmd)}): {stderr[:800]}")
    return proc


def _write_mitmproxy_bundle(*, cert_path: Path, key_path: Path, bundle_path: Path) -> None:
    """
[REDACTED]
    Put key first to avoid tooling that stops parsing after the first block.
    """
    key = key_path.read_text(encoding="utf-8").rstrip()
    cert = cert_path.read_text(encoding="utf-8").rstrip()
    bundle_path.write_text(f"{key}\n{cert}\n", encoding="utf-8")
    _set_private_key_mode(bundle_path)


def _cert_has_ca_true(cert_path: Path) -> bool:
    # Keep it simple: parse openssl text output.
    try:
        out = _run_openssl(["x509", "-in", str(cert_path), "-noout", "-text"], cwd=cert_path.parent).stdout
    except EgressCAError:
        return False
    return "CA:TRUE" in out


def _key_matches_cert_rsa(cert_path: Path, key_path: Path) -> bool:
    """
    We generate RSA keys; use modulus check.
    If the key is not RSA for any reason, we treat it as mismatch.
    """
    try:
        cert_mod = _run_openssl(["x509", "-in", str(cert_path), "-noout", "-modulus"], cwd=cert_path.parent).stdout.strip()
        key_mod = _run_openssl(["rsa", "-in", str(key_path), "-noout", "-modulus"], cwd=key_path.parent).stdout.strip()
    except EgressCAError:
        return False
    return bool(cert_mod) and cert_mod == key_mod


def _existing_ca_is_valid(cert_path: Path, key_path: Path) -> bool:
    if not cert_path.is_file() or cert_path.stat().st_size == 0:
        return False
    if not key_path.is_file() or key_path.stat().st_size == 0:
        return False
    if not _cert_has_ca_true(cert_path):
        return False
    if not _key_matches_cert_rsa(cert_path, key_path):
        return False
    return True


def ensure_egress_ca(
    ca_dir: Path,
    *,
    common_name: str,
    days_valid: int = 3650,
    overwrite: bool = False,
    key_bits: int = 2048,
) -> dict:
    """
    Single-mode CA generation (automatic).
    - If valid CA already exists and overwrite=False: reuse.
    - Otherwise: generate a proper CA (CA:TRUE, keyCertSign) via openssl.
    Also creates mitmproxy-compatible files:
      - mitmproxy-ca-cert.pem  (cert only)
      - mitmproxy-ca.pem       (key+cert bundle)
    """
    ca_dir.mkdir(parents=True, exist_ok=True)

    cert_path = ca_dir / "egress-ca.crt"
    key_path = ca_dir / "egress-ca.key"
    mitm_cert_path = ca_dir / "mitmproxy-ca-cert.pem"
    mitm_bundle_path = ca_dir / "mitmproxy-ca.pem"
    openssl_conf = ca_dir / "openssl.cnf"

    created = False

    if overwrite or not _existing_ca_is_valid(cert_path, key_path):
        # Minimal config to guarantee proper CA extensions.
        openssl_conf.write_text(
            """[req]
distinguished_name=req_distinguished_name
x509_extensions=v3_ca
prompt=no

[req_distinguished_name]
CN=unused

[v3_ca]
basicConstraints=critical,CA:TRUE
keyUsage=critical,keyCertSign,cRLSign
subjectKeyIdentifier=hash
""",
            encoding="utf-8",
        )

        # Generate key + self-signed CA cert.
        _run_openssl(["genrsa", "-out", str(key_path), str(key_bits)], cwd=ca_dir)
        _set_private_key_mode(key_path)

        _run_openssl(
            [
                "req",
                "-x509",
                "-new",
                "-key",
                str(key_path),
                "-sha256",
                "-days",
                str(days_valid),
                "-out",
                str(cert_path),
                "-subj",
                f"/CN={common_name}",
                "-config",
                str(openssl_conf),
                "-extensions",
                "v3_ca",
            ],
            cwd=ca_dir,
        )
        created = True

        # Sanity: fail fast if we somehow produced a non-CA cert.
        if not _existing_ca_is_valid(cert_path, key_path):
            raise EgressCAError("generated CA is invalid (missing CA:TRUE and/or key mismatch)")

    # Derive mitmproxy files from the *same* CA.
    shutil.copyfile(cert_path, mitm_cert_path)
    _write_mitmproxy_bundle(cert_path=cert_path, key_path=key_path, bundle_path=mitm_bundle_path)

    return {
        "created": created,
        "common_name": common_name,
        "egress_ca_crt": str(cert_path),
        "egress_ca_key": str(key_path),
        "mitmproxy_ca_pem": str(mitm_bundle_path),
        "mitmproxy_ca_cert_pem": str(mitm_cert_path),
    }
```

### `honeypot-platform/packages/hoho_runtime/hoho_runtime/orchestration/compose_down_all.py`  _(~5.2 KB; showing ≤800 lines)_
```python
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import json
import re
import subprocess


@dataclass
class DownAllResult:
    projects_found: list[str]
    projects_stopped: list[str]
    projects_failed: list[str]
    stray_projects_cleaned: list[str]


def _sanitize_project_name(value: str) -> str:
    sanitized = re.sub(r"[^a-z0-9_-]", "-", value.lower()).strip("-_")
    return sanitized or "hoho"


def _run_cmd(cmd: list[str]) -> tuple[int, str, str]:
    proc = subprocess.run(cmd, capture_output=True, text=True)
    return proc.returncode, proc.stdout, proc.stderr


def _run_action(cmd: list[str], *, dry_run: bool) -> int:
    print("$ " + " ".join(cmd))
    if dry_run:
        return 0
    proc = subprocess.run(cmd)
    return proc.returncode


def _list_compose_projects() -> set[str]:
    projects: set[str] = set()
    rc, stdout, _ = _run_cmd(["docker", "compose", "ls", "--format", "json"])
    if rc == 0 and stdout.strip():
        try:
            payload = json.loads(stdout)
            if isinstance(payload, list):
                for entry in payload:
                    if not isinstance(entry, dict):
                        continue
                    name = entry.get("Name") or entry.get("name")
                    if isinstance(name, str) and name.startswith("hoho-"):
                        projects.add(name)
        except json.JSONDecodeError:
            pass
    return projects


def _list_projects_by_label() -> set[str]:
    projects: set[str] = set()
    cmd = [
        "docker",
        "ps",
        "-a",
        "--filter",
        "label=com.docker.compose.project",
        "--format",
        "{{.Label \"com.docker.compose.project\"}}",
    ]
    rc, stdout, _ = _run_cmd(cmd)
    if rc != 0:
        return projects

    for line in stdout.splitlines():
        project = line.strip()
        if project.startswith("hoho-"):
            projects.add(project)
    return projects


def _remove_stray_project(project_name: str, *, remove_volumes: bool, dry_run: bool) -> bool:
    failed = False

    rc, stdout, _ = _run_cmd(
        ["docker", "ps", "-a", "--filter", f"label=com.docker.compose.project={project_name}", "-q"]
    )
    container_ids = [item for item in stdout.split() if item]
    if rc == 0 and container_ids:
        cmd = ["docker", "rm", "-f", *container_ids]
        if _run_action(cmd, dry_run=dry_run) != 0:
            failed = True

    rc, stdout, _ = _run_cmd(
        ["docker", "network", "ls", "-q", "--filter", f"label=com.docker.compose.project={project_name}"]
    )
    network_ids = [item for item in stdout.split() if item]
    if rc == 0 and network_ids:
        cmd = ["docker", "network", "rm", *network_ids]
        if _run_action(cmd, dry_run=dry_run) != 0:
            failed = True

    if remove_volumes:
        rc, stdout, _ = _run_cmd(
            ["docker", "volume", "ls", "-q", "--filter", f"label=com.docker.compose.project={project_name}"]
        )
        volume_ids = [item for item in stdout.split() if item]
        if rc == 0 and volume_ids:
            cmd = ["docker", "volume", "rm", *volume_ids]
            if _run_action(cmd, dry_run=dry_run) != 0:
                failed = True

    return not failed


def down_all(
    repo_root: Path,
    *,
    remove_volumes: bool = False,
    dry_run: bool = False,
    include_stale: bool = True,
) -> DownAllResult:
    """
    Stops/removes all hoho honeypot compose projects.
    Primary source of truth: deploy/compose/<honeypot_id>/docker-compose.yml.
    Secondary (stale) cleanup: docker compose ls + docker labels.
    """
    compose_files = sorted((repo_root / "deploy" / "compose").glob("*/docker-compose.yml"))

    projects_found: list[str] = []
    projects_stopped: list[str] = []
    projects_failed: list[str] = []
    stray_projects_cleaned: list[str] = []

    handled_projects: set[str] = set()

    for compose_file in compose_files:
        honeypot_id = compose_file.parent.name
        project_name = _sanitize_project_name(f"hoho-{honeypot_id}")

        projects_found.append(project_name)
        handled_projects.add(project_name)

        cmd = ["docker", "compose", "-p", project_name, "-f", str(compose_file), "down", "--remove-orphans"]
        if remove_volumes:
            cmd.append("--volumes")

        rc = _run_action(cmd, dry_run=dry_run)
        if rc == 0:
            projects_stopped.append(project_name)
        else:
            projects_failed.append(project_name)

    if include_stale:
        stale_projects = _list_compose_projects() | _list_projects_by_label()
        for project_name in sorted(stale_projects):
            if not project_name.startswith("hoho-"):
                continue
            if project_name in handled_projects:
                continue

            if _remove_stray_project(project_name, remove_volumes=remove_volumes, dry_run=dry_run):
                stray_projects_cleaned.append(project_name)
            else:
                projects_failed.append(project_name)

    return DownAllResult(
        projects_found=projects_found,
        projects_stopped=projects_stopped,
        projects_failed=projects_failed,
        stray_projects_cleaned=stray_projects_cleaned,
    )
```

### `honeypot-platform/packages/hoho_runtime/hoho_runtime/orchestration/compose_render.py`  _(~24.2 KB; showing ≤800 lines)_
```python
from copy import deepcopy
from pathlib import Path, PurePosixPath
import re
import shutil

import yaml

from hoho_runtime.config import DEFAULT_STORAGE_ROOT


SENSOR_IMAGES = {
    "proxy": "hoho/sensor-http-proxy:latest",
    "fsmon": "hoho/sensor-fsmon:latest",
    "pcap": "hoho/sensor-pcap:latest",
    "egress_proxy": "hoho/sensor-egress-proxy:latest",
    "falco": "hoho/sensor-falco:latest",
}


def _as_list(value) -> list:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def _collect_service_networks(service: dict) -> list[str]:
    networks = service.get("networks", [])
    if isinstance(networks, list):
        return [n for n in networks if isinstance(n, str)]
    if isinstance(networks, dict):
        return [n for n in networks.keys() if isinstance(n, str)]
    return []


def _parse_mount(volume_entry):
    if isinstance(volume_entry, str):
        parts = volume_entry.split(":")
        if len(parts) < 2:
            return None
        source = parts[0]
        target = parts[1]
        return {"source": source, "target": target, "raw": volume_entry}

    if isinstance(volume_entry, dict):
        source = volume_entry.get("source")
        target = volume_entry.get("target")
        if source and target:
            return {"source": source, "target": target, "raw": volume_entry}
    return None


def _find_covering_mount(service: dict, watch_path: str):
    watch = str(PurePosixPath(watch_path))
    best_mount = None
    best_len = -1
    for volume in _as_list(service.get("volumes", [])):
        parsed = _parse_mount(volume)
        if not parsed:
            continue
        target = str(PurePosixPath(parsed["target"]))
        if watch == target or watch.startswith(f"{target}/"):
            if len(target) > best_len:
                best_mount = parsed
                best_len = len(target)
    return best_mount


def _named_volume_source(source: str) -> bool:
    return not source.startswith("/") and not source.startswith(".")


def _collect_named_volumes(services: dict) -> set[str]:
    named = set()
    for service in services.values():
        for volume in _as_list(service.get("volumes", [])):
            parsed = _parse_mount(volume)
            if parsed and _named_volume_source(parsed["source"]):
                named.add(parsed["source"])
    return named


def _as_bool(value, default: bool = False) -> bool:
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in {"1", "true", "yes", "on"}
    return bool(value)


def _storage_env(honeypot_id: str, session_id: str | None = None, agent_id: str | None = None, telemetry: dict | None = None) -> dict:
    telemetry = telemetry or {}
    filters = telemetry.get("filters", {}) if isinstance(telemetry, dict) else {}
    return {
        "HOHO_PACK_ID": honeypot_id,
        "HOHO_HONEYPOT_ID": honeypot_id,
        "HOHO_STORAGE_BACKEND": "filesystem",
        "HOHO_STORAGE_ROOT": "/artifacts",
        "HOHO_SESSION_ID": session_id or "unknown-session",
        "HOHO_AGENT_ID": agent_id or "unknown-agent",
        "HOHO_EMIT_FILTERS_JSON": yaml.safe_dump(filters.get("emit", []), default_flow_style=True).strip() if filters.get("emit") is not None else "[]",
        "HOHO_FORWARD_FILTERS_JSON": yaml.safe_dump(filters.get("forward", []), default_flow_style=True).strip() if filters.get("forward") is not None else "[]",
    }


def _low_runtime_service(pack: dict, artifacts_bind_mount: str, honeypot_dir: Path, session_id: str | None = None, agent_id: str | None = None) -> dict:
    listen = _as_list(pack.get("listen", []))
    ports = []
    for entry in listen:
        if not isinstance(entry, dict):
            continue
        port = entry.get("port")
        if port is None:
            continue
        ports.append(f"{int(port)}:{int(port)}")

    return {
        "image": "hoho/low-runtime:latest",
        "environment": {
            **_storage_env(pack["metadata"]["id"], session_id=session_id, agent_id=agent_id, telemetry=pack.get("telemetry", {})),
            "HOHO_PACK_PATH": "/honeypot/honeypot.yaml",
        },
        "volumes": [
            artifacts_bind_mount,
            f"{honeypot_dir.resolve()}:/honeypot:ro",
        ],
        "ports": ports,
    }




def _sanitize_name(value: str) -> str:
    sanitized = re.sub(r"[^a-z0-9_-]", "-", value.lower()).strip("-_")
    return sanitized or "hoho"


def _inject_egress_proxy_env(service: dict, service_names: list[str], port: int, set_env_bundles: bool):
    env = service.setdefault("environment", {})
    proxy_url = f"http://egress:{port}"
    no_proxy = ",".join(["localhost", "127.0.0.1", *service_names])

    env["HTTP_PROXY"] = proxy_url
    env["HTTPS_PROXY"] = proxy_url
    env["NO_PROXY"] = no_proxy
    env["http_proxy"] = proxy_url
    env["https_proxy"] = proxy_url
    env["no_proxy"] = no_proxy

    if set_env_bundles:
        env["SSL_CERT_FILE"] = "/hoho/ca/egress-ca.crt"
        env["REQUESTS_CA_BUNDLE"] = "/hoho/ca/egress-ca.crt"
        env["CURL_CA_BUNDLE"] = "/hoho/ca/egress-ca.crt"
        env["NODE_EXTRA_CA_CERTS"] = "/hoho/ca/egress-ca.crt"


def render_compose(
    pack: dict,
    out_dir: str | None = None,
    artifacts_root: str | None = None,
    honeypot_dir: str | Path | None = None,
    session_id: str | None = None,
    agent_id: str | None = None,
) -> Path:
    pack_id = pack["metadata"]["id"]
    interaction = pack.get("metadata", {}).get("interaction")
    root = Path(out_dir or f"./deploy/compose/{pack_id}")
    shutil.rmtree(root, ignore_errors=True)
    root.mkdir(parents=True, exist_ok=True)

    runtime_root = root / "runtime"
    runtime_dir = runtime_root / "ca"
    runtime_dir.mkdir(parents=True, exist_ok=True)
    falco_runtime_dir = runtime_root / "falco"
    falco_runtime_dir.mkdir(parents=True, exist_ok=True)
    install_script = runtime_dir / "install-ca.sh"
    install_script.write_text(
        """#!/usr/bin/env sh
set -eu

cert_path=${1:-/hoho/ca/egress-ca.crt}
if [ ! -f \"$cert_path\" ]; then
    echo \"CA cert not found: $cert_path\" >&2
    exit 1
fi

if ! command -v update-ca-certificates >/dev/null 2>&1 && ! command -v update-ca-trust >/dev/null 2>&1; then
    if command -v apt-get >/dev/null 2>&1; then
        apt-get update >/dev/null 2>&1 || true
        apt-get install -y ca-certificates >/dev/null 2>&1 || true
    elif command -v apk >/dev/null 2>&1; then
        apk add --no-cache ca-certificates >/dev/null 2>&1 || true
    elif command -v dnf >/dev/null 2>&1; then
        dnf install -y ca-certificates >/dev/null 2>&1 || true
    elif command -v yum >/dev/null 2>&1; then
        yum install -y ca-certificates >/dev/null 2>&1 || true
    fi
fi

if command -v update-ca-certificates >/dev/null 2>&1; then
    mkdir -p /usr/local/share/ca-certificates
    cp "$cert_path" /usr/local/share/ca-certificates/hoho-egress-ca.crt
    update-ca-certificates || true
fi

if command -v update-ca-trust >/dev/null 2>&1; then
    mkdir -p /etc/pki/ca-trust/source/anchors
    cp "$cert_path" /etc/pki/ca-trust/source/anchors/hoho-egress-ca.crt
    update-ca-trust extract || true
fi

if [ -n "${HOHO_TRUST_EXTRA_COMMANDS:-}" ]; then
    printf '%s\n' "${HOHO_TRUST_EXTRA_COMMANDS}" | while IFS= read -r cmd; do
        [ -n "$cmd" ] || continue
        sh -c "$cmd" || true
    done
fi

exit 0
""",
        encoding="utf-8",
    )

    storage_root = Path(artifacts_root or pack.get("storage", {}).get("root", DEFAULT_STORAGE_ROOT))
    storage_root.mkdir(parents=True, exist_ok=True)
    artifacts_bind_mount = f"{storage_root.resolve()}:/artifacts"

    if interaction == "low":
        if honeypot_dir is None:
            raise ValueError("low interaction compose rendering requires honeypot_dir")
        services = {"honeypot": _low_runtime_service(pack, artifacts_bind_mount, Path(honeypot_dir), session_id=session_id, agent_id=agent_id)}
    else:
        services = deepcopy(pack.get("stack", {}).get("services", {}))


    telemetry = pack.get("telemetry", {}) if isinstance(pack.get("telemetry", {}), dict) else {}
    for service in services.values():
        env = service.setdefault("environment", {})
        env.setdefault("HOHO_HONEYPOT_ID", pack_id)
        env.setdefault("HOHO_SESSION_ID", session_id or "unknown-session")
        env.setdefault("HOHO_AGENT_ID", agent_id or "unknown-agent")
        env.setdefault("HOHO_EMIT_FILTERS_JSON", yaml.safe_dump(telemetry.get("filters", {}).get("emit", []), default_flow_style=True).strip())
        env.setdefault("HOHO_FORWARD_FILTERS_JSON", yaml.safe_dump(telemetry.get("filters", {}).get("forward", []), default_flow_style=True).strip())

    valid_attach_services = set(services.keys())
    networks_used: set[str] = set()
    network_defs: dict[str, dict] = {}

    for service in services.values():
        networks_used.update(_collect_service_networks(service))

    for sensor in pack.get("sensors", []):
        sname = sensor["name"]
        stype = sensor["type"]
        attach = sensor.get("attach", {})
        config = sensor.get("config", {})

        sensor_service = {
            "image": SENSOR_IMAGES.get(stype, "busybox:latest"),
            "environment": _storage_env(pack_id, session_id=session_id, agent_id=agent_id, telemetry=pack.get("telemetry", {})),
            "volumes": [artifacts_bind_mount],
        }

        if stype == "fsmon":
            target_service_name = attach.get("service")
            target_service = services.get(target_service_name)
            if not target_service:
                raise ValueError(f"fsmon sensor '{sname}' attaches to unknown service '{target_service_name}'")

            watch_paths = _as_list(config.get("watch", []))
            if not watch_paths:
                raise ValueError(f"fsmon sensor '{sname}' requires config.watch")

            allow_globs = _as_list(config.get("allow_globs"))
            deny_globs = _as_list(config.get("deny_globs"))
            sensor_service["environment"].update(
                {
                    "FSMON_WATCH": ",".join(watch_paths),
                    "FSMON_ALLOW": ",".join(allow_globs) if allow_globs else "*",
                    "FSMON_DENY": ",".join(deny_globs),
                }
            )
            if config.get("max_bytes") is not None:
                sensor_service["environment"]["FSMON_MAX_BYTES"] = str(config["max_bytes"])

            seen_mounts = set()
            for watch_path in watch_paths:
                mount = _find_covering_mount(target_service, watch_path)
                if not mount:
                    raise ValueError(
                        f"fsmon watch path {watch_path} is not backed by a named volume/bind mount in service {target_service_name}; "
                        "sidecar can't see container rootfs"
                    )
                mount_key = (mount["source"], mount["target"])
                if mount_key in seen_mounts:
                    continue
                seen_mounts.add(mount_key)
                sensor_service["volumes"].append(f"{mount['source']}:{mount['target']}")

            target_networks = _collect_service_networks(target_service)
            if target_networks:
                sensor_service["networks"] = target_networks
                networks_used.update(target_networks)

        elif stype == "proxy":
            target_service_name = attach.get("service")
            target_service = services.get(target_service_name)
            if not target_service:
                raise ValueError(f"proxy sensor '{sname}' attaches to unknown service '{target_service_name}'")
            upstream = config.get("upstream")
            if not upstream:
                raise ValueError(f"proxy sensor '{sname}' requires config.upstream")

            listen_port = int(config.get("listen_port", 8080))
            listen_host = str(config.get("listen_host", "0.0.0.0"))
            keep_host_header = _as_bool(config.get("keep_host_header"), default=True)
            sensor_service["environment"].update(
                {
                    "UPSTREAM": upstream,
                    "PROXY_LISTEN_PORT": str(listen_port),
                    "PROXY_LISTEN_HOST": listen_host,
                    "PROXY_KEEP_HOST_HEADER": "true" if keep_host_header else "false",
                }
            )

            target_networks = _collect_service_networks(target_service)
            if target_networks:
                sensor_service["networks"] = target_networks
                networks_used.update(target_networks)

            moved_ports = _as_list(target_service.get("ports", []))
            if moved_ports:
                proxy_ports = []
                for port in moved_ports:
                    if isinstance(port, str) and ":" in port:
                        host_port = port.rsplit(":", 1)[0]
                        proxy_ports.append(f"{host_port}:{listen_port}")
                    else:
                        proxy_ports.append(port)
                sensor_service["ports"] = proxy_ports
                target_service["ports"] = []

        elif stype == "pcap":
            target_service_name = attach.get("service")
            target_network = attach.get("network")
            if target_service_name:
                if target_service_name not in valid_attach_services:
                    raise ValueError(f"pcap sensor '{sname}' attaches to unknown service '{target_service_name}'")
                sensor_service["network_mode"] = f"service:{target_service_name}"
            elif target_network:
                sensor_service["networks"] = [target_network]
                networks_used.add(target_network)

            sensor_service["cap_add"] = ["NET_ADMIN", "NET_RAW"]
            if config.get("rotate_seconds") is not None:
                sensor_service["environment"]["PCAP_ROTATE_SECONDS"] = str(config["rotate_seconds"])
            if config.get("rotate_count") is not None:
                sensor_service["environment"]["PCAP_ROTATE_COUNT"] = str(config["rotate_count"])
            if config.get("interface") is not None:
                sensor_service["environment"]["PCAP_INTERFACE"] = str(config["interface"])

        elif stype == "falco":
            if interaction != "high":
                raise ValueError("falco sensor is only supported for high interaction honeypots")

            mode = str(config.get("mode", "privileged"))
            engine = str(config.get("engine", "modern_ebpf"))
            priority_min = str(config.get("priority_min", "Warning"))
            append_fields = _as_list(config.get("append_fields", []))
            any_exec = _as_bool(config.get("any_exec"), default=False)
            enforce = config.get("enforce", {})
            enforce_enabled = _as_bool(enforce.get("enabled"), default=False)
            enforce_priorities = _as_list(enforce.get("match_priorities", ["Critical", "Error"]))
            enforce_rules = _as_list(enforce.get("match_rules", []))
            enforce_action = str(enforce.get("action", "stop_container"))
            cooldown_seconds = int(enforce.get("cooldown_seconds", 60))

            project_name = _sanitize_name(f"hoho-{pack_id}")
            attach_services = _as_list(attach.get("services", []))
            for attach_service_name in attach_services:
                if attach_service_name not in valid_attach_services:
                    raise ValueError(f"falco sensor '{sname}' attaches to unknown service '{attach_service_name}'")

            default_rules = ["/app/rules/hoho_rules.yaml"]
            if any_exec:
                default_rules.append("/app/rules/hoho_any_exec.yaml")

            sensor_service["environment"].update(
                {
                    "FALCO_PRIORITY_MIN": priority_min,
                    "FALCO_ENGINE": engine,
                    "FALCO_RULES": ",".join(default_rules),
                    "HOHO_FALCO_PROJECT": project_name,
                    "HOHO_FALCO_ONLY_PROJECT": "true",
                    "HOHO_FALCO_APPEND_FIELDS": ",".join(str(f) for f in append_fields if f),
                    "HOHO_FALCO_ENFORCE_ENABLED": "true" if enforce_enabled else "false",
                    "HOHO_FALCO_ENFORCE_MATCH_PRIORITIES": ",".join(str(x) for x in enforce_priorities),
                    "HOHO_FALCO_ENFORCE_MATCH_RULES": ",".join(str(x) for x in enforce_rules),
                    "HOHO_FALCO_ENFORCE_ACTION": enforce_action,
                    "HOHO_FALCO_ENFORCE_COOLDOWN_SECONDS": str(cooldown_seconds),
                }
            )
            if attach_services:
                sensor_service["environment"]["HOHO_FALCO_ONLY_SERVICES"] = ",".join(attach_services)

            custom_rules = []
            for rule_path in _as_list(config.get("rules", [])):
                if not isinstance(rule_path, str) or not rule_path:
                    continue
                if rule_path.startswith("runtime/falco/"):
                    continue
                if rule_path.startswith("./"):
                    rule_src = (Path(honeypot_dir) / rule_path).resolve() if honeypot_dir else None
                    if rule_src and rule_src.is_file():
                        dst = falco_runtime_dir / rule_src.name
                        shutil.copy2(rule_src, dst)
                        custom_rules.append(f"/runtime/falco/{dst.name}")
                else:
                    custom_rules.append(rule_path)

            rules_all = [*default_rules, *custom_rules]
            sensor_service["environment"]["FALCO_RULES"] = ",".join(rules_all)

            tracefs_host = Path("/sys/kernel/tracing")
            if not tracefs_host.exists():
                tracefs_host = Path("/sys/kernel/debug/tracing")
            
            if engine in {"kmod", "ebpf"}:
                sensor_service["volumes"].extend([
                    "/dev:/host/dev",
                    "/boot:/host/boot:ro",
                    "/lib/modules:/host/lib/modules:ro",
                    "/usr:/host/usr:ro",
                ])

            sensor_service["volumes"].extend(
                [
                    f"{falco_runtime_dir.resolve()}:/runtime/falco:ro",
                    f"{tracefs_host}:/sys/kernel/tracing:ro",
                    "/proc:/host/proc:ro",
                    "/etc:/host/etc:ro",
                    "/var/run/docker.sock:/host/var/run/docker.sock",
                ]
            )

            sensor_service.setdefault("security_opt", [])
            if "apparmor:unconfined" not in sensor_service["security_opt"]:
                sensor_service["security_opt"].append("apparmor:unconfined")

            # Critical for modern eBPF: allow mlocking BPF maps
            sensor_service.setdefault("ulimits", {})
            sensor_service["ulimits"]["memlock"] = {"soft": -1, "hard": -1}

            if mode == "privileged":
                sensor_service["privileged"] = True
            sensor_service["network_mode"] = "host"
        elif stype == "egress_proxy":
            attach_services = _as_list(attach.get("services", []))
            for attach_service_name in attach_services:
                if attach_service_name not in valid_attach_services:
                    raise ValueError(
                        f"egress_proxy sensor '{sname}' attaches to unknown service '{attach_service_name}'"
                    )

            listen_host = str(config.get("listen_host", "0.0.0.0"))
            listen_port = int(config.get("listen_port", 3128))
            force_egress = _as_bool(config.get("force_egress_via_proxy"), default=True)

            tls_mitm = config.get("tls_mitm", {})
            tls_mitm_enabled = _as_bool(tls_mitm.get("enabled"), default=False)
            install_trust = tls_mitm.get("install_trust", {})
            set_env_bundles = _as_bool(install_trust.get("also_set_env_bundles"), default=True)
            extra_commands = _as_list(install_trust.get("extra_commands", []))

            capture = config.get("capture", {})
            capture_enabled = _as_bool(capture.get("enabled"), default=True)
            capture_bodies = str(capture.get("bodies", "*"))
            capture_max_bytes = int(capture.get("max_bytes", 52428800))
            capture_store_ok_only = _as_bool(capture.get("store_ok_only"), default=True)
            capture_min_bytes = int(capture.get("min_bytes", 1))
            redact_headers =[REDACTED]

            sensor_service["environment"].update(
                {
                    "PROXY_LISTEN_HOST": listen_host,
                    "PROXY_LISTEN_PORT": str(listen_port),
                    "PROXY_STACK_ID": pack_id,
                    "PROXY_TLS_MITM_ENABLED": "true" if tls_mitm_enabled else "false",
                    "PROXY_CA_CERT_PATH": "/runtime/ca/egress-ca.crt",
                    "PROXY_CA_KEY_PATH": "/runtime/ca/egress-ca.key",
                    "PROXY_MITM_BUNDLE_PATH": "/runtime/ca/mitmproxy-ca.pem",
                    "PROXY_MITM_CERT_PATH": "/runtime/ca/mitmproxy-ca-cert.pem",
                    "PROXY_CAPTURE_ENABLED": "true" if capture_enabled else "false",
                    "PROXY_CAPTURE_BODIES": capture_bodies,
                    "PROXY_CAPTURE_MAX_BYTES": str(capture_max_bytes),
                    "PROXY_CAPTURE_STORE_OK_ONLY": "true" if capture_store_ok_only else "false",
                    "PROXY_CAPTURE_MIN_BYTES": str(capture_min_bytes),
                    "PROXY_REDACT_HEADERS": ",".join(redact_headers),
                }
            )
            sensor_service["volumes"].append(f"{(root / 'runtime').resolve()}:/runtime:ro")
            sensor_service["volumes"].append(f"{(root / 'runtime' / 'ca').resolve()}:/runtime/ca:ro")
            sensor_service["volumes"].append(f"{(storage_root / pack_id).resolve()}:/artifacts/{pack_id}")

            all_service_names = sorted([name for name in services.keys() if name != sname])
            for attach_service_name in attach_services:
                attach_service = services[attach_service_name]
                _inject_egress_proxy_env(attach_service, all_service_names, listen_port, set_env_bundles)
                if tls_mitm_enabled:
                    if extra_commands:
                        attach_service.setdefault("environment", {})["HOHO_TRUST_EXTRA_COMMANDS"] = "\n".join(
                            str(cmd) for cmd in extra_commands
                        )
                    attach_service.setdefault("volumes", []).extend(
                        [
                            f"{(root / 'runtime' / 'ca' / 'install-ca.sh').resolve()}:/hoho/ca/install-ca.sh:ro",
                            f"{(root / 'runtime' / 'ca' / 'egress-ca.crt').resolve()}:/hoho/ca/egress-ca.crt:ro",
                        ]
                    )

            sensor_service["networks"] = list(networks_used)
            #networks_used.update({"hp_internal", "hp_external", "frontend"})
            
            if force_egress:
                network_defs["hp_internal"] = {"internal": True}
                network_defs["hp_external"] = {}
                sensor_service["networks"] = ["hp_internal", "hp_external"]
                networks_used.update({"hp_internal", "hp_external"})

                for attach_service_name in attach_services:
                    services[attach_service_name]["networks"] = ["hp_internal"]

        services[sname] = sensor_service


    forwarding = telemetry.get("forwarding", {}) if isinstance(telemetry, dict) else {}
    if _as_bool(forwarding.get("enabled"), default=False):
        token_env = forwarding.get("token_env", "HOHO_HUB_TOKEN")
        hub_url = forwarding.get("hub_url", "")
        fwd_env = _storage_env(pack_id, session_id=session_id, agent_id=agent_id, telemetry=telemetry)
        fwd_env.update({
            "HOHO_HUB_URL": hub_url,
            "HOHO_HUB_TOKEN": f"${{{token_env}}}",
        })
        services["telemetry-forwarder"] = {
            "image": "hoho/telemetry-forwarder:latest",
            "environment": fwd_env,
            "volumes": [artifacts_bind_mount],
        }

    compose = {"services": services}

    named_volumes = sorted(_collect_named_volumes(services))
    if named_volumes:
        compose["volumes"] = {volume_name: {} for volume_name in named_volumes}

    if networks_used or network_defs:
        compose["networks"] = {name: network_defs.get(name, {}) for name in sorted(networks_used | set(network_defs.keys()))}

    out = root / "docker-compose.yml"
    out.write_text(yaml.safe_dump(compose, sort_keys=False), encoding="utf-8")
    return out
```

### `honeypot-platform/packages/hoho_runtime/hoho_runtime/orchestration/compose_run.py`  _(~6.7 KB; showing ≤800 lines)_
```python
import json
import os
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

from hoho_core.model.event import build_base_event

def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _append_event(storage_pack_root: Path, event: dict) -> None:
    events_path = storage_pack_root / "index" / "events.jsonl"
    events_path.parent.mkdir(parents=True, exist_ok=True)
    with events_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event) + "\n")


def ensure_pack_eventlog(artifacts_pack_root: Path) -> Path:
    """
    Ensure <root>/index/events.jsonl exists and is writable by current user.
    Returns the path to events.jsonl.
    """
    index_path = artifacts_pack_root / "index"
    index_path.mkdir(parents=True, exist_ok=True)

    events_path = index_path / "events.jsonl"
    try:
        fd = os.open(events_path, os.O_CREAT | os.O_APPEND | os.O_WRONLY, 0o666)
    except OSError as exc:
        raise SystemExit(
            "[hoho] ERROR: unable to create/open events log before startup: "
            f"{events_path} ({exc}). Fix ownership and retry, e.g. `sudo chown -R "
            f"$USER:$USER {artifacts_pack_root}`."
        ) from exc

    try:
        os.fchmod(fd, 0o666)
    finally:
        os.close(fd)

    if not os.access(events_path, os.W_OK):
        owner_uid = events_path.stat().st_uid
        owner_gid = events_path.stat().st_gid
        current_uid = os.getuid()
        current_gid = os.getgid()
        raise SystemExit(
            "[hoho] ERROR: events log is not writable before startup: "
            f"{events_path} (owner={owner_uid}:{owner_gid}, current={current_uid}:{current_gid}). "
            "Fix ownership and retry, e.g. `sudo chown -R $USER:$USER "
            f"{artifacts_pack_root}`."
        )

    return events_path


def _emit_ca_install_event(
    *,
    storage_pack_root: Path,
    honeypot_id: str,
    service_name: str,
    event_name: str,
    session_id: str,
    agent_id: str,
    exit_code: int | None = None,
    stderr_snippet: str | None = None,
) -> None:
    event = build_base_event(
        honeypot_id=honeypot_id,
        component="runtime.compose",
        proto="runtime",
        session_id=session_id,
        agent_id=agent_id,
        event_name=event_name,
    )
    event["runtime"] = {"service": service_name}
    if exit_code is not None:
        event["runtime"]["exit_code"] = exit_code
    if stderr_snippet:
        event["runtime"]["stderr_snippet"] = stderr_snippet
    try:
        _append_event(storage_pack_root, event)
    except OSError as exc:
        print(f"[hoho] WARN: cannot append to events.jsonl: {exc}")




def _bool_enabled(value: object, default: bool = False) -> bool:
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return bool(value)
    return str(value).strip().lower() in {"1", "true", "yes", "on"}

def _run_ca_install(
    *,
    compose_file: Path,
    project_name: str | None,
    env_file: Path | None,
    service_name: str,
    storage_pack_root: Path,
    honeypot_id: str,
    session_id: str,
    agent_id: str,
) -> None:
    cmd = _compose_base_cmd(compose_file, project_name, env_file=env_file)
    cmd.extend(["exec", "-T", service_name, "sh", "/hoho/ca/install-ca.sh", "/hoho/ca/egress-ca.crt"])
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode == 0:
        _emit_ca_install_event(
            storage_pack_root=storage_pack_root,
            honeypot_id=honeypot_id,
            service_name=service_name,
            event_name="runtime.ca_install",
            session_id=session_id,
            agent_id=agent_id,
        )
        return

    stderr = (proc.stderr or "").strip()
    _emit_ca_install_event(
        storage_pack_root=storage_pack_root,
        honeypot_id=honeypot_id,
        service_name=service_name,
        event_name="runtime.ca_install",
        session_id=session_id,
        agent_id=agent_id,
        exit_code=proc.returncode,
        stderr_snippet=stderr[:500],
    )

def _compose_base_cmd(compose_file: Path, project_name: str | None, env_file: Path | None = None) -> list[str]:
    cmd = ["docker", "compose"]
    if env_file is not None:
        cmd.extend(["--env-file", str(env_file)])
    if project_name:
        cmd.extend(["-p", project_name])
    cmd.extend(["-f", str(compose_file)])
    return cmd

def run_compose(
    compose_file: Path,
    project_name: str | None = None,
    *,
    pack: dict | None = None,
    artifacts_root: Path | None = None,
    attach_logs: bool = True,
    log_services: Iterable[str] | None = None,  # None => all services
    log_tail: int | str = "all",                  # e.g. 0, 200, "all"
    log_no_color: bool = True,
    env_file: Path | None = None,
    session_id: str = "unknown-session",
    agent_id: str = "unknown-agent",
) -> int:
    if pack and artifacts_root:
        honeypot_id = pack.get("metadata", {}).get("id", "unknown-pack")
        storage_pack_root = artifacts_root / honeypot_id
        storage_pack_root.mkdir(parents=True, exist_ok=True)
        (storage_pack_root / "ca").mkdir(parents=True, exist_ok=True)
        ensure_pack_eventlog(storage_pack_root)

    base = _compose_base_cmd(compose_file, project_name, env_file=env_file)

    # 1) Start detached so post-start steps can run.
    rc = subprocess.call([*base, "up", "-d"])
    if rc != 0:
        return rc

    # 2) Post-start installs (CA, etc.)
    if pack and artifacts_root:
        honeypot_id = pack.get("metadata", {}).get("id", "unknown-pack")
        storage_pack_root = artifacts_root / honeypot_id

        for sensor in pack.get("sensors", []):
            if sensor.get("type") != "egress_proxy":
                continue
            tls_mitm = sensor.get("config", {}).get("tls_mitm", {})
            if not _bool_enabled(tls_mitm.get("enabled", False)):
                continue
            for service in sensor.get("attach", {}).get("services", []):
                _run_ca_install(
                    compose_file=compose_file,
                    project_name=project_name,
                    env_file=env_file,
                    service_name=service,
                    storage_pack_root=storage_pack_root,
                    honeypot_id=honeypot_id,
                    session_id=session_id,
                    agent_id=agent_id,
                )

    # 3) Attach back to logs AFTER everything is installed.
    if attach_logs:
        cmd = [*base, "logs", "-f", "--tail", str(log_tail)]
        if log_no_color:
            cmd.append("--no-color")
        if log_services:
            cmd.extend(list(log_services))
        return subprocess.call(cmd)

    return 0
```

### `honeypot-platform/packages/hoho_runtime/hoho_runtime/server/__init__.py`  _(~0.0 KB; showing ≤800 lines)_
```python

```

### `honeypot-platform/packages/hoho_runtime/hoho_runtime/server/http.py`  _(~3.0 KB; showing ≤800 lines)_
```python
import json
import os
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
        event = build_base_event(
            honeypot_id=self.pack["metadata"]["id"],
            component="runtime.http",
            proto="http",
            session_id=os.getenv("HOHO_SESSION_ID", "unknown-session"),
            agent_id=os.getenv("HOHO_AGENT_ID", "unknown-agent"),
            event_name="http.request",
        )
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

### `honeypot-platform/runtimes/low_runtime/Dockerfile`  _(~0.2 KB; showing ≤800 lines)_
```
FROM python:3.11-slim

WORKDIR /app

COPY packages/hoho_core /src/hoho_core
COPY packages/hoho_runtime /src/hoho_runtime

RUN pip install --no-cache-dir /src/hoho_core /src/hoho_runtime

ENTRYPOINT ["python", "-m", "hoho_runtime.container.low_runtime"]
```

### `honeypot-platform/runtimes/low_runtime/README.md`  _(~0.2 KB; showing ≤800 lines)_
```md
# low_runtime

Container runtime for low-interaction honeypots.

Build from `honeypot-platform/`:

```bash
docker build -t hoho/low-runtime:latest -f runtimes/low_runtime/Dockerfile .
```
```

### `honeypot-platform/scripts/build_sensors.sh`  _(~1.4 KB; showing ≤800 lines)_
```bash
#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

mkdir -p sensors/fsmon/packages/
cp -r packages/hoho_core sensors/fsmon/packages/hoho_core
docker build -t hoho/sensor-fsmon:latest sensors/fsmon

mkdir -p sensors/http_proxy/packages/
cp -r packages/hoho_core sensors/http_proxy/packages/hoho_core
docker build -t hoho/sensor-http-proxy:latest sensors/http_proxy

mkdir -p sensors/pcap/packages/
cp -r packages/hoho_core sensors/pcap/packages/hoho_core
docker build -t hoho/sensor-pcap:latest sensors/pcap

mkdir -p sensors/egress_proxy/packages/
cp -r packages/hoho_core sensors/egress_proxy/packages/hoho_core
docker build -t hoho/sensor-egress-proxy:latest sensors/egress_proxy

mkdir -p sensors/falco/packages/
cp -r packages/hoho_core sensors/falco/packages/hoho_core
docker build -t hoho/sensor-falco:latest sensors/falco

# low interaction runtime
docker build -t hoho/low-runtime:latest -f runtimes/low_runtime/Dockerfile .

# docker build -t hoho/sensor-fsmon:latest        -f sensors/fsmon/        .
# docker build -t hoho/sensor-http-proxy:latest   -f sensors/http_proxy/Dockerfile   .
# docker build -t hoho/sensor-egress-proxy:latest -f sensors/egress_proxy/Dockerfile .
# docker build -t hoho/sensor-pcap:latest         -f sensors/pcap/Dockerfile         .
# docker build -t hoho/sensor-falco:latest        -f sensors/falco/Dockerfile        .

# docker build -t hoho/low-runtime:latest -f runtimes/low_runtime/Dockerfile .
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

### `honeypot-platform/scripts/check_layout.sh`  _(~0.5 KB; showing ≤800 lines)_
```bash
#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

fail() {
  echo "layout check failed: $1" >&2
  exit 1
}

RUNS_SUBTREE="runs"
LEGACY_RUNS_PATH="run/artifacts/${RUNS_SUBTREE}"

if [ -d "$LEGACY_RUNS_PATH" ]; then
  fail "forbidden path exists: ${LEGACY_RUNS_PATH}"
fi

if find honeypots -type f \( -name 'docker-compose*.yml' -o -name 'docker-compose*.yaml' \) | grep -q .; then
  fail "forbidden compose file found under honeypots/"
fi

python3 scripts/validate_honeypots_layout.py

echo "layout check passed"
```

### `honeypot-platform/scripts/migrate_honeypots_layout.py`  _(~4.8 KB; showing ≤800 lines)_
```python
#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import re
import shutil
from pathlib import Path

LEVELS = ("high", "low")
HONEYPOT_FILE = "honeypot.yaml"
README_FILE = "README.md"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def extract_metadata_id(yaml_text: str) -> str | None:
    metadata_match = re.search(r"^metadata:\s*\n([\s\S]*?)(?=^\S|\Z)", yaml_text, flags=re.M)
    if not metadata_match:
        return None
    md_block = metadata_match.group(1)
    id_match = re.search(r"^\s+id:\s*([\w.-]+)\s*$", md_block, flags=re.M)
    return id_match.group(1) if id_match else None


def find_pack_asset_roots(yaml_text: str, level: str) -> set[Path]:
    roots: set[Path] = set()
    prefix = f"./packs/{level}/"
    for match in re.finditer(r"([\"']?)(\./packs/(high|low)/[^\s\"']+)\1", yaml_text):
        value = match.group(2)
        if not value.startswith(prefix):
            continue
        rel = value[len(prefix) :]
        first = rel.split("/", 1)[0]
        if first:
            roots.add(Path(first))
    return roots


def rewrite_pack_paths(yaml_text: str, level: str) -> str:
    return yaml_text.replace(f"./packs/{level}/", "./")


def copy_file_if_missing(src: Path, dst: Path, warnings: list[str]) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        if sha256_file(src) != sha256_file(dst):
            warnings.append(f"conflict kept existing file: {dst}")
        return
    shutil.copy2(src, dst)


def merge_tree(src_root: Path, dst_root: Path, warnings: list[str]) -> None:
    for src in src_root.rglob("*"):
        rel = src.relative_to(src_root)
        dst = dst_root / rel
        if src.is_dir():
            dst.mkdir(parents=True, exist_ok=True)
        else:
            copy_file_if_missing(src, dst, warnings)


def migrate_level(repo_root: Path, level: str, dry_run: bool) -> tuple[int, list[str]]:
    packs_root = repo_root / "packs" / level
    honeypots_root = repo_root / "honeypots" / level
    honeypots_root.mkdir(parents=True, exist_ok=True)

    warnings: list[str] = []
    migrated = 0

    for pack_file in sorted(packs_root.glob("*.yaml")):
        yaml_text = pack_file.read_text(encoding="utf-8")
        honeypot_id = extract_metadata_id(yaml_text)
        if not honeypot_id:
            warnings.append(f"skipped (missing metadata.id): {pack_file}")
            continue

        target_dir = honeypots_root / honeypot_id
        target_dir.mkdir(parents=True, exist_ok=True)

        merge_candidates = [repo_root / "honeypots" / honeypot_id, repo_root / "honeypots" / level / honeypot_id]
        for candidate in merge_candidates:
            if candidate.is_dir():
                merge_tree(candidate, target_dir, warnings)

        for asset_root in sorted(find_pack_asset_roots(yaml_text, level)):
            src_asset = packs_root / asset_root
            dst_asset = target_dir / asset_root
            if not src_asset.exists():
                warnings.append(f"referenced asset missing: {src_asset}")
                continue
            if src_asset.is_dir():
                merge_tree(src_asset, dst_asset, warnings)
            else:
                copy_file_if_missing(src_asset, dst_asset, warnings)

        target_pack = target_dir / HONEYPOT_FILE
        rewritten = rewrite_pack_paths(yaml_text, level)
        if target_pack.exists() and target_pack.read_text(encoding="utf-8") != rewritten:
            warnings.append(f"overwrite canonical {HONEYPOT_FILE} from pack source: {target_pack}")
        if not dry_run:
            target_pack.write_text(rewritten, encoding="utf-8")

        readme = target_dir / README_FILE
        if not readme.exists() and not dry_run:
            readme.write_text(
                f"# {honeypot_id}\n\nMigrated honeypot. Document setup, run steps, and reset procedures here.\n",
                encoding="utf-8",
            )

        migrated += 1

    return migrated, warnings


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    total = 0
    warnings: list[str] = []

    for level in LEVELS:
        migrated, level_warnings = migrate_level(repo_root, level, args.dry_run)
        total += migrated
        warnings.extend(level_warnings)

    print(f"[migrate] mode={'dry-run' if args.dry_run else 'apply'} migrated_packs={total}")
    if warnings:
        print("[migrate] warnings:")
        for item in warnings:
            print(f"  - {item}")


if __name__ == "__main__":
    main()
```

### `honeypot-platform/scripts/validate_honeypots_layout.py`  _(~2.3 KB; showing ≤800 lines)_
```python
#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

LEVELS = ("high", "low")


def extract_metadata_id(yaml_text: str) -> str | None:
    metadata_match = re.search(r"^metadata:\s*\n([\s\S]*?)(?=^\S|\Z)", yaml_text, flags=re.M)
    if not metadata_match:
        return None
    md_block = metadata_match.group(1)
    id_match = re.search(r"^\s+id:\s*([\w.-]+)\s*$", md_block, flags=re.M)
    return id_match.group(1) if id_match else None


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    errors: list[str] = []

    honeypots_root = repo_root / "honeypots"
    for level in LEVELS:
        level_root = honeypots_root / level
        if not level_root.is_dir():
            errors.append(f"missing level directory: {level_root.relative_to(repo_root)}")
            continue

        for hp_dir in sorted(p for p in level_root.iterdir() if p.is_dir()):
            pack_file = hp_dir / "honeypot.yaml"
            readme_file = hp_dir / "README.md"

            if not pack_file.is_file():
                errors.append(f"missing honeypot.yaml: {hp_dir.relative_to(repo_root)}")
                continue
            if not readme_file.is_file():
                errors.append(f"missing README.md: {hp_dir.relative_to(repo_root)}")

            yaml_text = pack_file.read_text(encoding="utf-8")
            metadata_id = extract_metadata_id(yaml_text)
            if metadata_id != hp_dir.name:
                errors.append(
                    f"metadata.id mismatch in {pack_file.relative_to(repo_root)}: metadata.id={metadata_id!r}, folder={hp_dir.name!r}"
                )

            for match in re.finditer(r"([\"'])([^\"']*\.\./[^\"']*)\1", yaml_text):
                value = match.group(2)
                resolved = (hp_dir / value).resolve()
                try:
                    resolved.relative_to(hp_dir.resolve())
                except ValueError:
                    errors.append(f"path escapes honeypot directory in {pack_file.relative_to(repo_root)}: {value}")

    if errors:
        print("layout validation failed:")
        for error in errors:
            print(error)
        return 1

    print("honeypots layout validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

### `honeypot-platform/sensors/egress_proxy/Dockerfile`  _(~0.3 KB; showing ≤800 lines)_
```
FROM python:3.11-slim
WORKDIR /app
COPY proxy/egress_capture_addon.py /app/egress_capture_addon.py
COPY proxy/gen_ca.py /app/gen_ca.py
COPY entrypoint.sh /entrypoint.sh

COPY packages/hoho_core /src/hoho_core
RUN pip install --no-cache-dir /src/hoho_core mitmproxy && chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
```

### `honeypot-platform/sensors/egress_proxy/entrypoint.sh`  _(~1.6 KB; showing ≤800 lines)_
```bash
#!/usr/bin/env sh
set -eu

: "${PROXY_LISTEN_HOST:=0.0.0.0}"
: "${PROXY_LISTEN_PORT:=3128}"
: "${PROXY_STACK_ID:=${HOHO_PACK_ID:-unknown-pack}}"
: "${PROXY_TLS_MITM_ENABLED:=true}"
: "${PROXY_CA_CERT_PATH:=/runtime/ca/egress-ca.crt}"
: "${PROXY_CA_KEY_PATH:=/runtime/ca/egress-ca.key}"
: "${PROXY_MITM_BUNDLE_PATH:=/runtime/ca/mitmproxy-ca.pem}"
: "${PROXY_MITM_CERT_PATH:=/runtime/ca/mitmproxy-ca-cert.pem}"

CONF_DIR="/artifacts/${PROXY_STACK_ID}/mitmproxy-conf"
CA_DIR="/artifacts/${PROXY_STACK_ID}/ca"
mkdir -p "${CONF_DIR}" "${CA_DIR}"

is_truthy() {
  value=$(printf '%s' "$1" | tr '[:upper:]' '[:lower:]')
  [ "${value}" = "true" ] || [ "${value}" = "1" ] || [ "${value}" = "yes" ] || [ "${value}" = "on" ]
}

if is_truthy "${PROXY_TLS_MITM_ENABLED}"; then
  for required in "${PROXY_MITM_CERT_PATH}" "${PROXY_MITM_BUNDLE_PATH}" "${PROXY_CA_CERT_PATH}" "${PROXY_CA_KEY_PATH}"; do
    if [ ! -s "${required}" ]; then
      echo "ERROR: TLS MITM is enabled but required runtime CA file is missing: ${required}" >&2
      exit 1
    fi
  done

  cp "${PROXY_MITM_CERT_PATH}" "${CONF_DIR}/mitmproxy-ca-cert.pem"
  cp "${PROXY_MITM_BUNDLE_PATH}" "${CONF_DIR}/mitmproxy-ca.pem"
  cp "${PROXY_CA_CERT_PATH}" "${CA_DIR}/egress-ca.crt"
  TLS_ARGS=""
else
  TLS_ARGS="--set connection_strategy=lazy"
fi

set -- \
  --mode regular \
  --listen-host "${PROXY_LISTEN_HOST}" \
  --listen-port "${PROXY_LISTEN_PORT}" \
  --set confdir="${CONF_DIR}" \
  -s /app/egress_capture_addon.py

if [ -n "${TLS_ARGS}" ]; then
  # shellcheck disable=SC2086
  set -- "$@" ${TLS_ARGS}
fi

mitmdump "$@" &
child=$!

wait "$child"
```

### `honeypot-platform/sensors/egress_proxy/proxy/egress_capture_addon.py`  _(~3.6 KB; showing ≤800 lines)_
```python
import os
from pathlib import Path
from urllib.parse import urlparse

from hoho_core.model.event import build_base_event
from hoho_core.storage.fs import FilesystemArtifactStore
from hoho_core.utils.redact import redact_headers

HONEYPOT_ID = os.getenv("HOHO_HONEYPOT_ID", os.getenv("HOHO_PACK_ID", "unknown-pack"))
SESSION_ID = os.getenv("HOHO_SESSION_ID", "unknown-session")
AGENT_ID = os.getenv("HOHO_AGENT_ID", "unknown-agent")
ROOT = Path(os.getenv("HOHO_STORAGE_ROOT", "/artifacts"))
STORE = FilesystemArtifactStore(str(ROOT), HONEYPOT_ID)
CAPTURE_ENABLED = os.getenv("PROXY_CAPTURE_ENABLED", "true").lower() in {"1", "true", "yes", "on"}
CAPTURE_BODIES = os.getenv("PROXY_CAPTURE_BODIES", "*")
CAPTURE_MAX_BYTES = int(os.getenv("PROXY_CAPTURE_MAX_BYTES", "52428800"))
CAPTURE_STORE_OK_ONLY = os.getenv("PROXY_CAPTURE_STORE_OK_ONLY", "true").lower() in {"1", "true", "yes", "on"}
CAPTURE_MIN_BYTES = int(os.getenv("PROXY_CAPTURE_MIN_BYTES", "1"))
REDACT_HEADERS =[REDACTED]


def _guess_filename(flow_id: str, url: str, headers, digest: str) -> str:
    content_disp = headers.get("Content-Disposition", "")
    marker = "filename="
    if marker in content_disp:
        candidate = content_disp.split(marker, 1)[1].strip().strip('"\'')
        if candidate:
            return candidate

    path = urlparse(url).path
    tail = Path(path).name
    if tail:
        return tail
    return f"{digest[:32] if digest else flow_id}.bin"


def response(flow):
    req = flow.request
    resp = flow.response
    event_id = flow.id

    body = (resp.raw_content or b"") if resp else b""
    total_bytes = len(body)
    should_store = CAPTURE_ENABLED and CAPTURE_BODIES == "*"
    if CAPTURE_STORE_OK_ONLY and resp is not None:
        should_store = should_store and (200 <= resp.status_code <= 399)
    should_store = should_store and total_bytes >= CAPTURE_MIN_BYTES

    ev = build_base_event(
        honeypot_id=HONEYPOT_ID,
        component="sensor.egress_proxy",
        proto="http",
        session_id=SESSION_ID,
        agent_id=AGENT_ID,
        event_name="egress.response",
    )
    ev["event_id"] = event_id
    ev["request"] = {
        "method": req.method,
        "url": req.pretty_url,
        "headers_redacted": redact_headers(dict(req.headers.items(multi=True)), REDACT_HEADERS),
    }
    ev["response"] = {
        "status_code": resp.status_code if resp else None,
        "headers_redacted": redact_headers(dict(resp.headers.items(multi=True)), REDACT_HEADERS) if resp else {},
        "bytes": total_bytes,
    }
    ev["egress"] = {"capture_enabled": CAPTURE_ENABLED}

    if should_store:
        stored = body[:CAPTURE_MAX_BYTES]
        blob = STORE.put_blob(stored)
        truncated = len(stored) < total_bytes
        filename = _guess_filename(event_id, req.pretty_url, resp.headers if resp else {}, blob["sha256"])
        obj_path = ROOT / HONEYPOT_ID / "objects" / event_id / "egress.response" / filename
        blob_path = ROOT / HONEYPOT_ID / blob["storage_ref"]
        obj_path.parent.mkdir(parents=True, exist_ok=True)
        if not obj_path.exists():
            obj_path.symlink_to(blob_path)
        ev["artifacts"] = [
            {
                "kind": "egress.response_body",
                **blob,
                "meta": {
                    "bytes_total": total_bytes,
                    "truncated": truncated,
                    "filename_guess": filename,
                    "url": req.pretty_url,
                },
            }
        ]
        ev["decision"]["truncated"] = truncated

    STORE.append_event(HONEYPOT_ID, ev)
```

### `honeypot-platform/sensors/egress_proxy/proxy/gen_ca.py`  _(~2.2 KB; showing ≤800 lines)_
```python
#!/usr/bin/env python3
from __future__ import annotations

import sys
from datetime import UTC, datetime, timedelta
from pathlib import Path

from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: gen_ca.py <conf_dir>", file=sys.stderr)
        return 2

    conf_dir = Path(sys.argv[1])
    conf_dir.mkdir(parents=True, exist_ok=True)

    now = datetime.now(UTC)
    subject = issuer = x509.Name(
        [
            x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, "hoho egress proxy"),
            x509.NameAttribute(NameOID.COMMON_NAME, "hoho mitm CA"),
        ]
    )

    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    cert = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(now - timedelta(minutes=5))
        .not_valid_after(now + timedelta(days=3650))
        .add_extension(x509.BasicConstraints(ca=True, path_length=None), critical=True)
        .add_extension(
            x509.KeyUsage(
                digital_signature=True,
                key_encipherment=False,
                key_cert_sign=True,
                key_agreement=False,
                content_commitment=False,
                data_encipherment=False,
                encipher_only=False,
                decipher_only=False,
                crl_sign=True,
            ),
            critical=True,
        )
        .sign(private_key=key, algorithm=hashes.SHA256())
    )

    key_pem = key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    )
    cert_pem = cert.public_bytes(serialization.Encoding.PEM)

    (conf_dir / "mitmproxy-ca.pem").write_bytes(key_pem + cert_pem)
    (conf_dir / "mitmproxy-ca-cert.pem").write_bytes(cert_pem)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

### `honeypot-platform/sensors/falco/Dockerfile`  _(~1.3 KB; showing ≤800 lines)_
```
# sensors/falco/Dockerfile
FROM falcosecurity/falco:0.43.0-debian

USER root

RUN set -eux; \
    if command -v apt-get >/dev/null 2>&1; then \
        # Falco image adds download.falco.org repo but may not ship the GPG key -> apt update fails.
        # We don't need that repo for installing python.
        rm -f /etc/apt/sources.list.d/*falco* /etc/apt/sources.list.d/*falcosecurity* || true; \
        # Also remove any list that references download.falco.org, just in case
        grep -Rls "download.falco.org" /etc/apt/sources.list /etc/apt/sources.list.d 2>/dev/null | xargs -r rm -f || true; \
        apt-get update; \
        apt-get install -y --no-install-recommends python3 python3-pip ca-certificates; \
        rm -rf /var/lib/apt/lists/*; \
    else \
        echo "Expected apt-get in Falco base image, but not found"; \
        exit 1; \
    fi

WORKDIR /app

# Forwarder that converts Falco JSON alerts -> hoho events.jsonl
COPY forwarder.py /app/forwarder.py
COPY entrypoint.sh /app/entrypoint.sh
COPY rules/*.yaml /app/rules/

COPY packages/hoho_core /src/hoho_core

# If your forwarder talks to docker.sock, you likely want the docker SDK
RUN set -eux; \
    python3 -m pip install --no-cache-dir --break-system-packages /src/hoho_core docker requests; \
    chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
```

### `honeypot-platform/sensors/falco/README.md`  _(~0.6 KB; showing ≤800 lines)_
```md
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

## Default image rules
- `/app/rules/hoho_rules.yaml`
- `/app/rules/hoho_any_exec.yaml` (enabled by renderer when `any_exec: true`)

Additional `sensors[].config.rules` files are appended after defaults.
```

### `honeypot-platform/sensors/falco/entrypoint.sh`  _(~1.5 KB; showing ≤800 lines)_
```bash
#!/usr/bin/env sh
set -eu

RULES_CSV="${FALCO_RULES:-/app/rules/hoho_rules.yaml}"
PRIORITY_MIN="${FALCO_PRIORITY_MIN:-Warning}"
ENGINE="${FALCO_ENGINE:-modern_ebpf}"
APPEND_FIELDS="${HOHO_FALCO_APPEND_FIELDS:-}"

set -- falco --unbuffered \
  -o "log_level=${FALCO_LOG_LEVEL:-info}" \
  -o json_output=true \
  -o "priority=${FALCO_PRIORITY_MIN:-Warning}" \
  -o program_output.enabled=true \
  -o program_output.keep_alive=true \
  -o "program_output.program=python3 /app/forwarder.py" \
  -o "engine.kind=${ENGINE}"

# if [ "$ENGINE" = "modern_ebpf" ]; then
#   set -- "$@" -o engine.kind=modern_ebpf
# fi

if [ -n "$APPEND_FIELDS" ]; then
  APPEND_JSON="$(python3 - <<'PY'
import json
import os

csv = os.environ.get("HOHO_FALCO_APPEND_FIELDS", "")
extra_fields = []
for raw in csv.split(","):
    item = raw.strip()
    if not item:
        continue
    if "=" in item:
        key, value = item.split("=", 1)
        key = key.strip()
        value = value.strip()
        if key:
            extra_fields.append({key: value})
    else:
        extra_fields.append(item)

if extra_fields:
    print(json.dumps({"match": {"source": "syscall"}, "extra_fields": extra_fields}))
PY
)"
  if [ -n "$APPEND_JSON" ]; then
    set -- "$@" -o "append_output[]=${APPEND_JSON}"
  fi
fi

OLDIFS="$IFS"
IFS=','
for rule_file in $RULES_CSV; do
  trimmed="$(printf '%s' "$rule_file" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')"
  [ -n "$trimmed" ] || continue
  set -- "$@" -r "$trimmed"
done
IFS="$OLDIFS"

printf 'Starting Falco command: %s\n' "$*"
exec "$@"
```

### `honeypot-platform/sensors/falco/forwarder.py`  _(~7.8 KB; showing ≤800 lines)_
```python
import json
import os
import sys
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path
from urllib import request

HONEYPOT_ID = os.getenv("HOHO_HONEYPOT_ID", os.getenv("HOHO_PACK_ID", "unknown-pack"))
SESSION_ID = os.getenv("HOHO_SESSION_ID", "unknown-session")
AGENT_ID = os.getenv("HOHO_AGENT_ID", "unknown-agent")
ROOT = Path(os.getenv("HOHO_STORAGE_ROOT", "/artifacts"))
EVENTS_PATH = ROOT / HONEYPOT_ID / "index" / "events.jsonl"
ONLY_PROJECT = os.getenv("HOHO_FALCO_ONLY_PROJECT", "true").strip().lower() in {"1", "true", "yes", "on"}
PROJECT = os.getenv("HOHO_FALCO_PROJECT", "")
ONLY_SERVICES = {s for s in os.getenv("HOHO_FALCO_ONLY_SERVICES", "").split(",") if s}
ENFORCE_ENABLED = os.getenv("HOHO_FALCO_ENFORCE_ENABLED", "false").strip().lower() in {"1", "true", "yes", "on"}
ENFORCE_PRIORITIES = {x for x in os.getenv("HOHO_FALCO_ENFORCE_MATCH_PRIORITIES", "Critical,Error").split(",") if x}
ENFORCE_RULES = {x for x in os.getenv("HOHO_FALCO_ENFORCE_MATCH_RULES", "").split(",") if x}
ENFORCE_ACTION = os.getenv("HOHO_FALCO_ENFORCE_ACTION", "stop_container")
ENFORCE_COOLDOWN_SECONDS = int(os.getenv("HOHO_FALCO_ENFORCE_COOLDOWN_SECONDS", "60"))
DOCKER_SOCK = "/host/var/run/docker.sock"
_last_enforce = {}


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def append_event(event: dict) -> None:
    EVENTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    with EVENTS_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event) + "\n")


def docker_api(path: str, method: str = "GET"):
    opener = request.build_opener(request.ProxyHandler({}))
    opener.add_handler(request.HTTPHandler())
    url = f"http://localhost{path}"
    req = request.Request(url, method=method)
    req.add_header("Host", "docker")
    return opener.open(req, timeout=3)


def docker_request(path: str, method: str = "GET"):
    import http.client

    conn = http.client.HTTPConnection("localhost")
    conn.sock = __import__("socket").socket(__import__("socket").AF_UNIX, __import__("socket").SOCK_STREAM)
    conn.sock.connect(DOCKER_SOCK)
    conn.request(method, path)
    resp = conn.getresponse()
    data = resp.read()
    conn.close()
    return resp.status, data


def inspect_container(container_id: str) -> dict:
    status, body = docker_request(f"/containers/{container_id}/json")
    if status >= 400:
        return {}
    try:
        return json.loads(body.decode("utf-8"))
    except Exception:
        return {}


def stop_container(container_id: str) -> bool:
    status, _ = docker_request(f"/containers/{container_id}/stop?t=5", method="POST")
    return status < 400


def list_project_containers(project: str) -> list[str]:
    status, body = docker_request("/containers/json")
    if status >= 400:
        return []
    items = json.loads(body.decode("utf-8"))
    out = []
    for item in items:
        labels = item.get("Labels", {})
        if labels.get("com.docker.compose.project") == project:
            out.append(item.get("Id", ""))
    return [x for x in out if x]


def extract_container_id(alert: dict) -> str:
    fields = alert.get("output_fields", {}) or {}
    container_id = fields.get("container.id")
    if not container_id or container_id == "<NA>":
        return ""
    return str(container_id)


def should_keep(alert: dict):
    container_id = extract_container_id(alert)
    if not container_id:
        return False, "", ""
    inspect = inspect_container(container_id)
    labels = inspect.get("Config", {}).get("Labels", {}) if inspect else {}
    project = labels.get("com.docker.compose.project", "")
    service = labels.get("com.docker.compose.service", "")
    if ONLY_PROJECT and PROJECT and project != PROJECT:
        return False, project, service
    if ONLY_SERVICES and service not in ONLY_SERVICES:
        return False, project, service
    return True, project, service


def should_enforce(alert: dict) -> bool:
    if not ENFORCE_ENABLED:
        return False
    rule = str(alert.get("rule", ""))
    priority = str(alert.get("priority", ""))
    if ENFORCE_RULES and rule in ENFORCE_RULES:
        return True
    if priority in ENFORCE_PRIORITIES:
        return True
    return False


def maybe_enforce(alert: dict, project: str, service: str) -> dict | None:
    if not should_enforce(alert):
        return None
    container_id = extract_container_id(alert)
    if not container_id:
        return None

    key = (ENFORCE_ACTION, container_id, project)
    now = time.time()
    last = _last_enforce.get(key, 0)
    if now - last < ENFORCE_COOLDOWN_SECONDS:
        return None
    _last_enforce[key] = now

    result = {"ok": False, "targets": []}
    if ENFORCE_ACTION in {"stop_container", "stop_service"}:
        result["targets"] = [container_id]
        result["ok"] = stop_container(container_id)
    elif ENFORCE_ACTION == "stop_stack" and project:
        targets = list_project_containers(project)
        result["targets"] = targets
        result["ok"] = all(stop_container(cid) for cid in targets) if targets else False
    return result


def make_base_event(alert: dict) -> dict:
    rule = str(alert.get("rule", "unknown"))
    priority = str(alert.get("priority", "Notice"))
    tags = ["falco", f"priority:{priority}", f"rule:{rule}"] + [str(t) for t in (alert.get("tags") or [])]
    return {
        "schema_version": 2,
        "event_id": f"falco-{uuid.uuid4().hex}",
        "ts": now_iso(),
        "honeypot_id": HONEYPOT_ID,
        "session_id": SESSION_ID,
        "agent_id": AGENT_ID,
        "event_name": "falco.alert",
        "component": "sensor.falco",
        "proto": "runtime",
        "classification": {"verdict": "alert", "tags": tags, "indicators": [rule]},
        "decision": {"truncated": False, "oversized": False, "rate_limited": False, "dropped": False},
        "artifacts": [],
        "falco": {
            "time": alert.get("time"),
            "rule": rule,
            "priority": priority,
            "source": alert.get("source"),
            "output": alert.get("output"),
            "output_fields": alert.get("output_fields", {}),
            "tags": alert.get("tags", []),
        },
    }


def main() -> int:
    for raw in sys.stdin:
        line = raw.strip()
        if not line:
            continue
        try:
            alert = json.loads(line)
        except Exception:
            print(f"[falco-forwarder] failed to parse alert line: {line[:300]}", file=sys.stderr)
            continue

        keep, project, service = should_keep(alert)
        if not keep:
            continue

        ev = make_base_event(alert)
        # Stamp static context here (no Falco append_output needed)
        ev["falco"]["output_fields"] = ev["falco"].get("output_fields", {}) or {}
        ev["falco"]["output_fields"].update(
            {
                "honeypot_id": HONEYPOT_ID,
                "sensor": "falco",
            }
        )
        ev["classification"]["tags"].extend([f"compose_project:{project}", f"compose_service:{service}"])
        append_event(ev)

        enforce_result = maybe_enforce(alert, project=project, service=service)
        if enforce_result is not None:
            append_event(
                {
                    **ev,
                    "event_id": f"falco-enforce-{uuid.uuid4().hex}",
                    "event_name": "falco.enforcement",
                    "classification": {
                        "verdict": "enforcement",
                        "tags": ["falco", "enforcement", f"action:{ENFORCE_ACTION}"],
                        "indicators": ev["classification"]["indicators"],
                    },
                    "falco_enforcement": {
                        "action": ENFORCE_ACTION,
                        "ok": enforce_result.get("ok", False),
                        "targets": enforce_result.get("targets", []),
                    },
                }
            )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

### `honeypot-platform/sensors/falco/rules/hoho_any_exec.yaml`  _(~0.5 KB; showing ≤800 lines)_
```yaml
- macro: hoho_container
  condition: container.id != "host" and container.id != "" and container.id != "<NA>"

- rule: Hoho Any Exec in Container
  desc: Catch all process executions in containers (noisy; optional)
  condition: hoho_container and evt.type=execve and proc.name exists
  output: >
    Hoho Any Exec | user=%user.name proc=%proc.name cmd=%proc.cmdline
    container_id=%container.id image=%container.image.repository
  priority: NOTICE
  tags: [hoho, process, exec]
```

### `honeypot-platform/sensors/falco/rules/hoho_rules.yaml`  _(~1.9 KB; showing ≤800 lines)_
```yaml
- macro: hoho_container
  condition: container.id != "host" and container.id != "" and container.id != "<NA>"

- list: hoho_shell_bins
  items: [sh, bash, ash, dash, zsh, ksh]

- list: hoho_download_bins
  items: [curl, wget, aria2c, fetch]

- list: hoho_network_bins
  items: [nc, ncat, socat, nmap]

- list: hoho_interpreter_bins
  items: [python, python3, perl, php, ruby]

- rule: Hoho Shell Spawned in Container
  desc: Detect shell execution in container
  condition: hoho_container and evt.type=execve and proc.name in (hoho_shell_bins)
  output: >
    Hoho Shell Spawned | user=%user.name proc=%proc.name cmd=%proc.cmdline
    container_id=%container.id image=%container.image.repository
  priority: ERROR
  tags: [hoho, process, shell]

- rule: Hoho Downloader Executed in Container
  desc: Detect downloader process execution in container
  condition: hoho_container and evt.type=execve and proc.name in (hoho_download_bins)
  output: >
    Hoho Downloader Exec | user=%user.name proc=%proc.name cmd=%proc.cmdline
    container_id=%container.id image=%container.image.repository
  priority: WARNING
  tags: [hoho, process, downloader]

- rule: Hoho Network Tool Executed in Container
  desc: Detect network utility execution in container
  condition: hoho_container and evt.type=execve and proc.name in (hoho_network_bins)
  output: >
    Hoho Network Tool Exec | user=%user.name proc=%proc.name cmd=%proc.cmdline
    container_id=%container.id image=%container.image.repository
  priority: WARNING
  tags: [hoho, process, network_tool]

- rule: Hoho Interpreter Executed in Container
  desc: Detect scripting interpreter execution in container
  condition: hoho_container and evt.type=execve and proc.name in (hoho_interpreter_bins)
  output: >
    Hoho Interpreter Exec | user=%user.name proc=%proc.name cmd=%proc.cmdline
    container_id=%container.id image=%container.image.repository
  priority: WARNING
  tags: [hoho, process, interpreter]
```

### `honeypot-platform/sensors/fsmon/Dockerfile`  _(~0.3 KB; showing ≤800 lines)_
```
FROM python:3.11-slim
WORKDIR /app
COPY fsmon/fsmon.py /app/fsmon.py
COPY fsmon/rules.schema.json /app/rules.schema.json
COPY entrypoint.sh /entrypoint.sh

COPY packages/hoho_core /src/hoho_core


RUN pip install --no-cache-dir /src/hoho_core watchdog && chmod +x /entrypoint.sh
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

### `honeypot-platform/sensors/fsmon/fsmon/fsmon.py`  _(~2.3 KB; showing ≤800 lines)_
```python
import fnmatch
import os
from pathlib import Path

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from hoho_core.model.event import build_base_event
from hoho_core.storage.fs import FilesystemArtifactStore

HONEYPOT_ID = os.getenv("HOHO_HONEYPOT_ID", os.getenv("HOHO_PACK_ID", "unknown-pack"))
SESSION_ID = os.getenv("HOHO_SESSION_ID", "unknown-session")
AGENT_ID = os.getenv("HOHO_AGENT_ID", "unknown-agent")
ROOT = Path(os.getenv("HOHO_STORAGE_ROOT", "/artifacts"))
WATCH_DIRS = os.getenv("FSMON_WATCH", "/watched").split(",")
MAX_BYTES = int(os.getenv("FSMON_MAX_BYTES", "262144"))
ALLOW = [x for x in os.getenv("FSMON_ALLOW", "*").split(",") if x]
DENY = [x for x in os.getenv("FSMON_DENY", "").split(",") if x]
STORE = FilesystemArtifactStore(str(ROOT), HONEYPOT_ID)


def allow_path(path: str) -> bool:
    if any(fnmatch.fnmatch(path, pat) for pat in DENY):
        return False
    return any(fnmatch.fnmatch(path, pat) for pat in ALLOW)


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

        blob = STORE.put_blob(data)
        ev = build_base_event(
            honeypot_id=HONEYPOT_ID,
            component="sensor.fsmon",
            proto="fs",
            session_id=SESSION_ID,
            agent_id=AGENT_ID,
            event_name="fs.write",
        )
        ev["classification"] = {"verdict": "postex", "tags": ["fs_change"], "indicators": [str(path)]}
        ev["decision"]["truncated"] = len(data) >= MAX_BYTES
        ev["artifacts"] = [
            {
                "kind": "fs_write",
                **blob,
                "meta": {"path": str(path), "preview": data[:128].decode("utf-8", errors="ignore")},
            }
        ]
        STORE.append_event(HONEYPOT_ID, ev)


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

### `honeypot-platform/sensors/http_proxy/Dockerfile`  _(~0.3 KB; showing ≤800 lines)_
```
FROM python:3.11-slim
WORKDIR /app
COPY proxy/capture_addon.py /app/capture_addon.py
COPY entrypoint.sh /entrypoint.sh
COPY packages/hoho_core /src/hoho_core

RUN pip install --no-cache-dir /src/hoho_core mitmproxy PyYAML jsonschema && chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
```

### `honeypot-platform/sensors/http_proxy/README.md`  _(~0.9 KB; showing ≤800 lines)_
```md
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
```

### `honeypot-platform/sensors/http_proxy/entrypoint.sh`  _(~0.8 KB; showing ≤800 lines)_
```bash
#!/usr/bin/env sh
set -eu

: "${UPSTREAM:=http://upstream:80}"
: "${PROXY_LISTEN_HOST:=0.0.0.0}"
: "${PROXY_LISTEN_PORT:=8080}"
: "${PROXY_KEEP_HOST_HEADER:=true}"
: "${PROXY_EXTRA_ARGS:=}"

is_truthy() {
    value=$(printf '%s' "$1" | tr '[:upper:]' '[:lower:]')
    case "$value" in
        1|true|yes|on)
            return 0
            ;;
        *)
            return 1
            ;;
    esac
}

set -- \
    --mode "reverse:${UPSTREAM}" \
    --listen-host "${PROXY_LISTEN_HOST}" \
    --listen-port "${PROXY_LISTEN_PORT}" \
    -s /app/capture_addon.py

if is_truthy "${PROXY_KEEP_HOST_HEADER}"; then
    set -- "$@" --set keep_host_header=true
fi

if [ -n "${PROXY_EXTRA_ARGS}" ]; then
    # shellcheck disable=SC2086
    set -- "$@" ${PROXY_EXTRA_ARGS}
fi

exec mitmdump "$@"
```

### `honeypot-platform/sensors/http_proxy/proxy/capture_addon.py`  _(~2.7 KB; showing ≤800 lines)_
```python
import os
import sys
from pathlib import Path

from hoho_core.model.event import build_base_event
from hoho_core.storage.fs import FilesystemArtifactStore
from hoho_core.utils.redact import redact_headers

HONEYPOT_ID = os.getenv("HOHO_HONEYPOT_ID", os.getenv("HOHO_PACK_ID", "unknown-pack"))
SESSION_ID = os.getenv("HOHO_SESSION_ID", "unknown-session")
AGENT_ID = os.getenv("HOHO_AGENT_ID", "unknown-agent")
ROOT = Path(os.getenv("HOHO_STORAGE_ROOT", "/artifacts"))
STORE = FilesystemArtifactStore(str(ROOT), HONEYPOT_ID)


def _log_error(message: str):
    print(f"capture_addon error: {message}", file=sys.stderr)


def _peername(flow):
    client_conn = getattr(flow, "client_conn", None)
    if not client_conn:
        return None
    peername = getattr(client_conn, "peername", None)
    if isinstance(peername, tuple) and len(peername) >= 2:
        return peername
    return None


def _forwarded_for_values(req) -> list[str]:
    header_val = req.headers.get("X-Forwarded-For", "")
    if not header_val:
        return []
    return [v.strip() for v in header_val.split(",") if v.strip()]


def response(flow):
    try:
        req = flow.request
        resp = flow.response
        body = req.raw_content or b""

        peername = _peername(flow)
        src_ip = peername[0] if peername else None
        src_port = peername[1] if peername else None

        ev = build_base_event(
            honeypot_id=HONEYPOT_ID,
            component="sensor.http_proxy",
            proto="http",
            session_id=SESSION_ID,
            agent_id=AGENT_ID,
            event_name="http.request",
        )
        ev["event_id"] = flow.id
        ev["src"] = {
            "ip": src_ip,
            "port": src_port,
            "forwarded_for": _forwarded_for_values(req),
            "user_agent": req.headers.get("User-Agent"),
        }
        ev["http"] = {"host": req.headers.get("Host")}
        ev["request"] = {
            "method": req.method,
            "path": req.path,
            "query": dict(req.query),
            "headers_redacted": redact_headers(dict(req.headers.items(multi=True))),
            "content_type": req.headers.get("Content-Type"),
            "content_length": len(body),
        }
        ev["response"] = {
            "status_code": resp.status_code if resp else None,
            "bytes_sent": len(resp.raw_content or b"") if resp else 0,
            "profile": None,
        }
        if body:
            blob = STORE.put_blob(body, mime=req.headers.get("Content-Type", "application/octet-stream"))
            ev["artifacts"] = [{"kind": "request_body", **blob, "meta": {}}]
        STORE.append_event(HONEYPOT_ID, ev)
    except Exception as exc:  # noqa: BLE001
        _log_error(str(exc))
```

### `honeypot-platform/sensors/pcap/Dockerfile`  _(~0.3 KB; showing ≤800 lines)_
```
FROM python:3.11-slim
RUN apt update && apt install -y --no-install-recommends tcpdump
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
COPY packages/hoho_core /src/hoho_core
RUN pip install --no-cache-dir /src/hoho_core

ENTRYPOINT ["/entrypoint.sh"]
```

### `honeypot-platform/sensors/pcap/README.md`  _(~0.1 KB; showing ≤800 lines)_
```md
# sensor-pcap

Tcpdump wrapper with rotated capture files stored as blob artifacts plus pcap segment events.
```

### `honeypot-platform/sensors/pcap/entrypoint.sh`  _(~1.4 KB; showing ≤800 lines)_
```bash
#!/usr/bin/env bash
set -euo pipefail
HONEYPOT_ID="${HOHO_HONEYPOT_ID:-${HOHO_PACK_ID:-unknown-pack}}"
SESSION_ID="${HOHO_SESSION_ID:-unknown-session}"
AGENT_ID="${HOHO_AGENT_ID:-unknown-agent}"
ROOT="${HOHO_STORAGE_ROOT:-/artifacts}"
ROTATE_SECONDS="${PCAP_ROTATE_SECONDS:-60}"
ROTATE_COUNT="${PCAP_ROTATE_COUNT:-10}"
OUT_DIR="${ROOT}/${HONEYPOT_ID}/pcap"
mkdir -p "$OUT_DIR" "${ROOT}/${HONEYPOT_ID}/index"

tcpdump -i any -w "${OUT_DIR}/segment-%Y%m%d-%H%M%S.pcap" -G "$ROTATE_SECONDS" -W "$ROTATE_COUNT" || true
for f in "$OUT_DIR"/*.pcap; do
  [ -f "$f" ] || continue
  sha=$(sha256sum "$f" | awk '{print $1}')
  bdir="${ROOT}/${HONEYPOT_ID}/blobs/${sha:0:2}"
  mkdir -p "$bdir"
  cp "$f" "$bdir/$sha"
  printf '{"schema_version":2,"event_id":"pcap-%s","ts":"%s","honeypot_id":"%s","session_id":"%s","agent_id":"%s","event_name":"pcap.segment","component":"sensor.pcap","proto":"tcp","classification":{"verdict":"probe","tags":["pcap_segment"],"indicators":[]},"decision":{"truncated":false,"oversized":false,"rate_limited":false,"dropped":false},"artifacts":[{"kind":"pcap_segment","sha256":"%s","size":%s,"mime":"application/vnd.tcpdump.pcap","storage_ref":"blobs/%s/%s","meta":{"source":"%s"}}]}
' "$(date +%s)" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$HONEYPOT_ID" "$SESSION_ID" "$AGENT_ID" "$sha" "$(wc -c < "$f")" "${sha:0:2}" "$sha" "$f" >> "${ROOT}/${HONEYPOT_ID}/index/events.jsonl"
done
```
