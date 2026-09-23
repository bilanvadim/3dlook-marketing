---
review: review-1.md (Doc tab "Review 1", fetched 2026-09-23)
decided_by: coordinator (per new-article.md review procedure), checked against brand-assets/
rule: THIS FILE WINS over review-1.md wherever they differ. Agents read both.
scope: claim control + technical precision + voice. NOT a restructure: H1, question order and
  wording (= FAQPage Question.name), Quick answers table, clinical boundary, 5 internal links, the
  single progress question, 2 visuals, pilot next step and CTA all STAY (review "What should remain unchanged").
---

# Review 1: decisions

## A. Personal feedback (voice)

**A1. "Reads like a presentation speech: fact after fact in short sentences with no connection."** ACCEPT, the main job of this round.
Rewrite for connected prose. Each answer opens with the direct answer, then explains in linked
sentences: why it matters, what it depends on, what the program has to do about it. Use explicit
relationships ("because", "which means", "depends on", "as a result"), not stacked 6-9-word
declaratives. The v1 sentence mean was 12.2 words. Aim for about 14-16 words. article_lint gate 10
still caps the mean at 16, so the fix is linking sentences, not making them long. Merge pairs like
"Capture runs only through the supported SDK flow. Every scan follows the same instructions..."
into one sentence that states the relationship. Keep the FAQ discipline: direct answer in the
first 1-2 sentences.

**A2. "Still" overemphasizes diminishing factors.** ACCEPT. Remove "still" from all four Quick answers
qualifications and from the prose (v1 had it ~9x). State the dependency plainly: "Usable results depend
on suitable capture conditions." / "Accessibility, available space, and device placement affect
completion." Keep "still" at most once in the whole article, and only where time contrast is literal.

**A3. "So" contradicts the guardrail.** ACCEPT. terminology-guardrails.md §2.9. v1 line "Implementations
that do so see meaningfully worse accuracy" is deleted anyway (see C1). No "so" as a result connector
anywhere.

**A4. "See" contradicts the guardrail.** ACCEPT. Same v1 sentence ("...see meaningfully worse accuracy");
deleted. Do not use "see" for attributed outcomes or reading directions ("see below", "see the framework").
Link anchors are integrated into the sentence (guardrail "Internal linking": links directly on anchors).

**A5. Illustration placements need different formatting from article text.** ACCEPT. Format every
placement as its own blockquote with a bold bracketed label, a blank line before and after:

    > **[Illustration 1: Guided capture and quality-control flow]**
    > Designer brief: ...one or two sentences, no figures other than approved ones...

Same for Illustration 2. The placement text must not read as article prose.

## B. ChatGPT's required corrections (Doc line numbers = v1 Doc)

**C1. Lines 29-31: "Capture runs only through the SDK" + custom flows "meaningfully worse accuracy".**
ACCEPT. Canon tech-spec.md does say this, but the phrase is internal sales guidance, and the reviewer
reports public customer terms describe SDKs as optional. New wording: the standard end-user flow uses
the supported SDK, which provides the guided capture controls. Remove the accuracy comparison (FX-CQ-001
is no longer used in this article).

**C2. Lines 39-41: RTPV presented as pose + framing + phone tilt in one function.** ACCEPT. Separate them:
RTPV checks the user's position and framing; the SDK's guidance also covers the phone-angle (tilt)
requirements. tech-spec.md "pose / tilt validation" supports tilt as a separate check. Do not mention a
gyroscope (not in canon).

**C3. Line 43: "Skeletal tracking runs on-device or live in the browser" + face obfuscation.** ACCEPT. Delete
the sentence. Face obfuscation belongs to the privacy FAQ, which is already linked in Q8.

**C4. Line 47: "The photo capture layer... is not customizable."** ACCEPT. New wording: the core capture flow
is standardized, while the organization controls and brands the surrounding onboarding, instructions
and results experience. Do not say the tutorial can be disabled (not in canon); do not claim anything
is "not customizable".

**C5. Lines 51-63: real-time correction blended with retakes after submission.** ACCEPT. Q3 separates two cases:
(1) capture-time guidance, where the prompts help the user fix position, framing or phone angle before the photo is taken;
(2) a failed or unusable capture that needs another attempt. Q3 owns (1) and names (2) briefly; Q6 owns
the failed-scan route. No claims about which conditions block capture.

**C6. Lines 67-71: sport/regular/oversized, prompts, response payload need product confirmation.** ACCEPT the
broader wording: "The Clothing Detector identifies clothing conditions that may interfere with capture
and can prompt corrective action." Drop the sport/regular/oversized classes and the payload sentence
from Q4. Keep the explanation of why body-following clothing matters. Open item for product: confirm
the classes and the payload field before they come back.

