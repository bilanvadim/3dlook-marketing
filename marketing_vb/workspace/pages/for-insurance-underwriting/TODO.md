---
product: fitxpress
type: todo
vertical: insurance-underwriting
date: 2026-08-31
---

# TODO — /for-insurance-underwriting/

## Live since 2026-10-21: post-launch

Done on 2026-10-21: in `page-sitemap.xml`, indexed by Google with a self canonical, linked from the main
menu, shared form `11acb23a` embedded, live text captured in `published-live-2026-10-21.md`,
`landing-map.md` marks the Hub 4 row as live at the wrong URL.

Decided by Vadim on 2026-10-21: the root URL is a mistake, and the page moves to `/fitxpress/` as planned.
Client logos may be used on the website, so the logo strip stays.

- [ ] **Move to `/fitxpress/for-insurance-underwriting/`, with a 301 from `/for-insurance-underwriting/`.**
      Do it now, while the page has one day of history. **Owner: Asselya + developer.**
      1. WordPress: give the page the same parent as the fitness landing (its breadcrumb points at
         `?page_id=36425`) and keep the slug `for-insurance-underwriting`.
      2. 301 from `/for-insurance-underwriting/` to `/fitxpress/for-insurance-underwriting/`.
      3. Point the main menu item "Life Insurance Underwriting" at the new URL directly, not through the 301.
      4. JSON-LD: today the page's graph holds 14 references to the root URL. After the move none may remain,
         in `@id`, `url` or the breadcrumb.
      5. Check that the Yoast canonical is the new URL and that `page-sitemap.xml` lists the new URL, not the old one.
      6. Search Console: inspect the new URL and request indexing. The old one should turn into "Page with
         redirect" within days.
      7. Breadcrumb Home → FitXpress → FitXpress for Insurance Underwriting comes with the parent. Its
         FitXpress crumb repeats the fitness page's bug (`?page_id=36425`, a 404) until `/fitxpress/` ships.
- [ ] **GTM `fx_vertical`: two rows, both `insurance`:** `/fitxpress/for-insurance-underwriting/` (the plan's
      row, needed for the move) and `/for-insurance-underwriting/` (the page lives there until the move).
      Page Path matches exactly, so without the root row today's leads arrive with an empty `fx_vertical`.
      Then send a test lead per runbook 0.10 §6 from the URL the page is on, `test+fx-insurance@3dlook.me`:
      `form_name = fx_lp_demo`, `fx_vertical = insurance`, UTM fields filled. **Owner: Asselya (GTM).**
- [ ] **Yoast title and meta description to the final values** (`page-final-2026-10-02.md` → Yoast). The live
      title is the 2026-08-31 v1 one, without `accelerated underwriting`, which is the keyword rank tracking
      watches for this page (`rank-keywords.csv`, US, target 5). **Owner: Asselya.**
- [ ] **"9 vs 27" source label**: change "Gen Re, Next Gen Underwriting Survey" to the LIMRA study its link
      points to. **Owner: Asselya.**
- [ ] **Down link from the hub article** `/content-hub/mobile-body-scanning-insurance-underwriting/`
      (landing-map rule 6), to the `/fitxpress/` URL once the page has moved. Today its body links only to
      `/for-bmi-verification/` ("BMI/build verification"), and the landing is reachable from it only
      through the menu. Add one in-body link in the first 30%, anchor "accelerated underwriting" or "build
      and BMI evidence for underwriting". It is the only published article in Hub 4. **Owner: Asselya.**
- [ ] **llms.txt on the site** (Last updated 2026-09-18) does not list the page. Add it with the `/fitxpress/`
      URL after the move; the line is in the repo draft
      (`workspace/research/seo-fitxpress-2026-09/2026-09-27-llms.txt`). **Owner: Asselya.**
- [ ] **`#demo` anchor.** Articles are told to link `{landing}#demo`; this page answers to `#form`.
      Either add `id="demo"` to the form block or keep `#form` (landing-map now says `#form` for this row).
- [ ] **Search Console at 30 and 90 days after the move**: item 20 below.

> **Blind judge: 69 / 85, gate not taken. Weakest axis proof of belonging, 10 / 20. One hard fail:
> fewer than two case studies from this vertical.** Same fact that failed G-I. Detail in
> `judge-round-1.json`.

