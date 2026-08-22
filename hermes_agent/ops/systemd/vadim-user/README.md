# Conductor — vadim_prod `systemd --user` deployment

Verbatim mirror of what is live in `~/.config/systemd/user/` on the shared VPS.
Not a template: no `@TOKEN@` placeholders, nothing to render. Copy it in as-is.

## Why this is separate from the units one level up

`../hermes-conductor.service{,.template}` are **system** units — `User=@USER@`,
`WantedBy=multi-user.target`, filled by `install.sh` into `../generated/`. The box
already runs one of those at `/etc/systemd/system/hermes-conductor.service`, and it
belongs to **`sergiy_prod`**. Vadim's conductor is a `--user` instance instead:
`After=default.target`, `WantedBy=default.target`, no `User=`, HOME from the user
manager. Two accounts, one machine, two independent workers. Do not merge these.

## The one rule that will bite you

`systemd.exec(5)`: **`EnvironmentFile=` overrides `Environment=`.** Measured, not
assumed — `systemd-run --property=EnvironmentFile=… --property=Environment=…` on
this box returns the *file's* value.

The base unit loads `conductor/.env` via `EnvironmentFile=`. So any variable that
file sets **beats every drop-in below**, no matter the number prefix. That is
exactly how `DATABASE_URL` broke on 2026-08-22: `.env` had `file:./ho.db`,
`10-deployment-paths.conf` had the correct absolute path in `Environment=`, and the
file won. Worse, systemd resolves a relative `file:` against `WorkingDirectory` —
which drop-in 10 moves to the `/srv` tree — so the worker would have opened a
**0-byte** `ho.db` there while `conductor-monitor.sh` and the gateway both read
`~/.hermes/ho.db`. A conductor polling an empty queue forever, no error anywhere.

Rule of thumb: put anything `.env` also sets **in `.env`**. Use a drop-in only for
keys `.env` does not mention.

## Drop-ins

| File | What it buys | What breaks without it |
|---|---|---|
| `10-deployment-paths.conf` | Runs the `/srv` code tree (it has the libSQL connection-leak fix), queue stays in `~/.hermes/ho.db` | The 3dlook tree's older `store.ts` leaks a connection per transaction — 5.4 GB while polling an *empty* queue, OOM-killed 2026-08-14 |
| `20-profiles-dir.conf` | `HO_PROFILES_DIR` → the tree that actually has `marketing_vb*.json` | Silent: a `marketing_vb_sm` job passes the DB CHECK, logs `no manifest … falling back`, and runs with **none** of the mvb-* plugins. No error, no failed step |
| `30-memory.conf` | `MemoryMax=3G`, `MemorySwapMax=512M` | A leak takes the whole box instead of just this unit. `MemorySwapMax` is the line that protects the neighbouring account |
| `40-snapshot.conf` | `HO_SNAPSHOT_SH` → pre-run `refs/hermes/snapshots/job-<id>` | Autonomous runs get **no rollback point**. Autocommit skips `main`, and Vadim's work is on `main`. Job #90 ran without it |
| `50-webhook-port.conf` | Pins `HO_WEBHOOK_PORT=3001` | Falls back to a hardcoded upstream default. Measured: `:3011` is the other account's runtime, `:3001` is Vadim's — the comment in the `/srv` `.env` claiming the opposite is wrong |

Observed on this box: 91 MB in use, 156 MB peak, against the 3 G cap: it is a runaway detector,
not a diet.

## Install

    U=~/.config/systemd/user
    cp hermes-conductor.service hermes-conductor-guard.service hermes-conductor-guard.timer "$U/"
    mkdir -p "$U/hermes-conductor.service.d"
    cp hermes-conductor.service.d/*.conf "$U/hermes-conductor.service.d/"
    systemctl --user daemon-reload
    systemctl --user enable --now hermes-conductor.service
    systemctl --user enable --now hermes-conductor-guard.timer
    systemctl --user start hermes-conductor-guard.service   # see gotcha 1

### Gotcha 1 — the guard timer needs one manual kick

`hermes-conductor-guard.timer` has only monotonic triggers (`OnBootSec=1min`,
`OnUnitActiveSec=2min`). After a boot long past, `OnBootSec` has elapsed and
`OnUnitActiveSec` has no anchor, so `list-timers` shows `NEXT -` and it **never
fires**. `Persistent=true` does not help — that applies to `OnCalendar` only.
Starting the service once gives `OnUnitActiveSec` its anchor; it then cycles every
2 min. Check with `systemctl --user list-timers hermes-conductor-guard.timer` and
insist on a real `NEXT`.

### Gotcha 2 — the guard is safe, and here is why

It kills rogue `conductor.ts` processes that squat `:3001` (agent-spawned `nohup`
restarts) so the managed unit can bind. Four guards, all required to fire: `comm`
is `node`; cmdline under one of **Vadim's** two conductor dirs (never
`/srv/sergiy_prod/*`); uid 1006; and cgroup does **not** contain
`hermes-conductor.service`. That last one is what protects the managed process.
Dry run it before trusting it: `DRY_RUN=1 …/conductor-guard/hermes-conductor-guard.sh`.

## Verify a live install

    systemctl --user cat hermes-conductor         # all 5 drop-ins listed?
    journalctl --user -u hermes-conductor -n 20   # want: DATABASE_URL → file:/home/vadim_prod/.hermes/ho.db
                                                  #       conductor up. polling…
    # the DB it really opened — the log line can lie, a file descriptor cannot:
    for p in $(pgrep -f 'DEV/dev/conductor.*conductor.ts'); do ls -l /proc/$p/fd | grep ho.db; done

Three consumers share that one SQLite file: this worker, the `conductor-monitor.sh`
cron (`HO_DB=~/.hermes/ho.db`), and the gateway's `claude_switcher.py` (`HO_DB` env
or `~/.hermes/ho.db`). Telegram Approve/Deny does **not** go through the webhook —
the gateway writes the decision straight into `ho_escalations` and the worker picks
it up by polling. Keep all three pointed at the same absolute path.
