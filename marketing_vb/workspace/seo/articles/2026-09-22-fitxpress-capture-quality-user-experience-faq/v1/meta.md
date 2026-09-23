---
meta_title: "FitXpress Capture Quality & User Experience FAQ"
meta_description: "Telehealth and digital-health teams: a capture quality FAQ on guided photo capture, RTPV, clothing detection, self-scanning, retakes, workflow, and timing."
url_slug: /content-hub/fitxpress-capture-quality-user-experience-faq/
category: Product FAQ
---

## Judgment checklist

- [x] intro_hook: Opens on the concrete procurement question in the first sentence ("...whether users can complete a two-photo scan reliably without a technician present"), the exact primary_intent from page_specs, before any product description — no throat-clearing.
- [x] cta_type: Single BOFU/direct CTA in Next steps, brief §13 verbatim, matching the MOFU/BOFU funnel stage and the implementation/procurement buyer audience in page_specs; no mid-article CTA.
- [x] anchors_sources: All 6 links (5 internal + Book a demo) use descriptive, sense-bearing anchor text identical to brief §10, each once at first mention; zero external/third-party sources anywhere in the piece, so no vendor-blog citation risk applies.
- [x] cannibalization: `already_live: false`, no existing page owns capture quality/input-quality-control intent (plan-audit cannibalization check, 5 questions). Each of the 5 adjacent topics (mechanics, accuracy, telehealth BOFU, patient engagement, trust FAQ) gets exactly one link at first mention and no restatement.
- [x] distinct_intent: Owns "can remote users produce reliable body data without staff supervision" plus how FitXpress controls pose, clothing, and capture conditions. Verified against brief §3's six-item "do not turn into" list: no expansion into general telehealth, two-photo mechanics, accuracy methodology, patient engagement, privacy/regulatory content, or clinical decision-making (edit-notes.md §16 QA items 1-2, 5, 10 all PASS).
- [x] vertical_boundary: "FitXpress is not a medical device." appears once verbatim (Q8), "positioned as" zero times, italic scope note in the intro, FXS-SCOPE boundary paragraph in Q8, RTPV explicitly non-clinical in both Q2 and the Quick answers table. Telehealth stays context only, never the subject.

## Meta variants

### Title
1. FitXpress Capture Quality & User Experience FAQ (47 chars) — recommended, brief §2 verbatim, not re-generated (see Open items)
2. FitXpress Capture Quality FAQ for Telehealth Teams (50 chars)
3. Capture Quality & User Experience FAQ | FitXpress (49 chars)

### Description
1. Telehealth and digital-health teams: a capture quality FAQ on guided photo capture, RTPV, clothing detection, self-scanning, retakes, workflow, and timing. (155 chars) — recommended
2. Capture quality FAQ for telehealth and digital-health teams: guided photo capture, RTPV, clothing detection, self-scanning, retakes, workflow, and timing. (154 chars)
3. How FitXpress controls capture quality: guided photo capture, RTPV, clothing checks, self-scanning, retakes, workflow integration, and timing, answered. (152 chars)

## Schema notes

Article or BlogPosting via the standard content-hub template (brief §14), plus ONE connected
FAQPage entity — no per-question FAQPage blocks. `Question.name` must be byte-identical to the
11 H3 strings in final.md, in document order:

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

`acceptedAnswer.text` for each must be the corresponding visible answer text in final.md, taken
in full (the direct-answer sentence plus the supporting paragraph(s) under that H3, not just the
first sentence), and kept in sync if final.md changes again before CMS entry. Q3 uses a straight
apostrophe (`'`) in the H3; use the identical character in `Question.name` — the brief's source
doc has a curly one (plan-audit item 9). The Quick answers table and Next steps/CTA are not part
of the FAQPage entity (brief §14, plan-audit "FAQPage: 11 questions only").

## Open items

