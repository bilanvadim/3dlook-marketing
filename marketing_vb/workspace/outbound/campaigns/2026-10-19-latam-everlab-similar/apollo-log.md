# Apollo pulls — 2026-10-19-latam-everlab-similar

Written by `scripts/apollo-pull.py`. Credits are Apollo's own `credits_consumed`.

## 2026-10-21 search
- companies 13, 70 titles
- candidates 61, other employer 0, already in Sales Nav 6

## 2026-10-21 enrich → apollo-2026-10-21.csv
- written 67, skipped 0, credits 67

## 2026-10-21 coordinator, by hand (search → enrich above)
- The domain search found 0 at gotimeless.ai (with titles), toma.mx, medriocheck-up.com.br and medicinadelongevidad.com. Added to the candidates before `enrich`:
  - Timeless: Brand and Content Manager at gotimeless.ai (no title filter there, 3 people in all); CEO and CPO of the parent Choiz (choiz.com.mx, seniority filter). Enriched: the CEO lists "CEO & Co-Founder at Timeless AI".
  - Med-Rio Check-up: Apollo keeps the org without a domain; searched by the org name (q_keywords, managers and up): IT manager and 4 medical managers (billing manager left out; the director is already in Sales Nav). Enriched domain is medrio.com.br.
  - TOMA Health: 3 people by the org name. Enriched domain is tomahealth.com.au (Sydney), a different company: **the 3 rows were removed from apollo-2026-10-21.csv** (3 credits spent on the check).
- Marked in-sales-nav by hand (the name match missed accents or compound surnames): Jeane Tsutsui, Gustavo Stuani Guimarães, Marcelo Nico, Rodrigo Meyer, Marcos Vignal (Fleury), Germán de la Llave (AIONIS).
- Rendrik Franco (Fleury, strategy and new businesses) enriched although he is in Sales Nav: his Sales Nav row says "Fleury Group", which the join cannot take without also taking the French "Fleury" rows.
- Aliases in companies.csv / companies-verified.csv: "Fleury Lifecare (Grupo Fleury / Grupo Fleury S.A.)", "Med-Rio Check-up (MED-RIO)".
- CCML: nobody in Apollo by domain or by name. TOMA Health (Mexico): nobody.
