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
