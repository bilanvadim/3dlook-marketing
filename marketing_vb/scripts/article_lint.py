#!/usr/bin/env python3
"""article_lint.py — every mechanical gate on an SEO article, in one call.

WHY
---
The 2026-09-02 pipeline audit (`docs/seo-pipeline-audit-2026-09-02.md`) measured one article
revision at 30.9M tokens / $87.31 and found that the checks worth running are the ones a
script can run. Two concrete findings drive this file:

1. **The QC agent was doing arithmetic.** The August social baseline spent 7.1M tokens /
   $36.35 on `quality-controller` per pack. On the 2026-09-02 article run no QC agent ran at
   all; verification was `detect-ai-tells.py` plus about fifteen ad-hoc greps, and it caught
   more than the agent had been catching, including an unsupported product claim that had
   survived a 20-item expert review. Ad-hoc greps are not repeatable, so they are here.

2. **`detect-ai-tells.py` reports the wrong word count for a length gate.** Its `\\b\\w+\\b`
   count includes frontmatter, HTML comment markers and table pipes: it reported 3,055 words
   for an article whose prose is 2,691. Anyone gating on "within +/-10% of target" from that
   number is judging a different quantity. `prose_words()` below is the gate-worthy count.

WHAT IT DOES NOT DO
-------------------
It does not judge whether the argument holds, whether a section earns its place, or whether
the voice is right. That is `quality-controller`'s job and it should run on exactly that,
after this script is green. A clean lint is a floor, not a verdict.

THE NUMBER HEURISTIC IS DELIBERATELY NARROW
-------------------------------------------
Gate 3 flags an unsourced *product* figure, not every digit. A gate that fires on "four to
twelve weeks" and "two photographs" trains people to ignore it, so it only looks at shapes
that carry product claims: percentages, measurements with a unit, and counts above 1,000.
Everything else is a false positive waiting to happen.

USAGE
    scripts/article_lint.py workspace/seo/articles/<slug>/draft.md
    scripts/article_lint.py .../final.md --pack workspace/seo/_context-packs/<slug>.yaml
    scripts/article_lint.py .../plan.md --plan          # plan-stage gates
    scripts/article_lint.py .../final.md --json         # machine-readable
    scripts/article_lint.py .../final.md --no-exit-code # always exit 0

Exit code is 1 on FAIL unless --no-exit-code. That is deliberate and differs from
`detect-ai-tells.py`, which is a diagnostic and always exits 0: this one is a gate.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DETECTOR = os.path.join(REPO, "brand-assets", "style-guides", "scripts", "detect-ai-tells.py")

# Figures and terms that a decision superseded. Each entry is (pattern, what to use instead,
# when and who decided). These exist because a stale figure is worse than a missing one: it
# reads as verified. Add a row when a decision retires a number, do not delete the old row.
SUPERSEDED = [
    (r"\b150\s*(?:to|[-–])\s*205\b", "150 to 220 cm", "Vadim 2026-09-02, one figure for training data and validation population"),
    (r"\bDEXA\b", "DXA, or `DXA (also written DEXA)` where the older spelling is the search term",
     "Vadim confirmed DXA 2026-09-02"),
    (r"\bessential fat\b", "omit in wellness copy", "Review 1 item 13, 2026-09-02"),
    (r"\bbeneficial fat\b", "omit in wellness copy", "Review 1 item 13, 2026-09-02"),
    (r"\bpredicted weight\b", "omit; no approved claim supports it", "Review 1 item 13 closed against the reviewer, 2026-09-02"),
    (r"\bbody composition values\b", "body composition estimates", "Review 1 item 13, 2026-09-02"),
]

# Abbreviations that guardrail M1 requires expanding at first use. BMI, AI, US, EU, CEO, UK,
# WWW and iOS are the commonly-known exception (terminology-guardrails.md section 1) and are
# deliberately absent.
M1_ABBREVS = {
    "DXA": "dual-energy X-ray absorptiometry",
    "BIA": "bioelectrical impedance analysis",
    "GLP-1": "glucagon-like peptide-1",
    "FDA": "Food and Drug Administration",
    "HIPAA": "Health Insurance Portability and Accountability Act",
    "GDPR": "General Data Protection Regulation",
    "API": "application programming interface",
    "SDK": "software development kit",
    "BMR": "basal metabolic rate",
    "CRO": "Contract Research Organization",
    "ICH": "International Council for Harmonisation",
}


# ---------------------------------------------------------------- text helpers

def split_frontmatter(text: str):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}, text
    fm = {}
    for line in m.group(1).split("\n"):
        if ":" in line and not line.startswith((" ", "-", "#")):
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip()
    return fm, text[m.end():]


def strip_comments(text: str) -> str:
    return re.sub(r"<!--.*?-->", " ", text, flags=re.S)


def prose_words(body: str) -> int:
    """The count a length gate should use: prose only.

    Drops HTML comments (claim markers, TODO markers), keeps link anchor text and drops the
    URL, drops heading hashes, table pipes, alignment rows and emphasis markers.
    """
    t = strip_comments(body)
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    t = re.sub(r"^[ \t]*#{1,6}[ \t]*", "", t, flags=re.M)
    t = t.replace("|", " ")
    t = re.sub(r"^[\s:|\-]+$", "", t, flags=re.M)
    t = t.replace("**", "").replace("*", "").replace("`", "")
    return len(t.split())


def body_lines(body: str, line_offset: int = 0):
    r"""Yield (line_text, file_line_no) for prose lines only.

    Granularity is the line, not the sentence, and that is deliberate. In these articles a
    paragraph is one line and claim markers sit inline *after* the sentence's full stop, so
    splitting on `(?<=[.!?])\s+` detached every marker from the claim it supports and made
    gate 3 fire on all seventeen of them. The first version of this file did exactly that.
    """
    for i, line in enumerate(body.split("\n"), 1):
        st = line.strip()
        if not st or st.startswith("#") or st.startswith("|") or st.startswith("<!--"):
            continue
        yield line, i + line_offset


def extract_target(plan_fm: dict, plan_body: str) -> int | None:
    """The plan's prose-word target.

    Order matters. A loose regex over the plan body is dangerous because the plan is full of
    other four-digit numbers: the first version of this matched `Apparel 2,398`, a market
    figure in a competitor table, and gated a 2,729-word article against it. So: frontmatter
    first, then two explicitly labelled shapes, and nothing else.
    """
    fmv = plan_fm.get("target_words") or plan_fm.get("word_target")
    if fmv:
        try:
            return int(str(fmv).replace(",", "").split()[0])
        except (ValueError, IndexError):
            pass
    for pat in (
        r"\|\s*\*\*Total\*\*\s*\|\s*\*\*([\d,]{3,6})\*\*",   # | **Total** | **2,650** |
        r"\*\*Target:\*\*\s*([\d,]{3,6})\s*words",                  # **Target:** 2,650 words
        r"Word count total:\s*([\d,]{3,6})",                          # Word count total: 2,650
        r"Target\s+\*\*([\d,]{3,6})\s*words",                        # Target **2,650 words
    ):
        m = re.search(pat, plan_body)
        if m:
            return int(m.group(1).replace(",", ""))
    return None


# ---------------------------------------------------------------- pack loading

def load_pack(path: str | None, article_path: str):
    """Find and parse the context pack. Returns (pack_dict_or_None, resolved_path_or_None)."""
    if path is None:
        slug = os.path.basename(os.path.dirname(os.path.abspath(article_path)))
        guess = os.path.join(REPO, "workspace", "seo", "_context-packs", f"{slug}.yaml")
        path = guess if os.path.exists(guess) else None
    if not path or not os.path.exists(path):
        return None, None
    try:
        import yaml
    except ImportError:
        return None, path
    with open(path) as fh:
        raw = yaml.safe_load(fh)
    return (raw or {}).get("context_pack", raw), path


# ---------------------------------------------------------------- gates

def gate_detector(article_path: str):
    """Gate 1. Delegate hard bans to detect-ai-tells.py rather than re-encoding them.

    The audit's F3 finding is that these rules already live in four places and are enforced
    in one. This gate calls the one.
    """
    if not os.path.exists(DETECTOR):
        return False, [f"detector not found at {DETECTOR}"], {}
    try:
        out = subprocess.run(
            [sys.executable, DETECTOR, article_path, "--channel", "article"],
            capture_output=True, text=True, timeout=120,
        )
        d = json.loads(out.stdout)
    except Exception as exc:
        return False, [f"detector failed to run: {exc}"], {}

    problems = []
    for h in d.get("hard_fails", []):
        ex = h.get("hits", [{}])[0].get("marker", "")
        problems.append(f"hard fail: {h['category']} x{h['count']}" + (f"  e.g. {ex!r}" if ex else ""))
    for v in d.get("house_rule_violations", []) or []:
        problems.append(f"house rule: {v}")
    sm = d.get("style_metrics", {})
    return not problems, problems, {
        "detector_words": d.get("total_words"),
        "ai_density": d.get("ai_density_per_1000_words"),
        "verdict": d.get("verdict", "").split("—")[0].strip(),
        "rhythm_variation": sm.get("rhythm", {}).get("variation") if isinstance(sm.get("rhythm"), dict) else None,
    }


def gate_length(body: str, target: int | None, tolerance: float = 0.15):
    """Gate 2. Prose word count against the plan's target."""
    n = prose_words(body)
    if target is None:
        return True, [f"prose words {n} (no target given, not gated)"], {"prose_words": n}
    lo, hi = int(target * (1 - tolerance)), int(target * (1 + tolerance))
    ok = lo <= n <= hi
    msg = f"prose words {n} vs target {target} (band {lo}-{hi})"
    return ok, [msg if ok else f"OUT OF BAND: {msg}"], {"prose_words": n, "target": target}


