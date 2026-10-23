---
qc_date: 2026-10-23
agent: icp-validator
artifact: workspace/outbound/campaigns/2026-10-22-uk-insurance-underwriting/icp-validation-summary.md; workspace/outbound/campaigns/2026-10-22-uk-insurance-underwriting/decisions.md
track: outbound
artifact_type: icp-validation
product: fitxpress
profile: katerina
total_score: 15/20
status: good
coordinator_review: done
---

# QC Report — icp-validator — 2026-10-23

**Artifact:** `icp-validation-summary.md` + `decisions.md` (five batches merged, 1,283 rows)
**Scored against:** `card-validate.md` and `people-compact.csv`, sampled per group: all 148 PASS, all 130 WEAK, every FAIL whose reason names protection, underwriting, life, medical or a chief title. Limits, bans and completeness are taken from code as fact.
**Total: 15/20**, good, at the low edge. The counts all reconcile and most reasons hold up against the compact rows. The defects:
- the five batches apply different standards to the same titles;
- two rules not in the card cut core-lane people;
- the summary names none of the 91 people in the Apollo gap batch.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 3 | 5 |
| B | Factual accuracy | 4 | 5 |
| C | Brand & tone | 3 | 3 |
| D | Format & structure | 2 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence — 3/5
- **Underwriting team managers FAIL, even though the card tiers them.** Card l.33 puts "underwriting managers" at P3, and the `underwriting` lane (l.34) includes them. Standing decision 4 (l.97) allows FAIL only for wrong company, left, collision, duplicate, out-of-line or out-of-UK. Yet in the title top-up batch:
  - Lara Harkins (decisions l.1258, Underwriting Team Manager at The Exeter, a protection-only insurer, L&D underwriter career) is FAIL.
  - Bethan Shepherd (l.1215, Medical UW Team Manager at L&G, ex senior medical underwriter) is FAIL.
  - Brian Kemp (l.1202) and Scott Wallace / Nicky McRae (l.1208, l.1210) are FAIL.
  - The gap batch PASSes Jane Tarbuck (l.1088) with the same title type at P3. None of these FAILs is offered as a pool.
- **An invented "depth" sub-cap.** Nine people with card P2 titles (development underwriters, rules developers), all protection-confirmed, are WEAK only because "the team is already covered":
  - Arbuckle, Lyle, Bowden (Royal London);
  - Young, Green (Scottish Widows);
  - Phillips (L&G);
  - Sims (Pacific Life Re);
  - Martin (UnderwriteMe);
  - Lawson (Aviva innovation).

  This is summary l.125–151. The only limit in the card is `cap_per_group: 50` (l.76). Royal London sits at 15.
- **FAILs inside protection.** "protection marketing head" (Stephanie Richards, l.1242) and "protection governance and assurance" (Kelly Mhasal, l.1181) are FAIL. Standing decision 3 gives every function inside protection a lane, so these should be WEAK or a pool.
- **Decision 2 (card l.113) is not flagged.** Pravina Ladva (l.1101) is Swiss Re's Group Chief Digital and Technology Officer, an executive of the parent left open for Olena. She is PASS P3 from katerina with no note. The RGA global philosophy heads (Emma Jones l.1124, Rebecca Abayakoon l.1125) need the same flag for Nick.
- **Followed correctly:** the anti-cases, which were applied cleanly:
  - group risk (Yash Gupta, Chloe Carter);
  - PMI (Aviva Health, VitalityHealth);
  - GI at Aviva, Zurich and LV=;
  - equity release and Retail Retirement (Megan Davies, Paul Murchan);
  - Ireland (Stuart Crichton WEAK);
  - claims kept out under OQ4.

### B. Factual accuracy — 4/5
- **The counts reconcile.**
  - Totals: 148 / 130 / 1005 = 1,283.
  - Per batch: 12+7+26+54+49 PASS, 19+17+27+37+30 WEAK, 418+274+206+44+63 FAIL.
  - Per group, for example Aviva 20/24/453 and Royal London 15/15/109.
  - Angles: 46+35+23+18+15+8+3. The 63 title-top-up FAILs add up across the reason list.
- **The reasons match the compact rows.** Checked: Doran (ex PLRe Global Chief Underwriter), Mapplebeck (Magnum, SS/G, UwMe), Daniel Smith (headline still Aviva), Grace Flowers (Zurich GI CUO), Megan Davies (equity release).
- **l.48 overstates.** It says "underwriting owners … missing at all 12 companies", but the Aviva Sales Nav slice held Sue Hendry, "Head of Protection UW/Claims" (l.286), as the batch's own note says (l.281).
- **Deborah Smith (l.1095) is PASS P1 `medical`.** Her only history is acute medicine and CT2 neurology, both trainee-grade. The summary itself lists her under "CMO titles to eyeball" (l.59). Her title is borderline, which by the prompt's own rule makes her WEAK; Harpreet Sarna was handled that way.
- **Toby Bainbridge is P1 (l.221)** on the title "Head of Insurance Solutions". That is not a card P1 title, and the P1 rests on his history, so P2 is safer.
- **Royal London × LV= (l.57) is settled on two searches.** QC cannot verify it either way. If a 2025–26 combination exists, LV= (5 PASS) falls under the recent-acquisition rule, so it needs one confirmation before import.
- No product numbers and no client names appear.

### C. Brand & tone — 3/3
- No issues. The reasons are plain and specific, and the em dashes appear only in template headings.

