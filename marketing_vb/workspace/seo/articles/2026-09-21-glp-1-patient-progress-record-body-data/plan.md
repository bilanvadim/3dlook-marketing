---
slug: 2026-09-21-glp-1-patient-progress-record-body-data
product: fitxpress
author: Assel Sekerova
primary_keyword: glp-1 patient progress record
primary_use_case: "Telehealth & GLP-1 / Weight Loss Programs (icp-detail.md #1), progress-record composition slice"
hub: GLP-1 Market & Progress Tracking (Hub 3)
cluster: Documentation
intent: BOFU
action_type: create-net-new
priority: P1
target_words: 2100
status: approved
created: 2026-09-21
audit: plan-audit.md
---

# SEO Plan, 2026-09-21-glp-1-patient-progress-record-body-data

**Mode:** no-checkpoint run (2026-09-21). This plan goes to the write stage once the plan lint
passes. Vadim reviews post-factum; every contested call and open item sits in `plan-audit.md`.

## Content Strategy Fit (Phase 0)

- **Hub / cluster:** GLP-1 Market & Progress Tracking (Hub 3) → Documentation
- **Action type:** "Create net-new" (verbatim from the sheet row, content-plan.md:163), resolved by the coordinator. GO.
- **Angle:** record COMPOSITION. Which body-data fields belong in a GLP-1 patient progress record, why each group is there, and at what cadence entries stay comparable. Operational, not clinical.
- **Existing pages:** `glp-1-market` is the up-link only, its market and progress thesis is not repeated. `fitxpress-admin-panel-launch` is the named row anchor, linked from the delivery section. `online-pharmacy-bmi-verification-a-2026-compliance-guide` is a link only, its workflow is never re-explained. `top-7-remote-body-composition-tools-glp-1-clinics` is optional related reading.
- **Cannibalization guardrail:** Hub 3 preamble, every GLP-1 supporting asset owns a distinct intent and does not repeat GLP-1 Market, Online Pharmacy BMI Verification, Visual Progress Tracking or the GLP-1 tools list. Three live boundaries apply here: no market growth, no buyer tools comparison, no BMI or eligibility workflow. Two planning boundaries apply as well: the sister P1 row owns BASELINE standardization (one passing sentence here, never a section), and the same-day Hub 2 sibling owns record CONSISTENCY across telehealth (this one owns which fields a GLP-1 entry carries). Full reasoning in `plan-audit.md`.
- **Vertical boundary:** GLP-1 owns medication-supported weight-loss progress tracking, body composition, patient records, clinic workflows and tools for GLP-1 clinics. No dosing, no eligibility criteria, no diagnosis framing anywhere. Record fields are operational, never clinical recommendations. No claim about the medication itself, only about the body-data layer around it. FitXpress is not a medical device.
- **Internal links planned:** up → `glp-1-market` (Section 1) · side → `fitxpress-admin-panel-launch` (Section 5), `online-pharmacy-bmi-verification-a-2026-compliance-guide` (FAQ 3), `top-7-remote-body-composition-tools-glp-1-clinics` (Section 10 related reading) · down → `https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/` and no other product URL · trust → `mobile-body-scanning-accuracy` (Section 4, the only figure in the draft), `fitxpress-data-privacy-security-regulatory-faq` (Section 7).

## Keyword Analysis

### Primary cluster

- **Primary keyword:** glp-1 patient progress record
- **Monthly volume:** no data (Ahrefs returns null for the phrase). **Difficulty:** no data.
- **Seed had data:** no (`seed_has_data: false`).

**Stated plainly, because it changes how this page should be judged.** There is no measured
search demand for this topic in any phrasing close to its actual intent. The exact seed and its
close variants ("glp-1 patient progress", "patient progress record", "glp-1 progress tracking")
all return no data. "glp-1 progress" is a measured zero, which is a different fact from no data.
The only head term with a number, "glp-1 patient" at 10/mo, pulled the automatic idea set toward
patient-assistance programs, education PDFs and portal logins, so none of the 40 generated ideas
touch this subject. Nothing was substituted for the seed, because there was nothing to substitute
that matched the intent.

So this is a sales-support BOFU and GEO asset, not a traffic play:

1. It answers a direct question in the shape an AI answer engine can quote, which is where this
   query actually gets asked today.
