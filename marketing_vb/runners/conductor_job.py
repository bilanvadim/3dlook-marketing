#!/usr/bin/env python3
"""
Conductor job helper for Hermes Agent.
Usage:
  python3 conductor_job.py enqueue <title> <prompt> [profile] [work_dir] [max_turns]
  python3 conductor_job.py status [job_id]
  python3 conductor_job.py result <job_id>
  python3 conductor_job.py watch <job_id> [timeout_secs]
"""
import sys
import time
import sqlite3
import json

HO_DB = "/home/vadim_prod/3dlook-marketing/claude_code/DEV/full_stack_sm/conductor/ho.db"
DEFAULT_PROFILE = "marketing_vb_sm"
DEFAULT_WORKDIR = "/home/vadim_prod/3dlook-marketing/marketing_vb"
DEFAULT_MAX_TURNS = 80
DEFAULT_KIND = "feature"


def _db():
    return sqlite3.connect(HO_DB, timeout=15)


def enqueue(args):
    title = args[0]
    prompt = args[1]
    profile = args[2] if len(args) > 2 else DEFAULT_PROFILE
    work_dir = args[3] if len(args) > 3 else DEFAULT_WORKDIR
    max_turns = int(args[4]) if len(args) > 4 else DEFAULT_MAX_TURNS

    con = _db()
    cur = con.execute(
        "INSERT INTO ho_jobs(kind, title, prompt, profile, work_dir, max_turns) "
        "VALUES(?, ?, ?, ?, ?, ?)",
        (DEFAULT_KIND, title[:120], prompt, profile, work_dir, max_turns),
    )
    con.commit()
    job_id = cur.lastrowid
    con.close()
    print(json.dumps({"ok": True, "job_id": job_id, "profile": profile}))
    return 0


def status(args):
    job_id = args[0] if args else None
    con = _db()
    if job_id:
        rows = con.execute(
            "SELECT id, kind, substr(title,1,80), status, profile, attempts, "
            "substr(result_summary,1,500), substr(error,1,200), created_at, finished_at "
            "FROM ho_jobs WHERE id=?",
            (int(job_id),),
        ).fetchall()
    else:
        rows = con.execute(
            "SELECT id, kind, substr(title,1,60), status, profile, attempts, created_at "
            "FROM ho_jobs ORDER BY id DESC LIMIT 15"
        ).fetchall()
    con.close()

    if job_id and not rows:
        print(json.dumps({"ok": False, "error": f"Job #{job_id} not found"}))
        return 1

    if job_id:
        r = rows[0]
        print(json.dumps({
            "ok": True,
            "job": {
                "id": r[0], "kind": r[1], "title": r[2], "status": r[3],
                "profile": r[4], "attempts": r[5],
                "result_summary": r[6], "error": r[7],
                "created_at": r[8], "finished_at": r[9],
            }
        }, indent=2))
    else:
        print(json.dumps({
            "ok": True,
            "jobs": [
                {"id": r[0], "kind": r[1], "title": r[2], "status": r[3],
                 "profile": r[4], "attempts": r[5], "created_at": r[6]}
                for r in rows
            ]
        }, indent=2))
    return 0


def result(args):
    job_id = int(args[0])
    con = _db()
    row = con.execute(
        "SELECT status, result_summary, error FROM ho_jobs WHERE id=?", (job_id,)
    ).fetchone()
    con.close()
    if not row:
        print(json.dumps({"ok": False, "error": f"Job #{job_id} not found"}))
        return 1
    print(json.dumps({"ok": True, "status": row[0], "result": row[1], "error": row[2]}))
    return 0


def watch(args):
    job_id = int(args[0])
    timeout = int(args[1]) if len(args) > 1 else 600  # default 10 min
    terminal_states = {"done", "failed", "aborted"}
    started = time.time()

    con = _db()
    while time.time() - started < timeout:
        row = con.execute(
            "SELECT status FROM ho_jobs WHERE id=?", (job_id,)
        ).fetchone()
        if not row:
            print(json.dumps({"ok": False, "error": f"Job #{job_id} not found"}))
            return 1
        status_val = row[0]
        if status_val in terminal_states:
            row2 = con.execute(
                "SELECT status, result_summary, error FROM ho_jobs WHERE id=?", (job_id,)
            ).fetchone()
            con.close()
            print(json.dumps({
                "ok": True, "status": row2[0],
                "result": row2[1], "error": row2[2],
                "elapsed": round(time.time() - started),
            }))
            return 0
        time.sleep(5)
    con.close()
    print(json.dumps({
        "ok": False, "error": f"Timeout after {timeout}s. Current status: {status_val}"
    }))
    return 1


COMMANDS = {
    "enqueue": enqueue,
    "status": status,
    "result": result,
    "watch": watch,
}

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        print(f"Usage: {sys.argv[0]} {{{ '|'.join(COMMANDS) }}} ...", file=sys.stderr)
        sys.exit(1)
    cmd = sys.argv[1]
    sys.exit(COMMANDS[cmd](sys.argv[2:]))
