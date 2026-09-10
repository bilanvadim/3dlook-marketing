---
status: published
slug: remote-body-measurement-online-fitness-coaching
published_date: 2026-09-04
published_url: https://3dlook.ai/content-hub/remote-body-measurement-online-fitness-coaching/
final_source_file: published-live-2026-09-04.md
draft_submitted: draft-v4-revision2.md
author: Assel Sekerova
product: fitxpress
hub: "AI in Fitness"
cluster: Digital Coaching
action_type: net-new
verified_against_live: 2026-09-10
divergence: substantial-rewrite
---

# FINAL PUBLISHED VERSION

**The live page is not the text we shipped.** Structure, claims and numbers survived; the prose was
rewritten end to end by the editorial side before publication. Treat
`published-live-2026-09-04.md` as the text of record and `draft-v4-revision2.md` /
`publish-package.md` as in-flight history. `social_pack.py resolve_source` already ranks
`published-live-*` above the package, so the social pack picks the live text automatically.

| Field | Value |
|---|---|
| **Live URL** | https://3dlook.ai/content-hub/remote-body-measurement-online-fitness-coaching/ |
| **Published** | 2026-09-04 (captured 2026-09-10) |
| **Author (byline on site)** | Assel Sekerova |
| **Title (live H1)** | Remote Body Measurement for Online Fitness Coaching Programs |
| **Meta title (live)** | Online Fitness Coaching Programs: Remote Body Measurement |
| **Target keyword** | remote body measurement / online fitness coaching programs |
| **Word count** | live body ~2,560 · submitted draft 2,644 |
| **Categories on site** | Blog › Fitness, Technology |

## Meta: shipped as recommended

- **Title** — byte-identical to the package recommendation (57 chars, no `| 3DLOOK` suffix). ✅
- **Description** — one edit: our final `…and what a pilot should measure.` became
  `…& what it should measure` (ampersand, "pilot" dropped, no closing period). Cosmetic, keyword-neutral.
- **Slug and URL** — exactly as recommended, in the hub pattern. ✅

## What survived

Section-by-section the live page is a 1:1 map of the approved outline. Eleven H2s in the drafted order,
both comparison tables intact with the same row set, all five FAQ items, the scope note in the intro, the
non-medical-device disclaimer, and every number we cleared:

- 80+ model-generated measurements · under 45 seconds · five output categories
- Smart Scales ~3.5% average prediction error, still labelled software-predicted, not a physical scale
- 96–97% agreement vs expert pattern-maker manual measurement, typical absolute error 1.5–2.0 cm
- Scan-to-scan repeatability under 1 cm for most evaluated measurements
- Photos deleted immediately after processing or retained up to 30 days at the business client's
  instruction, retained photos auto-blurred
- HIPAA / GDPR posture, encryption in transit and at rest

Three headings were renamed, all cosmetically:

| Draft | Live |
|---|---|
| How it fits the coaching workflow | How remote body measurement fits the coaching workflow |
| Implementation | Implementation considerations |
| What FitXpress does not do | FitXpress scope and limitations |

The FAQ moved out of the body into an accordion at the end of the page and is emitted as valid
FAQPage schema (5 Question / 5 Answer nodes). Article, BreadcrumbList, Person and Organization
schema are all present.

## What the editorial pass changed

**1. Register.** This is the big one. Every paragraph was re-registered from the specific, human voice
review 2 asked for into product-documentation prose — mostly passive, mostly nominalised. Examples:

> **Draft:** Managing a large remote roster means nobody is in the room to put a tape measure around a
> client's waist, and the measurement still has to happen.
> **Live:** Online fitness coaching programs need a consistent way to collect body measurements when
> clients and coaches are in different locations.

> **Draft:** A coach adjusting a program at week eight needs both records to have been made the same way.
> A tape held half an inch higher can produce an apparent difference caused by placement rather than body change.
> **Live:** Comparability depends on consistent devices, timing, pose, framing, clothing, and technique.
> Circumferences vary with tape placement and tension.