def gate_claims(body: str, pack, line_offset: int = 0):
    """Gate 3. Claim traceability, both directions.

    a) every claim marker resolves to an id the pack actually contains
    b) every product-shaped figure sits in a sentence that carries a marker

    (b) is what caught nothing on 2026-09-02 because nobody was checking it. The
    `predicted weight` error came in through an expert review and was found by accident.
    """
    problems = []
    markers = re.findall(r"<!--\s*claim:\s*([A-Za-z0-9-]+)\s*-->", body)
    used = sorted(set(markers))
    if pack is None:
        return True, ["no context pack found, claim gate skipped"], {"claims_used": used}

    known = {c["id"] for c in (pack.get("approved_claims") or []) if isinstance(c, dict) and "id" in c}
    for cid in used:
        if cid not in known:
            problems.append(f"claim marker {cid} is not in the pack's approved_claims")

    # (b) unsourced product figures
    NUM = re.compile(
        r"(?<![\w.])("
        r"\d+(?:\.\d+)?\s*%"                                  # 45%, 96-97% (first half)
        r"|\d+(?:\.\d+)?\s*(?:cm|kg|mm|m)\b"                  # 1.5 cm, 210 kg
        r"|\d+(?:\.\d+)?\s*seconds?\b"                        # 45 seconds
        r"|\d{1,3}(?:,\d{3})+"                                # 150,000
        r"|\d{4,}"                                            # 30000
        r")"
    )
    for line, ln in body_lines(body, line_offset):
        if "claim:" in line:
            continue  # the paragraph is sourced; which figure maps to which id is the editor's call
        # Strip URLs first. A date path like /uploads/2026/09/ is not a product figure, and
        # asking for a claim marker on the year trains people to ignore this gate. Alt text
        # survives the strip on purpose: a number stated in alt text IS a published claim.
        scan = re.sub(r"\((?:https?:)?//?[^)\s]*\)", "()", strip_comments(line))
        scan = re.sub(r"https?://\S+", " ", scan)
        figs = {m.group(1) for m in NUM.finditer(scan)}
        for f in sorted(figs):
            problems.append(f"line {ln}: figure {f!r} sits in a paragraph with no claim marker")

    return not problems, problems, {"claims_used": used, "claims_known": len(known)}


