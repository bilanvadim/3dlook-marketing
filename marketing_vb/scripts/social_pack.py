#!/usr/bin/env python3
"""social_pack.py — the mechanical half of the social pipeline.

WHY THIS EXISTS
---------------
Measured on one real pack (`glp-1-market-hub`, 9 posts, 2026-08-28, session
1ee1d21a), deduplicated by message id because the transcript logs each streamed
message several times:

    stage                        runs  turns   context tokens        $ (Opus list)
    coordinator (one session)       1    151       25,492,296              55.66
    post-drafter                    9    111        7,541,484              36.78
    quality-controller              9    112        7,087,562              36.35
    post-brand-checker              9     45        2,176,363               4.49
    ---------------------------------------------------------------------------
    total                                42,883,301 tokens · ~$133 · ~$14.8/post

59% of that went on the COORDINATOR, not on writing. Its median request carried
206K tokens of context and it made 151 of them: 165 Bash calls (229KB of output),
27 subagent reports, an 8KB run brief and a 27KB digest, all accumulating in one
session where every later request re-reads every earlier one. None of that work
needs a language model. Directory listings, digest assembly, manifest shaping,
length arithmetic and "which profiles are still missing" are file operations.

This script is those file operations. What is left for the model is writing the
post and judging it.

The second thing it does is make the drafter prompt BYTE-IDENTICAL across
profiles up to its last section (`prompt` subcommand). Prompt caching keys on the
exact prefix, so nine drafters that open with the same bytes let eight of them
read a cache instead of writing one. On the measured pack each drafter paid
70-95K of cache WRITES (billed above input rate) for a prefix that was
substantially the same text in a different order. Combined with
`subagentPromptCacheTtl: "1h"` in .claude/settings.json — the subagent default is
5 MINUTES and the profiles ran 4-6 minutes apart, so every prefix expired just
before the next drafter could have used it — that is the single cheapest change
in the pipeline.

WHAT IT DOES NOT DO
-------------------
No judgment. It never decides an angle, never rewrites a sentence, never scores a
post. `brief` generates the parts of the run brief that are lookups and leaves a
marked human section for the claims discipline, which is the part that actually
needs reading the article.

USAGE
    scripts/social_pack.py profiles [<slug>]
    scripts/social_pack.py source   <slug>
    scripts/social_pack.py brief    <slug> [--force]
    scripts/social_pack.py prompt   <slug> <profile> [--check-prefix]
    scripts/social_pack.py qc-plan  <slug>
    scripts/social_pack.py manifest <slug> [--write]
    scripts/social_pack.py digest   <slug> [--write]
    scripts/social_pack.py report   <slug> [--write]
    scripts/social_pack.py scores   [<slug>]
"""
from __future__ import annotations

import argparse
import glob
import hashlib
import json
import os
import re
import sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.dirname(HERE)                                   # …/marketing_vb
CONFIG = os.path.join(PROJ, "brand-assets", "social-profiles-config.md")
LI_PROMPTS = os.path.join(PROJ, "brand-assets", "linkedin-post-prompts.md")
LI_SPLIT = os.path.join(PROJ, "brand-assets", "linkedin-prompts")
PAST = os.path.join(PROJ, "brand-assets", "past-posts")
QUALITY = os.path.join(PROJ, "workspace", "_quality", "social")

HUMAN_START = "<!-- HUMAN:START — claims discipline and visuals. Regeneration keeps this. -->"
HUMAN_END = "<!-- HUMAN:END -->"

# Company accounts first, then personal LinkedIn alphabetically. Same order the
# digest uses, defined once here.
COMPANY_ORDER = ["twitter-company", "instagram-company", "facebook-company",
                 "linkedin-company"]

# Length budgets, in the unit the profile's own brief is written in. LinkedIn is
# specified in WORDS by linkedin-post-prompts.md; the three company accounts are
# specified in CHARACTERS by social-profiles-config.md. Keeping both units is not
# sloppiness, it is what the two source files say, and it is why the manifest
# carries exactly one length field per profile.
BUDGET = {
    "twitter-company":    ("chars", 1, 280),
    "instagram-company":  ("chars", 600, 1000),
    "facebook-company":   ("chars", 800, 1200),
    "linkedin-company":   ("words", 180, 280),
    "_linkedin_personal": ("words", 100, 170),
}

# Budgets whose upper bound is a WALL, not a target. Everywhere else the lint
# allows 10% over the band before it hard-fails, because a 251-word post against
# a 250-word target is not worth a rewrite round on Opus. The five personal
# LinkedIn profiles are different: 170 is Vadim's decision of 2026-09-04, taken
# because 240-250-word posts read like memos, and 187 would put them straight
# back there.
HARD_MAX = {"_linkedin_personal": 170}

PERSONAL_LINKEDIN_EXCLUDE = ("linkedin-company",)


def is_personal_linkedin(profile: str) -> bool:
    """One of the five people. `linkedin-company` is a company page and keeps its
    own length, register and rules — see `linkedin-post-prompts.md`."""
    return (profile.startswith("linkedin-")
            and profile not in PERSONAL_LINKEDIN_EXCLUDE)


def budget_for(profile: str):
    """(unit, lo, hi) for one profile. Single source for the brief, the lint and
    the manifest, so a budget change is one edit."""
    if profile in BUDGET:
        return BUDGET[profile]
    if profile.startswith("linkedin-"):
        return BUDGET["_linkedin_personal"]
    return (None, 0, 0)


def hard_max_for(profile: str):
    """The ceiling that hard-fails with no tolerance, or None if the profile's
    upper bound is a target."""
    if profile in HARD_MAX:
        return HARD_MAX[profile]
    if is_personal_linkedin(profile):
        return HARD_MAX["_linkedin_personal"]
    return None


# ---------------------------------------------------------------------------
# shared parsing — imported by post-lint.py, so it exists in exactly one file
# ---------------------------------------------------------------------------

def split_frontmatter(text: str):
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end < 0:
        return {}, text
    raw, rest = text[3:end], text[end + 4:]
    fm = {}
    for line in raw.splitlines():
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line.strip())
        if m:
            fm[m.group(1)] = m.group(2).strip().strip('"\'')
    return fm, rest.lstrip("\n")


