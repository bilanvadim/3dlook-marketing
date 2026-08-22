# Conductor ops — verified recipes (vadim's tree)

Session-verified operational detail for the `ho.db` / conductor worker on Вадим's
box. The SKILL.md narrative is authoritative; this file holds the exact, tested
commands so future sessions don't re-discover them.

## 1. Starting the conductor WORKER (vadim)

There is **NO active `hermes-conductor.service` unit** for vadim. The unit file is
`hermes-conductor.service.KEEP-vadim` — the `.KEEP-vadim` suffix is a deliberate
guard that makes systemd ignore the file, so:

```
systemctl --user start hermes-conductor     # ❌ "Failed to start hermes-conductor.service: Unit ... not found"
systemctl --user cat   hermes-conductor.service   # ❌ "No files found for hermes-conductor.service"
```

(The live `hermes-conductor.service` belongs to Сергей's tree at `/srv/...`;
do NOT touch it. Both vadim unit files carry the `.KEEP-vadim` guard.)

**Start the worker directly via its run script** (this is exactly what the
guarded unit's `ExecStart` does — `npm start` inside the conductor dir):

```bash
cd /home/vadim_prod/3dlook-marketing/claude_code/DEV/full_stack_sm/conductor
export PATH=/home/vadim_prod/.local/bin:/usr/local/bin:/usr/bin:/bin
export HERMES_REPO# (do NOT inline-source .env — it is blocked by the secret-guard)
exec bash /home/vadim_prod/3dlook-marketing/hermes_agent/ops/conductor-run.sh
```

Notes:
- `conductor-run.sh` itself sources `.env` (EnvironmentFile-style) via `npm start` /
  working dir; you do NOT need to `source ./.env` in your command (and you
  must not — the inline `.env` read trips the secret guard).
- Run it as a **long-lived background process** (`terminal(background=true)`, do
  NOT set `notify_on_complete` — it never exits). Verify with `ps aux | grep
  'conductor.ts' | grep -v sergiy`.
- It auto-applies `sql/schema.sql` to the local `ho.db` and runs `npm start`.
- **It will NOT auto-start after reboot** (no active systemd unit / no symlink in
  `default.target.wants`). Removing the `.KEEP-vadim` guard + enabling the unit is
  a systemd decision for Вадим, not the agent.

## 2. `ho.db` schema gotchas

Source of truth: `PRAGMA table_info(...)`.

| Table | Primary key / key columns | Note |
|---|---|---|
| `ho_jobs` | **`id`** (INTEGER PK) — NOT `job_id` | `SELECT … FROM ho_jobs WHERE id=90` ✅ / `WHERE job_id=90` ❌ "no such column: job_id" |
| `ho_steps` | `id` PK, **`job_id`** FK | step rows keyed by `job_id` |
| `ho_project_status` | **`job_id`** | view column is `job_id` |
| `ho_questions` / `ho_escalations` | `id` PK, `job_id` FK | |

Key columns in `ho_jobs`: `id, kind, title, prompt, priority, status, max_turns,
max_wall_secs, permission_mode, work_dir, resume_session_id, attempts, profile,
created_at, not_before, claimed_by, claimed_at, finished_at, result_summary, error`.

**Marketing profiles leave `ho_steps` EMPTY by design.** Conductor ignores
`ho_steps` for non-dev profiles (`HO_STEP_PROFILES`), running the pipeline via
internal slash commands (`/post-from-article`, etc.). So "no rows in ho_steps"
after minutes is **NOT a stall signal** for `marketing_vb*` jobs — judge progress
by `ho_jobs.status` + artifacts on disk, not by step rows.

### Correct monitor queries

```bash
# Job list (running/queued/deferred) — uses ho_project_status.job_id ✅
sqlite3 ~/.hermes/ho.db "SELECT job_id,job_status,percent,done_steps,total_steps,open_questions,open_escalations FROM ho_project_status WHERE job_status NOT IN ('done','failed','aborted');"

# Per-job DETAIL — ho_jobs uses id, NOT job_id ✅
sqlite3 ~/.hermes/ho.db "SELECT id,status,attempts,claimed_by,claimed_at,finished_at,result_summary,error FROM ho_jobs WHERE id=<n>;"

# Per-step (only meaningful for dev-profile jobs)
sqlite3 ~/.hermes/ho.db "SELECT step_no,title,status,attempts,score FROM ho_steps WHERE job_id=<n> ORDER BY step_no;"

# Open questions / escalations
sqlite3 ~/.hermes/ho.db "SELECT id,job_id,step_no,question FROM ho_questions WHERE status='open';"
sqlite3 ~/.hermes/ho.db "SELECT id,job_id,reason,question FROM ho_escalations WHERE status='open';"
```

`job_status` values: `queued` → `running` → `deferred` (limit back-off, auto-resumes)
→ `done` / `failed` / `aborted`. `claimed_by` shows the worker PID (e.g. `ho-3252369`)
once a worker claims it; empty after it defers/ releases.

## 3. Finishing a DEFERRED marketing job on OpenCode (validated)

When a marketing/content conductor job (e.g. `posts <slug>`) goes `deferred`
because Claude hit its session/usage limit mid-run, you can finish the *missing*
pieces on the free OpenCode coder instead of waiting for the reset. The pipeline
writes per-artifact files to disk, so OpenCode completes only what's left by
treating existing outputs as templates.

This is an **explicit user override** ("переключи" / "finish on OpenCode") — not
autonomous. Recipe:

```bash
cd /home/vadim_prod/3dlook-marketing/marketing_vb   # MUST be inside the repo
export PATH="$HOME/.opencode/bin:$PATH"
export OPENCODE_CONFIG="$HOME/.config/opencode/opencode.jsonc"
# launch as long-lived background; do NOT pass -m (model comes from opencode.jsonc = llm-fop-strong/auto via failover proxy)
opencode run '... targeted prompt: create ONLY the missing <profile>/post.md files, mirror the frontmatter+format of an existing one, follow brand-assets/linkedin-post-prompts.md + social-profiles-config.md, then update manifest.json (add entries, set ready_for_review:true). Do NOT commit/push. ...'
```

Pre-checks before launching:
- `opencode` binary at `~/.opencode/bin/opencode` (v1.16.2). If not on PATH, use that full path.
- The strong failover proxy must be alive: `systemctl --user is-active llm-failover-proxy-strong.service` (HTTP 401 on `/v1/models` is expected — means the endpoint exists; OpenCode authenticates via the proxy config, no key needed inline).
- Pin the prompt to the **missing** profiles only (from `ls workspace/social/articles/<slug>/`), and tell OpenCode to treat an existing `post.md` as the format/tone template. This matches how the conductor itself drafts.
- After OpenCode finishes, verify all 9 `*/post.md` exist + `manifest.json` is complete; then `mvb-run.py digest <slug>` for Вадим's review (tg-bridge is off, so posts don't arrive in Telegram otherwise).
