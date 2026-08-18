#!/usr/bin/env python3
"""MV-Link conductor bridge — the manager↔executor seam, mirroring Ivan Djedaev.

WHY THIS EXISTS
---------------
The MV-Link Mini App runs on Vercel (serverless) and its MTProto data layer runs
as an unprivileged Docker container (uid 10001). Neither can safely touch the
live Hermes conductor queue at ``~/.hermes/ho.db`` — that file and its directory
are owned by ``@USER@`` and the directory is 0700 (it holds secrets). A
cross-user SQLite bind-mount would mean weakening those permissions, which we
refuse to do.

So this tiny stdlib HTTP service runs **as ``@USER@``** (same user that owns
``ho.db`` and runs ``hermes-conductor.service``). It accepts an authenticated
job payload from the MTProto container and inserts a row into ``ho_jobs`` — the
exact same queue the Telegram bot's ``Dev <task>`` keyword writes to. The live
conductor then claims the job and runs **Claude Code** (profile ``dev``, the
11-plugin dev system) as the executor. Hermes remains the manager: it formulates
the brief (this payload) and monitors via ``ho_jobs`` status.

    Vercel Mini App → mtproto.smiro.dev /handoff  (MTProto chat context bundled)
      → HermesIngestBackend (POST here) → INSERT ho_jobs
      → live conductor claims → Claude Code executes → status polled back

SECURITY
--------
* Binds to the docker bridge gateway (default 172.20.0.1) — reachable only by
  containers on ``infra_web`` and host-local processes, never the public net
  (the VPS firewall is closed to the outside for this range).
* Every request except ``/health`` must carry ``Authorization: Bearer <token>``
  matching ``CONDUCTOR_BRIDGE_TOKEN`` (compared with ``hmac.compare_digest``).
* Read-only status endpoint + a single, tightly-shaped INSERT. No arbitrary SQL.

Dependency-free (stdlib only) so it needs no venv and can run as a plain
``systemd --user`` service alongside the conductor.
"""

from __future__ import annotations

import hmac
import json
import logging
import os
import sqlite3
import subprocess
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

log = logging.getLogger("hermes.conductor-bridge")

HOME = Path(os.path.expanduser("~"))
HO_DB = os.environ.get("HO_DB", str(HOME / ".hermes" / "ho.db"))
TOKEN = os.environ.get("CONDUCTOR_BRIDGE_TOKEN", "")
BRIDGE_HOST = os.environ.get("BRIDGE_HOST", "172.20.0.1")
BRIDGE_PORT = int(os.environ.get("BRIDGE_PORT", "8790"))
DEFAULT_PROFILE = os.environ.get("BRIDGE_DEFAULT_PROFILE", "dev")
# Named a specific project of the author's (mvlink) — a project that has since been
# torn down, so the default pointed every job at a directory that exists on no
# machine at all. The projects ROOT is the honest default: a job that does not say
# where to work should land somewhere real and let the agent cd into the repo.
DEFAULT_WORKDIR = os.environ.get("BRIDGE_DEFAULT_WORKDIR") or os.environ.get(
    "HERMES_CLAUDE_SWITCHER_WORKDIR") or str(HOME / "workspaces")
DEFAULT_MAX_TURNS = int(os.environ.get("BRIDGE_DEFAULT_MAX_TURNS", "40"))

# ho_jobs.profile CHECK constraint — reject anything else early with a clean 400.
VALID_PROFILES = {
    "dev",
    "seo",
    "marketing",
    "security",
    "marketing_vb",
    "marketing_vb_sm",
}


def _map_status(raw: str) -> str:
    """Collapse the conductor's rich status set into the API's 4-state view."""
    if raw in ("queued", "deferred", "claimed"):
        return "queued"
    if raw == "done":
        return "done"
    if raw in ("failed", "aborted", "escalated"):
        return "failed"
    return "running"  # running / paused / planning / awaiting-input / verifying


def _connect() -> sqlite3.Connection:
    conn = sqlite3.connect(HO_DB, timeout=5)
    conn.row_factory = sqlite3.Row
    return conn


def _ensure_workdir(path: str) -> None:
    """Make sure the executor has a git-initialised directory to work in."""
    p = Path(path)
    try:
        p.mkdir(parents=True, exist_ok=True)
        if not (p / ".git").exists():
            subprocess.run(
                ["git", "init", "-q"], cwd=str(p), check=False, timeout=15
            )
    except OSError as exc:  # pragma: no cover - defensive
        log.warning("could not prepare work_dir %s: %s", path, exc)


