# Systems (profiles) — dev · seo · marketing · security

Claude Code here runs as **one of four mutually-exclusive systems**. Only ONE is
active at a time, on purpose: too many agents/skills at once dilute the model's
selection and burn context. You pick a system (a "profile"), and Claude Code
loads only that system's agents, skills and commands.

| Profile | For | Marketplace(s) | Entry command | Agents |
|---|---|---|---|---|
| **dev** (default) | full-stack development | `full_stack_sm` | `/sm-feature`, `/sm-verify`, `/sm-docs`, `/sm-evaluate` | 13 + 7 advisory (ECC) |
| **seo** | search optimization | `full_stack_sm`(base) + `seo_sm` | `/seo-audit` | 5 |
| **marketing** | digital marketing | `full_stack_sm`(base) + `marketing_sm` | `/mkt-campaign` | 5 |
| **security** | security audit/hardening | `full_stack_sm`(subset) + `security_sm` | agents / `/sm-verify` | auditor + hunter |

Every non-dev profile also loads the shared base `hermes-core` (orchestration,
scratchpad handoff, session-handoff) + `hermes-verify` (quality gates), so
planning and "done = verified" work the same everywhere.

---

## Switching

The switcher rewrites `~/.claude/settings.json` to enable **exactly** the target
profile's plugins (mutual exclusion) and records the active one in
`~/.claude/.active-profile`.

```bash
cd /srv/sergiy_prod/ai-agents-config/claude_code/DEV

./switch-profile.sh --list        # profiles + which is active
./switch-profile.sh --current     # active profile
./switch-profile.sh marketing     # switch (dev | seo | marketing | security)
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
  insert into hc_jobs(kind,title,prompt,profile,work_dir)
  values('feature','…','…','seo','/path/to/project');   -- dev|seo|marketing|security
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

### dev
`/sm-feature "<what to build>"` → architect → plan → frontend/backend/database/
platform engineers → qa + security-auditor → code-reviewer + runtime-verifier.
Advisory ECC reviewers available: react/typescript/database-reviewer,
performance-optimizer, silent-failure-hunter, refactor-cleaner,
type-design-analyzer (all read-only — they propose, you apply).

### seo
`/seo-audit "<domain / task>"` → `seo-strategist` diagnoses (crawl→index→
content→authority→analytics), prioritizes by ICE, delegates to
`technical-seo-engineer`, `content-strategist`, `link-authority-strategist`,
`seo-analyst`. White-hat only; data-grounded (GSC/GA4, no invented metrics).

### marketing
`/mkt-campaign "<goal / campaign>"` → `marketing-strategist` sets strategy
(ICP→positioning→funnel→channels→budget), delegates to `content-marketer`,
`paid-media-buyer`, `lifecycle-marketer`, `marketing-analyst`. Content skills
include ECC's `content-engine`, `brand-voice`, `crosspost`, `article-writing`,
`market-research`. Unit-economics before scaling; spend/publish gated.

### security
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
- `route-profile.sh --num <n>` → `1=dev 2=marketing 3=seo 4=security`.
- `route-profile.sh "<task>"` → an optional suggested default to show in the ask.
- `dispatch-in-profile.sh <profile> -- <cmd>` → switch + **verify** + run under a
  lock (switch can't be skipped or raced). Headless `claude -p` needs no restart;
  interactive TUI does. Concurrent multi-profile → conductor `hc_jobs.profile`.

```bash
# Hermes: ask → parse reply → dispatch
p=$(claude_code/DEV/route-profile.sh --num 2)                 # user answered "2" -> marketing
claude_code/DEV/dispatch-in-profile.sh "$p" -- claude -p '<task>' --workdir <proj>
```

Intent → profile: SEO/ranking/SERP/crawl/keywords/backlinks → **seo**;
campaign/ads/funnel/email/social/content/positioning → **marketing**;
audit/vulnerability/OWASP/RLS/secrets → **security**; anything code → **dev**.
