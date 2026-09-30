#!/usr/bin/env python3
"""hlth-news-watch.py — nightly scan of HLTH news (hlth.com/insights/news) for outbound triggers.

WHY
---
Vadim 2026-09-30: «сканувати кожен день вночі і на ранок присилати в Telegram овервью новини,
якщо вона корисна для 3DLOOK і аутбаунду — чому корисна і яку кампанію можна запустити».
HLTH posts three healthtech news items every weekday (funding, launches, partnerships,
regulation). A few of them are trigger events for FitXpress segments (GLP-1 telehealth,
online pharmacies, insurers, employer wellness...), and nobody reads the feed daily.

HOW
---
1. The site is Angular SSR over a public JSON API; the same call the page makes returns the
   full text, tags and a stable id — no HTML scraping:
       https://api.prod.hlth.com/api/contents/insights?contentType=News&page=0&pageSize=30
2. Items not yet reported and published in the last --max-age-days go to one headless Claude
   call (`claude -p`, no tools, JSON schema) with the 3DLOOK context: overview.md, the full
   icp-detail.md, the outbound campaigns (hypothesis front matter), the sending profiles.
3. Companies the model names are checked against global-company-registry.json by code
   (existing customer / already in a campaign), not by the model.
4. Report → Telegram (outbound-pipeline.telegram_send). Only items scoring 2-3 get the full
   write-up; 1 is a one-liner; 0 is listed by title so the filter can be sanity-checked.
   A day with nothing at 2-3 is one line.
5. Every item scoring 3 also gets a LinkedIn post for Vadim's own profile (Vadim 2026-09-30:
   «якщо новина має 3 бали — пост на мій LinkedIn, новина з посиланням на повну статтю»).
   Written against brand-assets/linkedin-prompts/linkedin-vadim.md + hard-bans-card.md, then
   gated by post-lint.py (the same gate as every pack post: 170-word wall, sentence length,
   geo in the first sentence, AI tells, numbers only from the news or proof-points); up to two
   rewrites on a hard fail. The post goes to Telegram as its own message, ready to copy.
   The HLTH link sits in the CTA line, outside the linted body: a URL is ~15 "words".
6. The report and the posts are committed and pushed (subject prefix `hlth-news: `). The
   committed JSON carries titles, links and analyses, never the article text: that is HLTH's
   copy, and this repo is public.

Reported = sent to Vadim. A run without --notify prints, commits nothing and marks nothing. A
failed analysis leaves the items unreported, so the next run picks them up with the new ones.
Analyses are cached in the state file and a written post.md is reused (existence = done), so a
retry after a failed send does not pay twice.

Outputs (committed):
    workspace/research/hlth-news/<date>.{md,json}                 the report, analyses
    workspace/social/hlth-news/<hlth-slug>/linkedin-vadim/post.md  score-3 posts
State: ~/.hermes/.hlth-news-state.json · log: ~/.hermes/logs/hlth-news.log (cron)

USAGE
    scripts/hlth-news-watch.py run [--notify] [--max-age-days 4] [--model opus]
    scripts/hlth-news-watch.py status

Exit codes: 0 = ok · 1 = fetch or analysis failed (alert sent with --notify) · 3 = broken setup.
"""
from __future__ import annotations

import argparse
import fcntl
import html
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
MVB = HERE.parent                                     # .../marketing_vb
ROOT = MVB.parent                                     # the git toplevel
PRODUCT = MVB / "brand-assets" / "product-info"
CAMPAIGNS = MVB / "workspace" / "outbound" / "campaigns"
GLOBAL_REG = MVB / "workspace" / "outbound" / "exclusions" / "global-company-registry.json"
OUT_DIR = MVB / "workspace" / "research" / "hlth-news"
POST_DIR = MVB / "workspace" / "social" / "hlth-news"
LI_BRIEF = MVB / "brand-assets" / "linkedin-prompts" / "linkedin-vadim.md"
BANS_CARD = MVB / "brand-assets" / "style-guides" / "hard-bans-card.md"
PIPE = HERE / "outbound-pipeline.py"
REGISTRY = HERE / "outbound-registry.py"
POST_LINT = HERE / "post-lint.py"
POST_PROFILE = "linkedin-vadim"
MAX_POSTS = 2                                         # per run; the profile posts ~1/week
BRANCH = "main"
OWN_SUBJECT = "hlth-news: "                           # every commit this script makes

