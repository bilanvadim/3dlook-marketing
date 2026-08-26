#!/usr/bin/env python3
"""mvb-verify-job.py — did a finished job actually produce anything?

WHY
---
A conductor job is marked `done` when its SDK session ends cleanly. Nothing looks
at whether the session DID anything, and the summary is written by the same model
that failed, so it reads like progress either way. Twice now that has banked a
job with zero output:

  job 94 (2026-08-25) — 50s, "запустил orchestrator в фоне", no files
  job 98 (2026-08-26) — 29s, same sentence, and the spawned agent made zero tool
                        calls before dying with the session

Both were reported to Vadim as ✅ done. The prompt has been hardened twice; this
is the check that does not depend on the model cooperating.

WHAT IT MEASURES
Files under <work_dir>/workspace/ whose mtime falls inside the job's run window.
That is deliberately generic — no per-track table of expected artifacts to keep in
sync with the pipelines, and it answers the only question that matters: did this
run leave anything behind?

A legitimate zero exists: a Phase 0 gate that correctly stops ("this topic is a
refresh, not a new article") returns a recommendation and writes nothing. So the
verdict is graded rather than binary — duration and the summary's own wording
separate "stopped on purpose" from "closed having done nothing".

USAGE
    mvb-verify-job.py <job_id> [--quiet]
Exit: 0 produced artifacts · 1 suspicious (zero artifacts) · 2 job not found.
"""
from __future__ import annotations

import os
import sqlite3
import sys
import time

HO_DB = os.environ.get("HO_DB") or os.path.expanduser("~/.hermes/ho.db")
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv"}
# Phrases a run uses when it hands work off and stops. Their presence next to a
# zero-artifact result is what turns "maybe it legitimately stopped" into a bug.
HANDOFF = ("в фоне", "фоново", "background", "async agent launched",
           "жду завершения", "жду результат", "запустил", "launched successfully")


def parse(ts):
    if not ts:
        return None
    for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S"):
        try:
            return time.mktime(time.strptime(ts[:19], fmt))
        except ValueError:
            continue
    return None


def main(argv=None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    quiet = "--quiet" in args
    ids = [a for a in args if not a.startswith("-")]
    if not ids:
        print("usage: mvb-verify-job.py <job_id>")
        return 2
    if not os.path.exists(HO_DB):
        print(f"нет очереди {HO_DB}")
        return 2
    c = sqlite3.connect(HO_DB, timeout=10)
    c.row_factory = sqlite3.Row
    j = c.execute("select * from ho_jobs where id=?", (int(ids[0]),)).fetchone()
    if not j:
        print(f"job #{ids[0]} не найден")
        return 2

    # Window starts at created_at, NOT claimed_at. The conductor re-claims on every
    # resume, so claimed_at is the LAST claim: for job 95, which ran 2.5h across
    # eight resumes, claimed_at..finished_at is four seconds and every artifact it
    # wrote falls outside it. Measuring the whole lifetime is the only way to ask
    # "did this job leave anything behind" without lying about a resumed run.
    start = parse(j["created_at"])
    end = parse(j["finished_at"]) or time.time()
    last = parse(j["claimed_at"])
    if start is None:
        print(f"job #{j['id']}: нет created_at — судить не о чем")
        return 1
    # A file written in the last seconds before the row was updated can carry an
    # mtime a hair outside the window; a small margin costs nothing and avoids a
    # false alarm on a real artifact.
    lo, hi = start - 5, end + 30
    root = os.path.join(j["work_dir"], "workspace")

    touched = []
    for dirpath, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for fn in files:
            p = os.path.join(dirpath, fn)
            try:
                m = os.path.getmtime(p)
            except OSError:
                continue
            if lo <= m <= hi:
                touched.append(os.path.relpath(p, j["work_dir"]))

    dur = int(end - start)                      # whole lifetime, queue time included
    session = int(end - last) if last else dur  # just the final session
    summary = (j["result_summary"] or "").lower()
    handoff = any(h in summary for h in HANDOFF)

    if touched:
        if not quiet:
            print(f"✅ job #{j['id']}: {len(touched)} файл(ов) (жизнь {dur}s, последняя сессия {session}s)")
            for t in sorted(touched)[:8]:
                print(f"     {t}")
            if len(touched) > 8:
                print(f"     … ещё {len(touched)-8}")
        return 0

    # Zero artifacts. Say how confident we are, and why.
    if handoff:
        why = ("резюме говорит о передаче работы («в фоне» / «async agent launched» / "
               "«жду завершения») — это шаблон job 94 и 98: сессия закрылась, "
               "субагент умер вместе с ней")
    elif dur < 120:
        why = f"job прожил {dur}s — слишком коротко для реальной работы"
    else:
        why = ("возможно, это законная остановка на гейте (Phase 0 сказал refresh / "
               "section-first) — тогда рекомендация должна быть в резюме")
    print(f"⚠️ job #{j['id']} [{j['status']}] закрылся без единого артефакта "
          f"(жизнь {dur}s, последняя сессия {session}s).")
    print(f"   {why}")
    print(f"   📂 искал в {root}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
