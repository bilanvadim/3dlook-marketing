# Apollo pulls — 2026-10-29-us-insurance-underwriting

Written by `scripts/apollo-pull.py`. Credits are Apollo's own `credits_consumed`.

## 2026-11-05 search
- companies 32, 67 titles
- candidates 1791, other employer 0, already in Sales Nav 0

## 2026-11-05 selection before enrich (Vadim's decision)
- Hlib's Sales Nav sheet 1FjQnu… («nick - Enrichment data 2026-11-04», 616 rows) NOT used: Seniority «Owner/Partner» pull — Nationwide agency owners, NM advisors, Principal EAs, name-alikes; 1 persona fit (Ethos co-founder). Not saved to sales-nav-raw/.
- The search above ran through a scratch wrapper adding `person_locations[]=United States` (the script has no location filter; reinsurer domains are global).
- Vadim 2026-11-05: Apollo, at most 15 per company. Coordinator pre-filter on titles: hypothesis NOT list + P&C lines (auto/home/farm/commercial…), director level and up; ranked C-level/founder → SVP/EVP → VP → Head → AVP/medical director → director → associate director, underwriting/medical/new-business titles first within a level; top 15 per company.
- 1,791 candidates → 395 `candidate`, 1,396 `not-selected` (pool kept in apollo-candidates.csv for later widening).

## 2026-11-05 enrich → apollo-2026-11-05.csv
- written 393, skipped 2, credits 395
  - skipped Joshua Sp***r: no LinkedIn URL
  - skipped Magdalena Kl***o: current employer is ? (?)

## 2026-11-05 enrich → apollo-2026-11-05-2.csv
- written 13, skipped 0, credits 13
