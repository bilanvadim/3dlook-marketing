---
artifact: icp-validator (step 4), model A/B on the compact inputs
campaign: 2026-09-14-eu-erakulis-similar
date: 2026-09-28
decision: keep opus
---

# icp-validator: opus vs sonnet on the new inputs

Both runs read `card-validate.md` + `people-compact.csv` (321 people) and nothing else,
wrote `decisions.md`, and ran `apply-decisions` + `skipped`. The reference is the list
Vadim approved on 2026-09-28: 125 people to send.

| | opus | sonnet | hand-run the same day (opus, 4 rounds) |
|---|---:|---:|---:|
| Requests | 9 | 18 | 46 |
| Tokens processed | 1.04M | 3.13M | 7.86M |
| PASS / WEAK / FAIL | 120 / 12 / 189 | 116 / 12 / 193 | 125 / 0 / 196 |
| Approved people it also sends | 119 of 125 (95%) | 115 of 125 (92%) | reference |
| Approved people it holds as WEAK | 5 | 4 | |
| Approved people it fails | 1 | 6 | |
| Sends someone not approved | 1 | 1 | |
| Same angle, where both send | 93 of 119 | 88 of 115 | |

opus and sonnet agree with each other on 311 of 321 people (96%).

## Reading it

- The threshold set before the run was 95% agreement on the approved SEND list. opus meets
  it, sonnet does not.
- Most of sonnet's six misses are people Vadim added **by name** against the letter of a
  pool rule (a COO and a Chief of Staff at companies that do have a product lead, a
  Technical PM, a "New Channels Lead" whose headline says user acquisition). sonnet applied
  the rule as written. That is defensible, and it is also not what the manager chose.
- Both models hold the same empty-profile executives as WEAK (Cristina G., Sebastian W.,
  Kenichi Takahira). On the hand run these went out; the flag is new.
- Both fail Andrii Savchuk (BetterMe PM, supplements background in the headline). The hand
  run passed him on the title alone. The headline is in the compact list for this reason.
- Both found the same name collisions by headline (KILO Akustik, Strefa Kilo).

## Decision

`icp-validator` stays on **opus**. sonnet re-read its own tables to check its counts and
ended up processing three times the tokens, so at list prices the two runs cost about the
same (roughly $1.5 against $2.5). The model choice moves the bill by a dollar per
campaign, and the list is the one artifact every later step inherits.

The saving in this step came from the inputs and from `promote`, not from the model:
7.86M → 1.04M tokens.
