# Changelog

One canonical repository serving two isolated runtimes on one VPS. Versions are bumped by
whoever changes what those runtimes install; `status.sh` prints the version and every backup
manifest records it, so a restore can say what it is restoring.

The entries below say what changed **and what was wrong before**, because on a system that
updates itself the reason is the part you need six months later. Anything marked ⚠ changed
behaviour that a runtime depends on.

## 0.1.0 — 2026-08-12

First version of the platform as a platform: one repo, two profiles, a render step, nine
operational scripts, and a conductor that is no longer two diverging copies.

### Added

- **`config/profiles/{sergiy_prod,vadim_prod}.vars`** — per-user values, committed, never
  secret: identity, project root, systemd scope per service, profile role, and the **ports**.
  Ports are the main reason a profile exists: both runtimes bind the same loopback, so a shared
  value does not error — the second binder silently loses.
- **`scripts/render.sh <profile>`** — clean clone → runtime tree. Idempotent; `--check` reports
  what would change without touching anything, which is what lets update/doctor tell a *missed
  render* from real *drift*.
- **`scripts/`** — the nine operational scripts plus a shared `lib.sh`:
  `deploy.sh`, `update.sh`, `check-update.sh`, `status.sh`, `diff.sh`, `validate.sh`,
  `backup.sh`, `doctor.sh`, `rollback.sh`.
- **`VERSION`**, this changelog.
- **`agents-ai/.../ops/conductor-snapshot.sh`** — a pre-run recovery point written to
  `refs/hermes/snapshots/job-<id>` without touching HEAD, the branch, the index or the working
  tree. Autonomous runs previously had none: autocommit deliberately skips main/master and these
  repos work on main.
- **conductor tests** — `contention.test.ts`, `signature.test.ts`, `backoff.test.ts`, plus new
  cases in the breaker and store suites. 39 → **113** assertions.

### Fixed

- ⚠ **The conductor was two divergent lineages**, each holding real fixes the other lacked. Line
  counts made it look like one was simply newer; the diffs showed a two-way merge. Now one
  codebase with both sets. From the deployed side: the turn signature hashes the whole tool
  input instead of the first 80 chars of the target (six reads of six *different* files in one
  deep directory collapsed into one signature and read as a loop — that killed one job and
  caused 8 of the first 11 escalations ever raised); read-only tools get their own, longer stuck
  threshold; a rate-limit **backoff ladder** with per-job and account-wide no-progress streaks
  (a flat 60 s retry cannot clear an hours-long usage window — one job burned 193 zero-turn runs
  in 3 h 22 m); escalations no longer expire, so a late button tap still lands and the job parks
  and re-asks instead of dying; "approve" on a *breaker* escalation means **continue**, not
  "done", and only an SDK result event may mark a job done. From the canonical side: `posEnv` on
  every tunable (a blank line in `.env` must not become a real 0), heartbeats while streaming and
  while a human thinks, a poison-job attempt cap, stale recovery that returns the dead worker's
  *step* to pending, `finishStep` no longer nulling the whole evidence trail, and
  `answerQuestion` releasing a job parked in `awaiting-input`.
- ⚠ **Lock waits froze the whole conductor process.** SQLITE_BUSY looked like impatience, so
  `busy_timeout` was raised to 30 s. The local libSQL driver is **synchronous**: a 5 s lock wait
  let exactly 0 timers fire. The errors stopped and the process stalled instead — the escalation
  webhook never reached `listen()`. Now a short in-driver wait plus an async retry ladder that
  yields. Two bugs surfaced proving it: a failed transaction that is not rolled back **poisons
  the client** (it stays inside the transaction and every later write conflicts with its own
  dangling one — SQLITE_BUSY forever on a database nobody else holds), and WAL is a *correctness*
  requirement here, not a speed tweak (in rollback-journal mode a reader blocks a writer's
  COMMIT, so the lock holder cannot commit while the pollers cannot write).
