---
qc_date: 2026-11-02
agent: icp-validator
artifact: workspace/outbound/campaigns/2026-10-29-eu-insurance-underwriting/icp-validation-summary.md + decisions.md
track: outbound
artifact_type: icp-validation
total_score: 15/20
status: good
coordinator_review: done
---

# QC Report — icp-validator — 2026-11-02

**Artifact:** `workspace/outbound/campaigns/2026-10-29-eu-insurance-underwriting/icp-validation-summary.md`, `decisions.md`
**Inputs scored against:** `card-validate.md`, `people-compact.csv`, shared `rulings.md` (13 rulings)
**Total: 15/20** — good (bottom of the band)

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 3 | 5 |
| B | Factual accuracy | 4 | 5 |
| C | Brand & tone | 3 | 3 |
| D | Format & structure | 2 | 3 |
| E | Output quality | 3 | 4 |

## What held up (checked, no action)

- **Location rule:** all 138 PASS sit in the row's country. Out-of-country FAILs are correct, including Craig Duncan (Munich Re, CH), Sara Fenelon (Gen Re, FR) and Michael Haas (Swiss Re, DE). Out-of-cut market teams are WEAK as the card says (Ehlers, Bueno, Kamm, Cerny, Jemai, Chapelain).
- **Empty-profile ruling 10:** no PASS row has the `empty-profile` flag. Every flagged P1 title is WEAK (Guthoerl, Langenstrass, Woltmann, Schmarowski, Brohmi, Gray), and so is Karsten Koch (DPO).
- **Team managers (ruling 5):** these are consistent across batches: Kulemann P2 (solutions), Lokhorst, Rienhoefer and Jonker-Heidolph P3. Nobody was cut as "only a team manager".
- **Rank titles (ruling 4):** bare "General Manager", "Head of Section" and "Director" titles FAIL "scope not shown" in all batches. Teichmann passes on her headline, and Lofink and Rettig are WEAK on earlier L&H roles. That is consistent.
- **Anti-cases caught:** iptiQ run-off (Kraeuchi), group protection (Conway WEAK), Firmengeschäft (Ball), Technische Versicherung (Jessica Müller), private health (Kouvaras), a leaver (Maguire, "available Oct 2026"), the Shay Browne duplicate.
- **Summary vs decisions.md:** these match exactly. PASS 138 (P1 26 · P2 52 · P3 60), WEAK 44 (all 44 names in the table), FAIL 552, all 27 group counts, all 7 angle counts and the 8 Irish Life referrals are correct. Batch sizes reconcile (178+166+145+245 = 734).

## What was wrong (specific)

### A. Adherence — 3/5
- **Ruling 12 (P1 needs visible scope) is broken for Klemens Binswanger** (decisions.md:327, P1). The title is "Head UW & Claims Continental Europe" with no L&H in the title, the headline or earlier roles (compact:256). The reason admits "L&H read from context, not title". The same uncertainty got WEAK elsewhere: Rodrigo Belloube, Ueli Konrad, Florian Fuchsbrunner.
- **Ruling 12 is split across batches for CMOs.** John Schoonbee (Swiss Re, :422) and Alban Senn (Munich Re, :588) are P1. Gabriele Teichmann, Hannover Re's Group Medical Officer (:634), is P2. That is the same seat, and ruling 12 says "C-level without visible life scope → P2 at most". Only the Hannover Re batch applied it.
- **Margot Wilson is P1** (:632) as "MD, L&H Global Services". That is a business-unit head, not the card's reinsurer P1 (L&H underwriting head, UW R&D, automated UW). The comparable seats are all P2: Augusto Diaz-Leante (:420), Fabian Schmitt (:564) and Ulrich Pasdika (:732).
- **PPL-1 route-in below C-level is missing at AXA Life Europe.** Only the CEO and COO go out (Lynam :52, McCormack :3). The export holds Caroline Clinton, Head of IT at AXA Life Europe (compact:192), who was FAILed as "company IT head" (:58). Neither reason says why the account has no route-in. The agent prompt requires that ("отступил — скажи в reason").
- **Ruling 6 (CIO is not CTO) is applied both ways in the same batch.** Koos van der Veen, CIO NN Life & Pensions, is PASS P3 technical-integration (:71). The company CIOs and IT heads of single-line life insurers all FAIL: Amir Fattah (LV 1871, :29), Clinton (AXA LE, :58), Dennis Roehrs (CosmosDirekt, :88) and Denis Eivers (New Ireland, :147). At a single-line life insurer, "company-wide" is life-scoped, which is exactly Koos's argument.
- **The coordinator's Jason Stone edit is labelled "by the card's own rules", and it isn't.** He is located in Switzerland. His headline scope is "Europe, Middle East, Africa, UK & Ireland" (compact:133), which includes Ireland and continental Europe, both in the cut. The card's WEAK rule covers teams serving markets *outside* the cut, and the UK rule is about location. The comparable seat, Volker Homola (BD L/H Continental Europe, :551), is P2. WEAK is a defensible conservative call, but it was not required by the card.

### B. Factual accuracy — 4/5
- Every number in the summary reconciles with decisions.md (see above). No people were invented.
- **Angelique R** (:238): the reason says "insurance physician with an RGA background". In a Dutch profile, "verzekeringsarts RGA" (compact:686) most likely means *Register Geneeskundig Adviseur*, the Dutch register for medical advisers, not Reinsurance Group of America. That is a probable misreading, and it is the only fact behind her PASS.
- Binswanger's "health-insurer board seat" is inferred from a truncated string ("Eidg. Gesundh…").
- Summary line 270 calls Andre Rozemuller's title a "P1 title". It is "Teammanager … AOV Medisch Acceptatie", a team-manager title (decisions.md:244 says "closest to").
- Summary lines 261/272 describe "six group architects", but Achraf Ben Abdallah is a CTO. That makes five architects and one CTO.

