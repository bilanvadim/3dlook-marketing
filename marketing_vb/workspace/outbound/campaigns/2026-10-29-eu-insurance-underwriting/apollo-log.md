# Apollo pulls — 2026-10-29-eu-insurance-underwriting

Written by `scripts/apollo-pull.py`. Credits are Apollo's own `credits_consumed`.

## 2026-11-02 search
- companies 32, 37 titles
- candidates 930, other employer 1, already in Sales Nav 44
- location: `person_locations[]` added per row by a session wrapper (apollo-pull.py has no location filter): group A the entity's country, group B the head-office country, group C Germany + Ireland
- free persona pre-filter (session script, hypothesis Target buyer persona): seniority + persona words, P&C/GI/claims/sales/individual-contributor words out, multi-line groups and reinsurers need a life/medical/biometric word; `munichre.com` searched twice (Munich Re Germany, Munich Re Automation Solutions) → 213 `duplicate`
- after pre-filter: candidates 90 (≤ 100 credits, Vadim's decision 13: no separate approval), `persona-out` 794, `duplicate` 213, `in-sales-nav` 44

## 2026-11-02 enrich → apollo-2026-11-02.csv
- written 81, skipped 9, credits 90
  - skipped Michael Ve***y: current employer is Zurich Insurance (zurich.com)
  - skipped Laura Co***n: current employer is Zurich Insurance (zurich.com)
  - skipped Shane Fa***y: current employer is Zurich Insurance (zurich.com)
  - skipped Colette Ho***n: current employer is Zurich Insurance (zurich.com)
  - skipped Cormac Fr***y: current employer is Zurich Insurance (zurich.com)
  - skipped Niall Wa***h: current employer is Zurich Insurance (zurich.com)
  - skipped Anthony Fs***i: current employer is Laya healthcare (layahealthcare.ie)
  - skipped Kevin Wr***n: current employer is Laya healthcare (layahealthcare.ie)
  - skipped Clare Fs***i: current employer is Laya healthcare (layahealthcare.ie)

## 2026-11-02 enrich → apollo-2026-11-02-2.csv
- written 6, skipped 0, credits 6
  - the 6 Zurich Life Ireland people re-enriched with zurich.com accepted as the row's domain (Apollo lists Zurich Life Assurance plc staff under Zurich Insurance); Laya healthcare 3 stay skipped (private health, Anti-cases)
