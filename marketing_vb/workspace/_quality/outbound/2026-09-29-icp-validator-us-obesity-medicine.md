---
qc_date: 2026-09-29
agent: icp-validator
artifact: workspace/outbound/campaigns/2026-09-29-us-obesity-medicine/icp-validation-summary.md + decisions.md
track: outbound
artifact_type: icp-validation
total_score: 18/20
status: excellent
coordinator_review: done
---

# QC Report — icp-validator — 2026-09-29

**Artifact:** `workspace/outbound/campaigns/2026-09-29-us-obesity-medicine/icp-validation-summary.md`, `decisions.md`
**Scored against:** `card-validate.md` + `people-compact.csv` only (the agent's inputs). Counts and identity columns taken as fact from the code checks.
**Total: 18/20** — excellent

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 5 | 5 |
| B | Factual accuracy | 4 | 5 |
| C | Brand & tone | 3 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 3 | 4 |

## What was checked and holds

- All 65 PASS match the card persona by name and tier: P1 25/25, P2 22 of the card's 23 (Rivas held as WEAK), P3 18/18. Per-group PASS equals the card's "Send est." for all 7 groups.
- All 46 persona FAILs sit in the card's pools at exactly the card's sizes: R1 14, R2 7, R3 10, R4 15. Mitchell Greenberg is FAIL as card row 9 requires, even though `compact` grouped him under FlyteHealth and gave him only an `empty-profile` flag.
- Every figure in the summary recounts correctly from `decisions.md`: angles 20/20/13/5/3/3/1, waves 47/18, group splits, Form Health at 27 if R1 is taken, 41% out on persona.
- Waves follow the card (P3 = wave 2), which is stricter than the prompt default (wave 2 for referral only). This is correct, because card decisions win.

## What was wrong (specific)

### A. Adherence — 5/5
- No issues. It used exactly the two inputs, `decisions.md` is pipe-delimited with no `|` in reasons, FAIL reasons are 2-5 words plus a pool tag, and `apply-decisions` and `skipped` both ran (`people-validated.csv` and `skipped-detail.md` exist). The pools arrived in the first report together with the `promote` command, and the run stopped at the checkpoint. The pools table uses the card's R1-R4 instead of the `skipped` buckets, and line 117 explains the deviation. It is the right call.

### B. Factual accuracy — 4/5
- `decisions.md` line 73 (Dominick Garbellano): "runs the employer and plan programs whose outcomes get reported". This is stated as fact but is an inference. His history (Senior Technical PM, Certified Scrum Master) points more to internal program/delivery management than to client programs.
- `decisions.md` line 85 (Steven Keem): "owns the connected-device roadmap". The card only says Ilant "promises continuous insights from connected devices", so ownership is inferred.
- Summary line 135: "Per the card, knownwell ..., JumpstartMD ... and Enara ... do not run a phone-camera scan." The card lists the devices they use. It does not assert that they have no camera scan. Form Health and FlyteHealth (Withings scales) are also missing from the line.
- Summary line 106: the "name join" mechanism is asserted as the cause. That is plausible but not verified from the inputs.
- No invented numbers, clients or proof points. Every company figure (41/29/44 staff, 46 states, 15 clinics, 0/60) comes from the card.

### C. Brand & tone — 3/3
- No banned words. The em dashes at lines 10, 109 and 137 are headings copied verbatim from the prompt template, and the en dash at line 30 is an empty-cell marker, so none of them counts against the agent. The prose is plain and precise and every reason is defensible.

### D. Format & structure — 3/3
- Frontmatter carries `product: fitxpress`, `profile` and `status`. The sections follow the template, and the added "two identity traps" block is additive and useful. `decisions.md` matches the prescribed schema exactly.

### E. Output quality — 3/4
- **The checkpoint misses three decisions that belong to it.** The card cites "Open question 2" and "Open question 4" by number but does not carry the list, and the agent did not flag the missing list. `hypothesis.md` (Approval note, line 298) defers OQ1, OQ2, OQ5/8 and OQ9 to this checkpoint, and OQ3 is also a list decision. "Vadim — please confirm" covers OQ1, OQ2, OQ4 and OQ5 but not three others:
  - OQ3: keep the knownwell research lane (3 PASS).
  - OQ8: cap 15 vs 20 under nick's post-mortem rule. Form Health and knownwell hold 38 of 65 PASS (58%), and the agent does not mention this concentration anywhere.
  - OQ9: send lane D cold at all (5 PASS). The agent quoted the card's own "0 of 60, 22 PASS-level" evidence in `decisions.md` line 56 but did not raise it.
  The root cause is the card. The agent-attributable part is that it saw numbered references to a list it did not have and said nothing.
- Top concerns order (lines 130-135): #1 is the "Message angle" cut, which is by design and matters to the next step, not to this checkpoint. The one real pipeline defect found, `compact` grouping `IntelliHealth` into FlyteHealth against the card's URL rule without firing `other-company-page`, is #4.
- Line 134, thin P3 profiles: lists four people but not Chong Tseng (Director of Systems Operations, P3). His only earlier role is "Crossfit Coach at Crossfit One World" (`people-compact.csv` line 4), which makes him the thinnest PASS on the list.
- Line 139, Q1: bundles "65 people" with the size waiver but gives no fallback count. Without the waiver the list is 58 people across 5 accounts (Ilant 5 and CMWL 2 drop out).

## Top 3 issues (priority for improver)

1. When the card references numbered Open questions or sections it does not carry, say so explicitly in Top concerns and put the checkpoint-relevant gaps first (here, OQ3/OQ8/OQ9 were never put to Vadim). Pipeline fix outside the agent: `outbound_pack.py card --for validate` should carry the hypothesis "Open questions" section, or at least the items the Approval note defers to validate.
2. Order Top concerns by what the checkpoint decision needs. Concerns that are by-design or belong to the next step go last, and newly found pipeline defects (the name-join grouping) go first. Surface account concentration when two groups hold more than 50% of the SEND list.
3. Keep PASS reasons to what the title, headline, earlier roles and card support, and mark inferences as inferences (Garbellano, Keem). In a thin-profile concern, include every PASS whose history does not support the title (Chong Tseng).

## Coordinator review

(filled in by Claude in chat after the auto-QC run)

## coordinator_review

```
agreement: ✅ agree
top_issue: the validate card drops the hypothesis's Open questions, so OQ3/OQ8/OQ9 (research lane, cap 15 vs 20, cold engineering lane) never reached the checkpoint list; the coordinator puts them in front of Vadim directly.
```
