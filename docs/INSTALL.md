# Install — from a bare machine to a working system

For a fresh VPS. If you are recovering an existing one, read [RECOVERY.md](RECOVERY.md)
first: the order is different and the queue database needs care.

## Short version

```bash
git clone https://github.com/bilanvadim/3dlook-marketing.git
cd 3dlook-marketing
./bootstrap/install.sh --dry-run     # read what it will do
./bootstrap/install.sh
```

Then do the three things a script cannot do (below), and re-run `install.sh`. It is
idempotent — running it twice on a healthy machine changes nothing.

## What the machine needs first

* **Linux with systemd, and a `--user` session that survives logout.** The
  installer refuses to continue without it, because every service here is a
  `systemd --user` unit:
  ```bash
  sudo loginctl enable-linger $USER
  ```
* `git python3 node npm sqlite3 curl jq` — the installer offers to `apt-get` them.
* Node ≥ 18. The conductor builds `better-sqlite3`, a native module.

## The three manual steps

The installer reports each as a warning with the exact command rather than
pretending to have done it.

**1. Claude Code.** Needs an interactive OAuth login against a Max/Pro
subscription. No `ANTHROPIC_API_KEY` — the conductor authenticates with the
ambient subscription credentials.
```bash
sudo npm i -g @anthropic-ai/claude-code
claude          # then: /login
```
Worth knowing before you plan work: the conductor uses **the same usage window as
your interactive sessions**. One autonomous run can lock you out of your own
terminal, which is why the social pipeline fans out into one job per profile
instead of one big run.

**2. Hermes Agent.** The gateway is a third-party package, installed rather than
vendored here. Install it, then `hermes auth` if your provider needs it.

**3. Secrets.** `install.sh` copies `secrets.env.example` to
`~/.config/ai-agent-stack/secrets.env` (mode 600) and never overwrites it. Fill it
in. Every key is documented in the example with what breaks without it. The two
that stop Telegram from connecting at all:
```
TELEGRAM_BOT_TOKEN=      # from @BotFather
TELEGRAM_ALLOWED_USERS=  # your numeric Telegram user id, comma-separated
```

## What the installer actually does

1. Checks OS, systemd and the `--user` session.
2. Installs missing packages (apt only; anything else it tells you and stops).
3. Creates `~/.hermes`, `~/.hermes/logs`, `~/.config/ai-agent-stack` (700).
4. Creates `secrets.env` from the example if absent. **Never overwrites.**
5. `npm install` in the conductor, if `better-sqlite3` is not already built.
6. Copies systemd units and drop-ins from
   `hermes_agent/ops/systemd/vadim-user/` into `~/.config/systemd/user/`,
   then `daemon-reload`. **Copies, not symlinks** — a `git checkout` of a branch
   without those files would otherwise pull a unit out from under a running
   service.
7. Rewrites only its own crontab block, between markers. Your other entries
   survive untouched.
8. Marks scripts executable.
9. Enables and starts `hermes-gateway` and `hermes-conductor`.
10. Runs `bootstrap/verify.sh`.

It never touches `~/.hermes/ho.db`. Queue state belongs to the machine, and
clobbering a live queue during what is also the repair tool would be the worst
failure this script could have.

## Verifying

```bash
./bootstrap/verify.sh
```
`SYSTEM READY` and exit 0 means every check passed. Exit 2 means warnings —
usually unfilled secrets or a missing Claude Code login. Exit 1 means something is
actually broken; read the `[FAIL]` lines.

Then prove the whole chain, not just that services are up:
```bash
~/.hermes/mtproto/venv/bin/python bootstrap/e2e-telegram.py \
    --send "Відповідай рівно одним рядком: INSTALL-OK" --expect "INSTALL-OK"
```
This needs an enrolled MTProto session (`~/.hermes/mtproto/enroll.sh`, interactive
— Telegram sends a login code). Without it, send a message from your phone
instead; the point is the same.

## Choosing a profile

Claude Code hosts several mutually exclusive systems, one active at a time.
Available: `dev`, `marketing`, `marketing_vb`, `marketing_vb_sm`, `sandbox_sm`,
`security`, `seo`. Marketing pipelines run under **`marketing_vb_sm`**, and
`mvb-run.py` sets it per job — you do not switch profiles by hand for those.

## After install

- [CONFIGURATION.md](CONFIGURATION.md) — what lives where, and why nothing is
  edited in place at runtime.
- [TELEGRAM.md](TELEGRAM.md) — how to actually drive the system.
- [TROUBLESHOOTING.md](TROUBLESHOOTING.md) — the failure modes that have really
  happened here.
