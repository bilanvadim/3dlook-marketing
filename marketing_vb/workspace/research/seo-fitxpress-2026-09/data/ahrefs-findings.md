# Ahrefs findings: SEO plan for FitXpress (3dlook.ai)

Pulled 2026-09-25 from the Ahrefs API v3 (data date 2026-09-24). Everything was read-only.
Units used: **40,090** (workspace went from 42,839 to 82,929 of 800,000; the counter resets 2026-09-30).
Raw JSON for every call is in `scratchpad/ah/*.json`.
How to read the numbers:
- Volumes are monthly searches.
- KD is Ahrefs keyword difficulty. `null` means Ahrefs has no figure. It does not mean zero.
- CPC is in US cents, so 450 means $4.50.
- TP is traffic potential.

---

## 1. Site overview: 3dlook.ai

| Metric | Value |
|---|---|
| Domain Rating | **63** (Ahrefs rank 214,116) |
| Organic keywords (all countries, subdomains) | **164**. 70 of them rank in positions 1–3 |
| Organic traffic, current estimate | **693/mo**. Traffic value is $227/mo |
| Paid keywords | 0 |
| Live backlinks / referring domains | 6,140 / **2,034** (all-time: 26,973 / 4,765) |

### Organic traffic trend, monthly (subdomains, all countries)

| Month | Traffic | Month | Traffic |
|---|---|---|---|
| 2024-09 | 5,038 | 2025-09 | 3,683 |
| 2024-12 | 4,496 | 2025-10 | 2,765 |
| 2025-03 | **5,953** (peak) | 2026-01 | 3,234 |
| 2025-05 | 5,949 | 2026-03 | 2,967 |
| 2025-06 | 5,579 | 2026-04 | 2,568 |
| 2025-08 | 4,883 | 2026-05 | 1,546 |
| | | 2026-06 | 1,250 |
| | | 2026-07 | 820 |
| | | 2026-09 | **653** |

Traffic fell **89% from the peak**. There were two steps down:
- **Sep–Oct 2025:** from about 4.9K to 2.7K.
- **May–Jul 2026:** from 2.6K to 0.8K.

This lines up with the earlier finding in memory `project_traffic_drop_2026`, which put the drop on consumer "3D body shape" queries, core updates and AI Overviews.
Traffic value fell faster than traffic, from $3.4K/mo to $0.23K/mo. The site has lost its commercial terms, not only volume.
Referring domains **doubled** over the same period (984 → 2,037). Authority is not the problem.

### Top pages by traffic

| URL | Traffic | Keywords | Top keyword (position) |
|---|---|---|---|
| / | 187 | 14 | 3dlook (1) |
| /content-hub/lean-body-mass-vs-muscle-mass/ | 119 | 19 | dry lean mass (5) |
| /content-hub (hub) | 67 | 13 | percentual de gordura homem (3) |
| /content-hub/body-composition-activities-...-mobile-progress-tracking/ | 59 | 2 | body composition meaning (9, PH) |
| /content-hub/visible-abs-myths-...-ai-driven-3d-body-scanning/ | 49 | 23 | when do abs start to show (6) |
| /content-hub/nft-in-fashion/ | 25 | 11 | ar fashion nft (5) |
| /content-hub/ai-in-fitness-industry/ | 19 | 5 | ai fitness (10) |
| /content-hub/virtual-fitting-room-for-ecommerce/ | 14 | 5 | virtual fitting room technology (6) |
| /mobile-tailor/ | 14 | 6 | mobile tailor (2) |
| /content-hub/glp-1-market/ | 12 | 1 | what is glp (9, IN) |
| /technology/ | 12 | 2 | 3dlook |

### Keyword mix

The sample is the top 170 country-rows by traffic.

| Group | Rows | Traffic |
|---|---|---|
| Health / fitness | 104 | 357 |
| Apparel / fashion / other | 46 | 153 |
| Brand | 20 | 186 |

By country: US 95, IN 26, GB 11, CA 10, AU 5.

### Health/fitness keywords 3dlook holds (flagged)

