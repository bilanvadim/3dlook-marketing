# Hermes Agent AI ↔ Fullstack agents — integration contract

This is the boundary between the **external manager** (Hermes Agent AI, NoSearch, on the VPS) and the **Fullstack agents** system (Claude Code + this conductor). Hermes is a *thin, non-technical manager*: it talks to the human over Telegram, gathers a product brief, hands work down, and reports status. All technical work, planning, execution and **verification** live on the Fullstack side. Hermes only **reads state and relays**.

> Source of truth for a project lives HERE (conductor libSQL state + scratchpad files in the workspace), never inside Hermes. If Hermes restarts, it rehydrates everything from the surfaces below. Hermes holds only its Telegram thread.

## Responsibility split
| | Hermes Agent AI (manager) | Fullstack agents (Claude Code + conductor) |
|---|---|---|
| Telegram channel + notifications | ✅ owns | — |
| Product intake (what/who/scale/design/i18n/payments/SEO/deadline) | ✅ asks the human | — |
| Deep technical questions | relays them to the human | ✅ `product-architect` authors them (asks only the 4–6 genuinely-ambiguous) |
| Detailed plan + execution | — | ✅ `product-architect` plans, specialists build |
| Independent verification (gates re-run, reviewer 0–100, runtime e2e) | reports the verdict/score | ✅ `hermes-verify` does it |
| Progress %, "running / waiting-on-limits / blocked" | ✅ reads + reports | ✅ exposes it |

## Project status machine (what Hermes reports)
```
planning ──▶ awaiting-input ──▶ running ──▶ verifying ──▶ done
   │              ▲   │            │  │                     ▲
   │              └───┘            │  └─▶ deferred (waiting-on-limits) ─┘ (resume)
   └─▶ (architect makes defaults)  └─▶ escalated / blocked / needs_review ─▶ (human)
```
- **planning** — architect building the plan.
- **awaiting-input** — waiting for the human to answer open questions (see below). Claude Code is NOT running; nothing is consumed.
- **running** — steps executing.
- **deferred** — paused on a token/rate limit; Hermes shows "waiting on limits", auto-resumes.
- **verifying** — a step is in the verification loop.
- **escalated / blocked / needs_review** — needs a human decision (relayed via Telegram).
- **done / failed / aborted** — terminal.

## Surfaces Hermes consumes (SQLite/libSQL — direct SQL; local file or Turso)
- **`ho_project_status`** (view) — per job: `job_status`, `percent`, `total_steps`, `done_steps`, `open_questions`, `open_escalations`, `last_activity`. The single read for a Telegram status update.
- **`ho_steps`** — per-step state: `status`, `attempts`, `score`, `acceptance` (with evidence), reviewer/runtime reports. Drives "% done" and "what's happening now".
- **`ho_questions`** — the async interview channel. Hermes reads `status='open'` rows, relays to Telegram, writes answers via `ho_answer_question(id, text)`. When the last open question is answered, the job leaves `awaiting-input` and resumes.
- **`ho_escalations`** — human decisions (approve/deny/abort) for gated actions / blocks.
- **`ho_jobs`** — the job + `resume_session_id` (durable resume).

## The awaiting-input (interview) flow — where context lives
1. `product-architect` needs human input → writes its questions + partial state to **scratchpad files** in the workspace, inserts rows into **`ho_questions`** (status=open), sets job `awaiting-input`. **The Claude Code run ends** (no idle session, no token burn).
2. Hermes reads open questions → asks the human in Telegram → writes answers back with `ho_answer_question(...)`.
3. When no open questions remain, the conductor flips the job back to `queued/running` and **resumes by re-reading the scratchpad files** (file-based continuation; `resume_session_id` is best-effort for short gaps).

→ Authoritative project context = **scratchpad files + libSQL** (Fullstack side). Hermes = thin relay. Hermes' own long-term cross-project memory (Obsidian Graph) is separate and added later.

## Per-step execution (the deterministic loop)
For each ready step (`ho_next_step` picks the next `pending` step whose `depends_on` are all `done`):
1. executor builds it (TDD, policy packs by `tags`);
2. gates re-run independently (ultracite/typecheck/test/build);
3. `code-reviewer` scores 0–100 + verdict; if approved, `runtime-verifier` proves it runs;
4. decision via the pure `steploop` module: **done / retry (progress-delta, cumulative critiques) / needs_review / blocked**.
The decision logic is unit-tested (`steploop.ts`); the SDK calls are the one integration seam (`agent-runner.ts`).

## What Hermes must NEVER do
Author technical decisions, write code/designs, or be the source of truth for a project. It asks product questions, relays the architect's questions, triggers work, reads these surfaces, and tells the human. That's it.
