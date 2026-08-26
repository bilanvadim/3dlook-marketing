# Recovery — the VPS is gone, or something on it is badly wrong

Two very different situations. Start by deciding which one you are in.

| Situation | Go to |
|---|---|
| Machine destroyed / migrating to new hardware | [Full rebuild](#full-rebuild) |
| Machine alive, system misbehaving | [TROUBLESHOOTING.md](TROUBLESHOOTING.md) first |
| A job finished but produced nothing | [Job-level recovery](#job-level-recovery) |
| The conductor tree looks wrong | [Runtime drift](#runtime-drift) |

---

## Full rebuild

**What the repo can restore:** every service definition, all agents, skills,
commands, prompts, brand assets, the conductor application, the routing logic, the
installer and the health check.

**What it deliberately cannot:** your secrets, your Claude Code login, and the job
queue. Those are machine state, not project state — see [what is lost](#what-is-lost).

```bash
sudo loginctl enable-linger $USER
git clone https://github.com/bilanvadim/3dlook-marketing.git
cd 3dlook-marketing
./bootstrap/install.sh          # will warn about the manual steps
# fill ~/.config/ai-agent-stack/secrets.env
claude                          # /login
./bootstrap/install.sh          # again — idempotent
./bootstrap/verify.sh
```

Expect `SYSTEM READY`. Then send one message through Telegram and check you get an
answer; services being up is not the same as the chain working.

### What is lost

- **`~/.hermes/ho.db`** — the job queue with its history. Not in git on purpose:
  it is per-machine state, and committing a live SQLite file that a service is
  writing produces torn snapshots. A fresh install starts with an empty queue.
  Unfinished jobs do not survive; re-enqueue them with `mvb-run.py`.
- **Telegram topics** live in Telegram, so they come back with your account.
  Topic→job mapping (`~/.hermes/mvb-job-threads.json`) does not, so notifications
  for pre-existing jobs fall back to the General topic.
- **The MTProto session** used by the E2E harness. Re-enrol interactively:
  `~/.hermes/mtproto/enroll.sh`.

### If you have a backup of the old machine

Restore these three, in this order, before the second `install.sh`:

```
~/.config/ai-agent-stack/secrets.env    # 600 — everything else is derived from it
~/.hermes/ho.db                         # queue history, if you want continuity
~/.hermes/mtproto/session.enc           # 600 — saves re-enrolling
```

Copy `ho.db` only while the conductor is **stopped**, and take it with
`sqlite3 old.db ".backup new.db"` rather than `cp`. A live SQLite database in WAL
mode is not one file, and a plain copy silently loses recent commits — that is not
theoretical, it bit this project on 2026-08-26 while testing a snapshot script.

---

## Job-level recovery

A `done` status only means the SDK session ended cleanly. It does not mean work
happened.

```bash
hermes_agent/ops/mvb-verify-job.py <id>
```

Counts files touched under `work_dir/workspace` across the job's lifetime. If it
reports zero artifacts, the run produced nothing regardless of how confident the
summary reads. Two documented cases (jobs 94 and 98) closed `done` in under a
minute having done nothing but report "запустил orchestrator в фоне".

Recovery is simply to re-enqueue — jobs are cheap to repeat and the pipelines are
checkpointed:

```bash
hermes_agent/ops/mvb-run.py article "<the exact same topic>" approve
```

The topic string must match the original **verbatim**: it keys the directory under
`workspace/seo/articles/`.

---

## Runtime drift

The system can be running something other than what git says. The two checks that
catch it:

```bash
./bootstrap/verify.sh                              # asks the RUNNING process for its cwd
marketing_vb/scripts/check-agent-copies.py         # md5-compares every agent copy
```

Reading unit files is not enough — a drop-in can override `WorkingDirectory`, which
is exactly how the conductor ran out of `/srv/…/ai-agents-config` for weeks while
the base unit still named this repo.

If agent copies have drifted, **do not blindly overwrite in either direction**. On
2026-08-26 eleven agents were drifting in *both* directions at once: some rules
were newer in the marketplace source, others newer in the installed copies, and no
copy was a superset. Diff and merge rule by rule.

To reset the runtime to what git holds:

```bash
./bootstrap/install.sh      # reinstalls units, drop-ins, cron; restarts services
```

---

## If the conductor will not start

```bash
journalctl --user -u hermes-conductor -n 50 --no-pager
```

Most common causes, in order of how often they have actually happened:

1. **`node_modules` missing or built against the wrong dependency.** The source
   needs `better-sqlite3`; an older tree had `@libsql/client`, which leaked
   connections and OOM-killed the box.
   ```bash
   cd claude_code/DEV/full_stack_sm/conductor && npm install
   ```
2. **A rogue conductor squatting port 3001.** The guard catches it:
   ```bash
   DRY_RUN=1 bash hermes_agent/ops/conductor-guard/hermes-conductor-guard.sh
   ```
3. **Rate limit, not a crash.** `paused: rate limit — retry in Ns` in the journal
   means it is waiting, not broken. The monitor pushes a ⏳ notice for stalls over
   ten minutes.
