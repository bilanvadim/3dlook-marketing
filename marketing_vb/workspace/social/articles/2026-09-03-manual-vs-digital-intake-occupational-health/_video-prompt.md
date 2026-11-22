# Video assignment: `2026-09-03-manual-vs-digital-intake-occupational-health`

You are writing the on-screen words for ONE short brand video (15-20 seconds, silent,
text only) that goes out next to this pack. A script renders it in the house template
in two shapes (9:16 for Instagram Reels, 4:5 for LinkedIn company, Facebook and
Instagram feed). You write words only, as JSON. Read nothing else first: everything
you need is in this file.

## Where the words come from

Only from the FINAL posts below. They already passed the number lint, the brand check
and QC. Shorten, cut and reorder their wording; never add a fact, a number, a product
capability, a customer or a claim that no post makes. Every number you use must appear
in a post below in the same digits (a script compares them). Wording about accuracy,
compliance or FitXpress's scope is taken exactly as a post words it, or left out.

## What the video is for

A teaser that stops the scroll and sends people to the article. One angle, not a
summary of the pack. Take the strongest angle the company accounts use
(`linkedin-company`, `instagram-company`, `facebook-company`) unless a personal post
carries a sharper, still company-safe point. The video speaks as 3DLOOK, never as a
person: no "I", no names, no market a personal profile is written for.

## The six fields

- `eyebrow`: the subject in 1-4 words, plain ("GLP-1 programs", "Occupational health").
- `hook`: one claim, never a question. 3-12 words, at most 80 characters. A viewer who
  sees only this line must know what the subject is.
- `stat` (optional object, omit it when no post carries a sourced figure; no stat beats
  a weak one): `value` at most 8 characters ("43%", "<1 cm"), `label` 3-14 words that
  make the number self-explanatory, `source` 2-10 words naming the source exactly as
  the post does ("KFF 2025 Employer Health Benefits Survey"). A figure from 3DLOOK's
  own validation uses the post's own wording and source line.
- `points`: 2 or 3 lines, each 2-8 words and at most 48 characters, parallel in form.
  Checklist questions are allowed here (they are the one place a question fits).
- `close`: 3-10 words, at most 64 characters: what the article gives the viewer.
- `cta`: leave out (the template says "Read the full article").

House rules that hold on screen too: no em dash or en dash, no hashtags, no emoji, no
exclamation marks, English only. The house word bans hold exactly as in the posts
(they are checked mechanically after you save, along with every limit above).

## Output

Write exactly this shape to `workspace/social/articles/2026-09-03-manual-vs-digital-intake-occupational-health/_video/video.json` (UTF-8 JSON, no comments, no trailing text):

```json
{
  "eyebrow": "…",
  "hook": "…",
  "stat": {"value": "…", "label": "…", "source": "…"},
  "points": ["…", "…", "…"],
  "close": "…",
  "from_profiles": ["linkedin-company"]
}
```

`from_profiles` lists the posts whose wording you used. When the file is saved, reply
with one line: the hook, and which profile's angle it comes from.

## Claims discipline for this pack (from the run brief)

The posts below were written under these rules. They bind the video too, and where a post and this section differ, this section wins. A figure the section says to give together with another (both ends of a finding, a boundary, a qualifier) goes on screen together or not at all: a silent card cannot add the context a post had around it.

_Every number and boundary below is in the article's own wording. Anything not
listed here is not available to a post._

- Capture: "a guided two-photo smartphone scan completed in under 45 seconds."
- Output: "80+ body measurements, BMI, and a session timestamp."
- Repeatability: "Repeatability testing used a real-world customer dataset with
  five scans per participant. For most of the evaluated measurements, typical
  scan-to-scan differences remained below 1 cm." (below 1 cm, not "under 1 cm" —
  match the article's own phrasing if quoted directly)
- Accuracy: "reported accuracy was approximately 96-97%, with a typical
  absolute error of 1.5-2.0 cm depending on the body part," measured against
  expert pattern-maker tape measurement. These are two separate benchmarks
  (repeatability vs accuracy) — never combine them into one figure.
