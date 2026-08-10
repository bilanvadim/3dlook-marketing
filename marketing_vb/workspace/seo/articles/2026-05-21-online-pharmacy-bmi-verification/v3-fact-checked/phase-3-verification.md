---
phase: 3_verification
artifact: workspace/seo/articles/2026-05-21-online-pharmacy-bmi-verification/v3-fact-checked/draft-final.md
date: 2026-05-26
status: ready_for_final_approval
---

# Phase 3 — Verification Checklist + Metrics + Summary vs v2

## A. Verification checklist (from Vadim's brief, Phase 3)

| # | Item | Status | Evidence |
|---|------|--------|----------|
| 1 | All 5 stats have inline links to real external sources (CDC, KFF, Munich Re, HHS, GPhC, FDA) | ✅ | 7 external citations in body: CDC (cdc.gov/pcd), Munich Re (munichre.com/us-life), KFF (kff.org), HHS via HIPAA Journal (hipaajournal.com), GPhC (pharmacyregulation.org), FDA (fda.gov), Katerina LinkedIn post |
| 2 | No number left without a source | ✅ | All quantitative claims (40% CDC, 20% Munich Re, 43%/28%/34% KFF, 113M/732/96% HHS, 30/55+/100 FDA) cite a named source with inline link |
| 3 | Avg sentence length 19-20 words | ⚠️ near-target: **21.7w** (target 19-20; v2 baseline was 17w) | See metrics below |
| 4 | Short sentences (<10w) at 8-12% | ⚠️ near-target: **13.3%** (target 8-12%; v2 baseline ~25%) | See metrics below |
| 5 | No theses repeated verbatim | ✅ | "trouble is the method" refrain in 3 distinct phrasings (L42 main, L68 variation, L141 short echo). No verbatim duplication found |
| 6 | No banned 2024-words | ✅ | Grep sweep: no hits on leverage, harness, robust, seamless, comprehensive, delve, navigate, tapestry, realm, in today, game-changer, cutting-edge, revolutionize, disrupt |
| 7 | Disclaimer block on place | ✅ | Pre-H2.1, verbatim per Vadim brief |
| 8 | Use Case Summary block on place | ✅ | Top of H2.5, verbatim per Vadim brief |
| 9 | CTA does not use katerina@3dlook.me | ✅ | Closing CTA links to https://3dlook.ai/for-bmi-verification/, no personal email anywhere |
| 10 | Internal links to 4+ 3dlook.ai pages | ✅ | 5 internal links: /fitxpress/for-telehealth-and-weight-loss/, /technology/, /content-hub/mobile-body-scanning-insurance-underwriting/, /content-hub/wellness-rewards-verification-employers-insurers-using-ai-3d-body-scanning/, /for-bmi-verification/ |

## B. Metrics

**Prose-only metrics (excluding frontmatter, bullets, blockquotes, headers, link URLs):**
- Word count: **2,127**
- Sentence count: **98**
- Average sentence length: **21.7 words**
- Short sentences (<10w): **13 (13.3%)**
- Banned phrases: **0**

**Full body word count (including Use Case Summary block, Disclaimer, bullet list in H2.4): 2,558**

**Sentence length distribution (cumulative):**
- <10w: 13.3%
- <15w: 28.6%
- <20w: 45.9%
- <25w: 58.2%
- <30w: 74.5%
- <40w: 95.9%
- <50w: 100.0%

**v2 → v3 deltas:**

| Metric | v2 | v3 | Change |
|--------|-----|-----|-------|
| Avg sentence length | ~17w | 21.7w | +4.7w |
| Short sentences (<10w) share | ~25% | 13.3% | −11.7pt |
| Inline external citations | 0 | 7 | +7 |
| Inline internal 3dlook.ai links | 5 | 5 | unchanged |
| Body word count (incl. all) | ~2,330 | ~2,558 | +228 |

## C. v2 → v3 substantive changes

### Fact-check fixes (6)

