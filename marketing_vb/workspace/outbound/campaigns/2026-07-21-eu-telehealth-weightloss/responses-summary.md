# Responses Summary — 2026-07-21-eu-telehealth-weightloss (as of 2026-09-02)

**Re-run.** The earlier pass classified only 4 of this campaign's replies (3 unique
contacts) because Closely's inbox listing hid two-thirds of the responses.
`responses-raw.csv` has since been rebuilt from the authoritative per-campaign contact
drill and now holds 5 replies (4 unique contacts), each with a `thread_file`. This file
and `responses-classified.csv` replace that partial output entirely. This is Olena's
profile (Continental Europe): all 5 replies came back in English, so no translation was
needed — the exact original wording is quoted rather than paraphrased below and in the
CSV, per instruction.

## Counts
- Total responses: 5 (4 unique contacts, 307 messages sent — 1.3% reply rate)
- Interested: 0 (0%)
- Maybe-later: 0
- Referrals: 0
- Decline: 3 (60%)
- Negative: 0 (0%)
- Questions: 0
- OOO: 0
- Other/unclear: 2 (40%) — both from the same contact, Alex Hill, Sidekick Health

## Interested — for sales handoff
None in this pull.

## Questions — Vadim/Olena needs to reply personally
None in this pull.

## Decline — exclude from future campaigns

### Janne Kanervisto — Chief Medical Officer, Head of Sleep Medicine — Terveystalo
- Replied to: Message 1 (clinical-operations angle, WEAK tier)
- Their message: «Hi! Thank you but I'm not interested.»
- No door-open, no referral. He was already flagged `classification: WEAK` in his own
  thread file — sleep medicine, not weight-management — so this may be a targeting miss
  inside Terveystalo's 170-contact block as much as a messaging problem.

### Philipp Sauer — Head of Privacy (Senior Legal Counsel) — Oviva
- Replied to: Message 1 (compliance angle, PASS_P3 tier)
- Their message: «Not interested»
- Curt but not hostile — decline, not negative. Flagged `classification: PASS_P3`
  (tertiary persona) in his own thread — again plausibly a targeting-tier issue, not a
  message-quality issue.

### Peter Csonka — Director — Tampere Center for Child, Adolescent and Maternal Health Research - TamCAM
- Replied to: Message 1 (clinical-operations angle, WEAK tier)
- Their message: «Hi, thank you for your message. We are not interested at the moment.»
- The "at the moment" phrasing is softer than the other two declines, but there is no
  explicit ask to follow up later, so this is scored `decline` (medium confidence) rather
  than `maybe-later`. TamCAM is a maternal/child-health research center, not a
  weight-management or telehealth program — this contact plausibly should not have been
  on the list at all.

## Other/unclear — Alex Hill, Sidekick Health (job change)
- **2026-08-12**: «Hey, I'm actually no longer at Sidekick but wishing you all the best!»
  — not a refusal of the pitch, a departure notice. Sidekick Health is a named pure-play
  target in `hypothesis.md`; the account isn't dead, the contact is stale.
- **2026-08-30**: «All good!» — arrived 18 days later. `which_message_replied_to` says
  message 1, but the content reads like an acknowledgment of something in between (not
  present in this raw pull, likely an Olena reply to the departure notice that the export
  didn't carry).

## Negative responses — pattern check

Zero negative (angry / "stop contacting me") responses — nothing here crosses into that
category. All 3 declines are short, polite refusals with no hostility and no door-open
language. The 60% decline rate looks high for a 5-response sample, but 2 of the 3
decliners (Kanervisto, Sauer) were already scored WEAK/PASS_P3 — secondary/tertiary fits —
before they ever replied, and the third (Csonka) sits at an off-ICP research organization,
not a weight-management/telehealth target. This reads as an ICP-validator tiering and
list-quality issue more than a messaging problem, but the sample (5 of 307) is too small
for a confident verdict either way.

## Recommendations
- Reply rate (5 responses / 4 unique contacts out of 307 sent = 1.3%) is well below the
  campaign's ≥5% target, and interested count (0) is below the ≥4-qualified-leads target.
  This fuller pull (5 vs. the earlier partial 4) doesn't change that read — confirm with
  Vadim whether more responses exist in closely.io before treating this as final.
- Mark all three decliners excluded from future FitXpress campaigns: `835d9c042c71`
  (Philipp Sauer), `d9c1169479fc` (Janne Kanervisto), and `1423ee4ade13` (Peter Csonka).
- Sidekick Health: don't drop the account over Alex Hill's departure — flag for a
  replacement contact search (Product/Clinical Ops lead), since it's a named pure-play
  target in the hypothesis.
- Peter Csonka's organization (TamCAM, a child/maternal-health research center) looks like
  it may not belong on a weight-management/telehealth contact list at all — worth checking
  how it entered the 456-contact pull before the next campaign in this vertical.
- For future pulls: `responses-raw.csv` still only captures Alex Hill's two ends of a
  longer exchange, not what Olena sent in between. Worth checking with Vadim whether the
  export can carry full thread history per contact, not just the latest inbound message.
- No sales handoff needed from this pull — 0 interested, 0 questions.
