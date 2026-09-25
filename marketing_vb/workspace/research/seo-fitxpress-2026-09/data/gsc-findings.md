# GSC findings — 3dlook.ai, FitXpress health & fitness SEO baseline

Property `sc-domain:3dlook.ai`, search type = web, data state = final. Pulled 2026-09-25.

**Periods used**

- **L3M** (last 3 months) = 2026-06-24 → 2026-09-22 (91 days, last final day)
- **P3M** (prior 3 months) = 2026-03-25 → 2026-06-23
- **YoY** = 2025-06-24 → 2025-09-22
- **16-month trend** = 2025-05-01 → 2026-09-22 (Sep 2026 = 22 days only)

**Caveats.** GSC hides anonymised (rare) queries: query-level tables cover only ~40–45% of site impressions (see §5 'anon' column). Query×page rows are by-page aggregation, so a query's impressions summed over pages exceed its property total. The query×page P3M pull and YoY query pull hit the 25,000-row cap (long tail truncated; top rows unaffected). Clusters are regex-assigned (first match wins; rules in the appendix); 'Health/fitness' = every cluster except brand-3DLOOK, apparel/fashion and Other.

## 0. Key findings (decision-relevant)

1. **Health/fitness is half of all visibility but a fifth of clicks.** L3M: health-flagged pages = 48% of page impressions (438.9K of 908.6K) but 19% of clicks (1,966 of 10,139). Visible health/fitness queries: 742 clicks / 177.8K impr (CTR 0.4%) in L3M vs 1,795 / 359.5K in P3M (impr −51%) and 2,937 clicks YoY.
2. **Visibility without traffic.** The two biggest health pages are zero-click: `/content-hub/lean-body-mass-vs-muscle-mass/` 79.8K impr → 56 clicks (pos 6.1), `/content-hub/visible-abs-myths-…/` 80.7K impr → 188 clicks (pos 7.6). "lean mass" (6,346 impr, pos 3.9), "lean meaning body" (5,014, pos 2.6), "skeletal muscle mass" (894, pos 1.1) get 0 clicks: AI Overview / definition-box territory. Consumer definitional queries will not feed FitXpress; stop treating them as a growth lever.
3. **No page targets FitXpress's own head terms.** Homepage `/` holds "ai body scanner" (881 impr, pos 5.6, 43 clk), "ai body scanner app" (537, 8.4), "ai body scan" (458, 5.8), "3d body scanner" (1,083, pos 26.4), "body scanner" (987, pos 28), "3d body composition scanner" (354, pos 33). Before the redirect `/fitxpress/` ranked pos 3.1 for "ai body scanner" (3,060 impr, Jun 25–Feb 26) and earned 745 clicks in 9 months. "body scanning technology" (9,188 impr, pos 10.1) is served by the *apparel* article.
4. **The brand term itself is weak.** "fitxpress" = 373 impr, **pos 6.0**, 21 clicks, split across 4 URLs (`/for-bmi-verification/` 252, the new telehealth page 138, the redirected telehealth URL 81, `/fitxpress/for-connected-and-digital-fitness/` 41). Pre-redirect `/fitxpress/` held it at pos 4.4 with 291 clicks.
5. **ICP-vertical demand is visible but ranks too low.** Telehealth/AI-in-healthcare cluster: 8.3K impr, **0 clicks**, pos 39.7 (P3M 25.5). GLP-1/weight-loss: 7.2K impr, 12 clicks, pos 35.2 (was 23.3). The `/content-hub/glp-1-market/` page sits at pos 43–68. Weight-loss-clinic *marketing* queries: 12K impr, 3 clicks — wrong audience (agencies), and one article only.
6. **Quick wins exist in striking distance:** 197 health/fitness queries at pos 4–20 with ≥80 impr (80.2K impr, 402 clicks). The B2B-shaped ones: body scanning technology (9,188, 10.1), bmi verification (81, 5.2), best mobile body scanning solution for telehealth (46, 2.9), mobile body scanning platforms body composition tracking (86, 9.3), body composition software visualization client engagement (79, 4.5), replace our aging body scanner (180, 19.7), body measurement software (289, 3.3 on its article).
7. **Cannibalisation hot spots (health):** `/` vs `/content-hub/3d-body-scanning/` (2,879 impr at stake: weight tracker 3d, 3d body analysis, 3d body fat scanner); `/content-hub/3d-body-scanning/` vs `/content-hub/virtual-body-measurements/` (1,151); `/for-bmi-verification/` vs the telehealth page on "fitxpress"; `/content-hub/body-scanner-machines-vs-mobile-3d-body-scan/` vs `/content-hub/body-scanning-technology-comparison/`.
8. **Markets/devices.** Health-cluster impressions are 46% USA but clicks are 35% India (246 of 696; mostly consumer "ai body scanner"). US CTR 0.2% at pos 18.8. Desktop has 49% of health impressions at pos 20.5 and 0.1% CTR; mobile 50% at pos 8.5 and 0.7% CTR — B2B research (desktop) is where we rank worst.
9. **Brand demand is falling too.** Branded impressions ~4.6–4.9K/mo (Jun–Sep 2025) → 2.2K (Aug 2026); branded clicks 1,805–2,060 → 827. Brand share of clicks rose from ~14% to ~27% only because non-brand fell faster (non-brand visible clicks 4,623 in Jul 2025 → 339 in Aug 2026).
10. **Winners to build on:** `/content-hub/body-scanning-technology-comparison/` (5.3K impr, +383% vs P3M), `/content-hub/3dlook-turns-two-photos-structured-body-data/` (+62%), `/structured-body-data-for-telehealth-digital-health-programs/` (new, 2.7K impr, pos 5.6), `/content-hub/how-to-take-your-body-measurements-at-home/` (flat, 31.6K impr), the waist-fluctuation physiology article (58K impr, 285 clicks, pos 5.0).

## 1. Topic clusters — L3M vs P3M vs YoY

| Cluster | #queries L3M | Clicks L3M | Impr L3M | CTR L3M | Pos L3M | Clicks P3M | Impr P3M | Pos P3M | Clicks YoY | Impr YoY | Pos YoY | Impr L3M vs P3M |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Apparel sizing / fashion (non-health) | 3682 | 179 | 119,244 | 0.2% | 19.1 | 379 | 207,174 | 15.2 | 908 | 472,600 | 33.5 | -42% |
| **Body composition / body fat / lean mass** | 3020 | 80 | 78,529 | 0.1% | 7.3 | 349 | 190,311 | 8.0 | 201 | 9,146 | 37.5 | -59% |
| **Body scanning (AI / 3D / mobile)** | 536 | 254 | 22,816 | 1.1% | 17.6 | 556 | 28,105 | 15.1 | 1248 | 63,461 | 24.3 | -19% |
| **Body measurement (how-to / app / AI)** | 1172 | 188 | 19,662 | 1.0% | 14.0 | 314 | 27,563 | 12.2 | 502 | 35,166 | 24.1 | -29% |
| Other | 3903 | 146 | 18,383 | 0.8% | 24.0 | 443 | 48,143 | 13.2 | 8811 | 89,924 | 27.9 | -62% |
| **Fitness tech / fitness industry** | 688 | 32 | 17,086 | 0.2% | 21.0 | 72 | 57,881 | 10.8 | 316 | 72,508 | 21.0 | -70% |
| **Weight-loss clinic marketing** | 92 | 3 | 12,022 | 0.0% | 13.3 | 3 | 10,236 | 8.1 | 9 | 4,687 | 18.3 | +17% |
| **Telehealth / digital health / AI in healthcare** | 575 | 0 | 8,264 | 0.0% | 39.7 | 2 | 10,809 | 25.5 | 30 | 30,090 | 40.6 | -24% |
| **Progress tracking / body visualisation** | 328 | 118 | 7,334 | 1.6% | 22.3 | 355 | 9,597 | 19.3 | 211 | 11,029 | 31.4 | -24% |
| **GLP-1 / weight loss / obesity** | 353 | 12 | 7,191 | 0.2% | 35.2 | 46 | 11,945 | 23.3 | 91 | 15,091 | 30.8 | -40% |
| Brand: 3DLOOK / other brand | 58 | 2678 | 7,114 | 37.6% | 5.3 | 3691 | 8,468 | 2.7 | 5586 | 11,893 | 3.1 | -16% |
| **Waist / circumference / anthropometrics** | 195 | 18 | 3,151 | 0.6% | 5.6 | 18 | 5,459 | 5.1 | 42 | 3,691 | 10.2 | -42% |
| **BMI** | 223 | 16 | 1,361 | 1.2% | 15.2 | 46 | 6,962 | 10.5 | 89 | 2,142 | 20.6 | -80% |
| **Brand: FitXpress** | 5 | 21 | 404 | 5.2% | 6.8 | 34 | 607 | 7.4 | 198 | 1,185 | 5.0 | -33% |
| **ALL HEALTH/FITNESS (bold rows)** | | **742** | **177,820** | 0.4% | | 1795 | 359,475 | | 2937 | 248,196 | | -51% |

### Top queries per health/fitness cluster (L3M)

Columns: clicks, impressions, CTR, avg position (L3M) · main ranking URL (most impressions) · # URLs that got impressions · P3M impressions / position.

#### Brand: FitXpress

| Query | Clk | Impr | CTR | Pos | Ranking URL | #URLs | P3M impr | P3M pos |
|---|---|---|---|---|---|---|---|---|
| fitxpress | 21 | 373 | 5.6% | 6.0 | /for-bmi-verification/ | 8 | 557 | 7.4 |
| fit xpress | 0 | 27 | 0.0% | 14.6 | /for-bmi-verification/ | 3 | 9 | 20.6 |
| fitexpress colle | 0 | 2 | 0.0% | 38.0 | /fitxpress/for-connected-and-digital-fitness/ | 1 | 0 | - |
| fit express colle | 0 | 1 | 0.0% | 31.0 | /fitxpress/for-connected-and-digital-fitness/ | 1 | 0 | - |
| fitexpress | 0 | 1 | 0.0% | 38.0 | /fitxpress/for-connected-and-digital-fitness/ | 1 | 6 | 25.5 |

#### Body composition / body fat / lean mass

| Query | Clk | Impr | CTR | Pos | Ranking URL | #URLs | P3M impr | P3M pos |
|---|---|---|---|---|---|---|---|---|
| lean body mass | 1 | 8844 | 0.0% | 7.2 | /content-hub/lean-body-mass-vs-muscle-mass/ | 1 | 17953 | 6.9 |
| lean mass | 0 | 6346 | 0.0% | 3.9 | /content-hub/lean-body-mass-vs-muscle-mass/ | 1 | 5048 | 4.6 |
| lean meaning body | 0 | 5014 | 0.0% | 2.6 | /content-hub/lean-body-mass-vs-muscle-mass/ | 1 | 1478 | 5.5 |
| lean muscle mass | 0 | 4728 | 0.0% | 6.4 | /content-hub/lean-body-mass-vs-muscle-mass/ | 1 | 4665 | 4.4 |
| what is lean body mass | 1 | 2534 | 0.0% | 9.1 | /content-hub/lean-body-mass-vs-muscle-mass/ | 1 | 6321 | 8.2 |
| lean body meaning | 0 | 2532 | 0.0% | 3.5 | /content-hub/lean-body-mass-vs-muscle-mass/ | 1 | 4239 | 7.1 |
| lean body mass meaning | 0 | 2310 | 0.0% | 9.4 | /content-hub/lean-body-mass-vs-muscle-mass/ | 1 | 3968 | 7.7 |
| lean body | 0 | 2021 | 0.0% | 3.0 | /content-hub/lean-body-mass-vs-muscle-mass/ | 2 | 3209 | 3.2 |
| lean mass meaning | 0 | 1738 | 0.0% | 7.7 | /content-hub/lean-body-mass-vs-muscle-mass/ | 1 | 2110 | 7.8 |
| what is lean mass | 0 | 1627 | 0.0% | 8.1 | /content-hub/lean-body-mass-vs-muscle-mass/ | 1 | 2700 | 8.8 |
| what is lean muscle mass | 1 | 1183 | 0.1% | 6.6 | /content-hub/lean-body-mass-vs-muscle-mass/ | 2 | 1583 | 5.9 |
| bia scan | 0 | 1008 | 0.0% | 5.8 | /content-hub/bia-scan/ | 1 | 1243 | 5.7 |
| skeletal muscle mass | 0 | 894 | 0.0% | 1.1 | /content-hub/lean-body-mass-vs-muscle-mass/ | 1 | 548 | 1.3 |
| dry lean mass | 3 | 725 | 0.4% | 5.8 | /content-hub/lean-body-mass-vs-muscle-mass/ | 1 | 1008 | 5.8 |
| lean body mass คือ | 0 | 659 | 0.0% | 10.5 | /content-hub/lean-body-mass-vs-muscle-mass/ | 1 | 188 | 10.5 |

#### Body scanning (AI / 3D / mobile)

| Query | Clk | Impr | CTR | Pos | Ranking URL | #URLs | P3M impr | P3M pos |
|---|---|---|---|---|---|---|---|---|
| body scanning technology | 0 | 9188 | 0.0% | 10.1 | /content-hub/body-scanning-technology-for-apparel/ | 5 | 5948 | 10.6 |
| 3d body scanner | 1 | 1083 | 0.1% | 26.4 | / | 8 | 1494 | 19.3 |
| body scanner | 0 | 987 | 0.0% | 28.0 | / | 7 | 1294 | 26.0 |
| ai body scanner | 43 | 881 | 4.9% | 5.6 | / | 15 | 1261 | 3.2 |
| ai body scanner app | 22 | 537 | 4.1% | 8.4 | / | 4 | 1345 | 7.2 |
| 3d body scan | 0 | 489 | 0.0% | 34.2 | / | 6 | 1083 | 22.4 |
| ai body scan | 19 | 458 | 4.1% | 5.8 | / | 13 | 572 | 3.4 |
| 3d body analysis | 0 | 429 | 0.0% | 34.2 | / | 6 | 636 | 16.8 |
| 3 d body scan | 0 | 366 | 0.0% | 35.7 | / | 3 | 483 | 23.8 |
| body scanner ai | 32 | 269 | 11.9% | 2.8 | / | 11 | 264 | 1.2 |
| girl body scanner ai | 22 | 249 | 8.8% | 6.4 | / | 2 | 260 | 6.5 |
| 3d body scanning | 0 | 243 | 0.0% | 33.8 | / | 4 | 589 | 17.8 |
| data center body scanner | 0 | 206 | 0.0% | 12.2 | /content-hub/ai-body-scanners-vs-dexa-scans/ | 4 | 140 | 15.6 |
| 3d bodyscanner | 0 | 194 | 0.0% | 42.6 | / | 1 | 204 | 33.8 |
| body scanner website | 25 | 188 | 13.3% | 4.7 | / | 7 | 246 | 4.3 |

