---
phase: 4_self_critique_v2_asselya
article: 2026-06-10-ai-body-scanners-vs-dexa-rewrite
date: 2026-06-12
status: applied_inline_to_v2_draft_final
parent: v2-asselya/draft-final.md
revisions_applied: 12 inline editorial comments [a]–[l]
---

# Phase 4 — Self-critique of v2-asselya revisions

## 12 edits applied — verification table

| # | Comment | Resolution | Verified |
|---|---------|------------|----------|
| [a] | Add 8 SEO/keyword phrases once or twice | 7 of 8 woven naturally into body; "DEXA replacement" already present multiple times in v1 | ✅ each phrase 2-3 occurrences |
| [b] | Vary "body-data layer" with alternatives | 4 variants used: "remote tracking layer," "mobile measurement layer," "structured body-data workflow," plus the original "mobile body-data layer" kept where it's the central reframe phrase | ✅ |
| [c] | Disclaimer "not as a medical device" sounds like legal classification | Replaced with verbatim: "FitXpress is not positioned for diagnostic medical-device use in this workflow." | ✅ 1 occurrence in disclaimer; "not a medical device" eliminated |
| [d] | Add short-answer block after disclaimer | Added verbatim block as blockquote after disclaimer, before H2.1 | ✅ |
| [e] | "FDA-cleared as a medical imaging device" / "FDA-cleared medical imaging device" | Replaced both with "regulated clinical imaging equipment" | ✅ 0 "FDA-cleared" hits; 1 "regulated clinical imaging equipment" hit |
| [f] | "BMI inputs" → "BMI outputs" | Replaced in all 4 locations (H2.3 product description, H2.6 baseline bullet, H2.7 diagnostic section, FAQ Q1) | ✅ 0 "BMI inputs" hits; 4 "BMI outputs" hits |
| [g] | Move "Is FitXpress a DEXA replacement, alternative, or complement?" section right after the comparison table | Restructured: H2.4 (comparison table) → H2.5 (replacement/alternative/complement, central thesis) → H2.6 (hardware promoted to own H2 from H3) | ✅ Order verified at lines 81 → 97 → 134 |
| [h] | Replace rhetorical "DEXA answers / FitXpress answers" pair | Replaced with verbatim "DEXA can provide an imaging-based assessment point; FitXpress depicts what is changing between those points continuously." Kept the "The two outputs serve different roles in the same program:" lead-in for sentence rhythm | ✅ |
| [i] | "clinical-grade body composition" → "imaging-based or protocol-defined body composition assessment" | Replaced in H2.10 metabolic-clinics paragraph | ✅ |
| [j] | FAQ regulatory — safer formulation without FDA-scope reference | Replaced FAQ Q11 with verbatim safer wording. **H2.7 in-body still references the FDA General Wellness guidance with link** — the FDA mention stays in the explanatory section but is removed from the FAQ snippet (which is the form most often surfaced by AI answer engines and search snippets). | ✅ |
| [k] | "elite athletic testing" → "research or sports performance contexts" | Replaced in FAQ Q12. Merged into existing "research-grade body composition measurement" framing to avoid redundancy: "research or sports performance contexts requiring imaging-grade body composition measurement" | ✅ |
| [l] | Add new FAQ "Can mobile body scanning replace DEXA for body composition tracking?" | Added verbatim as 14th FAQ at end | ✅ |

**12/12 edits applied. Zero silent changes. Zero verbatim-replacement violations.**

## Structural change verification ([g])

v1 section order:
- H2.4: DEXA vs FitXpress (with table)
- H2.4 → H3: Where hardware body scanners fit
- H2.5: Replacement, alternative, or complement?

v2-asselya section order (per [g]):
- H2.4: DEXA vs FitXpress (with table)
- H2.5: Is FitXpress a DEXA replacement, alternative, or complement?
- H2.6: Where hardware body scanners fit (promoted to its own H2)
- H2.7: How FitXpress fits inside a GLP-1 or metabolic program
- (downstream sections renumbered accordingly)

