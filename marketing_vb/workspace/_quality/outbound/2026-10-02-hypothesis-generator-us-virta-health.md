---
qc_date: 2026-10-02
agent: hypothesis-generator
artifact: workspace/outbound/campaigns/2026-10-02-us-virta-health/hypothesis.md
track: outbound
artifact_type: hypothesis
total_score: 16/20
status: good
coordinator_review: done
---

# QC Report: hypothesis-generator, 2026-10-02, us-virta-health

**Artifact:** `workspace/outbound/campaigns/2026-10-02-us-virta-health/hypothesis.md`
**Total: 16/20** (good)

**Sources I scored against:**
- the hypothesis-generator prompt
- icp-detail.md §1 and the IT & Technical Roles section (:569-604)
- proof-points.md
- accuracy-formulations.md §1-2
- compliance.md §1, §7 and §9
- audience.md segment 1
- `sales-nav-raw/export-1.csv`, all 40 rows read
- the 2026-09-29 cardiometabolic and 2026-10-01 Options QC reports
- `scripts/outbound_pack.py` CARD_SECTIONS (:729-734)

**What reaches the message writer:** the messages card carries `Use case`, `Message angle`, `Rules for steps 3-5` and `Vadim's decisions`. "Read this first", the evidence table and `Target buyer persona` do not reach the sequencer.

**Taken as given:**
- Vadim's standing decisions, including the GLP-1 hub linked as it is.
- Limits, bans, the detector and completeness.

**Limits of this QC:**
- This session has no web tool. I did not re-fetch the Virta pages. Source fidelity is judged against the artifact's own quoted evidence and the export.
- This session has no shell, so notify.py was not run.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 5 | 5 |
| B | Factual accuracy | 3 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence: 5/5
- No issues.
- **Template and decisions:** every template section is present, with one hypothesis, the titles block and the Message 1 gate kept. The standing decisions are carried over verbatim (lines 278-289).
- **Export:** it checks out against the CSV. There are 40 rows: 38 at Virta, plus Everlaw and LaborFirst. Matching is on URL, and the tiers add up to 6/8/2/21 = 37. The Julia Julia identity collision is well argued: her skills are pattern-making and draping, with one line of experience.
- **The four QC lessons are applied structurally:**
  - displacement is verified per claim;
  - outcome promises are banned as a general rule (line 257);
  - the framings are mechanical `banned_terms`;
  - there are 19 sourced Virta facts.
  - The exception is V6 (see B, C and E).

### B. Factual accuracy: 3/5
- **The *Obesity* paper is misquoted in the carded fact.**
  - The evidence quote (line 64) and line 77 say: "Future studies of pharmacological, surgical, and lifestyle-driven WL interventions should also assess LBM". The paper's subtitle is "A call for more research".
  - V6 (line 182, messages card) and line 26 drop "future studies of". They become "weight-loss interventions should also assess it".
  - That turns a research-design recommendation into a care-practice recommendation. The shift runs in the direction that suits our pitch.
  - Line 77's heading, "Virta's own science asks for lean-mass assessment in weight loss", overstates it the same way.
- **One title has no source.** V6 and line 77 call Athinarayanan "Virta's research lead", but the evidence (line 64) identifies her only as "(Virta Health)".
- **Two carded facts are not anchored in any quoted evidence:**
  - V1 (line 177): "no charge for implementation, non-participants or engagement". The quoted employers-page text at line 78 does not contain it.
  - V7 (line 183): "Most weight-loss members are not on GLP-1s". Nothing is quoted; it is attributed to the revenue press release.
- **Clean on the focus items:**
  - Fees at risk (V1 and line 78) and the guarantees (V2) are quoted with their percentage and ratio withheld.
  - The GLP-1 platform (V3) is sourced to the 2026-06-10 release.
  - The surgical pathway (V12) is sourced to three outlets, with the partner name banned.
  - **Device claims** stay positive and sourced: a cellular scale, a glucose and ketone meter, a cuff for some members, and a 440 lb scale limit (line 80). "Not found" and "not verified" are kept separate (lines 65-66). Copy is banned from saying what the devices lack (lines 167, 258).
  - **Numbers in Rules** (line 255) come only from proof-points.md and compliance.md (30 days). The one exception is 2-4 weeks from icp-detail.md:597, limited to `technical-integration`. Earlier QCs licensed it, so it is not capped here.
  - **Compliance:** the US line is verbatim from compliance.md §9. The FDA, MDR and SOC 2 sentences are verbatim from compliance.md §1. "Not a medical device" is scoped to UK/EU MDR (line 134). Guardrail #7's equivalence wording is correct (line 131).
  - **Client names:** none anywhere. The 34,000 line has no name and no geography.