- Three workflow phases: pre-appointment intake, on-site screening, clinical
  review. Only the first is remote-capable.
- Scope / medical framing (quote or paraphrase tightly, never loosen):
  "FitXpress does not perform medical examinations, make fitness-for-duty or
  clearance determinations, or serve as a basis for hiring or employment
  decisions. FitXpress is not a medical device."
- Disability population: "FitXpress was not specifically trained on data
  representing people with physical disabilities, and its measurement
  performance has not been established for this population." A documented
  manual alternative is required for that case — do not imply universal
  coverage.
- Data handling: "FitXpress encrypts data in transit and at rest, deletes
  photos after processing, and retains generated outputs in accordance with
  the deployment terms."
- GDPR (article's exact wording): "In most enterprise deployments, the
  customer acts as the controller, and 3DLOOK acts as the processor under the
  General Data Protection Regulation (GDPR)."
- HIPAA: "A Business Associate Agreement under the Health Insurance
  Portability and Accountability Act (HIPAA) is available on request." Never
  say "HIPAA compliant."
- Third-party sources cited in the article (NHANES anthropometry manual, OSHA
  respirator-confidentiality Appendix C, EEOC pre-employment guidance) are
  regulatory/procedural context, not 3DLOOK claims — do not attribute their
  figures or requirements to 3DLOOK.
- Byline: Assel Sekerova. Published September 21, 2026. Published URL is the
  `article_slug` above — no other slug or working-folder name in a post.

## The final posts

### twitter-company (text + photo)

**Angle:** The appointment-time squeeze. Manual intake makes forms, tape measuring and record entry compete with testing for the same slot; moving eligible steps earlier is the trade. Punchy, data-first for @3DLOOK.

**Claims used:** "guided two-photo smartphone scan completed in under 45 seconds"; three phases where only pre-appointment intake is remote-capable.

In occupational health screening, manual intake puts forms, tape measuring and record entry inside the same appointment as testing. Move the eligible steps ahead of the visit and a two-photo scan captures measurements in under 45 seconds.

### instagram-company (carousel)

**Angle:** The human "before you arrive" moment. Simplified how-it-works: the record can be ready before you even leave home, and the clinic visit then focuses on what needs a person.

**Claims used:** "guided two-photo smartphone scan completed in under 45 seconds"; on-site steps (drug screening, vision/hearing, physical exam) remain in person; "FitXpress is not a medical device."

Picture finishing your clinic paperwork before you have even left the house.

That is the shift happening in occupational health screening.

The old way: you arrive, fill out forms, a staff member measures you with a tape, and someone types it all into the record. All of that competes with your actual testing for the same appointment.

The digital way moves the eligible steps earlier. A guided two-photo scan on your phone captures body measurements in under 45 seconds. 📱 By the time you arrive, the record is already there, and the visit can focus on the checks that genuinely need to happen in person.

It does not replace the clinic. Drug screening, vision and hearing checks, and the physical exam still happen on-site. And FitXpress is not a medical device. It supplies body-measurement data for a clinician to review.

A smaller change than it sounds. A real difference to your morning.

Link in bio.

### facebook-company (text + photo)

**Angle:** The honest decision framework. Digital intake is not automatically right; the post lays out when manual still fits, when digital fits, and why most programs land on a hybrid. Warm, balanced, discussion-oriented.

**Claims used:** Manual-fits / digital-fits conditions from the article's decision framework; "guided two-photo smartphone scan" in "under 45 seconds"; hybrid needs a defined manual fallback.

Going digital is not automatically the right call for occupational health screening. Sometimes the manual, in-person process is still the better fit, and knowing the difference matters.

Manual intake still makes sense when appointment capacity is comfortable, when reliable smartphone or network access is limited, or when body measurement is a small part of a visit that already runs smoothly.

Digital intake earns its place when high volume is straining fixed appointment slots, when several sites or partners need one consistent process, or when rescreens keep tracing back to missing intake data. A guided two-photo smartphone scan captures body measurements in under 45 seconds, before the person arrives, allowing the visit to focus on the tests that need to happen in person.

Most strong programs land on a hybrid: eligible steps done ahead of time, equipment-based testing kept on-site, and a manual fallback defined for anyone who cannot complete a scan.

Which side does your program lean toward right now?

Read the full article: [link]

### linkedin-company (infographic)

**Angle:** Measurement consistency across sites, not a single accuracy number, is the real enterprise problem. Manual measurement varies with technique/training; a standardized capture procedure and structured records are the business value. FitXpress positioned as one part of intake.

**Claims used:** NHANES waist-measurement procedure complexity (regulatory context, not a 3DLOOK claim); "80+ body measurements, BMI, and a session timestamp"; "guided two-photo smartphone scan"; standardized procedure subject to capture-quality requirements; determinations stay with responsible professionals; "FitXpress is not a medical device."

Measurement consistency is quietly one of the hardest problems in occupational health screening.

A manual body measurement depends on technique. The published NHANES anthropometry manual spells out what a single standardized waist measurement actually requires: an examiner palpating a specific point on the hip, marking it at the midaxillary line, a recorder checking the tape is level, and a reading taken at normal expiration. That is a lot of training and quality control to reproduce the same number across every site and every staff member.

For a single clinic, technique variance may be manageable. For a program spanning multiple sites or vendor partners, it becomes an operational problem: rescreens, corrections, and records that are hard to compare.

This is where the conversation is shifting. Enterprise health programs are asking less about a single accuracy figure and more about whether a process produces consistent, structured records at scale.

FitXpress fits here as one part of pre-appointment intake. A guided two-photo smartphone scan produces 80+ body measurements, BMI, and a session timestamp through a standardized procedure, subject to capture-quality requirements. It supplies body-measurement data for clinician review; clearance and fitness-for-duty determinations stay with the responsible professionals. FitXpress is not a medical device.

The takeaway for operators: judge an intake method by how consistently and cleanly it produces records at scale.

Read the full article on comparing manual and digital intake. 👇

### linkedin-katerina (text)

**Angle:** CEO market observation. The question enterprise health buyers ask about measurement is shifting from a single accuracy number to governance: same result across many sites, in a reviewable form.

**Claims used:** Manual measurement varies with technique and training; standardized capture procedure; timestamped structured record; "FitXpress is not a medical device"; clinical determination stays with the clinician.

Enterprise health buyers have stopped asking me one question about measurement.

They used to ask how accurate a body scan is. One number.

Now the sharper teams ask something else. Can it produce the same result across ten sites, next quarter, in a form we can review?

That is a different bar. That shifts the question from precision to governance.

Manual measurement varies with technique and training. At a single clinic that is fine. Across a screening program with many sites, it becomes rescreens and records that do not line up.

A standardized capture procedure changes that calculus. So does a timestamped, structured record that a reviewer can actually trust.

FitXpress is one way to reach that consistency. It is not a medical device, and the clinical call stays with the clinician.

If you ran your intake data across every site tomorrow, would the numbers agree?

Explore the article.

### linkedin-vadim (text)

**Angle:** Operational. The exception path, not the happy path, decides whether a digital intake rollout scales. Teach: define a documented fallback and transfer route for every remote step before launch.

**Claims used:** Requires a "defined manual alternative for people unable to complete the remote intake"; FitXpress "was not specifically trained on data representing people with physical disabilities, and its measurement performance has not been established for this population"; two-photo scan.

The part of a digital intake rollout that breaks first is the exception path.

Everyone plans the happy path. Person gets a link, does a two-photo scan, the record lands. Clean.

Then reality. Someone has no compatible phone. Someone's connection drops mid-capture. Someone cannot hold the standard standing pose.

Worth knowing: FitXpress was not specifically trained on data representing people with physical disabilities, and its performance has not been established for that group. That case needs a documented manual measurement path, every time.

Here is the operational rule I would hold to. For every step you move before the visit, define the fallback and the transfer route before launch, while it is still cheap to change.

An intake process is only as scalable as its worst-case handling.

What share of your intake volume actually ends up on the fallback path today?

Happy to share the full comparison article.

### linkedin-nick (text)

**Angle:** "Accurate enough for which decision?" Teach US healthcare operators to separate the two benchmarks a vendor should report, repeatability vs accuracy, and never accept them blended.

**Claims used:** Repeatability: typical scan-to-scan differences "below 1 cm" for most measurements. Separate validation vs expert tape: "approximately 96-97%," typical absolute error "1.5-2.0 cm depending on the body part." Two separate benchmarks. Determinations stay with the reviewing provider.

"Is it accurate?" is the wrong first question to ask a body-measurement vendor.

The better question is: accurate enough for which decision, measured against what?

Two numbers matter, and they are not the same thing. Repeatability is how close repeated scans land on each other. Accuracy is how close a scan lands to a reference measurement.

A vendor should give you both, separately. Watch for anyone who blends them into one impressive figure.

For FitXpress, repeatability testing showed typical scan-to-scan differences below 1 cm for most measurements. A separate validation against expert tape measurement reported roughly 96-97% accuracy, with a typical error of 1.5-2.0 cm depending on the body part.

Which number you need depends on your workflow. And the clinical determination still sits with your reviewing provider. FitXpress supplies the data.

For your program, which matters more: consistency over time, or closeness to a reference?

Read the full comparison.

### linkedin-olena (text)

**Angle:** Trust, not accuracy, is the real adoption blocker for remote scanning. Teach: settle controller/processor roles and photo-deletion terms in writing before rollout. EU-wide GDPR framing, no country-specifics.

**Claims used:** "encrypts data in transit and at rest, deletes photos after processing"; outputs retained per deployment terms; "the customer acts as the controller, and 3DLOOK acts as the processor under the General Data Protection Regulation (GDPR)."

Adoption of remote body scanning stalls on trust long before it stalls on accuracy.

When you ask people to photograph themselves for a health record, their first questions are about the images. Where do they go? Who can see them?

A good answer is concrete. With FitXpress, data is encrypted in transit and at rest, and photos are deleted after processing. Generated outputs are kept according to the deployment terms.

The roles matter just as much. In most enterprise deployments, the customer acts as the controller under the General Data Protection Regulation, and 3DLOOK acts as the processor.

My practical tip: settle those roles and the photo-deletion terms in writing before rollout, while you still have negotiating room. It is what your privacy team and your users both ask for.

What blocks scan adoption more in your programs: the technology, or the trust conversation?

Read the article.

### linkedin-katya (text)

**Angle:** Commercial / buying behaviour. A pilot that "feels smoother" is not evidence. Teach: measure appointment time, missing records, corrections and rescreens before and during the pilot, and check that rescreens were caused by intake in the first place.

**Claims used:** Test the operational effect by comparing appointment-time intake, missing records, corrections and rescreens before and during the pilot; changes are meaningful only when existing causes connect to intake; two-photo scan "under 45 seconds."

Most digital intake pilots get judged on the wrong evidence.

A vendor demos a fast scan, the room is impressed, and the pilot gets called a success because it felt smoother. That is not proof.

The commercial question is whether it moved a number that costs you money. Appointment time. Missing records. Corrections. Rescreens.

Watch the causation, though. Teams celebrate fewer rescreens without checking whether intake was ever the cause. If the cause sat elsewhere, the scan did not fix it.

The fix is simple. Before a pilot, measure those four things. During the pilot, measure them again. Compare honestly.

A guided scan that produces measurements in under 45 seconds is only worth buying if it moves the number you actually care about.

Before your next pilot, do you know what is really driving your rescreens?

Let me know if you'd like the full comparison.
