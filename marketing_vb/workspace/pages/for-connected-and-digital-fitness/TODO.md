---
product: fitxpress
type: todo
vertical: connected-and-digital-fitness
date: 2026-10-02
---

# TODO before publishing

## Blockers
- [ ] Vadim approves the v3 copy (`page-v3-2026-10-06.md`) and the H1 (`open-items.md` A, 1), and decides on shipping below 85 (73/85).
- [ ] WordPress build in place at the live URL; the canonical stays on self (Nika's prototype pointed to `/fitxpress/for-connected-fitness/`).
- [ ] The breadcrumb's middle level: the live page links `?page_id=36425` (404). Link `/fitxpress/` only once it no longer 301s to `/`.

## Build
- [ ] Shared HubSpot form `FX | LP | Demo` at `#demo`; GTM lookup row for this path → `fx_vertical = connected-and-digital-fitness`.
- [ ] Schema from `page-v3-2026-10-06.html` (Service, FAQPage, BreadcrumbList); Rich Results Test.
- [ ] H1 size: the v3 H1 is longer (product + audience + outcome); the prototype caps it at 50 px desktop / 30 px mobile to keep the hero in the first viewport.
- [ ] Logo row under the hero strip: all 3DLOOK client logos, cleared set from design, alt text = client name (`[PLACEHOLDER]` in the prototype).
- [ ] Ask Nika where 95%+ consistency, the per-body-part table, 99.5% SLA and React Native come from (open item D).
- [ ] Sticky "Book a demo" on mobile: at 375×667 the hero button sits at 776 px.
- [ ] Hero visual: the progress-record card, captioned "Illustrative example".
- [ ] Yoast: title, description, focus keyphrase from `page.md`.
- [ ] 375 / 768 / 1280 / 1440, contrast, keyboard; analytics events fired by hand.

## After publishing
- [ ] Search Console at 30 and 90 days against the baseline in `gate-reports.md` (677 impressions, 10 clicks, position 15.2 for Jul-Sep).
- [ ] Hub 1 articles already link here (`landing-map.md` row is `live`); check their "Book a demo" buttons point to `…/#demo`.
