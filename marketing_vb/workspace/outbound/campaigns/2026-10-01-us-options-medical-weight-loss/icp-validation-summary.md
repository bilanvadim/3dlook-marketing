---
product: fitxpress
campaign: 2026-10-01-us-options-medical-weight-loss
profile: nick
step: 4 (validate)
date: 2026-10-01
checkpoint: waived by Vadim 2026-10-01 («продовжуй без апруву»); this file is the record
---

# ICP Validation Summary — 2026-10-01-us-options-medical-weight-loss

> **Superseded counts.** The sections down to the coordinator note record the first round (5 people). The current list is 14 people, 13 to send: see "Widening 2026-10-01" at the end.

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

## Widening 2026-10-01 (Apollo leadership pull)

Source: Vadim's decision 2026-10-01 «додай всіх» (card, "widening: Apollo leadership pull"). It supersedes decision 2026-10-01 #4. The checkpoint is waived, so this section is the record. The first five rows of `decisions.md` are unchanged; nine rows were added.

### Stats (from `apply-decisions`, run 2026-10-01)

- People in the list: 14 · **PASS 13** (P1: 4, P2: 3, P3: 6) · WEAK 0 · **FAIL 1** (Kenny Scott, left Options)
- Excluded by registry: 0. No `registry:` flag on any of the nine new rows. The registry check ran with the campaign's own record exempted, as the card says.
- Other flags on the new rows: none (no `empty-profile`, no `other-company-page`, no `geo:`).
- To send: 13 · `cap_per_group` 50
- Previous `people-validated.csv` kept as `people-validated-v1-2026-10-01.csv`

| Group | To send | Share | Cap |
|---|---|---|---|
| Options Medical Weight Loss | 13 | 100% | 50 |

| Angle | People | Who |
|---|---|---|
| `at-home-scan` | 5 | Castle, Tarnawa, Walker, Nelson, Collins |
| `program-feature` | 2 | Del Cecato, Pflanz |
| `referral` | 6 | Hicks, Foy, Stevens, Waclawski, Ruff, Leflore |

### The nine decisions

| Person | Title | Decision | P | Angle | Why |
|---|---|---|---|---|---|
| Matthew Walker | Founder | PASS | 1 | at-home-scan | Physician founder and former CEO, now on the board (card: P1). |
| Roscoe Nelson | Chief Medical Officer | PASS | 1 | at-home-scan, clinical register | CMO since 2026-03. Sets the clinical standard for what providers measure at follow-ups (card: P1). |
| Joe Pflanz | Chief Marketing Officer | PASS | 2 | program-feature | Promoted from Head of Marketing and Ecommerce at Options. Asks what the scan adds to the offer, from the marketing seat. Del Cecato asks from sales and growth (card: P2). |
| Krystle Collins | Regional Clinical Operations Director | PASS | 2 | at-home-scan, clinical register | Nurse practitioner running clinical operations across a region. Her question is regional; Tarnawa's is about the follow-up record (card: P2). |
| Kaytee Stevens | Regional Director | PASS | 3 | referral | Came up through Director of Service and Director of New Clinic Openings at Options. Her ask can center on service or new clinic openings. |
| Jami Waclawski | Regional Director | PASS | 3 | referral | Multi-unit operations and sales, aesthetics and weight loss. Her ask can center on regional sales. |
| Jacob Ruff | Clinic Director | PASS | 3 | referral | Promoted from Weight Loss Consultant and then Associate Clinic Director at Options. His ask can center on the consultation flow and check-ins between visits. |
| Justin Leflore | Clinical Director | PASS | 3 | referral | Kept under decision 2026-09-29 #7 (stale profiles stay): nothing in his row shows he left. See flags. |
| Kenny Scott | Regional Director of Sales & Operations | **FAIL** | | | Left Options for Crunch Fitness. See flags. |

