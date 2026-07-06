---
phase: 1_pre_writing_fact_check
article: 2026-06-10-ai-body-scanners-vs-dexa-rewrite
date: 2026-06-10
status: awaiting_vadim_approve_before_phase_2
brief_source: Vadim brief 2026-06-10 (17-section spec for rewrite of existing canonical article)
existing_article: https://3dlook.ai/content-hub/ai-body-scanners-vs-dexa-scans/
title_decision: A (Vadim approved) — "AI Body Scanners vs. DEXA Scans: Where Mobile Body Scanning Fits"
length_target: 3,500–4,200 (FX use-case sweet spot)
external_sources_verify_status: all 3 verified live
editorial_guardrails_applied: brand-assets/style-guides/editorial-guardrails.md (11-point checklist)
---

# Phase 1 — Pre-writing fact-check

## 1. Existing article fetched and audited

Full article text retrieved from `https://3dlook.ai/content-hub/ai-body-scanners-vs-dexa-scans/`. Current state has multiple issues against editorial guardrails 2026-06-09 and against the rewrite brief.

### 1a. Banned language present in existing article

| Phrase in current article | Banned by | Action |
|---|---|---|
| H1: "The Future of Body Analysis" | Editorial guardrail #8 (no editorializing) + style-guide §7 ("Pioneer/pioneering — feels dated") | Replace with Title A: "Where Mobile Body Scanning Fits" |
| "revolutionary fusion of computer vision" | CLAUDE.md §6 ("revolutionary" banned) | Cut |
| "groundbreaking research" | Same | Cut — Mayo section needs full rewrite anyway |
| "superior insights" | Same | Cut |
| "revolutionizing healthcare" | Same | Cut |
| "Daily/weekly monitoring possible" + "Frequency: Daily/weekly monitoring possible" (table cell) | Brief Section 8 ("Daily scanning can create noise") + editorial guardrail #1 (substantiation) | Replace with realistic cadence framing per brief Section 8 |
| "Complete analysis in under 5 minutes" | Inconsistent with FX product spec (~45 sec) — editorial guardrail #2 (one number everywhere) | Replace with FX standard "results processed in roughly 45 seconds" |
| "over 400 body measurements" | Inconsistent with FX product spec (80+ measurements) — editorial guardrail #2 | Replace with "80+ body measurements" |
| "Wellness device classification" (regulatory row in table) | Editorial guardrail #6 + brief Section 12 ("Avoid presenting FitXpress as simply a 'wellness device classification' unless legal has approved that exact wording") | Replace with "regulatory classification depends on intended use…" per brief Section 12 |

### 1b. Factual / numerical errors in existing article

| Claim | Issue | Source-verified correction |
|---|---|---|
| "Researchers analyzed over 3,000 participants" (Mayo study) | Wrong number. Mayo press release says 1,280 + 133 = **1,413 participants** | Use accurate number (1,280 training + 133 mobile-app validation) OR cut citation |
| "The mobile app integration (myBVI) demonstrated 'excellent performance'" — presented inside a 3DLOOK FitXpress article | **myBVI is a Select Research product, NOT FitXpress.** The Mayo study evaluated myBVI — not 3DLOOK / FitXpress. The current article implicitly attributes the Mayo result to FitXpress. | Per brief Section 11: cite Mayo research as background third-party context only, with explicit attribution to myBVI / Select Research, and explicit statement that FitXpress is a different product without comparable validation. |
| "Body composition market projected to reach $4.8 billion by 2027… or $535.6M in 2023 → $935.8M by 2032" | Two market figures cited side-by-side from different sources — internally inconsistent ($4.8B vs $935.8M) | Replace with single sourced market frame OR drop market-size opener entirely; the rewrite brief does not require a market-size hook |
| "Initial Setup: $10,000–50,000 for professional-grade systems" + "Per-Scan Costs: $5–20" + "ROI within 6–12 months" | No source. Vendor-specific, can't be defended at diligence. | Per editorial guardrail #1 (cut what you can't back): drop all specific $ figures. Keep qualitative framing only if cost is discussed at all. |
| "FDA-approved medical device" for DEXA (table cell) | DEXA scanners are typically **FDA-cleared via 510(k)**, not "FDA-approved." Approval and clearance are distinct regulatory categories. | Use "regulated as a medical device" or "FDA-cleared medical imaging device" |
| "DEXA radiation: ~0.001 mSv" (one passing line) + "DEXA: 1/10th of standard chest X-ray" (another line) | Internally inconsistent — chest X-ray is ~0.1 mSv, so 1/10th would be ~0.01 mSv, not 0.001. The actual DEXA dose varies by scan region (~0.001–0.01 mSv). | Replace with sourced range per RadiologyInfo: "very small dose of ionizing radiation" — qualitative, not numerical |

