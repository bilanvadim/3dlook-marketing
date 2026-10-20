---
slug: 2026-09-19-glp-1-fitness-apps-body-composition-tracking
product: fitxpress
status: ready_for_review
pipeline_mode: no-checkpoint
revision: 4
review_round: "Review 1 (2026-10-20), structural"
published_slug: glp-1-muscle-loss-fitness-apps
author: Assel Sekerova
created: 2026-10-20
generated_by: scripts/article_package.py (mechanics) + seo-publisher meta.md (judgment)
source_final: "final.md (1795 prose words, lint FAIL)"
word_count: 1795
stop_rule: OK
---

# Publish Package — 2026-09-19-glp-1-fitness-apps-body-composition-tracking

## Meta

**Title:** GLP-1 Muscle Loss Concerns: Fitness App Progress Views (54/60 chars)
**Description:** What fitness apps can show beyond scale weight for members on GLP-1 treatment, what research says on GLP-1 muscle loss, and what a scan cannot determine. (153/160 chars)
**Slug:** `glp-1-muscle-loss-fitness-apps`
**Category:** AI in Fitness

## Механический чек-лист (17/17, считал скрипт)

- [x] **lint_verdict** — article_lint: FAIL (FAIL только из документированного M1-титульного кейса, gate_m1_note во frontmatter)
- [x] **detector_clean** — ai_density 0.0/1000, hard_fails [], house_rules []
- [x] **keyword_h1** — «glp-1 muscle loss» в H1: «GLP-1 Muscle Loss Concerns for Fitness Apps: Tracking Body Change Beyond Scale Weight»
- [x] **keyword_h2** — keyword в 1 H2 (норма 1-2)
- [x] **claims_traceable** — claims_used: ['FXS-ACCURACY', 'FXS-DELIVERY', 'FXS-LIFECYCLE', 'FXS-MEDICAL', 'FXS-OUTPUTS', 'FXS-POPULATION', 'FXS-REPEAT', 'FXS-SPEED', 'T-34K', 'T-BASELINE', 'T-BODY-PROGRESS', 'T-ESTIMATES', 'T-GUARDRAIL-DXA', 'T-MUSCLE-FUNCTION', 'T-PRIVACY-ROLES', 'T-RECORDS-ACTORS', 'T-REPEAT-SCOPE', 'T-TABLE', 'T-VALIDATION', 'T-WEIGHT-SOURCE']
- [x] **no_banned_claims** — banned claims + superseded figures gates
- [x] **word_count** — 1795 слов против target 1600 (полоса линтера ±15%; жёсткие ±10% = MISS — отметить в open items)
- [x] **links_4_directions** — направления: {'up': 2, 'sideways': 2, 'down': 1, 'trust': 2}
- [x] **medical_framing** — «FitXpress is not a medical device.» ×1; «positioned as» ×0
- [x] **no_named_entities** — клиенты/конкуренты: нет
- [x] **no_stale_urls** — устаревшие URL: нет
- [x] **accuracy_discipline** — {'accuracy_figures_present': True, 'links_to_framework': True}
- [x] **m1_abbreviations** — gate 8 (M1) — известный титульный кейс (H1, gate_m1_note), прецедент 2026-09-19; в open items дайджеста
- [x] **sentence_length** — mean 15.3
- [x] **faq_present** — FAQ: 2 вопросов
- [x] **boundary_section** — «does not do»-секция: False; scope note сверху: True
- [x] **scope_note_early** — курсивная scope note в первых строках

## Суждение seo-publisher — 8/8 judgment-пунктов ok (meta.md, verbatim без frontmatter)

## Judgment checklist

- [x] intro_hook: opens on a member logging a falling scale weight that cannot say fat, lean mass or fluid, so the problem lands in sentence one and two.
- [x] cta_type: MOFU evaluation link in Next steps to the fitness landing, no demo button, as plan.md prescribes.
- [x] landing_link: down link is "body composition tracking for fitness apps" to /fitxpress/for-connected-and-digital-fitness/ (live, Link now), at 15.8% of the body, anchor from the map; no stand-in, no relink debt.
- [x] anchors_sources: anchors read as part of the sentence; outside sources are PubMed (Neeland 2024), obesity.org advisory and KFF, none are vendor blogs.
- [x] cannibalization: row 125/166/167 do not target muscle loss after this ships (noted below); existing GLP-1 market and coaching articles are linked, not repeated; guardrail of the pack held.
- [x] distinct_intent: owns "what a fitness app can show for members on GLP-1 treatment", not methods education (row 167) and not the GLP-1 market argument.
- [x] vertical_boundary: no dosing, eligibility, drug names or muscle assessment; scope note and FAQ 1 state the scan does not measure muscle or muscle loss.
- [x] terminology_actors: fitness app, member, prescribing clinician and GLP-1 program are named; no organization or buyer; "customer" only inside the locked repeatability lead.

## Meta variants

### Title
1. GLP-1 Muscle Loss Concerns: Fitness App Progress Views (54 chars)
2. GLP-1 Muscle Loss Questions: What Fitness Apps Can Show (56 chars)

### Description
1. What fitness apps can show beyond scale weight for members on GLP-1 treatment, what research says on GLP-1 muscle loss, and what a scan cannot determine. (153 chars)

## Open items

