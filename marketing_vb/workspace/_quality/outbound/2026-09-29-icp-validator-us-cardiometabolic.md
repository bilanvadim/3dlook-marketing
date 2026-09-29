---
qc_date: 2026-09-29
agent: icp-validator
artifact: workspace/outbound/campaigns/2026-09-29-us-cardiometabolic/icp-validation-summary.md + decisions.md
track: outbound
artifact_type: icp-validation
total_score: 18/20
status: excellent
coordinator_review: done
---

# QC Report — icp-validator — 2026-09-29

**Artifact:** `workspace/outbound/campaigns/2026-09-29-us-cardiometabolic/icp-validation-summary.md`, `decisions.md`
**Scored against:** `card-validate.md` + `people-compact.csv` only (the agent's inputs). Counts and identity columns are taken as fact from the code checks. Not marked down, per the coordinator: the registry company-field concern (fixed in `build-import`), the displacement web re-check and the job-change checks (no web access).
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

- **Persona fit is exact.** All 71 PASS match the card's named persona, with the same tier and lane for each person: 9amHealth 32 (6/4/2/20), Superpower 23 (4/3/10/6), Level2 16. The only four people the card had in the send list who are not PASS are all Level2, and each one is WEAK for a stated reason. Perry is held because the card's own identity condition (card line 50) was not met. Conlin, Tinsley and Jasper carry `empty-profile`, and the prompt forbids PASS for that flag without a second confirmation.
- **The coordinator's instructions were followed.** Signos is 20 WEAK with the card's preset tiers and lanes, all 20 checked against card line 112. edgar tudela and the `a68474427` Reilly duplicate are FAIL, and those are the only two FAILs. Everyone is wave 1. Sláva Lukianchuk (`geo:olena`) stays on nick, per card line 85.
- **Every figure in the summary recounts correctly** from `decisions.md`: P 13/11/17/30, angles 31/14/12/9/5, 21 of 32 at 9amHealth are referral, and 75 in the card minus 4 gives 71. The pools table matches `skipped-detail.md`.
- **The facts in PASS reasons check out against the compact rows:** ex-mySugr/Roche, ex-Livongo, ex-Humana, ex-Allscripts, ex-Headspace, ex-a16z, ex-UCLH, and "Open to Opportunities" for Michelle N. Jones. None of them is invented.

## What was wrong (specific)

### A. Adherence — 5/5
- No issues. The agent read only the two inputs. `decisions.md` follows the pipe schema with no `|` inside reasons, and both `apply-decisions` and `skipped` ran. The pools and `promote` commands are in the first report. The run stopped at the checkpoint. P4 goes beyond the prompt's "1-3", but that is the card's tier scheme, and the card wins.

### B. Factual accuracy — 4/5
- **Rabcuka's row contradicts the card, and nobody flagged it.** Summary line 69 lists her as "Lead Scientist and Clinical Strategy", which is the card's text. Her compact row (line 69) gives the current title as **"Chief Business Development Officer"** on the Oxford company page, and only the headline names Superpower. Top concern line 152 raises this pattern for Malkin, Chua and Clayton, all of whom are referrals. It does not raise it for Rabcuka, who is P2 `clinical` and so gets the full pitch with the compliance line. `people-validated.csv` still carries the CBDO title for message-sequencer to read.
- The Title column in the SEND table mixes export titles with titles from the card and does not say which is which. Card titles are used for Malkin ("Medical Advisor" vs row "Co-Founder"), Chua ("Telemedicine Physician" vs "Founder & CEO / Physician") and Clayton (vs "Sub-Investigator"). The "(export: X)" tag only partly signals this.
- Some inferences are written as facts. At `decisions.md` line 48, Agoro "owns clinical protocol, including what is measured around GLP-1 prescribing", yet her positions column shows "Medical Director at Encompass Health". That is the same concurrent-role caveat the agent itself applied to Chua and Clayton at line 152. Also, summary line 145 gives the "name join" as the cause of edgar's grouping, which is plausible but not verified.

### C. Brand & tone — 3/3
- No banned words. The em dashes at lines 9, 103 and 157 are headings copied from the prompt template. The prose is plain, and every reason would hold up if Vadim asked "why is he here".

### D. Format & structure — 3/3
- The frontmatter has `product: fitxpress`, `profile`, `step` and `date`. There is no `status:`, but the prompt template does not ask for one. The sections follow the template. The added FAIL section and Wave column are extras and do no harm. `decisions.md` matches the schema exactly.

### E. Output quality — 3/4
- **The promote block (lines 125-139) does not do what the summary says it does.** Line 111 says "Tiers and lanes are preset from the card", and line 161 says "no new round needed". The facts are different:
  - `apply-decisions` wrote an empty `priority` for every WEAK row (`people-validated.csv` lines 12, 28, 88, 95).
  - `promote` falls back to priority `"3"` when no `--priority` is passed (`outbound_pack.py:1269`). As written, every one of the 24 promoted people would land at P3. That includes the Signos CEO, the VP Product, Level2's CEO and all P4 referrals.
  - The agent split Signos "one call per lane". It also needed one call per lane and tier: 7 calls in all.
  - `promote` refuses `empty-profile` without `--force` (`outbound_pack.py:1248-1253`), so the Conlin and Jasper commands fail. The command that bundles Perry with Tinsley fails whole, and Perry, who has no flags, goes down with it.
  - The coordinator notes that Vadim takes every pool, so this is the path that will actually run.
- **OQ3 was not asked.** The top-up pull was raised as a concern (line 153) but is missing from "Vadim — please confirm". The hypothesis Approval note keeps Signos, Reilly, the top-up pull and the page defects for Vadim at step 4. The card cites OQ1 and OQ3 by number but does not carry the list, and the agent did not say it was missing. The previous run's QC (`2026-09-29-icp-validator-us-obesity-medicine.md`) flagged the same gap.

## Top 3 issues (priority for improver)

1. The `promote` commands have to be runnable and keep the tiers. Pass `--priority` from the card (one call per lane and tier), add `--force` for rows flagged `empty-profile`, and never bundle an unflagged person with a flagged one. Pipeline fix outside the agent: `apply-decisions` should keep `priority` on WEAK rows so that `promote` can inherit it.
2. When the card cites numbered Open questions it does not carry, say so, and put every one of them that belongs to this checkpoint in the confirm list (here, OQ3, the top-up pull). This is a repeat from the previous run's QC.
3. Apply the "rests on the card, not on the row" check to every re-grouped person, not just the referrals. Rabcuka (P2 clinical, row title CBDO) needs it most. Mark SEND-table titles that come from the card, and mark concurrent-role inferences (Agoro) as inferences.

## Coordinator review

(filled in by Claude in chat after the auto-QC run)

## coordinator_review

```
agreement: ✅ agree
top_issue: the summary's ready-made promote commands would drop every WEAK to P3 and fail on empty profiles; the coordinator promotes from decisions.md priorities with --force where needed once Vadim decides, and puts OQ3 and the Rabcuka title conflict in front of him directly.
```
