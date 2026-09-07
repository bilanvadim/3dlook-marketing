---
article: bariatric-hub-refresh
published_slug: bariatric-pre-qualification-mobile-3d-body-scanning
review: 1
review_source: review-1.md (verbatim extract of the Google Doc tab "Review 1")
written: 2026-09-07
written_by: coordinator
snapshot: v1/ (draft-v1-writer, draft-v2-editor, editor-report, plan, plan-audit, publisher-report, publish-package, refresh-gap-analysis, writer-notes, published-live-2026-07-27)
scope: "Hub refresh, content-plan row 67 (P0), plus the two P2 rows the reviewer folded in: row 68 (Pre-qualification refresh) and row 69 (Remote intake). The reviewer numbered these 66/67/68, counting from the first data row instead of the sheet's own row numbers; same three rows."
authority: "THIS FILE WINS over review-1.md wherever the two differ. Agents read both."
next_stages: edit (seo-editor) -> publish (seo-publisher) -> qc (quality-controller)
---

# Review 1 — decisions

The reviewer read the CMS-ready body in `publish-package.md` §6 and scored it 6.5/10, with 8.5/10
available after revision. Nothing in the review touches the two settled checkpoint decisions
(byline `Assel Sekerova`, re-date on republish, slug unchanged) and nothing touches the H1 or the
primary keyword, so this is an `edit` round, not a re-plan.

**How to read this file.** Every review item appears below with a disposition and the source that
grounds it. Where a row says **verbatim**, the quoted sentence is the text to place; do not
paraphrase it and do not improve it. Where a row says **amended**, the reviewer's intent is
accepted but their wording is not, and the replacement text in this file is what ships. Two rows
are **declined**, both because the reviewer is wrong about our product rather than about the
writing.

**The trap this file exists to avoid.** On the occupational-health article, a decisions row that
summarised an instruction *became* the instruction, and the editor applied the summary instead of
the reviewer's line. So: the "Text to place" column below is literal copy, not description of copy.

---

## A. Two external facts verified before ruling

**A1. CMS-0057-F decision timeframes exclude QHP issuers on the FFEs. The reviewer is right.**
Checked 2026-09-07 against both pages the reviewer cited.

- CMS fact sheet, verbatim: *"We are requiring impacted payers (excluding QHP issuers on the FFEs)
  to send prior authorization decisions within 72 hours for expedited (i.e., urgent) requests and
  seven calendar days for standard (i.e., non-urgent) requests."*
- CMS prior-authorization API FAQ, verbatim: *"Because the final rule did not alter prior
  authorization timelines for QHP issuers on the FFEs, these rules and related FAQs do not apply to
  them,"* and *"Requests marked with an asterisk (\*) in the chart above may be granted an extension
  of up to 14 additional calendar days, subject to the program-specific regulatory conditions."*
- On reporting, the fact sheet says payers *"publicly report certain prior authorization metrics
  annually by posting them on their website"* and separately that they *"must provide a specific
  reason for denied prior authorization decisions."* The denial reason goes to the requester. It is
  not part of the public annual posting.

The article's §3 sentence *"CMS-0057-F applies to Medicare Advantage organizations, Medicaid and
CHIP … and Qualified Health Plans on the Federally Facilitated Exchange"* is true of the rule as a
whole. What is false is carrying that same list into the **timeframe** claim and into the FAQ. That
is the correction, and it is narrower than "delete the list".

**A2. §4's third table row cannot be true on its own face.** It reports a 2025 procedure count
"from the same claims cohort" as a JAMA Surgery analysis the row above dates 2022 to 2024. A
2022-2024 cohort cannot yield a 2025 count. The reviewer's account (the counts come from an Epic
Cosmos EHR analysis running 2018-2025, reported in the ASMBS release) explains the mismatch. No
re-sourcing is needed because the ruling below removes the row.

---

## B. Must-fix issues

### B1. CMS-0057-F accuracy — **apply, amended**

Three edits in §3 plus one in the FAQ.

**(a) Delete these two sentences from §3, entire:**

> When the record supporting medical necessity is assembled only after the payer asks for it, a
> missing timestamped BMI record stops being a delay and becomes a denial that now carries a
> published reason. Published reasons accumulate, which makes the pattern of a program's incomplete
> submissions legible over a year.

