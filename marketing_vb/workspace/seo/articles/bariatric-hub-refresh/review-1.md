---
article: bariatric-hub-refresh
published_slug: bariatric-pre-qualification-mobile-3d-body-scanning
review: 1
source: "Google Doc «Rewrite - Bariatric Pre-Qualification and Patient Progress Tracking: Body Data for Obesity Care Teams», tab «Review 1» (t.3aezkxquqscs)"
source_url: https://docs.google.com/document/d/15bydjzHTEHhHt5LAapc4iqTsIAdcWUMtn4ryu9E4SHo/edit?tab=t.3aezkxquqscs
extracted: 2026-09-07
extracted_by: coordinator, oo googledocs get_document_by_id include_tabs_content=true
arrived_at: checkpoint 2 (CMS-ready body in publish-package.md)
scope: "Hub refresh (content plan row 67, P0) PLUS the two P2 rows folded in by the reviewer: row 68 (Pre-qualification refresh) and row 69 (Remote intake). Rows are 1-indexed on the sheet including the header; the reviewer numbered them 66/67/68."
status: verbatim — do not edit. Rulings live in review-1-decisions.md, which wins on any conflict.
---

# Review 1 — verbatim

Transcribed from the Google Doc tab without edits. Tables are flattened to pipe rows and the
doc's duplicated bare anchors are dropped; wording, ordering and headings are the reviewer's.
The reviewer's own source links are preserved inline.

One artefact is left in place deliberately: the line beginning "You're right — Smart Scale is a
FitXpress feature" is the reviewer's mid-session correction of their own item 4. It is why item 4
appears as "Revised recommendation 4". Kept because the decisions file rules on the revised
version, not the withdrawn one.

---

