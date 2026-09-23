---
slug: 2026-09-22-fitxpress-capture-quality-user-experience-faq
product: fitxpress
status: ready_for_review
created: 2026-09-23
generated_by: scripts/article_package.py (mechanics) + seo-publisher meta.md (judgment)
source_final: "final.md (2431 prose words, lint PASS)"
word_count: 2431
stop_rule: OK
---

# Publish Package — 2026-09-22-fitxpress-capture-quality-user-experience-faq

## Meta

**Title:** FitXpress Capture Quality & User Experience FAQ (47/60 chars)
**Description:** Telehealth and digital-health teams: a capture quality FAQ on guided capture, RTPV, clothing detection, self-scanning, retakes, timing, and progress tracking. (158/160 chars)
**Slug:** `/content-hub/fitxpress-capture-quality-user-experience-faq/`
**Category:** Product FAQ

## Механический чек-лист (16/17, считал скрипт)

- [x] **lint_verdict** — article_lint: PASS
- [x] **detector_clean** — ai_density 0.37/1000, hard_fails [], house_rules []
- [x] **keyword_h1** — «capture quality» в H1: «FitXpress User Experience and Capture Quality FAQ»
- [x] **keyword_h2** — keyword в 1 H2 (норма 1-2)
- [x] **claims_traceable** — claims_used: ['FX-CQ-002', 'FX-CQ-003', 'FX-CQ-005', 'FX-CQ-006', 'FX-CQ-007', 'FX-CQ-009', 'FX-R1-ADMIN', 'FX-R1-CORE', 'FX-R1-FLOW', 'FX-R1-SDK', 'FX-R1-UPLOAD', 'FX-R2-3D', 'FX-R2-CLOTH', 'FX-R2-LEAN', 'FX-R2-PLACEMENT', 'FX-R2-STANDARD', 'FX-R2-SUBMIT', 'FX-R2-UPLOAD', 'FXS-DELIVERY', 'FXS-IDS', 'FXS-LIFECYCLE', 'FXS-MEDICAL', 'FXS-OUTPUTS', 'FXS-SCOPE', 'FXS-SPEED']
- [x] **no_banned_claims** — banned claims + superseded figures gates
- [x] **word_count** — 2431 слов против target 2300 (полоса линтера ±15%; жёсткие ±10% = ok)
- [x] **links_4_directions** — направления: {'up': 1, 'sideways': 1, 'down': 1, 'trust': 2}
- [x] **medical_framing** — «FitXpress is not a medical device.» ×1; «positioned as» ×0
- [x] **no_named_entities** — клиенты/конкуренты: нет
- [x] **no_stale_urls** — устаревшие URL: нет
- [x] **accuracy_discipline** — {'accuracy_figures_present': True, 'links_to_framework': True}
- [x] **m1_abbreviations** — gate 8 (M1)
- [x] **sentence_length** — mean 14.2
- [✗] **faq_present** — FAQ: 0 вопросов
- [x] **boundary_section** — «does not do»-секция: False; scope note сверху: True
- [x] **scope_note_early** — курсивная scope note в первых строках

## Суждение seo-publisher — 6/6 judgment-пунктов ok (meta.md, verbatim без frontmatter)

## Judgment checklist

