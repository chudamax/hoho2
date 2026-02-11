# Repository Brief: hoho2

_Generated 2026-02-11 14:08 UTC_

## Quick Facts
- **Branch:** main
- **Commit:** c250dd7 (2026-02-11 14:35:33 +0100)
- **Total commits:** 48
- **Files scanned:** 86
- **Text files embedded (after filters):** 86

## Language & LOC Overview (approx.)
- **python** — files: 36 (41.9%), LOC: 1935
- **md** — files: 23 (26.7%), LOC: 6079
- **bash** — files: 10 (11.6%), LOC: 233
- **yaml** — files: 7 (8.1%), LOC: 591
- **other** — files: 5 (5.8%), LOC: 243
- **json** — files: 2 (2.3%), LOC: 406
- **toml** — files: 2 (2.3%), LOC: 30
- **html** — files: 1 (1.2%), LOC: 12

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
  - packs
    - high
      - cve-2017-12629_solr_rce.yaml
      - cve-2020-25213_wp_file_upload.yaml
      - cve-2021-41773_42013_apache_rce.yaml
      - example_wp_stack.yaml
    - low
      - cve-2021-41773_apache-2-4-49-2-4-50-traversal-rce.yaml
      - example_upload_sink.yaml
      - example_web.yaml
  - sensors
    - egress_proxy
      - Dockerfile
      - entrypoint.sh
    - fsmon
    - http_proxy
    - pcap
  - honeypots
      - cve-2017-12629_solr_rce
        - README.md
        - reset.sh
      - cve-2021-41773_42013
      - cve-2021-41773_apache-2-4-49-2-4-50-traversal-rce
      - hoho_core
        - __init__.py
        - version.py
      - hoho_runtime
        - cli.py
        - config.py
      - proxy
        - egress_capture_addon.py
        - gen_ca.py
      - fsmon
        - fsmon.py
        - rules.schema.json
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
          - ca_pregen.py
          - compose_down_all.py
          - compose_render.py
          - compose_run.py
        - server
          - http.py
          - tcp.py
        - cgi-bin
          - health.sh
        - htdocs
          - index.html
```

## Recent Commits
- c250dd7 | 2026-02-11 | Merge pull request #15 from chudamax/codex/add-high-level-interaction-honeypot-for-solr-cve-2017-12629
- e9d0423 | 2026-02-11 | Add high-interaction Solr CVE-2017-12629 honeypot pack
- 65edc5b | 2026-02-11 | updates
- 594d3cd | 2026-02-11 | updates
- 824665b | 2026-02-10 | updates
- 401ce97 | 2026-02-10 | Merge pull request #14 from chudamax/codex/simplify-egress-proxy-tls-mitm-certificates
- 11bbc2a | 2026-02-10 | Simplify egress TLS MITM cert handling to automatic runtime CA
- 3ceb032 | 2026-02-10 | up
- 8407a4c | 2026-02-10 | Merge branch 'main' of github.com:chudamax/hoho2
- 3130cb2 | 2026-02-10 | updates

## Files (embedded, trimmed)
> Secret-looking lines are redacted by default. Large files are truncated to stay within budgets.

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

### `AGENTS.md`  _(~3.1 KB; showing ≤800 lines)_
```md
# AGENTS.md (repo root)

## Honeypot layout (Simple Layout v1)
Authoritative spec: `honeypot-platform/docs/DIRECTORY_LAYOUT.md`.

MUST:
- Always use `honeypot_id == metadata.id`.
- Create packs only at `honeypot-platform/packs/{low,high}/<honeypot_id>.yaml`.
- Create docs only at `honeypot-platform/honeypots/{low,high}/<honeypot_id>/README.md`.
- Artifacts always go to `honeypot-platform/run/artifacts/<honeypot_id>/...`.
- Compose output always goes to `honeypot-platform/deploy/compose/<honeypot_id>/docker-compose.yml`.

MUST NOT:
- Do not create `.md` next to pack YAML files (`packs/**/*.md` is forbidden).
- Do not create `honeypot-platform/run/artifacts/<runs-subtree>/**` (no run-id subtrees).
- Do not create non-canonical honeypot folders (example forbidden: `honeypots/high/2021-41773_42013/`).

## Docs that must be consulted (before implementing or changing packs)
- Pack + schema rules: `honeypot-platform/docs/PACK_SPEC.md`
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

## Working reference packs (golden examples)
High-interaction (full stack + sensors):
- `honeypot-platform/packs/high/cve-2021-41773_42013_apache_rce.yaml`

Low-interaction (DSL emulation):
- `honeypot-platform/packs/low/cve-2021-41773_apache-2-4-49-2-4-50-traversal-rce.yaml`

## Operational commands (stop/cleanup)
- Stop everything: `hoho down-all` (optionally `--volumes`)
- Per-honeypot manual stop:
  `docker compose -p "hoho-<honeypot_id>" -f deploy/compose/<honeypot_id>/docker-compose.yml down -v`
```

### `REPO_BRIEF.md`  _(~161.5 KB; showing ≤800 lines)_
```md
# Repository Brief: hoho2

_Generated 2026-02-10 18:50 UTC_

## Quick Facts
- **Branch:** main
- **Commit:** 3ceb032 (2026-02-10 18:50:30 +0000)
- **Total commits:** 41
- **Files scanned:** 83
- **Text files embedded (after filters):** 83

