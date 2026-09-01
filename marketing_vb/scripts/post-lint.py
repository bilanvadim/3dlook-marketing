#!/usr/bin/env python3
"""post-lint.py — mechanical gate for ONE social post, before any LLM looks at it.

WHY
---
Measured on the `glp-1-market-hub` pack (9 posts, 2026-08-28): the LLM quality
loop cost 42.9M context tokens, of which `quality-controller` alone was 7.1M over
112 turns. What it actually caught on that pack was, in order: "under a minute"
where `proof-points.md` says "Under 45 seconds"; `article_slug` carrying the
workspace FOLDER name (`glp-1-market-hub`) instead of the published slug
(`glp-1-market`); and a design tip claiming the article assets avoid photography
when `cover-3.webp` is a photograph. The first two are string comparisons. Paying
Opus twelve turns to do a string comparison is the thing this file removes.

So: everything decidable by comparing the post against files on disk runs here,
for free, and the LLM gates keep only the judgment — is the angle strong, does the
voice hold, is the position real.

Scope, deliberately narrow:
  * this checks ONE post.md. Cross-profile deduplication is `social-editor`'s job
    and cannot be decided from a single file.
  * it does NOT edit. Same reason `post-brand-checker` does not: a mechanical fix
    to a sentence that a human would have cut is a worse post that now passes.

BODY vs FILE. Every check runs on the POST BODY, not on the whole file. The file
also carries an `**Angle:**` / `**Claims used:**` metadata block (400+ words on
recent packs) and a `### Design tip`, and running a copy detector over those
produces confident nonsense: on 2026-08-28 the only "hard fail" reported for
`linkedin-vadim` was two em dashes inside `## Post — linkedin-vadim — glp-1-market`,
a heading that post-drafter's own file template mandates. Body extraction is the
first thing this script does and the reason its verdicts are usable.

USAGE
    scripts/post-lint.py workspace/social/articles/<slug>/<profile>/post.md
    scripts/post-lint.py <slug> <profile>              # same thing, resolved
    scripts/post-lint.py <slug> --all                  # every profile in the pack
    ... [--summary] [--gate] [--json]

`--gate` exits 1 when there is at least one hard fail, so a runner can branch on
it. Without it the exit code is 0 and the JSON is a diagnostic — same contract as
`detect-ai-tells.py`, which this script calls for the copy layer instead of
re-implementing its 27 categories.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.dirname(HERE)                                  # …/marketing_vb

# The frontmatter/body parsers and the profile list live in social_pack.py and are
# imported, not copied. Two copies of a 15-line parser is how this repo lost the
# manifest schema: three agents each carried their own and the file's shape
# depended on which one wrote last.
sys.path.insert(0, HERE)
from social_pack import (                                     # noqa: E402
    split_frontmatter, extract_body, active_profiles, resolve_source,
    published_slug, budget_for,
)
DETECTOR = os.path.join(PROJ, "brand-assets", "style-guides", "scripts", "detect-ai-tells.py")
CONFIG = os.path.join(PROJ, "brand-assets", "social-profiles-config.md")
PROOF = os.path.join(PROJ, "brand-assets", "product-info", "proof-points.md")
LI_PROMPTS = os.path.join(PROJ, "brand-assets", "linkedin-post-prompts.md")

REQUIRED_FM = ("profile", "platform", "article_slug", "product", "status", "created")
DESIGN_FIELDS = ("Article visual:", "Format:", "Adaptation:", "Keep:")
FORMATS = ("text", "text + photo", "carousel", "infographic", "lead magnet", "poll", "screenshot")

EMOJI = re.compile(
    "[" "\U0001F300-\U0001FAFF" "\U00002600-\U000027BF" "\U0001F1E6-\U0001F1FF"
    "\U00002190-\U000021FF" "\U00002B00-\U00002BFF" "\U0000FE0F" "]")
HASHTAG = re.compile(r"(?<!\w)#[A-Za-z][\w-]{1,}")


# ---------------------------------------------------------------------------
# parsing
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# numbers
# ---------------------------------------------------------------------------

_NUM = re.compile(r"(?<![\w.])(\d[\d,]*\.?\d*)\s*(%|percent|cm|kg|mm|seconds?|secs?|"
                  r"minutes?|mins?|hours?|days?|weeks?|months?|years?|million|billion|"
                  r"m\b|bn\b|k\b|x\b)?", re.I)
# Numbers that are never a claim: years, small counts, list markers, version-ish.
_SAFE = re.compile(r"^(19|20)\d\d$")


def numeric_claims(body: str):
    """Number-ish tokens in the body that could be a factual claim."""
    out = []
    for m in _NUM.finditer(body):
        raw = m.group(1).replace(",", "").rstrip(".")
        unit = (m.group(2) or "").lower()
        digits = m.group(1).replace(",", "").rstrip(".")
        if _SAFE.match(digits):
            continue
        try:
            val = float(raw)
        except ValueError:
            continue
        # bare small integers with no unit are counts ("two photos", "three dates")
        if not unit and val <= 10 and val == int(val):
            continue
        out.append((m.group(0).strip(), val, unit, body[:0]))
    return out


def _num_tokens(text: str):
    """Digit strings present in a reference text, trailing sentence period removed.

    "…by 2030." and "…by 2030" are the same figure; without the strip every number
    that ended a sentence in the post read as unsourced. Three of the four findings
    on the first real pack were this."""
    return {t.replace(",", "").rstrip(".")
            for t in re.findall(r"\d[\d,]*\.?\d*", text)}


def check_numbers(body: str, source_text: str):
    """Any number in the post must exist in the article of record or proof-points.

    Not a hallucination test — a DRIFT test. The 2026-08-28 pack shipped "under a
    minute" against a sourced "Under 45 seconds": true, unsourced, and weaker than
    the real figure. Comparison is on the digits, because the wording around a
    number is exactly what a post is allowed to change."""
    try:
        proof = open(PROOF, encoding="utf-8", errors="replace").read()
    except OSError:
        proof = ""
    allowed = _num_tokens(source_text) | _num_tokens(proof)
    issues = []
    for token, val, unit, _ in numeric_claims(body):
        digits = re.findall(r"\d[\d,]*\.?\d*", token)
        if not digits:
            continue
        d = digits[0].replace(",", "").rstrip(".")
        if d in allowed:
            continue
        # 30/45 in "30 to 45 seconds" style ranges, both halves must resolve
        issues.append({
            "number": token,
            "why": "not present in the article of record or in proof-points.md",
        })
    return issues


# ---------------------------------------------------------------------------
# detector bridge
# ---------------------------------------------------------------------------

def run_detector(body: str, profile: str):
    if not os.path.exists(DETECTOR):
        return {"error": f"detector not found at {DETECTOR}"}
    try:
        p = subprocess.run(
            [sys.executable, DETECTOR, "--stdin", "--channel", "post",
             "--profile", profile],
            input=body, capture_output=True, text=True, timeout=120)
        return json.loads(p.stdout or "{}")
    except (OSError, ValueError, subprocess.SubprocessError) as e:
        return {"error": f"{type(e).__name__}: {e}"}


# ---------------------------------------------------------------------------
# the lint
# ---------------------------------------------------------------------------

def lint(path: str, source_text: str = "", source_slug: str = ""):
    rel = os.path.relpath(path, PROJ)
    if not os.path.exists(path):
        return {"post": rel, "hard_fails": [{"check": "missing", "detail": "no post.md"}],
                "warnings": [], "metrics": {}}
    text = open(path, encoding="utf-8", errors="replace").read()
    fm, _ = split_frontmatter(text)
    body, cta, design = extract_body(text)
    profile = fm.get("profile") or os.path.basename(os.path.dirname(path))

    hard, warn = [], []

    def H(check, detail):
        hard.append({"check": check, "detail": detail})

    def W(check, detail):
        warn.append({"check": check, "detail": detail})

    # 1. structure
    for k in REQUIRED_FM:
        if not fm.get(k):
            H("frontmatter", f"missing `{k}:`")
    if not body:
        H("body", "no post body found between the metadata block and the design tip")
    if source_slug and fm.get("article_slug") and fm["article_slug"] != source_slug:
        H("article_slug", f"`{fm['article_slug']}` != published slug `{source_slug}` "
                          "(a social artifact carrying the folder name cannot be joined "
                          "to the published URL)")
    if design:
        for f in DESIGN_FIELDS:
            if f"**{f}" not in design:
                W("design_tip", f"missing `**{f}**` field")
        fmt = re.search(r"\*\*Format:\*\*\s*(.+)", design)
        if fmt:
            # Every post on the measured pack wrote `carousel (3 slides)` or
            # `poll (linkedin native, two options: …)`. The parenthetical is useful
            # to the designer, so only the leading token is validated.
            raw = fmt.group(1).strip().strip("`")
            head = re.split(r"\s*[({\[]", raw, 1)[0].strip().lower()
            if head not in FORMATS:
                W("design_tip", f"format `{head}` is not one of the seven allowed formats")
            elif fm.get("format") and fm["format"].strip().lower() != head:
                W("design_tip", f"design tip says `{head}`, frontmatter says "
                                f"`{fm['format']}` — the manifest reads the frontmatter")
    else:
        W("design_tip", "no `### Design tip` block")
    if not cta:
        W("cta", "no `**CTA:**` line")

    # 2. placeholders
    for marker in ("[CONFIRM]", "TODO", "TBD", "{slug}", "{profile}"):
        if marker in body:
            H("placeholder", f"`{marker}` left in the body")

    # 3. length. A platform HARD limit is a hard fail; a brief's word range is a
    # target, so being inside 10% of it is a warning. `linkedin-katerina` shipped
    # at 251 against 180-250 on the measured pack: worth telling someone, not
    # worth a rewrite round on Opus.
    unit, lo, hi = budget_for(profile)
    tweets = re.split(r"^\s*(?:\[Tweet\s*\d+/\d+\]|---)\s*$", body, flags=re.M) \
        if re.search(r"\[Tweet\s*\d+/\d+\]", body) else [body]
    tweets = [t.strip() for t in tweets if t.strip()]
    words = len(re.findall(r"\b[\w'-]+\b", body))
    chars = max((len(t) for t in tweets), default=0)
    if unit == "words" and body:
        if words > hi * 1.10 or words < lo * 0.90:
            H("length", f"{words} words, brief says {lo}-{hi}")
        elif words > hi or words < lo:
            W("length", f"{words} words, brief says {lo}-{hi}")
    elif unit == "chars" and body:
        if chars > hi:
            over = [f"{len(t)}" for t in tweets if len(t) > hi]
            H("length", f"{'tweet(s) at ' + ', '.join(over) if len(tweets) > 1 else str(chars)}"
                        f" chars, hard limit {hi}")
        elif chars < lo:
            W("length", f"{chars} chars, brief says {lo}-{hi}")

    # 4. house rules — hard, and they outrank every per-profile brief
    tags = HASHTAG.findall(body)
    if tags:
        H("hashtags", f"{len(tags)} hashtag(s): {', '.join(tags[:5])} — the house rule is 0")
    emoji = EMOJI.findall(body)
    if len(emoji) > 2:
        H("emoji", f"{len(emoji)} emoji, the house rule is max 2")

    # 5. numbers
    if body and source_text:
        for iss in check_numbers(body, source_text):
            H("number_drift", f"{iss['number']} — {iss['why']}")

    # 6. copy layer, on the body only
    det = run_detector(body, profile) if body else {}
    for hf in det.get("hard_fails", []) or []:
        ex = (hf.get("hits") or [{}])[0].get("example", "")
        H(f"ai-tells:{hf.get('category')}",
          f"{hf.get('count')}× — {ex[:120]}")
    # The detector reports hashtags, emoji AND rhythm under house_rule_violations.
    # Hashtags and emoji are the two rules that override every per-profile brief;
    # "monotone rhythm: variation 0.34 (want >0.35)" is a style signal and became
    # a hard fail on two shipped posts that were otherwise clean. Only the first
    # two gate.
    for v in det.get("house_rule_violations", []) or []:
        t = str(v)
        (H if re.search(r"hashtag|emoji", t, re.I) else W)("ai-tells:house_rule", t[:160])

    return {
        "post": rel,
        "profile": profile,
        "hard_fails": hard,
        "warnings": warn,
        "metrics": {
            "words": words, "chars": chars,
            "unit": unit, "budget": [lo, hi],
            "hashtags": len(tags), "emoji": len(emoji),
            "ai_density_per_1000_words": det.get("ai_density_per_1000_words"),
            "severity": det.get("severity"),
        },
        "verdict": "PASS" if not hard else f"FAIL ({len(hard)})",
    }


def summarise(res):
    out = [f"{res['verdict']:12s} {res['post']}"]
    m = res.get("metrics") or {}
    if m.get("unit"):
        out.append(f"  len: {m['words']} words / {m['chars']} chars "
                   f"(budget {m['budget'][0]}-{m['budget'][1]} {m['unit']}) · "
                   f"#{m['hashtags']} hashtags · {m['emoji']} emoji · "
                   f"ai-density {m.get('ai_density_per_1000_words')}")
    for h in res["hard_fails"]:
        out.append(f"  ✗ [{h['check']}] {h['detail']}")
    for w in res["warnings"]:
        out.append(f"  · [{w['check']}] {w['detail']}")
    return "\n".join(out)


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("target", help="path to post.md, or an article slug")
    p.add_argument("profile", nargs="?", help="profile id (when target is a slug)")
    p.add_argument("--all", action="store_true", help="every active profile in the pack")
    p.add_argument("--slug", help="article slug, when `target` is a path outside the "
                                  "workspace layout (the slug is what makes the number "
                                  "and published-slug checks possible)")
    p.add_argument("--summary", action="store_true")
    p.add_argument("--gate", action="store_true", help="exit 1 on any hard fail")
    a = p.parse_args(argv)

    paths, source_text, source_slug = [], "", ""
    if os.path.sep in a.target or a.target.endswith(".md"):
        paths = [os.path.abspath(a.target)]
        # …/workspace/social/articles/<slug>/<profile>/post.md — recover the slug
        # from the path so a direct path gets the same checks as `<slug> <profile>`.
        m = re.search(r"workspace/social/articles/([^/]+)/", paths[0])
        slug = a.slug or (m.group(1) if m else None)
    else:
        slug = a.target
        root = os.path.join(PROJ, "workspace", "social", "articles", slug)
        if a.all or not a.profile:
            paths = [os.path.join(root, pid, "post.md") for pid, _, _ in active_profiles()]
        else:
            paths = [os.path.join(root, a.profile, "post.md")]
    if slug:
        src, _st, _err = resolve_source(slug)
        if src:
            source_text = open(src, encoding="utf-8", errors="replace").read()
            source_slug = published_slug(slug) or ""

    results = [lint(x, source_text, source_slug) for x in paths if os.path.exists(x)
               or not a.all]
    if a.summary:
        print("\n".join(summarise(r) for r in results))
    else:
        print(json.dumps(results if len(results) > 1 else results[0], indent=2))
    if a.gate and any(r["hard_fails"] for r in results):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