2. It is the documentation anchor the Hub 3 row needs for the FitXpress Admin Panel post and the
   BMI-verification guide.
3. It gives sales and clinical-operations conversations one page that lists what a progress
   record carries.

Judge it on assisted conversions, sales use and AI-answer citations, not on sessions. Ranking
targets for this slug would be a fiction. Logged as open item 1 in `plan-audit.md`.

### Adjacent pocket, measured but off-intent

| Keyword | Volume | KD | Intent | Where it goes |
|---|---|---|---|---|
| glp-1 monitoring tools for home use | 60 | no data | commercial, clinical | Not targeted. Lab and home-monitoring intent |
| glp-1 lab monitoring | 30 | no data | informational, clinical | FAQ 1 only, as the boundary question |
| glp-1 blood work monitoring | 20 | no data | informational, clinical | Not targeted |
| glp-1 monitoring | 10 | no data | informational | FAQ 1 only |
| glp-1 patient | 10 | no data | navigational, mixed | Section 1, natural weave |
| glp-1 progress | 0 | no data | informational | Measured zero, not a target |
| glp-1 progress tracking | no data | no data | informational | Section 4, passing mention at most |

"no data" means Ahrefs returns null for that phrase. It is not a zero, and the two are not
merged anywhere in this plan.

**The monitoring pocket is bloodwork and dosage follow-up intent, not documentation intent.** It
appears in exactly one place, FAQ 1, phrased as the difference between a body-data record and lab
monitoring. Chasing it anywhere else would pull the draft into clinical territory this vertical
does not own.

## Recommended Title

**H1:** What Body Data Should Be Included in a GLP-1 Patient Progress Record?

The question format is the asset here. With no keyword to chase, the ranking surface is the
direct-question query, and a title that matches the question verbatim is what an answer engine
can lift. The primary keyword sits in the last four words of the H1 and is repeated verbatim in
the Section 2 heading, which is what the keyword gate checks. No em dash, no content-plan labels,
no clinical promise.

### Rejected

1. *GLP-1 Patient Progress Records: Which Body Data Fields to Capture and When.* Declarative and
   keyword-forward, but it drops the question match that is this page's only real distribution
   route. Keep it as the social and outreach phrasing.
2. *Body Data for GLP-1 Progress Tracking: A Documentation Checklist.* "Progress tracking" reads
   as the hub's own thesis, and "checklist" promises a downloadable asset that is not being built.
3. *What to Track in a GLP-1 Program Beyond Scale Weight.* Drifts into the progress-visibility
   and engagement angle that other pages own, and "what to track" invites clinical reading.
4. *GLP-1 Progress Documentation: What Belongs in the Patient Record.* Closest runner-up, but
   "documentation" as the lead noun collides with the same-day Hub 2 sibling's territory.

### Meta angle (starting point for seo-meta-generator, not final)

- Angle: a progress record is only as useful as the fields every entry carries, and those fields
  can be named.
- Draft title: What Belongs in a GLP-1 Patient Progress Record
- Draft description: The body-data fields a GLP-1 progress record carries at each entry, why each
  group is there, and what keeps entries comparable over time.

## Voice guardrails for this draft

Mean sentence length under 16 words, gate 10. Write like this:

- "A progress record is useful when every entry carries the same fields."
- "Scale weight records the change. It does not record what changed."
- "The program chooses the interval and selects which scans are compared."
- "Clinical decisions stay with the care team."

Hard bans that bite most often here: em dash anywhere including headings, "objective" about our
outputs, "this article", "plus" as a connector, "so" introducing a benefit, "positioned as".
Write "80+ body measurements", never "body metrics". BMI and BMR are calculated metrics, body
composition figures are estimates. Never write "processed, not stored", "no personal identifiers",
"HIPAA compliant", "SOC 2 certified" or "FitXpress tracks each patient over time". Do not call the
record "audit-ready" or "compliant"; say it is structured, timestamped and retrievable.

**Abbreviations, gate 8.** Expand at first prose use: glucagon-like peptide-1 (GLP-1) in Section 1,
application programming interface (API) and software development kit (SDK) in Section 5, Health
Insurance Portability and Accountability Act (HIPAA) and General Data Protection Regulation (GDPR)
in Section 7, basal metabolic rate (BMR) in Section 2, dual-energy X-ray absorptiometry (DXA) and
bioelectrical impedance analysis (BIA) in FAQ 4. BMI is on the commonly-known list and stays
unexpanded. GLP-1 also appears in the H1, which sits before any prose: if gate 8 still flags it,
that is the known title case shared with the live GLP-1 articles, and the editor rules on it. The
title does not change for the gate.

