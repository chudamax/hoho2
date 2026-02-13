import asyncio
import hashlib
import json
import logging
import os
from contextlib import suppress
from datetime import UTC, datetime
from pathlib import Path
from urllib.parse import urlparse

from fastapi import FastAPI, Header, HTTPException, Request
from fastapi.responses import FileResponse, RedirectResponse, StreamingResponse

from .db import BlobMeta, HubDB
from .filetype import detect_blob

DATA = Path(os.getenv("HOHO_HUB_DATA", "./data"))
BLOBS = DATA / "blobs"
TOKEN = os.getenv("HOHO_HUB_TOKEN", "")
BACKFILL_ENABLED = os.getenv("HOHO_HUB_BACKFILL", "0") == "1"
FILETYPE_DETECT_ENABLED = os.getenv("HOHO_HUB_FILETYPE_DETECT", "1") == "1"
FILETYPE_DETECT_MAX_BYTES = max(1, int(os.getenv("HOHO_HUB_FILETYPE_DETECT_MAX_BYTES", "262144")))
FILETYPE_LAZY = os.getenv("HOHO_HUB_FILETYPE_LAZY", "0") == "1"
FILETYPE_BACKFILL_ENABLED = os.getenv("HOHO_HUB_FILETYPE_BACKFILL", "0") == "1"
FILETYPE_BACKFILL_LIMIT = max(1, int(os.getenv("HOHO_HUB_FILETYPE_BACKFILL_LIMIT", "100")))
WEBUI_DIST = Path(__file__).parent / "webui_dist"

logger = logging.getLogger(__name__)

DB = HubDB(DATA / "hub.db")
if BACKFILL_ENABLED or DB.artifacts_count() == 0:
    DB.backfill_artifacts()

app = FastAPI()
_SUBSCRIBERS: set[asyncio.Queue] = set()


def _auth(authorization: str | None, x_hoho_token: str | None):
    if not TOKEN:
        return
    bearer = (authorization or "").replace("Bearer ", "")
    if bearer != TOKEN and x_hoho_token != TOKEN:
        raise HTTPException(status_code=401, detail="unauthorized")


def _event_summary(event: dict) -> dict:
    artifacts = (event.get("artifacts") or []) if isinstance(event.get("artifacts"), list) else []
    req = event.get("request") or {}
    src = event.get("src") or {}
    resp = event.get("response") or {}
    http = event.get("http") or {}
    hdrs = req.get("headers_redacted") or {}
    forwarded_for = src.get("forwarded_for") if isinstance(src.get("forwarded_for"), list) else []
    user_agent = src.get("user_agent") or hdrs.get("User-Agent")
    return {
        "event_id": event.get("event_id"),
        "ts": event.get("ts"),
        "honeypot_id": event.get("honeypot_id") or event.get("pack_id"),
        "session_id": event.get("session_id"),
        "event_name": event.get("event_name"),
        "component": event.get("component"),
        "verdict": (event.get("classification") or {}).get("verdict"),
        "tags": (event.get("classification") or {}).get("tags") or [],
        "artifacts_count": len(artifacts),
        "artifact_badges": _artifact_badges_for_artifacts(artifacts),
        "http_summary": {
            "method": req.get("method"),
            "path": req.get("path"),
            "status_code": resp.get("status_code"),
            "host": http.get("host") or hdrs.get("Host"),
            "user_agent": _truncate(user_agent, 160) if isinstance(user_agent, str) else user_agent,
        },
        "src_summary": {
            "ip": src.get("ip"),
            "port": src.get("port"),
            "forwarded_for_first": forwarded_for[0] if forwarded_for else None,
            "forwarded_for_count": len(forwarded_for),
        },
    }




