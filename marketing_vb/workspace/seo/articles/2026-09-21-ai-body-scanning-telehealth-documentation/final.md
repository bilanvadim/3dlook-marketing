---
slug: 2026-09-21-ai-body-scanning-telehealth-documentation
product: fitxpress
status: edited
author: Assel Sekerova
primary_keyword: telehealth documentation
hub: AI in Telehealth (Hub 2)
cluster: Documentation
intent: BOFU
word_count: 1867
editing_passes: 5
ai_density_before: 0.95
ai_density_after: 0.0
claims_verified: [FX-001, FX-002, FX-003, FX-004, FX-005, FX-006, FX-007, FX-008, FX-009, FX-011]
changes_summary: |
  - Pass 1, citations and repeated facts: the retention sentence and the anonymized-ID sentence
    appeared verbatim in Section 5 and Section 8 (two 1.00 near-duplicate pairs). Section 8 now
    owns both canonical sentences; Section 5 keeps only the operational consequence
    ("a program can retrieve an entry months after capture").
  - Pass 1: the hub link appeared twice with the same long anchor (Section 4 and Related reading,
    0.71 pair). Section 4 now uses the short anchor "AI in telehealth"; the full title stays in
    Related reading.
  - Pass 2, structure: Section 2 lead-in fixed (it announced "three groups" over four bullets);
    the 45-second fact moved into the lead-in sentence. Section 4 closing no longer uses
    corrective "rather than". Related-reading and CTA order unchanged.
  - Pass 3, expert voice: added the approved population limitation (not trained on data
    representing people with physical disabilities, performance not established for that
    population) to the pilot section, where it changes the pilot design. Removed the unquantified
    time-saving claim "returns minutes to the clinical team" and replaced it with a hedge on
    where the gain appears. Two more hedges added as end-clauses (correction handling, gain size).
  - Pass 3: repeated phrases cut. "scan to scan" 4 to 2 in the body plus the approved FAQ figure,
    "the receiving system" 3 to 2, "the capture step" 3 to 2, "enters the record" 3 to 1,
    "body measurement capture" 3 to 2. Actor naming standardized on "the person" (draft mixed
    member / person / patient).
  - Pass 3b: "What FitXpress does not do" kept as its own section (Hub 2 does not own it);
    scope note still early; four link directions intact; BOFU CTA unchanged.
  - Pass 4, polish: editorial call on API and SDK reversed after testing. Both were left bare for
    the clinical-operations and technical-evaluation audience, and gate M1 failed on them, so both
    are expanded on first use ("application programming interface (API)", "software development
    kit (SDK)"). DXA, BIA, BMR, HIPAA, BAA and GDPR stay expanded on first use; BMI stays
    unexpanded per the exception list.
  - Pass 4: stacked negation removed from FAQ 1 ("does not guarantee ... and makes no
    determination" cut to one negative clause) and from Section 7 (three separate boundary
    sentences, one negation each).
  - No new numbers. The only accuracy figure is still "below 1 cm" in FAQ 4, with its dataset
    condition and the framework link on the same answer.
self_check: |
  - Still machine-like on first read: Section 3 was four paragraphs of stated trend with nothing
    a practitioner would only know from doing the work. Fixed by grounding the closing paragraph
    in what the two inputs actually describe (body versus conversation) instead of asserting that
    AI "has entered" documentation.
  - Still machine-like: the article had capability and boundary, but no place where the product
    is weak. Added the approved population limitation to the pilot section, because a pilot design
    is where that limit costs someone real work.
  - Still machine-like: three paragraphs in a row opened with "The ..." in Sections 5 and 6, and
    the closing lines of Section 5 and Section 6 both ran as summary verdicts. Openings varied;
    Section 6 now ends on how corrections and recalculation actually behave.
  - Still machine-like: "the capture step" and "scan-to-scan" had become refrains carrying no new
    information after their second use. Reduced to the uses that name a real thing.
  - sentence length gate after edits: mean_words 12.9, over_25 = 0 (0.0%), over_35 = 0;
    near_duplicate_pairs none.
---

# Telehealth Documentation: How AI Body Scanning Creates More Consistent Records

By Assel Sekerova

## Where telehealth documentation loses consistency

A telehealth record usually collects body data from three places. The person reports a weight at sign-up, a home scale reports a different one later, and a progress photo arrives in a message thread. Each input lands in its own format, on its own day.

Consistency is decided at capture. What a program collects at intake sets what it can retrieve and compare later.

Self-reported weight and height are hard to verify at intake. Staff re-enter values and chase missing fields before a consultation can start. That work sits with the clinical team, and it grows with volume.

The cost shows up later. A care coordinator opens a record before a check-in and finds four entries in three formats. A program lead builds an outcomes summary for a payer partner, and two of the time points have no usable entry at all.

***Scope note.*** *FitXpress provides remote body-measurement capture and structured records. The program's own systems hold the rest of the chart. Clinical review, treatment decisions, and eligibility decisions stay with the program's clinicians. FitXpress is not a medical device.*

## Short answer: what a structured body-data record contains

A guided two-photo scan returns structured outputs in under 45 seconds. <!-- claim: FX-004 --> The entry it produces carries three groups of data.

- **What the person submits.** Front and side photos, gender, height, and optionally weight. <!-- claim: FX-002 -->
- **What the scan generates.** 80+ body measurements, a 3D model, and scan-to-scan comparison outputs. Calculated metrics include BMI and basal metabolic rate (BMR). Body composition estimates cover body fat percentage, lean mass, and fat mass. <!-- claim: FX-002 --> <!-- claim: FX-005 -->
- **What the system records technically.** Capture-quality and pose-validation flags, clothing classification, face-obfuscation confirmation, and processing logs with timestamps and request metadata. <!-- claim: FX-002 -->

Body measurements are circumferences, lengths, and widths. BMI and BMR are calculated from the inputs, and body composition figures are estimates. The distinction matters when a program decides which fields it stores and which ones it compares over time.

## Why record consistency is under pressure now

Remote-first programs grew faster than their intake did. Consultation capacity moved online early, and the record-keeping around it often stayed manual.

Programs are also asked to show their work. Payers, employers, and regulators expect outcomes traceable to a dated, consistent entry. A summary built from mixed inputs is harder to defend than one built from entries that share a format.

Documentation expectations for telehealth keep being revised. Each revision lands on the same operational question: which fields the program captures, and whether it can retrieve them later.

AI reached documentation work first through note-taking tools that draft the visit summary. Body data is a separate input to the same record. It arrives before the consultation, and it describes the body while the note describes the conversation.

## Where body data enters a telehealth workflow

Body data reaches a telehealth program at three points. The workflow around each one decides how much of it lands in the record in usable form. [AI in telehealth](https://3dlook.ai/content-hub/the-potential-of-ai-in-telehealth/) covers the wider picture of remote-care workflows, privacy, and patient experience.

### At intake

Remote capture runs before the first consultation. The person completes a guided two-photo scan on a smartphone, and the record exists before anyone opens it for review. <!-- claim: FX-006 --> Programs that verify BMI as part of eligibility follow a separate path, covered in the guide to [remote BMI verification for online pharmacies](https://3dlook.ai/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/).

### Between visits

Repeat capture happens at intervals the program chooses. Each capture produces an entry in the same format, with its own timestamp. The program selects which scans it compares. <!-- claim: FX-006 -->

### Before clinician review

The record is retrieved in one place ahead of the consultation. Missing or low-quality captures become visible earlier, while there is still time to repeat them. Testing, physical examination, and clinical judgment stay with the provider. <!-- claim: FX-006 -->

Documentation of a telehealth physical exam still rests on what the provider observes and writes during the visit. Remote capture changes when the measurement data arrives, and what shape it arrives in. Telehealth visit documentation requirements are set by the program and its advisors, and remote capture supplies input to them.

## Where FitXpress fits: capture, records, and the Admin Panel

[FitXpress](https://3dlook.ai/) provides the capture step. What reaches the program afterwards is one structured entry per scan.

Delivery runs on two routes, and most programs take the first. Results come back through the FitXpress application programming interface (API) or software development kit (SDK), directly into the product the program already runs. <!-- claim: FX-001 --> The person stays inside one experience, and the outputs land in the system that holds the rest of the record. The page on [structured body data for telehealth and digital health programs](https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/) describes what an integration covers.

The FitXpress Admin Panel is the optional second route. It gives teams a centralized view and management of scan results without building a dashboard of their own. <!-- claim: FX-001 --> The [FitXpress Admin Panel launch post](https://3dlook.ai/content-hub/fitxpress-admin-panel-launch/) describes the feature.

Both routes leave a record behind. A program can retrieve an entry months after capture, which is what makes any later comparison possible. <!-- claim: FX-003 --> Every entry carries a timestamp and processing metadata. <!-- claim: FX-002 -->

The timing of an entry matters as much as its contents. A record that exists before review is available to whoever opens the chart, in the same shape every time.

## What changes in the record

What changes is the shape of the entry. Who reviews it, and who decides, stays the same.

| **What the record carries** | **Fragmented intake inputs** | **Structured body-data record** |
|---|---|---|
| Fields on each entry | Vary with the source and the visit | The same set every time |
| Timestamp | Depends on when someone logged the item | Applied at capture, on every entry |
| Format | Free text, images, and scale readings | Structured outputs in one shape |
| Availability before review | Assembled during or just before the consultation | Present in the record before review begins |
| Manual re-entry | Often needed to move values into the system | Reduced where the integration carries the values |
| Comparison across time points | Limited by differing formats | Supported, because entries share a format |

A record that carries the same fields every time is quicker to read and easier to compare. <!-- claim: FX-002 --> Less of it has to be rebuilt inside the consultation, although the size of that gain depends on how much was missing before.

Manual re-entry falls where the integration carries values into the program's system, although that system still decides how corrections are handled. Entries stay comparable over time because they are retained and share a format. <!-- claim: FX-003 --> Calculated metrics and body composition estimates are recalculated on each scan, and each entry shows the figures from that day. <!-- claim: FX-005 -->

## What FitXpress does not do

FitXpress supports remote intake and body-measurement capture, body composition outputs, and comparison of the scans a program selects. It also covers structured data collection for research protocols, and documentation that supports workflows the customer manages. <!-- claim: FX-006 -->

It does not independently determine a diagnosis, a treatment or medication recommendation, insurance or clinical-trial eligibility, employment eligibility, or any other high-impact individual decision. <!-- claim: FX-006 --> Final decisions stay with the program's clinicians, underwriters, and other designated decision-makers. <!-- claim: FX-006 -->

Remote capture does not replace clinician review, dual-energy X-ray absorptiometry (DXA), bioelectrical impedance analysis (BIA), or calibrated scales. Those methods answer different questions under different conditions. Where a program needs a reference-method measurement, remote capture sits alongside it. FitXpress is not a medical device.

## Data handling, retention, and access

Measurements, body composition data, and 3D models are retained on an ongoing basis unless the customer agreement says otherwise. <!-- claim: FX-003 --> Deletion is by scan identifier, on the customer's request. <!-- claim: FX-003 --> Scan records are associated with anonymized, randomly generated identifiers, and 3DLOOK cannot identify a specific individual from stored scan records. <!-- claim: FX-009 -->

FitXpress can support deployments governed by the Health Insurance Portability and Accountability Act (HIPAA). In those deployments 3DLOOK acts as a business associate under an executed Business Associate Agreement (BAA), where applicable. <!-- claim: FX-007 --> In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under the General Data Protection Regulation (GDPR). <!-- claim: FX-008 -->

Procurement and security reviews of secure telehealth documentation platforms go further than retention and legal roles. The [FitXpress data, privacy, security, and regulatory FAQ](https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/) answers the rest, including storage regions, photo handling, and model training.

## How to evaluate documentation consistency in a pilot

A capture change earns its place where the existing gap is in intake. If records are already complete and comparable, moving the capture step will not return much.

Five measures describe the record before and during a pilot:

- Completion rate of remote capture, by cohort.
- Share of records complete at the point of review.
- How often a value is re-entered manually.
- How often the manual fallback path is used.
- How many entries are comparable across time points.

Each of those is something the program measures in its own systems. None of them is a result to expect in advance. Baselines taken before launch make the second reading worth having.

One limit belongs in the pilot design from the start. FitXpress was not specifically trained on data representing people with physical disabilities, and its measurement performance has not been established for this population. <!-- claim: FX-012 --> This matters when a disability affects the standard standing pose or capture sequence.

### Who this fits

Remote-first programs running repeat check-ins across more than one site or partner. The roles that usually own the decision are Head of Clinical Operations, Care Coordination Manager, and Medical Director. A single-site program with low volume and a complete paper trail has less to gain.

## Next steps

Compare the inputs the program collects today against what the record has to carry at review, and name the fields that arrive inconsistently. Then [talk to 3DLOOK about the telehealth intake workflow](https://3dlook.ai/pricing/#bd-modal-personalized).

Related reading:

- [AI in telehealth: workflows, privacy, patient experience, and remote body data use cases](https://3dlook.ai/content-hub/the-potential-of-ai-in-telehealth/)
- [How mobile body scanning improves patient engagement](https://3dlook.ai/content-hub/mobile-body-scanning-patient-engagement/)

## FAQ

### Can body scan records help a telehealth program meet its documentation requirements?

The program and its advisors decide which documentation requirements for telehealth apply and how records are used. FitXpress provides structured, timestamped records that enter the program's own process. It does not guarantee compliance or certify a program's records.

### How is this different from AI tools that draft telehealth visit notes?

Note-taking tools capture what was said during a consultation and turn it into a summary. FitXpress captures body-measurement data before the consultation and returns it as a structured record. Programs reviewing AI tools for telehealth visit documentation are usually solving a different part of the chart. The two inputs meet in the same record, from different points in the workflow.

### What happens when a patient cannot complete a remote scan?

Some people lack a suitable device or a stable connection. Others cannot hold the capture pose. The program, therefore, needs a documented manual alternative, and a rule for how a measurement taken that way joins the record. <!-- claim: FX-006 -->

### Do repeat scans produce comparable entries over time?

Comparability depends on the capture protocol and on the receiving system. Internal repeatability testing used a real-world customer dataset with five scans per participant. For most of the evaluated measurements, typical scan-to-scan differences remained below 1 cm. <!-- claim: FX-011 --> The [mobile body scanning accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) describes the test conditions and separates repeatability from accuracy.
