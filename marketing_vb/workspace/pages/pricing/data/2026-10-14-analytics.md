# /pricing/ — analytics pull (2026-10-14)

Scope: `https://3dlook.ai/pricing/` only. Read-only pulls. Raw JSON and the saved HTML are in the session scratchpad (`…/scratchpad/pricing/{gsc,ga,clarity,ah,live}`), not in the repo.

| Source | Window | How |
|---|---|---|
| GSC | **L3M** 2026-07-13 → 10-11 · **P3M** 2026-04-13 → 07-12 · **YoY** 2025-07-13 → 2025-10-11 · monthly trend 2025-06 → 2026-10-11 | `oo connector run google_search_console -a query_search_analytics`, `sc-domain:3dlook.ai`, page **equals** `https://3dlook.ai/pricing/` |
| GA4 | **L90** 2026-07-15 → 10-13 · **YoY** 2025-07-15 → 2025-10-13 · monthly 2025-01 → 2026-10-13 | `oo connector run google_analytics -a run_report`, property 251675969 |
| Clarity | last 72 h, ≈ 2026-10-11 14:00 → 10-14 14:00 UTC | `microsoft_clarity export_live_insights`, 3 calls (URL×Device, URL×Channel, URL×Source) |
| Ahrefs | data date 2026-10-13 | API v3, ~2,500 units (215,746 → 218,268 of 800K) |
| Live page | 2026-10-14 ~14:27 UTC | one curl of the HTML + one headless Chromium load (390×844) |

---

## 1. Live page as of 2026-10-14 (facts)

**Head:** title `3DLOOK Pricing | FitXpress & Mobile Tailor Plans` · meta description `Get flexible body measurement prices with 3DLOOK to suit any business. Sign up for a 7-day trial or request a demo.` (same text in og:description and in the WebPage JSON-LD) · canonical self · og:type `article` · JSON-LD: WebPage, ImageObject, BreadcrumbList, WebSite, Organization. **No Product/Offer and no FAQPage schema.** WordPress template `page-pricing-redesign-2026`.

**Structure.** One H1 `Our Pricing`, plus an H2 `Our Pricing` (two hero blocks are stacked; the Mobile Tailor hero sits at `opacity: 0` over the FitXpress one). Each plan card is in the HTML **twice** (two `#pricing_plan` sections with the same id), so every H3 appears twice. H2s: Our Pricing; Recognized by customers and industry experts; Frequently asked questions ×2 (one per product); "Maximize Mobile Tailor Benefits with Premium Features" (contact modal); "Shape the Future of Health and Fitness Tech" ×3 (demo modals for Starter / Pro / Personalized).

**Default tab (checked in a real browser):** plain `/pricing/` opens on **FitXpress** (dark theme, Starter/Pro/Personalized, FitXpress FAQ). `/pricing/?mt` opens Mobile Tailor. The Mobile Tailor menu links to `?mt`; the main header "Pricing" and the footer link go to plain `/pricing/`.

**Monthly / Annual toggle.** "save up to 20%". Annual values are in `data-year` (yearly totals).

### FitXpress tab (default)

| Plan | Monthly | Annual (`data-year`) | Volume as written | CTA → target | Features as listed |
|---|---|---|---|---|---|
| **Starter** — badge "Recommended" | $1 000/month | $10,800/yr · "Save 10%" | Up to 500 scans per month | Book a demo → `#bd-modal-starter` (HubSpot form modal) | Body composition metrics, including BMI, BMR, Fat %, Lean mass · 80+ body measurements · Predicted weight · API access + Web & Mobile SDKs · Guided implementation support |
| **Pro** | $1 500/month | $14,400/yr · "Save 20%" | Up to 1000 scans per month | Book a demo → `#bd-modal-pro` | Starter + 3D Body progress tracking + 3D Goal Visualization |
| **Personalized** | $Custom/month | Custom | Scalable scan volumes | Talk to sales → `#bd-modal-personalized`, "We'll respond within 1 business day" | Pro + Flexible scan volumes (1000+ per plan) · Multilingual guided capture flow · Dedicated customer support · Exclusive annual plan discounts |

### Mobile Tailor tab (`?mt`)

