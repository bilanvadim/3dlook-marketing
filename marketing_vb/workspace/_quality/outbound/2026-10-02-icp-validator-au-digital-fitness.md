---
qc_date: 2026-10-02
agent: icp-validator
artifact: workspace/outbound/campaigns/2026-08-14-au-digital-fitness/icp-validation-summary.md + decisions.md
track: outbound
artifact_type: icp-validation
total_score: 17/20
status: good
coordinator_review: done
---

# QC Report — icp-validator — 2026-10-02

**Artifact:** `workspace/outbound/campaigns/2026-08-14-au-digital-fitness/icp-validation-summary.md`, `decisions.md`
**Scored against:** `card-validate.md`, `people-compact.csv` (151 rows) and the coordinator brief. Code has already verified completeness (151 in, 151 decisions; 125 PASS / 16 WEAK / 10 FAIL), so those counts are not re-scored. Cap 50, no waves, a lane for every function and the FAIL-only-for-wrong-company rule are treated as givens.
**Total: 17/20** (good)

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 4 | 5 |
| B | Factual accuracy | 4 | 5 |
| C | Brand & tone | 3 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence — 4/5
- Every step of the prompt cycle is done. The decisions file, the summary, the WEAK table, the pools, the top concerns and the confirm block are all present. The AIA ranking follows the card instruction to rank by fit to AIA Vitality and the wellbeing-program-owner persona.
- Card line 203 says "the validator ranks the 60". 57 people are ranked and 2 are FAIL, but Gerald John (decisions line 87) has no rank. Summary line 197 still says he sits "below the cap line". That contradicts the agent's own ranking: P3 technical-integration people are at #24 (Marie Huong) and #37 (David O'Driscoll), so a verified CTO would rank above the P4 referrals at #38-50.
- Trivial: the pools table lists every pool, including non-senior ones (line 220). The prompt asks for pools with senior roles only.

### B. Factual accuracy — 4/5
- About 30 reasons were spot-checked against the compact rows. The prior roles, headlines and locations are quoted correctly (Tristan Oam, Jo Moon, Aakash Malhotra, Mark Broom, Peter Kelly, Victor Garcia via Natural Therapy Pages, and others). No proof-point numbers or client names appear.
- The arithmetic reconciles. Group totals match the compact file. Lanes add up to 125 (P1 48 = 24+14+8+2; P2 39 = 19+6+7+7). Geo flags split 14 = 8 PASS / 4 WEAK / 2 FAIL.
- Two reasons claim more than the row shows. Both are copied into `people-validated.csv` and so can reach message-sequencer:
  - decisions line 132, Ryan Ansell, "owns ... the FUELLED app". The row (compact 132) shows only Head of Brand & Marketing, ex Marketing Manager. Nothing ties him to FUELLED.
  - decisions line 44, A/Prof Harris, "medical voice on the Vitality health check". The row (compact 31) shows no AIA role and no Vitality link, only Griffith University and a pain-physician post on the Gold Coast.

### C. Brand & tone — 3/3
- No banned words in either file. `decisions.md`, which feeds copy, has no dashes.
- Non-scoring: the em dashes in the summary are Russian grammatical dashes and template headings in an internal report. The body is in Russian, but "Vadim — please confirm" (line 250 onward) switches to Ukrainian. This is the same kind of language switch noted in the Virta report.

### D. Format & structure — 3/3
- The frontmatter has `product: fitxpress`, the campaign, the profile and the step.
- `decisions.md` uses the pipe format with no `|` inside reasons, and every FAIL reason is 2-5 words.
- WEAK rows carry a tier, which the prompt reserves for PASS. Line 186 explains why, and it helps any later promote.

### E. Output quality — 3/4
**What holds:**
- All 10 FAILs are sound:
  - Ballard and Gallagher have explicit "open to / exploring opportunities" signals.
  - The other 8 are clear collisions: a Philadelphia gym page, KIC Holdings, Gujarat, Mongolia, a Brazilian FitStop and three non-Sonder people in India and the Philippines.
- The AIA top 7 are exactly the Vitality and AIA Health owners. The top-15 line is drawn, broken down by lane, and tied to Open question 7.
- The agent flagged its own judgment calls (Steven Lu, Stephanie Phillips, Riley Woodcock, Pete Hull, the empty-profile passes).

