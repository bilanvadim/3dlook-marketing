---
name: marketing-vb-sm
description: The blended marketing workflow for the marketing_vb_sm system — how Vadim's brand-driven 3DLOOK teams (mvb-*) and Sergiy's marketing specialists (mkt-*) work as ONE team. Use whenever running the marketing_vb_sm profile, the /vbsm-campaign command, or coordinating a campaign that needs both strategy/measurement (Sergiy) and brand-grounded execution (Vadim). Defines phases, which agent owns each step, and the precedence rules when the two systems overlap.
---

# marketing-vb-sm — Vadim × Sergiy blended marketing

This system merges two teams into one pipeline:

- **Vadim's world (`mvb-*`)** — brand truth and execution. Owns brand voice,
  audience truth, factual claims, and the social / SEO / outbound production
  lines. Authoritative on *what is true and on-brand for 3DLOOK*.
- **Sergiy's world (`mkt-*` + Hermes base)** — strategy, prioritization,
  cross-channel breadth, and measurement. Owns the strategic frame, ICE
  prioritization, paid media, lifecycle/CRM, analytics, and evidence-based
  "done" (`hermes-verify`).

The mix exists because each side is strong where the other is thin: Vadim's
system is deep on brand-safe production but has no strategy/paid/lifecycle/
attribution layer; Sergiy's system has that layer but no 3DLOOK brand memory.

## Precedence (resolve overlaps deterministically)

| Concern | Owner (wins) |
|---|---|
| Brand voice, tone, visual identity | **Vadim** (`brand-checker`) |
| Factual claims / accuracy about 3DLOOK & the product | **Vadim** (`context-pack-builder` approved claims, `quality-controller`) |
| Audience / ICP truth | **Vadim** (`about-me.md`, `audience.md`, `brand-assets/`) — Sergiy's `marketing-strategist` *reads* these, does not overwrite |
| Strategy frame, ICE prioritization, budget, unit economics | **Sergiy** (`marketing-strategist`) |
| Organic social & SEO article production | **Vadim** (`mvb-social`, `mvb-seo`) |
| Editorial calendar & distribution strategy | **Sergiy** (`content-marketer`) feeds Vadim's producers |
| Outbound (ICP → hypothesis → shortlist → sequencing) | **Vadim** (`mvb-outbound`) |
| Paid media (search/social/display, bidding, ROAS) | **Sergiy** (`paid-media-buyer`) |
| Email / CRM / lifecycle / retention | **Sergiy** (`lifecycle-marketer`) |
| Attribution, funnel/cohort, CAC/LTV/ROAS, dashboards | **Sergiy** (`marketing-analyst`) |
| Definition of done / evidence gate | **Sergiy** (`hermes-verify`) + Vadim QC |

Rule of thumb: **Sergiy decides *what to do and why*; Vadim decides *whether
it is on-brand and true*; production is owned by whichever team runs that
channel.** When in doubt about brand or fact → Vadim wins. When in doubt about
priority or spend → Sergiy wins.

## Phases

Write everything into `.claude/scratchpad/<slug>/vbsm/`.

1. **Strategy (Sergiy).** Run `marketing-strategist` following the
   `marketing-strategy` skill (layers L0–L8, ICE). It MUST first read Vadim's
   brand context (`about-me.md`, `audience.md`, `brand-assets/`, past posts &
   articles, competitors). Output: `strategy.md`, `plan.md` (ICE-scored,
   delegatable steps with agent/tags/acceptance/metric/budget), `risks.md`.
2. **Approval gate.** Stop. Present the plan + assumptions. Wait for explicit
   `go` before any production, spend, or outbound.
3. **Brand context pack (Vadim).** Run `context-pack-builder` to assemble the
   approved brand facts/claims each producer must ground in.
4. **Execution (route each play to its owner):**
   - organic social → `mvb-social` (+ `content-marketer` for calendar/angle)
   - SEO articles → `mvb-seo` (planner → writer → editor → publisher)
   - outbound → `mvb-outbound` flow
   - paid → `paid-media-buyer`
   - email/lifecycle → `lifecycle-marketer`
5. **QC gate (both).** Every asset passes Vadim's `brand-checker` +
   `quality-controller` (brand/fact) AND Sergiy's `hermes-verify` (evidence
   that acceptance criteria are met). No asset ships until both pass.
6. **Measurement (Sergiy).** `marketing-analyst` sets up attribution, defines
   the metrics from `plan.md`, and reports funnel / CAC / LTV / ROAS.

## Anti-patterns

- Letting `marketing-strategist` invent product claims — it proposes, Vadim's
  `context-pack-builder` / `brand-checker` ratify.
- Shipping a paid or lifecycle asset without Vadim's brand QC.
- Running production before the approval gate.
- Duplicated SEO: use Vadim's `mvb-seo` line, not an ad-hoc writer.
