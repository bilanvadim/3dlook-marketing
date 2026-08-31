---
product: fitxpress
type: todo
vertical: insurance-underwriting
date: 2026-08-31
---

# TODO — /for-insurance-underwriting/

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
4. **Form destination.** Which plugin or endpoint receives the demo request, and where the submission
   lands. **Owner: whoever owns WordPress.**
5. **Homepage links down.** No parent page on this site links to its verticals in the body. Without a
   vertical block on the homepage the page is reachable only through the nav dropdown.
   **Owner: whoever owns WordPress.**

## Conflicting numbers, which guardrail #2 forbids resolving silently

6. `proof-points.md` says demographic coverage 150 to 205 cm; `about-me.md` says the validation
   population is 150 to 220 cm. **Owner: Vadim.**
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
