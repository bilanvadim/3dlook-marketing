---
qc_date: 2026-09-29
agent: message-sequencer
artifact: workspace/outbound/campaigns/2026-09-29-us-cardiometabolic/messages/ (primary: ginacamryn, adamdecosta, dannygrannick; risk set: christineoleksiuk, elizabeth-reilly-md789, rabcuka, james-conlin-419853389, abemalkin; 3 summaries; _check.json; all three _batch-*.md read in full for cross-person checks)
track: outbound
artifact_type: messages
total_score: 13/20
status: marginal
coordinator_review: done
---

# QC Report: message-sequencer, 2026-09-29, us-cardiometabolic

**Artifact:** `workspace/outbound/campaigns/2026-09-29-us-cardiometabolic/messages/` (75 people, 3 batches)
**Total: 13/20, marginal.** This needs targeted fixes to about 20 records. It does not need regeneration. The hooks are grounded: every hook I checked against `_profiles-*.md` is real, none is invented, and every flagged profile got neutral copy. The technical lane at Level2 is the best copy in the campaign. The points are lost on three things: account rules at 9am, the campaign's "only this company" line in Message 1, and near-identical referral copy inside 9am.

Scored against `card-messages.md` and the three `_profiles-*.md` files. As instructed, I did not cap D for the missing `product:` frontmatter.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 3 | 5 |
| B | Factual accuracy | 3 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 2 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence: 3/5
- **Nine Message 1s have no line that could only have been written to the company.** card:84 and card:108 ("Kept as a failure, not a note") require one. The gate does not check for it.
  - The Superpower technical lane never names Superpower and never says "between blood draws", in either message. The sequences could go to any company: erhan-justice (_batch-superpower:251-253), will-c-2b884010a (275-277), nmashchenko (297-299), fritz-stauffacher (319-321), slavalukianchuk (343-345), audricserador (365-367).
  - At 9am, oyebola-agoro (_batch-9amhealth:109-111) and rebecca-eberspacher (181-183) never name 9am or the Data Hub.
  - At Level2, pamelaperrymba (_batch-level2:197-199) never names Level2, but `_summary-level2.md:10` says the copy is "addressed as Level2 clinical operations".
- **The content asset was mostly dropped.** card:60 assigns `/ai-body-data-wellness-platforms/` to Superpower's product, clinical and operations lanes. All 11 of those Superpower M2s omit it. dannygrannick M2 is 382/550 and has room for it. At 9am, five M2s dropped the GLP-1 hub link "for the 550 cap" (`_summary-9amhealth.md:15`), but the link line is about 100 characters. By my count paulgeevarghese M2 (about 402) and oyebola M2 (about 367) both have room for it.
- **oyebola ignores the 9am lead.** card:38 and card:44 say to lead with a standardized, guided capture: "80+ body measurements beyond waist and a 3D model". Her M1 offers only body-composition estimates.
- Done correctly: Rabcuka per step-4 decision 5, the empty-profile Level2 people written from their titles, the referral lane without a compliance line, and different M2 openers inside each company.

### B. Factual accuracy: 3/5
- **9am rule (card:38, card:75): never imply that waist or body composition is new to 9am.**
  - christineoleksiuk:18 has "a guided body record to show an employer beyond weight". The Data Hub already shows weight, waist and A1C, and the scale reports body composition. card:48 prescribes "beyond weight" for 9am commercial roles, so the card contradicts its own 9am rule. The agent flagged this one to Vadim.
  - The agent's own elaboration makes it worse in three records it did not flag: mike-reeve (_batch-9amhealth:285) "beside weight and A1C trends", lindsay-gilreath (321) "next to weight and A1C trends", and andrewwoolwine (357) "beside weight and A1C". Each lists two of the three Data Hub trends and leaves out waist, which the new record would include.
  - oyebola (109-111) pitches "body composition estimates such as lean mass and fat mass" to the account whose cellular scale already reports body composition.
- **The speed claim has one public definition, "under 45 seconds from the photos to structured results" (card:71, card:178).** Four 9am records drift from it:
  - ginacamryn:18 "in under 45 seconds"
  - gregschwartz (233) "come back as structured results in under 45 seconds"
  - josh-tolentino (259) "in under 45 seconds"
  - oyebola (119) "structured results arrive in under 45 seconds from the photos"

  Level2 and Superpower use the exact phrase every time.
- **elizabeth-reilly-md789:29.** "96-97% accuracy … for the body measurements. Results reach the care team as estimates". This calls the body measurements estimates. Body measurements are measurements. Body composition is the estimate.
- No problems with the rest: numbers from proof-points only, no clients named, the 112,100 figure never attributed to one platform, and the compliance line verbatim. libbymacfarlane M2 (_batch-level2:41) appends "each from two photos on a phone" to the 34,000 line. That is true for FitXpress, but it is an embellishment.