Neither conclusion follows from the rule (A1). What survives from that paragraph is the operational
point that already precedes it: a long review window absorbs a request for more information and a
seven-day window leaves little room for one. Keep that. Do not replace the deleted sentences with a
softer version of the same inference.

**(b) The timeframe statement.** Place the reviewer's replacement, with two mechanical
conformances to the page's own style (they are style, not content, and the reviewer did not rule on
style): dates as `1 January 2026`, and `7 calendar days` / `72 hours` in numerals, both as the page
already writes them everywhere else.

> Beginning 1 January 2026, CMS-0057-F requires Medicare Advantage organizations and specified
> Medicaid and CHIP payers to issue standard non-drug prior-authorization decisions within 7
> calendar days and expedited decisions within 72 hours, subject to applicable extension provisions.
> The rule did not change the decision timeframes for Qualified Health Plans on Federally
> Facilitated Exchanges. It also requires specific denial reasons and public reporting of
> aggregated prior-authorization metrics.

**(c) Keep these two existing sentences.** They are correct, they are the payer-mix point a program
director actually needs, and the reviewer did not ask for them: *"It does not cover every commercial
plan governed by the Employee Retirement Income Security Act. Medicare fee-for-service does not use
prior authorization for bariatric procedures at all."* Keep the closing line that reading the rule
against a specific plan contract is work for compliance counsel.

**(d) FAQ "How long do payers have to decide a bariatric prior authorization?"** Currently answers
that impacted means *"Medicare Advantage, Medicaid, CHIP and Qualified Health Plans on the Federally
Facilitated Exchange"* on the same clock. Rewrite so the timeframes attach to MA, Medicaid and CHIP,
the QHP exclusion is stated, and the extension provision is mentioned once.

### B2. A timestamped scan is not automatically payer-accepted evidence — **apply in full**

The largest item, and it agrees with our own guardrails rather than fighting them: the page's own
disclaimer already says these outputs are *supporting evidence within decisioning workflows operated
by licensed bariatric programs*. The body then drifts. Apply the reviewer's distinction everywhere
the drift appears: Use Case Summary, §3, §5, §6, §7, §9, §10 and the FAQ.

**Text to place where the distinction is first drawn (verbatim):**

> A structured scan record can give the program a dated and standardized body-data input before the
> consultation. Whether a payer accepts that record for a specific documentation requirement depends
> on the plan and should be confirmed during implementation.

**The §10 comparison table.** Rename the row *"What a payer reviewer can verify"* to **"Documentation
generated"**, keeping its two existing cells. Then add a new final row **"Payer acceptance"** whose
two cells both say the same thing in the table's register: acceptance follows the plan's own
documentation requirements and is confirmed during implementation, not from the capture method. Do
not write a cell that implies either method is pre-accepted.

**Specific phrases that carry the overstatement today and must go or be re-cut:**

- §7 pathway table, *"Provides structured, timestamped documentation inputs"* — acceptable as an
  input claim; keep, but it may not be paired anywhere with a verification claim.
- §9 *"Whether those records are audit-ready follows from how the data was captured"* — reframe;
  audit-readiness is the program's determination, not a property the capture confers.
- §5 *"a reviewer at the payer cannot confirm when it was taken or how"* — this compares a scan
  record with a free-text note. Keep the comparison, drop any implication that the scan record is
  therefore confirmable by that reviewer.

### B3. §4 conflates two datasets — **apply, with the table mostly removed**

Delete the three-row indicator table and the paragraph that reconciles ASMBS against the claims
cohort. Keep **one** indicator, correctly attributed:

> Metabolic bariatric surgery use fell 34.1% while GLP-1 receptor agonist use rose 140.4% between
> 2022 and 2024, measured inside one insured claims cohort of 11.7 million adults.

Cite it to the JAMA Surgery paper itself, `https://doi.org/10.1001/jamasurg.2026.1343`, which the
reviewer supplied and which is a stronger source than the EurekAlert release the draft currently
links. Then link to the GLP-1 market hub for the wider market picture, which is what the
cannibalization guardrail on content-plan row 67 asks for: *"Do not duplicate GLP-1 or telehealth
generic pages."*

Everything else in §4 goes: the 2023 ASMBS national estimate (270,089 / 279,967), the cohort
procedure counts (40,265 / 42,615 / 37,339 / 33,429), and the ASMBS-versus-claims reconciliation
paragraph. The two practitioner quotes (Funk, Kurian) may stay if the section survives the
restructure in §D as the GLP-1 bridge; they carry the funnel-shape point without a market-size
claim.