def _event_summary_by_id(event_id: str) -> dict | None:
    row = DB.conn.execute(
        """
        select event_id, ts, honeypot_id, session_id, event_name, component, verdict, tags,
               http_method, http_path, http_status_code, http_user_agent, http_host,
               src_ip, src_port, src_forwarded_for
        from events
        where event_id=?
        """,
        (event_id,),
    ).fetchone()
    if not row:
        return None
    item = dict(row)
    item["tags"] = json.loads(item.get("tags") or "[]")
    mimes_by_event = DB.get_event_artifact_mimes([event_id])
    item["artifacts_count"] = len(mimes_by_event.get(event_id, []))
    item["artifact_badges"] = _artifact_badges_from_mimes(mimes_by_event.get(event_id, []))
    item["http_summary"] = _event_http_summary_from_row(item, user_agent_limit=160)
    item["src_summary"] = _event_src_summary_for_list(item)
    return item
def _bucket_mime(mime: str | None) -> str:
    m = (mime or "application/octet-stream").lower()
    if m.startswith("text/"):
        return "text"
    if m.startswith("image/"):
        return "image"
    if m in {"application/x-executable", "application/x-sharedlib", "application/x-mach-binary"}:
        return "exe"
    if m in {"application/zip", "application/x-tar", "application/gzip", "application/x-7z-compressed", "application/x-rar"}:
        return "archive"
    return "binary"


def _artifact_badges_for_artifacts(artifacts: list[dict]) -> list[str]:
    badges: list[str] = []
    for artifact in artifacts:
        if not isinstance(artifact, dict):
            continue
        badge = _bucket_mime(str(artifact.get("detected_mime") or artifact.get("mime") or ""))
        if badge not in badges:
            badges.append(badge)
    return badges


def _artifact_badges_from_mimes(mimes: list[str]) -> list[str]:
    badges: list[str] = []
    for mime in mimes:
        badge = _bucket_mime(mime)
        if badge not in badges:
            badges.append(badge)
    return badges


def _enrich_artifacts(artifacts: list[dict]) -> list[dict]:
    shas = [str(a.get("sha256")) for a in artifacts if isinstance(a, dict) and a.get("sha256")]
    meta_by_sha = DB.get_blob_meta_many(shas)
    enriched: list[dict] = []
    for artifact in artifacts:
        if not isinstance(artifact, dict):
            continue
        item = dict(artifact)
        sha = str(item.get("sha256") or "")
        meta = meta_by_sha.get(sha)
        if meta:
            item["detected_mime"] = meta.detected_mime
            item["detected_desc"] = meta.detected_desc
            item["guessed_ext"] = meta.guessed_ext
        enriched.append(item)
    return enriched




def _truncate(value: str | None, limit: int) -> str | None:
    if value is None:
        return None
    if len(value) <= limit:
        return value
    return value[:limit]


def _parse_forwarded_for(value: str | None) -> list[str]:
    if not value:
        return []
    try:
        parsed = json.loads(value)
    except json.JSONDecodeError:
        return []
    if not isinstance(parsed, list):
        return []
    return [str(item) for item in parsed if isinstance(item, str)]


def _event_http_summary_from_row(row: dict, user_agent_limit: int | None = None) -> dict:
    user_agent = row.get("http_user_agent")
    if isinstance(user_agent, str) and user_agent_limit is not None:
        user_agent = _truncate(user_agent, user_agent_limit)
    return {
        "method": row.get("http_method"),
        "path": row.get("http_path"),
        "status_code": row.get("http_status_code"),
        "host": row.get("http_host"),
        "user_agent": user_agent,
    }


def _event_src_summary_for_list(row: dict) -> dict:
    forwarded_for = _parse_forwarded_for(row.get("src_forwarded_for"))
    return {
        "ip": row.get("src_ip"),
        "port": row.get("src_port"),
        "forwarded_for_first": forwarded_for[0] if forwarded_for else None,
        "forwarded_for_count": len(forwarded_for),
    }


def _event_src_summary_for_detail(row: dict) -> dict:
    return {
        "ip": row.get("src_ip"),
        "port": row.get("src_port"),
        "forwarded_for": _parse_forwarded_for(row.get("src_forwarded_for")),
    }

