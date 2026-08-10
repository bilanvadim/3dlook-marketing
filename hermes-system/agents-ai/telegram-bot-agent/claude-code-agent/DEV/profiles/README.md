# Profiles — one Claude Code "system" at a time

Claude Code degrades when too many agents/skills/commands compete for selection
and context. So each domain is its own **mutually-exclusive profile**: only one
is enabled at any moment.

| Profile | Marketplace(s) | What loads |
|---|---|---|
| `dev-sm` | `dev-sm` (`dev-sm`) | full-stack dev team (10 plugins) |
| `seo-sm` | `seo-sm` (`seo-sm`) + shared base | SEO agents/skills + core/verify |
| `marketing-sm` | `marketing-sm` (`marketing-sm`) + shared base | marketing agents/skills + core/verify |
| `security-sm` | `dev-sm` (subset) | security-auditor + QA + verify (seed for ECC adoption) |
| `test-sm` | `dev-sm` + `marketing-sm` + `ai-agents-mvb*` | experimental MIX: Vadim's `mvb-*` teams + `mkt-*` + base (`/vbsm-campaign`) |
| `sandbox-sm` | `dev-sm` (core only) + `sandbox-sm` | trial bench: `hermes-core` + `sbx-probe`, one candidate at a time — see `../sandbox-sm/README.md` |

**Shared base** kept in every non-dev profile: `hermes-core` (orchestration,
session-handoff) + `hermes-verify` (quality gates) — so handoff and "done means
working" stay consistent across systems. `sandbox-sm` is the one exception: it
drops `hermes-verify` too, because the point there is that anything answering
besides the base is the candidate under trial.

## Switching (interactive Claude Code)

```bash
./switch-profile.sh --list          # show profiles + active one
./switch-profile.sh seo-sm             # activate SEO
./switch-profile.sh --current       # what's active
```

It registers any needed marketplaces, then rewrites `~/.claude/settings.json`
`enabledPlugins` to **exactly** the profile's set (mutual exclusion) and records
the active profile in `~/.claude/.active-profile`.
**A Claude Code restart is required** — plugins load only at session start.

## Switching (automated — conductor)

Each job carries a `profile` (column on `ho_jobs`, migration
`conductor/sql/003_profiles.sql`). When the conductor starts an Agent SDK
session for a job it should activate that profile before dispatching. Hermes
sets the profile at intake:

Only the four working systems are routable. `test-sm` and `sandbox-sm` are absent
from `route-profile.sh` and from the `ho_jobs.profile` CHECK on purpose: no
intent classifier and no autonomous job may land in an experimental or unvetted
profile. You enter those by hand.

- **Explicit:** "переключись на SEO / do this as SEO" → profile = `seo-sm`.
- **By intent:** SEO/ranking/SERP/crawl → `seo-sm`; campaign/ads/funnel/email →
  `marketing-sm`; audit/vulnerability/RLS/OWASP → `security-sm`; everything code →
  `dev-sm`.

See the `vps-orchestration` skill → "Profile routing" for Hermes' rules.

## Adding domain content

Profiles are the harness; the systems are still thin. Fill `seo-sm` /
`marketing-sm` with real plugins — authored, or adopted from vetted sources
(e.g. ECC) via `/sm-evaluate` + `skill-guard`. Add the new plugin names to the
relevant `profiles/<name>.json` `enabledPlugins`.
