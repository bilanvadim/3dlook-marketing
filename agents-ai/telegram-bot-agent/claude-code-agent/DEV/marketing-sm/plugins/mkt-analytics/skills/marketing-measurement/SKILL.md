---
name: marketing-measurement
description: How to measure marketing honestly and report it — metric definitions and sources (GA4/ad accounts/CRM/ESP), unit economics (CAC/LTV/ROAS/payback), attribution models and their limits, incrementality testing, the baseline→change→effect method with confounders, forecasting with assumptions, and a clean report format. Use when baselining, measuring campaign impact, modeling economics, or building a marketing report/dashboard.
---

# Marketing measurement & reporting

The job is credible ROI and cause→effect, not a wall of vanity metrics.

## Metrics & sources
| Metric | Source | Meaning |
|---|---|---|
| Impressions, CTR, CPC, CPM | Ad platforms | reach & cost of attention |
| Conversion rate by funnel stage | GA4 / backend | where it leaks |
| CPA / CAC | ad spend + conversions/CRM | cost to acquire |
| LTV | CRM/backend | value of a customer |
| ROAS, payback period | revenue ÷ spend | does it pay, how fast |
| Retention / churn (cohorts) | CRM/product | leaky-bucket health |
| Email open/click/conv | ESP | lifecycle performance |
| Pipeline / revenue | CRM/backend | the outcome that matters |

Lead reports with **CAC/LTV/ROAS + pipeline/revenue**; CTR/CPC are diagnostics.

## Unit economics (the gate)
- **CAC** = spend ÷ new customers (by channel). **LTV** = margin × lifespan.
- Healthy when **LTV : CAC** is comfortably > 1 (often ≥3 as a rule of thumb) and
  **payback** period fits cashflow. This gate governs scaling decisions.

## Attribution (and its limits)
State the model: last-click (simple, biased to bottom funnel), position-based,
data-driven, or MMM for the top. Every model is a lens, not truth. For big spend
decisions prefer **incrementality**: holdout/geo/PSA tests that measure lift vs a
control — the honest answer to "did the ads cause this?".

## Baseline → change → effect
1. **Baseline** targeted metrics before launch; record date/window/source.
2. **Mark the change** (what shipped, which channels/segments, budget).
3. **Measure** over a comparable window; segment to the affected channel/cohort.
4. **Attribute honestly** with the stated model; note tracking gaps (iOS/privacy,
   cookie loss) that under-report.

## Confounders to always name
Seasonality · other campaigns/launches in-window · price/promo changes · privacy/
tracking loss · PR/organic spikes · market shifts. If you can't rule them out, say so.

## Forecasting
Conservative, scenario-based (low/expected/high) with explicit assumptions (CVR,
CAC by channel, budget, seasonality). Ranges with caveats, never false precision.

## Report format
- **Executive summary** — what paid off, what didn't, next (3–5 lines).
- **Economics** — CAC | LTV | ROAS | payback, by channel.
- **Results table** — metric | baseline | current | Δ | window | source.
- **Funnel & cohorts** — conversion by stage; retention curves.
- **Caveats** — attribution model, confounders, tracking gaps.
- **Next** — next ICE-prioritized plays (hand back to marketing-strategist).

Reproducibility: document each pull (query/date-range/segment/UTM+attribution
rules) so the report re-runs next period.
