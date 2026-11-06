# Video assignment: `2026-09-19-glp-1-fitness-apps-body-composition-tracking`

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

Write exactly this shape to `workspace/social/articles/2026-09-19-glp-1-fitness-apps-body-composition-tracking/_video/video.json` (UTF-8 JSON, no comments, no trailing text):

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

## The final posts

### twitter-company (text + photo)

**Angle:** Keep the core gap, but land a judgment: a lone falling number reads as a win, yet means little until composition, measurements and training sit beside it. POV on top of the fact, not a retelling of the premise.

**Claims used:** Weight "shows the change in weight. It does not show whether fat mass, lean mass, or fluid made up the change"; a fitness app can show body measurements, composition estimates and training history together.

A dropping number on glucagon-like peptide-1 (GLP-1) looks like a win. The scale can't tell whether fat mass, lean mass, or fluid made up the change. Put measurements, composition estimates and training history on one timeline, giving the number context. Full read:

### instagram-company (infographic)

**Angle:** The visual "fuller picture" idea: weight, waist, body composition and strength training on one timeline, each labeled by source. Human, screen-level moment of seeing more than one number.

**Claims used:** Progress view shows weight, waist and other circumferences, fat and lean mass estimates, and completed strength sessions on one record; each value carries its source label; guided scan; lean mass is not muscle; scan cannot determine which tissue changed.

The scale is one line on the chart. Your progress is the whole picture. 📊

For someone on glucagon-like peptide-1 (GLP-1) treatment, a drop on the scale doesn't show whether fat mass, lean mass, or fluid made up the change.

A fitness app can show more than one number. Weight. Waist and hip measurements. Body composition estimates. Completed strength sessions. All on one timeline, each labeled with where the value came from.

A quick guided phone scan captures the measurements at each check-in, and the app adds them to the training history it already keeps.

One honest note. A scan can estimate lean mass, and lean mass is not the same as muscle. It cannot tell you which tissue changed. That conversation stays with your clinician.

Progress is easier to read when every value shows its source.

Link in bio.

### facebook-company (text + photo)

**Angle:** Accessible, honest take on what a scan can and cannot tell you: it can show a fuller progress view, but it cannot prove a member lost muscle. Managing expectations for a broad audience, closed with a question.

**Claims used:** Scan cannot determine muscle loss or the cause of a lean-mass change; lean mass is not muscle and includes organs, bone, fluids, water in fat tissue; fitness app shows weight, measurements, composition estimates, strength sessions with source labels; under 45 seconds; clinical questions go to the prescribing clinician.

Can a body scan tell you whether you've lost muscle on a GLP-1 medication? The honest answer is no, and that matters.

When the number on the scale drops, it doesn't show whether the loss was fat, lean mass, or fluid. That's a real gap for anyone tracking progress during treatment.

A fitness app can close part of it. Alongside weight, it can show body measurements like waist and hip, body composition estimates, and the strength sessions a member has already completed. A guided phone scan turns the photos into structured results in under 45 seconds, and each value carries a label for where it came from.

Here's the part we think matters most. A scan estimates lean mass, and lean mass is not the same as muscle. It includes organs, bone, fluid and water in fat tissue. No single scan can prove a member lost muscle, or say what caused a change. Those questions belong with a prescribing clinician.

The useful goal is simpler: give members a fuller, honest view of their progress than the scale alone.

What would you want to see on a progress screen beyond weight?

Read the full article:

### linkedin-company (carousel)

**Angle:** The market trend behind the article: GLP-1 raised the bar for what a progress view must show, and the design task is source-labeled trends. FitXpress positioned as the enabling layer, not the centre.

**Claims used:** Weight does not show whether fat/lean/fluid changed; Neeland 2024 review 40-60% and ~15% or less; under 45 seconds, 80+ body measurements, composition estimates, 3D model; separate source-labeled trends; lean mass is not muscle; FitXpress is not a medical device; treatment decisions remain with the prescribing clinician.

GLP-1 treatment has changed what a progress screen needs to show.

When a member loses weight on these medications, the scale records the change. It does not show whether fat mass, lean mass, or fluid made up that change. A 2024 review in Diabetes, Obesity and Metabolism examined lean mass change with these therapies. In some studies, reductions in lean mass accounted for 40% to 60% of total weight loss. Other studies put the share at approximately 15% or less. A single weight number sits on top of all of it.

For fitness and coaching apps, this creates a clear design task. Show body data alongside training history, and label where every value comes from.

FitXpress supports this inside the app's own interface. A guided front-and-side photo capture returns structured results in under 45 seconds: 80+ body measurements, body composition estimates, and a 3D model. The app can display weight, circumferences, composition estimates and completed strength sessions as separate trends, each marked by source.

One boundary stays fixed. A scan estimates lean mass, and lean mass is not muscle. It cannot determine which tissue changed or establish the cause. FitXpress is not a medical device, and treatment decisions remain with the prescribing clinician.

Honest, source-labeled progress is becoming a baseline expectation. 📊

Read the full article on how fitness apps can track progress beyond scale weight:

### linkedin-katerina (text)

**Angle:** Strategic observation: GLP-1 moved the market toward progress records beyond scale weight, and the differentiator is now restraint. Honest product limits are becoming a buying criterion.

**Claims used:** Weight doesn't show fat/lean/fluid split; Neeland 2024 review 40-60% and ~15% or less; lean mass is not muscle; no scan proves which tissue changed.

