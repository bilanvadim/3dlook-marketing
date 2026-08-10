---
name: marketing-vb-sm
description: The blended marketing workflow for the marketing_vb_sm system — how Vadim's brand-driven 3DLOOK teams (mvb-*) and Sergiy's marketing specialists (mkt-*) work as ONE team. Use whenever running the marketing_vb_sm profile, the /vbsm-campaign command, or coordinating a campaign that needs both strategy/measurement (Sergiy) and brand-grounded execution (Vadim). Defines the phases, who owns each step, and the precedence rules when the two systems overlap.
---

# marketing-vb-sm — Vadim × Sergiy blended marketing

This system merges two teams into one pipeline:

- **Vadim's world (`mvb-*`)** — brand truth and execution. Owns brand voice,
  audience truth, factual claims, and the social / long-form / outbound
  production lines. Authoritative on *what is true and on-brand for 3DLOOK*.
- **Sergiy's world (`mkt-*` + Hermes base)** — strategy, prioritization,
  cross-channel breadth, and measurement. Owns the strategic frame, ICE
  prioritization, paid media, lifecycle/CRM, analytics, and evidence-based
  "done" (`hermes-verify`).

The mix exists because each side is strong where the other is thin: Vadim's
system is deep on brand-safe production but has no strategy/paid/lifecycle/
attribution layer; Sergiy's system has that layer but no 3DLOOK brand memory.

## The rule that keeps this from rotting

**Execution is delegated to Vadim's own entry points, never re-implemented here.**

The first version of this skill hardcoded his agent chain — "social → post-drafter
+ visual-brief", "SEO → planner → writer → editor → publisher". His system then
moved on: `/weekly-posts` was deprecated in favour of `/post-from-article` (posts
are now derived from an approved article, not from a quarterly plan), and four
social agents plus three long-form writers appeared. The hardcoded chain silently
kept running an older, smaller version of his system — skipping his editor and
publisher entirely.

So: **the mix calls his commands and his `orchestrator`**, which are the live
definition of his pipelines, and wraps them with Sergiy's layer before and after.
When Vadim changes a workflow, the mix follows automatically.