### 1c. CTA inventory in existing article

| CTA | Current state |
|---|---|
| Primary | "Sign up for a 7-day trial" / "Let's talk" → `https://3dlook.ai/pricing/` |
| Secondary | "Download the eBook" → `https://3dlook.ai/content-hub/the-next-big-leap-in-health-beyond-2025/` |

Per style-guide §5: compliance buyers get **demo-only**, never trial. Rewrite should drop the "7-day trial" framing and use the standard FX demo CTA (`https://3dlook.ai/pricing/#bd-modal-personalized`). Telehealth, GLP-1, and metabolic health buyers fall on the compliance side.

---

## 2. External sources verified (3 of 3)

All three sources recommended in brief Section 14 verified live with real URLs.

### 2a. RadiologyInfo.org — DEXA / DXA patient information

- **URL verified:** https://www.radiologyinfo.org/en/info/dexa ✅
- **Use in rewrite:** Section 2 ("What DEXA Scans Do Well") — DEXA definition, "very small dose of ionizing radiation," "diagnose osteoporosis," "most commonly used and the most standard method for diagnosing osteoporosis"
- **Citation style:** inline anchor link, e.g., `[RadiologyInfo.org's DEXA patient guide](https://www.radiologyinfo.org/en/info/dexa)`
- **Safe direct quotes from source:**
  - "uses a very small dose of ionizing radiation"
  - "commonly used to diagnose osteoporosis, to assess an individual's risk for developing osteoporotic fractures"
  - "simple, quick and noninvasive"
  - "the most commonly used and the most standard method for diagnosing osteoporosis"

### 2b. FDA General Wellness Policy for Low Risk Devices

- **URL verified:** https://www.fda.gov/regulatory-information/search-fda-guidance-documents/general-wellness-policy-low-risk-devices ✅
- **Reissued:** January 6, 2026 (current version)
- **Use in rewrite:** Section 12 ("Does FitXpress Require Regulatory Clearance?") — anchor for the "intended use determines regulatory classification" framing the brief requires
- **Citation style:** inline anchor link to FDA guidance page
- **Safe framing supported by FDA guidance:**
  - "The guidance addresses the FDA's compliance policy for low-risk products that promote a healthy lifestyle ('general wellness products')."
  - "Whether a product is regulated as a device depends on its intended use, judged objectively from labeling, marketing, and other statements."
  - "General wellness products may prompt users to consult a health care professional when outputs fall outside normal thresholds, so long as they do not make disease-specific, diagnostic, or treatment-oriented statements."
- **Critical for the rewrite:** this guidance frame supports the "not positioned as a medical device" framing per editorial guardrail #6 without making any definitive regulatory claim about FitXpress specifically. We can describe the FDA framework neutrally and let the buyer's legal team make their own classification.

### 2c. Mayo Clinic 3D Body Volume Scanner + myBVI study

- **URL verified:** https://newsnetwork.mayoclinic.org/discussion/3d-body-volume-scanner-uses-ai-to-help-predict-metabolic-syndrome-risk/ ✅
- **Published in:** European Heart Journal – Digital Health
- **Tool used in study:** A 3D body volume scanner "originally developed for the clothing industry" + the **myBVI mobile app from Select Research** — neither is 3DLOOK / FitXpress
- **Actual sample size:** 1,280 training + 133 mobile-app validation = 1,413 participants (NOT 3,000)
- **Actual results:** 85% AI accuracy in predicting metabolic syndrome risk, vs BMI 72%, waist-hip 78%
- **Critical compliance note:** The existing 3DLOOK article presents this study inside a FitXpress comparison article, which implicitly suggests FitXpress has similar validation. **It does not.** Per brief Section 11 + editorial guardrail #1 (substantiation): if Mayo research is cited at all, it must be as third-party context for the broader "body shape data has predictive value for metabolic health" theme, with explicit attribution to myBVI as the actual study tool, and explicit statement that FitXpress has not undergone equivalent validation.
- **Safer alternative:** cut the Mayo case-study section entirely; replace with general statement about the research direction without naming specific studies. This is the cleaner editorial choice per editorial guardrail #1.