#### Body measurement (how-to / app / AI)

| Query | Clk | Impr | CTR | Pos | Ranking URL | #URLs | P3M impr | P3M pos |
|---|---|---|---|---|---|---|---|---|
| how to use a measuring tape for body | 2 | 1070 | 0.2% | 7.3 | /content-hub/how-to-take-your-body-measurements-at-home/ | 1 | 1345 | 6.7 |
| ai measurement tool | 8 | 530 | 1.5% | 3.7 | /mobile-tailor/ | 5 | 261 | 6.8 |
| ai measurement | 2 | 362 | 0.6% | 18.5 | /mobile-tailor/ | 2 | 194 | 18.5 |
| ai body measurements | 30 | 331 | 9.1% | 6.9 | /mobile-tailor/ | 6 | 378 | 4.9 |
| where can i get my measurements taken | 0 | 331 | 0.0% | 5.4 | /content-hub/how-to-take-your-body-measurements-at-home/ | 2 | 47 | 3.6 |
| how to use measuring tape for body | 0 | 320 | 0.0% | 5.8 | /content-hub/how-to-take-your-body-measurements-at-home/ | 1 | 354 | 6.9 |
| ai measuring tool | 6 | 317 | 1.9% | 2.5 | /mobile-tailor/ | 4 | 210 | 4.8 |
| how to take body measurements | 2 | 317 | 0.6% | 18.9 | /content-hub/how-to-take-your-body-measurements-at-home/ | 1 | 216 | 32.2 |
| body measurement software | 0 | 274 | 0.0% | 31.3 | /content-hub/body-measurement-software/ | 5 | 289 | 24.1 |
| how to read body measurements | 0 | 271 | 0.0% | 2.1 | /content-hub/how-to-take-your-body-measurements-at-home/ | 1 | 29 | 7.2 |
| ai body measurement | 6 | 238 | 2.5% | 16.0 | /mobile-tailor/ | 5 | 477 | 11.2 |
| body measurement 3d | 0 | 238 | 0.0% | 6.0 | /content-hub/3d-body-scanning/ | 4 | 281 | 5.7 |
| 3d body measurements | 1 | 234 | 0.4% | 20.9 | /content-hub/3d-body-scanning/ | 5 | 548 | 17.1 |
| digital body measurements | 1 | 233 | 0.4% | 38.5 | /content-hub/virtual-body-measurements/ | 8 | 264 | 22.5 |
| body measurement technology | 1 | 219 | 0.5% | 46.2 | /content-hub/body-measurement-software/ | 10 | 406 | 21.3 |

#### Progress tracking / body visualisation

| Query | Clk | Impr | CTR | Pos | Ranking URL | #URLs | P3M impr | P3M pos |
|---|---|---|---|---|---|---|---|---|
| weight tracker 3d | 92 | 1118 | 8.2% | 6.9 | / | 8 | 1264 | 4.4 |
| body visualizer | 4 | 679 | 0.6% | 44.4 | / | 4 | 678 | 55.7 |
| body measurements visualizer | 1 | 382 | 0.3% | 10.7 | /content-hub/3d-body-scanning/ | 2 | 52 | 28.2 |
| body measurement visualizer | 1 | 340 | 0.3% | 10.4 | /content-hub/3d-body-scanning/ | 3 | 42 | 35.5 |
| body calculator 3d | 4 | 295 | 1.4% | 9.7 | / | 2 | 482 | 9.7 |
| body 3d model weight | 0 | 282 | 0.0% | 7.7 | /content-hub/3d-body-scanning/ | 2 | 534 | 7.8 |
| height weight 3d | 1 | 255 | 0.4% | 7.7 | /content-hub/3d-body-scanning/ | 2 | 185 | 5.8 |
| what connected fitness equipment tracks progress? | 0 | 254 | 0.0% | 4.9 | /content-hub/connected-fitness-industry/ | 1 | 316 | 4.4 |
| body measurements 3d model | 1 | 205 | 0.5% | 17.4 | /content-hub/3d-body-scanning/ | 4 | 325 | 15.1 |
| body visualiser | 1 | 143 | 0.7% | 41.0 | / | 3 | 140 | 51.1 |
| 3d body visualizer | 1 | 136 | 0.7% | 44.1 | / | 3 | 328 | 27.9 |
| body image simulator | 0 | 115 | 0.0% | 9.7 | /content-hub/3d-body-scanning/ | 3 | 24 | 20.6 |
| best vendors to reduce returns using 3d fit and product visualization | 0 | 103 | 0.0% | 1.8 | /content-hub/virtual-clothing-try-on/ | 9 | 0 | - |
| body visualizer 3d | 0 | 101 | 0.0% | 39.3 | / | 4 | 119 | 39.7 |
| height weight 3d model | 0 | 100 | 0.0% | 7.9 | /content-hub/3d-body-scanning/ | 2 | 30 | 7.6 |

#### BMI

| Query | Clk | Impr | CTR | Pos | Ranking URL | #URLs | P3M impr | P3M pos |
|---|---|---|---|---|---|---|---|---|
| bmi 3d | 5 | 102 | 4.9% | 13.3 | / | 2 | 166 | 11.7 |
| bmi verification | 0 | 81 | 0.0% | 5.2 | /for-bmi-verification/ | 2 | 86 | 13.1 |
| how to bmi scales work | 0 | 77 | 0.0% | 35.0 | /content-hub/body-composition-scale/ | 1 | 27 | 45.3 |
| mobile body scanning software remote bmi verification | 0 | 69 | 0.0% | 1.0 | /content-hub/bariatric-pre-qualification-mobile-3d-body-scanning/ | 4 | 72 | 1.2 |
| at what bmi do abs show | 0 | 59 | 0.0% | 12.7 | /content-hub/visible-abs-myths-measurable-outcomes-ai-driven-3d-body-scanning/ | 1 | 236 | 10.5 |
| 3d bmi | 2 | 48 | 4.2% | 12.8 | / | 2 | 68 | 13.9 |
| bmi visualizer 3d | 2 | 43 | 4.7% | 20.1 | / | 2 | 117 | 19.3 |
| bmi 3d model | 1 | 43 | 2.3% | 13.7 | /content-hub/3d-body-scanning/ | 2 | 76 | 14.0 |
| bmi calculator weight tracker 3d | 2 | 42 | 4.8% | 8.7 | / | 2 | 104 | 7.8 |
| bmi model 3d | 1 | 38 | 2.6% | 12.1 | /content-hub/3d-body-scanning/ | 2 | 21 | 16.7 |
| 3d body bmi | 0 | 38 | 0.0% | 14.1 | /content-hub/3d-body-scanning/ | 2 | 48 | 11.8 |
| how do bmi scales work | 0 | 35 | 0.0% | 29.0 | /content-hub/body-composition-scale/ | 1 | 36 | 45.0 |
| bmi calculator 3d | 1 | 34 | 2.9% | 15.9 | / | 2 | 4663 | 8.9 |
| at what bmi are abs visible | 0 | 32 | 0.0% | 9.1 | /content-hub/visible-abs-myths-measurable-outcomes-ai-driven-3d-body-scanning/ | 1 | 42 | 9.0 |
| bmi body 3d | 0 | 19 | 0.0% | 8.3 | /content-hub/3d-body-scanning/ | 2 | 22 | 10.1 |

#### GLP-1 / weight loss / obesity

| Query | Clk | Impr | CTR | Pos | Ranking URL | #URLs | P3M impr | P3M pos |
|---|---|---|---|---|---|---|---|---|
| weight management market | 0 | 468 | 0.0% | 32.2 | /content-hub/weight-loss-industry-overview/ | 2 | 531 | 27.3 |
| 3d body image weight loss | 0 | 413 | 0.0% | 21.1 | /content-hub/body-scanning-technology-for-weight-loss/ | 4 | 567 | 13.8 |
| weight loss products market | 0 | 403 | 0.0% | 30.1 | /content-hub/weight-loss-industry-overview/ | 2 | 414 | 24.7 |
| weight loss industry | 3 | 402 | 0.7% | 6.0 | /content-hub/weight-loss-industry-overview/ | 2 | 1441 | 2.4 |
| medical weight loss clinic market | 0 | 366 | 0.0% | 13.0 | /content-hub/top-10-weight-loss-clinic-marketing-tips/ | 2 | 445 | 15.5 |
| glp-1 drug market | 0 | 363 | 0.0% | 61.6 | /content-hub/glp-1-market/ | 1 | 342 | 59.7 |
| weight management product market | 0 | 363 | 0.0% | 49.5 | /content-hub/weight-loss-industry-overview/ | 1 | 395 | 41.4 |
| weight control products market | 0 | 342 | 0.0% | 52.9 | /content-hub/weight-loss-industry-overview/ | 1 | 382 | 59.9 |
| glp-1 market | 0 | 277 | 0.0% | 62.4 | /content-hub/glp-1-market/ | 1 | 110 | 66.6 |
| glp 1 analogue market | 0 | 212 | 0.0% | 68.7 | /content-hub/glp-1-market/ | 1 | 116 | 66.4 |
| how to market a weight loss clinic | 0 | 187 | 0.0% | 15.3 | /content-hub/top-10-weight-loss-clinic-marketing-tips/ | 2 | 145 | 6.3 |
| slimming aids market | 0 | 181 | 0.0% | 64.0 | /content-hub/weight-loss-industry-overview/ | 1 | 360 | 44.6 |
| google ads for weight loss clinics | 0 | 149 | 0.0% | 16.9 | /content-hub/top-10-weight-loss-clinic-marketing-tips/ | 1 | 135 | 18.7 |
| us weight control products market | 0 | 109 | 0.0% | 45.3 | /content-hub/weight-loss-industry-overview/ | 1 | 311 | 39.8 |
| google ads for weight loss clinic | 0 | 99 | 0.0% | 24.0 | /content-hub/top-10-weight-loss-clinic-marketing-tips/ | 1 | 53 | 24.5 |

#### Weight-loss clinic marketing

| Query | Clk | Impr | CTR | Pos | Ranking URL | #URLs | P3M impr | P3M pos |
|---|---|---|---|---|---|---|---|---|
| weight loss clinic marketing | 0 | 3344 | 0.0% | 11.4 | /content-hub/top-10-weight-loss-clinic-marketing-tips/ | 1 | 2491 | 6.6 |
| successful weight loss clinic social media campaigns 2025 2026 | 0 | 2888 | 0.0% | 8.4 | /content-hub/top-10-weight-loss-clinic-marketing-tips/ | 1 | 817 | 8.3 |
| successful weight loss clinic social media campaigns | 0 | 787 | 0.0% | 6.1 | /content-hub/top-10-weight-loss-clinic-marketing-tips/ | 1 | 0 | - |
| weight loss marketing | 0 | 550 | 0.0% | 6.6 | /content-hub/top-10-weight-loss-clinic-marketing-tips/ | 1 | 473 | 3.1 |
| weight loss digital marketing | 0 | 394 | 0.0% | 3.5 | /content-hub/top-10-weight-loss-clinic-marketing-tips/ | 1 | 315 | 5.9 |
| marketing for weight loss clinic | 0 | 308 | 0.0% | 12.2 | /content-hub/top-10-weight-loss-clinic-marketing-tips/ | 1 | 219 | 7.8 |
| digital marketing for weight loss | 0 | 263 | 0.0% | 5.4 | /content-hub/top-10-weight-loss-clinic-marketing-tips/ | 1 | 191 | 5.8 |
| medical weight loss marketing | 0 | 262 | 0.0% | 18.0 | /content-hub/top-10-weight-loss-clinic-marketing-tips/ | 1 | 854 | 5.4 |
| weight loss clinic marketing plan | 0 | 214 | 0.0% | 2.6 | /content-hub/top-10-weight-loss-clinic-marketing-tips/ | 1 | 141 | 2.4 |
| weight loss clinic advertising | 1 | 192 | 0.5% | 15.3 | /content-hub/top-10-weight-loss-clinic-marketing-tips/ | 1 | 206 | 10.6 |
| marketing weight loss | 0 | 191 | 0.0% | 2.3 | /content-hub/top-10-weight-loss-clinic-marketing-tips/ | 1 | 167 | 2.1 |
| medical weight loss marketing agency | 0 | 164 | 0.0% | 35.1 | /content-hub/top-10-weight-loss-clinic-marketing-tips/ | 1 | 7 | 45.6 |
| weight loss program marketing | 0 | 151 | 0.0% | 1.4 | /content-hub/top-10-weight-loss-clinic-marketing-tips/ | 1 | 2028 | 1.1 |
| digital marketing for weight loss clinics | 0 | 150 | 0.0% | 8.4 | /content-hub/top-10-weight-loss-clinic-marketing-tips/ | 1 | 150 | 2.6 |
| weight loss seo | 0 | 149 | 0.0% | 59.1 | /content-hub/top-10-weight-loss-clinic-marketing-tips/ | 1 | 157 | 28.7 |

#### Telehealth / digital health / AI in healthcare

