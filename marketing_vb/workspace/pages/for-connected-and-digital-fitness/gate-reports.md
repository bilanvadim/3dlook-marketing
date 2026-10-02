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
