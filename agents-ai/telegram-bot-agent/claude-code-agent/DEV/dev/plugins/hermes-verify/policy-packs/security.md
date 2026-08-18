# Security policy pack

## AuthN / AuthZ
- **Default auth = Better Auth** (MIT, self-host, Postgres/Drizzle). No Supabase Auth. Sessions are server-validated.
- Every endpoint authenticates; every resource checks authorization (ownership/tenant/role) — not just "logged in".
- Authorization enforced server-side AND at the DB (RLS). Bridge to RLS: after Better Auth validates the session, set a per-request session GUC (`SET LOCAL app.user_id`, `app.tenant_id`); policies read `current_setting(...)`. Never trust the client for access decisions.

## Input & output
- Validate/normalize all input (Zod) at the boundary. Parameterized queries only — never string-built SQL.
- Output encoding to prevent XSS; no user input reflected unescaped. Set security headers (CSP, HSTS, etc.).

## Secrets & data
- No secrets in code/logs/commits/responses — env vars only. Least-privilege keys; service-role server-side only.
- PII minimized and access-logged where relevant. No sensitive data in error messages.

## Dependencies & supply chain
- Read the source before adopting a skill/MCP/dep (13.4% of public skills had critical vulns). No `curl | sh`. Pin versions.

## Reviewer checks (any critical flaw here = automatic BLOCK)
- Missing authz, injection, secret leakage, broken tenant isolation, unvalidated input on a privileged path → block, regardless of score.