def gate_banned(body: str, pack):
    """Gate 4. The pack's own banned_claims and banned_words."""
    if pack is None:
        return True, ["no context pack found, banned gate skipped"], {}
    problems = []
    text = strip_comments(body).lower()

    for w in (pack.get("banned_words") or []):
        if isinstance(w, str) and re.search(r"\b" + re.escape(w.lower()) + r"\b", text):
            problems.append(f"banned word: {w!r}")

    # banned_claims are prose descriptions, not greppable strings. Match on their distinctive
    # multi-word cores instead of the whole sentence, and only where a literal match is a
    # real signal rather than a coincidence.
    # Cores are regexes, not substrings, and each is scoped to the *asserted* form. The first
    # version matched bare "guarantee" and fired on "does not guarantee retention", which is
    # the disclaimer the guardrails ask for. A gate that flags the correct wording is worse
    # than no gate, so every row here must be unfireable by a well-written boundary sentence.
    CORES = {
        "most accurate body scanning": r"most accurate body[- ]scanning",
        "guaranteed compliance": r"(?<!not )(?<!does not )guarantees?\s+(?:\w+\s+){0,2}complian|makes?\s+you\s+compliant",
        "FDA-cleared": r"fda[- ]cleared",
        "SOC 2": r"soc\s*2",
        "automatic fraud detection": r"(?<!not )detects?\s+fraud|automatic\w*\s+fraud\s+detect",
    }
    for label, core in CORES.items():
        m = re.search(core, text)
        if m:
            problems.append(f"banned claim shape {label!r}: found {m.group(0)!r}")
    return not problems, problems, {}


