# Install — Sergiy config on Vadim's machine

This branch (`sergiy_config`) adds Sergiy's two-layer agent system on top of
Vadim's existing marketing project:

- **Claude Code layer** — 6 switchable "systems" (profiles), see `claude_code/DEV/SYSTEMS.md`.
- **Hermes layer** — an autonomous orchestrator (Telegram bot + conductor worker
  that drives Claude Code over a Postgres `hc_*` job queue).

> Vadim's original system is **untouched** under [`marketing_vb/`](marketing_vb).
> Nothing here modifies it; it is only *also* packaged as a switchable system.

## 0. Prerequisites

| Tool | For | Notes |
|---|---|---|
| `claude` CLI | all Claude Code systems | logged in (subscription) or `ANTHROPIC_API_KEY` |
| `python3` | switch-profile.sh | stdlib only |
| `node` + `npm` | Hermes conductor | Node 20+ |
| Postgres (`psql`) | conductor state + Hermes | self-hosted Supabase or any Postgres |
| `docker` | Supabase stack / conductor isolation | optional if you point at a remote PG |
| Telegram bot token | Hermes escalations | optional but recommended |

## 1. Bootstrap

```bash
git clone -b sergiy_config <this-repo> && cd 3dlook-marketing
./install.sh                       # checks deps, prepares conductor, renders systemd units
# or Claude-Code-only:
./install.sh --no-conductor
```

`install.sh` never runs sudo — it prepares files and **prints** the privileged
commands. Pass machine values for the systemd units:

```bash
./install.sh --user vadim --home /home/vadim --stack-env /srv/vadim/supabase/.env
```

## 2. Claude Code — the 6 systems

```bash
claude_code/DEV/switch-profile.sh --list          # dev seo marketing security marketing_vb marketing_vb_sm
claude_code/DEV/switch-profile.sh marketing_vb_sm # activate one
# → RESTART Claude Code (plugins load at session start)
claude_code/DEV/switch-profile.sh --current
```

Marketplace paths in `profiles/*.json` are **relative** and resolved at switch
time, so no path editing is needed regardless of where you cloned the repo.

- **marketing_vb_sm** — Vadim's default: brand-grounded execution + Sergiy's
  strategy/measurement. Entry `/vbsm-campaign`.
- **marketing_vb** — Vadim's original, pure. Run inside a dir with
  `brand-assets/` + `workspace/` (e.g. `marketing_vb/`). Entries `/new-article`,
  `/weekly-posts`, `/outbound`, …
- **marketing / dev / seo / security** — Sergiy's generic systems.

Full details: `claude_code/DEV/SYSTEMS.md`.

## 3. Hermes conductor (autonomous worker)

The conductor pulls jobs from Postgres `hc_*`, runs them through the Claude
Agent SDK in the profile named on the job, and escalates to Telegram.

```bash
cd claude_code/DEV/full_stack_sm/conductor
npm ci && npm test                 # 27 core tests, no API/network
cp .env.example .env               # then edit:
#   DATABASE_URL   → your Postgres (self-hosted Supabase reachable as supabase-db)
#   ANTHROPIC_API_KEY (or leave empty to use the logged-in Claude plan)
#   TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID (escalations)

# apply schema (hc_jobs, hc_runs, hc_steps, hc_questions, hc_escalations, …)
psql "$DATABASE_URL" -f sql/schema.sql
psql "$DATABASE_URL" -f sql/002_steps_questions.sql
psql "$DATABASE_URL" -f sql/003_profiles.sql
```

Run as a service (unit was rendered to `hermes_agent/ops/systemd/generated/`):

```bash
sudo cp hermes_agent/ops/systemd/generated/hermes-conductor.service /etc/systemd/system/
sudo systemctl daemon-reload && sudo systemctl enable --now hermes-conductor
systemctl status hermes-conductor
```

`conductor-run.sh` resolves the Postgres IP + password fresh at each start
(from `STACK_ENV`'s `POSTGRES_PASSWORD`), or uses `DATABASE_URL` if you set it
directly in `.env`.

## 4. Push-notifier (cron)

Pushes new open questions / escalations / terminal jobs to Telegram:

```bash
( crontab -l 2>/dev/null; \
  echo "*/5 * * * * $PWD/hermes_agent/ops/conductor-monitor.sh >> \$HOME/.hermes/conductor-monitor.log 2>&1" ) | crontab -
# first run: mark current state as seen (no backlog spam)
hermes_agent/ops/conductor-monitor.sh --init
```

It reads `$HOME/.hermes/.env` for `TELEGRAM_BOT_TOKEN` / `TELEGRAM_ALLOWED_USERS`
(override with `HERMES_ENV_FILE`).

## 5. Telegram bot (chat entry point)

Vadim already ships a bot under `marketing_vb/telegram-bot/`. Two options:
- **Keep Vadim's bot** for marketing chat; use the conductor + monitor above for
  autonomous jobs. (Simplest.)
- **Run Sergiy-style Hermes** (OpenCode gateway) as the single orchestrator that
  routes to Claude Code by profile — that's the reference in
  `hermes_agent/skills/vps-orchestration/SKILL.md` (paths there are examples).

## 6. Enqueue a job

```bash
psql "$DATABASE_URL" -c \
 "insert into hc_jobs(kind,title,prompt,profile,work_dir)
  values('feature','smoke','напиши hello в файл hi.txt','marketing_vb_sm','$PWD');"
# watch it move queued → running → done
psql "$DATABASE_URL" -c "select id,status,profile,result_summary from hc_jobs order by created_at desc limit 5;"
```

`profile` ∈ `dev | seo | marketing | security | marketing_vb | marketing_vb_sm`.
The worker loads exactly that system's plugins for the job (concurrency-safe),
so you never switch the global `settings.json` for autonomous runs.

## Notes / caveats

- `hermes_agent/skills/vps-orchestration/SKILL.md` documents Sergiy's reference
  VPS; its absolute paths are examples — adapt to your machine.
- The conductor **does not cap cost** by design (quality-first); the only
  runaway guard is the in-process circuit breaker.
- The `marketing_vb` plugins are copies of `marketing_vb/.claude/`; if Vadim
  edits the originals, re-sync the plugin copies.
