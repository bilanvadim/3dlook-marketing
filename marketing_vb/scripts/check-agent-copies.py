#!/usr/bin/env python3
"""check-agent-copies.py — fail loudly when the same agent exists in several
places with different contents.

WHY
---
Every agent in this system lives in three files:

  claude_code/DEV/marketing_vb/plugins/<pkg>/agents/<name>.md   ← marketplace SOURCE
  marketing_vb/.claude/plugins/<pkg>/0.2.0/agents/<name>.md     ← installed artifact
  marketing_vb/.claude/agents/<group>/<name>.md                 ← project-local copy

Nothing keeps them equal. Editing only the project copies loses the change on the
next plugin install; editing only DEV means the running pipeline never sees it.
Both have happened. On 2026-08-26 all four SEO agents were drifting in BOTH
directions at once: DEV was ahead on "em dash banned outright", the project
copies were ahead on the abbreviation exception, and neither was a superset — so
whichever way someone "synced" them, real rules would have been lost.

Worse, the project copy and the plugin copy declare the SAME `name:` in their
frontmatter. While they are identical that is harmless; the moment they diverge,
which one answers to the name is a coin toss. That is exactly how the
`brand-checker` collision happened, where a bare name reached the shallow social
agent and the deep fact-checker never ran.

Comparing copies against each other only catches DIVERGENCE. It is blind to a copy
that is simply GONE — with one location missing, the survivors still agree and the
check stays green. On 2026-08-28 `marketing_vb/.claude/plugins/mvb-core/0.2.0/` was
deleted whole and five agents sat in two places out of three for two days while this
script reported success every morning. So presence is now checked as well: every
agent must exist in all three ROOTS. Measured 2026-08-30, all 28 do, so the strict
rule costs nothing today and fires the moment a location disappears.

This script does not fix anything: an automatic merge here would silently pick a
winner, which is the failure it exists to prevent. It reports, and a human
decides which side is right.

USAGE
    scripts/check-agent-copies.py [--quiet] [--notify]
`--notify` pushes drift to Telegram (same bot/chat as conductor-monitor.sh), and
is meant for the cron run — a log nobody opens is not an alert. Deduped on the
CONTENT of the drift, not on "drift exists": the same unresolved divergence stays
quiet day after day, while a NEW one gets through immediately. Fixing everything
clears the marker, so the next regression alerts again on its own.
Exit: 0 all copies present and equal · 1 drift and/or a missing copy · 3 setup broken.
"""
from __future__ import annotations

import hashlib
import os
import subprocess
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.dirname(HERE)                       # …/marketing_vb
REPO = os.path.dirname(PROJ)                       # …/3dlook-marketing

ENVF = os.environ.get("HERMES_ENV_FILE", os.path.expanduser("~/.hermes/.env"))
STATE = os.path.expanduser("~/.hermes/.agent-copies-state")

ROOTS = [
    os.path.join(REPO, "claude_code", "DEV", "marketing_vb", "plugins"),
    os.path.join(PROJ, ".claude", "plugins"),
    os.path.join(PROJ, ".claude", "agents"),
]
# Parallel to ROOTS, in the same order — used to name the location an agent is
# missing from. A path alone does not say what that location is FOR.
ROOT_LABELS = [
    "DEV-источник (marketplace)",
    "установленный плагин",
    "проектная копия",
]


def root_of(path: str):
    """Which ROOT a found file belongs to. The roots do not nest, so the first
    prefix match is the only one."""
    for i, root in enumerate(ROOTS):
        if path.startswith(root + os.sep):
            return i
    return None


def digest(path: str) -> str:
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()


def collect():
    found = defaultdict(list)
    for root in ROOTS:
        if not os.path.isdir(root):
            continue
        for dirpath, _dirs, files in os.walk(root):
            # An agent definition is any .md sitting under an `agents/` directory.
            # Not just directly IN one: the project copies are grouped into
            # subfolders (.claude/agents/seo/, /_shared/, /social/, /outbound/),
            # and an earlier version of this check required basename == "agents",
            # so it skipped every grouped file and reported drift between the two
            # plugin copies while the copy that actually runs went unexamined.
            norm = dirpath.replace(os.sep, "/")
            if "/agents/" not in norm + "/" and os.path.basename(dirpath) != "agents":
                continue
            # A plugin also ships skills, commands and references; those live
            # outside agents/ and are deliberately not compared here.
            for fn in files:
                if fn.endswith(".md"):
                    found[fn[:-3]].append(os.path.join(dirpath, fn))
    return found