**No customer names.** Yazen and every other client stay out of the draft, the meta, the alt text,
the FAQ and the publish package. If a case reference helps, write "a weight-loss management
platform" with no geography.

## Article Outline

### Section 1. Why GLP-1 progress records lose their shape

- **Goal:** name the composition problem in the record itself, then scope the piece.
- **Words:** 200
- **Must-cover:** entries arrive from different places, self-reported weight, a home scale, patient
  photos, a coach's note; entries do not carry the same fields from month to month; scale weight
  records that something changed without recording what changed; when a payer or employer partner
  asks what the program achieved, the record has to be reassembled after the fact.
- **Open with the plain-statement reframe:** the useful question is which fields every entry has to
  carry. No rhetorical question, no "what most teams get wrong".
- **Claims:** none. Pain points come from the ICP block in the pack.
- **Ends with the scope note, italic, early:** FitXpress provides remote body-measurement capture
  and structured records. Clinical review, treatment and dosing decisions, and eligibility
  decisions stay with the program's clinicians. FitXpress is not a medical device.
- **Links:** up-link to the GLP-1 market hub once, descriptive anchor, no label words.
- **Keywords:** glp-1 patient progress record (once, naturally), glp-1 patient.
- **Boundary:** no market sizing, no growth statistics, no dosing, no eligibility criteria.

### Section 2. Short answer: what belongs in a GLP-1 patient progress record

- **Goal:** answer the title question directly, in bullets, early enough for an answer engine to
  lift the passage whole.
- **Words:** 240
- **Structure:** one short lead sentence, then three labelled bullet groups, then one closing line.
- **Must-cover, in three groups:**
  - **What the patient submits:** front and side photos, gender, height, optional weight.
  - **What the scan generates:** 80+ body measurements, BMI, BMR, body fat percentage, lean mass,
    fat mass, a 3D model, scan-to-scan comparison outputs.
  - **What the system records about the capture:** capture-quality and pose-validation flags,
    clothing classification, face-obfuscation confirmation, processing logs with timestamps and
    request metadata.
  - Closing line: capture uses two photos and returns structured outputs in under 45 seconds.
- **Claims:** FXS-LIFECYCLE (anchor), FXS-OUTPUTS (anchor), FXS-SPEED.
- **Keywords:** the H2 carries the primary keyword verbatim, which gate 7 requires. Do not reword
  this heading.
- **Boundary:** body measurements are circumferences, lengths and widths; BMI and BMR are
  calculated metrics; body composition figures are estimates. Keep that distinction inside the
  bullet wording. Invent no field beyond these two claims: no scores, no risk flags, no export
  formats, no audit trail, no charts.

### Section 3. Why each group of fields earns its place

- **Goal:** the reasoning layer, which is what makes this page different from a feature list.
- **Words:** 330
- **Structure:** three H3s, prose under each, two to four sentences per idea.
  - **H3 What the patient submits.** Height and gender condition the generated outputs. An optional
    self-reported weight sits in the entry next to the generated figures instead of replacing them.
    Photos are the input to the capture, not the record itself.
  - **H3 What the scan generates.** Measurements record where the body changed, which scale weight
    alone cannot show. Body composition estimates describe what the change is made of, lean mass
    and fat mass separately. A scan-to-scan comparison output is what makes two entries readable
    side by side rather than two unrelated snapshots.
  - **H3 What the capture itself records.** Capture-quality and pose-validation flags tell the team
    whether an entry is usable before anyone compares it. Timestamps place the entry on a timeline.
    Processing logs make a specific entry retrievable later.
- **Claims:** FXS-LIFECYCLE, FXS-OUTPUTS.
- **Keywords:** glp-1 patient progress record (once more at most), body data.
- **Boundary:** no clinical interpretation of any field, no thresholds, no statement that a change
  in a field means anything about treatment or medication response. One passing sentence at most on
  the first entry serving as a starting point; baseline standardization belongs to a separate
  planned article and must not become a section here.

### Section 4. Cadence, and why entries stay comparable

