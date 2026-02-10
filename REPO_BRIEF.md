# Repository Brief: hoho2

_Generated 2026-02-10 14:37 UTC_

## Quick Facts
- **Branch:** main
- **Commit:** 1a315d8 (2026-02-10 15:23:01 +0100)
- **Total commits:** 19
- **Files scanned:** 77
- **Text files embedded (after filters):** 77

## Language & LOC Overview (approx.)
- **python** — files: 32 (41.6%), LOC: 958
- **md** — files: 21 (27.3%), LOC: 4541
- **bash** — files: 7 (9.1%), LOC: 122
- **other** — files: 6 (7.8%), LOC: 236
- **yaml** — files: 6 (7.8%), LOC: 460
- **json** — files: 2 (2.6%), LOC: 173
- **toml** — files: 2 (2.6%), LOC: 30
- **html** — files: 1 (1.3%), LOC: 12

## Directory Tree (depth ≤ 10)

```text
- .gitignore
- AGENTS.md
- REPO_BRIEF.md
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
    - build_sensors.sh
    - check_docs.sh
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
      - cve-2021-41773_42013_apache_traversal_rce.yaml
      - example_wp_stack.yaml
    - low
      - cve-2021-41773_apache-2-4-49-2-4-50-traversal-rce.md
      - cve-2021-41773_apache-2-4-49-2-4-50-traversal-rce.yaml
      - example_upload_sink.yaml
      - example_web.yaml
  - sensors
    - fsmon
      - Dockerfile
      - entrypoint.sh
    - http_proxy
    - pcap
  - honeypots
      - cve-2021-41773_42013_apache_traversal_rce
        - README.md
        - reset.sh
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
        - cgi-bin
          - health.sh
        - htdocs
          - index.html
  - run
    - artifacts
      - example-upload-sink
        - index
          - events.jsonl
      - example-web
```

## Recent Commits
- 1a315d8 | 2026-02-10 | Merge pull request #6 from chudamax/codex/add-high-interaction-honeypot-for-rce
- 47eec09 | 2026-02-10 | Add Apache 2.4.49/2.4.50 high-interaction traversal RCE honeypot
- 9aa29a2 | 2026-02-10 | updates
- 25748eb | 2026-02-10 | Merge pull request #5 from chudamax/codex/add-low-interaction-honeypot-for-apache-rce
- c1828c1 | 2026-02-10 | Add low-interaction Apache 2.4.49/2.4.50 traversal RCE honeypot pack
- a80731a | 2026-02-10 | updates
- 95d3407 | 2026-02-10 | updates
- eaf8062 | 2026-02-10 | Merge pull request #4 from chudamax/codex/implement-bind-mount-artifacts-for-multi-instance
- 8eb48c5 | 2026-02-10 | Add run-isolated compose storage bind mounts
- 8c9e2d8 | 2026-02-10 | Merge pull request #3 from chudamax/codex/fix-proxy-host-header-and-client-ip-handling

## Files (embedded, trimmed)
> Secret-looking lines are redacted by default. Large files are truncated to stay within budgets.

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

### `AGENTS.md`  _(~0.7 KB; showing ≤800 lines)_
```md
# AGENTS.md (repo root)

# Honeypots: low-interaction
- When asked to create a new low-interaction honeypot from a CVE, ALWAYS read:
  honeypot-platform/docs/runbooks/low-interaction-honeypot-from-cve.md
- Follow the runbook exactly: research -> derive request transcripts -> implement YAML pack -> validate/run -> document.


## Honeypots: high-interaction
- When asked to create a new high-interaction honeypot from a CVE, ALWAYS read:
  docs/runbooks/high-interaction-honeypot-from-cve.md
- Prioritize isolation + capture: pcap, proxy download capture, filesystem monitoring, process/audit logs.
- Provide a one-command reset that creates a new session artifact folder.
```

### `REPO_BRIEF.md`  _(~99.3 KB; showing ≤800 lines)_
```md
# Repository Brief: hoho2

_Generated 2026-02-10 13:28 UTC_

## Quick Facts
- **Branch:** main
- **Commit:** eaf8062 (2026-02-10 14:24:54 +0100)
- **Total commits:** 12
- **Files scanned:** 66
- **Text files embedded (after filters):** 66

## Language & LOC Overview (approx.)
- **python** — files: 32 (48.5%), LOC: 958
- **md** — files: 16 (24.2%), LOC: 3333
- **other** — files: 6 (9.1%), LOC: 236
- **bash** — files: 5 (7.6%), LOC: 90
- **yaml** — files: 3 (4.5%), LOC: 180
- **json** — files: 2 (3.0%), LOC: 173
- **toml** — files: 2 (3.0%), LOC: 30

## Directory Tree (depth ≤ 10)

```text
- .gitignore
- REPO_BRIEF.md
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
    - build_sensors.sh
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
- eaf8062 | 2026-02-10 | Merge pull request #4 from chudamax/codex/implement-bind-mount-artifacts-for-multi-instance
- 8eb48c5 | 2026-02-10 | Add run-isolated compose storage bind mounts
- 8c9e2d8 | 2026-02-10 | Merge pull request #3 from chudamax/codex/fix-proxy-host-header-and-client-ip-handling
- 2310a19 | 2026-02-10 | Fix http proxy host preservation and client addr capture
- ededa93 | 2026-02-10 | up
- fe48da6 | 2026-02-10 | Merge pull request #2 from chudamax/codex/implement-yaml-parsing-and-validation
- 8f582f5 | 2026-02-10 | Implement YAML pack parsing and sidecar-aware compose rendering
- 9c5165c | 2026-02-10 | updates
- faecb69 | 2026-02-10 | updates
- 002af03 | 2026-02-10 | Merge pull request #1 from chudamax/codex/create-yaml-first-honeypot-platform

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

