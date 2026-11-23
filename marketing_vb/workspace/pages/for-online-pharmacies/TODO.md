---
product: fitxpress
type: handoff-todo
vertical: online-pharmacies
status: gate-not-taken-75
date: 2026-11-23
---

# TODO: FitXpress for online pharmacies

> **Gate not taken: 75/85 after 3 blind rounds (73, 71, 75), weakest axis Sales argument. Publishing requires Vadim's
> explicit decision.** Details for every item: `open-items.md` (numbers in brackets).
> Block order: value first (the scan record before How it works), applied after round 3 at Vadim's request
> 2026-11-23; matches round 1's one_fix; not re-scored.

## 1. Blocking

**(a) Vadim: weight-accuracy figure vs `roadmap.md` [1].** The page states "approximately 3.5% mean absolute error under
evaluated conditions" (accuracy H2, figure tile, method sentence). `roadmap.md` (2026-11-11) says no weight-accuracy
numbers until R&D publishes its baseline; `proof-points.md`, the live insurance landing and the BMI page v7 use the
figure. If it goes: delete the tile and the method sentence and use the qualitative replacement text in [1].

**(b) Vadim: H1, title and focus keyphrase [2, 3, 16d].** H1 "FitXpress for online pharmacies: a live weight check
before weight-loss prescribing"; title "Order-Flow Weight Checks for Online Pharmacies | FitXpress"; keyphrase "weight
checks for online pharmacies" (zero measured demand; the round-3 judge called it unnatural). "BMI verification" stays
out of H1, H2s, title and meta (non-competition).

**(c) Product confirmations [4-8, 7a].**
- Live capture in every SDK, web included (the page says photos are taken live in the order flow).
- How much the Smart Scales estimate depends on the height the patient enters [7a].
- Where the mismatch threshold lives: configured in FitXpress or applied by the pharmacy's system [5].
- A re-order scan counts as one API request [6].
- The Admin Panel (failed-scan messages, photo-deletion dates) is available on Starter [7].
- Whether the SDK capture can run on the same phone while the patient is on a video call (the call app holds the
  camera), or needs a second device or a step straight after the call [6a]. The page says "during or straight after
  an online consultation" until product answers.

**(d) Whitney and Asel: regulatory framing [17, 17a, 18, 18a, 18b].**
- The GPhC wording: two verbatim phrases from the February 2025 guidance, the cost sentence, the scope sentence.
- The guidance's own examples (video consultation, in person, clinical records, the GP) do not include a photo-based
  estimate; the page never says FitXpress counts as that verification [18a].
- Whether MHRA or CQC context belongs on a UK pharmacy landing [18b].
- Whether a verbatim regulator quotation may carry "independently" despite the reserved-word gate [17a].

**(e) Asel: spelling and pricing [16a, 24a].** US house spelling on a UK-led page; USD prices (the live `/pricing/` is
USD only).

**(f) Katerina: sign-off roles [16c].** Superintendent pharmacist and compliance lead as the people who agree pilot
criteria and judge GPhC fit.

## 2. Before publishing (technical)

- [ ] Build in the theme from `page.html`; delete the two `data-prototype-chrome` blocks (header, footer)
- [ ] Replace the form mock with the shared HubSpot embed, as on the live fitness page; section `id="demo"`, alias `id="form"` (`wordpress-notes.md`)
- [ ] Add the page path to the GTM `fx_vertical` lookup (`online-pharmacies`), now and again after the 301
- [ ] Add the Service, FAQPage and DefinedTerm JSON-LD; check Yoast's WebPage and BreadcrumbList match; validate in validator.schema.org
- [ ] Check the client logo strip with design (UK Meds first; the rest = the shared strip of the live use-case pages)
- [ ] Measure performance; check 1440 px; tab through the page with a keyboard
- [ ] After publish: a test submission shows `generate_lead` (`form_name = fx_lp_demo`, `fx_vertical = online-pharmacies`) in GA4 DebugView and the same `fx_vertical` on the HubSpot contact; `demo_click` fires on each button

## 3. Inbound links when it ships

- [ ] BMI verification feature page: the pharmacy card links down here (both the live `/for-bmi-verification/` and Asel's v7 rebuild)
- [ ] Compliance guide (`/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/`): its down link and demo button point to `/for-bmi-verification/` today; relink to this page and `#demo`
- [ ] `brand-assets/content-strategy/landing-map.md`: flip the online-pharmacies row to `live`, "Link now" = this URL, "Demo button now" = `{URL}#demo`, anchors = weight checks for online pharmacies · FitXpress for online pharmacies · weight check before weight-loss prescribing
- [ ] Grep the published pharmacy and BMI articles that still link the stand-in and relink them
- [ ] When `/fitxpress/` ships: 301 to `/fitxpress/for-online-pharmacies/`, Search Console baseline first, update canonical, breadcrumb (three levels), schema URLs and the GTM row

## 4. Template and site issues found while building (not this page's files)

- [ ] Live fitness landing: consider the same value-first order (scan record before How it works) Vadim chose here
- [ ] Live fitness landing has no `#demo` anchor (its form is the footer at `#form`), while `landing-map.md` rule 4 and Kit slot 15 send article buttons to `{landing}#demo` [21]
- [ ] Fitness prototype 12 px captions (`#808080` on white) measure 3.95:1, under 4.5:1; check the live page [22]
- [ ] Live fitness hero says "results in under 45 seconds after capture"; the one public wording is "under 45 seconds from the photos to structured results" [23]
- [ ] `site-inventory.md` still lists "Starter $1,000/mo (up to 500 scans)"; live `/pricing/` reads "500 API requests included per month" [24]
- [ ] Live insurance graph defines Smart Scales as "scale-weight data"; the entity inventory says "estimated weight data" (this page uses the inventory)

## 5. Nice to have (round-3 judge points without a ruling)

- An H1 or lede that names the paid-for outcome more directly (defensible prescribing without losing orders)
- FAQ headings in search phrasing rather than brand phrasing
- One line in the form block on what happens after submission (HubSpot Meetings opens)
- A button or soft link inside the accuracy block (about 2,500 px without one at 1280×800)
- Sibling links as cards instead of a text line
- A vertical figure in the hero once a client approves one
