# Security system (`security`)

Claude Code marketplace for the **security** profile. Sibling of `dev`
(dev), `seo` (SEO), `marketing` (marketing). Only one profile is active at a
time — switch with `../switch-profile.sh security` (see `../profiles/`).

The `security` profile loads the shared base + auditor:
`hermes-core` (orchestration), `hermes-quality` (**security-auditor** — Opus,
Trail-of-Bits methodology), `hermes-verify` (gates), plus this marketplace's
`sec-core`.

## sec-core (vetted ECC adoptions, MIT)

| Component | Type | What it adds |
|---|---|---|
| **security-bounty-hunter** | skill | exploitability-first vuln triage (reachable + user-controlled + meaningful sink; explicit "skip these" noise list) — reduces false positives vs the broad auditor |
| **silent-failure-hunter** | agent | hunts fail-open fallbacks / swallowed errors / lost error propagation (security-adjacent: fail-open == auth/validation bypass) |

Both were selected via `/sm-evaluate`-style evaluation + `skill-guard` vetting.
Provenance and MIT license: `plugins/sec-core/ATTRIBUTION.md`.

## Not adopted (and why)
- `security-review` / `security-reviewer` — redundant with our `security-auditor`.
- `safety-guard` — good PreToolUse-guard pattern but ships no code; we already run
  `.claude/hooks/guard.py`. Revisit to harden guard.py with its ruleset.
- `security-scan` — wraps external `ecc-agentshield`; our `agents-ai/telegram-bot-agent/hermes-agent/ops/
  skill-guard` already runs AgentShield, so it's redundant + a supply-chain surface.
- language-specific security packs (laravel/django/quarkus/springboot/perl) — wrong
  stack (we're TS/React/Next/Postgres).

## Extending
Add vetted security skills/agents to `sec-core` (or new `sec-*` plugins), then list
them in `../profiles/security.json` `enabledPlugins`.
