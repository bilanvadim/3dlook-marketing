#!/usr/bin/env python3
"""outbound-responses-daily.py — closely.io replies: commit them, classify them, report them.

WHY THIS EXISTS
---------------
`closely-pull.py pull-all` has pulled every campaign's replies into `responses-raw.csv`
nightly since the cron fix of 2026-09-18, and then nothing happened to them. Four replies
from 7-9 September sat in two files for three nights: uncommitted (the files showed as
modified in every `git status`, where they risked being swept into an unrelated commit),
unclassified (`responses-classified.csv` still had the 09-03 rows), and unseen by Vadim.
A pull nobody reads is the same failure as the export that never arrived: steps 8-9 still
did not run. Vadim, 2026-09-21: every morning a Telegram report with the new replies, the
campaign, the sending account and the classifier's verdict, all of it automatic.

WHAT IT DOES
------------
    night    runs right after `closely-pull.py pull-all`, on the same cron line (23:30 UTC).
             1. Commits and pushes the campaigns' response files, and only those files.
             2. For each campaign with replies missing from `responses-classified.csv`,
                runs the `check-responses` gate and enqueues `/outbound responses <slug>`
                as a conductor job through mvb-run.py, which is the one sanctioned way in.
    morning  06:00 UTC = 09:00 Kyiv in summer.
             1. Commits and pushes the classifier's output, but only files that pass
                `check-classified` and belong to no job still running.
             2. Sends the report to Telegram: new replies by campaign and sending account,
                each with the classifier's category and summary, or the reason it has
                none yet. A morning with no replies still gets a one-line message, because
                a silent cron is how the pull was lost for sixteen nights in September.
    status   read-only: what is pending, what is dirty, and what the state file remembers.
    weekly   Mondays 06:10 UTC. The full funnel per campaign and per sending account
             (invites, accepted, messages, replied, positive replies, last 7 days) from the
             snapshot `closely-pull.py pull-all --stats` writes each night into
             ~/.hermes/outbound-stats/. Read-only, no Closely session. Since 2026-10-23.

WHAT COUNTS AS NEW
------------------
A reply is its campaign + person (linkedin_url, else person_id, else name) + response_date.
`~/.hermes/.outbound-responses-state.json` keeps the replies already reported. A reply is
marked reported only once it has been reported WITH a classification. An unclassified
reply stays in every morning report until the classifier catches up, so a failed job
cannot make a reply disappear. The first run takes as its baseline every reply that is
already classified, since those were reviewed by hand on 2026-09-02/03.

GUARDRAILS
----------
  * Git: commits only `responses-raw.csv`, `responses-classified.csv` and
    `responses-summary.md` under workspace/outbound/campaigns/, via `git commit -- <paths>`,
    so anything else staged or modified is left alone. It commits only on `main`, never
    during a merge or rebase, never while index.lock exists, and never force-pushes. A failed
    push leaves the commit local and says so in the report. The next run pushes it.
    Vadim decided on 2026-09-12 that response exports stay tracked (marketing_vb/.gitignore).
  * Classifier: at most one job per campaign per distinct set of unclassified replies. If a
    finished job left the same replies unclassified, it is NOT re-enqueued every night, which
    would burn quota. The morning report flags it instead.
  * One run at a time (flock). --dry-run changes nothing: no commit, no job, no message and
    no state written.

USAGE
    scripts/outbound-responses-daily.py night   [--dry-run]
    scripts/outbound-responses-daily.py morning [--notify] [--dry-run]
    scripts/outbound-responses-daily.py status
    scripts/outbound-responses-daily.py weekly  [--notify]
Without --notify, `morning` and `weekly` print the report instead of sending it. Env for tests:
HO_DB, OUTBOUND_DAILY_STATE, OUTBOUND_DAILY_LOCK, OUTBOUND_DAILY_MVB_RUN.
Exit codes: 0 = ok · 1 = something needs attention (it is in the output) · 3 = broken setup.
"""
from __future__ import annotations

import argparse
import csv
import fcntl
import hashlib
import importlib.util
import json
import os
import re
import sqlite3
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
MVB = HERE.parent                                     # .../marketing_vb
ROOT = MVB.parent                                     # the git toplevel
CAMPAIGNS = MVB / "workspace" / "outbound" / "campaigns"
PIPE = HERE / "outbound-pipeline.py"
MVB_RUN = Path(os.environ.get("OUTBOUND_DAILY_MVB_RUN")
               or ROOT / "hermes_agent" / "ops" / "mvb-run.py")
HO_DB = os.environ.get("HO_DB") or os.path.expanduser("~/.hermes/ho.db")
STATE = Path(os.environ.get("OUTBOUND_DAILY_STATE")
             or os.path.expanduser("~/.hermes/.outbound-responses-state.json"))
LOCK = Path(os.environ.get("OUTBOUND_DAILY_LOCK")
            or os.path.expanduser("~/.hermes/.outbound-responses.lock"))
BRANCH = "main"
RAW, CLASSIFIED, SUMMARY = "responses-raw.csv", "responses-classified.csv", "responses-summary.md"
TERMINAL = ("done", "failed", "aborted", "escalated")
TG_LIMIT = 3800                                       # Telegram caps a message at 4096

PROFILE_NAMES = {"katerina": "Katerina Galich", "nick": "Nick Omelchak",
                 "olena": "Olena Kudryavtseva", "katya": "Kateryna Boichuk",
                 "vadim": "Vadim Bilan"}
CATEGORY_UA = {
    "interested": "🔥 зацікавлений", "maybe-later": "⏳ пізніше", "referral": "↪️ переадресував",
    "decline": "✖️ відмова", "negative": "⛔ негатив", "question": "❓ питання",
    "out-of-office": "🏖 OOO", "other/unclear": "❔ неясно",
}


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# outbound-pipeline.py owns telegram_send() and loads outbound-registry.py (profiles,
# LinkedIn URL normalisation). Imported, not copied, so the rules cannot drift.
OP = _load("outbound_pipeline", PIPE)
REG = OP.REG


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


# ----------------------------------------------------------------------- replies

def read_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def person_of(row: dict) -> str:
    li = (row.get("linkedin_url") or "").strip()
    if li:
        return "li:" + REG.norm_linkedin(li)
    pid = (row.get("person_id") or "").strip()
    if pid:
        return "id:" + pid
    return "name:" + (row.get("full_name") or "").strip().lower()


def reply_key(row: dict) -> str:
    return f"{person_of(row)}|{(row.get('response_date') or '').strip()}"


def campaigns() -> list[Path]:
    return sorted(p for p in CAMPAIGNS.iterdir()
                  if p.is_dir() and not p.name.startswith("_") and (p / RAW).exists())


def campaign_profile(cdir: Path, rows: list[dict]) -> str:
    """Sending account: the export's own column if Closely ever fills it, then the
    hypothesis frontmatter, then the market in the slug (outbound-registry rules)."""
    accts = {(r.get("sending_account") or "").strip() for r in rows} - {""}
    if len(accts) == 1:
        return accts.pop()
    h = cdir / "hypothesis.md"
    if h.exists():
        m = re.search(r"^profile:\s*([a-z]+)", h.read_text(encoding="utf-8", errors="replace"), re.M)
        if m:
            return m.group(1)
    return REG.infer_profile(cdir.name) or "?"


