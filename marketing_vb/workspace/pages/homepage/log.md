# Homepage (/) — log

Start here: `spec-2026-10-21.md` (Ukrainian), then `page-2026-10-21.md` (copy, EN) and `page-2026-10-21.html` (prototype).

## 2026-10-21 · v1

**Request (Vadim):** a new homepage that meets current standards and routes visitors through the site; 3 products today, more coming, so adding a product must be easy; study how others solved it; SEO and AEO; the old Figma homepage as a reference. Mid-task: «врахуй наш план і ранбук загальний по сео».

**Inputs:** Assel's Doc 1YuYdX… §«Главная страница и карта запросов» (agreed 10-12: title, H1, card grid, query map, what to drop from Figma); SEO plan 09-25 (§1.1a, §1.6, §5, §9); phase-0 runbook (0.2, 0.5, 0.7, 0.8, 0.9, 0.10); dev TZ (P0-3, P0-4, P1-3, P1-7, P2-1, release /fitxpress/); `site-inventory.md`, `landing-map.md`, `proof-points.md`, `accuracy-formulations.md`, `compliance.md`, `tech-spec.md`, `DESIGN.md`; live 3dlook.ai (/, /mobile-tailor/, /wrist-measurement/, /technology/, /about-us/, llms.txt) fetched 21.10; Figma file yQlvzqLeCJAAQjaHSKIduC, canvas 970:248 (frames 970:250, 5465:2044, 5982:7988) via `oo connector run figma`.

**Research:** `research-world-examples-2026-10-21.md` (18 live homepages); `research-seo-aeo-standards-2026-10-21.md` (Google, schema.org, web.dev, W3C, crawler docs). It changed three things in the spec: FAQ rich results are gone since 2026-05-07 (FAQPage markup now optional); GPTBot is training-only, so its 403 is not a release blocker (OAI-SearchBot serves ChatGPT search and gets 200); llms.txt instruction lines must become plain facts.

**Checks run:** `detect-ai-tells.py --channel page` on the copy: 0 hard bans, density 0.0; remaining flags are deliberate (H1 without a product name on a company page; GLP-1, IDs, IEEE left unexpanded). Prototype screenshots (jpeg in this folder): 1440 full page, 1440 with the Use cases menu open, 1280 stress test (6 cards), 390 full page; no horizontal scroll at 390 after the grid `min-width:0` fix; hero + CTA inside 1280×800.

**Not done / waiting:** open items O-1…O-10 in the spec (Wrist card with Sales, head/hand card, awards, logos, privacy scope for MT/Wrist, new form, Sign in, /developers/, visuals, comparison table). Nothing committed or sent.
