---
phase: 1_internal_data_audit
article: 2026-05-29-3dlook-accuracy-enterprise-evaluation
date: 2026-05-29
status: awaiting_approval_before_phase_2
---

# Phase 1 — Internal Data Audit (3DLOOK Accuracy Pillar)

## 0. Source materials status

**PDFs in `/mnt/user-data/uploads/`:** **NOT AVAILABLE** in this environment. The directory does not exist. The three documents Vadim referenced —
- *Comprehensive Datasets and Precision Metrics, May 2024*
- *3DLOOK Technology Presentation, May 2025*
- *Updated Security Privacy Slide, Aug 2025*

— were not auto-shared into the workspace.

**What this means for the audit:**
The brief itself lists vetted numbers Vadim has already curated from those three PDFs. For this article we treat **the brief as the authoritative numeric source**. No number will be used in the article that is not on Vadim's vetted list (Section 1 below). Numbers I would have wanted to verify directly against the PDFs are flagged for Yurii's review (Section 3).

**Recommendation:** if Vadim has the PDFs locally, he can drop them into `workspace/seo/articles/2026-05-29-3dlook-accuracy-enterprise-evaluation/source-materials/` before Phase 3 (full draft) so the writer can re-check exact figures and methodology language. Not blocking Phase 2.

---

## 1. Vetted numbers — to use in the article

Every number below is on Vadim's approved list. Each row maps the number to its planned article section, the attribution language required, and whether it needs a hedge.

### A. Dataset scope (H2.2 / H2.4)

| # | Number | Use in article | Attribution required | Hedge required? |
|---|--------|----------------|----------------------|-----------------|
| 1 | 5,000+ participants | H2.2 Dimension 1, H2.4 methodology | "3DLOOK proprietary dataset" | Yes — internal scope |
| 2 | 150,000+ photographs | H2.4 methodology | "3DLOOK internal dataset" | Yes — internal scope |
| 3 | 30,000+ 3D scans | H2.4 ground-truth methodology | "ground-truth 3D scans captured for the 3DLOOK validation dataset" | Yes — internal scope |
| 4 | 430,000+ individual measurements | H2.4 methodology | "internal dataset" | Yes — internal scope |
| 5 | US/Europe geography | H2.2 Dimension 1 | "internal validation dataset spanning US and Europe" | Yes — disclosed scope limitation |
| 6 | Age 16–78, height 150–205 cm, weight 38–210 kg | H2.2 Dimension 1, H2.4 | "internal validation dataset demographics" | Yes — disclosed scope, NOT a "works for everyone" claim |
| 7 | Gender 48% male / 52% female | H2.2 Dimension 1 footnote | "internal dataset gender mix" | Yes |
| 8 | "Nearly a decade of R&D" | H2.4 framing | (no specific year) | Soft — temporal framing only |

### B. Performance metrics (H2.2, H2.3, H2.5)

| # | Number | Use in article | Attribution required | Hedge required? |
|---|--------|----------------|----------------------|-----------------|
| 9 | Measurement accuracy 96–97% | H2.2 Dimension 1 | "Internal validation against 3DLOOK's proprietary ground-truth dataset shows measurement accuracy of 96–97%" | **YES — strong hedge**. Never "96–97% accurate" standalone |
| 10 | Repeatability >95% across scan sessions | H2.2 Dimension 2, H2.5 | "Internal repeatability testing shows scan-to-scan consistency above 95%" | YES — strong hedge |
| 11 | Average weight prediction error 3.5% (±3% margin) | H2.3 Smart Scales output, FAQ | "Internal testing of Smart Scales weight estimation shows an average error of approximately 3.5%" | YES — hedged; mark as Smart Scales-specific |
| 12 | Smart Scales MAE 2.1 kg, SD 1.49, relative error 3.11% | H2.3 Smart Scales (briefly), FAQ | "Smart Scales internal testing: MAE 2.1 kg, SD 1.49 kg, relative error 3.11%" | YES — Smart Scales-specific, in beta context |
| 13 | BMI calculation 89% accuracy, 76% users within 5% deviation | H2.3 or FAQ | "Internal BMI accuracy testing: 89%; 76% of users within 5% deviation" | YES |

