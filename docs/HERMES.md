# Hermes — the manager half

Entry point for the Hermes side. Per-component detail lives beside the component:

- [`agents-ai/telegram-bot-agent/hermes-agent/README.md`](../agents-ai/telegram-bot-agent/hermes-agent/README.md)
- [`.../SETUP.md`](../agents-ai/telegram-bot-agent/hermes-agent/SETUP.md) · [`.../CONFIG.md`](../agents-ai/telegram-bot-agent/hermes-agent/CONFIG.md) · [`.../MODEL-ROUTER.md`](../agents-ai/telegram-bot-agent/hermes-agent/MODEL-ROUTER.md)
- [`.../SOUL.md`](../agents-ai/telegram-bot-agent/hermes-agent/SOUL.md) — the persona, and the rules the agent obeys

## The parts

| | |
|---|---|
| **gateway** | Telegram front end. Owns the bot's single allowed `getUpdates` consumer, routes messages, runs the switcher |
| **mem0 + Qdrant** | per-user memory; a Qdrant instance per account on its own loopback ports |
| **model-router** | picks today's models, writes them where the gateway and the switcher read them |
| **llm-failover-proxy** | two OpenAI-compatible chains — *agentic* (default) and *strong* (heavy mode) — each failing over across providers |

Hermes is a **manager, not a coder**: it plans and delegates, and the executor is Claude Code.
`SOUL.md` states that, and it is the file `hermes update` most likes to reset — which is why
`hermes-update.py` re-applies it from this repo after every update.

## Template versus runtime

The repo holds templates; the runtime is `~/.hermes`, and it is **generated**:

```
repo template  ──install.sh──▶  ~/.hermes/{config.yaml, mem0.json, SOUL.md, .env, …}
secrets.env    ──install.sh──▶  ~/.hermes/.env, ai-models.env, mtproto/creds.env, …
```

Edit the source, never a generated copy. `doctor.sh` compares the secret source against its copies
by hash, because when they diverge the running system keeps using the copy while the source says
otherwise and the next `install.sh` silently reverts the live value — no error in either direction.

Identity tokens (`@OWNER@`, `@GH_OWNER@`, `@PROJECT_ROOT@`) are substituted at this deploy step, by
`install.sh` and then by `hermes-update.py`'s `_render_identity()` on every update. They are
**not** `render.sh`'s job — `hermes-update.py` holds `("@OWNER@", "HERMES_OWNER")` as *code*, so a
tree-wide substitution rewrites the renderer's own token table.

## Escalation: how a decision reaches a running job

The conductor opens a row in `ho_escalations` and pushes a Telegram message with buttons. Tapping
one hits the gateway's `ho:` branch, which writes the decision **straight into the conductor's
database** — `HO_DB`, defaulting to `~/.hermes/ho.db`. There is no HTTP hop in that path; the
conductor's webhook is a second, independent route for standalone runs.

So both halves must resolve the **same file**. When they do not, every tap writes `approved` into
one database while the conductor times out against another, and **nothing is logged** — both sides
are working perfectly, on different files. `doctor.sh` checks this first for that reason.

Escalations never expire: the row stays `open`, so a late tap still lands and the job parks and
re-asks rather than dying. "Approve" on a *breaker* escalation means **continue**, not "it is done"
— only the agent's own result event may mark a job done.

## Models: chains, not per-call keys

Everything model-facing goes through the two loopback chains, so provider choice is one config
file rather than a setting in five places. The Claude → **OpenCode** fallback works this way too:
`opencode-zen` is a *provider inside both chains*, reached over HTTP. Nothing shells out to an
`opencode` binary, and its presence or absence on a box is irrelevant to the fallback.

Ports are per-profile. Both runtimes bind the same loopback, so a shared value does not error — the
second binder simply loses and its half goes quiet.

## Per-account, never shared

Its own Telegram bot (Telegram allows exactly one `getUpdates` reader per token, so a shared bot
makes both sides lose updates at random), its own Qdrant and memory, its own MTProto session, its
own queue, its own keys. See [`../SECRETS.md`](../SECRETS.md) — a credential that has existed in
another account's file is burned and must be rotated, not moved.

## Checks that apply here

```bash
./scripts/status.sh     # services, assigned ports, queue counts, memory point count
./scripts/doctor.sh     # gateway↔conductor agree on one db; secrets source vs copies; ports; scope
```