## Language & LOC Overview (approx.)
- **python** — files: 36 (43.4%), LOC: 1912
- **md** — files: 22 (26.5%), LOC: 5809
- **bash** — files: 9 (10.8%), LOC: 236
- **yaml** — files: 6 (7.2%), LOC: 490
- **other** — files: 5 (6.0%), LOC: 243
- **json** — files: 2 (2.4%), LOC: 437
- **toml** — files: 2 (2.4%), LOC: 30
- **html** — files: 1 (1.2%), LOC: 12

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
  - packs
    - high
      - cve-2020-25213_wp_file_upload.yaml
      - cve-2021-41773_42013.yaml
      - example_wp_stack.yaml
    - low
      - cve-2021-41773_apache-2-4-49-2-4-50-traversal-rce.yaml
      - example_upload_sink.yaml
      - example_web.yaml
  - sensors
    - egress_proxy
      - Dockerfile
      - entrypoint.sh
    - fsmon
    - http_proxy
    - pcap
  - honeypots
      - cve-2021-41773_42013
        - README.md
        - reset.sh
      - cve-2021-41773_apache-2-4-49-2-4-50-traversal-rce
      - hoho_core
        - __init__.py
        - version.py
      - hoho_runtime
        - cli.py
        - config.py
      - proxy
        - egress_capture_addon.py
        - gen_ca.py
      - fsmon
        - fsmon.py
        - rules.schema.json
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
          - ca_pregen.py
          - compose_down_all.py
          - compose_render.py
          - compose_run.py
        - server
          - http.py
          - tcp.py
        - cgi-bin
          - health.sh
        - htdocs
          - index.html
```

## Recent Commits
- 3ceb032 | 2026-02-10 | up
- 8407a4c | 2026-02-10 | Merge branch 'main' of github.com:chudamax/hoho2
- 3130cb2 | 2026-02-10 | updates
- 6f74138 | 2026-02-10 | Merge pull request #13 from chudamax/codex/add-host-side-ca-generation-for-egress-proxy
- e6def8f | 2026-02-10 | Pre-generate runtime egress CA before compose up
- 81214e2 | 2026-02-10 | Merge pull request #12 from chudamax/codex/add-hoho-down-all-command
- 71386d5 | 2026-02-10 | Add hoho down-all cleanup command
- 0fe9066 | 2026-02-10 | Merge pull request #11 from chudamax/codex/fix-egress_proxy-ca-generation-delay
- 2045ad6 | 2026-02-10 | Fix egress proxy CA auto-generation and runtime wait logic
- 3141788 | 2026-02-10 | Merge pull request #10 from chudamax/codex/fix-events.jsonl-permission-error

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

### `AGENTS.md`  _(~1.4 KB; showing ≤800 lines)_
```md
# AGENTS.md (repo root)

## Honeypot layout (Simple Layout v1)
- Authoritative spec: `honeypot-platform/docs/DIRECTORY_LAYOUT.md`.
- Always use `honeypot_id == metadata.id`.
- Create packs only at `honeypot-platform/packs/{low,high}/<honeypot_id>.yaml`.
- Create docs only at `honeypot-platform/honeypots/{low,high}/<honeypot_id>/README.md`.
- Never create `.md` next to pack YAML files.
- Artifacts always go to `honeypot-platform/run/artifacts/<honeypot_id>/...`.
- Compose always goes to `honeypot-platform/deploy/compose/<honeypot_id>/docker-compose.yml`.
- Never create `honeypot-platform/run/artifacts/<runs-subtree>/**`.
- Never create non-canonical honeypot folders such as `honeypot-platform/honeypots/high/<cve-only>/`.

# Honeypots: low-interaction
- When asked to create a new low-interaction honeypot from a CVE, ALWAYS read:
  `honeypot-platform/docs/runbooks/low-interaction-honeypot-from-cve.md`
- Follow the runbook exactly: research -> derive request transcripts -> implement YAML pack -> validate/run -> document.

## Honeypots: high-interaction
- When asked to create a new high-interaction honeypot from a CVE, ALWAYS read:
  `honeypot-platform/docs/runbooks/high-interaction-honeypot-from-cve.md`
- Prioritize isolation + capture: pcap, proxy download capture, filesystem monitoring, process/audit logs.
- Provide a one-command reset script at `honeypot-platform/honeypots/high/<honeypot_id>/reset.sh`.
```

### `REPO_BRIEF.md`  _(~155.3 KB; showing ≤800 lines)_
```md
# Repository Brief: hoho2

_Generated 2026-02-10 17:52 UTC_

## Quick Facts
- **Branch:** main
- **Commit:** 81214e2 (2026-02-10 18:49:55 +0100)
- **Total commits:** 36
- **Files scanned:** 82
- **Text files embedded (after filters):** 82

## Language & LOC Overview (approx.)
- **python** — files: 35 (42.7%), LOC: 1745
- **md** — files: 22 (26.8%), LOC: 5383
- **bash** — files: 9 (11.0%), LOC: 242
- **yaml** — files: 6 (7.3%), LOC: 490
- **other** — files: 5 (6.1%), LOC: 239
- **json** — files: 2 (2.4%), LOC: 437
- **toml** — files: 2 (2.4%), LOC: 30
- **html** — files: 1 (1.2%), LOC: 12

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
  - packs
    - high
      - cve-2020-25213_wp_file_upload.yaml
      - cve-2021-41773_42013.yaml
      - example_wp_stack.yaml
    - low
      - cve-2021-41773_apache-2-4-49-2-4-50-traversal-rce.yaml
      - example_upload_sink.yaml
      - example_web.yaml
  - sensors
    - egress_proxy
      - Dockerfile
      - entrypoint.sh
    - fsmon
    - http_proxy
    - pcap
  - honeypots
      - cve-2021-41773_42013
        - README.md
        - reset.sh
      - cve-2021-41773_apache-2-4-49-2-4-50-traversal-rce
      - hoho_core
        - __init__.py
        - version.py
      - hoho_runtime
        - cli.py
        - config.py
      - proxy
        - egress_capture_addon.py
        - gen_ca.py
      - fsmon
        - fsmon.py
        - rules.schema.json
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
          - compose_down_all.py
          - compose_render.py
          - compose_run.py
        - server
          - http.py
          - tcp.py
        - cgi-bin
          - health.sh
        - htdocs
          - index.html