### `REPO_BRIEF.md`  _(~93.3 KB; showing ≤800 lines)_
```md
# Repository Brief: hoho2

_Generated 2026-02-10 11:49 UTC_

## Quick Facts
- **Branch:** main
- **Commit:** fe48da6 (2026-02-10 12:48:26 +0100)
- **Total commits:** 7
- **Files scanned:** 65
- **Text files embedded (after filters):** 65

## Language & LOC Overview (approx.)
- **python** — files: 32 (49.2%), LOC: 804
- **md** — files: 16 (24.6%), LOC: 1983
- **other** — files: 6 (9.2%), LOC: 236
- **bash** — files: 4 (6.2%), LOC: 50
- **yaml** — files: 3 (4.6%), LOC: 180
- **json** — files: 2 (3.1%), LOC: 173
- **toml** — files: 2 (3.1%), LOC: 30

## Directory Tree (depth ≤ 10)

```text
- .gitignore
- REPO_BRIEF.md
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
- fe48da6 | 2026-02-10 | Merge pull request #2 from chudamax/codex/implement-yaml-parsing-and-validation
- 8f582f5 | 2026-02-10 | Implement YAML pack parsing and sidecar-aware compose rendering
- 9c5165c | 2026-02-10 | updates
- faecb69 | 2026-02-10 | updates
- 002af03 | 2026-02-10 | Merge pull request #1 from chudamax/codex/create-yaml-first-honeypot-platform
- d757b05 | 2026-02-10 | Remove generated artifact blob from repository
- c6f004d | 2026-02-10 | Initial commit

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

### `REPO_BRIEF.md`  _(~56.7 KB; showing ≤800 lines)_
```md
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
[REDACTED]

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
```
<!-- trimmed: file exceeded per-file limits -->

### `honeypot-platform/deploy/compose/README.md`  _(~0.4 KB; showing ≤800 lines)_
```md
# Rendered Compose Output

`hoho render-compose` writes generated Compose bundles into this tree.

- Default (`hoho render-compose <pack>`): `deploy/compose/<pack_id>/docker-compose.yml`
- Run-specific (`hoho render-compose <pack> --run-id <run_id>` or `hoho run <pack>`):
  `deploy/compose/<pack_id>/<run_id>/docker-compose.yml`

Run-specific folders are intended for concurrent isolated stacks.
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

### `honeypot-platform/docs/DEPLOYMENT.md`  _(~2.4 KB; showing ≤800 lines)_
```md
# Deployment

## Quickstart: Low-Interaction Pack
1. Validate pack:
   - `hoho validate packs/low/example_web.yaml`
2. Run runtime:
   - `hoho run packs/low/example_web.yaml`
3. Send traffic to configured listen port.
4. Inspect `run/artifacts/<pack_id>/index/events.jsonl` and `blobs/`.

## Quickstart: High-Interaction Pack (simple render mode)
1. Validate pack:
   - `hoho validate packs/high/example_wp_stack.yaml`
2. Render compose bundle:
   - `hoho render-compose packs/high/example_wp_stack.yaml`
3. Start stack:
   - `docker compose -f deploy/compose/example-wp-stack/docker-compose.yml up -d`
4. Artifacts land on host under:
   - `run/artifacts/example-wp-stack/...`

## Quickstart: High-Interaction Pack (`hoho run`, isolated)
1. Start run:
   - `hoho run packs/high/example_wp_stack.yaml`
2. `hoho run` prints JSON with `pack_id`, `run_id`, `artifacts_host_path`, `compose_file`, `project_name`.
3. Artifacts land on host under:
   - `run/artifacts/<honeypot_id>/...`

## Smoke Commands (high interaction)
From `honeypot-platform/`:
1. Render:
   - `hoho render-compose packs/high/example_wp_stack.yaml`
2. Bring up:
   - `docker compose -f deploy/compose/example-wp-stack/docker-compose.yml up -d`
3. Generate traffic:
   - `curl -i http://127.0.0.1:8088/`
4. Trigger fsmon via watched volume-backed path:
   - `docker compose -f deploy/compose/example-wp-stack/docker-compose.yml exec web sh -lc 'echo test > /var/www/html/wp-content/uploads/probe.txt'`
5. Verify artifacts/events:
   - `tail -n 50 run/artifacts/example-wp-stack/index/events.jsonl`

## Multi-instance verification helpers
After starting isolated runs with `hoho run`:

```bash
# find the newest run
ls -1d run/artifacts/<honeypot_id>

# tail events
tail -n 20 run/artifacts/<honeypot_id>/index/events.jsonl

# list blobs
find run/artifacts/<honeypot_id>/blobs -type f | head
```

## Generated Output Policy
- `deploy/compose/**` is generated output from `hoho render-compose` and should not be committed.
- Runtime artifacts under `run/artifacts/**` are also generated and ignored.
- Keep only `deploy/compose/README.md` tracked as documentation for this build-output directory.

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

### `honeypot-platform/docs/PACK_SPEC.md`  _(~2.9 KB; showing ≤800 lines)_
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

### `honeypot-platform/docs/SENSORS.md`  _(~2.5 KB; showing ≤800 lines)_
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
```

### `honeypot-platform/docs/STORAGE_LAYOUT.md`  _(~1.2 KB; showing ≤800 lines)_
```md
# Storage Layout

## Root Structure
Default root is `./run/artifacts`.

### Simple mode (no run id)
Used by low-interaction runtime and `hoho render-compose` without `--run-id`.

```text
<root>/<pack_id>/
  index/events.jsonl
  blobs/<sha256_prefix>/<sha256>
  objects/<event_id>/<kind>/<filename>
```

### Run mode (isolated instances)
Used by `hoho run` for high-interaction packs by default, and by `hoho render-compose --run-id <id>`.

```text
<root>/runs/<run_id>/<pack_id>/
  index/events.jsonl
  blobs/<sha256_prefix>/<sha256>
  objects/<event_id>/<kind>/<filename>
```

Each run gets a unique `<run_id>` directory, so concurrent stacks do not interleave artifacts. Cleanup is straightforward: remove one `runs/<run_id>` directory.

## Blob Dedupe
Blobs are keyed by SHA256 and written once. Repeated payloads map to existing blob paths. `storage_ref` values in events point to the stable blob or object location.

## Event File
`events.jsonl` is append-only and stores one JSON object per line for easy stream processing.

## Object Materialization
`objects/` is reserved for per-event extracted files or metadata sidecars when operators need easier browsing than raw blob references.
```

### `honeypot-platform/docs/runbooks/high-interaction-honeypot-from-cve.md`  _(~13.6 KB; showing ≤800 lines)_
```md
<!--
File: docs/runbooks/high-interaction-honeypot-from-cve.md
Purpose: Codex/humans runbook to create a new HIGH-interaction honeypot from a CVE ID.
-->

# Runbook: Create a high-interaction honeypot from a CVE (real service in a sandbox)

