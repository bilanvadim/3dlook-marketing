---
qc_date: 2026-07-05
agent: post-drafter
artifact: workspace/social/articles/2026-06-16-clinical-trials-obesity-metabolic-hybrid-dct/twitter-company/post.md
track: social
artifact_type: post
total_score: 19/20
status: excellent
coordinator_review: pending
---

# QC Report — post-drafter — 2026-07-05

**Artifact:** `workspace/social/articles/2026-06-16-clinical-trials-obesity-metabolic-hybrid-dct/twitter-company/post.md`
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
No issues. `product: fitxpress` correctly carried from `publish-package.md` frontmatter. `article_slug` field correctly uses the publish-package's `article_slug` (`clinical-trial-anthropometric-measurement-software-obesity-trials`), not the dated workspace folder name — matches the template spec exactly. `brand-assets/past-posts/twitter-company/` is empty (0 files); per the prompt's explicit fallback ("If the folder is empty, continue without them, do not STOP") this is not a violation. Design tip's "Article visual" line closely paraphrases the actual Section 4 ("OG Image Brief") content — multi-site motif, guided-scan smartphone, timestamp/structured-record icon — confirming the article's OG brief was actually read, not skipped. Manifest updated correctly, with an added `"note"` field flagging this is a partial run (only twitter-company generated so far) — a thoughtful, accurate addition beyond the bare template.

### B. Factual accuracy — 5/5
No issues. "Under 45 seconds" matches `proof-points.md` → Speed → "Time from photo to results | Under 45 seconds" verbatim. "12-month study" / "twelve-month study" duration is pulled directly from the source article body ("Documentation conventions can drift over a twelve-month study"), not invented. No customer names, no case studies, no comparison claims. Post text stays inside the article's `compliance_guardrails` (no DEXA-alternative claim, no endpoint-validation claim, no eligibility-determination claim) despite `compliance_sensitive: true` on the source article.

### C. Brand & tone — 3/3
No issues. No banned words (leverage/utilize/harness/robust/seamless/comprehensive/delve/navigate/tapestry/realm/unlock/unleash/game-changing/cutting-edge). No em-dash, no "not just X, it's Y," no triple parallelism. Tone matches the `twitter-company` profile spec ("Punchy, data-first. One sharp insight from the article — industry commentary tone").

### D. Format & structure — 3/3
No issues. Frontmatter complete (`profile`, `platform`, `article_slug`, `product`, `status`, `created`). File saved at the exact path specified by the prompt template. Tweet body is 255 characters including the "Link in bio" close — within the 280 hard limit and inside the prompt's "single tweet: 240-260 chars" guidance. Design tip has all 4 required fields (Article visual / Format / Adaptation / Keep).

### E. Output quality — 3/4
- The core sentence has a minor dangling-modifier ambiguity: "They fail on the workflow around it, drifting across sites and staff over a 12-month study." — it's not immediately clear whether "drifting" attaches to "workflow" or to the trials themselves. Reads fine on a skim but a careful copyedit pass (5 min) would tighten it, e.g., "...workflow around it: it drifts across sites and staff over a 12-month study."
- Otherwise strong: single clear angle (workflow vs. measurement, the article's actual thesis), no summarizing, professional and non-generic for a B2B thought-leadership tweet.

## Top 3 issues (приоритет для improver)

1. Minor: dangling modifier in the main tweet sentence ("drifting across sites and staff") creates slight ambiguity — a 5-minute copyedit, not a rewrite.
2. None (Adherence, Factual accuracy, Brand/tone, Format all clean).
3. None.

## Coordinator review

(заполняется Claude в чате после автозапуска QC)
