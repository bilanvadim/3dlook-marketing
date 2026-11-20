# Apollo pulls — 2026-11-19-us-connected-fitness

Written by `scripts/apollo-pull.py`. Credits are Apollo's own `credits_consumed`.

## 2026-11-19 search
- companies 24, 68 titles
- candidates 190, other employer 1, already in Sales Nav 0

## 2026-11-20 search
- companies 24, 68 titles
- candidates 158, other employer 1, already in Sales Nav 32

## 2026-11-20 gap selection (coordinator, Vadim «67 кредитів»)
- Hlib's Sales Navigator sheet (`sales-nav-raw/export-1.csv`, 305 rows, a seniority pull) arrived first; Apollo fills gaps only.
- Re-ran `search` after the sheet (dedupe against it): 158 candidates.
- Held without credits: Peloton (59, `held-peloton`: Hlib already has CPO, SVP and VP Product there) and 32 off-persona titles (`held-off-persona`: product marketing, design, safety, sales, FP&A, SKU/master data, hardware, Beachbody coaches' own businesses).
- Enriched: 67 (BODi 14, Trainerize 3, Jefit 2, RP Strength 1 for the <3-people gap; persona owners Hlib's pull missed at iFIT 15, Tonal 9, MyFitnessPal 7, Echelon 5, Future 2, Fitbod 2, Everfit 2, Lose It! 2, Centr 2, Ergatta 1).

## 2026-11-20 enrich → apollo-2026-11-20.csv
- written 66, skipped 1, credits 67
  - skipped Pat Do***e: no LinkedIn URL

## 2026-11-20 search
- companies 7, seniority owner,founder,c_suite,partner,vp,head,director
- candidates 38, other employer 0, already in Sales Nav 17

## 2026-11-20 top-up selection (coordinator, Vadim «Так, 58 кредитів»)
- Vadim asked whether 109 covers Sales Nav + Apollo for every company: Apollo had been enriched only for gaps (67). Top-up approved: Peloton persona rows and a seniority search for small companies.
- The 67 enriched earlier are now status `enriched` (enrich charges every `candidate` row again otherwise).
- Peloton: 42 of 59 `held-peloton` rows reopened (persona titles; design, marketing, quality, hardware, planning stay held).
- Free seniority search (owner, founder, c_suite, partner, vp, head, director) for Hydrow, Trainwell, Ladder, Fitbod, TrueCoach, Exercise.com, Jefit via a scratch wrapper around cmd_search, merged by apollo_id: 47 new rows; off-persona titles held (marketing, supply chain, brand, creative, copywriting, growth, commercial, sales, support). TrueCoach 0 found; Fitbod 0 new.
- To enrich: 58 (Peloton 42, Ladder 7, Hydrow 3, Trainwell 2, Exercise.com 2, Jefit 2).

## 2026-11-20 enrich → apollo-2026-11-20-2.csv
- written 57, skipped 1, credits 58
  - skipped Jack Te***y: no LinkedIn URL
