---
qc_date: 2026-11-05
agent: icp-validator
artifact: workspace/outbound/campaigns/2026-10-29-us-insurance-underwriting/icp-validation-summary.md; workspace/outbound/campaigns/2026-10-29-us-insurance-underwriting/decisions.md
track: outbound
artifact_type: icp-validation
product: fitxpress
profile: nick
total_score: 17/20
status: good
coordinator_review: done
---

# QC Report — icp-validator — 2026-11-05

**Artifact:** `icp-validation-summary.md` + `decisions.md` (one batch, 393 rows)
**Scored against:** `card-validate.md` and `people-compact.csv`, every row read. Limits, bans and completeness are taken from code as fact.
**Total: 17/20**, good. The counts reconcile and the three rules the coordinator asked about mostly hold. The defects:
- the "line not stated" rule is applied differently at Mutual of Omaha and The Standard;
- WEAK question 2 contradicts the agent's own pool-E reasoning;
- one new-business P1 sits outside the tiers and the summary doesn't flag it.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 4 | 5 |
| B | Factual accuracy | 4 | 5 |
| C | Brand & tone | 3 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 3 | 4 |

## What held up (checked, no action)

- **Counts reconcile exactly:**
  - Totals: 286 / 24 / 83, with P1/P2/P3 = 43/167/76.
  - All 32 group rows match.
  - The seven angles sum to 286.
  - The FAIL categories reconcile against decisions.md: 28 other line · 24 P&C · 8 left · 11 off-persona · 6 DI sales · 6 tech.
  - WEAK splits 16/3/5. The SEND table has 286 rows and the WEAK table has 24.