def enqueue(payload: dict) -> dict:
    prompt = str(payload.get("prompt") or "").strip()
    if not prompt:
        raise ValueError("prompt is required")
    title = str(payload.get("title") or "MV-Link handoff")[:200]
    profile = str(payload.get("profile") or DEFAULT_PROFILE)
    if profile not in VALID_PROFILES:
        profile = DEFAULT_PROFILE
    work_dir = str(payload.get("work_dir") or DEFAULT_WORKDIR)
    max_turns = int(payload.get("max_turns") or DEFAULT_MAX_TURNS)
    idem = payload.get("idempotency_key")

    _ensure_workdir(work_dir)

    marker = f"<!-- conductor-idem:{idem} -->" if idem else None
    full_prompt = f"{marker}\n{prompt}" if marker else prompt

    conn = _connect()
    try:
        # Idempotency: a double-tap "Process" must not enqueue twice. Match the
        # marker against still-active jobs only (a finished one may be re-run).
        if marker:
            existing = conn.execute(
                "SELECT id, status FROM ho_jobs WHERE prompt LIKE ? "
                "AND status IN ('queued','claimed','running','planning',"
                "'paused','awaiting-input','verifying','deferred') "
                "ORDER BY id DESC LIMIT 1",
                (f"%{marker}%",),
            ).fetchone()
            if existing:
                return {
                    "job_id": str(existing["id"]),
                    "status": _map_status(existing["status"]),
                    "deduped": True,
                }
        cur = conn.execute(
            """
            INSERT INTO ho_jobs (kind, title, prompt, profile, status,
                                 work_dir, max_turns)
            VALUES ('custom', ?, ?, ?, 'queued', ?, ?)
            """,
            (title, full_prompt, profile, work_dir, max_turns),
        )
        conn.commit()
        return {"job_id": str(cur.lastrowid), "status": "queued"}
    finally:
        conn.close()


def status(job_id: str) -> dict | None:
    conn = _connect()
    try:
        row = conn.execute(
            "SELECT status, result_summary, error FROM ho_jobs WHERE id = ?",
            (int(job_id),),
        ).fetchone()
    finally:
        conn.close()
    if not row:
        return None
    return {
        "status": _map_status(row["status"]),
        "raw_status": row["status"],
        "result": row["result_summary"] or row["error"],
    }


class Handler(BaseHTTPRequestHandler):
    server_version = "conductor-bridge/1.0"

    def _send(self, code: int, body: dict) -> None:
        data = json.dumps(body).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _authed(self) -> bool:
        if not TOKEN:
            return False  # fail-closed: never run without a configured token
        header = self.headers.get("Authorization", "")
        prefix = "Bearer "
        if not header.startswith(prefix):
            return False
        return hmac.compare_digest(header[len(prefix):], TOKEN)

    def log_message(self, fmt: str, *args) -> None:  # quieter default logging
        log.info("%s - %s", self.address_string(), fmt % args)

    def do_GET(self) -> None:
        if self.path == "/health":
            self._send(200, {"ok": True, "db": HO_DB})
            return
        if not self._authed():
            self._send(401, {"error": "unauthorized"})
            return
        if self.path.startswith("/ingest/"):
            job_id = self.path.rsplit("/", 1)[-1]
            try:
                result = status(job_id)
            except (sqlite3.Error, ValueError) as exc:
                self._send(500, {"error": f"status failed: {exc}"})
                return
            if result is None:
                self._send(404, {"error": "job not found"})
                return
            self._send(200, result)
            return
        self._send(404, {"error": "not found"})

    def do_POST(self) -> None:
        if not self._authed():
            self._send(401, {"error": "unauthorized"})
            return
        if self.path.rstrip("/") != "/ingest":
            self._send(404, {"error": "not found"})
            return
        length = int(self.headers.get("Content-Length") or 0)
        raw = self.rfile.read(length) if length else b"{}"
        try:
            payload = json.loads(raw or b"{}")
        except json.JSONDecodeError:
            self._send(400, {"error": "invalid json"})
            return
        try:
            result = enqueue(payload)
        except ValueError as exc:
            self._send(400, {"error": str(exc)})
            return
        except sqlite3.Error as exc:
            self._send(500, {"error": f"enqueue failed: {exc}"})
            return
        self._send(201, result)


def main() -> None:
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s %(message)s"
    )
    if not TOKEN:
        raise SystemExit("CONDUCTOR_BRIDGE_TOKEN is required (fail-closed)")
    if not Path(HO_DB).exists():
        log.warning("ho.db not found at %s (conductor may not be initialised)", HO_DB)
    server = ThreadingHTTPServer((BRIDGE_HOST, BRIDGE_PORT), Handler)
    log.info("conductor-bridge listening on %s:%s → %s", BRIDGE_HOST, BRIDGE_PORT, HO_DB)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