| Plan | Monthly | Annual | Volume | CTA → target | Features |
|---|---|---|---|---|---|
| **Basic** | $499/month | $5,389/yr · "Save 10%" | Up to 100 scans per month | Sign up for a trial → `mtm.3dlook.me/accounts/signup` | 80+ Measurements · Data Export CSV · 3D Model View · 3D Model Export · Web Widget Integration · Basic Support |
| **Premium** — badge "Best Deal" | $999/month | $9,590/yr · "Save 20%" | Up to 500 scans per month | Start a Trial → same signup | Basic + Web Widget Customization · Real-Time Notifications · SMS/Email Templates · Premium Support |
| **Enterprise** | $Custom/month | Custom | 500+ scans per month | **"Start a Trial" → `#modal-pricing-contact`** (a contact form, not a trial) | Premium + API and SDK (web and mobile) · Dedicated Support |

### Copy and link problems found on the live page

| # | What | Where |
|---|---|---|
| 1 | "Sign up for a 7-day trial" — meta description, og:description, JSON-LD, and the **footer CTA heading on the FitXpress view**. FitXpress has no self-serve trial (decision 09-27, 10-14). The footer button under it, "Let's talk", links to `/pricing/` itself. | head + footer |
| 2 | FitXpress FAQ: "FitXpress **maintains HIPAA compliance** and adheres to GDPR principles" — "HIPAA compliant" is a hard fail in new text (trust FAQ is the compliance source). | FAQ "How secure is the data?" |
| 3 | FitXpress FAQ: "approximately 96-97% accuracy … and 95%+ repeatability". 96–97% is canon but must be worded verbatim from `accuracy-formulations.md`; **"95%+ repeatability" is explicitly not published** (CLAUDE.md §1, since 2026-09-02). | FAQ accuracy |
| 4 | Shared FAQ: "With over 80 long-term customers" — public claim is "100+ clients"; "eight years of development" — check. | FAQ "What sets … apart" |
| 5 | Processing time contradicts itself: "under 40 seconds" vs "all in under 45 seconds". | FAQ scan time vs metrics |
| 6 | Volumes are sold as "scans", while the API bills four request types against one pool (scan, predicted model, 3D progress, 2D progress render). "Predicted weight" reads as a forecast. 2D progress renders are not mentioned. | FX cards |
| 7 | Prices typed with a space separator ("$1 000", "$1 500") and "$Custom/month". | cards |
| 8 | Awards strip is fashion/retail-era only (Gartner Hype Cycle Retail 2021, Digiday in-store, LVMH 2019, fashion-tech startups 2022) and shows on the FitXpress view too. | awards |
| 9 | Hero subline "Launch ready API and SDK's" (apostrophe). | FX hero |
| 10 | Header nav items "Use Cases", "Made-to-Measure", "Resources", "About 3DLOOK" are `href="#"` (Clarity logs 12 real sessions on `/pricing/#` in 72 h). | header |
| 11 | Page weight: 4 HubSpot form embeds, OptinMonster, Hotjar, Clarity, HubSpot chat, Clearout, GTM. Headless Chrome load: **0 console errors**, so Clarity's script errors come from real-browser conditions (third-party scripts or interactions); their text is not exposed by the API. | scripts |
| 12 | Mobile (390×844): the first plan card starts at y≈770 px, i.e. at the fold; page height ≈6,500 px. | layout |

`/pricing-2026/` (the redesign draft) had 12 GA4 views from 4 users in L90 and now returns 404.

---

## 2. Search Console (facts)

### Totals

| Window | Clicks | Impressions | CTR | Avg pos |
|---|---|---|---|---|
| L3M 2026-07-13 → 10-11 | **160** | 11,305 | 1.42% | 3.5 |
| P3M 2026-04-13 → 07-12 | 235 | 22,041 | 1.07% | 3.5 |
| YoY 2025-07-13 → 2025-10-11 | 298 | 45,614 | 0.65% | 6.0 |

Δ L3M vs YoY: clicks −46%, impressions −75%.

Monthly clicks: 2025-06…2026-01 ≈ 82–113/mo → 2026-07 61 · 08 47 · 09 46 · 10 (1–11) 26.

### Query mix (visible queries only; anonymised queries are dropped by GSC)

| Class | L3M clicks / impr / pos | YoY clicks / impr / pos |
|---|---|---|
| Brand (3dlook / 3d look / variants) | 97 / 4,068 / 1.2 | 201 / 7,813 / 1.3 |
| Brand + Mobile Tailor | 2 / 164 / 4.6 | 3 / 284 / 4.6 |
| Brand + FitXpress/API | 3 / 56 / 2.4 | 9 / 254 / 4.0 |
| Non-brand "body scanner / ai body scan" (consumer) | 0 / 240 / 8.1 | 0 / 6,696 / 7.5 |
| Non-brand generic | 5 / 112 / 5.8 | 0 / 4,501 / 8.1 |
| Non-brand Mobile Tailor intent | 4 / 97 / 4.6 | 5 / 231 / 6.7 |

