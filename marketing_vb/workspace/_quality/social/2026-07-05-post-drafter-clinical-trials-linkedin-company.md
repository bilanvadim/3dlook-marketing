---
qc_date: 2026-07-05
agent: post-drafter
artifact: workspace/social/articles/2026-06-16-clinical-trials-obesity-metabolic-hybrid-dct/linkedin-company/post.md
track: social
artifact_type: post
total_score: 19/20
status: excellent
coordinator_review: pending
---

# QC Report — post-drafter — 2026-07-05

**Artifact:** `workspace/social/articles/2026-06-16-clinical-trials-obesity-metabolic-hybrid-dct/linkedin-company/post.md`
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
No issues. `product: fitxpress` correctly carried from `publish-package.md` frontmatter. `article_slug` uses the publish-package's slug (`clinical-trial-anthropometric-measurement-software-obesity-trials`) verbatim, per the template spec. Section 4 ("OG Image Brief") of `publish-package.md` was read and quoted accurately in the design tip — the multi-site motif, guided-scan-phone, and timestamp/clipboard/structured-record icon all match the source's "Visual concept" bullets word-for-word. The `linkedin-company` profile block was read and applied correctly: tone ("expert, data-driven, company voice — not personal, outcome-focused not feature-focused") drove a fully third-person post about FitXpress with zero founder-voice framing, and `avoid` ("founder personal voice, opinions without data, generic AI buzzwords") is respected throughout. `brand-assets/past-posts/linkedin-company/` is non-empty (15 files); the post does not mimic their emoji/arrow-bullet formatting, but those posts predate the 2026-07-01 CLAUDE.md change that removed hashtags/emoji-flood guidance project-wide, so a prose-only, no-emoji approach here is the correct current standard rather than a skipped step. The angle statement correctly identifies the single strongest thread from the article (operational proof-point stack scoped against what FitXpress doesn't do) rather than summarizing the whole piece.

### B. Factual accuracy — 5/5
No issues. "80+ body measurements and body composition estimates in about 45 seconds" (line 22) matches `proof-points.md` (80+ measurements; under 45 seconds) and the article body verbatim ("80+ body measurements, BMI outputs, and body composition estimates, with results processed in roughly 45 seconds," draft-final.md). "A study window that can run 12 months or longer" (line 20) reflects the article's own framing ("the study window can run twelve months or longer," draft-final.md). The scope paragraph (line 24) — DEXA/trained-anthropometrist measurement stays in place; endpoint validation and eligibility determinations stay with sponsor/CRO/investigator — correctly honors the source article's `compliance_guardrails` (`no_dexa_alternative`, `no_endpoint_validation_claim`, `no_eligibility_determination`) despite `compliance_sensitive: true` on the source. No customer name is invoked (the article's `customer_reference_status: none_yet_thought_leadership_entry` is respected), no accuracy/superiority percentage is claimed (avoids the anti-positioning trap on a topic where it would have been easy to reach for "96-97% accuracy"), and no comparison numbers are invented.

### C. Brand & tone — 3/3
No issues. No banned words (leverage/utilize/harness/robust/seamless/comprehensive/delve/navigate/tapestry/realm/unlock/unleash/game-changing/cutting-edge) anywhere in the post body. No em-dash used anywhere in the published copy, and no "it's not just X, it's Y" construction. No triple-parallelism filler. Tone matches CLAUDE.md §6 and the profile's "expert, data-driven... outcome-focused" instruction — e.g., line 26 frames the value strictly in operational terms (fewer measurement-only visits, less coordinator time, audit traceability) rather than product features.

### D. Format & structure — 3/3
No issues. Frontmatter complete (`profile`, `platform`, `article_slug`, `product`, `status`, `created`). File saved at the exact expected path. Post body (lines 18-28) is ~1,772 characters — within the profile's 1200-1800 char spec, though close to the ceiling (see E). CTA ("Read the full article") matches one of the two options specified in the profile config exactly. Design tip block has all 4 required fields (Article visual / Format / Adaptation / Keep) and the `infographic` format choice is justified by an explicit reference to the article's own manual-vs-FitXpress comparison structure.

### E. Output quality — 3/4
- The post runs to ~1,772 of the 1,800-character ceiling as five dense, unbroken paragraphs with no bullets, bolding, or line-break devices. The two prior top-performing `linkedin-company` posts in `brand-assets/past-posts/linkedin-company/` (2026-04-30 "Better outcomes start with better data," 2026-05-19 "Insurance underwriting still relies heavily...") both used short lines, arrow/checkmark bullets, and white space to stay scannable in-feed — this draft is comparatively harder to skim on mobile before the "see more" cutoff, even though the opening hook (line 18, ~129 characters) lands within the visible preview. A 5-10 minute pass to break out the operational-gains list (line 26: fewer site visits / less coordinator time / audit-ready records) into 3 short lines would improve scannability without touching the substance.
- Otherwise strong: a genuinely differentiated angle for a company-page post (regulatory-scope literacy rather than a feature recap), precise compliance framing that a compliance-literate CRO/sponsor reader will recognize as credible rather than promotional, and a design tip that adapts the OG banner into a feed-native comparison graphic rather than reusing it as-is.

## Top 3 issues (приоритет для improver)

1. Minor: near-ceiling length (1,772/1,800 chars) delivered as five unbroken paragraphs reduces in-feed scannability relative to the profile's own top-performing past posts — a formatting pass (short lines/bullets for the operational-gains sentence), not a rewrite.
2. None (Adherence, Factual accuracy, Brand/tone, Format all clean).
3. None.

## Coordinator review

(заполняется Claude в чате после автозапуска QC)