- [x] intro_hook: Hook rewritten this round (W1) but keeps the same shape as v1/v2: opens with the concrete procurement question ("...whether users can complete a two-photo scan reliably without a technician present") before any product description. review-2-decisions.md W1 accepted the reviewer's two paragraphs, adjusting only "need to know" for tone and removing "The FAQ covers..." meta-copy. Still the strongest available hook.
- [x] cta_type: Next steps / Book a demo section is byte-identical to v1 and v2 (edit-notes.md invariants: "The CTA line is byte-identical"). Single BOFU/direct CTA, no mid-article CTA added despite the new progress section.
- [x] anchors_sources: Same 5 internal links + Book a demo, each once at first mention. The patient-engagement link moved from the old Q11 bridge to the new Q12 (visual display) per P3, still once, still the most relevant first mention now that Q12 is the visual-presentation question. Zero external/third-party sources in the rewritten answers.
- [x] cannibalization: `already_live: false` still holds; no existing page owns capture quality / input-quality-control intent. Review 2's P0 overrode brief §7 to answer the three progress questions in full, which is the one place this round could have drifted into the patient-engagement page's territory. Mitigated by design: each answer stays 150-170 words (edit-notes.md), covers outputs/mechanics/boundaries rather than presentation UX, and still links out to patient-engagement once (Q12) for "how programs present results over time" instead of restating it. Flagged as an ongoing watch item in Open items, not closed by one round of review.
- [x] distinct_intent: Still owns "can remote users produce reliable body data without staff supervision" plus how FitXpress controls pose, clothing, and capture conditions. The new progress section extends that same intent (what outputs a successful scan returns and how an organization compares two of them) rather than competing with patient-engagement's intent (how programs design an engagement experience around those outputs). edit-notes.md §16 QA re-verifies this against the new final.md.
- [x] vertical_boundary: "FitXpress is not a medical device." appears once verbatim (Q8, unchanged). "Positioned as" zero times. RTPV stays explicitly non-clinical (Q2, Quick answers table). New this round: Q11's lean-mass-not-muscle-mass correction (FX-R2-LEAN) and Q12's "visual differences between 3D models are not a direct map of fat or muscle tissue" (FX-R2-3D) are both boundary sentences that tighten claims discipline rather than loosen it, correcting the prospect's own terminology instead of silently adopting it.

## Meta variants

### Title
1. FitXpress Capture Quality & User Experience FAQ (47 chars) — recommended, unchanged since brief §2 / v2, untouched by Review 2
2. FitXpress Capture Quality FAQ for Telehealth Teams (50 chars)
3. Capture Quality & User Experience FAQ | FitXpress (49 chars)

### Description
1. Telehealth and digital-health teams: a capture quality FAQ on guided capture, RTPV, clothing detection, self-scanning, retakes, timing, and progress tracking. (158 chars) — recommended. Adds "progress tracking" to reflect the new H2 (3 new H3s, ~500 words); drops only "workflow" to make room. Keyword "capture quality" appears once.
2. Telehealth and digital-health teams: a capture quality FAQ on guided photo capture, RTPV, clothing detection, self-scanning, retakes, workflow, and timing. (155 chars) — v2 fallback, no progress mention, kept in case CMS prefers the stable wording already indexed once from v2.
3. How FitXpress controls capture quality and progress tracking: guided photo capture, RTPV, clothing checks, self-scanning, retakes, and timing, answered. (152 chars)

## Schema notes

Article or BlogPosting via the standard content-hub template, plus ONE connected FAQPage entity,
no per-question FAQPage blocks. `Question.name` stays byte-identical to the visible H3 wording.
Round 2 (P1) replaced the old Q11 bridge with three new questions, so the entity now holds **13**
questions, in document order:

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
11. How do you track fat loss and lean-mass change?
12. How can programs visually display fat-mass and lean-mass changes?
13. How should programs show meaningful progress at 5, 10, or 20 pounds of weight loss?

**Every `acceptedAnswer.text` must be regenerated from the CURRENT final.md, not carried over from
v2's schema draft.** Questions 11-13 are entirely new (P1) and have no prior `acceptedAnswer` to
reuse. Questions 2, 4, 5, 7, 8, 10 also changed under this round's wording corrections (W2-W7:
RTPV standardization language, Clothing Detector wording, repeatability conditions, phone
placement, integration step 3, camera-roll wording) — pull fresh text for those too, not just the
three new ones. Questions 1, 3, 6, 9 are unchanged from v2's schema. Pull `acceptedAnswer.text` as
the direct-answer sentence plus the supporting paragraph(s) under each H3 in the current final.md,
and re-sync at CMS entry time if final.md changes again. Q3 keeps the straight apostrophe (`'`) in
both the H3 and `Question.name` (plan-audit item 9; the source doc has a curly one). The Quick
answers table (now 8 rows, including the new Progress row) and Next steps/CTA stay outside the
FAQPage entity.

## CMS housekeeping (review-2.md "Publish pack" tab, review-2-decisions.md section H)

- Remove both designer-brief blockquotes (Illustration 1 and Illustration 2) once the final visuals
  are inserted in the CMS. Do not publish the bracketed `> **[Illustration N: ...]**` placeholder
  text or the "Designer brief:" line.
- Format the Quick answers table at approximately 30% / 35% / 35% column widths (Topic / Direct
  answer / Important qualification), with the smaller table font already used on the live trust FAQ.
- FAQ schema: 13 `Question.name` entries, exactly the visible H3 wording (see Schema notes above).
- Keep the current internal links as-is: no link additions or removals in this housekeeping pass.

## Open items

1. **Vadim: optional target-weight visualization in Q13.** Canon (`tech-spec.md`, `how-it-works.md`, `overview.md`) documents an optional 3D goal / target-weight visualization. Review 2's P4 deliberately mentions it in neither direction in the 5/10/20-pound answer. Decide whether Q13 should name it as a clearly labelled projection (e.g., "a 3D model at a target weight, shown as a projection, not a guarantee") or stay silent, as it does now.
2. **Product: Clothing Detector classes and payload field are still internal.** Q4 uses only the reviewer's broader wording (FX-R2-CLOTH, "identifies clothing conditions that may interfere with capture"). The sport/regular/oversized classification and the response-payload flag (FX-CQ-003, FXS-LIFECYCLE) stay out pending confirmation of current customer-facing behavior; they can return to Q4 once confirmed.
3. **Product: "stable surface around desk height" narrower than canon.** FX-R2-PLACEMENT ("on a stable surface around desk height," Q7) replaces canon FX-CQ-007's "flat surface, such as a table or counter" for this article only, on the reviewer's reasoning that a counter may place the phone too high. If product confirms this is the correct guidance, update the canon phrasing in tech-spec.md so future articles don't diverge from it silently.
4. **Cannibalization watch: progress content vs. the patient-engagement / progress-tracking cluster.** Review 2's P0 overrode brief §7 and the pack's `excluded_topics` to answer the three progress questions in full (previously deliberately excluded as belonging to that cluster). The mitigation is link-out plus brevity (see the cannibalization judgment item above), but this is a one-time editorial call under review pressure, not a structural guarantee against future drift. Worth a look the next time the patient-engagement page or another progress-tracking article is revised, to confirm the two pages still read as distinct.
5. **`article_lint.py` does not recognise the illustration blockquote format.** The `> **[Illustration N: ...]**` / "Designer brief:" blockquote format (both illustrations) is not in the lint's `_SENT_SKIP` pattern, so it counts roughly 70-90 words of designer-brief text as prose in the gate numbers. The article passes every gate regardless (144 sentences counted, still within band); this is a tooling gap to close if the blockquote format becomes the house standard.
6. **`faq_present` mechanical checklist false positive.** The 13 H3 questions sit under three descriptive H2s ("How FitXpress controls capture quality," "Capture conditions, failed scans, and self-scanning," "Workflow integration and timing," "Tracking and displaying progress" — four, after this round's split), the same structural pattern as the live trust FAQ. `article_package.py`'s `faq_present` check only looks for a literal "## FAQ" heading and reads 0 questions. `article_lint.py` itself does not gate on this. Non-blocking.
7. **No measured demand for "capture quality."** Still no Ahrefs data (brand/product term); closest measured adjacent head is "body measurement app" (150/mo, KD 22), consumer-tracker framed, not this page's B2B-procurement intent. This is a GEO / sales-support / internal-link-hub page by design, the same call as the GLP-1 Progress Record article (2026-09-21): judge it on citations and sales use, not sessions.

## Image and alt-text suggestions

1. End of Q1 ("How does FitXpress help users capture usable photos?"), Illustration 1 placement (blockquote with a bold bracketed label). Unchanged from v2. Concept: guided instructions leading into positioning and framing checks (RTPV), a clothing check, front and side capture, and structured results in under 45 seconds from the photos, the only timing figure on the page; a retake loop runs back from the checks, and clinical review sits outside the product, in the organization's workflow. Alt: "Diagram of guided capture steps with positioning, framing, and clothing checks before processing, and a retake path." (116 chars)
2. Between Q12 ("How can programs visually display fat-mass and lean-mass changes?") and Q13, Illustration 2 placement (blockquote, same format). New concept this round, replacing v2's accuracy/repeatability evidence panel, per review-2-decisions.md V2 and final.md's own designer brief: matching baseline and follow-up 3D body models side by side, with body fat percentage, fat mass, lean mass, and one or two circumference changes under clear "Baseline", "Follow-up", and "Change" labels. No body region is coloured to suggest a tissue change, and every figure is an illustrative placeholder. Alt: "Baseline versus follow-up 3D body models with body fat, fat mass, lean mass, and circumference change labels." (109 chars)

## article_lint.py, verbatim

```
workspace/seo/articles/2026-09-22-fitxpress-capture-quality-user-experience-faq/final.md
mode: article

[ok  ] hard bans (detect-ai-tells)
         . detector_words: 2676
         . ai_density: 0.37
         . verdict: CLEAN
         . rhythm_variation: 0.37
[ok  ] prose length
         prose words 2431 vs target 2300 (band 1955-2645)
         . prose_words: 2431
         . target: 2300
[ok  ] claim traceability
         . claims_used: ['FX-CQ-002', 'FX-CQ-003', 'FX-CQ-005', 'FX-CQ-006', 'FX-CQ-007', 'FX-CQ-009', 'FX-R1-ADMIN', 'FX-R1-CORE', 'FX-R1-FLOW', 'FX-R1-SDK', 'FX-R1-UPLOAD', 'FX-R2-3D', 'FX-R2-CLOTH', 'FX-R2-LEAN', 'FX-R2-PLACEMENT', 'FX-R2-STANDARD', 'FX-R2-SUBMIT', 'FX-R2-UPLOAD', 'FXS-DELIVERY', 'FXS-IDS', 'FXS-LIFECYCLE', 'FXS-MEDICAL', 'FXS-OUTPUTS', 'FXS-SCOPE', 'FXS-SPEED']
         . claims_known: 36
[ok  ] banned claims
[ok  ] superseded figures
[ok  ] internal links
         . links_total: 6
         . links_distinct: 6
         . asset_urls: 0
         . directions: {'up': 1, 'sideways': 1, 'down': 1, 'trust': 2}
[ok  ] keyword placement
         . keyword: capture quality
         . occurrences: 3
         . h2_count: 6
         . in_first_paragraph: False
[ok  ] abbreviations (M1)
[ok  ] accuracy discipline
         . accuracy_figures_present: True
         . links_to_framework: True
[ok  ] sentence length
         . limits: article (mean <= 16, <= 6% over 25, <= 1 over 35)
         . sentences: 144
         . mean_words: 14.2
         . p90_words: 22
         . over_25: 0 (0.0%)
         . over_35: 0
         . near_duplicate_pairs: none
         . repeated_phrases: ['front and side x5', 'body fat percentage x4', 'and phone placement x4', 'the organization controls x3', 'the capture flow x3', 'percentage fat mass x3']

VERDICT: PASS
Mechanics are clean. Judgment is still open: run quality-controller on whether
the argument holds and whether each section earns its place.
```

## detect-ai-tells.py, verbatim (--summary)

```
SEO / blog article · en · 2676 words
AI density: 0.37/1000 (budget 6.0) -> low
VERDICT: CLEAN — check the positive side (voice, varied rhythm, a stated boundary) and ship.

TOP SOFT MARKERS:
  1x 'is a capture-quality control, not a clinical' (L52)
```

## Article

Текст НЕ дублируется в пакете: единственный источник — `final.md` (2431 prose words) рядом с этим файлом.
