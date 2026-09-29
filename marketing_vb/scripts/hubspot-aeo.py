#!/usr/bin/env python3
"""hubspot-aeo.py — read HubSpot AEO (AI-search visibility) for 3dlook.ai. Read-only.

WHY THIS EXISTS
---------------
HubSpot AEO (portal 6014382, app.hubspot.com/ai-visibility) sends our tracked prompts through
ChatGPT, Gemini and Perplexity every day. It records whether 3DLOOK is mentioned, which pages
get cited, and what HubSpot suggests publishing next. The official way to reach this data is the
"HubSpot connector" for Claude/ChatGPT
(knowledge.hubspot.com/seo/use-aeo-with-the-hubspot-connector).

We do not need a second connection. The `oo` HubSpot connection already authenticates against
the same remote MCP server (mcp.hubspot.com). The AEO tools are not exposed as
`oo connector run` actions, but `oo connector proxy` sends raw JSON-RPC to the server with oo's
OAuth, and the AEO tools answer. That means no new app, no new token and no Super Admin approval.

READ-ONLY BY RULE
  HubSpot is read-only for us. This script refuses two operations with exit 2:
  manage_aeo_prompts CREATE, which adds tracked prompts, runs them immediately and uses up the
  prompt capacity, and manage_aeo_recommendations START_ACTION. Add or remove prompts in the UI:
  https://app.hubspot.com/ai-visibility/6014382/prompts

THREE CONSUMERS
  * People, ad hoc: status / prompts / prompt / competitors / citations / recs / snapshot.
  * The SEO pipeline: `topic` writes workspace/seo/_aeo/{date}-{slug}.yaml. It contains the
    tracked prompts ranked by overlap with the article topic, the open HubSpot recommendations
    for it, and the pages AI assistants cite for the closest prompts. context-pack-builder §7e
    passes this file to seo-planner as `aeo_signals`. These are the questions buyers really ask
    AI assistants, so the plan can answer them directly (usually in the FAQ).
  * Cron, weekly: `watch --notify` compares the last 7 days with the 7 before and sends Telegram.
    The report covers visibility per assistant, prompts that moved, our pages that AI started or
    stopped citing, articles published in the last 60 days and whether they are cited yet, and
    new or changed recommendations. This is the "after publication" loop. A new article is
    checked every week without anyone having to remember it.

DATA NOTES, LEARNED FROM THE API ON 2026-09-29 (do not re-derive)
  * The COMPETITORS section does not reconcile with ASSISTANT_BREAKDOWN. Over 7 days there
    were 576 responses and ASSISTANT_BREAKDOWN counted 471 competitor mentions, but
    COMPETITORS gave sizestream 6,631 mentions. The share-of-voice percentages are also computed
    over a much larger base: all five tracked brands together come to about 16%. Treat
    COMPETITORS as a relative ranking only. Before quoting a competitor number anywhere, check it
    in the HubSpot UI. Our own-brand count matches ASSISTANT_BREAKDOWN ownedMentions.
  * `filters` apply only to SUMMARY and PROMPTS. CITATIONS, COMPETITORS and ASSISTANT_BREAKDOWN
    are always portal-wide for the date window.
  * CITATIONS returns domains (top 50), not URLs. Page-level data comes from two places: a
    prompt DETAIL call (the citationUrls of every run) and CITATION_ANALYSIS for one URL, which
    is what `citations --url` runs.
  * Page-level counts summed from DETAIL come out below CITATIONS.ownedCitations for the same
    week (392 vs 493 for 2026-09-22…28). `watch` uses the DETAIL counts only to rank pages and
    to spot pages appearing or disappearing. The headline figure is ownedCitations. Never add
    the two together or compare one with the other.
  * Being cited is not the same as being named. On 2026-09-29 the DXA-alternatives page was
    cited 33 times on "What are the best alternatives to DEXA scans…", yet that prompt's
    visibility was 0%. The assistants used the page as a source and still did not name 3DLOOK.
  * setupStatus.inputProfileConfigured=false means AEO setup is not finished. Empty sections are
    expected in that case, so do not report them as "no data yet".
  * Prompt DETAIL returns the full AI answer text for every run and can be large. The server
    caps it at 25 runs, which is more than one week of runs (7 days x 3 assistants = 21).
  * The plan covers three assistants: CHATGPT, GEMINI and PERPLEXITY. The CLAUDE and
    GOOGLE_AI_* enum values exist but have no runs.
  * `visibility` is the percentage of responses that mention the brand
    (mentionCount / responseCount). In one week a prompt gets about 21 responses, so a single
    response moves it by about 5 points. `watch` only reports moves of 15 points or more.
  * The runs happen daily at about 05:00-09:00 UTC. The weekly windows end yesterday, so a run
    in progress never cuts a window short.

USAGE
    scripts/hubspot-aeo.py status                 # visibility, run freshness, prompt capacity
    scripts/hubspot-aeo.py prompts [--below 20] [--phase AWARENESS]
    scripts/hubspot-aeo.py prompt <id> [--assistant CHATGPT] [--runs 3] [--full]
    scripts/hubspot-aeo.py competitors            # relative only, see DATA NOTES
    scripts/hubspot-aeo.py citations [--url https://3dlook.ai/content-hub/...]
    scripts/hubspot-aeo.py recs [--status NEW] [--type CONTENT] [--id <rec id>]
    scripts/hubspot-aeo.py snapshot [--out-dir workspace/research/aeo]
    scripts/hubspot-aeo.py topic "<seed topic>" --slug <slug> [--terms "extra words"] [--out <path>]
    scripts/hubspot-aeo.py watch [--notify]       # cron: Mon 06:47 UTC
  common: --from YYYY-MM-DD --to YYYY-MM-DD (default: the last 30 days) · --json

  workspace/research/aeo/ (snapshots, weekly reports) is excluded in .git/info/exclude. The
  remote is PUBLIC, and a full dump of prompts, competitor data and HubSpot's ICP profiles is
  strategy, the same reasoning as hubspot-findings.md. The per-article `topic` file is
  committed with its article, like the Ahrefs `_keywords` file. It holds no money and no
  competitor figures.
Exit: 0 ok · 2 refused · 3 broken setup / API error.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import importlib.util
import json
import math
import re
import shutil
import subprocess
import sys
import textwrap
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlsplit

MCP_URL = "https://mcp.hubspot.com/"
PORTAL = 6014382
PROMPTS_URL = f"https://app.hubspot.com/ai-visibility/{PORTAL}/prompts"
# cron has no ~/.local/bin on PATH, hence the fallback (same as gsc-indexing-watch.py)
OO = shutil.which("oo") or str(Path.home() / ".local" / "bin" / "oo")
REPO = Path(__file__).resolve().parent.parent
DEFAULT_OUT = REPO / "workspace" / "research" / "aeo"
TOPIC_DIR = REPO / "workspace" / "seo" / "_aeo"
ARTICLES = REPO / "workspace" / "seo" / "articles"
STATE = Path.home() / ".hermes" / ".aeo-watch-state.json"
PIPE = Path(__file__).with_name("outbound-pipeline.py")
TG_LIMIT = 3800
MOVE_POINTS = 15          # a weekly prompt has ~21 responses; one response is ~5 points
FRESH_DAYS = 60           # "recently published" for the weekly citation check
ASSISTANTS = ("CHATGPT", "GEMINI", "PERPLEXITY", "CLAUDE", "GOOGLE_AI_MODE", "GOOGLE_AI_OVERVIEWS")
ASSISTANT_NAMES = {"CHATGPT": "ChatGPT", "GEMINI": "Gemini", "PERPLEXITY": "Perplexity",
                   "CLAUDE": "Claude", "GOOGLE_AI_MODE": "AI Mode", "GOOGLE_AI_OVERVIEWS": "AI Overviews"}
PHASES = ("AWARENESS", "CONSIDERATION", "EVALUATION", "DECISION")
REC_STATUSES = ("NEW", "IN_PROGRESS", "COMPLETED", "ARCHIVED", "FAILED", "DISMISSED", "DRAFT_CREATED")
OPEN_RECS = ("NEW", "IN_PROGRESS")
READ_TOOLS = {"get_aeo_metrics", "manage_aeo_prompts", "manage_aeo_recommendations", "tool_guidance"}
READ_OPERATIONS = {"manage_aeo_prompts": {"DETAIL"}, "manage_aeo_recommendations": {"LIST", "DETAIL"}}
STOPWORDS = set("""a an and are as at be by can could do does for from how i in into is it its of on or
our should that the their them these this those to vs was we what when where which who why will
with without you your include including""".split())


class Broken(Exception):
    """oo or HubSpot failed. Exit 3."""


class Refused(Exception):
    """A write operation was requested. Exit 2."""


# ------------------------------------------------------------------ transport

def call(tool: str, arguments: dict) -> dict:
    """One MCP tools/call through `oo connector proxy`, returning the tool's JSON payload."""
    if tool not in READ_TOOLS:
        raise Refused(f"{tool} is not an AEO read tool")
    op = (arguments.get("operation") or {}).get("_operationType")
    if tool in READ_OPERATIONS and op not in READ_OPERATIONS[tool]:
        raise Refused(f"{tool} {op} writes to HubSpot; HubSpot is read-only for us. "
                      f"Manage prompts in the UI: {PROMPTS_URL}")
    if not Path(OO).exists():
        raise Broken(f"`oo` CLI not found (looked on PATH and at {OO})")
    body = {"jsonrpc": "2.0", "id": 1, "method": "tools/call",
            "params": {"name": tool, "arguments": arguments}}
    cmd = [OO, "connector", "proxy", "hubspot", "--method", "POST", "--endpoint", MCP_URL,
           "--headers", json.dumps({"Content-Type": "application/json",
                                    "Accept": "application/json, text/event-stream"}),
           "--body", json.dumps(body), "--json"]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    except subprocess.TimeoutExpired:
        raise Broken(f"oo proxy timed out after 180s on {tool}")
    if proc.returncode != 0:
        raise Broken(f"oo proxy exit {proc.returncode}: {(proc.stderr or proc.stdout).strip()[:500]}")
    try:
        rpc = json.loads(proc.stdout)["data"]["data"]
    except (ValueError, KeyError, TypeError):
        raise Broken(f"unexpected oo proxy output: {proc.stdout[:500]}")
    if "error" in rpc:
        raise Broken(f"MCP error on {tool}: {json.dumps(rpc['error'])[:500]}")
    result = rpc.get("result") or {}
    text = "".join(c.get("text", "") for c in result.get("content", []) if c.get("type") == "text")
    if result.get("isError"):
        raise Broken(f"{tool} returned an error: {text[:500]}")
    try:
        return json.loads(text)
    except ValueError:
        return {"text": text}


