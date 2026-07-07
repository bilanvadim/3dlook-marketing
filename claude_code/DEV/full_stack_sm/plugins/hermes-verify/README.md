# hermes-verify

The quality & verification layer — makes **"done" mean the code actually works** on front, back and db. Ported from the battle-tested executor↔reviewer loop of the `main` OrchestrAgent system, adapted to the Fullstack agents model.

## What's inside
- **code-reviewer** (agent) — adversarial reviewer, scores 0-100, checks every acceptance criterion against real evidence, verdict approve/request_changes/block. Re-runs gates itself; never trusts the executor's word.
- **runtime-verifier** (agent) — boots the real stack (db migrate → backend → frontend), runs Playwright e2e + endpoint smoke against the live system. Proves "всё рабочее на front/back/db".
- **verification-protocol** (skill) — the loop: independent gate re-run → score → runtime proof → retry with progress-delta + cumulative critiques + needs-review soft-block.
- **ultracite-lint** (skill) — Ultracite (Biome-based) is the standard linter/formatter for every project; `npx ultracite lint` is gate #1.
- **policy-packs/** — per-layer standards (security, database, backend, frontend, platform, testing, realtime) the executor builds to and the reviewer checks against.

## Use
- `/sm-verify [feature]` — run the full protocol on demand.
- Automatically: the orchestrator runs the protocol after each implementation task and before any release (see `CLAUDE.md`).

## The gates (re-run independently, never self-reported)
1. `npx ultracite lint` · 2. `tsc --noEmit` · 3. `npm test` · 4. `npm run build` · 5. runtime/e2e (live stack).

## Defaults
`PASS_SCORE=85` · `NEEDS_REVIEW=70` · `MIN_PROGRESS_DELTA=3` · `MAX_ATTEMPTS=3`.

> Autonomous step-state (per-step retry/resume in the conductor via an `ho_steps` table) is the next phase — this plugin defines the logic; the conductor will execute it deterministically.
