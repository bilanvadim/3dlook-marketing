---
qc_date: 2026-09-20
agent: post-drafter
artifact: workspace/social/articles/bariatric-hub-refresh/linkedin-company/post.md
track: social
artifact_type: post
total_score: 20/20
status: excellent
lint: pass
coordinator_review: |
  agreement:
  top_issue:
---

# QC Report — post-drafter — linkedin-company — 2026-09-20

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
- Hook names the market problem the brief asks for and matches the stated Angle: "Obesity care has a sequencing problem, and it rarely gets named." This is the brief's "identify the biggest market trend or problem discussed", not a restatement of the article's title.
- FitXpress appears exactly once, framed as an input supplier, not the subject: "FitXpress supplies those inputs." Matches "mention FitXpress only where it fits naturally — never the centre of the post" and the anti-positioning instinct in CLAUDE.md §3 (outcomes, not the product).
- Closing paragraph is a business-value list ("intake completion, time to a completed record, prior-authorization rework, measurement-only appointments, and follow-up completion") pulled verbatim from the article's Use Case Summary business-value row — matches "focus on business value rather than product promotion."
- Voice check: "the nine items we would confirm" uses "we" as the company voice, never first-person singular — matches "third person or 'we'. Never a founder's personal voice."
- CTA is specific rather than generic ("including the nine items we would confirm in a bariatric pilot") — this count is correct against the article's "What to confirm in a bariatric pilot" table, which has exactly nine rows.

### B. Factual accuracy — 5/5 (lint pass; checked what lint can't)
- `lint.hard_fails` and `lint.warnings` are both empty, so no `number_drift`, no format hard fails.
- Checked the one pattern lint cannot catch — a quantifier or population boundary narrowed in transcription. CDC line: article "40.3% of US adults had obesity (BMI of 30 or higher) and 9.4% had severe obesity (BMI of 40 or higher)" → post "40.3% of US adults had obesity and 9.4% had severe obesity." The dropped clause is a BMI-threshold gloss, not the population scope ("US adults" is preserved) — this is not the employers/firms-with-5,000+-workers failure mode, it's a legitimate compression.
- ASMBS "less than 1% of eligible patients undergo surgery in a given year" and the 2026 narrative-review attrition line ("as high as 60%, while other cohorts... reported substantially different rates") both carry their subject and hedge intact against the article's own wording.
- No case or client substitution (no named client appears in this post at all), no number reassigned to a different subject than the article uses it for.

### C. Brand & tone — 3/3
- No banned words, no em-dash rhetoric, no triple parallelism, no slogan-style close, no first person.
- "Earlier body data does not resolve those gaps. What it changes is where a program can measure." is two separate sentences, not the banned "X, not Y" corrective-negation formation — it reads as analysis, not a templated AI construction.
- Register stays enterprise/educational throughout; the emoji (📊) sits next to the CTA and the measurement framing, not decorative.

### E. Output quality — 4/4
- **Position:** "Earlier body data does not resolve those gaps. What it changes is where a program can measure." This is a real judgment call — it explicitly declines to oversell what earlier capture does (it doesn't fix attrition or low surgery uptake) while asserting the actual claim (it relocates the measurement point). That's the difference between this post and a compiled fact list: it tells the reader what the data does *not* do before saying what it does.
- The three-stat opening paragraph (CDC / ASMBS / 2026 review) is dense but each figure is load-bearing for the position that follows, not filler.
- **Angle distinctness:** `sibling_angles` were not included in this ab-compare input, so cross-profile distinctness cannot be judged here. Judged in isolation, the angle ("sequencing, not measurement, is the market's problem") is specific enough to survive on its own — it is not a generic "3D scanning helps bariatric programs" framing.

## Top issue for `post-drafter`

None — no defect found in this pass; hold this post up as a reference example of a position stated in plain declarative sentences rather than left implicit in the fact list.