# A line that is *talking about* a retired figure is not using it. Plans, decision records and
# deletion ledgers are full of "150 to 205 is superseded, use 150 to 220", and the first version
# of gate 5 fired on all of them: 30 hits on a plan that was entirely correct. A gate that
# flags the correct text is worse than no gate.
META_MARKERS = re.compile(
    r"supersed|deprecat|retired|correct(?:ed|ion)|resolved|was\s+150|instead of|no longer|"
    r"not added|do(?:es)? not appear|never in|deleted|removed|cut\b|uncited|omit|"
    r"->|→|\bto DXA\b|\bvs\b|diverg|open item|\bv1\b|review item|decisions §|"
    r"old\s+(?:figure|value|wording)|stale|no approved claim",
    re.I,
)

# A term wrapped in quotes, backticks or bold is being NAMED, not used. This single rule
# retired most of the false positives on its own: a plan that writes `predicted weight` in
# backticks to forbid it is doing the right thing, and so is a deletions ledger row.
QUOTED = re.compile(r"""[\"'`*]$""")


def _is_named_not_used(line: str, start: int, end: int) -> bool:
    before = line[max(0, start - 2):start]
    after = line[end:end + 2]
    return bool(QUOTED.search(before)) and bool(re.match(r"""^[\"'`*]""", after))


def gate_superseded(body: str, allow_discussion: bool = True, line_offset: int = 0):
    """Gate 5. Figures and terms a decision retired.

    A stale number is worse than a missing one, because it reads as verified. Every row in
    SUPERSEDED exists because someone had to hunt the old value out of the repo by hand.

    `allow_discussion` exempts a line that is discussing the supersession rather than using
    the figure. Keep it on for plans and decision records; the article body rarely needs it,
    but a deletions note inside a draft is legitimate.
    """
    problems = []
    text = strip_comments(body)
    lines = text.split("\n")
    for pat, instead, why in SUPERSEDED:
        for i, line in enumerate(lines, 1):
            for m in re.finditer(pat, line, re.I):
                if allow_discussion and (
                    META_MARKERS.search(line) or _is_named_not_used(line, m.start(), m.end())
                ):
                    continue
                # `DEXA` is licensed on a line that also carries `DXA`: that covers
                # `DXA (also written DEXA)` for search coverage and the published
                # `ai-body-scanners-vs-dexa-scans` slug. A comparison article legitimately
                # targets the DEXA query, and a gate that forbade it would fight SEO.
                # Tried as a regex lookbehind first; Python needs fixed width, so it lives here.
                if m.group(0).upper() == "DEXA" and re.search(r"\bDXA\b", line):
                    continue
                problems.append(f"line {i + line_offset}: {m.group(0)!r} is superseded, use {instead} ({why})")
    return not problems, problems, {}


