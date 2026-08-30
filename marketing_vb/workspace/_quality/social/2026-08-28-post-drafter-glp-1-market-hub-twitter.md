---
qc_date: 2026-08-28
agent: post-drafter
artifact: workspace/social/articles/glp-1-market-hub/twitter-company/post.md
track: social
artifact_type: post
total_score: 16/20
status: good
coordinator_review: |
  agreement: ✅ agree
  top_issue: Findings 1 and 2 were real and both fixed; finding 3 was my own instruction, not an agent miss.
  notes: |
    Fixed on 2026-08-28 before the pack moved on:
      1. Design tip no longer claims the article assets avoid photography — cover-3.webp is a photo,
         only the two banner_* files are abstract data cards. Corrected in the post and written into
         the pack run brief so the remaining seven drafts cannot repeat it.
      2. article_slug corrected glp-1-market-hub -> glp-1-market in both posts and in manifest.article.slug.
         The folder keeps the -hub suffix (it mirrors the SEO working dir); the slug field must match
         publish-package frontmatter and the live URL. Also written into the run brief.
      3. Not an agent failure. publish-package §4 genuinely has no OG direction, and I instructed the
         drafter to anchor on the live page assets instead, because §4 predates the refresh and the live
         page now ships three 2026 visuals. The agent followed the coordinator brief. Fair catch that it
         did not say the required input was missing.
    Carried to Vadim rather than fixed here:
      - The tweet attaches a banner crop while the reply link renders its own preview card from the
         article URL, so two different images appear. Real, and a publishing-time decision.
    Agreed with the B-section judgement call: ~25M and $200B are article-sourced third-party market
    figures logged in publish-package §7, not product claims, so the proof-points cap correctly did not
    apply. Same reading I used when briefing the pack.
    Two blocked checks are infrastructure gaps, not artifact defects, and both recur across reports:
    past-posts/twitter-company/ has never been seeded, and quality-controller has no Bash so
    detect-ai-tells.py cannot run. Neither is post-drafter's fault; raising both with Vadim.
---

# QC Report — post-drafter — 2026-08-28

**Artifact:** `workspace/social/articles/glp-1-market-hub/twitter-company/post.md`
**Total: 16/20** — good

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 4 | 5 |
| B | Factual accuracy | 4 | 5 |
| C | Brand & tone | 3 | 3 |
| D | Format & structure | 2 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence — 4/5
- Correct source used: the artifact cites `published-live-2026-08-28.md` (line 15) and the live URL (line 16), not a superseded `draft-v*`. Profile config honoured: single tweet, 240-260 band, no hashtags, no emoji, no bullet lists, punchy/data-first tone.
- **Design-tip sourcing done superficially (the one shallow step).** Step 3 requires the design tip to start from `publish-package.md` §4 "Suggested OG image direction". §4 of this article contains **no OG direction at all** — it says "no new OG image brief was commissioned" and raises two open flags for Vadim (is the existing hero still right for the 2026 market-led framing; H1 unchanged). The artifact silently substituted the live page's in-body assets and never states that the required input was missing, so §4's open flag disappears between stages instead of being carried forward.
- Related mislabel: line 34 presents `banner_1-3.webp` (an in-body infographic) as the "**Article visual**". The article's actual OG/hero asset is `cover-3.webp` (live frontmatter `cover_image`). The consequence is unflagged: the tweet's attached photo and the link-preview card generated from the article URL in the reply will be two different images.
- `brand-assets/past-posts/twitter-company/` does not exist (whole folder absent, not just empty). Per the prompt's explicit fallback this is not a violation, but the artifact does not flag the missing corpus either.

### B. Factual accuracy — 4/5
- Line 24 "J.P. Morgan projects ~25M US users by 2030" matches the live article verbatim in substance (line 59: "Projected US adoption | Approximately 25 million people ... by 2030", J.P. Morgan link). Attribution named, geography correct, year correct.
- **Not applying the proof-points cap, deliberately.** ~25M and $200B are absent from `proof-points.md`, but they are third-party market figures carried from the live article with citations and logged in `publish-package.md` §7 Claims Audit. `post-drafter` hard rule #1 permits "what is in the article or product-info/". Applying the cap here would penalise the correct behaviour; the cap targets unsourced product claims, and this post makes zero product claims.
- **Line 37 is wrong on a checkable detail:** "the abstract data-card treatment used across all three article assets, with **no patient photography**". `cover-3.webp` alt text (live file line 38) is "A woman sits at a desk with a laptop; her body stats are shown over three dates" — that is person photography. The claim holds for `banner_1-3.webp` and `banner_2-2.webp` only, not "all three".
- **Line 24 hardens a deliberately hedged claim:** "Check-ins **often run on** a scale number". The article says "may rely on" (line 105) and "Progress photos **may** also vary in lighting" (line 107). That hedging is not accidental — Review 2 softened claims across this article. Twitter compression makes "often" defensible, but it is a directional strengthening of the source.
- Credit where due: the two exclusion reasons in the Adaptation line are precise and correct — $200B does cover the broader incretin category (line 58), and the KFF figures do apply only to surveyed firms with 5,000+ workers (lines 60-61, 65). Design tokens correct per `DESIGN.md`: `#143DFF` (not `#2962FF`), `#050F40`, Satoshi (not Inter).
- No invented customers, no invented product capability, no anti-positioning claim, correct product (`fitxpress`).