```

## Recent Commits
- 81214e2 | 2026-02-10 | Merge pull request #12 from chudamax/codex/add-hoho-down-all-command
- 71386d5 | 2026-02-10 | Add hoho down-all cleanup command
- 0fe9066 | 2026-02-10 | Merge pull request #11 from chudamax/codex/fix-egress_proxy-ca-generation-delay
- 2045ad6 | 2026-02-10 | Fix egress proxy CA auto-generation and runtime wait logic
- 3141788 | 2026-02-10 | Merge pull request #10 from chudamax/codex/fix-events.jsonl-permission-error
- ae26527 | 2026-02-10 | Fix events log permission handling in compose runtime
- 121d81e | 2026-02-10 | up
- f497d6e | 2026-02-10 | Merge pull request #9 from chudamax/codex/add-egress_proxy-sensor-type
- 87640a3 | 2026-02-10 | Add high-interaction egress proxy sensor with MITM capture pipeline
- a724fc1 | 2026-02-10 | Merge pull request #8 from chudamax/codex/fix-hoho-cli-output-paths

## Files (embedded, trimmed)
[REDACTED]

### `.gitignore`  _(~4.7 KB; showing ≤800 lines)_
```
artifacts/
run/
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
```

### `AGENTS.md`  _(~1.4 KB; showing ≤800 lines)_
```md
# AGENTS.md (repo root)

## Honeypot layout (Simple Layout v1)
- Authoritative spec: `honeypot-platform/docs/DIRECTORY_LAYOUT.md`.
- Always use `honeypot_id == metadata.id`.
- Create packs only at `honeypot-platform/packs/{low,high}/<honeypot_id>.yaml`.
- Create docs only at `honeypot-platform/honeypots/{low,high}/<honeypot_id>/README.md`.
- Never create `.md` next to pack YAML files.
- Artifacts always go to `honeypot-platform/run/artifacts/<honeypot_id>/...`.
- Compose always goes to `honeypot-platform/deploy/compose/<honeypot_id>/docker-compose.yml`.
- Never create `honeypot-platform/run/artifacts/<runs-subtree>/**`.
- Never create non-canonical honeypot folders such as `honeypot-platform/honeypots/high/<cve-only>/`.

# Honeypots: low-interaction
- When asked to create a new low-interaction honeypot from a CVE, ALWAYS read:
  `honeypot-platform/docs/runbooks/low-interaction-honeypot-from-cve.md`
- Follow the runbook exactly: research -> derive request transcripts -> implement YAML pack -> validate/run -> document.

## Honeypots: high-interaction
- When asked to create a new high-interaction honeypot from a CVE, ALWAYS read:
  `honeypot-platform/docs/runbooks/high-interaction-honeypot-from-cve.md`
- Prioritize isolation + capture: pcap, proxy download capture, filesystem monitoring, process/audit logs.
- Provide a one-command reset script at `honeypot-platform/honeypots/high/<honeypot_id>/reset.sh`.
```

### `REPO_BRIEF.md`  _(~141.7 KB; showing ≤800 lines)_
```md
# Repository Brief: hoho2

_Generated 2026-02-10 16:56 UTC_

## Quick Facts
- **Branch:** main
- **Commit:** 121d81e (2026-02-10 16:56:20 +0000)
- **Total commits:** 30
- **Files scanned:** 80
- **Text files embedded (after filters):** 80

## Language & LOC Overview (approx.)
- **python** — files: 33 (41.2%), LOC: 1393
- **md** — files: 22 (27.5%), LOC: 5369
- **bash** — files: 9 (11.2%), LOC: 205
- **yaml** — files: 6 (7.5%), LOC: 490
- **other** — files: 5 (6.2%), LOC: 238
- **json** — files: 2 (2.5%), LOC: 437
- **toml** — files: 2 (2.5%), LOC: 30
- **html** — files: 1 (1.2%), LOC: 12

## Directory Tree (depth ≤ 10)

```text
- .gitignore
- AGENTS.md
- REPO_BRIEF.md
- honeypot-platform
  - docs
```
<!-- trimmed: file exceeded per-file limits -->

### `honeypot-platform/deploy/compose/README.md`  _(~1.2 KB; showing ≤800 lines)_
```md
# Compose output directory

By default, `hoho` writes compose bundles under `<project_root>/deploy/compose/<honeypot_id>/`.

When `-o/--output` is not provided, the CLI discovers `project_root` by walking up from the pack path and selecting:
1. the first ancestor containing `deploy/compose` (or `deploy/compose/README.md`),
2. otherwise the first ancestor containing `packs/`,
3. otherwise the pack file's parent directory.

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

### `honeypot-platform/docs/DEPLOYMENT.md`  _(~0.6 KB; showing ≤800 lines)_
```md
# Deployment

## High-interaction quickstart
1. Validate pack:
   - `hoho validate packs/high/<honeypot_id>.yaml`
2. Render compose (fixed output path):
   - `hoho render-compose packs/high/<honeypot_id>.yaml`
3. Start stack:
   - `docker compose -p "hoho-<honeypot_id>" -f deploy/compose/<honeypot_id>/docker-compose.yml up -d`
4. Inspect artifacts:
   - `run/artifacts/<honeypot_id>/index/events.jsonl`
   - `run/artifacts/<honeypot_id>/blobs/`

## Notes
- `deploy/compose/**` is generated and should not be committed.
- `run/artifacts/<honeypot_id>/` is overwritten for each new run of the same honeypot.
- Run only one active stack per `honeypot_id`.
```

### `honeypot-platform/docs/DIRECTORY_LAYOUT.md`  _(~2.6 KB; showing ≤800 lines)_
```md
# DIRECTORY_LAYOUT.md

## Simple Layout v1 (authoritative)

### Source packs (YAML only)
- `honeypot-platform/packs/low/<honeypot_id>.yaml`
- `honeypot-platform/packs/high/<honeypot_id>.yaml`

Optional assets (only if required):
- `honeypot-platform/packs/low/<honeypot_id>/**`
- `honeypot-platform/packs/high/<honeypot_id>/**`

### Operator docs/scripts
- `honeypot-platform/honeypots/low/<honeypot_id>/README.md`
- `honeypot-platform/honeypots/high/<honeypot_id>/README.md`
- `honeypot-platform/honeypots/high/<honeypot_id>/reset.sh` (recommended)

### Generated output (never committed)
- Compose: `honeypot-platform/deploy/compose/<honeypot_id>/docker-compose.yml` (overwritten)
- Artifacts: `honeypot-platform/run/artifacts/<honeypot_id>/**` (overwritten)

