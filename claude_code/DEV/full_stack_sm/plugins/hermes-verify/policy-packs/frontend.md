# Frontend policy pack (TypeScript / Next.js App Router / React)

## Structure
- Server Components by default; `"use client"` only where interaction/state needs it. Data fetching on the server; no secrets in client bundles.
- Co-locate component + test + styles. No prop-drilling past 2 levels (context or composition).

## State & data
- Server state via the framework's data layer / a query lib; local UI state stays local. No fetch waterfalls — parallelize.
- Handle all four states explicitly: loading, empty, error, success. No silent failures.

## Quality & a11y
- TS strict, no `any` on public boundaries. Semantic HTML, labelled controls, keyboard-navigable, visible focus. Respects `prefers-reduced-motion`.
- Lint/format via Ultracite (gate). Images optimized; no layout shift on load.

## Reviewer checks
- Client/server boundary correct, no secret in client. loading/empty/error/success all handled. a11y basics pass. Critical path covered by a Playwright e2e (runtime-verifier).
