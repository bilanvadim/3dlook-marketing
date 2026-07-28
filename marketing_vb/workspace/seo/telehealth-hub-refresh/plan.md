---
slug: telehealth-hub-refresh
product: fitxpress
primary_keyword: AI in telehealth body data
primary_use_case: brand-assets/product-info/icp-detail.md (Segment 1 — Telehealth & Weight-Loss / GLP-1, filtered to the remote-care workflow / documentation / patient-experience slice)
hub: "AI in Telehealth: Workflows, Privacy, Patient Experience, and Remote Body Data Use Cases"
cluster: Main hub
intent: Hub (TOFU/MOFU top, one BOFU close)
action_type: refresh-expand-hub (Vadim override 2026-07-27 → run full pipeline, treat as publish-planned-hub)
priority: P0
status: draft
created: 2026-07-27
author: Assel Sekerova
refresh_target: https://3dlook.ai/content-hub/the-potential-of-ai-in-telehealth/
meta_description: "AI in telehealth is reshaping remote-care workflows, privacy, documentation, and patient experience. See where structured remote body data and FitXpress fit in." # 156 chars
---

# SEO Plan — telehealth-hub-refresh

## Content Strategy Fit (Phase 0)

> Run as documentation only. `action_type` in content-plan.csv = "Refresh / expand hub," which the standard Phase 0 gate would STOP-and-recommend. **Vadim override (context pack `action_type_override`, 2026-07-27):** proceed through the full pipeline, treat as equivalent to `publish-planned-hub`. No gate/stop. Phases 1–3 executed below.

- **Hub / cluster:** "AI in Telehealth: Workflows, Privacy, Patient Experience, and Remote Body Data Use Cases" → Main hub (this page IS the hub).
- **Action type:** refresh-expand-hub → full pipeline (override). We refresh the existing `/the-potential-of-ai-in-telehealth/` page in place into the hub. We do NOT create a competing AI-in-telehealth page (verbatim recommendation from content-plan.csv). Distinct angle vs the old page: the 2024 article is a generic AI-trends overview; the refresh adds the four owned pillars — remote-care workflows, privacy/documentation, patient experience, and a structured remote-body-data (FitXpress) layer — and re-frames the whole page around operational (not clinical) use.
- **Existing pages:**
  - `https://3dlook.ai/content-hub/the-potential-of-ai-in-telehealth/` → **refresh target** (edit in place, keep URL). Reuse its industry stats (H2.2) and use-case examples (H2.3); strip 2024 tone, add operational/boundary framing.
- **Cannibalization guardrail (verbatim):** "Keep telehealth focused on remote-care workflows, privacy, documentation, and patient experience. Separate from GLP-1 eligibility and online pharmacy BMI verification." **How we comply:** no BMI-verification explainer here (Online Pharmacy 2026 guide owns that intent — sideways link only, H2.8); no GLP-1 eligibility-decisioning language (GLP-1 hubs own that — sideways link only); UK Meds/pharmacy proof point (FX-009) used only as a one-line cross-vertical mention, never a centerpiece; Yazen (FX-010) used as the telehealth/weight-loss-adjacent proof point.
- **Vertical boundary (§9 Telehealth):** OWNS remote-care workflows, patient experience, documentation, privacy, remote monitoring. Does NOT own — and must not assert — diagnosis, treatment/eligibility/underwriting/clearance decisioning, replacement of clinicians/DEXA/BIA/calibrated scales, guaranteed compliance, automatic fraud detection, or medical-device framing. This boundary runs through every H2, and is stated explicitly as a scope note in H2.1 + a dedicated "What FitXpress Does NOT Do" subsection in H2.7.
- **Internal links planned (4 directions, §11):**
  - **up** → parent Main Health hub ("AI Body Data for Health, Fitness, Telehealth, Insurance, Occupational Health, and Clinical Research") — link only if live; else omit.
  - **sideways** → GLP-1 Market hub; GLP-1 Compliance Challenge; Online Pharmacy BMI Verification 2026 guide (link only, do not re-explain); Visual Progress Tracking for GLP-1 Adherence/Retention; Two Photos → Structured Body Data; Accuracy Drives ROI in Digital Health; FitXpress Admin Panel launch.
  - **down (BOFU)** → `https://3dlook.ai/fitxpress/for-telehealth-and-weight-loss/`.
  - **trust** → Accuracy framework (`/content-hub/mobile-body-scanning-accuracy/`); Data/Privacy/Security/Regulatory FAQ not yet live → interim link to `/legal/`, keep privacy section short/context-specific.

