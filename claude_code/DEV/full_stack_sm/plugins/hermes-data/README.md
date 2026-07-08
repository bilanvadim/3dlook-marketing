# hermes-data
Default DB is **plain PostgreSQL** (self-hosted/managed), not Supabase. Connect via `DATABASE_URL`; use a least-privilege role for routine work and a separate admin/migration role server-side only.

MCP: **DBHub MCP** — connects to several Postgres databases at once, searches tables/indexes/procedures, runs SQL in transactions. Use a read-only role for routine work; grant write/DDL only temporarily for migration sessions. (Postgres MCP Pro / crystaldba is an alternative for query-plan/index advice.) Full infra map: `STACK.md`.
