# 3dlook-marketing · `sergiy_config`

This branch ports **Sergiy's two-layer agent architecture** onto Vadim's
3DLOOK marketing repo, **without touching Vadim's original system**. Same shape
as Sergiy's setup: **Hermes as the orchestrator + Claude Code as the hands.**

```
3dlook-marketing/  (branch sergiy_config)
├── marketing_vb/            ← Vadim's ORIGINAL system, moved here untouched
│                              (.claude agents/commands, telegram-bot, runners,
│                               brand-assets, workspace, docs) — source of truth
├── claude_code/DEV/         ← Claude Code layer: 6 switchable systems
│   ├── full_stack_sm/       ·  dev base (11 hermes-* plugins) + conductor
│   ├── seo_sm/              ·  seo system
│   ├── marketing_sm/        ·  Sergiy's marketing system (mkt-*)
│   ├── security_sm/         ·  security system
│   ├── marketing_vb/        ·  Vadim's system, packaged as plugins (mvb-*)
│   ├── marketing_vb_sm/     ·  MIX: Vadim × Sergiy marketing (bridge plugin)
│   ├── profiles/*.json      ·  the 6 systems (relative, portable paths)
│   ├── switch-profile.sh    ·  activate exactly one system
│   ├── route-profile.sh     ·  intent → system classifier + 6-way menu
│   └── SYSTEMS.md           ·  full guide to the 6 systems
├── hermes_agent/            ← Hermes orchestrator ops (conductor runner,
│                              model-router, skill-guard, systemd templates)
├── install.sh               ← one-shot installer (checks, conductor, systemd)
└── INSTALL.md               ← step-by-step setup on your machine
```

## The 6 Claude Code systems

| System | What | Entry |
|---|---|---|
| `marketing_vb_sm` | **Vadim's default** — brand-grounded execution + Sergiy strategy/measurement | `/vbsm-campaign` |
| `marketing_vb` | Vadim's original, pure (no Hermes base) | `/new-article`, `/weekly-posts`, `/outbound`, … |
| `marketing` | Sergiy's generic marketing | `/mkt-campaign` |
| `dev` | full-stack development | `/sm-feature` |
| `seo` | search optimization | `/seo-audit` |
| `security` | security audit / hardening | agents / `/sm-verify` |

Only ONE is active at a time (mutual exclusion) — switch with
`claude_code/DEV/switch-profile.sh <system>` then restart Claude Code.

## The mix (`marketing_vb_sm`)

Sergiy decides **what to do and why** (strategy, ICE prioritization, paid,
lifecycle, attribution); Vadim decides **whether it's on-brand and true**
(brand voice, product claims, QC); each team owns its production channels. See
the `marketing-vb-sm` skill and `claude_code/DEV/SYSTEMS.md` for the full
workflow and precedence rules.

## Hermes orchestrator

`hermes_agent/` + the conductor in `full_stack_sm/conductor/` let jobs run
autonomously: a Telegram/queue request becomes an `ho_jobs` row (SQLite/libSQL) with a `profile`,
and the conductor runs Claude Code in that system, verifies with evidence, and
escalates to a human only when needed.

## Get started

```bash
./install.sh                # or ./install.sh --no-conductor
```

Full instructions: [INSTALL.md](INSTALL.md) · systems guide:
[claude_code/DEV/SYSTEMS.md](claude_code/DEV/SYSTEMS.md).
