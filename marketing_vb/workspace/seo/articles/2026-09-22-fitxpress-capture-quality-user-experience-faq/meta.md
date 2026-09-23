---
meta_title: "FitXpress Capture Quality & User Experience FAQ"
meta_description: "Telehealth and digital-health teams: a capture quality FAQ on guided photo capture, RTPV, clothing detection, self-scanning, retakes, workflow, and timing."
url_slug: /content-hub/fitxpress-capture-quality-user-experience-faq/
category: Product FAQ
---

## Judgment checklist

- [x] intro_hook: Unchanged from v1 and still the strongest available hook. First sentence states the concrete procurement question ("...whether users can complete a two-photo scan reliably without a technician present") before any product description; review-1-decisions.md left the intro untouched (not in scope of Review 1).
- [x] cta_type: Next steps / Book a demo section is byte-identical to v1 (decisions "Carried over, unchanged": CTA verbatim, pilot next step). Single BOFU/direct CTA, no mid-article CTA added during the rewrite.
- [x] anchors_sources: Same 5 internal links + Book a demo, each once at first mention, descriptive anchor text unchanged (decisions: "5 internal links once each, CTA verbatim"). Zero external/third-party sources in the rewritten answers, so no vendor-blog citation risk.
- [x] cannibalization: `already_live: false` holds; no existing page owns capture quality / input-quality-control intent. Review's own cannibalization check (review-1.md) confirms differentiation after the corrections: "This FAQ owns capture reliability, user guidance, exceptions, self-scanning, and operational implementation." The pack now carries the `content_strategy.internal_link_targets` block (up/sideways/down/trust) added this round; its 5 URLs match the 5 links actually used in final.md one-for-one, so the guardrail is populated, not just asserted.
- [x] distinct_intent: Still owns "can remote users produce reliable body data without staff supervision" plus how FitXpress controls pose, clothing, and capture conditions. edit-notes.md §16 QA items 1-2 (telehealth stays context only, progress section has not grown into a competing article) both re-verified PASS against the new final.md, not just the old one.
- [x] vertical_boundary: "FitXpress is not a medical device." appears once verbatim (Q8, unchanged). "Positioned as" zero times. Italic scope note in the intro unchanged. RTPV stays explicitly non-clinical in both Q2 ("does not assess posture as a medical, musculoskeletal, or health condition") and the Quick answers table. The disability/population claim (FXS-POPULATION) was removed from this article this round (review-1-decisions C9); its removal narrows the boundary further, it does not weaken it, since the remaining accessibility guidance carries no unsupported population claim.

## Meta variants

Unchanged from v1: nothing in Review 1 touches title, description, or URL (review-1-decisions.md "Carried over, unchanged": H1 and SEO title stay; review-1.md "What should remain unchanged": "The H1 is correct"). Reproduced here for the record, not re-generated.

### Title
1. FitXpress Capture Quality & User Experience FAQ (47 chars) — recommended, brief §2 verbatim
2. FitXpress Capture Quality FAQ for Telehealth Teams (50 chars)
3. Capture Quality & User Experience FAQ | FitXpress (49 chars)

### Description
1. Telehealth and digital-health teams: a capture quality FAQ on guided photo capture, RTPV, clothing detection, self-scanning, retakes, workflow, and timing. (155 chars) — recommended
2. Capture quality FAQ for telehealth and digital-health teams: guided photo capture, RTPV, clothing detection, self-scanning, retakes, workflow, and timing. (154 chars)
3. How FitXpress controls capture quality: guided photo capture, RTPV, clothing checks, self-scanning, retakes, workflow integration, and timing, answered. (152 chars)

## Schema notes