API = "https://api.prod.hlth.com/api/contents/insights?contentType=News&page=0&pageSize={n}"
PAGE = "https://hlth.com/insights/news/{slug}"
UA = "Mozilla/5.0 (X11; Linux x86_64) 3dlook-hlth-news-watch"

STATE = Path(os.environ.get("HLTH_NEWS_STATE") or os.path.expanduser("~/.hermes/.hlth-news-state.json"))
LOCK = Path(os.environ.get("HLTH_NEWS_LOCK") or os.path.expanduser("~/.hermes/.hlth-news.lock"))
# claude -p runs here: an empty dir, so no project CLAUDE.md or auto-memory leaks into the prompt.
CLAUDE_CWD = Path(os.path.expanduser("~/.hermes/hlth-news-cwd"))
MODEL = os.environ.get("HLTH_NEWS_MODEL", "opus")
FALLBACK_MODEL = "sonnet"
TG_LIMIT = 3800                                       # Telegram caps a message at 4096
TEXT_CAP = 4000                                       # chars of article body per item
KEEP_DAYS = 45                                        # state pruning
STALE_DAYS = 4                                        # newest item older than this = feed stopped

PROFILES = {"katerina": "UK", "nick": "USA", "olena": "Europe / EU", "katya": "Israel",
            "vadim": "Australia"}


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def log(msg: str) -> None:
    print(f"{now_utc():%F %T} {msg}", flush=True)


# ------------------------------------------------------------------------- fetch

