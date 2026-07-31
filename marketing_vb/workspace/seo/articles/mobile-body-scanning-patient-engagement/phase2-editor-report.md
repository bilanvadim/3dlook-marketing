# Phase 2 Editor Report — mobile-body-scanning-patient-engagement

**Input:** `draft-v1-writer.md` (writer draft, 2,814 words incl. writer-notes block)
**Output:** `draft-v3-edited.md` (status: edited)
**Final article word count (body only, writer-notes block removed):** ~2,318 words (within the 2,200–3,000 plan target)
**Editing passes run:** 4 (Citation dedup · Structure & flow · Expert voice + Pass 3b strategy compliance · Final polish)

---

## Pass 1 — Citation dedup

**External research citations (H2.3):** both preserved and each cited exactly once. No dedup needed.
- Telehealth-utilization study (MEPS / *Healthcare*): https://pmc.ncbi.nlm.nih.gov/articles/PMC12897674/ — intact, resolves.
- GLP-1 discontinuation study (*JAMA Network Open*): https://pmc.ncbi.nlm.nih.gov/articles/PMC11786232/ — intact, resolves.

**Internal-link dedup:** the writer flagged 10 distinct targets with 2 repeated anchors (12 total instances), above the style-guide 6–9 soft target.
- `mobile-body-scanning-accuracy/` appeared in H2.4 and H2.10 → kept the stronger H2.4 anchor (where repeatability is introduced and defined), removed the H2.10 duplicate; replaced with a non-linked prose reference to capture protocol.
- `legal/` (privacy) appeared in H2.7 and H2.10 → kept the H2.7 anchor (the full privacy paragraph), removed the H2.10 duplicate; replaced with a cross-reference to the privacy note above.

**Result:** anchor instances 12 → 10. Distinct targets stay at 10 because **all 10 are plan-mandated in the plan's final link map** (dropping any distinct target would drop a plan-mandated link, which the brief forbids). All 4 directions remain covered. This is the maximum defensible trim without violating the "do not drop any plan-mandated link / any of the 4 directions" constraint.

---

## Pass 2 — Structure & flow

- **Transitions:** no "Furthermore / Moreover / Additionally" sentence starters anywhere. H2-to-H2 flow uses thematic bridges, unchanged.
- **Intro:** 2-sentence concrete pain hook confirmed ("Remote care removed the touchpoint… What remains is a figure a patient types into an app between visits."). Reframe move ("the useful question is narrower…") retained.
- **Conclusion:** actionable, ends on operational recap + single BOFU CTA. No "in summary we discussed."
- **Rhythm fix (H2.9):** the four per-vertical paragraphs all opened "In [vertical]…" (monotone). Varied the 3rd and 4th openings ("Wellness and coaching programs use the same visible progress…", "Remote patient monitoring depends on a reproducible body record…") so the section no longer reads as a mechanical parallel list.

---

## Pass 3 — Expert voice

