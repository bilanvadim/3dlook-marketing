# conductor-bridge — external job intake → Hermes conductor queue

`bridge.py` is a tiny stdlib HTTP service that lets an **external caller** (e.g. a
docker container on the bridge network, such as the MV-Link app) submit a job to
the Hermes conductor without touching the DB directly. It authenticates the
request and `INSERT`s a row into `~/.hermes/ho.db → ho_jobs` — the same queue that
`hermes-conductor.service` drains and the bot's `Dev <task>` uses.

```
external caller ──POST /enqueue (Bearer CONDUCTOR_BRIDGE_TOKEN)──▶ bridge.py ──INSERT──▶ ho_jobs ──▶ hermes-conductor
                 GET  /status/<job_id> ◀── ho_jobs status/result ──┘
```

- Binds the **docker bridge gateway** (`BRIDGE_HOST=172.20.0.1:8790` by default) —
  reachable only by containers on that network, not the public internet.
- Every request must carry `CONDUCTOR_BRIDGE_TOKEN` (constant-time compared).
- Config: `bridge.env` (from `bridge.env.example`, **chmod 600**).

## Run as a service
```bash
cp ops/conductor-bridge/bridge.env.example ~/.hermes/conductor-bridge/bridge.env   # fill + chmod 600
cp ops/conductor-bridge/bridge.py          ~/.hermes/conductor-bridge/bridge.py
# install the unit (edit User=/paths first), then:
systemctl --user enable --now conductor-bridge.service
```

> Historical note: this bridge was built for the MV-Link Mini App (since removed).
> It's kept here as reusable infra for any external system that needs to enqueue
> conductor jobs. Skip it if you don't run an external job producer.