def extract_body(text: str):
    """(body, cta, design_tip) from a post.md, for either layout on disk.

    CURRENT layout (post-drafter since 2026-07):

        ## Post: {profile} / {slug}
        **Angle:** …  **Claims used:** …  **Length:** …     <- metadata block
        ---
        {BODY}
        **CTA:** …
        ---
        ### Design tip

    LEGACY layout (packs up to 2026-08-07): no heading, no metadata block, the body
    starts straight after the frontmatter, and the design tip is a bold
    `**Design tip**` paragraph with unbolded `Article visual:` lines in a blockquote.

    Getting this wrong is not a cosmetic failure. A first version of this function
    keyed the metadata block off "any `**Key:**` line", which matched `**CTA:**` in
    the legacy layout, so the body was taken to start after the `---` that FOLLOWS
    the CTA — i.e. the design tip became "the post" and the post disappeared. Every
    legacy pack then reported inflated lengths and em-dash hard fails that were
    really design-tip prose.

    So: cut the design tip first, decide the start from whether a `## Post` heading
    exists, and never treat `**CTA:**` as metadata."""
    _fm, rest = split_frontmatter(text)

    design = ""
    m = (re.search(r"^###\s+Design tip\s*$", rest, re.M)
         or re.search(r"^\*\*Design tip\*\*\s*$", rest, re.M))
    if m:
        design = rest[m.end():]
        rest = rest[:m.start()]

    lines = rest.splitlines()
    start = 0
    if re.search(r"^##\s+Post\b", rest, re.M):
        seen_meta = False
        for i, line in enumerate(lines):
            t = line.strip()
            if t.startswith("## Post"):
                seen_meta = True
                continue
            # metadata keys, but never the CTA — that one closes the body
            if seen_meta and re.match(r"^\*\*[A-Z][^*]*:\*\*", t) \
               and not t.startswith("**CTA:**"):
                continue
            if seen_meta and t == "---":
                start = i + 1
                break

    cta, keep = "", []
    for line in lines[start:]:
        t = line.strip()
        if t.startswith("**CTA:**"):
            cta = t[len("**CTA:**"):].strip()
            continue
        keep.append(line)
    body = "\n".join(keep)
    # HTML comments are the drafter's notes to itself, not post text. The
    # `twitter-company` post on the 2026-08-28 pack carried
    # "<!-- Single tweet, 257 chars. No thread. -->", which made the body read as
    # 365 characters (over the 280 limit) and put 257 and 260 into the post as
    # unsourced numbers. Three findings, all of them the comment.
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    body = re.sub(r"\n?---\s*$", "", body.strip()).strip()
    return body, cta, design.strip()


def active_profiles():
    """[(profile_id, platform, handle)], posts_per_week > 0, in config order.

    Parsed from the file Vadim edits, so enabling a profile stays a one-file
    change and the fan-out, the digest and the manifest all follow."""
    try:
        text = open(CONFIG, encoding="utf-8", errors="replace").read()
    except OSError:
        return []
    out = []
    for block in re.findall(r"```yaml\n(.*?)```", text, re.S):
        pid = re.search(r"^profile_id:\s*(\S+)", block, re.M)
        ppw = re.search(r"^posts_per_week:\s*(\d+)", block, re.M)
        plat = re.search(r"^platform:\s*(\S+)", block, re.M)
        if pid and ppw and int(ppw.group(1)) > 0:
            p = pid.group(1).strip().strip('"\'')
            out.append((p, plat.group(1).strip() if plat else "", handle_for(p, block)))
    return out


def handle_for(profile: str, block: str) -> str:
    """The `handle` the manifest requires, derived instead of remembered.

    The config does not use one field for it: `handle:` on twitter and instagram,
    `page:` on facebook, and nothing at all on the six LinkedIn profiles, which
    carry `owner:` with the role in brackets. So the order is handle, page, then
    the owner's name with the bracketed role stripped, and the two company
    LinkedIn/Facebook entries resolve to the company name.

    This normalises one existing value: `linkedin-katerina` was carrying
    `katerina-galich-64014614`, a LinkedIn URL fragment that is in no source file,
    while the other four personal profiles carried plain names. It becomes
    `Katerina Galich`."""
    m = re.search(r"^handle:\s*(.+)$", block, re.M)
    if m:
        return m.group(1).strip().strip('"\'')
    m = re.search(r"^page:\s*(.+)$", block, re.M)
    if m:
        return m.group(1).strip().strip('"\'')
    if profile == "linkedin-company":
        return "3DLOOK"
    m = re.search(r"^owner:\s*(.+)$", block, re.M)
    if m:
        return re.sub(r"\s*\(.*?\)\s*", "", m.group(1)).strip().strip('"\'')
    return ""


def skipped_profiles():
    try:
        text = open(CONFIG, encoding="utf-8", errors="replace").read()
    except OSError:
        return []
    out = []
    for block in re.findall(r"```yaml\n(.*?)```", text, re.S):
        pid = re.search(r"^profile_id:\s*(\S+)", block, re.M)
        ppw = re.search(r"^posts_per_week:\s*(\d+)", block, re.M)
        if pid and ppw and int(ppw.group(1)) == 0:
            out.append(pid.group(1).strip().strip('"\''))
    return out


def digest_order(profiles):
    comp = [p for p in COMPANY_ORDER if p in profiles]
    rest = sorted(p for p in profiles if p not in COMPANY_ORDER)
    return comp + rest


def profile_block(profile: str):
    """The raw yaml block for one profile from social-profiles-config.md."""
    try:
        text = open(CONFIG, encoding="utf-8", errors="replace").read()
    except OSError:
        return ""
    for block in re.findall(r"```yaml\n(.*?)```", text, re.S):
        if re.search(rf"^profile_id:\s*{re.escape(profile)}\s*$", block, re.M):
            return block.strip()
    return ""