This runbook describes a repeatable process to implement a **high-interaction** honeypot starting from only a **CVE name/ID** (e.g., `CVE-2020-25213`).

High-interaction here means: you run a **real (vulnerable) service** in a controlled sandbox and capture **full attacker workflow** (pre-exploit probes, exploitation, post-exploitation downloads, file drops, process activity) for later analysis.

> This is a **defensive** runbook. It focuses on safe deployment, isolation, and telemetry.  
> Do **not** embed weaponized payloads or “how-to exploit” instructions in the repo.

---

## Where to put this so Codex uses it

**Recommended:**
- Save this file as: `docs/runbooks/high-interaction-honeypot-from-cve.md`
- Add a pointer in your repo-root `AGENTS.md`:

```md
# AGENTS.md (repo root)

## Honeypots
- When asked to create a new high-interaction honeypot from a CVE, ALWAYS read:
  docs/runbooks/high-interaction-honeypot-from-cve.md
- Prioritize isolation + capture (pcap, proxy downloads, fsmon, process/audit logs).
```

If you often work in a specific folder (e.g., `honeypots/high/`), add a folder-local `AGENTS.md` there as well.

---

## What “high-interaction” means (scope)

A high-interaction honeypot includes:

- A **real service stack** (app + dependencies) at a vulnerable version
- A safe **sandbox boundary** (container, preferably microVM / gVisor / Kata)
- **Complete telemetry**:
  - network (PCAP)
  - application logs
  - file-system changes (new/modified files)
  - process execution / command lines (best-effort)
  - outbound downloads captured via proxy (HTTP/HTTPS)
- **Resetability**:
  - fast “wipe and redeploy” (immutable image + ephemeral volumes)
  - clear artifact directories for each session/time window

---

## Inputs

Minimum required:

- `CVE_ID`: `CVE-YYYY-NNNN`

Optional:

- `PRODUCT_HINT`: “WordPress”, “Apache httpd”, “MOVEit”, etc.
- `DEPLOYMENT_MODE`: `docker-compose` or `k8s`
- `ISOLATION_LEVEL`: `container` | `gvisor` | `kata` (prefer stronger isolation for risky CVEs)
- `INGRESS_PORTS`: e.g., 80/443/8080
- `EGRESS_POLICY`: `deny-all` (best) or `allow-with-proxy` (common for download capture)

---

## Output deliverables

You must produce:

1. A runnable **high-interaction environment** for the CVE:
   - `docker-compose.yml` or Kubernetes manifests
   - a pinned vulnerable image reference (or Dockerfile that builds it)
   - configuration files (app config, reverse proxy config, etc.)

2. A **capture stack**:
   - PCAP capture (e.g., tcpdump sidecar)
   - filesystem monitoring (inotify/auditd/agent)
   - outbound proxy capture (HTTP/HTTPS)
   - structured event log (JSONL) + blob storage for artifacts

3. Documentation:
   - `README.md` for the honeypot (how to run/reset, what is captured, safety notes)
   - “Telemetry contract” (event fields, tags, artifact paths)

Recommended paths (adjust to your repo conventions):

- `honeypots/high/<cve-id>_<slug>/docker-compose.yml`
- `honeypots/high/<cve-id>_<slug>/README.md`
- `honeypots/high/<cve-id>_<slug>/config/…`
- `run/artifacts/high/<cve-id>_<slug>/<session-id>/…`

---

## Safety & operational rules (non-negotiable)

- **Isolation first**: assume the service will be compromised.
  - Prefer **Kata Containers** or **gVisor** if available.
  - If plain Docker, run rootless where possible and harden aggressively.

- **No sensitive networks**:
  - Place in an isolated VLAN/DMZ or a dedicated cloud account/subnet.
  - Never attach to internal corp networks.

- **Egress policy** (choose one):
  1) **Deny-all egress** (safest) + fake DNS responses, or
  2) **Allow egress only via a controlled proxy** that captures downloads and can block risky destinations.

- **No credentials reuse**: decoy credentials only; never put real secrets in env vars or config.

- **Artifact hygiene**:
  - All captures go to a dedicated artifact root with per-session folders.
[REDACTED]

- **Do not embed exploit payloads** in repo docs or comments. Keep matching/transcripts abstract.

---

## Reference architecture (recommended)

### Components

1. **Ingress reverse proxy** (front door)
   - Terminates TLS (optional), normalizes requests, logs requests
   - Can implement basic deception headers, rate limits, and route to target

2. **Target service stack** (the vulnerable workload)
   - App container(s) + DB/cache as required
   - Version-pinned image(s)

3. **Capture plane**
   - **PCAP**: tcpdump on the bridge/network namespace (sidecar or host-level)
   - **FS monitor**: watches web roots, temp dirs, upload dirs, and known persistence locations
   - **Process/audit**: command lines + exec events (best-effort via auditd/eBPF/agent)
   - **Outbound proxy**: transparent or explicit proxy to record downloads (HTTP/HTTPS)
   - **Artifact sink**: local filesystem or object store (MinIO/S3) with immutable session folders

4. **Reset plane**
   - rebuild/recreate containers
   - purge writable volumes (or use tmpfs/ephemeral volumes)
   - rotate artifacts

### Data flow

Ingress → Target (real service)  
Target egress → Proxy → Internet (optional)  
All traffic mirrored to PCAP capture  
FS/proc changes + proxy downloads saved as artifacts  
Structured events emitted to JSONL

---

## Phase 1 — Research the CVE (enough to deploy safely)

### 1.1 Identify deployment requirements
Determine:
- product + vulnerable version(s)
- required dependencies (DB, redis, Java, etc.)
- baseline “healthy” response when service is working
- typical attack surface (HTTP endpoints, admin panels, file upload locations)

### 1.2 Decide “what must be captured”
For this CVE family, decide whether you need:
- request bodies (uploads, serialized blobs)
- full response bodies (rare; usually avoid)
- filesystem diffs (often yes)
- outbound download capture (often yes for post-exploitation)

Deliverable: a short “capture plan” section in the honeypot README.

---

## Phase 2 — Choose/build the vulnerable workload

Preferred options (in order):

1) **Known vulnerable container image** (reproducible, pinned digest)  
2) Build from upstream release tarballs/packages at a pinned version  
3) Build from source at a tag/commit (last resort)

