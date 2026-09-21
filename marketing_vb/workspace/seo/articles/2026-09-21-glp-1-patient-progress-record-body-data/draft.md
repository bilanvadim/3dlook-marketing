---
slug: 2026-09-21-glp-1-patient-progress-record-body-data
product: fitxpress
section: full
status: draft
author: Assel Sekerova
primary_keyword: glp-1 patient progress record
hub: GLP-1 Market & Progress Tracking (Hub 3)
cluster: Documentation
intent: BOFU
target_words: 2100
word_count: 1961
gate_m1_note: gate 8 flags GLP-1 in the H1, the known title case; expanded at first prose use, title unchanged per plan
claims_used: [FXS-LIFECYCLE, FXS-OUTPUTS, FXS-SPEED, FXS-REPEAT, FXS-DELIVERY, FXS-SCOPE, FXS-MEDICAL, FXS-RETENTION, FXS-IDS, FXS-HIPAA, FXS-GDPR, FXS-POPULATION]
---

# What Body Data Should Be Included in a GLP-1 Patient Progress Record?

By Assel Sekerova

## Why GLP-1 progress records lose their shape

A glucagon-like peptide-1 (GLP-1) program collects body data from several places at once. A patient reports a weight at sign-up. A home scale sends a number six weeks later. A progress photo arrives in a message thread, and a coach writes a note after the call.

Each input lands in its own format, on its own day. From one month to the next, entries rarely hold the same set of fields.

The useful question is which fields every entry has to carry. A GLP-1 patient progress record holds its shape when the answer is the same at every check-in.

Scale weight records that something changed. It does not record what changed, or where.

