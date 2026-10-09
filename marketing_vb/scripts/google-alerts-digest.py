#!/usr/bin/env python3
"""google-alerts-digest.py — daily Google Alerts digest from Vadim's mailbox to a Slack channel.

WHY
---
Vadim 2026-10-09: «налаштувати гугл алерти на мою пошту і щоб вони також пересилалися ...
в канал слаку. про компанію, продукти, конкурентів та ключові слова» + «додати Вадима
Роговського, Вітні Каткарт та Катерину Галіч». Google Alerts has no API and an alert delivers
to one mailbox only. A raw Gmail forward would need the recipient to confirm a code and would
pass on the noise as is: the old `3dlook` alert mostly catches "a 3D look" in games and sports.

HOW
---
1. Alerts are created by hand at google.com/alerts under vadim.bilan@3dlook.me (ALERTS below is
   the list; `links` prints one prefilled link per alert). They land in his inbox as usual.
2. This script reads new alert mail through `oo connector run gmail` (same account), splits
   each mail into items (query, news/web/blogs, text block, real URL behind google.com/url) and
   dedupes by URL across alerts and days. Links to our own sites are dropped by code.
3. One headless Claude call (`claude -p`, no tools, JSON schema, empty cwd so no CLAUDE.md or
   memory leaks in) keeps what is really about the watched entity or the market and drops
   namesakes. It returns a clean title, the source and a one-line note in English.
4. One message to the Slack channel (`oo connector run slack post_message`, Vadim's identity),
   grouped: 3DLOOK / people / products / competitors / market. Nothing relevant = no post.
   Everything in Slack is English (Vadim 2026-10-09: «все має бути на англ в слаці»).
   The same digest goes as an HTML email from his mailbox to --email / $GOOGLE_ALERTS_EMAIL_TO
   (Vadim 2026-10-09: «давай ще Каті Галіч на пошту відправляти»), after the Slack post, so a
   failed Slack post never leaves a sent email behind to be duplicated on the retry.
5. Failures go to Vadim's Telegram. Mail older than the lookback is never touched, and so is
   the inbox: the script only reads.

Posted = processed. Without --post the script prints and marks nothing. Analyses are cached in
the state file, so a retry after a failed post does not pay twice.

State: ~/.hermes/.google-alerts-state.json · log: ~/.hermes/logs/google-alerts.log (cron)

USAGE
    scripts/google-alerts-digest.py run [--post] [--channel C0...] [--email a@x,b@y] [--lookback-days 3]
    scripts/google-alerts-digest.py links        # prefilled google.com/alerts links
    scripts/google-alerts-digest.py status

Exit codes: 0 = ok · 1 = gmail, analysis or Slack failed (Telegram alert with --post) · 3 = setup.
"""
from __future__ import annotations

import argparse
import fcntl
import hashlib
import html
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.parse
from datetime import datetime, timedelta, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
MVB = HERE.parent
OVERVIEW = MVB / "brand-assets" / "product-info" / "overview.md"
PIPE = HERE / "outbound-pipeline.py"                 # telegram_send

OO = shutil.which("oo") or str(Path.home() / ".local" / "bin" / "oo")
GMAIL_QUERY = "from:googlealerts-noreply@google.com newer_than:{days}d"
CHANNEL = os.environ.get("GOOGLE_ALERTS_SLACK_CHANNEL", "")
EMAIL_TO = os.environ.get("GOOGLE_ALERTS_EMAIL_TO", "")       # comma-separated
STATE = Path(os.environ.get("GOOGLE_ALERTS_STATE") or os.path.expanduser("~/.hermes/.google-alerts-state.json"))
LOCK = Path(os.path.expanduser("~/.hermes/.google-alerts.lock"))
CLAUDE_CWD = Path(os.path.expanduser("~/.hermes/google-alerts-cwd"))
MODEL = os.environ.get("GOOGLE_ALERTS_MODEL", "sonnet")
FALLBACK_MODEL = "opus"
OWN_HOSTS = ("3dlook.ai", "3dlook.me")
KEEP_DAYS = 60                                       # state pruning
SILENT_DAYS = 7                                      # no alert mail this long = alerts broken