Rules:
- pin versions tightly (tags + digests)
- document how the vulnerable version was selected
- keep configuration minimal and realistic (default-ish)

Deliverable: `images.md` or README section listing:
- image references/digests
- exposed ports
- required env vars
- any initialization steps (DB migration, admin user creation with decoy creds)

---

## Phase 3 — Add isolation + hardening controls

### 3.1 Container hardening baseline (even for vulnerable services)
- drop Linux capabilities (keep minimal)
- run as non-root where possible (some apps require root; document)
- read-only filesystem for containers except explicit writable mounts
- separate networks for ingress vs egress
- resource limits (cpu/mem/pids)
- no Docker socket mounted (never)

### 3.2 Stronger isolation (recommended)
If your environment supports:
- **Kata**: microVM boundary
- **gVisor**: syscall interception sandbox

Deliverable: a short section in README indicating the chosen isolation level and how to enable it.

---

## Phase 4 — Build the capture stack

### 4.1 PCAP capture (must-have)
Capture at least:
- ingress traffic to target
- egress traffic from target (if allowed)

Implementation options:
- tcpdump on the Docker network interface (host-level)
- sidecar container sharing the network namespace (k8s: sidecar; docker: `network_mode: service:<name>`)

Output:
- `pcap/<timestamp>.pcap.gz`

### 4.2 HTTP/HTTPS outbound download capture (recommended)
Goal: capture files/tools pulled during post-exploitation.

Approaches:
- explicit proxy env vars (`HTTP_PROXY`, `HTTPS_PROXY`) in the target container
- transparent proxy via iptables redirect in the target namespace
- include a local CA and trust it in the target container (for HTTPS interception) **only if you accept that risk and document it**

Outputs:
- proxy access logs (structured)
- downloaded binaries/scripts saved as blobs
- optional: SHA256 manifest of all captured downloads

### 4.3 Filesystem monitoring (must-have)
Monitor typical drop locations:
- web roots
- upload dirs
- `/tmp`, `/var/tmp`
- app-specific plugin/theme/module dirs
- cron/systemd/autostart locations (if present in container)

Implementation options:
- lightweight inotify watcher writing JSON events
- periodic file tree snapshot + diff (slower but simple)
- auditd/eBPF (more complete, more complex)

Outputs:
- `fs/events.jsonl`
- `fs/snapshots/<t>/...` (optional)
- `blobs/files/<sha256>_<name>` for extracted new/modified files

### 4.4 Process / execution telemetry (best-effort, recommended)
Capture:
- process start/exit events
- command line, uid/gid
- network connections (optional)

Implementation options (pick what you can run safely):
- auditd inside container (sometimes heavy)
- host-level eBPF agent (preferred if you control host)
- app-layer logs (always)

Output:
- `proc/events.jsonl`

---

## Phase 5 — Define the artifact layout (consistent & analyzable)

Recommended artifact root:
- `run/artifacts/high/<cve-id>_<slug>/<session-id>/`

Within a session:
- `events/events.jsonl` (normalized events across subsystems)
- `pcap/traffic.pcap.gz`
- `proxy/` (logs + downloads + manifests)
- `fs/` (fs events + extracted files)
- `app/` (container logs, app logs)
- `meta/session.json` (timestamps, image digests, config hash)

Session ID suggestions:
- ISO timestamp + random suffix
- include honeypot id and port mapping

---

## Phase 6 — Run, reset, and rotate

### 6.1 Run
- bring up the stack
- verify health endpoints
- verify capture tools are writing artifacts
- verify egress policy is correct

### 6.2 Reset (must be fast)
Provide a `reset.sh` (or Make target) that:
- stops containers
- deletes writable volumes (or recreates them)
- starts fresh
- rotates artifacts into a new session folder

### 6.3 Rotation & retention
- rotate PCAP and logs by time and size
- keep a retention policy to avoid disk exhaustion

---

## Phase 7 — Smoke validation (no exploit payloads)

Validate that the honeypot “feels real” without executing exploitation:

- `curl /` and a few expected endpoints (login page, static assets)
- confirm reverse proxy logs are recorded
- confirm PCAP contains the test traffic
- upload a benign file (if the app supports uploads) and confirm:
  - request body capture (if enabled)
  - fs monitor recorded a new file
  - blob extraction stored it

---

## Minimal documentation for every high-interaction honeypot

Create `honeypots/high/<cve-id>_<slug>/README.md` with:

- Overview: CVE, product, vulnerable version(s)
- How to run / stop / reset
- Ports exposed
- Egress policy (deny-all vs proxy-only)
- What is captured:
  - PCAP
  - proxy downloads
  - fs changes
  - process telemetry
- Artifact directory structure
- Safety notes (isolation level, warnings)

---

## Acceptance checklist (definition of done)

- [ ] Stack is runnable via `docker compose up` (or `kubectl apply`)
- [ ] Target service is reachable and returns plausible responses
- [ ] PCAP is created and rotated
- [ ] Filesystem monitor records and extracts new/modified files
- [ ] Proxy capture is in place (if egress allowed) and stores downloads as blobs
- [ ] Structured events exist (JSONL) with consistent fields and tags, including `cve:<CVE_ID>`
- [ ] Reset is one command and produces a fresh session folder
- [ ] README exists with safety + capture details

---

## Templates (generic, safe)

### A) Suggested docker-compose layout (conceptual)

> This is a conceptual template showing component roles. Adapt to your repo conventions and target app.

```yaml
services:
  ingress:
    image: nginx:stable
    ports:
      - "8080:80"
    volumes:
      - ./config/nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on: [target]
    networks: [ingress_net]

  target:
    image: <pinned-vulnerable-image>
    networks:
      - ingress_net
      - egress_net
    environment:
      # if using explicit proxy:
      # HTTP_PROXY: http://proxy:8080
      # HTTPS_PROXY: http://proxy:8080
      # NO_PROXY: localhost,127.0.0.1
      - TZ=UTC
    volumes:
      - target_data:/var/lib/target   # keep minimal; prefer ephemeral
      - ./run/artifacts:/artifacts

  proxy:
    image: <proxy-image>
    networks: [egress_net]
    volumes:
      - ./run/artifacts:/artifacts

  pcap:
    image: <tcpdump-image>
    # docker: share netns with target
    network_mode: "service:target"
    volumes:
      - ./run/artifacts:/artifacts

  fsmon:
    image: <fsmon-image>
    volumes:
      - target_data:/watch:ro
      - ./run/artifacts:/artifacts
    depends_on: [target]
    networks: [ingress_net]

networks:
  ingress_net: {}
  egress_net: {}

volumes:
  target_data: {}
```