def _publish_event(summary: dict):
    stale = []
    for queue in _SUBSCRIBERS:
        try:
            queue.put_nowait(summary)
        except asyncio.QueueFull:
            stale.append(queue)
    for queue in stale:
        _SUBSCRIBERS.discard(queue)


def _blob_path(sha: str) -> Path:
    return BLOBS / sha[:2] / sha


def _blob_meta_to_dict(meta: BlobMeta) -> dict[str, str | int | None]:
    return {
        "sha256": meta.sha256,
        "size": meta.size,
        "detected_mime": meta.detected_mime,
        "detected_desc": meta.detected_desc,
        "guessed_ext": meta.guessed_ext,
        "detected_at": meta.detected_at,
    }


def _detect_and_store_blob_meta(sha: str, path: Path, size: int | None = None) -> BlobMeta | None:
    if not FILETYPE_DETECT_ENABLED:
        return None

    try:
        detected = detect_blob(path, max_bytes=FILETYPE_DETECT_MAX_BYTES)
        meta = BlobMeta(
            sha256=sha,
            size=size,
            detected_mime=detected.get("detected_mime"),
            detected_desc=detected.get("detected_desc"),
            guessed_ext=detected.get("guessed_ext"),
            detected_at=datetime.now(UTC).isoformat(),
            meta_json=None,
        )
        DB.upsert_blob_meta(meta)
        return meta
    except Exception as exc:  # pragma: no cover - upload path must not break
        logger.warning("blob metadata detection failed for %s: %s", sha, exc)
        return None


def _ensure_blob_meta(sha: str, size: int | None = None) -> BlobMeta | None:
    if not sha:
        return None

    meta = DB.get_blob_meta(sha)
    if meta:
        return meta
    if not FILETYPE_DETECT_ENABLED or not FILETYPE_LAZY:
        return None

    path = _blob_path(sha)
    if not path.exists():
        return None
    return _detect_and_store_blob_meta(sha, path, size=size)


def _backfill_blob_meta():
    if not FILETYPE_DETECT_ENABLED or not FILETYPE_BACKFILL_ENABLED:
        return
    for sha in DB.list_blob_shas_missing_meta(FILETYPE_BACKFILL_LIMIT):
        path = _blob_path(sha)
        if not path.exists():
            continue
        _detect_and_store_blob_meta(sha, path, size=path.stat().st_size)


_backfill_blob_meta()


@app.put("/api/v1/blobs/{sha}")
async def put_blob(sha: str, request: Request, authorization: str | None = Header(default=None), x_hoho_token: str | None = Header(default=None)):
    _auth(authorization, x_hoho_token)
    data = await request.body()
    if hashlib.sha256(data).hexdigest() != sha:
        raise HTTPException(status_code=400, detail="sha mismatch")
    p = _blob_path(sha)
    p.parent.mkdir(parents=True, exist_ok=True)
    if not p.exists():
        p.write_bytes(data)

    if FILETYPE_DETECT_ENABLED and not FILETYPE_LAZY:
        _detect_and_store_blob_meta(sha, p, size=len(data))

    return {"ok": True}


@app.head("/api/v1/blobs/{sha}")
def head_blob(sha: str):
    p = _blob_path(sha)
    if not p.exists():
        raise HTTPException(status_code=404)
    return {}


@app.post("/api/v1/events")
def post_event(event: dict, authorization: str | None = Header(default=None), x_hoho_token: str | None = Header(default=None)):
    _auth(authorization, x_hoho_token)
    if "honeypot_id" not in event and "pack_id" in event:
        event["honeypot_id"] = event["pack_id"]
    DB.insert_event(event)
    summary = _event_summary_by_id(str(event.get("event_id") or ""))
    if summary:
        _publish_event(summary)
    return {"ok": True}


@app.get("/api/v1/honeypots")
def list_honeypots(limit: int = 200):
    limit = max(1, min(limit, 1000))
    rows = DB.conn.execute(
        """
        select honeypot_id,
               max(ts) as last_seen_ts,
               count(distinct session_id) as sessions_count,
               count(*) as events_count
        from events
        group by honeypot_id
        order by last_seen_ts desc
        limit ?
        """,
        (limit,),
    ).fetchall()
    return [dict(row) for row in rows]