## MUST rules
- MUST use `honeypot_id` as the only filesystem identifier.
- MUST set `metadata.id == <honeypot_id>` in the corresponding YAML.
- MUST keep packs as `.yaml` files under `packs/{low,high}`.
- MUST keep human docs under `honeypots/{low,high}/<honeypot_id>/README.md`.
- MUST render compose to `deploy/compose/<honeypot_id>/docker-compose.yml`.
- MUST write artifacts to `run/artifacts/<honeypot_id>/...`.
- MUST overwrite compose + artifacts in place for each run.

## MUST NOT rules
- MUST NOT create `run/artifacts/<runs-subtree>/**`.
- MUST NOT create Markdown beside pack YAML files (`packs/**/*.md`).
- MUST NOT commit generated compose files under `honeypots/**`.
- MUST NOT create folders that differ from `honeypot_id` (example forbidden: `honeypots/high/2021-41773_42013/`).

## Naming
- Recommended `honeypot_id` format: `cve-YYYY-NNNN` or `cve-YYYY-NNNN_YYYY-NNNN`.
- Examples:
  - `cve-2021-41773_42013`
  - `cve-2020-25213`

## Overwrite warning
Simple Layout v1 has **no run isolation**. Operators must not run two copies of the same honeypot concurrently. Starting a new run for a honeypot overwrites prior artifacts and compose output for that `honeypot_id`.

Operational guidance:
- Stop existing compose project first.
- Clear `run/artifacts/<honeypot_id>/` before new runs.
- Use per-honeypot reset scripts for consistent restart behavior.

## Examples

Low interaction:
- Pack: `honeypot-platform/packs/low/cve-2020-25213.yaml`
- README: `honeypot-platform/honeypots/low/cve-2020-25213/README.md`
- Artifacts: `honeypot-platform/run/artifacts/cve-2020-25213/`

High interaction:
- Pack: `honeypot-platform/packs/high/cve-2021-41773_42013.yaml`
- README: `honeypot-platform/honeypots/high/cve-2021-41773_42013/README.md`
- Compose: `honeypot-platform/deploy/compose/cve-2021-41773_42013/docker-compose.yml`
- Artifacts: `honeypot-platform/run/artifacts/cve-2021-41773_42013/`
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

### `honeypot-platform/docs/PACK_SPEC.md`  _(~3.8 KB; showing ≤800 lines)_
```md
# Pack Specification (v1)

## File Format
- Pack files are real YAML (`.yaml`/`.yml`), parsed with YAML semantics.
- JSON packs (`.json`) are also accepted.

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
- `sensors`: sensor descriptors with `name`, `type`, `config`, and `attach`.

## Sensor Config + Attach Semantics
### `fsmon`
```yaml
- name: fsmon-sensor
  type: fsmon
  config:
    watch:
      - /var/www/html
      - /var/www/html/wp-content/uploads
    allow_globs: ["**"]
    deny_globs: ["**/cache/**"]
    max_bytes: 262144
  attach:
    service: web
```
- `attach.service` is required.
- **Important:** fsmon sidecars can only see files from shared volumes/binds. Each watched path must be covered by a mount in the attached service, or compose rendering fails.

### `proxy`
```yaml
- name: proxy-sensor
  type: proxy
  config:
    upstream: http://web:80
    listen_port: 8080
    listen_host: 0.0.0.0
    keep_host_header: true
  attach:
    service: web
```
- `config.upstream` is required.
- `listen_port` defaults to `8080` and is used for both proxy bind port and moved port mappings.
- `listen_host` is optional and defaults to `0.0.0.0`.
- `keep_host_header` is optional and defaults to `true` so upstream services receive the original client `Host` header.
- Port fronting rule: if attached service publishes host ports, renderer moves published ports from the app service to the proxy service, mapping to the proxy listen port.

Redirect troubleshooting:
- If redirects point to internal service names like `web:...`, ensure `keep_host_header: true` (default) in proxy config.

### `pcap`
```yaml
- name: pcap-sensor
  type: pcap
  config:
    interface: any
    rotate_seconds: 60
    rotate_count: 10
  attach:
    service: proxy-sensor
```
- Prefer `attach.service` for true sidecar behavior (`network_mode: service:<name>`).
- Optional `attach.network` is supported for network joins when service sidecar mode is not used.

## Validation Rules
Schema validation is run first (shape/types). Semantic checks run after schema validation and enforce interaction-specific requirements:
- low interaction packs require `behaviors`
- high interaction packs require `stack`


### `egress_proxy`
```yaml
- name: egress
  type: egress_proxy
  attach:
    services: ["web"]
  config:
    listen_host: "0.0.0.0"
    listen_port: 3128
    force_egress_via_proxy: true
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
- High-interaction only.
- `attach.services[]` must point to services in `stack.services`.
- `force_egress_via_proxy: true` renders `hp_internal` (internal) and `hp_external` networks, attaching app services only to internal and proxy to both.
- Capture defaults to `bodies: "*"` (all response bodies, subject to caps); use `bodies: "none"` or `capture.enabled: false` for metadata-only mode.
- TLS MITM auto-generates and persists a per-stack CA when enabled and triggers post-start CA trust installation for attached services.
```

### `honeypot-platform/docs/README.md`  _(~0.2 KB; showing ≤800 lines)_
```md
# Honeypot Platform Documentation

This directory contains architecture, specification, sensor, storage, deployment, and security guidance for the YAML-first honeypot platform.
```

### `honeypot-platform/docs/SECURITY.md`  _(~1.1 KB; showing ≤800 lines)_
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
```

