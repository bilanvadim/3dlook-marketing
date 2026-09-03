#!/usr/bin/env python3
"""content-plan-sync.py — the strategy spreadsheet is the master; the repo copies are what agents read.

Same failure class as check-agent-copies.py and split-linkedin-prompts.py --check: a master that
moved on and a derivative nobody re-exported is silent drift, and here it is expensive. Phase 0 in
`seo-planner` resolves every article against `content-plan.md`; a stale row means an article gets
planned against the wrong priority, the wrong action type, or a cannibalization guardrail that has
since changed. On 2026-09-03 `content-plan.md` still carried "Last synced from source: 2026-07-07"
while five priority rows in published-articles-inventory.md disagreed with the sheet.

Two derivatives, deliberately handled differently:

  content-plan.csv  — a byte-for-byte export of the sheet. Mechanical, lossless, so --sync rewrites it.
  content-plan.md   — the file the agents actually read. It carries hand-written material the sheet
                      does NOT have (per-hub preambles such as the Hub 8 block-lift, formatting,
                      curated cross-references). Regenerating it from the CSV would destroy that,
                      so this script never writes it. It tells you which rows to reconcile.

Usage:
  content-plan-sync.py                    # --check: report drift, exit 1 if any
  content-plan-sync.py --sync             # also rewrite content-plan.csv (old one snapshotted)
  content-plan-sync.py --notify --quiet   # cron shape: silent unless drift, one Telegram ping
  content-plan-sync.py --gid 123456       # a tab other than the first

Exit: 0 clean · 1 drift found · 2 could not fetch or read
"""

import csv
import hashlib
import io
import os
import subprocess
import sys
import time

SHEET_ID = "1Sy7EzzZZvCKyrD30pbhElEpCZDbzuMtMkxdiDTIP8AE"
SHEET_URL = "https://docs.google.com/spreadsheets/d/{id}/export?format=csv&gid={gid}"

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STRAT = os.path.join(ROOT, "brand-assets", "content-strategy")
CSV_LOCAL = os.path.join(STRAT, "content-plan.csv")
MD_LOCAL = os.path.join(STRAT, "content-plan.md")
INVENTORY = os.path.join(STRAT, "published-articles-inventory.md")
SNAPDIR = os.path.join(STRAT, ".content-plan-snapshots")

ENVF = os.environ.get("HERMES_ENV_FILE", os.path.expanduser("~/.hermes/.env"))
STATE = os.path.expanduser("~/.hermes/.content-plan-state")

# Columns we treat as decision-bearing. A change in any of these can redirect an article, so they
# are reported cell by cell. Everything else is reported as "other columns changed" without the
# diff body, because the Recommendations column runs to paragraphs and would bury the signal.
KEY_COLS = ("Intent", "Action Type", "Execution Priority", "Cannibalization Guardrail",
            "Published article", "Published / Updated")

P_TOKENS = ("P0", "P1", "P2")


def norm(s):
    """Fold a title to something two documents can be compared on."""
    return " ".join("".join(c.lower() if c.isalnum() else " " for c in s).split())


def fetch(gid):
    url = SHEET_URL.format(id=SHEET_ID, gid=gid)
    # -f so an HTTP 4xx is an error and not an empty "clean" diff; the export endpoint answers 200
    # with an HTML login page when a sheet stops being link-readable, so the content-type is checked
    # too — that is the failure that would otherwise read as "every row was deleted".
    try:
        out = subprocess.run(
            ["curl", "-sfL", "-m", "60", "-w", "\n%{content_type}", url],
            check=True, capture_output=True, text=True).stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ не смог скачать лист (curl exit {e.returncode}). "
              f"Проверь, что таблица ещё link-readable: {url}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"❌ не смог скачать лист: {type(e).__name__}: {e}", file=sys.stderr)
        return None
    body, _, ctype = out.rpartition("\n")
    if "text/csv" not in ctype:
        print(f"❌ лист отдал не CSV, а {ctype.strip()!r} — почти наверняка доступ к таблице "
              f"закрыли и это страница логина. Ничего не синкаю.", file=sys.stderr)
        return None
    return body


def rows(text):
    """CSV text -> (header, {row_key: {col: value}}, [order]). Rows are keyed by hub+cluster+title."""
    rdr = csv.reader(io.StringIO(text))
    try:
        header = next(rdr)
    except StopIteration:
        return [], {}, []
    out, order = {}, []
    for i, r in enumerate(rdr):
        if not any(c.strip() for c in r):
            continue
        rec = {header[j]: (r[j] if j < len(r) else "") for j in range(len(header))}
        hub = rec.get("Main hub topic", "").strip()
        cluster = rec.get("Cluster section", "").strip()
        title = rec.get("Supporting articles", "").strip()
        key = (norm(hub), norm(cluster), norm(title)) if (hub or cluster or title) else (f"row{i}",)
        # A duplicated key would silently swallow a row; keep both by disambiguating.
        base, n = key, 2
        while key in out:
            key = base + (str(n),)
            n += 1
        out[key] = rec
        order.append(key)
    return header, out, order