### C. Methodology specifics (H2.3, H2.4)

| # | Number / fact | Use in article | Attribution required | Hedge required? |
|---|--------|----------------|----------------------|-----------------|
| 14 | Two-photo guided capture, any background, fully clothed | H2.3 mechanism | Standard product description | No (factual) |
| 15 | ~30 second 3D model generation | H2.3, H2.4 | Product description | No |
| 16 | 80+ body measurements | H2.3 outputs | Product description (fingerprint phrase) | No |
| 17 | 86 anatomical parameters per person in dataset | H2.4 methodology | "86 anatomical parameters captured per participant in the validation dataset" | Yes — internal methodology |
| 18 | 4 dynamic cameras (hardware ground-truth setup) | H2.4 methodology | "ground-truth capture rig" | Yes |
| 19 | 34 photo configurations per user (Photo Flow Simulation) | H2.4 methodology | "Photo Flow Simulation across 34 capture configurations" | Yes |
| 20 | 1 million polygons with 1 mm accuracy per 3D model | H2.4 methodology | "ground-truth 3D models generated at approximately 1 mm spatial resolution" | Yes — describes 3DLOOK's internal benchmark setup, not the mobile scan output |
| 21 | Distance/angle/slope/lighting variations in Photo Flow Simulation | H2.4 | "varied capture conditions" | Yes |

### D. Body composition framework (H2.3, H2.6)

| # | Item | Use in article | Attribution required | Hedge required? |
|---|------|----------------|----------------------|-----------------|
| 22 | BMI formula: weight(kg) / height(m²) | H2.3 outputs | Standard formula reference | No |
| 23 | BMR formula: Mifflin-St Jeor | H2.3 outputs | Standard formula reference | No |
| 24 | Body Fat %: U.S. Navy formula | H2.3 outputs, H2.6 | "3DLOOK uses the U.S. Navy formula for body fat percentage estimation, selected through internal comparative evaluation of established anthropometric methods" | YES — never claim it's "validated" beyond internal eval; never compare numerically to Brozek |

### E. NCSU academic partnership (H2.2 Dimension 5, H2.4, H2.9)

| # | Item | Use in article | Attribution required | Hedge required? |
|---|------|----------------|----------------------|-----------------|
| 25 | NCSU / Wilson College of Textiles, 2022 | H2.2 Dimension 1 + Dimension 5, H2.4, H2.9 | "Through a 2022 collaboration with North Carolina State University's Wilson College of Textiles, the 3DLOOK dataset was expanded using the Size Stream Body Scanner for ground-truth 3D scans" | **CRITICAL HEDGE**: NEVER "validated by NCSU". Frame as "dataset expansion through academic collaboration" |
| 26 | Both casual and tight-fitting clothing | H2.4 | Methodology note | Yes |
| 27 | Multi-ethnic, multi-occupation metadata | H2.2 Dimension 1 | Dataset scope note | Yes — NOT a "works for everyone" claim |

### F. Real-world reliability features — all in production as of May 2026 (H2.2 Dimension 3, H2.8)

| # | Feature | Use in article | Attribution required | Hedge required? |
|---|---------|----------------|----------------------|-----------------|
| 28 | AI-driven skeletal tracking with real-time pose validation | H2.2 D3, H2.8 | "Production feature" — present tense OK (Vadim confirmed) | No |
| 29 | Red/green marker visual feedback | H2.8 | Production feature | No |
| 30 | Voice prompts for posture correction | H2.8 | Production feature | No |
| 31 | AI clothing detection (sport / regular / oversized) | H2.2 D3, H2.8 | Production feature | No |
| 32 | Garment-aware shape estimation corrections | H2.2 D3, H2.8 | Production feature | No |
| 33 | Face obfuscation for privacy | H2.8 | Production feature | No |

### G. Compliance (H2.8) — from Updated Security Privacy Slide Aug 2025

