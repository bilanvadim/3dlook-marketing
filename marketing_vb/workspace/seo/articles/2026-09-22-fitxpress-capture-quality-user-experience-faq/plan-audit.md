---
slug: fitxpress-capture-quality-user-experience-faq
plan: plan.md
created: 2026-09-22
audience: seo-publisher, Vadim, external reviewer (not needed by the writer)
---

# Plan audit: fitxpress-capture-quality-user-experience-faq

## Open items (for Vadim / product before publish)

1. **Primary keyword vs fixed H1.** Seed `body scanning app accuracy` has no Ahrefs data (`seed_has_data: false`). The brief fixes the H1 ("FitXpress User Experience and Capture Quality FAQ"), and `article_lint.py` gate 7 requires the primary keyword in the H1 and one H2. No measured term fits that H1. Resolution: `primary_keyword: capture quality` (unmeasured, no data, not 0) as the on-page anchor; `body measurement app` (150/mo, KD 22) recorded as the demand head and woven once. Vadim confirms that a GEO / sales-support FAQ with no measured primary demand is acceptable (same call as the GLP-1 Progress Record article, 2026-09-21).
2. **RTPV naming.** Coordinator decision: keep "Real-Time Pose Validation (RTPV)" as in the brief and the approved meta description, defined at first use as the SDK's real-time pose and tilt validation. The acronym is not attested in product-info canon (tech-spec.md, how-it-works.md, faq.md, overview.md). Confirm with product that RTPV is the customer-facing name. If not, Q2's H3 and the schema `Question.name` must change together.
3. **Clothing Detector behavior.** Coordinator decision: use "Clothing Detector" as the brief does, described as a capture-quality feature with canon behavior only (tech-spec.md:47-50: classifies fit sport / regular / oversized, flags and prompts the user, flag in the response payload). Proper-noun naming is not attested in canon. Confirm current customer-facing behavior and naming (brief §6.4 asks for this explicitly).
4. **Blocked vs prompted capture.** Not confirmed anywhere. The plan says prompts, corrections, another attempt only. If product confirms a hard block for some conditions, Q3/Q4 can say so later.
5. **BMI inputs (Q11).** Plan says "where the required inputs are provided (height is submitted; weight is optional)", from FXS-LIFECYCLE. Confirm whether BMI without a submitted weight uses Smart Scales predicted weight; if yes, the brief reserves "predicted weight" for Smart Scales and Q11 needs a precise sentence. Currently Smart Scales is deliberately not mentioned.
6. **Timing.** Only "under 45 seconds" for the full processing pipeline (FXS-SPEED). about-me.md also lists a sub-30-second figure for measurements plus model; excluded per brief §6.9 and coordinator decision (no sub-timings). Capture and onboarding time are described qualitatively.
7. **React Native, timer / voice guidance.** Omitted per coordinator decision. If product confirms either, Q7/Q8 can add it.
8. **Quick answers table rewording.** Three qualifications in brief §5 are editorial instructions ("Do not claim that…"). Plan rewrites them as publishable statements (rows Clothing, Retakes, Timing). Timing row states the figure instead of "the approved product timeframe". Vadim may prefer the brief's literal cells.
9. **Q3 apostrophe.** Brief uses a curly apostrophe ("user’s"). Plan standardizes to straight `'` in both the H3 and schema. Check the CMS renders the same character in both.

## Phase 0 record
- Pack: `phase_0_resolved: true`; action_type verbatim "Create net-new (off-plan, approved by Vadim 2026-09-22)". No content-plan row sought, per coordinator.
- Inventory: `already_live: false`.
- Cannibalization check (5 questions):
  1. Existing article answering this? No page owns capture quality / input controls. Adjacent pages own mechanics (3dlook-turns-two-photos-structured-body-data), accuracy (mobile-body-scanning-accuracy), engagement/progress (mobile-body-scanning-patient-engagement), privacy (trust FAQ), telehealth BOFU (structured-body-data-for-telehealth-digital-health-programs).
  2. Title overlap with a hub? No. "Capture quality" and "user experience" appear in no live H1.
  3. Broad enough for a page? Yes: 11 distinct procurement questions, brief-mandated.
  4. Refresh / section-first signal? None (off-plan, approved net-new).
  5. Intent owned: "Can remote users produce reliable body data without staff supervision?" plus how FitXpress controls photo quality, pose, clothing, and conditions.
- Guard against overlap: each adjacent topic gets one link at first mention and at most two sentences.

## Keyword analysis (full)
Source: pack `keywords_raw`, Ahrefs API v3, pulled 2026-09-22, 3,352 units across four seeds. Figures as in the pack, not rounded.

