---
slug: 2026-09-03-manual-vs-digital-intake-occupational-health
kind: editorial-delta
compared: final.md revision 5, doc tab Version 3, against editorial-final-2026-09-11.md, doc tab Final version
date: 2026-09-11
rules: brand-assets/style-guides/editorial-rewrites.md
---

# What the editor changed between our revision 5 and the final

**Verdict on revision 5** (Assel Sekerova, relayed by Vadim on 2026-09-11): «в той версии мне не
нравилась длинна предложений, были повторения и читалось это всё как явно AI».

Revision 5 had passed `article_lint.py` (all nine gates) and `detect-ai-tells.py` (CLEAN, 0.86 per
1,000). Neither measured sentence length or repetition. The general rules drawn from this delta,
with before/after pairs, are in `brand-assets/style-guides/editorial-rewrites.md`. This file is
the article-specific record: provenance, numbers, how the open items were settled, and where the
final departs from repo canon.

## Provenance of the doc tabs

Similarity is word-sequence similarity against our `final.md` revision 5.

| Tab | What it is | Similarity to revision 5 |
|---|---|---|
| Version 3 | our revision 5 as uploaded | 0.98 |
| Version 4 | first editorial pass: privacy paragraph split, first H2 renamed, FAQ answer 2 rewritten | 0.91 |
| Version 5 | editorial rewrite | 0.43 |
| Final version | polish of Version 5 | 0.34 |

## Numbers

| | Revision 5 | Final |
|---|---|---|
| Prose words | 2,160 | 1,877 |
| Mean words per prose sentence | 17.7 | 14.7 |
| Sentences over 25 words | 13 of 93 | 3 of 94 |
| Sentences over 35 words | 6 | 1 |
| H2 sections | 10 | 9 |
| Comparison table rows | 14 | 11 |
| Metrics table | 8 rows | removed |
| FAQ questions | 4 | 3 |
| Lists with a serial comma / without | 3 / 23 | 24 / 2 |
| Visuals | one figure caption | Cover, Image 1, Image 2, plus an Illustrations tab |

## Structure, section by section

- **H1:** "…: Which Method Fits Which Workflow" became "…: A Workflow Comparison".
- **Intro:** the H2 "The intake step is where screening programs lose time" became "Where manual
  intake can slow occupational health screening". The list of four operational costs and the
  "Framed as … software preference" reframe are gone; the intro opens on the scene and closes on
  "The choice turns on two questions".
- **Scope note:** an italic blockquote became a bold-label paragraph. It now names FitXpress's
  part ("provides remote body-measurement capture") and ends "FitXpress is not a medical device."
- **Short answer:** five bullets stay five, with new labels: "What was moved before the visit?",
  "Effect on appointment time.", "How the methods differ."
- **Phases:** numbered list became bullets; the figure caption became `(Image 1) - Concept`. The
  opener "The comparison gets confusing when…" became "Occupational health screening consists of
  three phases."
- **Comparison table:** 14 rows became 11, with a bold header. The two paragraphs under it (one
  per review round, open item R2-1) became one paragraph of three sentences.
- **"How to evaluate the change" H2 was removed:** the eight-row metrics table, the two diligence
  questions and the vendor sentence became three sentences on how to pilot, inside the decision
  framework.
- **Decision framework:** prose became three H3s with bullets, "Manual intake fits when",
  "Digital intake fits when", "A hybrid model fits when". The EEOC paragraph grew into five short
  sentences (same inquiry for all entering employees, confidentiality, reasonable
  accommodations), and "It never decides a candidate." was cut.
- **New paragraph:** a disability limitation (see canon departures, item 3).
- **Where FitXpress fits:** `(Image 2) - Concept`; accuracy and repeatability in short sentences;
  the privacy paragraph in four sentences; the product link now sits on the anchor "FitXpress".
- **FAQ:** the EEOC question was removed (the body covers it). Question 2 is now "Which parts of
  occupational health screening remain on-site?" Answers are two or three sentences.
- **Next steps:** one sentence became two, the second starting "Then".
- **Links:** the hub is linked once (was twice); the accuracy framework twice; external NHANES,
  OSHA and EEOC once each.

## Review 2 open items, as the final settles them

- **R2-1**, the two adjacent reviewer paragraphs after the comparison table: merged into one.
- **R2-2**, "processes no personal identifiers": removed.
- **R2-3**, GDPR roles: kept as the canonical sentence, with "the" before controller and
  processor and GDPR spelled out.
- **R2-4**, retention: "retains generated outputs in accordance with the deployment terms" shipped,
  and the "immediately after processing or within 30 days, per client policy" window was dropped.

## Where the final departs from repo canon (decided by Vadim, 2026-09-11)

Decisions: (1) the direct medical-device form, everywhere; (2) and (4) `compliance.md` is not
changed for now; (3) the limitation is approved and added to product-info; (5) the keyword gate is
softened, the first paragraph is no longer required; (6) no change, the guardrail #3 note sits in
`accuracy-formulations.md` §5.

1. **Medical device.** Final: "FitXpress is not a medical device." Canon since 2026-09-02: "It is
   not positioned as a medical device." (`editorial-guardrails.md` #6, licensed by the detector).
2. **BAA.** Final: "A Business Associate Agreement under the Health Insurance Portability and
   Accountability Act (HIPAA) is available on request." `compliance.md`: "We sign BAAs for
   HIPAA-covered customers."
3. **Disability limitation**, not in `brand-assets/product-info/`: "FitXpress was not specifically
   trained on data representing people with physical disabilities, and its measurement
   performance has not been established for this population."
4. **Retention and personal identifiers** (R2-2, R2-4 above) against `compliance.md` and
   `proof-points.md`, which still state both.
5. **Primary keyword in the first paragraph.** The final keeps it in the H1 and one H2 only.
   `article_lint.py` gate 7 asks for the first paragraph too, so it fails on the final.
6. **"Internal"** is dropped from both studies ("Repeatability testing…", "A separate
   validation…"). Guardrail #3 prefers naming it internal.

## Illustrations (doc tab "Illustrations", verbatim)

| Name | Placement | Concept |
|---|---|---|
| Cover | Top of the article | A restrained comparison of clinic-based intake and pre-appointment digital capture, without reproducing the detailed workflow diagram. |
| Three phases of occupational health screening | After the section introducing the three phases | Show pre-appointment intake, on-site screening and clinical review. Highlight that only eligible intake activities move before the visit. |
| From guided capture to structured results | In "Where FitXpress fits" | Show the two-photo smartphone capture leading to body measurements, calculated BMI and a session timestamp. Keep clinical interpretation and employment decisions outside the product flow. |

> I would remove the other proposed visuals:
> - The manual-versus-digital comparison would repeat the main table.
> - The method-selection illustration would repeat the manual, digital and hybrid guidance.
> - The alternative measurement path is important, but one paragraph or a small callout is sufficient.
> - The validation figures can appear as a compact evidence panel within the FitXpress visual instead of becoming a separate illustration.

## Gates on the final

- `detect-ai-tells.py` reported a HARD FAIL on `robustness`, which is dimension 3 of the canonical
  accuracy framework ("Real-world robustness", `accuracy-formulations.md` §1.6). The pattern was
  narrowed to `robust` / `robustly` on 2026-09-11.
- `claim traceability` fails because the editor's text carries no claim markers. Expected for this
  file; it is a record, not a pipeline draft.
- `keyword placement` failed on the first paragraph (canon departure 5); after the 2026-09-11
  softening of gate 7 it passes.
- New gate `sentence length`: PASS (14.7 mean, 3.2% over 25 words, 1 over 35). Revision 5 fails it.
