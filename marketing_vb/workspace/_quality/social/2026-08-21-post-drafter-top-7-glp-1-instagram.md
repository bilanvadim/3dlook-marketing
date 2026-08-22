---
qc_date: 2026-08-21
agent: post-drafter
artifact: workspace/social/articles/top-7-remote-body-composition-tools-glp-1-clinics/instagram-company/post.md
track: social
artifact_type: post
total_score: 19/20
status: excellent
coordinator_review: "agreement: ✅ agree | top_issue: em-dash in Angle metadata (fixed post-QC)"
---

# QC Report — post-drafter — 2026-08-21

**Artifact:** `workspace/social/articles/top-7-remote-body-composition-tools-glp-1-clinics/instagram-company/post.md`
**Total: 19/20** — excellent

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 5 | 5 |
| B | Factual accuracy | 5 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 4 | 4 |

## What was wrong (specific)

### A. Adherence — 5/5
- All required inputs honored: IG config block applied (tone, 600-1000 char caption, hook before the "more" cut), OG image direction from publish-package §4 adapted (not reinvented) in the Design tip, product bias 100% FitXpress respected.
- Angle is a single strong claim from the article, not a summary — matches "pick one angle" instruction.
- `past-posts/instagram-company/` is empty, so step 4 (read 5 past posts) could not be performed — correctly continued rather than STOP, per prompt. Not an artifact fault.

### B. Factual accuracy — 5/5
- All numbers trace to `proof-points.md`: "80+ body measurements" (line 47), "under 45 seconds" (line 40), repeatability "less than a centimetre" = `< 1 cm` (line 30), "7 categories" from the article.
- Correct product (fitxpress), correct segment (GLP-1 telehealth).
- Claims discipline clean: line 24 "It doesn't replace a scale, a DXA appointment, or a clinician" states limits honestly; no diagnosis / decisioning / medical-device claim; accuracy not reduced to a single universal number (about-me hard rule respected). No anti-positioning ("most accurate") lead. No invented clients.

### C. Brand & tone — 2/3
- Line 13 (Angle metadata): em-dash used in an explanatory construction — "the article's opening claim — two people can lose the same weight...". Hard rule #3 / CLAUDE.md §6 ban em-dash; brand-checker check 3 would flag it. Note: the published post body (lines 18-26) is em-dash-free and clean.
- Minor: line 22 renders repeatability as "less than a centimetre" (British spelling) rather than the locked `< 1 cm` convention from about-me. Acceptable in casual IG prose, flagged for awareness, not double-counted.
- No banned words. Single emoji (📲), within limits. Human/visual IG tone matches config. Could not run the Social-track override (compare vs 3+ past posts) — folder empty.

### D. Format & structure — 3/3
- Frontmatter complete: `profile`, `platform`, `article_slug`, `product: fitxpress`, `status`, `created` all present.
- File in correct path (`.../instagram-company/post.md`).
- All template sections present (Source article, Angle, Goal, body, CTA, Design tip with Article visual / Format / Adaptation / Keep). Caption ~900 chars (in 600-1000 range); hook first line ~100 chars (under 125). Minor: Angle field runs two sentences where template asks for one — not deducted.

### E. Output quality — 4/4
- Ready to publish as-is. Strong stoppable hook (line 18) that lands the exact GLP-1 audience hook from `audience.md` (make progress visible → repeat check-ins → retention; repeatability so small changes aren't lost in noise).
- Unique human angle, not generic; honest-limits paragraph adds credibility without diluting the message. Design tip is faithful to the OG direction and gives the designer a clear carousel adaptation.

## Top 3 issues (приоритет для improver)

1. Em-dash in the Angle metadata line (line 13) — banned construction slips through in the meta field even though the post body is clean; brand-checker should also sweep meta fields.
2. Repeatability written as "less than a centimetre" instead of the locked `< 1 cm` convention (about-me) — minor, but a house convention drift.
3. Angle field is two sentences vs template's one — cosmetic.

## Coordinator review

agreement: ✅ agree
top_issue: em-dash in the Angle metadata line — fixed directly (replaced with colon) after this QC ran; body text was already clean