### C. Brand & tone — 3/3
- Grep over the whole file: **zero em dashes**, zero banned words (leverage/utilize/harness/robust/seamless/comprehensive/delve/tapestry/realm/unlock/unleash/game-changing/cutting-edge), no `positioned as`, no `objective` about our output. No "not just X, it's Y", no triple parallelism, no hashtags, no emoji.
- Voice matches `about-me.md`: "a photo shot in whatever lighting" is the exemplar cadence ("Users stand in odd lighting, wear sweaters over t-shirts"), and the closing line is a verdict, so the post takes a position rather than only stating (rule 6c).
- `audience.md` segment 1 "Don't" list respected: no diagnostic claim, no DEXA/scale-replacement claim, no eligibility decisioning, no bleed into UK pharmacy compliance.
- Watch item, not scored down: "Same capture method every time, or records aren't comparable" sits near the banned corrective-contrast pattern. It reads as an operational condition plus consequence, not "X, not Y", so it passes.
- Social override note: the 3-post style comparison against `past-posts/twitter-company/` could not be run — the folder does not exist. Detector `detect-ai-tells.py` not run (this QC pass has no Bash).

### D. Format & structure — 2/3
- **`article_slug: glp-1-market-hub` (line 5) is the workspace folder name, not the slug from `publish-package.md` frontmatter, which is `glp-1-market`** (the live article's `slug` is also `glp-1-market`). The template specifies "{slug from publish-package frontmatter}". The same field getting this right was called out as a point of adherence in the 2026-07-05 twitter QC. Consequence: the artifact and `manifest.json` are keyed on a slug that does not match the published URL, so anything joining social artifacts to the article by `article_slug` will miss.
- Minor: `Angle` (line 17) is two sentences where the template asks for one.
- Everything else clean: all 6 required frontmatter fields present including `product: fitxpress`, plus useful extras (`handle`, `article_url`, `format`). Correct path. All 4 design-tip fields present. Body verified at **251 chars** (self-report accurate), inside 240-260 and 29 under the 280 limit. `manifest.json` follows the canonical schema — `profile_id`/`platform`/`handle`/`post_file`/`status`/`format`, exactly one length field (`character_count_body`, the correct unit for twitter), only its own entry, `profiles_skipped: []`, `ready_for_review: false`.

### E. Output quality — 3/4
- Post copy is ready as-is. One angle, the article's real thesis (volume growing faster than documentation), no summary, no product pitch, and correct mechanics — link in the reply keeps the body under 260 so nothing truncates.
- **Design tip is a brief, not a tip.** The prompt asks for 3 lines; `Adaptation` (line 36) is a ~60-word sentence carrying two parenthetical justifications, and `Keep` (line 37) is another long one. Useful content, wrong container — needs a trim plus the "all three assets" correction.
- The angle does not use the segment-1 hook from `audience.md` (visible progress → repeat check-ins → adherence → retention). Legitimate, since the hub's thesis is documentation consistency, but it means the tweet lands on a problem with no forward pull for the reader.
- Estimate: 5-10 minutes of Vadim's editing, all of it in the design tip, none in the copy.

## Top 3 issues (приоритет для improver)

1. Line 37: "no patient photography ... across all three article assets" is false for `cover-3.webp` (a woman at a desk, per live alt text) — fix the claim, and name `cover-3.webp` as the actual OG/hero so the mismatch between the tweet photo and the reply link-preview is a decision, not an accident.
2. Line 5: `article_slug` should be `glp-1-market` (publish-package / live frontmatter), not the folder name `glp-1-market-hub`; `manifest.json` inherits the same wrong key.
3. `publish-package.md` §4 shipped **no OG image direction** and two open flags for Vadim; the design tip substituted live in-body assets without saying so. The prompt's "quote the OG direction" step needs an explicit fallback that requires naming the missing input, otherwise an unresolved dependency disappears between stages.

## Coordinator review

