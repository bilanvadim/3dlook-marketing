---
qc_date: 2026-09-04
agent: post-drafter
artifact: workspace/social/articles/2026-05-21-online-pharmacy-bmi-verification/linkedin-olena/post.md
track: social
artifact_type: post
total_score: 19/20
status: excellent
lint: pass
coordinator_review: |
  agreement: ✅ agree
  top_issue: Persona seam in "When I review a vendor, I ask this first" — Olena is 3DLOOK's own BD rep, not a buyer, so casting her as vendor-evaluator one sentence before "In FitXpress, images are blurred..." reads slightly inverted; not a rewrite-worthy defect on this single post, worth watching if the first-person-fix pattern recurs across the pack.
---

# QC Report — post-drafter — linkedin-olena — 2026-09-04

**Total: 19/20** — excellent

## Scores

| # | Category | Score | Max | Basis |
|---|----------|-------|-----|-------|
| A | Adherence | 5 | 5 | judged |
| B | Factual accuracy | 5 | 5 | lint + judged |
| C | Brand & tone | 2 | 3 | judged |
| D | Format & structure | 3 | 3 | lint |
| E | Output quality | 4 | 4 | judged |

## Findings

### A. Adherence — 5/5
- Region discipline is clean: no country name anywhere (lint confirms 0 geo mentions), GDPR is used as the one EU-wide framework the brief explicitly allows ("Under the General Data Protection Regulation (GDPR)…"), and there is no UK/US/Israel material.
- Personal-profile rule 3 (no location announcement, no "I speak with…" line) is honored — the post never states who Olena talks to or where.
- Rule 4 (teach one thing) is satisfied concretely: "what happens to the image after the estimate is produced?" is a single, usable procurement question, not a listicle.
- Rule 5 (hook is a claim, not a question) is satisfied: "Every verification step you add is also a data-retention decision." is a falsifiable assertion, exactly the required opener shape.
- Sentence-length variance (lint: longest 26 words) is the one place the brief's "most under 15 words" is stretched, but the brief itself asks for rhythm variation ("a four-word line next to a twenty-word one"), and the single long sentence carries the pivotal regulatory question — this reads as deliberate emphasis, not a skipped step.
- Verified against the article (`published-live-2026-08-24.md`): the post's framing of camera-roll evidence ("says little about when or how it was made") tracks the article's own language ("limited evidence of when, how, or by whom it was created") without inventing a number or a case. No subject-swap or quantifier loss found in the FitXpress claim (blur/delete-by-default is consistent with `proof-points.md`'s "Immediate delete OR within 30 days per client policy" / "Photo blur on storage: Auto-applied").

### C. Brand & tone — 2/3
- No banned words, no em-dash rhetoric, no "not just X, it's Y." The lapse is the one lint already flagged and it is real on inspection, not a false positive: three of the post's seven paragraphs use the identical shape — short assertion, short pivot — "Good move. But it changes your data footprint." / "Data minimization isn't a footnote here. It's the difference between reducing fraud risk and creating a retention liability." The rhythm is intentional (short paragraphs are the brief's own instruction) but repeating the same two-beat pattern three times reads templated rather than spoken.
- Minor persona note, not scored as a lapse but worth flagging for the improver: "When I review a vendor, I ask this first" casts Olena (3DLOOK's own BD rep) as a vendor-evaluator rather than a vendor. It works as a teaching device but sits slightly oddly next to "In FitXpress, images are blurred…" in the very next sentence — she is reviewing and answering in the same breath.

### E. Output quality — 4/4
- **Position:** the post makes an explicit priority call and asks the reader to reorder their own checklist: "that raises a question worth putting before accuracy itself" and "When I review a vendor, I ask this first, before any accuracy number." This is a judgment (privacy-before-accuracy), not a restatement of the article's facts.
- **Angle distinctness:** clearly separate from the other eight. `linkedin-katya` owns the generic procurement-question/vendor-theatre angle with no EU regulatory content; this post is the GDPR-specific retention mechanic (blur, delete, structured-output retention) that only Olena's brief permits. It doesn't overlap with `linkedin-company`'s enterprise-governance framing, `linkedin-katerina`'s GPhC anchor, or `linkedin-nick`'s CDC/BAA framing.

## Top issue for `post-drafter`

None — vary the short-paragraph rhythm (not every block needs the assertion-then-pivot shape) if this pattern recurs across the pack, but it is not a defect worth a prompt change on this single post.