@app.get("/api/v1/honeypots/{honeypot_id}/sessions")
def list_sessions(honeypot_id: str, limit: int = 200):
    limit = max(1, min(limit, 1000))
    rows = DB.conn.execute(
        """
        select session_id, agent_id, started_ts, last_seen_ts
        from sessions
        where honeypot_id=?
        order by last_seen_ts desc
        limit ?
        """,
        (honeypot_id, limit),
    ).fetchall()
    return [dict(row) for row in rows]


@app.get("/api/v1/honeypots/{honeypot_id}/sessions/{session_id}/events")
def list_session_events(honeypot_id: str, session_id: str, before_ts: str | None = None, limit: int = 200):
    limit = max(1, min(limit, 1000))
    params: list[str | int] = [honeypot_id, session_id]
    q = """
        select event_id, ts, event_name, component, verdict, tags,
               http_method, http_path, http_status_code, http_user_agent, http_host,
               src_ip, src_port, src_forwarded_for
        from events
        where honeypot_id=? and session_id=?
    """
    if before_ts:
        q += " and ts < ?"
        params.append(before_ts)
    q += " order by ts desc limit ?"
    params.append(limit)
    rows = DB.conn.execute(q, params).fetchall()
    event_ids = [str(row["event_id"]) for row in rows if row["event_id"]]
    mimes_by_event = DB.get_event_artifact_mimes(event_ids)
    out = []
    for row in rows:
        item = dict(row)
        item["tags"] = json.loads(item.get("tags") or "[]")
        item["artifact_badges"] = _artifact_badges_from_mimes(mimes_by_event.get(item["event_id"], []))
        item["http_summary"] = _event_http_summary_from_row(item, user_agent_limit=160)
        item["src_summary"] = _event_src_summary_for_list(item)
        out.append(item)
    return out


@app.get("/api/v1/events")
def list_events(limit: int = 200):
    limit = max(1, min(limit, 1000))
    rows = DB.conn.execute(
        """
        select event_id, ts, honeypot_id, session_id, event_name, component, verdict, tags,
               http_method, http_path, http_status_code, http_user_agent, http_host,
               src_ip, src_port, src_forwarded_for
        from events
        order by ts desc
        limit ?
        """,
        (limit,),
    ).fetchall()
    event_ids = [str(row["event_id"]) for row in rows if row["event_id"]]
    mimes_by_event = DB.get_event_artifact_mimes(event_ids)
    out = []
    for row in rows:
        item = dict(row)
        item["tags"] = json.loads(item.get("tags") or "[]")
        item["artifacts_count"] = len(mimes_by_event.get(item["event_id"], []))
        item["artifact_badges"] = _artifact_badges_from_mimes(mimes_by_event.get(item["event_id"], []))
        item["http_summary"] = _event_http_summary_from_row(item, user_agent_limit=160)
        item["src_summary"] = _event_src_summary_for_list(item)
        out.append(item)
    return out


@app.get("/api/v1/events/{event_id}")
def get_event(event_id: str):
    row = DB.conn.execute(
        """
        select raw_json, http_method, http_path, http_status_code, http_user_agent, http_host,
               src_ip, src_port, src_forwarded_for
        from events
        where event_id=?
        """,
        (event_id,),
    ).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="event not found")
    event = json.loads(row["raw_json"])
    artifacts = (event.get("artifacts") or []) if isinstance(event.get("artifacts"), list) else []
    event["artifacts"] = _enrich_artifacts(artifacts)
    return {
        "event": event,
        "http_summary": _event_http_summary_from_row(dict(row)),
        "src_summary": _event_src_summary_for_detail(dict(row)),
    }