| Keyword | Country | Position | Volume | KD | URL |
|---|---|---|---|---|---|
| body composition meaning | PH | 9 | 6,500 | 0 | /content-hub/body-composition-activities… |
| body scanner | IN | 18 | 5,900 | 17 | / |
| what body fat percentage to see abs | US | 17 | 1,700 | 3 | /content-hub/visible-abs… |
| what is lean body mass | US | 26 | 1,500 | 22 | /content-hub |
| skeletal muscle vs muscle mass | US | 16 | 600 | 36 | /lean-body-mass-vs-muscle-mass/ |
| what is lean mass | US | 14 | 500 | 34 | same |
| fitness technology | US | 13 | 450 | 26 | /top-fitness-tech-companies/ |
| muscle mass vs skeletal muscle | US | **1** | 350 | 19 | /lean-body-mass-vs-muscle-mass/ |
| ai body scanner app | IN | 12 | 350 | 1 | / |
| dry lean mass | US | **1** | 250 | 18 | /lean-body-mass-vs-muscle-mass/ |
| bia scan | US | **1** | 250 | 5 | /content-hub/bia-scan/ |
| what is lean muscle mass | US | **1** | 150 | 34 | /lean-body-mass-vs-muscle-mass/ |
| visible abs | US | **1** | 150 | 0 | /visible-abs… |
| ai body scanner | US | **1** | 90 (KE: 150) | 2 | /content-hub/ai-body-scanners-vs-dexa-scans/ |
| body scanning technology | US | 10 | 100 | 33 | /body-scanning-technology-for-apparel/ |
| connected fitness equipment | US | 6 | 90 | 12 | /connected-fitness-industry/ |
| what is a body composition scale | US | 10 | 70 | 31 | /body-composition-scale/ |
| virtual body measurement | US | 8 | 60 | 55 | /virtual-body-measurements/ |
| how to measure waist with phone | US | 8 | 60 | 0 | /content-hub |

**Takeaway:** 3dlook ranks #1 on many small informational body-composition terms (lean mass, abs, BIA). It is absent from the top 10 on every head commercial term tested: "3d body scanner", "body scan app", "body composition test", "body measurement app", "body fat percentage calculator" and "waist to height ratio".

The one exception is **"ai body scanner"**. 3dlook ranks #1 in the organic results, and **3dlook.ai is also cited in the Google AI Overview** for it (US).

---

## 2. Competitor landscape

### Organic competitors Ahrefs detects (US, by keyword overlap)

| Domain | Common keywords | Their keywords | Traffic | DR |
|---|---|---|---|---|
| inbodyusa.com | 27 | 9,760 | 85,116 | 72 |
| bodyspec.com | 21 | 29,308 | 193,910 | 57 |
| grandviewresearch.com | 13 | 14,281 | 107,082 | 91 |
| menshealth.com | 11 | 219,024 | 1,030,170 | 87 |
| marketresearch.com / towardshealthcare.com | 10 / 8 | — | — | 80 / 66 |
| mtailor.com | 6 | 372 | 5,195 | 41 |
| fitnessai.com | 4 | 6,280 | 31,413 | 49 |
| bmivisualizer.com | 3 | 461 | 7,114 | 25 |

The real SERP rivals for body-composition content are **InBody and BodySpec**, not the other scan-API vendors.
Market-research sites compete with 3dlook's "industry overview" posts.

### Named players (global, subdomains)