def linkedin_brief(profile: str):
    """The per-profile section of linkedin-post-prompts.md, plus the rules that
    apply to every LinkedIn profile. Returns "" for non-LinkedIn profiles."""
    if not profile.startswith("linkedin-"):
        return ""
    split = os.path.join(LI_SPLIT, f"{profile}.md")
    if os.path.exists(split):
        return open(split, encoding="utf-8", errors="replace").read().strip()
    try:
        text = open(LI_PROMPTS, encoding="utf-8", errors="replace").read()
    except OSError:
        return ""
    secs = re.split(r"^## ", text, flags=re.M)
    shared, mine = [], ""
    for s in secs:
        head = s.splitlines()[0] if s else ""
        if head.startswith("House-rule overrides") or head.startswith("Additional resolutions") \
           or head.startswith("Rules that apply to every LinkedIn profile"):
            shared.append("## " + s.strip())
        # personal-only: the length ceiling, sentence length, location discipline.
        # Same split as scripts/split-linkedin-prompts.py, which is what normally
        # produces these files; this branch only runs when the derivative is gone.
        if head.startswith("Rules for the five personal profiles") \
           and is_personal_linkedin(profile):
            shared.append("## " + s.strip())
        if head.startswith(f"`{profile}`"):
            mine = "## " + s.strip()
    return ("\n\n".join(shared) + "\n\n" + mine).strip()


# ---------------------------------------------------------------------------
# article of record
# ---------------------------------------------------------------------------

_SKIP_PREFIX = ("plan", "changelog", "qc-", "review", "log", "phase",
                "publisher-report", "source-with-comments", "comments")


def prose_lines(text: str) -> int:
    """Lines that read as article prose: not a table row, bullet, heading or quote,
    and long enough to be a sentence.

    Needed because file size does not separate an article from a checklist.
    `glp-1-market-hub/publish-package.md` is 18KB of meta and checklist with no
    article body at all, and the 2026-08-28 run brief had to warn the drafters by
    hand not to use it."""
    n = 0
    for line in text.splitlines():
        s = line.strip()
        if not s or s[0] in "|-#>*+" or s.startswith("```"):
            continue
        if len(s.split()) >= 15:
            n += 1
    return n


def resolve_source(slug: str):
    """(path, status, error) — the text the posts must be written FROM.

    Ranking, highest first:
      0  published-live-*.md   the page as published, when the pack follows a publish
      1  publish-package.md    the canonical package
      2  *final*.md / *revision*.md   newest version wins
      3  revised.md / edited.md / draft.md

    `published-live-*` is ranked ABOVE the package on purpose. On the 2026-08-28
    pack the package carried no article body and the drafts were ~500 words behind
    the live page after a late editorial pass, so every claim taken from a draft
    was untraceable to the published text. The switcher's resolver did not know
    about these files and the coordinator had to redirect nine drafters by hand.

    A candidate with fewer than 25 prose lines is skipped as a stub or a
    checklist, whatever its size."""
    root = os.path.join(PROJ, "workspace", "seo", "articles", slug)
    if not slug or not os.path.isdir(root):
        return None, None, f"no article directory workspace/seo/articles/{slug or '<slug>'}"

    def rank(name: str):
        n = name.lower()
        if not n.endswith(".md") or n.startswith(_SKIP_PREFIX):
            return None
        if n.startswith("published-live"):
            return 0
        if "publish-pack" in n:
            return 1
        if "final" in n or "revision" in n:
            return 2
        if n in ("revised.md", "edited.md", "draft.md"):
            return 3
        return None

    def ver(name: str) -> int:
        m = re.search(r"\bv(\d+)", name.lower())
        return int(m.group(1)) if m else 0

    cands = []
    paths = []
    for n in os.listdir(root):
        p = os.path.join(root, n)
        if os.path.isfile(p):
            paths.append(p)
        elif os.path.isdir(p) and not n.startswith("."):
            paths += [os.path.join(p, x) for x in os.listdir(p)
                      if os.path.isfile(os.path.join(p, x))]
    for p in paths:
        r = rank(os.path.basename(p))
        if r is None:
            continue
        cands.append((r, -ver(os.path.basename(p)), -os.path.getmtime(p), p))
    cands.sort()
    for *_x, p in cands:
        text = open(p, encoding="utf-8", errors="replace").read()
        if prose_lines(text) < 25:
            continue
        fm, _ = split_frontmatter(text)
        return p, fm.get("status", ""), None
    return None, None, ("no usable article text in the directory "
                        "(no published-live, package or draft with an article body)")


def _package_and_source(slug: str):
    """[(path, text)] for the publish package and the resolved source, in that order."""
    out = []
    root = os.path.join(PROJ, "workspace", "seo", "articles", slug)
    pkg = os.path.join(root, "publish-package.md")
    if os.path.exists(pkg):
        out.append((pkg, open(pkg, encoding="utf-8", errors="replace").read()))
    src, _st, _e = resolve_source(slug)
    if src and src != pkg:
        out.append((src, open(src, encoding="utf-8", errors="replace").read()))
    return out


# Frontmatter keys the SEO pipeline has actually used for the live URL, in
# precedence order. There is no single convention: the glp-1 package carries
# `production_url` + `target_url`, others carry none at all. Never fall back to
# grepping the body for a 3dlook.ai URL — the first one in a package is usually an
# internal link, and doing that made the wellness-platforms package report
# `beyond-bmi-business` (a link inside it) as its own address.
_URL_KEYS = ("production_url", "target_url", "published_url", "article_url",
             "live_url", "url")
_SLUG_KEYS = ("article_slug",)


def published_url(slug: str):
    for _path, text in _package_and_source(slug):
        fm, _ = split_frontmatter(text)
        for k in _URL_KEYS:
            if fm.get(k, "").startswith("http"):
                return fm[k]
    return ""


def published_slug(slug: str):
    """The slug the post frontmatter must carry: the PUBLISHED one.

    Order matters and is the point of this function:
      1. frontmatter `article_slug` — what the package says it shipped as;
      2. the package's `**URL slug:**` line — where the SEO pipeline records the
         intended address before publishing;
      3. the last segment of the live URL;
      4. frontmatter `slug:`;
      5. the workspace folder name.

    `slug:` sits fourth deliberately. On the wellness-platforms package it holds
    `2026-08-31-ai-body-data-wellness-platforms-hub`, a working directory name,
    while the Meta section says the page is `ai-body-data-wellness-platforms`. On
    the glp-1 pack the same mismatch shipped: two posts carried the folder name and
    QC caught it, because a social artifact carrying it cannot be joined to the
    published URL."""
    docs = _package_and_source(slug)
    for _path, text in docs:
        fm, _ = split_frontmatter(text)
        for k in _SLUG_KEYS:
            if fm.get(k):
                return fm[k]
    for _path, text in docs:
        m = re.search(r"^\*\*URL slug:\*\*\s*`?([\w/-]+)`?", text, re.M)
        if m:
            return m.group(1).strip("/").split("/")[-1]
    url = published_url(slug)
    if url:
        seg = [x for x in url.rstrip("/").split("/") if x]
        if seg and seg[-1] not in ("content-hub", "blog"):
            return seg[-1]
    for _path, text in docs:
        fm, _ = split_frontmatter(text)
        if fm.get("slug"):
            return fm["slug"]
    return slug