| Query | Clk | Impr | CTR | Pos | Ranking URL | #URLs | P3M impr | P3M pos |
|---|---|---|---|---|---|---|---|---|
| ai in telehealth | 0 | 820 | 0.0% | 29.9 | /content-hub/the-potential-of-ai-in-telehealth/ | 1 | 633 | 26.6 |
| ai telehealth | 0 | 742 | 0.0% | 21.8 | /content-hub/the-potential-of-ai-in-telehealth/ | 1 | 716 | 15.2 |
| artificial intelligence in telemedicine | 0 | 501 | 0.0% | 33.1 | /content-hub/the-potential-of-ai-in-telehealth/ | 1 | 543 | 30.2 |
| ai in telemedicine | 0 | 396 | 0.0% | 27.8 | /content-hub/the-potential-of-ai-in-telehealth/ | 1 | 427 | 26.3 |
| applied ai in healthcare market | 0 | 339 | 0.0% | 72.4 | /content-hub/ai-healthcare-ai-used-today-key-applications-real-world-examples-industry-impact/ | 1 | 355 | 68.3 |
| which companies are shaping the future of healthcare technology? | 0 | 194 | 0.0% | 8.6 | /content-hub/top-health-tech-companies/ | 1 | 52 | 8.3 |
| health tech companies | 0 | 152 | 0.0% | 60.0 | /content-hub/top-health-tech-companies/ | 1 | 77 | 21.7 |
| telemedicine ai | 0 | 150 | 0.0% | 24.3 | /content-hub/the-potential-of-ai-in-telehealth/ | 1 | 151 | 25.0 |
| ai in the healthcare industry | 0 | 107 | 0.0% | 79.9 | /content-hub/ai-healthcare-ai-used-today-key-applications-real-world-examples-industry-impact/ | 1 | 122 | 78.3 |
| visual ai tools for telehealth patient consultations | 0 | 102 | 0.0% | 33.8 | /content-hub/the-potential-of-ai-in-telehealth/ | 1 | 113 | 23.0 |
| ai for telehealth | 0 | 101 | 0.0% | 30.9 | /content-hub/the-potential-of-ai-in-telehealth/ | 1 | 94 | 26.4 |
| best mobile body scanning solution patient engagement | 0 | 98 | 0.0% | 3.0 | /content-hub/body-scanner-machines-vs-mobile-3d-body-scan/ | 5 | 84 | 3.9 |
| wellness and fitness companies | 0 | 98 | 0.0% | 30.9 | /content-hub/top-fitness-tech-companies/ | 1 | 128 | 15.4 |
| health tech company | 0 | 94 | 0.0% | 58.1 | /content-hub/top-health-tech-companies/ | 1 | 183 | 15.7 |
| healthcare technology companies | 0 | 94 | 0.0% | 51.3 | /content-hub/top-health-tech-companies/ | 1 | 228 | 21.7 |

#### Waist / circumference / anthropometrics

| Query | Clk | Impr | CTR | Pos | Ranking URL | #URLs | P3M impr | P3M pos |
|---|---|---|---|---|---|---|---|---|
| how to measure waist with phone | 1 | 375 | 0.3% | 6.2 | /content-hub/how-to-take-your-body-measurements-at-home/ | 6 | 487 | 6.7 |
| how many inches does your waist fluctuate in a day | 3 | 167 | 1.8% | 2.7 | /content-hub/the-enormous-impact-of-daily-physiological-changes-on-the-accuracy-of-our-body-measurements/ | 1 | 147 | 2.3 |
| best time to measure waist | 0 | 137 | 0.0% | 5.8 | /content-hub/the-enormous-impact-of-daily-physiological-changes-on-the-accuracy-of-our-body-measurements/ | 1 | 133 | 6.0 |
| does your waist size change | 0 | 128 | 0.0% | 5.7 | /content-hub/the-enormous-impact-of-daily-physiological-changes-on-the-accuracy-of-our-body-measurements/ | 1 | 215 | 3.8 |
| is your waist smaller in the morning | 0 | 124 | 0.0% | 5.8 | /content-hub/the-enormous-impact-of-daily-physiological-changes-on-the-accuracy-of-our-body-measurements/ | 1 | 94 | 3.6 |
| how much can your waist fluctuate in a day | 2 | 104 | 1.9% | 3.5 | /content-hub/the-enormous-impact-of-daily-physiological-changes-on-the-accuracy-of-our-body-measurements/ | 1 | 64 | 2.8 |
| how much does your waist expand after eating | 3 | 102 | 2.9% | 2.3 | /content-hub/the-enormous-impact-of-daily-physiological-changes-on-the-accuracy-of-our-body-measurements/ | 1 | 113 | 1.7 |
| how much does waist size fluctuate during the day | 1 | 102 | 1.0% | 3.2 | /content-hub/the-enormous-impact-of-daily-physiological-changes-on-the-accuracy-of-our-body-measurements/ | 1 | 125 | 2.1 |
| does your waist size change throughout the day | 3 | 79 | 3.8% | 2.1 | /content-hub/the-enormous-impact-of-daily-physiological-changes-on-the-accuracy-of-our-body-measurements/ | 2 | 49 | 2.0 |
| does waist size fluctuate throughout the day | 2 | 79 | 2.5% | 1.6 | /content-hub/the-enormous-impact-of-daily-physiological-changes-on-the-accuracy-of-our-body-measurements/ | 2 | 39 | 2.2 |
| does your waist size change with age | 0 | 77 | 0.0% | 5.7 | /content-hub/the-enormous-impact-of-daily-physiological-changes-on-the-accuracy-of-our-body-measurements/ | 1 | 73 | 4.5 |
| how much can waist size fluctuate in a day | 1 | 70 | 1.4% | 2.3 | /content-hub/the-enormous-impact-of-daily-physiological-changes-on-the-accuracy-of-our-body-measurements/ | 1 | 53 | 3.0 |
| is your waist bigger at night | 0 | 65 | 0.0% | 3.8 | /content-hub/the-enormous-impact-of-daily-physiological-changes-on-the-accuracy-of-our-body-measurements/ | 1 | 63 | 2.1 |
| should i measure my waist before or after eating | 0 | 61 | 0.0% | 3.3 | /content-hub/the-enormous-impact-of-daily-physiological-changes-on-the-accuracy-of-our-body-measurements/ | 1 | 45 | 5.2 |
| how much does your waist expand during the day | 0 | 58 | 0.0% | 2.6 | /content-hub/the-enormous-impact-of-daily-physiological-changes-on-the-accuracy-of-our-body-measurements/ | 1 | 58 | 1.6 |

#### Fitness tech / fitness industry

| Query | Clk | Impr | CTR | Pos | Ranking URL | #URLs | P3M impr | P3M pos |
|---|---|---|---|---|---|---|---|---|
| fitness technology | 1 | 735 | 0.1% | 11.9 | /content-hub/top-fitness-tech-companies/ | 1 | 1236 | 14.5 |
| fitness software companies | 0 | 633 | 0.0% | 18.3 | /content-hub/top-fitness-tech-companies/ | 1 | 844 | 13.6 |
| connected fitness | 1 | 597 | 0.2% | 6.9 | /content-hub/connected-fitness-industry/ | 1 | 897 | 9.8 |
| ai fitness vs movement intelligence | 0 | 511 | 0.0% | 15.5 | /content-hub/ai-in-fitness-industry/ | 1 | 162 | 11.7 |
| connected gym equipment market | 0 | 459 | 0.0% | 17.3 | /content-hub/connected-fitness-industry/ | 1 | 618 | 17.4 |
| tech fitness | 0 | 433 | 0.0% | 9.0 | /content-hub/top-fitness-tech-companies/ | 3 | 13058 | 7.7 |
| connected fitness equipment | 1 | 405 | 0.2% | 7.9 | /content-hub/connected-fitness-industry/ | 1 | 413 | 11.2 |
| gym fitness company acquisitions technology | 0 | 392 | 0.0% | 9.8 | /content-hub/top-fitness-tech-companies/ | 1 | 0 | - |
| fitness companies | 1 | 366 | 0.3% | 18.5 | /content-hub/top-fitness-tech-companies/ | 1 | 681 | 12.9 |
| ai fitness | 4 | 341 | 1.2% | 23.0 | /content-hub/ai-in-fitness-industry/ | 2 | 802 | 14.7 |
| health fitness companies | 0 | 312 | 0.0% | 37.9 | /content-hub/top-fitness-tech-companies/ | 1 | 279 | 27.7 |
| health and fitness companies | 0 | 303 | 0.0% | 34.4 | /content-hub/top-fitness-tech-companies/ | 1 | 363 | 21.0 |
| fitness apps vs movement intelligence | 0 | 295 | 0.0% | 34.2 | /content-hub/ai-in-fitness-industry/ | 1 | 105 | 24.6 |
| top health and fitness companies | 0 | 289 | 0.0% | 44.3 | /content-hub/top-fitness-tech-companies/ | 1 | 292 | 20.7 |
| fitness tech | 3 | 285 | 1.1% | 14.4 | /content-hub/top-fitness-tech-companies/ | 2 | 506 | 11.4 |

#### Brand: 3DLOOK / other brand

| Query | Clk | Impr | CTR | Pos | Ranking URL | #URLs | P3M impr | P3M pos |
|---|---|---|---|---|---|---|---|---|
| 3dlook | 1712 | 2715 | 63.1% | 1.1 | / | 39 | 3644 | 1.4 |
| 3d look | 522 | 1151 | 45.4% | 1.1 | / | 27 | 1355 | 1.1 |
| mobile tailor | 89 | 1080 | 8.2% | 6.7 | /mobile-tailor/ | 10 | 812 | 4.1 |
| new york city mobile tailor | 0 | 310 | 0.0% | 45.0 | /mobile-tailor/for-made-to-measure/ | 2 | 98 | 46.8 |
| 3dlook mobile tailor | 123 | 197 | 62.4% | 2.7 | /mobile-tailor/ | 37 | 220 | 1.1 |
| site:3dlook.ai | 0 | 190 | 0.0% | 27.4 | /content-hub/ | 138 | 76 | 23.6 |
| which is better for determining size and fit, true fit or 3dlook? | 0 | 187 | 0.0% | 2.2 | /content-hub/size-recommendation-tools/ | 24 | 105 | 2.6 |
| which is better: mirrar vs. 3dlook | 0 | 97 | 0.0% | 3.1 | /content-hub/fit3d-vs-3dlook/ | 8 | 172 | 3.3 |
| 3dlook company | 4 | 94 | 4.3% | 1.9 | / | 16 | 75 | 1.0 |
| mobile tailor app | 16 | 90 | 17.8% | 1.3 | /mobile-tailor/ | 5 | 103 | 1.2 |
| based on reviews mirrar vs. 3dlook | 0 | 88 | 0.0% | 3.9 | /content-hub/fit3d-vs-3dlook/ | 6 | 86 | 4.2 |
| 3d look ai | 44 | 78 | 56.4% | 1.0 | / | 13 | 93 | 1.0 |
| site:3dlook.me | 0 | 63 | 0.0% | 14.5 | / | 38 | 24 | 6.0 |
| 3dlook official website | 0 | 61 | 0.0% | 1.0 | / | 13 | 89 | 1.0 |
| 3d looks | 18 | 58 | 31.0% | 1.2 | / | 15 | 52 | 1.0 |

## 2. Striking distance — health/fitness queries at avg position 4–20 (L3M, ≥80 impressions)

Sorted by impressions. 'Upside' = rough extra clicks/3 months if the query reached ~position 3 at an assumed 6% CTR (AIO-depressed benchmark) minus current clicks. ICP flag = query signals B2B/buyer or ICP vertical (api/sdk/software/app/scanner/verification/telehealth/clinic/insurance/pharmacy/GLP-1/bariatric/occupational/clinical).

