import json
import sqlite3
from dataclasses import dataclass
from pathlib import Path


def _normalize_action(value: str | None, limit: int = 200) -> str:
    collapsed = " ".join((value or "").split())
    if not collapsed:
        return "-"
    if len(collapsed) <= limit:
        return collapsed
    return collapsed[: max(0, limit - 1)] + "…"


def _build_http_action(event: dict) -> str:
    req = event.get("request") if isinstance(event.get("request"), dict) else {}
    http = event.get("http") if isinstance(event.get("http"), dict) else {}
    headers = req.get("headers_redacted") if isinstance(req.get("headers_redacted"), dict) else {}
    method = str(req.get("method") or "-")
    path = str(req.get("path") or "/")

    query = req.get("query")
    if isinstance(query, dict) and query:
        query_parts = [f"{key}={query[key]}" for key in sorted(query)]
        path = f"{path}?{'&'.join(query_parts)}"

    host = http.get("host") or headers.get("Host")
    url = f"http://{host}{path}" if host else path
    return _normalize_action(f"{method} {url}")


def _build_fs_action(event: dict) -> str:
    artifacts = event.get("artifacts") if isinstance(event.get("artifacts"), list) else []
    chosen_artifact: dict | None = None
    fs_path = "-"
    for artifact in artifacts:
        if not isinstance(artifact, dict):
            continue
        meta = artifact.get("meta") if isinstance(artifact.get("meta"), dict) else {}
        for key in ("path", "filepath", "file_path", "target_path"):
            value = meta.get(key)
            if isinstance(value, str) and value:
                fs_path = value
                chosen_artifact = artifact
                break
        if chosen_artifact:
            break

    if fs_path == "-":
        classification = event.get("classification") if isinstance(event.get("classification"), dict) else {}
        indicators = classification.get("indicators") if isinstance(classification.get("indicators"), list) else []
        for indicator in indicators:
            if isinstance(indicator, str) and indicator.startswith("/"):
                fs_path = indicator
                break

    artifact_for_type = chosen_artifact or (artifacts[0] if artifacts and isinstance(artifacts[0], dict) else {})
    filetype = (
        artifact_for_type.get("detected_desc")
        or artifact_for_type.get("detected_mime")
        or artifact_for_type.get("mime")
        or "unknown"
    )
    return _normalize_action(f"{fs_path} ({filetype})")


def _build_falco_action(event: dict) -> str:
    falco = event.get("falco") if isinstance(event.get("falco"), dict) else {}
    fields = falco.get("output_fields") if isinstance(falco.get("output_fields"), dict) else {}
    proc_name = fields.get("proc.name")
    proc_cmdline = fields.get("proc.cmdline")
    if proc_name and proc_cmdline:
        return _normalize_action(f"{proc_name} — {proc_cmdline}")
    if proc_name:
        return _normalize_action(str(proc_name))
    if proc_cmdline:
        return _normalize_action(str(proc_cmdline))
    if falco.get("rule"):
        return _normalize_action(str(falco.get("rule")))
    return _normalize_action(str(event.get("event_name") or "-"))


