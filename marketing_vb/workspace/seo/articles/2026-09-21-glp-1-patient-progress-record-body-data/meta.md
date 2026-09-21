---
meta_title: "GLP-1 Patient Progress Record: What Body Data to Include"
meta_description: "A GLP-1 patient progress record stays readable only when every entry carries the same fields. See which ones belong, and why each earns its place."
url_slug: glp-1-patient-progress-record-body-data
category: GLP-1 & Weight Loss Programs
---

## Judgment checklist

- [x] intro_hook: First two sentences open on a concrete month-four file with mismatched entries (a weight and a coach's note, then a weight plus a waist measurement plus two photos), not an abstract claim, so the fragmentation problem is visible before the article names it.
- [x] cta_type: Single BOFU direct CTA in Section 10, "talk to 3DLOOK about the GLP-1 progress record workflow" linked to the pricing modal, plus the down-link product page in Section 5. Matches plan's CTA placement exactly, no mid-article CTA.
- [x] anchors_sources: All 9 links are descriptive, sense-bearing anchors ("GLP-1 market overview", "mobile body scanning accuracy framework", "FitXpress Admin Panel launch post", etc.) into 3dlook.ai content-hub or product pages. No external sources anywhere, matching the plan's link list; nothing to vet for vendor-blog quality.
- [x] cannibalization: glp-1-market used as up-link only, no growth/market repeated; BMI-verification linked once in FAQ 3, workflow not re-explained; tools listicle in related reading only, no comparison table; baseline standardization gets exactly one passing sentence at the end of Section 3 ("standardizing that first capture is its own piece of work") and is not developed into a section. One known overlap remains: the "what happens when a patient cannot complete a scan" FAQ question is shared with the same-day Hub 2 sibling, kept deliberately per plan-audit §4 and flagged below rather than silently duplicated.
- [x] distinct_intent: Owns record composition, which fields a GLP-1 entry carries and why, at what cadence they stay comparable. Distinct from market growth (glp-1-market), buyer tool comparison (tools listicle), BMI/eligibility workflow (online-pharmacy guide), baseline definition (unwritten sister row), and general telehealth record consistency (same-day Hub 2 sibling).
- [x] vertical_boundary: Scope note runs early (end of Section 1, italic), "What FitXpress does not do" restates it at claim level (Section 6), and "FitXpress is not a medical device." appears verbatim. No dosing, prescribing, or medication-effectiveness content anywhere; grepped for drug names and dosing-schedule language, zero hits. Eligibility and reference-method questions are answered once each in FAQ 3/FAQ 4 only, never in the body.

## Meta variants

### Title
1. GLP-1 Patient Progress Record: What Body Data to Include (56 chars) — recommended
2. What Belongs in a GLP-1 Patient Progress Record (47 chars)
3. GLP-1 Patient Progress Record Fields, Explained (47 chars)

### Description
1. A GLP-1 patient progress record stays readable only when every entry carries the same fields. See which ones belong, and why each earns its place. (146 chars) — recommended
2. Every entry in a GLP-1 patient progress record needs the same fields: what is submitted, what the scan generates, and what the capture logs. (140 chars)
3. A GLP-1 patient progress record needs the same fields in every entry, submitted, generated, and capture-condition data. See what belongs, and why. (146 chars)

## Open items

- **Zero measured search demand, by design.** No data for the exact phrase or close variants (`seed_has_data: false`); the one measured adjacent pocket ("glp-1 monitoring", 10-60/mo) is bloodwork/dosage intent and stays confined to FAQ 1. Judge this page on sales use, assisted conversions and AI-answer citations, not sessions (plan-audit open item 1).
- **Known M1 title case.** `article_lint.py` flags "GLP-1" unexpanded in the H1 (gate 8) because the abbreviation sits before any prose can spell it out. This is the same shape accepted on the live GLP-1 articles, precedent from 2026-09-19; the term is expanded at first prose use in Section 1 ("glucagon-like peptide-1 (GLP-1)"), and the title does not change to satisfy the regex. Counts as the article's one non-compliance checklist item below, not a STOP trigger on its own.
- **Written ahead of its October pencil.** Row priority is P1, pencilled for October 2026; it shipped in September so the Hub 3 documentation anchor is live alongside the same-day Hub 2 sibling. Flag if the October slot matters for reporting (plan-audit open item 2).
- **Baseline sister row still unwritten.** "How Weight-Loss Clinics Can Standardize Baseline Body Data for GLP-1 Patients" (P1, separately pencilled) is this article's natural cross-link once it exists; nothing to link to yet (plan-audit open item 3).
- **One shared FAQ question with the Hub 2 sibling** ("what happens when a patient cannot complete a scan"). Kept deliberately in both, per plan-audit open item 4, because the approved limitation is genuinely relevant on both pages and the wording is not identical between them. Flagging in case a single canonical answer is preferred later.
- **Second in-text visual is optional.** Plan leaves the "entry over time" visual (Section 4) to designer discretion, to skip if the prose already carries the comparability point. Cover visual is not optional.

## Image and alt-text suggestions

1. Cover, top of article. Concept: one progress-record entry rendered as three grouped field blocks (submitted, generated, technical) on the brand navy background. Alt: "Diagram of a body-data record split into submitted, generated, and capture-condition fields." (92 chars)
2. Entry-over-time visual, Section 4, optional. Concept: two entries at two dates side by side, the same field slots filled in both, showing what comparability looks like in practice. Alt: "Two body-data entries from different dates showing the same fields filled in for comparison." (92 chars)
