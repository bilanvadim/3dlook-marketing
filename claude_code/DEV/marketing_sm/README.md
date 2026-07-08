# Digital marketing system (`ai-agents-mkt`)

Claude Code marketplace for the **marketing** profile. Sibling of `full_stack_sm`
(dev) and `seo_sm` (SEO). Only one profile is active at a time — switch with
`../switch-profile.sh marketing` (see `../profiles/`).

The `marketing` profile also loads the shared base (`hermes-core`,
`hermes-verify` from `ai-agents-config`), so orchestration, scratchpad handoff,
session-handoff and quality gates work exactly like the dev system.

## The team (5 plugins)

| Plugin | Agent | Owns |
|---|---|---|
| `mkt-core` | **marketing-strategist** | strategy, positioning, GTM, ICE prioritization, the plan (+ `/mkt-campaign`, `marketing-strategy` skill) |
| `mkt-content` | **content-marketer** | content strategy, copywriting, editorial calendar, organic social & distribution (+ `content-calendar` skill) |
| `mkt-paid` | **paid-media-buyer** | paid acquisition (search/social/display), budgets, bidding, ROAS, creative A/B (+ `paid-media` skill) |
| `mkt-lifecycle` | **lifecycle-marketer** | email/CRM, nurture, automation, segmentation, retention (opt-in, deliverability) |
| `mkt-analytics` | **marketing-analyst** | attribution, funnel & cohort, GA4, CAC/LTV/ROAS, forecasting, reporting (+ `marketing-measurement` skill) |

## Orchestration

`marketing_sm/CLAUDE.md` is the marketing orchestrator doc (analogous to
`full_stack_sm/CLAUDE.md`): work cycle, who-to-call table, hard rules
(honest & compliant, data-grounded, spend/publish gated, unit-economics before
scaling), model tiering. Start with **`/mkt-campaign "<goal / campaign>"`**.

## Method (skills)

- `marketing-strategy` — strategy layers L0–L8 → anti-patterns → ICE → plan schema
  (each step: agent/tags/acceptance/metric/budget/deps).
- `content-calendar` — pillars→personas→stages, editorial calendar, copy structure,
  atomize/repurpose, distribution.
- `paid-media` — media plan, campaign structure, honest A/B testing, scale-what-pays
  economics with budget caps + approval gates.
- `marketing-measurement` — metrics/sources, unit economics, attribution &
  incrementality, baseline→change→effect, forecasting, report format.

## Extending

Add domain plugins the same way (e.g. `mkt-social` for a dedicated community/social
role, `mkt-brand`, `mkt-partnerships`/affiliate), or adopt vetted external skills
via `/sm-evaluate` + `skill-guard`, then add the plugin name to
`../profiles/marketing.json` `enabledPlugins`.