Top L3M queries: `3dlook` 72 clk / 2,492 impr / pos 1.0 · `3d look` 17 / 1,073 · `ai body scanner` 0 / 138 / 8.6 · `3dlook mobile tailor` 2 / 129 / 4.6 · **`3d body scanner for tailoring price` 4 / 88 / 3.9** (the only real non-brand pricing query, Mobile Tailor intent; YoY 5 / 120) · `3dlook api` 1 / 38 / 3.0 · `3dlook pricing` 4 / 10 / 1.0 (YoY 10 / 165) · `3d body measurement software` 0 / 22 / 9.4. Conversational fragments appear in small numbers ("yes", "sure", "how much is each", "what is the price", "what would be the cost?", "ile to kosztuje", "what does a business-grade 3d body scanner cost to buy or lease…").

### Country and device (query-visible subset: 111 of 160 L3M clicks)

| Country | L3M clicks / impr / pos | YoY clicks / impr |
|---|---|---|
| USA | 31 / 1,382 / 2.9 | 72 / 2,003 |
| India | 14 / 638 / 1.5 | 29 / 4,196 |
| UK | 8 / 228 / 1.8 | 11 / 1,299 |
| Australia | 5 / 95 | 10 / 466 |
| Canada | 4 / 137 | 8 / 622 |

| Device | L3M clicks / impr / CTR / pos | YoY clicks / impr / pos |
|---|---|---|
| Desktop | 57 / 3,086 / 1.85% / 1.7 | 95 / 6,146 / 2.5 |
| Mobile | 53 / 1,616 / 3.28% / 2.2 | 122 / 13,419 / 6.2 |

---

## 3. GA4 (facts)

Caveats: page tracking was dead 2026-02-05 → 06-25, so only YoY comparisons work. Direct is inflated by bot-like sessions (SG/CN). New events `demo_click`, `pricing_plan_click`, `generate_lead` start **2026-10-07/08** (6 days of data). Since 2026-10-02, `form_start` fires on page load for each of the 4 HubSpot forms (≈4 events per view, 2,132 events / 457 users in L90) — not a user signal.

### Page totals

| | L90 | YoY |
|---|---|---|
| Views | **4,877** | 4,131 |
| Users | 3,604 | 2,824 |
| Sessions | 4,462 | 3,638 |
| Engaged sessions | 3,159 (71%) | 3,023 (83%) |
| Engagement time per user | 36 s | 43 s |
| Scroll-90% events per view | 14% (677) | 21% (877) |

Monthly views 2025: 1,076–2,132 · 2026-07 1,670 · 08 1,549 · 09 1,670 · 10 (1–13) 720.

### Channel (views on the page)

| Channel | L90 views / users | YoY views |
|---|---|---|
| Direct | 2,378 / 1,849 | 740 |
| Organic Search | 1,703 / 1,226 | 2,649 |
| AI Assistant | 334 / 239 | 0 |
| Referral | 334 / 261 | 442 |
| Organic Video | 44 | 56 |
| Paid Search | 18 | 2 |

Sessions that **land** on /pricing/ (L90): Direct 1,526 (50% engaged; YoY 170) · google organic 286 · affiliate/referral (Seamly) 150 · chatgpt 75 · youtube 35. `/pricing/?mt=` landings: 152.

### Device and country (views, L90)

| Device | L90 views | Eng. s/user | YoY views |
|---|---|---|---|
| Desktop | 3,170 (65%) | 41 | 1,907 (46%) |
| Mobile | 1,666 (34%) | 28 | 2,190 (53%) |
| Tablet | 41 | | 34 |

Countries: US 1,010 · India 753 · UK 229 · Germany 155 · Canada 140 · Pakistan 130 · Nigeria 118 · Brazil/France/Italy 116 each · **Singapore 101 (≈8 s engagement per user — bot-like)** · Ukraine 91 · Australia 87 · China 86.

### Where visitors come from (pageReferrer of page_views, L90, top 30 referrers = 94% of views)

