---
product: fitxpress
type: gate-report
vertical: insurance-underwriting
status: g-i-waiver-requested
date: 2026-08-31
---

# Gate reports — /for-insurance-underwriting/

## G-I · Should this page exist

| Criterion | Result | Evidence |
|---|---|---|
| Use-case file exists | **PASS** | `brand-assets/product-info/use-cases/fx-insurance-underwriting.md` |
| 2+ publishable case studies from this vertical | **FAIL** | Zero. `case-studies/` holds Burlington Medical, Generation Tux, Jim's Formal Wear, Safariland, UK Meds, Yazen. None is an insurer. `proof-points.md` lists no insurance customer. The coverage table in `page-types.md` already records `FX — insurance underwriting → cases available: —` |
| Demand exists | **PASS** | `content-plan.md` Hub 4 "Insurance Underwriting & BMI Verification", P0, a 12-row cluster. Hub article live since May 2026 (`mobile-body-scanning-insurance-underwriting`, ~4,200 words) |
| 5 facts absent from the parent page | **PASS**, 8 found | NAIC accelerated-underwriting expectations · Munich Re 2025 build/BMI as the second-largest driver of misclassification · CDC 40% underestimate of severe obesity · the attending physician statement wait · the disclosed-versus-captured comparison step · the underwriter review queue as the escalation target · HIPAA covered-entity status varying by carrier · body data possibly falling under biometric rules by jurisdiction. The homepage carries none of these |
| BD owner confirms the objections differ | **NOT RUN** | Nick Omelchak owns the US market. Not consulted. Open item |
| Parent and URL settled | **PASS, pending Vadim** | Parent `/`, proposed `/for-insurance-underwriting/`, confirmed free (HTTP 404 on 2026-08-31) |
| 60% uniqueness achievable | **PASS, measured** | Homepage re-fetched 2026-08-31: 1,029 words, **zero occurrences of "insurance" or "underwriting"**. Its H2 set is "Leveraging accurate 3D body data", "Industry-acclaimed technology", "Advanced solutions for advanced growth and efficiency", "AI Body Data for Better Health & Fitness", "Integration". Of the 14 sections on the new page, 2 have any homepage equivalent (the integration boundary, and part of the quick-answer block), so roughly 86% is unique. The homepage breaks two current guardrails in its own headings, `leveraging` and `industry-acclaimed`, and is a rewrite candidate, never a style model |

### Verdict

**G-I fails on one criterion: zero case studies from this vertical.** Per `kit-vertical-page.md`, a
failed G-I means no page, and instead a section on the parent page along with the vertical's hub
article, revisited when the second case lands.

**A waiver is requested from Vadim**, on these grounds:

1. The vertical is P0 in the content plan and its hub article has been live since May 2026. The cluster
   has an authority page and no commercial page to convert into.
2. A full presentation deck for this exact vertical already exists
   (`fitxpress-insurance-underwriting-deck-copy.md`, 29 slides), which means the sales motion is live
   and the page is the missing web surface for it.
3. What stands in for the missing cases: the page claims **no insurance deployment**. It states
   pilot stage plainly, and the proof block carries adjacent regulated deployments (unnamed) along with
   the company-level 2025 scan volume. Nothing is fabricated and no adjacent case is dressed up as an
   insurance one.

**If the waiver is refused**, the fallback is the Kit's own: an insurance section on the homepage plus
the existing hub article, revisited when the first carrier pilot closes. The draft in `page.md` is then
held, not published.

---

## G-A · Architecture gate

| Check | Result |
|---|---|
| **Parent** | `/` (the homepage is the FitXpress parent; `/fitxpress/` 301s to it) |
| **URL** | `/for-insurance-underwriting/` — matches the `/for-{vertical}/` root pattern used by `/for-bmi-verification/`. Verified 404 on 2026-08-31, so no redirect or Search Console baseline is needed |
| **Sibling set** | `/for-bmi-verification/`, `/structured-body-data-for-telehealth-digital-health-programs/`, `/fitxpress/for-connected-and-digital-fitness/` |
| **Sitemap re-pulled** | Yes, 2026-08-31. 30 pages, identical to the `site-inventory.md` snapshot of 2026-08-23. No drift |
| **Search Console baseline** | Not applicable, the URL does not exist |

