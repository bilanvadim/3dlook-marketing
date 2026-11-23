---
product: fitxpress
type: wordpress-notes
vertical: online-pharmacies
status: gate-not-taken-75
date: 2026-11-23
---

# WordPress notes: /for-online-pharmacies/

> Gate not taken: 75/85 after 3 blind rounds. Do not publish without Vadim's explicit decision (`TODO.md`).

## URL, canonical, 301 plan

- URL now: `https://3dlook.ai/for-online-pharmacies/` (root, because `/fitxpress/` still 301s to `/`). Canonical to
  self.
- When `/fitxpress/` ships: 301 `/for-online-pharmacies/` → `/fitxpress/for-online-pharmacies/`. Before the move, save
  a Search Console baseline. With the move, update the canonical, the breadcrumb (add the FitXpress middle level), the
  URLs in the JSON-LD (`@id`s included) and the GTM `fx_vertical` lookup row.
- In the sitemap; indexable.

## Yoast fields

| Field | Value |
|---|---|
| SEO title | `Order-Flow Weight Checks for Online Pharmacies \| FitXpress` (58 / 60) |
| Meta description | `Weight checks for online pharmacies: FitXpress adds a weight estimate from photos taken live at checkout, for the prescriber to review before supplying.` (152 / 155) |
| Focus keyphrase | `weight checks for online pharmacies` (Yoast will flag it missing from the introduction; known, open item 16d) |
| Canonical | `https://3dlook.ai/for-online-pharmacies/` |
| Breadcrumb title | FitXpress for Online Pharmacies |

Both fields differ from the BMI feature page and the compliance guide.

## Build

- Closest live template: `/fitxpress/for-connected-and-digital-fitness/` (same block order and components). The
  prototype `page.html` uses the fitness final CSS, namespaced `.fx-op-*`.
- Delete the two blocks marked `data-prototype-chrome` (header, footer): the theme supplies both.
- One H1. Section order as in `README.md`: since 2026-11-23 the scan record sits before How it works (Vadim), the
  opposite of the live fitness page; band colours alternate white / light accordingly.
- "Order and re&#8209;order" in the hero strip uses a non-breaking hyphen.
- The comparison is a table at 960 px and up, one card per option below (both in the markup; CSS switches).
- Client logos: UK Meds first, then the shared strip; alt text = client name. URLs in `page.html`.
- External links (GPhC PDFs, API documentation) open in a new tab with `rel="noopener"`.

## Form and anchors

- Embed the shared HubSpot form `FX | LP | Demo` exactly as the live fitness page does:
  `hbspt.forms.create({ portalId: "6014382", formId: "11acb23a-e81c-46ee-bb23-4d47a0ef0125", region: "na1", … })`,
  including the theme's `onFormReady` placeholder handling. No page-specific fields.
- The form section carries `id="demo"`. Every button on the page links to `#demo` (Kit slot 15, `landing-map.md`
  rule 4). Keep an alias `id="form"` on the same block, because the live template's footer form uses `#form`.
- Hidden field `fx_vertical` comes from GTM: add the path `/for-online-pharmacies/` → `online-pharmacies` to the
  lookup (and the `/fitxpress/…` path after the 301).

## Schema

Yoast supplies `WebPage`, `WebSite`, `Organization` and `BreadcrumbList`. Add the rest of the graph from the
`## Schema markup` block in `page.md` (also at the end of `page.html`) in a Custom HTML block:

- `Service` `https://3dlook.ai/for-online-pharmacies/#fitxpress-online-pharmacy-service`, with `audience`
  (`BusinessAudience`, online pharmacies and digital prescribing services) and `areaServed` United Kingdom.
- `FAQPage` `…/#faq`, four questions, answers text-identical to the page (if an answer changes on the page, change it
  here).
- `DefinedTermSet` `https://3dlook.ai/#entity-inventory` and five `DefinedTerm` nodes (Smart Scales, BMI, BMI
  verification, Real-Time Pose Validation, accuracy). These @ids are not defined on their own URLs, so every landing
  that mentions them defines them, as the live insurance and fitness pages do.
- The `WebPage` node in the block only wires `about`, `mainEntity`, `hasPart`, `breadcrumb` and `mentions` to Yoast's
  WebPage `@id` (the page URL). Check that Yoast's BreadcrumbList has the same two items.
- Organization is always `https://3dlook.ai/#organization` (Yoast's id).
- Validate in validator.schema.org (the Rich Results Test no longer checks FAQPage).

## FAQ markup

Four `<details><summary><h3>…</h3></summary><p>…</p></details>` items: native keyboard and tap behaviour, state
announced by the browser. The integration answer links the FitXpress API documentation.

## Analytics (verify manually after publish)

| Event | Fires on |
|---|---|
| `generate_lead` (`form_name = fx_lp_demo`, `fx_vertical = online-pharmacies`) | successful form submission |
| `demo_click` | each demo button; `data-cta` values in the prototype: `hero`, `patient-flow`, `sample`, `how-it-works`, `order-flow`, `pilot`, `form` |
| `meeting_booked` | HubSpot Meetings booking after submission |

Check: a test submission shows in GA4 DebugView with the right `fx_vertical`, and the HubSpot contact carries the same
value.

## Images and performance

No new images. Logos are WebP from the theme folder (0.8-4.6 KB, lazy-loaded). Performance was not measured on the
prototype; measure after the build.
