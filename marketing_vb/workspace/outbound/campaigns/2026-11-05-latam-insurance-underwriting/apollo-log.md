# Apollo pulls — 2026-11-05-latam-insurance-underwriting

Written by `scripts/apollo-pull.py`. Credits are Apollo's own `credits_consumed`.

## 2026-11-06 search (located, coordinator scratch wrapper)
- companies 16, 47 titles, person_locations[] = row hq_country, max 300/company
- candidates 539, other employer 2
- 2026-11-06 coordinator title pre-filter (hypothesis persona: manager+ level, LOB/function exclusions, life/medical/underwriting word at multi-line insurers, L&H at reinsurers, ≤15 per company, tier rank) + hand overrides → 70 `candidate`, 471 `not-selected` (kept as pool). Zero at Brasilseg/BB Seguros, HSBC Seguros, Swiss Re Brasil (no L&H head in Apollo); SCOR Mexico and Hannover Re Mexico only ambiguous "Director Suscripción" / "Underwriting Manager".
- 2026-11-06 Vadim: Sales Navigator first (Hlib), Apollo only as top-up after it. `enrich` NOT run; 0 credits spent. Brief sent to Hlib (Slack DM, file sales-nav-latam-insurance-katya.txt): 16 companies, Brazil/Mexico, title Boolean (EN+PT+ES) + NOT + seniority, filter fallback.
