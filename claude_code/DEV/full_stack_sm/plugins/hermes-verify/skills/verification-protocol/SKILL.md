---
name: verification-protocol
description: The loop that makes "done" mean working code. After any implementation task, independently re-run the gates (ultracite lint, typecheck, tests, build), score the work 0-100 with code-reviewer, prove it runs end-to-end with runtime-verifier, and retry with progress-delta + cumulative critiques until it passes or escalates. Use whenever a task is "finished", before any release, or via /sm-verify.
---

# Verification protocol — never trust "it works", prove it

"The executor said it's done" is a claim. This protocol turns claims into evidence. The orchestrator (or the orchestrator in autonomous mode) runs it per implementation task; the same logic applies whether one person or a robot drives it.

## The non-negotiable rule
**Re-run every gate yourself. Never accept a self-reported gate.** The executor's `quality_gates` block is a hint; ground truth is you running the command and reading the output.

## The gates (independent re-run, in this order)
1. **Lint + format — Ultracite:** `npx ultracite lint` must be clean (auto-fixable issues: `npx ultracite format` then re-lint). See the `ultracite-lint` skill for setup.
2. **Types:** `npm run typecheck` or `npx tsc --noEmit` — zero errors.
3. **Tests:** `npm test` (or `pnpm test` / `pytest`) — all green; coverage meaningful (reviewer judges).
4. **Build:** `npm run build` — succeeds.
5. **Runtime/e2e (the "всё рабочее" gate):** hand off to `runtime-verifier` — boots db+back+front and runs Playwright e2e + endpoint smoke against the LIVE stack. This is what proves front/back/db actually work together, not just in isolation.

A failing gate is a **finding**, never a reason to weaken the gate.

## The loop (per task)
```
attempt = 1
loop:
  1. executor implements the task (TDD: tests first), writes handoff report
  2. RE-RUN gates 1-4 independently.
       └─ if any fail → synthesize score=0, skip the reviewer (cheap fail), go to retry
  3. code-reviewer scores 0-100 + verdict (reads code+diff+policy packs, checks AC with evidence)
  4. if verdict == approve (score ≥ 85, zero critical):
        run runtime-verifier (gate 5).
          ├─ runtime pass  → DONE  (record score + evidence, commit)
          └─ runtime fail  → treat as a critical issue, go to retry
  5. else → retry
retry:
  - append reviewer issues to cumulative critiques file (.../review/critiques.json)
  - reset working tree to the step baseline (git) so a bad attempt doesn't contaminate the next
  - attempt += 1, re-run executor WITH the full critique history + retry_instructions
  - PROGRESS-DELTA GATE on score:
       delta = score - prev_score
       delta < 0            → BLOCK now (regression) → escalate to human
       0 ≤ delta < 3        → BLOCK (plateau, retrying won't help) → escalate
       delta ≥ 3            → keep going
  - stop conditions:
       score ≥ 85 ∧ runtime pass            → DONE
       attempts ≥ MAX (default 3) ∧ score ≥ 70 ∧ monotonic growth → NEEDS_REVIEW (hand to human, not a hard fail)
       else                                  → BLOCK (max_attempts) → escalate
```

## Defaults (override per task)
- `PASS_SCORE = 85`, `NEEDS_REVIEW = 70`, `MIN_PROGRESS_DELTA = 3`, `MAX_ATTEMPTS = 3`.

## Cumulative critiques
Keep `.claude/scratchpad/<feature>/review/critiques.json` as an append-only array of every attempt's `{attempt, score, critical_issues, retry_instructions}`. The executor reads the WHOLE history on each retry — so it sees what was already tried, not just the last note.

## Acceptance with evidence
Every acceptance criterion must end the loop as `verified` with concrete evidence (test name + result, file:line, endpoint response, Playwright trace). `not_verifiable` counts against the score — if you can't prove it, it isn't done.

## Escalation (autonomous mode)
On BLOCK or NEEDS_REVIEW the orchestrator opens an escalation (Telegram) with the score, the top issues, and the diff — the human decides retry/approve/abort. In interactive mode, surface the same to the operator.

## Policy packs
Before reviewing/implementing a task, load the relevant `plugins/hermes-verify/policy-packs/<layer>.md` (by the task's tags) — they are the shared per-layer standard the executor builds to and the reviewer checks against.