---

## 3. Brief alignment with editorial guardrails (11-point checklist)

All 11 principles checked against the brief. Brief is well-aligned overall.

| # | Guardrail | Brief alignment | Action for Phase 3 |
|---|-----------|-----------------|--------------------|
| 1 | Claim substantiation — cut what you can't back | ✅ Strong — Brief Section 10 explicitly counsels against "as accurate as DEXA" + Section 11 counsels against turning third-party research into FitXpress claims | Apply throughout — especially Mayo section + cost-benefit section |
| 2 | One number, everywhere the same | ✅ Strong — Brief specifies FX product numbers (80+ measurements, 3D model, etc.) | Use FX fingerprint numbers consistently (80+ measurements, ~45 sec, two-photo capture) |
| 3 | "Independent" / "validated" / "third-party" reserved | ⚠ Soft — Brief uses "validated and approved" once in regulatory context | Acceptable — brief use is conditional ("unless… validated and approved") |
| 4 | Drop bare ">X%" without methodology | ✅ Strong — Brief Section 10 covers this | Apply — no "85% accuracy" without full myBVI attribution |
| 5 | Honest caveats beat clean overclaims | ✅ Strong — Brief Section 16 compliance guardrails | Apply throughout |
| 6 | Medical/regulatory: "not positioned as," never "does not apply" | ✅ Strong — Brief Section 12 says "Avoid presenting FitXpress as simply a 'wellness device classification' unless legal has approved that exact wording" | Apply verbatim Asselya/legal framing from earlier articles |
| 7 | Conditional language for boundaries | ✅ Strong — Brief Section 16 uses conditional framings ("when the workflow requires…") | Apply |
| 8 | Diligence register, not insider register | ✅ Strong — Brief Section 15 ("Avoid: Overly promotional language, 'Revolutionary' language") | Apply — replace existing article's "Future of Body Analysis" / "Revolutionary fusion" register |
| 9 | Lead with the right question, with concrete verticals | ✅ Strong — Brief Section 1 explicitly names telehealth / GLP-1 / metabolic / weight management | Apply |
| 10 | Structure defaults (numbered lists, clean tables) | ✅ Strong — Brief includes 2 tables (Sections 4 + 15) | Apply |
| 11 | When in doubt, flag — don't decide | ✅ Strong — Brief Section 12 explicitly defers regulatory claims to legal | Apply — surface open items rather than silent edits |

**No editorial guardrail violations in the brief.** Brief is internally consistent with the framework established 2026-06-09.

---

## 4. Compliance-sensitive fragments + recommended safe wording

