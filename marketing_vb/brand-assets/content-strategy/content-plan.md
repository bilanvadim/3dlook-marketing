# 3DLOOK Health Content Plan (Hub-and-Cluster Editorial Matrix)

> **Source of truth:** [Content Strategy spreadsheet](https://docs.google.com/spreadsheets/d/1Sy7EzzZZvCKyrD30pbhElEpCZDbzuMtMkxdiDTIP8AE/edit?gid=0#gid=0)
> **Rules that govern how to write against this plan:** [`content-strategy-guidelines.md`](./content-strategy-guidelines.md)
> **Scope:** FitXpress health verticals (fitness, telehealth, GLP-1, insurance, wellness, bariatrics, clinical trials, occupational health). Mobile Tailor is out of scope for this plan.
> **Last synced from source:** 2026-09-03. If the sheet changes, re-sync this file — it is the offline copy the agents read (they do not fetch Google). `scripts/content-plan-sync.py` pulls the sheet weekly (Mon 06:23 UTC) and reports drift; it rewrites `content-plan.csv` on `--sync` but never this file, because the per-hub preambles and condensed guardrails below are written by hand and are not in the sheet.
> **2026-09-03 sync found 31 changed rows across a two-month gap** — mostly publication status plus rewritten cannibalization guardrails in Hub 7, and **two priority moves (P2 → P1)**. Both are applied below. The clinical-trials cluster in particular replaced one generic guardrail with a per-row one, so those rows now carry different instructions than they did in July.
> **Last reconciled against the live site:** 2026-08-18 (7 health articles verified page-by-page — see `published-articles-inventory.md` → "Live-Page Verification Pass"), plus single-article checks on **2026-08-24** (`online-pharmacy-bmi-verification` rewrite) and **2026-08-28** (`glp-1-market` hub refresh). Publication status below reflects what is actually live, which can be ahead of the last sheet sync.

## Published P0 hubs (verified live 2026-08-18)

| Hub | Article | Published | Live URL |
|---|---|---|---|
| Hub 0 — Main Health | AI Body Data Across Health Programs | 2026-07-24 | https://3dlook.ai/content-hub/ai-body-data-health-hub/ |
| Hub 0 — Accuracy trust asset | Body Scanning Accuracy: A Framework for Enterprise Decisions | 2026-07-03 | https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/ |
| Hub 1 — Fitness | AI in Fitness: Structured Body Data, Progress Tracking, Coaching | 2026-07-31 | https://3dlook.ai/content-hub/ai-in-fitness-industry/ |
| Hub 2 — Telehealth | AI in Telehealth: Workflows, Privacy, Patient Experience, Remote Body Data | 2026-08-07 | https://3dlook.ai/content-hub/the-potential-of-ai-in-telehealth/ |
| Hub 2 — Patient experience | How Mobile Body Scanning Improves Patient Engagement | 2026-08-14 | https://3dlook.ai/content-hub/mobile-body-scanning-patient-engagement/ |
| Hub 7 — Clinical Trials | Standardizing Anthropometric Measurements for Hybrid & Decentralized Obesity Trials | 2026-07-17 | https://3dlook.ai/content-hub/clinical-trial-anthropometric-measurement-software-obesity-trials/ |
| Hub 8 — Occupational Health | Standardizing Occupational Health Screening | 2026-07-10 | https://3dlook.ai/content-hub/occupational-health-screening-software/ |
| Hub 3 — GLP-1 Market | GLP-1 Market Growth and the Need for Better Patient Progress Tracking — **refreshed, republished in place** | 2026-08-28 (re-dated by the republish) | https://3dlook.ai/content-hub/glp-1-market/ |
| Hub 4 anchor (+ Hub 2 BMI row) | Online Pharmacy BMI Verification: A 2026 Compliance Guide — **rewritten, republished in place, now also owns telehealth BMI verification** | 2026-08-24 (re-dated by the republish) | https://3dlook.ai/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/ |

**Remaining P0 hub gaps:** Data, Privacy, Security & Regulatory FAQ (trust asset #2, not started as a published page — **now the last remaining P0 hub gap**) · Wellness Platforms hub (conditional on wellness apps becoming a priority ICP).

## How agents use this file

Before any new FitXpress article, `seo-planner` (Phase 0) and `context-pack-builder` (track=seo) **must locate the topic's row here** and carry these fields downstream:

- **Main hub topic** — the authority page this piece belongs under (every supporting article links up to it).
- **Cluster section** — the narrow slot inside the hub.
- **Intent** — TOFU / MOFU / BOFU / comparison(GEO) / listicle / objection-handling → sets depth and CTA.
- **Action Type** — the writing instruction (see legend). **This is a gate**, not a suggestion.
- **Execution Priority** — P0 (backbone, write/refresh first) · P1 (strong supporting) · P2 (conditional, validate demand or start as a hub section).
- **URL of already published articles** — refresh target, internal-link source, or cannibalization warning.
- **Recommendation** — the specific angle/decision for this row.
- **Cannibalization Guardrail** — hard boundary; a new page must not duplicate what already owns the intent.

**A title without its strategy row is not a brief.** If the topic is not in this plan, `seo-planner` stops and asks Vadim to place it (hub + cluster + action type) before proceeding.

## Action Type legend (treat as a writing instruction)

| Action Type | What the agent does |
|---|---|
| **Create net-new** | Write a new article — only if no existing page owns the intent. Check the published-URL column first. |
| **Refresh / expand existing** | **Do NOT draft new.** Improve the existing page (add sections, FAQs, internal links, current positioning). |
| **Section first** | Add the topic as a section inside the hub before any standalone page. Prevents cannibalizing the hub. |
| **Review / decide** | Do not auto-create. First decide: new article / hub section / product-page section / lead magnet / defer. |
| **Lead magnet / sales asset** | Write as a checklist/buyer guide. Do not publish as a thin SEO page unless expanded into a full guide. |
| **Publish planned hub** | The hub is drafted/planned — publish it; do not create a second broad overview. |

## Two cross-cluster trust assets (referenced by every vertical)

1. **Accuracy framework** — `mobile-body-scanning-accuracy` is the canonical source for accuracy framing. Never reduce accuracy to one universal number; always qualify by decision / reference method / capture protocol / population / workflow / tolerance.
2. **Data, Privacy, Security & Regulatory FAQ** (P0, planned) — canonical source for data storage, photo/3D-mesh/measurement retention, server geography, deletion, ownership, HIPAA/GDPR/CCPA/SOC 2/FDA. Vertical pages carry only short notes that link here. **Compliance claims require legal/product/security sign-off before publishing.**

---

## Hub 0 — AI Body Data for Health (Main Health hub)

Navigation hub only — gateway to all FitXpress verticals. Do NOT create another generic AI-in-healthcare article; do not compete with individual vertical hubs.

| Cluster | Article | Intent | Action | Pri | Notes / guardrail |
|---|---|---|---|---|---|
| Main Health hub | AI Body Data for Health, Fitness, Telehealth, Insurance, Occ. Health, Clinical Research | Hub | ✅ **PUBLISHED 2026-07-24** | P0 | **Live:** [`ai-body-data-health-hub`](https://3dlook.ai/content-hub/ai-body-data-health-hub/) — "AI Body Data Across Health Programs: A Guide to Verified Body Measurement" (updated 07-27). Navigation gateway only. Do not create a second generic AI-in-healthcare article. |
| Accuracy / buyer evaluation | How to Evaluate AI Body Scanning Accuracy in 2026 | MOFU/BOFU | ✅ **PUBLISHED 2026-07-03** | P0 | **Live:** [`mobile-body-scanning-accuracy`](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) — "Body Scanning Accuracy: A Framework for Enterprise Decisions" (updated 07-30). Keep as evaluation framework ("accurate enough for which decision?"), not a "3DLOOK is accurate" page. Do not duplicate the DEXA article. |
| Data / privacy / regulatory FAQ | Data, Privacy, Security & Regulatory FAQ | Objection / procurement / GEO | Net-new central FAQ | P0 | Canonical trust asset. Use FAQ schema. Link from all vertical hubs. Compliance answers need legal/security/product approval. |

## Hub 1 — AI in Fitness

**Hub is live (2026-07-31).** `ai-in-fitness-industry` was refreshed in place. Keep ONE AI-in-fitness hub — do not create a second broad overview. Separate fitness app/product strategy from wellness & GLP-1. Send BOFU traffic to FitXpress pages. P1/P2 cluster articles below are now unblocked.

| Cluster | Article | Intent | Action | Pri | Notes / guardrail |
|---|---|---|---|---|---|
| Main hub | AI in Fitness: Body Data, Progress Tracking, Personalization, Digital Coaching | Hub | ✅ **PUBLISHED 2026-07-31** | P0 | **Live:** [`ai-in-fitness-industry`](https://3dlook.ai/content-hub/ai-in-fitness-industry/) — refreshed in place from the Sep 2024 version. No second broad AI-in-fitness page. Open item: add the up-link to the Main Health hub (it was not live at publish time). |
| Digital coaching | Remote Body Measurement for Online Fitness Coaching Programs | MOFU/BOFU | Create net-new | P1 | Targets coaches/platform workflows, not generic apps. BOFU → `/fitxpress/for-connected-and-digital-fitness/`. |
| Comparison | Smart Scale vs AI Body Scan: What Fitness Apps Should Track | GEO/comparison | Create net-new | P1 | Consider one shared fitness/wellness comparison page vs two near-duplicates. |
| Privacy/trust | Privacy Considerations for AI Body Scanning in Fitness Apps | Objection | Create net-new | P1 | Practical (consent, image handling, retention), non-legal. |
| GLP-1 bridge | GLP-1 and Fitness Apps: Tracking Body Composition, Not Just Weight | Cross-cluster bridge | Create net-new | P1 | Bridge to `glp-1-market` / `visual-progress-tracking-glp1-...`. |
| Progress tracking | AI Fitness Progress Tracking: Why Weight Alone Is Not Enough | TOFU | Create net-new | P2 | Only if fitness-specific; else section in Fitness hub. |
| Body composition | Body Recomposition Tracking: Measuring Progress Beyond the Scale | TOFU/MOFU | Create net-new | P2 | Avoid duplicate body-comp basics; keep to recomposition/progress. |
| Fitness apps | AI Body Scanning for Fitness Apps | BOFU | Review / decide | P2 | Use existing FitXpress page as BOFU destination. |
| Product strategy | Why Progress Visibility Is a Retention Lever for Fitness Apps | MOFU | Create net-new | P2 | Better as a hub section first. |
| Implementation | How to Add AI Body Scanning to a Fitness App | BOFU | Create if validated | P2 | Product-page section first; consider combined fitness/wellness implementation guide. |
| Lead magnet | Fitness App Buyer's Checklist for AI Body Scanning Tools | Conversion | Lead magnet | P2 | Gated/ungated checklist; not a thin blog page. |

## Hub 2 — AI in Telehealth

**Hub is live (2026-08-07).** `the-potential-of-ai-in-telehealth` was refreshed in place at the same URL — do not create a second telehealth overview. Keep telehealth on remote-care workflows, privacy, documentation, patient experience. **Separate from GLP-1 eligibility and online-pharmacy BMI verification** unless the piece is explicitly the bridge. P1/P2 cluster articles below are now unblocked; new cluster pieces link up to this hub.

> **Boundary update 2026-08-24.** One exception to the "separate from online-pharmacy BMI verification" rule is now live and deliberate: `online-pharmacy-bmi-verification-a-2026-compliance-guide` was rewritten and republished in place with a **telehealth BMI verification section**, so that page — not this hub — owns telehealth remote BMI verification. Telehealth cluster pieces should link to it for BMI verification rather than re-explaining the workflow.

| Cluster | Article | Intent | Action | Pri | Notes / guardrail |
|---|---|---|---|---|---|
| Main hub | AI in Telehealth: Workflows, Privacy, Patient Experience, Remote Body Data | Hub | ✅ **PUBLISHED 2026-08-07** | P0 | **Live:** [`the-potential-of-ai-in-telehealth`](https://3dlook.ai/content-hub/the-potential-of-ai-in-telehealth/) — refreshed **in place** at the same URL from the Sep 2024 version. No competing page. |
| Patient experience | How Mobile Body Scanning Improves Patient Engagement | TOFU/MOFU | ✅ **PUBLISHED 2026-08-14** | P0 | **Live:** [`mobile-body-scanning-patient-engagement`](https://3dlook.ai/content-hub/mobile-body-scanning-patient-engagement/). Broader than GLP-1; don't cannibalize the GLP-1 visual-progress page. |
| BMI verification | What Is Telehealth BMI Verification / How to Verify BMI Remotely in Telehealth 2026 | BOFU | ✅ **DONE 2026-08-24 — shipped as a section, not a page** | P0 | **Live inside** [`online-pharmacy-bmi-verification-a-2026-compliance-guide`](https://3dlook.ai/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/) → section *"How to verify BMI remotely in a telehealth workflow"* (four sub-sections: when extra verification is needed · four remote methods · practical workflow · how FitXpress supports it). This is exactly the instruction this row carried. **Do not re-pitch and do not publish a standalone page** — the drafted standalone at `workspace/seo/articles/telehealth-bmi-verification-2026/` is frozen as SUPERSEDED. Reopen only if search data shows "telehealth BMI verification" demand materially separate from the pharmacy term. |
| Workflow | Remote Body Measurement Workflows for Telehealth Providers | MOFU | Create net-new | P1 | Operational, not trend-led. |
| GLP-1 bridge | Remote Body Data Tracking for GLP-1 Telehealth Programs | MOFU/BOFU | Create net-new | P1 | Focus longitudinal tracking, not eligibility verification. |
| Privacy | AI Body Scanning in Telehealth: Privacy, Consent, Data Governance Basics | Objection | Create net-new | P1 | Careful legal language. |
| Documentation | How AI Body Scanning Supports More Consistent Telehealth Documentation | BOFU | Create net-new | P1 | Anchored by Admin Panel (records/export/workflow). |
| Comparison | Progress Photos vs Structured Body Data in Virtual Weight-Loss Programs | GEO/comparison | Create net-new | P1 | About documentation quality & manipulation risk, not photo-bashing. |
| Telehealth | Top Telehealth Companies | Listicle | Create net-new | P1 | Vendor/category landscape; do not turn into a FitXpress product page. |
| Patient experience | Helping Telehealth Patients Understand Progress Beyond Weight | TOFU/MOFU | Create if validated | P2 | Hub section first. |
| Implementation | How to Add Remote Body Measurement to a Telehealth Platform | BOFU | Review / decide | P2 | Include product-page section. |
| Buyer guide | Telehealth Buyer's Checklist for AI Body Measurement Tools | Lead magnet | Lead magnet | P2 | Gated/downloadable. |
| Scale | How Telehealth Platforms Can Scale Patient Monitoring Without More Manual Work | Executive/BOFU | Refresh / expand | P2 | Expand `accuracy-drives-roi-digital-health`. |
| Weight-loss use case | AI Body Scanning for Telehealth Weight-Loss Programs | BOFU | Create net-new | P2 | Product page = BOFU destination. |

## Hub 3 — GLP-1 Market & Progress Tracking

**Hub is live (2026-08-28).** `glp-1-market` was refreshed in place at the same URL — do not create a second GLP-1 market overview. The hub owns market growth, delivery models (telehealth, in-person/hybrid clinic, pharmacy-led, employer-supported), and the progress-tracking gap as an industry-level problem. **Avoid duplicating** GLP-1 Market, Visual Progress Tracking, Beyond BMI, and Online-Pharmacy BMI Verification — each page owns a distinct intent. P1/P2 cluster articles below are now unblocked; new cluster pieces link up to this hub.

| Cluster | Article | Intent | Action | Pri | Notes / guardrail |
|---|---|---|---|---|---|
| Main hub | GLP-1 Market Growth and the Need for Better Patient Progress Tracking | Hub | ✅ **PUBLISHED 2026-08-28** | P0 | **Live:** [`glp-1-market`](https://3dlook.ai/content-hub/glp-1-market/). Refreshed in place — same URL, re-dated. Live text added a market-structure section (Novo/Lilly, oral + combination therapies) and a four-row market-indicator table; claims are hedged harder than the draft. Live text of record: `workspace/seo/articles/glp-1-market-hub/published-live-2026-08-28.md`. Does **not** own eligibility verification, diagnosis or dosing. |
| Tools / listicle | 7 Body Composition and Progress-Tracking Tools for Remote GLP-1 Clinics | MOFU/BOFU | ✅ **PUBLISHED 2026-08-21** | P0 | **Live:** [`top-7-remote-body-composition-tools-glp-1-clinics`](https://3dlook.ai/content-hub/top-7-remote-body-composition-tools-glp-1-clinics/). Published H1 dropped the "Top 7" ranking framing (slug kept). Answers "which tools should GLP-1 clinics evaluate?" FitXpress = remote structured-data layer, not universal replacement. |
| Remote monitoring | Remote Body Measurement for GLP-1 Programs: A Workflow for Virtual Clinics | BOFU | Create net-new | P1 | Focus repeated follow-up scans (vs BMI verification). |
| Documentation | What Body Data Should Be in a GLP-1 Patient Progress Record? | BOFU | Create net-new | P1 | Strong BOFU for clinics/platforms. |
| Baseline data | How Weight-Loss Clinics Can Standardize Baseline Body Data for GLP-1 Patients | BOFU | Create net-new | P1 | Keep distinct from bariatric pre-qualification. |
| Progress tracking | GLP-1 Progress Tracking: Why Weight Alone Does Not Tell the Full Story | TOFU/MOFU | Refresh / expand | P2 | Refresh `visual-progress-tracking-glp1-...`; don't duplicate. |
| Body composition | Body Composition Tracking for GLP-1 Patients: Metrics, Methods, Limits | MOFU | Create net-new | P2 | Only if GLP-1-specific; else add section to body-comp page. |
| Beyond BMI | Beyond BMI: Better Body-Data Signals for GLP-1 Weight-Loss Programs | TOFU/MOFU | Refresh / expand | P2 | Add GLP-1 section to `beyond-bmi-business`. |
| Clinic operations | How GLP-1 Clinics Can Scale Progress Tracking Without More In-Person Visits | BOFU | Create if validated | P2 | Section in ROI article or standalone. |
| Comparison | DEXA vs Mobile Body Scanning for GLP-1 Progress Tracking | GEO/comparison | Refresh / expand | P2 | Add GLP-1 subsection to `ai-body-scanners-vs-dexa-scans`. |
| Patient engagement | How Visual Progress Tracking Can Improve Engagement in GLP-1 Programs | MOFU | Refresh / expand | P2 | Already covered — refresh, don't create. |
| Lead magnet | GLP-1 Progress Tracking Checklist for Weight-Loss Clinics | Conversion | Lead magnet | P2 | Could embed inside GLP-1 progress article. |

## Hub 4 — Insurance Underwriting & BMI Verification

`online-pharmacy-bmi-verification` currently acts as the hub. **Rewritten and republished in place 2026-08-24** — same URL, now covering both pharmacy order-flow and telehealth remote BMI verification, and re-dated by WordPress to 2026-08-24 (the older 17.06.2026 / Jun 4 dates in the registers were the pre-rewrite publication and no longer appear on the page). Frame everything as **underwriting-support / BMI-build verification only**. Do NOT imply automated underwriting, fraud detection, or employment-screening decisions.

| Cluster | Article | Intent | Action | Pri | Notes / guardrail |
|---|---|---|---|---|---|
| Main hub | Mobile Body Data for Insurance Underwriting: BMI Verification, Risk Documentation, Applicant Experience | Hub | Refresh / expand | P0 | `mobile-body-scanning-insurance-underwriting` acts as hub. No second overview. |
| Documentation | How Insurers Can Create More Consistent Body Data Records for Underwriting Review | BOFU | Create net-new | P1 | If documentation/audit trail is a sales objection. |
| Fraud / misreporting | Self-Reported BMI vs Verified Body Data in Insurance Applications | GEO/comparison | Review / decide | P1 | Underwriter-support only; no automated fraud detection. |
| Privacy and consent | Privacy and Consent Considerations for Body Data in Insurance Workflows | Objection | Create net-new | P1 | Sensitive; link to central FAQ. |
| Insurance | Top Insurance Tech Companies | Listicle | Create net-new | P1 | Vendor/category landscape. |
| BMI verification | BMI Verification for Life Insurance: Why Self-Reported H/W Creates Risk | MOFU | Refresh / expand | P2 | Section inside insurance page, or narrow BOFU if life-insurance demand. |
| Underwriting workflow | How Mobile Body Scanning Can Support Accelerated Underwriting Workflows | BOFU | Refresh / expand | P2 | Expand workflow table; no duplicate. |
| Applicant experience | Reducing Friction in Life Insurance Applications With Remote Body Measurement | MOFU | Refresh / expand | P2 | Standalone if targeting digital distribution partners. |
| Human review | AI in Insurance Underwriting: Why Human Review Still Matters | Trust/compliance | Create if validated | P2 | Section first; standalone only as governance/trust. |
| Wellness-linked insurance | How Body Data Can Support Wellness-Linked Insurance Programs | Expansion | Refresh / expand | P2 | Refresh wellness-rewards page instead of duplicating. |
| Vendor evaluation | Questions Insurers Should Ask Before Using AI Body Measurement Tools | BOFU | Create net-new | P2 | Buyer-guide section or standalone checklist. |
| Lead magnet | Insurance Buyer's Checklist for Remote BMI Verification Tools | Conversion | Lead magnet | P2 | Downloadable checklist. |

## Hub 5 — Wellness Platforms

Wellness Rewards Verification = employer/insurer sub-hub; Beyond BMI = broad educational bridge. Create a separate Wellness Platforms hub only if wellness apps become a priority ICP. Keep claims **softer** — no clinical/clearance/diagnostic language.

| Cluster | Article | Intent | Action | Pri | Notes / guardrail |
|---|---|---|---|---|---|
| Main hub | AI Body Data for Wellness Platforms: Progress Tracking, Personalization, Engagement | Hub | Create net-new | P0 | Don't replace Wellness Rewards Verification; create full hub only if wellness apps are priority ICP. |
| Tools / listicle | Top Mobile Body Scanning Software for Wellness Apps | MOFU/BOFU | Net-new listicle | P0 | "What wellness apps should look for" angle, not "top software in general." |
| Personalization | How Body Data Can Personalize Wellness Programs | MOFU | Refresh / expand | P1 | Refresh `beyond-bmi-business`. |
| Preventive wellness | Using Body Measurements in Preventive Health and Wellness Programs | MOFU | Create net-new | P1 | Keep clinical claims soft. |
| Nutrition coaching | Body Data for Nutrition and Lifestyle Coaching Platforms | BOFU | Create net-new | P1 | The main nutrition/lifestyle coaching asset: structured measurements, body-composition indicators, visual progress, scan-to-scan tracking. **FitXpress does not generate meal plans, prescribe diets, or provide nutrition advice.** |
| Smart scale comparison | Smart Scale vs AI Body Scan for Wellness Tracking | GEO/comparison | Create net-new | P1 | Consider one shared smart-scale comparison page. |
| Privacy | Privacy Considerations for Body Data in Wellness Apps | Objection | Create net-new | P1 | Objection-handling FAQ. |
| Employee wellness / rewards | Top Employee Rewards Platforms | Listicle | Create net-new | P1 | Vendor landscape → link to wellness-rewards use case. |
| Progress tracking | Wellness Progress Tracking: Why Weight Alone Is Not Enough | TOFU | Review / decide | P2 | Add wellness section to Beyond BMI first. |
| User engagement | How Visual Progress Tracking Can Improve Wellness App Engagement | MOFU | Create net-new | P2 | Only if wellness-app specific. |
| Corporate wellness | Remote Body Measurement for Employee Wellness Programs | BOFU | Refresh / expand | P2 | Expand wellness-rewards page. |
| Product integration | How to Add Body Scanning to a Wellness App | BOFU | Review / decide | P2 | Combined implementation guide with fitness apps; avoid two near-identical how-tos. |
| Lead magnet | Wellness Platform Buyer's Checklist for AI Body Measurement Tools | Conversion | Lead magnet | P2 | Sales enablement, not thin SEO. |

## Hub 6 — Bariatrics

`bariatric-pre-qualification-mobile-3d-body-scanning` is the hub. Keep tied to obesity-care intake, pre-auth, pre-qualification, patient progress. Do NOT duplicate generic GLP-1 / telehealth / body-composition pages.

| Cluster | Article | Intent | Action | Pri | Notes / guardrail |
|---|---|---|---|---|---|
| Main hub | Bariatric Pre-Qualification and Patient Progress Tracking | Hub | Refresh / expand | P0 | Expand with pre-auth, patient progress, GLP-1 bridge, post-op. |
| Pre-qualification | Bariatric Pre-Qualification: Capture BMI Earlier and More Consistently | BOFU | Refresh / expand | P2 | Already covered — refresh, don't duplicate. |
| Pre-auth documentation | Bariatric Pre-Authorization Documentation: What Body Data Payers May Need | BOFU | Create net-new | P1 | Strong section or standalone for payer-doc keywords. |
| GLP-1 bridge | GLP-1 Before Bariatric Surgery: Why Body Composition & Progress Matter | MOFU | Create net-new | P1 | GLP-1 changes bariatric pathways. |
| Post-op progress | Tracking Body Changes After Bariatric Surgery Beyond Weight Loss | MOFU | Create net-new | P1 | Progress tracking, not medical advice. |
| Patient records | What Body Data Should Be in a Bariatric Patient Progress Record? | BOFU | Create net-new | P1 | Documentation workflows. |
| Hybrid care | Hybrid Bariatric Care: Virtual Check-Ins With Standardized Body Data | BOFU | Create net-new | P1 | Focus on hybrid-care model. |
| Remote intake | Remote Body Measurement for Bariatric Patient Intake | BOFU | Refresh / expand | P2 | Section first; standalone only if intake-workflow focused. |
| Body composition | Body Composition Tracking in Bariatric Care: Metrics, Methods, Limits | MOFU | Create net-new | P2 | Only if bariatric-specific. |
| Comparison | Manual Measurements vs AI Body Scanning for Bariatric Clinics | GEO/comparison | Review / decide | P2 | Keep bariatric-specific. |
| Lead magnet | Bariatric Documentation Checklist (BMI, Measurements, Progress) | Conversion | Lead magnet | P2 | Downloadable; link from hub + GLP-1. |

## Hub 7 — Clinical Trials (Hybrid & Decentralized Obesity Trials)

**Hub is live (2026-07-17).** Keep **trial-ops / protocol-workflow focused**. Do NOT blur into telehealth or bariatric care delivery; do NOT imply endpoint validation or replacement of protocol-defined reference methods. P1 supporting articles below are now unblocked — **four of them since the 2026-09-03 sync**, which also replaced this cluster's single shared guardrail with a per-row one. Read the row's own guardrail, not just this preamble.

| Cluster | Article | Intent | Action | Pri | Notes / guardrail |
|---|---|---|---|---|---|
| Main hub | Standardizing Anthropometric Measurements for Hybrid & Decentralized Obesity Trials | BOFU/use case | ✅ **PUBLISHED 2026-07-17** | P0 | **Live:** [`clinical-trial-anthropometric-measurement-software-obesity-trials`](https://3dlook.ai/content-hub/clinical-trial-anthropometric-measurement-software-obesity-trials/) (updated 07-27). Covers sponsors/CROs, site variability, coordinator burden, structured records, audit readiness, scope boundaries. |
| Comparison | Manual Tape Measurements vs Mobile Body Scanning in Clinical Trials | GEO/comparison/MOFU | Create net-new, narrower than originally planned | P1 | Trial-specific: workflow consistency, coordinator burden, protocol boundaries. Workflow comparison, **not** universal method replacement — do not imply scanning replaces all manual anthropometry or protocol-defined reference methods. |
| Vendor evaluation | What CROs Should Ask Before Using Remote Body Measurement Tools | BOFU/buyer evaluation | Create net-new supporting | P1 | Sales-enablement buyer guide, framed as a checklist/evaluation guide for vendor selection. Do not repeat the hub's "why trials need standardization" story. |
| DCT workflow | Remote Anthropometric Measurement Workflows for DCTs | BOFU | Create net-new | P2 | Major hub section first; standalone only if DCT-workflow demand. |
| Obesity trials | Body Measurement Standardization in Obesity & Metabolic Trials | BOFU | Create if validated | P2 | Hub SEO anchor; sponsor/CRO vocabulary. |
| Site consistency | Reducing Measurement Variability Across Multi-Site Trials | MOFU/BOFU | Section first; standalone only if validated | P2 | Site ops & monitoring, not generic measurement-variability content. If standalone, target clinical operations and monitoring teams specifically. |
| Hybrid trials | How Hybrid Trials Can Capture Body Measurements Between Site Visits | BOFU | Section first; standalone only if campaign focus | P2 | Between-visit capture only. Do not repeat the hub's site-based, DCT, audit or full-workflow material. |
| Patient experience | Reducing Participant Burden in Obesity Trials With Remote Check-Ins | MOFU | Create net-new if patient-centric DCT messaging matters | P2 | Owns participant burden. Do not repeat the full operational business case, and do not claim retention improvement as guaranteed — frame it as reducing workflow friction that may support retention. |
| Data quality | Anthropometric Data Quality in DCTs: Workflow, Capture, Documentation | MOFU | Create net-new | P2 | Avoid overclaiming validation / endpoint replacement. |
| Documentation | Audit-Ready Body Measurement Records for Hybrid Trials | BOFU | Section first; standalone only if validated | P2 | "Supports monitoring and audit readiness," never "guarantees compliance." |
| Integration | Adding Remote Body Measurement to a DCT Platform: API, Workflow, and Data Handoff Considerations | BOFU/implementation | Create net-new supporting | **P1** ⬆ | Targets API/SDK & data-handoff questions. Keep it technical/operational — not another general DCT measurement article. No commitments about integrations product has not confirmed. *(P2 → P1 in the 2026-09-03 sync.)* |
| Eligibility support | Remote BMI Pre-Checks in Obesity Trial Recruitment: What They Can and Cannot Do | MOFU/BOFU | Create net-new supporting | **P1** ⬆ | **High sensitivity.** Never say FitXpress determines eligibility. Use "supports pre-check," "provides input," "where protocol allows," "investigator-led determination." *(P2 → P1 in the 2026-09-03 sync.)* |
| Lead magnet | Clinical Trial Checklist for Remote Anthropometric Data Capture | Conversion/sales enablement | Lead magnet / downloadable checklist | P2 | Not a thin indexed post. PDF, gated or ungated checklist, or a CTA embedded inside the CRO buyer guide. |

## Hub 8 — Occupational Health Screening

**Hub is live (2026-07-10)** — the "publish the hub first" block on supporting articles is lifted; the P0/P1 supporting pieces below are unblocked. Keep every claim inside the **intake/documentation boundary** — never hiring, clearance, diagnosis, or fitness-for-duty decisioning.

| Cluster | Article | Intent | Action | Pri | Notes / guardrail |
|---|---|---|---|---|---|
| Main hub | Standardizing Occupational Health Screening: Faster Intake, Better Documentation, Fewer Rescreens | BOFU/use case | ✅ **PUBLISHED 2026-07-10** | P0 | **Live:** [`occupational-health-screening-software`](https://3dlook.ai/content-hub/occupational-health-screening-software/) (updated 07-17). Owns pre-employment/pre-placement/return-to-work intake, fit-for-duty documentation support, rescreens, multi-site, workforce screening vendors, workers'-comp. |
| Comparison | Manual Intake vs Digital Intake in Occupational Health Screening | GEO/comparison | Net-new supporting — **IN PROGRESS 2026-09-03** | P0 | Throughput, missing data, rescreens, multi-site consistency. No medical/clearance claims. Plan approved at checkpoint 1; working dir `workspace/seo/articles/2026-09-03-manual-vs-digital-intake-occupational-health/`. Sheet pencils it for September 2026. |
| Return-to-work | Return-to-Work Screening Documentation: How Digital Intake Reduces Delays | BOFU/workflow | Net-new supporting | P0 | Distinct buyer (workers'-comp/absence). Not "clears employees for duty." |
| Workers' comp / absence | Remote Intake for Workers' Compensation and Return-to-Work Documentation | BOFU | Net-new supporting | P1 | Workers'-comp/absence program ops; don't overlap return-to-work article. |
| Workforce screening vendors | Digital Intake Workflows for Workforce Screening Vendors | BOFU/vendor | Net-new supporting | P1 | Multi-employer programs; no medical-review/clearance claims. |
| Buyer guide / lead magnet | Occupational Health Buyer's Checklist for Digital Intake & Body Measurement Tools | Conversion | Lead magnet | P1 | PDF/embedded; not a thin post. |
| Compliance / trust | Fit-for-Duty Assessment Intake: What Digital Tools Can and Cannot Do | Objection/trust | Net-new / FAQ expansion | P2 | High sensitivity. No "automated fit-for-duty" / "clearance automation." Intake/documentation support only. |
| Rescreens / rework | What Causes Rescreens in Occupational Health Screening and How to Reduce Them | MOFU/BOFU | Section first | P2 | H2+FAQ in hub first; standalone only if demand validates. |
| Pre-employment screening | Pre-Employment Medical Screening Intake: Reduce Bottlenecks Before the Appointment | BOFU/workflow | Section first | P2 | Post-offer intake framing. No hiring-decision implication. |
| Multi-site consistency | How Occupational Health Providers Can Standardize Body Measurements Across Sites | BOFU | Section first | P2 | Clinic networks/providers (vs vendor article). |
