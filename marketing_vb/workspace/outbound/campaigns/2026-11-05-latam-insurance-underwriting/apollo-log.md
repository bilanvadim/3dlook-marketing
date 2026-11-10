# Apollo pulls — 2026-11-05-latam-insurance-underwriting

Written by `scripts/apollo-pull.py`. Credits are Apollo's own `credits_consumed`.

## 2026-11-06 search (located, coordinator scratch wrapper)
- companies 16, 47 titles, person_locations[] = row hq_country, max 300/company
- candidates 539, other employer 2
- 2026-11-06 coordinator title pre-filter (hypothesis persona: manager+ level, LOB/function exclusions, life/medical/underwriting word at multi-line insurers, L&H at reinsurers, ≤15 per company, tier rank) + hand overrides → 70 `candidate`, 471 `not-selected` (kept as pool). Zero at Brasilseg/BB Seguros, HSBC Seguros, Swiss Re Brasil (no L&H head in Apollo); SCOR Mexico and Hannover Re Mexico only ambiguous "Director Suscripción" / "Underwriting Manager".
- 2026-11-06 Vadim: Sales Navigator first (Hlib), Apollo only as top-up after it. `enrich` NOT run; 0 credits spent. Brief sent to Hlib (Slack DM, file sales-nav-latam-insurance-katya.txt): 16 companies, Brazil/Mexico, title Boolean (EN+PT+ES) + NOT + seniority, filter fallback.

## 2026-11-09 enrich → apollo-2026-11-09.csv
- written 50, skipped 8, credits 58
  - skipped Andres Sa***o: current employer is BANORTE SEGUROS Y PENSIONES (segurosbanorte.com.mx)
  - skipped Susana Gr***s: current employer is BANORTE SEGUROS Y PENSIONES (segurosbanorte.com.mx)
  - skipped Francisco Mo***a: current employer is BANORTE SEGUROS Y PENSIONES (segurosbanorte.com.mx)
  - skipped Leonardo Pe***z: current employer is BANORTE SEGUROS Y PENSIONES (segurosbanorte.com.mx)
  - skipped Luis Pi***n: current employer is BANORTE SEGUROS Y PENSIONES (segurosbanorte.com.mx)
  - skipped Yahir He***z: current employer is BANORTE SEGUROS Y PENSIONES (segurosbanorte.com.mx)
  - skipped Ricardo So***a: current employer is BANORTE SEGUROS Y PENSIONES (segurosbanorte.com.mx)
  - skipped Eduardo Ro***o: current employer is BANORTE SEGUROS Y PENSIONES (segurosbanorte.com.mx)

## 2026-11-09 enrich → apollo-2026-11-09-2.csv
- written 8, skipped 0, credits 8
- 2026-11-09 coordinator: Hlib's Sales Nav sheet (1xr160xq…, 452 rows, a company-wide seniority pull, not the title Boolean) saved as `sales-nav-raw/export-1.csv`; 12 of the 70 candidates were already in it → status `in-sales-nav`; the other 58 enriched. 8 Banorte rows were skipped by the literal domain check (Apollo org domain `segurosbanorte.com.mx` vs shortlist `segurosbanorte.com`, same employer BANORTE SEGUROS Y PENSIONES) → domain fixed in their candidate rows and re-enriched → `apollo-2026-11-09-2.csv`; Apollo charged again (8). Enriched rows now carry status `enriched`. **Total 66 credits.**

## 2026-11-09 enrich → apollo-2026-11-09-3.csv
- written 12, skipped 0, credits 12
- 2026-11-09 coordinator, after Vadim's checkpoint («добери з аполо якщо треба»): free located gap search (scratch `gap_search.py`: other domains, `q_keywords` seguros/vida, seniorities) for HSBC Seguros, BBVA Seguros, Brasilseg, Bradesco Vida e Previdência, SCOR Mexico, Banorte → 216 rows, 12 picked by hand (HSBC Director de Seguros Protection + Head of Insurance Specialists; BBVA SD Técnico Global Vida, Presidente BBVA Seguros, Director Estrategia y Portafolio de Seguros, Director de Tecnología Seguros y Pensiones; Brasilseg President; BVP Diretor-Presidente, a Diretor, a Superintendente Sênior; SCOR Head of L&H BD LatAm, Senior Client Manager MX L&H) → enriched through a scratch wrapper that accepts those Apollo org names as the shortlist rows (search gives no org domain) → `apollo-2026-11-09-3.csv`, **12 credits; campaign total 78**.

## 2026-11-10 enrich → apollo-2026-11-10.csv
- written 6, skipped 0, credits 6
- 2026-11-10 coordinator, after the Account facts round and Vadim's «Усі 7»: free name search (scratch `owner_search.py`, `q_keywords` = name, `person_locations[]` Brazil, with and without the row domain) found 6 of 7 owners (Andre Calazans was already in this file as `not-selected`, set to `candidate`); Tatiene Rokkaku (Brasilseg) not in Apollo. Enriched through a scratch wrapper that tells the employer check the Apollo org names of the rows (Allianz → Allianz Brasil, Bradesco Seguros → Bradesco Vida e Previdência). **Campaign total 84 credits.**