**C7. Line 81: "the single biggest factor in measurement accuracy".** ACCEPT. Delete. Say that no single
public percentage or ranking describes the effect of individual capture conditions.

**C8. Lines 91-93: accuracy + repeatability block duplicates the Accuracy Framework.** ACCEPT. Keep the three
definitions (accuracy / repeatability / capture quality) and ONE concise proof point, the repeatability
figure (FX-CQ-009, "below 1 cm for most of the evaluated measurements"). Repeatability matches this
article's topic (consistent capture across repeated scans). Drop the 96-97% / 1.5-2.0 cm sentence. The
framework link sits in the same paragraph, for validation figures, tested population and methodology.
Shorten the Q5 accuracy part by about one paragraph (Cannibalization check). The accuracy gate in
article_lint must still pass: a figure + a framework link in one paragraph.

**C9. Line 115: disability-training statement.** ACCEPT for this article, PARTLY DISAGREE on the reason. The
sentence is canon (accuracy-formulations.md §5), and it is already live on the occupational-health
intake article, so it is not "unsupported by the public source set". This FAQ does not need it,
though: remove FXS-POPULATION here and keep the practical accessibility guidance and the
alternative-path route. Open item for Vadim: the reviewer wants Product + Legal sign-off on this sentence.
If that applies across all content, it changes a canon formulation that is already live.

**C10. Line 121: "Standard indoor lighting is fine, and any background works".** ACCEPT. Replace with: "Users
should follow the on-screen guidance for lighting, distance, framing, and phone placement." Keep the
phone-on-a-flat-surface detail (FX-CQ-007).

**C11. Line 147: "Camera SDK (React) for web and hybrid apps"; Admin Panel.** ACCEPT. Use "web and mobile SDKs,
including supported iOS and Android integrations" plus the API. Admin Panel = an optional, complementary
interface for monitoring and exporting results. It does not replace integration (consistent with
Vadim 2026-09-21: API/SDK primary, Admin Panel optional).

**C12. Line 149: "Results can stay server-side only... submission confirmation".** ACCEPT. Replace with: "The
organization controls which outputs appear in its interface and how they are routed for review."
FX-CQ-008 is no longer used.

**C13. Lines 157-165: timing definitions.** PARTLY REJECT. The reviewer proposes "under a minute" for the guided
flow. That figure is NOT in canon (proof-points.md, compliance.md and overview.md all say "under 45 seconds",
"time from photo to results"), and the brief itself says: if there is no newer product confirmation,
use "The full FitXpress processing pipeline returns results in under 45 seconds". ACCEPT the underlying
problem: v1 defined 45 s as processing only, and that contradicts canon. Fix: one definition on the
whole page, the canon one, time from the photos to structured results is under 45 seconds (FXS-SPEED).
Onboarding before capture depends on the organization's own screens. No other timing figures, no
"under a minute". The same definition goes in the Quick answers Timing row and in the Illustration 1 brief.
Open item: product to confirm one central timing definition (reviewer notes live pages mix 40 s /
45 s / under a minute).

**C14. Line 171: "Access to the device's camera roll is disabled".** ACCEPT. Keep only: "Users cannot upload
existing photos in the standard guided FitXpress capture flow." plus the explanation of why guided capture
matters (no fraud framing).

## C. Carried over, unchanged
- H1, SEO title, URL, question order and the exact 11 H3 strings (FAQPage Question.name).
- "RTPV is a capture-quality control, not a clinical posture assessment" stays (licensed boundary).
- "FitXpress is not a medical device." verbatim. Lean mass, never muscle mass. Body Progress = customer-selected scans by scan ID.
- 5 internal links once each, CTA verbatim, pilot next step.
- Word target: 1,800-2,400. Shrinking Q5 and the cut claims may bring the page under 2,000 words. That is fine if it stays ≥ 1,800.

## D. Vadim's answers to the open items (2026-09-23)
1. Disability-training sentence: removed **only here**; stays canon elsewhere (accuracy-formulations.md §5 scope note).
2. Timing: **one** definition, "under 45 seconds from the photos to structured results" (now in proof-points.md + tech-spec.md).
3. Clothing Detector classes/payload: OK to keep out until product confirms.
4. "Real-Time Pose Validation (RTPV)", "Clothing Detector" and Admin Panel "monitoring and exporting": **added to canon** (tech-spec.md, how-it-works.md, FXS-DELIVERY). Open items 4-5 of meta.md are closed.
5. QC note on "regular-fit / oversized" in Q4: OK as written.
