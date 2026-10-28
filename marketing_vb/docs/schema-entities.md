# Schema entities

`schema-entities.csv` is a snapshot of Asselya's entity inventory: the Google Sheet
"GEO: Content & Entity inventory" (`1fR3fcveMZe1SLidfa61Can3NsDkQfADvQ2oexDRVtjE`), tab "Entity inventory".
The Sheet is the source of truth. The snapshot was taken on 2026-10-28, and Asselya shared the link in
Slack that day. Re-pull the Sheet before relying on a row that may have changed.

The live landing graphs are already built from it. `/for-insurance-underwriting/` and `/wrist-measurement/`
carry a `DefinedTermSet` "3DLOOK Entity Inventory" (`https://3dlook.ai/#entity-inventory`), and every
`DefinedTerm` `@id` on those pages matches the file (checked 2026-10-28).

## Rules for anyone writing JSON-LD (page-builder, seo-publisher, people)

- **Reuse the entity's `@id`, name and definition from the file.** Never mint a second `@id` for an
  entity already listed.
- **Organization is always `https://3dlook.ai/#organization`.** Yoast generates that id on every page, and
  the custom landing graphs reuse it. The file still says `https://3dlook.ai/about-us/#organization`;
  until the Sheet is fixed, the Yoast id wins. A second id would split 3DLOOK into two entities.
- **WebSite is `https://3dlook.ai/#website`** (Yoast).
- **Validate in [validator.schema.org](https://validator.schema.org/).** Google dropped FAQ rich results on
  2026-05-07 and removed the docs on 2026-06-15, so the Rich Results Test no longer checks `FAQPage`.
- **FAQ articles** (the whole body is Q&A under H3): use one `FAQPage` in a Custom HTML block, with
  `@id` = page URL + `#faq` and `isPartOf` → the page URL. Don't use the Yoast FAQ block there,
  because it is visible and would repeat the questions. **Regular articles** with a short FAQ at the end:
  use the Yoast FAQ block, which merges into Yoast's graph.

## Open issues in the Sheet (reported to Asselya 2026-10-28)

1. Organization `@id` is `about-us/#organization`, not `https://3dlook.ai/#organization` (see above).
2. "Body progress" (concept) and "Body Progress" (FitXpress feature) share `https://3dlook.ai/#body-progress`.
   They need different ids.

## Entity tree (tab "Entity tree")

```
3DLOOK
│
├── FitXpress
│   ├── Smart Scales
│   ├── Future Body
│   ├── Body progress
│   └── Health workflows
│       └── BMI verification
│
├── Mobile Tailor
│   └── Apparel workflows
│       └── Made-to-measure
│
├── 3DLOOK AI Wrist Measurement
│   ├── wrist measurement
│   └── sizing and fit logic
│
└── Mobile body scanning
├── Two-photo body scanning
├── Capture workflow
├── Capture conditions
└── Body metrics
        ├── Body measurements
        ├── Body composition
         │   ├── Body-fat percentage
         │   ├── Fat mass
         │   └── Lean mass
         ├── BMI
         └── BMR


Measurement quality framework
├── Accuracy
├── Repeatability
├── Validation methodology
├── Robustness
└── Reference methods
```