### B) Event schema (minimal)

Emit events with at least:

- `ts` (ISO8601)
- `source` (`ingress|app|proxy|pcap|fs|proc`)
- `cve` (`CVE-YYYY-NNNN`)
- `honeypot_id`
- `src_ip`, `src_port`, `dst_port` (when known)
- `summary`
- `tags` (list)
- `artifact_refs` (paths or blob hashes)

---

## Notes on “realism”

High-interaction realism comes from:
- correct base responses (headers, status codes, HTML)
- real assets (static files, admin panel structure)
- realistic latency and occasional errors
- consistent banners/version strings (but do not leak your host identity)

Avoid:
- too-perfect always-200 responses
- unrealistic giant debug banners (unless that product actually does)
- accidental exposure of your infra (hostname, cloud metadata, internal IPs)
```

### `honeypot-platform/docs/runbooks/low-interaction-honeypot-from-cve.md`  _(~9.0 KB; showing ≤800 lines)_
```md
<!--
File: docs/runbooks/low-interaction-honeypot-from-cve.md
Purpose: Codex/humans runbook to create a new low-interaction honeypot pack from a CVE ID.
-->

# Runbook: Create a low-interaction honeypot from a CVE (YAML-first)

This runbook describes a repeatable process to implement a **low-interaction** honeypot **from only a CVE name/ID** (e.g., `CVE-2021-41773`).

Low-interaction here means: **behavioral emulation** (request/response), not a real vulnerable service.  
The goal is to **attract and record** probes/exploit attempts and produce high-quality telemetry + artifacts for analysis.

---

## Where to put this so Codex uses it

**Recommended:**
- Save this file as: `docs/runbooks/low-interaction-honeypot-from-cve.md`
- Add a pointer in your repo-root `AGENTS.md`:

```md
# AGENTS.md (repo root)

## Honeypots
- When asked to create a new low-interaction honeypot from a CVE, ALWAYS read:
  docs/runbooks/low-interaction-honeypot-from-cve.md
- Follow the runbook exactly: research -> derive request transcripts -> implement YAML pack -> validate/run -> document.
- Do not paste weaponized payloads into docs or code comments; use abstract patterns only.
```

If you often work in a specific folder (e.g., `packs/low/`), you can also add a **folder-local** `AGENTS.md` there with the same pointer.

---

## Inputs

Minimum required:

- `CVE_ID`: `CVE-YYYY-NNNN`

Optional:

- `PRODUCT_HINT`: if provided (e.g., "Apache httpd"), use it to speed up research.
- `SERVICE_PERSONA`: desired banner style (server header / HTML style), if you care.
- `LISTEN_PORTS`: default ports to bind (e.g., 80/443/8080).

---

## Output deliverables

You must produce:

1. A new **YAML pack** implementing the emulation behavior.
2. A short **pack README** describing what it catches, what it stores, and how to run it. Also oneline examples to test the honeypot instance.
3. A minimal **tagging/telemetry contract** (what events/tags/indicators are emitted).

Recommended paths (adjust to your repo conventions):

- Pack: `packs/low/<cve-id>_<slug>.yaml`
- Doc:  `packs/low/<cve-id>_<slug>.md`

---

## Safety & operational rules (non-negotiable)

- **Never run real vulnerable code** in low-interaction packs.
- **Never “attack back”** and never add outbound exploitation logic.
- Store untrusted request bodies as **opaque bytes** (optionally gzip), do not parse/execute.
[REDACTED]

---

## Phase 1 — Research the CVE

### 1.1 Identify the exposed surface

Determine:

- Affected product and typical deployment context
- Protocol surface (HTTP? SOAP? JSON-RPC? multipart upload? etc.)
- Default ports/paths (if common)
- Vulnerability class (path traversal, SQLi, auth bypass, deserialization, etc.)
- Typical attacker objectives (file read, command exec, web shell dropper, etc.)

**Deliverable:** a short “CVE profile” note (can live in the pack README) with:
- product/version range (approx)
- vuln type
- primary endpoint(s)
- method(s)
- expected responses attackers look for

### 1.2 Extract “attack transcripts”

Find at least **one** public PoC/writeup that provides observable request structure:

- HTTP method
- path(s) / parameter names
- required headers (if any)
- content type and body shape (if POST/PUT)
- typical status codes and response markers

**Deliverable:** list of 2–5 request patterns:
- `PRIMARY_PROBES`: most distinctive requests
- `SECONDARY_FOLLOWUPS`: common follow-up probes (`/`, `/login`, `/robots.txt`, etc.)
- `NEGATIVE_CASES`: patterns you should *not* over-match
- `EXAMPLES_TO_TEST`: exploitations examples

---

## Phase 2 — Design the emulation behavior

### 2.1 Choose “service persona”

Pick:
- `Server` header value
- baseline landing page/body style (HTML/text/JSON)
- whether to emulate TLS (if your platform supports it)

### 2.2 Decide what to capture

At minimum, capture:
- method/path/query
- selected headers (with redaction)
- body bytes when relevant (uploads, serialized blobs, etc.)
- source IP / connection metadata (whatever your platform provides)

Tagging guidance:
- Always tag `cve:<CVE_ID>`
- Add `product:<name>` and `technique:<vuln-type>`
- Use a simple `verdict`: `probe | exploit | upload | unknown`

### 2.3 Decide response strategy

For each primary probe:
- choose a plausible status: `200/403/404/500`
- return plausible headers and small body marker
- optionally add:
  - `delay` + jitter
  - `drop` (timeout simulation) for some patterns

Goal: scanners/exploit scripts should think “something is there” and keep going,  
but you should not reveal “too perfect” behavior.

---

## Phase 3 — Implement the YAML pack

Create a new file:

`packs/low/<cve-id>_<short-slug>.yaml`

Example filename:
- `packs/low/cve-2021-41773_apache-traversal.yaml`

### 3.1 YAML template (copy/paste)

> Adjust keys to match your engine’s schema; the structure below is intentionally generic.

