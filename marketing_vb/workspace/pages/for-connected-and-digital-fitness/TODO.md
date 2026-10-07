---
product: fitxpress
type: todo
vertical: connected-and-digital-fitness
date: 2026-10-07
---

# TODO before publishing

## Blockers
- [x] Vadim approved the final copy, 2026-10-07 (`page-final-2026-10-07.{md,html}`, merged from v3 and the team's fixes).
- [ ] Product answers P1-P3 (`open-items.md`); until then the safer wording stays.
- [ ] WordPress build in place at the live URL; the canonical stays on self (Nika's prototype pointed to `/fitxpress/for-connected-fitness/`).
- [ ] The breadcrumb's middle level: the live page links `?page_id=36425` (404). The final links `/fitxpress/`, which still 301s to `/` (2026-10-07): ship `/fitxpress/` first or unlink it.

## Build
- [ ] Shared HubSpot form `FX | LP | Demo` at `#demo`; GTM lookup row for this path → `fx_vertical = connected-and-digital-fitness`.
- [ ] Schema from `page-final-2026-10-07.html` (WebPage, Service, FAQPage, BreadcrumbList; FAQ answers text-identical, checked 2026-10-07); Rich Results Test.
- [ ] H1 size: check the hero still fits 1280×800 with the final's shorter H1.
- [ ] Logo row under the hero strip: Zing Coach and verv first (in the final), then the rest of the cleared client set from design, alt text = client name.
- [ ] Comparison: table on desktop, cards under 960 px (in the final's CSS); check both.
- [ ] Ask Nika where 95%+ consistency, the per-body-part table, 99.5% SLA and React Native come from (open item D).
- [ ] Sticky "Book a demo" on mobile: at 375×667 the hero button sits at 776 px.
- [ ] Hero visual: the progress-record card, captioned "Illustrative example".
- [ ] Yoast: title, description, focus keyphrase from `page-final-2026-10-07.md` (see M4).
- [ ] 375 / 768 / 1280 / 1440, contrast, keyboard; analytics events fired by hand.

## After publishing
- [ ] Search Console at 30 and 90 days against the baseline in `gate-reports.md` (677 impressions, 10 clicks, position 15.2 for Jul-Sep).
- [ ] Hub 1 articles already link here (`landing-map.md` row is `live`); check their "Book a demo" buttons point to `…/#demo`.