---

## Keyword Analysis (Phase 1)

### Primary cluster — AI in telehealth body data workflows
- **Primary keyword:** AI in telehealth body data
- **Search intent:** Informational / hub (TOFU-MOFU). Buyers researching how AI and remote body data fit into telehealth operations before shortlisting a vendor.
- **Volume / difficulty:** not supplied in context pack — leave for meta-generator to backfill from Ahrefs/SEMrush; treat as head-term hub with long-tail capture across the secondary clusters.

### Secondary clusters
| Cluster | Keywords (weave naturally) | Intent | Volume |
|---------|----------------------------|--------|--------|
| Remote body measurement in telehealth | remote body measurement telehealth, remote body scanning telehealth, mobile body scanning telehealth | Informational / commercial | TBD |
| Telehealth patient experience | telehealth patient experience, remote care patient engagement, virtual care progress tracking | Informational | TBD |
| AI body scanning privacy | AI body scanning privacy, telehealth data privacy HIPAA, body scan data governance | Informational / commercial | TBD |
| Telehealth documentation AI | telehealth documentation AI, structured remote records, AI clinical documentation support | Informational | TBD |
| AI telehealth use cases (from old page) | AI in telehealth use cases, AI telehealth workflow, remote patient monitoring AI | Informational (TOFU) | TBD |

- **Primary keyword placement:** in H1, meta description, first 100 words of H2.1 preamble, H2.2 opener, and one FAQ answer.
- **Secondary keyword placement:** one cluster mapped per H2 (see "Keywords to weave" in each block below) so no single section keyword-stuffs.

---

## Recommended Title (Phase 2)

**H1 (FIXED per brief — recommended):**
> AI in Telehealth: Workflows, Privacy, Patient Experience, and Remote Body Data Use Cases

**Why this title is correct (for the record):** It signals a hub, not a single article — the four-noun list ("Workflows, Privacy, Patient Experience, Remote Body Data") maps one-to-one onto the four owned pillars from the vertical boundary and tells procurement researchers the page covers scope, not a single narrow answer. The primary keyword theme ("AI in Telehealth" + "Remote Body Data") sits in the first three and last four words. It stays inside the boundary (no "diagnosis," "eligibility," or "BMI verification" in the title, which would collide with the GLP-1 and pharmacy pages). It matches the 2026 measured, operational tone rather than the old "The Potential of AI in Telehealth" trend framing.

### Other options (not chosen — documented)
1. "AI in Telehealth: A Hub for Remote-Care Workflows, Privacy, and Body Data" — tighter, but drops "patient experience" (a named owned pillar) and reads slightly more generic.
2. "AI and Remote Body Data in Telehealth: Workflows, Privacy, and Patient Experience" — leads with body data, which over-narrows a hub that must also cover non-FitXpress AI use cases in H2.3; risks looking like a product page.
3. "The AI in Telehealth Hub: Use Cases, Workflows, Privacy, and Documentation" — clear hub signal but "Documentation" is less searched than "Patient Experience," and it buries the remote-body-data differentiator.

---

## Article Outline (Phase 3)

Follows about-me.md 12-part structure, compressed into 11 hub H2s: buyer problem/scope (H2.1) → why now (H2.2) → use-case landscape (H2.3) → where FitXpress fits (H2.4) → workflow/what improves (H2.5) → privacy/documentation (H2.6) → what FitXpress does NOT do + challenges (H2.7) → cross-cluster navigation/decision routing (H2.8) → future outlook (H2.9) → FAQs (H2.10) → CTA + disclaimer (H2.11).

Sensitive-vertical rule: **scope note + italic disclaimer placed early**, inside H2.1.

