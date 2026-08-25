# FitXpress Product Marketing Playbook — deck handoff

**Artifact:** `FitXpress-Product-Marketing-Playbook-Nika.pptx` (61 slides, 16:9, 216 KB)
**Built from:** `fitxpress-marketing-playbook-nika.md`
**Structured after:** `FitXpress_Sales_Playbook_June 2006` (Google Slides, Katerina's Drive sales folder)
**Generator:** `build_nika_deck.py` (re-run it to rebuild after any edit to the source markdown)

---

## Getting it into Drive as Google Slides

The Google Drive connector available to the automation can only create files from **inline**
content, and a 61-slide deck is 216 KB of binary (294,460 base64 characters), which cannot be
passed through a tool parameter. So the conversion is a manual one-step import:

1. Open the sales folder:
   `https://drive.google.com/drive/folders/1UdeWy90iiTVzHrLPsmOyYqM0wl3l_BlO`
2. Drag `FitXpress-Product-Marketing-Playbook-Nika.pptx` into it (or **New → File upload**).
3. Right-click the uploaded file → **Open with → Google Slides**.
4. In Slides: **File → Save as Google Slides**. Delete the leftover `.pptx` afterwards.

Google converts shapes, tables, gradients and text faithfully. Alternative home if you would
rather keep the root folder for sales material only: the existing
**`Marketing docs & Decks`** subfolder (`1ulCBEN_-aaXwCT1RM2EmUmRPSLOKyqAJ`). The root is the
better match for parity with the sales playbook, which also sits there.

---

## Fonts

Both the theme fonts and every run declare **Satoshi**, per `DESIGN.md`. Satoshi is a Fontshare
face and is not in the Google Fonts library, so Google Slides will substitute a fallback on
screen while preserving the declared typeface. To render it properly, install Satoshi locally
and use the **Extensis Fonts** add-on, or export to PDF from a machine that has the font.
`DESIGN.md`'s own fallback stack is `'Satoshi','Inter',system-ui`.

---

## Structure (9 sections, mirroring the markdown)

| Slides | Content |
|---|---|
| 1 to 3 | Cover, What's Inside, and the proof-points.md rule as a four-step flow |
| 4 to 8 | **01 Role and scope**: what Nika owns vs what routes elsewhere, the team, asset locations, first two weeks |
| 9 to 15 | **02 Brand and voice**: positioning, the voice, claims discipline table, repeatability vs accuracy, banned language, the nine disclaimer patterns |
| 16 to 19 | **03 Design system**: colour swatches and both ten-step scales, type scale, spacing and radius, do and don't |
| 20 to 33 | **04 Use-case library**: the boundary rule, the proof tiers, an eleven-segment matrix, then one slide per segment |
| 34 to 39 | **05 Deck playbook**: the 60/40 principle, design rules, the 19-slide core across two slides, the ten-step localization flow |
| 40 to 46 | **06 Landing-page playbook**: the four gates, the 17 slots across two slides, FAQ, CTA by funnel stage, pre-launch checklist |
| 47 to 53 | **07 Messaging and proof**: hero lines, the approved proof set across two slides, compliance and citation rules, objections |
| 54 to 57 | **08 QA checklist**: claims and voice, disclaimers and design and conversion, structure and sign-off |
| 58 to 60 | **09 Open items**: the four ranked blockers, then the twelve corrections |
| 61 | Close, with the five approvers |

---

## Checks that were run against the deck copy

- **Numbers.** Every figure traces to section 7.3 of the source markdown, which is itself copied
  from `proof-points.md`. The ISO 0.40 cm benchmark is shown as *pending and unusable* rather
  than as proof, per open item 2.
- **Em and en dashes:** 0 occurrences.
- **Banned words:** present only where the deck is quoting the ban list, the anti-positioning
  list or open item 9. No banned word is used as copy.
- **`detect-ai-tells.py --channel page`:** density 3.18 per 1,000 against a budget of 6.0. All 49
  reported hard fails are the ban-list and "Never claim" slides quoting the terms they prohibit;
  `the audience` is a false positive on the filename `audience.md`.
- **Layout:** a text-fit estimator in the generator measures every text box before rendering and
  scales the point size down to a floor of 80% to keep copy inside its box. Zero overflow
  warnings. A geometry pass confirms no shape leaves the canvas or crosses into the footer band.
- **Archive integrity:** zip CRC check passes; 61 slide parts present.

---

## Things a reader should know

- `#2962FF` is deliberately absent. The deck uses `#143DFF` and flags the superseded placeholder
  as open item 1, matching the source markdown.
- Slide 33 (BCRL) carries a deliberately **grey, non-committal hero band** instead of the navy
  outcome band, because that segment has no writable hero outcome. That is content, not a
  styling slip.
- The navy zones use a radial gradient with a measurement-grid texture per `DESIGN.md`. If
  Google Slides simplifies the radial path on import, it degrades to a blue-to-navy gradient,
  which is still on-brand.
- Client logos, product renders and the guided-capture UI are **not** embedded. `DESIGN.md` asks
  for product imagery over icons, and the brand-mark asset kit is not in the repo (section 3.7
  logo caveat). Those slots are left clean for a designer.