### `honeypot-platform/docs/SENSORS.md`  _(~3.2 KB; showing ≤800 lines)_
```md
# Sensors

## Shared Contract
All sensors read common environment variables:
- `HOHO_PACK_ID`
- `HOHO_STORAGE_BACKEND=filesystem`
- `HOHO_STORAGE_ROOT=/artifacts`

`/artifacts` is a sensor/container mountpoint. The runtime maps it to a host path:
- Simple mode: `<storage.root>`
- Isolated run mode: `<storage.root>/runs/<run_id>`

Sensors append canonical events to `<root>/<pack_id>/index/events.jsonl` and write artifacts as content-addressed blobs.

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

Troubleshooting redirects:
- Symptom: browser gets redirected to an internal compose DNS name (for example `http://web:8088/...`).
- Cause: reverse proxy rewrites `Host` by default unless `keep_host_header` is enabled.
- Fix: keep `PROXY_KEEP_HOST_HEADER=true` (default). Set it to `false` only when upstream behavior requires rewritten host headers.

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

Runtime env used by renderer:
- `PCAP_ROTATE_SECONDS`
- `PCAP_ROTATE_COUNT`
- `PCAP_INTERFACE` (currently emitted, may be ignored by entrypoint depending on image implementation)

## Operational Notes
Disk usage can grow quickly from uploads and pcap segments. Use external rotation, retention cleanup, and dedicated storage volumes.


## Egress Proxy Sensor
- Runs mitmproxy in explicit forward-proxy mode.
- Emits `sensor.egress_proxy.http` per flow with request/response metadata and redacted headers.
- Supports response-body capture with `capture.bodies: "*"` (default) or metadata-only with `"none"`.
- Persists mitmproxy confdir under artifacts (`run/artifacts/<id>/mitmproxy-conf/`).
- With `tls_mitm.enabled: true`, hoho generates a runtime CA via openssl before startup and exports it for trust install at `run/artifacts/<id>/ca/egress-ca.crt`.
- Runtime can execute `/hoho/ca/install-ca.sh` in attached services after startup and emits `system.ca_install.succeeded` / `system.ca_install.failed` events.
- If trust install fails, HTTP capture still works; HTTPS may degrade to CONNECT-only visibility.
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

