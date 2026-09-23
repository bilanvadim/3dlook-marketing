#!/usr/bin/env python3
"""gsc-indexing-watch.py — weekly: which 3dlook.ai pages newly fell out of (or into) Google's index.

WHY
---
Search Console's "Why pages aren't indexed" report is not in the API, and nobody opens the UI
until traffic is already gone. On 2026-09-17 two fresh posts turned out to carry
rel=canonical → glp-1-market (they were WordPress clones of it) and had silently dropped out
of the sitemap; on 2026-09-23 one of them was still "URL is unknown to Google" and the other
still clustered under glp-1-market. Both were found only because someone asked.

So: every sitemap URL through the URL Inspection API (oo connector google_search_console),
diffed against last week's state. Telegram only when something CHANGED — a standing issue
that was already reported is not re-sent, because 11 fashion-era posts that Google will
never index would turn this into noise within a month.

What counts as news:
  🔴 new problem   — a URL that was indexed (or unseen) and now is not
  🔁 changed       — a non-indexed URL whose coverage state or Google canonical moved
  🟢 fixed         — was not indexed, now is
  ⏳ still unknown — "URL is unknown to Google" ≥ 7 days after it entered the sitemap (once)
  ➖ left sitemap  — was in the sitemap last week, is not now (the canonical-bug symptom:
                     a page with a foreign canonical is dropped by Yoast from the sitemap)
Failures (sitemap unreadable, oo not authorised, >10% of inspections failed) always ping,
and do NOT overwrite the state — a half-run must not make next week's diff look clean.

Notes (see memory reference_gsc_indexing_audit):
  * 3dlook.ai answers 503 to parallel curl → sitemaps are fetched sequentially with retries.
  * inspect_url ≈ 8 s each, 8 in parallel is fine, quota 2000/day (~200 used per run).
  * Requesting indexing is UI-only; the message says which URLs need the button.

USAGE
    gsc-indexing-watch.py                 # run, print report, do not send
    gsc-indexing-watch.py --notify        # send to Telegram if anything is new / on failure
    gsc-indexing-watch.py --baseline      # record current state silently (first run)
    gsc-indexing-watch.py --from-dir DIR  # reuse saved inspect_url JSONs (debug / baseline)
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

SITE = "sc-domain:3dlook.ai"
SITEMAP_INDEX = "https://3dlook.ai/sitemap_index.xml"
OO = str(Path.home() / ".local" / "bin" / "oo")
STATE = Path.home() / ".hermes" / ".gsc-indexing-state.json"
PIPE = Path(__file__).with_name("outbound-pipeline.py")
UA = "Mozilla/5.0 (compatible; 3dlook-gsc-watch)"
WORKERS = 8
UNKNOWN_GRACE_DAYS = 7
TG_LIMIT = 3800
MEDIA = re.compile(r"\.(jpe?g|png|webp|gif|svg|pdf)$", re.I)


def now() -> datetime:
    return datetime.now(timezone.utc)


def short(u: str) -> str:
    return u.replace("https://3dlook.ai", "") or "/"


# ------------------------------------------------------------------ sitemap

def fetch(url: str, tries: int = 5) -> str:
    last = ""
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=30) as r:
                body = r.read().decode("utf-8", "replace")
            if "<loc>" in body:
                return body
            last = f"no <loc> in {len(body)}-byte body"
        except Exception as e:  # noqa: BLE001 — 503s are routine here, retry them all
            last = f"{type(e).__name__}: {e}"
        time.sleep(3 * (i + 1))
    raise RuntimeError(f"{url}: {last}")


def sitemap_urls() -> list[str]:
    subs = re.findall(r"<loc>([^<]+)</loc>", fetch(SITEMAP_INDEX))
    urls: list[str] = []
    for s in subs:
        time.sleep(1)
        urls += [u for u in re.findall(r"<loc>([^<]+)</loc>", fetch(s)) if not MEDIA.search(u)]
    return sorted(set(urls))


# ------------------------------------------------------------------ inspection

def parse(raw: str) -> dict:
    r = json.loads(raw)["data"]["inspectionResult"]["indexStatusResult"]
    return {
        "verdict": r.get("verdict", ""),
        "state": r.get("coverageState", ""),
        "google_canonical": r.get("googleCanonical", ""),
        "user_canonical": r.get("userCanonical", ""),
        "last_crawl": (r.get("lastCrawlTime") or "")[:10],
    }


def inspect(url: str, from_dir: Path | None) -> tuple[str, dict | None, str]:
    if from_dir:
        f = from_dir / (hashlib.md5(url.encode()).hexdigest()[:12] + ".json")
        try:
            return url, parse(f.read_text()), ""
        except Exception as e:  # noqa: BLE001
            return url, None, f"{type(e).__name__}"
    err = ""
    for i in range(3):
        p = subprocess.run(
            [OO, "connector", "run", "google_search_console", "-a", "inspect_url", "--json",
             "-d", json.dumps({"siteUrl": SITE, "inspectionUrl": url})],
            capture_output=True, text=True, timeout=180)
        try:
            return url, parse(p.stdout), ""
        except Exception:  # noqa: BLE001
            err = (p.stdout + p.stderr).strip().replace("\n", " ")[:200]
            time.sleep(5 * (i + 1))
    return url, None, err


# ------------------------------------------------------------------ diff

def diff(prev: dict, cur: dict, today: str) -> dict:
    out = {k: [] for k in ("new", "changed", "fixed", "unknown", "left")}
    for u, c in cur.items():
        p = prev.get(u)
        ok = c["verdict"] == "PASS"
        if p is None:
            if not ok and c["state"] != "URL is unknown to Google":
                out["new"].append(u)
            continue
        was_ok = p["verdict"] == "PASS"
        if not ok and was_ok:
            out["new"].append(u)
        elif ok and not was_ok:
            out["fixed"].append(u)
        elif not ok and (p["state"] != c["state"] or p["google_canonical"] != c["google_canonical"]):
            out["changed"].append(u)
        if (not ok and c["state"] == "URL is unknown to Google" and not c.get("unknown_reported")
                and (datetime.fromisoformat(today) - datetime.fromisoformat(c["first_seen"])).days
                >= UNKNOWN_GRACE_DAYS):
            out["unknown"].append(u)
            c["unknown_reported"] = True
    out["left"] = sorted(u for u in prev if u not in cur)
    return out


def line(u: str, c: dict, prev: dict | None = None) -> str:
    s = f"• {short(u)}\n   {c['state']}"
    if prev and prev.get("state") != c["state"]:
        s = f"• {short(u)}\n   {prev['state']} → {c['state']}"
    if c["google_canonical"] and c["google_canonical"] != u:
        s += f"\n   Google выбрал канонической: {short(c['google_canonical'])}"
    if c["user_canonical"] and c["user_canonical"] != u:
        s += f"\n   ⚠️ наш canonical указывает на: {short(c['user_canonical'])}"
    if c["last_crawl"]:
        s += f" · обход {c['last_crawl']}"
    return s


def report(d: dict, cur: dict, prev: dict, stats: str) -> str:
    parts = [f"🔎 Индексация 3dlook.ai — что нового за неделю\n{stats}"]
    sec = [("new", "🔴 Новые проблемы — выпали из индекса или сразу не попали"),
           ("changed", "🔁 Изменился статус проблемной страницы"),
           ("unknown", f"⏳ Google не знает о странице ≥{UNKNOWN_GRACE_DAYS} дней после появления в сайтмапе — нужен Request indexing"),
           ("fixed", "🟢 Вернулись в индекс")]
    for k, title in sec:
        if d[k]:
            parts.append(title + "\n" + "\n".join(line(u, cur[u], prev.get(u)) for u in sorted(d[k])))
    if d["left"]:
        parts.append("➖ Пропали из сайтмапа (сняты с публикации — или canonical на чужую страницу, как было с wellness/coaching 17.09)\n"
                     + "\n".join(f"• {short(u)}" for u in d["left"]))
    parts.append("Request indexing — только в интерфейсе GSC → URL Inspection.")
    text = "\n\n".join(parts)
    return text if len(text) <= TG_LIMIT else text[:TG_LIMIT - 40] + "\n…(обрезано, полный список в логе)"


def send(text: str) -> bool:
    spec = importlib.util.spec_from_file_location("outbound_pipeline", PIPE)
    op = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(op)
    return op.telegram_send(text)


# ------------------------------------------------------------------ main

def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--notify", action="store_true")
    ap.add_argument("--baseline", action="store_true")
    ap.add_argument("--from-dir", type=Path)
    ap.add_argument("--urls", type=Path, help="URL list instead of fetching the sitemap")
    a = ap.parse_args(argv)
    ts = now().strftime("%Y-%m-%d %H:%M UTC")
    today = now().date().isoformat()

    def fail(msg: str) -> int:
        print(f"[{ts}] FAIL {msg}")
        if a.notify:
            send(f"⚠️ Проверка индексации 3dlook.ai не отработала ({ts})\n{msg}\nСостояние не обновлено; следующий запуск сравнит с прошлой неделей.")
        return 1

    try:
        urls = a.urls.read_text().split() if a.urls else sitemap_urls()
    except Exception as e:  # noqa: BLE001
        return fail(f"Сайтмап не читается: {e}")
    if len(urls) < 50:
        return fail(f"В сайтмапе всего {len(urls)} URL — похоже на сбой сайта, а не на правду.")

    with cf.ThreadPoolExecutor(WORKERS) as ex:
        res = list(ex.map(lambda u: inspect(u, a.from_dir), urls))
    errs = [(u, e) for u, r, e in res if r is None]
    if len(errs) > len(urls) * 0.1:
        return fail(f"URL Inspection упал на {len(errs)}/{len(urls)} URL (oo не авторизован или квота?). Пример: {errs[0][1]}")

    prev_all = json.loads(STATE.read_text()) if STATE.exists() else {}
    prev = prev_all.get("urls", {})
    cur: dict[str, dict] = {}
    for u, r, _ in res:
        if r is None:  # keep last known state for the few that errored
            if u in prev:
                cur[u] = prev[u]
            continue
        r["first_seen"] = prev.get(u, {}).get("first_seen", today)
        if prev.get(u, {}).get("unknown_reported") and r["state"] == "URL is unknown to Google":
            r["unknown_reported"] = True
        cur[u] = r

    n_ok = sum(1 for c in cur.values() if c["verdict"] == "PASS")
    stats = f"{len(urls)} URL в сайтмапе · в индексе {n_ok} · не в индексе {len(urls) - n_ok}"
    if errs:
        stats += f" · {len(errs)} не проверились"
    print(f"[{ts}] {stats}")

    if a.baseline or not prev:
        STATE.write_text(json.dumps({"checked": ts, "urls": cur}, ensure_ascii=False, indent=1))
        print("baseline recorded, nothing sent")
        return 0

    d = diff(prev, cur, today)
    STATE.write_text(json.dumps({"checked": ts, "urls": cur}, ensure_ascii=False, indent=1))
    if not any(d.values()):
        print("no changes")
        return 0
    text = report(d, cur, prev, stats)
    print(text)
    if a.notify and not send(text):
        print("Telegram send failed")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