### C. Brand & tone — 3/3
- No banned words. The only em dashes are in template headings.

### D. Format & structure — 2/3
- Frontmatter is complete (`product: fitxpress`, profile, campaign, stage, status), and the path and template sections are correct.
- **Three summary table rows are broken** by a literal `|` in the title: line 83 (Simon Fallais), line 169 (Paul Notté de Vaupleux) and line 199 (Arthur van der Wal, "Directievoorzitter | CEO").
- **13 Swiss Re WEAK rows in decisions.md have no `angle` or `wave`** (Konrad :251, Vitale, Murray, Avedikian, Spagnuolo, Renggli, Burghartz, Ehlers, Meier, Bueno, Gray, Kamm, Cerny). The other three batches filled both. If Vadim takes them, promote has no angle to carry.

### E. Output quality — 3/4
- The summary is genuinely useful: it surfaces the pools, names the seniority-pull problem, proposes concrete trims, and gives the Hlib re-pull list.
- **Data architecture is split across batches.** Christian Braun (Swiss Re, Head Group Data Architecture, :371) is PASS P3 technical-integration. Mark Rodgers (Irish Life, Head of Data Architecture and Engineering, :119) is FAIL "data engineering head".
- **Line uncertainty is split.** Shane Farrelly is WEAK because he "may sit in Zurich GI" (:207), at a life entity. Rene Steenks is PASS P2 at multi-line Achmea with "line not shown" (:246), and Achmea owns Zilveren Kruis, a private-health anti-case under ruling 7.
- **a.s.r.: 10 medisch adviseurs pass P2 on title alone**, at a multi-line group (ruling 7). The backgrounds tilt toward claims and disability assessment: UWV bezwaar en beroep (Van Liere, Middelbos), freelance expertises (Balk), and two insurance-medicine trainees (Groot, Yntema). Only Middelbos shows a line (Inkomen). The validator deferred the call to Vadim ("Keep, or keep 3-4") instead of grading them.
- **Two DPOs each at three accounts:** Aviva Ireland (Lyons, Forrester), New Ireland (Scully plus deputy Ferguson) and SCOR (Dewkurun, Juillard). This pads technical-integration (27 of 138), and the summary does not flag it.
- Minor tier drift: Lauren McCormack is P1 and Siobhan Buckley P2, though both titles carry "Health & Protection" and Buckley's demotion cites the health mix. Kshiti A. (L&H IT EMEA) is P3, against P2 for Agarwal and Von Kielpinski. Jennifer H. (L&H data) is WEAK, against P2 for Ian Long.

## Top 3 issues (priority for improver)

1. **P1 consistency:** Binswanger P1 breaks ruling 12. The CMOs are split (Schoonbee and Senn P1, Teichmann P2), and Wilson is P1 while the comparable L&H business heads are P2. The rulings sheet needs one line on reinsurer CMOs and on business-unit MDs.
2. **CIO and head-of-IT split at single-line insurers** (Koos PASS; Fattah, Clinton, Roehrs and Eivers FAIL). Combined with the PPL-1 gap, this leaves AXA Life Europe with no route-in below C-level and no reason given.
3. **Line-unknown medical advisers pass P2 at multi-line groups** (Steenks at Achmea, 9 of 10 at a.s.r.). The same uncertainty is WEAK elsewhere (Farrelly). Angelique R's PASS rests on a probable misreading of "RGA".

## Concrete fixes

1. Binswanger → WEAK "line not shown". Schoonbee and Senn → P2 `medical` (or Teichmann → P1, but pick one rule). Wilson → P2 `reinsurance`. P1 goes from 26 to 22-23.
2. Either PASS P3 `technical-integration` for Fattah, Clinton, Roehrs and Eivers (matching Koos), or FAIL Koos. At minimum, take Clinton so AXA Life Europe has a route-in below C-level.
3. Mark Rodgers → P3 `technical-integration` to match Braun, or drop both.
4. Steenks → WEAK "line not shown". At a.s.r., keep Middelbos (Inkomen) and Angelique R with a corrected reason, and WEAK the other eight "line not shown (acceptance vs AOV claims)".
5. Keep one DPO per account at Aviva Ireland, New Ireland and SCOR.
6. Summary: reword the Jason Stone line as a coordinator judgement, not a card rule. Change "six group architects" to "five architects and one CTO", and drop "P1 title" for Rozemuller.
7. Strip `|` from the three titles in the summary tables. Fill `angle` and `wave 1` for the 13 Swiss Re WEAK rows.

## Coordinator review

```
agreement: ✅ agree
top_issue: P1 and CIO rules drifted between the four parallel batches; fixed by one rule each.
```

All seven fixes applied by the coordinator on 2026-11-02 (22 rows marked "(QC fix 2026-11-02)" in decisions.md, then apply-decisions): fix 1 as proposed (P1 26 → 22); fix 2 = PASS P3 for the single-line insurers' IT heads (Fattah, Clinton, Eivers), Roehrs stays FAIL because CosmosDirekt is multi-line; fix 3 = drop both (Braun FAIL); fixes 4-5 as proposed; fix 6 reworded (Jason Stone kept WEAK as the coordinator's call, "four group architects and SCOR's group CTO"); fix 7 done (no `|` in table cells, 13 WEAK rows filled). Result PASS 127 · WEAK 57 · FAIL 550. Verified mechanically (column counts, SEND/WEAK rows = decisions.md), no second QC.
