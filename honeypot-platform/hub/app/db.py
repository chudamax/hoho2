import json
import sqlite3
from pathlib import Path


class HubDB:
    def __init__(self, path: Path):
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(str(path), check_same_thread=False)
        self.conn.execute(
            """
            create table if not exists events(
              event_id text primary key,
              honeypot_id text,
              session_id text,
              ts text,
              event_name text,
              component text,
              verdict text,
              tags text,
              raw_json text
            )
            """
        )
        self.conn.execute(
            """
            create table if not exists sessions(
              honeypot_id text,
              session_id text,
              agent_id text,
              started_ts text,
              last_seen_ts text,
              primary key(honeypot_id, session_id)
            )
            """
        )
        self.conn.commit()

    def insert_event(self, event: dict):
        tags = event.get("classification", {}).get("tags", [])
        self.conn.execute(
            "insert or replace into events(event_id,honeypot_id,session_id,ts,event_name,component,verdict,tags,raw_json) values(?,?,?,?,?,?,?,?,?)",
            (
                event.get("event_id"),
                event.get("honeypot_id") or event.get("pack_id"),
                event.get("session_id"),
                event.get("ts"),
                event.get("event_name"),
                event.get("component"),
                event.get("classification", {}).get("verdict"),
                json.dumps(tags),
                json.dumps(event),
            ),
        )
        self.conn.execute(
            "insert into sessions(honeypot_id,session_id,agent_id,started_ts,last_seen_ts) values(?,?,?,?,?) "
            "on conflict(honeypot_id,session_id) do update set last_seen_ts=excluded.last_seen_ts",
            (
                event.get("honeypot_id") or event.get("pack_id"),
                event.get("session_id"),
                event.get("agent_id"),
                event.get("ts"),
                event.get("ts"),
            ),
        )
        self.conn.commit()
