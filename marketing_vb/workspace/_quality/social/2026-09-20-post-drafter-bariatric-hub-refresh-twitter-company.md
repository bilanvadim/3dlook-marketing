---
qc_date: 2026-09-20
agent: post-drafter
artifact: workspace/social/articles/bariatric-hub-refresh/twitter-company/post.md
track: social
artifact_type: post
total_score: 18/20
status: excellent
lint: pass
coordinator_review: |
  agreement:
  top_issue:
---

# QC Report — post-drafter — twitter-company — 2026-09-20

**Total: 18/20** — excellent

## Scores

| # | Category | Score | Max | Basis |
|---|----------|-------|-----|-------|
| A | Adherence | 5 | 5 | judged |
| B | Factual accuracy | 3 | 5 | lint + judged |
| C | Brand & tone | 3 | 3 | judged |
| D | Format & structure | 3 | 3 | lint |
| E | Output quality | 4 | 4 | judged |

## Findings

### A. Adherence — 5/5
- 258 chars sits inside both the hard budget (1-280) and the profile's tighter target
  ("length: 240-260 chars for single tweet").
- Content type matches "One striking stat or claim from the article" (34.1% / 140.4%,
  JAMA Surgery) followed by a "Short POV on industry trend" — the tone brief calls for
  "One sharp insight from the article — не переказ," and the post does not summarize the
  article, it isolates one framing (which BMI counts) that the article raises only in
  passing (published-live-2026-09-20.md line 78).
- No hashtags, no emoji, no bullet list — matches "hashtags: none" and "avoid: bullet
  lists, emoji flood, generic corporate speak."
- CTA ("Full breakdown of the intake workflow, link in reply") matches the profile's
  "article link у відповіді."

### B. Factual accuracy — 3/5 (lint pass, but one claim overstates its source)
- The two headline numbers (surgery use fell 34.1%, GLP-1 use rose 140.4%, 2022-2024,
  JAMA Surgery) are correctly sourced and correctly attributed — matches
  published-live-2026-09-20.md line 74 exactly.
- The second sentence loses a hedge the linter cannot see. Article: "A patient **may
  therefore** arrive at bariatric intake with a current BMI below an earlier documented
  value" (line 78) — an inference drawn from a population-level claims-cohort study plus
  a separate ASMBS conference study (~6,700 patients, ~8% average pre-op weight loss),
  explicitly hedged as a possibility for an individual patient, not a documented pattern.
  Post: "Patients arrive at intake with a current BMI below their earlier documented
  value" — drops "may" and "therefore," and converts a hedged, singular inference into an
  unqualified, generalized claim about patients as a class. The underlying numbers are
  real and correctly cited; the claim built on top of them is stated with more certainty
  than the article itself claims. This is the same class of defect as a dropped
  quantifier (source scopes a claim, tweet drops the scoping), just on a hedge rather
  than a number.

### C. Brand & tone — 3/3
- No banned words, no em dash, no "not just X, it's Y." Register matches the profile's
  "Punchy, data-first... Industry commentary tone" — short declarative sentences, a
  rhetorical question used functionally (naming the open variable), no filler.

### E. Output quality — 4/4
- **Position:** "That's the documentation problem." The post does not stop at reciting
  the trend stat — it reframes the GLP-1-vs-surgery reversal as an operational question
  ("Which number counts, from when, and how was it captured?") rather than a clinical or
  market story. That reframing is the judgment call; a compiled version of this tweet
  would have stopped after the stat.
- **Angle distinctness:** N/A — `sibling_angles` is empty (this is the first profile in
  the pack), so this post is setting the pack's angle map rather than being checked
  against one.

## Top issue for `post-drafter`

When compressing a hedged, inferential sentence from the article ("a patient may
therefore arrive...") into a tweet, keep the modal hedge or the conditional framing —
turning a possibility about an individual case into an unqualified plural claim about
patients generally overstates what the cited studies actually establish.
