# Install

Two paths, and picking the wrong one is the usual mistake:

| You have | Use |
|---|---|
| a fresh account, nothing installed | **Full install** below |
| the account already runs the stack, you want newer config | [`UPDATE.md`](UPDATE.md) |
| the tree exists but is not a git checkout, or has no `node_modules` | `scripts/deploy.sh` alone |

Everything runs **as the target account**. Every script refuses to touch a profile that is not
the current user's — the paths in a profile are absolute, so the wrong profile name would rewrite
the other account's runtime, which is the one thing this setup exists to prevent.

## 0. Prerequisites

- Debian/Ubuntu, `sudo` for the account
- `git`, `curl`, `python3` (3.12+), `sqlite3`, `node` 22+, `npm`
- a Telegram bot of this account's own (**never** another account's), from @BotFather
- the account's own provider keys
- `loginctl enable-linger <user>` so user services survive logout — `install.sh` does this

## 1. Add a profile

If the account has no `config/profiles/<user>.vars`, create one from an existing file and change
**every** value. See [`config/README.md`](config/README.md).

The ports are the part to get right. Both runtimes bind the same loopback, so a shared value does
not error — the second service to start silently loses, and its half of the system goes quiet.
That is not a hypothetical: while both profiles defaulted to `3001`, one account's escalation
buttons did nothing for weeks. `scripts/validate.sh` refuses a profile set with any duplicate
port, across profiles *and* across keys.

Commit and push the profile before deploying: `deploy.sh` clones from the canonical remote.

## 2. Deploy the tree

```bash
git clone <canonical-repo> /tmp/bootstrap && cd /tmp/bootstrap
./scripts/deploy.sh <profile>
```

This clones to the profile's destination, renders it, installs the conductor's dependencies, and
writes `conductor/.env` from the profile. It is idempotent — safe to re-run.

Three things it does deliberately:

- **Clones alongside and swaps** if a non-git directory is already there, so a failure at any
  point leaves the old tree intact. (One account's tree was a plain copy with no remote; this is
  the recovery path for that.)
- **Installs `node_modules`.** Their absence is the entire reason one account's unit had to be
  pinned back to an old tree with a drop-in.
- **Never writes credentials**, and leaves an existing `conductor/.env` alone. Silently rewriting
  it is how one account ends up holding another's bot token.

## 3. Secrets

Create `~/.config/ai-agent-stack/secrets.env`, mode **600**, directory **700**:

```bash
install -d -m 700 ~/.config/ai-agent-stack
touch ~/.config/ai-agent-stack/secrets.env && chmod 600 ~/.config/ai-agent-stack/secrets.env
```

Fill it from `secrets.env.example`. Read [`SECRETS.md`](SECRETS.md) first — in particular the rule
that a key which has ever appeared in another account's file is **burned** and must be rotated,
not moved.

## 4. Install the runtime

```bash
./install.sh
```

Installs the Hermes agent and its venv, mem0 + a per-user Qdrant, the two failover proxy chains,
the systemd units, linger, and the Claude Code plugin marketplaces. It reads the secrets file
written above, and prompts for anything missing when run interactively.

Then add the conductor's Telegram credentials, which `deploy.sh` deliberately left out:

```bash
CD=/srv/<user>/ai-agents-config/agents-ai/telegram-bot-agent/claude-code-agent/DEV/dev/conductor
printf 'TELEGRAM_BOT_TOKEN=%s\nTELEGRAM_CHAT_ID=%s\n' "<this account's token>" "<chat id>" >> "$CD/.env"
chmod 600 "$CD/.env"
```

## 5. MTProto session (optional)

Only needed for reading this account's own Telegram history. Interactive, and it must be run **by
the account owner at their own terminal**:

```bash
~/.hermes/mtproto/enroll.sh
```

Telegram invalidates a login code that has been **forwarded** — including forwarded to you by the
account owner. A code relayed through anyone else can never work, no matter how fast. The owner
types it themselves or the enrolment fails.

## 6. Verify

```bash
./scripts/status.sh    # what is running
./scripts/doctor.sh    # what is quietly wrong
```

`doctor.sh` must be clean, or the exceptions must be understood. It checks the things that produce
no error message: the gateway and the conductor resolving the same `ho.db`, the unit and the
running process agreeing on a tree, no duplicate unit in the other systemd scope, ports held by
this account, no secret shared with the other account, the tree fully rendered, and the pre-run
snapshot actually wired.

End-to-end test, which exercises the queue, the SDK session, the breaker and the Telegram path in
one go:

```
<system> <a small task>        # e.g.  dev  add a line to README and stop
```

Watch it: `journalctl --user -u hermes-conductor -f` (or without `--user` where the conductor is a
system unit — the profile records which).

## 7. First backup

```bash
./scripts/backup.sh
```

Captures what git does not have: secrets, live Hermes config, the queue, the unit files
**including drop-ins**, and the vector memory. Do this before the first real job, so there is a
known-good point to return to.

## Then

Updates are [`UPDATE.md`](UPDATE.md). Do not `git pull` by hand: a deployed tree carries render
output as local modifications, and `update.sh` is what distinguishes that from real drift before
discarding anything.