def gate_links(body: str, pack):
    """Gate 6. All four internal-link directions, canonical form, no bare URLs."""
    problems = []
    # An asset is a file, not a page. The canonical trailing slash and the anchor-phrase rule
    # are about pages; forcing a "/" onto `/uploads/2026/09/banner_1.webp` would break it.
    # Illustrations live at `3dlook.ai/wp-content/uploads/YYYY/MM/*.webp`, which is how the
    # published corpus does it, so this fired on every article that carried an image.
    ASSET = re.compile(r"/wp-content/|\.(?:webp|png|jpe?g|gif|svg|avif|mp4|webm|pdf)$", re.I)

    all_urls = re.findall(r"https://3dlook\.ai/[A-Za-z0-9/_.-]*", body)
    urls = [u for u in all_urls if not ASSET.search(u)]
    assets = [u for u in all_urls if ASSET.search(u)]

    for u in set(urls):
        if not u.endswith("/"):
            problems.append(f"non-canonical URL, missing trailing slash: {u}")
    for m in re.finditer(r"(?<!\()(?<!\]\()https://3dlook\.ai/\S+", body):
        if ASSET.search(m.group(0)):
            continue
        seg = body[max(0, m.start() - 2):m.start()]
        if not seg.endswith("]("):
            problems.append(f"bare URL, not on an anchor phrase: {m.group(0)[:60]}")

    info = {"links_total": len(urls), "links_distinct": len(set(urls)),
            "asset_urls": len(assets)}
    if pack is None:
        return not problems, problems + ["no context pack, link-direction gate skipped"], info

    targets = (pack.get("content_strategy") or {}).get("internal_link_targets") or {}
    covered = {}
    for direction in ("up", "sideways", "down", "trust"):
        want = targets.get(direction)
        want = [want] if isinstance(want, str) else (want or [])
        hits = 0
        for w in want:
            url = w.split("#")[0].strip()
            if url.startswith("http") and url in body:
                hits += 1
        covered[direction] = hits
        if hits == 0 and any(str(w).startswith("http") for w in want):
            problems.append(f"link direction {direction!r} is not covered by any link")
    info["directions"] = covered
    return not problems, problems, info


def gate_keyword(body: str, primary: str | None):
    """Gate 7. Primary keyword placement: H1, first paragraph, at least one H2."""
    if not primary:
        return True, ["no primary_keyword in plan frontmatter, keyword gate skipped"], {}
    problems = []
    low = strip_comments(body).lower()
    p = primary.lower()

    h1 = next((l for l in body.split("\n") if l.startswith("# ")), "")
    h2s = [l for l in body.split("\n") if l.startswith("## ")]
    paras = [x for x in strip_comments(body).split("\n\n") if x.strip() and not x.lstrip().startswith("#")]
    first_para = paras[0].lower() if paras else ""

    if p not in h1.lower():
        problems.append(f"primary keyword {primary!r} not in H1")
    if p not in first_para:
        problems.append(f"primary keyword {primary!r} not in the first paragraph")
    if not any(p in h.lower() for h in h2s):
        problems.append(f"primary keyword {primary!r} not in any H2")
    return not problems, problems, {"keyword": primary, "occurrences": low.count(p), "h2_count": len(h2s)}


def gate_m1(body: str):
    """Gate 8. Guardrail M1: expand each abbreviation at first use."""
    problems = []
    text = strip_comments(body)
    for abbr, expansion in M1_ABBREVS.items():
        m = re.search(r"\b" + re.escape(abbr) + r"\b", text)
        if not m:
            continue
        window = text[max(0, m.start() - 120):m.start()]
        if expansion.lower() not in window.lower():
            ln = text[:m.start()].count("\n") + 1
            problems.append(f"line {ln}: {abbr} used before being expanded as {expansion!r} (guardrail M1)")
    return not problems, problems, {}


