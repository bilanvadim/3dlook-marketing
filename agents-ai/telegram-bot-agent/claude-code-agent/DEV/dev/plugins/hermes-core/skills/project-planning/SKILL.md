---
name: project-planning
description: How to turn a raw idea into a production-grade, executable project plan — a deep adaptive technical interview across all stack layers, anti-pattern prediction, and a richly structured step list (each step with acceptance criteria, layer tags, quality bar, dependencies). Use at the start of any non-trivial feature/project, in /sm-feature, or whenever someone says "build X" / "how should we build this". Ported from the OrchestrAgent interviewer.
---

# Project planning — interview, then a plan you can actually execute

A vague idea is not a plan. Before any code, produce a detailed plan that the specialist agents can execute and the `verification-protocol` can check. Two phases: **interview** (the orchestrator, in the live session) → **synthesis** (product-architect writes the artifacts) → **hard approval gate**.

## Phase 1 — adaptive interview (orchestrator asks the human)
Cover these layers, but ADAPT depth to scale (a weekend MVP ≠ millions of users). Skip what's irrelevant; go deep where risk lives. Ask in small batches, don't interrogate.

- **L0 Domain** — what problem, who for, what does success look like, what's explicitly out of scope.
- **L1 Architecture style** — modular monolith (default) vs services; sync vs event-driven.
- **L2 Data** — entities + relationships, source of truth, multi-tenant? consistency needs, retention/PII.
- **L3 Backend compute** — API style, heavy/long work (→ queue), third-party calls.
- **L4 Auth & security** — who authenticates, roles/tenancy, compliance (GDPR/etc).
- **L5 Performance & scale** — expected load, latency budget, hot paths, caching need.
- **L6 Frontend** — surfaces (web/mobile), SSR/CSR, key flows, design expectations.
- **L7 Realtime** — live updates? delivery semantics.
- **L8 Integrations** — external APIs, webhooks, payment, email.
- **L9 Deploy** — hosting, environments, CI/CD, rollback expectations.
- **L10 Observability** — logging, error tracking, metrics, alerts.
- **L11 Testing** — coverage expectations, e2e for which flows.

**State assumptions explicitly** when the human doesn't know — don't silently choose. Surface trade-offs.

## Phase 1b — predict anti-patterns (call them out BEFORE they're built)
Actively warn and steer away from: N+1 queries · shared DB between services · premature microservices · secrets in code · multi-tenant tables without RLS · unbounded queries / no pagination · non-idempotent job handlers · endpoints without authz · frontend fetch waterfalls · no migration discipline. For each real risk in this project, note it and the chosen mitigation.

## Phase 2 — synthesis (product-architect writes these to `.claude/scratchpad/<slug>/`)
- `spec.md` — problem, scope, out-of-scope, global acceptance.
- `architecture.md` — components, data flow, ER model, bounded contexts; every decision in ADR form (context → decision → consequences) with at least one rejected alternative.
- `nfr.md` — SLOs (latency/availability/RPO-RTO), throughput, consistency, compliance.
- `risks.md` — risk register: probability × impact × mitigation.
- `plan.md` — the executable step list (schema below).

## The plan step schema (each step in `plan.md`)
Each step must carry enough for a specialist to execute it and for `code-reviewer`/`runtime-verifier` to check it:
```
### Step <N> — <title>
- phase: infrastructure|data|core|integration|hardening|polish
- agent: design-director|frontend-engineer|backend-engineer|database-engineer|platform-engineer|qa-engineer|sre-engineer
- tags: [backend, database, security]      # → load these policy-packs (plugins/hermes-verify/policy-packs/<tag>.md)
- description: what to build (1-3 sentences)
- acceptance:                              # → code-reviewer verifies EACH with evidence
  - AC-1: <observable, testable criterion>
  - AC-2: ...
- quality_bar: { tests: required, e2e: <yes|no>, perf: "<budget or n/a>" }   # → verification thresholds
- depends_on: [<step numbers>]             # ordering; no edge = parallelizable
- risk: low|medium|high
- files_likely_affected: [paths]
- status: pending                          # pending|running|done|blocked (orchestrator updates)
```
Rules for good steps: each sized for ONE agent in ONE session; acceptance criteria are observable and testable (they become the reviewer's checklist); tag every step so the right policy pack and specialist apply; declare real dependencies only (over-declaring kills parallelism).

## Phase 3 — HARD approval gate
After writing the artifacts, the orchestrator shows the human a summary (feature, key decisions, first 3-5 steps + agents, top risks) and **STOPS**. No implementation until the human explicitly approves (e.g. types `go`). The human may refine: "edit step N: …" or "show step N". No implicit consent.

## Hand-off to execution
On approval, delegate per `scratchpad-protocol`, honoring `depends_on` and the parallelism limits in CLAUDE.md. Each finished step runs through `verification-protocol` (its `acceptance` + `tags` + `quality_bar` drive the review and runtime gates).