```yaml
apiVersion: honeypot.dev/v1
kind: HoneypotPack

metadata:
  id: cve-YYYY-NNNN-short-slug
  name: "CVE-YYYY-NNNN <Product> <VulnType> (low)"
  interaction: low
  tags:
    - cve
    - cve:YYYY-NNNN
    - product:<product>
    - technique:<vuln-type>
  description: >
    Low-interaction emulation for CVE-YYYY-NNNN. Captures probes/exploit attempts
    and returns plausible responses. Does not run real vulnerable software.

listen:
  - host: 0.0.0.0
    port: 8080

telemetry:
  emit_events: true
  redact_headers: [REDACTED]

limits:
  max_body_bytes: 1048576
  max_upload_bytes: 10485760

storage:
  backend: filesystem
  root: ./run/artifacts

behaviors:
  # --- Primary probe 1 ---
  - name: primary-probe-1
    match:
      method: GET
      pathRegex: "<stable pattern from transcript>"
    actions:
      - emit_event:
          verdict: exploit
          tags: ["cve:CVE-YYYY-NNNN", "product:<product>", "technique:<vuln-type>"]
          indicators: ["cve:CVE-YYYY-NNNN"]
      - delay:
          ms: 120
          jitterMs: 80
      - respond:
          status: 200
          headers:
            Content-Type: text/plain
            Server: "<persona>"
          body: "OK"

  # --- Primary probe 2 (POST example) ---
  - name: primary-probe-2
    match:
      method: POST
      path: "<path from transcript>"
      contentTypeContains: "application/x-www-form-urlencoded"
    actions:
      - emit_event:
          verdict: exploit
          tags: ["cve:CVE-YYYY-NNNN", "product:<product>", "technique:<vuln-type>"]
      - store_body:
          kind: request_body
          gzip: true
      - respond:
          status: 500
          headers:
            Content-Type: text/plain
            Server: "<persona>"
          body: "Internal Server Error"

  # --- Secondary: landing ---
  - name: landing
    match:
      method: GET
      path: /
    actions:
      - emit_event:
          verdict: probe
          tags: ["product:<product>"]
    respond:
      status: 200
      headers:
        Content-Type: text/html
        Server: "<persona>"
      body: "<html><body><h1>It works</h1></body></html>"

  # --- Default catch-all ---
  - name: default
    match:
      pathGlob: "/*"
    actions:
      - emit_event:
          verdict: unknown
          tags: []
    respond:
      status: 404
      headers:
        Content-Type: text/plain
      body: "not found"
```

### 3.2 Match rules: how to avoid overfitting

Prefer matching on:
- distinctive paths (or path prefixes)
- presence of parameter keys (not full payload values)
- short header tokens (only if truly distinctive)

Avoid:
- full payload regexes that capture weaponized strings
- matching on user-agent only
- matching on highly variable encodings unless necessary

Rule ordering:
- Most specific CVE rules first
- Generic landing/catch-all last

---

## Phase 4 — Validate & run (smoke)

1. Validate (if your platform supports it):
- `honeypot validate packs/low/<pack>.yaml`

2. Run:
- `honeypot run packs/low/<pack>.yaml`

3. Send harmless requests:
- `curl -i http://127.0.0.1:<port>/`
- `curl -i http://127.0.0.1:<port>/<known-probe-path>`

4. Confirm artifacts exist:
- event log (e.g., JSONL)
- stored request bodies (if enabled)

---

## Phase 5 — Document the pack

Create:

`packs/low/<cve-id>_<slug>.md`

Minimum contents:
- What it emulates (product/vuln family)
- What it captures (which endpoints, whether it stores bodies)
- Event tags/fields used
- How to run it (port, command)
- Known limitations (what is *not* emulated)

---

## Acceptance checklist

A pack is “done” when:

- [ ] YAML pack committed under `packs/low/`
- [ ] Pack has `metadata.id`, CVE tags, and persona headers
- [ ] ≥2 primary probe behaviors implemented from transcripts
- [ ] Every request emits an event
- [ ] POST/PUT bodies are stored when relevant (gzip, size limit)
- [ ] Responses are plausible (status + headers + small body)
- [ ] A short pack README exists under `packs/low/`

---

## Optional: future automation (scaffolder)

If you later build a CLI scaffolder, desired behavior:

- `honeypot scaffold --cve CVE-YYYY-NNNN --out packs/low/...`
- Pull CVE metadata and references
- Create YAML skeleton + README stub
- Leave TODOs for transcript-derived match rules
```

### `honeypot-platform/honeypots/high/cve-2021-41773_42013_apache_traversal_rce/README.md`  _(~2.3 KB; showing ≤800 lines)_
```md
# High-Interaction Honeypot: Apache 2.4.49/2.4.50 Traversal RCE

## Overview
- CVEs: `CVE-2021-41773` (path traversal + file disclosure) and `CVE-2021-42013` (path traversal + RCE when CGI is enabled).
- Product: Apache HTTP Server (`httpd`) vulnerable branch `2.4.49/2.4.50`.
- Pack file: `packs/high/cve-2021-41773_42013_apache_traversal_rce.yaml`.

## Capture plan
This honeypot prioritizes full attacker workflow visibility with currently supported sensors:
- PCAP rotation via `pcap-sensor`.
- Reverse-proxy request/response metadata + request body capture via `proxy-sensor`.
- Filesystem monitoring for web content, CGI paths, and `/tmp` via `fsmon-sensor`.

Process telemetry is best-effort in this repository; add host eBPF/audit integrations in deployment environments that support them.

## Run
From `honeypot-platform/`:

```bash
hoho validate packs/high/cve-2021-41773_42013_apache_traversal_rce.yaml
hoho run packs/high/cve-2021-41773_42013_apache_traversal_rce.yaml
```

If you prefer manual compose:

```bash
hoho render-compose packs/high/cve-2021-41773_42013_apache_traversal_rce.yaml
docker compose -f deploy/compose/cve-2021-41773_42013_apache_traversal_rce/docker-compose.yml up -d
```

## Stop
```bash
docker compose -f deploy/compose/cve-2021-41773_42013_apache_traversal_rce/docker-compose.yml down -v
```

## One-command reset
Use `./honeypots/high/cve-2021-41773_42013_apache_traversal_rce/reset.sh`.
- Stops/removes prior compose project.
- Creates a new session artifact folder under `run/artifacts/high/cve-2021-41773_42013_apache_traversal_rce/<session-id>/`.
- Re-renders compose with that artifact root.
- Starts a fresh stack.

