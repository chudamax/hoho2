# Deprecated: packs/

`packs/` is deprecated as the primary honeypot source.

Use canonical honeypot folders instead:
- `honeypot-platform/honeypots/high/<honeypot_id>/honeypot.yaml`
- `honeypot-platform/honeypots/low/<honeypot_id>/honeypot.yaml`

CLI compatibility remains temporarily:
- `hoho run honeypot-platform/packs/high/<id>.yaml`
- `hoho run honeypot-platform/packs/low/<id>.yaml`

These old paths emit a deprecation warning.