@app.get("/api/v1/events/{event_id}/artifacts")
def get_event_artifacts(event_id: str):
    row = DB.conn.execute("select raw_json from events where event_id=?", (event_id,)).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="event not found")
    event = json.loads(row["raw_json"])
    artifacts = (event.get("artifacts") or []) if isinstance(event.get("artifacts"), list) else []
    return _enrich_artifacts(artifacts)


@app.get("/api/v1/artifacts")
def list_artifacts(
    honeypot_id: str | None = None,
    session_id: str | None = None,
    kind: str | None = None,
    mime_prefix: str | None = None,
    detected_mime_prefix: str | None = None,
    http_only: int = 0,
    src_ip: str | None = None,
    q: str | None = None,
    limit: int = 200,
    offset: int = 0,
):
    limit = max(1, min(limit, 1000))
    offset = max(0, offset)
    clauses = []
    params: list[str | int] = []

    if honeypot_id:
        clauses.append("a.honeypot_id=?")
        params.append(honeypot_id)
    if session_id:
        clauses.append("a.session_id=?")
        params.append(session_id)
    if kind:
        clauses.append("a.kind=?")
        params.append(kind)
    if mime_prefix:
        clauses.append("a.mime like ?")
        params.append(f"{mime_prefix}%")
    if detected_mime_prefix:
        clauses.append("bm.detected_mime like ?")
        params.append(f"{detected_mime_prefix}%")
    if http_only == 1:
        clauses.append("(e.http_method is not null or e.http_path is not null)")
    if src_ip:
        clauses.append("e.src_ip=?")
        params.append(src_ip)
    if q:
        clauses.append("(a.event_id like ? or a.sha256 like ? or a.storage_ref like ? or a.meta_json like ?)")
        like = f"%{q}%"
        params.extend([like, like, like, like])

    sql = """
        select
            a.artifact_id,
            a.ts,
            a.honeypot_id,
            a.session_id,
            a.event_id,
            a.kind,
            a.sha256,
            a.size,
            a.mime,
            a.storage_ref,
            a.meta_json,
            bm.detected_mime,
            bm.detected_desc,
            bm.guessed_ext,
            e.http_method,
            e.http_path,
            e.http_status_code,
            e.http_user_agent,
            e.http_host,
            e.src_ip,
            e.src_port,
            e.src_forwarded_for
        from artifacts a
        left join blob_meta bm on bm.sha256 = a.sha256
        left join events e on e.event_id = a.event_id
    """
    if clauses:
        sql += " where " + " and ".join(clauses)
    sql += " order by a.ts desc limit ? offset ?"
    params.extend([limit, offset])

    rows = DB.conn.execute(sql, params).fetchall()
    out = []
    for row in rows:
        detected_mime = row["detected_mime"]
        detected_desc = row["detected_desc"]
        guessed_ext = row["guessed_ext"]

        sha = row["sha256"]
        if sha and FILETYPE_LAZY and not detected_mime and not detected_desc:
            detected = _ensure_blob_meta(sha, size=row["size"])
            if detected:
                detected_mime = detected.detected_mime
                detected_desc = detected.detected_desc
                guessed_ext = detected.guessed_ext

        out.append(
            {
                "artifact_id": row["artifact_id"],
                "ts": row["ts"],
                "honeypot_id": row["honeypot_id"],
                "session_id": row["session_id"],
                "event_id": row["event_id"],
                "kind": row["kind"],
                "sha256": sha,
                "size": row["size"],
                "mime": row["mime"],
                "storage_ref": row["storage_ref"],
                "meta": json.loads(row["meta_json"] or "{}"),
                "detected_mime": detected_mime,
                "detected_desc": detected_desc,
                "guessed_ext": guessed_ext,
                "http_summary": _event_http_summary_from_row(dict(row), user_agent_limit=160),
                "src_summary": _event_src_summary_for_list(dict(row)),
            }
        )
    return out


