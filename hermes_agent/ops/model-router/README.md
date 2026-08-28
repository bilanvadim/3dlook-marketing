# Only `router_lib.py` is live here

The model-router — the thing that probed provider catalogues every morning and wrote the
winner into `~/.hermes/config.yaml` — was **deleted on 2026-08-26**. Model choice lives
exclusively inside llm-failover-proxy now, which knows what is alive per REQUEST rather
than once a day. See `llmfp_proxy/README.md`.

| file | status |
|---|---|
| `router_lib.py` | **LIVE.** Shared helpers (`telegram()`, `restart_gateway()`, `env()`) imported by `hermes-update.py` and `llmfp-morning-agent.sh`. `hermes-update.py` syncs THIS FILE ONLY into `~/.hermes/model-router/`. |
| `refresh.py`, `free_providers.py`, `*.json` | **RETIRED.** The selector itself, kept for reference. Nothing runs them. |

## Why the sync is one file and not this directory

`hermes-update.py` used to copy the whole directory every morning. With the selector
deleted from the runtime but still present here, that copy would have **resurrected it
from git on the next update** — two systems each believing they know which model is alive
today, which is the exact arrangement the proxy exists to replace. The updater now names
`router_lib.py` explicitly; do not widen it back to a glob.

## Do not re-enable

If a future change wants a morning model decision, it belongs in the proxy's list system
(`llmfp use`, and the paranoid `llmfp-morning-agent.sh` that verifies the switch actually
took), not here. `refresh.py` also reads `~/.hermes/ai-models.env`, a credentials file that
exists only to feed thirteen direct provider keys the proxy made unnecessary.
