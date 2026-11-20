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