def label(rec):
    title = (rec.get("Supporting articles") or rec.get("Main hub topic") or "?").strip()
    hub = (rec.get("Main hub topic") or "?").strip()
    pri = (rec.get("Execution Priority") or "—").strip()
    act = (rec.get("Action Type") or "—").strip()
    short = hub if len(hub) <= 46 else hub[:43] + "..."
    return f"{title}  [hub: {short} · {pri} · {act}]"


def diff_plan(live, local):
    """Compare the sheet against the repo CSV. Returns a list of human-readable findings."""
    _, lrows, lorder = rows(live)
    _, prows, porder = rows(local)
    found = []

    added = [k for k in lorder if k not in prows]
    removed = [k for k in porder if k not in lrows]
    if added:
        found.append(f"➕ НОВЫХ строк в таблице: {len(added)}")
        found += [f"   · {label(lrows[k])}" for k in added]
    if removed:
        found.append(f"➖ строк ИСЧЕЗЛО из таблицы (есть в репо, нет в листе): {len(removed)}")
        found += [f"   · {label(prows[k])}" for k in removed]

    changed = 0
    for k in lorder:
        if k not in prows:
            continue
        a, b = prows[k], lrows[k]
        hits, other = [], []
        for col in set(list(a.keys()) + list(b.keys())):
            av, bv = (a.get(col) or "").strip(), (b.get(col) or "").strip()
            if av == bv:
                continue
            if col in KEY_COLS:
                hits.append((col, av, bv))
            else:
                other.append(col)
        if not hits and not other:
            continue
        changed += 1
        found.append(f"✏️  {label(b)}")
        for col, av, bv in sorted(hits):
            found.append(f"      {col}: {av or '(пусто)'} → {bv or '(пусто)'}")
        if other:
            found.append(f"      (также изменились: {', '.join(sorted(set(other)))})")
    if changed:
        found.insert(0, f"✏️  ИЗМЕНЁННЫХ строк: {changed}")
    return found


def inventory_priority_drift(live):
    """Cross-check the sheet's Execution Priority against what published-articles-inventory.md says.

    Heuristic on purpose: the inventory shortens titles ("Manual Intake vs Digital Intake" for
    "...in Occupational Health Screening"), so rows are matched on a normalized prefix. It is
    reported as a hint to verify, never as a fact. This exists because on 2026-09-03 five of seven
    open rows in that file sat under P1 while the sheet said P0, P0, P0, P2, P2.
    """
    try:
        inv = io.open(INVENTORY, encoding="utf-8").read()
    except OSError:
        return []
    # Only the gap-analysis section. The "Content Plan Coverage: Health Hubs" table above it carries
    # a P-token per *hub*, and a hub label is a substring of its own articles' titles — scanning it
    # made the sheet's P2 "AI in Insurance Underwriting..." collide with hub 7's P0 row.
    # Blockquoted lines are skipped too: the reconciliation note here contains its own P0/P1 table.
    marker = "## Gap Analysis vs Content Plan"
    section = inv.split(marker, 1)[1] if marker in inv else inv
    _, lrows, lorder = rows(live)
    inv_lines = [ln for ln in section.splitlines()
                 if ln.lstrip().startswith("|") and any(t in ln for t in P_TOKENS)]
    out = []
    for k in lorder:
        rec = lrows[k]
        pri = (rec.get("Execution Priority") or "").strip()
        title = (rec.get("Supporting articles") or "").strip()
        if pri not in P_TOKENS or len(norm(title)) < 20:
            continue
        nt = norm(title)
        for ln in inv_lines:
            cells = [c.strip() for c in ln.strip().strip("|").split("|")]
            hit = next((c for c in cells
                        if len(norm(c)) >= 20 and (norm(c) in nt or nt.startswith(norm(c)[:24]))), None)
            if not hit:
                continue
            said = [t for t in P_TOKENS if t in ln]
            # A struck-through row is a closed item; its old priority is history, not drift.
            if "~~" in ln or not said or pri in said:
                continue
            out.append(f"   · {title}\n"
                       f"       лист: {pri} · инвентарь: {'/'.join(said)}  ({hit[:60]})")
    if out:
        out.insert(0, f"⚠️  ПРИОРИТЕТЫ расходятся с published-articles-inventory.md "
                      f"({len(out)}) — эвристика по названиям, проверь глазами:")
    return out


