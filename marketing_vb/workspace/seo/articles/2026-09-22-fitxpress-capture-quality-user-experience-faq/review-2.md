---
source: Google Doc 1-55t2X23q4zE1fMn6uBDrMt98QyQzkljVmmDWn9Dao0, tab t.omw9auyh3z0r "Review 2" + tab t.wf3v1w6lyzbb "Publish pack" (housekeeping)
fetched: 2026-09-23
applies_to: v2/final.md (Doc tab "Version 2" = v2/final.md, verified: whitespace-only diff; line numbers refer to the Doc)
---

# Review 2

I would not publish it yet. The body is essentially unchanged, and the most important remaining issue is that it does not fully answer the original prospect brief.
## Main content gap  <!-- h.2mu433c49kyn -->
The article consolidates the final three prospect questions into “What progress outputs are available?” As a result:
| Original question | Current coverage |
| How do you track fat vs muscle progress? | Partially answered |
| How do you visually display fat vs muscle change? | Not directly answered |
| How do you show meaningful progress—5 lbs vs 10 lbs vs 20 lbs? | Not answered |
This matters because those are distinct buying questions. They should not be hidden inside a general list of outputs.
Also, FitXpress estimates lean mass, not muscle mass. The article should correct the prospect’s terminology explicitly rather than silently replacing it.
### Recommended replacement for the current progress section  <!-- h.b8cluy9jqoz4 -->
#### How do you track fat loss and lean-mass change?  <!-- h.jk3fkeejdsaz -->
FitXpress can return body fat percentage, fat mass, and lean mass for each successful scan. Programs can compare these values between a baseline and a later scan, together with selected body measurements.
FitXpress does not provide a direct measurement of muscle mass. Lean mass includes muscle but also includes water, bone, organs, and other non-fat tissue. For that reason, customer-facing interfaces and supporting copy should use lean mass rather than muscle mass.
Body Progress compares two customer-selected scans using their scan IDs. The customer decides whether progress tracking is enabled and how the comparison is presented to users or care teams.
#### How can programs visually display fat-mass and lean-mass changes?  <!-- h.1tem1vmcom4p -->
FitXpress returns structured scan outputs and a 3D body model. The customer controls how those outputs appear in its interface.
A progress view can combine:
- Baseline and follow-up values.
- Change from baseline.
- Body fat percentage, fat mass, and lean mass.
- Selected circumference changes.
- A comparison of the 3D body models generated from the two scans.
The 3D comparison can help users see changes in body shape, while the numerical outputs provide the quantitative record. Visual differences in a 3D model should not be presented as a direct map of fat or muscle tissue.
#### How should programs show meaningful progress at 5, 10, or 20 pounds of weight loss?  <!-- h.baehgmii6mgd -->
FitXpress does not apply a generic 5-, 10-, or 20-pound body transformation. The same amount of weight loss can correspond to different changes in fat mass, lean mass, body shape, and circumference for different people.
Programs should therefore show progress using the individual’s actual baseline and follow-up results. Where body weight is collected separately, the interface can place weight change alongside:
- Fat mass and lean mass changes.
- Body fat percentage.
- Selected body measurements.
- The actual baseline-to-follow-up 3D comparison.
This presents what changed for that individual without implying that every pound lost came from fat or that a specific weight change always produces the same visible result.
Add a corresponding Quick Answers row:
| Topic | Direct answer | Important qualification |
| Progress | Programs can compare fat mass, lean mass, body fat percentage, measurements, and selected scans over time. | Lean mass is not the same as muscle mass, and FitXpress does not generate generic 5-, 10-, or 20-pound transformations. |
## Remaining wording corrections  <!-- h.o7uyo4balliy -->
### 1. Opening, lines 3–5  <!-- h.m6pij8k9f7b1 -->
“Before committing to a build” sounds too internal and engineering-oriented. Also, “FitXpress is guided…” is missing an article.
Recommended:
Before integrating remote body capture, telehealth and digital-health teams need to know whether users can complete a two-photo scan reliably without a technician present. The answer depends on the guidance provided during capture and the conditions in which the scan is completed.
FitXpress is a guided, two-photo body-measurement technology that programs embed in their existing app or web experience. Integration is available through web and mobile software development kits (SDKs) and an application programming interface (API).
Remove “The FAQ covers…” because it is unnecessary meta copy.
### 2. Standardization and accuracy, line 44  <!-- h.bxaxgflp0ow -->
Current:
…a design decision intended to protect measurement accuracy.
Recommended:
The core capture flow in which RTPV operates is standardized to support consistent capture across users and scan sessions.
“Protect measurement accuracy” still presents a causal accuracy claim more strongly than the available evidence supports.
### 3. Clothing Detector, lines 62–64  <!-- h.x96v0f1yficf -->
The current wording is acceptable only if Product has explicitly confirmed that the detector itself triggers the clothing-change and retake instructions.
Safer wording:
The Clothing Detector identifies clothing conditions that may interfere with capture. When the supported flow identifies a clothing problem, the user can be asked to adjust the clothing or repeat the capture.
I would also replace “form-fitting or regular-fit clothing” with:
Clothing that follows the body outline helps keep that outline visible.
### 4. Repeatability conditions, line 74  <!-- h.z6qcrbrt8ejk -->
Current wording is unnecessarily rigid:
using the same room, phone position, and clothing
Replace with:
using similar lighting, camera placement, pose, distance, and clothing conditions
Users do not literally need the same room or garments.
### 5. Phone placement, line 111  <!-- h.pmifvgmofnhi -->
Replace:
on a flat surface, such as a table or counter
With:
on a stable surface around desk height
A counter may place the phone too high.
### 6. Integration sequence, line 129  <!-- h.nr4tk1w02nsb -->
“The customer’s backend submits the required data” assumes one specific integration architecture.
Safer:
The captured data is submitted through the integration for FitXpress processing.
### 7. Existing photos, line 163  <!-- h.hcozq24k56u6 -->
“A photo from the camera roll never passed through those checks” is too absolute. A saved photo could theoretically have originated in another guided flow.
Recommended:
Camera-roll photos are outside the standard guided FitXpress flow and do not provide the same controlled capture process within the current scan session.
## Visual recommendation  <!-- h.dix7c8meqo8e -->
Keep the first capture-quality flow. Replace the second accuracy/repeatability illustration with a baseline-versus-follow-up progress display. The accuracy concepts are already explained in the canonical Accuracy Framework, whereas the current article explicitly needs to show how progress can be presented.
The replacement visual could include:
- Matching baseline and follow-up 3D models.
- Body fat percentage.
- Fat mass.
- Lean mass.
- One or two circumference changes.
- Clear “baseline,” “follow-up,” and “change” labels.
Avoid coloring parts of the body as “fat loss” or “muscle gain,” because the 3D model does not directly localize tissue-composition changes.
After these changes, the article will answer the complete prospect brief and should be ready for final product verification and publication.



# Publish pack tab (housekeeping)

## Publication housekeeping  <!-- h.h7a8q2u960xk -->
- Remove the two designer briefs after inserting the final visuals.
- Format the Quick Answers table with approximately 30% / 35% / 35% columns and the smaller table font.
- Add the new progress questions to the FAQ schema using exactly the visible wording.
- Keep the current internal links. They establish good continuity with the accuracy, privacy, telehealth, processing, and engagement pages without duplicating those pages.