| # | Query | Cluster | Clk | Impr | CTR | Pos | URL | Upside | ICP |
|---|---|---|---|---|---|---|---|---|---|
| 1 | body scanning technology | Body scanning (AI / 3D / mobile) | 0 | 9188 | 0.0% | 10.1 | /content-hub/body-scanning-technology-for-apparel/ (+4 more) | 551 | Y |
| 2 | lean body mass | Body composition / body fat / lean mass | 1 | 8844 | 0.0% | 7.2 | /content-hub/lean-body-mass-vs-muscle-mass/ | 530 |  |
| 3 | lean muscle mass | Body composition / body fat / lean mass | 0 | 4728 | 0.0% | 6.4 | /content-hub/lean-body-mass-vs-muscle-mass/ | 284 |  |
| 4 | weight loss clinic marketing | Weight-loss clinic marketing | 0 | 3344 | 0.0% | 11.4 | /content-hub/top-10-weight-loss-clinic-marketing-tips/ | 201 | Y |
| 5 | successful weight loss clinic social media campaigns 2025 2026 | Weight-loss clinic marketing | 0 | 2888 | 0.0% | 8.4 | /content-hub/top-10-weight-loss-clinic-marketing-tips/ | 173 | Y |
| 6 | what is lean body mass | Body composition / body fat / lean mass | 1 | 2534 | 0.0% | 9.1 | /content-hub/lean-body-mass-vs-muscle-mass/ | 151 |  |
| 7 | lean body mass meaning | Body composition / body fat / lean mass | 0 | 2310 | 0.0% | 9.4 | /content-hub/lean-body-mass-vs-muscle-mass/ | 139 |  |
| 8 | lean mass meaning | Body composition / body fat / lean mass | 0 | 1738 | 0.0% | 7.7 | /content-hub/lean-body-mass-vs-muscle-mass/ | 104 |  |
| 9 | what is lean mass | Body composition / body fat / lean mass | 0 | 1627 | 0.0% | 8.1 | /content-hub/lean-body-mass-vs-muscle-mass/ | 98 |  |
| 10 | what is lean muscle mass | Body composition / body fat / lean mass | 1 | 1183 | 0.1% | 6.6 | /content-hub/lean-body-mass-vs-muscle-mass/ (+1 more) | 70 |  |
| 11 | weight tracker 3d | Progress tracking / body visualisation | 92 | 1118 | 8.2% | 6.9 | / (+7 more) | 0 |  |
| 12 | how to use a measuring tape for body | Body measurement (how-to / app / AI) | 2 | 1070 | 0.2% | 7.3 | /content-hub/how-to-take-your-body-measurements-at-home/ | 62 |  |
| 13 | bia scan | Body composition / body fat / lean mass | 0 | 1008 | 0.0% | 5.8 | /content-hub/bia-scan/ | 60 |  |
| 14 | ai body scanner | Body scanning (AI / 3D / mobile) | 43 | 881 | 4.9% | 5.6 | / (+14 more) | 10 | Y |
| 15 | successful weight loss clinic social media campaigns | Weight-loss clinic marketing | 0 | 787 | 0.0% | 6.1 | /content-hub/top-10-weight-loss-clinic-marketing-tips/ | 47 | Y |
| 16 | fitness technology | Fitness tech / fitness industry | 1 | 735 | 0.1% | 11.9 | /content-hub/top-fitness-tech-companies/ | 43 | Y |
| 17 | dry lean mass | Body composition / body fat / lean mass | 3 | 725 | 0.4% | 5.8 | /content-hub/lean-body-mass-vs-muscle-mass/ | 40 |  |
| 18 | lean body mass คือ | Body composition / body fat / lean mass | 0 | 659 | 0.0% | 10.5 | /content-hub/lean-body-mass-vs-muscle-mass/ | 40 |  |
| 19 | fitness software companies | Fitness tech / fitness industry | 0 | 633 | 0.0% | 18.3 | /content-hub/top-fitness-tech-companies/ | 38 | Y |
| 20 | how does a body composition scale work | Body composition / body fat / lean mass | 0 | 613 | 0.0% | 7.1 | /content-hub/body-composition-scale/ | 37 |  |
| 21 | connected fitness | Fitness tech / fitness industry | 1 | 597 | 0.2% | 6.9 | /content-hub/connected-fitness-industry/ | 35 |  |
| 22 | when do abs start to show | Body composition / body fat / lean mass | 1 | 574 | 0.2% | 4.1 | /content-hub/visible-abs-myths-measurable-outcomes-ai-driven-3d-body-scanning/ | 33 |  |
| 23 | weight loss marketing | Weight-loss clinic marketing | 0 | 550 | 0.0% | 6.6 | /content-hub/top-10-weight-loss-clinic-marketing-tips/ | 33 |  |
| 24 | ai body scanner app | Body scanning (AI / 3D / mobile) | 22 | 537 | 4.1% | 8.4 | / (+3 more) | 10 | Y |
| 25 | what is dry lean mass | Body composition / body fat / lean mass | 1 | 536 | 0.2% | 4.4 | /content-hub/lean-body-mass-vs-muscle-mass/ | 31 |  |
| 26 | ai fitness vs movement intelligence | Fitness tech / fitness industry | 0 | 511 | 0.0% | 15.5 | /content-hub/ai-in-fitness-industry/ | 31 |  |
| 27 | lean muscle mass meaning | Body composition / body fat / lean mass | 0 | 508 | 0.0% | 7.4 | /content-hub/lean-body-mass-vs-muscle-mass/ | 30 |  |
| 28 | connected gym equipment market | Fitness tech / fitness industry | 0 | 459 | 0.0% | 17.3 | /content-hub/connected-fitness-industry/ | 28 |  |
| 29 | ai body scan | Body scanning (AI / 3D / mobile) | 19 | 458 | 4.1% | 5.8 | / (+12 more) | 8 |  |
| 30 | tech fitness | Fitness tech / fitness industry | 0 | 433 | 0.0% | 9.0 | /content-hub/top-fitness-tech-companies/ (+2 more) | 26 |  |
| 31 | body fat percentage for visible abs men | Body composition / body fat / lean mass | 0 | 410 | 0.0% | 5.0 | /content-hub/visible-abs-myths-measurable-outcomes-ai-driven-3d-body-scanning/ | 25 |  |
| 32 | connected fitness equipment | Fitness tech / fitness industry | 1 | 405 | 0.2% | 7.9 | /content-hub/connected-fitness-industry/ | 23 |  |
| 33 | weight loss industry | GLP-1 / weight loss / obesity | 3 | 402 | 0.7% | 6.0 | /content-hub/weight-loss-industry-overview/ (+1 more) | 21 |  |
| 34 | lean body mass vs skeletal muscle mass | Body composition / body fat / lean mass | 0 | 396 | 0.0% | 5.3 | /content-hub/lean-body-mass-vs-muscle-mass/ (+1 more) | 24 |  |
| 35 | gym fitness company acquisitions technology | Fitness tech / fitness industry | 0 | 392 | 0.0% | 9.8 | /content-hub/top-fitness-tech-companies/ | 24 | Y |
| 36 | body measurements visualizer | Progress tracking / body visualisation | 1 | 382 | 0.3% | 10.7 | /content-hub/3d-body-scanning/ (+1 more) | 22 |  |
| 37 | how to measure waist with phone | Waist / circumference / anthropometrics | 1 | 375 | 0.3% | 6.2 | /content-hub/how-to-take-your-body-measurements-at-home/ (+5 more) | 22 |  |
| 38 | fitxpress | Brand: FitXpress | 21 | 373 | 5.6% | 6.0 | /for-bmi-verification/ (+7 more) | 1 |  |
| 39 | fitness companies | Fitness tech / fitness industry | 1 | 366 | 0.3% | 18.5 | /content-hub/top-fitness-tech-companies/ | 21 | Y |
| 40 | medical weight loss clinic market | GLP-1 / weight loss / obesity | 0 | 366 | 0.0% | 13.0 | /content-hub/top-10-weight-loss-clinic-marketing-tips/ (+1 more) | 22 | Y |
| 41 | lean mass vs muscle mass | Body composition / body fat / lean mass | 0 | 365 | 0.0% | 6.5 | /content-hub/lean-body-mass-vs-muscle-mass/ | 22 |  |
| 42 | ai measurement | Body measurement (how-to / app / AI) | 2 | 362 | 0.6% | 18.5 | /mobile-tailor/ (+1 more) | 20 |  |
| 43 | body measurement visualizer | Progress tracking / body visualisation | 1 | 340 | 0.3% | 10.4 | /content-hub/3d-body-scanning/ (+2 more) | 19 |  |
| 44 | ai body measurements | Body measurement (how-to / app / AI) | 30 | 331 | 9.1% | 6.9 | /mobile-tailor/ (+5 more) | 0 |  |
| 45 | where can i get my measurements taken | Body measurement (how-to / app / AI) | 0 | 331 | 0.0% | 5.4 | /content-hub/how-to-take-your-body-measurements-at-home/ (+1 more) | 20 |  |
| 46 | how do body composition scales work | Body composition / body fat / lean mass | 2 | 327 | 0.6% | 8.5 | /content-hub/body-composition-scale/ | 18 |  |
| 47 | how to use measuring tape for body | Body measurement (how-to / app / AI) | 0 | 320 | 0.0% | 5.8 | /content-hub/how-to-take-your-body-measurements-at-home/ | 19 |  |
| 48 | how to take body measurements | Body measurement (how-to / app / AI) | 2 | 317 | 0.6% | 18.9 | /content-hub/how-to-take-your-body-measurements-at-home/ | 17 |  |
| 49 | marketing for weight loss clinic | Weight-loss clinic marketing | 0 | 308 | 0.0% | 12.2 | /content-hub/top-10-weight-loss-clinic-marketing-tips/ | 18 | Y |
| 50 | body calculator 3d | Progress tracking / body visualisation | 4 | 295 | 1.4% | 9.7 | / (+1 more) | 14 |  |

Total health/fitness striking-distance queries (pos 4–20, ≥80 impr): 197; impressions 80,186; clicks 402.

### 2b. ICP/B2B-intent subset (pos 4–20, ≥30 impressions)

| Query | Clk | Impr | Pos | URL |
|---|---|---|---|---|
| body scanning technology | 0 | 9188 | 10.1 | /content-hub/body-scanning-technology-for-apparel/ (+4) |
| weight loss clinic marketing | 0 | 3344 | 11.4 | /content-hub/top-10-weight-loss-clinic-marketing-tips/ |
| successful weight loss clinic social media campaigns 2025 2026 | 0 | 2888 | 8.4 | /content-hub/top-10-weight-loss-clinic-marketing-tips/ |
| ai body scanner | 43 | 881 | 5.6 | / (+14) |
| successful weight loss clinic social media campaigns | 0 | 787 | 6.1 | /content-hub/top-10-weight-loss-clinic-marketing-tips/ |
| fitness technology | 1 | 735 | 11.9 | /content-hub/top-fitness-tech-companies/ |
| fitness software companies | 0 | 633 | 18.3 | /content-hub/top-fitness-tech-companies/ |
| ai body scanner app | 22 | 537 | 8.4 | / (+3) |
| gym fitness company acquisitions technology | 0 | 392 | 9.8 | /content-hub/top-fitness-tech-companies/ |
| fitness companies | 1 | 366 | 18.5 | /content-hub/top-fitness-tech-companies/ |
| medical weight loss clinic market | 0 | 366 | 13.0 | /content-hub/top-10-weight-loss-clinic-marketing-tips/ (+1) |
| marketing for weight loss clinic | 0 | 308 | 12.2 | /content-hub/top-10-weight-loss-clinic-marketing-tips/ |
| girl body scanner ai | 22 | 249 | 6.4 | / (+1) |
| fitness tech companies | 0 | 233 | 10.0 | /content-hub/top-fitness-tech-companies/ |
| data center body scanner | 0 | 206 | 12.2 | /content-hub/ai-body-scanners-vs-dexa-scans/ (+3) |
| which companies are shaping the future of healthcare technology? | 0 | 194 | 8.6 | /content-hub/top-health-tech-companies/ |
| weight loss clinic advertising | 1 | 192 | 15.3 | /content-hub/top-10-weight-loss-clinic-marketing-tips/ |
| body scanner website | 25 | 188 | 4.7 | / (+6) |
| how to market a weight loss clinic | 0 | 187 | 15.3 | /content-hub/top-10-weight-loss-clinic-marketing-tips/ (+1) |
| online body scanner | 16 | 185 | 14.9 | / (+11) |
| body scanner machine | 0 | 156 | 19.4 | /content-hub/body-scanner-machines-vs-mobile-3d-body-scan/ (+3) |
| connected fitness solutions | 0 | 152 | 7.9 | /content-hub/connected-fitness-industry/ |
| digital marketing for weight loss clinics | 0 | 150 | 8.4 | /content-hub/top-10-weight-loss-clinic-marketing-tips/ |
| google ads for weight loss clinics | 0 | 149 | 16.9 | /content-hub/top-10-weight-loss-clinic-marketing-tips/ |
| female body scanner online | 7 | 137 | 8.5 | / (+1) |
| fitness technology platform | 0 | 132 | 14.9 | /content-hub/top-fitness-tech-companies/ (+1) |
| ai measurement app | 0 | 116 | 7.0 | /mobile-tailor/ (+1) |
| what brands offer technology-based fitness recovery solutions? | 0 | 115 | 6.8 | /content-hub/top-fitness-tech-companies/ |
| weight loss marketing companies | 0 | 110 | 19.5 | /content-hub/top-10-weight-loss-clinic-marketing-tips/ |
| body scanner online | 6 | 92 | 6.6 | / (+2) |
| ai telemedicine | 0 | 90 | 19.2 | /content-hub/the-potential-of-ai-in-telehealth/ |
| weight loss clinic marketing focas ams | 2 | 88 | 12.1 | /content-hub/top-10-weight-loss-clinic-marketing-tips/ |
| mobile body scanner | 0 | 88 | 18.5 | / (+7) |
| mobile body scanning platforms body composition tracking | 0 | 86 | 9.3 | /content-hub/body-scanning-technology-for-weight-loss/ (+2) |
| healthcare technology experts | 0 | 83 | 14.8 | /content-hub/top-health-tech-companies/ |
| most accurate body measurement solution from smartphone photo | 0 | 83 | 4.0 | /content-hub/virtual-body-measurements/ (+1) |
| bmi verification | 0 | 81 | 5.2 | /for-bmi-verification/ (+1) |
| ai body measurement app | 2 | 79 | 10.3 | /mobile-tailor/ (+5) |
| body composition software visualization client engagement | 0 | 79 | 4.5 | /content-hub/beyond-bmi-business/ (+2) |
| body measurement scanner | 1 | 73 | 19.4 | / (+7) |

### 2c. Already top-3 but CTR < 1% (AI Overview / snippet mismatch) — health/fitness, ≥150 impr

| Query | Clk | Impr | Pos | URL |
|---|---|---|---|---|
| lean mass | 0 | 6346 | 3.9 | /content-hub/lean-body-mass-vs-muscle-mass/ |
| lean meaning body | 0 | 5014 | 2.6 | /content-hub/lean-body-mass-vs-muscle-mass/ |
| lean body meaning | 0 | 2532 | 3.5 | /content-hub/lean-body-mass-vs-muscle-mass/ |
| lean body | 0 | 2021 | 3.0 | /content-hub/lean-body-mass-vs-muscle-mass/ |
| skeletal muscle mass | 0 | 894 | 1.1 | /content-hub/lean-body-mass-vs-muscle-mass/ |
| weight loss digital marketing | 0 | 394 | 3.5 | /content-hub/top-10-weight-loss-clinic-marketing-tips/ |
| skeletal muscle vs muscle mass | 1 | 291 | 3.8 | /content-hub/lean-body-mass-vs-muscle-mass/ |
| what does lean mean in body | 0 | 278 | 1.2 | /content-hub/lean-body-mass-vs-muscle-mass/ |
| how to read body measurements | 0 | 271 | 2.1 | /content-hub/how-to-take-your-body-measurements-at-home/ |
| how to measure body fat | 0 | 267 | 1.3 | /content-hub/how-to-measure-body-composition/ |
| abs | 0 | 258 | 1.2 | /content-hub/visible-abs-myths-measurable-outcomes-ai-driven-3d-body-scanning/ |
| what is lean body | 0 | 250 | 2.6 | /content-hub/lean-body-mass-vs-muscle-mass/ |
| weight loss clinic marketing plan | 0 | 214 | 2.6 | /content-hub/top-10-weight-loss-clinic-marketing-tips/ |
| how to measure your body with a measuring tape | 0 | 201 | 2.8 | /content-hub/how-to-take-your-body-measurements-at-home/ |
| marketing weight loss | 0 | 191 | 2.3 | /content-hub/top-10-weight-loss-clinic-marketing-tips/ |
| what is connected fitness? | 0 | 165 | 2.9 | /content-hub/connected-fitness-industry/ |
| dry lean mass vs skeletal muscle mass | 1 | 161 | 2.9 | /content-hub/lean-body-mass-vs-muscle-mass/ |
| weight loss program marketing | 0 | 151 | 1.4 | /content-hub/top-10-weight-loss-clinic-marketing-tips/ |
| when do abs become visible | 1 | 150 | 3.5 | /content-hub/visible-abs-myths-measurable-outcomes-ai-driven-3d-body-scanning/ |