### H2.1 — What This Hub Covers (and Who It's For)
- **Goal:** Reader immediately understands this is the telehealth hub, its four pillars, who it serves (care teams, clinical ops, member-engagement leads at $2M+ remote-care orgs), and the operational-not-clinical scope. Sets the reframe: not "can AI diagnose?" but "where does AI, and structured remote body data, fit into a remote-care workflow?"
- **Word count target:** 200
- **Must-cover:** (1) one-sentence definition of the hub scope; (2) the four pillars named (workflows, privacy, patient experience, remote body data); (3) who it's for (buyer personas); (4) **early scope note + italic disclaimer** — FitXpress is a mobile body-scanning / structured-data-capture layer that supports clinician review; it does not diagnose or make treatment decisions and is not positioned as a medical device; (5) primary keyword in first 100 words.
- **Keywords to weave:** AI in telehealth body data; AI in telehealth use cases.
- **Sources:** none (original framing). Model the scope-note voice on `clinical-trials-anthropometric-measurement.md`.
- **Approved claims:** none (framing only).
- **Boundary:** state the boundary up front — operational layer, supports clinician review, not a medical device, no diagnosis/eligibility/decisioning. This is the master scope note the rest of the hub inherits.

### H2.2 — Why AI in Telehealth Matters Now
- **Goal:** Establish the "why now" with industry data reused from the existing article, reframed operationally (adoption + burden pressure → demand for standardized remote workflows and structured data), not as hype.
- **Word count target:** 400
- **Must-cover:** (1) 75% of healthcare orgs using AI report improved ability to treat disease; (2) 80% report reduced staff burnout; (3) telemedicine market ~$79.93B (2023) → ~$290.90B by 2032; (4) 97%+ telehealth adoption during COVID-19; (5) physical exam ~11% vs patient history ~76% of the diagnostic process → framing: remote care already leans on structured non-exam data, which is where a remote body-data layer fits. **Verify each is cited as a generic industry stat, not a 3DLOOK proprietary claim** — attribute generically ("industry surveys," "market analyses"), no invented sources, no bare >X% tied to a FitXpress decision.
- **Keywords to weave:** AI in telehealth body data; AI telehealth workflow; remote patient monitoring AI.
- **Sources:** existing-article.md (stats reuse — do not refetch web). Meta-generator/writer should attach the original stat attributions if available; otherwise phrase as "industry surveys indicate" per Guardrail #1.
- **Approved claims:** none of FX-001–016 here (these are industry stats, kept explicitly separate from FitXpress numbers per Guardrail #2).
- **Boundary:** these are industry-wide figures; do not let any of them read as a FitXpress performance or outcome claim. No "AI improves X by Y%" attributed to FitXpress.

### H2.3 — AI Use Cases Reshaping Telehealth
- **Goal:** Give the neutral landscape of where AI shows up in telehealth today, condensed from the old article into 6 categories, with consistent boundary language that these tools support workflows and augment clinicians rather than replace clinical judgment.
- **Word count target:** 450
- **Must-cover:** 6 categories, each with a one-line named example from the old page: (1) Remote patient monitoring — KardiaMobile / AliveCor; (2) Virtual health assistants & triage chatbots — Ada Health; (3) AI-assisted diagnostics (radiology/imaging support) — Viz.ai, Aidoc; (4) Personalized care insights — Merative; (5) Behavioral & mental-health support — Woebot; (6) Administrative & documentation automation — Augmedix; plus Resmed under monitoring/predictive. Each category one short paragraph. Do NOT position FitXpress inside these — FitXpress gets its own section (H2.4).
- **Keywords to weave:** AI in telehealth use cases; remote patient monitoring AI; AI clinical documentation support.
- **Sources:** existing-article.md (use-case examples reuse). No web refetch. Named third-party companies described factually as market examples only — no endorsement, no comparison to FitXpress.
- **Approved claims:** none.
- **Boundary:** every category carries "supports/augments the care team; clinical judgment stays with clinicians." No diagnostic-authority language for any tool. Do not imply FitXpress performs diagnostics, imaging, or triage.

### H2.4 — Remote Body Data as a Structured Capture Layer
- **Goal:** Introduce FitXpress positioning: mobile body scanning from two smartphone photos as a structured remote-body-data capture layer that drops clean, comparable metrics into the patient record. First place FitXpress is described in depth.
- **Word count target:** 400
- **Must-cover:** (1) two photos (front + side) → results in under 45 seconds (FX-005); (2) 80+ body measurements (FX-006); (3) body-composition outputs — BMI (Body Mass Index), BMR (basal metabolic rate), fat %, lean mass, fat mass, essential/beneficial fat (FX-007); (4) framing as a structured-data-capture / remote-intake layer, not a diagnostic or scale-replacement tool; (5) route ALL accuracy discussion to the accuracy-framework article (link) rather than restating numbers — if repeatability is mentioned, write `< 1 cm` and frame it as why longitudinal progress checks are meaningful.
- **Keywords to weave:** remote body measurement telehealth; mobile body scanning telehealth; AI in telehealth body data.
- **Sources:** existing-article.md (FitXpress paragraph), `3dlook-turns-two-photos-structured-body-data.md` (mechanics framing), accuracy-framework URL (link out, don't restate).
- **Approved claims:** FX-005 (under 45 seconds), FX-006 (80+ measurements), FX-007 (composition outputs). FX-003 (`< 1 cm` repeatability) only if repeatability is raised, and route detail to accuracy framework. Expand BMI/BMR/DEXA at first use (M1).
- **Boundary:** structured-data-capture layer that supports clinician review; not a diagnosis, not a DEXA (dual-energy X-ray absorptiometry) or calibrated-scale replacement; no bare accuracy number (Guardrail #4 — link to framework). Weight output is "software output, not a scale" if FX-004 is touched.

### H2.5 — Remote Care Workflows and Patient Experience
- **Goal:** Show the concrete 6-step remote-care workflow the body-data layer plugs into, and the patient-experience friction it reduces — the operational core of the hub.
- **Word count target:** 450
- **Must-cover:** (1) 6-step workflow — intake → processing → structured data delivery → provider review → documentation → follow-up; (2) patient-friction reduction — no clinic visit required for a measurement, visual/3D progress the patient can see, structured remote check-ins; (3) tie to segment hook — visible body progress supports repeat check-ins, which supports adherence/retention; (4) `< 1 cm` repeatability framing so small real changes are not lost in measurement noise (route accuracy detail to framework); (5) Yazen (FX-010) as the telehealth/weight-loss-adjacent proof point; one-line UK Meds (FX-009) cross-vertical mention only.
- **Keywords to weave:** telehealth patient experience; remote care patient engagement; virtual care progress tracking; AI telehealth workflow.
- **Sources:** existing-article.md; `wellness-rewards-verification...` (CTA/structure); Yazen/UK Meds from approved_claims table only.
- **Approved claims:** FX-010 (Yazen 34,000 scans/2025), FX-009 (UK Meds 7,500 scans/2025 — one-line mention only), FX-003 (`< 1 cm`), FX-005/FX-006 (brief callback allowed).
- **Boundary:** "provider review" and "documentation" are the human steps — the layer supports them, it does not auto-decide, auto-triage, or auto-flag fraud. No eligibility/GLP-1-prescription language (keep on the GLP-1 pages). UK Meds stays a mention, not a centerpiece (cannibalization guardrail).

### H2.6 — Privacy, Documentation, and Data Governance
- **Goal:** Address the procurement-critical privacy/documentation questions with a short, context-specific treatment (not a generic privacy explainer), framed via data-privacy frameworks.
- **Word count target:** 400
- **Must-cover:** (1) HIPAA (Health Insurance Portability and Accountability Act) maintained for US healthcare (FX-012); GDPR (General Data Protection Regulation) principles followed for EU (FX-013); (2) photo handling — immediate delete or within 30 days per client policy, auto-blur if retained (FX-015); no personal identifiers processed (FX-016); (3) encryption — TLS in transit, AWS S3 SSE-S3 at rest (FX-014); (4) documentation value — structured, comparable records support consistent internal review and payer/employer reporting; (5) keep it short and link to `/legal/` (interim) and, when live, the central Data/Privacy/Security/Regulatory FAQ — this is a trust link, not a full explainer.
- **Keywords to weave:** AI body scanning privacy; telehealth data privacy HIPAA; body scan data governance; structured remote records; telehealth documentation AI.
- **Sources:** approved_claims (FX-012–016), `/legal/` (interim trust link), accuracy-framework/privacy-FAQ URLs.
- **Approved claims:** FX-012, FX-013, FX-014, FX-015, FX-016. Expand HIPAA/GDPR at first use (M1).
- **Boundary:** compliance framed as data-privacy (HIPAA/GDPR/SOC 2 where applicable), NOT medical-device (no FDA Class II / CE-MDR). Say "supports compliant workflows," never "makes you compliant" (Guardrail #6 / banned claims). Do NOT assert SOC 2 or FDA status — both flagged do-not-use without Vadim. Positive scoping, one clear statement per sentence (M2).

### H2.7 — Challenges and Guardrails (including What FitXpress Does NOT Do)
- **Goal:** Keep the old article's honest challenges list, then add an explicit boundary subsection so the hub is self-limiting — the strongest trust signal on the page.
- **Word count target:** 400
- **Must-cover:** (1) four challenges reframed operationally — model bias (data-driven), privacy/security, regulatory complexity, staff/technology readiness; (2) **"What FitXpress Does NOT Do" subsection** built from banned_claims: does not diagnose or make treatment decisions; does not make eligibility/underwriting/hiring/clearance decisions; does not replace clinicians, DEXA, BIA (bioelectrical impedance analysis), calibrated scales, or protocol-defined reference methods; does not guarantee regulatory compliance; does not perform automatic fraud detection; is not a standalone medical authority / medical device; (3) frame the boundary as design intent, not a caveat.
- **Keywords to weave:** AI body scanning privacy; AI in telehealth body data (light).
- **Sources:** existing-article.md (challenges), banned_claims list (context pack).
- **Approved claims:** none (this is the negative-space section).
- **Boundary:** THIS is the boundary section — enumerate the full banned-claims list as positive scope statements (M2). Do not name competitors while discussing method limits (compare by method/role only).

### H2.8 — Explore the Telehealth Cluster (Cross-Cluster Navigation)
- **Goal:** Route readers to the six supporting Telehealth-cluster articles and to related sideways/down/trust destinations — the hub's link-equity distribution and intent-routing section.
- **Word count target:** 250
- **Must-cover:** (1) one-line description + link for each of the 6 supporting cluster articles: How Mobile Body Scanning Improves Patient Engagement; What Is Telehealth BMI Verification in 2026; Remote Body Measurement Workflows for Telehealth Providers; AI Body Scanning in Telehealth: Privacy, Consent, and Data Governance Basics; How AI Body Scanning Supports More Consistent Telehealth Documentation; Progress Photos vs Structured Body Data in Virtual Weight-Loss Programs (describe as the cluster's supporting articles; live URLs not required yet); (2) sideways links to related hubs/clusters (GLP-1 Market, GLP-1 Compliance Challenge, Online Pharmacy BMI Verification 2026, Visual Progress Tracking GLP-1, Two Photos → Structured Body Data, Accuracy Drives ROI, Admin Panel launch); (3) trust links (accuracy framework, `/legal/`); (4) down link to the FitXpress for Telehealth & Weight-Loss product page.
- **Keywords to weave:** remote body measurement telehealth; telehealth documentation AI; telehealth patient experience.
- **Sources:** internal_link_targets (context pack §internal_link_targets); brief's supporting-articles list.
- **Approved claims:** none.
- **Boundary:** for the "BMI Verification 2026" and GLP-1 links, use a one-line routing description only — do NOT re-explain BMI verification or GLP-1 eligibility here (those pages own that intent — cannibalization guardrail).

### H2.9 — Future Outlook
- **Goal:** Keep the old article's forward-looking angles but bound them: these directions stay clinician-reviewed, not autonomous.
- **Word count target:** 300
- **Must-cover:** (1) personalized medicine / personalized care insights; (2) predictive analytics with remote monitoring; (3) more capable virtual health assistants; (4) explicit boundary framing — these remain decision-support that a clinician reviews, not autonomous decision-makers; structured longitudinal body data becomes more useful as programs mature.
- **Keywords to weave:** AI in telehealth body data; remote patient monitoring AI.
- **Sources:** existing-article.md (future section).
- **Approved claims:** none.
- **Boundary:** no predictions that imply autonomous diagnosis/decisioning or that FitXpress will move into diagnostic/decisioning territory. Hedge with "may," "can support," "is expected to" (Guardrail #1).

### H2.10 — Frequently Asked Questions
- **Goal:** GEO/AEO-friendly answers (2–5 sentences each) to real procurement/search questions, each self-contained.
- **Word count target:** 450
- **Must-cover (7 questions):**
  1. What is AI in telehealth? (define generically, operational framing)
  2. How does mobile body scanning fit into a telehealth workflow? (map to the 6-step workflow from H2.5)
  3. Can AI body scanning replace DEXA or in-clinic assessments? (No — supports clinician review; not a reference-method replacement)
  4. What body data does FitXpress capture? (80+ measurements FX-006; BMI/BMR/fat %/lean mass/fat mass FX-007; under 45s FX-005)
  5. Is FitXpress HIPAA compliant? (HIPAA maintained FX-012; GDPR principles FX-013; encryption FX-014; photo handling FX-015; "supports compliant workflows," not "makes you compliant")
  6. Does FitXpress make clinical decisions? (No — structured-data-capture layer; clinical decisions stay with the care team)
  7. What kinds of telehealth programs use mobile body scanning? (remote weight-loss/metabolic, longitudinal monitoring, member-engagement programs; Yazen FX-010 as example)
  8. How is this different from self-reported weight and BMI? (structured, repeatable `< 1 cm` capture vs unverifiable self-report; route accuracy to framework)
- **Keywords to weave:** all secondary clusters, one per answer where natural.
- **Sources:** approved_claims table; existing-article.md; accuracy framework (link).
- **Approved claims:** FX-005, FX-006, FX-007, FX-010, FX-012, FX-013, FX-014, FX-015, FX-016, FX-003 (`< 1 cm`). Numbers byte-identical to body (Guardrail #2).
- **Boundary:** Q3 and Q6 are explicit boundary answers — keep them unambiguous and positive-scoped (M2). No SOC 2 / FDA assertions in Q5.

### H2.11 — Next Steps, CTA, and Disclaimer
- **Goal:** Close with an intent-appropriate CTA pair and the standard disclaimer.
- **Word count target:** 200
- **Must-cover:** (1) soft MOFU evaluation CTA (e.g., "See how FitXpress supports remote progress tracking," "Explore how mobile body scanning works" → accuracy framework / Two Photos article); (2) ONE direct BOFU CTA to the FitXpress for Telehealth & Weight-Loss product page ("Explore FitXpress for telehealth and weight-loss" / "Book a FitXpress demo"); (3) standard italic disclaimer — FitXpress is a mobile body-scanning and structured-data-capture solution that supports clinician review; it is not a medical device and does not diagnose, treat, or make clinical, eligibility, or coverage decisions.
- **Keywords to weave:** AI in telehealth body data (closing mention).
- **Sources:** internal_link_targets (down = product page; trust = accuracy framework).
- **Approved claims:** none new; disclaimer language per claims_discipline.
- **Boundary:** exactly one BOFU CTA (don't force demo CTAs throughout the hub); disclaimer wording matches H2.1 scope note and the "not positioned as a medical device" phrasing (Guardrail #6).

---

## Article meta
- **Estimated words:** ~2,900–3,100 (target band 2,500–3,500). Section targets sum: 200+400+450+400+450+400+400+250+300+450+200 = 3,900 ceiling; writer trims toward ~3,000.
- **Estimated read time:** ~13–15 min.
- **CTA placement:** soft evaluation CTAs after H2.4 and H2.5 (top/mid); single direct BOFU CTA in H2.11 (close). No mid-hub demo spam.
- **Internal links:** up → Main Health hub (if live); sideways → 7 related cluster/hub URLs (§internal_link_targets); down → `/fitxpress/for-telehealth-and-weight-loss/`; trust → `/content-hub/mobile-body-scanning-accuracy/` + `/legal/` (interim). Cross-cluster (H2.8) → 6 supporting Telehealth-cluster articles.
- **Author:** Assel Sekerova (no founder-voice trigger).
- **Disclaimer:** standard "not a medical device / does not diagnose or make decisions" — early scope note (H2.1) + closing disclaimer (H2.11).

## Flags for writer / Vadim
1. **Numbers-quarantine:** H2.2 industry stats (75% / 80% / $79.93B→$290.90B / 97% / 11% vs 76%) must be attributed generically as industry data and kept visually separate from FitXpress FX-numbers (Guardrail #2). No stat may read as a FitXpress outcome.
2. **Do-not-use:** SOC 2 and FDA status not confirmed in proof-points.md — do not assert in H2.6/H2.10 without Vadim.
3. **Audience gap:** no pure telehealth-workflow segment in audience.md; segment 1 filtered to the non-GLP-1 slice per guardrail — Vadim/Asselya to confirm filtering is adequate.
4. **Privacy FAQ not live:** H2.6/H2.8 link `/legal/` as interim; swap to central Data/Privacy/Security/Regulatory FAQ when published.
5. **Up-link conditional:** Main Health hub may not be live — omit the up-link if so.
