---
slug: 2026-09-03-manual-vs-digital-intake-occupational-health
review: 2
source: >
  Google Doc "Article - Manual Intake vs Digital Intake in Occupational Health Screening",
  tab "Review 2" (t.9ltdnz6zu0ug), heading h.vfkq9lbxo5ik.
  https://docs.google.com/document/d/14y0xQ5MbrM6Xb56gdNVDYa6LfWoy451D5bdfIaYW668/edit?tab=t.9ltdnz6zu0ug
pulled: 2026-09-07
pulled_by: oo connector googledocs get_document_by_id (include_tabs_content=true)
reviews: final.md revision 3 == doc tab "Version 2" (t.tu0rpu3uja72), verified sentence-for-sentence
fidelity: VERBATIM. Nothing reconstructed, nothing paraphrased. Soft line breaks restored.
decisions: review-2-decisions.md
---

# Review 2 — verbatim

## Remaining essential corrections
### 1. The intake-versus-screening distinction is still inconsistent
The heading says:
The three phases of occupational health intake
But on-site testing and clinical review are not phases of intake. They belong to the wider occupational health screening workflow.
Change the heading to:
The three phases of the occupational health screening workflow
Change the opening to:
The occupational health screening workflow has three phases. A remote intake channel reaches the first, while testing, examination and clinical review remain within the wider screening process.
Update the figure label accordingly.
The same problem remains in these statements:
Manual intake reaches every phase.
All three, since the person is on site.
Manual intake does not “reach” clinical review merely because the person is present. Replace the table row with:
| Dimension | Manual intake | Digital intake |
| Relationship to the wider workflow | Intake is completed at or around the visit; testing and review follow | Eligible intake is completed before the visit; testing and review follow |
The short-answer bullet could become:
Neither method wins outright. Manual intake combines data collection with the on-site visit. Digital intake moves eligible steps before the appointment, while testing, examination and clinical review remain unchanged.
### 2. One sentence incorrectly describes both methods
Current wording:
Both are captured and transcribed under appointment-time pressure...
“Both” refers to the questionnaire and measurement, but the sentence can initially sound as though both intake methods operate under appointment pressure.
Use:
The operational cost sits inside that overlap. In manual workflows, questionnaires and measurements are often collected or transcribed at or around the appointment. Missing or inconsistent information can then delay review or require follow-up.
### 3. Several table rows remain too absolute
I recommend these changes:
| Current row | Recommended revision |
| Where the step happens: “In the clinic, in the appointment slot” | “Usually at or around the clinic appointment” |
| Time inside the appointment slot: “Testing and examination only” | “Testing, examination and any intake exceptions that require support” |
| Ongoing labor: “Configuration and support effort instead of in-appointment staff time” | “Less routine collection and transcription; ongoing monitoring and exception support” |
| Integration dependency: “None” | “Can operate without systems integration, but may still require manual entry into the receiving system” |
| Data-entry correction: “Fewer transcription steps; corrections are made in the receiving system” | “Can reduce transcription when integrated; corrections follow the receiving system’s process” |
The paragraph after the table should also be rebalanced. Suggested replacement:
Manual intake has lower integration requirements and provides immediate in-person support. Digital intake can improve pre-appointment availability, standardize the capture procedure and reduce transcription when connected to the receiving system. The appropriate model depends on volume, access requirements, exception rates and the existing technology environment.
This is more accurate than saying the decision turns mainly on consistency and record format.
### 4. The prevalence of hybrid workflows is unsupported
Current wording:
For most programs the answer is hybrid...
The article provides no evidence for “most programs.” This can remain decisive without making a prevalence claim:
A hybrid model combines remote questionnaire and body-measurement capture with on-site testing and examination. The split is determined component by component, with a fallback and transfer path for each step moved before the visit.
### 5. The FitXpress output sentence needs correction
Current wording treats BMI as one of the 80+ body measurements:
...covering 80+ body measurements, including the circumferences and BMI...
Use:
The scan produces structured results associated with a scan timestamp. Outputs include 80+ body measurements and calculated metrics such as BMI.
“Time-stamped at capture” should also be verified. If the timestamp applies to the scan session or result rather than the exact capture event, “associated with a scan timestamp” is safer and more precise.
### 6. The privacy paragraph still contains claims that should be changed
The following wording remains problematic:
- “Processes no personal identifiers.”
- “Deletes photos immediately after processing or within 30 days.”
- “Follows GDPR principles.”
- “It is not a clearance, eligibility or fitness-for-duty input.”
The final sentence is especially important: FitXpress is being described throughout the article as an intake layer, so saying it is not an “input” contradicts that positioning. The correct boundary is that it does not make the determination.
Suggested replacement:
FitXpress encrypts data at rest and in transit. In most enterprise deployments, the customer acts as controller and 3DLOOK acts as processor under GDPR. A HIPAA Business Associate Agreement is available on request. Photos are deleted after processing, while generated outputs are retained according to the agreed deployment terms. FitXpress supports intake and documentation; it does not make clearance, eligibility or fitness-for-duty determinations.
I would remove “processes no personal identifiers” unless that exact statement has been confirmed for every deployment. Session identifiers and customer-side record matching can make such an absolute statement difficult to maintain.
The detailed AWS S3 SSE-S3 and TLS wording is technically specific but adds little comparison value. It would fit better in the privacy and regulatory FAQ.
### 7. The accuracy conclusion understates the wider case for digital intake
Current wording:
The case for a digital channel rests on repeatability instead.
The article itself identifies additional operational advantages. Replace it with:
The measurement case therefore rests on repeatability and standardized capture rather than a claim of superiority over expert tape measurement. The wider operational case includes pre-appointment availability, structured transfer and reduced reliance on transcription.
The approved 96-97%, 1.5-2.0 cm and repeated-scan statements can remain.
## Recommended editorial refinements
These are less critical but would improve the final version:
- Replace:
switching without checking them spends money to make things worse
with:
Manual intake remains practical in several situations: ...
- Replace:
a remote-only channel strands part of the population
with:
The workflow therefore needs a manual alternative for people who lack the required access or cannot complete the remote capture.
- Replace:
The last is the diligence question worth handing any vendor, including this one.
with:
Any vendor should be able to explain how repeatability was evaluated, including the measurements, sample, number of repeated scans and reference method.
- Remove:
Clinic software calls this digital patient intake...
It does not add meaningful information and slightly interrupts the progression.
- In “How to evaluate the change,” the questions about rescreens, integration and fallback repeat the table directly. Retain the metric table and reduce the five questions to the two broader diligence questions: which components move, and how measurement performance was evaluated.
## Final verdict
The article now delivers the intended comparison value and respects the cannibalization guardrail. After correcting the intake/screening terminology, revising the remaining absolute table entries, and replacing the privacy paragraph, it should be ready for final proofreading and publication.



---

## Heading anchors in the source tab

- `h.vfkq9lbxo5ik` — Remaining essential corrections
- `h.jr7hgf6di562` — 1. The intake-versus-screening distinction is still inconsistent
- `h.9ybv751rsh40` — 2. One sentence incorrectly describes both methods
- `h.d5t3996k720l` — 3. Several table rows remain too absolute
- `h.bxc2u9og4657` — 4. The prevalence of hybrid workflows is unsupported
- `h.y1xy49fjcs7y` — 5. The FitXpress output sentence needs correction
- `h.qzsm2cpychp0` — 6. The privacy paragraph still contains claims that should be changed
- `h.z0q5tsxiirtn` — 7. The accuracy conclusion understates the wider case for digital intake
- `h.669nigfs10gh` — Recommended editorial refinements
- `h.uv44x9ruv95v` — Final verdict