def account_label(profile: str) -> str:
    name = PROFILE_NAMES.get(profile)
    return f"{name} ({profile})" if name else profile


class Classified:
    """Look up the classifier's row for a raw reply. The classifier writes its own CSV,
    so the join degrades on purpose: exact person+date, then person+day, then the name
    when that person has only one classified row."""

    def __init__(self, rows: list[dict]):
        self.exact: dict[tuple, dict] = {}
        self.day: dict[tuple, list] = {}
        self.by_name: dict[str, list] = {}
        for r in rows:
            date = (r.get("response_date") or "").strip()
            for p in self._persons(r):
                self.exact.setdefault((p, date), r)
                self.day.setdefault((p, date[:10]), []).append(r)
            self.by_name.setdefault((r.get("full_name") or "").strip().lower(), []).append(r)

    @staticmethod
    def _persons(r: dict) -> list[str]:
        out = []
        li = (r.get("linkedin_url") or "").strip()
        if li:
            out.append("li:" + REG.norm_linkedin(li))
        pid = (r.get("person_id") or "").strip()
        if pid:
            # A campaign without person_id puts linkedin_url in that column (agent rule 4).
            out.append(("li:" + REG.norm_linkedin(pid)) if "linkedin.com" in pid else "id:" + pid)
        name = (r.get("full_name") or "").strip().lower()
        if name:
            out.append("name:" + name)
        return out

    def find(self, raw: dict) -> dict | None:
        date = (raw.get("response_date") or "").strip()
        persons = self._persons(raw)
        for p in persons:
            if (p, date) in self.exact:
                return self.exact[(p, date)]
        for p in persons:
            hits = self.day.get((p, date[:10]), [])
            if len(hits) == 1:
                return hits[0]
        hits = self.by_name.get((raw.get("full_name") or "").strip().lower(), [])
        return hits[0] if len(hits) == 1 else None


def survey() -> list[dict]:
    """One dict per campaign: raw rows, classifier lookup, unclassified rows, profile."""
    out = []
    for cdir in campaigns():
        raw = read_csv(cdir / RAW)
        cl = Classified(read_csv(cdir / CLASSIFIED))
        unclassified = [r for r in raw if cl.find(r) is None]
        out.append({"slug": cdir.name, "dir": cdir, "raw": raw, "cl": cl,
                    "unclassified": unclassified,
                    "profile": campaign_profile(cdir, raw)})
    return out


def fingerprint(rows: list[dict]) -> str:
    return hashlib.sha1("\n".join(sorted(reply_key(r) for r in rows)).encode()).hexdigest()[:16]


# ------------------------------------------------------------------------- state

def load_state() -> dict | None:
    try:
        return json.loads(STATE.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return None
    except (OSError, ValueError) as e:
        sys.exit(f"✗ state file {STATE} unreadable ({e}) — fix or remove it; "
                 "removing it re-baselines on the classified replies")


def baseline(camps: list[dict]) -> dict:
    """First run: every reply that is already classified counts as reported."""
    return {"version": 1, "created": now_utc().isoformat(timespec="seconds"),
            "reported": {c["slug"]: sorted(reply_key(r) for r in c["raw"]
                                           if c["cl"].find(r) is not None)
                         for c in camps},
            "jobs": {}}


def save_state(st: dict) -> None:
    tmp = STATE.with_suffix(".tmp")
    tmp.write_text(json.dumps(st, ensure_ascii=False, indent=1), encoding="utf-8")
    os.replace(tmp, STATE)


# --------------------------------------------------------------------------- git

def git(*args: str, timeout: int = 120) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(ROOT), *args],
                          capture_output=True, text=True, timeout=timeout)


