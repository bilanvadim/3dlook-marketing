---
product: fitxpress
profile: nick
market: USA
created: 2026-08-07
status: draft
---

# Outbound Hypothesis — 2026-08-07 (US Consumer Digital Fitness & Weight Management)

## Vertical
US-headquartered consumer digital fitness and weight-management platforms — subscription apps and connected-fitness services in the "Connected & Digital Fitness" ICP segment (icp-detail.md §8), where the core job is retaining paying subscribers and showing visible physical progress over time. This is Nick's (BD, USA) first campaign; USA-only per geo discipline (CLAUDE.md §5). Inspired by our client Erakulis (CR7's fitness/nutrition/sleep app with a phone-camera BodyScan feature) as a proof-point that a consumer app already wants an embedded body-composition layer — Erakulis is NOT US-HQ and is our customer, so it must never be a target, only the vertical inspiration.

## Sub-segment
US-HQ consumer subscription fitness / weight-loss / nutrition / wellness apps and connected-fitness platforms with:
- ~$1M+ annual recurring revenue (subscription-focused; the §8 floor), roughly Series B through public,
- mobile-first delivery (iOS/Android, freemium or paid),
- body metrics / body composition already shipped as a feature OR a natural next feature (weight/measurements/progress tracking present but shallow).

Three flavors inside the net:
- **Weight-management / GLP-1 companion apps** — consumer-facing tracking and coaching apps riding the GLP-1 wave that need to prove body-composition outcomes (fat vs lean mass), not just scale weight.
- **Connected & digital fitness / coaching apps** — training, body-transformation and AI-coaching subscriptions that live or die on visible progress and retention.
- **Nutrition / holistic wellness apps** — multi-pillar consumer apps (fitness + nutrition + recovery) adding a body-metrics pillar as a differentiator, the Erakulis pattern.

## Use case (1 sentence)
FitXpress as the embedded verified body-composition and progress-visualization layer for US digital fitness and weight-loss apps — a 2-photo scan producing 80+ measurements, body composition (body fat %, lean mass, fat mass, BMI, BMR) and a 3D progress model in under 45 seconds via API/SDK, so an app gets the "BodyScan" feature every fitness app wants without building computer vision in-house.

