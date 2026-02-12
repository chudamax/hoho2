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
TOKEN = os.getenv("HOHO_HUB_TOKEN", "")
DB = HubDB(DATA / "hub.db")
app = FastAPI()
templates = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))


def _auth(authorization: str | None, x_hoho_token: str | None):
    if not TOKEN:
        return
    bearer = (authorization or "").replace("Bearer ", "")
    if bearer != TOKEN and x_hoho_token != TOKEN:
        raise HTTPException(status_code=401, detail="unauthorized")


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
