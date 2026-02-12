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