# ---------------------------------------------------------------------------
# pack state
# ---------------------------------------------------------------------------

def pack_root(slug: str):
    return os.path.join(PROJ, "workspace", "social", "articles", slug)


def pack_state(slug: str):
    root = pack_root(slug)
    done, missing = [], []
    for pid, _plat, _h in active_profiles():
        p = os.path.join(root, pid, "post.md")
        if os.path.exists(p) and extract_body(open(p, encoding="utf-8",
                                                  errors="replace").read())[0]:
            done.append(pid)
        else:
            missing.append(pid)
    return done, missing


def past_posts_map():
    """profile -> [paths]. The spec's `past-posts/{profile}/` resolves for one
    profile out of nine; the personal ones live under
    `past-posts/linkedin-personal/<name>/`. Resolved here by matching the
    profile's given name against the directory names, so the drafter never has to
    be told the layout by hand again."""
    out = {}
    for pid, _plat, handle in active_profiles():
        direct = os.path.join(PAST, pid)
        if os.path.isdir(direct):
            out[pid] = sorted(glob.glob(os.path.join(direct, "*.md")))
            continue
        first = (handle.split() or [""])[0].lower()
        hits = []
        for d in sorted(glob.glob(os.path.join(PAST, "linkedin-personal", "*"))):
            if not os.path.isdir(d):
                continue
            name = os.path.basename(d).lower()
            if first and (first in name or name.split("-")[0] in pid):
                hits = sorted(glob.glob(os.path.join(d, "*.md")))
                break
        out[pid] = hits
    return out


def sibling_angles(slug: str, exclude: str):
    """[(profile, angle, format)] already written in this pack. Read from the
    files, so it is correct after a resume and cannot go stale the way a
    hand-maintained table in the run brief does."""
    out = []
    root = pack_root(slug)
    for pid in digest_order([p for p, _, _ in active_profiles()]):
        if pid == exclude:
            continue
        p = os.path.join(root, pid, "post.md")
        if not os.path.exists(p):
            continue
        text = open(p, encoding="utf-8", errors="replace").read()
        fm, _ = split_frontmatter(text)
        m = re.search(r"^\*\*Angle:\*\*\s*(.+)$", text, re.M)
        angle = (m.group(1).strip() if m else "").strip()
        if len(angle) > 400:
            angle = angle[:400].rsplit(" ", 1)[0] + " …"
        out.append((pid, angle, fm.get("format", "")))
    return out


def last_qc_seen():
    """profile -> the date of its most recent QC report, from the report filenames
    in workspace/_quality/social (`YYYY-MM-DD-post-drafter-<slug>-<profile>.md`)."""
    out = {}
    ids = [p for p, _pl, _h in active_profiles()]
    for p in sorted(glob.glob(os.path.join(QUALITY, "*.md"))):
        name = os.path.basename(p)
        m = re.match(r"(\d{4}-\d{2}-\d{2})", name)
        if not m:
            continue
        for pid in ids:
            # Report filenames are not uniform: the LinkedIn ones carry the full
            # profile id, the three company accounts are named `-twitter.md`,
            # `-instagram.md`, `-facebook.md` with no `-company` suffix.
            aliases = {pid, pid.replace("linkedin-", ""), pid.replace("-company", "")}
            if any(a and (a == name[:-3].split("-")[-1] or f"-{a}." in name
                          or f"-{a}-" in name or name.endswith(f"-{a}.md"))
                   for a in aliases):
                out[pid] = max(out.get(pid, ""), m.group(1))
    return out


def qc_reports(slug: str):
    """profile -> score string, from workspace/_quality/social."""
    out = {}
    for p in sorted(glob.glob(os.path.join(QUALITY, "*.md"))):
        text = open(p, encoding="utf-8", errors="replace").read()
        fm, _ = split_frontmatter(text)
        if fm.get("artifact", "").find(slug) < 0 and slug not in os.path.basename(p) \
           and slug not in text[:2000]:
            continue
        m = re.search(r"total_score:\s*(\d+)\s*/\s*(\d+)", text) or \
            re.search(r"\*\*Total:\s*(\d+)\s*/\s*(\d+)", text)
        if not m:
            continue
        prof = ""
        for pid, _plat, _h in active_profiles():
            if pid in os.path.basename(p) or f"/{pid}/" in text[:3000]:
                prof = pid
                break
        if not prof:
            continue
        out[prof] = f"{m.group(1)}/{m.group(2)}"
    return out


# ---------------------------------------------------------------------------
# brief
# ---------------------------------------------------------------------------