GLP-1 has quietly rewritten what a progress screen is expected to show.

A year ago, weight was enough. Now a weight drop raises a harder question. Was it fat, lean mass, or fluid?

The research is why. One 2024 review found lean mass made up 40% to 60% of total weight loss in some studies, and 15% or less in others. That is a wide range to hide under a single number.

The market is moving toward progress records that separate trends by source. Weight, measurements, composition estimates, training history, each labeled.

What I find more telling is the restraint. The serious products now state plainly what a scan cannot do. Lean mass is not muscle. No scan proves which tissue changed.

Enterprise buyers are starting to reward that honesty over a bigger claim.

I unpacked this in a new piece on tracking progress beyond the scale.

Where have you seen an honest limit win a deal over a bolder promise?

### linkedin-vadim (text + photo)

**Angle:** Operational: check-ins fail on capture consistency, not the scan. Teach two things in order: standardize capture, then set a flagging threshold from observed scan-to-scan variation.

**Claims used:** Capture conditions (same clothing, time of day, setting; guided flow checks pose and quality); smallest difference worth showing depends on observed scan-to-scan variation and the interval; repeated scans showed typical scan-to-scan differences of less than 1 cm (internal testing); figures describe body measurements.

Most body-scan check-ins fail on consistency, not on the scan itself.

If a member scans in different clothing, at a different time of day, in a different room, you can't tell real change from noise.

Two things fix most of it.

First, standardize capture. Same clothing, same time of day, same setting, every time. The guided flow should check pose and quality before it accepts the photos.

Second, set a threshold. Decide the smallest difference worth flagging to a member, based on your observed scan-to-scan variation and how far apart check-ins sit. Smaller moves stay in the record without a callout.

For context, repeated FitXpress scans in internal testing showed typical scan-to-scan differences of less than 1 cm. That figure covers body measurements only.

The full article walks through baseline, cadence and capture conditions.

How are you setting the threshold for a change worth showing?

### linkedin-nick (text)

**Angle:** First-person BD take: the fitness app's narrow job in a GLP-1 program is its edge, and drawing the line early between what the app records and what the clinician reads keeps an app-plus-provider program clean.

**Claims used:** 2025 joint advisory (incl. The Obesity Society) names muscle and bone loss, backs strength training with adequate protein; an app offering workouts supports one part of that guidance; lean mass is not muscle; no scan proves which tissue changed; clinical concerns go to the prescribing clinician.

I keep telling teams building weight-loss apps: your job here is narrow, and that's your edge.

When I look at a glucagon-like peptide-1 (GLP-1) program, the prescribing clinician owns treatment, dosing and any read on muscle or bone loss. The app owns something else. A clear record of body change next to the training a member does.

That record matters more now. A 2025 joint advisory from four US bodies, including The Obesity Society, names muscle and bone loss as challenges of GLP-1 therapy. It backs strength training with adequate protein. An app with workouts supports one part of that.

What it can't do is diagnose. A scan estimates lean mass, and lean mass is not muscle. No scan proves which tissue changed. That goes to the clinician.

I've seen programs get messy when that line gets drawn late. The full article maps where that line sits.

When you scoped an app-plus-provider program, where did you draw the line?

### linkedin-olena (text)

**Angle:** Adoption and trust: a scan workflow that assumes everyone can stand for it quietly loses members. Teach one thing: design the fallback capture path first, label the method, keep methods as separate trends.

**Claims used:** FitXpress was not specifically trained on data representing people with physical disabilities, performance not established for that population; the app can offer manual measurements or a weight-only progress view; the progress view labels the method behind each value and keeps results from different methods as separate trends.

The fastest way to lose members from a scan workflow is to assume everyone can stand for it.

A standard body scan needs a standing pose and a capture sequence. Not every member can do that. FitXpress was not specifically trained on data representing people with physical disabilities, and its performance for that group has not been established.

If the only path is the standard scan, those members quietly drop out. That shows up later as patchy data and uneven adoption.

The fix is to design the fallback first. Offer manual measurements or a weight-only progress view, and label the method behind every value. Keep results from different methods as separate trends. A switch in method should never look like real body change.

Inclusive capture is not a nice-to-have. It is what keeps your progress data honest across a whole cohort.

The article covers this alternative path in more detail.

How do you handle members who can't complete a standard scan today?

### linkedin-katya (text)

**Angle:** Commercial trust: with GLP-1 pushing every platform to show more than scale weight, the vendor who admits limits is the safer bet. Teach a buyer test: ask what the product refuses to claim.

**Claims used:** Lean mass is not muscle; no scan proves which tissue changed or whether a member lost muscle; a scan cannot establish the cause; clinical questions stay with the clinician.

In digital health, the vendor who admits limits is usually the safer bet.

GLP-1 has every platform racing to show more than scale weight. That is the right instinct. The risk is a vendor who oversells what a body scan can tell you.

Here is a test I'd run on any body-data vendor. Ask what their product refuses to claim.

A credible answer sounds like this. A scan estimates lean mass, and lean mass is not muscle. No scan proves which tissue changed, or whether a member lost muscle at all. That belongs with the clinician.

A vendor who promises muscle measurement from two photos is telling you how the next conversation goes wrong.

For a buying team, that restraint is not weakness. It is what protects member trust once the feature ships.

What is the first limit you ask a vendor to put in writing?

The full article is worth a read if you're scoping this:
