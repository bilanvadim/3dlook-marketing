---
slug: accuracy-roi-telehealth-refresh
product: fitxpress
status: ready_for_review
created: 2026-09-23
generated_by: scripts/article_package.py (mechanics) + seo-publisher meta.md (judgment)
source_final: "final.md (2161 prose words, lint PASS)"
word_count: 2161
stop_rule: OK
pipeline_mode: no-checkpoint
---

# Publish Package — accuracy-roi-telehealth-refresh

## Meta

**Title:** Accuracy and Digital Health ROI: Verified vs Self-Reported (58/60 chars)
**Description:** As enrollment grows, checking self-reported height and weight eats staff time. Compare capture methods and build a digital health ROI model from your numbers. (158/160 chars)
**Slug:** `accuracy-drives-roi-digital-health`
**Category:** Telehealth

## Механический чек-лист (17/17, считал скрипт)

- [x] **lint_verdict** — article_lint: PASS
- [x] **detector_clean** — ai_density 0.0/1000, hard_fails [], house_rules []
- [x] **keyword_h1** — «digital health roi» в H1: «Accuracy and Digital Health ROI: Scaling Patient Monitoring Without More Manual Work»
- [x] **keyword_h2** — keyword в 1 H2 (норма 1-2)
- [x] **claims_traceable** — claims_used: ['FXS-ACCURACY', 'FXS-DELIVERY', 'FXS-GDPR', 'FXS-HIPAA', 'FXS-IDS', 'FXS-MEDICAL', 'FXS-OUTPUTS', 'FXS-POPULATION', 'FXS-REPEAT', 'FXS-RETENTION', 'FXS-SCOPE', 'FXS-SPEED']
- [x] **no_banned_claims** — banned claims + superseded figures gates
- [x] **word_count** — 2161 слов против target 2150 (полоса линтера ±15%; жёсткие ±10% = ok)
- [x] **links_4_directions** — направления: {'up': 2, 'sideways': 2, 'down': 1, 'trust': 2}
- [x] **medical_framing** — «FitXpress is not a medical device.» ×2; «positioned as» ×0
- [x] **no_named_entities** — клиенты/конкуренты: нет
- [x] **no_stale_urls** — устаревшие URL: нет
- [x] **accuracy_discipline** — {'accuracy_figures_present': True, 'links_to_framework': True}
- [x] **m1_abbreviations** — gate 8 (M1)
- [x] **sentence_length** — mean 11.9
- [x] **faq_present** — FAQ: 3 вопросов
- [x] **boundary_section** — «does not do»-секция: False; scope note сверху: True
- [x] **scope_note_early** — курсивная scope note в первых строках

## Суждение seo-publisher — 6/6 judgment-пунктов ok (meta.md, verbatim без frontmatter)

## Judgment checklist