## Ports and exposure
- Host `8091` -> proxy sensor -> Apache `80`.

## Egress policy
- Default deployment leaves container egress unchanged.
- For production capture zones, enforce network policy with deny-all or proxy-only egress at infrastructure layer.

## Artifact directory structure
Each reset/run creates a session root:

```text
run/artifacts/high/cve-2021-41773_42013_apache_traversal_rce/<session-id>/
  cve-2021-41773_42013_apache_traversal_rce/
    index/events.jsonl
    blobs/
```

## Safety notes
- Treat this target as compromised-by-design.
- Deploy in isolated network segments only.
- Use dedicated artifact storage and retention policy to avoid disk exhaustion.
```

### `honeypot-platform/honeypots/high/cve-2021-41773_42013_apache_traversal_rce/reset.sh`  _(~0.9 KB; showing ≤800 lines)_
```bash
#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/../../.." && pwd)"
PACK="packs/high/cve-2021-41773_42013_apache_traversal_rce.yaml"
PACK_ID="cve-2021-41773_42013_apache_traversal_rce"
SESSION_ID="$(date -u +%Y%m%dT%H%M%SZ)-$(openssl rand -hex 3)"
ARTIFACT_ROOT="${ROOT_DIR}/run/artifacts/high/${PACK_ID}/${SESSION_ID}"
OUT_DIR="${ROOT_DIR}/deploy/compose/${PACK_ID}"
COMPOSE_FILE="${OUT_DIR}/docker-compose.yml"

mkdir -p "${ARTIFACT_ROOT}"

if [ -f "${COMPOSE_FILE}" ]; then
  docker compose -f "${COMPOSE_FILE}" down -v || true
fi

(
  cd "${ROOT_DIR}"
  PYTHONPATH="packages/hoho_core:packages/hoho_runtime" python -m hoho_runtime.cli render-compose "${PACK}" \
    --artifacts-root "${ARTIFACT_ROOT}" \
    -o "${OUT_DIR}"
)

docker compose -f "${COMPOSE_FILE}" up -d

echo "session_id=${SESSION_ID}"
echo "artifacts=${ARTIFACT_ROOT}/${PACK_ID}"
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