| # | Item | Use in article | Attribution required | Hedge required? |
|---|------|----------------|----------------------|-----------------|
| 34 | HIPAA compliance | H2.8 | "HIPAA-maintained for US healthcare contexts" | No (standard product framing) |
| 35 | GDPR principles | H2.8 | Standard framing | No |
| 36 | TLS encryption in transit | H2.8 | Standard framing | No |
| 37 | AWS S3 with SSE-S3 (always on) | H2.8 | Standard framing | No |
| 38 | Photo deletion: immediate or 30 days per client policy | H2.8 | Standard framing | No |
| 39 | Automatic blur on retained photos | H2.8 | Standard framing | No |
| 40 | No personal identifiers processed | H2.8 | Standard framing | No |
| 41 | Images never shared with third parties | H2.8 | Standard framing | No |
| 42 | `privacy@3dlook.me` for data deletion | H2.8 (or footer note) | Standard framing | No |

---

## 2. Numbers NOT to use (with reason)

| # | Item | Reason for exclusion |
|---|------|----------------------|
| N1 | Brozek vs Navy body fat MAE comparison (specific numbers) | **Vadim flagged: source presentation has error.** The article will say only "3DLOOK uses the U.S. Navy formula, selected through internal comparative evaluation of established anthropometric methods" — no MAE numbers, no Brozek comparison. |
| N2 | Any "clinically validated" / "clinical-grade" framing | Not clinically validated. Hard guardrail per brief. |
| N3 | "DEXA-equivalent" or "InBody-equivalent" | Different methodologies. Hard guardrail. |
| N4 | "Peer-reviewed" | No peer-reviewed publication on file. Hard guardrail. |
| N5 | "Third-party validated" (beyond NCSU dataset expansion) | NCSU partnership was dataset expansion, not independent validation. Hard guardrail. |
| N6 | "More accurate than DEXA / InBody / manual measurements" | Not a comparable measurement. Hard guardrail. |
| N7 | "Works for every body type / BMI / age / ethnicity" | Not a verified breadth claim. Hard guardrail. |
| N8 | "9 years of R&D" specific | Vadim noted "nearly a decade" is the current correct phrasing; "9 years" is outdated. |
| N9 | Any customer-pilot specific numbers (UK Meds, Yazen, etc.) | Not bariatric/accuracy article context; would also require fresh permission. Out of scope. |
| N10 | Any external academic study numbers (e.g., "published 2024 evaluations of mobile body measurement systems show waist circumference MAE near 1.88 cm" from the body-scanning-technology-comparison article) | This is NOT a 3DLOOK number — it's a third-party benchmark used in the comparison article. We do not import it into this pillar because the pillar is about 3DLOOK's own evidence, not external benchmarks. |

---

## 3. Numbers requiring Yurii (or other internal SME) verification before publish

These are numbers from Vadim's vetted list that I would normally cross-check against the source PDFs. The brief flags `yurii_review_required: true` in the frontmatter — the items below are the specific cross-check candidates Yurii should confirm.

