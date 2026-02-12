import json
import os
import time
from dataclasses import dataclass
from pathlib import Path

import requests

from hoho_core.telemetry.filters import load_rules_from_env, should_keep


@dataclass
class ShipperStats:
    shipped: int = 0
    skipped: int = 0
    errors: int = 0


def _iter_honeypot_dirs(artifacts_root: Path, honeypot_ids: list[str] | None) -> list[Path]:
    if honeypot_ids:
        return [artifacts_root / honeypot_id for honeypot_id in honeypot_ids]

    out: list[Path] = []
    if not artifacts_root.exists():
        return out

    for child in sorted(artifacts_root.iterdir()):
        if not child.is_dir():
            continue
        if (child / "index" / "events.jsonl").exists():
            out.append(child)
    return out


def _read_cursor(index_dir: Path, cursor_name: str) -> int:
    cursor_path = index_dir / cursor_name
    if not cursor_path.exists():
        old_cursor = index_dir / "forwarder.cursor"
        if old_cursor.exists():
            cursor_path.write_text(old_cursor.read_text(encoding="utf-8"), encoding="utf-8")

    if not cursor_path.exists():
        return 0

    raw = cursor_path.read_text(encoding="utf-8").strip()
    if not raw:
        return 0

    try:
        return max(int(raw), 0)
    except ValueError:
        return 0


def _write_cursor(index_dir: Path, cursor_name: str, offset: int) -> None:
    (index_dir / cursor_name).write_text(str(offset), encoding="utf-8")


def _iter_artifact_shas(event: dict) -> list[str]:
    shas: list[str] = []
    for artifact in event.get("artifacts", []):
        if not isinstance(artifact, dict):
            continue
        sha = artifact.get("sha256")
        if isinstance(sha, str) and sha:
            shas.append(sha)
    return shas


def _upload_blob_if_missing(session: requests.Session, hub_url: str, headers: dict[str, str], blob_path: Path, sha: str) -> None:
    head = session.head(f"{hub_url}/api/v1/blobs/{sha}", headers=headers, timeout=5)
    if head.status_code != 404:
        return
    if not blob_path.exists() or not blob_path.is_file():
        return
    with blob_path.open("rb") as blob_fd:
        session.put(f"{hub_url}/api/v1/blobs/{sha}", data=blob_fd, headers=headers, timeout=20)


def _load_filters() -> list[dict]:
    return load_rules_from_env("HOHO_FORWARD_FILTERS_JSON")


def _ship_once_for_honeypot(
    session: requests.Session,
    hub_url: str,
    headers: dict[str, str],
    honeypot_dir: Path,
    cursor_name: str,
    max_events: int | None,
) -> ShipperStats:
    stats = ShipperStats()
    index_dir = honeypot_dir / "index"
    events_path = index_dir / "events.jsonl"
    blobs_root = honeypot_dir / "blobs"

    index_dir.mkdir(parents=True, exist_ok=True)
    if not events_path.exists():
        events_path.touch()

    offset = _read_cursor(index_dir, cursor_name)
    rules = _load_filters()

    with events_path.open("r", encoding="utf-8") as handle:
        handle.seek(offset)
        while True:
            line = handle.readline()
            if not line:
                break
            next_offset = handle.tell()

            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue

            keep, _rule = should_keep(event, rules)
            if not keep:
                stats.skipped += 1
                _write_cursor(index_dir, cursor_name, next_offset)
                offset = next_offset
                continue

            try:
                for sha in _iter_artifact_shas(event):
                    blob_path = blobs_root / sha[:2] / sha
                    _upload_blob_if_missing(session, hub_url, headers, blob_path, sha)
                response = session.post(f"{hub_url}/api/v1/events", json=event, headers=headers, timeout=10)
                response.raise_for_status()
            except requests.RequestException:
                stats.errors += 1
                break

            stats.shipped += 1
            _write_cursor(index_dir, cursor_name, next_offset)
            offset = next_offset

            if max_events is not None and stats.shipped >= max_events:
                break

    return stats


def run_shipper(
    *,
    artifacts_root: Path,
    hub_url: str,
    honeypot_ids: list[str] | None,
    once: bool,
    interval_seconds: float,
    token_env: str,
    cursor_name: str,
    max_events: int | None,
) -> int:
    token = os.getenv(token_env, "")
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    hub_url = hub_url.rstrip("/")

    session = requests.Session()
    backoff_seconds = 1.0

    try:
        while True:
            batch = ShipperStats()
            honeypot_dirs = _iter_honeypot_dirs(artifacts_root, honeypot_ids)

            for honeypot_dir in honeypot_dirs:
                stats = _ship_once_for_honeypot(
                    session,
                    hub_url,
                    headers,
                    honeypot_dir,
                    cursor_name,
                    max_events,
                )
                batch.shipped += stats.shipped
                batch.skipped += stats.skipped
                batch.errors += stats.errors

            print(
                f"[shipper] shipped={batch.shipped} skipped={batch.skipped} errors={batch.errors} "
                f"honeypots={len(honeypot_dirs)}"
            )

            if batch.errors > 0:
                time.sleep(backoff_seconds)
                backoff_seconds = min(backoff_seconds * 2.0, 30.0)
            else:
                backoff_seconds = 1.0
                if once:
                    return 0
                time.sleep(interval_seconds)

            if once:
                return 0
    except KeyboardInterrupt:
        return 0
    except OSError:
        return 3
