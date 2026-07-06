# Database policy pack (plain PostgreSQL / Drizzle)

Default DB is **plain PostgreSQL** (self-hosted/managed), not Supabase. The app owns auth and connects with its own role — there is no Supabase Auth / PostgREST. Connection via `DATABASE_URL`; server-side only. **One project = one database + one DB user**; migrations owned by only Drizzle (TS) OR only Alembic (Py), never both. Extensions in use: `pg_cron` (schedules), `pgmq` (queues), `pgvector` (vector search), `pg_net` (DB→HTTP). See `STACK.md` for the full Supabase→OSS map.

## Schema & migrations
- All schema changes via Drizzle migrations, committed and reviewed — never ad-hoc DDL on a live DB.
- Migrations are forward-only and reversible-in-practice (have a down/rollback plan). Never edit an already-applied migration.
- Explicit types, NOT NULL by default, sane defaults, FKs with ON DELETE intent stated.

## RLS (multi-tenant = deny-by-default) — Postgres-native
- RLS **enabled** on every table holding tenant/user data. No table ships without a policy decision recorded.
- Auth context comes from the APP, not Supabase: the app authenticates the user, then sets a per-request session GUC (e.g. `SET LOCAL app.user_id = '...'`, `app.tenant_id`); policies scope by `current_setting('app.tenant_id', true)`. (No `auth.uid()` — that was Supabase-specific.)
- The app connects with a least-privilege role that does NOT bypass RLS; a separate admin/migration role is server-side only.
- Cross-tenant access must be DB-refused, proven by a test that sets a different tenant GUC and fails to read.

## Performance
- Index foreign keys and frequent filter/sort columns. No unbounded queries; paginate.
- Avoid N+1 (batch/join). Watch for sequential scans on hot paths (`explain analyze`).

## Reviewer checks
- Migration present + reviewed for any schema change. RLS on + policy correct (with a deny test). Indexes for new query patterns. No destructive statement without an explicit, gated migration.
