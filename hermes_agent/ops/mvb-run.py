#!/usr/bin/env python3
"""Enqueue a 3DLOOK marketing pipeline as a conductor job — the ONE way Hermes starts one.

WHY THIS EXISTS
---------------
Hermes had no tool for this. `CMD_TO_PROFILE` in claude_switcher.py knows dev / seo /
marketing / security, none of which is Vadim's marketing system, so every article, post
batch and outbound campaign was started by the manager hand-writing SQL through its
`terminal` / `execute_code` tools. On 2026-08-17 that produced job 88 in three attempts —
`syntax error near "How"` (an apostrophe in the brief), then an IntegrityError, then a row
that was wrong in three ways at once:

  * work_dir was the repo ROOT, one level above marketing_vb, where the agents' relative
    reads (CLAUDE.md, brand-assets/, workspace/) resolve to nothing;
  * the brief was re-typed as prose instead of calling /post-from-article, so it competed
    with the pipeline's own instructions;
  * two ho_steps rows were inserted next to it, which silently switched the run into the
    dev step-verifier (`npx ultracite lint`, `npm test` in a tree with no package.json) →
    gates failed 3× per step → "blocked" → two Telegram escalations → approved by hand →
    job closed as `done — all 2 steps done` with zero posts written.

Every one of those is a formatting decision, which is exactly what a script should own.

WHAT IT GUARANTEES
------------------
  * profile + work_dir come from the profile manifest (`runFrom`), never from a guess;
  * the prompt is the pipeline's own slash command with the minimum context around it;
  * ho_steps is never written — a content pipeline's gate is its own QC plus Vadim's
    approval of the digest, not `npm test`;
  * preconditions are checked BEFORE a job exists (does the article dir exist, is there a
    readable source, which file and what status) and refusals are printed, not enqueued;
  * a duplicate of a job that is still running is refused with the live job id, so a
    retried tool call cannot double-start a pipeline.

The route table, the prompts and the precondition checks are NOT duplicated here: they are
imported from claude_switcher.py, so the Telegram buttons and this script can never drift.

USAGE
    mvb-run.py article  "<topic>"          # SEO pipeline  (/new-article)
    mvb-run.py posts    <slug|url>         # social posts  (/post-from-article)
    mvb-run.py outbound "<market/task>"    # outbound      (/outbound)
    mvb-run.py campaign "<task>"           # blended VB×SM (/vbsm-campaign)
    mvb-run.py articles                    # what can be turned into posts, and from which file
    mvb-run.py digest   <slug>             # the finished posts, ready to forward into Telegram
    mvb-run.py status [job_id]             # job status + open questions/escalations
Exit codes: 0 = enqueued or informational · 2 = refused (reason on stdout) · 3 = broken setup.
"""

from __future__ import annotations

import importlib.util
import os
import sqlite3
import sys

HO_DB = os.environ.get("HO_DB") or os.path.expanduser("~/.hermes/ho.db")
SWITCHER = os.environ.get("MVB_SWITCHER") or os.path.expanduser(
    "~/3dlook-marketing/hermes_agent/ops/claude-switcher/claude_switcher.py")
MAX_TURNS = int(os.environ.get("MVB_MAX_TURNS", "300"))
CMD_TO_ROUTE = {"article": "mvb:article", "posts": "mvb:posts",
                "outbound": "mvb:outbound", "campaign": "mvb:campaign"}
TERMINAL = ("done", "failed", "aborted", "escalated")


def load_switcher():
    """Import claude_switcher as a module. Its top-level imports are stdlib only
    (telegram is imported inside functions), so this works outside the gateway."""
    if not os.path.exists(SWITCHER):
        sys.exit(f"⚠️ не найден claude_switcher.py: {SWITCHER}\n"
                 "Это единственный источник маршрутов — сообщи Вадиму, "
                 "SQL руками НЕ пиши.")
    spec = importlib.util.spec_from_file_location("mvb_switcher", SWITCHER)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["mvb_switcher"] = mod
    try:
        spec.loader.exec_module(mod)
    except Exception as exc:                       # pragma: no cover - setup breakage
        sys.exit(f"⚠️ claude_switcher.py не импортируется: {exc}\n"
                 "Сообщи Вадиму. SQL руками НЕ пиши.")
    if not hasattr(mod, "MVB_ROUTES"):
        sys.exit("⚠️ в claude_switcher.py нет MVB_ROUTES — версия старая. "
                 "Сообщи Вадиму, SQL руками НЕ пиши.")
    return mod


def db() -> sqlite3.Connection:
    if not os.path.exists(HO_DB):
        sys.exit(f"⚠️ нет очереди {HO_DB} — conductor не установлен?")
    c = sqlite3.connect(HO_DB, timeout=10)
    c.row_factory = sqlite3.Row
    return c


def live_duplicate(conn: sqlite3.Connection, title: str):
    """A non-terminal job with the same title = this pipeline is already running."""
    return conn.execute(
        "select id, status from ho_jobs where title=? and status not in "
        "('done','failed','aborted','escalated') order by id desc limit 1",
        (title,)).fetchone()


