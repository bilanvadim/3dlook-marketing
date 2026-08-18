# Disaster recovery

Ordered by how often it is actually needed. **Read the section before running it** — several of
these discard data, and which data is not always obvious.

Before anything: `./scripts/status.sh` and `./scripts/doctor.sh`. Most "the system is broken" turns
out to be one service down or a tree/database disagreement, both of which they name outright.

## First: is it code or state?

Conflating these is how a bad afternoon becomes a bad week.

| | Cost of rolling back | Command |
|---|---|---|
| **Code** — the tree is on a bad commit | cheap, reversible | `rollback.sh` |
| **State** — queue, memory, secrets, config | **destructive**, opt-in per part | `rollback.sh --queue/--memory/--config` |

Rolling back code loses nothing. Restoring the queue discards every job that ran since the
snapshot; restoring the memory discards everything the agent learned since. `rollback.sh` prints
what will be lost and asks, per part.

## 1. A bad update

```bash
./scripts/rollback.sh            # previous commit, re-render, reinstall deps, restart
```

`update.sh` normally does this itself: a typecheck or test failure rolls back before any restart.
Use this when a problem shows up **after** the restart, or later.

It reinstalls `node_modules` for the commit it returns to — dependencies must match the code, or
the tests pass against a `node_modules` from somewhere else.

## 2. A service will not start

```bash
journalctl --user -u hermes-conductor -n 50 --no-pager     # or without --user; profile says which
./scripts/doctor.sh
```

The three causes seen here, none of which announce itself clearly:

- **Port taken.** Another runtime, or a stray process, holds the port. `doctor.sh` reports who
  owns each of this profile's ports and fails if it is the other account.
- **The unit points at a tree that cannot start.** Missing `node_modules` → `npm start` exits 127.
  `deploy.sh` installs them; check the drop-in as well as the unit, because the drop-in wins.
- **A stale process outside the unit.** A conductor started by hand (nohup) squats the webhook
  port and the managed unit crash-loops with EADDRINUSE. The guard timer handles this; verify it
  covers the current tree path.

## 3. The queue looks wrong — jobs stuck, escalations unanswered

Check the two halves agree on one database **first**:

```bash
./scripts/doctor.sh | head -20
```

A gateway and a conductor on different `ho.db` files produce exactly this symptom and **log
nothing**: every Telegram Approve/Deny writes `approved` into one file while the conductor times
out against another. Both halves are working perfectly, on different databases. That is what
happened on this box, for weeks.

Individual stuck jobs:

```bash
sqlite3 ~/.hermes/ho.db "select id,status,title,claimed_at from ho_jobs
  where status in ('claimed','running','verifying','escalated');"
sqlite3 ~/.hermes/ho.db "select id,job_id,reason,status,created_at from ho_escalations where status='open';"
```

A job whose worker died is recovered automatically after `HO_STALE_RUN_SECS` (default 900 s), which
returns its **step** to pending as well — without that, dependent work stayed blocked and the job
closed itself as failed, losing the work silently.

To release one by hand, prefer answering the escalation (the buttons still work — the row stays
open by design, so a late tap lands) over editing rows.

## 4. Restore the queue from a backup

**Discards every job recorded since the snapshot.** `rollback.sh` prints the delta first.

```bash
./scripts/rollback.sh --from ~/.hermes/backups/<stamp> --queue
```

It stops the conductor first (a live writer and a file swap do not mix), keeps the displaced
database aside as `ho.db.replaced-<stamp>` — restoring a backup is itself an action you may want to
undo — runs `integrity_check`, and starts the conductor again.

## 5. Restore the memory (mem0 / Qdrant)

**Replaces the collection.** Everything learned since the snapshot is gone.

```bash
./scripts/rollback.sh --from ~/.hermes/backups/<stamp> --memory
```

Backups use the Qdrant **snapshot API**, not a copy of the storage directory: the process holds the
segment files open, and a filesystem copy of a live collection restores as a corrupt one.

Verify afterwards: `status.sh` prints the collection status and point count. Green with a plausible
count is the answer; green with 0 means the restore did not land.

## 6. Restore config and secrets

```bash
./scripts/rollback.sh --from ~/.hermes/backups/<stamp> --config
```

Overwrites the live `secrets.env`, `~/.hermes/{.env,config.yaml,mem0.json,SOUL.md,auth.json}`, the
conductor's `.env`, and the proxy configs.

The **vault** is deliberately the exception: it is extracted *alongside* as
`~/.hermes/AI-Second-Brain.restored-<stamp>` rather than over the live one. Overwriting a knowledge
store with an older copy silently deletes whatever was written since, and unlike the queue there is
no count to warn you with. Merge what you need.

If the reason you are restoring is a **leaked or shared** credential, restoring does not close it —
see [`SECRETS.md`](SECRETS.md). Rotate.

## 7. Rebuild one account from scratch

The account is gone, or so far off that repair is slower than rebuilding. Nothing here needs the
other account, and nothing here should touch it.

1. `INSTALL.md` §0–2 — prerequisites, profile (it is already in git), `deploy.sh`.
2. Restore secrets from the newest backup, or re-issue them. A key of unknown history gets
   rotated, not reused.
3. `install.sh` — services, venvs, units, linger.
4. Restore the queue and memory from the backup (§4, §5 above) if that history matters.
5. `doctor.sh` until clean.
6. `backup.sh` — a fresh known-good point.

## 8. Both accounts, or the whole box

The canonical repo is on GitHub, so **config is never the problem**. What is only on this machine:

- the secrets (each account's own)
- `~/.hermes/ho.db` — queue history
- the Qdrant collections — agent memory
- `~/.hermes/AI-Second-Brain` — the knowledge vault (git holds only the empty seed)
- the MTProto session (`session.enc`) — must be re-enrolled interactively by the owner; a forwarded
  login code can never work
- the systemd units and **drop-ins**

All of the above except the MTProto session are in `backup.sh` output. Which is the point of taking
one: a rebuild from git alone gives you a working system with no history and no credentials.

Rebuild order: box prerequisites → clone → per account, §7.

## What to check before calling it recovered

```bash
./scripts/status.sh        # every service active, every assigned port listening
./scripts/doctor.sh        # clean, or every exception understood
./scripts/diff.sh          # no drift; render output only
```

Then one real end-to-end job — `<system> <small task>` — and watch it reach `done` through the
conductor log. A stack that starts is not the same as a stack that works: a queue can be readable,
every service active, and the escalation path still dead because two components disagree about a
file path.
