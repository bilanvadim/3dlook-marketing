---
status: published
slug: manual-vs-digital-intake-occupational-health-screening
published_date: 2026-09-21
modified_date: 2026-09-21
published_url: https://3dlook.ai/content-hub/manual-vs-digital-intake-occupational-health-screening/
final_source_file: published-live-2026-09-21.md
draft_submitted: final.md (revision 5, doc tab "Version 3") → superseded by editorial-final-2026-09-11.md (doc tab "Final version")
source_doc: https://docs.google.com/document/d/14y0xQ5MbrM6Xb56gdNVDYa6LfWoy451D5bdfIaYW668/edit?tab=t.argfqjgqdt2t
author: Assel Sekerova
product: fitxpress
hub: "Occupational Health Screening (content-plan Hub 8, inventory #11)"
cluster: comparison / GEO / MOFU
verified_against_live: 2026-09-21
divergence: live = editor's final of 2026-09-11 almost verbatim; pipeline revision 5 is history
---

# FINAL PUBLISHED VERSION

**The live page is the editor's final (`editorial-final-2026-09-11.md`), not the pipeline's
revision 5.** Word-level similarity to the live body: `editorial-final-2026-09-11.md` **0.965**,
`final.md` (revision 5) **0.37**, `publish-package.md` **0.17**. `final.md`,
`publish-package.md`, `v1/` and `v2/` are in-flight history. Treat
`published-live-2026-09-21.md` as the text of record. `social_pack.py resolve_source` ranks
`published-live-*` first, so a social pack reads it without further setup.

| Field | Value |
|---|---|
| **Live URL** | https://3dlook.ai/content-hub/manual-vs-digital-intake-occupational-health-screening/ |
| **Published / updated** | 2026-09-21 08:58 / 09:09 UTC (captured the same morning) |
| **Byline** | Assel Sekerova (JSON-LD: "Asselya Sekerova") |
| **H1** | Manual vs Digital Intake in Occupational Health Screening: A Workflow Comparison |
| **Meta title (live)** | Manual vs Digital Intake in Occupational Health Screening, which is the package's variant 1 ✅ |
| **Meta description (live)** | "Manual vs digital intake in occupational health screening, compared step by step: workflow, cost, exceptions & the metrics to test." This is variant 1 with "and" → "&" and "before switching" cut |
| **Canonical** | self ✅ · in `post-sitemap.xml` ✅ (161 URLs on 09-21) · FAQPage schema ✅ (3 Q&A) |
| **Word count** | live ~1,970 incl. tables and related reading · editor's final 1,877 prose · revision 5 2,160 prose |

## What changed between the editor's final and the live page

- Intro: "whether moving them addresses" → "whether moving them **would** address"; the hub link's
  anchor lost the word "hub" ("occupational health screening software").
- "Next steps" moved **above** the FAQ, and a "Related reading" list was added under it: the
  occupational-health hub and the main health hub (`ai-body-data-health-hub`).
- "Frequently asked questions" → "FAQ" (Yoast accordion).
- The doc's "(Cover) / (Image 1) / (Image 2) - Concept" placeholders became real images, which the
  capture drops.

Everything else, including the tables, the numbers, the scope note and the disability limitation,
is the editor's text word for word. The Review 1 and Review 2 decisions only reach the live page
where the editor kept them. `editorial-delta-2026-09-11.md` records what she changed from
revision 5.

## Defects and gaps on the live page

- **Comparison table row typo:** "Set up an ongoing effort" should read "Set-up and ongoing
  effort". It came from the editor's doc and went live unchanged.
- **No link to the trust FAQ.** The privacy paragraph in "Where FitXpress fits" does not link
  `fitxpress-data-privacy-security-regulatory-faq/`. Content Plan v2.0 asks every vertical privacy
  section to link it.
- **Privacy wording departs from `compliance.md`,** as it already did in the editor's final. Vadim
  left `compliance.md` unchanged on 2026-09-11. The live page says "A Business Associate Agreement …
  is available on request", while canon says a BAA is available "for qualifying enterprise
  deployments". The live page says "deletes photos after processing", while canon says
  "immediately after processing, or within 30 days" per the customer's instructions. Posts should
  quote `compliance.md`, not this paragraph.
- **The primary keyword is not in the first body paragraph** (open since 2026-09-11). It is in the
  H1, the meta title and the deck line.

## Capture note

The scope note is `<strong><em>Scope note.</em></strong><em> Digital intake…</em>` in the HTML,
which `capture-live.py` renders as `***Scope note.**** Digital intake…*`. The text is complete; only
the emphasis markers look odd.
