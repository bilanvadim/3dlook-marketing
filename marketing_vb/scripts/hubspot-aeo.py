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

DATA NOTES, LEARNED FROM THE API ON 2026-09-29 (do not re-derive)
  * The COMPETITORS section does not reconcile with ASSISTANT_BREAKDOWN. Over 7 days there
    were 576 responses and ASSISTANT_BREAKDOWN counted 471 competitor mentions, but
    COMPETITORS gave sizestream 6,631 mentions. The share-of-voice percentages are also computed
    over a much larger base: all five tracked brands together come to about 16%. Treat
    COMPETITORS as a relative ranking only. Before quoting a competitor number anywhere, check it
    in the HubSpot UI. Our own-brand count matches ASSISTANT_BREAKDOWN ownedMentions.
  * `filters` apply only to SUMMARY and PROMPTS. CITATIONS, COMPETITORS and ASSISTANT_BREAKDOWN
    are always portal-wide for the date window.
  * CITATIONS returns domains (top 50), not URLs. To see how one page is cited, use
    `citations --url`, which runs CITATION_ANALYSIS: per-assistant counts and the prompts that
    cited the page.
  * setupStatus.inputProfileConfigured=false means AEO setup is not finished. Empty sections are
    expected in that case, so do not report them as "no data yet".
  * Prompt DETAIL returns the full AI answer text for every run and can be large. The default
    here is 3 runs; the server caps it at 25.
  * The plan covers three assistants: CHATGPT, GEMINI and PERPLEXITY. The CLAUDE and
    GOOGLE_AI_* enum values exist but have no runs.
  * `visibility` is the percentage of responses that mention the brand
    (mentionCount / responseCount). A score of 0 on a tracked prompt means none of the
    assistants named us.

