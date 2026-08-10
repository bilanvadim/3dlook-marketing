# Conductor — operational runbook

Autonomous worker that runs the dev-sm/seo-sm/marketing-sm/security-sm systems
over the Claude Agent SDK, with a circuit breaker, durable resume, and Telegram
escalations. State = SQLite/libSQL (`ho_*` tables). **Live-verified 2026-07-18.**

## Run (systemd --user, like hermes-gateway)

```bash
cp agents-ai/telegram-bot-agent/hermes-agent/ops/systemd/hermes-conductor.service ~/.config/systemd/user/
systemctl --user daemon-reload
systemctl --user enable --now hermes-conductor.service
systemctl --user status hermes-conductor.service     # → active; log: "conductor up. polling…"
```

ExecStart = `agents-ai/telegram-bot-agent/hermes-agent/ops/conductor-run.sh` (defaults `DATABASE_URL` to
`file:$HOME/.hermes/ho.db`, ensures schema, `npm start`). The `.env` is injected
via `EnvironmentFile=` (npm start does not read .env by itself). Auth = the
logged-in Claude plan (no API key). Idle with an empty queue = does nothing.

## Dispatch a job

```bash
sqlite3 ~/.hermes/ho.db "insert into ho_jobs(kind,title,prompt,profile,work_dir,max_turns,max_wall_secs)
  values('feature','<title>','<prompt>','dev-sm','/home/sergiy_prod/workspaces/<proj>',60,7200);"
```

- **`profile` MUST be a long name** — `dev-sm | seo-sm | marketing-sm | security-sm`
  (matches `agents-ai/telegram-bot-agent/claude-code-agent/DEV/profiles/<profile>.json`). The worker logs
  `job N profile='dev-sm' → 11 plugin(s)` when it resolves.
- `work_dir` is the project checkout (its `.claude/` is loaded via
  `settingSources:['project']`). For real projects, point at a repo that has the
  marketplace `.claude/` so the guard + Stop-hook (commit/push) apply.
- `max_turns` / `max_wall_secs` bound one run; hitting them **escalates** (breaker
  backstop), it does not silently kill.

## Monitor & decide

- Status for Telegram: `select * from ho_project_status where id=<job>;`
  (`job_status`, `percent`, `open_questions`, `open_escalations`).
- `conductor-monitor.sh` (cron */5) pushes new questions / escalations / done
  jobs to Telegram (dedup; run `--init` once after setup).
- **Interview questions** (`ho_questions`, status=open) → answer:
  `update ho_questions set answer=?, status='answered' where id=?;` → job leaves
  `awaiting-input` and resumes.
- **Escalations** (`ho_escalations`, status=open) → decide via Telegram buttons
  (`ho:approve|deny|abort:<id>`) or SQL:
  `update ho_escalations set status='approved'|'denied'|'aborted', decided_by='me',
   decided_at=datetime('now') where id=<id> and status='open';`
  The worker picks it up within the poll interval.

## Gotcha — stale ho.db profile constraint

`conductor-run.sh` runs `schema.sql` with `create table if not exists`, so it
will **not** migrate an existing table. A `ho.db` created from an older schema
may still carry the legacy short-name constraint
(`profile in ('dev','seo',...)`) — inserting `'dev-sm'` then fails the CHECK, and
inserting `'dev'` resolves **0 plugins** (`no manifest for 'dev'`). Rebuild it
(the current `schema.sql` has the correct `'dev-sm'…` constraint):

```bash
systemctl --user stop hermes-conductor.service
cp ~/.hermes/ho.db ~/.hermes/ho.db.bak            # empty/throwaway state only
rm -f ~/.hermes/ho.db ~/.hermes/ho.db-wal ~/.hermes/ho.db-shm
sqlite3 ~/.hermes/ho.db < agents-ai/telegram-bot-agent/claude-code-agent/DEV/dev-sm/conductor/sql/schema.sql
systemctl --user start hermes-conductor.service
```

## Live smoke — what was verified (2026-07-18)

A throwaway `feature` job proved end-to-end: claim → **dev-sm → 11 plugins** →
Claude ran (created the target file) via SDK plan-auth under systemd → circuit
breaker **turn-backstop** fired → `ho_escalations` row (`reason=turns`) → decision
`aborted` picked up in <6s → job terminal `aborted` → worker back to idle. Unit
tests: 8 (breaker/steploop/steprunner) + 15 (store) green. Note: a full
autonomous project run (many turns, real repo, commit/push/deploy) has NOT been
exercised yet — start with a small job and a generous but bounded `max_turns`.
