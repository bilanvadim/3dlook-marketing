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
Without --notify, `morning` prints the report instead of sending it. Env for tests:
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
    args = ap.parse_args(argv)

    if args.cmd == "status":
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