- **Sourcing:** about 45 external URLs, mostly primary sources: Virta's site, help-center API, app listings, PubMed, plus Fierce, MedCity and Axios. Two (Lancet and BGH) were reused from 2026-09-29 without a fresh fetch, and the artifact says so.

### C. Brand & tone: 2/3
- **V6 (line 182) carries a campaign-banned term in a "copy may use" fact.** "preserving lean body mass during weight loss is essential" contains `preserving lean`, which is in this file's own `banned_terms` (line 9). The same line warns that the paper's title contains a banned word.
- **Line 208 (Rad Thie):** "body-size record" leans toward appearance language, for a brand the artifact itself flags as body-image-careful (line 133, Risk 6).
- Otherwise the carded sections are clean: person-first wording, the "objective", "seamless", "comprehensive" and "not promises" traps are handled, and there is no corrective negation.

### D. Format & structure: 3/3
- No issues.
- The frontmatter is complete: `product`, `profile`, `market`, `use_case`, `cap_per_group` and `banned_terms`. The path is correct and the titles block has one title per line.

### E. Output quality: 3/4
- **The strongest clinical hook leads the writer into an implied lean-mass assessment.**
  - Line 205 pairs V6 with "lean mass and fat mass estimates captured at home" for the CMO.
  - Line 209 offers Caroline Roberts V6 together with "body composition estimates … in a future protocol".
  - Together with the misquoted V6, the natural M1 reads as "your paper says assess LBM, and our scan estimates lean mass". Line 171 ("never a lean-mass assessment") and line 259 forbid exactly that.
- **Line 206 (Bergethon, V12) puts the scan next to eligibility.**
  - The question is about members "working toward a procedure", which means a BMI eligibility window.
  - Asking what "a standardized body record over those weeks" should contain points the scan at that eligibility, which line 259 and audience.md §1 ("implying eligibility decisioning") forbid.
- **Same-function peers share a former-employer hook.** This is the mail-merge risk the artifact names as its #1 rule (line 24):
  - Kristen Larson and Leana Balasco: both Personify (lines 218-219). Line 240 lists this very pair as "must not share a context line".
  - Manu Diwakar and Andrew Chen: both Kaia Health (lines 231 and 233), both in finance.
  - Jack Rose and Taylor P.: both Carrot (lines 228 and 230), both in sales.
  - Kathryn Geskermann and Jeff Stanley: both Kaiser (lines 204 and 210), in different lanes.
- **Some referral asks repeat each other in substance:**
  - Leana (line 219) "Who owns what members capture in the Virta app…" and Tara (line 225) "Who on product owns what members can capture at home in the app?" are the same ask, in the same commercial group.
  - Kristen (218), Andre (222), Manu (231), Judy (236) and Dani (237) all ask "who on product is the right person for a body scan".
  - Judy and Dani are the two communications people, and line 240 does not list them as a pair.
- **Line 208 (Rad Thie)** pairs V2 (guarantees, including guaranteed weight loss) with "how the weight-loss programs are presented to plans and employers". That invites guarantee or outcome framing.
- **Line 181 (V5): "a year after GLP-1 deprescription"** is a study figure in words, inside a fact marked "No figures" and against line 255.
- **Strong otherwise:**
  - an exhaustive displacement search (114 help-center articles, 25 release notes);
  - discipline on "not verified either way";
  - a person-level verdict for all 40 rows;
  - the Tara Conboy reclassification, argued and raised as an open question;
  - the investor-relations and IPO traps caught from the export;
  - metrics honestly sized for about 6 accepts.

## Top 3 issues (priority for improver)

1. **V6 and its two hooks (lines 182, 205, 209).** V6 misquotes the paper: "future studies of WL interventions" becomes "weight-loss interventions". It carries the banned `preserving lean` and an unsourced "research lead". Lines 205 and 209 pair it with lean-mass and body-composition estimates, which implies the scan answers the paper's call. Lines 171 and 259 forbid that.
2. **Same-function peers share a former-employer hook:**
   - Personify ×2 (lines 218-219), the very pair line 240 forbids;
   - Kaia ×2 in finance (lines 231 and 233);
   - Carrot ×2 in sales (lines 228 and 230).
   - Referral asks repeat each other too: Leana and Tara; Kristen, Andre, Manu, Judy and Dani.
3. **Line 206 (V12, Bergethon)** ties the body record to the BMI-eligibility window for surgery, against line 259 and audience.md §1. Line 208 (V2, Rad Thie) invites guarantee framing.

## Coordinator review

(filled in by Claude in chat after the automatic QC run)

## coordinator_review

```
agreement: ✅ agree
top_issue: the Obesity paper's research recommendation was shortened into a care-practice claim and paired with our lean-mass estimates; all 11 fixes sent back to hypothesis-generator before the list is stamped, and the coordinator re-checks the paper's wording on the web (QC had no web).
```