**Where the judgment slips:**
- **AIA lane tags contradict the agent's own reasons.**
  - Eight people are tagged `product` although their reason is a referral reason ("insurance product, can route to Vitality"):
    - Penny Sheppard (P1, line 52)
    - Raymond Cheng (54), Cate Menzies (55), Sheraden Bulsing (61), Simon Layne (62), Nicky Serret (63), Aakash Malhotra (64, actuarial) and Jo Moon (65, ex claims), all P2
  - Kim Clough (60) and Chris Freeman (77) run life product and pricing and went to `referral` with "risk side, never underwriting". Group and life policy product managers sit on that same risk side.
  - Following the lane table literally ("product managers → product") overrides the card's AIA row ("Wellness and engagement only, never underwriting"). It also means message-sequencer will send API/SDK build-versus-buy copy to life-insurance PMs. Chris Healey (line 49, Chief Executive Group Insurance, P1 product) is borderline for the same reason.
- **The left-company test is applied unevenly.**
  - Erica Graham is WEAK (line 122) because her headline names her own business.
  - Giorgia Iacono is PASS P2 (line 121), though her headline ("Owner of Market Me By G and Makeup At Gigi") and both earlier roles are her own businesses. Kitty Robinson, whose Fernwood history is confirmed, holds the same title (compact 123), and Giorgia's person_id carries a different surname (`giorgia-tigani`).
  - Holly Brazier (line 27) shows the weaker version of the same pattern: her headline is "Founder @PadelWithHolly" and does not mention Hapana.
- **The collision test is applied unevenly.**
  - Carlos Sumner and Neel Parekh are FAIL on: empty profile, foreign location, a title that conflicts with the card.
  - The same pattern lands in WEAK at P1 for Carole King (106) and Audrey Gutfreund (103). The agent itself says "probably another KIC" about them.
  - Gabor Steinbacher (116) is the same case: his whole record is a Hungarian gym chain, with nothing linking him to Springday.
  - Result: Vadim gets three near-certain collisions to decide, labelled P1.
- **Pete Hull is PASS P1 (line 126) on an empty US stub with no roles.** The flag rule asks for a second confirmation. A name match is weak confirmation when the card places the founder-CEO in Brisbane, and the card makes duplicate profiles a FAIL. This uses up the Fitstop CEO slot without a check.
- **The top-15 cut line.** A/Prof Harris (#15) is an insurer CMO, which is the medical risk side, and his record has no AIA role. He sits inside the line, while Peter Kelly (#16) sits outside it. Kelly's record shows ex Head of Member Engagement and ex Head of Digital Propositions, the closest match to the engagement persona in ranks 16-50.
- **Minor gap in thin coverage.** Top concerns (line 245) notes that VALD and Springday have no partnerships owner. It does not say the same for Hapana, which the persona lists first for that role.
- **Is the 125-person PASS list defensible as a referral-heavy list?** Yes, under standing decision 3: P4 is 32 of 125 (26%). Adding the 8 mis-laned AIA product rows, the honest referral motion covers 40 people (32%), 24 of them at AIA. Sonder, the weakest-fit company on the card, is the second-largest group (12, of whom 5 are referral). The summary does not raise this as a portfolio concern.

## Decisions I would reverse
- Penny Sheppard, Raymond Cheng, Cate Menzies, Sheraden Bulsing, Simon Layne, Nicky Serret, Aakash Malhotra, Jo Moon: `product` → `referral` P4 (AIA rank unchanged).
- Giorgia Iacono: PASS → WEAK, the same test as Erica Graham.
- Pete Hull: PASS → WEAK, to verify the profile URL before the Fitstop CEO slot is used.
- Top-15 line: swap A/Prof Harris (#15) and Peter Kelly (#16).
- Lower stakes: Gabor Steinbacher, Carole King and Audrey Gutfreund WEAK → FAIL (collision).

## Top 3 issues (priority for improver)

1. **At AIA, the lane table overrides the card's company constraint.** Eight insurance-policy product people are tagged `product` with "can route" reasons, against the agent's own pricing → referral rule. The prompt needs a rule: when the reason is a routing reason, the lane is `referral`.
2. **The FAIL/WEAK thresholds for identity and job change are not applied evenly across rows.** Compare Erica Graham with Giorgia Iacono, Carlos Sumner with Carole King, Audrey Gutfreund and Gabor Steinbacher, and Pete Hull with any empty foreign stub. The prompt should state one test for each signal and apply it to every row.
3. **Reasons assert facts that the row does not show** (Ryan Ansell and FUELLED, Harris and the Vitality health check), and the top-15 cut line places a risk-side CMO above the strongest engagement profile in ranks 16-50.

## Coordinator review

(filled in by Claude in chat after the auto-QC run)

## coordinator_review

```
agreement: ✅ agree
top_issue: 8 AIA insurance-product people were laned `product` and would have received build-versus-buy copy; sent back with the PASS/WEAK/FAIL corrections before Vadim's checkpoint.
```