def fetch(n: int = 30) -> list[dict]:
    req = urllib.request.Request(API.format(n=n), headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    items = (data.get("data") or {}).get("items")
    if not isinstance(items, list):
        raise ValueError(f"unexpected API shape: {str(data)[:200]}")
    return items


def plain(h: str | None) -> str:
    s = re.sub(r"(?i)<br\s*/?>|</p>|</li>|</h\d>", "\n", h or "")
    s = html.unescape(re.sub(r"<[^>]+>", "", s))
    s = re.sub(r"[ \t ]+", " ", s)
    return re.sub(r"\n\s*\n+", "\n\n", s).strip()


def item_view(it: dict) -> dict:
    return {"id": it["id"], "title": (it.get("title") or "").strip(),
            "date": (it.get("publishDate") or "")[:10], "tags": it.get("tagNames") or [],
            "url": PAGE.format(slug=it.get("slug") or ""),
            "text": plain(it.get("longDescription"))[:TEXT_CAP]}


# ------------------------------------------------------------------------- state

def load_state() -> dict:
    try:
        st = json.loads(STATE.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        st = {}
    st.setdefault("reported", {})        # id -> publish date
    st.setdefault("analyses", {})        # id -> analysis (cache, survives a failed send)
    return st


def save_state(st: dict) -> None:
    cutoff = (now_utc() - timedelta(days=KEEP_DAYS)).strftime("%F")
    st["reported"] = {k: v for k, v in st["reported"].items() if v >= cutoff}
    st["analyses"] = {k: v for k, v in st["analyses"].items() if v.get("_date", "") >= cutoff}
    STATE.parent.mkdir(parents=True, exist_ok=True)
    tmp = STATE.with_suffix(".tmp")
    tmp.write_text(json.dumps(st, ensure_ascii=False, indent=1), encoding="utf-8")
    tmp.replace(STATE)


# ------------------------------------------------------------------------- context

def campaigns_brief() -> str:
    rows = []
    for d in sorted(p for p in CAMPAIGNS.iterdir() if p.is_dir()):
        hyp = d / "hypothesis.md"
        if not hyp.exists():
            continue
        t = hyp.read_text(encoding="utf-8", errors="replace")
        fm = {}
        m = re.match(r"---\n(.*?)\n---", t, re.S)
        if m:
            for line in m.group(1).splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    fm[k.strip()] = v.strip()
        h1 = next((l[2:].strip() for l in t.splitlines() if l.startswith("# ")), "")
        rows.append(f"- {d.name} | profile={fm.get('profile', '?')} | market={fm.get('market', '?')} "
                    f"| status={fm.get('status', '?')} | use_case={fm.get('use_case', '?')} | {h1}")
    return "\n".join(rows)


def registry() -> dict:
    try:
        return json.loads(GLOBAL_REG.read_text(encoding="utf-8")).get("companies", {})
    except (OSError, ValueError):
        return {}


def registry_brief(reg: dict) -> str:
    cust = [v.get("display_name") or k for k, v in reg.items() if v.get("status") == "existing_customer_excluded"]
    manual = [v.get("display_name") or k for k, v in reg.items() if v.get("status") == "manually_excluded"]
    active = [f"{v.get('display_name') or k} ({v.get('covered_by_profile')})"
              for k, v in reg.items() if v.get("status") == "active"]
    return (f"Existing customers (never cold outbound): {', '.join(cust)}\n"
            f"Manually excluded: {', '.join(manual)}\n"
            f"Already contacted by a profile ({len(active)}): {', '.join(active)}")


SYSTEM = """You are the outbound market-intelligence analyst for 3DLOOK. Every morning you read the \
latest healthtech news from HLTH and tell Vadim (marketing lead) which items are useful for 3DLOOK \
sales/outbound, why, and what outbound campaign they justify. You are strict: most HLTH news \
(drug discovery, oncology diagnostics, hospital ops AI, brain-computer interfaces...) is NOT \
useful, and saying so is the right answer. Never invent facts: every claim about the company in \
the news must come from the article text; every claim about 3DLOOK must come from the context."""

TASK = """## Scoring
- 3 = direct trigger: the company in the news is itself a FitXpress/Mobile Tailor ICP account \
(see ICP) and the news gives a fresh reason to reach out now (funding to scale, launch or \
expansion of weight-loss/GLP-1, BMI-gated prescribing, underwriting, wellness/rewards programme, \
remote monitoring, body-composition or progress tracking, clinical trial with anthropometrics, \
uniforms at scale...).
- 2 = segment signal: the company itself is not a realistic account (too big, wrong geo, already \
covered), but the news moves an ICP segment — its lookalikes/competitors become a campaign, or it \
gives a sharp new hook for an existing campaign.
- 1 = weak: tangential (general digital-health trend, maybe a content idea), no concrete play.
- 0 = not relevant to 3DLOOK.

## For every item with score >= 2
- `why`: the concrete link: their pain/workflow -> what FitXpress (or Mobile Tailor) does for it. \
2-3 sentences, specific, no marketing fluff.
- `campaign`: a concrete outbound campaign: which profile sends it (profile markets below; pick \
the geo the targets are in, or "none" if no profile covers it), market, who exactly to target \
(the company itself and/or named lookalike types), which roles, the angle (the hook in 1-2 \
sentences, built on the news trigger), and `existing_campaign` = slug of an existing campaign it \
should feed instead of a new one (or empty). `task` = a one-line English task Vadim can hand to \
the outbound pipeline, e.g. "USA: GLP-1 telehealth platforms that just raised Series B+ — BMI \
verification at intake".
- `caveat`: what could make it a bad idea (company already a customer or contacted — see list, \
geo no profile covers, enterprise too large, regulated claim risk). Empty if none.

## Rules
- Output text fields in Ukrainian (company, product and job-title names stay in English). Short.
- `companies`: every company named in the article (as written), so code can check the registry.
- `segment`: the ICP segment name from icp-detail.md (e.g. "FitXpress §1 Telehealth & GLP-1") or "—".
- Never propose naming a 3DLOOK client in outreach. Never build an angle on "HIPAA compliant", \
"SOC 2 certified", "medical-grade", "FDA-cleared" or any accuracy number — the outbound pipeline \
will reject it.
- For score 0-1 keep `why` to one short sentence and leave `campaign` empty.
- Return one entry per input item, same ids.

## Sending profiles (each sends only to its geo)
{profiles}

## Outbound campaigns so far
{campaigns}

## Outbound registry
{registry}

## 3DLOOK overview
{overview}

## ICP (full)
{icp}

## News items
{items}
"""

SCHEMA = {
    "type": "object",
    "properties": {"items": {"type": "array", "items": {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "score": {"type": "integer", "minimum": 0, "maximum": 3},
            "segment": {"type": "string"},
            "what": {"type": "string", "description": "1-2 sentences: what happened"},
            "why": {"type": "string"},
            "play": {"type": "string", "enum": ["direct_account", "lookalikes", "hook_for_existing",
                                                 "content_only", "none"]},
            "campaign": {"type": "object", "properties": {
                "title": {"type": "string"},
                "profile": {"type": "string", "enum": [*PROFILES, "none"]},
                "market": {"type": "string"},
                "targets": {"type": "string"},
                "roles": {"type": "string"},
                "angle": {"type": "string"},
                "existing_campaign": {"type": "string"},
                "task": {"type": "string"}}},
            "companies": {"type": "array", "items": {"type": "string"}},
            "caveat": {"type": "string"}},
        "required": ["id", "score", "segment", "what", "why", "play", "companies"]}}},
    "required": ["items"],
}


def build_prompt(items: list[dict], reg: dict) -> str:
    news = "\n\n".join(
        f"### id={i['id']}\nTitle: {i['title']}\nDate: {i['date']}\nTags: {', '.join(i['tags'])}\n\n{i['text']}"
        for i in items)
    return TASK.format(
        profiles="\n".join(f"- {p}: {m}" for p, m in PROFILES.items()),
        campaigns=campaigns_brief(), registry=registry_brief(reg),
        overview=(PRODUCT / "overview.md").read_text(encoding="utf-8"),
        icp=(PRODUCT / "icp-detail.md").read_text(encoding="utf-8"),
        items=news)


def claude_bin() -> str:
    return shutil.which("claude") or os.path.expanduser("~/.local/bin/claude")


def claude_json(system: str, prompt: str, schema: dict, model: str) -> tuple[dict, float]:
    """One headless call, no tools, structured output. Raises on any failure."""
    CLAUDE_CWD.mkdir(parents=True, exist_ok=True)
    r = subprocess.run(
        [claude_bin(), "-p", "--model", model, "--tools", "", "--strict-mcp-config",
         "--no-session-persistence", "--output-format", "json",
         "--system-prompt", system, "--json-schema", json.dumps(schema)],
        input=prompt, text=True, capture_output=True, timeout=900, cwd=CLAUDE_CWD)
    out = json.loads(r.stdout or "{}")
    if r.returncode or out.get("is_error"):
        raise RuntimeError(f"rc={r.returncode} {str(out.get('result') or r.stderr)[:300]}")
    return (out.get("structured_output") or json.loads(out.get("result") or "{}"),
            out.get("total_cost_usd") or 0.0)


def analyze(items: list[dict], reg: dict, model: str) -> dict[str, dict]:
    """One headless Claude call for all items. Returns id -> analysis. Raises on failure."""
    prompt = build_prompt(items, reg)
    last = None
    for attempt, m in enumerate([model, model, FALLBACK_MODEL]):
        if attempt:
            time.sleep(90)
        try:
            res, cost = claude_json(SYSTEM, prompt, SCHEMA, m)
            got = {a["id"]: a for a in res.get("items", []) if a.get("id")}
            missing = [i["id"] for i in items if i["id"] not in got]
            if missing:
                raise RuntimeError(f"model skipped {len(missing)} of {len(items)} items")
            log(f"analysis ok: model={m} cost=${cost:.3f} items={len(items)}")
            return got
        except Exception as e:  # noqa: BLE001
            last = e
            log(f"analysis attempt {attempt + 1} ({m}) failed: {type(e).__name__}: {str(e)[:300]}")
    raise RuntimeError(f"analysis failed after 3 attempts: {last}")


# ------------------------------------------------------------------------- LinkedIn post

POST_SYSTEM = """You write LinkedIn posts for Vadim Bilan, marketing at 3DLOOK, on his personal \
profile. The brief below is his, and it is binding. You react to one healthtech news item and \
translate it into what it means for people running health programs at scale, so that his \
audience stops, learns one thing, and opens the full story."""

POST_TASK = """## Task
Write one LinkedIn post by Vadim that reacts to the news item below.

- It is a NEWS post: the reader must learn what happened (name the company, the move) in the \
first lines, then get Vadim's operator take on it: one thing they can use.
- Every fact about the news comes from the article text below. Any number you use must appear in \
the article text as written. Do not quote 3DLOOK numbers.
- FitXpress / 3DLOOK: at most one natural mention and only if it genuinely fits the take. Never \
name a 3DLOOK client. Never claim "HIPAA compliant", "SOC 2 certified", "medical-grade", \
"FDA-cleared", or any accuracy figure.
- English. Body 100-170 words (170 is a hard wall; aim ~140). Most sentences under 15 words, \
none over 30. No country or region name in the first sentence. 0-1 emoji. No hashtags. No em \
dashes. Blank line between short paragraphs. Close the body on a question that needs the \
reader's own numbers or experience.
- Do NOT put the link in `post`. `link_intro` is 2-6 words that lead into the link on its own \
last line (e.g. "Full story on HLTH:"). The code appends the URL.
- `angle`: one line in Ukrainian for Vadim: the take and why it will land with his audience.

## Vadim's LinkedIn brief
{brief}

## Hard bans (the linter enforces these)
{bans}

## 3DLOOK overview (for the one optional FitXpress mention)
{overview}

## Why the analyst flagged this item (internal, do not quote)
{why}

## News item
Title: {title}
Date: {date}
URL: {url}

{text}
"""

POST_SCHEMA = {"type": "object", "properties": {
    "angle": {"type": "string"}, "post": {"type": "string"}, "link_intro": {"type": "string"}},
    "required": ["angle", "post", "link_intro"]}


def post_path(item: dict) -> Path:
    return POST_DIR / item["url"].rsplit("/", 1)[-1] / POST_PROFILE / "post.md"


def post_file(item: dict, gen: dict, day: str) -> str:
    slug = item["url"].rsplit("/", 1)[-1]
    body = gen["post"].strip()
    words = len(re.findall(r"\b[\w'-]+\b", body))
    cta = f"{gen['link_intro'].strip()} {item['url']}"
    return (f"---\nprofile: {POST_PROFILE}\nplatform: linkedin\narticle_slug: hlth-{slug}\n"
            f"product: fitxpress\nformat: text\nstatus: draft\ncreated: {day}\n"
            f"source_url: {item['url']}\n---\n\n"
            f"## Post: {POST_PROFILE} / hlth-{slug}\n\n"
            f"**Angle:** {gen['angle'].strip()}\n"
            f"**Source:** HLTH news, {item['date']}: {item['title']}\n"
            f"**Length:** {words} words / 100-170 words\n\n---\n\n"
            f"{body}\n\n**CTA:** {cta}\n\n---\n\n### Design tip\n\n"
            "**Article visual:** none; LinkedIn renders the HLTH link preview.\n"
            "**Format:** text\n**Adaptation:** No visual needed — native platform format.\n"
            "**Keep:** n/a\n")


def post_for_telegram(path: Path) -> tuple[str, str]:
    """(body + link, the lint-visible angle) from a post.md on disk."""
    sp = _load("social_pack", HERE / "social_pack.py")
    text = path.read_text(encoding="utf-8")
    body, cta, _ = sp.extract_body(text)
    angle = re.search(r"^\*\*Angle:\*\*\s*(.+)$", text, re.M)
    intro, _, url = cta.rpartition(" ")
    return f"{body}\n\n{intro}\n{url}", angle.group(1) if angle else ""


def write_post(item: dict, why: str, model: str, day: str) -> tuple[Path, dict]:
    """Generate, lint, rewrite up to twice. Returns (path, last lint result)."""
    lint_mod = _load("post_lint", POST_LINT)
    path = post_path(item)
    path.parent.mkdir(parents=True, exist_ok=True)
    prompt = POST_TASK.format(
        brief=LI_BRIEF.read_text(encoding="utf-8"), bans=BANS_CARD.read_text(encoding="utf-8"),
        overview=(PRODUCT / "overview.md").read_text(encoding="utf-8"), why=why,
        title=item["title"], date=item["date"], url=item["url"], text=item["text"])
    res = {}
    for attempt in range(3):
        gen, cost = claude_json(POST_SYSTEM, prompt, POST_SCHEMA, model)
        path.write_text(post_file(item, gen, day), encoding="utf-8")
        res = lint_mod.lint(str(path), source_text=item["text"])
        log(f"post {path.parent.parent.name}: attempt {attempt + 1} cost=${cost:.3f} "
            f"{res['verdict']} {res['metrics'].get('words')}w")
        if not res["hard_fails"]:
            break
        fails = "\n".join(f"- [{h['check']}] {h['detail']}" for h in res["hard_fails"])
        prompt += (f"\n\n## Your previous draft failed the linter\n{gen['post']}\n\nHard fails:\n"
                   f"{fails}\n\nRewrite the post fixing exactly these. Keep the take.")
    return path, res


# ------------------------------------------------------------------------- git

def git(*args: str, timeout: int = 120) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True, timeout=timeout)


