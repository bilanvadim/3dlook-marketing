# Microsoft Clarity — 3dlook.ai (FitXpress SEO/CRO support)

**Window:** last 72 h as of the pull on 2026-09-25 (about 2026-09-22 → 09-25 UTC). This is the only window the Data Export API offers (1–3 days max), so **the sample is small**. Most FitXpress and health pages have 10–20 real sessions or fewer. Read the numbers as signals to check, not conclusions.
**Source:** `oo connector run microsoft_clarity -a export_live_insights`. 8 API calls were made, and the raw JSON is in `scratchpad/clarity/01…08_*.json`.
**Units:** engagement time is shown as average seconds per session (total / active). Scroll depth is an average %. For dead, rage, quickback and script errors, the tables show "% of sessions with the event / event count".
**Connector limitation:** `Country/Region` as a breakdown dimension is **silently ignored**. Calls 06 (Country+Device) and 08 (URL+Country) came back as Device-only and URL-only data. Country is only available as the overall top-10 list from call 01.

## 1. Overall (72 h)

| Metric | Value |
|---|---|
| Real sessions | **1,037** (distinct users 2,765 incl. bots) |
| Bot sessions (Clarity-flagged, excluded from all metrics) | **1,792 → 63% of all sessions** |
| Pages / session | 1.32 |
| Avg scroll depth | **37%** |
| Engagement time | 253 s total / **69 s active** |
| Dead clicks | 6.35% of sessions, 191 clicks |
| Rage clicks | 0.3% of sessions, 17 clicks (12 on one careers page) |
| Quickbacks | 3.6% of sessions, 57 |
| Excessive scroll | 0 |
| Script errors | **9.4% of sessions, 284 errors** |
| Error clicks | 1 (homepage, mobile, organic) |

Top real-session countries: US 232, India 119, Ukraine 69, Italy 67, UK 56, Poland 56, Canada 39, Germany 31, France 25, Pakistan 24. **Singapore and China are not in the top 10 of real sessions.** This matches Clarity classifying the GA4-suspect SG/CN direct ~5 s sessions as bots, but the connector can't break bots down by country, so this is not confirmed.

## 2. Bots

| Segment | Real | Bots | Bot share |
|---|---|---|---|
| Channel "Other" (no referrer, no UTM) · PC | 248 | **1,642** | 87% |
| Channel "Other" · Mobile | 58 | 49 | 46% |
| **PaidSearch (google / cpc)** | **0** | **47** | **100%** |
| OrganicSearch (all devices) | 372 | 13 | 3% |
| Direct (= source `3dlook.ai`, internal referrer) | 295 | 5 | 2% |
| AiPlatform (chatgpt 43, claude 2, copilot 1) | 46 | 0 | 0% |

- Bots come in with **no referrer on desktop**, which fits the GA4 "direct ~5 s" pattern. GA4 almost certainly counts part of this as Direct, so GA4 Direct numbers and anything built on them (engagement rate, conversion rate) are inflated or diluted.
- **All 47 google/cpc sessions are bots.** They could be AdsBot landing-page checks or click fraud. Either way, Clarity saw **zero human paid-search sessions** in 72 h. Check Google Ads clicks against this.
- Bot share per page is highest on content-hub articles. Many health articles have more bot sessions than real ones, for example the FitXpress privacy FAQ (18 bots vs 6 real), bariatric (12 vs 8), glp-1-market (12 vs 2), top-7 GLP-1 tools (11 vs 4), ai-body-data-health-hub (11 vs 3) and online-pharmacy BMI guide (10 vs 4). /for-bmi-verification/ has 10 bots vs 10 real, telehealth 15 vs 20, and connected-fitness 13 vs 11.

## 3. FitXpress, pricing and contact pages

| Page | Real sess | Bots | Scroll | Time tot/act (s) | Dead | Rage | Quickback | Script err |
|---|---|---|---|---|---|---|---|---|
| / (homepage, FitXpress parent) | 300 | 133 | 33% | 148 / 45 | 7% / 33 | 0 | 4% / 14 | 7% / 39 |
| /structured-body-data-for-telehealth-digital-health-programs/ | 20 | 15 | **28%** | 771 / 174 | 0 | 0 | 5% / 2 | **20% / 14** |
| /for-bmi-verification/ | 10 | 10 | **28%** | 212 / 23 | **20% / 12** | 0 | **20% / 2** | 10% / 2 |
| /fitxpress/for-connected-and-digital-fitness/ | 11 | 13 | 59% | 437 / 129 | **18% / 13** | 0 | 0 | 18% / 4 |
| /pricing/ | 124 | 24 | 43% | 194 / 52 | **10% / 39** | 2% / **5** | 5% / 7 | **21% / 68** |
| /contact-us/ | 16 | 11 | 64% | 107 / 60 | 0 | 0 | 12% / 2 | **31% / 10** |
| /technology/ | 39 | 13 | 39% | 461 / 293 | 0 | 0 | 8% / 3 | 21% / 16 |
| /contact/ (404) | 0 | 0 | — | — | — | — | — | — |