I reviewed the CMS-ready article in the publish package.
The article covers the planned hub refresh and both later P2 updates, but it is not ready to publish yet. Its strategic foundation is strong; the main problems are regulatory accuracy, overstatement of payer acceptance, one conflated data comparison, and a few product-positioning issues.
Overall assessment: 6.5/10 in its current form; potentially 8.5/10 after revision.
## Requirements coverage
| Requirement | Assessment | Comment |
| Main bariatric hub | Met | The H1, audience and overall scope align well with obesity-care teams. |
| Pre-authorization expansion | Met, but needs correction | Substantial coverage, although the article overstates what scan records can contribute to payer documentation. |
| Patient progress tracking | Met | Section 8 establishes baseline-to-follow-up use, but body-composition estimates need more careful positioning. |
| GLP-1 bridge | Partially met | The bridge is relevant, but Section 4 becomes a generic GLP-1 market section and risks cannibalizing the GLP-1 hub. |
| Post-operative tracking | Met | Clearly addressed, although several benefit statements are stronger than the evidence supports. |
| P2 pre-qualification update | Met | The definition, workflow and FAQ coverage are sufficient to absorb this topic into the hub. |
| P2 remote intake update | Met at section level | The four-stage workflow is a good start. It needs slightly more operational detail around failed capture, retakes, human review and data handoff. |
| Bariatric-specific guardrail | Mostly met | Generic telehealth duplication is avoided. Generic GLP-1 coverage and the “bariatric surgery basics” FAQs should be reduced. |
| BOFU value | Good foundation | Buyer roles, workflow and limitations are useful, but the article needs a stronger pilot-evaluation framework. |
The two planned P2 articles do not currently need separate pages. The existing hub can own both intents once the relevant sections are strengthened. A future standalone remote-intake page would only be justified if it focuses narrowly on integration, capture completion, quality control and operational handoffs.
## Must-fix issues
### 1. The CMS-0057-F section contains material inaccuracies
The seven-day and 72-hour decision timeframes exclude Qualified Health Plans on Federally Facilitated Exchanges. The article currently includes them when describing who is “on this clock,” including in the FAQ.
The official CMS guidance also notes that certain requests may qualify for extensions of up to 14 calendar days.[CMS’s FAQ confirms both qualifications](https://www.cms.gov/initiatives/burden-reduction/overview/interoperability/frequently-asked-questions/prior-authorization-api).
The article also conflates two separate requirements:
- Payers must give the provider or patient a specific reason for a denial.
- Payers publish aggregated prior-authorization metrics.
Specific denial reasons are not publicly accumulated in a way that makes one program’s incomplete submissions “legible over a year.”[CMS describes those as separate requirements](https://www.cms.gov/newsroom/fact-sheets/cms-interoperability-prior-authorization-final-rule-cms-0057-f).
Delete or rewrite:
“a missing timestamped BMI record stops being a delay and becomes a denial”
and:
“Published reasons accumulate, which makes the pattern of a program’s incomplete submissions legible over a year.”
Neither conclusion follows from the rule.
A safer replacement would be:
Beginning January 1, 2026, CMS-0057-F requires Medicare Advantage organizations and specified Medicaid and CHIP payers to issue standard non-drug prior-authorization decisions within seven calendar days and expedited decisions within 72 hours, subject to applicable extension provisions. The rule did not change the decision timeframes for Qualified Health Plans on Federally Facilitated Exchanges. It also requires specific denial reasons and public reporting of aggregated prior-authorization metrics.
The meta description should consequently stop making the “7-day payer clock” the universal lead.
### 2. A timestamped scan is not automatically payer-accepted evidence
This is the largest positioning issue. The article repeatedly moves from:
structured and timestamped record
to:
verifiable evidence for a payer packet
without establishing that a payer will accept a mobile-scan output as documentation of BMI or another required measurement.
A timestamp supports traceability. It does not independently verify:
- Patient identity
- The source of height or weight
- Measurement validity
- Clinical appropriateness
- Payer acceptance
This affects the Use Case Summary, Sections 3, 5, 6, 7, 9 and 10, plus several FAQs.
Use this distinction consistently:
A structured scan record can give the program a dated and standardized body-data input before the consultation. Whether a payer accepts that record for a specific documentation requirement depends on the plan and should be confirmed during implementation.
The comparison table is particularly problematic. An EHR note can be timestamped, while a scan timestamp does not necessarily make the underlying measurement acceptable to a payer. Replace “What a payer reviewer can verify” with “Documentation generated” and add a separate row for “Payer acceptance.”
### 3. Section 4 conflates two different datasets
The article combines:
- A JAMA Surgery claims analysis of 11.7 million insured adults covering 2022–2024, which reported GLP-1 use increasing 140.4% and metabolic bariatric surgery use declining 34.1%.[JAMA Surgery study](https://doi.org/10.1001/jamasurg.2026.1343)
- An Epic Cosmos electronic-health-record analysis covering 2018–2025, from which the annual procedure counts such as 40,265 and 33,429 are taken.[ASMBS release](https://asmbs.org/news_releases/as-glp-1-use-skyrockets-and-bariatric-surgery-slows-most-obesity-goes-untreated/)
The table describes the annual counts as coming from “the same claims cohort.” They do not.
The best solution is to remove most of this table. It duplicates the GLP-1 market hub and contributes little to the bariatric intake argument. Retain one carefully sourced indicator showing that GLP-1 use is changing the population reaching bariatric programs, then link to the GLP-1 hub for the wider market analysis.
You’re right — Smart Scale is a FitXpress feature. The recommendation should be to clarify and correctly characterize weight estimation, not remove it.
### Revised recommendation 4: Retain and better explain Smart Scale
Keep predicted weight in the article because it is directly relevant to remote bariatric intake and BMI cross-checking. However, revise the current wording:
“it carries a ±3.5% average error margin as a software estimate”
“±3.5%” suggests a guaranteed error interval. The approved claim is a mean absolute error of approximately 3.5% under the evaluated conditions.
Recommended replacement:
FitXpress Smart Scale estimates weight from the guided photo capture. In internal validation under evaluated capture conditions, including tight-fitting clothing, predicted weight showed a mean absolute error of approximately 3.5% compared with scale weight. Because it remains a software estimate, a calibrated scale should be used whenever a clinical protocol or payer requires a directly measured weight.
### Explain how Smart Scale supports BMI review
The article currently says FitXpress returns BMI without explaining the underlying workflow. The bariatric use case becomes more convincing if it distinguishes the two BMI values:
- BMI-1: calculated from self-reported height and weight.
- BMI-2: calculated from self-reported height and the weight predicted by FitXpress Smart Scale.
- Comparison: the program can compare BMI-1 and BMI-2 and route material differences for human review.
Suggested text for Section 7:
FitXpress can support an additional BMI cross-check through Smart Scale. BMI based on the patient’s self-reported height and weight can be compared with BMI calculated from the same height and Smart Scale’s predicted weight. A material difference between the two values becomes a review signal rather than an automated eligibility conclusion.
This would strengthen the pre-qualification section because it explains what “BMI verification capability” actually means.
### Update the product description
Current wording:
“the output covers 80+ body measurements along with BMI, basal metabolic rate, body-fat percentage, and lean and fat mass”
Recommended:
The output can include a 3D model, 80+ body measurements, predicted weight through Smart Scale, BMI, basal metabolic rate, body-fat percentage, lean mass and fat mass. Results are generated from a guided two-photo capture completed on the patient’s smartphone.
### Update the Use Case Summary
The Outputs row could become:
| Field | Revised detail |
| Outputs | Predicted weight through Smart Scale, BMI values for comparison, 80+ body measurements, body-composition estimates, capture timestamp and capture-quality outcomes |
The Role row should retain the human-review boundary:
| Field | Revised detail |
| Role | Provides structured body-data inputs and discrepancy signals for program review; it does not determine eligibility or payer acceptance |
### Update Stage 1 of the intake workflow
Stage 1. Remote capture at intake. After the patient submits the intake questionnaire, the program sends a scan link. The patient completes the guided two-photo capture on their smartphone. FitXpress returns structured body data, including predicted weight through Smart Scale, BMI, body measurements and body-composition estimates. Where self-reported weight is also collected, the program can compare the resulting BMI values and route material differences for human review.
### Revised post-operative wording
Smart Scale can also remain in the progress-tracking section, but the distinction between estimates and direct measurements should be explicit:
Predicted weight can add another consistent data point to remote follow-up. In internal validation under evaluated conditions, Smart Scale showed a mean absolute error of approximately 3.5% compared with scale weight. Programs should treat it as a software estimate and continue using a calibrated scale wherever their clinical protocol requires directly measured weight.
### 5. Several operational outcomes are presented as established results
Examples include:
- “Higher consult-to-procedure conversion”
- “fewer measurement-only visits”
- “the difference between a first-pass submission and a resubmission”
- “Every verification step... is also a point where a patient can leave”
- “replaces the fragmented manual measurements”
The cited attrition research establishes that attrition varies widely; it does not establish that mobile scanning reduces attrition or improves conversion. The CDC’s 40% figure is a population-level comparison between self-reported and bias-corrected severe-obesity prevalence, not evidence that every individual self-reported BMI is inaccurate.[CDC study](https://www.cdc.gov/pcd/issues/2023/23_0005.htm)
Present these as:
- Operational hypotheses to test
- Potential workflow benefits
- Pilot KPIs
Useful pilot metrics would include intake completion, retake rate, time from inquiry to completed body-data record, pre-auth rework, measurement-only appointments and follow-up completion.
### 6. Remove references to unpublished “dedicated guides”
The CMS-ready body repeatedly tells readers that topics are handled in future guides, even though those guides are not live:
- “has a dedicated guide of its own”
- “treated in a guide to remote body measurement”
- “covered separately”
- “handled in two further guides”
These are visible promises, not merely internal link markers. Remove them until the corresponding pages publish. The hub already contains the P2 material and should answer the question directly.
### 7. Revise the privacy and compliance paragraph
The statement that FitXpress “processes no personal identifiers” is too broad and potentially misleading. Body data and session-linked outputs may still qualify as personal data even if names and contact details are not required as scan inputs.
Use the approved GDPR formulation:
In most enterprise deployments, the customer acts as controller and 3DLOOK acts as processor under GDPR.
Also align photo retention with the approved product statement: photos are deleted after processing, while outputs are retained. Avoid adding “or within a configurable retention window” unless that variation has been confirmed for this product and deployment.
## Recommended structure
The current article spends roughly half its length establishing market context before reaching the actual workflow. For a BOFU-weighted hub, the operational answer should arrive earlier.
| Order | Recommended section |
| 1 | Introduction and concise Use Case Summary |
| 2 | What structured remote body data contributes, and what it does not decide |
| 3 | Remote Body Measurement for Bariatric Patient Intake: A Four-Stage Pre-Qualification Workflow |
| 4 | Pre-qualification and pre-authorization documentation |
| 5 | The GLP-1 bridge: current BMI, historical BMI and documentation continuity |
| 6 | Patient progress tracking before and after surgery |
| 7 | Where FitXpress fits: outputs, accuracy, repeatability and limitations |
| 8 | Manual measurement versus guided capture |
| 9 | What to confirm in a bariatric pilot |
| 10 | Focused FAQs, CTA and relevant reading |
This structure fully incorporates both planned P2 updates while keeping the page centered on bariatric operations.
## Additional content improvements
- Rewrite the introduction. Phrases such as “which record has to be in the file, dated when, and for whom to review” and “the verification stack most of them still run” are abstract and unnecessarily technical.A clearer opening:Bariatric programs often collect or verify body measurements during the first consultation. When those inputs are missing, inconsistent or captured too late, pre-qualification and pre-authorization preparation can require additional follow-up. Structured remote intake can provide dated body measurements before the visit, establish a baseline for progress tracking and leave eligibility and treatment decisions with the care team.
- Revise Stage 2. “Patients who clearly meet criteria move...” makes the scan sound like a screening or eligibility engine. Describe the coordinator confirming completeness and routing the record for authorized human review. Include retake or in-clinic fallback where capture quality is insufficient.
- Distinguish measurements from estimates in the post-operative section. Body-composition estimates should complement weight and circumference trends only where the program considers them appropriate. They should not be presented as equivalent to DXA or professional BIA.
- Remove “weeks apart” from the repeatability definition unless the validation protocol actually tested unchanged subjects weeks apart.
- Change “one capture asset... replaces fragmented manual measurements” to “the same data structure can be generated at multiple pathway stages alongside measurements required by the program or payer.”
- Add a compact pilot-evaluation table covering capture completion, quality failures and retakes, workflow integration, role-based review, population fit, payer acceptance and data governance.
- Reduce the FAQ section from 16 questions to approximately 7–9. Remove the “Bariatric surgery basics” block: it attracts patient-facing informational intent and adds little value for the stated buyer. Several other FAQs simply repeat the body.
- Remove unrelated links to occupational health, insurance underwriting and wellness rewards. They weaken bariatric topical focus. Keep the health hub, GLP-1 hub, telehealth hub, BMI-verification page, accuracy framework and product page.
A more accurate meta description would be:
See how obesity care teams can use remote body data for bariatric pre-qualification, intake, pre-auth preparation, and post-op progress tracking.
The article can become a strong bariatric hub and sales-enablement asset. Its strongest idea is the connection between earlier structured intake and a longitudinal patient record. The revision should make that idea central, while treating payer acceptance, clinical use and measurable operational impact as deployment-specific rather than established outcomes.