def commit_and_push(paths: list[Path], subject: str) -> tuple[bool, str]:
    """Commit only our own files; push only if every unpushed commit on main is ours.
    Same guards as outbound-responses-daily.py: someone's local commit is not ours to publish."""
    if git("rev-parse", "--abbrev-ref", "HEAD").stdout.strip() != BRANCH:
        return False, f"не на гілці {BRANCH}"
    gd = Path(git("rev-parse", "--absolute-git-dir").stdout.strip())
    for marker in ("MERGE_HEAD", "rebase-merge", "rebase-apply", "CHERRY_PICK_HEAD", "index.lock"):
        if (gd / marker).exists():
            return False, f"git зайнятий ({marker})"
    rel = [str(p.relative_to(ROOT)) for p in paths if p.exists()]
    if not git("status", "--porcelain", "--", *rel).stdout.strip():
        return True, "нічого комітити"
    r = git("add", "--", *rel)
    if r.returncode == 0:
        r = git("commit", "-q", "-m", subject, "--", *rel)
    if r.returncode:
        return False, f"commit: {(r.stderr or r.stdout).strip()[:200]}"
    sha = git("rev-parse", "--short", "HEAD").stdout.strip()
    foreign = [l for l in git("log", "--format=%s", f"origin/{BRANCH}..{BRANCH}").stdout.splitlines()
               if l and not l.startswith(OWN_SUBJECT)]
    if foreign:
        return False, f"коміт {sha} лишився локально: на {BRANCH} є чужі невідправлені коміти ({foreign[0][:60]})"
    try:
        r = git("push", "-q", "origin", BRANCH)
    except subprocess.TimeoutExpired:
        return False, f"коміт {sha} лишився локально: push завис"
    if r.returncode:
        return False, f"коміт {sha} лишився локально: {r.stderr.strip()[:160]}"
    return True, f"коміт {sha} → origin/{BRANCH}"


