import json
import sqlite3
from dataclasses import dataclass
from pathlib import Path


@dataclass
class BlobMeta:
    sha256: str
    size: int | None
    detected_mime: str | None
    detected_desc: str | None
    guessed_ext: str | None
    detected_at: str
    meta_json: str | None = None


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
        self.conn.execute(
            """
            create table if not exists blob_meta(
              sha256 text primary key,
              size integer,
              detected_mime text,
              detected_desc text,
              guessed_ext text,
              detected_at text,
              meta_json text
            )
            """
        )
        self.conn.execute("create index if not exists idx_artifacts_hs_ts on artifacts(honeypot_id, session_id, ts)")
        self.conn.execute("create index if not exists idx_artifacts_sha on artifacts(sha256)")
        self.conn.execute("create index if not exists idx_artifacts_ts on artifacts(ts)")
        self.conn.execute("create index if not exists idx_blob_meta_mime on blob_meta(detected_mime)")
        self.conn.execute("create index if not exists idx_blob_meta_detected_at on blob_meta(detected_at)")
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

    def upsert_blob_meta(self, meta: BlobMeta) -> None:
        self.conn.execute(
            """
            insert into blob_meta(sha256,size,detected_mime,detected_desc,guessed_ext,detected_at,meta_json)
            values(?,?,?,?,?,?,?)
            on conflict(sha256) do update set
              size=excluded.size,
              detected_mime=excluded.detected_mime,
              detected_desc=excluded.detected_desc,
              guessed_ext=excluded.guessed_ext,
              detected_at=excluded.detected_at,
              meta_json=excluded.meta_json
            """,
            (
                meta.sha256,
                meta.size,
                meta.detected_mime,
                meta.detected_desc,
                meta.guessed_ext,
                meta.detected_at,
                meta.meta_json,
            ),
        )
        self.conn.commit()

    def get_blob_meta(self, sha256: str) -> BlobMeta | None:
        row = self.conn.execute(
            "select sha256,size,detected_mime,detected_desc,guessed_ext,detected_at,meta_json from blob_meta where sha256=?",
            (sha256,),
        ).fetchone()
        if not row:
            return None
        return BlobMeta(
            sha256=row["sha256"],
            size=row["size"],
            detected_mime=row["detected_mime"],
            detected_desc=row["detected_desc"],
            guessed_ext=row["guessed_ext"],
            detected_at=row["detected_at"],
            meta_json=row["meta_json"],
        )

    def list_blob_shas_missing_meta(self, limit: int) -> list[str]:
        rows = self.conn.execute(
            """
            select a.sha256
            from artifacts a
            left join blob_meta bm on bm.sha256 = a.sha256
            where a.sha256 is not null and bm.sha256 is null
            group by a.sha256
            limit ?
            """,
            (limit,),
        ).fetchall()
        return [row["sha256"] for row in rows]