## 3. Pages — top 60 by impressions (L3M), with P3M and YoY

Flag: HEALTH = health/fitness/body-composition topic by URL; apparel = fashion/apparel topic; blank = corporate/other.

| # | Page | Flag | Clk L3M | Impr L3M | CTR | Pos | Clk P3M | Impr P3M | Pos P3M | Clk YoY | Impr YoY | Impr vs P3M |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | /content-hub/visible-abs-myths-measurable-outcomes-ai-driven-3d-body-scanning/ | HEALTH | 188 | 80,678 | 0.2% | 7.6 | 337 | 280,690 | 7.8 | 0 | 0 | -71% |
| 2 | /content-hub/lean-body-mass-vs-muscle-mass/ | HEALTH | 56 | 79,772 | 0.1% | 6.1 | 118 | 138,271 | 6.6 | 0 | 1,343 | -42% |
| 3 | / |  | 4256 | 63,330 | 6.7% | 17.3 | 7192 | 133,063 | 10.7 | 22891 | 274,033 | -52% |
| 4 | /content-hub/the-enormous-impact-of-daily-physiological-changes-on-the-accuracy-of-our-body-measurements/ | HEALTH | 285 | 58,105 | 0.5% | 5.0 | 313 | 99,880 | 5.2 | 453 | 45,969 | -42% |
| 5 | /content-hub/body-scanning-technology-for-apparel/ | apparel | 159 | 44,508 | 0.4% | 6.0 | 308 | 69,656 | 5.7 | 595 | 88,534 | -36% |
| 6 | /mobile-tailor/ | apparel | 1724 | 44,121 | 3.9% | 9.0 | 2046 | 65,842 | 6.9 | 2877 | 118,499 | -33% |
| 7 | /content-hub/virtual-clothing-try-on/ | apparel | 313 | 43,735 | 0.7% | 12.8 | 575 | 88,618 | 10.7 | 825 | 113,319 | -51% |
| 8 | /content-hub/body-measurement-app-for-clothing/ | apparel | 783 | 32,440 | 2.4% | 9.1 | 1468 | 83,267 | 7.0 | 1837 | 133,775 | -61% |
| 9 | /content-hub/how-to-take-your-body-measurements-at-home/ | HEALTH | 93 | 31,585 | 0.3% | 6.1 | 92 | 31,108 | 7.3 | 58 | 26,274 | +2% |
| 10 | /content-hub/3d-body-scanning/ | HEALTH | 79 | 17,221 | 0.5% | 14.1 | 168 | 27,744 | 11.1 | 252 | 18,254 | -38% |
| 11 | /content-hub/top-10-weight-loss-clinic-marketing-tips/ | HEALTH | 23 | 17,187 | 0.1% | 13.9 | 73 | 23,093 | 8.6 | 100 | 22,969 | -26% |
| 12 | /content-hub/average-conversion-rate-for-fashion-ecommerce/ | apparel | 20 | 16,004 | 0.1% | 10.6 | 46 | 52,259 | 7.1 | 64 | 52,850 | -69% |
| 13 | /content-hub/on-demand-clothing-manufacturing/ | apparel | 23 | 15,567 | 0.1% | 8.3 | 56 | 15,929 | 8.4 | 103 | 25,465 | -2% |
| 14 | /about-us/ |  | 53 | 15,454 | 0.3% | 3.8 | 57 | 14,723 | 3.2 | 69 | 62,137 | +5% |
| 15 | /content-hub/virtual-body-measurements/ | HEALTH | 532 | 13,928 | 3.8% | 12.5 | 1441 | 48,089 | 7.4 | 1177 | 88,509 | -71% |
| 16 | /pricing/ |  | 159 | 13,679 | 1.2% | 3.5 | 255 | 22,201 | 3.7 | 286 | 48,728 | -38% |
| 17 | /content-hub/ai-in-fitness-industry/ | HEALTH | 88 | 13,638 | 0.6% | 12.0 | 150 | 62,062 | 7.4 | 595 | 122,189 | -78% |
| 18 | /content-hub/top-11-fashion-technologies/ | apparel | 20 | 11,875 | 0.2% | 19.4 | 62 | 23,075 | 15.0 | 226 | 71,549 | -49% |
| 19 | /content-hub/virtual-fitting-room-for-ecommerce/ | apparel | 40 | 11,780 | 0.3% | 16.5 | 71 | 20,155 | 17.9 | 306 | 61,822 | -42% |
| 20 | /content-hub/top-fitness-tech-companies/ | HEALTH | 23 | 10,512 | 0.2% | 21.7 | 95 | 42,945 | 9.2 | 429 | 100,043 | -76% |
| 21 | /content-hub/artificial-intelligence-in-fashion/ | apparel | 7 | 9,782 | 0.1% | 17.0 | 25 | 27,081 | 10.4 | 181 | 56,705 | -64% |
| 22 | /content-hub/top-fitness-industry-trends/ | HEALTH | 10 | 8,950 | 0.1% | 20.2 | 49 | 37,724 | 11.8 | 0 | 2 | -76% |
| 23 | /content-hub/body-composition-scale/ | HEALTH | 31 | 8,869 | 0.3% | 8.4 | 16 | 10,388 | 8.3 | 0 | 0 | -15% |
| 24 | /content-hub/the-future-of-fashion-retail/ | apparel | 9 | 8,221 | 0.1% | 37.4 | 40 | 24,638 | 20.1 | 159 | 96,161 | -67% |
| 25 | /content-hub/apparel-return-rates-the-stats-retailers-cannot-ignore/ | apparel | 18 | 7,759 | 0.2% | 15.7 | 47 | 35,477 | 9.0 | 132 | 45,550 | -78% |
| 26 | /content-hub/connected-fitness-industry/ | HEALTH | 11 | 7,628 | 0.1% | 10.9 | 25 | 20,226 | 9.0 | 65 | 21,744 | -62% |
| 27 | /content-hub/weight-loss-industry-overview/ | HEALTH | 19 | 7,007 | 0.3% | 25.9 | 97 | 22,209 | 14.3 | 226 | 49,950 | -68% |
| 28 | /content-hub/ai-body-scanners-vs-dexa-scans/ | HEALTH | 58 | 6,958 | 0.8% | 9.4 | 108 | 19,244 | 7.9 | 224 | 16,935 | -64% |
| 29 | /content-hub/fashion-industry-challenges/ | apparel | 44 | 6,788 | 0.6% | 26.5 | 199 | 26,207 | 13.2 | 649 | 83,028 | -74% |
| 30 | /technology/ |  | 19 | 6,671 | 0.3% | 4.3 | 33 | 11,156 | 3.5 | 38 | 60,000 | -40% |
| 31 | /content-hub/how-to-impelement-ar-in-fashion/ | apparel | 2 | 6,380 | 0.0% | 20.1 | 6 | 14,892 | 11.9 | 9 | 26,392 | -57% |
| 32 | /content-hub/ar-clothing-try-on-tools/ | apparel | 14 | 6,308 | 0.2% | 18.4 | 80 | 21,566 | 10.6 | 228 | 46,104 | -71% |
| 33 | /content-hub/size-recommendation-tools/ | apparel | 14 | 6,054 | 0.2% | 13.0 | 31 | 15,455 | 9.0 | 53 | 10,231 | -61% |
| 34 | /mobile-tailor/for-made-to-measure/ | apparel | 112 | 5,942 | 1.9% | 11.6 | 85 | 5,584 | 7.7 | 69 | 13,305 | +6% |
| 35 | /content-hub/how-to-market-a-clothing-brand/ | apparel | 3 | 5,527 | 0.1% | 25.4 | 20 | 18,928 | 12.2 | 39 | 25,435 | -71% |
| 36 | /content-hub/how-to-handle-ecommerce-returns/ | apparel | 5 | 5,521 | 0.1% | 26.4 | 6 | 11,014 | 15.1 | 6 | 13,618 | -50% |
| 37 | /content-hub/body-scanning-technology-comparison/ | HEALTH | 27 | 5,302 | 0.5% | 7.6 | 1 | 1,098 | 8.1 | 0 | 0 | +383% |
| 38 | /content-hub/sustainable-fashion-trends/ | apparel | 20 | 5,278 | 0.4% | 33.3 | 187 | 20,511 | 14.5 | 244 | 53,936 | -74% |
| 39 | /content-hub/body-fat-percentage-men-women-ai-3d-scanning-goals/ | HEALTH | 103 | 5,094 | 2.0% | 10.7 | 719 | 49,916 | 8.4 | 0 | 0 | -90% |
| 40 | /careers/ |  | 45 | 4,569 | 1.0% | 3.3 | 31 | 4,225 | 2.8 | 36 | 4,099 | +8% |
| 41 | /content-hub/virtual-dressing/ | apparel | 72 | 4,563 | 1.6% | 31.3 | 103 | 7,875 | 17.1 | 60 | 10,027 | -42% |
| 42 | /content-hub/top-health-tech-companies/ | HEALTH | 7 | 4,479 | 0.2% | 41.3 | 10 | 7,210 | 16.7 | 25 | 25,987 | -38% |
| 43 | /content-hub/3dlook-turns-two-photos-structured-body-data/ | HEALTH | 16 | 4,410 | 0.4% | 5.5 | 6 | 2,715 | 5.9 | 0 | 0 | +62% |
| 44 | /content-hub/fit3d-vs-3dlook/ |  | 18 | 4,242 | 0.4% | 7.2 | 18 | 8,983 | 6.5 | 8 | 2,018 | -53% |
| 45 | /content-hub/the-potential-of-ai-in-telehealth/ | HEALTH | 5 | 4,174 | 0.1% | 25.3 | 14 | 9,549 | 13.5 | 82 | 35,222 | -56% |
| 46 | /content-hub/nft-in-fashion/ | apparel | 30 | 3,894 | 0.8% | 12.7 | 33 | 7,471 | 8.7 | 75 | 10,338 | -48% |
| 47 | /content-hub/how-to-reduce-returns-in-ecommerce/ | apparel | 1 | 3,871 | 0.0% | 30.2 | 8 | 10,232 | 17.4 | 8 | 16,287 | -62% |
| 48 | /content-hub/7-sustainable-fashion-technologies/ | apparel | 29 | 3,648 | 0.8% | 16.0 | 105 | 11,785 | 12.4 | 113 | 28,179 | -69% |
| 49 | /content-hub/fashion-ecommerce-in-2025/ | apparel | 2 | 3,569 | 0.1% | 29.0 | 26 | 20,147 | 12.5 | 71 | 50,120 | -82% |
| 50 | /content-hub/inbody-vs-3dlook-the-future-of-body-composition-measurement/ | HEALTH | 22 | 3,499 | 0.6% | 7.7 | 17 | 7,172 | 7.6 | 0 | 153 | -51% |
| 51 | /content-hub/skinny-fat-body-type/ | HEALTH | 7 | 3,404 | 0.2% | 7.1 | 12 | 12,248 | 9.1 | 1 | 137 | -72% |
| 52 | /content-hub/3d-body-scanning-apps-market-analysis-and-innovation-benchmarks/ | HEALTH | 9 | 3,185 | 0.3% | 14.6 | 26 | 9,942 | 7.9 | 8 | 5,519 | -68% |
| 53 | /content-hub/body-measurement-software/ | HEALTH | 21 | 3,148 | 0.7% | 21.5 | 62 | 10,406 | 11.3 | 113 | 14,788 | -70% |
| 54 | /content-hub/body-scanner-machines-vs-mobile-3d-body-scan/ | HEALTH | 12 | 3,077 | 0.4% | 11.6 | 18 | 7,525 | 9.3 | 0 | 0 | -59% |
| 55 | /content-hub/bia-scan/ | HEALTH | 7 | 2,804 | 0.2% | 10.0 | 9 | 4,345 | 9.8 | 0 | 180 | -35% |
| 56 | /content-hub/3dlook-announces-6-5-million-series-a-round/ |  | 7 | 2,695 | 0.3% | 5.1 | 7 | 3,173 | 4.2 | 18 | 2,152 | -15% |
| 57 | /structured-body-data-for-telehealth-digital-health-programs/ | HEALTH | 16 | 2,688 | 0.6% | 5.6 | 0 | 0 | 0.0 | 0 | 0 | new |
| 58 | /content-hub/how-to-measure-body-composition/ | HEALTH | 5 | 2,558 | 0.2% | 10.1 | 15 | 6,419 | 9.1 | 5 | 1,993 | -60% |
| 59 | /content-hub/glp-1-market/ | HEALTH | 5 | 2,530 | 0.2% | 43.1 | 8 | 5,139 | 19.0 | 15 | 7,893 | -51% |
| 60 | /sitemap/ |  | 1 | 2,520 | 0.0% | 7.4 | 0 | 566 | 5.5 | 0 | 0 | +345% |

Health-flagged pages L3M: 1966 clicks of 10139 (19.4%), 438,911 of 908,583 impressions (48.3%).

### Top 20 pages by clicks (L3M)

