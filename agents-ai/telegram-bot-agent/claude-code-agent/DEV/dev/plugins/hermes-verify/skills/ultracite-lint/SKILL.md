---
name: ultracite-lint
description: Ultracite is the standard linter/formatter for every project the Fullstack agents build (zero-config preset on top of Biome — one fast binary, no ESLint/Prettier). Use to set it up in a new project and to run the lint gate. The verification-protocol calls `npx ultracite lint` as gate #1.
---

# Ultracite — the project lint/format standard

Every project these agents build uses **Ultracite** (https://www.ultracite.ai) — a zero-config, AI-ready preset over **Biome**. One Rust binary replaces ESLint + Prettier: fast, deterministic, subsecond on large repos. This is the lint gate in the `verification-protocol`.

## Set it up in a project (once)
```bash
npx ultracite@latest init     # adds biome.jsonc (extends ultracite) + editor settings + devDep
```
This creates `biome.jsonc`. On **Ultracite v7** the preset is exported under `ultracite/biome/*` (a bare `"ultracite"` does NOT resolve — verified in a live run):
```jsonc
{
  "$schema": "https://biomejs.dev/schemas/2.0.0/schema.json",
  "extends": ["ultracite/biome/core"]
  // project overrides go here, sparingly
}
```
(Older docs show `extends: ["ultracite"]` — that's pre-v7. Trust `ultracite init` to write the correct value for the installed version, and verify the config resolves with `npx biome check .`.)
Pin it as a devDependency so CI and agents use the same version:
```bash
npm i -D ultracite @biomejs/biome
```
Add npm scripts so gates are uniform across projects:
```jsonc
// package.json
"scripts": {
  "lint": "ultracite lint",      // check only — used by the verification gate
  "format": "ultracite format"   // write fixes — used to auto-resolve before re-lint
}
```

## Run it (the gate)
- **Check (gate):** `npx ultracite lint` → must exit clean. Non-zero = gate fail.
- **Auto-fix then re-check:** `npx ultracite format && npx ultracite lint`. Only formatting/safe fixes are auto-applied; real issues still fail and go back to the executor.

## Rules for agents
- Lint gate = `npx ultracite lint`, run **independently** by the reviewer/verifier — never trust the executor's "lint passes".
- Auto-fix is allowed for formatting/safe rules (`ultracite format`); do NOT blanket-disable rules to make the gate green. A rule that's genuinely wrong for the project → narrow override in `biome.jsonc` with a one-line comment why.
- New project scaffolding MUST include `ultracite init` before the first task is reviewed.
- Keep overrides minimal — the point of Ultracite is one shared strict baseline across all projects.
