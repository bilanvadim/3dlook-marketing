---
qc_date: 2026-10-01
agent: icp-validator
artifact: workspace/outbound/campaigns/2026-10-01-us-options-medical-weight-loss/decisions.md (rows 7-15) + icp-validation-summary.md ("Widening 2026-10-01", lines 76-136)
track: outbound
artifact_type: icp-validation
total_score: 14/20
status: marginal
coordinator_review: done
---

# QC Report — icp-validator (widening round) — 2026-10-01

**Artifact:** `decisions.md` lines 7-15 (the 9 Apollo people) and `icp-validation-summary.md` lines 76-136
**Scored against:** `card-validate.md` (widening block lines 100-113, standing decisions lines 77-89) and `people-compact.csv` rows 7-15. The first five rows were not rescored. Limits and completeness were taken from the code checks. QC opened the raw Apollo row only to check facts the agent asserted.
**Total: 14/20** — marginal

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 3 | 5 |
| B | Factual accuracy | 2 | 5 |
| C | Brand & tone | 3 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 3 | 4 |

## What holds

- All 8 PASS rows match the card's tier and lane (card lines 104-108). Stats recount correctly: P1/P2/P3 = 4/3/6, angles 5/2/6, 13 of 50. The `flags` column is empty on rows 7-15, `people-validated-v1-2026-10-01.csv` exists, and `skipped-detail.md` matches.
- These are real findings: the Castle and Nelson link through Arizona Urology (line 126), Walker as a sponsor rather than the operator (line 128), and the reverse command with the `--wave 2` trap (line 116). The raw row confirms the Collins and Stevens histories: Director of Clinical Support and Director of New Clinic Openings were both at Options.

## What was wrong (specific)

### A. Adherence — 3/5
- **The Kenny Scott FAIL does not meet the card's own condition.** Card line 111 says Apollo "lists two current roles" and to drop him "if the profile shows he left Options". Summary line 116 admits "his LinkedIn page was not opened". Standing decision #3 (card line 83) reserves FAIL for people not actually at the company. #7 (line 87) keeps possibly stale profiles "unless the job-change check shows they have left". The prompt says "На грани → WEAK" and "Не будь слишком жёстким". A departure nobody has verified puts him in PASS P3 `referral` with the pre-send check, like Leflore, Hicks and Foy, or at most in WEAK. It does not justify a FAIL.
- **Leflore's row has no ask.** Decisions line 14 and summary line 109 only explain why he is kept. Card line 109 requires a distinct question for each person in a shared lane, and summary line 112 says "The referral notes above give the sequencer a separate ask for each referral person". That is not true for him.
- **"after a fitness-club background" (line 116) is not in either input.** Compact row 7 is cut off at "Senior General Ma…". The claim matches only the raw Apollo row (Life Time Inc., Q The Sports Club), which the prompt says not to read. Either the agent read outside its inputs or it guessed.

### B. Factual accuracy — 2/5
- **The cross-check that drives the FAIL is false.** Line 116 says: "For the eight other Apollo people, the current Options title is not repeated in earlier roles." Walker's compact row has the title "Founder" and earlier_roles "Founder at Options Medical Weight Loss, Chief Executive Officer at…". The compact list drops each person's first-listed role and keeps the rest. Walker's first-listed role is his board seat at Options. Kenny's is Crunch. So a title showing up in earlier_roles is a side effect of how the column is built. It does not mean the job is in the past.
- Line 116, "So the export treats Options as his previous job", contradicts card line 111 ("two current roles"). In the raw row, Kenny's Apollo record was refreshed 2026-09-26 and still lists Options.
- The departure is stated as fact in decisions line 15, skipped-detail line 9 and summary lines 110 and 135 ("left Options for Crunch Fitness"). Only line 116 calls it an inference.
- **Leflore:** "his only earlier role is ... The Lauren Group" (decisions line 14, summary line 117) misreads the compact field. It split "The Lauren Group, LLC" at the comma. The raw row lists four more earlier roles: multi-unit manager at Foot Solutions and at Good Feet, plus business development. The "unusual path to a Clinical Director title" doubt rests on that misreading. In round one the agent wrote "in the compact row" for Del Cecato but not here.
- Minor: "Nelson is part-time" (line 127) is a guess from a headline that lists two roles, stated as fact. "He built the in-clinic model" (decisions line 7) is an inference, and it reached Walker's message hook as fact (`messages/drmatthewwalker.md` lines 5 and 16). The raw row shows a chiropractic background (Chiropractor at Sheedy Family Chiropractic). "Physician" is his own headline word, so the risk is low, but message QC should know.
- Sourcing: no proof-point numbers, no client names and no invented roles.

### C. Brand & tone — 3/3
- No issues. This is an internal document. The only em dash is in the template heading (line 10).

### D. Format & structure — 3/3
- No issues. The pipe schema holds, no reason contains `|`, the FAIL reason is 5 words, line 12 notes the superseded counts, and the decisions-on-record block is adapted to the waiver.

### E. Output quality — 3/4
- The Kenny row has to be reversed or made WEAK before the send. As it stands, the referral lane loses its only regional Sales & Operations seat.
- The bar is inconsistent. The person the card calls possibly stale (Leflore, record 11 months old) stays. The person the card says lists Options as current (Kenny) goes.
- Leflore will get whatever ask the sequencer invents. Stevens is also in the Atlanta area, so overlap risk is highest there.
- Waclawski's ask ("what the programs include, framed around regional sales", decisions line 12) sits close to Del Cecato's sales angle in `program-feature`. That is cross-lane overlap at a single account.
- Line 129, "Still nobody owns the app or the vendor build", leaves out Pflanz. His earlier roles are Head of Marketing and Ecommerce and VP Ecommerce, which makes him the closest digital owner on the list.

## Top 3 issues (priority for improver)

1. **Kenny Scott FAIL on an unverified departure.** The card's drop condition ("profile shows he left") was not checked, and the card itself says both roles are current. Fix: PASS P3 `referral` pending the pre-send profile check (or WEAK). Rule for the prompt: apply a conditional drop from the card only when its condition is verified. A guess from a compact-list column means WEAK.
2. **A false cross-row check presented as evidence** (Walker's row contradicts "the current Options title is not repeated in earlier roles"). earlier_roles is every listed role except the first, so it can include current roles. If you test a pattern across rows, check every row before using it to drop someone.
3. **Leflore: no distinct referral ask, and "only earlier role" misreads a split field.** The single-account rule needs an ask per person. Attribute claims to "the compact row" and stay inside the two inputs ("fitness-club background" came from outside them).

## coordinator_review

```
agreement: ✅ agree
top_issue: Kenny Scott's FAIL rested on an unverified departure and a false cross-row check (earlier_roles can hold current jobs)
action: reversed to PASS P3 referral with promote (no wave); Apollo search lists Options as his current org (2026-09-26), web search inconclusive; Leflore kept, his distinct ask is in his messages; correction recorded in icp-validation-summary.md
```