def build_brief(slug: str, force: bool = False):
    """Generate the lookup half of `_run-brief.md` and keep the human half.

    On 2026-08-28 this file was written by hand inside a 200K-token coordinator
    session, and it was the reason the drafters stopped reading CLAUDE.md — worth
    keeping, wrong place to produce. Everything below that is a path, a list, a
    count or a length budget is a lookup; the claims discipline and the visual
    assets are the part that needs a person (or a model) to have read the article,
    and that part lives between the HUMAN markers and survives regeneration."""
    src, status, err = resolve_source(slug)
    if err:
        return None, err
    root = pack_root(slug)
    os.makedirs(root, exist_ok=True)
    path = os.path.join(root, "_run-brief.md")
    text = open(src, encoding="utf-8", errors="replace").read()
    fm, _ = split_frontmatter(text)
    profiles = active_profiles()
    pmap = past_posts_map()
    url = published_url(slug)
    pslug = published_slug(slug)

    human = (f"{HUMAN_START}\n\n"
             "## Claims discipline for this article\n\n"
             "_Fill in: every number and boundary the posts may state, in the live wording.\n"
             "Anything not listed here is not available to a post._\n\n"
             "## Article visuals for the Design tip\n\n"
             "_Fill in: the assets that actually ship with the article, described as they\n"
             "are. A design tip must adapt one of these, not invent one._\n\n"
             f"{HUMAN_END}")
    if os.path.exists(path) and not force:
        return path, "exists — pass --force to regenerate the mechanical half"
    if os.path.exists(path):
        old = open(path, encoding="utf-8", errors="replace").read()
        m = re.search(re.escape(HUMAN_START) + r"(.*?)" + re.escape(HUMAN_END), old, re.S)
        if m:
            human = HUMAN_START + m.group(1) + HUMAN_END

    rows = []
    for pid, plat, handle in profiles:
        unit, lo, hi = budget_for(pid)
        cap = hard_max_for(pid)
        span = f"{lo}-{hi} {unit}" + (f", {cap} is a wall" if cap else "")
        n = len(pmap.get(pid) or [])
        where = (os.path.relpath(os.path.dirname(pmap[pid][0]), PROJ)
                 if pmap.get(pid) else "—")
        rows.append(f"| `{pid}` | {plat} | {handle} | {span} | {n} | {where} |")

    out = f"""# Run brief — social pack for `{slug}`

> Mechanical sections are generated by `scripts/social_pack.py brief {slug}`.
> Do not hand-edit them; they will be overwritten. The claims and visuals section
> between the HUMAN markers is preserved across regeneration.

Generated: {date.today().isoformat()}

## Paths

| | |
|---|---|
| Repo root | `{PROJ}` |
| Article of record | `{os.path.relpath(src, PROJ)}` |
| Article status | `{status or "—"}` |
| Published URL | {url or "— not published"} |
| **`article_slug` for every post** | **`{pslug}`** |
| Pack directory | `{os.path.relpath(root, PROJ)}` |

`article_slug` is the PUBLISHED slug, not the folder name. The folder mirrors the
SEO working directory; a post carrying the folder name cannot be joined to the
published URL.

## Profiles in this pack ({len(profiles)} active)

| Profile | Platform | Handle | Length | Past posts | Where |
|---|---|---|---|---|---|
{chr(10).join(rows)}

Skipped this pack: {", ".join("`" + p + "`" for p in skipped_profiles()) or "none"}.

## House rules — these outrank every per-profile brief

- **0 hashtags** on every profile, without exception.
- **Maximum 2 emoji.** Higher numbers in `linkedin-post-prompts.md` are a ceiling
  that the house rule overrides, not a target.
- **No em dash**, in any channel.
- Facts come only from the article of record above, and numbers only in the
  wording that file uses.
- A post is *inspired by* the article, never a summary of it.
- **The five personal LinkedIn profiles run on the rules in their own brief**
  (`brand-assets/linkedin-prompts/<profile>.md`, section "Rules for the five personal
  profiles", house rule of 2026-09-04): 100-170 words with 170 a hard ceiling, no
  sentence over 30 words, no location announced in the first sentence and no line about
  who you speak with all day, one thing actually taught, and a hook that is a claim
  rather than a question. `linkedin-company` keeps 180-280 words and its corporate
  register.

## Output contract

- Post: `{os.path.relpath(root, PROJ)}/<profile>/post.md`
- Then run `scripts/post-lint.py {slug} <profile> --summary --gate`. It checks
  length, hashtags, emoji, em dash, banned phrasings, placeholders, the published
  slug and every number against the article and `proof-points.md`. Fix hard fails
  before anything else looks at the post.
- The manifest and the digest are **not** written by hand:
  `scripts/social_pack.py manifest {slug} --write` and `digest {slug} --write`.

{human}
"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(out)
    meta = {"slug": slug, "published_slug": pslug, "generated": date.today().isoformat(),
            "article_of_record": os.path.relpath(src, PROJ),
            "drafter_model": "opus", "qc_policy": "sampled"}
    with open(os.path.join(root, "_pack.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)
    return path, None


# ---------------------------------------------------------------------------
# prompt — the cache-prefix machine
# ---------------------------------------------------------------------------

SHARED_MARK = "===== YOUR PROFILE. Everything above this line is shared. ====="


def drafter_prompt(slug: str, profile: str):
    """(shared_prefix, profile_tail, error).

    The caller passes `shared + tail` to post-drafter verbatim. `shared` is
    identical for every profile in the pack, which is the whole point: prompt
    caching keys on the exact prefix, so the first drafter writes the cache and
    the other eight read it. Anything that varies — the profile, its brief, its
    past posts, the angles already taken — is in the tail, after the marker.

    The article is INLINED rather than referenced. A path costs the drafter a
    Read turn, and a turn is a whole extra request carrying the whole context;
    inlining it makes the drafter's first action writing the post. On the measured
    pack the drafters spent 6 to 12 turns on reads that this prefix replaces."""
    src, status, err = resolve_source(slug)
    if err:
        return None, None, err
    root = pack_root(slug)
    brief_path = os.path.join(root, "_run-brief.md")
    if not os.path.exists(brief_path):
        return None, None, (f"no run brief — run `scripts/social_pack.py brief {slug}` first")
    brief = open(brief_path, encoding="utf-8", errors="replace").read()
    article = open(src, encoding="utf-8", errors="replace").read()

    shared = f"""Write one social post for the pack below. Everything you need is in this
prompt; you should not need to read any file before writing.

{brief}

# Article of record — `{os.path.relpath(src, PROJ)}`

Every claim, number and boundary in your post must be traceable to the text
below, in the wording it uses here.

<article>
{article.strip()}
</article>

# What a good post in this pack looks like

- One angle. The strongest claim, number or insight for this profile's audience —
  not a summary of the article.
- The angle must be genuinely different from the ones already taken (listed in
  your profile section below).
- Take a position somewhere. A post that states and never judges reads as
  compiled rather than written.
- Close with the move your profile's brief specifies.
- Soft CTA. Never "Buy now" or "Book a demo now".

# Before you save, check your own draft for

Banned words (leverage, utilize, harness, robust, seamless, comprehensive, delve,
navigate, tapestry, realm, groundbreaking, cutting-edge, game-changer), negative
parallelism ("It's not just X, it's Y"), punch triads, em dash, presumed-reaction
openers ("what most teams get wrong"), `plus` stacking capabilities, `so`
introducing a benefit, `let` for allow, `by hand` for manually, `objective` about
our own output, and `positioned as` for anything the product is or is not — say
"FitXpress is not a medical device". Abbreviations are expanded at first use;
BMI, CEO, UK, US and EU never are.

