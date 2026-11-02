# Video assignment: `aeo-glp-1-tracking-between-visits`

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

Write exactly this shape to `workspace/social/articles/aeo-glp-1-tracking-between-visits/_video/video.json` (UTF-8 JSON, no comments, no trailing text):

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

## The question this pack answers

How can GLP-1 weight-loss clinics track body composition remotely between visits, and what tools belong in the care plan?

## The final posts

### instagram-company (carousel)

**Angle:** The practical sort a GLP-1 care team needs between appointments: which of the seven methods work from home and which need a visit, with one stance: the home side is where comparability is won or lost, so conditions get fixed before the first at-home check-in.

**Claims used:** "Connected scales, supported wearables, progress photos, and mobile body scanning can all be used from home"; professional BIA, DXA and manual measurement "all require an in-person visit"; "One possible model pairs a category designed for periodic, detailed in-clinic assessment... with a category designed for frequent, low-burden remote capture"; home BIA estimates "can vary with hydration, food intake, exercise, and measurement timing"; "Standardized conditions are important when comparing readings over time."

Between GLP-1 clinic visits, four of the seven body composition and progress tools work from home. Three need a visit.

Works from home 🏠
Connected scales: weight with a directional body composition estimate
Mobile body scanning: two phone photos turned into body measurements and a 3D model
Progress photos: a visual record of change
Wearables: activity and recovery, some with composition estimates

Needs a visit
Clinic-grade body composition analyzers
DXA scans (dual-energy X-ray absorptiometry)
Tape measure and calipers

One possible pairing: a clinic method for periodic, detailed checkpoints, and a home method for frequent, low-effort check-ins in between.

Our view: the home side is where comparability is won or lost. Scale readings shift with hydration, food, exercise and timing. Set the conditions before the first at-home check-in, and keep them the same every time.

Save this for your next care-plan review. Full comparison: link in bio.

### facebook-company (text + photo)

**Angle:** Progress photos between GLP-1 visits: why they cannot give a body composition number, the firm line that they should not be the only record a care team reviews, and the two questions that make them more useful. FitXpress named once as one of seven methods.

**Claims used:** Progress photos are "unstructured images; no numeric measurement"; "Differences in pose, distance, clothing, lighting, and camera angle can limit direct comparison"; best role "visual engagement and qualitative progress tracking as a complement to structured measurement data"; the article's two vendor questions on photos; mobile body scanning "uses two smartphone photos, front and side" to generate measurements, estimated composition outputs and a 3D model.

Progress photos are a familiar way to see change between GLP-1 clinic visits. On their own, they don't give a care team a body composition number to compare.

A progress photo is an unstructured image with no numeric measurement attached. Pose, distance, clothing, lighting and camera angle also change from week to week, which makes two photos hard to compare.

Photos support visual engagement and show qualitative progress. They shouldn't be the only record a care team reviews between visits.

Two questions help:
- Is there guidance for consistent pose, distance and lighting?
- Is each photo stored alongside structured measurement data from the same session?

The same phone camera can do structured work too. With mobile body scanning, such as our FitXpress, two guided photos, front and side, become body measurements and estimated body composition, along with a 3D model. It's one of seven methods in the full comparison.

Does your program use progress photos between visits? What do you compare them against?

Read the full article: https://3dlook.ai/content-hub/top-7-remote-body-composition-tools-glp-1-clinics/

### linkedin-company (carousel)

**Angle:** Widening employer coverage pushes remote between-visit measurement into procurement; the article's answer is to score every candidate, whatever its category, against one fixed set of questions. FitXpress appears as one candidate held to the same list.

**Claims used:** KFF 2025 Employer Health Benefits Survey: "43 percent of firms with 5,000 or more workers covered GLP-1 drugs for weight loss in 2025, up from 28 percent in 2024"; "Score every candidate tool against the same questions, regardless of category"; six of the article's buyer-checklist questions; "For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm"; white-label via API or SDK; "FitXpress is not a medical device".

A GLP-1 program choosing a body composition tool for between-visit check-ins should put the same questions to every vendor, whatever the category.

Coverage is widening. The KFF 2025 Employer Health Benefits Survey found that 43 percent of firms with 5,000 or more workers covered GLP-1 drugs for weight loss in 2025, up from 28 percent in 2024.

Many programs now operate through remote or hybrid care models, where in-clinic equipment is limited to scheduled visits. Between those visits, the choice runs across seven categories, from connected scales and smartphone scanning to wearables and imaging-center scans. They differ in remote capability and in what drives cost.

We suggest scoring every candidate against one list 📋
- What does it measure directly, and what does it estimate?
- What reference method and population were used for validation?
- How repeatable are results under normal at-home conditions?
- Can results be exported through an application programming interface (API)?
- How are photos, measurements, identifiers and session data retained?
- Where is clinician review required?

We apply the same list to FitXpress, our mobile body scanning product. For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm. It is delivered white-label through an API or software development kit (SDK), producing structured records for clinician review.

FitXpress is not a medical device. Where a protocol requires calibrated scales, professional bioelectrical impedance analysis or dual-energy X-ray absorptiometry, those methods keep their role.

The full article compares all seven categories and includes the complete buyer checklist. Read it here: https://3dlook.ai/content-hub/top-7-remote-body-composition-tools-glp-1-clinics/

### linkedin-katerina (text)

**Angle:** A founder's observation that in remote GLP-1 care the format a body composition result arrives in now matters as much as the method, and that procurement's first question is moving toward what lands in the patient record.

