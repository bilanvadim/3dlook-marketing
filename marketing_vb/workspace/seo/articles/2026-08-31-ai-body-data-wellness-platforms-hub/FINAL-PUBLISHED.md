---
status: published
slug: ai-body-data-wellness-platforms
published_date: 2026-09-14
modified_date: 2026-09-17
published_url: https://3dlook.ai/content-hub/ai-body-data-wellness-platforms/
final_source_file: published-live-2026-09-21.md
draft_submitted: final.md (revision 3) → superseded by final-google-doc.md (revision 6, editors' Google Doc)
author: Assel Sekerova
product: fitxpress
hub: "AI Body Data"
cluster: Wellness Platforms (Hub #8)
verified_against_live: 2026-09-21
divergence: live = Google Doc rev 6; pipeline rev 3 is history
---

# FINAL PUBLISHED VERSION

**The live page is the editors' Google Doc (revision 6), not the pipeline's revision 3.**
Word-level similarity to the live body: `final-google-doc.md` **0.94**, `final.md` **0.11**.
So `publish-package.md` / `final.md` are in-flight history. Treat
`published-live-2026-09-21.md` as the text of record. `social_pack.py resolve_source` ranks
`published-live-*` first, so the social pack (job #161, 2026-09-21, `--batch`) reads it.

| Field | Value |
|---|---|
| **Live URL** | https://3dlook.ai/content-hub/ai-body-data-wellness-platforms/ |
| **Published / updated** | 2026-09-14 / 2026-09-17 (captured 2026-09-21) |
| **Byline** | Assel Sekerova |
| **H1** | AI Body Data for Wellness Platforms: Progress Tracking, Personalization, and Engagement |
| **Meta title (live)** | AI Body Data for Wellness Platforms \| 3DLOOK — as the package recommended ✅ |
| **Meta description (live)** | "AI body data gives a wellness platform a repeatable progress signal, supporting personalization & engagement. See what to evaluate." — the editors' own text, not one of our three variants |
| **Word count** | live ~1,870 · Google Doc rev 6 ~1,980 · pipeline rev 3 ~3,030 |

## Structure

The live headings match the Google Doc rev 6 exactly. The only rename is
"Turning comparison into a useful wellness **platform** experience". The FAQ ships as an
accordion (FAQPage schema present). "Where to go next" became a "Further reading" link list.
Rev 3's summary table, "Practical wellness-platform workflow" and "What to evaluate in a
body-data provider" sections do not exist on the live page.

## Numbers on the live page (all present in the Google Doc)

- 96–97% overall accuracy vs expert manual measurement, typical error 1.5–2.0 cm (internal validation)
- Evaluated population: ages 16–78, 150–220 cm, 38–210 kg, US + Europe
- Two photos (front + side) → 80+ measurements, BMI, BMR, body fat %, lean/fat mass, 3D model, under 45 seconds
- Storage: Amazon S3, mandatory SSE-S3. Photos are removed immediately after processing or
  within 30 days per client retention, and retained photos are auto-blurred

## Defects on the live page

- ~~The FAQ link "3DLOOK accuracy and privacy framework" points to
  `/content-hub/mobile-body-scanning-accuracy/?utm_source=chatgpt.com`~~ — **fixed by Vadim
  2026-09-21** (live page modified 08:52 UTC, verified: bare URL, no `utm_source` left).

## Capture history

The first capture (08:28 UTC, which the social pack was drafted from) flattened the FAQ
accordion into `********…********` runs glued to the previous paragraph. `capture-live.py` was
fixed the same day, and the file was re-captured with `--force` after Vadim's link fix
(page modified 08:52 UTC). The text is the same as what the drafter read. What changed: the FAQ
is now `## FAQ` + `### question`, "Further reading" is a list, and the FAQ link goes to the
trust FAQ (`/fitxpress-data-privacy-security-regulatory-faq/`). The pack still lints 9/9
against it.
