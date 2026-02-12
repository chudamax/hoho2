import json
import sqlite3
from pathlib import Path


class HubDB:
    def __init__(self, path: Path):
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(str(path), check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
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
        self.conn.execute(
            """
            create table if not exists artifacts(
              artifact_id text primary key,
              event_id text,
              honeypot_id text,
              session_id text,
              ts text,
              kind text,
              sha256 text,
              size integer,
              mime text,
              storage_ref text,
              meta_json text
            )
            """
        )
        self.conn.execute("create index if not exists idx_artifacts_hs_ts on artifacts(honeypot_id, session_id, ts)")
        self.conn.execute("create index if not exists idx_artifacts_sha on artifacts(sha256)")
        self.conn.execute("create index if not exists idx_artifacts_ts on artifacts(ts)")
        self.conn.commit()

    def insert_event(self, event: dict):
        honeypot_id = event.get("honeypot_id") or event.get("pack_id")
        tags = event.get("classification", {}).get("tags", [])
        self.conn.execute(
            "insert or replace into events(event_id,honeypot_id,session_id,ts,event_name,component,verdict,tags,raw_json) values(?,?,?,?,?,?,?,?,?)",
            (
                event.get("event_id"),
                honeypot_id,
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
                honeypot_id,
                event.get("session_id"),
                event.get("agent_id"),
                event.get("ts"),
                event.get("ts"),
            ),
        )
        self._insert_artifacts_for_event(event)
        self.conn.commit()

    def _insert_artifacts_for_event(self, event: dict):
        event_id = event.get("event_id")
        artifacts = event.get("artifacts") or []
        if not event_id or not isinstance(artifacts, list):
            return

        for i, artifact in enumerate(artifacts):
            if not isinstance(artifact, dict):
                continue
            self.conn.execute(
                """
                insert or replace into artifacts(
                  artifact_id,event_id,honeypot_id,session_id,ts,kind,sha256,size,mime,storage_ref,meta_json
                ) values(?,?,?,?,?,?,?,?,?,?,?)
                """,
                (
                    f"{event_id}:{i}",
                    event_id,
                    event.get("honeypot_id") or event.get("pack_id"),
                    event.get("session_id"),
                    event.get("ts"),
                    artifact.get("kind"),
                    artifact.get("sha256"),
                    artifact.get("size"),
                    artifact.get("mime"),
                    artifact.get("storage_ref"),
                    json.dumps(artifact.get("meta") or {}),
                ),
            )

    def artifacts_count(self) -> int:
        row = self.conn.execute("select count(*) as c from artifacts").fetchone()
        return int(row["c"] if row else 0)

    def backfill_artifacts(self, limit: int | None = None):
        sql = "select raw_json from events order by ts desc"
        params: list[int] = []
        if limit:
            sql += " limit ?"
            params.append(limit)

        for row in self.conn.execute(sql, params):
            try:
                event = json.loads(row["raw_json"])
            except json.JSONDecodeError:
                continue
            self._insert_artifacts_for_event(event)
        self.conn.commit()