| Page | Flag | Clk | Impr | CTR | Pos | Clk P3M |
|---|---|---|---|---|---|---|
| / |  | 4256 | 63,330 | 6.7% | 17.3 | 7192 |
| /mobile-tailor/ | apparel | 1724 | 44,121 | 3.9% | 9.0 | 2046 |
| /content-hub/body-measurement-app-for-clothing/ | apparel | 783 | 32,440 | 2.4% | 9.1 | 1468 |
| /content-hub/virtual-body-measurements/ | HEALTH | 532 | 13,928 | 3.8% | 12.5 | 1441 |
| /content-hub/virtual-clothing-try-on/ | apparel | 313 | 43,735 | 0.7% | 12.8 | 575 |
| /content-hub/the-enormous-impact-of-daily-physiological-changes-on-the-accuracy-of-our-body-measurements/ | HEALTH | 285 | 58,105 | 0.5% | 5.0 | 313 |
| /content-hub/visible-abs-myths-measurable-outcomes-ai-driven-3d-body-scanning/ | HEALTH | 188 | 80,678 | 0.2% | 7.6 | 337 |
| /content-hub/body-scanning-technology-for-apparel/ | apparel | 159 | 44,508 | 0.4% | 6.0 | 308 |
| /pricing/ |  | 159 | 13,679 | 1.2% | 3.5 | 255 |
| /mobile-tailor/for-made-to-measure/ | apparel | 112 | 5,942 | 1.9% | 11.6 | 85 |
| /content-hub/body-fat-percentage-men-women-ai-3d-scanning-goals/ | HEALTH | 103 | 5,094 | 2.0% | 10.7 | 719 |
| /content-hub/how-to-take-your-body-measurements-at-home/ | HEALTH | 93 | 31,585 | 0.3% | 6.1 | 92 |
| /content-hub/ai-in-fitness-industry/ | HEALTH | 88 | 13,638 | 0.6% | 12.0 | 150 |
| /content-hub/3d-body-scanning/ | HEALTH | 79 | 17,221 | 0.5% | 14.1 | 168 |
| /content-hub/virtual-dressing/ | apparel | 72 | 4,563 | 1.6% | 31.3 | 103 |
| /content-hub/ai-body-scanners-vs-dexa-scans/ | HEALTH | 58 | 6,958 | 0.8% | 9.4 | 108 |
| /content-hub/lean-body-mass-vs-muscle-mass/ | HEALTH | 56 | 79,772 | 0.1% | 6.1 | 118 |
| /about-us/ |  | 53 | 15,454 | 0.3% | 3.8 | 57 |
| /careers/ |  | 45 | 4,569 | 1.0% | 3.3 | 31 |
| /content-hub/fashion-industry-challenges/ | apparel | 44 | 6,788 | 0.6% | 26.5 | 199 |

### 3b. Cannibalisation — non-brand queries where ≥2 URLs each take ≥15% of the query's page-impressions (L3M, ≥100 impr)

Brand queries (3dlook, site:) excluded — multiple URLs there are sitelinks, not cannibalisation.

| Query | Cluster | Query impr | URLs (impr / pos) |
|---|---|---|---|
| weight tracker 3d | Progress tracking / body visualisation | 1232 | / (1023 / 7.1); /content-hub/3d-body-scanning/ (185 / 7.0) |
| virtual fitting room | Apparel sizing / fashion (non-health) | 985 | /content-hub/virtual-fitting-room-for-ecommerce/ (677 / 20.5); /content-hub/virtual-dressing/ (271 / 75.4) |
| 3d body image weight loss | GLP-1 / weight loss / obesity | 934 | /content-hub/body-scanning-technology-for-weight-loss/ (325 / 17.8); / (319 / 54.5); /content-hub/3d-body-scanning/ (244 / 75.9) |
| virtual dressing room market | Apparel sizing / fashion (non-health) | 895 | /content-hub/virtual-fitting-room-for-ecommerce/ (391 / 39.8); /content-hub/virtual-dressing/ (259 / 84.7); /content-hub/virtual-clothing-try-on/ (245 / 70.6) |
| fashion retail technology | Apparel sizing / fashion (non-health) | 802 | /content-hub/top-11-fashion-technologies/ (389 / 44.3); /content-hub/digital-transformation-in-fashion-retail/ (263 / 70.6); /content-hub/the-future-of-fashion-retail/ (150 / 92.3) |
| 3d body analysis | Body scanning (AI / 3D / mobile) | 773 | / (411 / 33.9); /content-hub/3d-body-scanning/ (348 / 70.4) |
| virtual dressing room | Apparel sizing / fashion (non-health) | 703 | /content-hub/virtual-dressing/ (351 / 30.5); /content-hub/virtual-fitting-room-for-ecommerce/ (313 / 31.3) |
| augmented reality fashion | Apparel sizing / fashion (non-health) | 672 | /content-hub/how-to-impelement-ar-in-fashion/ (426 / 21.3); /content-hub/ar-clothing-try-on-tools/ (246 / 31.2) |
| fitxpress | Brand: FitXpress | 538 | /for-bmi-verification/ (252 / 6.3); /structured-body-data-for-telehealth-digital-health-programs/ (138 / 7.4); /fitxpress/for-telehealth-and-weight-loss/ (81 / 6.0) |
| how to measure waist with phone | Waist / circumference / anthropometrics | 469 | /content-hub/how-to-take-your-body-measurements-at-home/ (339 / 6.6); /content-hub/virtual-body-measurements/ (110 / 8.4) |
| technology in fashion retail | Apparel sizing / fashion (non-health) | 461 | /content-hub/top-11-fashion-technologies/ (375 / 18.0); /content-hub/digital-transformation-in-fashion-retail/ (83 / 73.3) |
| ai body measurements | Body measurement (how-to / app / AI) | 437 | /mobile-tailor/ (306 / 3.8); /content-hub/virtual-body-measurements/ (87 / 10.9) |
| augmented reality clothing | Apparel sizing / fashion (non-health) | 384 | /content-hub/ar-clothing-try-on-tools/ (324 / 15.7); /content-hub/how-to-impelement-ar-in-fashion/ (59 / 53.8) |
| us virtual dressing room market | Apparel sizing / fashion (non-health) | 296 | /content-hub/virtual-fitting-room-for-ecommerce/ (205 / 27.7); /content-hub/virtual-dressing/ (74 / 80.7) |
| body measurement software | Body measurement (how-to / app / AI) | 289 | /content-hub/body-measurement-software/ (126 / 3.3); /content-hub/body-measurement-app-for-clothing/ (49 / 44.4); / (45 / 36.3) |
| ai body scanners | Body scanning (AI / 3D / mobile) | 270 | / (68 / 5.8); /content-hub/ai-body-scanners-vs-dexa-scans/ (56 / 10.9); /content-hub/ai-body-scanning-for-fitness/ (46 / 67.8); /mobile-tailor/ (45 / 66.0) |
| 3d body measurements | Body measurement (how-to / app / AI) | 263 | /content-hub/3d-body-scanning/ (135 / 17.0); /content-hub/virtual-body-measurements/ (91 / 18.9) |
| construction software body | Other | 260 | / (99 / 14.6); /mobile-tailor/ (64 / 76.1); /content-hub/3d-body-scanning/ (60 / 60.5) |
| digital body measurements | Body measurement (how-to / app / AI) | 258 | /content-hub/virtual-body-measurements/ (87 / 2.7); /mobile-tailor/ (45 / 33.3); / (41 / 34.7) |
| fashion tech industry | Apparel sizing / fashion (non-health) | 256 | /content-hub/on-demand-fashion-industry-tech-landscape/ (163 / 35.6); /content-hub/top-11-fashion-technologies/ (93 / 28.3) |
| body measurement technology | Body measurement (how-to / app / AI) | 246 | /content-hub/body-measurement-software/ (54 / 21.7); /content-hub/virtual-body-measurements/ (40 / 32.5); /mobile-tailor/ (38 / 57.8) |
| 3d body fat scanner | Body composition / body fat / lean mass | 241 | / (128 / 24.1); /content-hub/3d-body-scanning/ (104 / 68.0) |
| body measurements 3d | Body measurement (how-to / app / AI) | 228 | /content-hub/3d-body-scanning/ (159 / 11.4); /content-hub/virtual-body-measurements/ (41 / 21.7) |
| 3d body measurement | Body measurement (how-to / app / AI) | 228 | /content-hub/virtual-body-measurements/ (76 / 26.0); /content-hub/3d-body-scanning/ (74 / 25.4); /mobile-tailor/ (49 / 24.9) |
| body measurements 3d model | Progress tracking / body visualisation | 227 | /content-hub/3d-body-scanning/ (141 / 13.5); /content-hub/virtual-body-measurements/ (59 / 22.3) |
| online fashion retail market | Apparel sizing / fashion (non-health) | 226 | /content-hub/the-future-of-fashion-retail/ (153 / 85.5); /content-hub/fashion-ecommerce-in-2025/ (73 / 71.1) |
| virtual fitting | Apparel sizing / fashion (non-health) | 218 | /content-hub/virtual-fitting-room-for-ecommerce/ (131 / 26.3); /content-hub/virtual-clothing-try-on/ (58 / 54.1) |
| ecommerce return health | Apparel sizing / fashion (non-health) | 209 | /content-hub/how-to-reduce-returns-in-ecommerce/ (166 / 26.2); /content-hub/how-to-handle-ecommerce-returns/ (43 / 31.5) |
| virtual body measurement | Body measurement (how-to / app / AI) | 205 | /content-hub/virtual-body-measurements/ (136 / 8.4); /content-hub/3d-body-scanning/ (44 / 17.3) |
| 3d fitting room | Apparel sizing / fashion (non-health) | 199 | /content-hub/virtual-fitting-room-for-ecommerce/ (88 / 18.3); /content-hub/virtual-dressing/ (85 / 12.5) |
| 3d body scanner for tailoring | Apparel sizing / fashion (non-health) | 195 | /mobile-tailor/ (87 / 22.4); /content-hub/body-scanning-technology-for-apparel/ (68 / 11.6) |
| 3d body scanning technologies | Body scanning (AI / 3D / mobile) | 187 | /content-hub/body-scanner-machines-vs-mobile-3d-body-scan/ (66 / 20.1); /content-hub/body-scanning-technology-comparison/ (44 / 15.2); / (40 / 28.9) |
| ai tailor | Apparel sizing / fashion (non-health) | 185 | /mobile-tailor/ (144 / 3.1); /mobile-tailor/for-made-to-measure/ (39 / 12.1) |
| 3d virtual fitting room | Apparel sizing / fashion (non-health) | 183 | /content-hub/virtual-fitting-room-for-ecommerce/ (115 / 14.3); /content-hub/virtual-dressing/ (41 / 48.5) |
| ar try on | Apparel sizing / fashion (non-health) | 181 | /content-hub/ar-clothing-try-on-tools/ (109 / 23.0); /content-hub/virtual-clothing-try-on/ (72 / 33.3) |
| replace our aging body scanner | Body scanning (AI / 3D / mobile) | 180 | /content-hub/ai-body-scanners-vs-dexa-scans/ (136 / 19.7); / (34 / 74.5) |
| size related returns | Apparel sizing / fashion (non-health) | 179 | /content-hub/apparel-return-rates-the-stats-retailers-cannot-ignore/ (131 / 45.7); /content-hub/how-to-handle-ecommerce-returns/ (37 / 35.0) |
| body scanner machine | Body scanning (AI / 3D / mobile) | 156 | /content-hub/body-scanner-machines-vs-mobile-3d-body-scan/ (82 / 9.4); / (71 / 31.5) |
| body scanning machine | Body scanning (AI / 3D / mobile) | 147 | /content-hub/body-scanning-technology-comparison/ (68 / 10.6); /content-hub/body-scanner-machines-vs-mobile-3d-body-scan/ (45 / 11.6); / (31 / 29.2) |
| female body scanner online | Body scanning (AI / 3D / mobile) | 142 | / (108 / 8.3); /content-hub/virtual-body-measurements/ (34 / 11.4) |

72 non-brand queries meet the rule; 30 of them are health/fitness.

Most-colliding URL pairs (sum of query impressions):

| URL A | URL B | Impr at stake |
|---|---|---|
| /content-hub/virtual-dressing/ | /content-hub/virtual-fitting-room-for-ecommerce/ | 3749 |
| / | /content-hub/3d-body-scanning/ | 2879 |
| /content-hub/digital-transformation-in-fashion-retail/ | /content-hub/top-11-fashion-technologies/ | 1263 |
| /content-hub/ar-clothing-try-on-tools/ | /content-hub/how-to-impelement-ar-in-fashion/ | 1168 |
| /content-hub/3d-body-scanning/ | /content-hub/virtual-body-measurements/ | 1151 |
| /content-hub/virtual-body-measurements/ | /mobile-tailor/ | 943 |
| / | /content-hub/body-scanning-technology-for-weight-loss/ | 934 |
| /content-hub/virtual-clothing-try-on/ | /content-hub/virtual-fitting-room-for-ecommerce/ | 552 |
| /for-bmi-verification/ | /structured-body-data-for-telehealth-digital-health-programs/ | 538 |
| /content-hub/how-to-take-your-body-measurements-at-home/ | /content-hub/virtual-body-measurements/ | 469 |
| /content-hub/how-to-handle-ecommerce-returns/ | /content-hub/how-to-reduce-returns-in-ecommerce/ | 462 |
| / | /content-hub/ai-body-scanners-vs-dexa-scans/ | 450 |
| / | /content-hub/body-scanner-machines-vs-mobile-3d-body-scan/ | 401 |
| /content-hub/body-measurement-software/ | /content-hub/virtual-body-measurements/ | 349 |
| /content-hub/body-scanner-machines-vs-mobile-3d-body-scan/ | /content-hub/body-scanning-technology-comparison/ | 334 |

## 4. Country and device split — health/fitness queries

Source A (cluster-accurate): query×country and query×device rows for L3M, filtered to the health/fitness clusters of §1 (anonymised queries dropped; query×country pull capped at 25,000 rows, so small-country tail is incomplete).
Source B (context): country/device totals for the broad health regex `body|bmi|fat|glp|weight|telehealth|fitness|health|waist|measure|scan|composition|…` (includes apparel body-scan queries), L3M vs P3M.

### 4a. Countries — health/fitness clusters, L3M (top 20 by impressions)

