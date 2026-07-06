---
qc_date: 2026-07-05
agent: post-drafter
artifact: workspace/social/articles/2026-06-16-clinical-trials-obesity-metabolic-hybrid-dct/facebook-company/post.md
track: social
artifact_type: post
total_score: 19/20
status: excellent
coordinator_review: pending
---

# QC Report — post-drafter — 2026-07-05

**Artifact:** `workspace/social/articles/2026-06-16-clinical-trials-obesity-metabolic-hybrid-dct/facebook-company/post.md`
**Total: 19/20** — Excellent

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 5 | 5 |
| B | Factual accuracy | 5 | 5 |
| C | Brand & tone | 3 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence — 5/5
No issues. `product: fitxpress` correctly carried from `publish-package.md` frontmatter. `article_slug` uses the publish-package's slug (`clinical-trial-anthropometric-measurement-software-obesity-trials`) verbatim, per template spec. `brand-assets/past-posts/facebook-company/` is empty (0 files); per the prompt's explicit fallback ("If the folder is empty, continue without them, do not STOP") this is correctly not treated as a blocker. `facebook-company` profile block was read and applied: tone ("accessible, community-oriented, explain without jargon, slightly warmer") drove a plain-language opener, and `avoid` ("dry B2B corporate tone, technical API details, pricing") was respected — no pricing, no API/integration detail. Section 4 OG image direction was read and quoted accurately in the design tip (multi-site dot motif, guided-scan smartphone, structured-record/timestamp icon, dark teal-blue palette). Manifest updated correctly with the `facebook-company` entry appended to the existing partial-run list.

### B. Factual accuracy — 5/5
No issues. "FitXpress returns 80+ measurements and body composition estimates in about 45 seconds" matches `proof-points.md` (80+ measurements; under 45 seconds) and the article body verbatim ("80+ body measurements, BMI outputs, and body composition estimates, with results processed in roughly 45 seconds," publish-package.md line 450). "A study that can run a year or more" reflects the article's "study window can run twelve months or longer" (line 439). "It doesn't replace the reference methods a protocol requires" correctly honors the source article's `compliance_guardrails` (`no_dexa_alternative`, `no_endpoint_validation_claim`) despite `compliance_sensitive: true` — a compliance-aware paraphrase, not a hallucinated hedge. No invented clients, no comparison claims, no numbers absent from `proof-points.md`.

### C. Brand & tone — 3/3
No issues. No banned words (leverage/utilize/harness/robust/seamless/comprehensive/delve/navigate/tapestry/realm/unlock/unleash/game-changing/cutting-edge). No em-dash or "not just X, it's Y" construction in the post copy itself (the only em-dash in the file is in the internal `**Angle:**` metadata line, not published caption text). No triple-parallelism filler pattern. Tone matches CLAUDE.md §6 (outcome-focused, no clickbait) and the profile's "slightly warmer" instruction (the closing question).

### D. Format & structure — 3/3
No issues. Frontmatter complete (`profile`, `platform`, `article_slug`, `product`, `status`, `created`). File saved at the exact expected path. Post body is 1,123 characters — within the profile's 800-1200 char spec. First paragraph carries the full meaning on its own, per the Facebook rule ("many readers don't tap 'more'"). CTA ("Read the full article (link in comments)") matches the profile's specified soft CTA exactly. Design tip has all 4 required fields (Article visual / Format / Adaptation / Keep); `text + photo` is a correct format choice given `poll` is explicitly disallowed on Facebook.

### E. Output quality — 3/4
- The compliance-hedge sentence — "It doesn't replace the reference methods a protocol requires." — introduces trial-ops jargon ("reference methods," "protocol requires") into a post whose profile spec explicitly calls for "explain without jargon" and a general, non-technical Facebook audience. It's necessary to stay inside the article's compliance guardrails, but it reads as inserted boilerplate rather than the warm, accessible voice the rest of the post uses — the same pattern flagged in the sibling Instagram QC for this article (2026-07-05-post-drafter-clinical-trials-instagram.md). A 5-minute rephrase (e.g., "It's not a replacement for the standard checks a trial requires") would keep the guardrail intact in plainer language.
- Otherwise strong: single clear angle (cross-site measurement consistency, not a full article summary), a genuine hook, a real engagement question tied to the stated `Goal: engagement`, and a design tip that adapts the OG banner into a Facebook-appropriate crop rather than reusing it as-is.

## Top 3 issues (приоритет для improver)

1. Minor: the compliance-hedge sentence ("reference methods a protocol requires") uses trial-ops jargon that cuts against the facebook-company profile's explicit "explain without jargon" instruction — a light rephrase, not a rewrite.
2. None (Adherence, Factual accuracy, Brand/tone, Format all clean).
3. None.

## Coordinator review

(заполняется Claude в чате после автозапуска QC)