- **Words:** 250
- **Must-cover:** the program sets the interval, commonly at intake and then at intervals it
  chooses; the same fields and the same capture protocol at every entry; comparability depends on
  the capture protocol and on the receiving system; repeatability is the reason two entries can be
  read against each other at all; the program selects which scans are compared.
- **Claims:** FXS-REPEAT, in the same paragraph as the framework link.
- **Accuracy discipline:** this is the only figure in the entire draft. Write "below 1 cm" or
  "< 1 cm", keep the condition attached (repeated scans, most of the evaluated measurements), and
  link the [mobile body scanning accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/)
  from that same paragraph. Do not add the 96-97% or 1.5-2.0 cm figures anywhere in the draft. Never
  place an internal figure and the ISO 8559 figure in one paragraph.
- **Keywords:** glp-1 progress tracking, passing mention only.
- **Boundary:** cadence is an operational choice the program makes. No follow-up interval
  recommendation, no dosing schedule, no clinical monitoring framing. Never write "FitXpress tracks
  each patient over time"; the program compares scans it selects.

### Section 5. Where FitXpress fits: capture and delivery

- **Goal:** the anchor section. Lead with API and SDK integration, present the Admin Panel second
  as the optional route, per the delivery wording fixed for both same-day articles.
- **Words:** 290
- **Must-cover, in this order:** (1) primary route, integration via API or SDK, with results
  delivered directly into the program's own product or interface, which is where the record already
  lives; (2) optional route, the FitXpress Admin Panel as a centralized view of scan results for
  teams that do not want to build their own dashboard; (3) each entry arrives structured and
  timestamped, in the same shape every time, which is what makes it a record and not a report.
- **Claims:** FXS-DELIVERY (anchor), FXS-LIFECYCLE (technical fields, timestamps).
- **Naming:** "FitXpress Admin Panel", exactly. No softening to "vendor console".
- **Links:** sideways to the Admin Panel post from the Admin Panel sentence. Down-link once to
  `https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/`.
- **Boundary:** no export formats, dashboards, role-based permissions, EHR integrations, alerts,
  webhooks or audit logs beyond the approved claims. Describe delivery and the shape of the entry,
  nothing past that. No accuracy figure here. Retention belongs to Section 7, not here.

### Section 6. What FitXpress does not do

- **Goal:** state the limits in claim terms, once, in the same register as the capability sections.
- **Words:** 140
- **Must-cover:** it does not independently determine a diagnosis, a treatment or medication
  recommendation, insurance or clinical-trial or employment eligibility, or any other high-impact
  individual decision; final decisions stay with the program's clinicians and other designated
  decision-makers; nothing in the record speaks to the medication itself, only to the body-data
  layer around it; FitXpress is not a medical device.
- **Claims:** FXS-SCOPE, FXS-MEDICAL.
- **Boundary:** write "FitXpress is not a medical device." exactly, never "positioned as". State
  the boundary at claim level only: the eligibility question is answered in FAQ 3 and the
  reference-method question in FAQ 4, so do not pre-answer either here, and do not restate the data
  handling facts that belong to Section 7.

### Section 7. What happens to the record that is kept

- **Goal:** short, factual, pointed at the trust FAQ. Do not restate the FAQ.
- **Words:** 130
- **Must-cover:** measurements, body composition data and 3D models are retained on an ongoing
  basis unless the customer agreement says otherwise, which is what allows a later entry to be
  compared with an earlier one; deletion is by scan identifier on the customer's request; scan
  records are associated with anonymized, randomly generated IDs and 3DLOOK cannot identify a
  specific individual from stored scan records; FitXpress can support HIPAA-governed deployments
  where 3DLOOK acts as a business associate under an executed BAA, where applicable; in most
  enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data
  processor under GDPR.
- **Claims:** FXS-RETENTION, FXS-IDS, FXS-HIPAA, FXS-GDPR.
- **Links:** trust link to the privacy, security and regulatory FAQ, from this paragraph.
- **Boundary:** five or six sentences, then the link. The GDPR sentence keeps the words "the data".
  No "HIPAA compliant", no "SOC 2 certified", no "no personal identifiers", no "processed, not
  stored". Photo handling is the FAQ's territory, one clause at most here.

### Section 8. How a program can check its own progress record