| Track | Call THIS (Vadim's live entry point) | Never do this instead |
|---|---|---|
| long-form / SEO article | `/new-article <topic|slug> [stage]` | drive seo-planner → writer → editor → publisher by hand |
| social posts from an article | `/post-from-article <article-slug>` | call post-drafter per profile yourself |
| outbound campaign | `/outbound [stage] [campaign-slug]` | drive the 8 outbound agents by hand |
| quarterly content plan | `/quarterly-review` | ask quarterly-strategist directly |
| QC of one artifact | `/qc <artifact-path>` | eyeball it |
| agent prompt improvements | `/improve-agents [days] [agent]` | edit his agents yourself |

If a track has no command, ask his `orchestrator` — it is his single entry point
and knows which workflow and which agents a request maps to.

## What Vadim's side actually contains (28 agents, 7 commands)

Inventory only — so the mix knows what exists. Order and gating live in his
`orchestrator` and commands, not here.

| Plugin | Agents |
|---|---|
| `mvb-core` (5) | `orchestrator` (his entry point, opus) · `context-pack-builder` (assembles the approved-facts pack every producer grounds in) · `brand-checker` (brand voice / no-go phrases / AI signatures) · `quality-controller` (20-point rubric, independent QC) · `agent-improver` |
| `mvb-social` (8) | `social-planner` · `post-drafter` · `brand-checker` (social variant) · `social-editor` (cross-profile dedup + voice audit) · `social-publisher` (manifest, ready_for_review) · `visual-brief` · `quarterly-strategist` · `social-analytics` |
| `mvb-seo` (7) | `seo-planner` (Phase 0 = content-strategy gate) · `seo-writer` · `seo-editor` · `seo-publisher` + the FitXpress FAQ section writers: `data-lifecycle-writer` · `enterprise-faq-writer` · `rights-compliance-writer` |
| `mvb-outbound` (8) | `hypothesis-generator` · `company-researcher` · `people-extractor` · `icp-validator` · `message-sequencer` · `closelyhq-importer` · `response-classifier` · `campaign-analyzer` |

**`brand-checker` exists twice, with different content and different jobs** —
`mvb-core:brand-checker` audits brand voice on any text or brief (RU), while
`mvb-social:brand-checker` returns PASS/FAIL on a single post and is invoked by
`post-drafter` (UA). In a plain `.claude/agents/` directory they collide on the
name; as plugins they separate. **Always namespace it in the mix:** say
`mvb-core:brand-checker` or `mvb-social:brand-checker`, never bare.

Two drifts inside his own system, stated as facts — do not "fix" them here, and
do not route around them:

- `/weekly-posts` is **deprecated**; `/post-from-article` replaced it. His
  `orchestrator` table still lists the old one.
- `social-planner` / `social-editor` / `social-publisher` describe the 9-profile
  chain, but `/post-from-article` currently runs `post-drafter` +
  `quality-controller` and assembles the digest itself. The command is the
  authority on what runs today.

## Precedence (resolve overlaps deterministically)

| Concern | Owner (wins) |
|---|---|
| Brand voice, tone, visual identity | **Vadim** (`mvb-core:brand-checker`, `mvb-social:brand-checker` per post) |
| Factual claims / accuracy about 3DLOOK & the product | **Vadim** (`context-pack-builder` approved claims, `quality-controller`) |
| Audience / ICP truth | **Vadim** (`about-me.md`, `audience.md`, `brand-assets/`) — Sergiy's `marketing-strategist` *reads* these, never overwrites |
| Per-profile posting rules (cadence, tone, length, product bias) | **Vadim** — `brand-assets/linkedin-post-prompts.md` beats `social-profiles-config.md`, and two house rules beat both: **no hashtags anywhere, max 1-2 emoji** |
| Which article may be written at all | **Vadim** — `seo-planner` Phase 0 against `brand-assets/content-strategy/content-plan.md`. No row → it stops. Sergiy's strategy does **not** override that gate; it feeds candidates into the plan |
| Strategy frame, ICE prioritization, budget, unit economics | **Sergiy** (`marketing-strategist`) |
| Quarterly content themes | **Vadim** (`quarterly-strategist`) owns themes; Sergiy's strategy sets the business objective they serve |
| Organic social & long-form production | **Vadim** (`/post-from-article`, `/new-article`) |
| Editorial calendar & distribution strategy | **Sergiy** (`content-marketer`) feeds Vadim's producers — it does not write |
| Outbound (ICP → hypothesis → shortlist → sequencing) | **Vadim** (`/outbound`) |
| Paid media (search/social/display, bidding, ROAS) | **Sergiy** (`paid-media-buyer`) |
| Email / CRM / lifecycle / retention | **Sergiy** (`lifecycle-marketer`) |
| Organic social post performance | **Vadim** (`social-analytics`, per-profile patterns) |
| Attribution, funnel/cohort, CAC/LTV/ROAS, dashboards | **Sergiy** (`marketing-analyst`) |
| Artifact quality score | **Vadim** (`quality-controller`, 20-point rubric — below 12 means stop) |
| Definition of done / evidence gate | **Sergiy** (`hermes-verify`) on top of Vadim's QC |

Rule of thumb: **Sergiy decides *what to do and why*; Vadim decides *whether it
is on-brand and true*; production is owned by whichever team runs that channel.**
In doubt about brand or fact → Vadim. In doubt about priority or spend → Sergiy.

## Phases

Write Sergiy-side artifacts into `.claude/scratchpad/<slug>/vbsm/`. Vadim's
artifacts stay where HIS pipelines put them (`workspace/seo/articles/<slug>/`,
`workspace/social/articles/<slug>/<profile>/`) — never relocate his outputs, his
agents and his Telegram bot read those paths.

1. **Strategy (Sergiy).** `marketing-strategist` following the
   `marketing-strategy` skill (layers L0–L8, ICE). It MUST first read Vadim's
   brand context — `CLAUDE.md`, `about-me.md`, `audience.md`, `brand-assets/`
   (incl. `content-strategy/content-plan.md`, `social-profiles-config.md`,
   `linkedin-post-prompts.md`), past posts and articles, competitors. Output:
   `strategy.md`, `plan.md` (ICE-scored, delegatable steps with
   agent/tags/acceptance/metric/budget), `risks.md`.
2. **Approval gate.** Stop. Present the plan, the assumptions, and the predicted
   anti-patterns. Wait for an explicit `go` before any production, spend, or
   outbound. Vadim's own pipelines have their own checkpoints on top of this —
   they are not redundant, do not skip either.
3. **Route each play to its owner (phase 4 below), and for anything on Vadim's
   side, hand it to his entry point** — his `context-pack-builder` runs inside
   his workflows; do not pre-run it yourself.
4. **Execution.**
   - long-form article → `/new-article`. If `seo-planner` Phase 0 returns
     `refresh` / `section-first` / `review-decide` / `lead-magnet`, that is a
     legitimate answer: report it and update `plan.md`. Do **not** force a new
     article.
   - social posts → `/post-from-article <slug>` **after** the article's
     `publish-package.md` is `approved_for_publish`. `visual-brief` only after
     Vadim approves the text.
   - outbound → `/outbound`. Human steps are real steps (Sales Navigator export,
     launch in closely.io); stop and say so rather than simulating them.
   - paid → `paid-media-buyer` · email/lifecycle → `lifecycle-marketer`
     (Sergiy's, no Vadim entry point exists) — both still pass phase 5.
5. **QC gate (both worlds).** Every asset passes Vadim's brand + fact check
   (`mvb-social:brand-checker` per post, `quality-controller` ≥ 12/20) **and**
   Sergiy's `hermes-verify` (evidence that the acceptance criteria in `plan.md`
   are met). Nothing ships until both pass.
6. **Measurement (Sergiy + Vadim).** `marketing-analyst` sets up attribution and
   reports funnel / CAC / LTV / ROAS against `plan.md`; `social-analytics` owns
   per-profile organic patterns. `campaign-analyzer` owns outbound learnings.

## Anti-patterns

- **Re-implementing Vadim's chain** instead of calling `/new-article`,
  `/post-from-article`, `/outbound`. This is how the mix went stale the first
  time; it is the single most important rule here.
- Letting `marketing-strategist` invent product claims — it proposes, Vadim's
  `context-pack-builder` / `brand-checker` ratify.
- Writing a post from a strategy brief instead of from an approved article — the
  social line starts at `publish-package.md`, not at an idea.
- Overriding `seo-planner` Phase 0 because the strategy wants that article now.
  Add the row to `content-plan.md` first, with Vadim.
- Calling `brand-checker` without a namespace — two different agents answer.
- Shipping a paid or lifecycle asset without Vadim's brand QC.
- Running production before the approval gate, or treating a QC score < 12 as
  advisory.
- Relocating Vadim's artifacts into the scratchpad — his agents and bot read
  `workspace/…` by path.
