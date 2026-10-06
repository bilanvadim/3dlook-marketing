# Apollo pulls — 2026-10-06-uk-weight-management

Written by `scripts/apollo-pull.py`. Credits are Apollo's own `credits_consumed`.

## 2026-10-06 search
- companies 17, 42 titles
- candidates 97, other employer 0, already in Sales Nav 16

## 2026-10-06 search
- companies 17, all functions
- candidates 658, other employer 0, already in Sales Nav 75

## 2026-10-06 search
- companies 18, all functions
- candidates 660, other employer 0, already in Sales Nav 75

## 2026-10-06 coordinator trim before enrich

The all-functions search (Vadim: «Якщо по деяким компаніям не всі співробітники, добрати іх в аполо») wrote 660 candidates over 18 companies; the full file is kept as `apollo-candidates-all-2026-10-06.csv`. `apollo-candidates.csv` was trimmed to the seven `apollo_topup: yes` accounts (MoreLife, Reset Health, LighterLife, Medicspot, Counterweight, Habitual, PronoKal UK), status `candidate` only, minus junk titles (HR, recruitment, administrators, finance/payroll, cleaners, graphic designers, software/QA engineers, bid writer, and non-health titles from name-alike "Habitual" businesses). Cap raised to 75 by Vadim the same day.
PronoKal UK: the two Apollo candidates (Médico Prescriptor, Dependienta y Comercial) are Spain staff, dropped; Philip Bazire stays the only PronoKal UK person. 128 to enrich.

## 2026-10-06 enrich → apollo-2026-10-06.csv
- written 127, skipped 1, credits 128
  - skipped Jo-Lee Da***s: current employer is GivenGain (givengain.com)
