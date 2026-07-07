# Install — Sergiy config on Vadim's machine

This branch (`sergiy_config`) adds Sergiy's two-layer agent system on top of
Vadim's existing marketing project:

- **Claude Code layer** — 6 switchable "systems" (profiles), see `claude_code/DEV/SYSTEMS.md`.
- **Hermes layer** — an autonomous orchestrator (Telegram bot + orchestrator worker
  that drives Claude Code over a SQLite/libSQL `ho_*` job queue).

> Vadim's original system is **untouched** under [`marketing_vb/`](marketing_vb).
> Nothing here modifies it; it is only *also* packaged as a switchable system.

## 0. Prerequisites

| Tool | For | Notes |
|---|---|---|
| `claude` CLI | all Claude Code systems | logged in (subscription) or `ANTHROPIC_API_KEY` |
| `python3` | switch-profile.sh | stdlib only |
| `node` + `npm` | Hermes orchestrator | Node 20+ |
| `sqlite3` | orchestrator state (libSQL file) | ships with most distros; state is a local file — **no Postgres/Supabase** |
| Turso / libSQL server | optional | only if you want a networked/shared DB instead of the local file |
| Telegram bot token | Hermes escalations | optional but recommended |

## 1. Bootstrap

```bash
git clone -b sergiy_config <this-repo> && cd 3dlook-marketing
./install.sh                       # checks deps, prepares orchestrator, renders systemd units
# or Claude-Code-only:
./install.sh --no-orchestrator
```

`install.sh` never runs sudo — it prepares files and **prints** the privileged
commands. Pass machine values for the systemd units:

```bash
./install.sh --user vadim --home /home/vadim
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

## 3. Hermes orchestrator (autonomous worker)

The orchestrator pulls jobs from its SQLite/libSQL `ho_*` queue, runs them through
the Claude Agent SDK in the profile named on the job, and escalates to Telegram.

```bash
cd claude_code/DEV/full_stack_sm/orchestrator
npm ci && npm test                 # unit + libSQL store smoke, no API/network
cp .env.example .env               # then edit:
#   DATABASE_URL   → file:./ho.db (default, zero infra) — or libsql://…/Turso for a networked DB
#   ANTHROPIC_API_KEY (or leave empty to use the logged-in Claude plan)
#   TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID (escalations)

# create the state (tables ho_jobs, ho_runs, ho_steps, ho_questions, ho_escalations + views)
sqlite3 ho.db < sql/schema.sql            # file: mode (install.sh already did this)
#   Turso/libSQL instead:  turso db shell <db> < sql/schema.sql
```

Run as a service (unit was rendered to `hermes_agent/ops/systemd/generated/`):

```bash
sudo cp hermes_agent/ops/systemd/generated/hermes-orchestrator.service /etc/systemd/system/
sudo systemctl daemon-reload && sudo systemctl enable --now hermes-orchestrator
systemctl status hermes-orchestrator
```

`orchestrator-run.sh` defaults `DATABASE_URL` to `file:$HO_STATE_DIR/ho.db`
(`$HO_STATE_DIR` = `$HOME/.hermes`) and auto-creates the schema for file: mode;
set `DATABASE_URL=libsql://…` in `.env` to use Turso/a libSQL server instead.

## 4. Push-notifier (cron)

Pushes new open questions / escalations / terminal jobs to Telegram:

```bash
( crontab -l 2>/dev/null; \
  echo "*/5 * * * * $PWD/hermes_agent/ops/orchestrator-monitor.sh >> \$HOME/.hermes/orchestrator-monitor.log 2>&1" ) | crontab -
# first run: mark current state as seen (no backlog spam)
hermes_agent/ops/orchestrator-monitor.sh --init
```

It reads `$HOME/.hermes/.env` for `TELEGRAM_BOT_TOKEN` / `TELEGRAM_ALLOWED_USERS`
(override with `HERMES_ENV_FILE`).

## 5. Telegram bot (chat entry point)

Vadim already ships a bot under `marketing_vb/telegram-bot/`. Two options:
- **Keep Vadim's bot** for marketing chat; use the orchestrator + monitor above for
  autonomous jobs. (Simplest.)
- **Run Sergiy-style Hermes** (OpenCode gateway) as the single orchestrator that
  routes to Claude Code by profile — that's the reference in
  `hermes_agent/skills/vps-orchestration/SKILL.md` (paths there are examples).

## 6. Enqueue a job

```bash
DB=claude_code/DEV/full_stack_sm/orchestrator/ho.db   # or your Turso shell
sqlite3 "$DB" \
 "insert into ho_jobs(kind,title,prompt,profile,work_dir)
  values('feature','smoke','напиши hello в файл hi.txt','marketing_vb_sm','$PWD');"
# watch it move queued → running → done
sqlite3 "$DB" "select id,status,profile,result_summary from ho_jobs order by created_at desc limit 5;"
```

`profile` ∈ `dev | seo | marketing | security | marketing_vb | marketing_vb_sm`.
The worker loads exactly that system's plugins for the job (concurrency-safe),
so you never switch the global `settings.json` for autonomous runs.

## Notes / caveats

- `hermes_agent/skills/vps-orchestration/SKILL.md` documents Sergiy's reference
  VPS; its absolute paths are examples — adapt to your machine.
- The orchestrator **does not cap cost** by design (quality-first); the only
  runaway guard is the in-process circuit breaker.
- The `marketing_vb` plugins are copies of `marketing_vb/.claude/`; if Vadim
  edits the originals, re-sync the plugin copies.