| Previous page | Views | Share of all views |
|---|---|---|
| Mobile Tailor pages (+ MT blog posts, incl. chatgpt-tagged MT URLs) | 1,845 | **38%** |
| Homepage | 1,021 | 21% |
| No referrer | 559 | 11% |
| Pricing itself (reload / modal hash) | 244 | 5% |
| Google / search | 211 | 4% |
| seamly.io (Mobile Tailor partner) | 165 | 3% |
| /technology/ | 136 | 3% |
| /contact-us/ | 88 | 2% |
| **FitXpress pages** (telehealth 33, BMI 20, fitness 13) | **66** | **1%** |
| AI assistants | 29 | 1% |

Of the views coming from Mobile Tailor pages, **1,662 land on plain `/pricing/` (FitXpress tab) and only 144 on `?mt`**.

### Where they go next (pages whose referrer is /pricing/, L90; 1,326 views)

Mobile Tailor pages 377 · pricing again 247 · /technology/ 181 · homepage 168 · about-us 70 · **FitXpress pages 94** · /contact-us/ 80 · case-studies 38 · partners 20 · wrist 18.

### Actions on the page

| Event | L90 | Notes |
|---|---|---|
| `form_submit` | 51 events / 47 users | Jul 19 · Aug 13 · Sep 20 · Oct 1–13: 5 (10-08 one submit counted on 2 forms). Product split not available before 10-07. |
| `generate_lead` (key event) | 3 | from 10-07 |
| `demo_click` (key event) | 25 events / 14 users in 6 days | Starter "Book a demo" 11 (incl. 1 Korean "데모 예약하기") · Pro 5 · Personalized "Talk to sales" 5 · header "Let's talk" 4 |
| `pricing_plan_click` | 13 / 6 users | `plan` param is filled with button text or the whole nav text — broken parameter |
| outbound `click` | 14 | social icons only (YouTube 7, Instagram 4, Facebook 1); **0 tracked clicks to `mtm.3dlook.me/accounts/signup`** in L90 and YoY (enhanced measurement does not see them, or nobody clicks) |
| Key events attributed to pricing landings | Direct 16, Organic 4, Unassigned 5, Organic Video 1 | |

---

## 4. Clarity, 72 h (facts) vs 2026-09-25 pull

| Metric | 2026-10-14 (all /pricing/ URL variants) | 2026-09-25 |
|---|---|---|
| Real sessions | **155** (PC 117, Mobile 36, Tablet 2) | 124 |
| Bot sessions | 27 (PC 22, "Other" 5) | 24 |
| Scroll depth | PC 45% · Mobile 39% | 43% (PC 42 / Mob 45) |
| Time total / active | PC 194 s / 60 s · Mobile 31 s / 20 s | 194 / 52 |
| Dead clicks | **PC 10% of sessions / 46 clicks** (44 on the main URL, 11% of 89 sessions) · Mobile 0 | 10% / 39 |
| Rage clicks | 1 (PC) | 5 |
| Quickbacks | PC 6% / 8 · Mobile 3% / 1 | 5% / 7 |
| Script errors | **PC 17% / 49 · Mobile 19% / 12** (main URL: 20% of sessions on both devices) | 21% / 68 |
| Error clicks / excessive scroll | 0 / 0 | 0 / 1 |

By channel: Clarity "Direct" = source `3dlook.ai` (internal navigation) **114 of 155 real sessions**, 22% with script errors · "Other" (no referrer) 28 real + 27 bots, 14% dead clicks · Organic 9 · Referral 5 (Seamly affiliate 4) · AI 1.

Not available from the API: which elements receive dead clicks, and the text of script errors. Hypothesis for desktop dead clicks: the invisible (`opacity: 0`) Mobile Tailor hero stacked on the FitXpress hero, and the `href="#"` nav items. Verify in Clarity recordings / heatmap UI.

---

## 5. Ahrefs (facts)