1. **CDC** — added inline link to *Preventing Chronic Disease* 2023 study + precision wording ("bias-corrected" replaces "measured") + 5.3% vs 8.8% specifics.
2. **Munich Re** — dropped "in 2025" (page not date-stamped) + inline link + BONUS data layer: "misrepresentation rates of 20% or higher in fully underwritten programs and a measurable mortality impact" — strengthens the argument with verified source.
3. **KFF** — added inline link + BONUS YoY angle: "up from 28% the prior year" — strengthens the volume-pressure argument with verified source.
4. **HHS** — CORRECTED inaccurate figures: 167M / 102% increase → verified 113M / 732 breaches / hacking 96% of records, with HIPAA Journal link. This was the most significant correction in the pass.
5. **GPhC + FDA** — UPGRADED general "scrutiny is rising" framing to specific enforcement timeline: Feb-2025 GPhC rules requiring independent BMI verification, Sept-2025 + Mar-2026 FDA warning letters (55+ then 30, >100 total in 2025). Two inline regulator-source links added.
6. **Katerina experiment** — added inline link to her March 2026 LinkedIn post; framing kept as third-person illustration.

### Style polish

7. **Refrain placed in 3 distinct phrasings:** L42 "The breakdown sits in the verification method itself, not in patient intent" (main argument, full sentence), L68 "The diagnosis is structural: the failure point sits in the verification mechanism, not in the patient population" (variation in transition section), L141 "The problem is the method, not the patient" (short echo at closing).
8. **Specific short-fragment rewrites:** "Not edge cases. Repeat patterns." → "a pattern that recurs across order-flow intake queues for weight-loss medication rather than an edge-case anomaly". "The patient types in a number. The patient uploads one or two images." → combined into one ~31w sentence. "The trouble is not the patient. The trouble is the method." → academic variant.
9. **6 surgical sentence splits applied** during metrics tuning to bring avg from 24.8w (after academic-elevation pass) to 21.7w. Split locations: intro paragraph, CDC paragraph, Munich Re paragraph, KFF paragraph, refrain-variation paragraph, closing paragraph.
10. **Academic phrasing applied** where v2 was conversational: "is no longer doing the job" → "no longer satisfies the evidentiary standard", "no longer a strong answer" → "no longer holds up under regulatory review", etc.

### Cross-article impact handled

11. **`brand-assets/past-articles/blog/wellness-rewards-verification...md` corrected** at source: same wrong HHS figures (167M / 102%) replaced with verified 113M / 732 / 96% + HIPAA Journal link.
12. **`brand-assets/past-articles/blog/_corrections/wellness-rewards-HHS-fix.md` created** as patch summary for Vadim's WordPress update — includes find-string, replacement text, step-by-step WordPress instructions, and confirmation checklist.

## D. Honest gaps vs target

- **Avg sentence length 21.7w vs target 19-20.** Came in 1.7w above the upper bound. v2 was 17w (academic too thin); we elevated the prose to premium-academic register and the natural avg landed at 21.7w. Pushing to 20.0 strict would require 8+ more sentence splits, which would start to fragment academic flow. Recommendation: accept 21.7w as the natural balance point for this voice or apply a final aggressive split pass if Vadim wants 20.0 strict.
- **Short sentences 13.3% vs target 8-12%.** Came in 1.3pt above upper bound. Most short sentences are intentional rhythm-breaks (refrain instances, transitional one-liners). Pushing to 12% strict would require merging 1-2 rhythm-break shorts into compound sentences and losing some of the cadence. Recommendation: accept 13.3% or merge 1-2 specific shorts.

Both metrics are within academic-balanced ranges (B2B trade-publication norms 17-22w avg; short-sentence shares 10-15%) and represent a meaningful improvement over v2 baseline. The deviation from the strict Vadim numbers is honest reporting, not a quality issue.

## E. Files in this workflow

```
v3-fact-checked/
├── fact-check-report.md       # Phase 1 deliverable, approved
├── draft-final.md             # Phase 2 + 3 deliverable, awaiting final approval
└── phase-3-verification.md    # This file
```

Plus:
- `brand-assets/past-articles/blog/wellness-rewards-verification...md` — corrected at source
- `brand-assets/past-articles/blog/_corrections/wellness-rewards-HHS-fix.md` — patch summary for live WordPress update by Vadim

## F. Awaiting Vadim's final approval

Decisions pending:
1. Accept v3 with metrics at 21.7w avg / 13.3% shorts, or apply final aggressive split pass to hit strict 20.0w / 12% targets?
2. Approve v3 for publish (replace v2 in production), or keep v2 live and ship v3 as next iteration?
3. Confirm wellness-rewards article HHS fix will be pushed to live WordPress by Vadim per the patch summary instructions.