**Claims used:** DXA "results typically arrive as a report (PDF or portal export)"; progress photos are "stored in a patient app or portal as an image, not a structured data field"; manual measurement is "typically manual entry into the patient record"; connected scales and mobile scanning produce a structured record; API and SDK delivery give "the care team with structured data within the systems it already uses".

In remote GLP-1 care, the result's format matters as much as the method.

Between visits, a body composition reading has to reach a clinician who wasn't there when it was taken. Its format decides whether anyone can compare it with the last one.

The formats differ widely. An imaging-center scan usually comes back as a PDF or portal export. Progress photos sit in an app as images. Tape measurements are typed into the record manually. Connected scales and smartphone scanning can produce a structured record.

My view: this is where procurement expectations are moving. The first question is becoming what lands in the patient record, and whether it reaches systems the care team already uses.

Of the readings your clinicians review between visits, what share arrives as a field they can compare session to session?

The article sets all seven methods side by side, data structure included. Link in the comments.

### linkedin-vadim (text)

**Angle:** How an operator should run a remote body composition pilot: baseline at intake, captures on the existing check-in schedule, a time-box, and clinician review time as the number to watch hardest.

**Claims used:** "Programs may establish a baseline at intake and schedule subsequent captures around their check-in protocol. Run a time-boxed pilot before committing at scale, and measure capture completion rate, record consistency across sessions, and clinician review time"; these measures "complement vendor specifications".

Judge a GLP-1 body composition pilot on clinician review time first.

Spec sheets describe the tool. They can't show what between-visit check-ins do to your care team's week.

Here's how I'd set one up. Take a baseline at intake. Schedule captures around the check-in protocol you already run. Time-box the pilot before committing at scale.

Then measure what happens. Capture completion rate shows whether patients do the check-ins at home. Record consistency across sessions shows whether two readings can be compared.

Clinician review time is the one I'd watch hardest. A method patients finish but clinicians struggle to review moves the work onto the care team.

If you've run a remote check-in pilot, how many minutes did a clinician spend per review? And did your team make the go or no-go call on it?

The full comparison of seven methods is linked in the comments.

### linkedin-nick (screenshot)

**Angle:** For between-visit GLP-1 comparison, ask a vendor for repeatability before accuracy, because the two are separate benchmarks answering different questions. FitXpress serves as the worked example of reporting both.

**Claims used:** "For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm"; separately, "compared with expert manual measurements, FitXpress reports 96-97% accuracy with a typical error margin of 1.5-2.0 cm"; "These figures represent two distinct benchmarks based on different reference methods"; vendor question "How repeatable are results under normal at-home conditions?"

Ask a body composition vendor for repeatability before accuracy.

Between GLP-1 visits, a care team compares this month's record with last month's. That comparison only holds if the method gives the same answer when nothing has changed.

Accuracy and repeatability are two separate benchmarks. Accuracy compares a reading with a reference method. Repeatability compares two readings of the same body.

Take FitXpress, the mobile scanning product we build. For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm.

Separately, compared with expert manual measurements, FitXpress reports 96-97% accuracy with a typical error margin of 1.5-2.0 cm.

For between-visit trends, I'd read the repeatability figure first.

The question I'd put to any vendor: how repeatable are results under normal at-home conditions?

What scan-to-scan difference would your clinicians accept before they stop trusting a between-visit trend?

Full comparison of seven methods in the comments.

### linkedin-olena (text)

**Angle:** The last question on the article's buyer checklist, "which program decisions should the output explicitly not support?", moved to the top: write the boundary down before a remote body composition pilot starts.

**Claims used:** Checklist question "Which program decisions should the output explicitly not support?"; "The role any output plays in eligibility, prescribing, or treatment decisions depends on the tool, its regulatory status, the program protocol, and clinician review"; "FitXpress is not a medical device and does not diagnose conditions or determine treatment, prescribing, or eligibility."

A remote body composition plan should start with what the data won't decide.

For a GLP-1 program adding check-ins between visits, that means one question: which program decisions should the output explicitly not support?

It sits last on the buyer checklist in the article below. I'd move it to the top.

Answering it early decides where clinician review sits.

Remote body data can inform a clinician's review. Its role in eligibility, prescribing and treatment depends on the tool, its regulatory status and the program protocol.

Our own product carries that boundary in one line: FitXpress is not a medical device. It does not diagnose conditions or determine treatment, prescribing or eligibility.

I'd write the boundary down before the pilot starts. Narrowing a data stream's role is harder once clinicians rely on it.

Is that boundary written down in your program, and who signed it off?

The full comparison is linked in the comments.

### linkedin-katya (infographic)

**Angle:** The commercial side of between-visit tracking: every method costs more as membership grows, and what differs is the unit being multiplied (devices or usage). Multiply each method's cost driver by the planned member count before comparing features.

**Claims used:** Primary cost drivers from the "At a Glance" table: connected scale "Per-patient or clinic-issued hardware", mobile body scanning "Software usage and integration" with "a smartphone with a camera; no dedicated scanning hardware"; checklist questions "What hardware must the clinic or patient purchase?" and "Can the tool support the intended patient volume and check-in cadence?"

In remote GLP-1 programs, every body composition method gets costlier as membership grows.

Between visits, what differs is the unit you're multiplying.

Take two at-home options. A connected scale is per-patient or clinic-issued hardware. Each new member means another device.

Smartphone scanning, the category 3DLOOK works in, runs on software usage and integration. The only hardware is a smartphone with a camera. Usage still grows with every member and every check-in.

My rule of thumb: before comparing features, multiply each method's cost driver by the member count and check-in cadence you plan for. Then ask every vendor what hardware the clinic or patient must purchase.

How many devices or scans would your current check-in method need at next year's member count, and who pays for them?

The full comparison is linked in the comments.
