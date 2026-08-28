# llm-failover-proxy — the single model selector

Everything that answers as "Hermes", every vision read, every mem0 embedding, the inline
approval judge and the whole OpenCode fallback resolve through the two loopback instances
described here. It is the most load-bearing configuration in the stack, and until
2026-08-28 it existed on exactly one machine, with no template, no unit and no installer
step anywhere in git.

## Why one selector

Hermes used to carry its own model-router that probed provider catalogues each morning and
wrote the winner into `config.yaml` — into `model.default`, `model.provider` and
`fallback_providers`, i.e. over the very keys that point at this proxy. It was deleted
2026-08-26. Two systems that each believe they know "which model is alive today" diverge,
and the proxy knows it per REQUEST rather than once a day. So: **the config always asks for
`auto`, and what stands behind `auto` is the proxy's business.**

Never write a concrete model name into `model.default` / `model.provider` / `model.base_url`,
and never add `model.model` — it overrides `model.default`. Doing it once took the channel
down with HTTP 503, because the name written did not exist at that provider.

## Layout

    ~/.config/llm-failover-proxy/
      .env                    the ONE keys file (0600) — OPENCODE/OPENROUTER/NVIDIA + GEMINI
      agentic/config.json     127.0.0.1:47831  everyday Hermes, vision, embeddings, judge
      agentic/.env            -> ../.env
      strong/config.json      127.0.0.1:47832  coding agent (OpenCode) + Hermes heavy mode
      strong/.env             -> ../.env

**Each instance MUST have its own directory.** `daemon.json`, `daemon.log` and
`<config>.stats.json` are written next to the config file, so two configs in one directory
share one `daemon.json` and `llmfp doctor|stop|restart --config agentic` then reports — and
acts on — whichever instance wrote it last. Measured on this box: `doctor` for the agentic
config printed the strong instance's port, so a restart meant for the chat chain would have
stopped the coding chain, and `Restart=on-failure` does not bring back a clean stop.

Install these templates by copying them into place and substituting:

| token | this machine | why it is a token |
|---|---|---|
| `@AGENTIC_PORT@` | `47831` | the VPS is shared; 47821/47822 belong to the other account |
| `@STRONG_PORT@`  | `47832` | same |
| `@LLMFP_LOCAL_KEY@` | generated per install | a local credential, but never committed |

## Keys

Referenced as `env:OPENCODE_API_KEY`, `env:OPENROUTER_API_KEY`, `env:NVIDIA_API_KEY`,
`env:GEMINI_API_KEY` — **never inline**. Until 2026-08-27 all three provider keys sat inline
in both configs and were frozen into nine `.bak-*` files beside them, so rotating one key
meant editing eleven files and the old value stayed on disk regardless.

Resolution order: real environment variables first, then the `.env` beside the config. The
systemd units therefore load `~/.config/ai-agent-stack/secrets.env` as an `EnvironmentFile`,
which is how `GEMINI_API_KEY` reaches the proxy — and is the first thing on this machine to
actually consume the documented "single source of secrets".

## The five lists

A list is an ORDERED failover chain, retried top-down on every request.

| list | served as | for |
|---|---|---|
| `for agent AI` | `auto` (active on agentic) | everyday Hermes conversation |
| `Reasoning ai models` | `auto` (active on strong) | code, heavy mode, OpenCode |
| `Vision` | `auto - Vision` | `auxiliary.vision` — image reading |
| `Embedding` | `auto - Embedding` | mem0 vectors, 3072 dims |
| `Judge` | `auto - Judge` | `auxiliary.approval`, inline, `max_tokens=16` |

`auto - <name>` serves that chain **without switching** the active list the conversation
shares. This requires llmfp **>= 1.9**; the 1.8.0 this box ran until 2026-08-27 had no such
addressing at all, which is why vision went straight to a pinned OpenRouter model and
embeddings straight to Google.

Run llmfp from `~/.local`, not the global `/usr/lib` install: `/usr` is root-owned and
shared with the other account, so upgrading it would change their stack too.

## Rules each list follows, and the failure each rule prevents

* **Vision** entries are verified by sending a real PNG and requiring the colour back.
  Catalogue capability flags are provider self-description; a text-only model answers 400 and
  Hermes silently "sees" nothing. Give reasoning models room: at `max_tokens=20`
  `gemini-3-flash-preview` returned EMPTY and looked incapable, at 400 it answered.
* **Embedding** entries all return **3072** dims, matching the live `hermes_mem0` collection.
  Never mix dimensions in one chain — Qdrant rejects the odd size per request, so failover
  becomes failure. Changing the embedding model means a NEW collection.
* **Judge** entries are measured at `max_tokens=16`, the judge's real budget, and must return
  one word. A reasoning model spends those tokens thinking and returns empty content, which
  turns every flagged command into an ESCALATE — a dead stop in a headless gateway.
* **Chain order is by measured success, and the top three span three providers.** Health is
  not the same as `enabled`: on 2026-08-27 slot 1 was 1-for-88 and permanently benched while
  slot 3 answered 3.6% of the time and, being the hedge target at `hedgeDelayMs 5000`, made
  nearly every request pay for a 429 first. The morning job reported "провайдеров: 3" every
  day throughout. It now also counts models with a recent success and no active cooldown.
* **Dead means deleted, sick means demoted.** `z-ai/glm-5.2` returns HTTP 410 Gone (EOL
  2026-08-21) and can never recover — removed. `openai/gpt-oss-20b:free` moved behind payment
  while `auxiliary.free_only` is true — removed. Models that merely fail often are pushed to
  the tail, because they do sometimes answer.

## `autostart.json` is disabled on purpose

`llmfp enable` writes a login entry, and afterwards ANY `llmfp` CLI call may spawn the
detached daemon it names. Here that daemon ran a frozen snapshot against a config path that
no longer existed, found 47831 taken, and bound **47832** — the strong port — pushing the
real strong instance to 47833. Hermes' heavy mode and all of OpenCode then spoke to an
orphan running old code for 21 hours, with nothing logged. systemd owns both lifecycles;
a login entry beside it is a second owner that binds whatever port is free.

Signature, if it recurs: a node process whose cgroup is a `session-*.scope` instead of a
`*.service`, and a `daemon.json` whose port does not match `server.port` beside it.