Total H2 count: 13 (was 12 in v1 due to hardware being H3). Within style-guide §2 range (4-15).

## Compliance posture vs v1

| Risk vector | v1 status | v2-asselya status |
|---|---|---|
| "not as a medical device" implied legal classification | ⚠ Present in disclaimer | ✅ Replaced with workflow-specific framing per [c] |
| "FDA-cleared medical imaging device" for DEXA | ⚠ Asserted in two places | ✅ Replaced with "regulated clinical imaging equipment" per [e] — softer, factually accurate, doesn't claim specific FDA pathway |
| "BMI inputs" implies BMI is fed into the system | ⚠ Imprecise (Smart Scales generates weight which feeds BMI calculation, but BMI itself is an output) | ✅ "BMI outputs" — accurate per FX product spec |
| Rhetorical "DEXA answers / FitXpress answers" parallelism | ⚠ Risky — reads as marketing copy | ✅ Replaced with direct factual statement per [h] |
| "clinical-grade body composition" applied to DEXA | ⚠ Could imply FitXpress is below "clinical-grade" universally | ✅ Replaced with "imaging-based or protocol-defined" per [i] — describes the method, not its grade |
| FAQ regulatory FDA reference | ⚠ FAQ snippet could read as definitive regulatory positioning | ✅ Safer non-FDA-scope FAQ wording per [j]; H2.7 body still has the FDA reference for context |
| "Elite athletic testing" terminology | ⚠ Implies highest-tier use case | ✅ "Research or sports performance contexts" per [k] — broader, less hyperbolic |

## Editorial guardrails 11-point audit (v2)

| # | Guardrail | Status |
|---|-----------|--------|
| 1 | Claim substantiation — cut what you can't back | ✅ Mayo cut (v1), cost figures cut (v1), now also FDA-cleared softened to "regulated clinical imaging equipment" |
| 2 | One number everywhere the same | ✅ FX fingerprint (80+, ~45 sec, two-photo) consistent; "BMI outputs" now consistent across body and FAQ |
| 3 | "Independent" / "validated" / "third-party" reserved | ✅ 0 hits in body |
| 4 | Drop bare ">X%" without methodology | ✅ Zero FX performance percentages claimed |
| 5 | Honest caveats beat clean overclaims | ✅ Multiple "does not" lists |
| 6 | Medical/regulatory: "not positioned as," never "does not apply" | ✅ Strengthened in [c] — now "not positioned for diagnostic medical-device use" (more workflow-specific than the prior "not as a medical device") |
| 7 | Conditional language for boundaries | ✅ "depending on intended use, claims, jurisdiction, and implementation context" used in disclaimer + FAQ |
| 8 | Diligence register, not insider register | ✅ Rhetorical "DEXA answers / FitXpress answers" removed per [h] — register now neutral throughout |
| 9 | Concrete verticals up front | ✅ Telehealth, GLP-1, metabolic, weight-management, wellness, fitness named in intro + every applicable section |
| 10 | Structure defaults | ✅ Numbered lists, clean Markdown tables, bulleted disclaimer/scope blocks |
| 11 | When in doubt, flag — don't decide | ✅ Asselya's 12 inline comments addressed surgically; no silent edits beyond the 12 specified |

**11/11 guardrails passing.**

## Open items for Vadim

1. **Avg sentence length (22.6w)** unchanged from v1 — marginally over 22 ceiling. The new short-answer block ([d]) and the [h] rewrite did not move the needle. Acceptable per Phase 5 metrics tolerance.

2. **Body word count grew from 3,520 to 3,663** (+143) due to [d] short-answer block + [a] keyword insertions + [l] new FAQ. Still inside 3,500-4,200 sweet spot.

3. **FAQ count grew from 13 to 14** with [l] addition.

4. **No new editorial-guardrail violations introduced.** All 12 Asselya comments are tightenings, not loosenings.

**Recommended next steps:** route v2 to Vadim full read → if approved, generate publish-package and route to CMS as in-place update at the existing canonical URL.