def gate_plan(body: str, fm):
    """--plan mode. Gates the plan, before anyone writes 2,700 words against it."""
    problems = []
    for field in ("slug", "primary_keyword", "hub", "intent", "action_type", "status"):
        if field not in fm:
            problems.append(f"plan frontmatter is missing {field!r}")
    if fm.get("status") not in ("approved", "draft", "awaiting_vadim"):
        problems.append(f"unexpected plan status {fm.get('status')!r}")

    # Deliberately NOT a loose regex over the plan body. The same mistake in extract_target
    # matched a competitor market figure ("Apparel 2,398"); here it summed 22 unrelated
    # numbers to 18,762 for a plan whose target is 2,650. Only the labelled total counts.
    target = extract_target(fm, body)
    info = {"target_words": target}
    if target is None:
        problems.append(
            "no resolvable word target. Add `target_words:` to the plan frontmatter, or a "
            "labelled total: `| **Total** | **N** |`, `**Target:** N words`, or `Word count total: N`"
        )

    h2_sections = len(re.findall(r"^#{3}\s*(?:Section\s*)?\d+", body, re.M))
    info["outline_sections"] = h2_sections
    if h2_sections == 0:
        problems.append("no numbered outline sections found")
    return not problems, problems, info




# The accuracy figures the live framework article actually publishes. Anything else claiming to
# be an accuracy or repeatability figure for our own measurement is not ours.
# Source: brand-assets/product-info/accuracy-formulations.md, transcribed 2026-09-02 from
# https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/
APPROVED_ACCURACY = [r"96-97\s*%", r"1\.5-2\.0\s*cm", r"less than 1\s*cm", r"<\s*1\s*cm",
                     r"0\.40\s*cm", r"\+/-\s*3\.5\s*%", r"±\s*3\.5\s*%"]

# The two studies use different references. The live article states the rule outright: "The
# numbers from the two studies should not be combined because the references differ."
INTERNAL_BENCH = re.compile(r"96-97\s*%|1\.5-2\.0\s*cm|less than 1\s*cm|<\s*1\s*cm")
ISO_BENCH = re.compile(r"0\.40\s*cm|ISO\s*8559")

FRAMEWORK_URL = "content-hub/mobile-body-scanning-accuracy/"


def gate_accuracy(body: str, line_offset: int = 0):
    """Gate 9. Accuracy discipline, against the live framework article's own rules.

    Three things a script can check, and one it cannot.

    Can: that an accuracy figure is one we actually publish; that the internal benchmark and
    the ISO benchmark are not quoted in the same paragraph; that a paragraph carrying a figure
    links to the framework article rather than leaving the reader to find the source.

    Cannot: whether the condition attached to a figure is the RIGHT condition. "Accurate enough
    for which decision?" is a judgment, and it stays with the editor.
    """
    problems = []
    text = strip_comments(body)

    # a) an accuracy-shaped figure that is not one of ours
    SHAPED = re.compile(
        r"(\d{1,3}(?:\.\d+)?\s*%\s*(?:accur|precis|repeatab|consisten)"
        r"|(?:accur|precis|repeatab|error|varian|toleran)\w*[^.\n]{0,40}?"
        r"(\d{1,3}(?:\.\d+)?\s*(?:%|cm|mm)))",
        re.I)
    for i, line in enumerate(text.split("\n"), 1):
        if META_MARKERS.search(line):
            continue
        for m in SHAPED.finditer(line):
            frag = m.group(0)
            if any(re.search(a, frag, re.I) for a in APPROVED_ACCURACY):
                continue
            problems.append(
                f"line {i + line_offset}: {frag.strip()!r} is not an accuracy figure we publish. "
                f"Approved set: 96-97%, 1.5-2.0 cm, < 1 cm, 0.40 cm (ISO), +/-3.5% (weight). "
                f"See accuracy-formulations.md")

    # b) the two benchmarks in one paragraph
    for pi, para in enumerate(text.split("\n\n")):
        if META_MARKERS.search(para):
            continue
        if INTERNAL_BENCH.search(para) and ISO_BENCH.search(para):
            ln = text[:text.find(para)].count("\n") + 1 + line_offset
            problems.append(
                f"line ~{ln}: the internal benchmark and the ISO 8559 benchmark appear in the "
                f"same paragraph. The live article: \"The numbers from the two studies should "
                f"not be combined because the references differ.\"")

    # c) a figure with no route to its source
    has_fig = bool(INTERNAL_BENCH.search(text))
    if has_fig and FRAMEWORK_URL not in body:
        problems.append(
            "an accuracy figure is stated but the article never links to the framework article "
            f"({FRAMEWORK_URL}). A cited figure whose source is nowhere on the page is the "
            "weaker configuration")

    info = {"accuracy_figures_present": has_fig,
            "links_to_framework": FRAMEWORK_URL in body}
    return not problems, problems, info


