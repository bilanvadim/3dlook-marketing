# Context Pack — Telehealth Hub Refresh
product: fitxpress
track: seo
target_agents: seo-planner, seo-writer
objective: Refresh https://3dlook.ai/content-hub/the-potential-of-ai-in-telehealth/ into full "AI in Telehealth" hub page
created: 2026-07-27

## content_strategy
- hub: "AI in Telehealth: Workflows, Privacy, Patient Experience, and Remote Body Data Use Cases"
- cluster: Main hub
- intent: Hub
- action_type: "Refresh / expand hub"
- action_type_override: "proceed-full-pipeline (Vadim-approved 2026-07-27) — treat as equivalent to publish-planned-hub; do NOT gate/stop, run full pipeline"
- priority: P0
- existing_urls:
  - https://3dlook.ai/content-hub/the-potential-of-ai-in-telehealth/  (refresh target)
- cannibalization_guardrail: "Keep telehealth focused on remote-care workflows, privacy, documentation, and patient experience. Separate from GLP-1 eligibility and online pharmacy BMI verification."
- recommendation (verbatim from content-plan.csv): "Refresh this page into the hub. Add workflow, privacy, body-data, patient-experience, and FitXpress sections. Do not create a competing AI-in-telehealth page."
- vertical_boundary (content-strategy-guidelines.md §9, Telehealth): "Owns remote-care workflows, patient experience, documentation, privacy, and remote monitoring. Keep telehealth separate from GLP-1 eligibility and online pharmacy compliance unless the article is explicitly about the bridge."
- related_cluster_rows_in_same_hub (for context — do not absorb into this refresh, they are separate future articles): patient engagement (TOFU/MOFU), BMI verification bridge (P0, refresh Online Pharmacy article instead), workflow article (P1), GLP-1 bridge tracking (P1), privacy/consent article (P1), documentation/Admin Panel article (P1), progress-photos-vs-structured-data comparison (P1)

### internal_link_targets (4 directions, content-strategy-guidelines.md §11)
- **up (this IS the hub — link out to parent Main Health hub):** "AI Body Data for Health, Fitness, Telehealth, Insurance, Occupational Health, and Clinical Research" hub (net-new / not yet published — link if live, else omit)
- **sideways (related clusters, do NOT duplicate their intent):**
  - GLP-1 Market hub: https://3dlook.ai/content-hub/glp-1-market/
  - GLP-1 Compliance Challenge: https://3dlook.ai/content-hub/glp-1-compliance-challenge/
  - Online Pharmacy BMI Verification (2026 guide): https://3dlook.ai/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/ (link sideways only — do NOT re-explain BMI verification here, that page owns the intent)
  - Visual Progress Tracking for GLP-1 Adherence/Retention: https://3dlook.ai/content-hub/visual-progress-tracking-glp1-adherence-retention/
  - Two Photos → Structured Body Data: https://3dlook.ai/content-hub/3dlook-turns-two-photos-structured-body-data/
  - Accuracy Drives ROI in Digital Health: https://3dlook.ai/content-hub/accuracy-drives-roi-digital-health/
  - FitXpress Admin Panel launch: https://3dlook.ai/content-hub/fitxpress-admin-panel-launch/
- **down (BOFU product page):** https://3dlook.ai/fitxpress/for-telehealth-and-weight-loss/
- **trust assets (central, always link rather than re-explaining):**
  - Accuracy framework (canonical): https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/ ("Body Scanning Accuracy: A Framework for Enterprise Decisions")
  - Data, Privacy, Security & Regulatory FAQ — **not yet published** (P0, in planning). Until live, link to https://3dlook.ai/legal/ and keep any privacy section short/context-specific, not a full generic privacy explainer.

