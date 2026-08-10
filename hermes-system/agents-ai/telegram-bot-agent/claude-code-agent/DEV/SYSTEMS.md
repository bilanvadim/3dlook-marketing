# Systems (profiles) — dev-sm · seo-sm · marketing-sm · security-sm (+ test-sm · sandbox-sm)

Claude Code here runs as **exactly one mutually-exclusive system at a time**, on
purpose: too many agents/skills at once dilute the model's selection and burn
context. You pick a system (a "profile"), and Claude Code loads only that
system's agents, skills and commands. Four are working systems; `test-sm` is an
experimental mix and `sandbox-sm` is the trial bench — neither is routable.

| Profile | For | Marketplace(s) | Entry command | Agents |
|---|---|---|---|---|
| **dev-sm** (default) | full-stack development | `dev-sm` | `/sm-feature`, `/sm-verify`, `/sm-docs`, `/sm-evaluate` | 13 + 7 advisory (ECC) |
| **seo-sm** | search optimization | `dev-sm`(base) + `seo-sm` | `/seo-audit` | 5 |
| **marketing-sm** | digital marketing | `dev-sm`(base) + `marketing-sm` | `/mkt-campaign` | 5 |
| **security-sm** | security audit/hardening | `dev-sm`(subset) + `security-sm` | agents / `/sm-verify` | auditor + hunter |
| **test-sm** | experimental marketing MIX (mvb) | `dev-sm`(base) + `marketing-sm` + `ai-agents-mvb*` | `/vbsm-campaign` | mvb + mkt teams |
| **sandbox-sm** | trialling ONE candidate before adoption | `dev-sm`(core only) + `sandbox-sm` | `/sbx-check` | none (base + probe) |

Every non-dev profile also loads the shared base `hermes-core` (orchestration,
scratchpad handoff, session-handoff) + `hermes-verify` (quality gates), so
planning and "done = verified" work the same everywhere.

---

## Switching

The switcher rewrites `~/.claude/settings.json` to enable **exactly** the target
profile's plugins (mutual exclusion) and records the active one in
`~/.claude/.active-profile`.

```bash
cd /srv/sergiy_prod/ai-agents-config/agents-ai/telegram-bot-agent/claude-code-agent/DEV

./switch-profile.sh --list        # profiles + which is active
./switch-profile.sh --current     # active profile
./switch-profile.sh marketing-sm     # switch (dev-sm | seo-sm | marketing-sm | security-sm | test-sm | sandbox-sm)
```

**Three ways it takes effect — know which you're in:**

- **Interactive TUI (you, in the app):** switch, then **restart Claude Code**.
  Plugins load only at session start. Verify with `/` (the new commands appear)
  or `switch-profile.sh --current`.
- **Headless (`claude -p …`):** no restart concept — each `claude -p` is a fresh
  process that reads settings at start. Just `switch-profile.sh <p>` **before**
  the call. `settings.json` is global, so don't run two different-profile
  headless calls at once — serialize, or use the conductor.
- **Conductor (autonomous A→Z jobs):** don't switch globally. Put the profile on
  the job; the worker loads that profile's plugins per-job (concurrency-safe):
  ```sql
  insert into ho_jobs(kind,title,prompt,profile,work_dir)
  values('feature','…','…','seo-sm','/path/to/project');   -- dev-sm|seo-sm|marketing-sm|security-sm
  ```

---

## How each system works (same pattern)

1. Run the entry command (`/sm-feature`, `/seo-audit`, `/mkt-campaign`) → the
   lead agent interviews you and writes a plan into `.claude/scratchpad/<slug>/`.
2. **Hard approval gate** — it stops and waits for your `go` before any change,
   deploy, or spend.