# ---------------------------------------------------------------- report

def build_report(body: str, pack, primary: str | None):
    """The descriptive numbers a coordinator wants, in one call instead of fifteen greps.

    Audit finding F6: the MAIN session was 48% of the 2026-09-02 run's tokens, 88 requests at
    ~170K context, and roughly fifteen of those requests were separate Bash greps to answer
    "how many H2s", "how many links per direction", "how often does the keyword appear",
    "is corporate framing still dominant". Every round-trip re-sends the whole context. This
    function answers all of them at once.

    These are NOT gates. Nothing here passes or fails; it is the shape of the article, for a
    human or a coordinator to judge.
    """
    out = {}
    clean = strip_comments(body)

    h2s = [l[3:].strip() for l in body.split("\n") if l.startswith("## ")]
    out["h2_count"] = len(h2s)
    out["h2_titles"] = h2s

    # words per H2 section
    per = []
    chunks = re.split(r"^## ", body, flags=re.M)
    for i, c in enumerate(chunks[1:], 0):
        title = c.split("\n")[0].strip()
        per.append({"section": title[:52], "words": prose_words(c)})
    out["words_per_section"] = per
    out["prose_words"] = prose_words(body)

    # links by direction, from the pack
    urls = re.findall(r"https://3dlook\.ai/[A-Za-z0-9/_.-]*", body)
    by_target = {}
    for u in urls:
        by_target[u] = by_target.get(u, 0) + 1
    out["links_total"] = len(urls)
    out["links_by_target"] = by_target
    if pack:
        targets = (pack.get("content_strategy") or {}).get("internal_link_targets") or {}
        dirs = {}
        for d in ("up", "sideways", "down", "trust"):
            want = targets.get(d)
            want = [want] if isinstance(want, str) else (want or [])
            dirs[d] = sum(1 for w in want if str(w).split("#")[0].strip().startswith("http")
                          and str(w).split("#")[0].strip() in body)
        out["links_by_direction"] = dirs

    if primary:
        out["primary_keyword"] = primary
        out["primary_occurrences"] = clean.lower().count(primary.lower())

    # claim usage
    markers = re.findall(r"<!--\s*claim:\s*([A-Za-z0-9-]+)\s*-->", body)
    tally = {}
    for m in markers:
        tally[m] = tally.get(m, 0) + 1
    out["claim_markers_total"] = len(markers)
    out["claims_by_id"] = dict(sorted(tally.items()))
    if pack:
        known = [c["id"] for c in (pack.get("approved_claims") or [])
                 if isinstance(c, dict) and "id" in c]
        out["claims_available_unused"] = sorted(set(known) - set(tally))

    # term-group balance. Reads `lint_term_groups` from the pack when present, so an article
    # whose whole point is a framing shift can be measured instead of eyeballed. On
    # 2026-09-02 this was the review's main item and it took a hand-written script to answer.
    groups = (pack or {}).get("lint_term_groups") or {}
    if groups:
        bal = {}
        no_urls = re.sub(r"https?://\S+", " ", clean)
        for gname, terms in groups.items():
            bal[gname] = {t: len(re.findall(r"\b" + re.escape(t), no_urls, re.I))
                          for t in (terms or [])}
            bal[gname]["_total"] = sum(v for k, v in bal[gname].items() if k != "_total")
        out["term_group_balance"] = bal
    return out


# ---------------------------------------------------------------- driver

