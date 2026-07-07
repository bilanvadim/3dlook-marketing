# Systems (profiles) — 6 mutually-exclusive Claude Code systems

Claude Code here runs as **one of six mutually-exclusive systems**. Only ONE is
active at a time, on purpose: too many agents/skills at once dilute the model's
selection and burn context. You pick a system (a "profile"), and Claude Code
loads only that system's agents, skills and commands.

| Profile | For | Marketplace(s) | Entry command | Notes |
|---|---|---|---|---|
| **marketing_vb_sm** | 3DLOOK marketing, blended | base + `marketing_vb` + `marketing_sm` + `marketing_vb_sm` | `/vbsm-campaign` | **Vadim's default** — brand-grounded execution + strategy/measurement |
| **marketing_vb** | Vadim's original system | `marketing_vb` | `/new-article`, `/weekly-posts`, `/outbound`, `/qc`, … | Pure, no Hermes base — faithful to `/marketing_vb` |
| **marketing** | generic digital marketing | base + `marketing_sm` | `/mkt-campaign` | Sergiy's marketing specialists |
| **dev** | full-stack development | `full_stack_sm` | `/sm-feature`, `/sm-verify`, `/sm-docs` | 11 plugins + advisory ECC |
| **seo** | search optimization | base + `seo_sm` | `/seo-audit` | white-hat, data-grounded |
| **security** | security audit/hardening | base(subset) + `security_sm` | agents / `/sm-verify` | auditor + hunter |

"base" = `hermes-core` (orchestration, scratchpad handoff, session-handoff) +
`hermes-verify` (quality gates), so planning and "done = verified" work the same
everywhere. The pure `marketing_vb` profile deliberately omits the base to stay
identical to Vadim's original project.

---

## The two marketing worlds and their mix

- **`marketing_vb`** — Vadim's 3DLOOK system packaged as plugins (marketplace
  `ai-agents-mvb`): orchestrator + brand-checker + quality-controller +
  context-pack-builder + social/SEO/outbound teams. Source of truth is the
  **pristine, untouched** project at repo root `/marketing_vb`.
- **`marketing`** — Sergiy's generic marketing system (marketplace
  `ai-agents-mkt`): marketing-strategist + content/paid/lifecycle/analytics.
- **`marketing_vb_sm`** — the **mix** (marketplace `ai-agents-mvb-sm` + both of
  the above + base). Sergiy sets strategy & measurement; Vadim's team executes
  on-brand and owns brand/fact QC. Entry: `/vbsm-campaign`. See the
  `marketing-vb-sm` skill for phases and precedence rules.

---

## Switching

The switcher rewrites `~/.claude/settings.json` to enable **exactly** the target
profile's plugins (mutual exclusion) and records the active one in
`~/.claude/.active-profile`. Marketplace paths in `profiles/*.json` are
**relative** to this directory, so the config is portable — it works wherever
the repo is checked out, no absolute paths.

```bash
cd claude_code/DEV      # (inside your checkout of this repo)

./switch-profile.sh --list             # profiles + which is active
./switch-profile.sh --current          # active profile
./switch-profile.sh marketing_vb_sm    # switch to any of the 6
```

**Three ways it takes effect — know which you're in:**

- **Interactive TUI (you, in the app):** switch, then **restart Claude Code**.
  Plugins load only at session start. Verify with `/` (new commands appear) or
  `switch-profile.sh --current`.
- **Headless (`claude -p …`):** each `claude -p` is a fresh process that reads
  settings at start. Run `switch-profile.sh <p>` **before** the call.
  `settings.json` is global, so don't run two different-profile headless calls
  at once — serialize, or use the orchestrator.
- **Orchestrator (autonomous A→Z jobs):** don't switch globally. Put the profile on
  the job; the worker loads that profile's plugins per-job (concurrency-safe):
  ```sql
  insert into ho_jobs(kind,title,prompt,profile,work_dir)
  values('feature','…','…','marketing_vb_sm','/path/to/project');
  -- profile ∈ dev|seo|marketing|security|marketing_vb|marketing_vb_sm
  ```