- **P&C staff at reinsurers is consistent.** All 18 P&C rows FAIL on title, headline or earlier-role evidence: Gen Re 6, Munich Re 9, SCOR 2, Swiss Re 1. Kevin Smith (left, P&C) is a separate FAIL. Reinsurer underwriters with no line shown are WEAK (Sirkar, Eberle, Bandele, Drabik, Sawyer). The empty-profile VPs at the life-only Hannover entity pass (Flender, Hiserote). Good catches: Demeno-Hoffman ("Automated Underwriting", commercial lines) and Bernal (FCAS, workers' comp).
- **CTO, CISO and privacy tiers are consistent across 21 companies.** All 37 sit at P3 `technical-integration`. Deputies FAIL when a chief is listed (Svalstad, Goodrich, Deporte). CIOs FAIL because the card calls them group-wide (Leechow, Watson). The only exception is Vipul Sharma, and the summary flags it (l.66).
- **Empty-profile:** none of the 48 flagged rows gets P1, and the P1-to-P2 rule is applied the same way to CUOs, CMDs and VPs.
- **Group history:** same-company group history leads to FAIL (Anderson, Workman at Lincoln). Group history at another company leads to WEAK (Pemberton, Pace). That rule is coherent.
- **Recent deals are never named.** Brighthouse, Legal & General and Hexure appear only in earlier roles, and every reason avoids them (Vigar :127, Flanagan :288, Lintecum :88, O'Donnell :239).
- **Sharp individual calls:** Cathy Bunch (PGIM real-estate lending), Tia Sullivan (headline outranks title), Warner Shue (P2 because of team-lead history), and the Munich Re domain-pull diagnosis (summary l.414).

## What was wrong (specific)

### A. Adherence — 4/5
- **Courtney Falu is P1** (decisions:256, "AVP, Life New Business, Policy Change and Jet Underwriting"). AVP is a card P2 title. Every comparable new-business seat is P2: Kenneth Byrd, "VP, Head of Protection New Business Operations" (:118), which is Protective's individual-life new-business head and a card P1 seat; Ricci, AVP Life NB (:214); McNamara (:101); Darnell (:184). The summary lists "three deviations" (l.66) and leaves her out. The prompt requires a departure to be stated in `reason`.
- **Gina Guzman (Munich Re, :332) is P1 `medical`.** The card's P1 medical seat is "at a carrier", and the reinsurer P1 list has no CMO. The comparable reinsurer CMD, Holowaty (RGA :308), is P2. Neither the summary nor the reason flags it.

### B. Factual accuracy — 4/5
- **Summary l.415:** the MoO trim keeps "those with visible life history (Ferguson, Hotham, Consolo, Dolezal)". The compact rows show no life history for three of them:
  - Hotham: Berkshire Hathaway, Unum (:217).
  - Consolo: Nationwide manager, North American Benefits (:219).
  - Dolezal: MoO consultant, HealthMarkets agent (:221).

  Only Ferguson (Lincoln underwriting, :216) is close.
- **l.68 says Ethos and Ladder are not named in the card.** Card decision 5 (l.145) names Ethos, Ladder Life and TruStage as group B.
- **l.417 says "Nationwide 7 FAIL (P&C)".** Only 6 are P&C. Mary Gray (:164) is chief of staff to the CTO of Nationwide Financial, the life and annuity side.
- **Matt Burrill (:4)**, "the research and mortality side that designs holdouts", is not in the row (:4 compact: VP & Actuary, no line).
- **Laura Hale is P2 for "no insurance history"** (:293). Malenoir is P1 (:392) with the same gap (MetaMap, PickTrace). His P1 holds under the "earlier CPO role" rule, but Hale's reason invites the comparison.
- No invented people, no product numbers.

### C. Brand & tone — 3/3
- No banned words. The only hit is the proper noun "Sales Navigator", l.12.
- Five em dashes appear in Russian prose (l.68, 407, 414-416). These are Russian copula punctuation in an internal checkpoint, not copy, so they are not scored.

### D. Format & structure — 3/3
- **Frontmatter is complete:** `product: fitxpress`, profile, campaign, created, stage, status.
- **All template sections are present.** The `|` in Sullivan's title was replaced with `/`, so no table breaks. Every WEAK row has an `angle`, and `wave` is 1 throughout.

### E. Output quality — 3/4
- **Mutual of Omaha vs the agent's own line rule.**
  - Twelve "Chief Underwriter, line not stated" pass at P3 (:216-228), and the summary itself notes MoO writes Medicare supplement, which is a card FAIL line (l.415).
  - The same "line not stated at a carrier with a big out-of-scope line" gets WEAK at Nationwide, The Standard, Swiss Re and SCOR.
  - Seven MoO reasons are word-for-word identical (:218, 222-224, 226-228), so the sequencer gets nothing to work with.
- **The Standard: the same uncertainty, three outcomes.**
  - Erdahl and Foran (VP Underwriting, line not stated) are WEAK (:273, :277).
  - Nattis (Director of Medical Underwriting, no group signal in the row) is FAIL "group" (:280).
  - Ingram and Syna (Associate MDs, "underwriting or claims role unclear") pass at P3 (:284-285). Their rows (a rheumatology professor; a neurologist and screenwriter) read like DI claims consultants, and the card does not pull claims.
- **WEAK question 2 contradicts pool E.**
  - l.425 recommends taking all 16 "line not visible" at P3 because a person from another line "may forward to a colleague".
  - That set includes 5 reinsurer underwriters, Cam Cook (LTC) and Teresa Loker (bank credit).
  - Pool E (l.407) rejects reinsurer P&C staff because "P&C and life are separate entities, you can't reach life underwriting through them".
- **Treaty:** Ospalik is FAIL "P&C treaty" (:376) and Bandele is WEAK (:362) on near-identical evidence: a treaty title, a GE reinsurance background and no line stated.
- **Name order:** "Valickus John" (Symetra, P2, :195, slug `valickus-john`) is in SEND with no note. With Nick's first-name greeting, the message will open "Valickus".
- **Promote command (l.410)** names Lynn Brown and Ashley Destito but drops Robert Reynolds, the third person recommended at l.403.
- **What holds:**
  - The concerns are specific and actionable: Munich Re has no underwriting head and needs a "Life" title re-pull, Foresters has no route-in, and the tech lane is 13% of SEND, with the duplicates to cut first named.
  - The pools carry recommendations and an angle.

## Top 3 issues (priority for improver)

1. **Mutual of Omaha.** None of the 12 rows shows a business line, and the card FAILs Medicare supplement, so apply the agent's own line rule:
   - WEAK all 12 as "line not stated (life, DI or Medicare supplement)", or state why MoO differs from Nationwide and The Standard.
   - Correct the trim list at l.415. Only Ferguson shows a life-carrier underwriting history.
   - Give the seven identical reasons a distinct hook.
2. **Split WEAK question 2:**
   - Keep the five reinsurer line-unknowns, Cook (LTC) and Loker (credit) out, consistent with pool E.
   - Offer the carrier line-unknowns at P3: Erdahl, Foran, Rahmani, Allocco, Kaczmar, Dawson, Pemberton, Pace and Clayton. Clayton's question is about function, not line.
3. **Tier and consistency drift:**
   - Courtney Falu → P2, or Byrd → P1, and list the choice among the deviations.
   - Guzman → P2, or note it as a deviation.
   - The Standard: put Ingram, Syna and Nattis on the same footing as Erdahl and Foran (WEAK).
   - Ospalik → WEAK to match Bandele.
   - Flag "Valickus John" for the sequencer (greeting = John).
   - Fix l.68, l.417 and the promote command.

## Notes outside the score
- notify.py was not run because this QC session has no shell. The coordinator should send: `QC: icp-validator → 17/20 (good) · Top issue: MoO 12 line-unknown "Chief Underwriters" PASS P3 while the same uncertainty is WEAK at Nationwide, The Standard and the reinsurers · File: workspace/_quality/outbound/2026-11-05-icp-validator-us-insurance-underwriting.md`

## Coordinator review

(filled in by Claude in chat after the automatic QC run)

## coordinator_review

agreement: ✅ agree
top_issue: the "line not stated" rule was applied unevenly: 12 Mutual of Omaha "Chief Underwriter" PASS at P3 while the same gap is WEAK at Nationwide, The Standard and the reinsurers. Coordinator check: at Symetra the individual-life chief underwriter is Mike Derrig (P1, Business Wire 2024-12-04), so "Valickus John" (same title, no line, reversed name order) is likely group/stop loss → WEAK. Fix round sent to the SAME validator with all QC points (MoO, WEAK Q2 vs pool E, Falu/Byrd, Guzman, The Standard medical directors, Ospalik/Bandele, Valickus, fact slips at summary l.68/l.417, Reynolds in promote). Verified by apply-decisions counts + re-read of the changed rows; no second QC unless SEND moves by more than ~10%.