The mechanical sweep runs after you save (`scripts/post-lint.py`), so do not
spend turns re-checking what a regex will catch. Spend them on the angle.

{SHARED_MARK}
"""

    plat_block = profile_block(profile)
    li = linkedin_brief(profile)
    pmap = past_posts_map()
    excerpts = []
    for p in (pmap.get(profile) or [])[:3]:
        t = open(p, encoding="utf-8", errors="replace").read()
        b, _c, _d = extract_body(t)
        b = (b or t).strip()
        excerpts.append(f"--- {os.path.basename(p)} ---\n{b[:1200]}")
    angles = sibling_angles(slug, profile)
    angle_rows = ("\n".join(f"| `{p}` | {a or '—'} | {f or '—'} |" for p, a, f in angles)
                  if angles else "| — | first profile in this pack | — |")
    unit, blo, bhi = budget_for(profile)
    pslug = published_slug(slug)

    tail = f"""
profile: `{profile}`

## Profile config

```yaml
{plat_block or "(profile not found in social-profiles-config.md — stop and report)"}
```
{("## Your LinkedIn brief — binding, and it wins over the config block above" + chr(10) + chr(10) + li) if li else ""}

## Angles already taken in this pack — pick a different entry point

| Profile | Angle | Format |
|---|---|---|
{angle_rows}

## Past posts for voice and cadence{" (none on file for this profile — write from the brief)" if not excerpts else ""}

{chr(10).join(excerpts) if excerpts else ""}

## Save to

`workspace/social/articles/{slug}/{profile}/post.md`

```markdown
---
profile: {profile}
platform: {(plat_block and re.search(r"^platform:\s*(\S+)", plat_block, re.M).group(1)) if plat_block and re.search(r"^platform:\s*(\S+)", plat_block, re.M) else ""}
article_slug: {pslug}
product: fitxpress
format: <one of: text | text + photo | carousel | infographic | lead magnet | poll | screenshot>
status: draft
created: {date.today().isoformat()}
---

## Post: {profile} / {pslug}

**Angle:** [one or two sentences — which claim you took and why this profile]
**Claims used:** [the specific claims, in the article's wording]
**Length:** [count] / {blo}-{bhi} {unit}

---

[post body]

**CTA:** [soft]

---

### Design tip

**Article visual:** [the article asset you anchor on, from the run brief]
**Format:** [same value as the frontmatter `format`]
**Adaptation:** [one sentence — what to change for this platform and angle]
**Keep:** [one sentence — what must stay for coherence with the article]
```

Keep `**Angle:**` and `**Claims used:**` to a few lines each. They are read by the
lint, the digest and the next profile's prompt; a 400-word metadata block is
carried into every one of those.

Write the post. Do not call another agent, and do not write the manifest or the
digest — the runner does both mechanically after you finish.
"""
    return shared, tail, None


def qc_prompt(slug: str, profile: str):
    """(shared, tail, error) — the compact input for `post-quality-controller`.

    Same shape and the same reason as `drafter_prompt`: the shared half is
    byte-identical for every profile sampled in the pack, and everything the agent
    would otherwise go looking for is handed over. The old QC path opened the
    rubric, `post-drafter.md`, `proof-points.md`, the profile config, the LinkedIn
    briefs, the article and the sibling posts: 12 turns for a 250-word post.

    The lint JSON goes in verbatim. That is what lets the agent stop deriving the
    mechanical categories and spend its judgment on the three that need it."""
    import subprocess
    src, _status, err = resolve_source(slug)
    if err:
        return None, None, err
    post = os.path.join(pack_root(slug), profile, "post.md")
    if not os.path.exists(post):
        return None, None, f"no post yet at {os.path.relpath(post, PROJ)}"
    text = open(post, encoding="utf-8", errors="replace").read()
    body, cta, design = extract_body(text)
    fm, rest = split_frontmatter(text)
    meta = rest.split("\n---", 1)[0].strip()
    r = subprocess.run([sys.executable, os.path.join(HERE, "post-lint.py"),
                        slug, profile, "--json"], capture_output=True, text=True)
    lint = r.stdout.strip() or "{}"

    shared = f"""Score one social post from the `{slug}` pack against
`docs/quality-rubric.md`, then write the report. Read the rubric; read nothing else
unless you decide a specific claim has to be checked against the article, in which
case open only `{os.path.relpath(src, PROJ)}`.

The mechanical categories are already decided for you by the lint output below.
Do not re-derive them and do not restate them. Judge A (adherence to the profile
brief), C (brand and tone) and E (output quality, and above all whether the post
takes a position anywhere).

Article of record: `{os.path.relpath(src, PROJ)}`
Report goes to: `workspace/_quality/social/{date.today().isoformat()}-post-drafter-{{slug}}-{{profile}}.md`

{SHARED_MARK}
"""
    tail = f"""
slug: `{slug}`
profile: `{profile}`

## lint (scripts/post-lint.py, verbatim)

```json
{lint}
```

## post_body

<post>
{body}
</post>

**CTA:** {cta or "(none)"}

## post_meta

{meta}

### Design tip

{design or "(none)"}

## profile_brief

{linkedin_brief(profile) or profile_block(profile) or "(no brief found)"}

## sibling_angles