## Blocking — nothing is built until these are answered

1. **G-I waiver.** The vertical has zero case studies. By the Kit's rule the page does not exist. Vadim
   decides: waive and publish as drafted, or hold and put an insurance section on the homepage instead.
   Detail in `gate-reports.md`. **Owner: Vadim.**
2. **Slug confirmation.** `/for-insurance-underwriting/`, at root, child of the homepage. Free as of
   2026-08-31. **Owner: Vadim.**
3. **Customer naming.** `case-studies/uk-meds.md` and `messaging.md` say UK Meds and Yazen can be named
   publicly. The insurance deck says the opposite, citing an NDA. The page names nobody until this is
   settled. **Owner: Vadim, Whitney.**
4. **Form destination.** Decided 2026-09-29: the shared HubSpot form `FX | LP | Demo` (anchor `#demo`),
   with a GTM `fx_vertical` row for the final path → `insurance` (tracking spec B2.5). The URL in this
   draft (`/for-insurance-underwriting/`, parent `/`) predates the 2026-09-27 hierarchy and becomes
   `/fitxpress/for-insurance-underwriting/`. **Owner: whoever owns WordPress + GTM.**
5. **Homepage links down.** No parent page on this site links to its verticals in the body. Without a
   vertical block on the homepage the page is reachable only through the nav dropdown.
   **Owner: whoever owns WordPress.**

## Conflicting numbers, which guardrail #2 forbids resolving silently

6. ~~`proof-points.md` says demographic coverage 150 to 205 cm; `about-me.md` says the validation
   population is 150 to 220 cm.~~ **RESOLVED 2026-09-02 — Vadim: 150 to 220 cm.** Propagated to
   `proof-points.md`, `how-it-works.md`, `faq.md`, this page and `fact-sheet.md`.
7. `pricing.md` contradicts the live `/pricing/` page. The page uses the live figures. **Owner: Vadim.**
8. Publication rights on "112,100 scans across 67 active customers in 2025", which is marked Internal in
   `proof-points.md` and does not appear anywhere on the live site. **Owner: Vadim.**

## Claims needing confirmation before publish

9. The HIPAA paragraph, the biometric-classification paragraph and the NAIC paragraph.
   **Owner: Whitney Cathcart.**
10. Whether SOC 2 should be mentioned at all. It is absent from the page today, and `audience.md` lists it
    among this buyer's procurement gates. **Owner: Vadim.**
11. Add the ISO 8559-1:2017 benchmark figures to `proof-points.md`, or confirm they stay out. They are on
    the live telehealth page and in `about-me.md` but absent from `proof-points.md`, so the accuracy block
    is thinner than the benchmark page's. **Owner: Vadim.** Highest value item on this list.
12. Twenty minutes with Nick Omelchak on the US objections, which G-I asks for and which was not done.
    **Owner: Vadim.**

## Missing content

13. **No case cards and no customer quote.** Both slots are unfilled because the vertical has no
    customer. Exit condition: the first carrier pilot closes, or an approved reference is available.
14. **No images exist.** `assets/` is empty. Seven visual briefs with alt text are in `README.md`. Someone
    has to produce them: guided-capture UI, the integration diagram, the five-stage journey.
15. **FAQ answers into the JSON-LD.** All 13, byte-identical to the rendered text.

## After the page is built, before it is called done

16. Validate the schema. Three types, none of them tested yet.
17. Check 375, 768, 1280 and 1440. Contrast and keyboard operation, including the accordion.
18. Verify the four analytics events firing manually.
19. Measure performance. Nothing has been measured, because nothing has been rendered.

## Post-launch

20. Search Console at 30 and 90 days, against a zero baseline. Watch specifically whether
    `/for-bmi-verification/` or the hub article loses ground: that would mean this page is a duplicate
    and should fold back into a section.

## Also worth doing, outside this page

21. **The insurance deck breaks the same guardrails the page is held to.** "Best-in-class repeatability",
    "independently benchmarked", "validated methodology", and figures absent from `proof-points.md`.
    Listed in `open-items.md` §11. The deck is in active sales use.