| # | Risk area | Brief location | Recommended safe wording |
|---|-----------|----------------|---------------------------|
| C1 | "FitXpress is not a DEXA replacement" (central thesis) | Brief Section 3 | Use verbatim throughout: "FitXpress is not a DEXA replacement. It is a complement to DEXA and hardware-based assessments — designed for frequent, remote, non-diagnostic body-data tracking between clinical measurement points." Place in intro + Section 5 + Conclusion. |
| C2 | Mayo Clinic study attribution | Brief Section 11 | If cited at all: "Research published in the *European Heart Journal – Digital Health* using a 3D body volume scanner and the myBVI mobile app (Select Research) reported X. **FitXpress is a different product and has not undergone equivalent validation.**" Else: cut. |
| C3 | DEXA "gold standard" framing | Existing article + brief Section 2 | Brief Section 2 explicitly says avoid blanket "gold standard for all body composition analysis" — replace with: "DEXA is widely used as a clinical standard for bone mineral density assessment and is also used for body composition analysis in clinical, athletic, and research contexts." Already in brief. Use verbatim. |
| C4 | "FitXpress is diagnostic" inference | Brief Section 11 | Verbatim from brief: "FitXpress outputs should be understood as supportive body-data signals. Diagnosis, treatment decisions, and clinical interpretation remain with qualified professionals." Place as standalone disclaimer in Section 11. |
| C5 | Regulatory clearance claim | Brief Section 12 + FDA general wellness policy verified | Use the FDA general wellness framework neutrally: "Regulatory classification depends on intended use, product claims, jurisdiction, and workflow. The [FDA's General Wellness: Policy for Low Risk Devices guidance](URL) describes when low-risk lifestyle products fall outside the device definition. FitXpress is not positioned as a medical device; the regulatory classification for a specific deployment should be evaluated by the deploying organization's legal/regulatory team based on intended use and claims." |
| C6 | "FDA-approved" / "FDA-cleared" for FitXpress | Brief Section 12 | Never used. Existing article does not claim this for FitXpress — only for DEXA. For DEXA, replace "FDA-approved" → "FDA-cleared medical imaging device" or "regulated as a medical device" |
| C7 | GLP-1 program positioning | Brief Section 9 | Use verbatim safer phrasing from brief: "In a GLP-1 or metabolic program, FitXpress should be positioned as a remote monitoring and engagement layer, not as a diagnostic or prescribing tool." Plus the explicit guardrails list (no eligibility determination, no obesity diagnosis, no sarcopenia diagnosis, etc.) |
| C8 | "Scan daily/weekly" cadence | Existing article FAQ + table | Replace with brief Section 8 realistic cadence: "Many GLP-1, metabolic, wellness, and fitness programs may choose every 2 to 4 weeks or monthly scanning. Daily scanning can create noise, user anxiety, and low-value data." |
| C9 | Cost-benefit specific $ figures | Existing article | Cut all specific $ figures. If cost is discussed: qualitative only ("subscription model" / "per-scan economics improve with volume" without specific $) |

---

## 5. Reuse / revise / cut map vs existing article

Per brief Section 9 reuse instructions, applied to identified sections of existing article:

| Existing section | Action | Notes |
|---|---|---|
| H1 "The Future of Body Analysis" | **Replace** with Title A | "Where Mobile Body Scanning Fits" |
| Market projection intro ($4.8B / $935.8M) | **Cut** | Internally inconsistent + not required by brief |
| "AI-Powered 3D Body Scanners: The Future of Accessible Health Monitoring" (H2) | **Rewrite per brief Section 3** | Drop "revolutionary fusion" + "400 measurements" + "5 minutes"; use FX fingerprint (80+, ~45 sec, two-photo) |
| "DEXA Scans: The Clinical Gold Standard" (H2) | **Rewrite per brief Section 2** | Drop "gold standard for all body composition" blanket; use safer RadiologyInfo-anchored framing |
| Technology Comparison table | **Rewrite per brief Section 4** | New role-based comparison table; drop $ figures; replace "Daily/weekly" with realistic cadence; replace "FDA-approved" with "FDA-cleared" for DEXA |
| "When AI 3D Scanners Excel" (H3) | **Reuse with edits per brief Section 6** | Move concept earlier; remove cadence overclaims |
| "When DEXA Remains Irreplaceable" (H3) | **Reuse with light edits per brief Section 2** | Keep "Clinical Diagnostics" + "Research Applications" subsections |
| "Revolutionary Case Study: Mayo Clinic" (H2) | **Cut OR rewrite per brief Section 11** | Recommend cut. If kept: explicit myBVI attribution + "FitXpress different product" disclaimer + accurate sample size (1,413 not 3,000) |
| Integration and Implementation (H2) | **Rewrite per brief Section 14** | New "Business Applications: Which Buyer Should Use Which Approach" — telehealth/GLP-1/metabolic first |
| Cost-Benefit Analysis (H2) | **Cut all $ figures** | Per editorial guardrail #1. Keep qualitative if any |
| Privacy and Data Security | **Reuse, expand per brief Section 13** | More specific to telehealth/body data/consent/biometric sensitivity |
| Business Applications (H2) | **Rewrite per brief Section 14** | Telehealth first; named subsections |
| Final Thoughts (H2) | **Rewrite per brief Section 17** | Hybrid-positioning conclusion + CTA |
| FAQ section | **Rewrite per brief Section 16** | 13 new/revised Q&A per brief spec |
| Primary CTA "7-day trial" | **Replace** | Standard FX demo CTA: `https://3dlook.ai/pricing/#bd-modal-personalized` |
| Secondary eBook CTA | **Cut** | Style-guide §5: one CTA per article |