def compute_event_action(event: dict) -> str:
    proto = str(event.get("proto") or "").lower()
    event_name = str(event.get("event_name") or "")

    if proto == "http" or event_name.startswith("http."):
        return _build_http_action(event)
    if proto == "fs" or event_name.startswith("fs."):
        return _build_fs_action(event)
    if event_name == "falco.alert" or isinstance(event.get("falco"), dict):
        return _build_falco_action(event)
    return _normalize_action(event_name or "-")


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
              http_method text,
              http_path text,
              http_status_code integer,
              http_user_agent text,
              http_host text,
              src_ip text,
              src_port integer,
              src_forwarded_for text,
              action text,
              raw_json text
            )
            """
        )
        self._ensure_events_columns()
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
        self.conn.execute("create index if not exists idx_events_hs_ts on events(honeypot_id, session_id, ts)")
        self.conn.execute("create index if not exists idx_events_http_path on events(http_path)")
        self.conn.execute("create index if not exists idx_events_http_status_code on events(http_status_code)")
        self.conn.execute("create index if not exists idx_events_http_host on events(http_host)")
        self.conn.execute("create index if not exists idx_events_src_ip on events(src_ip)")
        self.conn.execute("create index if not exists idx_artifacts_sha on artifacts(sha256)")
        self.conn.execute("create index if not exists idx_artifacts_ts on artifacts(ts)")
        self.conn.execute("create index if not exists idx_blob_meta_mime on blob_meta(detected_mime)")
        self.conn.execute("create index if not exists idx_blob_meta_detected_at on blob_meta(detected_at)")
        self.conn.commit()

    def _ensure_events_columns(self):
        existing = {
            str(row["name"])
            for row in self.conn.execute("pragma table_info(events)").fetchall()
            if row["name"]
        }
        desired: list[tuple[str, str]] = [
            ("http_method", "text"),
            ("http_path", "text"),
            ("http_status_code", "integer"),
            ("http_user_agent", "text"),
            ("http_host", "text"),
            ("src_ip", "text"),
            ("src_port", "integer"),
            ("src_forwarded_for", "text"),
            ("action", "text"),
        ]
        for name, col_type in desired:
            if name in existing:
                continue
            self.conn.execute(f"alter table events add column {name} {col_type}")

    def insert_event(self, event: dict):
        action = compute_event_action(event)
        event["action"] = action
        honeypot_id = event.get("honeypot_id") or event.get("pack_id")
        tags = event.get("classification", {}).get("tags", [])
        req = event.get("request") or {}
        src = event.get("src") or {}
        resp = event.get("response") or {}
        http = event.get("http") or {}
        hdrs = req.get("headers_redacted") or {}

        http_method = req.get("method")
        http_path = req.get("path")
        http_status_code = resp.get("status_code")
        http_user_agent = src.get("user_agent") or hdrs.get("User-Agent")
        http_host = http.get("host") or hdrs.get("Host")
        src_ip = src.get("ip")
        src_port = src.get("port")
        xff = src.get("forwarded_for") or []
        src_forwarded_for = json.dumps(xff, separators=(",", ":"))

        self.conn.execute(
            "insert or replace into events(event_id,honeypot_id,session_id,ts,event_name,component,verdict,tags,http_method,http_path,http_status_code,http_user_agent,http_host,src_ip,src_port,src_forwarded_for,action,raw_json) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (
                event.get("event_id"),
                honeypot_id,
                event.get("session_id"),
                event.get("ts"),
                event.get("event_name"),
                event.get("component"),
                event.get("classification", {}).get("verdict"),
                json.dumps(tags),
                http_method,
                http_path,
                http_status_code,
                http_user_agent,
                http_host,
                src_ip,
                src_port,
                src_forwarded_for,
                action,
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

    def backfill_event_actions(self, limit: int = 1000):
        rows = self.conn.execute(
            """
            select event_id, raw_json
            from events
            where action is null or action=''
            order by ts desc
            limit ?
            """,
            (max(1, limit),),
        ).fetchall()
        for row in rows:
            try:
                event = json.loads(row["raw_json"])
            except json.JSONDecodeError:
                continue
            action = compute_event_action(event)
            event["action"] = action
            self.conn.execute(
                "update events set action=?, raw_json=? where event_id=?",
                (action, json.dumps(event), row["event_id"]),
            )
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

    def get_blob_meta_many(self, shas: list[str]) -> dict[str, BlobMeta]:
        unique_shas = sorted({sha for sha in shas if sha})
        if not unique_shas:
            return {}

        placeholders = ",".join("?" for _ in unique_shas)
        rows = self.conn.execute(
            f"""
            select sha256,size,detected_mime,detected_desc,guessed_ext,detected_at,meta_json
            from blob_meta
            where sha256 in ({placeholders})
            """,
            unique_shas,
        ).fetchall()
        return {
            row["sha256"]: BlobMeta(
                sha256=row["sha256"],
                size=row["size"],
                detected_mime=row["detected_mime"],
                detected_desc=row["detected_desc"],
                guessed_ext=row["guessed_ext"],
                detected_at=row["detected_at"],
                meta_json=row["meta_json"],
            )
            for row in rows
        }

    def get_event_artifact_mimes(self, event_ids: list[str]) -> dict[str, list[str]]:
        unique_ids = sorted({event_id for event_id in event_ids if event_id})
        if not unique_ids:
            return {}

        placeholders = ",".join("?" for _ in unique_ids)
        rows = self.conn.execute(
            f"""
            select
              a.event_id,
              coalesce(m.detected_mime, a.mime, 'application/octet-stream') as mime,
              count(*) as c
            from artifacts a
            left join blob_meta m on m.sha256 = a.sha256
            where a.event_id in ({placeholders})
            group by a.event_id, mime
            """,
            unique_ids,
        ).fetchall()

        by_event: dict[str, list[str]] = {event_id: [] for event_id in unique_ids}
        for row in rows:
            by_event[row["event_id"]].extend([row["mime"]] * int(row["c"] or 0))
        return by_event