Article or BlogPosting via the standard content-hub template, plus ONE connected FAQPage entity,
no per-question FAQPage blocks. `Question.name` stays byte-identical to the 11 H3 strings, which
Review 1 did not touch (decisions.md: "question order and wording (= FAQPage Question.name)...
STAY"), in document order:

1. How does FitXpress help users capture usable photos?
2. What is Real-Time Pose Validation (RTPV)?
3. What happens when a user's position does not meet the capture requirements?
4. What happens when clothing may affect scan quality?
5. How much do user behavior and capture conditions affect the results?
6. What happens if a user cannot complete a valid scan?
7. Can users complete a scan alone at home?
8. Can FitXpress be integrated into a telehealth or clinical workflow?
9. How long do capture and processing take?
10. Can users upload existing photos instead of completing the guided capture?
11. What progress outputs are available after a successful scan?

**Every `acceptedAnswer.text` must be regenerated from the CURRENT final.md, not carried over from
v1's schema draft.** edit-notes.md item 11 ("The FAQ schema matches the visible FAQ exactly:
PENDING (publisher)") is the direct instruction: the H3 strings did not move, but every answer body
changed under Review 1 (A1 rewrote all 11 as connected prose; C1-C14 changed specific facts, most
visibly Q2 RTPV scope, Q4 Clothing Detector wording, Q5's dropped accuracy sentence, Q8 SDK/Admin
Panel wording, and Q9's single timing definition). Pull `acceptedAnswer.text` as the direct-answer
sentence plus the supporting paragraph(s) under each H3 in the current final.md, not just the first
sentence, and re-sync at CMS entry time if final.md changes again. Q3 keeps the straight apostrophe
(`'`) in both the H3 and `Question.name` (plan-audit item 9; the source doc has a curly one). The
Quick answers table and Next steps/CTA stay outside the FAQPage entity.

## Open items

- **Product: settle ONE central timing definition.** The reviewer reports live pages currently mix three figures (guided flow under a minute, processing under 40 seconds, processing under 45 seconds). This article uses the canon figure everywhere it states a time: "under 45 seconds from the photos to structured results" (FXS-SPEED), in the Quick answers Timing row, Illustration 1's designer brief, and Q9. No other timing figure appears on the page. Flagging so product/whoever owns the live pages reconciles them against this canon, not the other way around.
- **Product: confirm Clothing Detector classes and payload field before they return.** Q4 now uses only the reviewer's broader wording (FX-R1-CLOTH, "identifies clothing conditions that may interfere with capture and can prompt corrective action"). The sport/regular/oversized classification and the response-payload flag (FX-CQ-003, FXS-LIFECYCLE) were dropped per review-1-decisions C6 pending confirmation of current customer-facing behavior; they can come back to Q4 once confirmed.
- **Vadim: Product/Legal sign-off on the disability-training sentence.** The reviewer (review-1.md, ChatGPT feedback, line 115) asked for this sentence to be removed unless Product and Legal explicitly approve it. It is canon (`accuracy-formulations.md` §5, FXS-POPULATION) and is live verbatim on the occupational-health intake article. review-1-decisions.md C9 removed it from THIS article only (the practical accessibility and alternative-path guidance stays, with no population claim attached) and flagged that if the reviewer's objection applies to all content, it changes a canon formulation that is already published elsewhere. That cross-article question is for Vadim, not resolved here.
- **RTPV and Clothing Detector proper-noun names are still not attested in product-info canon.** tech-spec.md, how-it-works.md, faq.md and overview.md all use lowercase descriptive phrasing. Both names are kept because the brief requires them and the reviewer accepted both explicitly (review-1.md "What should remain unchanged": "'RTPV is not a clinical posture assessment' is an important distinction"; no objection to the Clothing Detector name itself, only to its unconfirmed classes). If product does not confirm RTPV as the customer-facing name, Q2's H3 and the schema `Question.name` change together.
- **"Exporting" for the Admin Panel comes from the reviewer, not canon.** review-1-decisions C11 accepted "an interface for monitoring and exporting results" (FX-R1-ADMIN) to replace the vaguer v1 wording. Canon (`overview.md`, FXS-DELIVERY) says only "optional centralized view"; export as a capability is not independently confirmed in product-info. Legalized in the pack this round as reviewer wording, narrower than tech-spec.md, per the pack's own note.
- **Q11 BMI weight input still open (carried from v1, untouched by Review 1).** Q11 says height is submitted with the scan and weight is optional, and does not mention Smart Scales. If BMI can be calculated from a non-user-submitted, Smart-Scales-predicted weight, Q11 needs a precise sentence and Smart Scales would need naming, per the brief's own reservation of "predicted weight" for that feature (plan-audit item 5).
- **`article_lint.py` does not recognise the new illustration blockquote format.** A5 (this round) reformatted both illustration placements as `> **[Illustration N: ...]**` blockquotes with a Designer brief line, on the reviewer's instruction that placements need to read as distinct from article prose. The lint's `_SENT_SKIP` pattern recognises `(Image N)` / `(Cover)` placeholders but not this new label, so it counts roughly 70 words and 4 sentences of designer brief as prose in the gate numbers (edit-notes.md, "Lint note"). The article passes every gate regardless; this is a tooling gap to close if the blockquote format becomes the house standard for illustration placements.
- **`faq_present` mechanical checklist shows a false positive on this article, same as v1.** The 11 H3 questions sit under three descriptive H2s ("How FitXpress controls capture quality," "Capture conditions, failed scans, and self-scanning," "Workflow integration, timing, and outputs"), the same structural pattern as the live trust FAQ, which also has no literal "## FAQ" heading. `article_package.py`'s `faq_present` check only looks for that literal heading and reads 0 questions on both articles. `article_lint.py` itself does not gate on this (verdict PASS). Non-blocking, well under the STOP threshold.
- **No measured demand for "capture quality."** It has no Ahrefs data (brand/product term); the closest measured adjacent head is "body measurement app" (150/mo, KD 22), consumer-tracker framed, not this page's B2B-procurement intent. This is a GEO / sales-support / internal-link-hub page by design, the same call as the GLP-1 Progress Record article (2026-09-21): judge it on citations and sales use, not sessions.

## Image and alt-text suggestions

1. End of Q1 ("How does FitXpress help users capture usable photos?"), Illustration 1 placement (now a blockquote with a bold bracketed label, per review A5). Concept, aligned with final.md's designer brief: guided instructions leading into positioning and framing checks (RTPV), a clothing check, front and side capture, and structured results in under 45 seconds from the photos, the only timing figure on the page; a retake loop runs back from the checks, and clinical review sits outside the product, in the organization's workflow. Alt: "Diagram of guided capture steps with positioning, framing, and clothing checks before processing, and a retake path." (116 chars)
2. End of Q5 ("How much do user behavior and capture conditions affect the results?"), Illustration 2 placement (blockquote, same format). Concept, unchanged from v1 and still matching final.md's brief: a three-column evidence panel covering accuracy against a reference method, repeatability across comparable scans, and capture-quality controls before processing, definitions only, no figures on the panel itself. Alt: "Panel comparing accuracy, repeatability, and capture-quality checks as three separate concepts." (95 chars)