# ------------------------------------------------------------------------- registry check

def registry_flags(companies: list[str], reg: dict, norm) -> list[str]:
    flags, seen = [], set()
    for name in companies:
        s = norm(name)
        if not s or s in seen:
            continue
        seen.add(s)
        hit = reg.get(s)
        if not hit:  # "Hims & Hers" vs "hims-hers-health": prefix match on a word boundary
            hit = next((v for k, v in reg.items() if len(s) >= 4 and (k.startswith(s + "-") or s.startswith(k + "-"))), None)
        if not hit:
            continue
        st = hit.get("status")
        if st == "existing_customer_excluded":
            flags.append(f"⛔ {name} — наш клієнт, не холодний аутбаунд")
        elif st == "manually_excluded":
            flags.append(f"⛔ {name} — виключено вручну з аутбаунду")
        elif st == "active":
            flags.append(f"ℹ️ {name} — вже в кампанії {hit.get('campaign_id', '?')} ({hit.get('covered_by_profile', '?')})")
    return flags


# ------------------------------------------------------------------------- render

def ddmm(d: str) -> str:
    return f"{d[8:10]}.{d[5:7]}" if len(d) >= 10 else d


def render(items: list[dict], an: dict[str, dict], reg: dict, norm) -> list[str]:
    """Returns Telegram-sized sections; the first is the header."""
    strong = sorted((i for i in items if an[i["id"]].get("score", 0) >= 2),
                    key=lambda i: -an[i["id"]]["score"])
    weak = [i for i in items if an[i["id"]].get("score", 0) == 1]
    zero = [i for i in items if an[i["id"]].get("score", 0) <= 0]
    dates = sorted({i["date"] for i in items})
    span = ddmm(dates[0]) if len(dates) == 1 else f"{ddmm(dates[0])}–{ddmm(dates[-1])}"
    if not strong:  # Vadim wants the write-up only when it is useful: one short line otherwise
        line = f"📰 HLTH · новини за {span}: {len(items)} шт., під аутбаунд нічого."
        if weak:
            line += "\nСлабкі сигнали: " + "; ".join(i["title"] for i in weak)
        return [line]
    parts = [f"📰 HLTH · новини за {span}: {len(items)} шт., корисних для 3DLOOK — {len(strong)}"]
    for i in strong:
        a = an[i["id"]]
        c = a.get("campaign") or {}
        mark = "🔥" if a["score"] >= 3 else "📌"
        lines = [f"{mark} [{a['score']}/3] {i['title']}",
                 f"Сегмент: {a.get('segment') or '—'}",
                 f"Що сталося: {a.get('what', '')}",
                 f"Чому корисно: {a.get('why', '')}"]
        if c:
            prof = c.get("profile") or "none"
            who = f"{prof} ({PROFILES[prof]})" if prof in PROFILES else "профіль не покриває гео"
            lines.append(f"Кампанія: {c.get('title', '')} — {who}")
            for label, key in (("Кого", "targets"), ("Ролі", "roles"), ("Кут", "angle")):
                if c.get(key):
                    lines.append(f"  {label}: {c[key]}")
            if c.get("existing_campaign"):
                lines.append(f"  Додати в існуючу: {c['existing_campaign']}")
            if c.get("task"):
                lines.append(f"  Задача для пайплайну: {c['task']}")
        lines += registry_flags(a.get("companies") or [], reg, norm)
        if a.get("caveat"):
            lines.append(f"⚠️ {a['caveat']}")
        lines.append(i["url"])
        parts.append("\n".join(lines))
    tail = []
    if weak:
        tail.append("Слабкі сигнали:\n" + "\n".join(f"• {i['title']} — {an[i['id']].get('why', '')}" for i in weak))
    if zero:
        tail.append("Не про нас: " + "; ".join(i["title"] for i in zero))
    if tail:
        parts.append("\n\n".join(tail))
    return parts


