# Default infrastructure & Supabase → open-source replacement map

The canonical stack for projects built by Fullstack agents. **No Supabase for new/migrated projects** — plain PostgreSQL + targeted OSS services, added on demand. `CLAUDE.md` / `FULLSTACK-AGENTS.md` point here; policy-packs enforce the per-layer details.

## Project decisions (2026-06-20)
- **way2buy — KEEPS Supabase.** Heavy user (Auth 45 · Realtime 17 · Storage 8 · RLS 11 · pgvector 8). Not worth migrating now.
- **`supabase.smiro.dev` → Supabase Studio** — already live: Traefik → `oauth2-proxy-supabase` (GitHub OAuth, user `SergeMiro` only) → `supabase-studio:3000`; API paths `/rest /auth /storage` → kong. Don't disturb (way2buy depends on it).
- **All other projects → plain PostgreSQL** per the map below. Status: SimplifyEU (Auth+Data+RLS — good pilot), ASCoFacade (Auth+Data, light storage/realtime), smiro.dev (trivial). The conductor itself uses this Postgres for its `hc_*` orchestration schema (direct `pg`).
- **New projects** start clean on this stack — no migration needed.

## What PostgreSQL already has (do NOT replace)
SQL, tables, schemas, roles/privileges, **RLS**, transactions, views, triggers, functions/stored procedures, **JSONB**, full-text search. These are native — never "replace" them.

## Supabase = Postgres + services. Replacement map
| Supabase service | Gap in plain PG | Replacement (our default) | Deploy footprint |
|---|---|---|---|
| Studio / Dashboard | web admin UI | **DBeaver / psql** locally; CloudBeaver CE if browser UI needed | 0–1 shared container |
| **Auth** | users, OAuth, sessions, reset | **Better Auth** (MIT, in each Next.js app); Keycloak only if one OIDC shared across Next.js + Python | Better Auth per-app; Keycloak 1 shared (on demand) |
| REST Data API | HTTP API over tables | **Next.js Route Handlers / FastAPI** (preferred — safer/flexible); PostgREST only where the frontend must hit the DB directly | inside each app |
| GraphQL API | GraphQL | don't add unless needed → PostGraphile / Hasura | per-project, on demand |
| **Realtime** | client WS subscriptions | light: **LISTEN/NOTIFY + SSE/WS** in the API; serious: **Centrifugo** (1 shared, channels `crm:*`, `agenda:*`, …) | 1 shared Centrifugo (on demand) |
| **Storage** | S3 file storage | **SeaweedFS** (Apache-2, S3 API, shared, per-project buckets); Cloudflare R2 as cloud option | 1 shared container (on demand) |
| Edge Functions | serverless runtime | Next.js Route Handlers / Server Actions / FastAPI / worker | inside backends |
| Cron jobs | scheduler | **pg_cron** extension | inside Postgres |
| Queues | message queue | **PGMQ** extension + worker (Next.js/Python) | inside Postgres; worker in app |
| Database Webhooks | HTTP from triggers | **pg_net** + trigger; more robust → transactional outbox + worker | inside Postgres |
| Vector / AI search | vector type+search | **pgvector** extension (NOT a gap — it's a PG extension) | inside Postgres |
| Connection pooling | pooler | **PgBouncer** | 1 shared (on demand) |
| Backups / PITR | backup policy | **pgBackRest** + separate backup storage | server-wide |
| Logs / metrics | observability UI | PG logs + `postgres_exporter` + Prometheus/Grafana | shared, only if needed |
| API gateway / HTTPS | single entry | **Traefik** (already deployed) | existing 1 container |
| CLI & migrations | Supabase CLI | `psql`, `pg_dump`/`pg_restore`, **Drizzle Kit** (TS) / **Alembic** (Python) | no service |
| MCP for AI | Supabase MCP | **DBHub MCP** (connects to several Postgres DBs) | 1 MCP, multi-DB |
| Projects switcher | project panel | **separate Postgres databases** in one server (`crm_db`, `agenda_db`, …) | one DB + one user per project |

## Install order
**Now (always-on):** PostgreSQL with extensions `pg_cron`, `pgvector`, `pgmq` (+ `pg_net` when needed) · **Traefik** · **pgBackRest** · **DBHub MCP** · the app containers.
**On demand only (don't pre-deploy):** Keycloak, Centrifugo, SeaweedFS, PgBouncer, Prometheus/Grafana. Add when a project actually needs centralized auth / serious realtime / files / many connections / monitoring.

## API & DB conventions
- Frontend → **Next.js Route Handlers / FastAPI** → PostgreSQL. Auto-REST (PostgREST) is the exception, not the default.
- **Next.js:** Drizzle + Better Auth + Route Handlers. **Python:** FastAPI + SQLAlchemy + Alembic.
- **One project = one database + one Postgres user.** Migrations owned by **only** Drizzle **or** only Alembic — never both on the same DB.
- RLS bridge: Better Auth validates the session → backend `SET LOCAL app.user_id / app.tenant_id` → policies use `current_setting(...)`. No `auth.uid()`.

## Minimal footprint (5 projects)
1 PostgreSQL · 5 databases · 5 DB users · Traefik · pgBackRest · DBHub MCP. Auth/Storage/Realtime/queues are added per project as needed — not kept running for all five.
