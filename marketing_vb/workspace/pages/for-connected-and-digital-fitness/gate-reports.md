---
product: fitxpress
type: gate-reports
vertical: connected-and-digital-fitness
date: 2026-10-02
---

# Gate reports: /fitxpress/for-connected-and-digital-fitness/

## G-I · Should this page exist

| Check | Result |
|---|---|
| Use-case file | ✅ `brand-assets/product-info/use-cases/fx-digital-fitness.md` (thin: 158 words; Nika's ICP card in the Drive doc is richer and was used for buyer titles and pains) |
| 2+ publishable cases from this vertical | **G-I: standing FX waiver 2026-09-27.** No fitness case exists in `case-studies/`. Stand-ins used: the workflow itself, anonymised `proof-points.md` figures, the accuracy framework, the trust FAQ. No invented or implied case |
| Demand | ✅ content-plan Hub 1 (Fitness); keyword map §2: `gym body scanner` cluster ~220/mo US, KD 1-11; HubSpot AEO prompts 51-81% for the Connected Fitness ICP |
| 5 facts absent from the parent | ✅ day-30 app retention (Adjust); 100-day abandonment and personalization (JMIR); App Store privacy details and Google Play Data safety for health and fitness data; the in-gym scanner comparison; the cohort-and-holdout pilot measured in day-30/day-90 retention and free-to-premium conversion; the coach view in online coaching apps |
| BD owner confirms the objections differ | ⚠️ Not asked. Nika's ICP card names the objections (Prism Labs' public sandbox: "why can't I test it myself?"). Open item |
| Parent and URL | ✅ `/fitxpress/` + `/fitxpress/for-connected-and-digital-fitness/` (live; keeps its URL, site-inventory migration rule 3) |
| 60% uniqueness | ✅ Shared with the parent: the record table's output list and the data lines. Unique: hero, problem, three steps, comparison, pilot, FAQ (about 70% of paragraphs) |

## G-A · Architecture

| Check | Result |
|---|---|
| Placed | ✅ Child of `/fitxpress/`; siblings linked in body: telehealth page (live root URL), `/for-bmi-verification/` |
| Cannibalisation | ✅ `gym body scanner` is owned by no article (keyword map §2). The hub `ai-in-fitness-industry` keeps "ai fitness"; `connected-fitness-industry` keeps "connected fitness"; "body composition" without a vertical stays with Hub 9. The title differs from the hub's |
| Inbound links | `landing-map.md` already lists this URL as `live` for Hub 1 (and as the stand-in for Hub 5 Wellness): every Hub 1 article links here. Request the in-body card on `/fitxpress/` when it ships |
| Search Console baseline | ✅ Captured 2026-10-02 for 2026-07-01…09-30: **677 impressions, 10 clicks, average position 15.2**. Queries are brand only ("fitxpress" 47 impressions, pos 5.0; typos; `site:` queries). Nothing to lose on non-brand queries |

## G-T · Technical (before publish)

Not taken: the page is not built in WordPress. Specified: canonical to self, Yoast title 57 and
description 150 characters, Service + FAQPage + BreadcrumbList in `page.html`. To verify on the build:
Rich Results Test, viewports 375/768/1280/1440, contrast, analytics events from the shared form.

## Dropped or changed slots

| Slot | Decision |
|---|---|
| 10 · Cases from this vertical | Dropped under the standing FX waiver. Nothing implied in its place |
| 11 · Customer quote | Dropped: no approved quote from this vertical |
| 2 · Problem numbers | Three figures, two of them from Adjust (day 1 and day 30). No second neutral source on fitness churn was found; one candidate study found self-monitoring did not predict app use |
| 13 · FAQ | Four questions. "What's the best alternative to hardware 3D body scanners for fitness studios?" (AEO 51%) was cut as a repeat of the comparison block's closing line |
| 16 · Sibling cards | No "keep reading" block, as on the final insurance page; siblings are linked in the pilot block's proof sentence |

## G-J · v3 (2026-10-06), page-v3-2026-10-06.md, 100-point scale since 2026-10-06

| Round | Total | Hard fails | Lowest | Applied |
|---|---|---|---|---|
| 1 | 69 | "validated capture" (guardrail #3) | place_and_technical | hard fail; sibling links; "only FitXpress" dropped; canonical identifiers line; accuracy answer first; recommended setup; jargon; onboarding FAQ answers directly |
| 2 | 71 | none | proof_of_belonging | one_fix (fitness logos or an anonymised fitness figure) **not applicable**: no fitness case or cleared logo exists; H1 hedged ("help retain"); 3D model removed (not on Starter, live /pricing/); Kidman study title; benefit cells rewritten; data-line fragment fixed; third accuracy figure dropped |
| 3 | 73 | none | place_and_technical | stop rule reached |

**Gate not taken: 73/85 after 3 rounds (69, 71, 73), weakest axis = place_and_technical** (G-T items that
only the WordPress build can measure: contrast, keyboard, 768/1440, analytics, Rich Results; the
redirecting /fitxpress/ parent). Post-round-3 fixes without rescoring: breadcrumb middle level unlinked
in the prototype (kit slot 1), Adjust restated as "by day 30, most users of health and fitness apps are no
longer active", the acquisition-spend line made conditional, the illustrative 3.4 cm no longer used as a
yardstick, a named subject in the comparison sentence. Detector CLEAN, ~1,335 words.