- **Goal:** give a clinical-operations reader something to run this quarter, and name who this fits.
- **Words:** 180
- **Must-cover, as a short numbered check:** does every entry carry the same fields; does every
  entry carry a timestamp; how many entries were captured with a usable pose; how many entries can
  be compared with the one before them; how often a manual fallback was used instead of a capture.
- **H3 Who this fits:** Head of Clinical Operations, Care Coordination Manager, Medical Director,
  Head of Outcomes, in remote-first GLP-1 programs running repeat check-ins across more than one
  site or partner.
- **Claims:** none required. Every item is something the program counts for itself.
- **Boundary:** no benchmark percentages, no ROI figure, no "programs typically see". Say what the
  record can show a partner, never what it guarantees. Do not promise defensible outcomes.

### Section 9. FAQ

- **Words:** 250 across four questions. Two to five sentences each, direct answer first.
- **Rule:** none of these repeats a body section. Do not add a fifth question that Section 2,
  Section 6, Section 7 or Section 8 already answers.

1. **How is a body-data progress record different from GLP-1 lab monitoring?** Lab monitoring
   answers clinical questions through bloodwork that the care team orders and reads. A body-data
   record documents measured body change over time: measurements, body composition estimates,
   timestamps. The two sit in the same patient file and answer different questions. FitXpress
   produces the body-data part and says nothing about labs, dosing or medication response.
   *(keywords: glp-1 monitoring, glp-1 lab monitoring. This is the only place the monitoring pocket
   appears. No test names, no clinical interpretation, no dosing.)*
2. **What happens when a patient cannot complete a scan?** FitXpress was not specifically trained
   on data representing people with physical disabilities, and its measurement performance has not
   been established for this population. This matters when a disability affects the standard
   standing pose or capture sequence. In those cases, the program needs a documented alternative
   measurement path. *(claim: FXS-POPULATION, the sentences as approved.)*
3. **Can this record confirm eligibility for a GLP-1 program?** Not on its own. FitXpress provides
   structured intake and supporting documentation for eligibility workflows the customer manages,
   and it does not independently determine eligibility. Final decisions stay with the program's
   clinicians. One sentence links the [online pharmacy BMI verification guide](https://3dlook.ai/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/)
   for programs working through remote BMI verification, and the workflow itself is never
   re-explained here. *(claim: FXS-SCOPE.)*
4. **Does a body-data record replace a calibrated scale, a DXA scan or BIA?** No. It supports
   remote capture between clinical assessment points, and it does not replace clinician review,
   calibrated scales, DXA or BIA. A program that already uses a reference method keeps it, and the
   body-data record sits alongside it. *(claims discipline; expand DXA and BIA here, gate 8. Spell
   it DXA; the older spelling belongs only in a search term or a published slug.)*

### Section 10. Next steps

- **Goal:** BOFU close, two or three sentences.
- **Words:** 90
- **Must-cover:** list the fields the current record carries at each entry, then the fields it
  should carry, and start from the gap between the two.
- **CTA (BOFU, direct):** primary link to
  `https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/`, along with
  "talk to 3DLOOK about the GLP-1 progress record workflow" at
  `https://3dlook.ai/pricing/#bd-modal-personalized`, the anchor pattern the live occupational
  health article uses.
- **Related reading, two items:** the GLP-1 market hub page and the remote body composition tools
  listicle, both with descriptive anchors.

## Article meta

- **Target:** 2100 words of prose (range 1,900 to 2,300, matching the live occupational-health
  intake article at ~1,877). Section budgets sum to 2,100.
- Estimated read time: 9 minutes
- Sections: 10 numbered sections including the FAQ, 4 H3s (three in Section 3, one in Section 8)
- **Tables: none.** The field list appears once, as bullets in Section 2. A table would repeat it
  and would copy the shape of the same-day sibling article. Reasoning in `plan-audit.md`.
- **Visuals:** cover image, and at most one in-text visual.

| Name | Placement | Concept |
|---|---|---|
| Cover | Top | One progress entry rendered as three grouped field blocks, submitted, generated, technical, on the brand navy background |
| Entry over time | Section 4, optional | Two entries side by side at two dates, same field slots filled in both, showing what comparability means in practice. Skip it if the prose already carries the point |

- CTA placement: Section 10 only, BOFU direct. No mid-article CTA.
- Internal links: up (1), sideways (3), down (1, the product page URL and no other), trust (2)
- Author: Assel Sekerova
