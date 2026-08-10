---
product: fitxpress
profile: nick
market: USA
campaign: 2026-08-07-us-digital-fitness
step: icp-validation (merged)
validated: 2026-08-10
total_scored: 643
---

# ICP Validation Summary — US Digital Fitness Campaign (merged, all 4 batches)

**Input:** `people-raw.csv` (643 contacts after normalization; 566 target + 77 NOISE rows)
**Output:** `people-validated.csv` (643 rows, merged from batch1..4)
**Method:** Conductor icp-validator (jobs #71–#74, 4 parallel batches of ~160, profile `nick`)

## Headline numbers

| Verdict | Count | % of 643 |
|---|---|---|
| PASS | 152 | 23.6% |
| WEAK | 96 | 14.9% |
| FAIL | 395 | 61.4% |

PASS by priority: **P1 = 44**, **P2 = 60**, **P3 = 48**.

**Message target set: PASS + WEAK = 248 contacts** → split into `people-validated-msg-batch1.csv` (124) + `people-validated-msg-batch2.csv` (124) for sequencing.

## Per-batch breakdown

| Batch | PASS | WEAK | FAIL | Total | Job |
|---|---|---|---|---|---|
| batch1 | 62 | 32 | 67 | 161 | #71 |
| batch2 | 40 | 29 | 92 | 161 | #72 |
| batch3 | 35 | 19 | 107 | 161 | #73 |
| batch4 | 15 | 16 | 129 | 160 | #74 |

## PASS + WEAK by target company

| Company | PASS | WEAK | PASS+WEAK |
|---|---|---|---|
| Personify Health | 30 | 33 | 63 |
| iFIT | 42 | 14 | 56 |
| MyFitnessPal | 16 | 12 | 28 |
| Tonal | 13 | 8 | 21 |
| Hydrow | 10 | 7 | 17 |
| Calibrate | 10 | 4 | 14 |
| Future | 5 | 8 | 13 |
| Echelon | 8 | 2 | 10 |
| Ladder | 8 | 1 | 9 |
| Found | 3 | 3 | 6 |
| Fitbod | 3 | 3 | 6 |
| Trainwell | 3 | 0 | 3 |
| Shotsy | 1 | 1 | 2 |

## Message angle distribution (PASS + WEAK, 248 contacts)

| Angle | Count |
|---|---|
| member-engagement | 130 |
| technical-integration | 60 |
| weight-management | 30 |
| digital-transformation | 28 |

## FAIL breakdown (395 total)

- **NOISE / off-target rows (homonym companies, funds, day-job people): 77** — auto-FAIL, no research cost.
- **Target-company contacts in non-buyer roles: 318** — the only real "missed" bucket; mostly HR/Talent, Engineering, Finance, Analytics, QA, ops/sales roles not matching the buyer persona.

## Notes
- Batch 2 (job #72) output CSV had stray `\r` separators breaking csv structure (323 parsed rows vs 161); repaired locally (161 rows) and 6 rows with unescaped quotes in profile_summary were reconstructed manually from field shift.
- Recommend: proceed with message sequencing for the 248 PASS+WEAK contacts in 2 Conductor jobs (P1→P2→P3→WEAK order).