def metrics(include: list[str], date_from: str, date_to: str, **extra) -> dict:
    data = call("get_aeo_metrics", {"include": include, "startDate": date_from, "endDate": date_to, **extra})
    if (data.get("setupStatus") or {}).get("inputProfileConfigured") is False:
        raise Broken("AEO setup is not complete for this business unit (no input profile). "
                     "Empty sections are expected until setup is finished.")
    return data


def list_recs(business_unit: int, status: str | None = None) -> list[dict]:
    op = {"_operationType": "LIST", "businessUnitId": business_unit, "limit": 100}
    if status:
        op["status"] = status
    return call("manage_aeo_recommendations", {"operation": op}).get("recommendations") or []


def prompt_runs(prompt_id: int, date_from: str, date_to: str, max_runs: int = 25) -> dict:
    return call("manage_aeo_prompts", {"operation": {
        "_operationType": "DETAIL", "promptId": prompt_id, "startDate": date_from,
        "endDate": date_to, "maxRuns": max_runs}})


# ------------------------------------------------------------------ helpers

def ts(ms: int | None) -> str:
    if not ms:
        return "-"
    return _dt.datetime.fromtimestamp(ms / 1000, _dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def prompt_rows(data: dict) -> list[dict]:
    return (data.get("prompts") or {}).get("prompts") or []


TRACKING = re.compile(r"^(utm_\w+|ref|fbclid|gclid|srsltid|hl)$")


def norm_url(u: str) -> str:
    """One page, one key. Tracking params go and our paths get the trailing slash WordPress
    serves. Other query params stay: play.google.com/store/apps/details?id=… is a different app
    per id, and dropping it merged every app store listing into one fake "most cited" URL."""
    s = urlsplit(u.strip())
    host = s.netloc.lower().removeprefix("www.")
    path = s.path or "/"
    if is_ours(u) and not path.endswith("/") and "." not in path.rsplit("/", 1)[-1]:
        path += "/"
    query = "&".join(kv for kv in s.query.split("&") if kv and not TRACKING.match(kv.split("=", 1)[0]))
    return f"https://{host}{path}" + (f"?{query}" if query else "")


def is_ours(u: str) -> bool:
    host = urlsplit(u).netloc.lower().removeprefix("www.")
    return host == "3dlook.ai" or host.endswith(".3dlook.ai")


def short(u: str) -> str:
    return u.replace("https://3dlook.ai", "") or "/"


def tokens(text: str) -> set[str]:
    out = set()
    for w in re.findall(r"[a-z0-9]+", (text or "").lower()):
        if w in STOPWORDS or (w.isdigit() and len(w) < 2) or len(w) < 2:
            continue
        if len(w) > 4 and w.endswith("ies"):
            w = w[:-3] + "y"
        elif len(w) > 3 and w.endswith("s") and not w.endswith("ss"):
            w = w[:-1]
        out.add(w)
    return out


def cited_ours(runs: list[dict]) -> Counter:
    c: Counter = Counter()
    for run in runs:
        for u in run.get("citationUrls") or []:
            if is_ours(u):
                c[norm_url(u)] += 1
    return c


# ------------------------------------------------------------------ formatting

def fmt_status(data: dict, date_from: str, date_to: str) -> str:
    s, r, lim = data.get("summary") or {}, data.get("runStatus") or {}, data.get("limits") or {}
    return "\n".join([
        f"HubSpot AEO · portal {PORTAL} · {date_from} → {date_to}",
        f"  visibility (avg):   {s.get('averageVisibility')}%",
        f"  prompts tracked:    {s.get('totalPrompts')}  (capacity {lim.get('promptsUsed')}/"
        f"{lim.get('promptsCapacity')}, onCredits={lim.get('onCredits')})",
        f"  AI responses:       {s.get('totalResponses')}  with a 3DLOOK mention: "
        f"{s.get('totalRunsWithMentions')}",
        f"  citations:          {s.get('totalCitations')}",
        f"  competitors/answer: {s.get('averageCompetitorsMentioned')}",
        f"  last run:           {ts(r.get('lastRunCompletedAt'))}"
        f"{'  (RUN IN PROGRESS)' if r.get('runInProgress') else ''}",
        f"  next run:           {ts(r.get('nextScheduledRun'))}",
    ])


def fmt_prompts(rows: list[dict]) -> str:
    out = ["  vis | ment/resp | phase  | loc | ICP                      | id           | prompt"]
    for p in rows:
        icp = ",".join(p.get("icpNames") or [])[:24]
        out.append(f"{p.get('visibility'):>5} | {p.get('mentionCount'):>4}/{p.get('responseCount'):<4} | "
                   f"{(p.get('buyingJourneyPhase') or '-')[:6]:6} | {(p.get('location') or '-')[:3]:3} | "
                   f"{icp:24} | {p.get('id')} | {p.get('prompt')}")
    return "\n".join(out)


def fmt_assistants(data: dict) -> str:
    out = ["assistant   | runs | runs w/ 3DLOOK | 3DLOOK mentions | competitor mentions | citations (ours)"]
    for a in (data.get("assistantBreakdown") or {}).get("byAssistant") or []:
        out.append(f"{a['assistant']:11} | {a.get('totalRuns'):>4} | {a.get('runsWithMentions'):>14} | "
                   f"{a.get('ownedMentions'):>15} | {a.get('competitorMentions'):>19} | "
                   f"{a.get('totalCitations')} ({a.get('ownedCitations')})")
    return "\n".join(out)


def fmt_competitors(data: dict) -> str:
    brands = sorted((data.get("competitors") or {}).get("brands") or [],
                    key=lambda b: b.get("mentionCount") or 0, reverse=True)
    out = ["COMPETITORS: relative ranking only; counts do not reconcile with the assistant table "
           "(see DATA NOTES)", "brand                | domain            | mentions | SoV %"]
    for b in brands:
        out.append(f"{(b.get('brandName') or '')[:20]:20} | {(b.get('domain') or '')[:17]:17} | "
                   f"{b.get('mentionCount'):>8} | {round(b.get('sharePercent') or 0, 2)}")
    return "\n".join(out)


def fmt_citations(data: dict, top: int = 25) -> str:
    c = data.get("citations") or {}
    out = [f"citations: {c.get('totalCitations')} total · ours {c.get('ownedCitations')} · "
           f"others {c.get('nonOwnedCitations')}", "  count | domain"]
    for d in (c.get("topDomains") or [])[:top]:
        flag = " (ours)" if d.get("ownedDomain") else " (competitor)" if d.get("competitorDomain") else ""
        out.append(f"  {d.get('citationCount'):>5} | {d.get('domain')}{flag}")
    return "\n".join(out)


def fmt_recs(recs: list[dict]) -> str:
    out = ["id         | status    | prio   | type      | title  →  content title"]
    for r in recs:
        title = r.get("title") or ""
        if r.get("contentTitle"):
            title += f"  →  {r['contentTitle']}"
        out.append(f"{r.get('id'):<10} | {(r.get('status') or '')[:9]:9} | {(r.get('priority') or '')[:6]:6} | "
                   f"{(r.get('type') or '')[:9]:9} | {title}")
    return "\n".join(out)


def emit(args, payload, text: str) -> None:
    print(json.dumps(payload, ensure_ascii=False, indent=1) if args.json else text)


# ------------------------------------------------------------------ ad-hoc commands

def cmd_status(args) -> None:
    data = metrics(["SUMMARY", "RUN_STATUS", "LIMITS"], args.date_from, args.date_to)
    emit(args, data, fmt_status(data, args.date_from, args.date_to))


def cmd_prompts(args) -> None:
    rows = prompt_rows(metrics(["PROMPTS"], args.date_from, args.date_to))
    if args.phase:
        rows = [p for p in rows if p.get("buyingJourneyPhase") == args.phase]
    if args.below is not None:
        rows = [p for p in rows if (p.get("visibility") or 0) < args.below]
    rows.sort(key=lambda p: (p.get("visibility") or 0, p.get("prompt") or ""))
    emit(args, rows, f"{len(rows)} prompts, lowest visibility first\n" + fmt_prompts(rows))


def cmd_prompt(args) -> None:
    op = {"_operationType": "DETAIL", "promptId": args.id, "startDate": args.date_from,
          "endDate": args.date_to, "maxRuns": args.runs}
    if args.assistant:
        op["aiAssistant"] = args.assistant
    data = call("manage_aeo_prompts", {"operation": op})
    if args.json:
        emit(args, data, "")
        return
    p = data.get("prompt") or {}
    out = [f"{p.get('prompt')}",
           f"  id {p.get('id')} · {p.get('buyingJourneyPhase')} · {p.get('location')} · "
           f"ICP {', '.join(p.get('icpNames') or [])} · product {', '.join(p.get('productNames') or [])}"]
    for run in data.get("runs") or []:
        out += ["", f"--- run {ts(run.get('completedAt'))} · model {run.get('aiModel')} · 3DLOOK mentions "
                    f"{run.get('ownedMentions')} · competitor mentions {run.get('competitorMentions')} · "
                    f"citations {run.get('totalCitations')} (ours {run.get('ownedCitations')})"]
        text = run.get("responseText") or ""
        out.append(text if args.full else textwrap.shorten(text.replace("\n", " "), 900, placeholder=" …"))
        out += [f"    cite: {u}" for u in run.get("citationUrls") or []]
    recs = data.get("recommendations") or []
    if recs:
        out += ["", "open recommendations for this prompt:", fmt_recs(recs)]
    print("\n".join(out))


def cmd_competitors(args) -> None:
    data = metrics(["COMPETITORS", "ASSISTANT_BREAKDOWN"], args.date_from, args.date_to)
    emit(args, data, fmt_assistants(data) + "\n\n" + fmt_competitors(data))


def cmd_citations(args) -> None:
    if args.url:
        data = metrics(["CITATION_ANALYSIS"], args.date_from, args.date_to, citationUrl=args.url)
        emit(args, data, json.dumps(data.get("citationAnalysis", data), ensure_ascii=False, indent=1))
    else:
        data = metrics(["CITATIONS"], args.date_from, args.date_to)
        emit(args, data, fmt_citations(data, top=50))


def cmd_recs(args) -> None:
    if args.id:
        data = call("manage_aeo_recommendations",
                    {"operation": {"_operationType": "DETAIL", "recommendationId": args.id}})
        emit(args, data, json.dumps(data, ensure_ascii=False, indent=1))
        return
    recs = list_recs(args.business_unit, args.status)
    if args.type:
        recs = [r for r in recs if r.get("type") == args.type]
    order = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}
    recs.sort(key=lambda r: (order.get(r.get("priority"), 3), -(r.get("score") or 0)))
    emit(args, recs, f"{len(recs)} recommendations\n" + fmt_recs(recs))