### C. Brand & tone: 2/3
- **Seven M2s lead with the accuracy figure, against prompt rule 6 and the card's anti-positioning.**
  - elizabeth-reilly:29 "On the numbers: 96-97%…"
  - 0327-fran-archila (_batch-9amhealth:217) "For the spec sheet: 96-97%…"
  - elisabeth-cavanagh-myers (_batch-level2:135) "For the spec sheet"
  - robin-tinsley (257) "A quality figure…"
  - manoj-arachige, elizabeth--wild, audricserador (Superpower)

  At 9am, which sends members a tape measure, the benchmark "against expert manual measurement" given to an endocrinologist is the weakest possible value line.
- **Triple lists:** paulgeevarghese (95) "no device to ship, return or support" and madeline-velez (167) "ship, replace or support".
- **Greeting and register slips:**
  - dr-molly-finley M1 and M2: "Hi Dr. Molly,"
  - mike-reeve: "the commercial seat" (for a CCO) and M2 "My first note may have been wordy." (his note was two short lines)
  - christineoleksiuk: "a CCO seat at FoodHealth"
- No banned words and no dashes, confirmed by the coordinator.

### D. Format & structure: 2/3
- **About 21 M1s run the CTA into the product paragraph.** The prompt and template want it on its own line. That covers 16 of 17 non-referral Superpower M1s (e.g. dannygrannick:18, rabcuka:18) and 5 at Level2 (james-conlin:18, holly-mcvey, madeline-lerche, robin-tinsley, chris-arntzen).
- **The summaries misstate the agent's own work.**
  - `_summary-superpower.md:13` says "No article link in any M2", then in the same line says tech people carry the trust FAQ. erhan and fritz do carry it.
  - The 9am "550 cap" reason is inaccurate for at least two of its five records (see A).
- System note, not scored: `rabcuka.md:1` (split-messages header) reads "Chief Business Development Officer — University of Oxford". The message bodies are clean. If the importer or anyone reviewing takes the title from that header, it contradicts step-4 decision 5.

### E. Output quality: 3/4
- **9am referral copy reads as a mail merge (prompt rule 2, "a forwarded screenshot must not read as a mail merge").** 21 people at one company get one ask, and 15 of them carry the same sentence verbatim: "I work at 3DLOOK; we build a two-photo body scan for member apps." Some pairs are 70-80% identical and would likely be forwarded to the same owner:
  - jacob-moore (481-483) and maribelle-gauna-estrada (643-645): both "…is why I am writing. Quick ask: who leads the clinical side of the 9am member app, or owns its roadmap?"
  - kayla-sheafer (337-339) and michellenjones1144 (427-429)

  Level2 shows the same pattern at a smaller scale: lovenj/carriehauser M1 paragraph 2 is verbatim, and shelby-p/rebecca-mclaughlin M2 both end "Two lines from me … is all it takes."
- **james-conlin M2 (:27) muddles two things.** It mixes "employer conversations under the Assured Value Program" with "the care team can compare across scans". For a CEO this is the weakest value line in the sample.
- The strong records:
  - adamdecosta: a question-form stack hook that asserts nothing about Level2's app, and "long enough to want a progress state" is real implementer language.
  - shaun-miller: the PDF line from his own bio.
  - rabcuka: the company-fact hook, the verbatim repeatability sentence, and no CBDO or Oxford.
  - abemalkin: a clean routing ask that works whether or not he is still an advisor.
  - dannygrannick: a real between-draws retention question.
  - ginacamryn: M1 is sound. Its M2 central argument, "no device to ship or support", is the lane's generic point, not the 9am-specific "one guided sequence each time" (card:46). This is minor, because M1 carries the guided sequence.

## Top 3 issues (priority for improver)

1. **9am account rule.** Five records imply that waist or body composition is new to 9am: christine, mike, lindsay, andrew and oyebola. The card causes part of it: card:48 prescribes "beyond weight" for 9am commercial roles, which contradicts card:38 and card:75. That line should be fixed in the card generator or hypothesis as well as in the copy.
2. **The "only this company" line is missing from nine Message 1s**, including the whole Superpower technical lane. The hypothesis treats this as a failure, and the gate does not see it. It is worth moving this into `check-messages` (the company name, or a card-listed company fact, in M1).
3. **The 9am referral lane is a template with the hook swapped.** 15 of 21 records share the same product sentence, and several pairs are 70-80% identical.

## Coordinator review

(filled in by Claude in chat after the auto-QC run)

## coordinator_review

```
agreement: ✅ agree
top_issue: the card's own referral line told the agent to write "beyond weight" for 9amHealth commercial roles; fixed in hypothesis.md (re-stamped, card rebuilt) and 34 flagged records sent back to their three batches. Rabcuka's import title corrected to her Superpower role per Vadim's decision 5.
```
