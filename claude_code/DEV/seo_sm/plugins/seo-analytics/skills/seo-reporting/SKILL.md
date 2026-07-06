---
name: seo-reporting
description: How to measure SEO impact honestly and report it — metric definitions and sources (GSC/GA4), the baseline→change→effect method with indexation lag and confounders, forecasting with stated assumptions, and a clean report format. Use when baselining, measuring the effect of a change, forecasting, or building an SEO report/dashboard.
---

# SEO reporting & impact measurement

The job is credible cause→effect, not a dashboard of vanity numbers.

## Metrics & sources
| Metric | Source | Meaning |
|---|---|---|
| Impressions, avg position, CTR, queries | Google Search Console | demand & visibility |
| Indexed pages, coverage, crawl stats | GSC (Pages/Coverage) | indexation health |
| Core Web Vitals (LCP/INP/CLS) | GSC / CrUX / PSI | UX signal |
| Organic sessions, engagement | GA4 | traffic that arrived |
| Organic conversions / revenue | GA4 (+ backend) | the outcome that matters |
| Referring domains, authority | link tool exports | off-page trend |
| Rank positions (tracked set) | rank tracker | movement on target queries |

Lead reports with **organic conversions/revenue**; rankings and traffic are the
ladder to it.

## Baseline → change → effect
1. **Baseline** the targeted metrics before the change ships; record the exact
   date/window and source.
2. **Mark the change** (date, what shipped, which URLs/queries).
3. **Wait for the lag.** Indexation + ranking response is typically **weeks**.
   Don't declare success or failure inside the noise window.
4. **Measure** the same metrics over a comparable window; compare like-for-like
   (same weekdays/season where possible).
5. **Attribute honestly.** Segment to the affected pages/queries (cohort) rather
   than sitewide, so unrelated movement doesn't contaminate the read.

## Confounders to always name
Seasonality · Google algorithm/core updates · other changes shipped in the window
· tracking changes · SERP-feature shifts · market/PPC changes. If you can't rule
them out, say so.

## Forecasting
Conservative, scenario-based (low/expected/high), with explicit assumptions
(CTR-by-position curve, achievable positions from difficulty, demand/volume
source). Forecasts are ranges with caveats, never single false-precision numbers.

## Report format
- **Executive summary** — what moved, what didn't, what's next (3–5 lines).
- **Results table** — metric | baseline | current | Δ | window | source.
- **Per-initiative effect** — tie movement to the shipped steps (cohort view).
- **Caveats** — lag, confounders, data gaps.
- **Next** — the next ICE-prioritized actions (hand back to seo-strategist).

Reproducibility: document the query/date-range/segment for each pull so the
report can be re-run next period.