- H1 swap for Vadim: the reviewer's own H1 is "GLP-1 and Fitness Apps: Tracking Body Change Beyond Scale Weight". It is a one-line swap, but it drops the primary keyword "glp-1 muscle loss" from the H1, so the H1 keyword gate fails unless the primary keyword is changed too. The shipped H1 keeps "GLP-1 Muscle Loss Concerns for Fitness Apps: ...".
- 34,000 scans: the reviewer asks for the customer's explicit permission to describe this use publicly. The 19.09 decision only covers the anonymized mention. If sign-off is wanted and not given, cut the two T-34K sentences (their own paragraph in Section 5); the cut is clean.
- Incoming links after publication (CMS work for Assel / site editors): add contextual links into this article from ai-in-fitness-industry and glp-1-market.
- M1 accepted: "GLP-1" in the H1 is used before it is expanded, so article_lint reports one FAIL on that gate only (Vadim, 2026-09-19). Every other gate passes.
- Wording differs from the decisions file, no action unless the reviewer wants her words back: the joint advisory is quoted as "strength training" (the advisory's own term on obesity.org; "resistance" does not occur there), where decisions §6 says "resistance training". The reviewer's "does not, by itself, fulfill all of that guidance" ships as "An app that offers workouts can support one part of that guidance." (stacked-negation rule). Same meaning, no claim added.
- Content plan sync: once this is live, rows 125, 166 and 167 should not target muscle loss (planner open item 9).
- Primary keyword is a weak match: glp-1 muscle loss is 600 / KD 45 with a consumer-heavy SERP, confirmed by Vadim on 19.09. Expect answer-engine coverage and the Hub 1 to Hub 3 link path, not classical organic volume.
- Customer name: the 34,000-scan customer is never named; the plan-audit question about naming Yazen is moot for this revision.
- Live-page debt, not ours: the live coaching article's privacy paragraph still says "maintains HIPAA compliance" and "adheres to GDPR principles", both retired in compliance.md since 2026-09-18.
- Page is not live (404 on 2026-10-20), so the slug glp-1-muscle-loss-fitness-apps is free.

## Image and alt-text suggestions

1. Cover, top of the article. Concept: a phone on a gym bench beside a dumbbell, showing a check-in card with a dated weight line and a waist tile marked "body scan". Any body is a neutral outline, no muscle definition. Alt: "Phone on a gym bench showing a fitness app check-in card with a weight trend and a waist measurement tile" (104 chars)
2. Image 1, Section 3 after the table. Concept: annotated app progress view labeled "Illustrative example". Three dated trend rows share one time axis: weight (entered by member or synced from scale), waist and hip circumferences (body scan), composition estimates (estimate), with training blocks. No muscle overlay, anatomy or muscle labels. Alt: "Illustrative fitness app progress view with dated weight, waist, hip and estimate trends and training blocks" (107 chars)
3. Image 2, Section 4 check-ins. Concept: capture to results. Two phone screens with pose outline and framing guide for front and side photos, then a results screen with circumferences, a smooth neutral 3D body model and estimates tagged "estimate". No muscle definition or labels. Alt: "Two phone screens guiding front and side photo capture, next to a results screen with body measurements" (102 chars)

## Change log

- QC (seo-qc) 16/20 ship with notes; editor fix pass on QC findings 1-2 applied, finding 3 (trim scope note) declined because decisions §6 keeps the scope note verbatim.

## article_lint.py, verbatim

```
workspace/seo/articles/2026-09-19-glp-1-fitness-apps-body-composition-tracking/final.md
mode: article

[ok  ] hard bans (detect-ai-tells)
         . detector_words: 2247
         . ai_density: 0.0
         . verdict: CLEAN
         . rhythm_variation: 0.56
[ok  ] prose length
         prose words 1795 vs target 1600 (band 1360-1839)
         . prose_words: 1795
         . target: 1600
[ok  ] claim traceability
         . claims_used: ['FXS-ACCURACY', 'FXS-DELIVERY', 'FXS-LIFECYCLE', 'FXS-MEDICAL', 'FXS-OUTPUTS', 'FXS-POPULATION', 'FXS-REPEAT', 'FXS-SPEED', 'T-34K', 'T-BASELINE', 'T-BODY-PROGRESS', 'T-ESTIMATES', 'T-GUARDRAIL-DXA', 'T-MUSCLE-FUNCTION', 'T-PRIVACY-ROLES', 'T-RECORDS-ACTORS', 'T-REPEAT-SCOPE', 'T-TABLE', 'T-VALIDATION', 'T-WEIGHT-SOURCE']
         . claims_known: 25
[ok  ] banned claims
[ok  ] superseded figures
[ok  ] internal links
         . links_total: 13
         . links_distinct: 7
         . asset_urls: 0
         . directions: {'up': 2, 'sideways': 2, 'down': 1, 'trust': 2}
[ok  ] keyword placement
         . keyword: glp-1 muscle loss
         . occurrences: 2
         . h2_count: 7
         . in_first_paragraph: False
[FAIL] abbreviations (M1)
         line 2: GLP-1 used before being expanded as 'glucagon-like peptide-1' (guardrail M1)
[ok  ] accuracy discipline
         . accuracy_figures_present: True
         . links_to_framework: True
[ok  ] sentence length
         . limits: article (mean <= 16, <= 6% over 25, <= 1 over 35)
         . sentences: 94
         . mean_words: 15.3
         . p90_words: 22
         . over_25: 1 (1.1%)
         . over_35: 0
         . near_duplicate_pairs: none
         . repeated_phrases: ['scan to scan x4', 'the progress view x3', 'the prescribing provider x3', 'the app team x3', 'glp 1 treatment x3', 'body composition tracking x3']

VERDICT: FAIL  (1 gate(s) failed)
```

## detect-ai-tells.py, verbatim (--summary)

```
SEO / blog article · en · 2247 words
AI density: 0.0/1000 (budget 6.0) -> low
VERDICT: CLEAN — check the positive side (voice, varied rhythm, a stated boundary) and ship.
```

## Article

Текст НЕ дублируется в пакете: единственный источник — `final.md` (1795 prose words) рядом с этим файлом.