| Profile | Angle |
|---|---|
{chr(10).join(f"| `{p}` | {a or '—'} |" for p, a, _f in sibling_angles(slug, profile)) or "| — | none yet |"}
"""
    return shared, tail, None


# ---------------------------------------------------------------------------
# qc plan
# ---------------------------------------------------------------------------

def qc_plan(slug: str):
    """Which profiles get an LLM quality pass this pack, and why.

    CLAUDE.md §14 defines QC as the input to `agent-improver`: it exists to find
    systematic problems in an agent's prompt, not to gate each artifact. The gate
    is Vadim approving the digest. On the measured pack QC ran nine times on Opus
    for 7.1M tokens and $36 to produce nine reports of 16-19/20, and the three
    defects it actually found are all now caught by `post-lint.py` for free.

    So: sample, but never sample blindly.
      * the first profile in digest order always runs — it sets the angle map the
        rest of the pack diverges from, and a bad angle there propagates;
      * every profile whose lint gate fails runs, whatever the sample says;
      * one rotating profile runs, chosen from the slug so the choice is stable
        across resumes and spreads coverage over packs rather than always landing
        on the same account.
    Everything else is covered by lint plus `post-brand-checker`."""
    import subprocess
    order = digest_order([p for p, _, _ in active_profiles()])
    if not order:
        return {"qc": [], "reason": {}}
    picked, why = [], {}
    picked.append(order[0])
    why[order[0]] = "first profile in the pack, sets the angle map"

    root = pack_root(slug)
    for pid in order:
        post = os.path.join(root, pid, "post.md")
        if not os.path.exists(post):
            continue
        r = subprocess.run([sys.executable, os.path.join(HERE, "post-lint.py"),
                            slug, pid, "--gate", "--json"],
                           capture_output=True, text=True)
        if r.returncode == 1 and pid not in picked:
            picked.append(pid)
            why[pid] = "lint reported hard fails"

    # Two rotating picks, not one, so a clean pack still gets three LLM passes out
    # of nine: the angle-setter plus one company and one personal account. Derived
    # from the slug, so a resumed pack samples the same profiles it started with.
    last = last_qc_seen()
    for group in (COMPANY_ORDER, [p for p in order if p not in COMPANY_ORDER]):
        rest = [p for p in order if p in group and p not in picked]
        if not rest:
            continue
        # Least-recently-inspected first, ties broken by config order. Coverage
        # beats randomness here: QC feeds `agent-improver`, which wants evidence
        # from every profile over time, and a hash-based pick left `linkedin-nick`
        # unsampled across all nine packs on disk while `linkedin-vadim` came up
        # four times.
        pick = min(rest, key=lambda p: (last.get(p, ""), rest.index(p)))
        picked.append(pick)
        why[pick] = ("never inspected" if pick not in last
                     else f"least recently inspected (last {last[pick]})")
    return {"qc": [p for p in order if p in picked],
            "skip": [p for p in order if p not in picked],
            "reason": why}


# ---------------------------------------------------------------------------
# manifest / digest / report
# ---------------------------------------------------------------------------

def build_manifest(slug: str):
    """The canonical schema is owned by `social-publisher`. This builds exactly
    that shape from the files, which is the point: on 2026-08-21 three agents each
    wrote a different shape and the file's form depended on which touched it last,
    ending with a manifest listing 3 profiles while 9 posts sat on disk."""
    import subprocess
    src, status, err = resolve_source(slug)
    if err:
        return None, err
    root = pack_root(slug)
    text = open(src, encoding="utf-8", errors="replace").read()
    fm, body = split_frontmatter(text)
    h1 = ""
    m = re.search(r"^#\s+(.+)$", body, re.M)
    if m:
        h1 = m.group(1).strip()
    scores = qc_reports(slug)
    profiles, ready_all = [], True
    for pid, plat, handle in active_profiles():
        post = os.path.join(root, pid, "post.md")
        entry = {"profile_id": pid, "platform": plat, "handle": handle,
                 "post_file": f"{pid}/post.md"}
        if not os.path.exists(post):
            entry["status"] = "draft"
            entry["format"] = ""
            ready_all = False
            profiles.append(entry)
            continue
        ptext = open(post, encoding="utf-8", errors="replace").read()
        pfm, _ = split_frontmatter(ptext)
        pbody, _cta, _d = extract_body(ptext)
        entry["format"] = pfm.get("format", "")
        r = subprocess.run([sys.executable, os.path.join(HERE, "post-lint.py"),
                            slug, pid, "--gate", "--json"],
                           capture_output=True, text=True)
        if not pbody:
            entry["status"] = "draft"
            ready_all = False
        elif r.returncode == 1:
            entry["status"] = "blocked"
            ready_all = False
        else:
            entry["status"] = "ready"
        # exactly one length field, in the unit the profile's brief uses
        if budget_for(pid)[0] == "words":
            entry["word_count_body"] = len(re.findall(r"\b[\w'-]+\b", pbody))
        else:
            entry["character_count_body"] = len(pbody)
        if pid in scores:
            entry["qc_score"] = scores[pid]
        profiles.append(entry)

    man = {
        "article": {
            "slug": published_slug(slug),
            "title": h1,
            "product": fm.get("product", "fitxpress"),
            "source_file": os.path.relpath(src, PROJ),
            "source_status": status or "",
            "published_url": published_url(slug),
            "date": date.today().isoformat(),
        },
        "profiles": profiles,
        "profiles_skipped": [{"profile_id": p, "reason": "posts_per_week: 0"}
                             for p in skipped_profiles()],
        "ready_for_review": bool(profiles) and ready_all,
    }
    return man, None


def build_digest(slug: str):
    src, _status, err = resolve_source(slug)
    if err:
        return None, err
    root = pack_root(slug)
    order = digest_order([p for p, _, _ in active_profiles()])
    parts = []
    n = 0
    for pid in order:
        post = os.path.join(root, pid, "post.md")
        if not os.path.exists(post):
            continue
        text = open(post, encoding="utf-8", errors="replace").read()
        body, cta, design = extract_body(text)
        if not body:
            continue
        n += 1
        block = [f"## {pid}", "", body, ""]
        if cta:
            block += [f"**CTA:** {cta}", ""]
        if design:
            quoted = "\n".join("> " + l if l.strip() else ">" for l in design.splitlines())
            block += ["> **Design tip**", quoted, ""]
        parts.append("\n".join(block))
    out = (f"# Review digest — {slug}\n\n"
           f"Article: `{os.path.relpath(src, PROJ)}`\n"
           f"Date: {date.today().isoformat()}\n"
           f"Profiles: {n}\n\n---\n\n" + "\n---\n\n".join(parts) + "\n\n---\n")
    return out, None


def build_report(slug: str):
    man, err = build_manifest(slug)
    if err:
        return None, err
    root = pack_root(slug)
    rows, issues = [], []
    for e in man["profiles"]:
        length = e.get("word_count_body") or e.get("character_count_body") or "—"
        mark = {"ready": "✅", "blocked": "❌", "draft": "…"}.get(e["status"], "?")
        rows.append(f"| {e['profile_id']} | {length} | {e.get('format') or '—'} | "
                    f"{e.get('qc_score') or '—'} | {mark} |")
        if e["status"] != "ready":
            issues.append(f"- `{e['profile_id']}` — {e['status']}")
    ready = sum(1 for e in man["profiles"] if e["status"] == "ready")
    out = f"""# Social Publish Report — {man['article']['slug']}

