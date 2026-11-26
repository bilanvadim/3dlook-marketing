# Responses Summary — 2026-10-29-us-insurance-underwriting (as of 2026-11-25)

## Counts
- Total responses: 2
- Interested: 0
- Maybe-later: 0
- Referrals: 0
- Decline: 1 (50%)
- Negative: 0
- Questions: 1 (требует личного ответа Вадима перед отправкой — accuracy claim)
- OOO: 0

## Interested — for sales handoff

None in this batch.

## Questions — Vadim needs to reply personally

### David Peters — Director of Underwriting — Bestow
- Replied to: Message 1
- Their message: «Interesting. Do you have any studies showing accuracy?»
- Question: whether we have studies/validation data for FitXpress accuracy.
- Suggested draft answer (Vadim, edit to taste — draft is in CSV `suggested_reply_draft`, first line is a `[CHECK: …]` flag, not a `[VADIM: …]`):
> «Hi David, no peer-reviewed studies yet, these are internal results. In testing against expert pattern-maker measurements, accuracy was about 96-97%, typical error 1.5-2.0 cm; scan-to-scan differences were usually under 1 cm. Full methodology is available under NDA. Framework: https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/ Happy to talk through how that applies to instant-issue cases. Nick»
- Why it needs a personal look before Hlib sends it: the draft states exact accuracy figures (96-97%, NDA-only methodology, not peer-reviewed) to an underwriting partner evaluating us for instant-issue cases — the kind of external claim `accuracy-formulations.md` says must always carry its conditions and never be left bare. Confirm the figures and framing are fine to send as-is before it goes to Closely.
- Full thread: `messages/david-peters-9b1b6898.md` + response in CSV

## Negative responses — pattern check

0 negative out of 2 (0%). Nothing to flag.

## Decline — for the record

### Jennifer Dalton — Director of Accelerated Underwriting — Munich Re Life US
- Replied to: Message 1
- Their message: «Unfortunately, I am not on the alitheia product.»
- Reading: she disclaims ownership of the alitheia rules-designer angle the opener was built on; she did not name a colleague who does own it, so there is no referral to add. Treated as `decline`, confidence `medium` because the reply is ambiguous between "wrong person, ask elsewhere" and "not interested" — no further contact recommended without new information.
- Suggested reply draft: none (decline is on the empty-drafts list in the reply kit).

## Recommendations

- David Peters is the one response needing Vadim's personal sign-off before Hlib sends anything: confirm the accuracy figures/framing in the draft, then it goes to Hlib via the morning sheet import same as any other `question` draft.
- Jennifer Dalton needs no further action; she is excluded from future `alitheia`-angle outreach at Munich Re Life US per the decline category, but the registry entry (step 9, `outbound-registry.py reply`) should join on her `linkedin_url` since no new contact was named.
- Sample size is 2: no messaging pattern conclusions should be drawn from this batch alone.