def git_blocker() -> str | None:
    """Why committing now would be unsafe, or None."""
    br = git("rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
    if br != BRANCH:
        return f"гілка `{br}`, а не `{BRANCH}`"
    gd = Path(git("rev-parse", "--absolute-git-dir").stdout.strip())
    for marker in ("MERGE_HEAD", "rebase-merge", "rebase-apply", "CHERRY_PICK_HEAD"):
        if (gd / marker).exists():
            return f"незавершений {marker}"
    if (gd / "index.lock").exists():
        return "index.lock — зараз працює інша git-операція"
    return None


def dirty_response_files(names: tuple[str, ...]) -> list[str]:
    """Modified or untracked response files, as paths relative to ROOT."""
    rel = CAMPAIGNS.relative_to(ROOT)
    specs = [f"{rel}/*/{n}" for n in names]
    out = git("status", "--porcelain=v1", "-z", "--untracked-files=all", "--", *specs).stdout
    paths, parts, i = [], out.split("\0"), 0
    while i < len(parts):
        entry = parts[i]
        i += 1
        if len(entry) < 4:
            continue
        xy, path = entry[:2], entry[3:]
        if "R" in xy or "C" in xy:
            i += 1                                    # the rename's source path follows
        if "D" in xy:
            continue                                  # never commit a deletion unattended
        paths.append(path)
    return sorted(set(paths))


def commit_and_push(paths: list[str], subject: str, body: str, dry: bool) -> tuple[bool, str]:
    if not paths:
        return True, "нічого комітити"
    if dry:
        return True, f"[dry-run] закомітив би {len(paths)} файл(и): {subject}"
    why = git_blocker()
    if why:
        return False, f"не комічу: {why}"
    r = git("add", "--", *paths)
    if r.returncode:
        return False, f"git add: {r.stderr.strip()[:200]}"
    r = git("commit", "-q", "-m", subject, "-m", body, "--", *paths)
    if r.returncode:
        return False, f"git commit: {(r.stderr or r.stdout).strip()[:200]}"
    sha = git("rev-parse", "--short", "HEAD").stdout.strip()
    return push(f"коміт {sha}")


OWN_SUBJECT = "outbound: replies "                   # every commit this script makes


def foreign_unpushed() -> list[str]:
    """Unpushed commits on main that this script did not make. Pushing them would publish
    someone's work that may be local on purpose, so their presence holds our push back."""
    r = git("log", "--format=%h %s", f"origin/{BRANCH}..{BRANCH}")
    return [l for l in r.stdout.splitlines() if l and not l.split(" ", 1)[1].startswith(OWN_SUBJECT)]


def push(what: str) -> tuple[bool, str]:
    foreign = foreign_unpushed()
    if foreign:
        n = len(foreign)
        return False, (f"{what} лишився локально: на {BRANCH} є {n} "
                       f"{plural(n, 'чужий невідправлений коміт', 'чужі невідправлені коміти', 'чужих невідправлених комітів')}"
                       f" ({foreign[0][:60]}…) — push відкладено, "
                       "щоб не опублікувати їх разом із моїм")
    try:
        r = git("push", "-q", "origin", BRANCH, timeout=120)
    except subprocess.TimeoutExpired:
        return False, f"{what} лишився локально: push завис (timeout)"
    if r.returncode:
        return False, f"{what} лишився локально: push не пройшов ({r.stderr.strip()[:160]})"
    return True, f"{what} → origin/{BRANCH}"


def unpushed() -> int:
    r = git("rev-list", "--count", f"origin/{BRANCH}..{BRANCH}")
    return int(r.stdout.strip() or 0) if r.returncode == 0 else 0


def new_vs_head(path: Path) -> int:
    """Rows in the working file that the committed version does not have."""
    rel = path.relative_to(ROOT).as_posix()
    r = git("show", f"HEAD:{rel}")
    old = set()
    if r.returncode == 0:
        old = {reply_key(x) for x in csv.DictReader(r.stdout.splitlines(keepends=True))}
    return sum(1 for x in read_csv(path) if reply_key(x) not in old)


def gate(sub: str, slug: str) -> tuple[int, str]:
    r = subprocess.run([sys.executable, str(PIPE), sub, "--campaign", slug],
                       capture_output=True, text=True, timeout=120)
    tail = (r.stdout + r.stderr).strip().splitlines()
    return r.returncode, (tail[-1] if tail else "")


# ------------------------------------------------------------------------- jobs

def job_row(job_id) -> dict | None:
    if not job_id or not os.path.exists(HO_DB):
        return None
    try:
        con = sqlite3.connect(f"file:{HO_DB}?mode=ro", uri=True, timeout=10)
        con.row_factory = sqlite3.Row
        row = con.execute("select id, status, finished_at, result_summary, error "
                          "from ho_jobs where id=?", (int(job_id),)).fetchone()
        con.close()
        return dict(row) if row else None
    except sqlite3.Error:
        return None


def enqueue(slug: str) -> tuple[int | None, str]:
    """(job_id, message). mvb-run refuses a duplicate of a live job and names it."""
    env = dict(os.environ, HO_DB=HO_DB)
    r = subprocess.run([sys.executable, str(MVB_RUN), "outbound", f"responses {slug}"],
                       capture_output=True, text=True, timeout=120, env=env)
    out = (r.stdout + r.stderr).strip()
    m = re.search(r"job #(\d+)", out)
    if r.returncode == 0 and m:
        return int(m.group(1)), f"job #{m.group(1)} поставлено"
    if r.returncode == 2 and m:
        return int(m.group(1)), f"job #{m.group(1)} уже в роботі"
    return None, f"mvb-run exit {r.returncode}: {out.splitlines()[-1] if out else '—'}"


# ------------------------------------------------------------------------ night

def cmd_night(args) -> int:
    camps = survey()
    st = load_state() or baseline(camps)
    problems = 0
    print(f"{now_utc():%Y-%m-%d %H:%M} UTC · night · {len(camps)} campaign(s) with replies")

    # 1. the pull's output, committed and pushed
    raws = dirty_response_files((RAW,))
    counts = {Path(p).parent.name: new_vs_head(ROOT / p) for p in raws}
    added = {k: v for k, v in counts.items() if v}
    subject = ("outbound: replies pulled — " +
               ", ".join(f"{k} +{v}" for k, v in added.items())) if added \
        else "outbound: replies re-pulled, no new rows"
    ok, msg = commit_and_push(
        raws, subject[:120],
        "Automated: scripts/outbound-responses-daily.py night, after closely-pull pull-all.\n"
        f"Files: {', '.join(raws)}", args.dry_run)
    print(f"  git: {msg}")
    problems += not ok
    if ok and not raws and unpushed() and not args.dry_run:
        ok2, msg2 = push("локальні коміти")
        print(f"  git: {msg2}")
        problems += not ok2

    # 2. classification for whatever is not classified yet
    for c in camps:
        todo = c["unclassified"]
        if not todo:
            continue
        slug, fp = c["slug"], fingerprint(todo)
        prev = st["jobs"].get(slug, {})
        prev_job = job_row(prev.get("job_id"))
        if prev_job and prev_job["status"] not in TERMINAL:
            print(f"  {slug}: {len(todo)} unclassified, job #{prev_job['id']} still "
                  f"{prev_job['status']} — waiting")
            continue
        if prev.get("fingerprint") == fp and prev_job:
            print(f"  {slug}: {len(todo)} unclassified, the same set job #{prev_job['id']} "
                  f"({prev_job['status']}) already had — NOT re-enqueuing, flagged for morning")
            prev["stuck"] = True
            problems += 1
            continue
        rc, last = gate("check-responses", slug)
        if rc != 0:
            print(f"  {slug}: check-responses exit {rc} — {last}")
            st["jobs"][slug] = {"gate_failed": last, "fingerprint": fp,
                                "at": now_utc().isoformat(timespec="seconds")}
            problems += 1
            continue
        if args.dry_run:
            print(f"  {slug}: {len(todo)} unclassified → [dry-run] would enqueue "
                  f"/outbound responses {slug}")
            continue
        jid, msg = enqueue(slug)
        print(f"  {slug}: {len(todo)} unclassified → {msg}")
        if jid is None:
            problems += 1
            st["jobs"][slug] = {"enqueue_failed": msg, "fingerprint": fp,
                                "at": now_utc().isoformat(timespec="seconds")}
        else:
            st["jobs"][slug] = {"job_id": jid, "fingerprint": fp,
                                "at": now_utc().isoformat(timespec="seconds")}

    st["last_night"] = now_utc().isoformat(timespec="seconds")
    if not args.dry_run:
        save_state(st)
    return 0 if problems == 0 else 1


# ---------------------------------------------------------------------- morning

def short(text: str, n: int = 280) -> str:
    t = re.sub(r"\s*\n\s*", " / ", (text or "").strip())
    t = re.sub(r"(?: / )+", " / ", t)
    return t if len(t) <= n else t[:n - 1].rstrip() + "…"


def plural(n: int, one: str, few: str, many: str) -> str:
    if n % 10 == 1 and n % 100 != 11:
        return one
    if 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14:
        return few
    return many


def fmt_date(iso: str) -> str:
    try:
        return datetime.fromisoformat(iso).strftime("%d.%m")
    except ValueError:
        return iso[:10]


def job_line(info: dict) -> str:
    if info.get("gate_failed"):
        return f"класифікатор не запускався: check-responses — {info['gate_failed']}"
    if info.get("enqueue_failed"):
        return f"класифікатор не поставився: {info['enqueue_failed']}"
    row = job_row(info.get("job_id"))
    if not row:
        return "класифікатор не запускався"
    s = f"класифікатор job #{row['id']}: {row['status']}"
    if info.get("stuck"):
        s += " — завершився, але ці відповіді лишились некласифікованими; повторно не ставлю"
    elif row["status"] in ("failed", "aborted", "escalated") and row.get("error"):
        s += f" ({short(row['error'], 120)})"
    return s


def cmd_morning(args) -> int:
    camps = survey()
    st = load_state() or baseline(camps)
    problems = 0
    day = now_utc().strftime("%d.%m")

    # 1. the classifier's output, committed if it is well-formed and finished
    commit_notes: list[str] = []
    ready: list[str] = []
    for p in dirty_response_files((CLASSIFIED, SUMMARY)):
        slug = Path(p).parent.name
        info = st["jobs"].get(slug, {})
        row = job_row(info.get("job_id"))
        if row and row["status"] not in TERMINAL:
            note = f"{slug}: job #{row['id']} ще {row['status']} — поки не комічу"
            if note not in commit_notes:
                commit_notes.append(note)
            continue
        if p.endswith(CLASSIFIED):
            rc, last = gate("check-classified", slug)
            if rc != 0:
                commit_notes.append(f"{slug}: check-classified exit {rc} ({last}) — не комічу")
                problems += 1
                continue
        ready.append(p)
    ready += dirty_response_files((RAW,))            # a night commit that did not happen
    ready = sorted(set(ready))
    if ready:
        slugs = sorted({Path(p).parent.name for p in ready})
        ok, msg = commit_and_push(
            ready, ("outbound: replies classified — " + ", ".join(slugs))[:120],
            "Automated: scripts/outbound-responses-daily.py morning. "
            "check-classified passed on every responses-classified.csv in this commit.\n"
            f"Files: {', '.join(ready)}", args.dry_run)
        commit_notes.append(msg)
        problems += not ok
    elif unpushed() and not args.dry_run:
        ok, msg = push("локальні коміти")
        commit_notes.append(msg)
        problems += not ok

    # 2. the report
    reported = {k: set(v) for k, v in st.get("reported", {}).items()}
    sections, hot, total, n_camps = [], [], 0, 0
    mark: dict[str, set] = {}
    for c in camps:
        slug = c["slug"]
        new = [r for r in c["raw"] if reply_key(r) not in reported.get(slug, set())]
        if not new:
            continue
        n_camps += 1
        total += len(new)
        new.sort(key=lambda r: r.get("response_date") or "")
        lines = [f"📂 {slug}", f"Акаунт: {account_label(c['profile'])}"]
        pending = 0
        for r in new:
            hit = c["cl"].find(r)
            who = r.get("full_name") or "?"
            co = (hit or {}).get("company") or r.get("company_name") or ""
            msgno = r.get("which_message_replied_to") or "?"
            lines.append(f"• {who}{' — ' + co if co else ''} · {fmt_date(r.get('response_date', ''))}"
                         f", відповідь на повідомлення {msgno}")
            lines.append(f"  «{short(r.get('response_text', ''))}»")
            if hit:
                cat = (hit.get("category") or "").strip()
                label = CATEGORY_UA.get(cat, cat or "?")
                lines.append(f"  → {label} ({hit.get('confidence') or '?'}): "
                             f"{short(hit.get('summary', ''), 220)}")
                act = (hit.get("extracted_action") or "").strip()
                if cat in ("interested", "question", "referral") and act:
                    lines.append(f"  ▸ {short(act, 200)}")
                if cat in ("interested", "question", "referral"):
                    hot.append(f"{CATEGORY_UA.get(cat, cat)}: {who} ({slug})")
                mark.setdefault(slug, set()).add(reply_key(r))
            else:
                pending += 1
                lines.append("  → ще не класифіковано")
        if pending:
            lines.append(job_line(st["jobs"].get(slug, {})))
            problems += 1
        sections.append("\n".join(lines))

    freshest = max(((c["dir"] / RAW).stat().st_mtime for c in camps), default=0)
    age_h = (now_utc().timestamp() - freshest) / 3600 if freshest else 1e9
    pull_note = (f"closely-pull востаннє оновив файли відповідей о "
                 f"{datetime.fromtimestamp(freshest, timezone.utc):%d.%m %H:%M} UTC"
                 if age_h < 20 else
                 f"⚠️ closely-pull не оновлював файли вже {age_h:.0f} год — "
                 "дивись ~/.hermes/logs/closely-pull.log")
    if age_h >= 20:
        problems += 1

    if total:
        head = [f"📬 Outbound, {day}: {total} {plural(total, 'нова відповідь', 'нові відповіді', 'нових відповідей')}"
                f" у {n_camps} {plural(n_camps, 'кампанії', 'кампаніях', 'кампаніях')}"]
        if hot:
            head.append("Потребують реакції: " + "; ".join(hot))
        blocks = ["\n".join(head)] + sections
        tail = [pull_note] + commit_notes
        blocks.append("\n".join(tail))
        blocks.append("Чернетки відповідей і повний розбір: responses-summary.md у папці кампанії.")
    else:
        blocks = [f"📬 Outbound, {day}: нових відповідей немає. {pull_note}."
                  + ("\n" + "\n".join(commit_notes) if commit_notes else "")]

    messages = chunk(blocks)
    for m in messages:
        print(m)
        print("-" * 40)
    sent = True
    if args.notify and not args.dry_run:
        for m in messages:
            sent = OP.telegram_send(m) and sent
        if not sent:
            problems += 1
            print("✗ Telegram send failed — nothing marked as reported, tomorrow repeats it")
    # Reported = seen by Vadim. A printed dry look (no --notify) marks nothing.
    if args.notify and sent and not args.dry_run:
        for slug, keys in mark.items():
            st.setdefault("reported", {}).setdefault(slug, [])
            st["reported"][slug] = sorted(set(st["reported"][slug]) | keys)
    if not args.dry_run:
        st["last_morning"] = now_utc().isoformat(timespec="seconds")
        save_state(st)
    return 0 if problems == 0 else 1


def chunk(blocks: list[str]) -> list[str]:
    out, cur = [], ""
    for b in blocks:
        while len(b) > TG_LIMIT:                      # a single oversized section
            out.append(b[:TG_LIMIT])
            b = b[TG_LIMIT:]
        if cur and len(cur) + 2 + len(b) > TG_LIMIT:
            out.append(cur)
            cur = b
        else:
            cur = f"{cur}\n\n{b}" if cur else b
    if cur:
        out.append(cur)
    return out


# ------------------------------------------------------------------------ weekly

# Vadim, 2026-10-23: full stats on every outreach campaign, collected at night with the
# replies. `closely-pull.py pull-all --stats` writes the snapshot (lifetime + last 7 days
# per Closely campaign); this only reads it, so it never opens a Closely session.
STATS_DIR = Path(os.environ.get("OUTBOUND_STATS_DIR")
                 or os.path.expanduser("~/.hermes/outbound-stats"))
POSITIVE = ("interested", "question", "referral")    # the morning report's "needs a reaction"
PROFILE_ORDER = ("katerina", "nick", "olena", "katya", "vadim")


def _sum(rows: list[dict], part: str, key: str):
    vals = [(r.get(part) or {}).get(key) for r in rows]
    vals = [v for v in vals if isinstance(v, (int, float))]
    return sum(vals) if vals else None


def _n(v) -> str:
    return "?" if v is None else f"{v:,}".replace(",", " ")


def _pct(a, b) -> str:
    return f" ({100 * a / b:.1f}%)" if a is not None and b else ""


def positives(cdir: Path) -> int:
    """People with at least one reply the classifier put in POSITIVE."""
    return len({person_of(r) for r in read_csv(cdir / CLASSIFIED)
                if (r.get("category") or "").strip() in POSITIVE})


def stat_units(rows: list[dict]) -> list[dict]:
    """One unit per folder (summing its Closely campaigns), else per Closely campaign.
    A campaign with no folder gets its sender from the account_id its mapped siblings use."""
    acct_profile: dict = {}
    for r in rows:
        if r.get("folder") and r.get("account_id") is not None:
            acct_profile.setdefault(r["account_id"],
                                    campaign_profile(CAMPAIGNS / r["folder"], []))
    groups: dict[str, list[dict]] = {}
    for r in rows:
        groups.setdefault(r.get("folder") or "closely:" + r["closely_id"], []).append(r)
    units = []
    for rs in groups.values():
        folder = rs[0].get("folder") or ""
        prof = (campaign_profile(CAMPAIGNS / folder, []) if folder
                else acct_profile.get(rs[0].get("account_id")))
        units.append({"folder": folder, "rows": rs,
                      "profile": prof or f"Closely account {rs[0].get('account_id', '?')}",
                      "date": folder[:10] if folder else min(r["created_at"] for r in rs),
                      "positives": positives(CAMPAIGNS / folder) if folder else None})
    return units


def funnel(rows: list[dict]) -> dict:
    replied = _sum(rows, "contacts", "finished_reply")
    return {"contacts": _sum(rows, "contacts", "total"),
            "active": _sum(rows, "contacts", "active"),
            "sent": _sum(rows, "lifetime", "connection_sent"),
            "acc": _sum(rows, "lifetime", "connection_accepted"),
            "msg": _sum(rows, "lifetime", "message_sent"),
            "replied": replied if replied is not None
            else _sum(rows, "lifetime", "message_replied"),
            "w_sent": _sum(rows, "last7", "connection_sent"),
            "w_acc": _sum(rows, "last7", "connection_accepted"),
            "w_replied": _sum(rows, "last7", "message_replied")}


def week_line(f: dict) -> str:
    return (f"7 днів: +{_n(f['w_sent'])} інвайтів, +{_n(f['w_acc'])} прийняли, "
            f"+{_n(f['w_replied'])} відповідей")


def cmd_weekly(args) -> int:
    snaps = sorted(STATS_DIR.glob("????-??-??.json"))
    if not snaps:
        msg = (f"📊 Outbound: знімка статистики немає в {STATS_DIR}. Його пише нічний "
               "`closely-pull.py pull-all --stats`; дивись ~/.hermes/logs/closely-pull.log")
        print(msg)
        if args.notify:
            OP.telegram_send(msg)
        return 1
    snap = json.loads(snaps[-1].read_text(encoding="utf-8"))
    pulled = datetime.fromisoformat(snap["pulled_at"].replace("Z", "+00:00"))
    age_h = (now_utc() - pulled).total_seconds() / 3600
    rows = [r for r in snap["campaigns"] if "error" not in r]
    broken = [r for r in snap["campaigns"] if "error" in r]
    units = stat_units(rows)

    t = funnel(rows)
    pos = sum(u["positives"] or 0 for u in units)
    head = [f"📊 Outbound — повна статистика, {now_utc():%d.%m}",
            f"Closely на {pulled:%d.%m %H:%M} UTC · {len(units)} "
            f"{plural(len(units), 'кампанія', 'кампанії', 'кампаній')} з {fmt_date(snap['since'])}",
            "",
            f"Разом: інвайтів {_n(t['sent'])} · прийняли {_n(t['acc'])}{_pct(t['acc'], t['sent'])}"
            f" · відповіли {_n(t['replied'])}{_pct(t['replied'], t['acc'])}"
            f" · позитивних {pos}",
            week_line(t)]
    if age_h > 30:
        head.append(f"⚠️ знімок старий ({age_h:.0f} год): нічний pull не дописав статистику, "
                    "дивись ~/.hermes/logs/closely-pull.log")
    blocks = ["\n".join(head)]

    by_prof: dict[str, list[dict]] = {}
    for u in units:
        by_prof.setdefault(u["profile"], []).append(u)
    order = sorted(by_prof, key=lambda p: (PROFILE_ORDER.index(p) if p in PROFILE_ORDER
                                           else len(PROFILE_ORDER), p))
    for prof in order:
        us = sorted(by_prof[prof], key=lambda u: u["date"], reverse=True)
        pf = funnel([r for u in us for r in u["rows"]])
        lines = [f"👤 {account_label(prof)} — інвайтів {_n(pf['sent'])}, прийняли "
                 f"{_n(pf['acc'])}{_pct(pf['acc'], pf['sent'])}, відповіли "
                 f"{_n(pf['replied'])}{_pct(pf['replied'], pf['acc'])}"]
        for u in us:
            f = funnel(u["rows"])
            title = (u["folder"][11:] if u["folder"] else
                     "«" + " + ".join(r["name"] for r in u["rows"]) + "», без папки")
            status = "/".join(sorted({r.get("status") or "?" for r in u["rows"]}))
            lines.append(f"• {title} · {fmt_date(u['date'])} · {status}")
            lines.append(f"  контактів {_n(f['contacts'])} (в роботі {_n(f['active'])}) · "
                         f"інвайтів {_n(f['sent'])} · прийняли {_n(f['acc'])}{_pct(f['acc'], f['sent'])}"
                         f" · повідомлень {_n(f['msg'])} · відповіли {_n(f['replied'])}"
                         f"{_pct(f['replied'], f['acc'])}"
                         + (f" · позитивних {u['positives']}" if u["positives"] else ""))
            if any(f[k] for k in ("w_sent", "w_acc", "w_replied")):
                lines.append("  " + week_line(f))
        blocks.append("\n".join(lines))

    tail = []
    if broken:
        tail.append("⚠️ не зібрано: " + "; ".join(
            f"{r['closely_id']} «{r.get('name', '')}» ({short(r['error'], 80)})" for r in broken))
    tail.append("Відповіли = люди, яким Closely закрив послідовність відповіддю; % від "
                "прийнятих (за ним і порівнюй кампанії). Позитивні = interested, question, "
                "referral за класифікатором. «Без папки» = кампанія ще без відповідей або не з "
                "пайплайну, назва з Closely.")
    sid = load_sheet_state().get("spreadsheet_id")
    if sid:
        tail.append(f"Таблиця: {SHEET_URL.format(sid)}")
    blocks.append("\n".join(tail))

    messages = chunk(blocks)
    for m in messages:
        print(m)
        print("-" * 40)
    if args.notify and not all(OP.telegram_send(m) for m in messages):
        print("✗ Telegram send failed")
        return 1
    return 0 if not broken and age_h <= 30 else 1


# ------------------------------------------------------------------------- sheet

# Vadim, 2026-10-23: «давай в гугл шітс стату відображати по кампаніям для наглядності».
# The same snapshot as `weekly`, one row per campaign, rewritten every morning. Sheets go
# through oo, and organic-dashboard.py owns that transport (absolute URLs only, request in a
# file): imported, not copied.
SHEET_STATE = Path(os.environ.get("OUTBOUND_SHEET_STATE")
                   or os.path.expanduser("~/.hermes/.outbound-stats-sheet.json"))
SHEET_TITLE = os.environ.get("OUTBOUND_SHEET_TITLE") or "3DLOOK Outbound Stats"
SHEET_URL = "https://docs.google.com/spreadsheets/d/{}/edit"
TAB_CAMP, TAB_ACCT, TAB_HIST, TAB_ABOUT = "Кампанії", "Акаунти", "Історія", "Про таблицю"
SHEET_TABS = (TAB_CAMP, TAB_ACCT, TAB_HIST, TAB_ABOUT)
HEAD_ROWS = 3                                         # title, subtitle, blank; header below
NAVY, BLUE = "#050F40", "#143DFF"                     # DESIGN.md
_OD = None


def _od():
    global _OD
    if _OD is None:
        _OD = _load("organic_dashboard", HERE / "organic-dashboard.py")
    return _OD


def load_sheet_state() -> dict:
    try:
        return json.loads(SHEET_STATE.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def step_replies(rows: list[dict]) -> dict:
    """Replies to the invite, to Message 1 and to Message 2, from the snapshot's steps.

    The flow is a TREE: `condition` steps fork it, and every branch carries its own
    Message 1 -> Message 2 pair at a different depth. So neither list order nor depth
    ranks a message; the number of message steps on its path from the root does (1 = M1,
    2 = M2). Checked on the 09-02 payloads: AU 138392 gives invite 1 + M1 2 + M2 2 = its
    5 replies, UK 139077 gives M2 1 + 3 = its 4."""
    out = {"invite": None, "m1": None, "m2": None}
    for r in rows:
        steps = r.get("steps") or []
        ids = {s.get("id") for s in steps}
        kids: dict = {}
        for s in steps:
            kids.setdefault(s.get("prev"), []).append(s)
        stack = [(s, 0) for s in steps if s.get("prev") not in ids]
        seen: set = set()
        while stack:
            s, n_msg = stack.pop()
            if s.get("id") in seen:
                continue
            seen.add(s.get("id"))
            if s.get("type") == "message":
                n_msg += 1
            v = s.get("message_replied")
            key = ("invite" if (s.get("type") or "").startswith("connection") else
                   {1: "m1", 2: "m2"}.get(n_msg) if s.get("type") == "message" else None)
            if key and isinstance(v, (int, float)):
                out[key] = (out[key] or 0) + v
            stack += [(k, n_msg) for k in kids.get(s.get("id"), [])]
    return out


def _ratio(a, b):
    return round(a / b, 4) if isinstance(a, (int, float)) and b else ""


def _v(x):
    return "" if x is None else x


def unit_title(u: dict) -> str:
    return u["folder"][11:] if u["folder"] else " + ".join(r["name"] for r in u["rows"])


def snapshot_units(path: Path) -> tuple[dict, list[dict]]:
    snap = json.loads(path.read_text(encoding="utf-8"))
    return snap, stat_units([r for r in snap["campaigns"] if "error" not in r])


def sheet_values(snaps: list[Path]) -> dict:
    snap, units = snapshot_units(snaps[-1])
    try:
        from zoneinfo import ZoneInfo
        kyiv = datetime.fromisoformat(snap["pulled_at"].replace("Z", "+00:00")) \
            .astimezone(ZoneInfo("Europe/Kyiv"))
    except Exception:                                 # noqa: BLE001
        kyiv = datetime.fromisoformat(snap["pulled_at"].replace("Z", "+00:00"))
    sub = (f"Дані Closely на {kyiv:%d.%m.%Y %H:%M} за Києвом · оновлюється щоранку · "
           f"кампанії, створені з {fmt_date(snap['since'])}")
    broken = [r for r in snap["campaigns"] if "error" in r]
    if broken:
        sub += " · не зібрано: " + ", ".join(f"{r['closely_id']} «{r.get('name', '')}»"
                                             for r in broken)

    def order(u):
        p = u["profile"]
        return (PROFILE_ORDER.index(p) if p in PROFILE_ORDER else len(PROFILE_ORDER), p)

    camp = [["Outbound — статистика кампаній"], [sub], [],
            ["Акаунт", "Кампанія", "Назва в Closely", "Старт", "Статус", "Контактів",
             "В роботі", "Інвайтів", "Прийняли", "% прийняли", "Повідомлень", "Відповіли",
             "% відповіли (від прийнятих)", "Позитивних", "% позитивних (від прийнятих)",
             "Відповіді на інвайт", "Відповіді на M1", "Відповіді на M2",
             "7 днів: інвайтів", "7 днів: прийняли", "7 днів: відповідей", "Closely ID",
             "Папка в репо"]]
    for u in sorted(sorted(units, key=lambda u: u["date"], reverse=True), key=order):
        f, sr = funnel(u["rows"]), step_replies(u["rows"])
        camp.append([
            account_label(u["profile"]), unit_title(u),
            " + ".join(r["name"] for r in u["rows"]), u["date"],
            "/".join(sorted({r.get("status") or "?" for r in u["rows"]})),
            _v(f["contacts"]), _v(f["active"]), _v(f["sent"]), _v(f["acc"]),
            _ratio(f["acc"], f["sent"]), _v(f["msg"]), _v(f["replied"]),
            _ratio(f["replied"], f["acc"]), _v(u["positives"]),
            _ratio(u["positives"], f["acc"]) if u["positives"] is not None else "",
            _v(sr["invite"]), _v(sr["m1"]), _v(sr["m2"]),
            _v(f["w_sent"]), _v(f["w_acc"]), _v(f["w_replied"]),
            ", ".join(r["closely_id"] for r in u["rows"]), u["folder"]])

    acct = [["Outbound — підсумки по акаунтах"], [sub], [],
            ["Акаунт", "Кампаній", "Контактів", "В роботі", "Інвайтів", "Прийняли",
             "% прийняли", "Повідомлень", "Відповіли", "% відповіли (від прийнятих)",
             "Позитивних", "% позитивних (від прийнятих)", "7 днів: інвайтів",
             "7 днів: прийняли", "7 днів: відповідей"]]
    groups: dict[str, list[dict]] = {}
    for u in units:
        groups.setdefault(u["profile"], []).append(u)
    for label, us in [(account_label(p), groups[p]) for p in sorted(groups, key=lambda p: order(
            {"profile": p}))] + [("Разом", units)]:
        f = funnel([r for u in us for r in u["rows"]])
        pos = sum(u["positives"] or 0 for u in us)
        acct.append([label, len(us), _v(f["contacts"]), _v(f["active"]), _v(f["sent"]),
                     _v(f["acc"]), _ratio(f["acc"], f["sent"]), _v(f["msg"]),
                     _v(f["replied"]), _ratio(f["replied"], f["acc"]), pos,
                     _ratio(pos, f["acc"]), _v(f["w_sent"]), _v(f["w_acc"]),
                     _v(f["w_replied"])])

    hist = [["Outbound — історія знімків"], ["Один рядок на кампанію за кожну ніч. "
                                             "Числа наростаючим підсумком."], [],
            ["Дата знімка", "Акаунт", "Кампанія", "Інвайтів", "Прийняли", "Повідомлень",
             "Відповіли", "Контактів в роботі"]]
    for p in reversed(snaps):
        try:
            s, us = snapshot_units(p)
        except (OSError, ValueError, KeyError):
            continue
        for u in sorted(us, key=order):
            f = funnel(u["rows"])
            hist.append([s["pulled_at"][:10], account_label(u["profile"]), unit_title(u),
                         _v(f["sent"]), _v(f["acc"]), _v(f["msg"]), _v(f["replied"]),
                         _v(f["active"])])

    about = [["Про таблицю"], [], *[[x] for x in (
        "Джерело: закритий API closely.io, той самий, з якого щоночі тягнуться відповіді. "
        "Знімок пише closely-pull.py pull-all --stats о 23:30 UTC, таблицю переписує "
        "outbound-responses-daily.py sheet щоранку. Правки руками зітруться.",
        "Одна строка = одна кампанія. Папка в репо, розбита в Closely на кілька кампаній "
        "(батчі), сумується в одну строку.",
        "Відповіли = люди, яким Closely закрив послідовність відповіддю. % рахуються від "
        "прийнятих: за ним і порівнюй кампанії. % від повідомлень завищує незавершені кампанії, "
        "бо M2 ще не пішло.",
        "Позитивні = interested, question, referral за класифікатором "
        "(responses-classified.csv), по людях.",
        "Відповіді на інвайт / M1 / M2 = відповіді після кроку послідовності, за статистикою "
        "кроків Closely.",
        "7 днів = події за останні 7 днів до знімка.",
        "Кампанія без папки = у неї ще немає відповідей (папку знаходимо за тими, хто відповів) "
        "або вона не з пайплайну. Назва та, що в Closely; акаунт визначено за account_id.",
        "Історія: один рядок на кампанію за кожну ніч, від 2026-10-23.")]]
    return {TAB_CAMP: camp, TAB_ACCT: acct, TAB_HIST: hist, TAB_ABOUT: about}


def write_stats_sheet(values: dict, st: dict) -> tuple[str, bool]:
    od = _od()
    sid, created = st.get("spreadsheet_id"), False
    if not sid:
        sid = od.sheets("POST", "", {
            "properties": {"title": SHEET_TITLE, "locale": "uk_UA", "timeZone": "Europe/Kyiv"},
            "sheets": [{"properties": {"title": t, "index": i}}
                       for i, t in enumerate(SHEET_TABS)]})["spreadsheetId"]
        st["spreadsheet_id"], created = sid, True
        SHEET_STATE.parent.mkdir(parents=True, exist_ok=True)
        SHEET_STATE.write_text(json.dumps(st, indent=1), encoding="utf-8")
    fields = "sheets(properties(sheetId,title),conditionalFormats)"
    meta = od.sheets("GET", f"/{sid}?fields={fields}")
    have = {s["properties"]["title"] for s in meta.get("sheets", [])}
    if any(t not in have for t in SHEET_TABS):
        od.sheets("POST", f"/{sid}:batchUpdate", {"requests": [
            {"addSheet": {"properties": {"title": t}}} for t in SHEET_TABS if t not in have]})
        meta = od.sheets("GET", f"/{sid}?fields={fields}")
    tabs = {s["properties"]["title"]: s["properties"]["sheetId"] for s in meta["sheets"]}
    size = {t: (max(len(v) + 20, 60), max(max(len(r) for r in v) + 2, 10))
            for t, v in values.items()}

    reqs: list[dict] = []
    for s in meta.get("sheets", []):
        for _ in s.get("conditionalFormats") or []:
            reqs.append({"deleteConditionalFormatRule": {"sheetId": s["properties"]["sheetId"],
                                                         "index": 0}})
    for t in SHEET_TABS:
        reqs.append({"updateSheetProperties": {"properties": {
            "sheetId": tabs[t], "gridProperties": {
                "rowCount": size[t][0], "columnCount": size[t][1],
                "frozenRowCount": 0 if t == TAB_ABOUT else HEAD_ROWS + 1,
                "frozenColumnCount": 2 if t == TAB_CAMP else 1 if t != TAB_ABOUT else 0}},
            "fields": "gridProperties(rowCount,columnCount,frozenRowCount,frozenColumnCount)"}})
    od.sheets("POST", f"/{sid}:batchUpdate", {"requests": reqs})
    od.sheets("POST", f"/{sid}/values:batchClear", {"ranges": [f"'{t}'" for t in SHEET_TABS]})
    # RAW: a campaign name is text even when it starts with = or +, a number stays a number
    od.sheets("POST", f"/{sid}/values:batchUpdate", {"valueInputOption": "RAW", "data": [
        {"range": f"'{t}'!A1", "values": v} for t, v in values.items()]})

    rgb = od.rgb
    reqs = []

    def rng(sh, r0, r1, c0, c1):
        return {"sheetId": sh, "startRowIndex": r0, "endRowIndex": r1,
                "startColumnIndex": c0, "endColumnIndex": c1}

    def fmt(sh, r0, r1, c0, c1, f, flds):
        reqs.append({"repeatCell": {"range": rng(sh, r0, r1, c0, c1),
                                    "cell": {"userEnteredFormat": f}, "fields": flds}})

    def width(sh, c0, c1, px):
        reqs.append({"updateDimensionProperties": {"range": {
            "sheetId": sh, "dimension": "COLUMNS", "startIndex": c0, "endIndex": c1},
            "properties": {"pixelSize": px}, "fields": "pixelSize"}})

    font = {"fontFamily": "Arial", "fontSize": 10}
    pct_cols = {TAB_CAMP: (9, 12, 14), TAB_ACCT: (6, 9, 11)}
    for t in SHEET_TABS:
        sh, (nrows, ncols), n = tabs[t], size[t], len(values[t])
        reqs.append({"updateCells": {"range": rng(sh, 0, nrows, 0, ncols),
                                     "fields": "userEnteredFormat"}})
        fmt(sh, 0, nrows, 0, ncols, {"textFormat": font, "verticalAlignment": "MIDDLE"},
            "userEnteredFormat(textFormat,verticalAlignment)")
        fmt(sh, 0, 1, 0, 1, {"textFormat": {**font, "bold": True, "fontSize": 14,
                                             "foregroundColor": rgb(NAVY)}},
            "userEnteredFormat.textFormat")
        if t == TAB_ABOUT:
            width(sh, 0, 1, 900)
            fmt(sh, 2, n, 0, 1, {"wrapStrategy": "WRAP"}, "userEnteredFormat.wrapStrategy")
            continue
        fmt(sh, 1, 2, 0, 1, {"textFormat": {**font, "italic": True,
                                             "foregroundColor": rgb("#6B7280")}},
            "userEnteredFormat.textFormat")
        fmt(sh, HEAD_ROWS, HEAD_ROWS + 1, 0, ncols, {
            "textFormat": {**font, "bold": True, "fontSize": 9,
                           "foregroundColor": rgb("#FFFFFF")},
            "backgroundColor": rgb(NAVY), "wrapStrategy": "WRAP"},
            "userEnteredFormat(textFormat,backgroundColor,wrapStrategy)")
        reqs.append({"updateDimensionProperties": {"range": {
            "sheetId": sh, "dimension": "ROWS", "startIndex": HEAD_ROWS,
            "endIndex": HEAD_ROWS + 1}, "properties": {"pixelSize": 48}, "fields": "pixelSize"}})
        first_num = {TAB_CAMP: 5, TAB_ACCT: 1, TAB_HIST: 3}[t]
        ncol_data = len(values[t][HEAD_ROWS])
        width(sh, 0, first_num, 150)
        width(sh, first_num, ncol_data, 92)
        reqs.append({"setBasicFilter": {"filter": {"range": rng(sh, HEAD_ROWS, max(n, HEAD_ROWS + 1),
                                                                0, ncol_data)}}})
        if n <= HEAD_ROWS + 1:
            continue                                  # no data rows: an empty range is a 400
        fmt(sh, HEAD_ROWS + 1, n, first_num, ncol_data,
            {"numberFormat": {"type": "NUMBER", "pattern": "#,##0"},
             "horizontalAlignment": "RIGHT"},
            "userEnteredFormat(numberFormat,horizontalAlignment)")
        for c in pct_cols.get(t, ()):
            fmt(sh, HEAD_ROWS + 1, n, c, c + 1,
                {"numberFormat": {"type": "PERCENT", "pattern": "0.0%"}},
                "userEnteredFormat.numberFormat")
            # one scale per rate column, within the campaigns only (not the «Разом» row)
            last = n - 1 if t == TAB_ACCT else n
            if last > HEAD_ROWS + 1:
                reqs.append({"addConditionalFormatRule": {"index": 0, "rule": {
                    "ranges": [rng(sh, HEAD_ROWS + 1, last, c, c + 1)],
                    "gradientRule": {"minpoint": {"color": rgb("#FFFFFF"), "type": "MIN"},
                                     "maxpoint": {"color": rgb("#9DB0FF"), "type": "MAX"}}}}})
        if t == TAB_CAMP:
            width(sh, 0, 1, 190)
            width(sh, 1, 2, 230)
            width(sh, 2, 3, 250)
            width(sh, 3, 5, 90)
            width(sh, ncol_data - 2, ncol_data, 170)
            fmt(sh, HEAD_ROWS + 1, n, ncol_data - 2, ncol_data,
                {"horizontalAlignment": "LEFT"}, "userEnteredFormat.horizontalAlignment")
            # positive replies are the column people look for first
            fmt(sh, HEAD_ROWS + 1, n, 13, 14, {"textFormat": {**font, "bold": True,
                                                              "foregroundColor": rgb(BLUE)}},
                "userEnteredFormat.textFormat")
        if t == TAB_ACCT:
            fmt(sh, n - 1, n, 0, ncol_data, {"textFormat": {**font, "bold": True},
                                            "backgroundColor": rgb("#EEF1FF")},
                "userEnteredFormat(textFormat,backgroundColor)")
        if t == TAB_HIST:
            width(sh, 2, 3, 230)
    od.sheets("POST", f"/{sid}:batchUpdate", {"requests": reqs})
    return sid, created


def cmd_sheet(args) -> int:
    snaps = sorted(STATS_DIR.glob("????-??-??.json"))
    if not snaps:
        print(f"✗ no snapshot in {STATS_DIR} — the nightly `closely-pull.py pull-all --stats` "
              "writes it")
        return 1
    values = sheet_values(snaps)
    if args.dry_run:
        for t, v in values.items():
            print(f"== {t} ({len(v)} rows)")
            for r in v[:12]:
                print("  ", r)
        return 0
    st = load_sheet_state()
    try:
        sid, created = write_stats_sheet(values, st)
    except Exception as e:                            # noqa: BLE001  (Broken, oo, network)
        print(f"✗ sheet: {e}")
        if args.notify:
            OP.telegram_send(f"⚠️ Outbound-таблиця не оновилась: {short(str(e), 300)}")
        return 3
    print(f"→ {SHEET_URL.format(sid)}")
    if created and args.notify:
        OP.telegram_send("📊 Таблиця зі статистикою outbound-кампаній створена, оновлюється "
                         f"щоранку: {SHEET_URL.format(sid)}")
    return 0


# ----------------------------------------------------------------------- status

def cmd_status(args) -> int:
    camps = survey()
    st = load_state()
    print(f"state: {STATE} ({'absent — the first run will baseline' if st is None else 'present'})")
    reported = {k: set(v) for k, v in (st or {}).get("reported", {}).items()}
    for c in camps:
        new = [r for r in c["raw"] if reply_key(r) not in reported.get(c["slug"], set())] \
            if st else c["unclassified"]
        info = (st or {}).get("jobs", {}).get(c["slug"], {})
        print(f"{c['slug']:48} {account_label(c['profile']):30} raw={len(c['raw']):3} "
              f"unclassified={len(c['unclassified'])} unreported={len(new)}"
              + (f" · {job_line(info)}" if info else ""))
    dirty = dirty_response_files((RAW, CLASSIFIED, SUMMARY))
    print(f"dirty response files: {len(dirty)}")
    for p in dirty:
        print(f"  {p}")
    print(f"unpushed commits on {BRANCH}: {unpushed()}")
    return 0


# ------------------------------------------------------------------------- main

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="outbound-responses-daily.py",
                                 description="closely.io replies: commit, classify, report")
    sub = ap.add_subparsers(dest="cmd", required=True)
    n = sub.add_parser("night", help="after closely-pull: commit + enqueue the classifier")
    n.add_argument("--dry-run", action="store_true")
    n.set_defaults(func=cmd_night)
    m = sub.add_parser("morning", help="commit the classifier's output + Telegram report")
    m.add_argument("--notify", action="store_true", help="send to Telegram (else print only)")
    m.add_argument("--dry-run", action="store_true")
    m.set_defaults(func=cmd_morning)
    s = sub.add_parser("status", help="read-only overview")
    s.set_defaults(func=cmd_status)
    w = sub.add_parser("weekly", help="full funnel per campaign from the nightly Closely "
                                      "snapshot (closely-pull.py pull-all --stats)")
    w.add_argument("--notify", action="store_true", help="send to Telegram (else print only)")
    w.set_defaults(func=cmd_weekly)
    sh = sub.add_parser("sheet", help="rewrite the Google Sheet with per-campaign stats from "
                                      "the latest snapshot (via oo)")
    sh.add_argument("--notify", action="store_true",
                    help="Telegram on failure, and once with the link when it is created")
    sh.add_argument("--dry-run", action="store_true", help="print the rows, write nothing")
    sh.set_defaults(func=cmd_sheet)
    args = ap.parse_args(argv)

    if args.cmd in ("status", "weekly", "sheet"):
        return args.func(args)
    LOCK.parent.mkdir(parents=True, exist_ok=True)
    with LOCK.open("w") as lf:
        try:
            fcntl.flock(lf, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            print("✗ another outbound-responses-daily run holds the lock — skipping")
            return 1
        return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