| Keyword | Volume | KD | Note |
|---|---|---|---|
| body scanning app accuracy (seed) | no data | no data | `seed_has_data: false` |
| body scanning | 450 | 43 | broad, mostly consumer / off-intent; not targeted |
| body scan app | 150 | 46 | parent topic "body scanner"; ideas mostly body-scan meditation and smart-scale apps |
| body measurement app | 150 | 22 | best volume/difficulty ratio; parent "body measurement tracker"; demand head |
| 3d body scanning app | 90 | no data | KD null = not measured, not 0 |
| body measurement tracker app | 70 | 8 | consumer tracker framing |
| body measurement app for clothing | 70 | 1 | apparel intent (Mobile Tailor); excluded from this FitXpress page |
| body scanning app | 50 | 1 | easy, small |
| 3d body scan app | 30 | 55 | small, hard |
| app accuracy | 0 | n/a | measured zero |
| capture quality (on-page primary) | not pulled | not pulled | brand/product term, GEO anchor |

Honest line: the whole on-topic cluster is 30-150/mo and mostly consumer intent. The page is a canonical procurement FAQ for answer engines, sales enablement, and internal linking. Traffic from these terms will be small. The H1 / SEO title / URL stand per brief regardless.

## Title
- H1 and SEO title are fixed by the brief (§2) and not re-generated. Five-variant exercise skipped deliberately; generating alternatives to an approved external brief would only create a decision nobody asked for.
- SEO title "FitXpress Capture Quality & User Experience FAQ" (47 chars) fits the SERP limit.

## Structure decisions
- **H2 grouping.** The brief lists 11 questions in order without groups. The structural model (live trust FAQ) groups H3 questions under descriptive H2s. Plan uses three groups in brief order: Q1-Q4 capture controls, Q5-Q7 conditions and exceptions, Q8-Q11 workflow, timing, outputs. First H2 carries the keyword ("How FitXpress controls capture quality").
- **12-part structure (about-me.md).** Mapped into FAQ form: buyer problem + short answer = intro and Quick answers; workflow = Q8; where FitXpress fits = Q1/Q2; what FitXpress does not do = Q2 boundary, Q8 scope, Q3/Q4 do-nots; implementation = Q6-Q9; FAQ = the whole body; CTA = Next steps. No separate "What FitXpress does NOT do" section: the boundaries sit inside the answers where the questions raise them, and a separate section would duplicate Q8.
- **Scope note.** Telehealth is a sensitive vertical, so an italic scope line closes the intro. It does not use the medical-device sentence, to avoid repeating it; that sentence sits once in Q8, where the brief requires it.
- **Q5 over budget.** 230 words, above the brief's 100-180 "most answers" band: it must carry three definitions plus a qualified evidence paragraph with its link. Q8 at 220 carries a 6-step list. All other answers 130-170.
- **FAQPage.** 11 questions only. Quick answers table and Next steps are not in the schema.

## Deliberately NOT covered (and why)
- Fat vs muscle progress, visual display of fat vs muscle change, 5/10/20-pound milestones (brief §7). Belong to the progress-tracking pages. Q11 is a bridge only.
- Two-photo model mechanics, training data, 3D model generation. Linked (Q1), not explained.
- Accuracy methodology, per-measurement figures, ISO 8559 benchmark, weight estimation accuracy. Owned by the accuracy framework; Q5 uses only the internal figures, qualified.
- HIPAA / GDPR / retention / storage / face-blur retention details. Linked to the trust FAQ from Q8; one face-obfuscation clause in Q2.
- Smart Scales and predicted weight. Not in the brief's outputs list; reserving the term avoids misuse.
- Billing of failed-pose scans (faq.md:72-73). Commercial detail; about-me.md bans pricing talk.
- Named clients (UK Meds, Yazen, others). Product-level FAQ; no names per coordinator and the 2026-09-19 decision.
- Competitors. Never named.
- Market sizing, underwriting KPIs. Out of scope.
- The internal repeatability percentage from proof-points.md. Never published.

## Claims map
| Claim id | Used in |
|---|---|
| FXS-SPEED | Table, Q1, Q9 |
| FXS-OUTPUTS | Q11 |
| FXS-DELIVERY | Intro, Q8 |
| FXS-ACCURACY | Q5 |
| FXS-REPEAT | Q5 |
| FXS-POPULATION | Q6 (text), Q7 (reference) |
| FXS-LIFECYCLE | Q4, Q11 |
| FXS-IDS | Q11 |
| FXS-SCOPE | Table, Q8 |
| FXS-MEDICAL | Q8 |
| FX-CQ-001 | Q1, Q2, Q5 |
| FX-CQ-002 | Table, Q1, Q2, Q3, Q7, Q10 |
| FX-CQ-003 | Table, Q4 |
| FX-CQ-004 | Q2 |
| FX-CQ-005 | Table, Q8 |
| FX-CQ-006 | Q10 |
| FX-CQ-007 | Q4, Q7 |
| FX-CQ-008 | Q8 |
| FXS-HIPAA, FXS-GDPR, FXS-RETENTION | not used; linked to trust FAQ |

## Publisher checklist hooks
- 11 H3 strings in the article = 11 `Question.name` in schema, byte-identical.
- Each of the 5 internal links appears exactly once; CTA link once.
- "under 45 seconds" is the only timing figure on the page.
- Accuracy figures appear only in Q5, with the framework link in the same paragraph; no ISO figure.
- No "React Native", "timer", "voice", "block", "reject", "muscle mass", "visceral", "predicted weight", client names.
