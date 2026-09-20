---
qc_date: 2026-09-20
agent: post-drafter
artifact: workspace/social/articles/bariatric-hub-refresh/twitter-company/post.md
track: social
artifact_type: post
total_score: 20/20
status: excellent
lint: pass
coordinator_review: |
  agreement:
  top_issue:
---

# QC Report — post-drafter — twitter-company — 2026-09-20

**Total: 20/20** — excellent

## Scores

| # | Category | Score | Max | Basis |
|---|----------|-------|-----|-------|
| A | Adherence | 5 | 5 | judged |
| B | Factual accuracy | 5 | 5 | lint + judged |
| C | Brand & tone | 3 | 3 | judged |
| D | Format & structure | 3 | 3 | lint |
| E | Output quality | 4 | 4 | judged |

## Findings

### A. Adherence — 5/5
- Brief calls for "Punchy, data-first. One sharp insight... не переказ" and lists "One striking stat or claim from the article" as a valid content type. The post opens with exactly that stat, compressed to a colon-delimited figure pair ("40%: 5.3% self-reported, 8.8% bias-corrected") rather than the article's fuller sentence — this is compression, not retelling.
- It does not stop at the stat. "That is a population-level result. The intake takeaway is smaller: record the source of every height and weight you receive." is the added POV layer the brief also allows ("Short POV on industry trend the article touches"), so the tweet is not a bare stat-dump.
- Length: 255 chars, inside the brief's tighter 240-260 band (not just the lint's generic 1-280 budget) — this is the profile-specific target, hit precisely.
- `hashtags: none` and no emoji, matching the brief; CTA in post_meta ("Soft, link in bio") matches the profile's `cta: "Link in bio"`.
- No market/region claim to police here (twitter-company carries no geo restriction, unlike the personal LinkedIn profiles), and the topic is 100% FitXpress, matching `product_bias`.

### C. Brand & tone — 3/3
- No banned words, no em dash, no "not just X, it's Y", no tripled parallelism, no slogan-style close. Checked against both the CLAUDE.md §6 list and the rubric's banned-words checklist.
- No inflated-significance language ("a new era of...", "plays a crucial role") and no filler tail after the actionable close — "record the source of every height and weight you receive" ends the post on the instruction itself.
- Direct-address "you" in the second sentence is a judgment call for a company account (contrast `linkedin-company`'s third-person register), but the profile brief for `twitter-company` does not prescribe a person, and "Industry commentary tone" plus "record... you receive" reads like a practitioner addressing peers, not a lapse into first-person brand voice.

### E. Output quality — 4/4
- **Position:** "That is a population-level result. The intake takeaway is smaller: record the source of every height and weight you receive." This is a judgment, not a fact restatement — it tells the reader what the stat does *not* license (an individual-level claim) and what to do instead. Without this second sentence the post would be a bare stat and E would cap at 2; with it, the post clears the bar.
- **Angle distinctness:** `sibling_angles` was not included in this qc-prompt, so cross-profile duplication cannot be checked here. Taken on its own, the angle is narrow and specific to intake documentation practice (not a generic "AI can help" framing), which is the right shape for a 255-char post.
- Reads as something a data-literate person wrote, not a compiled AI summary; ready to post as-is.

## Verification against the article (one claim checked)

Checked the CDC self-report figures against `workspace/seo/articles/bariatric-hub-refresh/published-live-2026-09-20.md` because this is exactly the class of defect (lost quantifier, subject swap) the lint cannot catch:

> "CDC researchers reported in Preventing Chronic Disease that self-reported BMI underestimated the population prevalence of severe obesity by 40%, with a prevalence of 5.3% based on self-reports and 8.8% after bias correction in 2020 data. This population-level result does not establish whether an individual patient's information is accurate. It does support a workflow that records the source of each value..."

The post's "40%: 5.3% self-reported, 8.8% bias-corrected" matches the article's figures and subject (CDC researchers) exactly. The population-level qualifier is not dropped — it is relocated into its own sentence ("That is a population-level result") rather than staying attached to the first clause, which is a legitimate compression choice for a 255-char tweet, not the quantifier-loss defect this pipeline usually produces. The operational close ("record the source of every height and weight you receive") tracks the article's "It does support a workflow that records the source of each value" without overclaiming the article's further "and routes discrepancies for review." No B deduction.

## Top issue for `post-drafter`

none — this post preserves the population-level qualifier exactly where the pipeline usually loses it (compare the "under a minute" / "Under 45 seconds" defect class), and pairs a correctly-scoped stat with an actual operational judgment rather than a restatement.
