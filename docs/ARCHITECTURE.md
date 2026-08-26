# Architecture — how a Telegram message becomes work

Written for someone (or some agent) who has never seen this VPS. It describes what
actually runs, verified against the live machine on 2026-08-26, not what a design
document once intended.

## The one-line version

Vadim types into Telegram. A **manager** decides whether that is conversation or a
job. If it is a job, it goes into a SQLite queue. A **conductor** picks it up and
opens a Claude Code session that does the work. The answer comes back to Telegram.

The manager never writes code or content. That is the whole point of the split.

```
                       ┌──────────────────────┐
                       │       Telegram       │   Vadim, in topics
                       └───────────┬──────────┘   (one topic per autonomous run)
                                   │ long-poll
                       ┌───────────▼──────────┐
                       │   hermes-gateway     │   systemd --user
                       │   (Hermes Agent)     │   ~/.hermes/hermes-agent, pip pkg
                       │   + claude_switcher  │   ← routing lives HERE, in this repo
                       └───────────┬──────────┘
                                   │
                 conversation ─────┴───── job
                       │                   │  mvb-run.py inserts ONE row
                       │                   ▼
                       │        ┌──────────────────────┐
                       │        │   ho_jobs (SQLite)   │  ~/.hermes/ho.db
                       │        └───────────┬──────────┘
                       │                    │ claimJob(), polling
                       │        ┌───────────▼──────────┐
                       │        │  hermes-conductor    │  systemd --user
                       │        │  (this repo's app)   │  claude_code/DEV/full_stack_sm/conductor
                       │        └───────────┬──────────┘
                       │                    │ Claude Agent SDK, settingSources:['project']
                       │        ┌───────────▼──────────┐
                       │        │     Claude Code      │  cwd = marketing_vb
                       │        └───────────┬──────────┘
                       │                    │
                       │     ┌──────────────┼──────────────┐
                       │  ┌──▼───┐      ┌───▼───┐     ┌────▼────┐
                       │  │Agents│      │Skills │     │  Tools  │
                       │  └──────┘      └───────┘     └─────────┘
                       │                    │
                       │        ┌───────────▼──────────┐
                       │        │ files in workspace/  │  the ONLY proof work happened
                       │        └───────────┬──────────┘
                       │                    │
                       │        ┌───────────▼──────────┐
                       └───────►│ conductor-monitor.sh │  cron */5 → Telegram
                                └──────────────────────┘
```

## The parts, and where each one lives

| Part | What it is | Where |
|---|---|---|
| **Hermes Agent** | The manager. Third-party pip package (`hermes-agent`, 0.20.5). Reads Telegram, decides route, never codes. | `~/.hermes/hermes-agent` (installed) |
| **claude_switcher.py** | The routing brain bolted onto the gateway: keyword → system, `mvb:*` routes, prompts, preconditions. **Ours.** | `hermes_agent/ops/claude-switcher/` → deployed to `~/.hermes/hermes-agent/gateway/` |
| **Conductor** | Autonomous worker. Claims jobs, runs the Claude Agent SDK, handles resume, rate-limit backoff, escalations. | `claude_code/DEV/full_stack_sm/conductor` (this repo) |
| **Queue** | `ho_jobs`, `ho_steps`, `ho_questions`, `ho_escalations`. | `~/.hermes/ho.db` — deliberately outside the repo |
| **Claude Code** | The executor. Third-party CLI. | `~/.local/bin/claude` |
| **Marketing system** | Agents, skills, commands, brand assets, workspace. | `marketing_vb/` |
| **Monitor** | Pushes questions, escalations, terminal jobs and backoff stalls to Telegram. | `hermes_agent/ops/conductor-monitor.sh`, cron `*/5` |

**Third-party by design:** Hermes Agent and Claude Code are installed software, not
vendored here. The repo owns the *configuration and logic* around them, and
`bootstrap/` installs them. That is a dependency on a published package, not on
another person's private tree.

## What is NOT part of this system

`/srv/vadim_prod/ai-agents-config` — Sergiy's system. Until 2026-08-26 the
conductor, the cron monitor and the daily updater all reached into it. They no
longer do, and `bootstrap/verify.sh` fails if any of that comes back. If you find
a reference to it while working here, it is either a historical comment or a bug.

## Telegram → job: the actual path

1. **Inbound.** Gateway long-polls Telegram. `claude_switcher` sees the message
   with its session key `chat#thread`.
2. **Route.** A leading keyword (`Стаття`, `Пости`, `Аутбаунд`, `Кампанія`) or the
   ⚙️ menu picks an `mvb:*` route. Anything else is conversation and stays with the
   manager.
3. **Enqueue.** The manager runs `hermes_agent/ops/mvb-run.py`, which is the ONLY
   sanctioned way to create a job. It imports the route table from
   `claude_switcher.py`, so the buttons and the script cannot drift apart. It fills
   `profile` and `work_dir` from the profile manifest, writes the pipeline's own
   slash command as the prompt, checks preconditions BEFORE a row exists, refuses
   duplicates, and records which Telegram topic asked so the answer returns there.
   It never writes `ho_steps`.
4. **Claim.** The conductor polls, claims the row, and opens an SDK session with
   `settingSources: ['project']`, `permissionMode: 'acceptEdits'`, cwd = `work_dir`.
5. **Work.** Claude Code loads `marketing_vb/CLAUDE.md`, the plugins, the agents.
   Artifacts go to files under `workspace/`. Never to chat.
6. **Return.** The conductor writes `result_summary` and a terminal status. Cron's
   monitor pushes it to the originating topic, with an artifact verdict attached.

### Two rules that exist because they were learned the hard way

**A `done` job proves nothing.** The status only says the session ended cleanly.
`mvb-verify-job.py` counts files touched under `work_dir/workspace` across the
job's lifetime, and the monitor downgrades ✅ to ⚠️ when that is zero. Jobs 94 and
98 both closed `done` in under a minute having written nothing.

**Allow rules must live in `settings.json`, not `settings.local.json`.**
`settingSources: ['project']` loads only the former. Rules parked in the latter are
invisible to every autonomous run, and with `acceptEdits` that means Bash,
WebSearch and WebFetch silently deny — a prompt no headless session can answer.

## Configuration model

Git is the source of truth; runtime locations receive copies through an install
step. Nothing is edited in place at runtime.

```
this repo  ──bootstrap/install.sh──►  ~/.config/systemd/user/…   (units, drop-ins)
                                      ~/.hermes/…                (gateway config, SOUL)
                                      crontab                    (monitor, checks)
```

Two things deliberately stay OUT of git: `~/.hermes/ho.db` (queue state travels
with the machine, not the repo) and `~/.config/ai-agent-stack/secrets.env` (real
credentials; `secrets.env.example` documents every key).

The daily `hermes update` re-applies vendored patches on top of the upstream
package. Those patch appliers live here, which is why an upstream reinstall does
not silently revert local behaviour.

## Where to look when something is wrong

| Symptom | Look here |
|---|---|
| Telegram silent | `systemctl --user status hermes-gateway`, `~/.hermes/logs/gateway.log` |
| Job never starts | `mvb-run.py status`, `journalctl --user -u hermes-conductor` |
| Job "done" with nothing to show | `mvb-verify-job.py <id>` |
| Agent behaving unexpectedly | `marketing_vb/scripts/check-agent-copies.py` — copies may have drifted |
| Anything at all | `bootstrap/verify.sh` |