| Country | Clicks | % clicks | Impr | % impr | CTR | Pos |
|---|---|---|---|---|---|---|
| USA | 129 | 18.5% | 70,816 | 45.7% | 0.2% | 18.8 |
| IND | 246 | 35.3% | 18,570 | 12.0% | 1.3% | 7.4 |
| GBR | 26 | 3.7% | 9,376 | 6.1% | 0.3% | 15.5 |
| PHL | 17 | 2.4% | 5,090 | 3.3% | 0.3% | 7.1 |
| AUS | 11 | 1.6% | 4,350 | 2.8% | 0.3% | 13.9 |
| CAN | 12 | 1.7% | 3,750 | 2.4% | 0.3% | 14.0 |
| DEU | 8 | 1.1% | 2,956 | 1.9% | 0.3% | 22.0 |
| THA | 6 | 0.9% | 2,260 | 1.5% | 0.3% | 8.6 |
| IDN | 10 | 1.4% | 2,129 | 1.4% | 0.5% | 9.6 |
| SGP | 3 | 0.4% | 1,974 | 1.3% | 0.2% | 22.9 |
| MYS | 12 | 1.7% | 1,918 | 1.2% | 0.6% | 7.6 |
| NLD | 6 | 0.9% | 1,760 | 1.1% | 0.3% | 23.2 |
| PAK | 20 | 2.9% | 1,556 | 1.0% | 1.3% | 7.2 |
| ARE | 1 | 0.1% | 1,320 | 0.9% | 0.1% | 12.1 |
| KOR | 2 | 0.3% | 1,081 | 0.7% | 0.2% | 26.2 |
| ZAF | 6 | 0.9% | 1,060 | 0.7% | 0.6% | 5.9 |
| ITA | 6 | 0.9% | 932 | 0.6% | 0.6% | 12.7 |
| SAU | 3 | 0.4% | 857 | 0.6% | 0.4% | 12.0 |
| TUR | 7 | 1.0% | 825 | 0.5% | 0.8% | 18.4 |
| FRA | 4 | 0.6% | 797 | 0.5% | 0.5% | 16.7 |
| **Total** | 696 | | 154,870 | | 0.4% | |

### 4b. Cluster × key markets (L3M impressions / clicks)

| Cluster | USA | GBR | CAN | AUS | IND | DEU | ARE | SAU | PHL | PAK |
|---|---|---|---|---|---|---|---|---|---|---|
| Body composition / body fat / lean mass | 14,165/23 (22%) | 3,876/6 (6%) | 1,840/1 (3%) | 1,852/0 (3%) | 12,533/5 (20%) | 1,229/1 (2%) | 837/0 (1%) | 589/0 (1%) | 3,473/1 (5%) | 1,112/2 (2%) |
| Body scanning (AI / 3D / mobile) | 14,313/17 (63%) | 1,468/8 (6%) | 294/5 (1%) | 617/3 (3%) | 2,233/159 (10%) | 514/2 (2%) | 130/0 (1%) | 49/2 (0%) | 143/5 (1%) | 259/15 (1%) |
| Body measurement (how-to / app / AI) | 8,201/54 (47%) | 1,107/10 (6%) | 352/6 (2%) | 320/4 (2%) | 2,093/62 (12%) | 72/1 (0%) | 109/0 (1%) | 61/0 (0%) | 1,045/7 (6%) | 91/3 (1%) |
| Fitness tech / fitness industry | 10,114/6 (71%) | 1,285/0 (9%) | 475/0 (3%) | 326/1 (2%) | 570/14 (4%) | 133/1 (1%) | 104/0 (1%) | 10/0 (0%) | 50/1 (0%) | 29/0 (0%) |
| Weight-loss clinic marketing | 10,273/2 (86%) | 240/0 (2%) | 184/0 (2%) | 754/0 (6%) | 41/0 (0%) | 60/0 (1%) | 31/1 (0%) | 4/0 (0%) | 10/0 (0%) | 4/0 (0%) |
| Telehealth / digital health / AI in healthcare | 6,061/0 (79%) | 478/0 (6%) | 47/0 (1%) | 50/0 (1%) | 244/0 (3%) | 99/0 (1%) | 53/0 (1%) | 6/0 (0%) | 21/0 (0%) | 8/0 (0%) |
| GLP-1 / weight loss / obesity | 4,057/4 (58%) | 124/0 (2%) | 212/0 (3%) | 161/0 (2%) | 407/4 (6%) | 627/0 (9%) | 2/0 (0%) | 21/0 (0%) | 28/0 (0%) | 3/0 (0%) |
| Progress tracking / body visualisation | 1,630/7 (25%) | 252/0 (4%) | 186/0 (3%) | 134/1 (2%) | 185/2 (3%) | 148/2 (2%) | 31/0 (0%) | 94/1 (1%) | 205/3 (3%) | 20/0 (0%) |
| Waist / circumference / anthropometrics | 1,508/15 (51%) | 416/1 (14%) | 130/0 (4%) | 105/2 (4%) | 220/0 (7%) | 31/0 (1%) | 15/0 (1%) | 10/0 (0%) | 102/0 (3%) | 23/0 (1%) |
| BMI | 494/1 (37%) | 130/1 (10%) | 30/0 (2%) | 31/0 (2%) | 44/0 (3%) | 43/1 (3%) | 8/0 (1%) | 13/0 (1%) | 13/0 (1%) | 7/0 (1%) |

### 4c. Broad health regex by country — L3M vs P3M (top 15)

| Country | Clk L3M | Impr L3M | % impr | Pos | Clk P3M | Impr P3M | Impr Δ |
|---|---|---|---|---|---|---|---|
| USA | 147 | 104,774 | 50.4% | 15.7 | 343 | 210,785 | -50% |
| IND | 272 | 22,309 | 10.7% | 8.1 | 521 | 41,581 | -46% |
| GBR | 29 | 13,388 | 6.4% | 15.2 | 84 | 22,209 | -40% |
| PHL | 20 | 5,761 | 2.8% | 7.7 | 61 | 9,903 | -42% |
| AUS | 13 | 5,292 | 2.5% | 13.6 | 29 | 8,605 | -39% |
| CAN | 16 | 4,700 | 2.3% | 13.7 | 54 | 12,345 | -62% |
| DEU | 11 | 3,733 | 1.8% | 20.1 | 45 | 6,876 | -46% |
| NLD | 9 | 2,809 | 1.4% | 18.4 | 26 | 4,610 | -39% |
| IDN | 12 | 2,477 | 1.2% | 10.7 | 86 | 4,943 | -50% |
| THA | 6 | 2,392 | 1.2% | 9.2 | 41 | 3,106 | -23% |
| MYS | 12 | 2,181 | 1.0% | 8.1 | 29 | 3,614 | -40% |
| SGP | 3 | 2,174 | 1.0% | 21.4 | 18 | 3,665 | -41% |
| PAK | 21 | 1,782 | 0.9% | 7.8 | 35 | 3,290 | -46% |
| ARE | 1 | 1,554 | 0.7% | 12.5 | 11 | 3,105 | -50% |
| ITA | 7 | 1,381 | 0.7% | 12.3 | 15 | 2,232 | -38% |
| Total | 786 | 207,838 | | | 2050 | 423,523 | |

Whole-site L3M clicks by country (context): IND 2180 (21.9%), USA 1987 (20.0%), GBR 603 (6.1%), IDN 280 (2.8%), CAN 266 (2.7%), AUS 264 (2.7%), DEU 186 (1.9%), BRA 185 (1.9%), PAK 181 (1.8%), VNM 165 (1.7%).

### 4d. Device — health/fitness clusters, L3M

| Device | Clicks | % | Impr | % | CTR | Pos |
|---|---|---|---|---|---|---|
| MOBILE | 562 | 80.7% | 84,226 | 50.1% | 0.7% | 8.5 |
| DESKTOP | 116 | 16.7% | 82,244 | 48.9% | 0.1% | 20.5 |
| TABLET | 18 | 2.6% | 1,595 | 0.9% | 1.1% | 11.1 |

Broad health regex by device, L3M vs P3M; whole site L3M for context:

| Device | Clk L3M | Impr L3M | CTR | Pos | Clk P3M | Impr P3M | Pos P3M | Site clk L3M | Site impr L3M |
|---|---|---|---|---|---|---|---|---|---|
| MOBILE | 625 | 90,081 | 0.7% | 8.8 | 1635 | 164,325 | 7.9 | 5529 | 314,818 |
| DESKTOP | 138 | 116,069 | 0.1% | 17.8 | 369 | 256,360 | 11.7 | 4267 | 450,816 |
| TABLET | 23 | 1,688 | 1.4% | 11.3 | 46 | 2,838 | 9.2 | 137 | 5,741 |

Note: /content-hub/lean-body-mass-vs-muscle-mass/ alone had 58,160 impressions and 21 clicks in L3M (0.0% CTR; mobile 45,901 impr / 16 clk). Top countries: IND 12,953 impr, USA 10,980, GBR 3,789, THA 2,058. A position-2–7 page with ~0.04% CTR is not a normal blue-link pattern: most impressions are almost certainly AI-Overview / 'things to know' / image-thumbnail citations — visibility without traffic.

## 5. Branded vs non-branded — monthly, 16 months

Brand regex: `3d ?look|3dlook|fit ?xpress|yourfit|your fit|mobile tailor|mtm app|savvy|3d-look`. 'Anon' = site total − branded − non-branded (queries Google withholds; mostly long-tail non-brand). Health regex column = broad health regex (§4 source B). FitXpress column = queries matching `fit ?xpress|fitexpress|fit express`.

| Month | Site clk | Site impr | Brand clk | Brand impr | Brand CTR | Non-brand clk | Non-brand impr | Anon clk | Anon impr | Brand % of clicks | Health-regex clk | Health-regex impr | Health pos | FitXpress-query clk / impr |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2025-05 | 8,645 | 507,317 | 1,236 | 3,458 | 35.7% | 2,441 | 241,359 | 4,968 | 262,500 | 14.3% | 806 | 80,714 | 21.8 | 21 / 299 |
| 2025-06 | 13,603 | 709,384 | 1,823 | 4,676 | 39.0% | 4,336 | 331,201 | 7,444 | 373,507 | 13.4% | 1,293 | 113,683 | 23.0 | 60 / 362 |
| 2025-07 | 13,832 | 699,018 | 1,979 | 4,930 | 40.1% | 4,623 | 330,956 | 7,230 | 363,132 | 14.3% | 1,072 | 118,953 | 28.5 | 77 / 437 |
| 2025-08 | 11,742 | 649,375 | 1,805 | 4,623 | 39.0% | 3,533 | 293,428 | 6,404 | 351,324 | 15.4% | 992 | 99,647 | 26.0 | 81 / 415 |
| 2025-09 | 12,717 | 550,514 | 2,060 | 4,900 | 42.0% | 4,018 | 201,005 | 6,639 | 344,609 | 16.2% | 1,092 | 79,462 | 22.4 | 36 / 332 |
| 2025-10 | 12,851 | 464,562 | 1,842 | 4,518 | 40.8% | 4,355 | 155,761 | 6,654 | 304,283 | 14.3% | 1,185 | 68,317 | 14.2 | 37 / 300 |
| 2025-11 | 11,893 | 490,843 | 1,801 | 4,386 | 41.1% | 3,580 | 164,711 | 6,512 | 321,746 | 15.1% | 1,231 | 72,993 | 11.6 | 28 / 344 |
| 2025-12 | 11,906 | 561,562 | 1,419 | 4,177 | 34.0% | 4,136 | 226,972 | 6,351 | 330,413 | 11.9% | 1,420 | 105,521 | 14.6 | 14 / 275 |
| 2026-01 | 11,506 | 789,971 | 1,515 | 4,298 | 35.2% | 4,058 | 280,415 | 5,933 | 505,258 | 13.2% | 1,244 | 136,614 | 13.2 | 15 / 319 |
| 2026-02 | 7,716 | 835,752 | 1,538 | 4,033 | 38.1% | 1,408 | 248,455 | 4,770 | 583,264 | 19.9% | 997 | 142,378 | 10.4 | 24 / 339 |
| 2026-03 | 7,922 | 1,042,627 | 1,534 | 3,386 | 45.3% | 1,387 | 336,550 | 5,001 | 702,691 | 19.4% | 1,131 | 234,078 | 8.7 | 18 / 193 |
| 2026-04 | 6,377 | 666,694 | 1,384 | 3,150 | 43.9% | 992 | 225,795 | 4,001 | 437,749 | 21.7% | 777 | 155,540 | 9.5 | 18 / 189 |
| 2026-05 | 5,970 | 610,295 | 1,210 | 2,978 | 40.6% | 826 | 209,272 | 3,934 | 398,045 | 20.3% | 671 | 143,336 | 10.6 | 9 / 247 |
| 2026-06 | 4,238 | 401,253 | 1,022 | 2,864 | 35.7% | 557 | 137,624 | 2,659 | 260,765 | 24.1% | 428 | 95,355 | 12.1 | 9 / 193 |
| 2026-07 | 3,518 | 262,970 | 1,012 | 2,727 | 37.1% | 396 | 102,314 | 2,110 | 157,929 | 28.8% | 318 | 66,393 | 15.4 | 6 / 124 |
| 2026-08 | 3,240 | 259,227 | 827 | 2,243 | 36.9% | 339 | 101,923 | 2,074 | 155,061 | 25.5% | 233 | 65,879 | 14.9 | 9 / 143 |
| 2026-09 (22d) | 2,324 | 181,084 | 623 | 1,873 | 33.3% | 199 | 85,798 | 1,502 | 93,413 | 26.8% | 138 | 59,134 | 10.9 | 3 / 86 |

## 6. Where FitXpress intent lives now (post-redirect)

Live check (curl, 2026-09-25): `/fitxpress/` → 301 → `/`; `/yourfit/` → 301 → `/`; `/fitxpress/for-telehealth-and-weight-loss/` → 301 → `/structured-body-data-for-telehealth-digital-health-programs/` (200); `/fitxpress/for-connected-and-digital-fitness/` → **200 (still live, legacy URL)**; `/for-bmi-verification/` → 200. There is no dedicated FitXpress product page; the brand name is carried by `/for-bmi-verification/`, the homepage and the new telehealth page.

