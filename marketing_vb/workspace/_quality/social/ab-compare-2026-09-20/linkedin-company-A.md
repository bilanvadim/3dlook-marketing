---
qc_date: 2026-09-20
agent: post-drafter
artifact: workspace/social/articles/bariatric-hub-refresh/linkedin-company/post.md
track: social
artifact_type: post
total_score: 18/20
status: excellent
lint: pass
coordinator_review: |
  agreement:
  top_issue:
---

# QC Report — post-drafter — linkedin-company — 2026-09-20

**Total: 18/20** — excellent

## Scores

| # | Category | Score | Max | Basis |
|---|----------|-------|-----|-------|
| A | Adherence | 5 | 5 | judged |
| B | Factual accuracy | 5 | 5 | lint + judged |
| C | Brand & tone | 2 | 3 | judged |
| D | Format & structure | 3 | 3 | lint |
| E | Output quality | 3 | 4 | judged |

## Findings

### A. Adherence — 5/5
- Regulatory scope is stated explicitly, twice: the hook ("A new prior-authorization clock is running for **US bariatric programs**.") and the body ("Medicare Advantage organizations and specified Medicaid and ... CHIP payers"). This mirrors the article's own scope note ("The regulatory examples below concern US adult bariatric programs.") rather than presenting a US-only rule as universal — correct discipline for a global company page discussing a country-specific regulator.
- Positioning matches CLAUDE.md §3's outcomes-over-accuracy strategy: the post leads with a business/regulatory pressure, not a capability claim, and explicitly bounds FitXpress ("It does not shorten a payer's deadline or assure acceptance, and FitXpress is not a medical device") instead of overselling.
- Structure follows the brief exactly: hook → regulatory context → business implication → problem → FitXpress fit → honest limits → operational payoff → CTA. Voice is third person throughout ("Clinical eligibility stays with the care team..."), no founder "I" voice, satisfying "third person or we, never founder's personal voice."
- CTA ("Read the full article on bariatric pre-qualification and progress tracking.") matches the brief's closing requirement verbatim in spirit.

### B. Factual accuracy — 5/5 (lint hard_fails empty; judged check below)
- Cross-checked every load-bearing claim against `published-live-2026-09-20.md`: the 7-day/72-hour CMS-0057-F timeframes, the "specified Medicaid and CHIP" qualifier (not dropped to a bare "Medicaid"), the Medicare fee-for-service and QHP-on-FFE carve-outs, the "80+ body measurements / BMI comparison / capture-quality flags" output list, "does not shorten a payer's deadline or assure acceptance," and the exact canonical "FitXpress is not a medical device." — all preserved with their qualifiers intact. No quantifier was widened or dropped (the CMS scope stays "specified" payers, not "all payers" or generic "employers").
- One soft spot, not a hard fail: "self-reported figures do not always hold up" replaces the article's specific CDC statistic (self-reported BMI underestimated severe-obesity prevalence by 40%, population-level). This is actually the *safer* choice — the article itself warns that population-level result "does not establish whether an individual patient's information is accurate," so quoting the 40% figure here would have been the overclaim. No deduction.

### C. Brand & tone — 2/3
- `lint.warnings` flags `ai-tells:house_rule`: "uniform paragraph length: every block the same size" (severity low). This is a real, judgeable tone issue, not noise: six of the seven body paragraphs run to almost exactly two sentences of similar length ("Faster decisions on the payer side raise the value of a clean submission. The practical question for intake teams is..." / "That is harder than it sounds... Body metrics vary in format..." / "This is where a structured capture earns its place. With FitXpress, a guided two-photo scan..."), giving the post a metronomic, template-generated cadence rather than natural variation. One minor lapse per the rubric → C=2.
- No banned words, no em dash, no "not just X, it's Y," no triple parallelism, no sloganistic close — the ending is a plain operational statement ("The value here is operational: a more complete first packet, and fewer round-trips."), not a hollow commitment-tail.

### E. Output quality — 3/4
- **Position:** the post does judge, not just recite. "Faster decisions on the payer side raise the value of a clean submission" and "This is where a structured capture earns its place" stake a specific claim — that the real consequence of CMS-0057-F is pressure on intake-side documentation, not a payer-side speed benefit patients or clinics can bank on — and "The value here is operational: a more complete first packet, and fewer round-trips" explicitly frames where the payoff is (and, by omission, where it isn't: not the deadline, not acceptance, not clinical eligibility). That is a defensible editorial position, not a mechanical summary of the rule.
- **Angle distinctness:** per the post's own `Angle:` line, this is the regulatory-deadline angle, distinct from the GLP-1, human-moment and bottleneck angles already used elsewhere in the pack. The CMS-0057-F hook and its 7-day/72-hour figures are specific to this post and not implied by any of the other three.
- Held to 3, not 4, because of the same cadence problem noted under C: the uniform two-sentence-paragraph rhythm reads slightly templated and would benefit from one pass varying sentence and paragraph length before publication — a 5-10 minute edit, not a rewrite.

## Top issue for `post-drafter`

Vary paragraph and sentence length across the body instead of settling into a uniform two-sentence block per paragraph — the `ai-tells:house_rule` uniform-paragraph-length flag is a symptom of a real cadence problem here, not noise, and is worth a prompt reminder if it recurs across the pack.