## Profiles: {ready}/{len(man['profiles'])}

| Profile | Length | Format | QC | Status |
|---|---|---|---|---|
{chr(10).join(rows)}

## Issues: {len(issues)}
{chr(10).join(issues) if issues else "- none"}

## Ready for review: {"YES" if man["ready_for_review"] else "NO"}

Generated by `scripts/social_pack.py report {slug}` from the files on disk.
Next: Vadim reviews the digest and approves, then `visual-brief` per approved post.
"""
    return out, None


# ---------------------------------------------------------------------------
# cli
# ---------------------------------------------------------------------------

def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = p.add_subparsers(dest="cmd", required=True)
    for name in ("profiles", "source", "brief", "qc-plan", "manifest", "digest",
                 "report", "scores"):
        s = sub.add_parser(name)
        s.add_argument("slug", nargs="?" if name in ("profiles", "scores") else None)
        if name in ("manifest", "digest", "report"):
            s.add_argument("--write", action="store_true")
        if name == "brief":
            s.add_argument("--force", action="store_true")
    for name in ("prompt", "qc-prompt"):
        sp = sub.add_parser(name)
        sp.add_argument("slug")
        sp.add_argument("profile", nargs="?")
        sp.add_argument("--check-prefix", action="store_true")
    a = p.parse_args(argv)

    if a.cmd == "profiles":
        act = active_profiles()
        if a.slug:
            done, missing = pack_state(a.slug)
            print(json.dumps({"active": [x[0] for x in act], "done": done,
                              "missing": missing,
                              "skipped": skipped_profiles()}, indent=2))
        else:
            for pid, plat, handle in act:
                print(f"{pid}\t{plat}\t{handle}")
        return 0

    if a.cmd == "source":
        src, status, err = resolve_source(a.slug)
        if err:
            print(f"✗ {err}", file=sys.stderr)
            return 2
        text = open(src, encoding="utf-8", errors="replace").read()
        print(json.dumps({"path": os.path.relpath(src, PROJ), "status": status,
                          "published_slug": published_slug(a.slug),
                          "published_url": published_url(a.slug),
                          "words": len(text.split()),
                          "prose_lines": prose_lines(text)}, indent=2))
        return 0

    if a.cmd == "brief":
        path, note = build_brief(a.slug, a.force)
        if not path:
            print(f"✗ {note}", file=sys.stderr)
            return 2
        print(f"{'✓' if not note else 'ℹ'} {os.path.relpath(path, PROJ)}"
              + (f" — {note}" if note else ""))
        return 0

    if a.cmd in ("prompt", "qc-prompt"):
        build = drafter_prompt if a.cmd == "prompt" else qc_prompt
        if a.check_prefix:
            hashes = {}
            for pid, _pl, _h in active_profiles():
                shared, _tail, err = build(a.slug, pid)
                if err:
                    print(f"· skipped {pid}: {err}")
                    continue
                hashes[pid] = hashlib.sha256(shared.encode()).hexdigest()[:16]
            if not hashes:
                print("✗ nothing to compare", file=sys.stderr)
                return 2
            uniq = set(hashes.values())
            for pid, h in hashes.items():
                print(f"{h}  {pid}")
            print(f"\n{'✓ one shared prefix' if len(uniq) == 1 else '✗ ' + str(len(uniq)) + ' DIFFERENT prefixes — caching will not be shared'}"
                  f"  ({len(shared)} chars, ~{len(shared)//4} tokens)")
            return 0 if len(uniq) == 1 else 1
        if not a.profile:
            print("✗ profile required (or use --check-prefix)", file=sys.stderr)
            return 2
        shared, tail, err = build(a.slug, a.profile)
        if err:
            print(f"✗ {err}", file=sys.stderr)
            return 2
        sys.stdout.write(shared + tail)
        return 0

    if a.cmd == "qc-plan":
        print(json.dumps(qc_plan(a.slug), indent=2))
        return 0

    if a.cmd == "manifest":
        man, err = build_manifest(a.slug)
        if err:
            print(f"✗ {err}", file=sys.stderr)
            return 2
        if a.write:
            path = os.path.join(pack_root(a.slug), "manifest.json")
            with open(path, "w", encoding="utf-8") as f:
                json.dump(man, f, indent=2)
                f.write("\n")
            print(f"✓ {os.path.relpath(path, PROJ)} — "
                  f"ready_for_review: {man['ready_for_review']}")
        else:
            print(json.dumps(man, indent=2))
        return 0

    if a.cmd in ("digest", "report"):
        out, err = (build_digest if a.cmd == "digest" else build_report)(a.slug)
        if err:
            print(f"✗ {err}", file=sys.stderr)
            return 2
        if a.write:
            name = "review-digest.md" if a.cmd == "digest" else "publish-report.md"
            path = os.path.join(pack_root(a.slug), name)
            with open(path, "w", encoding="utf-8") as f:
                f.write(out)
            print(f"✓ {os.path.relpath(path, PROJ)}")
        else:
            sys.stdout.write(out)
        return 0

    if a.cmd == "scores":
        packs = [a.slug] if a.slug else sorted(
            os.path.basename(d) for d in glob.glob(
                os.path.join(PROJ, "workspace", "social", "articles", "*"))
            if os.path.isdir(d))
        for slug in packs:
            sc = qc_reports(slug)
            meta = {}
            mp = os.path.join(pack_root(slug), "_pack.json")
            if os.path.exists(mp):
                try:
                    meta = json.load(open(mp))
                except ValueError:
                    meta = {}
            if not sc:
                continue
            vals = [int(v.split("/")[0]) for v in sc.values()]
            print(f"\n{slug}  (drafter: {meta.get('drafter_model', '?')}, "
                  f"qc: {meta.get('qc_policy', '?')})  "
                  f"mean {sum(vals)/len(vals):.1f}/20  n={len(vals)}")
            for pid in digest_order(list(sc)):
                print(f"  {sc[pid]:>6}  {pid}")
        return 0

    return 0


if __name__ == "__main__":
    sys.exit(main())
