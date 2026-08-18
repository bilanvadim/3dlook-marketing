# Backend policy pack

## API
- REST conventions, versioned `/api/v1/`. Response shape `{ data }` or `{ data: null, error: { code, message } }`.
- Status codes: 201 create, 204 delete, 400 malformed, 401 unauthenticated, 403 unauthorized, 404, 409 conflict, 422 validation, 429 rate-limited.
- Pagination: cursor-based for large sets, offset only for small/bounded.

## Error handling
- Structured logging with a `request_id`; safe messages to clients, stack traces only in logs.
- One global error handler; async errors propagated, never swallowed.

## Validation
- Validate input at the API boundary (Zod). Business rules in the service layer. DB constraints are the last line, not the first.

## Config & secrets
- All config via env vars, validated at startup (fail-fast). Dev defaults allowed; no secrets in code/logs/responses.

## Jobs & async
- Long work → queue (**PGMQ** extension on Postgres) + a worker, not the request thread. Idempotent handlers; retries with backoff; dead-letter on repeated failure.
- Scheduled work → **pg_cron**; outbound HTTP from the DB → **pg_net** or a transactional outbox + worker. (No Supabase services.)

## Reviewer checks
- Every endpoint has authn + authz. No N+1. Inputs validated. Errors structured. No secret leakage. Tests cover happy + auth-fail + validation paths.
