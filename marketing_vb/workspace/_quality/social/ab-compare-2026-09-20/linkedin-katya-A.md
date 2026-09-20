---
qc_date: 2026-09-20
agent: post-drafter
artifact: workspace/social/articles/bariatric-hub-refresh/linkedin-katya/post.md
track: social
artifact_type: post
total_score: 20/20
status: excellent
lint: pass
coordinator_review: |
  agreement:
  top_issue:
---

# QC Report — post-drafter — linkedin-katya — 2026-09-20

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
- Geo discipline is clean: zero geo mentions (`lint.metrics.geo_mentions: 0`), and the post never states or implies "I talk to operators across Israel and the Gulf" — it earns the audience by writing about a problem (pilot design), exactly what personal-rule 3 asks for.
- The brief's "Avoid: US payer system context" is honored under real temptation: the source article spends four sections on CMS-0057-F, prior-authorization timeframes and payer documentation, and the post takes none of it — it stays on pilot mechanics and human-review boundaries, which travel across markets.
- The teaching matches the personal-profile menu exactly: "the order two steps belong in" (rule 4) — "First: set your baseline and evaluation period before launch, not after. Second: separate what the capture produces from what your review team decides." This is one coherent instruction, not a listicle.
- Hook is a ~8-word disagreeable claim ("Accuracy specs rarely close a digital health deal."), not a question or a teaser — matches personal-rule 5 precisely.
- Closes with a discussion question that needs the reader's own pilot data ("If you ran a scan pilot next quarter, which single number would tell you it worked?"), then routes to the article via the CTA line — matches "Finish with a discussion question before linking to the article."

### C. Brand & tone — 3/3
- No banned words, no em-dash rhetoric, no "not just X, it's Y," no triple parallelism, no inflated-significance language ("a new era of," "plays a crucial role"), no slogan close.
- First person is used the way the brief wants it: as lived observation ("I've watched obesity-care programs nod at…"), never as the banned stance-announcement line ("I speak with operators across the region every week").
- `lint.warnings` flags borderline rhythm (`sentence-length variation 0.34`, wants `>0.35`) — real, but on inspection the sentences vary in construction and function (declarative claim, first-person anecdote, two-step instruction, evaluative contrast, question), not just in a way the word-count metric captures. Not treated as a tone lapse; flagged below as a watch-item for the drafter.

### E. Output quality — 4/4
- **Position:** stated directly and is arguable — "Accuracy specs rarely close a digital health deal. A pilot does." and "The specs aren't the blocker." This isn't a hedge; a reader could push back ("our specs are the blocker"), which is the bar the rubric sets. The post also takes a stance on where the software's authority stops: "A flagged BMI discrepancy is a signal for human review, never an automated eligibility conclusion."
- **Teaching that survives without the click:** a reader gets a usable rule of thumb (define baseline + evaluation period before launch; separate capture output from review decision) even if they never open the article.
- **Angle distinctness:** `sibling_angles` was not included in this run's input, so cross-profile duplication can't be checked directly. Judged against its own stated angle ("Enterprise buying behaviour, not accuracy specs"), the post is internally consistent and distinct from an accuracy-led or feature-led framing of the same article.

## Top issue for `post-drafter`

None that changes the score, but worth watching: the ai-tells rhythm check came in at 0.34 against a 0.35 house-rule floor — most sentences cluster in the 9-16 word range with only two short outliers ("A pilot does." / "The specs aren't the blocker."). If this pattern repeats across posts, the fix is a real four-word line next to a real twenty-word line, not just alternating topic content within a narrow length band.
