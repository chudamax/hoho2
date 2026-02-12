import asyncio
import hashlib
import json
import os
from contextlib import suppress
from pathlib import Path
from urllib.parse import urlparse

from fastapi import FastAPI, Header, HTTPException, Request
from fastapi.responses import FileResponse, RedirectResponse, StreamingResponse

from .db import HubDB

DATA = Path(os.getenv("HOHO_HUB_DATA", "./data"))
BLOBS = DATA / "blobs"
TOKEN = os.getenv("HOHO_HUB_TOKEN", "")
BACKFILL_ENABLED = os.getenv("HOHO_HUB_BACKFILL", "0") == "1"
WEBUI_DIST = Path(__file__).parent / "webui_dist"

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
    return {
        "event_id": event.get("event_id"),
        "ts": event.get("ts"),
        "honeypot_id": event.get("honeypot_id") or event.get("pack_id"),
        "session_id": event.get("session_id"),
        "event_name": event.get("event_name"),
        "component": event.get("component"),
        "verdict": (event.get("classification") or {}).get("verdict"),
        "tags": (event.get("classification") or {}).get("tags") or [],
        "artifacts_count": len(event.get("artifacts") or []),
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


@app.put("/api/v1/blobs/{sha}")
async def put_blob(sha: str, request: Request, authorization: str | None = Header(default=None), x_hoho_token: str | None = Header(default=None)):
    _auth(authorization, x_hoho_token)
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
def post_event(event: dict, authorization: str | None = Header(default=None), x_hoho_token: str | None = Header(default=None)):
    _auth(authorization, x_hoho_token)
    if "honeypot_id" not in event and "pack_id" in event:
        event["honeypot_id"] = event["pack_id"]
    DB.insert_event(event)
    _publish_event(_event_summary(event))
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
        select event_id, ts, event_name, component, verdict, tags
        from events
        where honeypot_id=? and session_id=?
    """
    if before_ts:
        q += " and ts < ?"
        params.append(before_ts)
    q += " order by ts desc limit ?"
    params.append(limit)
    rows = DB.conn.execute(q, params).fetchall()
    out = []
    for row in rows:
        item = dict(row)
        item["tags"] = json.loads(item.get("tags") or "[]")
        out.append(item)
    return out


@app.get("/api/v1/events/{event_id}")
def get_event(event_id: str):
    row = DB.conn.execute("select raw_json from events where event_id=?", (event_id,)).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="event not found")
    return json.loads(row["raw_json"])


@app.get("/api/v1/artifacts")
def list_artifacts(
    honeypot_id: str | None = None,
    session_id: str | None = None,
    kind: str | None = None,
    mime_prefix: str | None = None,
    q: str | None = None,
    limit: int = 200,
    offset: int = 0,
):
    limit = max(1, min(limit, 1000))
    offset = max(0, offset)
    clauses = []
    params: list[str | int] = []

    if honeypot_id:
        clauses.append("honeypot_id=?")
        params.append(honeypot_id)
    if session_id:
        clauses.append("session_id=?")
        params.append(session_id)
    if kind:
        clauses.append("kind=?")
        params.append(kind)
    if mime_prefix:
        clauses.append("mime like ?")
        params.append(f"{mime_prefix}%")
    if q:
        clauses.append("(event_id like ? or sha256 like ? or storage_ref like ? or meta_json like ?)")
        like = f"%{q}%"
        params.extend([like, like, like, like])

    sql = """
        select artifact_id, ts, honeypot_id, session_id, event_id, kind, sha256, size, mime, storage_ref, meta_json
        from artifacts
    """
    if clauses:
        sql += " where " + " and ".join(clauses)
    sql += " order by ts desc limit ? offset ?"
    params.extend([limit, offset])

    rows = DB.conn.execute(sql, params).fetchall()
    return [
        {
            "artifact_id": row["artifact_id"],
            "ts": row["ts"],
            "honeypot_id": row["honeypot_id"],
            "session_id": row["session_id"],
            "event_id": row["event_id"],
            "kind": row["kind"],
            "sha256": row["sha256"],
            "size": row["size"],
            "mime": row["mime"],
            "storage_ref": row["storage_ref"],
            "meta": json.loads(row["meta_json"] or "{}"),
        }
        for row in rows
    ]


@app.get("/api/v1/artifacts/{artifact_id}/download")
def download_artifact(artifact_id: str):
    row = DB.conn.execute("select kind, sha256, meta_json from artifacts where artifact_id=?", (artifact_id,)).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="artifact not found")
    sha = row["sha256"]
    if not sha:
        raise HTTPException(status_code=404, detail="artifact has no blob hash")

    p = BLOBS / sha[:2] / sha
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
                select event_id, ts, honeypot_id, session_id, event_name, component, verdict, tags
                from events
                where ts >= ?
                order by ts desc
                limit 200
                """,
                (since_ts,),
            ).fetchall()
            for row in reversed(rows):
                payload = dict(row)
                payload["tags"] = json.loads(payload.get("tags") or "[]")
                payload["artifacts_count"] = 0
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
    p = BLOBS / sha[:2] / sha
    if not p.exists():
        raise HTTPException(status_code=404)
    return FileResponse(str(p), filename=sha)