## Why this is plausible (3 reasons grounded in evidence)
1. **GLP-1 boom makes body-composition outcomes the retention battleground.** Lean-mass loss is the defining clinical conversation in GLP-1 weight loss right now — roughly 40% of total weight lost was lean mass in the STEP-1 semaglutide substudy vs ~25% in the SURMOUNT-1 tirzepatide substudy — so the 2026 differentiator among weight-loss programs is not the drug but whether the app can show how much of the loss is fat vs muscle. Consumer GLP-1 tracking apps (Shotsy, WeightWatchers GLP-1 program and peers) are already adding body-fat / lean-body-mass / waist-circumference tracking, but mostly rely on manual entry or a smart scale. FitXpress supplies verified body composition from a phone, which is the exact metric these apps now need to prove results and retain subscribers. Sources: [learnmuscles — 6 best GLP-1 tracking apps 2026](https://learnmuscles.com/blog/2025/11/27/6-best-glp-1-tracking-apps-compared-which-app-actually-works-in-2026/), [medspastandards — GLP-1 & body composition 2026](https://medspastandards.com/blog/glp1-muscle-loss-body-composition-med-spa-2026), [Healthline — tracking weight loss on GLP-1s](https://www.healthline.com/health/drugs/tracking-weight-loss-on-glp-1s).
2. **Fitness apps have the steepest churn curve in consumer subscriptions, and visible progress is a proven retention lever.** US-relevant 2026 benchmarks put median fitness-app monthly churn at ~10-13% (top quartile 4-6%), annual subscription retention around 33%, and ~38% of cancellations driven by loss of motivation / goal abandonment — the single largest churn driver, and precisely the gap that 3D progress visualization and side-by-side body comparison are built to close (icp-detail.md §8: "users lose motivation without visible progress"). In a market sized at ~$15.35B in 2026 growing ~13% CAGR, even small retention gains compound into large LTV, so a retention feature has a clear business case. Sources: [Lifecycle Architect — fitness app churn benchmarks 2026](https://lifecyclearchitect.com/benchmarks/fitness-apps-churn-rate-benchmarks/), [RetentionCheck — fitness app churn 2026](https://retentioncheck.com/churn-benchmarks/fitness-apps), [Mordor Intelligence — digital fitness apps market](https://www.mordorintelligence.com/industry-reports/digital-fitness-apps-market), [Adapty — health & fitness subscription benchmarks](https://adapty.io/blog/health-fitness-app-subscription-benchmarks/).
3. **Differentiation + a clean US regulatory lane, and the product fit is evidenced in our own materials.** AI personalization is now table stakes across fitness apps (icp-detail.md §8: "users expect AI personalization"); verified physical progress is not — it's a defensible, hard-to-fake feature that a content or AI-coaching app can't cheaply replicate. Crucially for a consumer play, body-composition trend tracking sits inside the FDA's General Wellness "low-risk device" enforcement-discretion lane as long as it stays non-diagnostic, is not tied to disease claims, and isn't used for clinical decision-making — which matches 3DLOOK's "operational, not clinical" positioning (CLAUDE.md §3) and keeps the feature out of regulated-device territory. HIPAA posture still matters when handling user health data; our compliance story (HIPAA-maintained, GDPR-aligned, photos deleted immediately or within 30 days, no personal identifiers processed, encryption at rest/in transit) is a selling point, not an afterthought. Product fit is direct: proof-points.md gives us 96-97% accuracy, <1 cm typical scan-to-scan repeatability, under 45s, 80+ measurements, full body-composition outputs, and fx-digital-fitness.md names this exact buyer/pain/KPI set with the "personalize training and visualize real progress with 3D scans" hero. Sources: [Troutman — FDA 2026 general wellness guidance](https://www.troutman.com/insights/fdas-2026-guidance-on-general-wellness-devices-policy-for-low-risk-devices/), [Faegre Drinker — 2026 general wellness & CDS updates](https://www.faegredrinker.com/en/insights/publications/2026/1/key-updates-in-fdas-2026-general-wellness-and-clinical-decision-support-software-guidance), `brand-assets/product-info/proof-points.md`, `brand-assets/product-info/use-cases/fx-digital-fitness.md`, `brand-assets/product-info/icp-detail.md` §8.

## Target buyer personas
- **Founder / CEO (primary for smaller/Series-B apps).** Owns the product-differentiation and retention bet. Cares about: subscription retention, LTV/CAC, standing out in a crowded app store. Objection: "Is a body scan enough to move retention?" → answer with the visible-progress / churn-driver evidence and the 200-request free trial to test on a cohort.
- **Chief Product Officer / Head of Product (primary).** Owns the roadmap and the "build vs buy" call on a BodyScan feature. Cares about: feature velocity, engagement/DAU-WAU, activation. Objection: "We could build this" → pre-trained model via API/SDK, no in-house computer-vision team or ML expertise required, ~weeks not quarters.
- **VP Engagement / VP Retention / Head of Growth.** Owns the metric this use case moves. Cares about: month-2-3 drop-off, check-in cadence, retention curve, CAC payback. Objection: "Will users actually do a scan?" → 2 photos, <45s, framed as a motivating 3D before/after, not a chore.
- **CTO / VP Engineering (technical-integration entry, weaker/P3 per icp-detail.md IT policy).** Not the economic buyer but the implementer/champion. Cares about: API/SDK quality, time-to-integrate, HIPAA architecture (photos processed not stored, deleted after extraction), reliability/scale. Use the `technical-integration` message angle for this persona.

## Anti-cases (where FitXpress does NOT fit)
- **Pure gym hardware / equipment makers with no software subscription layer** — no recurring-engagement surface to embed a scan into; retention economics don't apply.
- **Fitness content-only platforms with no measurement ambitions** (pure video libraries / streaming classes) — no body-data hook, wrong buyer conversation.
- **Platforms positioned on medical claims / as a regulated device** (diagnostic, disease-treatment or clinical-decision positioning) — would pull the engagement into regulated-device territory and outside FitXpress's "operational not clinical" scope (CLAUDE.md §3); if a consumer app is making disease claims, it's the wrong fit for this consumer angle.
- **Sub-$1M / pre-revenue apps with no integration budget** (§8 floor is $1M+; universal exclusion screens out free/freemium-only consumer apps with no enterprise/paid budget).
- **Recently acquired / merged companies** (ICP shifting, stalled sales cycle).
- **Non-US-HQ platforms — flag, do NOT hard-rule-out as a product anti-case.** FitXpress fits these fine as a product; this is a geo-discipline exclusion for THIS profile/campaign only (Nick = USA). Erakulis specifically is excluded on two counts: non-US-HQ AND existing customer — it is the inspiration, never a target. company-researcher should route any strong non-US fits to the appropriate geo profile rather than discard them.

## Validation criteria (Step 2 / company-researcher will check)
- At least 25-30 US-HQ consumer subscription fitness / weight-loss / nutrition-wellness apps matching the sub-segment ($1M+ ARR, mobile-first, body metrics shipped or a natural next feature) exist and are neither existing customers nor competitors (Prism Labs, Bodygram, Size Stream).
- Founder/CEO, CPO/Head of Product, VP Engagement/Retention, Head of Growth, or CTO contacts are reachable via Sales Navigator / open sources for a workable share of the list.
- Each candidate is genuinely US-HQ (not just US-operating) — geo discipline for the `nick` profile; non-US fits get flagged for other profiles, not force-fit here.
- A usable proof-point / analog exists without over-claiming — the Erakulis BodyScan pattern (as a vertical proof, not a named reference in cold copy without approval) plus fx-digital-fitness KPIs; confirm what can be said publicly with Vadim.
- Candidate positioning stays in general-wellness (non-diagnostic) territory, not medical-claims / regulated-device.

## Success metrics for this campaign
- Acceptance rate: target >= 30%
- Reply rate: target >= 5%
- Positive replies: target >= 4
- Qualified leads: target >= 2

## Open questions for Vadim
1. **Erakulis as a reference:** can we name Erakulis / "CR7's app" as a proof-point in outreach copy, or is it inspiration-only and must stay out of messages? Default assumption until confirmed: do NOT name it in cold copy.
2. **Lead angle:** recommend leading on retention + visible progress (the churn evidence) with GLP-1 body-composition outcomes as the sharpest "why now" wedge for weight-management apps, and reserving the `technical-integration` angle for CTO/eng contacts. Confirm the primary angle before message-sequencer.
3. **US HIPAA posture for consumer (non-clinical) apps:** confirm how hard to lead on HIPAA/data-handling for a *consumer* audience vs. keeping it as a reassurance point — some consumer PMs won't have HIPAA on their radar, and over-indexing on it can read as clinical.
4. **Net width:** the sub-segment reaches beyond pure fitness into GLP-1 companion apps and multi-pillar wellness/nutrition apps. Confirm you want the wider net for a first US campaign, or prefer a tighter first cut (e.g., weight-management companion apps only).

## Sources
- [learnmuscles — 6 best GLP-1 tracking apps compared (2026)](https://learnmuscles.com/blog/2025/11/27/6-best-glp-1-tracking-apps-compared-which-app-actually-works-in-2026/)
- [medspastandards — GLP-1 muscle loss & body composition 2026](https://medspastandards.com/blog/glp1-muscle-loss-body-composition-med-spa-2026)
- [Healthline — tracking weight loss on GLP-1 medications](https://www.healthline.com/health/drugs/tracking-weight-loss-on-glp-1s)
- [Lifecycle Architect — fitness app churn benchmarks 2026](https://lifecyclearchitect.com/benchmarks/fitness-apps-churn-rate-benchmarks/)
- [RetentionCheck — fitness app churn 2026](https://retentioncheck.com/churn-benchmarks/fitness-apps)
- [Mordor Intelligence — digital fitness apps market](https://www.mordorintelligence.com/industry-reports/digital-fitness-apps-market)
- [Adapty — health & fitness app subscription benchmarks](https://adapty.io/blog/health-fitness-app-subscription-benchmarks/)
- [Troutman Pepper Locke — FDA 2026 general wellness guidance](https://www.troutman.com/insights/fdas-2026-guidance-on-general-wellness-devices-policy-for-low-risk-devices/)
- [Faegre Drinker — key updates in FDA's 2026 general wellness & CDS guidance](https://www.faegredrinker.com/en/insights/publications/2026/1/key-updates-in-fdas-2026-general-wellness-and-clinical-decision-support-software-guidance)
