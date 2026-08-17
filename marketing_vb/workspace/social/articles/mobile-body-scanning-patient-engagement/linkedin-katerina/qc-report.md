---
qc_date: 2026-08-17
agent: post-drafter
artifact: workspace/social/articles/mobile-body-scanning-patient-engagement/linkedin-katerina/post.md
track: social
artifact_type: post
total_score: 19/20
status: excellent
coordinator_review: pending
---

# QC Report — post-drafter — 2026-08-17

**Artifact:** `workspace/social/articles/mobile-body-scanning-patient-engagement/linkedin-katerina/post.md`
**Total: 19/20** — excellent

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 4 | 5 |
| B | Factual accuracy | 5 | 5 |
| C | Brand & tone | 3 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 4 | 4 |

## What was wrong (specific)

### A. Adherence — 4/5
- Brief followed cleanly: founder voice, one strategic observation (buying question shifting from model performance to scope + data residency), why the market is changing, what enterprise buyers now expect, UK lens, invitation-to-article close. Word count 229 sits inside the 180-250 band. No emoji, no hashtags — house rules respected.
- UK lens handled correctly: references "UK remote care teams," "enterprise buyers here," "UK hosting available on request" without inventing MHRA/CQC/NHS specifics the source article does not raise (brief allows those "where the article supports it" — it does not).
- Deduction: frontmatter line 21 `Claims used: C1, C9 (UK hosting), C11` references a claim-ID scheme that does not exist. The source article tracks claims as `FX-TWOPHOTOS`, `FX-NOTDEVICE`, etc. (frontmatter lines 35-45); there is no C-numbered registry to verify against. The underlying claims are all accurate, but the tag is unverifiable metadata.

### B. Factual accuracy — 5/5
- Hosting claim (line 34): "Standard hosting runs in the US, with UK hosting available on request" matches article line 208 ("AWS in the United States, with EU or UK hosting available on request") and CLAUDE.md §12.
- "not positioned as a medical device... evaluated on data-privacy frameworks rather than medical-device ones" (line 34) matches article line 210 and about-me.md claims discipline exactly.
- "30, 60, and 90-day cycles" (line 30) matches article line 127.
- No invented numbers, no invented customers. Anti-positioning respected — the post deliberately pivots away from accuracy as the selling point ("It used to be about accuracy. Now it is about what happens between appointments"), which is on-strategy per CLAUDE.md §3.
- Claims discipline (about-me.md hard rules) fully honoured: "supports clinician review; the care team interprets it and makes the decision" — no diagnosis / decisioning / clinician-replacement claim; no accuracy figure reduced to one number; no repeatability number misstated.

### C. Brand & tone — 3/3
- No banned words (checked against messaging list: leverage/utilize/harness/robust/seamless/comprehensive/delve/navigate/tapestry/realm — none present).
- No em-dash rhetoric, no "not just X, it's Y."
- Register matches the katerina brief (calm, executive, experienced) and about-me.md voice fingerprint (declarative, buyer-framed, honest-about-limits).
- Watch item (not a deduction): line 32 "What does this layer decide, what does it not decide, and where does the data sit" is a three-clause parallel question. It reads as a natural founder cadence and maps to real buyer scope questions, so it does not trip the adjective-triad ban — but it is the closest thing to a triple-parallel construction in the post.

### D. Format & structure — 3/3
- Frontmatter complete: `product: fitxpress`, `status: draft`, `created`, `profile`, `platform`, `article_slug` all present.
- File at correct path `workspace/social/articles/{slug}/{profile}/post.md`.
- Template structure followed (Angle / Goal / post / CTA / Design tip with Article visual / Format / Adaptation / Keep).
- Design tip handled the missing OG block gracefully and transparently (line 48: "No OG block exists in draft-v5-revision1.md. Derived direction..."), and its token guidance is correct (navy `#050F40`, electric blue `#143DFF`, Satoshi — matches DESIGN.md).

### E. Output quality — 4/4
- Hook lands in the first two lines, fully visible before the LinkedIn "see more" cut (line 28).
- Genuine CEO-level angle: the buying-conversation shift from model performance to scope + data residency is a real strategic observation, not a rephrased article summary, and aligns with the §3 AI-risk positioning.
- Reads human, not AI-generated. Publishable as-is.

## Top 3 issues (приоритет для improver)

1. Frontmatter `Claims used: C1, C9, C11` uses a non-existent claim-ID scheme — either map to the article's `FX-*` IDs or drop the field (cosmetic, but it looks like fabricated traceability).
2. Line 32 triple-clause question is a borderline parallel construction — safe here, but a pattern to watch in founder-voice posts.
3. None material — post is approval-ready.

## Coordinator review

(заполняется Claude в чате после автозапуска QC)
