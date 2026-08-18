# Conductor — operational runbook

Autonomous worker that runs the dev/seo/marketing/security systems
over the Claude Agent SDK, with a circuit breaker, durable resume, and Telegram
escalations. State = SQLite (`ho_*` tables). **Live-verified 2026-07-18.**

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
  values('feature','<title>','<prompt>','dev','@HOME@/workspaces/<proj>',60,7200);"
```

- **`profile` MUST be a long name** — `dev | seo | marketing | security`
  (matches `agents-ai/telegram-bot-agent/claude-code-agent/DEV/profiles/<profile>.json`). The worker logs
  `job N profile='dev' → 11 plugin(s)` when it resolves.
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
(`profile in ('dev','seo',...)`) — inserting `'dev'` then fails the CHECK, and
inserting `'dev'` resolves **0 plugins** (`no manifest for 'dev'`). Rebuild it
(the current `schema.sql` has the correct `'dev'…` constraint):

```bash
systemctl --user stop hermes-conductor.service
cp ~/.hermes/ho.db ~/.hermes/ho.db.bak            # empty/throwaway state only
rm -f ~/.hermes/ho.db ~/.hermes/ho.db-wal ~/.hermes/ho.db-shm
sqlite3 ~/.hermes/ho.db < agents-ai/telegram-bot-agent/claude-code-agent/DEV/dev/conductor/sql/schema.sql
systemctl --user start hermes-conductor.service
```

## Why the store is on better-sqlite3, not libSQL (2026-08-14 incident)

The conductor took the whole machine down without running a single job. After 24 h
of polling an **empty** queue it held **33 021 open connections** to `ho.db` —
66 081 fds, **5.4 GB** RSS and 1.3 GB of swap. On a 15 GB box that meant swap
thrashing for everyone: the neighbouring `hermes-gateway` (a different account)
had its watchdog thread starved so badly it took **24 minutes** to reach its own
`os._exit()`, and the kernel OOM-killer fired at 07:31:56.

Cause: in the local libSQL driver `client.transaction()` hands its connection to
the transaction object and drops its own reference, and neither `commit()`,
`rollback()` nor `close()` ever calls `db.close()`. One orphaned connection per
transaction — ~170 KB of native page cache and 2 fds each, invisible to V8, so no
heap limit and no GC ever touches it. Still true in `@libsql/client` 0.17.4.

The first fix kept the driver and avoided the leaking call: `BEGIN IMMEDIATE`
through `execute()`, plus a `txChain` to serialize blocks and a `recycle()` to
close connections poisoned by a lost `BEGIN` — because a `BEGIN` that loses the
race leaves an unreset statement behind and every later `COMMIT` on that
connection then fails forever with `cannot commit transaction - SQL statements
in progress`. Note what that means: **the leak was also the recovery mechanism**
— the old code only survived contention because it threw the poisoned connection
away. Remove the leak naively and the worker breaks on its first contended claim.

That was a workaround for a driver we had no other reason to keep, so the store
moved to **better-sqlite3** (commit after f400b82). Same SQLite, same file, and
barely a different API — @libsql/client's local mode was itself built on a
better-sqlite3-COMPATIBLE fork. What it does not have, verified against the same
harness that reproduced both faults:

- no connection handoff, so nothing to leak — one Store owns one connection;
- no poisoning: after a `BEGIN` loses the race, the next transaction on that same
  connection commits normally, so `recycle()` is gone;
- synchronous transaction bodies, which cannot interleave, so `txChain` is gone.

**What we gave up**: `DATABASE_URL` is local-file only now. Pointing the queue at
a libSQL server or Turso Cloud is a deliberate project, not a URL change —
`store.ts` rejects a remote URL loudly rather than treating it as a filename.

`test/fdleak.test.ts` is the guard, and it is driver-agnostic: 200 transactions
must not grow the fd count. Its control run leaks connections on purpose and
asserts the counter noticed — if that control fails, the test has stopped
measuring anything and a green run above it means nothing.

Backstop, in `/etc/systemd/system/hermes-conductor.service.d/memory.conf` — so a
future runaway kills this service instead of the machine:

```ini
[Service]
MemoryHigh=2G
MemoryMax=3G
MemorySwapMax=512M
```

Healthy idle numbers to compare against: ~60 MB RSS and a flat fd count.
Check with `ls /proc/$(pgrep -f 'src/core/conductor.ts')/fd | wc -l` — note that
`systemctl show -p MainPID` returns the **wrapper** script, not the node process.

## Live smoke — what was verified (2026-07-18)

A throwaway `feature` job proved end-to-end: claim → **dev → 11 plugins** →
Claude ran (created the target file) via SDK plan-auth under systemd → circuit
breaker **turn-backstop** fired → `ho_escalations` row (`reason=turns`) → decision
`aborted` picked up in <6s → job terminal `aborted` → worker back to idle. Unit
tests: 8 (breaker/steploop/steprunner) + 15 (store) green. Note: a full
autonomous project run (many turns, real repo, commit/push/deploy) has NOT been
exercised yet — start with a small job and a generous but bounded `max_turns`.