3. After `go` → it delegates steps to specialists; **every step is verified with
   evidence** (not "done" on the agent's word).
4. Production actions (deploy, live SQL, paid campaigns, mailouts) are gated for
   human confirmation — enforced by `.claude/hooks/guard.py` + agent rules.

### dev-sm
`/sm-feature "<what to build>"` → architect → plan → frontend/backend/database/
platform engineers → qa + security-auditor → code-reviewer + runtime-verifier.
Advisory ECC reviewers available: react/typescript/database-reviewer,
performance-optimizer, silent-failure-hunter, refactor-cleaner,
type-design-analyzer (all read-only — they propose, you apply).

### seo-sm
`/seo-audit "<domain / task>"` → `seo-strategist` diagnoses (crawl→index→
content→authority→analytics), prioritizes by ICE, delegates to
`technical-seo-engineer`, `content-strategist`, `link-authority-strategist`,
`seo-analyst`. White-hat only; data-grounded (GSC/GA4, no invented metrics).

### marketing-sm
`/mkt-campaign "<goal / campaign>"` → `marketing-strategist` sets strategy
(ICP→positioning→funnel→channels→budget), delegates to `content-marketer`,
`paid-media-buyer`, `lifecycle-marketer`, `marketing-analyst`. Content skills
include ECC's `content-engine`, `brand-voice`, `crosspost`, `article-writing`,
`market-research`. Unit-economics before scaling; spend/publish gated.

### security-sm
`security-auditor` (Trail-of-Bits) + `security-bounty-hunter` (exploitability
triage) + `silent-failure-hunter` (fail-open hunting) + verification. Use for
audits, RLS/auth/secrets review, OWASP passes.

---

## Hermes orchestration

Hermes routes by intent and switches for you — see the `vps-orchestration` skill
→ "Profile routing". Say *"переключись на marketing и сделай X"* (explicit) or
just describe a marketing/SEO/security/dev task and Hermes picks the profile,
switches, runs it, and reports which system it used.

**Ask-by-default (Sergiy's rule): if <100% sure, ASK — don't guess.**
Unless Sergiy explicitly names the system, Hermes posts a menu and waits:
```
Какую систему запустить внутри Claude?
1. Dev
2. Marketing
3. SEO
4. Security
```
Sergiy replies with a number (e.g. `2`). Helpers make this deterministic:
- `route-profile.sh --menu` → the exact question above.
- `route-profile.sh --num <n>` → `1=dev-sm 2=marketing-sm 3=seo-sm 4=security-sm`.
- `route-profile.sh "<task>"` → an optional suggested default to show in the ask.
- `dispatch-in-profile.sh <profile> -- <cmd>` → switch + **verify** + run under a
  lock (switch can't be skipped or raced). Headless `claude -p` needs no restart;
  interactive TUI does. Concurrent multi-profile → conductor `ho_jobs.profile`.

```bash
# Hermes: ask → parse reply → dispatch
p=$(agents-ai/telegram-bot-agent/claude-code-agent/DEV/route-profile.sh --num 2)                 # user answered "2" -> marketing-sm
agents-ai/telegram-bot-agent/claude-code-agent/DEV/dispatch-in-profile.sh "$p" -- claude -p '<task>' --workdir <proj>
```

Intent → profile: SEO/ranking/SERP/crawl/keywords/backlinks → **seo-sm**;
campaign/ads/funnel/email/social/content/positioning → **marketing-sm**;
audit/vulnerability/OWASP/RLS/secrets → **security-sm**; anything code → **dev-sm**.

## Codebase Memory (MCP) — общий для всех профилей

`hermes-core` (база во всех профилях) бандлит MCP-сервер **`codebase-memory`**
(`plugins/hermes-core/.mcp.json`): tree-sitter knowledge-graph проекта, грузится
автоматически при включении плагина — в интерактиве И в headless-сессиях дирижёра
(через `options.plugins`). Правило использования для агентов — в `dev-sm/CLAUDE.md`
(«граф перед grep»).

**Redeploy (бинарь и конфиг живут ВНЕ репо, ставятся раз на машину):**
```bash
# 1) бинарь без авто-конфига (НЕ трогает наши хуки/настройки)
curl -fsSL https://raw.githubusercontent.com/DeusData/codebase-memory-mcp/main/install.sh \
  | bash -s -- --skip-config          # ставит в ~/.local/bin (уже в PATH)
# 2) каждый проект индексируется сразу; watcher выкл (авто-очистка ~/workspaces)
codebase-memory-mcp config set auto_index true
codebase-memory-mcp config set auto_watch false
```
Локально (egress = 0), MIT, single static binary. Обновление — `codebase-memory-mcp update`.
⚠️ Никогда не запускать голый `install` без `--skip-config` — он перезаписывает
pre-tool хуки/instruction-файлы агентов.
