# Realtime policy pack (websockets / SSE / Postgres LISTEN-NOTIFY)

**Stack:** light realtime → Postgres `LISTEN/NOTIFY` + SSE/WS in the API. Serious realtime → **Centrifugo** (1 shared server, channels namespaced per project `crm:*`, `agenda:*`). No Supabase Realtime (exception: way2buy keeps Supabase).

## Connection & delivery
- Authenticate the socket/channel on connect; authorize every subscription (tenant/user scope) — same rules as REST.
- Assume drops: auto-reconnect with backoff, resume/replay from a cursor, idempotent message handling (dedupe by id).
- Backpressure: bound buffers, drop/coalesce sensibly under load; never unboundedly queue.

## Correctness
- Define delivery semantics explicitly (at-least-once vs at-most-once) and handle duplicates accordingly.
- Order guarantees stated per channel; don't assume global ordering.

## Scale
- Fan-out via a broker/Realtime, not N app-loops. Heartbeats + idle timeouts to reap dead connections.

## Reviewer checks
- Channel authz present. Reconnect + replay handled. Handlers idempotent. Backpressure bounded. Load/disconnect path tested.