- ⚠ **The step executor ran with `bypassPermissions`.** That skips the work directory's own deny
  rules *and* its PreToolUse hooks — exactly where the protection lives — leaving a sentence in a
  prompt as the only guard. Now `acceptEdits`, with read-only web tools pre-approved because
  headless auto-denies them.
- ⚠ **`HO_WEBHOOK_PORT` was a shared default (3001).** It binds a real port, so on one box the
  second conductor to start silently lost every Approve/Deny tap. Now assigned per profile
  (3011 / 3001), bound to loopback only, and a bind failure no longer kills the worker.
- **`install.sh` corrupted its own renderer.** The tree-wide identity substitution rewrote
  `hermes-update.py`'s token table — it holds `("@OWNER@", "HERMES_OWNER")` as *code* — so the
  updater stopped recognising `@OWNER@` and the next `hermes update` would hand the agent a
  persona containing a literal `@OWNER@`. Found live on one account, in both the repo copy and
  the deployed one.
- **The `ho_jobs` profile CHECK rejected two shipped profiles** (`sandbox`, `test`): enqueueing
  against either failed with a bare constraint error and no hint why.
- **Duplicate enqueues** are now refused by a unique index (at most one *active* job per
  title + work_dir) instead of becoming three copies of the same work splitting one usage window.
- Telegram sends inspect the HTTP response and retry once without `parse_mode`; a breaker
  escalation's buttons say **Continue / Stop & keep** rather than Approve / Deny.

### Operational fixes not visible in the code

- **vadim_prod's tree was a plain copy, not a clone** — no remote, no update path, no way to tell
  drift from normal. Replaced with a real read-only clone (deploy key; GitHub ignores granular
  "Read" for collaborators on a personal repo) plus a render.
- ⚠ **The conductor unit and the running process pointed at different trees** for a full day,
  held that way by a drop-in. A reboot would have resolved the disagreement itself, silently,
  onto a tree that could not start (no `node_modules`) and a database that was an empty schema.
- ⚠ **The gateway and the conductor used different `ho.db` files.** Every Telegram Approve/Deny
  wrote `approved` into an empty schema while the conductor timed out against another file.
  Nothing logged — both halves were working perfectly, on different databases. The queue
  (77 jobs / 531 runs) now lives in `~/.hermes/ho.db`, outside any project checkout, and
  `doctor.sh` checks the two halves agree.
- **The conductor guard had become a no-op**: it filtered on the old tree's path, so a rogue
  started from the new one was ignored. It now covers both, with the cgroup test still protecting
  the managed process.

### Development separated from the runtimes

Both `/srv/*/ai-agents-config` trees are now **consumer** replicas carrying no commits; commits
happen in `/srv/sergiy_prod/ai-agents-config-dev`, which nothing reads at run time. Previously one
directory did both jobs, so an editor and a production system shared a path — saving a
half-finished edit made it the live config Claude Code and the conductor read on their next call,
and `update.sh --force` would `reset --hard` over real work rather than over regenerable render
output.

The runtime path deliberately did not move: two systemd units and all six `DEV/profiles/*.json`
name it absolutely, so relocating it would be downtime for no benefit. A `pre-commit` hook
installed by `deploy.sh` refuses commits in a consumer tree and names the dev checkout. The dev
checkout is under `/srv` and not `~/workspaces` because `repo-manager.sh` deletes a workspace
directory after 72 hours of inactivity.

`PROFILE_ROLE=author` is now unused by both profiles but kept: it is a real distinction, and
removing the handling would give a future author tree the wrong behaviour silently.

### Secrets consolidated