### D. Format & structure — 2/3
- The frontmatter is complete: `product: fitxpress`, `profile: katerina`, `campaign`, `created`, `stage`, `status`.
- **The Apollo gap batch has no SEND or WEAK table (l.157–181).** Its 54 PASS and 37 WEAK appear by name only in `decisions.md`. Several of the WEAKs carry P1 titles: Louise Colley (Protection Director), Grace Flowers (CUO), Marszalek and Yarham (Directors of Pricing and Underwriting), and Pete Sanderson (Head of Ops, Retail Protection).
- **There is no "Vadim — please confirm" section.** The only questions are the gap validator's three (l.177).
- **Pools are missing for two batches.** The title top-up has none, and the gap batch has a one-line count with no names (l.181).
- **The blank line at l.102 breaks the title top-up SEND table.** Fifteen rows, Stronach through Miller, will not render as a table.
- **Gap-batch WEAK rows have an empty `angle`** (decisions l.1008–1094), while every other batch fills it. Any promote of them needs a manual `--angle`.

### E. Output quality — 3/4
- **The batches apply different standards, so Vadim has to reconcile them himself:**
  - **Unscoped transformation heads:** pooled at Aviva (l.329) and L&G (l.379), but PASS at Royal London (Amy Higgs l.752: no group scope shown, UK Distribution background).
  - **Architecture:** PASS at Aviva (Lister), pooled at Royal London and L&G with "give architecture a tier" (l.265, l.381).
  - **Underwriting team managers:** see A.
- **The depth logic runs the wrong way.** The core `underwriting` lane is trimmed "for depth". Meanwhile Aviva alone sends 8 group innovation and transformation contacts at P3 `referral`: Belezina, Hannani, Spiro, Manstoff, Hayer, Devi, Welsh and Granville-Jones.
- **Step-5 skeleton risk.** These reasons are near-verbatim "a group-wide … lead the card places at P3 referral": Belezina l.29, Hannani l.131, Devi l.146, Manstoff l.153, Hayer l.240. Sohal (l.858) and Halász (l.960) have identical reasons. A reason that says "per the card" gives the sequencer no hook.
- **What holds:**
  - The main finding (l.46–48) is the most useful line in the file. The Sales Nav export was pulled by company, which the card forbids (l.39), and the two Apollo title pulls rescued the underwriting and medical lanes.
  - The data issues are sharp: the `compact` comma bug was fixed with a commit, the Wynn slug duplicate and the Robert Morrison ×2 identity check were caught, and so were the mixed company pages (LV= GI, Direct Line, VitalityHealth, Great Lakes, Faraday).
  - The judgment on GI vs protection, and on Vitality life vs health, is careful throughout. Pool A1 (single-line mutual executives) comes with a clear recommendation.

## Top 3 issues (приоритет для improver)

1. **Restore the card-tiered people cut by rules the card does not have.**
   - The 6 underwriting team managers FAILed in the title top-up (Harkins, Shepherd, Kemp, Wallace, McRae, Samuel) need PASS P3 or WEAK.
   - The 9 "depth" WEAKs should be PASS P2.
   - Mhasal and Richards should be WEAK or pooled.
   - Prompt fix for the improver: "team already covered" is not a WEAK reason, and the cap is the only limit.
2. **Make the summary a usable checkpoint.**
   - Add the gap batch's SEND (54) and WEAK (37) tables, plus a single "Vadim — please confirm" list (SEND N, WEAK, pools, holds).
   - Fix the broken table at l.102.
   - Fill `angle` on the gap WEAKs.
3. **Hold or flag the decision-2 and borderline PASSes.**
   - Pravina Ladva (Swiss Re Group, Olena's parent) should be WEAK or held.
   - The RGA global heads need a flag for Nick.
   - Deborah Smith should be WEAK until her CMO role is confirmed.
   - Confirm Royal London × LV= before import.
   - Give each of the five Aviva referral reasons and the two PLRe R&D reasons a distinct hook before step 5.

## Notes outside the score
- **notify.py was not run.** This QC session has no shell tool, so the coordinator has to send the Telegram notice.
- The batch inconsistency is a pipeline effect of running five parallel validators with no shared rulings. A short "rulings so far" block passed to later batches, or a reconciliation pass by the coordinator, would prevent it.

## Coordinator review

```
agreement: ✅ agree
top_issue: rules the card does not have (team managers FAIL, "team already covered" WEAK) cut card-tiered underwriting people; fixed by a round with the same validators
```

Applied 2026-10-23, verified by script, not by a second QC:
- Title top-up batch: team managers judged on business line only (5 FAIL → PASS P3, 2 → WEAK), coverage argument dropped (8 WEAK → PASS P2), protection-side functions FAIL → WEAK; the agent applied the same rules to 12 more rows outside the list, kept. Reasons de-duplicated per company.
- Apollo gap batch: Deborah Smith PASS P1 → WEAK, Pravina Ladva PASS P3 → WEAK (Swiss Re parent, decision 2), RGA global philosophy heads keep PASS with the decision-2 flag, every WEAK has an angle.
- Summary: gap and top-up sections rebuilt from the decision files (SEND and WEAK tables complete, no broken table), "Vadim — please confirm" section added, the "missing at all 12" line corrected (Sue Hendry).
- Result: PASS 148 → 160, WEAK 130 → 136, FAIL 1,005 → 987.
- Not done: the near-identical Aviva referral reasons and Sohal/Halász in the Sales Nav batches stay as they are; the messages step builds a per-person grid, so they are handled there. Royal London × LV= stays a confirm item for Vadim.
- Agree with the process note: parallel validators need a shared "rulings so far" block; recorded for the next big list.
