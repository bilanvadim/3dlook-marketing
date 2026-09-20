---
qc_date: 2026-09-20
agent: post-drafter
artifact: workspace/social/articles/bariatric-hub-refresh/facebook-company/post.md
track: social
artifact_type: post
total_score: 17/20
status: good
lint: pass
coordinator_review: |
  agreement:
  top_issue:
---

# QC Report — post-drafter — facebook-company — 2026-09-20

**Total: 17/20** — good

## Scores

| # | Category | Score | Max | Basis |
|---|----------|-------|-----|-------|
| A | Adherence | 4 | 5 | judged |
| B | Factual accuracy | 5 | 5 | lint + judged |
| C | Brand & tone | 2 | 3 | judged |
| D | Format & structure | 3 | 3 | lint |
| E | Output quality | 3 | 4 | judged |

## Findings

### A. Adherence — 4/5
- Product bias, length, hashtags and CTA all match the brief exactly: 100% FitXpress content, 1013 chars inside 800-1200, zero hashtags, and the CTA line "Read the full article (link in comments)." reproduces the brief's `«Read the full article» з посиланням` verbatim.
- Content type matches "Industry question that sparks discussion": the post closes on "where does the delay actually sit for you right now: getting the record, or getting it in a usable form?" — a genuine open question, not a rhetorical one with an implied answer.
- The brief's tone line is explicit: "Broader audience than LinkedIn — explain without jargon." The post keeps "pre-qualification," "prior-authorization packet," "payer," "clinical eligibility" undefined. Each is inferable from context, but none is glossed for a reader outside health-ops, so the "explain without jargon" instruction is only partially executed. This is the one point holding A back from 5 — it is a superficial pass on a named brief requirement, not a violation of anything hard (region, product, structure).

### C. Brand & tone — 2/3
- Lint already flags `ai-tells:house_rule` — uniform paragraph length. Word counts by paragraph: ~55 / ~45 / ~33 / ~26. The house-rule check is tuned to catch exactly this shape: three body blocks that read as same-size units before the closing one-liner, which is the "every paragraph is a slab" cadence AI drafts default to. This is the first minor lapse.
- "One thing worth saying plainly:" is a hedge-transition formula — it does not appear on the banned list, but it is the same family of scaffolding phrase the tone guardrails ask writers to cut rather than lean on to introduce a limitation. Combined with the paragraph-uniformity flag, that's two minor lapses, which is what keeps this at 2 rather than 3 (no single "3+ banned words" violation, so not a 1).
- No banned words present (leverage/utilize/harness/robust/seamless/comprehensive/delve/navigate/tapestry/realm/unlock/unleash/game-changing/cutting-edge — none found), no em dash, no "not just X, it's Y."

### E. Output quality — 3/4
- **Position:** the post does take a stance, not just compile facts. "Here is a quiet bottleneck in bariatric care... That is late." is a direct evaluative judgment on the current workflow, not a neutral restatement of the article. The scope-note paragraph ("this supplies inputs, not conclusions... FitXpress is not a medical device.") is also a chosen position — it draws the boundary of the claim rather than letting the reader assume more than the product does. This clears the "does it judge anywhere" bar the rubric cares about most.
- **Angle distinctness:** post_meta declares this "Distinct from Twitter's GLP-1 documentation angle and Instagram's human-moment framing" (no separate `sibling_angles` list was passed with this input to check against directly). Taking that framing at face value, it holds up: this post's angle is workflow-timing ("the record doesn't exist until the patient is already in the consultation") turned into an open discussion prompt, which is a different mechanism from a GLP-1-documentation angle or an emotional human-moment angle.
- Held to 3 rather than 4 by the same paragraph-uniformity pattern noted under C: the piece reads as three same-shaped explanatory blocks stacked before the question, which is competent and publishable but not yet the kind of rhythm-varied copy that reads as hand-written on a first pass.

## Top issue for `post-drafter`

If this recurs across the pack: paragraphs are landing at near-identical word counts (the house-rule ai-tells check exists because this is a known drafting default) — vary block length deliberately, especially by shortening or merging one of the three body paragraphs before the closing question.