**§5 is not affected.** Its Epic Cosmos study (Chhabra, 6,700 patients with prior GLP-1 use, about
8% total body weight lost before surgery) is a different study, correctly attributed today, and it
is the factual spine of the whole documentation-continuity argument. Keep it.

### B4. Smart Scales — **apply, amended on wording and on the product name**

The reviewer withdrew their original "remove predicted weight" recommendation mid-review and
replaced it with "retain and explain". We rule on the revised version. Substantively they are
right and this closes a real gap: the draft mentions the ±3.5% figure once, in §8, and never
explains where predicted weight comes from.

Five wording corrections to their suggested text, all sourced:

1. **The feature is called Smart Scales, plural** (`product-info/how-it-works.md`, backend
   pipeline step 6; `tech-spec.md` line 100). The reviewer writes "Smart Scale" throughout. Use ours.
2. **It is beta** (`how-it-works.md`: *"Smart Scales (beta)"*; `tech-spec.md`: *"Smart Scales
   (beta)"*). Say so at first mention. Shipping a beta capability as generally available on a
   healthcare buyer page is the same class of overstatement the rest of this review is correcting.
3. **"Internal validation" is not the provenance of this figure.** `proof-points.md` sources
   ±3.5% to the *FitXpress deck, real-world conditions*. "Internal validation" is the phrase
   `accuracy-formulations.md` §1.1 reserves for the measurement-accuracy study against
   pattern-maker manual measurements, which is a different study with a different reference.
4. **"Including tight-fitting clothing" has no source.** No brand-asset states a clothing condition
   for the weight estimate. What is on file is a clothing *detector* that classifies fit type and
   prompts the user (`how-it-works.md`, capture flow step 4 and backend pipeline step 2). Drop the clause.

5. **"Mean absolute error" claims a statistic we cannot back — declined.** `proof-points.md`
   records *"±3.5% average error margin"*, sourced to the FitXpress deck. "Average error margin"
   does not establish that the figure is specifically a mean absolute error, and asserting that it
   is would add precision no source supplies, which is editorial guardrail #1. The reviewer's
   underlying objection is sound and is applied a different way below: `±` must not read as a
   guaranteed bound on a single reading, so the sentence says outright that it is an average.

**The symbol stays, and that is a gate constraint rather than taste.** `article_lint.py` gate 9(a)
matches any `error … 3.5%` fragment against `APPROVED_ACCURACY`, whose only weight entries are
`+/-3.5%` and `±3.5%`. A sentence reading "an average error of approximately 3.5%" fails that gate
as an accuracy figure we do not publish. Keep `±3.5% average error margin`; carry the reviewer's
qualification in the words around it.

**Text to place, product paragraph in §7 (replaces the current output list):**

> The output can include a 3D model, 80+ body measurements, predicted weight through Smart Scales
> (beta), BMI, basal metabolic rate (BMR), body-fat percentage, lean mass and fat mass. Results come
> back in under 45 seconds from a guided two-photo capture completed on the patient's own smartphone.

**Text to place, the BMI cross-check in §7** (the reviewer's structure, anchored to what the product
actually emits — `how-it-works.md` backend pipeline step 6, *"cross-validates self-reported weight against the AI
estimate, flags mismatch"*, and `tech-spec.md`, *"Smart Scales weight estimate + mismatch flag (when
self-reported weight provided)"*):

> FitXpress can support an additional BMI cross-check through Smart Scales. Where the program also
> collects a self-reported weight, the capture compares it against the estimate and flags a
> mismatch. BMI from the patient's self-reported height and weight can then be read against BMI from
> the same height and the predicted weight. A material difference between the two values becomes a
> review signal rather than an automated eligibility conclusion.

**Do not rewrite that last clause.** `terminology-guardrails.md` Part 1 bans corrective
"rather than", and its exception is the product, clinical, legal and regulatory boundary. Saying
that a discrepancy is a review signal and not an eligibility conclusion is exactly that boundary,
it is the sentence B2 exists to protect, and the same licence covers the Role row below.

**Text to place, wherever the 3.5% figure lands:**

> Predicted weight stays a software estimate. Against scale weight it carries a ±3.5% average error
> margin under real-world conditions, an average across the evaluated captures rather than a bound
> on any single reading. A calibrated scale remains the reading wherever a clinical protocol or a
> payer requires a directly measured weight.

(Note for the editor: the draft's current sentence uses `so` to introduce that consequence, which
`terminology-guardrails.md` Part 2 bans. The replacement above already avoids it.)

**Gate note, resolved 2026-09-07.** The first edit pass failed `article_lint.py` gate 5 on six
hits of `predicted weight`: a blanket `SUPERSEDED` row inherited from the wellness hub's Review 1.
Vadim scoped that row to wellness copy the same day, because FX-008 covers weight estimation, the
capability is documented in `how-it-works.md` and `tech-spec.md`, and the live
`online-pharmacy-bmi-verification` page already publishes the phrase in its Outputs row. The B4
text above ships unchanged and the draft passes. Nothing here for the publisher to re-litigate.

**Gate note for the editor:** the paragraph carrying that figure must also link
`https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/`. That is the accuracy-discipline gate
in `article_lint.py`, not a preference (`accuracy-formulations.md` §3.2). Today the §8 paragraph
satisfies it; if the figure moves, the link moves with it.

**Use Case Summary rows.** Outputs and Role take the reviewer's text, with Smart Scales corrected:

| Field | Text to place |
|---|---|
| Outputs | Predicted weight through Smart Scales (beta), BMI values for comparison, 80+ body measurements, body-composition estimates, capture timestamp and capture-quality outcomes |
| Role | Provides structured body-data inputs and discrepancy signals for program review; it does not determine eligibility or payer acceptance |

**Stage 1 of the workflow** takes the reviewer's rewrite, Smart Scales corrected:

> **Stage 1. Remote capture at intake.** After the patient submits the intake questionnaire, the
> program sends a scan link. The patient completes the guided two-photo capture on their smartphone.
> FitXpress returns structured body data, including predicted weight through Smart Scales (beta),
> BMI, body measurements and body-composition estimates. Where self-reported weight is also
> collected, the program can compare the resulting BMI values and route material differences for
> human review.

**Post-operative paragraph** takes the reviewer's rewrite with correction 3 applied:

> Predicted weight can add another consistent data point to remote follow-up. Smart Scales carries a
> ±3.5% average error margin against scale weight under real-world conditions, averaged across
> captures rather than guaranteed on any one of them. Programs should treat it as a software
> estimate and continue using a calibrated scale wherever their clinical protocol requires a
> directly measured weight.

### B5. Operational outcomes presented as established results — **apply, with one carve-out**

Reframe as hypotheses to test, potential workflow benefits, and pilot KPIs. The five phrases the
reviewer named, plus the Use Case Summary **Business value** row, which is the densest concentration
of them (*"Higher consult-to-procedure conversion, fewer measurement-only visits"*). That row becomes
a statement of what a pilot would measure, not what the product delivers.

**Pilot KPIs to list (the reviewer's six, verbatim as a set):** intake completion, retake rate, time
from inquiry to completed body-data record, pre-auth rework, measurement-only appointments, and
follow-up completion.

**Carve-out: the CDC figure itself is already stated correctly.** The draft says *"self-reported BMI
underestimated the prevalence of severe obesity by 40%, at 5.3% on self-report against 8.8% after
bias correction in 2020 data"* — that is exactly the population-level comparison the reviewer
describes, not the misreading they are guarding against. **Do not touch that sentence.** What must
change is the inference drawn from it in the next line, *"a self-reported value is a placeholder
that still has to be verified"*, which generalises a population statistic to every individual
record. Same for the attrition paragraph: the published range and the "that spread is a stronger
case for a standardized intake record" reading are fine; *"Every verification step that requires an
in-person appointment is also a point where a patient can leave the pathway"* is the causal claim
that goes.

### B6. Remove references to unpublished guides — **apply in full**

Seven promises in the body, all of them the prose halves of the `DOWN-LINK LANDING` markers:

| § | Phrase to remove |
|---|---|
| 3 | "and the body-data half of that packet has a dedicated guide of its own" |
| 4 | "which is the subject of a separate guide on GLP-1 before bariatric surgery and body composition" |
| 5 | "What belongs in that record is specified in a dedicated guide to the bariatric patient progress record." |
| 6, Stage 1 | "Remote bariatric intake carries its own workflow questions, treated in a guide to remote body measurement for bariatric patient intake." |
| 6, Stage 2 | "Where a program pairs virtual check-ins with in-person visits, the same capture supports a hybrid bariatric care model, covered separately." |
| 8 | "Tracking body changes beyond weight loss, and the fuller specification of a progress record, are handled in two further guides." |
| 9 | "The payer-facing documentation set behind those records, and the checklist that follows from it, sit in the guides on bariatric pre-authorization documentation and the bariatric patient progress record." |

The hub already owns this material after the P2 fold-in; where a promise is deleted, the sentence
before it must answer the question rather than trail off.

**One more of the same kind the reviewer did not list, and it goes with them:** §10's *"A dedicated
FitXpress privacy and regulatory FAQ, not yet published, holds the fuller detail."* Same defect,
same fix. Note that `publish-package.md` §3c separately (and correctly) forbids *linking* that FAQ;
this decision removes the prose promise as well. §3b's DOWN-LINK table needs rebuilding by the
publisher once the phrases are gone.

### B7. Privacy and compliance paragraph — **split: two applied, one declined**

**(a) "processes no personal identifiers" — apply.** The reviewer is right that it is too broad for
a healthcare page. What `compliance.md` actually records is a *linkage* property (*"photos cannot be
linked to individuals via 3DLOOK"*), which is a narrower statement than "no personal data is
processed". The wellness hub already solved this with a sentence built from the same source
(`2026-08-31-ai-body-data-wellness-platforms-hub/final.md`), and reusing it keeps the two pages
consistent.

**(b) GDPR roles — apply.** The reviewer's formulation is the one the wellness hub adopted and
records in its `review-1-decisions.md` §C as the approved role formulation. See **§E1**: this
sentence is *not* in `compliance.md`, and a second article declined it on exactly that ground eight
days ago. It ships here, and the inconsistency goes to Vadim as a repo-level question, not as a
blocker on this page.

**(c) Photo retention — declined.** The reviewer asks us to drop "or within a configurable retention
window" *"unless that variation has been confirmed for this product"*. It is confirmed:
`compliance.md` Photo retention row reads *"Permanently removed immediately after processing OR
within 30 days, per client policy"*, and the buyer Q&A in the same file repeats it. The defect is
vagueness, not invention, so the fix is the concrete approved wording rather than deletion.

**(d) "outputs are retained" — not added.** The reviewer wants the paragraph to say outputs are
retained while photos are deleted. No approved brand-asset carries a 3DLOOK output-retention
statement; the only text that does is `workspace/seo/faq-data-privacy-security-clean.md`, which is
marked *"Draft — not yet reviewed"*. The reviewer's actual concern is that body data can still be
personal data, and that can be said without a retention claim.

**Text to place, §10 compliance bullet (whole bullet):**

> **Compliance posture.** FitXpress maintains Health Insurance Portability and Accountability Act
> (HIPAA) safeguards in US healthcare contexts and supports Business Associate Agreement execution.
> In most enterprise deployments, the customer acts as controller and 3DLOOK acts as processor under
> the General Data Protection Regulation (GDPR). Data is encrypted at rest in Amazon Web Services S3
> with server-side encryption always on, and in transit over Transport Layer Security. Photos are
> permanently removed immediately after processing, or within 30 days, depending on the client's
> configured policy, and are automatically blurred when stored. FitXpress does not receive names,
> contact details, or other direct identifiers that connect the scan with a specific individual.
> Body data and session-linked outputs can still qualify as personal data, which is the program's
> own assessment to make.

SOC 2 stays unmentioned (`compliance.md`, "What we do NOT claim"). The existing Validation
population and Validation strength bullets are untouched by this review; keep both verbatim.

---

## C. Recommended structure — **apply, mapped**

The reviewer's diagnosis is the right one for a BOFU-weighted hub: the operational answer arrives
around the 45% mark today. Their ten-section order is adopted. It is a reordering and a compression
of material that already exists, plus two new blocks, so it stays inside `edit`; nothing here
reopens the outline or the primary keyword, which is what would have made it a re-plan.

| New # | New section | Comes from |
|---|---|---|
| 1 | Introduction and concise Use Case Summary | New intro (§D1) + today's Use Case Summary with Outputs, Role and Business value rows revised (B4, B5) + the disclaimer, unchanged. Today's §1 market context compresses into two or three sentences here: the CDC prevalence figure and the ASMBS 1% reach figure survive, the attrition paragraph reduces to its range-and-variance point. |
| 2 | What structured remote body data contributes, and what it does not decide | Today's §2, plus the B2 payer-acceptance distinction stated here first. |
| 3 | Remote Body Measurement for Bariatric Patient Intake: A Four-Stage Pre-Qualification Workflow | Today's §6, Stages 1 and 2 rewritten (B4, D2). **Use the reviewer's H2 wording as given** — it carries content-plan row 69's article title, which is how the hub absorbs that P2 intent instead of a standalone page. |
| 4 | Pre-qualification and pre-authorization documentation | Today's §3 with B1 applied, plus the packet-contents paragraph. This is where row 68's intent lands. |
| 5 | The GLP-1 bridge: current BMI, historical BMI and documentation continuity | Today's §5, plus the one surviving indicator from §4 (B3). |
| 6 | Patient progress tracking before and after surgery | Today's §8, with B4's post-op wording and D3. |
| 7 | Where FitXpress fits: outputs, accuracy, repeatability and limitations | Today's §7 plus the "What FitXpress does not do" block from today's §9. |
| 8 | Manual measurement versus guided capture | Today's §10 comparison table with B2's row changes, plus the buyer-fit paragraph. |
| 9 | What to confirm in a bariatric pilot | Today's §10 three evaluation bullets (B7) + today's §9 operational content reframed as hypotheses (B5) + the new pilot-evaluation table (D5) + the pilot KPI list (B5). |
| 10 | Focused FAQs, CTA and relevant reading | Today's §11 reduced (D6) + today's §12 with three links removed (D7). |

---

## D. Additional content improvements

**D1. New introduction — apply, verbatim.** The reviewer's replacement, as written:

> Bariatric programs often collect or verify body measurements during the first consultation. When
> those inputs are missing, inconsistent or captured too late, pre-qualification and
> pre-authorization preparation can require additional follow-up. Structured remote intake can
> provide dated body measurements before the visit, establish a baseline for progress tracking and
> leave eligibility and treatment decisions with the care team.

The two abstract phrases they named go with it: *"which record has to be in the file, dated when,
and for whom to review"* and *"the verification stack most of them still run"*.

**D2. Stage 2 — apply.** Remove *"Patients who clearly meet criteria move into a
clinical-evaluation consult"*, which reads as an eligibility engine. Describe instead the
coordinator confirming completeness and routing the record for authorized human review, and add the
retake or in-clinic fallback where capture quality is insufficient. Grounded: pose validation runs
in real time and the clothing detector prompts the user to adjust (`how-it-works.md`, capture flow steps 3 and 4),
so retake logic is a real behaviour, not an aspiration. This is also the "slightly more operational
detail" the requirements table asks for on the P2 remote-intake row.

**D3. Estimates versus measurements in the post-operative section — apply.** Body-composition
estimates complement weight and circumference trends where the program considers them appropriate.
They are not presented as equivalent to DXA or professional BIA. Use `editorial-guardrails.md` #7's
wording for the boundary, which the page already carries in §9: *"not equivalent to … where the
workflow, protocol or regulatory standard requires those methods."* Do not import the live framework
article's "positioned as equivalent" phrasing; `terminology-guardrails.md` §2.10 fails it
(`accuracy-formulations.md` §2.1).

**D4. "weeks apart" — apply, remove.** `accuracy-formulations.md` §1.2 describes five repeated scans
per participant and states no time separation. The clause claims a protocol we do not have on file.

**D5. Two new blocks.**

- **"one capture asset… replaces the fragmented manual measurements"** becomes the reviewer's line,
  verbatim: *"the same data structure can be generated at multiple pathway stages alongside
  measurements required by the program or payer."*
- **New pilot-evaluation table** in new §9, the reviewer's seven rows: capture completion, quality
  failures and retakes, workflow integration, role-based review, population fit, payer acceptance,
  and data governance. Each row states what a program confirms, not what FitXpress provides.

**D6. FAQ reduction — apply, with one question retained on keyword grounds.** Sixteen questions go
to nine. (The ruling first said eight; the explicit remove-list below names seven of the
sixteen, which leaves nine. The list governs, and picking a tenth question to cut for the sake of
the headline number would be the coordinator inventing an edit the reviewer did not ask for.) Remove the two patient-facing basics questions, *"What is bariatric surgery?"* and *"What
are the main types of bariatric surgery?"*, and remove the five that restate body copy: *"How can
programs reduce wasted bariatric consult slots?"*, *"Why is weight alone not enough for bariatric
progress tracking?"*, *"How can bariatric programs monitor patients remotely after surgery?"*, *"How
is a follow-up scan compared with the baseline?"*, *"Who reviews the scan data?"*

**Retain, and re-home into the pre-qualification and pre-authorization group:** *"What are common
program and payer requirements?"* The reviewer's objection to the basics block is that it attracts
patient-facing informational intent; this question does not, because `plan.md` line 128 targets
`bariatric surgery requirements` (1,100/mo, KD 54, TP 5,000) through it **in the documentation sense
only**, with an explicit boundary that the answer describes what documentation programs and payers
require and never tells a reader whether they personally qualify. The existing answer already
honours that boundary. Dropping it would surrender the one FAQ carrying a keyword with real volume,
for no gain the reviewer asked for. Also update the "Bariatric surgery basics" H3, which no longer
describes anything once its other two questions are gone.

**D7. Internal links — apply.** Remove all three body links the reviewer named: occupational health
screening software (§10), mobile body scanning for insurance underwriting (§12 related reading), and
wellness rewards verification (§12 related reading). `content-strategy-guidelines.md` §11 names this
exact anti-pattern (*"may link to privacy FAQ and accuracy framework, not to unrelated wellness
pages"*).

Two things the editor and publisher both need to know:

- **The insurance-underwriting and wellness-rewards links are on the live page today**, and the
  context pack marks both *"Already present — keep"*. This decision knowingly drops two live
  internal links in exchange for topical focus on a hub. Publisher: record it in the package as a
  deliberate removal so nobody restores it at CMS entry as a "missing link".
- **The link-direction gate still passes.** `article_lint.py` gate 6 needs one link per direction;
  sideways retains GLP-1 market, AI in telehealth and the online-pharmacy BMI compliance guide. The
  online-pharmacy guide **stays** — the reviewer named three targets to remove and it is not one of
  them, and it carries the remote BMI-verification methodology this page deliberately does not
  re-explain.

**D8. Meta description — apply.** The 7-day clock stops being the universal lead. The reviewer's
replacement:

> See how obesity care teams can use remote body data for bariatric pre-qualification, intake,
> pre-auth preparation, and post-op progress tracking.

Publisher: keep it inside the character budget, keep `bariatric pre-qualification` in it, and
re-write §1's "Why this direction" rationale, which currently argues for the payer-clock lead that
this decision reverses. The recommended **meta title** is untouched by this review.

---

## E. Open items for Vadim, neither of them blocking

**E1. RESOLVED 2026-09-07 by Vadim: the GDPR controller/processor sentence is canonical.**

It now lives in `brand-assets/product-info/compliance.md` under "GDPR roles", with pointers from
`proof-points.md`, `how-it-works.md` and `CLAUDE.md` §12, and a changelog row. The hedge "In most
enterprise deployments" is part of the sentence and does not get trimmed. The ruling covers the
roles sentence only: Article 28 DPA, Standard Contractual Clauses, the UK Addendum and Article 9
special-category data stay unapproved. The occupational-health article's R2-3 decline was reversed
the same day and that article now carries the sentence. **B7(b) is unchanged — apply it.** The
history below is kept because it explains why the sentence needed a ruling at all.

**How the three articles had disagreed:**

| Where | Ruling | Date |
|---|---|---|
| `2026-08-31-ai-body-data-wellness-platforms-hub` | **Adopted.** Its `review-1-decisions.md` §C lists it as "the approved role formulation", replacing the vague "follows GDPR principles" | 2026-08-31 |
| `2026-08-26-remote-body-measurement-online-fitness-coaching` | Adopted, used verbatim per its revision-2 changelog | 2026-08-26 |
| `2026-09-03-manual-vs-digital-intake-occupational-health` | **Declined**, open item R2-3, on the ground that no brand-asset carries it | 2026-09-07 |

`compliance.md` says only *"Follows GDPR principles"*. The unreviewed
`workspace/seo/faq-data-privacy-security-clean.md` carries the fuller version (*"the enterprise
customer is the data controller and 3DLOOK is the data processor"*, Article 28 DPA, SCCs, UK
Addendum). **The question for Vadim:** add the controller/processor line to `compliance.md` as
canonical, or strike it from the two articles that ship it. Either answer settles all four places at
once. This page follows the reviewer and the two-article majority in the meantime.

**E2. The reviewer's verdict on the two P2 rows should go back into the content plan.** They rule
that content-plan rows 68 and 69 need no separate pages, that the hub owns both intents once these
edits land, and that a standalone remote-intake page would only be justified if it narrowed to
integration, capture completion, quality control and operational handoffs. That is a content-plan
edit, and the plan is synced from the Google Sheet every Monday, so it belongs in the sheet rather
than in `content-plan.md`.

---

## F. What the editor must not do

1. **Do not touch the H1, the slug, the primary keyword or the byline.** The review does not ask,
   and the first three are checkpoint-1 decisions.
2. **Do not delete the disclaimer** under the Use Case Summary. It is the strongest single sentence
   for B2 and the review implicitly endorses it.
3. **Do not "fix" the CDC sentence** (B5 carve-out) or the §5 Epic Cosmos study (B3).
4. **Do not add an accuracy or repeatability figure that is not already on the page.** The two that
   ship are 96-97% / 1.5-2.0 cm and "less than 1 cm", both verbatim from
   `accuracy-formulations.md`. FX-003 (ISO 0.40 cm) and FX-004 stay out for the reasons in
   `publish-package.md` §3e, which this review does not disturb.
5. **Do not soften a deletion into a hedge.** Where this file says delete (B1a, B3, B6), the
   sentence goes; a "may" version of the same claim is the same claim.
6. **Run `python3 scripts/article_lint.py` on the result** before handing off. Word count will fall
   well below 4,712; that is intended, and it is not a defect to correct by padding.

---

## G. After QC (17/20, 2026-09-07) — three coordinator rulings

`quality-controller` scored the round 17/20 (A 4 · B 4 · C 3 · D 3 · E 3) and confirmed the thing
this file was written to prevent: every "Text to place" block shipped literally, all three
carve-outs in B5 and B3 held, and nothing correct was "fixed". Three findings needed a ruling.

**G1. The ±3.5% passage shipped twice. Resolved: it now ships once, in §6.**
B4 supplied both a "wherever the figure lands" block and a separate post-operative block, and the
editor placed both, leaving ~55 words of the same content in adjacent sections. That is a defect in
this file, not in the edit: B4 should have said the two blocks were alternatives. The figure stays
in **§6, "Where FitXpress fits"**, where it sits beside the two-references explanation and carries
`FX-008`. In §5 the sentence keeps the use and the boundary without repeating the number:

> Predicted weight can add another consistent data point to remote follow-up, and it stays a
> software estimate: a calibrated scale remains the reading wherever the program's clinical protocol
> requires a directly measured weight.

Applied by the coordinator 2026-09-07, `article_lint.py` re-run, PASS. §5 still links the accuracy
framework for the repeatability figure it does carry, so the accuracy-discipline gate is unaffected.

**G2. The §6 heading dropping "repeatability" is correct, and gets disclosed rather than reverted.**
Section C's mapping named the section "outputs, accuracy, repeatability and limitations"; the draft
ships "outputs, accuracy and limitations". The editor did not disclose the change, which is the real
fault. The heading itself is right: the repeatability figure ended up in §5, where longitudinal
comparison is the argument, so a §6 heading promising repeatability would promise something the
section no longer delivers. **Keep the heading. Record the deviation in the package.**

**G3. "Consult-to-procedure conversion" surviving once in §6 is allowed.**
B5 turned outcome claims into hypotheses and KPIs. This one instance names a measure that directors
of operations already own, in the buyer-fit paragraph, and it does not assert that the product moves
it. That is the distinction B5 draws. **Keep it, and put it in the package's open items** so the
next reviewer sees it was a decision.

**The process fault behind G1 and G2, which matters more than either.** Both were flagged by the
editor in its own report and neither reached `publish-package.md`, the file Vadim actually reads.
§3g of that package exists because D7 said "record it in the package"; the same discipline was never
applied to the editor's escalations. Publisher: an editor flag is a package open item unless the
coordinator has ruled it closed, and these three are now ruled.