| Domain | DR | Organic traffic | Keywords (top-3) | What drives their traffic |
|---|---|---|---|---|
| **3dlook.ai** | **63** | **693** | 164 (70) | lean-mass/abs content, brand |
| bodyspec.com (DEXA) | 57 | **235,803** | 31,288 (11,960) | huge consumer health blog (weight loss, supplements, body types, Wegovy side effects 3,984/mo), DEXA city pages, body-fat % pages |
| inbodyusa.com | 72 | **128,881** | 10,704 (5,512) | body-fat % chart (19.9K), "inbody scan" (11.7K), skinny fat, x% body fat pages, lean body mass (4.7K) |
| inbody.com | 70 | 33,711 | 2,584 | localized DE/FR blog (BMR, body fat) |
| bmivisualizer.com | 25 | 14,696 | 535 | one tool: "bmi visualizer" / "body visualizer" |
| mtailor.com | 41 | 5,790 | 402 | apparel sizing |
| visbody.com | 44 | 5,305 | 1,773 (333) | brand (FR), posture blog, "3d body scan" |
| fit3d.com | 49 | 5,195 | 360 (152) | brand 3.4K; "3d body scan" #1; "3d body scanner" #1; muscle-in-deficit blog |
| styku.com | 53 | 3,614 | 217 (98) | brand 2.2K; "styku body scanner"; "3d body scanner" #1–2; body-composition exercises |
| spren.com (smartphone body-comp API) | 30 | 2,010 | 76 | homepage ranks for "how to measure body fat"; DEXA city pages |
| bodygram.com | 46 | 1,456 | 31 | brand only (mostly Japan) |
| shapescale.com | 47 | 963 | 237 | "inbody scan near me" hijack posts, Evolt/InBody reviews |
| prismlabs.tech | 28 | 368 | 109 | one post: "what different body fat % look like" (299). Solution pages for GLP-1, insurance and population health get **0** traffic |
| mirrorsize.com | 51 | 182 | 16 | brand |
| in3d.io | 37 | 129 | 16 | brand |
| sizestream.com | 37 | 36 | 15 | (their app ranks on Google Play instead) |
| evolt360.com | 45 | 0 | 1 | — (brand SERPs owned by third parties) |
| esenseis.com | 0 | 0 | 0 | not found / no footprint |