def cmd_enqueue(m, route: str, arg: str) -> int:
    r = m.MVB_ROUTES[route]
    work_dir = m._mvb_dir()
    if not os.path.isdir(work_dir):
        print(f"⚠️ каталог системы не найден: {work_dir} — проверь runFrom в манифесте профиля")
        return 3
    prompt, title, note, err = r["prepare"](arg)
    if err:
        print(err)                                  # already human-readable, Telegram-ready
        return 2
    conn = db()
    with conn:
        dup = live_duplicate(conn, title[:200])
        if dup:
            print(f"ℹ️ уже запущено: job #{dup['id']} ({dup['status']}) — «{title}». "
                  "Второй раз не ставлю.")
            return 2
        cur = conn.execute(
            "insert into ho_jobs(kind,title,prompt,profile,work_dir,max_turns) "
            "values('feature',?,?,?,?,?)",
            (title[:200], prompt, r["profile"], work_dir, MAX_TURNS))
        jid = cur.lastrowid
    print(f"🚀 job #{jid} · {r['label']} · profile={r['profile']} · max_turns={MAX_TURNS}")
    print(f"📂 {work_dir}")
    print(f"📝 {title}")
    if note:
        print(f"ℹ️ {note}")
    print("Вопросы и эскалации придут в Telegram; результат — тоже. "
          "ho_steps не создавались (и не надо).")
    return 0


def cmd_articles(m) -> int:
    root = os.path.join(m._mvb_dir(), "workspace", "seo", "articles")
    slugs = sorted(n for n in os.listdir(root) if os.path.isdir(os.path.join(root, n)))
    for s in slugs:
        src, note, err = m._mvb_article_source(s)
        print(f"{s}\n    {'⚠️ ' + err if err else note}")
    print(f"\n{len(slugs)} статей. Посты: mvb-run.py posts <slug>")
    return 0


def cmd_digest(m, slug: str) -> int:
    """Print the finished posts for `slug` so Hermes can forward them into Telegram.

    The conductor's own completion message truncates the job summary at 1500 chars, so
    the deliverable never fits there — and since the marketing tg-bridge is off, nothing
    else pushes the text. This is that missing last step: one command whose stdout IS the
    message. Prefers review-digest.md (the read-order compilation the pipeline builds);
    falls back to the per-profile post.md files when the run stopped before the digest."""
    if not slug:
        print("нужен slug: mvb-run.py digest <slug>")
        return 2
    root = os.path.join(m._mvb_dir(), "workspace", "social", "articles", slug)
    if not os.path.isdir(root):
        print(f"⚠️ постов для `{slug}` ещё нет ({root} не создан)")
        return 2
    digest = os.path.join(root, "review-digest.md")
    if os.path.exists(digest):
        print(open(digest, encoding="utf-8", errors="replace").read())
        print(f"\n— источник: workspace/social/articles/{slug}/review-digest.md")
        return 0
    posts = sorted(n for n in os.listdir(root)
                   if os.path.isfile(os.path.join(root, n, "post.md")))
    if not posts:
        print(f"⚠️ в {root} нет ни review-digest.md, ни <profile>/post.md — "
              "прогон ещё идёт или упал, проверь mvb-run.py status")
        return 2
    print(f"# Посты — {slug} (review-digest.md ещё не собран, {len(posts)} профилей)\n")
    for p in posts:
        print(f"\n## {p}\n")
        print(open(os.path.join(root, p, "post.md"), encoding="utf-8",
                   errors="replace").read())
    return 0


def cmd_status(argv) -> int:
    conn = db()
    if argv:
        rows = conn.execute(
            "select * from ho_jobs where id=?", (int(argv[0]),)).fetchall()
    else:
        rows = conn.execute(
            "select * from ho_jobs where status not in "
            "('done','failed','aborted','escalated') order by id desc limit 10").fetchall()
        if not rows:
            rows = conn.execute("select * from ho_jobs order by id desc limit 5").fetchall()
    if not rows:
        print("очередь пуста")
        return 0
    for j in rows:
        print(f"#{j['id']} [{j['status']}] {j['profile']} · {j['title']}")
        print(f"    📂 {j['work_dir']}  created {j['created_at']}"
              + (f"  finished {j['finished_at']}" if j["finished_at"] else ""))
        if j["result_summary"]:
            print(f"    → {j['result_summary'][:300]}")
        if j["error"]:
            print(f"    ⚠️ {j['error'][:300]}")
        n = conn.execute("select count(*) from ho_steps where job_id=?", (j["id"],)).fetchone()[0]
        if n:
            print(f"    ⚠️ у job есть {n} ho_steps — для маркетинговых профилей это лишнее "
                  "(conductor их игнорирует, но не создавай их)")
        for e in conn.execute(
                "select id, reason, question, status from ho_escalations where job_id=? "
                "and status='open' order by id", (j["id"],)):
            print(f"    ❓ эскалация #{e['id']} ({e['reason']}): {e['question'][:200]}")
        for q in conn.execute(
                "select id, question from ho_questions where job_id=? and status='open' "
                "order by seq", (j["id"],)):
            print(f"    ❓ вопрос #{q['id']}: {str(q['question'])[:200]}")
    return 0


def main(argv) -> int:
    if not argv or argv[0] in ("-h", "--help", "help"):
        print(__doc__)
        return 0
    cmd, rest = argv[0], argv[1:]
    if cmd == "status":
        return cmd_status(rest)
    m = load_switcher()
    if cmd == "articles":
        return cmd_articles(m)
    if cmd == "digest":
        return cmd_digest(m, " ".join(rest).strip())
    route = CMD_TO_ROUTE.get(cmd)
    if not route:
        print(f"неизвестная команда «{cmd}». Есть: "
              + ", ".join(list(CMD_TO_ROUTE) + ["articles", "digest", "status"]))
        return 2
    return cmd_enqueue(m, route, " ".join(rest).strip())


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