def pack(parts: list[str]) -> list[str]:
    msgs, cur = [], ""
    for p in parts:
        p = p if len(p) <= TG_LIMIT else p[:TG_LIMIT - 20] + "\n…(обрізано)"
        if cur and len(cur) + 2 + len(p) > TG_LIMIT:
            msgs.append(cur)
            cur = p
        else:
            cur = f"{cur}\n\n{p}" if cur else p
    if cur:
        msgs.append(cur)
    return msgs


# ------------------------------------------------------------------------- commands

def cmd_run(a) -> int:
    LOCK.parent.mkdir(parents=True, exist_ok=True)
    lock = LOCK.open("w")
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        log("another run holds the lock — exiting")
        return 0
    OP = _load("outbound_pipeline", PIPE)
    norm = _load("outbound_registry", REGISTRY).norm_company
    send = OP.telegram_send if a.notify else (lambda t: print(t + "\n" + "-" * 40) or True)

    st = load_state()
    try:
        raw = fetch()
    except Exception as e:  # noqa: BLE001
        log(f"fetch failed: {type(e).__name__}: {e}")
        if a.notify:
            OP.telegram_send(f"⚠️ HLTH-скан: API не відповів ({type(e).__name__}: {str(e)[:150]}). Спробую наступної ночі.")
        return 1

    cutoff = (now_utc() - timedelta(days=a.max_age_days)).strftime("%F")
    items = [item_view(it) for it in raw
             if it.get("id") and it["id"] not in st["reported"] and (it.get("publishDate") or "")[:10] >= cutoff]
    items.sort(key=lambda i: i["date"])
    items = items[-a.limit:]
    log(f"fetched {len(raw)}, new {len(items)} (cutoff {cutoff})")
    if not items:
        # HLTH posts on weekdays only, so Sunday and Monday mornings are empty by design and
        # stay silent. A feed whose newest item is older than STALE_DAYS (a long weekend is 4)
        # has stopped or moved, and that is worth one line.
        newest = max(raw, key=lambda it: it.get("publishDate") or "", default={})
        nd = (newest.get("publishDate") or "")[:10]
        stale = not nd or nd < (now_utc() - timedelta(days=STALE_DAYS)).strftime("%F")
        msg = f"📰 HLTH: нових новин нема. Остання — {ddmm(nd)} «{(newest.get('title') or '').strip()}»."
        if stale:
            msg += f" Стрічка стоїть понад {STALE_DAYS} дні — перевір hlth.com/insights/news."
        log(msg)
        if a.notify and stale:
            OP.telegram_send(msg)
        return 0

    reg = registry()
    todo = [i for i in items if i["id"] not in st["analyses"]]
    if todo:
        try:
            fresh = analyze(todo, reg, a.model)
        except Exception as e:  # noqa: BLE001
            log(str(e))
            if a.notify:
                OP.telegram_send("⚠️ HLTH-скан: аналіз не вдався (" + str(e)[:200] + "). Новини не втрачено — "
                                 "повторю наступної ночі. Заголовки:\n" + "\n".join(f"• {i['title']}" for i in todo))
            return 1
        for i in todo:
            st["analyses"][i["id"]] = {**fresh[i["id"]], "_date": i["date"]}
        save_state(st)  # cache before sending: a failed send must not pay for the analysis again
    an = {i["id"]: st["analyses"][i["id"]] for i in items}
    day = now_utc().strftime("%F")

    # score 3 -> a LinkedIn post for Vadim. A post.md on disk is done (reused, never rewritten).
    posts, post_errors = [], []
    for i in [i for i in items if an[i["id"]].get("score", 0) >= 3][:MAX_POSTS]:
        path = post_path(i)
        try:
            if path.exists():
                res = _load("post_lint", POST_LINT).lint(str(path), source_text=i["text"])
            else:
                path, res = write_post(i, an[i["id"]].get("why", ""), a.model, day)
            posts.append((i, path, res))
        except Exception as e:  # noqa: BLE001
            log(f"post for {i['title']!r} failed: {type(e).__name__}: {str(e)[:300]}")
            post_errors.append(f"⚠️ Пост до «{i['title']}» не вийшов ({type(e).__name__}). Спробую наступного разу.")

    msgs = pack(render(items, an, reg, norm))
    for i, path, res in posts:
        text, angle = post_for_telegram(path)
        m = res.get("metrics") or {}
        verdict = "лінт ✅" if not res["hard_fails"] else \
            "лінт ⚠️ " + "; ".join(f"[{h['check']}] {h['detail'][:80]}" for h in res["hard_fails"][:3])
        msgs.append(f"✍️ Пост на твій LinkedIn до новини «{i['title']}» · {m.get('words')} слів · {verdict}\n"
                    f"Кут: {angle}\nНаступне повідомлення — текст, готовий до копіювання ↓")
        msgs.append(text)
    msgs += post_errors

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    report_json, report_md = OUT_DIR / f"{day}.json", OUT_DIR / f"{day}.md"
    report_json.write_text(json.dumps(
        {"generated": now_utc().isoformat(timespec="seconds"),
         # no article text: it is HLTH's copy and this repo is public
         "items": [{k: v for k, v in i.items() if k != "text"} for i in items],
         "analyses": an,
         "posts": [str(p.relative_to(MVB)) for _, p, _ in posts]},
        ensure_ascii=False, indent=1), encoding="utf-8")
    report_md.write_text("\n\n---\n\n".join(msgs) + "\n", encoding="utf-8")

    sent = all([send(m) for m in msgs])
    if not a.notify:
        return 0
    if not sent:
        log("Telegram send failed — items stay unreported")
        return 1
    for i in items:
        st["reported"][i["id"]] = i["date"]
    save_state(st)
    log(f"reported {len(items)} items, {len(posts)} post(s), in {len(msgs)} message(s)")

    useful = sum(1 for i in items if an[i["id"]].get("score", 0) >= 2)
    subject = (f"{OWN_SUBJECT}{day} — {len(items)} news, {useful} useful"
               + (f", {len(posts)} LinkedIn post(s)" if posts else ""))
    ok, what = commit_and_push([report_json, report_md, *[p for _, p, _ in posts]], subject)
    log(what)
    if not ok:
        OP.telegram_send(f"⚠️ HLTH: звіт надіслано, але в репо не потрапив — {what}")
    return 0


def cmd_status(a) -> int:
    st = load_state()
    print(f"state: {STATE}")
    print(f"reported: {len(st['reported'])} · cached analyses: {len(st['analyses'])}")
    last = sorted(st["reported"].values())[-1:] or ["—"]
    print(f"newest reported publish date: {last[0]}")
    for p in sorted(OUT_DIR.glob("*.md"))[-5:]:
        print(f"  {p.relative_to(MVB)}")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run", help="fetch, analyse, report")
    r.add_argument("--notify", action="store_true", help="send to Telegram (else print only, mark nothing)")
    r.add_argument("--max-age-days", type=int, default=4, help="ignore items published earlier (default 4)")
    r.add_argument("--limit", type=int, default=20, help="max items per run (newest kept)")
    r.add_argument("--model", default=MODEL, help=f"claude model alias (default {MODEL})")
    sub.add_parser("status", help="what was reported, where the reports are")
    a = ap.parse_args(argv)
    if not (PRODUCT / "icp-detail.md").exists() or not PIPE.exists():
        print("broken setup: marketing_vb context or outbound-pipeline.py missing", file=sys.stderr)
        return 3
    return {"run": cmd_run, "status": cmd_status}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