## approved_claims (source: brand-assets/product-info/proof-points.md)
| id | claim | number | note |
|----|-------|--------|------|
| FX-001 | Overall accuracy vs manual measurements | 96–97% | qualify per about-me.md — never a bare universal number |
| FX-002 | Typical error margin | 1.5–2.0 cm | same study |
| FX-003 | Scan-to-scan repeatability | < 1 cm (locked convention per about-me.md) | "95%+ consistency" also sourced but write as `< 1 cm` |
| FX-004 | Weight estimation error | ±3.5% average (Smart Scales, MAE 2.1 kg) | "software output, not a scale" |
| FX-005 | Time to results | Under 45 seconds | 2 photos (front + side) |
| FX-006 | Body measurements captured | 80+ | product spec |
| FX-007 | Body composition outputs | BMI, BMR, fat %, lean mass, fat mass, essential/beneficial fat | product spec |
| FX-008 | Training data | 9+ years, 150K+ photos, 30K+ 3D scans, 430K+ measurements | company deck |
| FX-009 | UK Meds (online pharmacy) | 7,500 scans/2025, BMI verification use case, 7-month customer | internal — **note: UK Meds/pharmacy claim belongs to the pharmacy vertical, use only as a brief cross-vertical mention, not a telehealth-hub centerpiece per cannibalization guardrail** |
| FX-010 | Yazen | 34,000 scans/2025, weight-loss management support | internal — usable as telehealth/GLP-1-adjacent proof point |
| FX-011 | Healthyr | Patient profile complement use case | internal, no scan number given |
| FX-012 | HIPAA | Maintained (US healthcare) | security commitment |
| FX-013 | GDPR | Principles followed (EU) | security commitment |
| FX-014 | Encryption | TLS in transit, AWS S3 SSE-S3 at rest (always on) | security commitment |
| FX-015 | Photo retention | Immediate delete OR within 30 days per client policy; auto-blur if retained | security commitment |
| FX-016 | Personal identifiers | None processed | security commitment |

