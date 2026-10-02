---
qc_date: 2026-10-02
agent: icp-validator
artifact: workspace/outbound/campaigns/2026-10-02-us-virta-health/icp-validation-summary.md + decisions.md
track: outbound
artifact_type: icp-validation
total_score: 18/20
status: excellent
coordinator_review: done
---

# QC Report — icp-validator — 2026-10-02

**Artifact:** `workspace/outbound/campaigns/2026-10-02-us-virta-health/icp-validation-summary.md`, `decisions.md`
**Scored against:** `card-validate.md`, `people-compact.csv` plus the coordinator brief. Limits, completeness and identity were already verified by code (38/38, 37 PASS, 1 FAIL). The displacement re-check and the stale `--wave 2` hint were excluded from scoring, as the brief asked.
**Total: 18/20** (excellent)

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 5 | 5 |
| B | Factual accuracy | 4 | 5 |
| C | Brand & tone | 3 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence — 5/5
- No issues. Every coordinator instruction is met:
  - Julia Julia is FAIL as an identity collision. Her compact row (title "Founder & Director of Probiotic Research", headline "Head of Product R&D", no earlier roles) shows no Virta role.
  - Tara Conboy is P4 `referral`.
  - All 37 tiers and lanes match card lines 51-76 one to one (P1 6, P2 8, P3 2, P4 21), and the P4 order follows the card.
  - `wave` = 1 on every row.
  - FAIL is used only for the collision.
- Open questions are carried with their text. Q1 has its number. For Julia and Tara the agent states that `card-validate.md` gives no number. That is true: the card omits the hypothesis section "Open questions for Vadim" (these are Q2 and Q3 in `hypothesis.md` lines 333-334). The agent reported the gap and did not read the source, which is what its prompt requires.

### B. Factual accuracy — 4/5
- No proof-point numbers, client names or product claims appear. The product is fitxpress. The arithmetic checks out (37+1+2=40; 21/37=57%; cap 37/50).
- Summary line 108 misquotes the card. It says Kristin Bergethon was "ex-CMO at Physician Housecalls and Novocardia". Card line 56 says "ex-CMO at Physician Housecalls, Director of Product and Strategy at Novocardia". The error is in the very concern that warns about employer facts.
- Summary line 94: "Virta runs no probiotic research (card)" overstates the card. Card line 29 only says "nothing on Virta's site or research page mentions probiotic research".

### C. Brand & tone — 3/3
- This is an internal report with no banned words. The only em dashes are in the headings the prompt template prescribes.
- One non-scoring note: in "Vadim — please confirm", items 1-4 are in Russian and items 5-8 in English (lines 115-122).

### D. Format & structure — 3/3
- The frontmatter has `product: fitxpress`, the campaign and the profile.
- All template sections are present. The added FAIL table is useful.
- `decisions.md` matches the pipe format, with no `|` inside any reason. The FAIL reason is 5 words.

### E. Output quality — 3/4
- The judgment and persona fit are correct, and the list is ready for the checkpoint.
- Three top concerns add real value:
  - 57% of the list is in the referral lane, and no owner sits above the directors (tied to Q1).
  - The empty `flags` cell missed the collision.
  - Adriana Lindsey's tier rests on her bio.
- The former-employer check is incomplete. Decision 5 allows naming former employers in copy, so this is the one place a card fact reaches a prospect. The agent flagged only Liza Fryberger and Kristin Bergethon. It missed four more:
  - Shaila Chhibba: card line 67 says "payor contracting at HealthCare Partners". Compact line 21 does not show it.
  - Melissa Rondi: card line 57 says Deloitte. Compact line 28 does not show it.
  - Tara Conboy: card line 72 says Castlight and Limeade. Compact line 14 shows only Skedulo.
  - Adam Wolfberg: card line 55 says "ex-CMO at ... Ovia Health". Compact line 12 says "Physician-in-Chief at Ovia Health". This is a title mismatch, and the proposed rule ("name only an employer it can see on the row") does not catch it.
- `decisions.md` breaks the summary's own rule. Line 6 (Novocardia) and line 25 (Castlight, Limeade) cite card-only employers in `reason`, and that column is copied into `people-validated.csv`.

## Top 3 issues (priority for improver)

1. **The former-employer check is partial and contradicts itself.** It covers 2 of the 6 rows where card and row differ. It misses Adam Wolfberg's title mismatch at Ovia. And the reasons in `decisions.md` for kristin-bergethon and taraconboy, which carry into `people-validated.csv`, name card-only employers that the summary tells message-sequencer not to name.
2. **Two source misquotes in the summary:** Kristin's Novocardia role (line 108) and "runs no probiotic research" (line 94).
3. **Language switch** inside the confirm block (RU items 1-4, EN items 5-8).

**Pipeline note (not scored against the agent):** `outbound_pack.py card --for validate` dropped two parts of the hypothesis, "Open questions for Vadim" (Q1-Q3) and the "Identity and job-change checks, by name" list (`hypothesis.md` line 299: Holly Anderson, Taylor P., Rad Thie, Adriana Lindsey, Patrick Tumpane's two Virta stints). The validator never saw them. Before the checkpoint, the coordinator should renumber summary items 6 and 7 as hypothesis Q2 and Q3.

## Coordinator review

(filled in by Claude in chat after the auto-QC run)

## coordinator_review

```
agreement: ✅ agree
top_issue: card-only former employers (6 people, one wrong title) would have reached message copy; the hypothesis is being reconciled against the export rows before messages, the validator fixes its reasons and numbering, and the validate card now carries "Open questions" (outbound_pack.py CARD_SECTIONS).
```