### `honeypot-platform/docs/runbooks/high-interaction-honeypot-from-cve.md`  _(~2.3 KB; showing ≤800 lines)_
```md
# Runbook: high-interaction honeypot from CVE

## Required layout (Simple Layout v1)
Follow `honeypot-platform/docs/DIRECTORY_LAYOUT.md`.

- Pack YAML: `honeypot-platform/packs/high/<honeypot_id>.yaml`
- Pack assets (optional): `honeypot-platform/packs/high/<honeypot_id>/**`
- Operator doc: `honeypot-platform/honeypots/high/<honeypot_id>/README.md`
- Reset script: `honeypot-platform/honeypots/high/<honeypot_id>/reset.sh`
- Compose output: `honeypot-platform/deploy/compose/<honeypot_id>/docker-compose.yml`
- Artifacts: `honeypot-platform/run/artifacts/<honeypot_id>/...`

## Capture priorities
- PCAP capture.
- HTTP proxy capture for downloads and request metadata.
- Filesystem monitoring.
- Process/audit telemetry where available.

## Forbidden
- Do not create `run/artifacts/<runs-subtree>/**`.
- Do not use run-isolated filesystem paths.
- Do not put Markdown files in `honeypot-platform/packs/**`.

## Workflow
1. Research target CVE and deployable vulnerable stack.\
2. Sometimes specifically vulnerable images for testing are available at hub.docker.com. Search for it.
3. Build high-interaction YAML at `packs/high/<honeypot_id>.yaml`.
4. Add sensors for pcap/proxy/fs monitoring.
5. Create `honeypots/high/<honeypot_id>/README.md` and `reset.sh`.
6. Validate, render compose, and run.

## Working example (recommended to read first)
High-interaction reference pack:
- [`cve-2021-41773_42013_apache_rce.yaml`](../../packs/high/cve-2021-41773_42013_apache_rce.yaml)


## Validation and run
From repo root:

```bash
PYTHONPATH=honeypot-platform/packages/hoho_core:honeypot-platform/packages/hoho_runtime \
  python -m hoho_runtime.cli validate honeypot-platform/packs/high/<honeypot_id>.yaml

PYTHONPATH=honeypot-platform/packages/hoho_core:honeypot-platform/packages/hoho_runtime \
  python -m hoho_runtime.cli render-compose honeypot-platform/packs/high/<honeypot_id>.yaml


docker compose -p "hoho-<honeypot_id>" \
  -f honeypot-platform/deploy/compose/<honeypot_id>/docker-compose.yml up -d
```

## Why output overwrites
Simple Layout v1 intentionally overwrites compose/artifacts in fixed per-honeypot locations.

Operational guidance:
- Only one active run per `honeypot_id`.
- Stop/down the previous compose stack before restarting.
- Clear `run/artifacts/<honeypot_id>/` before a new run.
```

### `honeypot-platform/docs/runbooks/low-interaction-honeypot-from-cve.md`  _(~1.8 KB; showing ≤800 lines)_
```md
# Runbook: low-interaction honeypot from CVE

## Required layout (Simple Layout v1)
Follow `honeypot-platform/docs/DIRECTORY_LAYOUT.md`.

- Pack YAML: `honeypot-platform/packs/low/<honeypot_id>.yaml`
- Pack assets (optional): `honeypot-platform/packs/low/<honeypot_id>/**`
- Operator doc: `honeypot-platform/honeypots/low/<honeypot_id>/README.md`
- Compose output: `honeypot-platform/deploy/compose/<honeypot_id>/docker-compose.yml`
- Artifacts: `honeypot-platform/run/artifacts/<honeypot_id>/...`

## Forbidden
- Do not create `run/artifacts/<runs-subtree>/**`.
- Do not create Markdown files in `honeypot-platform/packs/**`.
- Do not use extra identifiers (`pack_id`, `run_id`) in filesystem paths.

## Workflow
1. Research CVE protocol surface and request patterns.
2. Derive safe request transcripts and matching logic.
3. Implement low-interaction YAML at `packs/low/<honeypot_id>.yaml`.
4. Document operator steps at `honeypots/low/<honeypot_id>/README.md`.
5. Validate and run.

## Working example (recommended to read first)
Low-interaction reference pack:
- [`cve-2021-41773_apache-2-4-49-2-4-50-traversal-rce.yaml`](../../packs/low/cve-2021-41773_apache-2-4-49-2-4-50-traversal-rce.yaml)



## Validation
From repo root:

```bash
PYTHONPATH=honeypot-platform/packages/hoho_core:honeypot-platform/packages/hoho_runtime \
  python -m hoho_runtime.cli validate honeypot-platform/packs/low/<honeypot_id>.yaml
```

## Why output overwrites
Simple Layout v1 keeps one active artifact location per honeypot. A new run overwrites `run/artifacts/<honeypot_id>/` and compose output for the same `honeypot_id`.

Operational guidance:
- Stop existing process before restart.
- Clear `run/artifacts/<honeypot_id>/` before the next run.
- Do not run two copies of the same honeypot concurrently.
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

### `honeypot-platform/honeypots/high/cve-2021-41773_42013/README.md`  _(~0.9 KB; showing ≤800 lines)_
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

### `honeypot-platform/honeypots/high/cve-2021-41773_42013/reset.sh`  _(~0.8 KB; showing ≤800 lines)_
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

### `honeypot-platform/packages/hoho_core/hoho_core/schema/pack_v1.json`  _(~9.9 KB; showing ≤800 lines)_
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
      "type": "object"
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
              "egress_proxy"
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
          }
        ],
        "additionalProperties": true
      }
    }
  },
  "additionalProperties": true
}
```

### `honeypot-platform/packages/hoho_core/hoho_core/schema/validate.py`  _(~2.4 KB; showing ≤800 lines)_
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

    services = pack.get("stack", {}).get("services", {})
    service_names = set(services.keys()) if isinstance(services, dict) else set()
    for sensor in pack.get("sensors", []):
        if sensor.get("type") != "egress_proxy":
            continue

        if interaction != "high":
            out.append("semantic error: sensor type 'egress_proxy' requires metadata.interaction=high")

        attach = sensor.get("attach", {})
        attached_services = attach.get("services", [])
        for service_name in attached_services:
            if service_name not in service_names:
                out.append(
                    f"semantic error: egress_proxy sensor '{sensor.get('name', '<unnamed>')}' attaches to unknown service '{service_name}'"
                )

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

### `honeypot-platform/packages/hoho_core/pyproject.toml`  _(~0.3 KB; showing ≤800 lines)_
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

### `honeypot-platform/packages/hoho_runtime/hoho_runtime/cli.py`  _(~8.0 KB; showing ≤800 lines)_
```python
import argparse
import json
import re
import shutil
from pathlib import Path

from hoho_core.schema.validate import load_pack, validate_pack
from hoho_runtime.config import DEFAULT_STORAGE_ROOT
from hoho_runtime.orchestration.compose_down_all import down_all
from hoho_runtime.orchestration.compose_render import render_compose
from hoho_runtime.orchestration.compose_run import run_compose
from hoho_runtime.orchestration.ca_pregen import EgressCAError, ensure_egress_ca
from hoho_runtime.server.http import run_low_http


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
        if (candidate / "packs").is_dir():
            return candidate

    return start


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
    pack = load_pack(args.pack)
    errors = validate_pack(pack)
    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        raise SystemExit(1)
    print("valid")


def cmd_render_compose(args):
    pack_path = Path(args.pack).expanduser().resolve()
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
    storage_root = _resolve_storage_root(pack, args.artifacts_root, project_root)
    out = render_compose(pack, out_dir=out_dir, artifacts_root=str(storage_root))
    print(out)


def cmd_run(args):
    pack_path = Path(args.pack).expanduser().resolve()
    project_root = _guess_project_root(pack_path)
    pack = load_pack(str(pack_path))
    storage_root = _resolve_storage_root(pack, args.artifacts_root, project_root)

    if pack["metadata"]["interaction"] == "low":
        pack.setdefault("storage", {})["root"] = str(storage_root)
        run_low_http(pack)
    else:
        honeypot_id = pack["metadata"]["id"]
        _warn_if_run_id_used(args.run_id)
        out_dir = _compose_output_dir(honeypot_id, args.output, project_root=project_root)

        artifacts_host_path = _prepare_artifacts_root(storage_root, honeypot_id)
        compose_file = render_compose(pack, out_dir=out_dir, artifacts_root=str(storage_root))
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
                }
            )
        )

        if args.no_up:
            print(compose_file)
        else:
            raise SystemExit(run_compose(compose_file, project_name=project_name, pack=pack, artifacts_root=storage_root))


def cmd_explain(args):
    pack = load_pack(args.pack)
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
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_val = sub.add_parser("validate")
    p_val.add_argument("pack")
    p_val.set_defaults(func=cmd_validate)

    p_run = sub.add_parser("run")
    p_run.add_argument("pack")
    p_run.add_argument("--no-up", action="store_true")
    p_run.add_argument("--run-id", default=None)
    p_run.add_argument("--artifacts-root", default=None)
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

### `honeypot-platform/packages/hoho_runtime/hoho_runtime/orchestration/compose_render.py`  _(~15.7 KB; showing ≤800 lines)_
```python
from copy import deepcopy
from pathlib import Path, PurePosixPath
import shutil

import yaml

from hoho_runtime.config import DEFAULT_STORAGE_ROOT


SENSOR_IMAGES = {
    "proxy": "hoho/sensor-http-proxy:latest",
    "fsmon": "hoho/sensor-fsmon:latest",
    "pcap": "hoho/sensor-pcap:latest",
    "egress_proxy": "hoho/sensor-egress-proxy:latest",
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


def _storage_env(pack_id: str) -> dict:
    return {
        "HOHO_PACK_ID": pack_id,
        "HOHO_STORAGE_BACKEND": "filesystem",
        "HOHO_STORAGE_ROOT": "/artifacts",
    }


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
) -> Path:
    pack_id = pack["metadata"]["id"]
    root = Path(out_dir or f"./deploy/compose/{pack_id}")
    shutil.rmtree(root, ignore_errors=True)
    root.mkdir(parents=True, exist_ok=True)

    runtime_dir = root / "runtime" / "ca"
    runtime_dir.mkdir(parents=True, exist_ok=True)
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

    services = deepcopy(pack.get("stack", {}).get("services", {}))
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
            "environment": _storage_env(pack_id),
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

        elif stype == "egress_proxy":
            if pack.get("metadata", {}).get("interaction") != "high":
                raise ValueError(f"egress_proxy sensor '{sname}' requires metadata.interaction=high")

            attach_services = _as_list(attach.get("services", []))
            for attach_service_name in attach_services:
                if attach_service_name not in services:
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

### `honeypot-platform/packages/hoho_runtime/hoho_runtime/orchestration/compose_run.py`  _(~6.1 KB; showing ≤800 lines)_
```python
import json
import os
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

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
    pack_id: str,
    service_name: str,
    kind: str,
    exit_code: int | None = None,
    stderr_snippet: str | None = None,
) -> None:
    event = {
        "schema_version": 1,
        "event_id": f"ca-install-{service_name}-{int(time.time() * 1000)}",
        "ts": _now_iso(),
        "pack_id": pack_id,
        "interaction": "high",
        "component": "runtime.compose",
        "kind": kind,
        "service": service_name,
    }
    if exit_code is not None:
        event["exit_code"] = exit_code
    if stderr_snippet:
        event["stderr_snippet"] = stderr_snippet
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
    service_name: str,
    storage_pack_root: Path,
    pack_id: str,
) -> None:
    cmd = ["docker", "compose"]
    if project_name:
        cmd.extend(["-p", project_name])
    cmd.extend(["-f", str(compose_file), "exec", "-T", service_name, "sh", "/hoho/ca/install-ca.sh", "/hoho/ca/egress-ca.crt"])
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode == 0:
        _emit_ca_install_event(
            storage_pack_root=storage_pack_root,
            pack_id=pack_id,
            service_name=service_name,
            kind="system.ca_install.succeeded",
        )
        return

    stderr = (proc.stderr or "").strip()
    _emit_ca_install_event(
        storage_pack_root=storage_pack_root,
        pack_id=pack_id,
        service_name=service_name,
        kind="system.ca_install.failed",
        exit_code=proc.returncode,
        stderr_snippet=stderr[:500],
    )

def _compose_base_cmd(compose_file: Path, project_name: str | None) -> list[str]:
    cmd = ["docker", "compose"]
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
) -> int:
    if pack and artifacts_root:
        pack_id = pack.get("metadata", {}).get("id", "unknown-pack")
        storage_pack_root = artifacts_root / pack_id
        storage_pack_root.mkdir(parents=True, exist_ok=True)
        (storage_pack_root / "ca").mkdir(parents=True, exist_ok=True)
        ensure_pack_eventlog(storage_pack_root)

    base = _compose_base_cmd(compose_file, project_name)

    # 1) Start detached so post-start steps can run.
    rc = subprocess.call([*base, "up", "-d"])
    if rc != 0:
        return rc

    # 2) Post-start installs (CA, etc.)
    if pack and artifacts_root:
        pack_id = pack.get("metadata", {}).get("id", "unknown-pack")
        storage_pack_root = artifacts_root / pack_id

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
                    service_name=service,
                    storage_pack_root=storage_pack_root,
                    pack_id=pack_id,
                )

    # 3) Attach back to logs AFTER everything is installed.
    print (11111111111)
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

### `honeypot-platform/packs/high/cve-2017-12629_solr_rce.yaml`  _(~1.7 KB; showing ≤800 lines)_
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

### `honeypot-platform/packs/high/cve-2020-25213_wp_file_upload.yaml`  _(~2.4 KB; showing ≤800 lines)_
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
      service: proxy-sensor
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
```

### `honeypot-platform/packs/high/cve-2021-41773_42013/cgi-bin/health.sh`  _(~0.1 KB; showing ≤800 lines)_
```bash
#!/bin/sh
echo "Content-Type: text/plain"
echo ""
echo "ok"
```

### `honeypot-platform/packs/high/cve-2021-41773_42013/htdocs/index.html`  _(~0.3 KB; showing ≤800 lines)_
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

### `honeypot-platform/packs/high/cve-2021-41773_42013_apache_rce.yaml`  _(~2.3 KB; showing ≤800 lines)_
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
        - ./packs/high/cve-2021-41773_42013/htdocs:/usr/local/apache2/htdocs
        - ./packs/high/cve-2021-41773_42013/cgi-bin:/usr/local/apache2/cgi-bin
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
      service: proxy-sensor
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
```

### `honeypot-platform/packs/high/example_wp_stack.yaml`  _(~1.6 KB; showing ≤800 lines)_
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

### `honeypot-platform/packs/low/cve-2021-41773_apache-2-4-49-2-4-50-traversal-rce.yaml`  _(~3.5 KB; showing ≤800 lines)_
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

### `honeypot-platform/packs/low/example_upload_sink.yaml`  _(~1.0 KB; showing ≤800 lines)_
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

### `honeypot-platform/packs/low/example_web.yaml`  _(~1.1 KB; showing ≤800 lines)_
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
```

### `honeypot-platform/scripts/build_sensors.sh`  _(~0.3 KB; showing ≤800 lines)_
```bash
#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

docker build -t hoho/sensor-fsmon:latest sensors/fsmon
docker build -t hoho/sensor-http-proxy:latest sensors/http_proxy
docker build -t hoho/sensor-pcap:latest sensors/pcap
docker build -t hoho/sensor-egress-proxy:latest sensors/egress_proxy
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

### `honeypot-platform/scripts/check_layout.sh`  _(~0.7 KB; showing ≤800 lines)_
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

if find packs -type f -name '*.md' | grep -q .; then
  fail "forbidden markdown file found under packs/"
fi

if find honeypots -type f -name '*.yaml' | grep -q .; then
  fail "forbidden yaml file found under honeypots/"
fi

if find honeypots -type f \( -name 'docker-compose*.yml' -o -name 'docker-compose*.yaml' \) | grep -q .; then
  fail "forbidden compose file found under honeypots/"
fi

echo "layout check passed"
```

### `honeypot-platform/sensors/egress_proxy/Dockerfile`  _(~0.3 KB; showing ≤800 lines)_
```
FROM python:3.11-slim
WORKDIR /app
COPY proxy/egress_capture_addon.py /app/egress_capture_addon.py
COPY proxy/gen_ca.py /app/gen_ca.py
COPY entrypoint.sh /entrypoint.sh
RUN pip install --no-cache-dir mitmproxy && chmod +x /entrypoint.sh
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

### `honeypot-platform/sensors/egress_proxy/proxy/egress_capture_addon.py`  _(~3.9 KB; showing ≤800 lines)_
```python
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

PACK_ID = os.getenv("HOHO_PACK_ID", "unknown-pack")
ROOT = Path(os.getenv("HOHO_STORAGE_ROOT", "/artifacts"))
CAPTURE_ENABLED = os.getenv("PROXY_CAPTURE_ENABLED", "true").lower() in {"1", "true", "yes", "on"}
CAPTURE_BODIES = os.getenv("PROXY_CAPTURE_BODIES", "*")
CAPTURE_MAX_BYTES = int(os.getenv("PROXY_CAPTURE_MAX_BYTES", "52428800"))
CAPTURE_STORE_OK_ONLY = os.getenv("PROXY_CAPTURE_STORE_OK_ONLY", "true").lower() in {"1", "true", "yes", "on"}
CAPTURE_MIN_BYTES = int(os.getenv("PROXY_CAPTURE_MIN_BYTES", "1"))
REDACT_HEADERS =[REDACTED]


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _events_path() -> Path:
    return ROOT / PACK_ID / "index" / "events.jsonl"


def _append_event(ev: dict) -> None:
    path = _events_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(ev) + "\n")


def _redact(headers) -> dict:
    out = {}
    for k, v in headers.items(multi=True):
        out[k] = "<redacted>" if k.lower() in REDACT_HEADERS else v
    return out


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

    artifacts = []
    if should_store:
        stored = body[:CAPTURE_MAX_BYTES]
        digest = hashlib.sha256(stored).hexdigest()
        truncated = len(stored) < total_bytes

        blob_path = ROOT / PACK_ID / "blobs" / digest[:2] / digest
        blob_path.parent.mkdir(parents=True, exist_ok=True)
        if not blob_path.exists():
            blob_path.write_bytes(stored)

        filename = _guess_filename(event_id, req.pretty_url, resp.headers if resp else {}, digest)
        obj_path = ROOT / PACK_ID / "objects" / event_id / "egress.response" / filename
        obj_path.parent.mkdir(parents=True, exist_ok=True)
        if not obj_path.exists():
            obj_path.symlink_to(blob_path)

        artifacts.append(
            {
                "kind": "egress.response_body",
                "sha256": digest,
                "bytes_captured": len(stored),
                "bytes_total": total_bytes,
                "truncated": truncated,
                "filename_guess": filename,
                "url": req.pretty_url,
                "storage_ref": f"blobs/{digest[:2]}/{digest}",
            }
        )

    ev = {
        "schema_version": 1,
        "event_id": event_id,
        "ts": _now(),
        "pack_id": PACK_ID,
        "interaction": "high",
        "kind": "sensor.egress_proxy.http",
        "component": "sensor.egress_proxy",
        "request": {
            "method": req.method,
            "url": req.pretty_url,
            "headers_redacted": _redact(req.headers),
        },
        "response": {
            "status_code": resp.status_code if resp else None,
            "headers_redacted": _redact(resp.headers) if resp else {},
            "bytes": total_bytes,
        },
        "artifacts": artifacts,
    }
    _append_event(ev)
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

### `honeypot-platform/sensors/http_proxy/proxy/capture_addon.py`  _(~3.6 KB; showing ≤800 lines)_
```python
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

PACK_ID = os.getenv("HOHO_PACK_ID", "unknown-pack")
ROOT = Path(os.getenv("HOHO_STORAGE_ROOT", "/artifacts"))


def _now():
    return datetime.now(timezone.utc).isoformat()


def _append_event(ev: dict):
    p = ROOT / PACK_ID / "index" / "events.jsonl"
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("a", encoding="utf-8") as f:
        f.write(json.dumps(ev) + "\n")


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
        digest = hashlib.sha256(body).hexdigest() if body else None

        if body:
            bp = ROOT / PACK_ID / "blobs" / digest[:2] / digest
            bp.parent.mkdir(parents=True, exist_ok=True)
            if not bp.exists():
                bp.write_bytes(body)

        peername = _peername(flow)
        src_ip = peername[0] if peername else None
        src_port = peername[1] if peername else None

        ev = {
            "schema_version": 1,
            "event_id": flow.id,
            "ts": _now(),
            "pack_id": PACK_ID,
            "interaction": "high",
            "component": "sensor.http_proxy",
            "src": {
                "ip": src_ip,
                "port": src_port,
                "forwarded_for": _forwarded_for_values(req),
                "user_agent": req.headers.get("User-Agent"),
            },
            "proto": "http",
            "http": {"host": req.headers.get("Host")},
            "request": {
                "method": req.method,
                "path": req.path,
                "query": dict(req.query),
                "headers_redacted": {
                    k: [REDACTED]
                    for k, v in req.headers.items()
                },
                "content_type": req.headers.get("Content-Type"),
                "content_length": len(body),
            },
            "response": {
                "status_code": resp.status_code if resp else None,
                "bytes_sent": len(resp.raw_content or b"") if resp else 0,
                "profile": None,
            },
            "classification": {"verdict": "unknown", "tags": [], "indicators": []},
            "decision": {
                "truncated": False,
                "oversized": False,
                "rate_limited": False,
                "dropped": False,
            },
            "artifacts": (
                [
                    {
                        "kind": "request_body",
                        "sha256": digest,
                        "size": len(body),
                        "mime": req.headers.get("Content-Type", "application/octet-stream"),
                        "storage_ref": f"blobs/{digest[:2]}/{digest}",
                        "meta": {},
                    }
                ]
                if body
                else []
            ),
        }
        _append_event(ev)
    except Exception as exc:  # noqa: BLE001
        _log_error(str(exc))
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