> **Draft:** The better question is narrower: accurate enough for which decision?
> **Live:** Accuracy requirements depend on the intended decision, reference method, capture protocol,
> population, and acceptable error.

The anti-AI-tells work from revision 2 does not survive this. It is worth re-running
`brand-assets/style-guides/scripts/detect-ai-tells.py` on `published-live-2026-09-04.md` before the next
article in this hub, because the live page — not our draft — is what the next reviewer will read as
"how 3DLOOK writes."

**2. One external source swapped, correctly.** Our BIA citation was PMID 32182203 (Libyan J Med, 2020 —
140 subjects, four successive 500 mL water intakes, fat mass overestimated 2.08–7.92% in males and
3.4–9.4% in females). The live page cites PMID 30297760 instead (Eur J Clin Nutr, 2019 — *BIA for body
composition assessment: reflections on accuracy, clinical utility, and standardisation*) and describes it
as "a review of BIA accuracy and standardization." **Verified against PubMed: the new anchor text matches
the new PMID.** The DXA citation (PMID 25029265, IJSNEM methodology review) is unchanged and still
correctly described. No mis-cited source on the live page — but the specific hydration numbers are gone,
so the BIA paragraph is now qualitative where ours was quantitative.

**3. Cut from the draft:**
- Model-maturity block — 9+ years of training data, 150K+ photos, 30K+ 3D scans, 430K+ measurements.
  This was our technical-diligence proof and it is not on the page anywhere.
- AWS as the named hosting infrastructure.
- Buyer personas by title (CEO / CPO / head of growth / CTO) — replaced by "business, product, coaching,
  privacy, and technical stakeholders."
- "Corporate wellness delivered to distributed employees" as a use case — replaced by "time-bound remote
  fitness programs."
- The hydration study numbers (see above).

**4. Added on the page:**
- **Accuracy population disclosure**, which we did not have: ages 16–78, heights 150–220 cm, weights
  38–210 kg, participants from the US and Europe, with "populations outside that scope require separate
  evaluation." This is a genuine improvement — reuse it in the next accuracy section.
- A mid-article eBook CTA (*The Digital Health Revolution*) after "How coaches can use the results."
- A numbered table of contents, share widget, author bio, and a "Further reading" block.
- Internal links grew from 5 to 8 in-body (added `ai-body-scanning-for-fitness`,
  `fitxpress-privacy-policy`, the eBook), plus the site's own related-posts rail.
- Explicit SDK/API paragraph in the workflow section (mobile/web SDK embeds capture, API submits scans
  and retrieves results).

**5. Softened.** "A calibrated scale remains the right instrument where a precise weight matters" became
"A connected or calibrated scale provides a direct weight reading." Several other competitive-honesty
lines lost their edge the same way.

## Consequence for the social pack

Posts are written from `published-live-2026-09-04.md`. Two things follow:

- The **model-maturity numbers and the hydration-study numbers are not linkable** to the live article.
  If a post wants them, they need a different source in `proof-points.md` or they do not ship.
- The **population disclosure** (16–78 years, 150–220 cm, 38–210 kg, US/Europe) is new, on-page, and is
  the strongest specific in the accuracy section. It is a good angle for the technical profiles.

## Files

| File | What it is |
|---|---|
| `published-live-2026-09-04.md` | **Text of record.** Live body, H1 to Further reading, captured 2026-09-10. |
| `.published-live-2026-09-04.html` | Raw page source behind that capture. **Local only, not committed** — no other article keeps its HTML in git; re-fetch from the live URL if it is ever needed again. |
| `publish-package.md` | What we submitted (revision 2). History. |
| `draft-v4-revision2.md` | Final approved draft. History. |
| `review1-*` / `review2-*` / `changelog-*` | Review rounds. History. |