# The alerts Vadim keeps at google.com/alerts. Defaults there are right for all but the
# Cyrillic one (Language → Any). Edit here, then `links`, then create the new ones by hand.
ALERTS = [
    ("company", '"3DLOOK"', "en"),
    ("people", '"Katerina Galich" OR "Kateryna Galich"', "en"),
    ("people", '"Whitney Cathcart"', "en"),
    ("people", '"Vadim Rogovskiy" OR "Vadym Rohovskyi"', "en"),
    ("people", '"Вадим Роговський" OR "Вадим Роговский" OR "Катерина Галич"', "uk"),
    ("product", '"FitXpress"', "en"),
    ("product", '"Mobile Tailor"', "en"),
    ("product", '"wrist measurement" OR "wrist sizing" OR "wrist sizer" app OR smartphone OR API OR AI OR online', "en"),
    ("competitor", '"Prism Labs"', "en"),
    ("competitor", '"Bodygram"', "en"),
    ("competitor", '"Size Stream" OR "SizeStream"', "en"),
    ("competitor", 'Spren BMI OR "body composition" OR "body scan"', "en"),
    ("competitor", '"Styku" OR "Fit3D"', "en"),
    ("competitor", '"InBody" "body composition" OR BIA OR scanner', "en"),
    ("competitor", '"Perfect Corp" wrist OR bracelet OR watch OR jewelry', "en"),
    ("competitor", '"GlamAR"', "en"),
    ("market", '"body scanning" OR "body scan" smartphone OR app OR AI', "en"),
    ("market", '"body composition" GLP-1 telehealth OR app OR remote', "en"),
    ("market", '"BMI verification" OR "verified BMI" OR "BMI fraud" OR "weight verification"', "en"),
    ("market", '"made-to-measure" OR uniforms "body scanning" OR "3D body scan" OR "digital measuring"', "en"),
    ("market", '"virtual try-on" watch OR bracelet OR jewelry', "en"),
]

SECTIONS = [("company", "3DLOOK"), ("people", "People"), ("product", "Products"),
            ("competitor", "Competitors"), ("market", "Market")]


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def log(msg: str) -> None:
    print(f"{now_utc():%F %T} {msg}", flush=True)


class Broken(RuntimeError):
    pass