**By device (focus pages):**

| Page · device | Sess | Scroll | Act (s) | Dead | Script err |
|---|---|---|---|---|---|
| /pricing/ · PC | 90 | 42% | 57 | 12% / 36 | 19% / 40 |
| /pricing/ · Mobile | 33 | 45% | 37 | 6% / 3 | **27% / 28** |
| / · PC | 214 | 34% | 56 | 7% / 21 | 6% / 23 |
| / · Mobile | 79 | 31% | 19 | 6% / 10 | 10% / 15 (+1 error click) |
| telehealth · PC | 16 | 26% | 214 | 0 | 19% / 6 |
| telehealth · Mobile | 4 | 30% | **11** | 0 | **25% / 8** (2 quickbacks) |
| BMI verification · PC | 8 | 30% | 25 | 12% / 11 | 12% / 2 |
| BMI verification · Mobile | 2 | 16% | 13 | 50% / 1 | 0 (1 quickback) |
| connected fitness · PC | 10 | 52% | 117 | 20% / 13 | 10% / 2 |
| /contact-us/ · PC | 12 | 68% | 76 | 0 | **42% / 10** |
| /contact-us/ · Mobile | 3 | 58% | 11 | 0 | 0 |

**By channel (where the traffic comes from):**
- The FitXpress pages get **almost no organic search** in this window. Telehealth has 17 Direct, 2 Other and **1 organic** session (and that one had 100% quickback plus 8 script errors). BMI verification has 10 Direct and **0 organic**. Connected fitness has 6 Direct, 3 Other, 2 AI platform and 0 organic. All their traffic is internal navigation from the site (Clarity labels it "Direct" with source `3dlook.ai`).
- /pricing/ has 101 of 124 sessions arriving internally (Direct). These carry most of the friction: **dead 11% / 37, rage 5, script errors 25% / 56**. Organic reaches pricing only 8 times.
- The homepage gets 144 organic sessions with 11% dead-click sessions (24 clicks), 30 Direct and 114 "Other".

**What this suggests.** Only recordings or heatmaps can confirm it, but the pattern points to the pricing page:
- Pricing has most of the site's dead clicks (39 of 191) and most of its rage clicks outside careers (5).
- It also has about 24% of all script errors (68 of 284).
- Pricing and contact-us have the highest script-error rates of any commercial page (21% and 31%, 42% on contact-us desktop).

This fits the known issue that the **JS-driven demo/"Contact sales" buttons** sometimes fail or do nothing, and the **contact form's embedded script (HubSpot or similar) throws errors**. BMI verification and connected fitness show dead clicks concentrated in 1–2 sessions (12 and 13 clicks), meaning one user tried the same element repeatedly. That is typical of a non-link element that looks like a button, or a demo CTA that didn't open.

## 4. Health articles: do readers reach the CTA?

| Article | Real | Bots | Scroll | Act (s) | Main channel |
|---|---|---|---|---|---|
| ai-body-scanners-vs-dexa-scans | 7 | 10 | 32% | 99 | organic 7/7 |
| manual-vs-digital-intake-occupational-health-screening | 7 | 7 | **19%** | 33 | Direct 6 |
| fitxpress-data-privacy-security-regulatory-faq | 6 | 18 | 45% | 23 | Direct 4 |
| fitxpress-admin-panel-launch | 5 | 8 | 52% | 12 | Direct 5 |
| the-potential-of-ai-in-telehealth | 4 | 8 | **5%** | 0 | Other |
| top-7-remote-body-composition-tools-glp-1-clinics | 4 | 11 | 29% | 13 | organic 2, Direct 2 (4% scroll) |
| glp-1-compliance-challenge | 4 | 8 | 23% | 3 | Other |
| online-pharmacy-bmi-verification-a-2026-compliance-guide | 4 | 10 | **18%** | 24 | Direct 2 (5% scroll) |
| body-fat-percentage-men-women-ai-3d-scanning-goals | 4 | 7 | 36% (mobile 4%) | 11 | organic 4 |
| bariatric-pre-qualification-mobile-3d-body-scanning | 8 | 12 | **18%** | 23 | Direct 4, referral 4 |
| body-scanning-technology-for-weight-loss | 4 | 8 | 62% | 34 | — |
| remote-body-measurement-online-fitness-coaching | 3 | 12 | 37% | 7 | Direct |
| ai-body-data-wellness-platforms | 3 | 10 | **10%** | 7 | Direct |
| ai-body-data-health-hub | 3 | 11 | **9%** | 2 | Direct |
| glp-1-market | 2 | 12 | **6%** | 4 | Direct |