- Reworded the near-banned construction "Privacy posture matters for a compliance buyer, so **it is worth stating plainly**" → "Privacy posture **is a procurement gate** for a compliance buyer, so **the specifics matter**." (H2.7). Sharper, buyer-framed, removes the AI-tell.
- Wove the head term "patient engagement" into H2.1 ("the repeat check-in that should drive **patient engagement**") for primary-keyword placement early in the body without introducing the product before H2.2 (respects the plan's "no product claims in H2.1" boundary).
- The draft already carries strong Assel-voice markers (the reframe move; "Production conditions are not lab conditions"; limits stated in the same breath as benefits; hedged operational verbs). No generic-AI pattern rewrites were needed beyond the two above — no triple-parallelism hype, no "not just X, it's Y", no em-dash rhetoric, no hype adjectives were present in the body.

**Open item flagged (guardrail #11 — flag, not silent edit):** a concrete production proof-point (Yazen, 34,000 FitXpress scans in 2025, from `proof-points.md` customer-outcomes) would materially strengthen H2.7 "Where FitXpress fits." It was **not inserted**, because the plan's per-section approved-claims list for H2.7 did not include a customer example, and the writer's `claims_used` set does not carry it. Recommend Asselya approve before insertion (volume-only framing, no engagement/retention outcome claim, so no guardrail breach).

---

## Pass 3b — Content-strategy compliance checklist

| Item | Result | Note |
|------|--------|------|
| Positioning §8 — no forbidden claims (diagnose / treatment / eligibility / underwriting / replaces clinician-DEXA-reference / guarantees compliance / detects fraud / standalone authority) | PASS | All framed as "supports / helps standardize / structured records." |
| "What FitXpress does NOT do" section present | PASS | H2.8, constructive framing, one clean negative per bullet. |
| Vertical boundary §9 — telehealth stays in remote-care/experience/documentation/privacy/monitoring | PASS | No eligibility/underwriting/pharmacy-BMI bleed. |
| Sensitive-vertical scope note early | PASS | Italic scope note in H2.2; full boundary in H2.8; closing disclaimer in H2.12. |
| Cannibalization §5 — broader than GLP-1; GLP-1 mechanics handed off sideways only | PASS | H2.9 links `visual-progress-tracking-glp1-adherence-retention/` as the deep dive; zero GLP-1 adherence-mechanics duplication; GLP-1 is 1 of 4 verticals. |
| Internal links §11 — 4 directions (up / sideways / down / trust) | PASS | Up: AI-in-telehealth hub (H2.1) + AI-body-data-health hub (H2.2). Sideways: two-photos, beyond-BMI, GLP-1 visual-progress, GLP-1 market, accuracy-drives-ROI. Down: FitXpress for telehealth & weight loss (H2.12). Trust: accuracy framework (H2.4) + legal/privacy (H2.7). |
| FAQ §14 — present, 2–5 sentences, includes "not a medical device / decisioning" and "what FitXpress does not do" | PASS | 8 Q&A pairs; answers 2–4 sentences; numbers byte-consistent with body (guardrail #2). |
| CTA §15 — matches intent, single BOFU close, not forced demo in TOFU | PASS | One direct BOFU close in H2.12 only; soft evaluation framing earlier; plan explicitly authorizes the single direct close. |

**No content-strategy checklist item failed.**

---

## Pass 4 — Final polish

- **Banned words / AI signatures:** grep of the body returned zero for em dash (—), en dash (–), "objective" (any use), "reader", "audience", "this article", "this guide", "by hand", "revolutionary", "game-changing", "transforming", "harness", "leverage", "utilize/utilizing", "robust", "seamless", "comprehensive", "cutting-edge", "groundbreaking", and "Furthermore/Moreover/Additionally" as starters. (All em dashes in the writer draft lived only in the non-published "Writer notes" meta-block, which is not carried into the edited article.)
- **"plus" as connector/quantifier:** the one hit, "80-plus measurements" (H2.2), was standardized to "more than 80 measurements" — also tightens one-number consistency (body/FAQ now all read "more than 80").
- **Abbreviations (M1) — expanded at first use, verified in reading order:** artificial intelligence (AI) H2.1 · Body Mass Index (BMI) H2.1 · application programming interface (API) H2.2 · software development kit (SDK) H2.2 · basal metabolic rate (BMR) H2.2 · Medical Expenditure Panel Survey (MEPS) H2.3 · glucagon-like peptide-1 (GLP-1) H2.3 · General Data Protection Regulation (GDPR) H2.7 · Health Insurance Portability and Accountability Act (HIPAA) H2.7 · System and Organization Controls 2 (SOC 2) H2.7 · Transport Layer Security (TLS) H2.7 · Amazon Web Services (AWS) H2.7 · dual-energy X-ray absorptiometry (DEXA) H2.8 · bioelectrical impedance analysis (BIA) H2.8 · electronic medical record (EMR) H2.10. All PASS.
- **Stacked negation (M2):** boundary sentences carry exactly one clean negative each (scope note H2.2, H2.8 bullets, FAQ 5/8, closing disclaimer). No chained "does not… nor does it…", no interrupted "is — and is not —", no double-negative idioms. Repeated disclaimer across sections left as-is (permitted — M2 governs per-sentence density, not disclaimer frequency).
- **Claims discipline:** every internal number traces to `proof-points.md` (more than 80 measurements; under 45 seconds; repeatability `< 1 cm`; photos deleted immediately or within 30 days; no personal identifiers; HIPAA/GDPR/SOC 2/TLS/AWS). Every external number carries a named source + live link. No invented figures.
- **"<30s" sub-timing:** confirmed absent. The only total-time figure is "under 45 seconds" (H2.2, FAQ). The QC-flagged "<30s" from a prior plan draft did not reappear. "In under a minute" (H2.5) is a colloquial restatement, not a conflicting figure.
- **Keyword placement:** primary keyword exact in H1 and verbatim in the H2.12 close ("that is how mobile body scanning improves patient engagement"); secondary keyword verbatim in H2.7 ("mobile body scanning and patient engagement meet in practice"); head term "patient engagement" now in H2.1; concept in H2.2 and H2.9 titles.
- **Frontmatter:** all required fields present and correct — slug, product, title (exact match), primary/secondary keyword, meta_description, hub, cluster, intent, action_type, priority: P0, existing_urls, cannibalization_guardrail, vertical_boundary, author: Assel Sekerova, status: edited, created, plus editor fields (word_count, editing_passes, claims_verified, changes_summary).

---

## External-link integrity (explicit check)

Both H2.3 external source links survived intact and unchanged:
- https://pmc.ncbi.nlm.nih.gov/articles/PMC12897674/ (telehealth utilization, MEPS / *Healthcare* 2026) — PRESERVED
- https://pmc.ncbi.nlm.nih.gov/articles/PMC11786232/ (GLP-1 discontinuation, *JAMA Network Open* 2025) — PRESERVED

## Carried-over writer verification notes (for publisher/QC)

- Source substitution in H2.3 (not a violation): CDC NCHS and HHS ASPE briefs returned HTTP 403 to the automated fetch; the peer-reviewed MEPS-based study was used instead. Named, methodology-backed, resolves cleanly. No figure invented.
- The 64.8% GLP-1 figure is consistent with the sideways sibling page `visual-progress-tracking-glp1-adherence-retention/`, so the stat is aligned across the cluster (guardrail #2).
- 96–97% one-time accuracy was deliberately kept out of the body; repeatability (`< 1 cm`) is the load-bearing longitudinal claim and accuracy detail routes to the accuracy framework link (about-me.md accuracy framing + guardrail #4). Left as the writer set it.
