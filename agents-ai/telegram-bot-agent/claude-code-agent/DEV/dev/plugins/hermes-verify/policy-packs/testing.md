# Testing policy pack

## What to test
- TDD: write tests for each acceptance criterion FIRST, then implement to pass them.
- Pyramid: many unit, some integration, few e2e. The critical user path MUST have a Playwright e2e (runtime-verifier).
- Cover edge cases: null/empty/zero/boundary/Unicode, error paths, authz failure, concurrency where relevant.

## Quality of tests
- A test must fail on a broken implementation — no tautological/always-green tests. Assert behavior, not implementation detail.
- Deterministic: no real network/time/random dependence; seed and isolate. Each test sets up and tears down its own state.
- Coverage is a signal, not a target — meaningful assertions over % chasing.

## Gates
- `npm test` green is a gate, re-run independently. A failing test is a finding — never weaken or delete a test to go green.

## Reviewer checks
- AC-to-test mapping exists. Tests would catch a regression. Edge + auth-fail paths covered. e2e exists for user-observable behavior.
