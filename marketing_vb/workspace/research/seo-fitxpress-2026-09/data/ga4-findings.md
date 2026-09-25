# GA4 findings: 3dlook.ai (FitXpress SEO/growth plan)

Pulled 2026-09-25 via `oo connector run google_analytics`. Read-only.
- **Property:** `GA4 3dlook`, ID **251675969**, stream `3dlook.ai` (G-NXNB16WGX6), timezone Europe/Kiev. The other 3DLOOK properties are client or app streams (YourFit, Mobile Tailor app, client widgets). `Keyword Hero - 3dlook.me` (392672847) is a separate legacy stream.
- **Periods used**
  - **L90** = 2026-06-27 … 2026-09-24
  - **Prior 90** = 2026-03-29 … 2026-06-26. **Not usable** (see §0).
  - **YoY** = 2025-06-27 … 2025-09-24
  - The 12/24-month trend runs to 2026-09-24. Sep 2026 is a partial month (24 days).
- Raw JSON dumps and the helper script are in `scratchpad/ga/`.

---

## 0. Tracking health: read this first

### 0.1 Page tracking was dead for 4.7 months (2026-02-05 → 2026-06-25)
Daily sessions fell from about 500–700/day to 10–50/day on **2026-02-05**. They came back on **2026-06-26** (224 → 400+/day). During the gap:
- `page_view` = 54 events in Mar–Jun combined
- `user_engagement` = 4

Only `session_start`, `first_visit`, `404_error` and the lead events kept firing. So the main GA4 tag was removed or blocked while other hits kept arriving: `ap_*` lead events and the 404 tracker, likely from a separate tag or plugin. Page-level data for Feb–Jun 2026 does not exist.
**Consequences:**
- The "last 90 vs prior 90" comparison is meaningless.
- Traffic comparisons have to be YoY.
- The January spike (12.9K sessions, Direct 4,040) is also suspect.

| Month | Sessions | Engaged | Key events |
|---|---|---|---|
| 2025-09 | 9,324 | 5,847 | 28 |
| 2025-10 | 8,906 | 5,732 | 31 |
| 2025-11 | 8,221 | 5,266 | 35 |
| 2025-12 | 7,428 | 4,804 | 27 |
| 2026-01 | 12,882 | 6,281 | 31 |
| 2026-02 | 2,855 | 1,016 | 39 |
| 2026-03 | 360 | 117 | 103 |
| 2026-04 | 344 | 99 | 100 |
| 2026-05 | 427 | 74 | 69 |
| 2026-06 | 1,749 | 710 | 93 |
| 2026-07 | 12,519 | 4,533 | 33 |
| 2026-08 | 11,839 | 4,343 | 28 |
| 2026-09 (24d) | 9,827 | 3,559 | 23 |

The key events for Mar–Jun are inflated by `get_14_day_trial`: 214 events from 99 users (60, 60, 42, 53 per month). The button hardly fires in normal months (1–8), so this looks like a bot or broken trigger.

Longer view: sessions were 16–17K/month in Sep–Nov 2024, 9.5K in Jun 2025, and 7.4K in Dec 2025. That is a structural decline of about 55% over 15 months, before any tracking break.

### 0.2 The re-installed tag (since 2026-06-26) measures differently
Engagement rate fell across the board, including on the same organic pages:
- Site: 64.5% YoY → 37.4% L90
- Organic: 66.8% → 42.9%
- Avg session duration, organic: 164s → 112s

`user_engagement` events halved (51.8K → 26.6K) while sessions rose. This is a measurement or implementation change, not a real behaviour shift. **Engagement-rate and time comparisons across YoY are not reliable**, but comparisons inside L90 are fine.

### 0.3 Bot and internal pollution in Direct
- **Direct = 16,924 sessions in L90, vs 5,775 YoY (×2.9)**. Its engagement rate is 31% and it is 79% desktop Chrome.
- Singapore Direct: 2,649 sessions, 5.5s average. 590 of them land on `/` at 1.3s average and 4.6% engaged. China Direct: 806. US Direct average: 42s.
- These are datacenter or bot patterns. **Treat roughly 3–5K of the L90 Direct sessions as non-human.**
- `/careers` Direct traffic (800 + job pages) is job-seekers.
- **No internal-traffic filter.** `staging.3dlook.me` and wp-admin previews are counted:
  - `/structured-body-data-for-telehealth-digital-health-programs/` shows 994 views, but **562 of them come from 3 users** referred by `staging.3dlook.me/wp-admin/post.php…`
  - The same happens on other FitXpress pages
  - The staging hostname itself logged 57 sessions in Jul and 17 in Sep

