---
product: fitxpress
type: todo
vertical: all
date: 2026-09-27
---

# TODO: /fitxpress/

Ordered: blockers → placeholders → claims to confirm → nice to have. Every `[PLACEHOLDER]` in
`page.md` is listed here, and every placeholder listed here exists in `page.md`.

## 0. First, for Vadim

- [ ] **Gate not taken: 74/85 after 3 rounds (70, 68, 74), weakest = Proof of belonging.** Publishing
      below 85 needs Vadim's explicit decision.
- [ ] **Proof lever: approve an anonymised FitXpress deployment figure** that cannot identify UK Meds,
      Yazen or Healthyr, and add it to `proof-points.md` (`open-items.md` A18).
- [ ] **Design/technical and Place-in-site can only be scored after the page is built** (plan in
      `fact-sheet.md`, "Planned build").

## 1. Blockers (launch cannot happen until these are done)

- [ ] **Remove the 301 `/fitxpress/` → `/`** (live on 2026-09-27, checked by curl). Save the Search Console
      baseline first (`gate-reports.md`).
- [ ] **Fix `/fitxpress` (no slash)**: it 301s to `/content-hub/fitxpress-admin-panel-launch/`; must go to
      `/fitxpress/`.
- [ ] **Homepage FitXpress block** linking to `/fitxpress/` (anchor "FitXpress" / "FitXpress AI body
      scanner"). Without it the page is orphaned from its strongest inbound source, and the "ai body
      scanner" intent cannot move from `/`. Homepage title should drop "AI body scanner" when the homepage
      is rewritten.
- [ ] **Pricing trial conflict.** `/pricing/` meta description and a closing block promise a 7-day trial;
      repo files say 1 month / 200 requests; Vadim's rule is no public trial. Fix `/pricing/` before this
      page links to it (`open-items.md` B1).
- [ ] **Logo approvals and assets.** UK Meds and Yazen approved for logos (Vadim 2026-09-27). **Healthyr:
      confirm** (no case-study file; current site alt text reads "Reddit"). Supply logo files (SVG or WebP).
- [ ] **Demo destination.** Which form or scheduler "Book a demo" opens, and where submissions land in
      HubSpot. `/contact-us/` shows JS errors in 31% of sessions (SEO plan §1 item 3); the button must be a
      real `<a>` link.
- [ ] **Nav and footer**: "FitXpress" items point to `/fitxpress/`.

## 2. Placeholders in the markup

- None. Visual markers (`[HERO]`, `[LOGO STRIP]`, `[OUTPUTS]`, `[WORKFLOW]`, `[INDUSTRIES]`, `[PAYLOAD]`,
  `[INTEGRATION]`, `[ACCURACY]`, `[COMPLIANCE]`, `[FAQ]`) are design briefs, not copy (`wordpress-notes.md` §4).
- [ ] **`/developers/` page** (SEO plan §4, 1.3). Not a page marker: the docs link goes straight to
      `https://docs.fitxpress.3dlook.me` (dofollow). When `/developers/` ships, switch both doc links to it.
- [ ] Confirm `https://docs.fitxpress.3dlook.me` is public and current before launch.

## 3. Claims to confirm (Vadim, Asselya, Whitney)

- [ ] Price named on a page vs `about-me.md` "never state prices" (`open-items.md` A1).
- [ ] New public sentence on API/SDK access after a demo call or NDA (A2).
- [ ] Smart Scales still beta? (A6)
- [ ] SDK recommendation as hedged opinion (A5).
- [ ] Medical-device short form, FDA sentence and decision-boundary paraphrase (A9, A10, A14). Whitney.
- [ ] Results-block destinations per program and the "standard 3D file format" wording (A15).
- [ ] Demo form fields and `generate_lead` mapping in HubSpot.
- [ ] Employer wellness link target (A11).
- [ ] Starter price and scan limit re-checked on `/pricing/` on publish day (schema `offers` too).

## 4. Link switches when vertical pages ship

Each industries card currently links to a live article. Switch the link when the page ships:

| Card | Link today | Switches to |
|---|---|---|
| Telehealth and GLP-1 | `/structured-body-data-for-telehealth-digital-health-programs/` | `/fitxpress/for-telehealth-…/` when rebuilt (301) |
| Online pharmacies | `/for-bmi-verification/` | `/fitxpress/for-online-pharmacies/` when rebuilt (301) |
| Connected fitness | `/fitxpress/for-connected-and-digital-fitness/` | stays; fix its breadcrumb (`?page_id=36425`, 404) |
| Life insurance | `/content-hub/mobile-body-scanning-insurance-underwriting/` | `/fitxpress/for-insurance-underwriting/` |
| Employer wellness and health plans | `/content-hub/wellness-rewards-verification-employers-insurers-using-ai-3d-body-scanning/` | `/fitxpress/for-{wellness slug}/` |
| Occupational health | `/content-hub/occupational-health-screening-software/` | `/fitxpress/for-occupational-health/` |
| Clinical trials | `/content-hub/clinical-trial-anthropometric-measurement-software-obesity-trials/` | `/fitxpress/for-clinical-trials/` |
| Bariatric and metabolic | `/content-hub/bariatric-pre-qualification-mobile-3d-body-scanning/` | `/fitxpress/for-bariatric-…/` |

Note: `workspace/pages/for-insurance-underwriting/` was drafted 2026-08-31 at the old root URL
`/for-insurance-underwriting/`; under the 2026-09-27 hierarchy it belongs at `/fitxpress/for-…/`.

## 5. Nice to have

- [ ] `/content-hub/body-measurement-software/` (2021) links up here with anchor "FitXpress body
      measurement API".
- [ ] Health hub, accuracy framework and trust FAQ articles link up here.
- [ ] Add `/fitxpress/` to `llms.txt` (draft at `workspace/research/seo-fitxpress-2026-09/2026-09-27-llms.txt`).
- [ ] G2 / Capterra reviews as a proof substitute (SEO plan §1.4); the page has no slot for a rating
      until one is in `proof-points.md`.
- [ ] HTML prototype with `DESIGN.md` §13 tokens if the layout needs approval before development.
- [ ] Re-sync `faq.md`, `pricing.md`, `about-me.md`, `overview.md`, `audience.md` against canon
      (`open-items.md` B2-B5).
