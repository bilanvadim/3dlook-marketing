# Secrets

**Nothing in this file's subject matter belongs in git. Not once, not temporarily, not in a
branch.** Git keeps history; a secret committed and then removed is still published.

## Where they live

`~/.config/ai-agent-stack/secrets.env` — file **600**, directory **700** — is **the source of
truth**. `install.sh` reads it and distributes the values into files the services actually read:

```
secrets.env  ──install.sh──▶  ~/.hermes/.env
                              ~/.hermes/ai-models.env
                              ~/.hermes/mtproto/creds.env
                              ~/.hermes/telegram-userbot/.env
                              ~/.hermes/conductor-bridge/bridge.env
```

**Those five are generated. Edit the source, never a copy.** Nothing enforces that at the
filesystem level, so `doctor.sh` compares every shared value between the source and the copies by
hash and fails on divergence — when they differ, the running system keeps using the copy while the
source says something else, and the next `install.sh` silently reverts the live value. Neither
direction produces an error.

`install.sh` resolves the source in this order: `--secrets <path>`, then the XDG store above, then
the legacy `<repo>/secrets.env`. The XDG path comes first because the in-kit default puts a file
full of API keys **inside a git checkout** — gitignored, but surviving on that one line, in a tree
that `update.sh` resets and `deploy.sh` clones-and-swaps.

Nothing is in git, ever: `*.env` is ignored repo-wide and only `*.example` templates are tracked.

Per-user profile values are **not** secrets and must be tracked, which is why they are
`config/profiles/*.vars` and not `.env` — that extension is gitignored, and naming them `.env`
made `git add config/` skip them **silently**. The commit looked right and the clone had no
profiles at all.

## The one rule

**Never copy a home directory, a config file or a credential between accounts.** Not to "save
time", not to compare, not as a starting point.

Specifically never: API keys, Telegram bot tokens, MTProto credentials, Claude auth, OAuth tokens,
cookies, OpenCode credentials, GitHub PATs, SSH private keys, shell history, conversations,
memories, the runtime DB, logs, PIDs, sockets, caches, session files.

This is not caution in the abstract. On this box an old cross-user config copy left **one
account's Google key serving as the other account's proxy gate**. Nothing was broken, nothing was
logged, and it was found only by hashing keys and noticing two matched. Undoing it required
rotating the key, not editing a file.

`doctor.sh` compares the two accounts' stores key by key **by hash**, so a match can be reported
without ever printing a value. Run it as each user; neither can read the other's file, and that is
correct.

## A shared key is burned

If a credential has ever existed in another account's file — even briefly, even by mistake —
**rotate it**. Moving it, deleting the copy, or "putting the right one back" does not undo it:
you no longer know what read it in the meantime.

The rotation that was actually done here, as a template:

1. **Verify the new key works first**, with a real call, *before* swapping anything. A rotation
   that installs a dead key turns one problem into an outage.
2. Enumerate every place the old value appears — count it, do not assume. It was in
   `~/.hermes/.env` under **two** different variable names and in `opencode/auth.json`. Since the
   generated copies are separate files, "changed it in secrets.env" is not the same as rotated.
3. Swap all of them, then re-scan every file for the old value and confirm zero.
4. Restart the consumers, verify with a real call again.
5. Only then delete the old key at the provider. Confirm the old value now returns **401** — that
   is the proof the rotation happened, not that the new one works.

## Never print a secret

Not to a terminal, not to a log, not into a commit message, not into a Telegram message. To
compare or identify, use a short hash:

```bash
printf '%s' "$value" | sha256sum | cut -c1-8
```

Every script here follows this: `backup.sh` copies secret files but never echoes them, `doctor.sh`
compares hashes, and masked output prints `<set>` for presence.

## Permissions

```bash
chmod 700 ~/.config/ai-agent-stack
chmod 600 ~/.config/ai-agent-stack/secrets.env ~/.hermes/.env
```

Never `chmod 777`, never world-readable, never `chown -R` across a home directory. `doctor.sh`
checks these modes.

## Telegram specifics

Each account has **its own bot**. Two runtimes must never share a token: Telegram allows exactly
one `getUpdates` consumer per token, so a shared bot makes both sides lose updates at random.

**A login code that has been forwarded is dead.** Telegram invalidates codes that were shared —
including a code the account owner forwards to you to "speed things up". Established the hard way:
four codes in a row failed, and the cause was not expiry but the forwarding itself. The owner must
type the code at their own terminal. Do not ask anyone to relay one.

## Backups contain secrets

`backup.sh` writes `~/.hermes/backups/<stamp>/` at **0700**, files **0600**, and says so in the
manifest. It is **not encrypted** — encrypting to a key stored on the same box buys nothing. If you
copy a backup off the machine, encrypt it before it leaves.

## Public-repo hygiene

`validate.sh` greps the tree for token **shapes**, not variable names — a variable called `FOO` can
still hold a bot token. Bot tokens, `sk-` keys, `ghp_`/`gho_` tokens and `AIza…` keys all fail the
build outside `*.example`.

If a secret does reach a public repo: rotate first, then clean history. In that order. Two repos
here needed exactly that, and rotation is what actually closed the exposure — the history rewrite
only stopped it getting worse.