**Key reading:** no direct B2B scan-API competitor (Prism, Bodygram, Spren, in3d, Mirrorsize, Size Stream) gets meaningful organic traffic. Their B2B solution pages (Prism's GLP-1 and insurance pages) get zero.
The only players with real SEO traffic are consumer or hardware brands with big body-fat content libraries: BodySpec, InBody and ShapeScale.
**3dlook already has the highest DR of the whole scan-vendor set (63)**, above Styku 53, Mirrorsize 51, Fit3D 49, ShapeScale 47, Bodygram 46, Visbody 44, Prism 28 and Spren 30.

### Content gaps: what competitors rank for that 3dlook doesn't (US)

| Cluster | Example keywords (US volume, KD) | Who owns it |
|---|---|---|
| "X% body fat" pages | 15% body fat 5,500/KD0; 15 body fat male 5,200/KD11; 20% body fat 4,400/KD11; 10% body fat 4,000/KD0; 20 percent body fat 3,100/KD0; 30% body fat 2,800/KD43; 25% body fat 2,500/KD29; 18% body fat 2,400/KD23; 12% body fat 2,400/KD0; 14 body fat 800/KD16 | inbodyusa (pos 1–2), bodyspec, spren |
| Visual body-fat guides | different body fat percentages 800/KD41; what does 10 body fat look like 500/KD22; body fat percentage pictures female 450/KD26; body fat % examples 450/KD30 | prismlabs (pos 4–10) |
| Body-fat % reference | body fat percentage 61K/KD63; chart 12K/KD48; women 8.6K/KD38; men 7.3K/KD40; healthy for women 6.2K/KD42 | inbodyusa, bodyspec (#1) |
| Muscle | how much muscle can you gain in a month 4,300/KD5; does muscle weigh more than fat 8,800/KD4; can you build muscle in a calorie deficit 3,000/KD2; skeletal muscle mass 5,600/KD33; major muscle groups 3,000/KD22 | inbodyusa, bodyspec, fit3d |
| Body composition | body composition exercises 5,400/KD0; body composition scale 3,700–3,900/KD27; what is body composition 9,000/KD34; example of body composition 450/KD29 | styku, bodyspec, inbodyusa |
| 3D scanner category | 3d body scan 800/KD39; 3d body scanner 600–700/KD26; body scanner machine 1,700/KD56; 3d body composition scanner 150/KD10; 3d body scanners 150/KD21 | fit3d, styku (#1) |
| Test comparisons | how accurate is inbody scan 600/KD0; styku vs dexa; evolt 360 body scan accuracy 90/KD0 | shapescale, styku |
| Location/price (low fit) | inbody scan near me 3,800; dexa scan [city] | bodyspec, shapescale |

---

## 3. Keyword universe

### 3a. High-volume consumer/informational (US unless noted)

| Keyword | Volume | KD | CPC | TP | Parent topic | Realistic for DR 63? |
|---|---|---|---|---|---|---|
| bmi calculator | 2,380,000 (UK 710K) | 78 (UK 4) | 1 | 1.62M | bmi calculator | **No**: calculator.net/NHS/CDC own it |
| dexa scan | 104,000 (UK 23K) | 69 | 120 | 19K | dexa scan | No (clinic/local intent) |
| body fat percentage | 61,000 | 63 | 15 | — | — | Hard |
| how to measure body fat | 45,000 | 60 | 6 | — | body fat percentage | Hard; has an AIO; SERP is all DR 84–95 |
| body composition | 40,000 | 0* | 60 | — | what is body composition | Medium (*KD 35 in inbody data) |
| body fat percentage calculator | **22,000** (UK 3,900) | **16** (UK 41) | 30 | **109,000** | body fat percentage | **Yes**: no AIO; DR 13 and DR 51 sites rank #2–3 |
| body fat percentage chart | 12,000 | 48 | 5 | — | body fat percentage | Medium |
| body shape calculator | 11,000 | 48 | 140 | 42,000 | body type | Medium |
| what is body composition | 9,000 | 34 | 3 | — | — | Medium |
| body visualizer | 8,300 | 44 | 70 | 22,000 | body visualizer | Medium: 3D avatar asset |
| waist to hip ratio | 8,000 | 34 | 2 | 5,900 | — | Medium |
| body scan | 7,800 | 61 | 200 | 600 | body scan **meditation** | No: mixed intent |
| full body scan | 6,400 | 33 | 130 | — | — | No: MRI/Prenuvo intent |
| body measurements | 6,700 | 26 | 20 | — | body type | Medium |
| waist to height ratio | 4,500 (**UK 2,200**) | 36 (**UK 12**) | 120 | 6,400 (UK 9,500) | waist to height ratio calculator | **Yes, especially UK** |
| waist measurement (UK) | 4,400 | 45 | 15 | 5,900 | height to waist ratio | Medium |
| lean body mass calculator | 3,200 | 31 | 7 | 6,100 | lean body mass | Yes: extends the existing #1 cluster |
| waist to height ratio calculator | 3,100 (UK 1,000) | 26 (UK 23) | 30 | 2,200 | — | **Yes** |
| body composition scan | 3,000 (UK 600) | 39 (UK 2) | 150 | 20,000 | dexa scan | Medium |
| body composition test | 2,700 (UK 450) | 22 | 100 | 1,900 | body composition test | **Yes**: SERP is .edu labs + inbody |
| bmi visualizer | 2,400 | 68 | 110 | 8,900 | brand of bmivisualizer | No |
| body composition analysis | 1,600 (UK 500) | 30 (UK 0) | 90 | 1,600 | body composition | Yes |
| muscle mass calculator | 1,400 | 25 | 60 | 5,700 | lean body mass | Yes |
| how to take body measurements | 1,600 | 11 | 3 | — | — | Yes |
| does ozempic cause muscle loss | 1,800 | 52 | 20 | — | ozempic and muscle loss | Medium (YMYL; medical publishers) |
| ozempic muscle loss | 1,100 | 53 | 25 | — | — | Medium |
| body scanner | 1,000 (global 13K) | 0 | 160 | 400 | 3d body scanner | Yes |
| weight loss tracker app | 1,000 (UK 150) | 0 (UK 35) | 120 | 900 | weight tracker | Yes, but app stores own it |
| 3d body scan | 800 (UK 150) | 39 (UK 26) | 120 | 3,700 | fit3d | Yes (compete with Fit3D/Styku) |
| 3d body scanner | 700 (UK 150) | 26 (UK 18) | 120 | 2,500 | styku | **Yes**: #2–4 are DR 49–72 |
| glp-1 muscle loss | 600 (+ "glp 1 muscle loss" 400) | 45 (11) | 8 | — | glp1 muscle loss | Medium: medical publishers, AIO |
| mounjaro muscle loss (UK) | 450 | 19 | 350 | — | — | **Yes (UK)** |
| body fat scanner | 450 | 54 | 100 | 19,000 | dexa scan | Medium |
| body measurement tracker | 400 | 1 | 90 | 600 | track body | Yes |

### 3b. GLP-1 eligibility and BMI verification (online-pharmacy/telehealth adjacent, highest CPC)

| Keyword | Country | Volume | KD | CPC |
|---|---|---|---|---|
| **bmi for mounjaro** | UK | **1,100** | **0** | 500 |
| what bmi for mounjaro | UK | 1,000 | 45 | 450 |
| what bmi do you need for mounjaro | UK | 700 | 41 | 500 |
| mounjaro bmi | UK | 500 | 55 | 400 |
| bmi for wegovy | UK / US | 400 / 300 | 21 / 39 | 500 |
| bmi for weight loss injections | UK | 350 | null | 300 |
| bmi for mounjaro uk | UK | 300 | null | 350 |
| bmi for ozempic | US | 500 | 48 | 450 |
| bmi for glp 1 | US | 350 | null | 300 |
| what bmi do you need for ozempic | US | 350 | 33 | **900** |
| bmi for zepbound | US | 250 | 4 | 450 |
| wegovy bmi requirements | US | 250 | 39 | 600 |
| wegovy bmi calculator | US | 90 | 18 | 200 |
| mounjaro bmi 27 | UK | 150 | null | 800 |

About 30 long-tail variants each in the US and the UK. The cluster adds up to roughly **6–8K/mo in the UK and about 5K/mo in the US**, with CPCs of $3–9.
The UK SERP for "bmi for mounjaro" is **all DR 0–6 GP-practice/NHS-surgery pages, plus boltpharmacy (DR 47)**.
AI Overview citations go to coxheathpharmacy.co.uk and an NHS ICB page.
**This is the most winnable high-value cluster for a DR 63 site.** Frame it as "BMI eligibility and how pharmacies verify BMI remotely". That is the FitXpress verified-BMI angle, and it is buyer-adjacent for online pharmacies.

### 3c. B2B / buyer-intent terms (the audience FitXpress sells to)

| Keyword | Volume | KD | CPC | Note |
|---|---|---|---|---|
| corporate wellness programs | 2,600 | 0 | 60 | employer-wellness buyers; TP 3,500 |
| remote patient monitoring | 6,800 | 51 | 400 | hard; RPM vendors |
| remote patient monitoring devices | 1,200 | 17 | 80 | winnable |
| remote patient monitoring companies | 700 | 41 | 400 | list-style |
| medical weight loss program | 1,200 | 27 | 450 | local-clinic intent |
| body composition analyzer | 600 | 0 | 150 | hardware buyers (gyms/clinics) |
| body composition machine | 300 | 0 | 200 | parent = "inbody 770 price" |
| wellness program for employees | 150 | 41 | 700 | |
| ai body scan / ai body scanner | 80 / 150 | 0 / 2 | 120–150 | **3dlook #1 + AIO citation** |
| body scan app | 150 | 46 | 60 | SERP = app stores, AIO |
| body measurement app | 150 | 22 | 100 | SERP = app stores + Reddit, AIO |
| body scanner app | 100 | 9 | 60 | |
| body measurement software | 70 | null | — | |
| 3d body scanner price | 70 | 2 | 120 | |
| glp-1 weight loss program | 60 | 56 | 600 | TP 314K (parent "glp1") |
| glp-1 tracker app / free | 70 / 300 | null | — | |
| bmi verification | 100 | null | — | branded/navigational intent |
| **Zero or no data:** body measurement api, body measurement sdk, body scanning api, body composition api, body scanning software, body composition software (10), mobile body composition, 3d body scanner for gym, telehealth weight verification, glp-1 progress tracking, bmi check online pharmacy, verify bmi online, body composition without scale, fitness app body scan, measure body with phone, 3d body scan cost (10), ai body composition (0), body fat from photo (20), body fat percentage from photo (10) | 0–20 | — | — | **the literal product/API terms have no measurable search demand** |

**Implication:** buyer-intent keywords that describe FitXpress have almost no search volume. Organic reach has to come from:
1. Informational health clusters where a scan is the natural answer: body-fat %, WHtR, BMI-for-GLP-1, muscle loss on GLP-1, body-composition testing.
2. Category terms: 3D body scanner, AI body scanner, body composition test/analyzer.
3. AI-Overview/LLM citation (GEO) for vendor and "how does X work" questions.

Product and solution pages should aim to convert that traffic, not to rank on their own.

---

## 4. SERP overviews (top 10, Sep 2026)

| Keyword (country) | AI Overview? | Who ranks (organic) | Read |
|---|---|---|---|
| body fat percentage calculator (US, 22K) | **No** (only PAA) | calculator.net DR84, fatcalc DR51, **totalmedsolutions DR13 (#3)**, UNC DR90, omnicalculator, legion, builtwithscience DR51 | Calculator tools; a DR 13 site at #3 shows it can be cracked. **Best head-term bet** (an interactive calculator plus a "get the real number by scan" CTA) |
| 3d body scanner (US) | Yes (cites styku, fit3d, artec3d) | styku DR53 #2, fit3d DR49 #3, artec3d DR72, Wikipedia, sizestream Play app, dexafit, gomeasure3d DR33 | Vendor homepages. A 3dlook category/comparison page can break in |
| body scan app (US) | Yes (cites App Store) | App Store, Play (sizestream, zozofit), zozofit.com DR44, gainframe.app DR24 blog | App-store SERP; a listicle ("best body scan apps") is the only web entry |
| ai body scanner (US) | Yes (**cites 3dlook.ai**, WW, Mayo, fitnessai, leanlens) | TrackBod app, weightwatchers, fox10, leanlens DR0, sizestream app, fitnessai DR49, Reddit, Mayo | Already won. Defend it and extend to "ai body scan" |
| body composition test (US) | Yes (cites appstate.edu, UC Davis, dexafit) | .edu labs, PMC, inbodyusa, Kaiser, craftbodyscan DR41, UC Davis | Winnable: a methods comparison (DEXA vs BIA vs 3D vs smartphone) |
| body measurement app (US) | Yes (App Store, hevy) | Play/App Store, Reddit, theprogressapp DR3, gainframe DR24, methreesixty app, hevy DR63, bodymapp DR37 | Listicle angle; low DR sites rank |
| how to measure body fat (US, 45K) | Yes (calculator.net, Kaiser, NASM) | calculator.net, Kaiser, Harvard, PMC, BHF, NHS ELHT DR60, UC Davis, NASM | Authority SERP (YMYL); long shot |
| waist to height ratio (UK) | Yes (NHS, BHF, Bupa) | NHS, BHF, Wikipedia, omnicalculator, Bupa, PMC, Men's Health, allhealthandcare DR5 | NHS-led, but a DR 5 site ranks #10. Worth a calculator page |
| bmi for mounjaro (UK) | Yes (coxheathpharmacy, NHS ICB) | cragshealthcare DR4, NHS surgeries DR0–6, boltpharmacy DR47, Facebook group | **Weak SERP, high CPC. Top opportunity** |
| glp-1 muscle loss (US) | Yes (Mayo store, preventionclinics, YouTube) | PMC, Mayo, ScienceDirect, UC Davis, MGH, sermo DR70, vorihealth DR42 | Medical-publisher SERP; enter via data/original research ("measuring lean-mass loss at home") |

AI Overviews appear on 9 of 10 of these SERPs. The only exception is the body-fat calculator.

---

## 5. Backlink context

### Referring domains, 3dlook.ai (monthly)

| 2024-09 | 2025-03 | 2025-09 | 2025-10 | 2025-11 | 2026-02 | 2026-04 | 2026-07 | 2026-09 |
|---|---|---|---|---|---|---|---|---|
| 984 | 1,271 | 1,495 | 1,633 | 1,364 | 1,960 | 1,720 | 1,960 | **2,037** |

RDs doubled while traffic fell about 89%. The loss is not a link problem. It is content and topic fit, plus AIO and core updates.
The local export `workspace/research/backlinks/` (2026-08-31) shows the health segment holds only **1,005 of about 13.4K backlinks**. Its top health donors are /ai-in-fitness-industry/ (326), /the-potential-of-ai-in-telehealth/ (263) and /glp-1-market/ (183).

### Link intersect

Method: the top 100 referring domains (DR 30–92) were pulled for each of fit3d, styku, prismlabs, bodygram, spren, shapescale and inbodyusa, giving 527 unique domains. Those were compared against 3dlook's 3,073-domain export.
Result: 3dlook already has **102**. **425 are a gap.**

**Domains linking to 3+ competitors that 3dlook lacks:**
- pitchbook.com (6 of 7 competitors)
- za.com (7)
- producthunt.com (prism, spren, shapescale)
- lever.co
- hackernoon.com
- angel.co / wellfound.com
- hunter.io
- similarweb
- yellowpages
- podcasts: castbox, pocketcasts (4 each)

This is mostly startup-profile, directory and podcast-hosting infrastructure. It is cheap to replicate: PitchBook/Wellfound profiles, a Product Hunt launch for a FitXpress demo, and podcast guest spots.

**Health/fitness and media gaps, and who they link to:**

| Domain | DR | Links to |
|---|---|---|
| womenshealthmag.com | 87 | styku, inbodyusa |
| mensjournal.com | 84 | styku, shapescale |
| health.com | 87 | inbodyusa |
| verywellfit.com | 84 | shapescale |
| shape.com | 83 | fit3d |
| mindbodygreen.com | 85 | fit3d |
| myfitnesspal.com | 84 | shapescale |
| medpagetoday.com | 82 | fit3d |
| sportsbusinessjournal.com | 83 | fit3d |
| frontofficesports.com | 78 | spren |
| rockhealth.com | 75 | prismlabs |
| eithealth.eu | 74 | spren |
| tempo.fit | 57 | prismlabs (partner) |
| fitnessai.com | 49 | prismlabs (partner) |
| theverge / engadget / venturebeat / zdnet / digitaltrends | 89–92 | styku, shapescale, bodygram |
| frontiersin.org, biomedcentral.com, springeropen.com | 89–92 | fit3d, inbodyusa (validation studies) |
| .edu labs: osu, brown, ttu, utah, clemson, ucf, sjsu, upenn, washington, usc, tufts, colostate, fsu | 82–91 | fit3d / inbodyusa / spren (research use, lab pages) |

Patterns to copy:
1. **Peer-reviewed validation studies** get cited on frontiersin/BMC and on university lab pages (Fit3D, InBody).
2. **Consumer health-media product reviews** (Women's Health, Men's Journal, Verywell Fit, Shape).
3. **Partner integration pages** (Prism ← Tempo, FitnessAI).
4. **Digital-health investor/ecosystem** coverage (Rock Health, EIT Health).

The full gap list is in `ah/intersect.json`.

---

## 6. Decision-relevant conclusions

1. **Authority is not the constraint.** DR 63 is the highest among scan vendors and RDs are 2,037 and growing. Content and topic fit are the constraint.
2. **Pure product/API keywords have about zero volume.** Don't build the plan around "body measurement API/SDK". Use them on landing pages for conversion and GEO.
3. **Winnable head terms for DR 63:**
   - body fat percentage calculator: 22K, KD 16, no AIO
   - waist-to-height ratio (calculator): US 4.5K/3.1K, UK 2.2K at KD 12
   - body composition test: 2.7K, KD 22
   - body composition analysis: 1.6K, KD 30
   - lean body mass / muscle mass calculators: 3.2K / 1.4K, KD 25–31
   - 3d body scanner / 3d body scan: 700/800, KD 26–39
   - body scanner: 1K, KD 0; 13K global
4. **Highest-value cluster: GLP-1 BMI eligibility.**
   - UK "bmi for mounjaro" is 1,100/mo at KD 0, and the SERP is dominated by DR 0–6 GP pages. The cluster totals about 6–8K UK plus about 5K US, at CPC $3–9.
   - It fits the online-pharmacy (UK priority) and telehealth ICPs.
   - Also: GLP-1/Ozempic/Mounjaro muscle loss, about 5K US combined, KD 11–53, plus UK Mounjaro muscle loss (450, KD 19).
5. **Scale play:** the "X% body fat" programmatic set is 30+ keywords of 800–5,500/mo each, mostly KD 0–30. InBody and BodySpec own it with #1–2. 3dlook already wins neighbouring lean-mass and abs terms, so this is the most direct way to recover traffic volume.
6. **AIO is on 9 of 10 key SERPs.** 3dlook is already cited for "ai body scanner". Structured, citable pages (definitions, method comparisons, validation numbers) matter as much as positions.
7. **Links:** get cheap startup-profile parity (PitchBook, Wellfound, Product Hunt, podcasts). Then chase health-media reviews and a published validation study, which is the Fit3D/InBody pattern behind their .edu and journal links.