The cost arrives later. When a payer or employer partner asks what the program achieved, the record has to be reassembled after the fact. Someone reads back through message threads, scale exports, and photos taken at three different distances. The clinical team absorbs that work, and it grows with the number of members enrolled. Wider context on medication-supported weight-loss programs sits in the [GLP-1 market overview](https://3dlook.ai/content-hub/glp-1-market/).

***Scope note.*** *FitXpress provides remote body-measurement capture and structured records. Clinical review, treatment and dosing decisions, and eligibility decisions stay with the program's clinicians. FitXpress is not a medical device.* <!-- claim: FXS-MEDICAL -->

## Short answer: what belongs in a GLP-1 patient progress record

Every entry carries three groups of fields. They cover what enters the system, what the system produces, and what the system logs about the capture.

- **What the patient submits.** Front and side photos, gender, height, and an optional self-reported weight. <!-- claim: FXS-LIFECYCLE --> These are the inputs the capture needs, and each one stays in the entry as its own field.
- **What the scan generates.** 80+ body measurements, which are circumferences, lengths, and widths. Body composition outputs cover BMI, basal metabolic rate (BMR), body fat percentage, lean mass, and fat mass. <!-- claim: FXS-OUTPUTS --> BMI and BMR are calculated metrics, and the composition figures are estimates. The entry also holds a 3D model and scan-to-scan comparison outputs. <!-- claim: FXS-LIFECYCLE -->
- **What the system records about the capture.** Capture-quality and pose-validation flags, clothing classification, face-obfuscation confirmation, and processing logs with timestamps and request metadata. <!-- claim: FXS-LIFECYCLE -->

Capture takes two photos, front and side, and returns the structured outputs in under 45 seconds. <!-- claim: FXS-SPEED -->

The first two groups describe the patient. The third describes the conditions the entry was captured under, which is what tells a coordinator whether the entry can be used.

## Why each group of fields earns its place

### What the patient submits

Height and gender come from the patient, and the capture uses both to generate the rest. <!-- claim: FXS-LIFECYCLE --> The same photo set produces different figures when the stated height changes, which is why both values stay in the entry.

Both values are submitted with each capture, and the entry records the basis its outputs were generated on. An optional self-reported weight keeps its own field. It sits beside the generated figures instead of standing in for them, and the care team can see which number came from where.

Photos are the input to the capture. The stored entry holds the outputs, and photo handling follows the deployment terms the program agreed.

### What the scan generates

Measurements record where the body changed. <!-- claim: FXS-OUTPUTS --> Scale weight alone does not carry that information, and a record built on weight alone cannot answer a question about a specific body area.

Body composition outputs describe what the change is made of. Lean mass and fat mass are held as separate fields, and both are estimates. <!-- claim: FXS-OUTPUTS --> An entry that carries them can be read next to a weight figure instead of in place of one.

A scan-to-scan comparison output allows one entry to be read against an earlier one. <!-- claim: FXS-LIFECYCLE --> Without it, the file holds a series of unrelated snapshots.

### What the capture itself records

Capture-quality and pose-validation flags tell the team whether an entry is usable before anyone compares it. <!-- claim: FXS-LIFECYCLE --> An entry that failed pose validation is a known gap in the timeline. A team that cannot see the flag reads the same entry as a result.

Clothing classification and face-obfuscation confirmation record the conditions of the capture itself. Timestamps place each entry on the timeline.

Processing logs make one entry retrievable months later, when a partner asks about a single time point. The first entry sets the starting point for everything compared afterwards, and standardizing that first capture is its own piece of work.

## Cadence, and why entries stay comparable

The program sets the interval. Many capture at intake and then at the check-ins the care plan already runs.

Cadence is an operational choice. It follows the schedule the program keeps for its own reasons, and the record inherits whatever that schedule produces.

What makes an interval useful is repetition. Each entry repeats the field set and the capture protocol of the one before it. A monthly entry with three fields missing is a gap the team finds later, usually while building a report.

An interval the program cannot sustain produces gaps. Those gaps surface later as missing time points in a partner report. Comparability depends on two things the program controls. The capture protocol has to be the same each time, and the receiving system has to store the entry in the same structure.

Repeatability is the reason two entries can be read against each other at all. Internal repeatability testing used a real-world customer dataset with five scans per participant. For most of the evaluated measurements, typical scan-to-scan differences remained below 1 cm. <!-- claim: FXS-REPEAT --> The [mobile body scanning accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) describes the test conditions and separates repeatability from accuracy.

Small real changes between two check-ins survive into the record when the captures follow the same protocol. For GLP-1 progress tracking, the interval matters less than the consistency of what each entry carries.

The program also selects which scans are compared. FitXpress produces comparison outputs for the two entries the program picks, and that choice stays with the team. <!-- claim: FXS-LIFECYCLE -->

## Where FitXpress fits: capture and delivery

Results reach the program primarily through application programming interface (API) or software development kit (SDK) integration, directly into its own product or interface. <!-- claim: FXS-DELIVERY --> That is where the progress record already lives, in the file a coordinator opens before a check-in.

The integration decides where each entry lands. The program's platform holds the record, and FitXpress supplies the body-data fields inside it. Programs evaluating that route can start from [structured body data for telehealth and digital health programs](https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/).

The FitXpress Admin Panel is the second route, and it is optional. It gives teams that do not want to build their own dashboard a centralized view of scan results. <!-- claim: FXS-DELIVERY --> The [FitXpress Admin Panel launch post](https://3dlook.ai/content-hub/fitxpress-admin-panel-launch/) covers the records and the workflow it holds.

Either route delivers the entry in the same shape. Each one arrives structured and timestamped, with the capture-quality flags and processing logs attached. <!-- claim: FXS-LIFECYCLE -->

The route does not change the fields. A scan captured at home before a check-in and a scan captured during onboarding produce the same entry structure. That consistency is what makes the output a record. A coordinator can open the entry from March and the entry from June and find the same fields in both.

## What FitXpress does not do

FitXpress does not independently determine a diagnosis, a treatment or medication recommendation, insurance eligibility, clinical-trial eligibility, employment eligibility, or any other high-impact individual decision. <!-- claim: FXS-SCOPE --> Final decisions stay with the program's clinicians and other designated decision-makers. <!-- claim: FXS-SCOPE -->

Nothing in the record speaks to the medication itself. The fields describe measured body change and the conditions of each capture. Questions about dosing, response, and treatment plans belong with the care team.

FitXpress is not a medical device. <!-- claim: FXS-MEDICAL -->

What FitXpress supports is narrower. It covers remote intake and body-measurement capture, body composition outputs and Body Progress comparisons, and structured records for workflows the program manages. <!-- claim: FXS-SCOPE -->

## What happens to the record that is kept

Measurements, body composition data, and 3D models are retained on an ongoing basis unless the customer agreement says otherwise. <!-- claim: FXS-RETENTION --> That is what allows a later entry to be compared with an earlier one. Deletion is by scan identifier on the customer's request. <!-- claim: FXS-RETENTION -->

Scan records are associated with anonymized, randomly generated IDs, and 3DLOOK cannot identify a specific individual from stored scan records. <!-- claim: FXS-IDS -->

Procurement teams usually ask about the Health Insurance Portability and Accountability Act (HIPAA) and the General Data Protection Regulation (GDPR). FitXpress can support HIPAA-governed deployments where 3DLOOK acts as a business associate under an executed BAA, where applicable. <!-- claim: FXS-HIPAA --> In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR. <!-- claim: FXS-GDPR --> The [FitXpress privacy, security, and regulatory FAQ](https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/) answers the photo-handling, storage, and documentation questions in full.

## How a program can check its own progress record

A program can audit the record it already has without new tooling. Five counts, taken over the entries of one quarter:

1. Does every entry carry the same fields?
2. Does every entry carry a timestamp?
3. How many entries were captured with a usable pose?
4. How many entries can be compared with the one before them?
5. How often did a manual fallback stand in for a capture?

Each count comes from records the program already holds. The answers show where the record loses its shape. A field missing from one entry in five points at the capture step. A missing timestamp points at the integration.

### Who this fits

The check suits a Head of Clinical Operations, a Care Coordination Manager, a Medical Director, or a Head of Outcomes. It earns its time in remote-first GLP-1 programs running repeat check-ins across more than one site or partner. Those are the programs most often asked to show an enterprise partner what the record contains.

## FAQ

### How is a body-data progress record different from GLP-1 lab monitoring?

Lab monitoring answers clinical questions through bloodwork that the care team orders and reads. A body-data record documents measured body change over time: measurements, body composition estimates, and timestamps. The two sit in the same patient file and answer different questions. FitXpress produces the body-data part and says nothing about labs, dosing, or medication response.

### What happens when a patient cannot complete a scan?

FitXpress was not specifically trained on data representing people with physical disabilities, and its measurement performance has not been established for this population. <!-- claim: FXS-POPULATION --> This matters when a disability affects the standard standing pose or capture sequence. In those cases, the program needs a documented alternative measurement path. <!-- claim: FXS-POPULATION -->

### Can this record confirm eligibility for a GLP-1 program?

Not on its own. FitXpress provides structured intake and supporting documentation for eligibility workflows the customer manages, and it does not independently determine eligibility. <!-- claim: FXS-SCOPE --> The eligibility decision belongs to the program's clinicians. Programs working through remote BMI verification can read the [online pharmacy BMI verification guide](https://3dlook.ai/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/).

### Does a body-data record replace a calibrated scale or a dual-energy X-ray absorptiometry (DXA) scan?

No. It supports remote capture between clinical assessment points. FitXpress is not equivalent to DXA, bioelectrical impedance analysis (BIA), or a calibrated scale when the workflow, protocol, or regulatory standard requires those methods. A program that already uses a reference method keeps it, and the body-data record sits alongside it.

## Next steps

List the fields the current record carries at each entry. Then list the fields it should carry, and start from the gap between the two lists. Most programs find the gap in the third group, the fields that describe the capture.

Then [talk to 3DLOOK about the GLP-1 progress record workflow](https://3dlook.ai/pricing/#bd-modal-personalized), or read what the integration delivers on [structured body data for telehealth and digital health programs](https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/).

Related reading:
- [GLP-1 market overview](https://3dlook.ai/content-hub/glp-1-market/)
- [Remote body composition tools for GLP-1 clinics](https://3dlook.ai/content-hub/top-7-remote-body-composition-tools-glp-1-clinics/)