**New sections to add (not in existing article):**
- Section 5: "Is FitXpress a DEXA Replacement, Alternative, or Complement?" (central new section)
- Section 6: "Why Would Someone Use FitXpress Instead of DEXA?"
- Section 7: "Why Use FitXpress Between DEXA Scans?"
- Section 8: "How Often Can Users Scan With FitXpress vs DEXA or Hardware?"
- Section 9: "How FitXpress Fits Inside a GLP-1 or Metabolic Program" (with compliance guardrails)
- Section 10: "Where Hardware Body Scanners Fit" (separate from DEXA)
- Section 11: "Is FitXpress Diagnostic?" (explicit disclaimer)
- Section 12: "Does FitXpress Require Regulatory Clearance?" (FDA general wellness framework)
- Section 15: Decision Framework Table

---

## 6. Open questions for Vadim before Phase 2

1. **Customer references**: Any FitXpress customers in telehealth / GLP-1 / metabolic / weight-management vertical to name? Or thought-leadership entry similar to bariatric + occupational health (no live customer)? **My default assumption: no live customer reference; frame article as buyer-education content.**

2. **Mayo Clinic / myBVI handling**: My strong recommendation is to **cut the Mayo case-study section entirely** rather than try to keep it with the necessary "myBVI is not FitXpress" disclaimers. The existing article's implicit attribution of myBVI results to FitXpress is the single biggest defensibility risk in the current piece. Alternative: keep as one brief background paragraph in Section 1 or 9 with explicit myBVI / Select Research attribution. **Confirm: cut or keep-with-explicit-attribution?**

3. **Cost figures**: My recommendation is to cut all specific $ ranges entirely (no source, vendor-specific, unverifiable). Brief Section 9 leaves cost-benefit in the "rewrite carefully" pile but the safer move is to cut $. **Confirm: cut all $ figures, or keep with qualitative ranges?**

4. **DEXA regulatory framing**: Replace existing article's "FDA-approved medical device" with "FDA-cleared medical imaging device" or "regulated as a medical device" — more accurate (DEXA scanners go through 510(k) clearance, not full approval). **Confirm: "FDA-cleared" is the right framing for DEXA?**

5. **FX product numbers consistency**: Use FX fingerprint throughout (80+ measurements, ~45 seconds processing, two-photo guided flow) — replacing existing article's "400 measurements" and "5 minutes." **Confirm: align all product-fact mentions to current FX product page spec?**

6. **Hardware scanners — naming**: Brief Section 10 says "address hardware-based body scanners separately from DEXA" but does NOT specify which hardware brands/products to name (e.g., Fit3D, Styku, Size Stream). Style-guide §4 says "Competitors: Never named directly" — implies stay generic. **Confirm: keep generic ("hardware body scanners"), do not name specific brands?**

7. **External link discipline**: Style-guide §4 historic default is "No footnotes. No external hyperlinks to source sites." But the occupational-health article (2026-06-08) departed from this for compliance-grade gov citations (BLS, EEOC, OSHA, ACOEM). This rewrite has 3 verified external sources (RadiologyInfo, FDA general wellness, optional Mayo Clinic). **Confirm: 3 external links acceptable for this article, consistent with the occupational-health precedent? Or revert to style-guide §4 default of no external links?**

8. **Brief Section 5 H1 alternative deferred**: Vadim confirmed Title A. Logging here that Title B ("FitXpress vs. DEXA Scans: Where Mobile Body Scanning Fits in Telehealth and GLP-1 Programs") is NOT used. ✅ No action — confirmed.

---

## 7. Phase 1 verdict

Brief is comprehensive and well-aligned with editorial guardrails. The rewrite work is mostly execution + 9 surgical safety fixes (compliance fragments C1–C9). Three external sources verified live. The most consequential editorial decision is **what to do with the Mayo Clinic section** — the existing article's implicit attribution of myBVI study results to FitXpress is the biggest defensibility risk in the current piece, and the cleanest fix is to cut that section entirely.

**8 open questions surface above** — most consequential: Q2 (Mayo handling), Q3 (cost figures), Q7 (external link discipline).

**Awaiting Vadim's resolution before Phase 2 outline.**