USAGE
    scripts/hubspot-aeo.py status                 # visibility, run freshness, prompt capacity
    scripts/hubspot-aeo.py prompts [--below 20] [--phase AWARENESS]
    scripts/hubspot-aeo.py prompt <id> [--assistant CHATGPT] [--runs 3] [--full]
    scripts/hubspot-aeo.py competitors            # relative only, see DATA NOTES
    scripts/hubspot-aeo.py citations [--url https://3dlook.ai/content-hub/...]
    scripts/hubspot-aeo.py recs [--status NEW] [--type CONTENT] [--id <rec id>]
    scripts/hubspot-aeo.py snapshot [--out-dir workspace/research/aeo]
  common: --from YYYY-MM-DD --to YYYY-MM-DD (default: the last 30 days) · --json

  The snapshot directory is excluded in .git/info/exclude. The remote is PUBLIC, and tracked
  prompts plus competitor data are strategy, the same reasoning as hubspot-findings.md.
Exit: 0 ok · 2 refused · 3 broken setup / API error.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import shutil
import subprocess
import sys
import textwrap
from pathlib import Path

MCP_URL = "https://mcp.hubspot.com/"
PORTAL = 6014382
PROMPTS_URL = f"https://app.hubspot.com/ai-visibility/{PORTAL}/prompts"
REPO = Path(__file__).resolve().parent.parent
DEFAULT_OUT = REPO / "workspace" / "research" / "aeo"
ASSISTANTS = ("CHATGPT", "GEMINI", "PERPLEXITY", "CLAUDE", "GOOGLE_AI_MODE", "GOOGLE_AI_OVERVIEWS")
PHASES = ("AWARENESS", "CONSIDERATION", "EVALUATION", "DECISION")
REC_STATUSES = ("NEW", "IN_PROGRESS", "COMPLETED", "ARCHIVED", "FAILED", "DISMISSED", "DRAFT_CREATED")
READ_TOOLS = {"get_aeo_metrics", "manage_aeo_prompts", "manage_aeo_recommendations", "tool_guidance"}
READ_OPERATIONS = {"manage_aeo_prompts": {"DETAIL"}, "manage_aeo_recommendations": {"LIST", "DETAIL"}}


class Broken(Exception):
    """oo or HubSpot failed. Exit 3."""


class Refused(Exception):
    """A write operation was requested. Exit 2."""


def call(tool: str, arguments: dict) -> dict:
    """One MCP tools/call through `oo connector proxy`, returning the tool's JSON payload."""
    if tool not in READ_TOOLS:
        raise Refused(f"{tool} is not an AEO read tool")
    op = (arguments.get("operation") or {}).get("_operationType")
    if tool in READ_OPERATIONS and op not in READ_OPERATIONS[tool]:
        raise Refused(f"{tool} {op} writes to HubSpot; HubSpot is read-only for us. "
                      f"Manage prompts in the UI: {PROMPTS_URL}")
    if not shutil.which("oo"):
        raise Broken("`oo` CLI not found on PATH (expected ~/.local/bin/oo)")
    body = {"jsonrpc": "2.0", "id": 1, "method": "tools/call",
            "params": {"name": tool, "arguments": arguments}}
    cmd = ["oo", "connector", "proxy", "hubspot", "--method", "POST", "--endpoint", MCP_URL,
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


def metrics(args, include: list[str], **extra) -> dict:
    payload = {"include": include, "startDate": args.date_from, "endDate": args.date_to, **extra}
    data = call("get_aeo_metrics", payload)
    setup = (data.get("setupStatus") or {}).get("inputProfileConfigured")
    if setup is False:
        raise Broken("AEO setup is not complete for this business unit (no input profile). "
                     "Empty sections are expected until setup is finished.")
    return data


def ts(ms: int | None) -> str:
    if not ms:
        return "-"
    return _dt.datetime.fromtimestamp(ms / 1000, _dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def prompt_rows(data: dict) -> list[dict]:
    return (data.get("prompts") or {}).get("prompts") or []


def fmt_status(data: dict, args) -> str:
    s, r, lim = data.get("summary") or {}, data.get("runStatus") or {}, data.get("limits") or {}
    return "\n".join([
        f"HubSpot AEO · portal {PORTAL} · {args.date_from} → {args.date_to}",
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


def list_recs(args, status: str | None = None) -> list[dict]:
    op = {"_operationType": "LIST", "businessUnitId": args.business_unit, "limit": 100}
    if status:
        op["status"] = status
    return call("manage_aeo_recommendations", {"operation": op}).get("recommendations") or []


def emit(args, payload, text: str) -> None:
    print(json.dumps(payload, ensure_ascii=False, indent=1) if args.json else text)


def cmd_status(args) -> None:
    data = metrics(args, ["SUMMARY", "RUN_STATUS", "LIMITS"])
    emit(args, data, fmt_status(data, args))


def cmd_prompts(args) -> None:
    rows = prompt_rows(metrics(args, ["PROMPTS"]))
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
    data = metrics(args, ["COMPETITORS", "ASSISTANT_BREAKDOWN"])
    emit(args, data, fmt_assistants(data) + "\n\n" + fmt_competitors(data))


def cmd_citations(args) -> None:
    if args.url:
        data = metrics(args, ["CITATION_ANALYSIS"], citationUrl=args.url)
        emit(args, data, json.dumps(data.get("citationAnalysis", data), ensure_ascii=False, indent=1))
    else:
        data = metrics(args, ["CITATIONS"])
        emit(args, data, fmt_citations(data, top=50))


def cmd_recs(args) -> None:
    if args.id:
        data = call("manage_aeo_recommendations",
                    {"operation": {"_operationType": "DETAIL", "recommendationId": args.id}})
        emit(args, data, json.dumps(data, ensure_ascii=False, indent=1))
        return
    recs = list_recs(args, args.status)
    if args.type:
        recs = [r for r in recs if r.get("type") == args.type]
    order = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}
    recs.sort(key=lambda r: (order.get(r.get("priority"), 3), -(r.get("score") or 0)))
    emit(args, recs, f"{len(recs)} recommendations\n" + fmt_recs(recs))


def cmd_snapshot(args) -> None:
    data = metrics(args, ["SUMMARY", "RUN_STATUS", "LIMITS", "PROMPTS", "CITATIONS", "COMPETITORS",
                          "ASSISTANT_BREAKDOWN", "ICPS_AND_PRODUCTS"])
    data["recommendations"] = list_recs(args)
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
        "```\n" + fmt_status(data, args) + "\n```",
        "## Prompts (lowest visibility first)\n\n```\n" + fmt_prompts(rows) + "\n```",
        "## By assistant\n\n```\n" + fmt_assistants(data) + "\n```",
        "## Cited domains\n\n```\n" + fmt_citations(data) + "\n```",
        "## Competitors\n\n```\n" + fmt_competitors(data) + "\n```",
        f"## New recommendations ({len(new)})\n\n```\n" + fmt_recs(new) + "\n```",
    ]) + "\n"
    stem.with_suffix(".md").write_text(md)
    emit(args, {"json": str(stem.with_suffix(".json")), "md": str(stem.with_suffix(".md"))},
         f"wrote {stem.with_suffix('.json')}\nwrote {stem.with_suffix('.md')}")


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
    args = ap.parse_args()
    try:
        args.fn(args)
    except Refused as e:
        print(f"REFUSED: {e}")
        return 2
    except Broken as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 3
    return 0


if __name__ == "__main__":
    sys.exit(main())
