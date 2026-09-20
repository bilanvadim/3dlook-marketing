---
qc_date: 2026-09-20
agent: post-drafter
artifact: workspace/social/articles/bariatric-hub-refresh/linkedin-nick/post.md
track: social
artifact_type: post
total_score: 18/20
status: excellent
lint: pass
coordinator_review: |
  agreement:
  top_issue:
---

# QC Report — post-drafter — linkedin-nick — 2026-09-20

**Total: 18/20** — excellent

## Scores

| # | Category | Score | Max | Basis |
|---|----------|-------|-----|-------|
| A | Adherence | 4 | 5 | judged |
| B | Factual accuracy | 5 | 5 | lint (hard_fails: []); checked for subject-swap and lost-quantifier defects the linter can't catch, found none |
| C | Brand & tone | 3 | 3 | judged |
| D | Format & structure | 3 | 3 | lint (hard_fails: []) |
| E | Output quality | 3 | 4 | judged |

## Findings

### A. Adherence — 4/5
- Geo discipline is clean: the post is scoped to a US federal regulator (CMS = Centers for Medicare & Medicaid Services), `geo_mentions: 0` per lint, no "For US teams…" opener, nothing that reads as an announced location — matches personal-profile rule 3 and Nick's brief ("Avoid: European regulatory context").
- Structure matches the required shape: hook as a claim, not a question ("The new prior-authorization clock does not cover every bariatric case."), short paragraphs, close on a question that needs the reader's own book-of-business split to answer ("Which covers more of your bariatric volume today: plans inside CMS-0057-F, or plans outside it?"), then "Article in the comments." as the invite.
- Miss: Nick's brief says "Mention FitXpress naturally when relevant." The post's entire teaching point is a documentation gap — "map what its packet needs for body-data documentation… The gap is usually a date or a source field" — and the design tip's own article visual is the prior-authorization coordinator having "access to the record before assembling the packet." That is the exact sentence where FitXpress's verified, timestamped body data would name itself, and it never does. Reads as skipped, not as the brief's "never force" restraint.

### C. Brand & tone — 3/3
- No banned words, no em dash, no "not just X, it's Y", no triple parallelism, no inflated-significance filler ("a new era of…", a commitment-tail sentence). The close is a real question, not a slogan.
- The one first-person line — "The move I would make first: take one plan, map what its packet needs…" — is exactly where personal-profile rule 5 asks for first person, and it stays there instead of leaking into a company voice elsewhere in the post.

### E. Output quality — 3/4
- **Position:** "For a bariatric program, the faster clock covers part of your book only. Worth confirming which part before you rebuild intake around it." followed by "The gap is usually a date or a source field." This is a specific diagnosis of where the failure actually shows up, not a restatement of the CMS rule — the post judges, it doesn't just report.
- **Angle distinctness:** `sibling_angles` were not included in this input, so distinctness against the rest of the pack can't be checked directly. The angle as stated in `post_meta` — "which share of a bariatric book the timeframes actually touch is the number worth knowing" — is a scoped, falsifiable claim rather than a generic "new rule matters" framing, which is the right shape for this rule regardless of what siblings did.
- What holds it at 3, not 4: lint's own warnings are real defects, not noise — the 27-word sentence and "every block the same size" ai-tell mean a short edit pass (vary one paragraph's rhythm, split the long sentence) is still needed before this is fully as-is. That's a 5-10 minute fix, not a rewrite, hence 3 rather than lower.

## Top issue for `post-drafter`

When the article's own workflow visual is built around a documentation gap that FitXpress closes, don't let "mention only when natural, never force" become an excuse to skip the product entirely — name it once, plainly, at the sentence where the gap is diagnosed.
