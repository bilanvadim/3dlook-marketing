# Apollo pulls — 2026-10-22-uk-insurance-underwriting

Written by `scripts/apollo-pull.py`. Credits are Apollo's own `credits_consumed`.

## 2026-10-23 search
- companies 23, 32 titles
- candidates 1025, other employer 0, already in Sales Nav 41

## 2026-10-23 search
- companies 14, 32 titles
- candidates 494, other employer 0, already in Sales Nav 0
- (coordinator) the search above ran over all 23 companies with no location filter: 1025 candidates, reinsurers and Zurich global. Replaced by the run below.

## 2026-10-23 search, gap only (coordinator)
- only the 11 shortlisted companies Sales Nav export-1.csv left empty; `person_locations[]=United Kingdom`; cmd_search reused unchanged via a scratch wrapper (no repo code change)
- domains tried: zurich.co.uk (0) → zurich.com; guardianfs.co.uk (0) → guardian1821.co.uk; hannover-re.com; ipipeline.com + uk.ipipeline.com (3 duplicates)
- 494 candidates → free persona pre-filter from hypothesis.md:91/:236 (P&C/GI lines, plain individual underwriters without development/philosophy/rules/research): 135 `candidate`, 356 `persona-out`, 3 `duplicate`
- enrich NOT run: 135 credits > 100, waiting on Vadim

## 2026-10-23 enrich → apollo-2026-10-23.csv
- written 135, skipped 0, credits 135

## 2026-10-23 search
- companies 12, 32 titles
- candidates 520, other employer 0, already in Sales Nav 59
- enrich 2026-10-23 (gap): Vadim «апрув по аполо», 135 credits, 135 written → `sales-nav-raw/apollo-2026-10-23.csv`. Gap candidates file kept in coordinator scratch.

## 2026-10-23 search, title top-up for the Sales Nav companies (coordinator)
- why: all three validators found the Sales Nav export was pulled company-wide, not by title: no Chief Underwriter / CUO / CMO / development or philosophy underwriter at any of the 12 companies
- the 12 companies Sales Nav covered, hypothesis titles, `person_locations[]=United Kingdom`, cmd_search reused via scratch wrapper: 520 candidates (55 already in Sales Nav)
- free pre-filters: persona (P&C, plain underwriters) → 253; multi-line groups (Aviva, L&G, Royal London, LV=, Scottish Widows) keep only protection-side titles, drop group protection / retirement / PMI / GI lines → **144 `candidate`**
- enrich NOT run: 144 credits, waiting on Vadim

## 2026-10-23 enrich → apollo-2026-10-23-2.csv
- written 143, skipped 1, credits 144
  - skipped Jon Fu***r: current employer is CEMAP (grupocemap.org)
- enrich 2026-10-23 (title top-up): Vadim «апрув», 144 credits, 143 written → `sales-nav-raw/apollo-2026-10-23-2.csv` (1 skipped: Jon Fuller now at CEMAP; already in the Sales Nav export). extract: 142 new (1 duplicate of a Sales Nav row), 1,283 people in total.