### Cannibalisation

Both inventories checked.

| Risk | Assessment |
|---|---|
| `/content-hub/mobile-body-scanning-insurance-underwriting/` (hub article, ~4,200 words) | **Split of intent, not a duplicate.** The hub answers "what is AI in underwriting and how does body scanning fit" for a researching reader. The page answers "can this run inside our accelerated program, and what does compliance need to see" for a buyer. The page must not repeat the hub's definition-of-underwriting sections, and the draft does not |
| `/for-bmi-verification/` (~659 words) | **Real overlap on the phrase "BMI verification".** That page is online-pharmacy and remote-prescribing eligibility. This page is underwriting evidence. Mitigation: the H1 and the Yoast title lead on *underwriting* and *build*, never on bare "BMI verification", and the two pages link to each other as siblings. Worth re-checking in Search Console 30 days after indexing |
| Homepage | No overlap. Health and fitness positioning, no insurance content |

### Inbound internal links to request

1. **The homepage links down.** No parent page on this site links to its verticals in the body today.
   One card in a vertical block on `/`.
2. The hub article `mobile-body-scanning-insurance-underwriting` links to the new page from its
   "Where FitXpress Fits" section and from "Next Steps", which currently point at `/` and
   `/for-bmi-verification/`.
3. `/for-bmi-verification/` and the telehealth page add it to their sibling blocks.
4. `/pricing/` and `/case-studies/` are outbound from the page, not inbound.

**G-A: PASS**, conditional on Vadim confirming the slug.

---

## Slots dropped, with reasons

| Slot | Decision | Reason |
|---|---|---|
| **10 · Cases from this vertical** | **Reduced to an honest deployment block** | Zero insurance customers exist. The Kit forbids an adjacent-vertical case card, and inventing one is a hard fail. The block states pilot stage and describes adjacent regulated deployments without naming them |
| **11 · Customer quote** | **Dropped** | No approved insurance quote exists. The deck carries the same gap and marks it `[APPROVED CUSTOMER QUOTE NEEDED]`. An unnamed or invented testimonial stays out |
| **9 · ISO 8559-1:2017 benchmark block** | **Dropped** | The figures (0.40 cm session-to-session, 14 companies, 8 countries, 27 subjects, 1,152 data points) are in `about-me.md` and on the live telehealth page but **absent from `proof-points.md`**. The Kit allows only `proof-points.md` figures. One line added to `proof-points.md` restores this block, and it is the single highest-value open item |

---

## G-T · Technical gate

Run against the draft, not against a live page. Nothing here can be closed before the page is built in
WordPress.

| Check | State |
|---|---|
| Indexable, in the sitemap, canonical to self | **Specified**, not verifiable pre-publish |
| Schema validates: Service with `audience` + `areaServed`, FAQPage, BreadcrumbList | **Written out in `README.md`**, modelled on the telehealth page's graph. Needs validation after build |
| Yoast title ≤ 60, description ≤ 155, both distinct from parent and hub | **PASS** — 52 and 152 characters, counted |
| Performance and accessibility at 375 / 768 / 1280 / 1440 | **NOT VERIFIED.** No page exists to measure. Reported as unverified to the judge |
| One primary conversion action | **PASS** — "Book a demo", hero and closing band, same label |
| Analytics events verified firing manually | **NOT VERIFIED.** Events named in `README.md`, verification is a post-publish task |
| Every `[marker]` replaced, alt text everywhere | **Visual markers remain by design** (`[HERO]`, `[CONTEXT]`, `[COMPLIANCE]`, `[WORKFLOW]`, `[ACCURACY]`, `[CASE CARD]`, `[INTEGRATION]`) as briefs for the designer. Alt text is in `README.md`. No content placeholder is left in the copy |
| `fact-sheet.md` written | **PASS** |

**G-T: conditional pass.** Four items can only close after the page is built. They are listed in
`TODO.md` as blockers, and are reported to the blind judge as unverified.