**Average scroll on health articles is about 5–35%, with active time usually under 30 s.** Most health articles end their CTA or product link in the last 20–30% of the page, and at these depths almost nobody gets there. The one high-intent organic article (DEXA comparison) holds attention at 99 s active, but readers still stop at about a third of the page. This matches GA4's "impressions, 0 conversions". **The CTA has to appear above the 30% line**, as an inline FitXpress box after the intro or first H2 plus a sticky or sidebar CTA. Several "Direct" article sessions have 4–10% scroll, which looks like internal team checks and further dilutes the real-reader signal.

## 5. Devices

| Device | Real | Bots | Scroll | Time tot/act (s) | Dead | Quickback | Script err |
|---|---|---|---|---|---|---|---|
| PC | 667 | 1,659 | 39% | 333 / 88 | 7% / 159 | 3% | 8% / 175 |
| Mobile | 325 | 51 | 34% | 100 / **31** | 4% / 30 | 4% | **12% / 106** |
| Tablet | 7 | 1 | 51% | 72 / 39 | 29% / 2 | 0 | 14% |

Mobile is about 1/3 of real traffic. It has **a third of the active time and a higher script-error rate**, especially on pricing (27%) and Direct-mobile overall (32%). Organic mobile is almost as large as organic desktop (183 vs 184 sessions) but engages much less (28 s vs 51 s active).

## 6. What blocks conversions (ranked)

1. **Pricing and contact JS errors plus dead clicks** on the demo/contact CTAs: pricing 21% of sessions with errors, contact-us 31%, pricing 39 dead clicks and 5 rage clicks. This is the only real friction cluster on the money path.
2. **FitXpress pages get no organic entry.** Their sessions are internal hops (telehealth 1 organic, BMI 0, connected fitness 0), so SEO fixes on those URLs are the lever, not CRO.
3. **Health articles are read to about 20–35% at most**, so end-of-article CTAs are never seen.
4. **Mobile under-engages** (31 s active) and has more script errors.
5. **Traffic quality.** 63% of sessions are bots, including 100% of google/cpc. Paid-search spend should be checked, and GA4 needs bot-filtered segments before conversion rates mean anything.
6. /contact/ still gets hits: 0 real sessions in the window but listed in the data. Redirect it to /contact-us/ (already known from GA4).

## 7. What the API cannot tell us

- Not available through the API: **which element** got the dead or rage clicks, **error messages or stack traces**, recordings, heatmaps (click, scroll, attention), funnels, form or field drop-off, and Smart Events or goal conversions.
- Bot sessions by country or page are not available. The API gives only bot totals per breakdown, and the country dimension is broken in the connector.
- No history beyond 72 h, so there are no trends or before/after comparisons.

## 8. What to check manually in the Clarity UI (last 30 days, filter "exclude bots")

1. **/pricing/ heatmap → Click map + "Dead clicks" and "Rage clicks" layers** (desktop and mobile separately). Identify the dead element: plan cards, the "Book a demo" / "Contact sales" buttons, or toggles.
2. **Recordings filtered by Page = /pricing/ AND "JavaScript errors" = yes**, then open the error tab in the player to read the actual error. Do the same for **/contact-us/** and watch whether the form renders and submits.
3. **Dashboard → JavaScript errors** widget: list the top error messages and which script they come from (form embed, chat widget, analytics tag).
4. **Scroll heatmaps** on the telehealth page, /for-bmi-verification/, /fitxpress/for-connected-and-digital-fitness/ and 3–4 health articles (DEXA, online-pharmacy BMI guide, top-7 GLP-1 tools, bariatric). Note the % line where the CTA or product link sits against the average fold (about 30%).
5. **Recordings: /for-bmi-verification/ and /fitxpress/for-connected-and-digital-fitness/ with "Dead clicks"** (only 1–2 sessions each). Find the element clicked 12–13 times.
6. **Smart Event / funnel**: define "Demo CTA click" (click on the demo button selector) → contact-us page → form submit. Clarity funnels need this set up in the UI.
7. **Settings → Bot detection** is on (it is, since bots are being excluded). Compare **Filters → Traffic → Paid search** sessions against Google Ads clicks for the same days.
8. **Filter Country = Singapore / China** in recordings to confirm they are flagged as bots or are 0-second sessions.
9. **Mobile recordings from organic on the homepage**: there is 1 error click and 19 s active time, so check whether the hero CTA or nav works on mobile.
10. **Filter out internal traffic** (Ukraine/Poland IPs, `staging.3dlook.me`, `localhost` referrers) with a Clarity custom tag or IP filter, so team visits stop polluting Direct-channel metrics.