### 0.4 Conversion tracking is incomplete (key finding)
**Configured key events** (events with keyEvents > 0) in L90:

| Key event | L90 | YoY | Fires on |
|---|---|---|---|
| `ap_ContactUsLead` | 83 | 100 | `/contact-us/` only |
| `get_14_day_trial` | 4 | 1 | Mobile Tailor pages and home |
| `ap_EducationalLead` | 2 | 4 | `/content-hub/case-study-burlington-medical/` |
| `send_form` | 0 | 3 | legacy |

Historical note: until May 2025 the key events also included `send_form` (1,600–2,000/month, clearly over-firing) and `Registration` (120–150/month, YourFit). Both were dropped in June 2025. `ap_YourFitLead` and `ap_signUpPreCompleted` were also key events then. The "keyEvents" series before Jun 2025 is therefore not comparable.

**Conversion events that exist but are NOT key events (L90):**

| Event | Count (users) | Where |
|---|---|---|
| `form_submit` (enhanced measurement) | 298 (262) | `/contact-us/` 83; **`/pricing/` 51**; **home `/` 48**; `body-measurement-app-for-clothing` 26; **`ebook-the-digital-health-revolution` 22**; careers 25; `/fitxpress/for-connected-and-digital-fitness/` 4; `/structured-body-data-for-telehealth…` 4; `/for-bmi-verification/` 3; `/fitxpress/for-telehealth-and-weight-loss/` 2; misc. content 1–5 each |
| `form_start` | 503 (439) | contact 171, home 132, pricing 75 |
| `demo_button_click` | 259 (243) | **Mobile Tailor pages 227** (made-to-measure 159, uniforms 53, on-demand 15); **FitXpress pages 32** (`/for-bmi-verification/` 14, telehealth-weight-loss 10, connected-fitness 8) |

What this means:
- **Only the /contact-us/ form counts as a conversion.** Pricing, home, product-page and ebook forms (about 130–150 non-careers submits in L90) and all demo-button clicks are invisible in key events.
- The demo button's downstream outcome (booked meeting) is not tracked at all. The `form_name` and `button_name` custom dimensions exist but come through as `(not set)`, so forms can't be told apart.
- `form_submit` also includes careers applications (about 25), so it can't simply be promoted to a key event. Each form needs a named event.
- `ap_ContactUsLead` kept firing through the page-tracking outage, at 42, 39, 24 and 38 per month in Mar–Jun. That makes it the only continuous series. It shows **lead volume holding at about 25–40/month**, trending down: 2025 H1 averaged about 47/month; Jul–Sep 2026 averaged about 27/month. Spam share is unknown.

### 0.5 Broken URLs creating 404s (L90)
404s in L90: 669 events.
- `/contact/`: 111 views, 108 of them Direct. An external link or email signature points to `/contact/` instead of `/contact-us/`. **This is a lead-path leak.**
- `/content-hub/webinars/*`: 29+
- `/yourfit`: 29
- `/news`: 24
- A malformed internal link, `/https:/3dlook.ai/content-hub/ebook-the-digital-health-revolution/`: 16

---

## 1. Channel mix

### L90 (2026-06-27…09-24) vs YoY (2025-06-27…09-24)