---

## How each system works (same pattern)

1. Run the entry command → the lead agent interviews you and writes a plan into
   `.claude/scratchpad/<slug>/`.
2. **Hard approval gate** — it stops and waits for your `go` before any change,
   deploy, spend, or mailout.
3. After `go` → it delegates steps to specialists; **every step is verified with
   evidence** (not "done" on the agent's word).

### marketing_vb_sm  (Vadim's default)
`/vbsm-campaign "<goal>"` → `marketing-strategist` reads Vadim's brand context
(`about-me.md`, `audience.md`, `brand-assets/`) and sets strategy → approval
gate → `context-pack-builder` grounds facts → execution routed per channel
(social/SEO/outbound to Vadim's teams; paid/lifecycle to Sergiy's) → QC by
`brand-checker` + `quality-controller` + `hermes-verify` → measurement by
`marketing-analyst`. Precedence: strategy/spend = Sergiy, brand/fact = Vadim.

### marketing_vb  (Vadim's original)
`orchestrator` is the single entry point; commands `/new-article`,
`/weekly-posts`, `/outbound`, `/post-from-article`, `/qc`, `/quarterly-review`,
`/improve-agents`. Run from a working dir that has `brand-assets/` + `workspace/`
(e.g. inside `/marketing_vb`).

### marketing  (Sergiy generic)
`/mkt-campaign "<goal>"` → `marketing-strategist` → `content-marketer`,
`paid-media-buyer`, `lifecycle-marketer`, `marketing-analyst`.

### dev
`/sm-feature "<what to build>"` → architect → plan → frontend/backend/database/
platform → qa + security-auditor → code-reviewer + runtime-verifier. Advisory
ECC reviewers (read-only): react/typescript/database-reviewer,
performance-optimizer, silent-failure-hunter, refactor-cleaner,
type-design-analyzer.

### seo
`/seo-audit "<domain / task>"` → `seo-strategist` (crawl→index→content→
authority→analytics), ICE-prioritized, delegates to technical/content/authority/
analyst specialists. White-hat, data-grounded.

### security
`security-auditor` (Trail-of-Bits) + `silent-failure-hunter` + verification.
Audits, RLS/auth/secrets review, OWASP passes.

---

## Hermes orchestration

Hermes routes by intent and switches for you — see the `vps-orchestration`
skill. Say *"переключись на marketing_vb_sm и сделай X"* (explicit) or describe a
task and Hermes picks the profile, switches, runs it, and reports which system
it used.

**Ask-by-default: if <100% sure, ASK — don't guess.** Unless the system is named
explicitly, Hermes posts a menu and waits:
```
Какую систему запустить внутри Claude?
1. Dev
2. Marketing (микс VB×SM)
3. Marketing VB (только система Вадима)
4. Marketing SM (общая система Сергея)
5. SEO
6. Security
```
Reply with a number. Helpers make this deterministic:
- `route-profile.sh --menu` → the exact question above.
- `route-profile.sh --num <n>` → `1=dev 2=marketing_vb_sm 3=marketing_vb 4=marketing 5=seo 6=security`.
- `route-profile.sh "<task>"` → coarse suggested default (dev|seo|marketing|
  security). On this marketing-first repo the `marketing` token maps by
  convention to the `marketing_vb_sm` mix.
- `dispatch-in-profile.sh <profile> -- <cmd>` → switch + **verify** + run under a
  lock (switch can't be skipped or raced).

```bash
# Hermes: ask → parse reply → dispatch
p=$(claude_code/DEV/route-profile.sh --num 2)                 # user answered "2" -> marketing_vb_sm
claude_code/DEV/dispatch-in-profile.sh "$p" -- claude -p '<task>' --workdir <proj>
```
