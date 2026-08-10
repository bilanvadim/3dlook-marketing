# Platform policy pack (hosting / CI/CD / deploy)

## CI/CD
- Pipeline runs the same gates as local: ultracite lint → typecheck → tests → build. Red pipeline never merges.
- Deploy is automated from git (Vercel Git integration): push → preview/prod deploy. `merge` to the default branch stays human-gated.

## Environments & config
- Separate dev/preview/prod config via env vars; no prod secrets in repo or build logs.
- Migrations run as an explicit, gated step before/with deploy — never silently.

## Reliability
- Health checks + readiness for every service. Zero-downtime deploy where possible; documented rollback (revert + redeploy).
- Idempotent infra scripts; no manual snowflake steps.

## Reviewer checks
- Gates wired in CI. Secrets out of repo/logs. Migration step gated. Rollback path stated. Deploy reproducible from git.
