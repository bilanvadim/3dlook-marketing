---
qc_date: 2026-10-06
agent: icp-validator
artifact: workspace/outbound/campaigns/2026-10-06-uk-weight-management/icp-validation-summary.md; workspace/outbound/campaigns/2026-10-06-uk-weight-management/decisions.md
track: outbound
artifact_type: icp-validation
product: fitxpress
profile: katerina
total_score: 16/20
status: good
coordinator_review: done
---

# QC Report — icp-validator — 2026-10-06

**Artifact:** `workspace/outbound/campaigns/2026-10-06-uk-weight-management/icp-validation-summary.md` + `decisions.md`
**Inputs scored against:** `card-validate.md`, `people-compact.csv` (256 rows: 141 export, 115 Apollo), and the coordinator notes (scope "maximum contacts, only junk out", cap 75, juniors PASS `referral`, Apollo `empty-profile` not a reason, 5 Medicspot registry FAIL, non-UK FAIL). Limits, completeness and identity were taken as fact from the code check.
**Total: 16/20** — good (approve after minor fixes)

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 4 | 5 |
| B | Factual accuracy | 4 | 5 |
| C | Brand & tone | 3 | 3 |
| D | Format & structure | 1 | 3 |
| E | Output quality | 4 | 4 |

E is 4, not 3: the decisions hold up row by row, and the summary finds things nobody asked it to find (see E).

## What was wrong (specific)

### A. Adherence — 4/5
- **debi johnson** (decisions line 38) is WEAK, but her row has a "Happily retired at Debi is now retired" position. The card's stop condition says "a profile shows the person has left (drop)", and standing decision 4 makes people who left a FAIL. WEAK sends back to Vadim a call the card already made.
- **The lane-by-title rule for Apollo additions is not applied literally, and the summary does not say so.** The card gives "commercial, finance and anyone below lead level → `referral`". Grace Shiplee (Senior Contract Manager) and Victoria Simpson (NHSE Digital Contract Manager & Reporting Strategy Coordinator) went to P2 `operations` (lines 144, 147). Sonel Patel (Head of Programme Online) went to `product`, while the rule says "programmes leads → `operations`" (line 217). All three calls can be defended: the card's KPI for NHS providers is commissioner reporting, and LighterLife's head-office ask is a product ask. The deviation should still have been stated.
- Everything else follows the card and the coordinator notes. The 15 export FAILs are exactly the card's fail-by-name list. Every card identity check is resolved: Kate Sykes, David Wong, Anthony Hardley and LighterLife Admin are held, and Sandra, Georgia Miller, Richard Ruff, Sahira Dar and Bhavini Shah are PASS. Apollo `empty-profile` rows are PASS. The 5 Medicspot registry FAILs keep the registry wording. All 35 non-UK rows are FAIL, and Edna Moneypenny (Belfast) is correctly kept as UK. Pools come with a promote command.

### B. Factual accuracy — 4/5
- Pool rationale (summary line 255): "they deliver the UK programme from Cape Town" is an inference from the job titles, but it is written as fact. It is also the argument for an exception to Vadim's approval §3. Neither input says this.
- Every count was re-derived from `decisions.md` and `people-compact.csv`, and all of them hold. PASS 203 = P1 17 + P2 25 + P3 161. FAIL 44 = 5 registry + 35 non-UK + 3 duplicates + 1 register. The group totals hold (LighterLife 68, MoreLife 57, Reset Health 43, Counterweight 11, Habitual 6), and so do the angles (148/15/14/13/7/6). Apollo arrivals per group are 30/24/27/18/10/6, and so are the "23 export `empty-profile` LighterLife PASS".
- The two duplicates the card missed are real: Debbie Shearing and Deborah Evans share the slug hash `27a2bb1a1` and their earlier roles, and Anne Tinto is a second slug for Anne-Marie Tinto. There are no invented clients or proof-point numbers. This is an internal artifact.

### C. Brand & tone — 3/3
- No issues. Internal artifact, no banned words. The em dashes in headings come from the template.

### D. Format & structure — 1/3
- `icp-validation-summary.md` has no frontmatter, so `product:` is missing. Under the hard rule, D cannot go above 1. This is the second run in a row: the 10-05 QC flagged the same thing, and its coordinator review asked for frontmatter on the summary. The author prompt's template still has none, so the fix belongs in the prompt, not only in this run.
- The sections match the template. `decisions.md` follows the `|` schema, and FAIL reasons are 2-5 words.

### E. Output quality — 4/4
- One line runs through every row, and it is defensible. Rows the card names as IN are PASS. Rows where the card opens a check the agent cannot close from the compact, or where the row shows a competitor, a move abroad or a later employer, are WEAK. Examples: Emma Walker (Cambridge Weight Plan), Emily Macleod (moving to the Netherlands), Samantha Oon (HeliosX listed before Habitual). Richard Ruff passes on the Everyone Health → Healthy You link, which is consistent with Beverley Ambler's row. Unlike 10-05, the same evidence does not get opposite decisions.
- The summary goes beyond the template. It names the Apollo arrival shortfall against the card (LighterLife 30 vs 32, PronoKal UK 0 rows), the gap in the `apply-decisions` printout (12 of 17 groups), the risk that Medicspot coaches moved with the weight-loss business, and the children's-copy rule for 4 MoreLife practitioners. Pools separate the rule-change asks (South Africa 11, Malaysia 6) from the closed ones.
- Small misses that do not cost a point:
  - Abimbola Loye (midwife, line 138) is PASS `referral` with no note for the sequencer. The card's anti-case covers pregnancy as well as children, and only children were flagged.
  - Summary line 269 says the agent "held only the rows where the compact itself conflicts". The decisions do not match that wording: Kate Sykes is held on Vadim's current-role condition, not on a conflict in her row.

## Top 3 issues (приоритет для improver)

1. **Summary has no frontmatter (`product: fitxpress`, `profile: katerina`).** This is the second run in a row after the 10-05 QC. Add the frontmatter to the template in `.claude/agents/outbound/icp-validator.md`, so the fix does not depend on the coordinator.
2. **"Has left" evidence is sent to WEAK instead of FAIL.** debi johnson's "is now retired" row meets the card's stop condition and standing decision 4. Apollo lane-rule deviations (Shiplee, Simpson, Patel) need a one-line note in the summary.
3. **Inferences are written as fact, and an anti-case note is missing.** "Counterweight delivers the UK programme from Cape Town" is used to argue for a rule exception. The midwife row has no pregnancy-context note for the sequencer.

## Coordinator review

(заполняется Claude в чате после автозапуска QC)

## coordinator_review

```
agreement: ✅ agree
top_issue: debi johnson (profile says retired) sat in WEAK instead of FAIL, and three Apollo rows took lanes that differ from the card's lane-by-title rule without a note; fixes 1-5 sent back to the same icp-validator (resumed, small context). The missing frontmatter is a template gap in the DEV source of icp-validator.md, raised with Vadim, not patched in the .claude copy.
```
