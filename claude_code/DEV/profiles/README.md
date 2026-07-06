# Profiles — one Claude Code "system" at a time

Claude Code degrades when too many agents/skills/commands compete for selection
and context. So the three domains are **mutually-exclusive profiles**: only one
is enabled at any moment.

| Profile | Marketplace(s) | What loads |
|---|---|---|
| `dev` | `full_stack_sm` (`ai-agents-config`) | full-stack dev team (10 plugins) |
| `seo` | `seo_sm` (`ai-agents-seo`) + shared base | SEO agents/skills + core/verify |
| `marketing` | `marketing_sm` (`ai-agents-mkt`) + shared base | marketing agents/skills + core/verify |
| `security` | `full_stack_sm` (subset) | security-auditor + QA + verify (seed for ECC adoption) |

**Shared base** kept in every non-dev profile: `hermes-core` (orchestration,
session-handoff) + `hermes-verify` (quality gates) — so handoff and "done means
working" stay consistent across systems.

## Switching (interactive Claude Code)

```bash
./switch-profile.sh --list          # show profiles + active one
./switch-profile.sh seo             # activate SEO
./switch-profile.sh --current       # what's active
```

It registers any needed marketplaces, then rewrites `~/.claude/settings.json`
`enabledPlugins` to **exactly** the profile's set (mutual exclusion) and records
the active profile in `~/.claude/.active-profile`.
**A Claude Code restart is required** — plugins load only at session start.

## Switching (automated — conductor)

Each job carries a `profile` (column on `hc_jobs`, migration
`conductor/sql/003_profiles.sql`). When the conductor starts an Agent SDK
session for a job it should activate that profile before dispatching. Hermes
sets the profile at intake:

- **Explicit:** "переключись на SEO / do this as SEO" → profile = `seo`.
- **By intent:** SEO/ranking/SERP/crawl → `seo`; campaign/ads/funnel/email →
  `marketing`; audit/vulnerability/RLS/OWASP → `security`; everything code →
  `dev`.

See the `vps-orchestration` skill → "Profile routing" for Hermes' rules.

## Adding domain content

Profiles are the harness; the systems are still thin. Fill `seo_sm` /
`marketing_sm` with real plugins — authored, or adopted from vetted sources
(e.g. ECC) via `/sm-evaluate` + `skill-guard`. Add the new plugin names to the
relevant `profiles/<name>.json` `enabledPlugins`.