### 6a. Monthly clicks / impressions of the FitXpress & YourFit URLs (16 months)

| Month | /fitxpress/ | /yourfit/ | /fitxpress/for-telehealth-and-weight-loss/ | /fitxpress/for-connected-and-digital-fitness/ | /content-hub/fitxpress-admin-panel-launch/ |
|---|---|---|---|---|---|
| 2025-05 | 97 / 6,984 | 272 / 23,976 | 2 / 270 | 0 / 306 | 0 / 0 |
| 2025-06 | 218 / 12,306 | 478 / 41,896 | 1 / 406 | 7 / 635 | 0 / 0 |
| 2025-07 | 170 / 11,702 | 467 / 41,875 | 1 / 446 | 3 / 822 | 0 / 0 |
| 2025-08 | 176 / 7,219 | 342 / 43,823 | 3 / 1,180 | 10 / 795 | 0 / 0 |
| 2025-09 | 105 / 7,262 | 297 / 40,138 | 4 / 3,081 | 3 / 824 | 0 / 0 |
| 2025-10 | 77 / 4,873 | 301 / 33,010 | 4 / 3,882 | 1 / 542 | 0 / 0 |
| 2025-11 | 63 / 4,464 | 247 / 13,263 | 7 / 4,688 | 1 / 265 | 0 / 0 |
| 2025-12 | 69 / 3,258 | 239 / 16,579 | 3 / 6,220 | 2 / 530 | 0 / 0 |
| 2026-01 | 64 / 3,275 | 199 / 19,708 | 6 / 4,041 | 5 / 397 | 0 / 0 |
| 2026-02 | 111 / 5,085 | 251 / 21,886 | 1 / 2,171 | 3 / 434 | 0 / 0 |
| 2026-03 | 14 / 956 | 0 / 52 | 19 / 2,490 | 1 / 523 | 0 / 0 |
| 2026-04 | 1 / 5 | 1 / 23 | 11 / 2,193 | 0 / 506 | 0 / 0 |
| 2026-05 | 0 / 4 | 1 / 10 | 9 / 1,618 | 1 / 145 | 0 / 0 |
| 2026-06 | 0 / 3 | 0 / 7 | 10 / 1,601 | 1 / 221 | 1 / 90 |
| 2026-07 | 0 / 18 | 2 / 11 | 13 / 1,131 | 3 / 170 | 1 / 102 |
| 2026-08 | 0 / 9 | 2 / 4 | 0 / 0 | 4 / 271 | 1 / 90 |
| 2026-09 | 0 / 4 | 0 / 3 | 0 / 0 | 1 / 191 | 1 / 46 |

Reading: `/fitxpress/` peaked at 218 clicks / 12.3K impr (Jun 2025) and ran ~65–110 clicks/mo through Feb 2026, then dropped to 14/956 in Mar 2026 and ~0 from Apr (redirect). `/yourfit/` (consumer virtual-fitting-room, apparel) lost ~250–470 clicks/mo at the same time. `/fitxpress/for-telehealth-and-weight-loss/` kept 10–19 clicks/mo until its redirect in Aug 2026.

### 6b. What /fitxpress/ ranked for before the redirect (2025-06-01 → 2026-02-28)

745 queries, 465 clicks, 26,936 impressions.

| Query | Clk | Impr | Pos |
|---|---|---|---|
| ai body scanner app | 11 | 3,526 | 5.6 |
| ai body scanner | 16 | 3,060 | 3.1 |
| fitxpress | 291 | 2,156 | 4.4 |
| ai body scan | 13 | 1,882 | 4.8 |
| ai body scanner free | 0 | 768 | 7.5 |
| body scan ai | 1 | 697 | 4.1 |
| body scanner ai | 4 | 392 | 2.1 |
| best ai body scanner app | 3 | 379 | 7.6 |
| fit xpress | 7 | 369 | 6.7 |
| ai body scan fitness free | 6 | 357 | 8.6 |
| ai body fat scanner | 0 | 355 | 6.3 |
| mobile body scan | 0 | 342 | 48.3 |
| ai body scanner for weight loss | 9 | 321 | 4.9 |
| ai body scan workout | 3 | 311 | 6.3 |
| ai body scan fitness app | 4 | 303 | 5.9 |
| free ai body scan | 1 | 288 | 9.6 |
| site:3dlook.ai | 0 | 274 | 4.0 |
| ai body scan fitness | 3 | 257 | 4.6 |
| body scan fitness | 0 | 253 | 42.1 |
| body rate ai | 5 | 252 | 7.9 |

`/fitxpress/for-telehealth-and-weight-loss/` same period: 433 queries, 12 clicks, 9,418 impr. Top by impressions: 3d body image weight loss (638, pos 21.1); fitxpress (632, pos 8.6); موقع يطلع شكل الجسم 3d (560, pos 9.7); height weight app 3d (520, pos 8.6); ai body scanner (401, pos 5.3); physique check ai (326, pos 5.6); bmi visualizer 3d (276, pos 9.5); weight guesser ai (266, pos 9.2); weight tracker 3d (244, pos 2.9); height and weight app 3d (205, pos 8.8).

### 6c. Same intent now (L3M) — which URL ranks

| Query | L3M clk | L3M impr | L3M pos | URLs now (impr / pos) |
|---|---|---|---|---|
| fitxpress | 21 | 373 | 6.0 | /for-bmi-verification/ (252 / 6.3); /structured-body-data-for-telehealth-digital-health-programs/ (138 / 7.4); /fitxpress/for-telehealth-and-weight-loss/ (81 / 6.0); /fitxpress/for-connected-and-digital-fitness/ (41 / 5.5) |
| fit xpress | 0 | 27 | 14.6 | /for-bmi-verification/ (23 / 13.0); /fitxpress/for-connected-and-digital-fitness/ (9 / 17.4); /fitxpress/ (3 / 2.0) |
| fitxpress app | 0 | 0 | - | - |
| 3dlook fitxpress | 0 | 0 | - | - |
| ai body scanner | 43 | 881 | 5.6 | / (791 / 5.7); /case-studies/ (196 / 8.2); /pricing/ (196 / 8.2); /technology/ (196 / 8.2) |
| ai body scanner app | 22 | 537 | 8.4 | / (518 / 8.6); /content-hub/ai-body-scanners-vs-dexa-scans/ (31 / 5.3); /content-hub/3d-body-scanning/ (1 / 2.0); /content-hub/ai-body-scanning-for-fitness/ (1 / 42.0) |
| ai body scan | 19 | 458 | 5.8 | / (413 / 5.4); /content-hub/ai-body-scanners-vs-dexa-scans/ (84 / 8.6); /case-studies/ (50 / 7.7); /pricing/ (50 / 7.7) |
| body scanner ai | 32 | 269 | 2.8 | / (265 / 2.8); /mobile-tailor/ (22 / 3.0); /content-hub/ai-body-scanners-vs-dexa-scans/ (19 / 10.2); /pricing/ (15 / 2.5) |
| ai body scanner for weight loss | 2 | 56 | 4.0 | / (43 / 3.7); /content-hub/body-scanning-technology-for-weight-loss/ (31 / 6.2); /case-studies/ (2 / 8.0); /pricing/ (2 / 8.0) |
| best ai body scanner app | 0 | 4 | 8.8 | / (3 / 11.3); /content-hub/body-scanning-technology-for-weight-loss/ (1 / 1.0) |
| ai body scan fitness app | 0 | 0 | - | - |
| 3d body composition scanner | 0 | 354 | 33.3 | / (354 / 33.3) |
| 3d body fat scanner | 1 | 156 | 31.0 | / (128 / 24.1); /content-hub/3d-body-scanning/ (104 / 68.0); /content-hub/body-fat-percentage-men-women-ai-3d-scanning-goals/ (2 / 65.0); /about-us/ (1 / 12.0) |
| 3d body image weight loss | 0 | 413 | 21.1 | /content-hub/body-scanning-technology-for-weight-loss/ (325 / 17.8); / (319 / 54.5); /content-hub/3d-body-scanning/ (244 / 75.9); /content-hub/body-fat-percentage-men-women-ai-3d-scanning-goals/ (46 / 42.0) |
| 3d bmi visualizer | 0 | 7 | 25.3 | / (6 / 29.8); /content-hub/3d-body-scanning/ (3 / 32.0) |
| bmi verification | 0 | 81 | 5.2 | /for-bmi-verification/ (80 / 5.3); /content-hub/beyond-bmi-business/ (1 / 2.0) |
| 3dlook api | 18 | 58 | 4.4 | / (55 / 2.5); /pricing/ (52 / 2.7); /about-us/ (46 / 3.1); /mobile-tailor/ (23 / 2.8) |
| body scanning technology | 0 | 9188 | 10.1 | /content-hub/body-scanning-technology-for-apparel/ (8161 / 9.9); /content-hub/body-scanning-technology-comparison/ (1041 / 10.1); /content-hub/body-scanner-machines-vs-mobile-3d-body-scan/ (26 / 47.4); / (25 / 60.8) |
| mobile body scanning software remote bmi verification | 0 | 69 | 1.0 | /content-hub/bariatric-pre-qualification-mobile-3d-body-scanning/ (69 / 1.2); /content-hub/body-scanner-machines-vs-mobile-3d-body-scan/ (30 / 10.3); /content-hub/ (13 / 8.5); / (2 / 1.0) |
| best mobile body scanning solution for telehealth | 0 | 46 | 2.9 | /content-hub/body-scanner-machines-vs-mobile-3d-body-scan/ (45 / 2.9); /structured-body-data-for-telehealth-digital-health-programs/ (1 / 3.0) |

### 6d. Queries landing on the current FitXpress-intent URLs (L3M)

- **/structured-body-data-for-telehealth-digital-health-programs/** — page total L3M 16 clk / 2,688 impr / pos 5.6; 52 visible queries. Top: fitxpress (3/138, 7.4); 3d look (0/115, 1.0); ai body scanner (0/85, 8.7); 3d look ai (0/42, 1.0); 3dlook ai (0/29, 1.0); 3dlook company (0/22, 3.4); ai body scan (0/22, 8.4); 3dlook api (0/15, 2.2); 3dlook (0/13, 2.9); 3dlook official website (0/13, 1.1).
- **/for-bmi-verification/** — page total L3M 35 clk / 1,068 impr / pos 6.2; 14 visible queries. Top: fitxpress (13/252, 6.3); bmi verification (0/80, 5.3); site:3dlook.ai (0/29, 8.4); fit xpress (0/23, 13.0); fitspressonovuglyca (0/6, 14.0); fiexpress (0/2, 99.5); site:https://3dlook.ai (0/2, 8.5); what is bmi verification (0/2, 1.0); express fit (0/1, 27.0); fitpress (0/1, 19.0).
- **/fitxpress/for-connected-and-digital-fitness/** — page total L3M 9 clk / 676 impr / pos 15.0; 14 visible queries. Top: site:3dlook.ai (0/59, 65.9); fitxpress (2/41, 5.5); fitspressonovuglyca (0/23, 8.9); fit xpress (0/9, 17.4); site:https://3dlook.ai * * * (0/5, 75.8); fitpress (0/3, 43.0); fitask (0/2, 70.0); fitexpres (0/2, 9.0); fitexpress colle (0/2, 38.0); fitviz (0/2, 35.5).

- **Homepage `/`** (L3M 4,256 clk / 63,330 impr) now absorbs the consumer/app FitXpress intent: ai body scanner 41/791 pos 5.7, weight tracker 3d 92/1,023 pos 7.1, ai body scanner app 22/518 pos 8.6, ai body scan 18/413 pos 5.4, body scanner ai 31/265 pos 2.8, 3d body scanner 1/1,077 pos 26.5, body scanner 0/961 pos 28.3, 3d body composition scanner 0/354 pos 33.3, 3d body image weight loss 0/319 pos 54.5.

## Appendix — cluster rules (case-insensitive regex, first match wins)

1. Brand: FitXpress — `fit ?xpress|fitexpress|fit[- ]express|fitxp`
2. Brand: 3DLOOK / other brand — `3d ?look|3dlook|3d-look|yourfit|your fit app|mobile tailor|savvy|3dl\b`
3. Apparel sizing / fashion (non-health) — `cloth|apparel|sportswear|fashion|tailor|garment|size recommend|made to measure|try-on|fitting|dressing|retail|ecommerce|manufactur|uniform|workwear|nft|swim|armor|xpertfit|fit3d|true fit|mirrar` (+ second fashion rule)
4. Weight-loss clinic marketing — weight/glp/obesity/bariatric × marketing/advertising/social media/campaign/seo/leads
5. GLP-1 / weight loss / obesity — `glp|ozempic|wegovy|semaglutide|tirzepatide|mounjaro|zepbound|weight loss|lose weight|obes|bariatric|weight management|weight control|slimming|weight gain|diet`
6. Telehealth / digital health — `telehealth|telemedicine|virtual care|remote patient|digital health|healthcare|health tech|medical|clinical|patient|pharmac|insur|underwrit|occupational|wellness`
7. BMI — `\bbmi\b|body mass index`
8. Body composition / body fat / lean mass — `lean|body fat|fat percent|composition|skeletal muscle|muscle mass|\bbia\b|dexa|visceral|abs|six pack|body type|fat mass|inbody`
9. Waist / circumference — `waist|hip ratio|circumference|anthropometr`
10. Progress tracking / visualisation — `weight track|progress|visuali[sz]|before and after|transformation|body image|3d model|avatar|body calculator|height weight`
11. Body scanning — `body ?scan|scanner|scanning|body analy[sz]`
12. Body measurement — `measur|tape|sizing`
13. Fitness tech — `fitness|gym|workout|exercise|sport|athlet|personal train|movement intelligence|wearable`

Raw pulls (JSON) are in `scratchpad/gsc/` (q_L, q_P, q_Y, qp_L, qp_P, p_L, p_P, p_Y, d_*, c_*, dev_*, qc_hf_L, qd_hf_L, dp_fx, qp_fx16, qp_fxpre, qp_b2b_L).