- [x] intro_hook: first two sentences state the operational scene directly ("A telehealth or GLP-1 program doubles its enrollment. Every self-reported height and weight that needs a second check or a re-entry becomes staff time.") — no throat-clearing, no rhetorical question.
- [x] cta_type: single direct CTA in Section 10 only, matching BOFU intent — "talk to 3DLOOK about the program's body-data workflow" links the product page's demo modal; no second CTA in the body.
- [x] anchors_sources: all internal anchors are descriptive (e.g. "guide to remote BMI verification methods", "progress-tracking requirements for GLP-1 programs"), none is "click here"; the one external source is CDC's *Preventing Chronic Disease* (government research, not a vendor blog).
- [x] cannibalization: BMI guide's verification workflow, glp-1-market's sizing, the engagement article's retention argument and the accuracy framework's methodology are each linked and not restated, matching the pack's guardrails; this refresh replaces itself at the same URL, no new competing page.
- [x] distinct_intent: the page owns one question — how much manual work body-data verification creates as a program scales, and how to model the return of standardizing capture — distinct from the telehealth hub (AI survey), the BMI guide (verification how-to), glp-1-market (market sizing) and the accuracy framework (methodology).
- [x] vertical_boundary: telehealth and GLP-1 boundaries both hold — no dosing, no eligibility decisioning, no DXA/BIA/scale replacement claim, no 3DLOOK-supplied ROI or outcome figure anywhere on the page (confirmed in editor-report.md's ROI-section check).

## Meta variants

### Title
1. Accuracy and Digital Health ROI: Verified vs Self-Reported (58 chars) — recommended. Keeps "Accuracy" and "ROI" per the brief, carries the exact primary keyword "digital health roi" starting at character 14 (first half), no em dash.
2. Digital Health ROI: Accuracy vs Self-Reported Data (50 chars) — keyword-first alternative, shortest, if the publisher wants maximum SERP room.
3. Accuracy and ROI in Digital Health: Self-Reported vs Verified Data (66 chars, the plan's suggestion) — rejected: over the 60-char budget, and it does not contain the primary keyword as a contiguous phrase ("ROI in Digital Health" reorders the words), which the assemble script's mechanical check would flag.

### Description
1. As enrollment grows, checking self-reported height and weight eats staff time. Compare capture methods and build a digital health ROI model from your numbers. (158 chars) — recommended. Leads with the manual-work problem, not FitXpress, per the plan's direction; names both new assets (Section 4 comparison, Section 5 model); keyword appears once; no digits (accuracy-formulations canon: a meta description has no room for the reference/population/protocol condition a figure needs, so it carries none).

## Open items

1. **Request indexing in GSC after republish.** The URL was dropped from Google's index on 2026-09-20 ("Crawled – currently not indexed", a quality judgement, not a technical fault). After the live page is replaced, request indexing via URL Inspection; do not assume the crawl will pick it up on its own schedule.
2. **Three inbound links to add on other pages** (refresh-gap-analysis.md §6, for Vadim/the web team, not this article):
   - `the-potential-of-ai-in-telehealth` — anchor "help remote-monitoring workflows scale" in the sentence about standardized capture and documentation.
   - `online-pharmacy-bmi-verification-a-2026-compliance-guide` — anchor "manual-review requirements grow" in the sentence about the operational effect of verification limits at volume.
   - `glp-1-market`, section "The Infrastructure Challenge Created by Market Growth" — one new sentence on scaling progress tracking without more in-person visits, linking here.
   `mobile-body-scanning-patient-engagement` already links to this page; no action needed there.
3. **FAQ schema now has 3 entries, not 4.** The editor merged the two eligibility/dosing questions from the plan's 4-question FAQ into one (editor-report.md: "the two FAQ questions that S7 and the scope note already answer are merged into one"). Whoever wires the FAQ schema markup should build it from final.md's three `### ` questions, not from plan.md's Section 9 spec.
4. **Link the telehealth-documentation article once it is live.** It is not published yet (workspace `2026-09-21-ai-body-scanning-telehealth-documentation`, pencilled Oct 2026). Section 3 currently names "documentation assembled after the fact" as one source of manual work with no link, as planned. Add the link there when the article ships; do not link a non-live URL now.
5. **Byline: Vadim Bilan, kept.** This is a refresh of his own original article (published 2026-01-07); CLAUDE.md §15's default-to-Assel does not apply to a refresh of an existing byline. Flag this explicitly in the digest so Vadim confirms it is still his intent.
6. **For the web editor: this is an in-place replacement, not a new post.** Replace the live body at `https://3dlook.ai/content-hub/accuracy-drives-roi-digital-health/` with final.md's content. The WordPress slug `accuracy-drives-roi-digital-health` stays exactly as is. No redirect, no new URL, no change to `live_published` (2026-01-07); update `live_modified` to the republish date.
7. **Thin demand, accepted knowingly (plan-audit.md #1).** The primary keyword measures 40/month; the refresh is justified by the deindexing and the compliance defects on the live page, and by GEO/sales support on the position 4-9 "self-reported vs verified" question family, not by search volume. No action needed, flagging for the digest so it reads as a deliberate call, not an oversight.
8. **Yazen dropped, differs from the plan.** The plan allowed one optional sentence naming Yazen (34K scans) in Section 7; the editor cut it and final.md carries no customer name. This is a valid editorial call (no compliance issue, no-client-names rule is an outbound-only rule), noting it only because it is a plan deviation worth Vadim seeing once.
9. **Weight-estimate wording resolved.** plan-audit.md #3 flagged "weight estimate" vs the BMI guide's "predicted weight" as needing confirmation. final.md uses "weight estimate" / "estimated weight" consistently throughout (Section 4 table, Section 7); this is the plan's chosen term and did not need to change.

## Image and alt-text suggestions

1. Cover, top under the H1 (Section 1). Concept: a program dashboard view, one column of self-reported entries showing gaps and flags, one column of timestamped structured records, no numbers on the image. Alt: "Dashboard view comparing self-reported entries with gaps to timestamped structured body-data records" (100 chars)
2. Image 1, Section 5 after the ROI variables table. Concept: three cost streams (staff handling time, exceptions and resubmissions, onboarding drop-off) flowing into one "cost per patient onboarded" box, split into a before-pilot and during-pilot view, no figures. Alt: "Diagram of three cost streams flowing into a cost-per-patient-onboarded box, before and during a pilot" (102 chars)
3. Image 2, Section 6 (GLP-1 clinic operations). Concept: a between-visit timeline for a GLP-1 program, baseline scan at enrollment, at-home scans at protocol-set intervals, a clinician visit reviewing the comparison. Alt: "Timeline of a GLP-1 program from baseline scan to at-home scans to a clinician visit reviewing progress" (103 chars)

## article_lint.py, verbatim

```
workspace/seo/articles/accuracy-roi-telehealth-refresh/final.md
mode: article

[ok  ] hard bans (detect-ai-tells)
         . detector_words: 2373
         . ai_density: 0.0
         . verdict: CLEAN
         . rhythm_variation: 0.45
[ok  ] prose length
         prose words 2161 vs target 2150 (band 1827-2472)
         . prose_words: 2161
         . target: 2150
[ok  ] claim traceability
         . claims_used: ['FXS-ACCURACY', 'FXS-DELIVERY', 'FXS-GDPR', 'FXS-HIPAA', 'FXS-IDS', 'FXS-MEDICAL', 'FXS-OUTPUTS', 'FXS-POPULATION', 'FXS-REPEAT', 'FXS-RETENTION', 'FXS-SCOPE', 'FXS-SPEED']
         . claims_known: 13
[ok  ] banned claims
[ok  ] superseded figures
[ok  ] internal links
         . links_total: 9
         . links_distinct: 7
         . asset_urls: 0
         . directions: {'up': 2, 'sideways': 2, 'down': 1, 'trust': 2}
[ok  ] keyword placement
         . keyword: digital health roi
         . occurrences: 2
         . h2_count: 10
         . in_first_paragraph: False
[ok  ] abbreviations (M1)
[ok  ] accuracy discipline
         . accuracy_figures_present: True
         . links_to_framework: True
[ok  ] sentence length
         . limits: article (mean <= 16, <= 6% over 25, <= 1 over 35)
         . sentences: 132
         . mean_words: 11.9
         . p90_words: 19
         . over_25: 0 (0.0%)
         . over_35: 0
         . near_duplicate_pairs: none
         . repeated_phrases: none

VERDICT: PASS
Mechanics are clean. Judgment is still open: run quality-controller on whether
the argument holds and whether each section earns its place.
```

## detect-ai-tells.py, verbatim (--summary)

```
SEO / blog article · en · 2373 words
AI density: 0.0/1000 (budget 6.0) -> low
VERDICT: CLEAN — check the positive side (voice, varied rhythm, a stated boundary) and ship.
```

## Article

Текст НЕ дублируется в пакете: единственный источник — `final.md` (2161 prose words) рядом с этим файлом.
