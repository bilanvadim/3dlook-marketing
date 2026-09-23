---
review: review-2.md (Doc tabs "Review 2" + "Publish pack", fetched 2026-09-23)
decided_by: coordinator (new-article.md review procedure), checked against brand-assets/
rule: THIS FILE WINS over review-2.md wherever they differ. It also wins over brief.md §7 and the pack's
  `excluded_topics` (see P0). review-1-decisions.md (incl. Vadim's answers in its section D) stays in force.
type: STRUCTURAL. Q11 is replaced by three questions, so plan.md changes first. Then edit → publish → QC.
---

# Review 2: decisions

## P. Progress section (structural)

**P0. Brief conflict.** brief.md §7 excluded full answers to the three prospect progress questions, and
the pack lists them in `excluded_topics`. Review 2 says they are distinct buying questions in the original
prospect brief and must be answered. ACCEPT. This round overrides §7 for this article only. Keep each answer to
roughly 120-180 words. Leave presentation depth to [mobile body scanning and patient engagement], which stays
linked once, so the section stays short and does not become a progress article.

**P1. Replace Q11 "What progress outputs are available after a successful scan?" with three H3s, verbatim from
the review.** They become FAQPage Question.name, in this order, after Q10:
1. "How do you track fat loss and lean-mass change?"
2. "How can programs visually display fat-mass and lean-mass changes?"
3. "How should programs show meaningful progress at 5, 10, or 20 pounds of weight loss?"
Keep the v2 output list (80+ body measurements, calculated BMI/BMR where the inputs are provided, body
composition estimates, 3D model, Body Progress) folded into question 1. That keeps the FXS-OUTPUTS and
FXS-LIFECYCLE coverage and the "weight is optional" line. Place the three under their own H2 "Tracking and
displaying progress". The previous H2 becomes "Workflow integration and timing".

**P2. Question 1 (lean mass).** ACCEPT the review text as the basis, including the explicit terminology correction:
FitXpress estimates lean mass and does not measure muscle mass directly. Lean mass includes muscle along with
water, bone, organs, and other non-fat tissue. That is a general physiology definition, not a product claim,
and it is allowed. Body Progress: two customer-selected scans compared by scan ID. The customer decides
whether tracking is enabled and how it is presented (brief §9, FXS-IDS).

**P3. Question 2 (visual display).** ACCEPT. The organization controls the interface. A progress view can combine
baseline and follow-up values, change from baseline, body fat %, fat mass, lean mass, selected circumferences,
and a comparison of the two 3D models. Keep the boundary sentence: visual differences in a 3D model are not a
direct map of fat or muscle tissue.

**P4. Question 3 (5/10/20 lb). ACCEPT with one change.** Review sentence: "FitXpress does not apply a generic 5-,
10-, or 20-pound body transformation." REJECTED as written. Canon has an optional 3D goal / target-weight
visualization (tech-spec.md "target weight visualization (3D model at goal weight)", how-it-works.md,
overview.md). A flat "does not generate" could contradict it. Write instead: milestone progress is shown from
the individual's actual baseline and follow-up scans, because the same weight change can correspond to
different changes in fat mass, lean mass, shape and circumferences. Do not mention the goal visualization in
either direction. Where weight is collected separately, it sits alongside the scan outputs (brief §9: identify
the weight source; milestone logic belongs to the program; FitXpress output does not detect milestones by
itself). Open item for Vadim: should the optional target-weight visualization be mentioned here as a
projection, clearly labelled?

**P5. Quick answers: add a "Progress" row.** Wording: "Programs can compare fat mass, lean mass, body fat
percentage, measurements, and selected scans over time." | "Lean mass is not the same as muscle mass, and
milestone views are built from each person's actual scans." The second cell is adapted per P4.

## W. Wording corrections

**W1. Opening.** ACCEPT the review's two paragraphs, lightly adjusted to guardrails ("need to know" is fine).
Remove "The FAQ covers…". Keep the third paragraph (preparation) and the scope note.
**W2. "a design decision intended to protect measurement accuracy".** ACCEPT: "The core capture flow in which
RTPV operates is standardized to support consistent capture across users and scan sessions."
**W3. Clothing Detector.** ACCEPT the safer wording: "The Clothing Detector identifies clothing conditions that may
interfere with capture. When the supported flow identifies a clothing problem, the user can be asked to adjust
the clothing or repeat the capture." Replace "form-fitting or regular-fit clothing" with "Clothing that follows
the body outline helps keep that outline visible." Also update the Quick answers Clothing qualification if it
still names garment classes.
**W4. Repeatability conditions.** ACCEPT: "using similar lighting, camera placement, pose, distance, and clothing
conditions".
**W5. Phone placement.** ACCEPT for this article: "on a stable surface around desk height". It is narrower than
canon FX-CQ-007 ("table, counter"), so it gets legalized as FX-R2 wording.
**W6. Integration step 3.** ACCEPT: "The captured data is submitted through the integration for FitXpress processing."
Check steps 1 and 5 for the same single-architecture assumption.
**W7. Existing photos.** ACCEPT: "Camera-roll photos are outside the standard guided FitXpress flow and do not provide
the same controlled capture process within the current scan session."

## V. Visuals
**V1.** Keep Illustration 1 (capture-quality flow).
**V2.** Replace Illustration 2 (accuracy/repeatability panel) with a baseline-versus-follow-up progress display:
matching baseline and follow-up 3D models; body fat %, fat mass, lean mass; one or two circumference changes;
clear "Baseline", "Follow-up", "Change" labels; no body regions coloured as "fat loss" or "muscle gain".
Place it in the new progress section, after question 2. Same blockquote format as Review 1 A5.

## H. Publish-pack housekeeping (for seo-publisher / CMS notes in meta.md)
- Remove the two designer briefs after inserting the final visuals.
- Quick Answers table: ~30% / 35% / 35% columns, smaller table font.
- FAQ schema: 13 questions now, Question.name = visible H3 wording exactly.
- Keep the current internal links.

## Word budget
13 questions after this round. Plan target 2,300 (lint band 1,955-2,645). Brief range is 1,800-2,400, so
aim for ≤ 2,450 by tightening Q5 and Q9, which the Review 1 cannibalization note already asked to keep short.
