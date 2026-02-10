# Compose output directory

By default, `hoho` writes compose bundles under `<project_root>/deploy/compose/<honeypot_id>/`.

When `-o/--output` is not provided, the CLI discovers `project_root` by walking up from the pack path and selecting:
1. the first ancestor containing `deploy/compose` (or `deploy/compose/README.md`),
2. otherwise the first ancestor containing `packs/`,
3. otherwise the pack file's parent directory.

If `-o/--output` is provided, `hoho` keeps existing behavior and uses that path as given.