def cmd_snapshot(args) -> None:
    data = metrics(["SUMMARY", "RUN_STATUS", "LIMITS", "PROMPTS", "CITATIONS", "COMPETITORS",
                    "ASSISTANT_BREAKDOWN", "ICPS_AND_PRODUCTS"], args.date_from, args.date_to)
    data["recommendations"] = list_recs(args.business_unit)
    data["_meta"] = {"portal": PORTAL, "from": args.date_from, "to": args.date_to,
                     "pulled_at": _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds")}
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = out_dir / args.date_to
    stem.with_suffix(".json").write_text(json.dumps(data, ensure_ascii=False, indent=1))
    rows = sorted(prompt_rows(data), key=lambda p: p.get("visibility") or 0)
    new = [r for r in data["recommendations"] if r.get("status") == "NEW"]
    md = "\n\n".join([
        f"# HubSpot AEO snapshot {args.date_to}",
        "```\n" + fmt_status(data, args.date_from, args.date_to) + "\n```",
        "## Prompts (lowest visibility first)\n\n```\n" + fmt_prompts(rows) + "\n```",
        "## By assistant\n\n```\n" + fmt_assistants(data) + "\n```",
        "## Cited domains\n\n```\n" + fmt_citations(data) + "\n```",
        "## Competitors\n\n```\n" + fmt_competitors(data) + "\n```",
        f"## New recommendations ({len(new)})\n\n```\n" + fmt_recs(new) + "\n```",
    ]) + "\n"
    stem.with_suffix(".md").write_text(md)
    emit(args, {"json": str(stem.with_suffix(".json")), "md": str(stem.with_suffix(".md"))},
         f"wrote {stem.with_suffix('.json')}\nwrote {stem.with_suffix('.md')}")


# ------------------------------------------------------------------ topic (SEO pipeline)

def rank(topic: set[str], docs: dict[int, str]) -> dict[int, float]:
    """Overlap score weighted by rarity. `body` and `scanning` sit in almost every prompt and
    weigh ~0, while `bariatric` or `dxa` carry the match. Used for ordering only. The planner
    judges relevance."""
    toks = {k: tokens(v) for k, v in docs.items()}
    df = Counter(w for t in toks.values() for w in t)
    n = max(len(toks), 1)
    return {k: round(sum(math.log((n + 1) / df[w]) for w in topic & t), 2) for k, t in toks.items()}


def cmd_topic(args) -> None:
    import yaml

    slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", args.slug)
    topic = tokens(f"{args.seed} {args.terms or ''}")
    data = metrics(["SUMMARY", "PROMPTS"], args.date_from, args.date_to)
    rows = prompt_rows(data)
    recs = [r for r in list_recs(args.business_unit) if r.get("status") in OPEN_RECS]

    docs = {p["id"]: p.get("prompt") or "" for p in rows}
    docs.update({r["id"]: " ".join(str(r.get(k) or "") for k in ("title", "contentTitle", "contentTopic", "summary"))
                 for r in recs})
    score = rank(topic, docs)

    matched = sorted((p for p in rows if score[p["id"]] > 0), key=lambda p: -score[p["id"]])[:8]
    prompts_out = []
    for i, p in enumerate(matched):
        item = {"id": p["id"], "prompt": p.get("prompt"), "visibility": p.get("visibility"),
                "phase": p.get("buyingJourneyPhase"), "icp": ", ".join(p.get("icpNames") or []),
                "match": score[p["id"]]}
        if i < 3:  # what the assistants cite for the three closest questions
            runs = prompt_runs(p["id"], args.date_from, args.date_to).get("runs") or []
            cites = Counter(norm_url(u) for run in runs for u in run.get("citationUrls") or [])
            item["runs_checked"] = len(runs)
            item["runs_naming_3dlook"] = sum(1 for run in runs if (run.get("ownedMentions") or 0) > 0)
            item["ai_cites"] = [{"url": u, "count": c, "ours": is_ours(u)} for u, c in cites.most_common(6)]
        prompts_out.append(item)

    rec_rows = sorted((r for r in recs if score[r["id"]] > 0),
                      key=lambda r: (-score[r["id"]], {"HIGH": 0, "MEDIUM": 1}.get(r.get("priority"), 2)))[:5]
    recs_out = [{"id": r["id"], "priority": r.get("priority"), "type": r.get("type"), "status": r.get("status"),
                 "title": r.get("title"), "content_title": r.get("contentTitle"),
                 "content_topic": r.get("contentTopic"), "summary": r.get("summary"),
                 "influencing_citations": (r.get("influencingCitations") or [])[:4],
                 "match": score[r["id"]]} for r in rec_rows]

    doc = {
        "source": f"HubSpot AEO, portal {PORTAL}, via scripts/hubspot-aeo.py topic",
        "pulled": _dt.date.today().isoformat(),
        "window": {"from": args.date_from, "to": args.date_to},
        "assistants": ["ChatGPT", "Gemini", "Perplexity"],
        "seed": args.seed,
        "portal_visibility_avg": (data.get("summary") or {}).get("averageVisibility"),
        "tracked_prompts_total": len(rows),
        "note": ("visibility = % of AI answers that name 3DLOOK. match = shared rare words with the "
                 "topic, an ordering hint only: judge relevance yourself. Prompt texts are raw buyer "
                 "queries (they may say DEXA); canon wording still applies in the article."),
        "matched_prompts": prompts_out,
        "no_prompt_covers_topic": not prompts_out,
        "open_recommendations": recs_out,
    }
    out = Path(args.out) if args.out else TOPIC_DIR / f"{_dt.date.today().isoformat()}-{slug}.yaml"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(yaml.safe_dump(doc, allow_unicode=True, sort_keys=False, width=100))
    emit(args, {"file": str(out), "matched_prompts": len(prompts_out), "recommendations": len(recs_out)},
         f"wrote {out}\n  matched prompts: {len(prompts_out)} · open recommendations: {len(recs_out)}"
         + ("\n  no tracked prompt shares a rare word with this topic" if not prompts_out else ""))


# ------------------------------------------------------------------ watch (weekly cron)

def fresh_articles(today: _dt.date) -> dict[str, str]:
    """published_url → "YYYY-MM-DD" (or "YYYY-MM-DD оновл.") for pages that went live, or were
    refreshed in place, in the last FRESH_DAYS days.

    Two writers, two field names. Hand captures carry `published_date`; `capture-live.py` carries
    `article_published_time` (WordPress og time). A refresh in place keeps its ORIGINAL publish
    time (accuracy-drives-roi: 2026-01-07, refreshed 2026-09-23), so when the publish date is old,
    the capture date in the file name stands in for "live in this form since"."""
    import yaml

    out: dict[str, str] = {}
    for f in ARTICLES.glob("*/published-live-*.md"):
        text = f.read_text(errors="replace")
        if not text.startswith("---"):
            continue
        try:
            fm = yaml.safe_load(text.split("---", 2)[1]) or {}
        except yaml.YAMLError:
            continue
        url = fm.get("published_url")
        pub = str(fm.get("published_date") or fm.get("article_published_time") or "")[:10]
        m = re.search(r"published-live-(\d{4}-\d{2}-\d{2})", f.name)
        if not url or not m:
            continue
        age = lambda d: (today - _dt.date.fromisoformat(d)).days  # noqa: E731
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", pub) and age(pub) <= FRESH_DAYS:
            label = pub
        elif age(m.group(1)) <= FRESH_DAYS:
            label = f"{m.group(1)} оновл."
        else:
            continue
        u = norm_url(url)
        out[u] = min(out.get(u, label), label)
    return out


def pct_delta(cur, prev) -> str:
    if cur is None or prev is None:
        return ""
    d = round(cur - prev, 1)
    return f" ({'+' if d >= 0 else ''}{d} п.п.)"


def assistant_line(cur: dict, prev: dict) -> str:
    pa = {a["assistant"]: a for a in (prev.get("assistantBreakdown") or {}).get("byAssistant") or []}
    parts = []
    for a in (cur.get("assistantBreakdown") or {}).get("byAssistant") or []:
        p = pa.get(a["assistant"], {})
        runs, hit = a.get("totalRuns") or 0, a.get("runsWithMentions") or 0
        was = f", було {p.get('runsWithMentions')}/{p.get('totalRuns')}" if p else ""
        parts.append(f"{ASSISTANT_NAMES.get(a['assistant'], a['assistant'])} {hit}/{runs}{was}")
    return " · ".join(parts)


def build_report(win: dict, cur: dict, prev: dict, recs: list[dict], cited: Counter,
                 cited_prompts: dict, fresh: dict[str, str], state: dict, failed: list[str]) -> str:
    sc, sp = cur.get("summary") or {}, prev.get("summary") or {}
    cc, cp = cur.get("citations") or {}, prev.get("citations") or {}
    first = not state
    lines = [f"📈 HubSpot AEO · тиждень {win['cur_from'][5:]}…{win['cur_to'][5:]} "
             f"(ChatGPT · Gemini · Perplexity)",
             f"Видимість 3DLOOK: {sc.get('averageVisibility')}%{pct_delta(sc.get('averageVisibility'), sp.get('averageVisibility'))}"
             f" · відповідей зі згадкою {sc.get('totalRunsWithMentions')}/{sc.get('totalResponses')}",
             f"Цитування наших сторінок: {cc.get('ownedCitations')} з {cc.get('totalCitations')}"
             f" (тиждень тому {cp.get('ownedCitations')} з {cp.get('totalCitations')})",
             f"По асистентах (відповіді зі згадкою): {assistant_line(cur, prev)}"]

    prev_vis = {p["id"]: p.get("visibility") for p in prompt_rows(prev)}
    rows = prompt_rows(cur)
    moves = sorted(((p.get("visibility") - prev_vis[p["id"]], p) for p in rows
                    if p["id"] in prev_vis and p.get("visibility") is not None and prev_vis[p["id"]] is not None
                    and abs(p.get("visibility") - prev_vis[p["id"]]) >= MOVE_POINTS),
                   key=lambda x: -abs(x[0]))
    zero = sum(1 for p in rows if not p.get("visibility"))
    zero_prev = sum(1 for p in prompt_rows(prev) if not p.get("visibility"))
    block = [f"\nПромпти: {len(rows)} · на нулі {zero} (тиждень тому {zero_prev})"]
    for d, p in moves[:6]:
        block.append(f"{'🟢' if d > 0 else '🔴'} {'+' if d > 0 else ''}{round(d)} → {p.get('visibility')}% · "
                     f"{textwrap.shorten(p.get('prompt') or '', 80, placeholder='…')}")
    if not moves:
        block.append(f"Жоден промпт не зрушив на {MOVE_POINTS}+ п.п.")
    new_prompts = [p for p in rows if p["id"] not in prev_vis]
    if new_prompts and prev_vis:
        block.append(f"🆕 нових промптів: {len(new_prompts)}")
    lines += block

    prev_cited = state.get("cited") or {}
    lines.append(f"\nНаші сторінки у відповідях ШІ: {len(cited)} URL")
    if not first:
        appeared = [u for u in cited if u not in prev_cited]
        gone = [u for u in prev_cited if u not in cited]
        for u in appeared[:5]:
            lines.append(f"🆕 {short(u)} · {cited[u]}× (промптів: {len(cited_prompts[u])})")
        for u in gone[:5]:
            lines.append(f"➖ зникла: {short(u)} (було {prev_cited[u]}×)")
    for u, c in cited.most_common(3):
        lines.append(f"· топ: {short(u)} · {c}×")

    if fresh:
        lines.append(f"\nСвіжі статті (≤{FRESH_DAYS} днів з публікації):")
        for u, d in sorted(fresh.items(), key=lambda x: x[1], reverse=True):
            c = cited.get(u, 0)
            lines.append(f"· {short(u)} ({d[5:]}): " + (f"{c}× (промптів: {len(cited_prompts[u])})"
                                                          if c else "ще не цитується"))

    prev_recs = state.get("recs") or {}
    n_new = sum(1 for r in recs if r.get("status") == "NEW")
    lines.append(f"\nРекомендації HubSpot: відкритих NEW {n_new} з {len(recs)}")
    if not first:
        for r in [r for r in recs if str(r["id"]) not in prev_recs][:5]:
            lines.append(f"🆕 {r.get('priority')} {r.get('type')}: "
                         f"{textwrap.shorten(r.get('contentTitle') or r.get('title') or '', 90, placeholder='…')}")
        changed = [(r, prev_recs[str(r["id"])]) for r in recs
                   if str(r["id"]) in prev_recs and prev_recs[str(r["id"])] != r.get("status")]
        for r, was in changed[:5]:
            lines.append(f"🔁 {textwrap.shorten(r.get('title') or '', 60, placeholder='…')}: {was} → {r.get('status')}")
    else:
        lines.append("Перший запуск: базу записано, нові рекомендації й сторінки рахуються з наступного тижня.")
    if failed:
        lines.append(f"\n⚠️ не прочитались промпти: {len(failed)} (їхні цитування не враховані)")
    lines.append("\nДеталі: scripts/hubspot-aeo.py prompts · recs --status NEW · citations --url <сторінка>")
    text = "\n".join(lines)
    return text if len(text) <= TG_LIMIT else text[:TG_LIMIT - 40] + "\n…(обрізано, повний звіт у файлі)"


def send(text: str) -> bool:
    spec = importlib.util.spec_from_file_location("outbound_pipeline", PIPE)
    op = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(op)
    return op.telegram_send(text)


def cmd_watch(args) -> int:
    today = _dt.date.today()
    day = lambda n: (today - _dt.timedelta(days=n)).isoformat()  # noqa: E731
    win = {"cur_from": day(7), "cur_to": day(1), "prev_from": day(14), "prev_to": day(8)}
    stamp = _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    def fail(msg: str) -> int:
        print(f"[{stamp}] FAIL {msg}")
        if args.notify:
            send(f"⚠️ Тижневий звіт HubSpot AEO не відпрацював ({stamp})\n{msg}\n"
                 "Стан не оновлено; наступний запуск порівняє з останнім вдалим.")
        return 3

    include = ["SUMMARY", "PROMPTS", "ASSISTANT_BREAKDOWN", "CITATIONS"]
    try:
        cur = metrics(include, win["cur_from"], win["cur_to"])
        prev = metrics(include, win["prev_from"], win["prev_to"])
        recs = list_recs(args.business_unit)
    except Broken as e:
        return fail(str(e))

    rows = prompt_rows(cur)
    cited: Counter = Counter()
    cited_prompts: dict[str, set] = defaultdict(set)
    failed: list[str] = []
    for p in rows:
        try:
            runs = prompt_runs(p["id"], win["cur_from"], win["cur_to"]).get("runs") or []
        except Broken as e:
            failed.append(f"{p['id']}: {e}")
            continue
        for u, c in cited_ours(runs).items():
            cited[u] += c
            cited_prompts[u].add(p["id"])
    if rows and len(failed) > len(rows) * 0.1:
        return fail(f"prompt DETAIL упав на {len(failed)}/{len(rows)} промптах. Приклад: {failed[0][:300]}")

    state = json.loads(STATE.read_text()) if STATE.exists() else {}
    fresh = fresh_articles(today)
    text = build_report(win, cur, prev, recs, cited, cited_prompts, fresh, state, failed)
    print(f"[{stamp}]\n{text}")

    DEFAULT_OUT.mkdir(parents=True, exist_ok=True)
    stem = DEFAULT_OUT / f"{today.isoformat()}-weekly"
    stem.with_suffix(".md").write_text(text + "\n")
    stem.with_suffix(".json").write_text(json.dumps(
        {"windows": win, "current": cur, "previous": prev, "recommendations": recs,
         "cited_ours": {u: {"count": c, "prompts": sorted(cited_prompts[u])} for u, c in cited.items()},
         "fresh_articles": fresh, "failed": failed}, ensure_ascii=False, indent=1))
    STATE.write_text(json.dumps({"checked": stamp, "window": win,
                                 "recs": {str(r["id"]): r.get("status") for r in recs},
                                 "cited": dict(cited)}, ensure_ascii=False, indent=1))
    if args.notify and not send(text):
        print("Telegram send failed")
        return 1
    return 0


# ------------------------------------------------------------------ main

def main() -> int:
    today = _dt.date.today()
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--from", dest="date_from", default=(today - _dt.timedelta(days=30)).isoformat())
    common.add_argument("--to", dest="date_to", default=today.isoformat())
    common.add_argument("--business-unit", type=int, default=0, help="3DLOOK is business unit 0")
    common.add_argument("--json", action="store_true")
    # Common flags live on the subcommands only: on both levels, the subparser default would
    # silently overwrite a root-level `--json`.
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("status", parents=[common]).set_defaults(fn=cmd_status)
    p = sub.add_parser("prompts", parents=[common])
    p.add_argument("--below", type=float, help="only prompts with visibility under this")
    p.add_argument("--phase", choices=PHASES)
    p.set_defaults(fn=cmd_prompts)
    p = sub.add_parser("prompt", parents=[common])
    p.add_argument("id", type=int)
    p.add_argument("--assistant", choices=ASSISTANTS)
    p.add_argument("--runs", type=int, default=3)
    p.add_argument("--full", action="store_true", help="print full AI answer text")
    p.set_defaults(fn=cmd_prompt)
    sub.add_parser("competitors", parents=[common]).set_defaults(fn=cmd_competitors)
    p = sub.add_parser("citations", parents=[common])
    p.add_argument("--url", help="one page: CITATION_ANALYSIS")
    p.set_defaults(fn=cmd_citations)
    p = sub.add_parser("recs", parents=[common])
    p.add_argument("--status", choices=REC_STATUSES)
    p.add_argument("--type", help="CONTENT, TECHNICAL, DOMAIN, URL")
    p.add_argument("--id", type=int, help="one recommendation: DETAIL")
    p.set_defaults(fn=cmd_recs)
    p = sub.add_parser("snapshot", parents=[common])
    p.add_argument("--out-dir", default=str(DEFAULT_OUT))
    p.set_defaults(fn=cmd_snapshot)
    p = sub.add_parser("topic", parents=[common], help="AEO signals for one article → workspace/seo/_aeo/")
    p.add_argument("seed")
    p.add_argument("--slug", required=True, help="article slug; a date prefix is stripped and re-added")
    p.add_argument("--terms", help="extra words to match on, e.g. the primary keyword and variants")
    p.add_argument("--out")
    p.set_defaults(fn=cmd_topic)
    p = sub.add_parser("watch", parents=[common], help="weekly report; cron runs it with --notify")
    p.add_argument("--notify", action="store_true", help="send the report (or a failure) to Telegram")
    p.set_defaults(fn=cmd_watch)
    args = ap.parse_args()
    try:
        rc = args.fn(args)
    except Refused as e:
        print(f"REFUSED: {e}")
        return 2
    except Broken as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 3
    return rc or 0


if __name__ == "__main__":
    sys.exit(main())
