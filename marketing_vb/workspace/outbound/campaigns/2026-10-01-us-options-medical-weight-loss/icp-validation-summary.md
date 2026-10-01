---
product: fitxpress
campaign: 2026-10-01-us-options-medical-weight-loss
profile: nick
step: 4 (validate)
date: 2026-10-01
checkpoint: waived by Vadim 2026-10-01 («продовжуй без апруву»); this file is the record
---

# ICP Validation Summary — 2026-10-01-us-options-medical-weight-loss

## Stats

From `apply-decisions`:

- People in the list: 5 · **PASS 5** (P1: 2, P2: 1, P3: 2) · WEAK 0 · FAIL 0
- Excluded by registry: 0 (no `registry:` flags on any row)
- To send: 5 · `cap_per_group` 50

| Group | To send | Share | Cap |
|---|---|---|---|
| Options Medical Weight Loss | 5 | 100% | 50 |

| Angle | People |
|---|---|
| `at-home-scan` | 2 |
| `program-feature` | 1 |
| `referral` | 2 |

Precision Medical Weight Loss (Jeremy Osborne) and Weight Loss Options Firm (Alberto Ortega) are not in `people-compact.csv`. They were removed upstream with their companies, as the verdict table and decision 2026-10-01 #1 say.

## Proposed to SEND

| Group | Person | Title | P | Angle |
|---|---|---|---|---|
| Options Medical Weight Loss | Jeremy Castle | Chief Executive Officer | 1 | at-home-scan |
| Options Medical Weight Loss | Jessica Tarnawa | Director of Medical Operations (NCO) | 1 | at-home-scan |
| Options Medical Weight Loss | Jory Del Cecato | Senior Director | 2 | program-feature |
| Options Medical Weight Loss | Joshua Hicks | Clinic Director | 3 | referral |
| Options Medical Weight Loss | Nicholas Foy | Clinic Director | 3 | referral |

All five match the card's persona table row for row (tier and lane).

## WEAK — нужно решение Вадима

None.

## Кого оставили за бортом: пулы

`skipped`: 0 not sent, 0 senior. No pools.

The only gap is outside the export: the COO, CMO and a technology lead appear on Options' leadership page but were not pulled. Decision 2026-10-01 #4 keeps the list as pulled. If Vadim pulls them, they go through `outbound-registry.py check`, `compact`, a decisions row and `apply-decisions` (COO and CMO fit `at-home-scan`, the technology lead fits `technical-integration`); `promote` cannot add people who are not in `people-validated.csv`.

## Top concerns

- **No one in the export owns the patient app or the vendor build.** Who owns Options Health Coach and the telehealth stack is not known; the COO, CMO and a technology lead are likely candidates, and none of them is in the list. Castle (P1) is the direct route; the two `referral` asks are the second.
- **Two of five rows rest on inference.** Del Cecato's title names no function, and his P2 `program-feature` lane comes from the card's reading of his headline and skills. His only earlier role in the compact row is Retail Sales Manager at GNC. Tarnawa's "NCO" is undefined, so copy should not expand it.
- **Job-change risk on both Clinic Directors.** Foy's headline is now "Healthcare Sales & Operations Leader", which matches the card's note that he is exploring pharma or device sales. Hicks has a thin, student-era profile. Both stay per decision 2026-09-29 #7. The card's stop condition still applies before send: if a profile shows the person has left, drop them and do not replace them from outside the export. This step could not run that check, because the compact list has no current-role dates.
- **One company, five people, one profile.** Everyone at Options gets the invite at the same time (no waves). Five parallel sequences to one account means the people may compare notes. The lanes should read as different asks, not one message sent five times.

## Vadim — decisions on record (checkpoint waived 2026-10-01)

1. SEND list: 5 people, as above. Applied.
2. WEAK: none.
3. Pools: none. The COO, CMO and technology lead are added only if Vadim pulls them (registry check → compact → decisions row → apply-decisions).
4. Cap: 5 of 50, no pressure.

## Coordinator note 2026-10-01 (pre-send stop conditions, card line 74)

- **Person level:** the 2026-09-28 export (Vadim's enrichment) lists Options as the current role for both Clinic Directors; Foy's headline signals a job search, which the referral lane tolerates.
- **Account level:** web search on 2026-10-01 found no sale, merger, bankruptcy or wider shutdown at Options, and no sign that Options runs a phone body scan or has signed a scanning vendor. The 2026-08-19 clinic closures are already in the hypothesis and stay out of the copy.
- All three stop conditions are clear; the five sequences go.

