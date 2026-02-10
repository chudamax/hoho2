# Rendered Compose Output

`hoho render-compose` writes generated Compose bundles into this tree.

- Default (`hoho render-compose <pack>`): `deploy/compose/<pack_id>/docker-compose.yml`
- Run-specific (`hoho render-compose <pack> --run-id <run_id>` or `hoho run <pack>`):
  `deploy/compose/<pack_id>/<run_id>/docker-compose.yml`

Run-specific folders are intended for concurrent isolated stacks.
