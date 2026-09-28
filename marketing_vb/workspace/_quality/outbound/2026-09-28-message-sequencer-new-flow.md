---
artifact: message-sequencer (step 5), old flow vs card + batch file
campaign: 2026-09-14-eu-erakulis-similar, batch Yazio (22 people)
date: 2026-09-28
---

# message-sequencer: the same 22 people, written twice

Same model (sonnet), same people, same day. The old run read the hypothesis, the product
files and built its own profile dump; the new run read `card-messages.md` and
`_profiles-yazio.md` and wrote one batch file that `split-messages` cut and checked.

| | old flow (shipped) | new flow, first try | new flow, after the fix |
|---|---:|---:|---:|
| Requests | 34 | 9 | 8 |
| Tokens processed | 4.58M | 1.27M | 0.93M |
| Gate rounds to exit 0 | n/a (hand-checked) | 2 | 1 |
| "80+" in the pair | 22 | 2 | 20 |
| "45 seconds" in the pair | 22 | 7 | 20 |
| Scale or integration number (34,000 · 112,100 · 2-4 weeks) | 22 | 0 | 8 |
| Distinct Message 2 openers | 22 | 2 ("Following up." ×20) | 22 |

## What the first try got wrong, and why

0 of 22 pairs carried a number. The hypothesis does demand one ("Message 1 gate", inside
Validation criteria), but the card cut only the rules sections, and the gate did not check
it. Three fixes: the card now carries the message-gate bullets, the agent prompt states the
rule, and `check-messages` fails a pair with no number when the hypothesis has a message
gate (and notes it otherwise, because `2026-09-27-uk-bariatric-prequal` was approved with
article-led pairs that cite none).

## What is still different

The two people without "80+" or "45 seconds" are the referral asks, which are exempt.
The shipped pairs each carried one of the two anonymous scale proofs because the
coordinator's prompt pushed them; the new pairs do so in 8 of 22. The hypothesis asks for
a product specific, not for a scale proof. If every pair should carry one, that is a line
in the hypothesis's "Rules for steps 3-5".
