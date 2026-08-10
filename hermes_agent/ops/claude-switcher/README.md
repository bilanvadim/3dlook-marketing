# claude-switcher — per-tab Hermes ↔ Claude, with autonomous systems

One Hermes bot, many isolated **tabs**. A tab is a Telegram DM **topic** (native
`/topic` mode): the root DM is a lobby, each topic is an independent session
keyed on **`(chat_id, thread_id)`**. In every tab a two-button bottom bar
(auto-shown on the first message) chooses who works there:

| Button / command | Effect (for the current tab) |
|---|---|
| **🤖 Claude** (`/claude`) | a **plain Claude Code chat** (Termius-like), in the tab's repo |
| **📇 Hermes** (`/hermes`) | the manager (default) — see *systems* below |
| `/cwd [path\|name]` | bind this tab to a project folder (repo); no arg = show + list |
| `/tabs` | pin the two-button bottom bar |
| `/heavy` | borrow **today's strong model** for a hard task (this tab only) |
| `/normal` | back to the everyday free model |

## Claude tab
Plain Claude Code (`claude -p --resume`) in the tab's repo — text, transcribed
**voice** and **screenshots** all go straight to it, reply comes back. It runs
shell itself, so it doubles as a terminal. Per-tab `--resume` session + per-tab
cwd (`/cwd`, or auto-guessed from the first message against `~/workspaces`).

## Hermes tab + systems (autonomous conductor)
Plain text → the normal Hermes manager. Prefix a message with a **system
keyword** to launch that system's **full autonomous cycle** via the conductor
(non-blocking):

| Type | Runs |
|---|---|
| `Dev <task>` | `full_stack_sm` — full-stack A→Z (plan → architect → build → verify → security) |
| `Marketing <task>` | `marketing_sm` |
| `SEO <task>` | `seo_sm` |
| `Security <task>` | `security_sm` |

(Keyword must be at the **start**; RU synonyms accepted, e.g. `Маркетинг`,
`Безопасность`.) The task becomes a `ho_jobs` row (profile + the tab's repo as
`work_dir` + an autonomous A→Z brief, `_entry_prompt`); the bot replies `🚀 job
#N` immediately and never blocks. The live `hermes-conductor.service` claims and
runs it. **Follow-ups in that tab** are routed to the job: an open architect
question is answered; an open escalation takes `approve/deny/abort` (also inline
`ho:*` buttons pushed by `conductor-monitor.sh`); otherwise it reports progress.
When the job reaches a terminal state, the next `Dev <task>` starts a new one.

## Heavy mode (`/heavy` · `/normal` · `csw:hv:*`)

Hermes runs on the strongest FREE model that can SEE (screenshots arrive in
Telegram), which is necessarily a small model. The morning model-router separately
picks a genuinely strong model for the backup coder (`pick.json` → `.coder` +
`.coder_provider`); heavy mode lends Hermes that model for one hard task.

- **Leaves on its own, unasked.** `maybe_auto_return` judges every message while
  heavy mode is on and drops back to the everyday model when the task stops
  developing: a substantive message sharing almost nothing with the running task
  (topic changed), 30 min without anything on-topic, or a 12-turn ceiling. Short
  acks («ок», «спасибо») never flip it by themselves but do age the idle timer, and
  the task fingerprint drifts with the conversation so long threads stay on the
  strong model. Asking each time would leave the capped strong model on whenever
  the question went unanswered. Switching the tab to the Claude chat also returns.
- **Offered, never silent.** `maybe_offer_heavy` fires on the plain-Hermes
  fall-through when the message looks hard (intent verbs like «спроектируй /
  разберись / отрефактори», or a brief ≥320 chars), at most once an hour per tab,
  and only OFFERS — an inline button does the switch. The `vps-orchestration`
  skill also tells Hermes to offer in words and to ASK before switching back; the
  deterministic offer exists because the everyday model is small and forgets.
- **Per-session override, no restart.** `_apply_override` writes
  `runner._session_model_overrides[session_key]` and calls `_evict_cached_agent`,
  the same seam `/model` uses, so the next turn is built on the new model with the
  session and its history intact. Rewriting `config.yaml` instead would need a
  gateway restart — Hermes would be killing the conversation it is answering.
- **Deliberately not persisted.** The api_key travels in memory only, so heavy
  mode dies on a gateway restart and the resting state is always the cheap
  everyday model.
- **Provider name mapping.** The router speaks models.dev ids (`google`,
  `openrouter`, `nvidia`); Hermes' own registry calls the first one `gemini` and
  has no `openrouter` at all — that one goes through the generic `openai-api`
  provider plus a `base_url`. See `_HERMES_PROVIDER`.
- Keys are read from `~/.hermes/ai-models.env` then `~/.hermes/.env`, the same
  order the router uses, so a key added for the coder powers heavy mode too.

## Forward-picker (lobby forwards → a tab)
Forward a client message straight into a topic and it lands in that tab.
Forwards that hit the **lobby** are caught (`run.py` intercept before the lobby
reminder, `maybe_handle_forward_in_lobby`): the bot detects the forward
(`raw_message.forward_origin`) and offers inline buttons for the chat's
**working tabs** — Claude tabs and tabs with a live conductor job, labelled
`📂 <repo> · <mode>` (`csw:fwd:<thread>:<token>`, `✖ Не надо` =
`csw:fwdx:<token>`). Tapping routes the forwarded text into that tab: a Claude
tab runs it as a turn (`_run_turn`); a job tab feeds it to the conductor
(`_handle_conductor_turn`). Payload held one-shot in `_PENDING_FWD`; the runner
is recovered via `adapter._message_handler.__self__`.

## State
`~/.hermes/claude-switcher-state.json`, per tab key:
`{claude: bool, cwd: path, sids: {sub: sid}, jobs: {profile: jid}, bar: bool}`.

## How it's wired
- **`claude_switcher.py`** — all logic + state.
- **`apply-claude-switcher-patch.py`** — idempotent anchor patch: CommandDefs
  (`/claude /hermes /tabs /cwd`) in `commands.py`; call-outs in `gateway/run.py`
  (command dispatch + primary/queued turn intercepts + forward-picker before the
  topic-lobby reminder); `csw:*` + `ho:*` callback branches in the adapter.
  MARKER-guarded; exits 2 if an upstream anchor moved.
- **`hermes-update.py`** re-applies it after each `hermes update` and alerts on drift.

## Config (env)
| Env | Default | Meaning |
|---|---|---|
| `HERMES_CLAUDE_SWITCHER_WORKDIR` | `/home/vadim_prod/workspaces` | default cwd + project-name search root |
| `HERMES_CLAUDE_SWITCHER_MAX_TURNS` | `40` | Claude chat `--max-turns` |
| `HERMES_CLAUDE_SWITCHER_TIMEOUT` | `900` | Claude chat per-turn timeout (s) |
| `HERMES_CONDUCTOR_MAX_TURNS` | `300` | conductor job `max_turns` |
| `HERMES_CLAUDE_BIN` | `$(which claude)` | claude binary |

## Conductor
The autonomous conductor (`hermes-conductor.service`, `ho.db`) runs the system
jobs. Ops: `conductor/RUNBOOK.md`. Escalations surface as `ho:*` buttons here.
