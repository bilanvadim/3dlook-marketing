# Update

```bash
./scripts/check-update.sh      # is there anything new?   (exit 0 current · 3 available · 1 unknown)
./scripts/update.sh            # apply it
```

That is the whole normal path. Both are safe to run at any time, as the account itself.

## Where to make changes

Both `/srv/*/ai-agents-config` trees are **runtime replicas**. Do not edit or commit in them: a
commit there is invisible to the other runtime and is discarded by the next `update.sh` reset, and
a saved half-finished edit becomes the live config immediately, because Claude Code and the
conductor read those files on their next call.

```
edit + commit + push   /srv/sergiy_prod/ai-agents-config-dev     ← development checkout
        │
        ▼
./scripts/update.sh    /srv/<user>/ai-agents-config              ← each runtime pulls it
```

A `pre-commit` hook in each runtime tree refuses commits and names the dev checkout
(`--no-verify` overrides it if you genuinely mean to). `deploy.sh` installs the hook.

## Do not `git pull` by hand

A deployed tree is **never** `git`-clean: the template names nobody (`@DEST@`, `@HOME@`, `@USER@`)
and `render.sh` rewrites those with this profile's paths, so ~24 files always show as modified. A manual `git pull` therefore either conflicts or,
worse, succeeds and leaves a half-rendered tree pointing partly at another account's paths.

`update.sh` handles this by discarding the render output and regenerating it. That is safe for one
specific reason: those modifications are **reproducible output**, not work. `diff.sh` is what
proves the claim before anything is discarded — it re-renders the pristine blob from git and
compares, so it can tell **render** from **drift**.

If drift exists, `update.sh` **stops and lists it** rather than throwing it away. Look at it
(`diff.sh <profile> --full`), then either get the change committed upstream where it belongs, or
re-run with `--force` to discard it deliberately.

## What update.sh does, in order

```
backup → reset → pull → render → deps → VERIFY → restart → doctor
                                           ↑
                            failure here rolls back and stops
```

1. **pre-flight** — refuses if there is drift (without `--force`); refuses if a *consumer* tree
   carries local commits, because the reset would destroy them; warns if jobs are in flight (they
   survive — durable resume re-claims them with their session id).
2. **backup** — full `backup.sh`. No backup, no update.
3. **reset + pull** — `--ff-only`. `git clean` is **never** used, in any form: untracked files
   here are the runtime (`conductor/.env` holds the DB path and Telegram credentials,
   `node_modules` is ~300 MB). `reset --hard` leaves both alone.
   From this point until the render, the tree is in **template form** — literal `@DEST@` paths —
   and a live runtime resolves those on its next call. An `EXIT` trap re-renders on any exit path
   until step 4 clears it, so a failed pull cannot leave the tree unusable.
4. **render** for this profile.
5. **deps** — `npm ci` only if `package-lock.json` moved.
6. **verify** — typecheck plus the full conductor suite (113 assertions), **before** any restart.
   A broken conductor that is still running is a far better place to be than one restarted into a
   crash loop. Failure here rolls the tree back, re-renders, restores dependencies, and stops.
7. **restart** — only what the diff touched: conductor for conductor changes, gateway for
   SOUL/skills/ops changes. Then confirms they came back.
8. **doctor** — post-update health. Failures here are reported with the rollback command.

## Options

| Flag | Effect |
|---|---|
| `--dry-run` | walks every stage, changes nothing |
| `--force` | discard real drift; also re-render/re-verify when already up to date |
| `--no-restart` | apply everything, leave the services on the old code (you restart later) |

## The script updates itself

If a pull contains a new `update.sh`, `lib.sh` or `diff.sh`, the run hands off to the **new** copy
with `--resumed-after-pull` and it finishes the remaining stages.

This exists because a self-updating script cannot otherwise deliver the fix for its own bug. It
happened twice in one afternoon: a bug in the drift detection made `update.sh` abort on a clean
tree, and the fix was in the exact commit it was refusing to pull. Both times the only way out was
running reset/pull/render by hand — the one thing this script exists to remove.

## Bootstrapping a tree that is too old

A checkout predating the scripts cannot run them. Once, by hand:

```bash
cd /srv/<user>/ai-agents-config
git reset -q --hard HEAD && git pull -q --ff-only origin main
./scripts/render.sh <profile>
```

`reset --hard` discards render output only; `.env` and `node_modules` are untracked and survive
(verify: they are still there afterwards). From then on `update.sh` maintains itself.

## When something went wrong

```bash
./scripts/rollback.sh                 # previous commit, re-render, restart  ← start here
./scripts/rollback.sh --to <commit>   # a specific commit
```

Code rollback is cheap and reversible. Restoring **state** — the queue, the memory, the secrets —
is not, and is opt-in per part. See [`DISASTER-RECOVERY.md`](DISASTER-RECOVERY.md).

## Automating the check

Notify, do not auto-apply. An update can restart the conductor, and choosing the moment is worth a
human. `check-update.sh` is built for this: it only fetches, and answers via exit code.

```
*/30 * * * * cd /srv/<user>/ai-agents-config && ./scripts/check-update.sh --quiet || \
             [ $? -ne 3 ] || echo "config updates available on $(hostname)" | <notify>
```

## What CI already guaranteed

Every commit on `main` has passed `scripts/validate.sh` — the same script you can run locally —
plus a render of **every** profile from a clean copy, asserting the render is idempotent and that
the author's account name never survives into another profile's tree. So `update.sh`'s own
verification step is a second, machine-specific opinion, not the first one.