def oo(args: list[str], timeout: int = 180) -> dict:
    try:
        p = subprocess.run([OO, *args, "--json"], capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        raise Broken(f"oo timed out after {timeout}s: {' '.join(args[:4])}")
    if p.returncode:
        raise Broken(f"oo exit {p.returncode}: {(p.stderr or p.stdout).strip()[:400]}")
    try:
        return json.loads(p.stdout)["data"]
    except (ValueError, KeyError):
        raise Broken(f"unexpected oo output: {p.stdout[:400]}")


# ------------------------------------------------------------------------- state

def load_state() -> dict:
    try:
        st = json.loads(STATE.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        st = {}
    for k in ("messages", "urls", "analyses"):
        st.setdefault(k, {})                         # gmail id / url / item key -> date or analysis
    return st


def save_state(st: dict) -> None:
    cutoff = (now_utc() - timedelta(days=KEEP_DAYS)).strftime("%F")
    for k in ("messages", "urls"):
        st[k] = {i: d for i, d in st[k].items() if d >= cutoff}
    st["analyses"] = {i: a for i, a in st["analyses"].items() if a.get("_date", "") >= cutoff}
    STATE.parent.mkdir(parents=True, exist_ok=True)
    tmp = STATE.with_suffix(".tmp")
    tmp.write_text(json.dumps(st, ensure_ascii=False, indent=1), encoding="utf-8")
    tmp.replace(STATE)


# ------------------------------------------------------------------------- gmail

def fetch_mail(days: int, limit: int = 100) -> list[dict]:
    data = oo(["connector", "run", "gmail", "-a", "fetch_emails", "-d", json.dumps(
        {"query": GMAIL_QUERY.format(days=days), "maxResults": limit, "detail": "full"})])
    return data.get("messages") or []


# "=== Новини - 2 нові результати за запитом [3dlook] ===" / "=== News - 1 new result for [x] ==="
HEAD = re.compile(r"^=== (.+?) - .*\[(.+)\] ===$")
LINK = re.compile(r"^<(https://www\.google\.com/url\?[^>]+)>$")
KINDS = {"новини": "news", "news": "news", "веб-пошук": "web", "web": "web",
         "блоги": "blogs", "blogs": "blogs", "відео": "video", "video": "video"}


def real_url(gurl: str) -> str:
    q = urllib.parse.parse_qs(urllib.parse.urlparse(gurl).query)
    return (q.get("url") or [gurl])[0]


def parse(text: str) -> list[dict]:
    """Split one alert mail (one alert, or a digest of several) into items."""
    items, query, kind, buf = [], "", "", []
    for line in text.replace("\r", "").split("\n"):
        line = line.rstrip()
        if line.startswith("- - - - -"):
            break                                    # footer: unsubscribe links
        m = HEAD.match(line)
        if m:
            kind = KINDS.get(m.group(1).strip().lower(), m.group(1).strip().lower())
            query, buf = m.group(2), []
            continue
        m = LINK.match(line)
        if m and query:
            url = real_url(m.group(1))
            block = " ".join(l.strip() for l in buf if l.strip())
            items.append({"key": hashlib.sha1(url.encode()).hexdigest()[:12], "url": url,
                          "query": query, "kind": kind, "text": block[:700]})
            buf = []
            continue
        buf.append(line)
    return items


def own_site(url: str) -> bool:
    host = urllib.parse.urlparse(url).netloc.lower()
    return any(host == h or host.endswith("." + h) for h in OWN_HOSTS)


# ------------------------------------------------------------------------- analysis

SYSTEM = """You triage Google Alerts for the marketing team of 3DLOOK, a body-scanning company \
(two smartphone photos -> 3D body model and body measurements, via API/SDK). Alerts match words, \
not meaning, so most hits are namesakes. You keep what the team should see and drop the rest."""

TASK = """## Watched entities
- Company: 3DLOOK (also written 3DLook; NOT the phrase "3D look" or "a 3D look at ...").
- People: Katerina (Kateryna) Galich, CEO; Whitney Cathcart, co-founder and CCO; Vadim \
Rogovskiy (Vadym Rohovskyi, Вадим Роговський), co-founder. Keep only these people, not namesakes.
- Products: FitXpress (health and fitness body scanning), Mobile Tailor (apparel and uniform \
measurements), 3DLOOK wrist measurement (3dlook.ai/wrist-measurement/: wrist size from two \
smartphone photos via API, mapped to a brand's size chart; for jewelry, bracelets, watches, \
wearables; it has no product name of its own). "Mobile Tailor" as a generic tailoring service \
is a namesake; medical wrist studies (carpal tunnel, wrist circumference as a health marker) \
are noise for the wrist product.
- Direct competitors: Prism Labs (mobile body composition scanning, NOT other "Prism" \
companies), Bodygram, Size Stream.
- Adjacent: Spren (body composition app, NOT the fantasy-novel "spren"), Styku, Fit3D, InBody \
(bioimpedance body composition, NOT the phrase "in body"). For wrist measurement: Perfect Corp \
and GlamAR, AR virtual try-on vendors that bundle an online wrist sizer (keep only their \
wrist, watch, bracelet or jewelry news, not makeup or beauty AR).
- Market: news that matters for selling body scanning to telehealth / GLP-1 / weight-loss \
programs, online pharmacies (BMI verification), insurers, employer wellness, fitness apps, \
made-to-measure apparel and uniform makers, and online sizing for jewelry, watch and wearable \
brands (wrist sizing, virtual try-on for watches and bracelets). Generic diet, gym or fashion \
content is noise.

## Rules
- keep=true only if the item is really about a watched entity, or is a concrete market \
development (launch, funding, partnership, regulation, study, notable case) in the areas above.
- 3DLOOK's own job ads and its own social posts: keep=false (drop_reason "own content").
- Competitor job ads: keep=true, category competitor, note says what role they hire for.
- category: company | people | product | competitor | market.
- entity: the watched name the item is about (e.g. "Bodygram"), or "" for market items.
- title: the article title as published, cleaned of site suffixes like " - YouTube" or \
" | LinkedIn". source: the publication or site name.
- note: English, at most 20 words: what happened and, if not obvious, why it matters for 3DLOOK. \
Facts only from the item text. No em dashes.
- drop_reason: a few English words when keep=false, else "".
- Return every item id exactly once.

## 3DLOOK overview
{overview}

## Items
{items}
"""

SCHEMA = {"type": "object", "properties": {"items": {"type": "array", "items": {
    "type": "object", "properties": {
        "id": {"type": "string"}, "keep": {"type": "boolean"},
        "category": {"type": "string", "enum": [s for s, _ in SECTIONS]},
        "entity": {"type": "string"}, "title": {"type": "string"}, "source": {"type": "string"},
        "note": {"type": "string"}, "drop_reason": {"type": "string"}},
    "required": ["id", "keep", "category", "entity", "title", "source", "note", "drop_reason"]}}},
    "required": ["items"]}


def claude_json(prompt: str, model: str) -> tuple[dict, float]:
    CLAUDE_CWD.mkdir(parents=True, exist_ok=True)
    claude = shutil.which("claude") or os.path.expanduser("~/.local/bin/claude")
    r = subprocess.run(
        [claude, "-p", "--model", model, "--tools", "", "--strict-mcp-config",
         "--no-session-persistence", "--output-format", "json",
         "--system-prompt", SYSTEM, "--json-schema", json.dumps(SCHEMA)],
        input=prompt, text=True, capture_output=True, timeout=900, cwd=CLAUDE_CWD)
    out = json.loads(r.stdout or "{}")
    if r.returncode or out.get("is_error"):
        raise RuntimeError(f"rc={r.returncode} {str(out.get('result') or r.stderr)[:300]}")
    return (out.get("structured_output") or json.loads(out.get("result") or "{}"),
            out.get("total_cost_usd") or 0.0)


def analyze(items: list[dict], model: str) -> dict[str, dict]:
    listing = "\n\n".join(f"id: {i['key']}\nalert: {i['query']} ({i['kind']})\nurl: {i['url']}\n"
                          f"text: {i['text']}" for i in items)
    prompt = TASK.format(overview=OVERVIEW.read_text(encoding="utf-8"), items=listing)
    last = None
    for attempt, m in enumerate([model, model, FALLBACK_MODEL]):
        if attempt:
            time.sleep(60)
        try:
            res, cost = claude_json(prompt, m)
            got = {a["id"]: a for a in res.get("items", []) if a.get("id")}
            missing = [i["key"] for i in items if i["key"] not in got]
            if missing:
                raise RuntimeError(f"model skipped {len(missing)} of {len(items)} items")
            log(f"analysis ok: model={m} cost=${cost:.3f} items={len(items)}")
            return got
        except Exception as e:  # noqa: BLE001
            last = e
            log(f"analysis attempt {attempt + 1} ({m}) failed: {type(e).__name__}: {str(e)[:300]}")
    raise RuntimeError(f"analysis failed after 3 attempts: {last}")


# ------------------------------------------------------------------------- render

def esc(s: str) -> str:
    return html.escape(s or "", quote=False)         # Slack mrkdwn escapes & < > only


def digest(items: list[dict], an: dict[str, dict], day: str) -> tuple[str, list, int]:
    """(headline, [(section label, [(item, analysis, who)])], dropped) shared by Slack and email."""
    kept = [i for i in items if an[i["key"]]["keep"]]
    n = len(kept)
    date = datetime.strptime(day, "%Y-%m-%d").strftime("%b %-d")
    head = f"Google Alerts · {date} · {n} mention{'' if n == 1 else 's'}"
    groups = []
    for cat, label in SECTIONS:
        group = sorted((i for i in kept if an[i["key"]]["category"] == cat),
                       key=lambda i: an[i["key"]].get("entity", ""))
        if group:
            groups.append((label, [(i, an[i["key"]], an[i["key"]].get("entity", "")
                                    if cat in ("competitor", "people") else "") for i in group]))
    return head, groups, len(items) - n


def render(items: list[dict], an: dict[str, dict], day: str) -> str:
    head, groups, dropped = digest(items, an, day)
    title, _, count = head.rpartition(" · ")
    lines = [f"*{title}* · {count}"]
    for label, rows in groups:
        lines += ["", f"*{label}*"]
        for i, a, who in rows:
            who = f"*{esc(who)}* · " if who else ""
            src = f" · _{esc(a['source'])}_" if a.get("source") else ""
            lines.append(f"• {who}<{i['url']}|{esc(a['title'] or i['url'])}>{src}")
            if a.get("note"):
                lines.append(f"    {esc(a['note'])}")
    if dropped:
        lines += ["", f"_Filtered out as noise: {dropped}_"]
    return "\n".join(lines)


def render_email(items: list[dict], an: dict[str, dict], day: str) -> tuple[str, str]:
    head, groups, dropped = digest(items, an, day)
    e = lambda s: html.escape(s or "")               # noqa: E731
    out = ['<div style="font-family:Arial,Helvetica,sans-serif;font-size:14px;line-height:1.45;'
           'color:#1a1a1a;max-width:640px">', f'<p style="font-size:16px"><b>{e(head)}</b></p>']
    for label, rows in groups:
        out.append(f'<h3 style="font-size:15px;margin:18px 0 6px">{e(label)}</h3>'
                   '<ul style="padding-left:18px;margin:0">')
        for i, a, who in rows:
            who = f"<b>{e(who)}</b> · " if who else ""
            src = f" · <i>{e(a['source'])}</i>" if a.get("source") else ""
            note = f'<br><span style="color:#555">{e(a["note"])}</span>' if a.get("note") else ""
            out.append(f'<li style="margin-bottom:8px">{who}<a href="{e(i["url"])}">'
                       f'{e(a["title"] or i["url"])}</a>{src}{note}</li>')
        out.append("</ul>")
    foot = f"Filtered out as noise: {dropped}. " if dropped else ""
    out.append(f'<p style="color:#777;font-size:12px;margin-top:18px">{foot}'
               "Daily digest of Google Alerts on 3DLOOK, our people, products, competitors and market.</p>")
    out.append("</div>")
    return head, "".join(out)


# ------------------------------------------------------------------------- deliver


def slack_post(channel: str, text: str) -> None:
    oo(["connector", "run", "slack", "-a", "post_message", "-d", json.dumps(
        {"channelId": channel, "text": text, "unfurlLinks": False, "unfurlMedia": False})])


def send_email(to: list[str], subject: str, body: str) -> None:
    oo(["connector", "run", "gmail", "-a", "send_email", "-d", json.dumps(
        {"to": to[0], "extraRecipients": to[1:], "subject": subject, "body": body, "isHtml": True}
        if to[1:] else {"to": to[0], "subject": subject, "body": body, "isHtml": True})])


# ------------------------------------------------------------------------- commands

def cmd_run(a) -> int:
    LOCK.parent.mkdir(parents=True, exist_ok=True)
    lock = LOCK.open("w")
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        log("another run holds the lock — exiting")
        return 0
    channel = a.channel or CHANNEL
    emails = [x.strip() for x in (a.email or EMAIL_TO).split(",") if x.strip()]
    if a.post and not channel:
        print("no Slack channel: pass --channel or set GOOGLE_ALERTS_SLACK_CHANNEL", file=sys.stderr)
        return 3
    tg = None
    if a.post:
        spec = importlib.util.spec_from_file_location("outbound_pipeline", PIPE)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        tg = mod.telegram_send

    st = load_state()
    day = now_utc().strftime("%F")
    try:
        mails = fetch_mail(a.lookback_days)
    except Broken as e:
        log(f"gmail failed: {e}")
        if tg:
            tg(f"⚠️ Google Alerts → Slack: пошта не читається ({str(e)[:200]}). Спробую завтра.")
        return 1
    new_mail = [m for m in mails if m["messageId"] not in st["messages"]]
    log(f"alert mails in {a.lookback_days}d: {len(mails)}, new {len(new_mail)}")

    if not mails:
        # Daily alerts on 3DLOOK alone come every few days; a full week of silence means the
        # alerts were deleted or delivery broke. One Telegram line per silent spell.
        try:
            recent = fetch_mail(SILENT_DAYS, limit=1)
        except Broken:
            recent = [None]
        if not recent and st.get("silent_warned") != day and tg:
            tg(f"⚠️ Google Alerts: за {SILENT_DAYS} днів не прийшло жодного листа від алертів. "
               "Перевір google.com/alerts під vadim.bilan@3dlook.me.")
            st["silent_warned"] = day
            save_state(st)
        return 0

    items, seen = [], set()
    for m in sorted(new_mail, key=lambda m: m["messageTimestamp"]):
        for it in parse(m.get("messageText") or ""):
            if it["url"] in st["urls"] or it["url"] in seen:
                continue
            seen.add(it["url"])
            items.append(it)
    own = [i for i in items if own_site(i["url"])]
    items = [i for i in items if not own_site(i["url"])]
    log(f"items: {len(items)} new, {len(own)} own-site dropped")

    if items:
        todo = [i for i in items if i["key"] not in st["analyses"]]
        if todo:
            try:
                fresh = analyze(todo, a.model)
            except Exception as e:  # noqa: BLE001
                log(str(e))
                if tg:
                    tg(f"⚠️ Google Alerts → Slack: аналіз не вдався ({str(e)[:200]}). "
                       "Листи не втрачено, повторю завтра.")
                return 1
            for i in todo:
                st["analyses"][i["key"]] = {**fresh[i["key"]], "_date": day}
            if a.post:
                save_state(st)                       # a failed post must not pay again
        an = {i["key"]: st["analyses"][i["key"]] for i in items}
        kept = sum(1 for i in items if an[i["key"]]["keep"])
        text = render(items, an, day)
        if not a.post:
            print(text)
            if kept and emails:
                print(f"\n(email to {', '.join(emails)}: «{render_email(items, an, day)[0]}»)")
            for i in items:
                if not an[i["key"]]["keep"]:
                    print(f"  [drop] {i['query']} · {an[i['key']].get('drop_reason')} · {i['text'][:90]}")
            return 0
        if kept:
            try:
                slack_post(channel, text)
            except Broken as e:
                log(f"slack failed: {e}")
                tg(f"⚠️ Google Alerts → Slack: пост не пройшов ({str(e)[:200]}). Повторю завтра.")
                return 1
            if emails:
                try:
                    send_email(emails, *render_email(items, an, day))
                    log(f"emailed: {', '.join(emails)}")
                except Broken as e:
                    # Slack already has it, so the items are still marked done: a retry would
                    # post to Slack twice. Vadim gets the failure and can forward by hand.
                    log(f"email failed: {e}")
                    tg(f"⚠️ Google Alerts: у Slack дайджест пішов, а лист на {', '.join(emails)} — ні "
                       f"({str(e)[:200]}). Перешли вручну, якщо треба.")
        log(f"posted: {kept} kept, {len(items) - kept} dropped" if kept else
            f"nothing relevant ({len(items)} dropped) — no post")
    elif not a.post:
        print("нових згадок немає")
        return 0

    for m in new_mail:
        st["messages"][m["messageId"]] = day
    for i in items + own:
        st["urls"][i["url"]] = day
    save_state(st)
    return 0


def cmd_links(a) -> int:
    for cat, q, hl in ALERTS:
        url = "https://www.google.com/alerts?" + urllib.parse.urlencode({"q": q, "hl": hl})
        print(f"{cat:<11} {q}\n            {url}")
    return 0


def cmd_status(a) -> int:
    st = load_state()
    print(f"state: {STATE}")
    print(f"mails processed: {len(st['messages'])} · urls seen: {len(st['urls'])} · "
          f"cached analyses: {len(st['analyses'])}")
    print(f"last processed: {max(st['messages'].values(), default='—')}")
    print(f"channel: {CHANNEL or '— (set GOOGLE_ALERTS_SLACK_CHANNEL or pass --channel)'}")
    print(f"email: {EMAIL_TO or '— (set GOOGLE_ALERTS_EMAIL_TO or pass --email)'}")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run", help="read new alert mail, filter, post the digest")
    r.add_argument("--post", action="store_true", help="post to Slack and mark processed (else print only)")
    r.add_argument("--channel", default="", help="Slack channel id (default $GOOGLE_ALERTS_SLACK_CHANNEL)")
    r.add_argument("--email", default="", help="comma-separated recipients (default $GOOGLE_ALERTS_EMAIL_TO)")
    r.add_argument("--lookback-days", type=int, default=3, help="gmail newer_than window (default 3)")
    r.add_argument("--model", default=MODEL, help=f"claude model alias (default {MODEL})")
    sub.add_parser("links", help="prefilled google.com/alerts link per alert")
    sub.add_parser("status", help="what was processed")
    a = ap.parse_args(argv)
    if not OVERVIEW.exists() or not PIPE.exists() or not Path(OO).exists():
        print("broken setup: overview.md, outbound-pipeline.py or oo missing", file=sys.stderr)
        return 3
    return {"run": cmd_run, "links": cmd_links, "status": cmd_status}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