| Priority | Number | Yurii check needed | Why |
|----------|--------|---------------------|-----|
| 1 (high) | Measurement accuracy 96–97% (item #9) | Confirm range is the current internally-documented figure as of May 2025 Technology Presentation PDF | Headline number — highest legal/buyer-trust exposure |
| 1 (high) | Repeatability >95% (item #10) | Confirm "across scan sessions" wording matches the PDF; confirm >95% is the documented threshold | Used in both H2.2 D2 and H2.5 |
| 1 (high) | Smart Scales MAE 2.1 kg / SD 1.49 / relative error 3.11% (item #12) | Confirm whether Smart Scales is positioned as "in beta" in the article or as production. Current draft framing assumes Smart Scales is described as a separate weight-estimation output | Smart Scales is the most technically detailed number in the article |
| 2 (med) | BMI 89% accuracy, 76% within 5% deviation (item #13) | Confirm both figures are current and refer to the same testing cohort | Used for BMI output context |
| 2 (med) | 86 anatomical parameters / 34 photo configurations / 1 million polygons (items #17, #19, #20) | Confirm these are current as of May 2025 Tech Presentation, not legacy May 2024 numbers | Methodology specifics — used to support the credibility of the ground-truth setup |
| 2 (med) | Dataset scope numbers — 5,000+ participants, 150,000+ photos, 30,000+ scans, 430,000+ measurements (items #1–4) | Confirm these are still current (Vadim said "nearly a decade" — dataset may have grown since May 2024 PDF) | Foundational credibility numbers |
| 3 (low) | Demographics — age 16–78, height 150–205 cm, weight 38–210 kg (item #6) | Confirm ranges have not narrowed/expanded since May 2024 | Minor — used as scope-limitation disclosure |

**Recommendation:** I'll draft on the brief's numbers in Phase 3, mark each yet-to-be-Yurii-confirmed number with `<!-- YURII CHECK: [item] -->` HTML comments so the post-draft review is straightforward, and surface the same list back to Vadim in Phase 5 (final metrics + compliance check). Vadim then routes to Yurii before publish.

---

## 4. Hedge-language inventory (lifted into one place)

Master hedge phrases to be used throughout the article, exactly as written here. Every internal performance number in the draft will sit inside one of these patterns:

| Pattern | Use when |
|---------|----------|
| "Internal validation shows…" | Lead-in to measurement accuracy figure |
| "Based on the 3DLOOK proprietary dataset…" | Dataset-scope context |
| "Performance evaluated through internal testing…" | Repeatability / Smart Scales / BMI |
| "Internal testing indicates…" | Softer-than-validation phrasing |
| "Different methodologies serve different purposes" | DEXA / InBody / smart scales comparison |
| "Within 3DLOOK's internal framework" | Body composition framing |
| "Through a 2022 collaboration with NCSU's Wilson College of Textiles, the dataset was expanded…" | NCSU framing — never "validated by NCSU" |
| "Not third-party validated, peer-reviewed, or clinically certified" | Direct disclosure (used in disclaimer + FAQ) |
| "Where direct comparative validation against a specific reference method has not been completed, 3DLOOK should not be positioned as equivalent to that method" | H2.2 D5 closing — the legal-defense-grade safe-wording line |

Banned phrasings to scan for in Phase 5:
- "validated as", "proven to be", "clinically", "DEXA-equivalent", "InBody-equivalent", "third-party validated" (without NCSU context), "peer-reviewed", "diagnostic", "works for every", "more accurate than DEXA/InBody/manual".

Also banned per CLAUDE.md §6 style: leverage, harness, robust, seamless, comprehensive, navigate (figurative), delve, tapestry, realm, "in today's…", "Furthermore / Moreover / Additionally" as sentence starters.

---

## 5. Open questions for Vadim before Phase 2

1. **PDFs locally available?** If Vadim has the three PDFs on his Windows drive, drop them into `workspace/seo/articles/2026-05-29-3dlook-accuracy-enterprise-evaluation/source-materials/` so the Phase 3 writer can cross-check figures one more time. Not blocking — happy to proceed without.
2. **Smart Scales positioning.** The brief lists Smart Scales metrics (MAE 2.1 kg etc.) under "Performance metrics" but does not specify whether to call Smart Scales "in beta" or "production." Default plan: describe it as a distinct **weight-estimation output** without "beta" framing unless Vadim says otherwise.
3. **H2.7 stance on competitor methods.** The brief says "different tools answer different questions" — confirm we should not name any product (DEXA, InBody, smart scales) negatively, and stay strictly in "different methodologies / different purposes" framing.
4. **NCSU phrasing — one specific sentence.** Brief says the safest phrasing is *"The technology was developed in collaboration with NCSU Wilson College of Textiles to expand the validation dataset"* (NOT "validated by NCSU"). Confirming I should use *that exact framing* anywhere NCSU appears, with the year (2022) and the Size Stream Body Scanner reference adjacent.
5. **Disclaimer length.** Brief provides a specific disclaimer block adapted for the accuracy context. Confirm we use it verbatim — not a tighter version. (My instinct says yes, use it verbatim, but flagging because it's a longer block than the bariatric article's disclaimer.)

---

## 6. Ready for Phase 2

Awaiting Vadim's approval on:
1. Vetted numbers table (Section 1) and attribution language plans
2. Numbers-NOT-to-use list (Section 2)
3. Yurii-verification list (Section 3) — confirm priorities
4. Hedge-language inventory (Section 4)
5. The 5 open questions in Section 5

Once approved, Phase 2 produces the 10-H2 outline with H3 subsections, data-point-to-section mapping, and internal-link map.