def notify(text: str, fingerprint: str) -> None:
    """Push once per distinct drift fingerprint. Silence on repeat is deliberate:
    an unresolved divergence is a standing condition, and a daily re-ping trains
    everyone to ignore the channel that is supposed to carry the new one."""
    try:
        seen = open(STATE, encoding="utf-8").read().split()
    except OSError:
        seen = []
    if fingerprint in seen:
        return
    bot = chat = ""
    try:
        for line in open(ENVF, encoding="utf-8"):
            if line.startswith("TELEGRAM_BOT_TOKEN="):
                bot = line.split("=", 1)[1].strip()
            elif line.startswith("TELEGRAM_ALLOWED_USERS="):
                chat = line.split("=", 1)[1].strip().split(",")[0]
    except OSError:
        pass
    if not bot or not chat:
        print("(нет TELEGRAM creds — не отправляю)", file=sys.stderr)
        return
    # --config -: the token would otherwise sit in argv, world-readable via ps,
    # and this runs from cron. -f: without it curl exits 0 on HTTP 400/429 and the
    # fingerprint gets marked sent for an alert that never arrived.
    try:
        subprocess.run(
            ["curl", "-sf", "-m", "15", "--config", "-",
             "--data-urlencode", f"chat_id={chat}",
             "--data-urlencode", f"text={text}"],
            input=f'url = "https://api.telegram.org/bot{bot}/sendMessage"\n',
            text=True, check=True, capture_output=True)
    except Exception as e:
        print(f"(Telegram не ушёл: {type(e).__name__}) — фингерпринт НЕ помечаю", file=sys.stderr)
        return
    with open(STATE, "a", encoding="utf-8") as f:
        f.write(fingerprint + "\n")


def main(argv=None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    quiet = "--quiet" in args
    want_notify = "--notify" in args

    # A whole ROOT being gone is one fact, not N missing agents — report it once
    # and drop it from what the per-agent presence check expects, so a single
    # mis-set path cannot bury the real findings under 28 identical lines.
    expect = [i for i, root in enumerate(ROOTS) if os.path.isdir(root)]
    gone_roots = [i for i in range(len(ROOTS)) if i not in expect]

    found = collect()
    if not found:
        print("⚠️ ни одного агента не найдено — проверь пути в ROOTS")
        return 3

    drift, missing = [], []
    for name, paths in sorted(found.items()):
        have = {root_of(p) for p in paths}
        gaps = [i for i in expect if i not in have]
        if gaps:
            missing.append((name, gaps))
        by_hash = defaultdict(list)
        for p in paths:
            by_hash[digest(p)].append(p)
        if len(by_hash) > 1:
            drift.append((name, by_hash))

    for i in gone_roots:
        print(f"⚠️ локация отсутствует целиком: {ROOT_LABELS[i]} "
              f"({os.path.relpath(ROOTS[i], REPO)})\n")

    if missing:
        print(f"❌ ПРОПАЖА у {len(missing)} агент(ов) — копия есть не везде:\n")
        for name, gaps in missing:
            print(f"  {name}")
            for i in gaps:
                print(f"    нет в: {ROOT_LABELS[i]}  "
                      f"({os.path.relpath(ROOTS[i], REPO)})")
            print()
        print("Сравнение копий друг с другом это НЕ ловит — оно про разное содержимое, "
              "а не про исчезнувшую локацию. Так 2026-08-28 целиком пропал "
              "marketing_vb/.claude/plugins/mvb-core/0.2.0/: пять агентов остались в двух "
              "местах из трёх, а чек двое суток был зелёным. Вернуть копию "
              "(git checkout HEAD -- <путь>), потом СВЕСТИ содержимое — восстановленный "
              "файл почти наверняка отстал от остальных.\n")

    if drift:
        print(f"❌ РАСХОЖДЕНИЕ в {len(drift)} агент(ах) — одно имя, разное содержимое:\n")
        for name, by_hash in drift:
            print(f"  {name}")
            for h, paths in by_hash.items():
                for p in paths:
                    print(f"    {h[:8]}  {os.path.relpath(p, REPO)}")
            print()
        print("Ни одна копия не считается по умолчанию правильной — сравни построчно "
              "(diff) и реши, какая сторона новее ПО КАЖДОМУ правилу. Слепая перезапись "
              "в любую сторону теряет настоящие правки: так уже было 2026-08-26.")

    if drift or missing or gone_roots:
        if want_notify:
            parts = []
            if missing:
                parts.append(f"пропали копии ({len(missing)}): "
                             + ", ".join(n for n, _ in missing))
            if drift:
                parts.append(f"разошлись ({len(drift)}): "
                             + ", ".join(n for n, _ in drift))
            if gone_roots:
                parts.append("нет локации: "
                             + ", ".join(ROOT_LABELS[i] for i in gone_roots))
            # The fingerprint covers BOTH findings, and tags each kind, so a copy
            # going missing is a new alert even while a known divergence is parked.
            fp = hashlib.md5("|".join(
                [f"M{n}:{''.join(map(str, g))}" for n, g in missing]
                + [f"D{n}:{''.join(sorted(bh))}" for n, bh in drift]
                + [f"R{i}" for i in gone_roots]).encode()).hexdigest()
            notify(
                "⚠️ Агенты: " + "; ".join(parts) + "\n"
                "Одно имя — разное содержимое (или копии вовсе нет) в DEV / установленном "
                "плагине / проектной папке. Пока так, какая копия ответит на имя — вопрос "
                "удачи, а пропавшую правку не увидит никто.\n"
                "Разбор: scripts/check-agent-copies.py (чинить построчно, не перезаписью).",
                fp)
        return 1

    # Everything agrees: drop the marker so a future regression alerts again.
    if want_notify and os.path.exists(STATE):
        try:
            os.remove(STATE)
        except OSError:
            pass
    if not quiet:
        print(f"✅ копии агентов совпадают ({len(found)} агент(ов) "
              f"× {len(expect)} локаци(й), пропаж нет)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
