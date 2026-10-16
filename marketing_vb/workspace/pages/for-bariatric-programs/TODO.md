---
product: fitxpress
type: vertical-page
vertical: bariatric
status: draft-v2
---

# TODO: bariatric landing v2 (`page-v2-2026-10-16.html`)

## Blockers before publishing

1. **Pricing unit.** The page prices in API requests (decision 2026-10-16). The live `/pricing/` still
   says "Up to 500 scans per month". Publish together with the new pricing page, or re-read `/pricing/`
   on the day it ships.
2. **Weight limits (product).** The public API accepts entered weights of 40-200 kg; the validation
   population covered 38-210 kg. Bariatric patients above 200 kg cannot enter their weight. Confirm the
   deployment limit and add it to the higher-weight FAQ. It is not on the page yet: the API documentation
   is not a `proof-points.md` source (round-2 judge hard fail), so the confirmed limit goes into
   `proof-points.md` first.
3. **Smart Scales status (product).** `tech-spec.md` labels it beta, and the page says "(beta)" in the
   record table, the pre-qualification block and the queue mock. The live `/pricing/` lists "Predicted weight" with no label. If it is no
   longer beta, drop the label everywhere at once.

## Placeholders (search `[PLACEHOLDER]`)

- Logo row: add the logos of all clients from design (kit rule, caption stays "100+ clients have used
  3DLOOK body scanning since 2016."). Alt text = client name.
- Form: swap `formConfig.formId` for the shared `FX | LP | Demo` form (comment in the script).

## Wording to confirm

- **Asselya:** H1 "Bariatric patient tracking with FitXpress…" uses the focus keyphrase. CLAUDE.md §12 says
  3DLOOK does not track people; the copy says the program links scan identifiers to patients. Confirm
  the H1 reads as the program's use.
- **Whitney:** MBSAQIP and NICE are cited as the programs' own follow-up requirements; the page makes no
  accreditation or compliance claim for FitXpress.
- **Vadim:** the Smart Scales weight-error figure ("approximately 3.5% mean absolute error under evaluated
  conditions") is not on the page because Nika marked it as contested internally; the kit asks for it
  where weight matters. Decide whether it goes into the accuracy block.

## Nice to have

- Sticky mobile CTA (WordPress template).
- Logos as WebP files instead of inline base64 PNG.
- Event names per the tracking spec (`generate_lead` with `form_name = fx_lp_demo`, `fx_vertical =
  bariatric`, `demo_click`, `meeting_booked`); the prototype pushes `demo_click` and
  `fitxpress_demo_form_submitted`.
- After launch: relink the bariatric hub article from `/for-bmi-verification/` to this page with the
  anchor "bariatric patient tracking" (`landing-map.md` rule 6).