- **No measured demand for the on-page primary keyword.** `capture quality` has no Ahrefs data (brand/product term); best measured adjacent head is `body measurement app` (150/mo, KD 22), consumer-tracker framed, not this page's B2B-procurement intent. This is a GEO / sales-support / internal-link-hub page by design, same call as the GLP-1 Progress Record article (2026-09-21) — judge on citations and sales use, not sessions (plan-audit item 1).
- **RTPV naming unconfirmed.** "Real-Time Pose Validation (RTPV)" is not attested in product-info canon (tech-spec.md, how-it-works.md, faq.md, overview.md all use lowercase descriptive phrasing). Kept because the external brief requires it (§6.2, §8). If product does not confirm this as the customer-facing name, Q2's H3 and the schema `Question.name` must change together (plan-audit item 2).
- **Clothing Detector naming and behavior unconfirmed.** Same gap as RTPV: canon uses lowercase "clothing classification" / "clothing detection", not a proper-noun feature name. Article uses canon behavior only (sport/regular/oversized, flag + prompt, payload field). Confirm current naming and behavior before publication (plan-audit item 3).
- **Blocked vs. prompted capture unconfirmed.** No canon source confirms a hard block for any quality condition; article says prompts, corrections, another attempt only, per brief §6.3's own caution. If product confirms a real block, Q3/Q4 can be sharpened later (plan-audit item 4).
- **Q11 BMI input when weight is not submitted.** Article says "where the required inputs are provided... height is submitted; weight is optional" and does not mention Smart Scales. If BMI can be calculated from a non-user-submitted (Smart Scales predicted) weight, Q11 needs a precise sentence and Smart Scales would need to be named per the brief's own reservation of "predicted weight" for that feature (plan-audit item 5).
- **React Native, timer, and voice guidance omitted.** No canon source names an explicit React Native SDK, a capture timer, or voice guidance; article uses "Camera SDK (React), for web and hybrid apps" only. Add if product confirms (plan-audit item 7).
- **Quick answers table cells rewritten from the brief.** Brief §5 gives the Clothing/Retakes/Timing qualification cells as editorial instructions ("Do not claim that…"), not publishable text; final.md rewrites them as direct statements. Vadim may prefer wording closer to the brief's literal cells (plan-audit item 8).
- **Accuracy/repeatability sentences use the pack's legalized short form.** FX-CQ-009/010 (accuracy-formulations.md §5 short forms, "internal" restored per editorial guardrail #3) replace the brief's own paraphrase and the FXS-ACCURACY/FXS-REPEAT long forms in Q5. Same claim, coordinator-approved alternate wording, not a new number (plan-audit item 9, edit-notes.md "Canon wording not in the pack").
- **Meta description reworded, not lifted verbatim.** The brief's literal description (159 chars) never uses the phrase "capture quality," so it fails the mechanical keyword-in-description check. The recommended variant above inserts the keyword with the smallest edit that still reads naturally; flag if Vadim prefers the brief's exact wording over mechanical compliance.
- **Context pack was missing link-direction data; added at assemble time.** This pack is off-plan (no content-plan row, no Phase 0 hub resolution per plan-audit.md), so `context-pack-builder` never populated `content_strategy.internal_link_targets`, and `article_package.py`'s links_4_directions check read all four directions as zero. Added that section to the pack directly, reusing only the brief's own §10 anchors/URLs (already verified in `internal_links`) and matching the exact bucket convention (accuracy framework + trust FAQ = trust, patient engagement = sideways, telehealth BOFU page = down) already used for 4 of these 5 URLs in the sibling 2026-09-21 packs. No new link, anchor, or claim; flagging so context-pack-builder's off-plan template gets this section by default next time.
- **`faq_present` mechanical check shows 0/false, non-blocking.** The article groups its 11 H3 FAQ questions under three descriptive H2s ("How FitXpress controls capture quality," "Capture conditions, failed scans, and self-scanning," "Workflow integration, timing, and outputs"), the same structural pattern as the live trust FAQ (`fitxpress-data-privacy-security-regulatory-faq.md`), which also has no literal "## FAQ" heading. `article_package.py`'s `faq_present` check only looks for that literal heading, so it reads 0 questions on both this article and its structural model. `article_lint.py` itself does not gate on this (verdict PASS); it is a script-detection gap, not an article defect. Mechanical checklist is 16/17 with this as the sole miss, well under the 2-fail STOP threshold. Worth widening the detector for Type-G-style articles later.

## Image and alt-text suggestions

1. End of Q1 ("How does FitXpress help users capture usable photos?"), (Image 1) placeholder. Concept: guided capture and quality-control flow — guided instructions, positioning/framing checks, clothing check, front and side capture, processing, structured results, with a retake loop running back from the checks; clinical review shown outside the product flow, per brief §12 primary visual. Alt: "Diagram of guided capture steps with positioning, framing, and clothing checks before processing, and a retake path." (116 chars)
2. End of Q5 ("How much do user behavior and capture conditions affect the results?"), (Image 2) placeholder, optional per brief §12. Concept: compact three-column evidence panel — accuracy against a reference method, repeatability across comparable scans, capture-quality controls before processing — definitions only, no figures on the panel itself. Alt: "Panel comparing accuracy, repeatability, and capture-quality checks as three separate concepts." (95 chars)
