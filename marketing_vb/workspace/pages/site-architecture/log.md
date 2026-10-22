# Site architecture and navigation — log

Start here: `architecture-2026-10-22.md` (Ukrainian), then `nav-prototype-2026-10-22.html` (switch 3 / 5 / 8 products and open each menu from the yellow bar).

## 2026-10-22 · v1

**Request (Vadim):** research best practice for the site structure; a header menu that looks good and is not bloated; new products are coming.

**Inputs:** live page-sitemap (32 pages) and post-sitemap (162 posts) on 22.10; GA4 property 251675969, 2026-07-22…10-21, page views vs landing sessions per page (how many visits reach a page from inside the site); the live header of 3dlook.ai (21.10); `../homepage/spec-2026-10-21.md` (product registry); `site-inventory.md`, `landing-map.md`, SEO plan, phase-0 runbook.

**Research:** `research-navigation-2026-10-22.md` — 15 live header teardowns (Stripe, Twilio, Datadog, Veriff, Persona, Yoti, Mitek, Perfect Corp, Banuba, NuraLogix, Styku, Size Stream, Prism, Bodygram, Fit3D) plus NN/g, Baymard and Google Search Central guidance.

**Recommendation:** 5 top-level items for any number of products (Products · Industries · Pricing · Resources · Company) + `Log in ▾` chooser + `Book a demo`; menus rendered from the product registry; product folders stay at the root, use cases at `/{product}/for-{audience}/`, `/industries/{x}/` only for an industry shared by 2+ products, `/products/` only from 7+ products.

**Checks:** prototype screenshots at 1440 (Products and Industries at 3 / 5 / 8 products, Log in) and 390 (mobile menu); no horizontal scroll at 390.

**Open:** A-1…A-7 in the architecture file. Nothing committed or sent.

## 2026-10-22 · approved, then adjusted

Vadim «ок» → A-1, A-2, A-4, A-7 closed. Later the same day: no header login (A-3: FitXpress has no public login; GA4 shows zero site clicks to the Mobile Tailor app), eBooks → `/content-hub/category/ebooks/` (A-5), head and ring not before 2027 (A-6). Prototype, screenshots and Figma updated; `screenshot-login.jpeg` removed.
