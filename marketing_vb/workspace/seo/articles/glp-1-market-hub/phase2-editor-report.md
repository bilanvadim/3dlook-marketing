# Phase 2 Editor Report — glp-1-market hub refresh (draft-v2-editor)

Editor pass over `draft-v1-writer.md` → `draft-v2-editor.md`. Four passes: citation dedup, structure/flow, expert-voice/AI-pattern reduction, final polish (banned words, abbreviations, claims discipline, links).

Date: 2026-08-01. Byline: Assel Sekerova (unchanged from writer). Status: `edited`.

---

## 1. Word count — before / after

| | Words (body, excl. frontmatter) |
|---|---|
| draft-v1-writer | ~4,150–4,300 (writer-measured; over the plan's stated cap) |
| draft-v2-editor | ~3,520 (target ~3,600; within the campaign-manager band of 3,150–3,650) |

Resolved the plan's internal inconsistency (per-section lower bounds summed to ~4,250 vs. stated total ~3,150–3,650) in favor of the campaign-manager's explicit restated instruction (~3,150–3,650, target ~3,600). Trimmed ~700 words by tightening prose only. No required must-cover point, approved claim, internal link, FAQ, or boundary section was dropped. Heaviest trims: H2.3 (deduped repeated J.P. Morgan attribution), H2.4, H2.7, H2.9, H2.12 FAQ. Both required FX-003 repeatability mentions (H2.9 and H2.10) were kept; surrounding sentences tightened.

---

## 2. Banned-word / terminology grep

Grepped the edited file for every hard-banned item. Result: **clean** (no matches) for: em dash (—), "objective" (as noun), "reader", "audience", "this article", "this guide", "by hand", "plus" (as connector), "revolutionary", "game-changing", "transform/transforming/transformative", "harness", "leverage", "utilize/utilizing", "robust", "seamless", "comprehensive", "delve", "Furthermore/Moreover/Additionally" as sentence-openers.

Fixes made vs. the writer draft:
- **SOC 2** removed from H2.11 (see §3, FX-012). Was the only "SOC 2" hit.
- **Triple parallelism** in H2.1 ("its own operators, its own economics, and its own retention problem") rewritten to "its own operators and economics, and a retention problem to match" (CLAUDE.md §6 bans triple parallelisms).
- En dashes retained only inside numeric ranges (96–97%, 25 to 30 → written as words; $2.7 to $2.9 billion) per the locked about-me.md/proof-points convention. No rhetorical em/en dashes.

---

## 3. Claims discipline — per claim ID (verified against proof-points.md)

| Claim | Proof-points wording | Draft wording | Verdict |
|---|---|---|---|
| FX-001 | 96-97% accuracy vs manual measurements | H2.10: "roughly 96–97% accuracy" — qualified (internal validation, guided protocol, defined test population); routed deep accuracy to accuracy-framework page | PASS — never bare, never universal |
| FX-003 | Variance across repeated scans < 1 cm | H2.9 + H2.10: "scan-to-scan repeatability of **< 1 cm**" (byte-identical both places) | PASS — written as `< 1 cm`; in a separate sentence from FX-001 in both sections |
| FX-004 | Weight estimation ±3.5% average error | H2.10: "about ±3.5% average error… software-derived signal for context rather than a replacement for a calibrated scale" | PASS |
| FX-005 | Under 45 seconds; 2 photos (front + side) | H2.8, H2.10, FAQ: "two smartphone photos, front and side… under 45 seconds" | PASS — matches proof-points exactly; "under 45 seconds" is the only total-time figure in the article |
| FX-006 | 80+ body measurements | H2.8, H2.10, FAQ: "80+ body measurements" | PASS |
| FX-007 | BMI, BMR, fat %, lean mass, fat mass | H2.6, H2.10, FAQ: same five outputs | PASS (proof-points also lists essential/beneficial fat; draft uses the approved subset) |
| FX-009 | UK Meds — BMI verification for online pharmacy | H2.10: one-line cross-vertical mention + link to pharmacy page | PASS |
| FX-010 | Yazen — 34,000 scans 2025, weight-loss management support | H2.10: "34,000 FitXpress scans in 2025… weight-loss management support workflow" | PASS |
| FX-012 | HIPAA / GDPR / no personal identifiers / photos deleted after processing / not a medical device | H2.2, H2.10, H2.11, FAQ | PASS after SOC 2 removal (below) |

**FX-001 vs FX-003 separation (H2.9/H2.10 check):** confirmed. FX-003 lands in its own paragraph (H2.9 line 116, H2.10 line 124). FX-001 lands in a distinct later paragraph (H2.10 line 126) that explicitly states "Accuracy is a separate question from repeatability." The two benchmarks are never combined in one sentence.

**FX-005 photo-count/angle wording:** proof-points says "2 (front + side)". Draft says "two smartphone photos, front and side." Confirmed match.

**FX-012 / SOC 2:** proof-points.md compliance table lists HIPAA, GDPR, TLS, AWS S3 SSE-S3, photo retention, photo blur, no personal identifiers — **no SOC 2**. "SOC 2 where applicable" appears only as a generic framing example in editorial-guardrails §6, not as a 3DLOOK-sourced certification. Per the task instruction (drop if not sourced; do not invent compliance certifications), the H2.11 phrase "(HIPAA, GDPR, and SOC 2 where applicable)" was changed to "data-privacy frameworks such as HIPAA and GDPR." No fabricated certifications remain.

**Numbers audit:** every quantitative figure traces either to proof-points.md (product claims) or to the three writer-verified external sources (market data in H2.3 / FAQ). No number lacks a source. Drug clinical-efficacy figures remain excluded.

---

## 4. Boundary / cannibalization check

- **H2.11 vs plan lines 32–34:** mirrors the vertical boundary — no diagnosis; no treatment/prescribing decisions; no eligibility/underwriting determination; not a replacement for clinicians, DEXA, BIA, or a calibrated scale (conditional per guardrail #7); guarantees no weight-loss/adherence/compliance outcome; not a medical device; not a standalone medical authority. PASS.
- **Sideways-owned topics handled with one line + link only (no re-explanation creep):**
  - Visual Progress Tracking (adherence/retention mechanics) — H2.5 hands off in one sentence, explicitly "not repeated here." PASS.
  - Beyond BMI (BMI critique) — H2.6 states the full critique "lives on the Beyond BMI page," does not reproduce it. PASS.
  - Online Pharmacy BMI Verification (compliance workflow) — H2.7 and H2.10 mention only that verification is the touchpoint and link out; no compliance-workflow re-explanation. PASS.
- No drug clinical-efficacy claims, no fraud-detection claim, no underwriting/eligibility decisioning language anywhere. PASS.

---

## 5. Internal links — live-check results

**Tooling note:** WebFetch/curl are not available in this editor's toolset, so live HTTP status codes could not be pulled directly. Instead, every internal URL was reconciled against the **authoritative link map in the context pack** (`workspace/seo/_context-packs/2026-08-01-glp-1-market-hub-refresh.yaml` → `internal_link_targets`, built for this exact task on 2026-08-01) and cross-checked against the **published-URL inventory** in `brand-assets/content-strategy/content-plan.csv`. The writer had flagged 6 best-guess slugs; 5 were wrong and are corrected below. Publisher should still run a final HTTP-200 pass before go-live.

| URL in writer draft | Status vs. authoritative sources | Action taken |
|---|---|---|
| /content-hub/visual-progress-tracking-glp-1/ | WRONG slug — canonical is `visual-progress-tracking-glp1-adherence-retention` (context pack + content-plan.csv, published) | Corrected (H2.2, H2.5) |
| /content-hub/beyond-bmi/ | WRONG slug — canonical is `beyond-bmi-business` (context pack + content-plan.csv, published) | Corrected (H2.2, H2.6) |
| /for-bmi-verification/ (used for "Online Pharmacy BMI Verification") | Product page exists, but the intended sideways target is the content-hub compliance guide `online-pharmacy-bmi-verification-a-2026-compliance-guide` (context pack + content-plan.csv, published 17.06.2026) | Corrected to the compliance-guide URL (H2.2, H2.7, H2.10) |
| /content-hub/glp-1-compliance-challenge/ | Matches context pack + content-plan.csv | Kept |
| /content-hub/weight-loss-industry-overview/ | Matches context pack link map | Kept (not independently found in content-plan.csv; publisher HTTP-verify) |
| /content-hub/body-scanning-technology-for-weight-loss/ | Matches context pack + referenced in content-plan.csv | Kept |
| /content-hub/weight-loss-clinic-marketing-tips/ | WRONG slug — canonical is `top-10-weight-loss-clinic-marketing-tips` (context pack) | Corrected (H2.7) |
| /content-hub/bariatric-pre-qualification/ | WRONG slug — canonical is `bariatric-pre-qualification-mobile-3d-body-scanning` (context pack + content-plan.csv, published) | Corrected (H2.9) |
| /content-hub/3dlook-turns-two-photos-structured-body-data/ | Matches context pack + content-plan.csv | Kept |
| /content-hub/ai-body-data-health-hub/ | Matches context pack up-link (Main Health hub) | Kept — see open issue #1 |
| /content-hub/ai-in-fitness-industry/ | Matches context pack + content-plan.csv (published 31.07.2026) | Kept |
| /content-hub/mobile-body-scanning-accuracy/ | Matches context pack + content-plan.csv (published 03.06.2026) | Kept |
| /fitxpress/for-telehealth-and-weight-loss/ | Matches context pack down-link | Kept |
| /legal/ | Matches context pack trust-link (interim) | Kept |

**Net link changes:** 5 slug corrections (visual-progress-tracking, beyond-bmi, online-pharmacy-bmi-verification, top-10-weight-loss-clinic-marketing-tips, bariatric-pre-qualification). No link was dropped; all 4 directions (up/side/down/trust) remain intact.

**External market sources (H2.3):** the three were WebFetch-verified by the writer (documented in writer-notes.md §H2.3). I could not independently re-fetch (no WebFetch tool), so I retained them as-is and deduped the J.P. Morgan citation to a single hyperlink (Pass 1). Publisher should re-confirm all three resolve at go-live:
- J.P. Morgan Research — https://www.jpmorgan.com/insights/global-research/current-events/obesity-drugs
- KFF 2025 Employer Health Benefits Survey — https://www.kff.org/health-costs/2025-employer-health-benefits-survey/
- STAT News (Hims & Hers FY2025) — https://www.statnews.com/2026/02/23/him-hers-earnings-2026-outlook-compounded-semaglutide/

---

## 6. FAQ completeness

All 8 FAQs from plan.md lines 228–235 are present, in order, each answered in 2–5 sentences with a direct answer up front (GEO/AEO-friendly):
1. What is driving GLP-1 market growth? ✓
2. How big is the GLP-1 market? ✓ (sourced figure, J.P. Morgan)
3. Why is progress tracking important for GLP-1 programs? ✓
4. What body data should GLP-1 programs track? ✓ (FX-007)
5. Can body scanning replace the scale or DEXA? ✓ (No — supports/complements)
6. Is this a medical device? ✓ (No — FX-012)
7. How do remote check-ins work? ✓ (FX-005/FX-006)
8. What does FitXpress not do? ✓ (mirrors H2.11)

CTA: single BOFU close ("See how FitXpress supports GLP-1 programs with structured progress tracking" → FitXpress telehealth/weight-loss page) + scope disclaimer. Intent-appropriate for a hub. PASS.

---

## 7. Frontmatter check

Present and correct: `slug` (glp-1-market), `product` (fitxpress), `title` (exact fixed title — "GLP-1 Market Growth and the Need for Better Patient Progress Tracking"), `primary_keyword` (GLP-1 market growth), `author` (Assel Sekerova), `status` (edited), `created` (2026-08-01), `hub` (glp-1-market), `cluster` (main-hub), `intent` (hub), `action_type` (refresh-expand-existing). Added `word_count`, `editing_passes`, `claims_verified` for the pipeline. PASS.

Primary keyword placement: H1 ✓; first paragraph of H2.1 ("GLP-1 market growth started inside diabetes care…") ✓; H2 heading "GLP-1 Market Growth: Size and Trajectory" ✓ (plus woven in H2.3 body). PASS.

---

## 8. HIPAA / GDPR abbreviation resolution (M1 open item)

Resolved per the task instruction in favor of **about-me.md convention**: HIPAA and GDPR are left **bare** (not expanded) as established terms, consistent with every past FitXpress article. This is the correct resolution because CLAUDE.md §15 hard-requirement #0 gives about-me.md priority on voice over the generic guardrail M1 first-use-expansion rule. All other abbreviations ARE expanded at first use per M1: GLP-1 (H2.1), BMI (H2.2), BMR (H2.6), DEXA/BIA (H2.11), API/SDK (H2.10). BMR and DEXA are expanded once at first use and use the short form thereafter (corrected two writer re-expansions in H2.10 and the FAQ).

---

## 9. Guardrail M2 (stacked negation) fixes

- H2.9 closing: "It does not make clinical decisions or replace clinical judgment" → positive frame "clinical decisions and judgment stay with the care team."
- H2.11: "it does not promise a clinical result and does not by itself make any program compliant" (chained negation) → "clinical results stay with the care model and overall program compliance stays with the program."
- H2.11 eligibility line collapsed to a single negation ("makes no eligibility or underwriting determination").
- FAQ #8: replacement boundary reframed positively ("Where DEXA, BIA, or a calibrated scale is required, it complements those methods rather than replacing them").
- The one required explicit boundary negation per section (guardrail #6, "not positioned as a medical device") is preserved; no second negation is chained onto it in the same sentence.

---

## 10. Remaining open issues for publisher / campaign manager

1. **Live HTTP-200 pass still owed.** Internal URLs were reconciled against the authoritative context-pack link map and the content-plan.csv inventory, not a live fetch (no WebFetch/curl in the editor toolset). Publisher should HTTP-verify all 14 internal + 3 external URLs at go-live. Two internal URLs could not be independently cross-confirmed in content-plan.csv and rely on the context-pack link map alone: `weight-loss-industry-overview` and `ai-body-data-health-hub` (the Main Health hub up-link — content-plan.csv shows the Main Health hub as "Create net-new," so confirm it is actually published at that slug before relying on it; if it 404s, drop the two hyperlinks and keep the anchor text).
2. **Byline** reassigned Dana Vioreanu → Assel Sekerova per instruction; confirm on the live CMS record at publish (refresh-in-place, same URL `/content-hub/glp-1-market/`).
3. **External sources** were writer-WebFetch-verified but not re-fetched by the editor; re-confirm resolution at publish.
4. No unresolved claims-discipline or boundary conflicts. No Open Items for Asselya beyond the URL live-check above.