The referral notes above give the sequencer a separate ask for each referral person. The single-account rule says these asks must differ from each other, from Hicks's (who decides the app) and from Foy's (who leads telehealth).

### Job-change flags

- **Kenny Scott: dropped (FAIL).** Apollo lists two current roles with the same title: Regional Director of Sales & Operations at Fitness Ventures (Crunch Fitness), and the same title at Options. His compact row puts "Regional Director of Sales & Operations at Options Medical Weight Loss" under **earlier roles**, right before a Senior General Manager role. So the export treats Options as his previous job and the Crunch Fitness role as his current one. For the eight other Apollo people, the current Options title is not repeated in earlier roles. The same title at a newer employer, after a fitness-club background, reads as a move to Crunch Fitness. Apollo had simply not closed the Options role. The card says to drop him if the profile shows he left (anti-case stop condition: drop and do not replace). This inference rests only on the compact row: his LinkedIn page was not opened. To reverse it, run `scripts/outbound_pack.py promote --campaign 2026-10-01-us-options-medical-weight-loss --names "kennysscott" --angle referral --pool A`. The script's printed hint adds `--wave 2`; leave it out, because there are no waves.
- **Justin Leflore: kept (PASS P3, referral).** His Apollo record was last refreshed 2025-10-27, almost a year old. His only earlier role is Managing Partner / Communications Director at The Lauren Group, LLC, which is an unusual path to a "Clinical Director" title. Nothing in the row shows he has left, so he stays under decision 2026-09-29 #7. The pre-send stop condition still applies to him.

### Pools (from `skipped`)

1 not sent, 1 senior: Kenny Scott (partnerships / BD / sales). It is a single person, not a pool. He is out because he left, not because the persona excludes his function. No other pools.

### Concerns added by the widening

- **Thirteen people at one account from one profile, all at once.** There are five `at-home-scan`, two `program-feature` and six `referral` sequences. Within each shared lane the question has to differ visibly, because these people work together and will compare notes. This applies most to Tarnawa, Nelson and Collins (all clinical register) and to the six referral asks.
- **Castle and Nelson share an employer.** Castle was COO at Arizona Urology Specialists (card), and Nelson's earlier roles include Senior Physician at Arizona Urology. They probably know each other well, so their two P1 sequences should not read as the same message.
- **Nelson is part-time.** His headline lists Urologist at Summit Urology alongside the CMO role, and he has been CMO only since 2026-03. Expect slower replies; the clinical register still fits.
- **Walker is now a board member, not the operator.** Castle runs operations, so Walker's P1 is sponsorship and access, not the day-to-day owner.
- **Still nobody owns the app or the vendor build.** The COO (Mark Wolbert) and a technology lead are not in Apollo either (card). The referral lane remains the route to them.

### Vadim — decisions on record (checkpoint waived 2026-10-01)

1. SEND list: 13 people (the first 5 plus 8 of the 9 Apollo people). Applied.
2. WEAK: none.
3. Kenny Scott: dropped as left for Crunch Fitness. Reversible with `promote` (command above) if his profile shows he is still at Options.
4. Cap: 13 of 50, no pressure.

### Coordinator correction 2026-10-01 (after QC 14/20)

- **Kenny Scott: FAIL reversed to PASS P3 `referral`** (`promote`, pool A, no wave; previous list kept as `people-validated-v2-2026-10-01.csv`). The card drops him only if the profile shows he left Options, and nothing verified that. Apollo lists both roles as current, and its people search returns Options as his current organisation (refreshed 2026-09-26). A web search on 2026-10-01 found nothing either way. The cross-row argument behind the FAIL was wrong: `earlier_roles` can hold current jobs (Walker's row does). The pre-send stop condition still applies to him.
- **Justin Leflore stays.** His referral ask (who sets clinical protocols for patients seen by video) lives in his messages, not in his decisions row. His history is longer than "The Lauren Group" (the compact row split that company's name at its comma).