`sergiy_prod` had no `secrets.env` — keys sat directly in the files `install.sh` is meant to
generate. Reconstructed the source from those copies (17 values, byte-for-byte verified),
including `MTPROTO_SESSION_KEY` and `CONDUCTOR_BRIDGE_TOKEN`, which `install.sh` mints when absent:
a new session key makes the existing `session.enc` undecryptable and a new bridge token
desynchronises the bridge from its clients. `install.sh` now resolves `--secrets` → XDG store →
legacy in-kit path; the old default kept a file full of API keys inside a git checkout. `doctor.sh`
compares the source against its generated copies by hash, because divergence produces no error in
either direction.

### The template now names nobody

Paths in `agents-ai/` are `@DEST@` / `@HOME@` / `@USER@`, substituted by `render.sh` from the
profile. Previously the tree carried the author's real paths as fact, so rendering was a no-op for
one profile and a rewrite for the other — the "template" was one user's tree that happened to work
for him, and `settings.json.example` handed out his repo path to anyone who copied it. Rendering is
now symmetric: ~24 files for either profile.

Proven equivalent rather than assumed: rendering the tokenised template as `sergiy_prod` reproduces
the previous tree **byte for byte**, with the only differences being the three `*.example` files
that intentionally moved from real paths to `YOUR_USER`.

`validate.sh` enforces the invariant in both directions — no absolute path may name any profile's
account, **and** the tokens must be present, because a tree that simply lost its paths would satisfy
the first half while rendering to a runtime with no paths at all. The check is about **paths, not
mentions**: `vps-maintenance/SKILL.md` deliberately says "do not kill processes owned by other users
(vadim_prod, root)", and tokenising that would render to "do not kill processes owned by *yourself*"
— the rule inverted. Test fixtures are excluded because `signature.test.ts` asserts that six real
128-character paths share their first 80 characters, which only holds for a fixed literal.

⚠ Consequence: between `update.sh`'s `reset --hard` and its render, a live tree is in template form
and therefore **broken**, not merely stale. An `EXIT` trap re-renders on any exit path until the
render clears it, so a failed pull cannot leave it that way.

### vault-sync was corrupting rendered trees, 48 times a day

`ops/vault-sync.sh` ran `git pull --rebase --autostash` on the **runtime tree** every 30 minutes.
On a rendered tree that is a wrecking ball: the ~30 files carrying a profile's paths are render
output, autostash treats them as user work, and reapplying them over a pulled template leaves
conflict markers in the working tree. It happened — every `profiles/*.json` on vadim_prod ended up
with `<<<<<<< Updated upstream` and stopped being valid JSON, so Claude Code resolved **no plugin
marketplaces at all**. sergiy_prod escaped by timing alone: the timer fired minutes either side of
the window.

Pulling was never needed for the script's job (it pushes a subdirectory) and a runtime replica must
not commit at all. The pull is gone, and the script now refuses to run in a replica and says why.
The timer is disabled on both accounts: in the whole history of this repo exactly **one** commit has
ever touched the vault, and it was the structural move — the sync half had never once done anything,
while the pull half was actively destructive.

The underlying problem is fixed rather than papered over: the vault was runtime CONTENT stored
inside a template repo. The live vault now lives in `~/.hermes/AI-Second-Brain`, seeded once from the
repo and never overwritten by a re-run; the repo copy is a pure seed (a schema, a README, empty
directories — 13 files, byte-identical on both accounts and untouched since the day they were
created, which is what made the decision easy). `install.sh` no longer deploys or enables
vault-sync, and the units and the deployed script are gone from both accounts. `backup.sh` archives
the vault, because git no longer holds anything resembling what an agent writes there; `rollback.sh`
extracts it *alongside* the live one rather than over it.

Also fixed: vadim_prod's crontab still ran `conductor-monitor.sh` with `HO_DB` pointing at the
pre-migration database inside the project checkout, so the monitor was watching a file the conductor
no longer writes.

### Known, deliberate, not yet done
- One leftover disabled unit file for `hermes-conductor` in the off-profile scope was **removed**
  (it named the pre-rename `DEV/dev-sm` path); `doctor.sh` reports both profiles clean.