def notify(text, fingerprint):
    """One ping per distinct drift fingerprint. Repeat silence is deliberate — an unreconciled sheet
    is a standing condition, and a weekly re-ping teaches everyone to mute the channel."""
    try:
        seen = io.open(STATE, encoding="utf-8").read().split()
    except OSError:
        seen = []
    if fingerprint in seen:
        return
    bot = chat = ""
    try:
        for line in io.open(ENVF, encoding="utf-8"):
            if line.startswith("TELEGRAM_BOT_TOKEN="):
                bot = line.split("=", 1)[1].strip()
            elif line.startswith("TELEGRAM_ALLOWED_USERS="):
                chat = line.split("=", 1)[1].strip().split(",")[0]
    except OSError:
        pass
    if not bot or not chat:
        print("(нет TELEGRAM creds — не отправляю)", file=sys.stderr)
        return
    # --config -: the token would otherwise sit in argv, world-readable via ps, and this runs from
    # cron. -f: without it curl exits 0 on HTTP 400/429 and the fingerprint gets marked sent for an
    # alert that never arrived.
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
    with io.open(STATE, "a", encoding="utf-8") as f:
        f.write(fingerprint + "\n")


def main(argv=None):
    args = argv if argv is not None else sys.argv[1:]
    quiet = "--quiet" in args
    want_sync = "--sync" in args
    want_notify = "--notify" in args
    gid = "0"
    if "--gid" in args:
        i = args.index("--gid")
        if i + 1 < len(args):
            gid = args[i + 1]

    live = fetch(gid)
    if live is None:
        return 2
    try:
        local = io.open(CSV_LOCAL, encoding="utf-8").read()
    except OSError as e:
        print(f"❌ нет локальной копии {CSV_LOCAL}: {e}", file=sys.stderr)
        return 2

    findings = diff_plan(live, local) + inventory_priority_drift(live)

    if not findings:
        if not quiet:
            _, lr, _ = rows(live)
            print(f"✅ content-plan.csv совпадает с листом ({len(lr)} строк), "
                  f"приоритеты в инвентаре не расходятся.")
            print(f"   Напоминание: content-plan.md — отдельная копия, её этот скрипт не проверяет "
                  f"построчно. Дата в её шапке: {md_synced_line()}")
        return 0

    print("=" * 78)
    print(f"СТРАТЕГИЧЕСКИЙ ЛИСТ РАСХОДИТСЯ С РЕПО — {time.strftime('%Y-%m-%d %H:%M')}")
    print(f"лист: https://docs.google.com/spreadsheets/d/{SHEET_ID}/edit?gid={gid}#gid={gid}")
    print("=" * 78)
    for ln in findings:
        print(ln)
    print()

    if want_sync:
        os.makedirs(SNAPDIR, exist_ok=True)
        snap = os.path.join(SNAPDIR, f"content-plan-{time.strftime('%Y%m%d-%H%M%S')}.csv")
        try:
            with io.open(snap, "w", encoding="utf-8") as f:
                f.write(local)
            with io.open(CSV_LOCAL, "w", encoding="utf-8") as f:
                f.write(live)
            print(f"✅ content-plan.csv обновлён из листа. Прежняя копия: {snap}")
        except OSError as e:
            print(f"❌ не смог записать CSV: {e}", file=sys.stderr)
            return 2
    else:
        print("ℹ️  Ничего не записано (это --check). Обновить CSV: "
              "scripts/content-plan-sync.py --sync")

    print()
    print("⚠️  content-plan.md НЕ ТРОГАЛСЯ, и это осознанно — в нём есть написанное руками, чего в "
          "листе нет\n"
          "    (преамбулы хабов вроде снятия блока на Hub 8, форматирование, перекрёстные ссылки).\n"
          "    Именно его читают агенты на Phase 0, так что расхождения выше надо перенести в него\n"
          "    руками или агентом, и только потом двигать дату в его шапке.\n"
          f"    Сейчас там: {md_synced_line()}")

    if want_notify:
        fp = hashlib.sha1("\n".join(findings).encode("utf-8")).hexdigest()[:16]
        head = findings[0] if findings else "drift"
        notify("📋 Стратегический лист разошёлся с репо\n\n"
               f"{len(findings)} находок. Первая: {head}\n\n"
               f"Разбор: scripts/content-plan-sync.py\n"
               f"Синк CSV: scripts/content-plan-sync.py --sync\n"
               "content-plan.md переносить руками — в нём есть то, чего в листе нет.", fp)
    return 1


def md_synced_line():
    try:
        for line in io.open(MD_LOCAL, encoding="utf-8"):
            if "Last synced from source" in line:
                return line.strip().lstrip("> ").strip()
    except OSError:
        pass
    return "(строку 'Last synced from source' в content-plan.md не нашёл)"


if __name__ == "__main__":
    sys.exit(main())