**Flagged — NOT found in product-info, do not use without asking Vadim:** SOC 2 certification status (about-me.md says "where applicable" but proof-points.md doesn't confirm it as an active cert); FDA approval/clearance status (never claim — see banned claims); ISO 8559-1 benchmark (0.40 cm session-to-session) is sourced in about-me.md but not in proof-points.md — usable per about-me.md as benchmark #2, but keep the two benchmarks separate, never combined.

## banned_claims
- Diagnosing conditions / making treatment decisions
- Making eligibility, underwriting, hiring, or fitness-for-duty/clearance decisions
- Replacing clinicians, DEXA, BIA, calibrated scales, or protocol-defined reference methods
- Guaranteeing regulatory compliance ("makes you compliant" — instead "supports compliant workflows")
- Automatic fraud detection claims
- Acting as standalone medical authority / "medical device" framing (frame as data-privacy compliance instead: HIPAA/GDPR/SOC2, not FDA Class II/CE-MDR)
- "Most accurate scanning" / "best-in-class" without a specific benchmarked figure attached
- Any number not in the approved_claims table above
- Reserved words unless independence is provable: "independent," "validated," "third-party validated" (default to "internal validation," "benchmark participation")
- Bare ">X%" without qualifying decision/reference/protocol/population/tolerance (guardrail #4 + about-me.md accuracy framing)
- Naming competitors (Prism Labs, Bodygram, Size Stream) directly — compare by method/role, never by name
- **Vertical-boundary specific for this hub:** no GLP-1 eligibility-decisioning language, no online-pharmacy BMI-compliance claims (those live on the separate pharmacy page) — this hub covers remote-care workflow/documentation/privacy/patient experience only

## voice_fingerprint (about-me.md)
- The reframe move (signature): open by turning the obvious question into the sharper one — e.g. "How accurate is it?" → "Accurate enough for which decision?"
- Declarative, unhurried: 15–30 word sentences, 2–4 sentence paragraphs; occasional short verdict lines
- Concrete over abstract: every claim carries a number, named source, condition, or disclosed limit
- Honest about limits in the same breath as capability — not a bolted-on disclaimer
- Buyer framing, not "you"-spam ("enterprise teams," "care teams," "programs")
- Neutral authority: cite external bodies (CDC, Munich Re, Swiss Re, NAIC, LIMRA, ISO) rather than asserting our own credibility
- No jokes in published copy — sober, dry-but-serious

## claims_discipline (about-me.md)
- NEVER: diagnose, make treatment/underwriting/hiring/clearance decisions, replace clinician/DEXA/BIA/calibrated scale, guarantee compliance, auto-detect fraud, act as standalone medical authority
- POSITION AS: mobile body-scanning solution; structured body-data capture layer; remote intake and documentation layer; workflow-standardization tool; progress-tracking / scan-to-scan comparison layer; support for review, monitoring, documentation, operational efficiency
- "Supports clinician review" is the workhorse phrase — use often, honestly
- Not a medical device — compliance framed via data-privacy frameworks (HIPAA/GDPR/SOC 2), not medical-device frameworks (FDA Class II/CE-MDR)

## accuracy_framing (about-me.md)
- Never reduce accuracy to one universal number — qualify by decision/reference/protocol/population/tolerance
- Repeatability ≠ accuracy; repeatability is what matters for longitudinal telehealth use (progress checks) — write as `< 1 cm`
- Two benchmarks, never combined: (1) internal validation vs expert manual measurement (~96–97% accuracy, 1.5–2.0 cm typical error, <1cm repeatability); (2) ISO 8559-1:2017 multi-company benchmark (0.40 cm session-to-session)
- Always route accuracy discussion to the central accuracy framework article (link), per content-strategy §10

## icp_context / segment_hook / do_not_say (audience.md — Segment 1: Telehealth & Weight-Loss / GLP-1, applied narrowly to the non-GLP-1-eligibility slice)
- **buyer_persona:** Founder/CEO; Chief Medical Officer / Medical Director; Head of Clinical Operations; Head of Member Engagement/Retention; Head of Outcomes/Program Insights; Care Coordination Manager (icp-detail.md, $2M+ revenue orgs)
- **pain_points (workflow/documentation/patient-experience angle only, per vertical boundary — de-emphasize GLP-1-eligibility-specific pain):**
  - Manual intake and progress-photo workflows are high-friction and slow to scale as remote-care volume grows
  - Self-reported / manual data feels outdated next to competitors and is hard to verify
  - No standardized way to show body progress over time to patients or to payer/employer partners
  - Fragmented data (self-report + scale + photos) blocks clean longitudinal tracking and consistent documentation
- **segment_hook:** Make body progress visible → supports repeat check-ins → supports adherence/retention; repeatability (`< 1 cm`) means small real changes aren't lost in measurement noise; defensible, structured records for internal review and payer/employer reporting
- **do_not_say:** No diagnostic claims; not positioned as a DEXA or calibrated-scale replacement; no eligibility-decisioning language; keep separate from UK online-pharmacy BMI compliance unless the piece is explicitly framed as the bridge (it is not, here)
- **Gap flagged:** audience.md's segment 1 is written as a combined "Telehealth & GLP-1" layer — there is no audience.md segment isolated purely to "remote-care workflow / documentation / patient experience" without GLP-1 framing. Apply the shared spine + segment 1's hook/pain points but filter out GLP-1-prescription-specific language per the cannibalization guardrail. Recommend Vadim/Asselya confirm this filtering is sufficient, or consider a segment addendum in a future audience.md update.

## tone (about-me.md + content-strategy-guidelines.md §13)
- Clear, specific, useful for B2B buyers; avoid hype
- Operational verbs: supports, helps standardize, provides structured records, reduces manual intake, standardizes capture, supports review, improves documentation consistency, reduces rework, supports scan-to-scan comparison
- Standard 12-part article structure (about-me.md): buyer problem → short answer/definition → why now → workflow/use-case → where FitXpress fits → what improves operationally → what FitXpress does NOT do → comparison/decision framework → buyer/ICP fit → implementation considerations → FAQs (2–5 sentence, GEO/AEO-friendly) → CTA
- Telehealth is a **sensitive vertical** — include a clear scope note + italic disclaimer early
- CTA: this is a Hub page — use TOFU/MOFU soft-to-evaluation CTAs at top-of-page sections ("Explore how mobile body scanning works," "See how FitXpress supports remote progress tracking"), reserve direct BOFU CTA ("Book a FitXpress demo," "Explore FitXpress for telehealth and weight-loss") for the hub's closing/product-fit section

## style_guardrails
- **M1 (editorial-guardrails.md):** expand every abbreviation at first use, including terms that feel obvious — BMI (Body Mass Index), GLP-1 (glucagon-like peptide-1), API/SDK spelled out, HIPAA/GDPR spelled out on first use, DEXA (dual-energy X-ray absorptiometry) if referenced
- **M2:** prefer positive scoping over stacked/interrupted negation — one clear scope statement per sentence (e.g., "FitXpress supports remote intake and documentation; clinical review and treatment decisions remain with the care team" — not chained negatives)
- **Guardrail #1:** cut claims not directly backed by a figure/source; hedge with supports/may reduce/can help, not faster/reduces/eliminates
- **Guardrail #2:** one number, byte-identical everywhere in the piece (body, FAQ, disclaimer)
- **Guardrail #3:** "independent/validated/third-party" are reserved words — don't use unless provable
- **Guardrail #4:** no bare >X% — attach methodology or link to accuracy framework
- **Guardrail #6:** "not positioned as a medical device," never "does not apply"
- Banned words (CLAUDE.md §6): leverage, utilize, harness, robust, seamless, comprehensive, delve, navigate (metaphorical), tapestry, realm, unlock, unleash, game-changing, cutting-edge, revolutionary, disrupt
- Banned constructions: em-dash in "X — is not just Y" rhetorical form, "It's not just X, it's Y," triple parallelisms ("fast, reliable, scalable"), "Furthermore/Moreover/Additionally" sentence-openers, "In today's fast-paced world," "Are you struggling with...?," "It's no secret that..."

## competitors_context (competitors.md)
Prism Labs is the primary FitXpress competitor here — strongest in GLP-1/weight-loss body-composition tracking and insurance/population-health risk stratification, with deep clinical-setting relationships. Bodygram is fitness/wellness-trainer-focused with weaker enterprise/clinical workflow and compliance posture (no strong HIPAA narrative). Our differentiation for telehealth: workflow-layer positioning (audit logs, integration depth), enterprise-grade compliance (HIPAA/GDPR), and two-product breadth. Never name competitors directly in the article; compare by method/role only, and never lead with "most accurate scanning" (this is the long-term Apple/Google-primitive defense — see competitors.md).

## examples
- `brand-assets/past-articles/blog/clinical-trials-anthropometric-measurement.md` — best model for a regulated/sensitive-vertical scope note, "operational not clinical" framing, and disclaimer/FAQ structure (per CLAUDE.md §15 hard requirement #2). Check its `known_issues` frontmatter for M1/M2 slips NOT to replicate.
- `brand-assets/past-articles/blog/wellness-rewards-verification-employers-insurers-using-ai-3d-body-scanning.md` — telehealth/insurance-adjacent, health-vertical structure and CTA pattern reference (Assel Sekerova byline, demo CTA)
- `brand-assets/past-articles/blog/mobile-body-scanning-insurance-underwriting.md` — insurance-adjacent regulated-vertical scoping example
- `brand-assets/past-articles/blog/3dlook-turns-two-photos-structured-body-data.md` — core product-mechanics article, useful for the "where FitXpress fits" section's technical framing

## other required reads (not duplicated here, agents should still open)
- `brand-assets/style-guides/blog-style-guide.md` (full read required per CLAUDE.md §15 hard req #1)
- `about-me.md` and `audience.md` full text (this pack summarizes but does not replace them)
- Author: default to Assel Sekerova per CLAUDE.md §15 (no founder-voice trigger present for this hub refresh)

## Gaps flagged by context-pack-builder
1. No pure "telehealth workflow/documentation" audience segment exists in `audience.md` — segment 1 bundles telehealth with GLP-1; filtered its pain points/hook to the non-eligibility slice per the cannibalization guardrail. Recommend Vadim/Asselya confirm this filtering is adequate.
2. Central Data/Privacy/Security/Regulatory FAQ (P0 trust asset) is not yet published — link to `/legal/` as an interim trust link.
3. SOC 2 and FDA status are not confirmed in proof-points.md — flagged as do-not-use-without-asking.