| Channel | L90 sessions | L90 ER | L90 key ev. | YoY sessions | YoY ER | YoY key ev. | Δ sessions |
|---|---|---|---|---|---|---|---|
| Direct | 16,924 | 31% | 45 | 5,775 | 63% | 27 | +193% (bot-inflated) |
| Organic Search | 13,449 | 43% | 34 | 18,103 | 67% | 62 | **−26%** |
| Referral | 2,574 | 36% | 2 | 2,585 | 55% | 11 | 0% (YoY includes ChatGPT) |
| AI Assistant | 1,385 | 44% | 3 | n/a (channel didn't exist; about 1,700 inside Referral) | | | about −20% |
| Organic Social | 457 | 42% | 1 | 234 | 56% | 2 | +95% |
| Unassigned | 369 | 12% | 2 | 1,114 | 39% | 5 | −67% |
| Paid Social | 88 | 35% | 1 | 0 | | | |
| Organic Video | 64 | 50% | 1 | 69 | 62% | 1 | |
| Paid Search | 29 | 0% | 0 | 6 | | | |
| Email | 28 | 46% | 0 | 32 | 31% | 0 | |
| **Total** | **34,915** | 37% | **89** | **27,671** | 64% | **108** | +26% sessions / **−18% key events** |

- **Organic search is down 26% YoY** (18.1K → 13.4K) and **organic-sourced contact leads are down 47%** (59 → 31 `ap_ContactUsLead`).
- The headline session growth is Direct bot traffic.
- There is no meaningful paid activity.

### 12-month trend by channel (sessions)

| Month | Organic | Direct | Referral | AI Assistant | Org. Social | Unassigned |
|---|---|---|---|---|---|---|
| 2025-09 | 5,932 | 1,989 | 799 | – | 128 | 377 |
| 2025-10 | 5,647 | 1,931 | 801 | – | 72 | 406 |
| 2025-11 | 5,490 | 1,619 | 681 | – | 66 | 345 |
| 2025-12 | 4,817 | 1,629 | 613 | – | 95 | 260 |
| 2026-01 | 7,307 | 4,040 | 918 | – | 138 | 366 |
| 2026-02* | 1,321 | 1,212 | 200 | – | 34 | 78 |
| 2026-03* | 64 | 263 | 11 | – | 1 | 21 |
| 2026-04* | 25 | 281 | 18 | – | 1 | 18 |
| 2026-05* | 24 | 375 | 14 | – | 2 | 12 |
| 2026-06* | 656 | 855 | 136 | 52 | 17 | 23 |
| 2026-07 | 4,889 | 5,866 | 927 | 334 | 206 | 102 |
| 2026-08 | 4,421 | 5,699 | 871 | 555 | 147 | 87 |
| 2026-09 (24d) | 3,443 | 4,877 | 669 | 451 | 91 | 166 |

\* Tracking outage (§0.1).

Organic ran about 5.5–5.9K/month in autumn 2025 and about 4.4–4.9K/month in Jul–Aug 2026. September is pacing to about 4.3K, a further slide.

### AI assistants as referrers
In YoY these came through as Referral; in L90 GA4 labels them "AI Assistant" plus a few in Referral.

| Source | L90 sessions | L90 ER | L90 key ev. | YoY sessions | YoY key ev. | Autumn 2025 (09-27…12-25) |
|---|---|---|---|---|---|---|
| chatgpt.com | 1,233 | 47% | 3 | 1,441 | 7 | 1,327 (11 key ev.) |
| claude.ai | 91 | 39% | 0 | 65 | 0 | 28 |
| gemini.google.com + gemini | 79 | 40% | 0 | 29 | 0 | 27 |
| perplexity.ai + perplexity | 28 | 32% | 0 | 148 | 0 | 129 |
| copilot.com / copilot.microsoft.com | 10 | 50% | 0 | 16 | 0 | 15 |
| grok / deepseek / poe / you.com | 2 | | 0 | 15 | 0 | 0 |
| **Total AI** | **about 1,445** | | **3** | **about 1,715** | **7** | **about 1,500 (11)** |

Takeaways:
- AI referrals are about 4% of sessions and ChatGPT is 85% of them. They are flat to slightly down YoY. Perplexity collapsed (148 → 28); Claude and Gemini are growing from a small base.
- **AI assistants send people to fashion pages, not health pages.** L90 AI landing pages:

  | AI landing page | Sessions |
  |---|---|
  | `/` | 369 |
  | `/mobile-tailor` | 214 |
  | `/mobile-tailor/for-made-to-measure` | 136 |
  | `/technology` | 78 |
  | `/pricing` | 71 |
  | `/about-us` | 47 |
  | `3dlook-turns-two-photos-structured-body-data` | 36 |
  | `body-measurement-app-for-clothing` | 22 |
  | `mobile-body-scanning-accuracy` | 21 |

- No FitXpress or health page reaches 10 AI sessions: `ai-in-fitness-industry` 9, `ebook-the-digital-health-revolution` 6.
- AI-referred users click demo buttons 47 times, mostly on Mobile Tailor pages.
- **LLMs currently associate 3DLOOK with fashion and tailoring, not with health or body composition.**

---

## 2. Organic landing pages

### By topic bucket (Organic Search, landing page)

| Bucket | L90 sessions | L90 engaged | L90 ER | L90 key ev. | YoY sessions | YoY engaged | YoY ER | YoY key ev. |
|---|---|---|---|---|---|---|---|---|
| Home `/` | 4,878 | 2,452 | 50% | 16 | 8,397 | 6,362 | 76% | 29 |
| Fashion / Mobile Tailor (incl. YourFit) | 4,418 | 1,872 | 42% | 8 | 4,983 | 3,404 | 68% | 24 |
| Generic body measurement/scanning | 1,363 | 589 | 43% | 0 | 1,072 | 749 | 70% | 0 |
| **Health / fitness / FitXpress** | **1,188** | 540 | 45% | **0** | **1,532** | 1,080 | 70% | **0** |
| Corporate (pricing, contact, about, careers, technology) | 655 | 314 | 48% | 10 | 797 | 386 | 48% | 7 |
| (not set) | 810 | 14 | 2% | 0 | 1,101 | 20 | 2% | 2 |

How the buckets were built (pages classified by URL keyword):
- The health bucket covers about 48 URLs. It is **8.9% of organic sessions**.
- "Generic" means `virtual-body-measurements`, `3d-body-scanning`, `physiological-changes…`, `how-to-take-your-body-measurements-at-home` and similar. That intent is mostly consumer.

Conversion findings:
- **Organic health/FitXpress content produced 0 key events in both periods.** The organic key-event conversion rate for health content is 0.0% (0/1,188 sessions).
- The only non-key signals on health pages: `form_submit` about 20 (ebook 22 across all channels, `for-bmi-verification` 3, `structured-body-data` 4, fitxpress pages 6) and `demo_button_click` 32.
- Home plus Mobile Tailor produce 21 of 34 organic key events.
- `ap_ContactUsLead` is last-touch on `/contact-us/`, so health readers who later convert through contact-us are attributed to their session's landing page. For health landers that number is 0.

### Top organic landing pages, L90 (with YoY)

| Landing page | Bucket | L90 sess | L90 ER | L90 key ev. | YoY sess |
|---|---|---|---|---|---|
| `/` | home | 4,878 | 50% | 16 | 8,397 |
| `/mobile-tailor` | fashion | 1,961 | 40% | 5 | 1,562 |
| (not set) | | 800 | 2% | 0 | 1,101 |
| `/content-hub/body-measurement-app-for-clothing` | fashion | 727 | 41% | 0 | 644 |
| `/content-hub/virtual-body-measurements` | generic | 538 | 44% | 0 | 602 |
| `/content-hub/virtual-clothing-try-on` | fashion | 410 | 43% | 0 | 399 |
| `/content-hub/the-enormous-impact-of-daily-physiological-changes…` | generic | 300 | 40% | 0 | 222 |
| `/pricing` | corp | 286 | 49% | 5 | 367 |
| `/content-hub/3d-body-scanning` | generic | 230 | 46% | 0 | 106 |
| `/content-hub/visible-abs-myths-measurable-outcomes…` | health | 196 | 41% | 0 | – (new) |
| `/content-hub/body-scanning-technology-for-apparel` | fashion | 189 | 48% | 1 | 248 |
| `/content-hub/ar-clothing-try-on-tools` | fashion | 157 | 50% | 0 | 100 |
| `/content-hub/how-to-take-your-body-measurements-at-home` | generic/consumer | 155 | 44% | 0 | 57 |
| `/mobile-tailor/for-made-to-measure` | fashion | 129 | 49% | 0 | 92 |
| `/content-hub/ai-in-fitness-industry` | health | 112 | 38% | 0 | 249 |
| `/content-hub/body-fat-percentage-men-women-ai-3d-scanning-goals` | health | 93 | 31% | 0 | – |
| `/content-hub/ebook-the-digital-health-revolution` | health | 83 | 65% | 0* | – |
| `/content-hub/lean-body-mass-vs-muscle-mass` | health | 77 | 42% | 0 | – |
| `/content-hub/ai-body-scanners-vs-dexa-scans` | health | 75 | 43% | 0 | 108 |
| `/content-hub/inbody-vs-3dlook…` | health | 45 | 47% | 0 | 1 |
| `/content-hub/top-fitness-tech-companies` | health | 44 | 30% | 0 | 164 |
| `/for-bmi-verification` | FitXpress product | 36 | 53% | 0 | 29 |
| `/structured-body-data-for-telehealth-digital-health-programs` | FitXpress product | 32 | 50% | 0 | – (new) |
| `/content-hub/top-10-weight-loss-clinic-marketing-tips` | health | 31 | 39% | 0 | 50 |
| `/content-hub/ai-body-scanning-for-fitness` | health | 29 | 55% | 0 | **410** |
| `/content-hub/body-scanning-technology-for-weight-loss` | health | 27 | 59% | 0 | 111 |
| `/fitxpress/for-telehealth-and-weight-loss` | FitXpress product | 16 | 44% | 0 | 23 |
| `/fitxpress/for-connected-and-digital-fitness` | FitXpress product | 15 | 60% | 0 | 28 |
| `/fitxpress` (hub) | FitXpress product | – (gone) | | | 155 |
| `/yourfit` | fashion | – (404 now) | | | 667 (3 key ev.) |

\* Ebook forms fire `form_submit` (22) but that is not a key event.

**Health winners and losers YoY (organic landing sessions):**
- Losers:
  - `ai-body-scanning-for-fitness` −93% (410 → 29)
  - `top-fitness-tech-companies` −73% (164 → 44)
  - `ai-in-fitness-industry` −55% (249 → 112)
  - `body-scanning-technology-for-weight-loss` −76% (111 → 27)
  - `weight-loss-industry-overview` −82% (87 → 16)
  - The `/fitxpress` hub is gone (155 → 0)
- Winners are new body-composition explainers: `visible-abs` 196, `body-fat-percentage` 93, `lean-body-mass` 77, `inbody-vs-3dlook` 45. These are **consumer-intent topics** with ER 31–47% and zero conversions.
- The 2026 ICP articles barely register in organic L90 so far:
  - `online-pharmacy-bmi-verification` 12
  - `top-7-remote-body-composition-tools-glp-1-clinics` 14
  - `glp-1-market` 12
  - `visual-progress-tracking-glp1` 9
  - `fitxpress-data-privacy-security-regulatory-faq` 7
  - `occupational-health-screening-software` 4
  - `clinical-trial-anthropometric…` 3
  - `wellness-rewards-verification…` 2
  - `mobile-body-scanning-insurance-underwriting` 1

---

## 3. Conversions: where the 89 L90 key events come from
All but 6 of the 89 are `ap_ContactUsLead` on `/contact-us/`.

| Channel | ContactUsLead | Other key ev. |
|---|---|---|
| Direct | 42 | 3 (2 trial, 1 edu) |
| Organic Search | 31 | 3 (2 trial, 1 edu) |
| AI Assistant | 3 | 0 |
| Referral | 2 | 0 |
| Unassigned | 2 | 0 |
| Organic Social / Paid Social / Organic Video | 1 / 1 / 1 | 0 |

**Landing pages of converting sessions (L90):**

| Landing page | Channel | Key events | Sessions |
|---|---|---|---|
| `/contact-us` | Direct | 22 | 311 |
| `/` | Organic | 16 | 4,878 |
| `/` | Direct | 8 | 4,531 |
| `/pricing` | Direct | 6 | 1,458 |
| `/mobile-tailor` | Organic | 5 | 1,961 |
| `/pricing` | Organic | 5 | 286 |
| `/contact-us` | Organic | 4 | 45 |
| `/contact-us` | AI Assistant | 2 | 12 |
| `/mobile-tailor` | Direct | 2 | 1,043 |
| `/content-hub` | Direct | 2 | 141 |
| Other rows | | 1 each | |

Among the 1-event rows: `body-scanning-technology-for-apparel`, `size-recommendation-tools`, `mobile-tailor/for-uniforms`, `made-outdoor case study`, `mobile-tailor-is-here`, `/technology`, `/about-us`, `/case-studies`.

Conversion rates and patterns:
- **No health, FitXpress or GLP-1 landing page appears as a converting landing page in L90 or YoY.**
- Organic key-event rate overall: 34 / 13,449 = **0.25%** (YoY 62 / 18,103 = 0.34%).
- Home organic: 0.33%. `/pricing` organic: 1.7%. Health content: **0%**.
- Device: desktop generates 29 of 34 organic key events and mobile only 4, even though mobile is 45% of organic sessions. B2B converts on desktop.

---

## 4. Organic by country and device

| Country | L90 organic sess | L90 ER | L90 key ev. | YoY sess | YoY key ev. | Δ |
|---|---|---|---|---|---|---|
| United States | 2,982 | 43% | 9 | 3,096 | 14 | −4% |
| **India** | **2,591** | 41% | 7 | 2,992 | 12 | −13% |
| United Kingdom | 797 | 41% | 2 | 1,205 | 2 | −34% |
| Australia | 379 | 44% | 2 | 509 | 2 | −26% |
| Canada | 366 | 42% | 1 | 479 | 0 | −24% |
| Italy | 341 | 61% | 0 | 201 | 1 | +70% |
| Germany | 288 | 46% | 1 | 415 | 3 | −31% |
| Brazil | 232 | 42% | 0 | 260 | 0 | |
| Pakistan | 223 | 46% | 1 | 249 | 2 | |
| Nigeria | 219 | 43% | 0 | 185 | 2 | |
| France | 213 | 42% | 1 | 259 | 1 | |
| Indonesia | 200 | 44% | 0 | 589 | 0 | −66% |
| Ukraine | 196 | 57% | 0 | – | | |
| Philippines | 195 | 35% | 0 | – | | |
| Saudi Arabia | 112 | 45% | 0 | **1,271** | 2 | **−91%** |
| Iraq / Egypt / Algeria | <100 each | | 0 | 326 / 234 / 188 | 2 | collapsed |

Geography:
- Core ICP geos (US, UK, CA, AU) are **4,524 / 13,449 = 34%** of organic sessions in L90 and produce 14 of 34 organic key events.
- **Non-ICP consumer geos dominate.** India alone is 19% of organic, and the long tail (PK, NG, ID, PH, BR, VN, TR, and others) adds more than 25%.
- The YoY drop is concentrated in the Middle East and Southeast Asia (SA, Iraq, Egypt, Algeria, Indonesia). That is the consumer "3D body shape" home-page traffic identified earlier.
- Google Translate proxy traffic (`3dlook-ai.translate.goog`) fell from about 850/month to about 60/month, which fits the same pattern.
- US organic is nearly flat (−4%). The UK is down 34%.

Device (organic):

| Device | L90 sess | L90 ER | L90 key ev. | YoY sess | YoY ER | YoY key ev. |
|---|---|---|---|---|---|---|
| Desktop | 7,128 | 50% | 29 | 6,162 | 62% | 51 |
| Mobile | 5,995 | 36% | 4 | 11,757 | 70% | 11 |
| Tablet | 147 | 44% | 1 | 132 | 77% | 0 |

- Mobile organic halved (−49%). That is the consumer traffic leaving.
- Desktop organic grew (+16%) but its key events fell from 51 to 29.

---

## 5. FitXpress-specific pages (all channels, page views, L90 vs YoY)

| Page | L90 views | L90 users | Avg eng. s/user | YoY views | Notes |
|---|---|---|---|---|---|
| `/pricing/` (shared FitXpress + Mobile Tailor) | 4,721 | 3,474 | 36 | 4,214 | 51 form submits, **0 key events** |
| `/contact-us/` | 1,046 | 822 | 30 | 1,430 | the only key-event page (83) |
| `/structured-body-data-for-telehealth-digital-health-programs/` | 994 | 266 | 94 | – (new) | **562 views from 3 internal users (staging preview)**; real traffic about 430 views: direct 279, google 105, chatgpt 20 |
| `/for-bmi-verification/` | 242 | 200 | 23 | 342 | 14 demo clicks, 3 form submits |
| `/fitxpress/for-connected-and-digital-fitness/` | 238 | 185 | 38 | 324 | 8 demo clicks, 4 form submits |
| `/fitxpress/for-telehealth-and-weight-loss/` | 136 | 97 | 34 | 459 | **−70%**; 10 demo clicks, 2 form submits |
| `/fitxpress/` (hub) | 0 | – | – | 536 | removed or redirected; no longer receives traffic |
| `/content-hub/ebook-the-digital-health-revolution/` | 359 | 305 | 17 | – | 22 form submits (ebook gate), not a key event |
| `/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/` | 99 | 70 | 31 | – | |
| `/content-hub/top-7-remote-body-composition-tools-glp-1-clinics/` | 77 | 59 | 35 | – | |
| `/content-hub/glp-1-market/` | 75 | 47 | 33 | 13 | |
| `/content-hub/fitxpress-data-privacy-security-regulatory-faq/` | 68 | 37 | 63 | – | |
| `/content-hub/fitxpress-admin-panel-launch/` | 65 | 50 | 15 | – | |
| `/content-hub/occupational-health-screening-software/` | 65 | 55 | 15 | – | |
| `/content-hub/visual-progress-tracking-glp1-adherence-retention/` | 29 | 27 | 8 | – | |
| `/content-hub/glp-1-compliance-challenge/` | 28 | 26 | 18 | 19 | |
| `/content-hub/accuracy-drives-roi-digital-health/` | 13 | 13 | 3 | – | |
| `/content-hub/manual-vs-digital-intake-occupational-health-screening/` | 13 | 6 | 84 | – | new |
| `/fitxpress-customer-terms-conditions/` | 62 | 50 | 11 | 38 | existing-customer signal |

Total views across all FitXpress product pages:

| Pages | L90 views | YoY views |
|---|---|---|
| hub + telehealth + fitness + BMI | 616 | 1,661 |
| Adding structured-body-data (excluding staging) | about 1,050 | 1,661 |

That is about −37% YoY even with the new page counted.

**Paths into FitXpress pages** (pageReferrer, L90):
- Most internal entries come from the home page (`/` → structured-body-data 86, → bmi 44, → connected-fitness 43, → telehealth 40).
- Next are `/pricing/` (28 / 19 / 13 / 12) and `/technology/` (20 / 22 / 13 / 7).
- The FitXpress pages link to each other (structured → connected-fitness 29; connected-fitness → bmi 22).
- **Almost no health blog article passes readers to a FitXpress product page.** The only visible one is `glp-1-compliance-challenge` → structured-body-data (7).
- Google is the direct referrer for only 38 (structured), 36 (bmi), 16 (telehealth) and 14 (fitness) views.
- No docs or API pages are on 3dlook.ai in this property. No `/demo` page exists: demo is a button (`demo_button_click`) whose result is not tracked.

---

## Decision-relevant takeaways
1. **Fix measurement before judging SEO.**
   - Page data is missing for 2026-02-05…06-25.
   - Direct is inflated by about 3–5K bot sessions (Singapore, China) and there is no internal-traffic filter (staging).
   - Only `/contact-us/` is a key event. Pricing, home and product-page forms, the ebook gate and demo-button clicks or bookings are not.
   - Custom dimensions `form_name` and `button_name` come through as `(not set)`.
   - `/contact/` 404s 111 times.
2. **Health content brings traffic but no leads.** Health, fitness and FitXpress pages are 8.9% of organic (1,188 sessions) with 0 key events in both periods. The new body-composition explainers attract consumer intent. The ICP articles (GLP-1, pharmacy BMI, occupational health, insurance) have under 15 organic sessions each.
3. **FitXpress product pages are losing ground:** about −37% views YoY, `/fitxpress` hub gone, `for-telehealth-and-weight-loss` −70%. Blog-to-product internal linking is almost absent.
4. **Organic −26% YoY, organic leads −47% YoY.** The loss is concentrated in mobile consumer geos (SA, ID, Iraq, Egypt). US is flat, UK −34%. Only 34% of organic is from ICP geos; India is 19%.
5. **AI assistants (about 4% of sessions, 85% ChatGPT) send people to Mobile Tailor and home pages, not FitXpress.** In LLMs, 3DLOOK is still a fashion brand.
