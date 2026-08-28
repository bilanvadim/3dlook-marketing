# There must be no ho.db in this directory

This is the conductor's `WorkingDirectory`, and `DATABASE_URL=file:./ho.db` — the value
this unit shipped with until 2026-08-22 — resolves relative to it. systemd expands that
against WorkingDirectory, so when a drop-in moved the runtime the worker opened a
DIFFERENT database from the one the gateway and the cron monitor were reading: a conductor
polling an empty queue forever, with no error anywhere.

The unit's DATABASE_URL is absolute now (`file:%h/.hermes/ho.db`, in
10-deployment-paths.conf), and `EnvironmentFile=` overrides `Environment=`, which is why
the value in conductor/.env must stay absolute too.

A file called `ho.db` here is a loaded gun regardless: it only takes one relative path,
one `cd`, or one tool defaulting to `./ho.db`. The 802 KB one that used to sit here held
77 jobs from before the 2026-08-12 repoint and was moved to
`~/.hermes/archive/ho.db.pre-repoint-20260812` on 2026-08-28.

Queue state belongs in `~/.hermes/`, never inside a project checkout — a repo gets cloned,
moved and cleaned, and queue history must not travel with it.

`bootstrap/verify.sh` (D1) warns if a database reappears here.