def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("path")
    ap.add_argument("--pack", help="context pack yaml (default: guessed from the article's slug dir)")
    ap.add_argument("--plan", action="store_true", help="run plan-stage gates instead of article gates")
    ap.add_argument("--target", type=int, help="prose word target (default: from plan.md beside the article)")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--no-exit-code", action="store_true", help="always exit 0")
    ap.add_argument("--report", action="store_true",
                    help="also print the descriptive numbers (shape of the article), not just gates")
    args = ap.parse_args()

    if not os.path.exists(args.path):
        print(f"no such file: {args.path}", file=sys.stderr)
        return 2

    with open(args.path) as fh:
        text = fh.read()
    fm, body = split_frontmatter(text)
    # so a reported line number is the one the editor will jump to
    line_offset = text[:len(text) - len(body)].count("\n") if body != text else 0

    results = []
    pack, primary = None, None

    def run(name, fn, *a):
        ok, problems, info = fn(*a)
        results.append({"gate": name, "ok": ok, "problems": problems, "info": info})

    if args.plan:
        run("plan structure", gate_plan, body, fm)
        run("superseded figures", gate_superseded, body, True, line_offset)
    else:
        pack, _pack_path = load_pack(args.pack, args.path)

        # target and primary keyword come from plan.md beside the article unless overridden
        target = args.target
        plan_path = os.path.join(os.path.dirname(os.path.abspath(args.path)), "plan.md")
        if os.path.exists(plan_path):
            with open(plan_path) as fh:
                pfm, pbody = split_frontmatter(fh.read())
            primary = pfm.get("primary_keyword")
            if target is None:
                target = extract_target(pfm, pbody)

        run("hard bans (detect-ai-tells)", gate_detector, args.path)
        run("prose length", gate_length, body, target)
        run("claim traceability", gate_claims, body, pack, line_offset)
        run("banned claims", gate_banned, body, pack)
        run("superseded figures", gate_superseded, body, True, line_offset)
        run("internal links", gate_links, body, pack)
        run("keyword placement", gate_keyword, body, primary)
        run("abbreviations (M1)", gate_m1, body)
        run("accuracy discipline", gate_accuracy, body, line_offset)

    failed = [r for r in results if not r["ok"]]
    verdict = "PASS" if not failed else "FAIL"

    report = None
    if args.report and not args.plan:
        report = build_report(body, pack, primary)

    if args.json:
        payload = {"path": args.path, "verdict": verdict, "gates": results}
        if report:
            payload["report"] = report
        print(json.dumps(payload, indent=2))
    else:
        print(f"{args.path}")
        print(f"mode: {'plan' if args.plan else 'article'}\n")
        for r in results:
            mark = "ok  " if r["ok"] else "FAIL"
            print(f"[{mark}] {r['gate']}")
            for p in r["problems"][:12]:
                print(f"         {p}")
            if len(r["problems"]) > 12:
                print(f"         ... and {len(r['problems']) - 12} more")
            for k, v in (r["info"] or {}).items():
                print(f"         . {k}: {v}")
        if report:
            print("\n--- shape (descriptive, not gated) ---")
            print(f"prose words {report['prose_words']} across {report['h2_count']} H2 sections")
            for row in report["words_per_section"]:
                print(f"    {row['words']:5d}  {row['section']}")
            if "links_by_direction" in report:
                print(f"  links {report['links_total']} total, "
                      f"{len(report['links_by_target'])} distinct, by direction: {report['links_by_direction']}")
            if "primary_occurrences" in report:
                print(f"  primary keyword {report['primary_keyword']!r}: {report['primary_occurrences']} occurrences")
            print(f"  claim markers {report['claim_markers_total']}: {report['claims_by_id']}")
            if report.get("claims_available_unused"):
                print(f"  approved but uncited: {', '.join(report['claims_available_unused'])}")
            for gname, bal in (report.get("term_group_balance") or {}).items():
                inner = ", ".join(f"{k} {v}" for k, v in bal.items() if k != "_total")
                print(f"  term group {gname}: total {bal['_total']}  ({inner})")

        print(f"\nVERDICT: {verdict}" + ("" if not failed else f"  ({len(failed)} gate(s) failed)"))
        if verdict == "PASS":
            print("Mechanics are clean. Judgment is still open: run quality-controller on whether\n"
                  "the argument holds and whether each section earns its place.")

    return 0 if (verdict == "PASS" or args.no_exit_code) else 1


if __name__ == "__main__":
    sys.exit(main())