### `honeypot-platform/packages/hoho_core/hoho_core/schema/pack_v1.json`  _(~4.9 KB; showing ≤800 lines)_
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
        "name": {"type": "string", "minLength": 1},
        "interaction": {"enum": ["low", "high"]},
        "tags": {"type": "array", "items": {"type": "string"}},
        "description": {"type": "string", "minLength": 1}
      },
      "additionalProperties": true
    },
    "storage": {"type": "object"},
    "limits": {"type": "object"},
    "telemetry": {"type": "object"},
    "listen": {"type": "array"},
    "responses": {"type": "object"},
    "behaviors": {"type": "array"},
    "stack": {
      "type": "object",
      "properties": {
        "runtime": {"type": "string"},
        "services": {
          "type": "object",
          "additionalProperties": {
            "type": "object",
            "properties": {
              "volumes": {
                "type": "array",
                "items": {
                  "oneOf": [
                    {"type": "string"},
                    {"type": "object"}
                  ]
                }
              },
              "networks": {
                "type": "array",
                "items": {"type": "string"}
              },
              "ports": {
                "type": "array",
                "items": {"type": "string"}
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
        "required": ["name", "type", "attach"],
        "properties": {
          "name": {"type": "string", "minLength": 1},
          "type": {"enum": ["fsmon", "proxy", "pcap"]},
          "attach": {
            "type": "object",
            "properties": {
              "service": {"type": "string", "minLength": 1},
              "network": {"type": "string", "minLength": 1}
            },
            "additionalProperties": false
          },
          "config": {
            "oneOf": [
              {
                "type": "object",
                "required": ["watch"],
                "properties": {
                  "watch": {
                    "type": "array",
                    "minItems": 1,
                    "items": {"type": "string", "minLength": 1}
                  },
                  "allow_globs": {
                    "type": "array",
                    "items": {"type": "string"}
                  },
                  "deny_globs": {
                    "type": "array",
                    "items": {"type": "string"}
                  },
                  "max_bytes": {"type": "integer", "minimum": 1}
                },
                "additionalProperties": false
              },
              {
                "type": "object",
                "required": ["upstream"],
                "properties": {
                  "upstream": {"type": "string", "minLength": 1},
                  "listen_port": {"type": "integer", "minimum": 1}
                },
                "additionalProperties": false
              },
              {
                "type": "object",
                "properties": {
                  "interface": {"type": "string", "minLength": 1},
                  "rotate_seconds": {"type": "integer", "minimum": 1},
                  "rotate_count": {"type": "integer", "minimum": 1}
                },
                "additionalProperties": false
              }
            ]
          }
        },
        "allOf": [
          {
            "if": {
              "properties": {"type": {"const": "fsmon"}},
              "required": ["type"]
            },
            "then": {
              "required": ["config"],
              "properties": {
                "config": {
                  "type": "object",
                  "required": ["watch"]
                },
                "attach": {
                  "type": "object",
                  "required": ["service"]
                }
              }
            }
          },
          {
            "if": {
              "properties": {"type": {"const": "proxy"}},
              "required": ["type"]
            },
            "then": {
              "required": ["config"],
              "properties": {
                "config": {
                  "type": "object",
                  "required": ["upstream"]
                },
                "attach": {
                  "type": "object",
                  "required": ["service"]
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

### `honeypot-platform/packages/hoho_core/hoho_core/schema/validate.py`  _(~1.7 KB; showing ≤800 lines)_
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

### `honeypot-platform/packages/hoho_runtime/README.md`  _(~0.1 KB; showing ≤800 lines)_
```md
# hoho_runtime

CLI and runtime components for low-interaction serving and high-interaction compose orchestration.
```

### `honeypot-platform/packages/hoho_runtime/hoho_runtime/__init__.py`  _(~0.0 KB; showing ≤800 lines)_
```python

```

### `honeypot-platform/packages/hoho_runtime/hoho_runtime/cli.py`  _(~4.1 KB; showing ≤800 lines)_
```python
import argparse
import json
import re
import secrets
from datetime import datetime, timezone
from pathlib import Path

from hoho_core.schema.validate import load_pack, validate_pack
from hoho_runtime.config import DEFAULT_STORAGE_ROOT
from hoho_runtime.orchestration.compose_render import render_compose
from hoho_runtime.orchestration.compose_run import run_compose
from hoho_runtime.server.http import run_low_http


def _sanitize_name(value: str) -> str:
    sanitized = re.sub(r"[^a-z0-9_-]", "-", value.lower()).strip("-_")
    return sanitized or "hoho"


def _generate_run_id() -> str:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    return f"{timestamp}-{secrets.token_hex(3)}"


def _compose_output_dir(pack_id: str, run_id: str | None, output: str | None) -> str | None:
    if output:
        return output
    if run_id:
        return str(Path("./deploy/compose") / pack_id / run_id)
    return None


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
    errors = validate_pack(pack)
    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        raise SystemExit(1)

    pack_id = pack["metadata"]["id"]
    out_dir = _compose_output_dir(pack_id, args.run_id, args.output)
    out = render_compose(pack, out_dir=out_dir, run_id=args.run_id, artifacts_root=args.artifacts_root)
    print(out)


def cmd_run(args):
    pack = load_pack(args.pack)
    if pack["metadata"]["interaction"] == "low":
        run_low_http(pack)
    else:
        pack_id = pack["metadata"]["id"]
        run_id = args.run_id or _generate_run_id()
        out_dir = _compose_output_dir(pack_id, run_id, args.output)
        compose_file = render_compose(pack, out_dir=out_dir, run_id=run_id, artifacts_root=args.artifacts_root)

        storage_root = Path(args.artifacts_root or pack.get("storage", {}).get("root", DEFAULT_STORAGE_ROOT))
        artifacts_host_path = (storage_root / "runs" / run_id).resolve() / pack_id
        project_name = _sanitize_name(f"hoho-{pack_id}-{run_id}")

        print(
            json.dumps(
                {
                    "pack_id": pack_id,
                    "run_id": run_id,
                    "artifacts_host_path": str(artifacts_host_path),
                    "compose_file": str(compose_file.resolve()),
                    "project_name": project_name,
                }
            )
        )

        if args.no_up:
            print(compose_file)
        else:
            raise SystemExit(run_compose(compose_file, project_name=project_name))


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

### `honeypot-platform/packages/hoho_runtime/hoho_runtime/orchestration/compose_render.py`  _(~8.8 KB; showing ≤800 lines)_
```python
from copy import deepcopy
from pathlib import Path, PurePosixPath

import yaml

from hoho_runtime.config import DEFAULT_STORAGE_ROOT


SENSOR_IMAGES = {
    "proxy": "hoho/sensor-http-proxy:latest",
    "fsmon": "hoho/sensor-fsmon:latest",
    "pcap": "hoho/sensor-pcap:latest",
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


def render_compose(
    pack: dict,
    out_dir: str | None = None,
    run_id: str | None = None,
    artifacts_root: str | None = None,
) -> Path:
    pack_id = pack["metadata"]["id"]
    root = Path(out_dir or f"./deploy/compose/{pack_id}")
    root.mkdir(parents=True, exist_ok=True)

    storage_root = Path(artifacts_root or pack.get("storage", {}).get("root", DEFAULT_STORAGE_ROOT))
    run_root_host = storage_root / "runs" / run_id if run_id else storage_root
    run_root_host.mkdir(parents=True, exist_ok=True)
    artifacts_bind_mount = f"{run_root_host.resolve()}:/artifacts"

    services = deepcopy(pack.get("stack", {}).get("services", {}))
    networks_used: set[str] = set()

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

        services[sname] = sensor_service

    compose = {"services": services}

    named_volumes = sorted(_collect_named_volumes(services))
    if named_volumes:
        compose["volumes"] = {volume_name: {} for volume_name in named_volumes}

    if networks_used:
        compose["networks"] = {name: {} for name in sorted(networks_used)}

    out = root / "docker-compose.yml"
    out.write_text(yaml.safe_dump(compose, sort_keys=False), encoding="utf-8")
    return out
```

### `honeypot-platform/packages/hoho_runtime/hoho_runtime/orchestration/compose_run.py`  _(~0.3 KB; showing ≤800 lines)_
```python
import subprocess
from pathlib import Path


def run_compose(compose_file: Path, project_name: str | None = None) -> int:
    cmd = ["docker", "compose"]
    if project_name:
        cmd.extend(["-p", project_name])
    cmd.extend(["-f", str(compose_file), "up", "-d"])
    return subprocess.call(cmd)
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

### `honeypot-platform/packs/high/cve-2020-25213_wp_file_upload.yaml`  _(~1.6 KB; showing ≤800 lines)_
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
```

### `honeypot-platform/packs/high/cve-2021-41773_42013_apache_traversal_rce.yaml`  _(~1.4 KB; showing ≤800 lines)_
```yaml
apiVersion: hoho.dev/v1
kind: HoneypotPack
metadata:
  id: cve-2021-41773_42013_apache_traversal_rce
  name: apache-httpd-2.4.49-2.4.50-traversal-rce
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
      image: httpd:2.4.49
      ports:
        - 8091:80
      volumes:
        - ./packs/high/cve-2021-41773_42013_apache_traversal_rce/htdocs:/usr/local/apache2/htdocs
        - ./packs/high/cve-2021-41773_42013_apache_traversal_rce/cgi-bin:/usr/local/apache2/cgi-bin
        - tmpdata:/tmp
      networks:
        - frontend
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
```

### `honeypot-platform/packs/high/cve-2021-41773_42013_apache_traversal_rce/cgi-bin/health.sh`  _(~0.1 KB; showing ≤800 lines)_
```bash
#!/bin/sh
echo "Content-Type: text/plain"
echo ""
echo "ok"
```

### `honeypot-platform/packs/high/cve-2021-41773_42013_apache_traversal_rce/htdocs/index.html`  _(~0.3 KB; showing ≤800 lines)_
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

### `honeypot-platform/packs/low/cve-2021-41773_apache-2-4-49-2-4-50-traversal-rce.md`  _(~3.2 KB; showing ≤800 lines)_
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

### `honeypot-platform/scripts/build_sensors.sh`  _(~0.2 KB; showing ≤800 lines)_
```bash
#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

docker build -t hoho/sensor-fsmon:latest sensors/fsmon
docker build -t hoho/sensor-http-proxy:latest sensors/http_proxy
docker build -t hoho/sensor-pcap:latest sensors/pcap
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
