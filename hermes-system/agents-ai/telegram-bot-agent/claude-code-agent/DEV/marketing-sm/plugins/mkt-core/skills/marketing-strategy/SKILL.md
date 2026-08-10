---
name: marketing-strategy
description: How to turn a marketing goal into a data-grounded strategy and a prioritized, executable plan — an adaptive diagnostic across business, ICP/personas, positioning/offer, funnel/lifecycle, channel mix, budget/unit-economics, message, and measurement, plus anti-pattern prediction, ICE prioritization, and a richly structured step list (each step with acceptance, metric, budget, dependencies). Use at the start of any non-trivial marketing initiative, in /mkt-campaign, or whenever someone says "grow leads/revenue / launch this / plan a campaign".
---

# Marketing strategy — diagnose → prioritize → plan

Turns "grow our marketing" into a defensible plan. Mirrors the dev
`project-planning` and the SEO `seo-methodology`, adapted to demand generation and
lifecycle. Diagnose with data, predict anti-patterns, prioritize by ICE, emit a
delegatable step list tied to metrics and budget.

## Principles
- **Unit economics first.** CAC < LTV, proven small before scaled. A channel that
  doesn't pay back doesn't get more budget.
- **Positioning before tactics.** Right ICP + offer + message beats channel tricks.
- **Data or it didn't happen.** Cite analytics/ad-account/CRM/benchmarks; label
  guesses ESTIMATE.
- **Honest & compliant.** No misleading claims, fake proof, dark patterns, spam;
  respect platform policy + law (ads, privacy/GDPR, email opt-in).

## Strategy layers (L0–L8) — adapt depth to scope
- **L0 Business & goals** — what's sold, price/margin, revenue/lead target,
  timeline, constraints, current baseline & CAC/LTV if known.
- **L1 Audience (ICP & personas)** — who buys, jobs-to-be-done, pains, objections,
  where they pay attention, buying triggers.
- **L2 Positioning & offer** — category, differentiation, value prop, the offer
  (pricing/packaging/incentive), proof.
- **L3 Funnel & lifecycle** — awareness → consideration → conversion → retention →
  referral; where the leaks are; the one bottleneck to fix first.
- **L4 Channel mix** — paid (search/social/display), owned (content/email/site),
  earned (PR/social/word-of-mouth); match channel to audience + funnel stage.
- **L5 Budget & unit economics** — allocation, target CPA/CAC by channel, expected
  ROAS, payback period; what "working" means numerically.
- **L6 Message & creative** — core narrative, hooks, angles per persona/stage,
  creative formats per channel.
- **L7 Measurement & tracking** — GA4, ad pixels/conversions API, UTM taxonomy,
  attribution model, KPI tree, reporting cadence.
- **L8 Competitive & market** — competitor positioning/offers/channels, whitespace,
  realistic opportunity.

## Anti-patterns to predict and pre-empt
Scaling spend before unit economics work · tactics before positioning · one channel
dependence (platform risk) · vanity metrics over pipeline/revenue · broad
"everyone" targeting · no tracking / broken attribution → flying blind · discount
addiction eroding margin · ignoring retention (leaky bucket) · misleading claims or
dark patterns (brand + legal risk) · creative fatigue with no refresh · email to a
non-opted-in list · launching without a measurement baseline.

## ICE prioritization
Score each play: **Impact** (1–5, revenue/pipeline potential) × **Confidence**
(0–1, evidence it works) ÷ **Effort** (1–5, cost incl. budget). Order desc.
Surface **quick wins** (high impact, low effort/spend, high confidence) first to
fund trust for bigger bets.

## Plan schema (what marketing-strategist emits to plan.md)
Each step is a delegatable unit:
- `step_no` · `phase` (Content | Paid | Lifecycle | Analytics) · `agent` · `title`
- `description` — what to do, concretely
- `tags` — e.g. `[paid, search]`, `[email, nurture]`, `[content, social]`
- `acceptance` — verifiable done-conditions (tracking fires, UTMs set, landing 200,
  creative matches brief + platform specs, segment defined, budget capped…)
- `quality_bar` — the standard (honest, compliant, on-brand, on-economics)
- `depends_on` — step numbers that must finish first
- `metric` — the KPI this moves (CTR, CPC, CPA/CAC, ROAS, conversion rate,
  open/click, LTV, pipeline) + how it's measured
- `budget?` — spend cap where the step involves paid media
- `ice` — {impact, confidence, effort, score}

## Verification (per step — never trust "done")
Prove it before launch: tracking/conversions fire, UTMs present, landing pages live
(200) and on-message, creative matches brief + platform specs, targeting/budget set
and capped, compliance checked (ads policy, privacy, opt-in). For on-site code
(landing pages, pixels) run `verification-protocol`. Baseline BEFORE and measure
AFTER via `marketing-analyst`, honest about attribution and the measurement window.