@app.get("/api/v1/blobs/{sha}/meta")
def get_blob_meta(sha: str):
    meta = DB.get_blob_meta(sha)
    if not meta and FILETYPE_LAZY:
        path = _blob_path(sha)
        if path.exists():
            meta = _detect_and_store_blob_meta(sha, path, size=path.stat().st_size)
    if not meta:
        raise HTTPException(status_code=404, detail="blob metadata not found")
    return _blob_meta_to_dict(meta)


@app.get("/api/v1/artifacts/{artifact_id}/download")
def download_artifact(artifact_id: str):
    row = DB.conn.execute("select kind, sha256, meta_json from artifacts where artifact_id=?", (artifact_id,)).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="artifact not found")
    sha = row["sha256"]
    if not sha:
        raise HTTPException(status_code=404, detail="artifact has no blob hash")

    p = _blob_path(sha)
    if not p.exists():
        raise HTTPException(status_code=404, detail="blob not found")

    meta = json.loads(row["meta_json"] or "{}")
    filename = meta.get("filename")
    if not filename and meta.get("url"):
        parsed = urlparse(meta["url"])
        segment = Path(parsed.path).name
        if segment:
            filename = segment
    if not filename:
        filename = f"{row['kind'] or 'artifact'}_{sha[:8]}.bin"
    return FileResponse(str(p), filename=filename)


@app.get("/api/v1/stream/events")
async def stream_events(honeypot_id: str | None = None, session_id: str | None = None, since_ts: str | None = None):
    def matches(evt: dict) -> bool:
        if honeypot_id and evt.get("honeypot_id") != honeypot_id:
            return False
        if session_id and evt.get("session_id") != session_id:
            return False
        return True

    async def event_stream():
        if since_ts:
            rows = DB.conn.execute(
                """
                select event_id, ts, honeypot_id, session_id, event_name, component, verdict, tags,
                       http_method, http_path, http_status_code, http_user_agent, http_host,
                       src_ip, src_port, src_forwarded_for
                from events
                where ts >= ?
                order by ts desc
                limit 200
                """,
                (since_ts,),
            ).fetchall()
            event_ids = [str(row["event_id"]) for row in rows if row["event_id"]]
            mimes_by_event = DB.get_event_artifact_mimes(event_ids)
            for row in reversed(rows):
                payload = dict(row)
                payload["tags"] = json.loads(payload.get("tags") or "[]")
                payload["artifacts_count"] = len(mimes_by_event.get(payload["event_id"], []))
                payload["artifact_badges"] = _artifact_badges_from_mimes(mimes_by_event.get(payload["event_id"], []))
                payload["http_summary"] = _event_http_summary_from_row(payload, user_agent_limit=160)
                payload["src_summary"] = _event_src_summary_for_list(payload)
                if matches(payload):
                    yield f"data: {json.dumps(payload, separators=(',', ':'))}\n\n"

        queue: asyncio.Queue = asyncio.Queue(maxsize=500)
        _SUBSCRIBERS.add(queue)
        try:
            while True:
                try:
                    evt = await asyncio.wait_for(queue.get(), timeout=15)
                    if matches(evt):
                        yield f"data: {json.dumps(evt, separators=(',', ':'))}\n\n"
                except asyncio.TimeoutError:
                    yield ": ping\n\n"
        finally:
            _SUBSCRIBERS.discard(queue)

    return StreamingResponse(event_stream(), media_type="text/event-stream")


@app.get("/")
def home_redirect():
    return RedirectResponse(url="/ui/")


@app.get("/ui/{path:path}", include_in_schema=False)
def serve_ui(path: str):
    if not WEBUI_DIST.exists():
        raise HTTPException(status_code=404, detail="web ui not built")

    target = (WEBUI_DIST / path).resolve()
    with suppress(ValueError):
        target.relative_to(WEBUI_DIST.resolve())
        if target.is_file():
            return FileResponse(str(target))
    return FileResponse(str(WEBUI_DIST / "index.html"))


@app.get("/blobs/{sha}")
def download_blob(sha: str):
    p = _blob_path(sha)
    if not p.exists():
        raise HTTPException(status_code=404)
    return FileResponse(str(p), filename=sha)