- **Organic keywords for the exact URL: 12, all brand** (`3dlook` US vol 150 pos 1; `3d look` IN/DE/FR/PL/CA/AU 10–30, pos 1). Estimated traffic ≈ 2/mo.
- **Backlinks:** 63 live (96 all-time) from **10 live referring domains** (16 all-time). Top by DR: printful.com 89 (4 links), f6s.com 83, thedigital.gov.ua 73, 3dlook.me 56 (24 links), bgfashion.net 52, apis.io 52, yespress.io 34, seamly.io 32, clad.you 17, softwr.com 10 (53 nofollow). Mostly apparel/MT context.
- **Pricing-intent demand around the category (US vol / KD / CPC¢):** `body scan cost` 150 / 0 / 90 (SERP = medical CT/PET/MRI prices) · `3d body scanner price` 70 / 0 / 120 (SERP = AI Overview citing a Fit3D-vs-Styku pricing blog, shopping units, ShapeScale price guide, marketplaces) · `body composition scan cost` 70 · `inbody price` 90 · `dexa scan cost` 5,100 (consumer/clinical) · `fit3d price` 10 · `styku pricing` 10 · `3d body scan cost` 10 · `3d body scanning software` 30. **Not in Ahrefs at all** (no measured demand): body scanning api pricing, body measurement api price, ai body scanner pricing, virtual tailor pricing, body scanning api, made to measure software pricing, bodygram / prism labs / sizer pricing, body scanning software price. `3dlook pricing` and `body measurement api` = 0. UK is smaller still.
- No competitor B2B **pricing page** ranks top 10 for these; the SERPs are hardware price guides, marketplaces and medical-imaging prices.

---

## 6. Interpretation (for the redesign)

1. **The page is a decision page, not an SEO page.** Ahrefs: 12 brand keywords; GSC: ~90% of clicks are brand. B2B pricing-intent search for API body scanning has no measured demand. Optimise for people already in the funnel; SEO work here = correct title/description and schema, not keywords.
2. **Most visitors are Mobile Tailor buyers, but the page greets them with FitXpress.** 38% of views come from MT pages (+3% Seamly), 1% from FitXpress pages; ~90% of MT-origin views land on plain `/pricing/`, which opens the FitXpress tab. Fix: remember/derive the tab from the referrer or make every MT link use `?mt`, and make the product switch impossible to miss.
3. **FitXpress demand is real but small and late-stage.** In 6 days of new tracking, FX demo buttons got 21 clicks (Starter 11, Pro 5, Personalized 5) vs 4 for the header "Let's talk". Starter (badged "Recommended") is the main entry point; keep it prominent.
4. **Trust and compliance copy is the biggest risk on the page:** "7-day trial" in meta/footer under FitXpress, "maintains HIPAA compliance", "95%+ repeatability" (banned since 09-02) and a non-canonical 96–97% sentence, "80 long-term customers", 40 vs 45 s. All are fixes regardless of design.
5. **The unit is unclear.** Cards sell "scans"; the API bills four request types; no "how to get started" path (demo → demo access → first month free after contract → plan) and no "no integration fee".
6. **Desktop is the buyer device here** (65% of views, longer engagement, ~1.9% search CTR at pos 1.7). Mobile is 34% and engages for ~20–30 s; on a 390 px screen the first card starts at the fold. Lead with plan cards and the switch, push awards/FAQ down.
7. **Friction signals persist:** script errors in ~20% of sessions on both devices (unchanged since 09-25), desktop dead clicks 10–11%. Likely third-party script load (4 HubSpot forms, OptinMonster, Hotjar, chat) and stacked hidden heroes; reduce embeds (one form, loaded on click) and remove the duplicated pricing markup.
8. **Next step after pricing is research, not contact:** visitors go on to MT pages, /technology/, homepage, About; only 80 go to /contact-us/. A page-level FAQ that answers billing, integration, data and accuracy questions keeps them on the decision page.
9. **AI assistants now send real traffic** (334 views L90 vs 0 YoY, mostly ChatGPT to MT URLs). Clear plan names, units and a FAQPage/Offer schema make the page quotable.
10. **Mobile Tailor Enterprise "Start a Trial" opens a contact form**, and there are 0 tracked clicks to the MT sign-up URL — the MT self-serve path is either untracked or unused; fix the label and add an event before judging it.
11. **Tracking is half-fixed:** `form_start` fires 4× on load; `pricing_plan_click.plan` holds nav text; one submit counted twice on 10-08. Fix before using the redesign's A/B numbers.

## 7. Could not get

- Element-level dead/rage clicks and script-error messages — not exposed by the Clarity Data Export API (needs the Clarity UI: heatmaps / recordings filtered to /pricing/).
- Clarity beyond 72 h — API limit.
- Prior-90-day GA4 comparison — page tracking gap 2026-02-05 → 06-25.
- FX vs MT split of form submits before 2026-10-07 — forms had no `form_id` until then.
- Clicks on Mobile Tailor "Sign up for a trial" — no event fires for `mtm.3dlook.me` links (not in outbound `click` data).
- Lead quality/value from pricing forms — HubSpot not queried here (no $ in git).
