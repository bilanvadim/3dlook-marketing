# Responses Summary — 2026-07-23-israel-telehealth (as of 2026-09-02)

**This is a re-run, third time, and this time on the campaign that actually belongs to this
folder.** The two prior classifications (4 rows, then 22 rows) both mixed in a Closely campaign
that does not belong here. `responses-raw.csv` has been rebuilt from Closely campaign `138170`
alone — the one created 2026-07-24 whose `message_1`/`message_2` copy matches this folder's
`messages/*.md` files verbatim — and now holds the correct **5 replies**. The 22-row version
mixed in campaign `125317` ("Israel top wellness use case c-level", created **2026-04-04**, an
unrelated earlier campaign with different copy imported via `GPT1`/`GPT2`/`GPT3` columns that
appear nowhere in this folder). Eight of April's decliners had been re-imported into this July
campaign, which is why contact overlap made the merge look plausible. This file and
`responses-classified.csv` replace the 22-row versions entirely — nothing from that layout was
reused.

## Read this before the numbers below

**This folder's real result is 127 invites → 38 accepted (29.9%) → 73 messages → 5 replies
(6.8% on messages sent, 13.2% on accepted).** Not the bigger funnel quoted in earlier drafts of
this analysis — that number is 79% April campaign.

**The four leads previously reported as `interested` for this campaign — Olchov Zhanna, Ben Ron,
Ron Weksler (all Maccabi), and Yaron Sheffer (Clalit) — belong to April's campaign (`125317`), not
this one.** They never received this folder's messages. They are not lost: two of them (Ben Ron —
`benr@mor.org.il`, Ron Weksler — `Wekslerrs@gmail.com`) gave direct email addresses and were never
answered, and as of today they are **95-144 days cold** (replies dated 2026-04-11 through
2026-05-30). They simply have no campaign folder here to be reported against — `125317` is not
documented anywhere in `workspace/outbound/campaigns/`. Someone should work those four leads today
regardless of which folder owns them; this document is not the place to do it, since it would mean
carrying April's rows forward into a July campaign's output, which is exactly the error being
corrected.

**This campaign, on its own copy and its own list, produced zero interested and zero negative
replies.** Its one substantive result is a live product question from Guy Sade (TytoCare) that
needs a personal answer.

## Data notes

- **`person_id` is empty on every row of `responses-raw.csv`.** This folder's people files
  (`people-to-sequence.csv`, `people-validated.csv`) key on `linkedin_url`, not `person_id`.
  `responses-classified.csv` uses **`linkedin_url` as the row identity** in the column where
  `person_id` would normally go, and carries `linkedin_url` through as its own column so that
  `outbound-registry.py reply` (step 9) can join on it — without that column the command matches
  0 rows and still reports success, which is what happened on an earlier run.
- No `hypothesis.md` exists in this campaign directory. `context-pack.md` was read instead: it
  supplies ICP segments A-F, approved claim ids FX-001..FX-008, banned claims, the HMO procurement
  note, and the katya tone note.
- All 5 replies are in English; no Hebrew text appeared in this batch, so there was nothing to
  translate. Original wording is quoted throughout, not paraphrased.
- `thread_file` was filled for 4 of 5 rows. For the fifth (Yael Ben Atar), no `thread_file` value
  was present in the raw export; grepping `messages/` by LinkedIn URL fragment found her thread at
  `messages/b01-4.md` — but it is addressed to "Yael Shaham, Board Member, Clalit Health
  Services," not "Yael Ben Atar." Same LinkedIn URL (`/in/yael-ben-atar-8aba53228`), different
  name on our file than in Closely's reply record; the URL slug agrees with Closely, which
  suggests our name/title record is the one that's wrong. Flagged, not resolved, in the
  classification below.
- One person (Netanel Friedman) replied twice, 4 days apart, to the same thread: a substantive
  decline on 2026-08-06, then a two-word sign-off ("Thanks, have a good day") on 2026-08-10. Both
  rows are in the CSV as required by the raw export, but they are one person and one signal, not
  two.

## Counts

- Total response rows: 5
- **Unique people: 4** (Netanel Friedman replied twice)
- Interested: 0 (0%)
- Maybe-later: 1 (20%)
- Referral: 0 (0%)
- Decline: 2 (40%)
- Negative: 0 (0%)
- Question: 1 (20%) ← **requires Vadim/Katya's personal reply**
- OOO: 0 (0%)
- Other/unclear: 1 (20%) — the second half of Netanel Friedman's two-part reply; folds into his
  decline row and is not an independent signal

## Interested — for sales handoff

**None this campaign.** Zero of this folder's 5 replies are interested. (The four Maccabi/Clalit
interested leads circulating in earlier drafts of this analysis are from the unrelated April
campaign `125317` and are addressed in "Read this before the numbers below," not here — reporting
them under this campaign's handoff section would repeat the exact merge error this re-run exists
to fix.)

## Questions — Vadim/Katya need to reply personally

### Guy Sade — Senior Director, Account Management — TytoCare
- Replied to: Message 2 (the account-growth/upsell follow-up)
- Question: «Does your product has FDA / CE approvals?»
- Context: the sequence pitched FitXpress as an upsell TytoCare's account managers could bundle
  alongside existing remote-exam tools. He needs the regulatory scope confirmed before considering
  that pitch for his managed accounts.
- Constraint: `context-pack.md`'s banned claims forbid claiming FDA-cleared or medical-device
  status — the answer has to state the real scope (HIPAA-compliant, GDPR-aligned, audit-ready,
  not positioned as a medical device), not dodge the question.
- Suggested draft answer (Vadim/Katya, edit to taste):
> «Hi Guy, good question to ask upfront. FitXpress isn't FDA-cleared or CE-marked as a medical
> device, and it isn't positioned as one. It's built for verified body measurement and composition
> data, HIPAA-compliant and GDPR-aligned, with audit-ready records. If that scope works for how
> you'd want to complement TytoCare's exam data, happy to go deeper on where it fits.»
- Full thread: `messages/b04-3.md` + response in CSV.

## Maybe-later — nurture

### Yael Ben Atar (recorded internally as Yael Shaham, Board Member) — Clalit Health Services
- «It sounds interesting! However, this is outside my role at Clalit, so I'm not the right person
  to help with this 🙏🏼» — reads as maybe-later per the campaign rule ("sounds interesting,
  but..." is not interested), not a referral, since she names no alternate contact.
- Do not exclude. Before any follow-up: manually verify her current name/title on LinkedIn — our
  file and Closely's reply record disagree on who she is, and her stated reason ("outside my
  role") is consistent with our record being wrong rather than just stale. Once verified, ask who
  at Clalit would be the right owner instead of closing her out.

## Decline

### Gali Atar — Head of Child Development Services Department, Health Division — Maccabi Health care Services
«Not my subject. Tnx.» Clean, polite decline, no re-engagement offered. She is one of 8 people
who had already declined 3DLOOK's unrelated April campaign and were re-imported into this July
list; she declined again.

### Netanel Friedman — Head of Finance | Sr. Director FP&A — TytoCare
«It looks interesting, but it's not something that's relevant to our current priorities or
business model. I appreciate you thinking of us, and I wish you the best of luck with FitXpress.»
Structural, company-fit decline, not a timing one — no offer to revisit. His follow-up "Thanks,
have a good day" four days later is a sign-off, not a second signal.

Both exclusions are person-level. Nothing here justifies excluding TytoCare as a company: Guy
Sade, at the same company, is a live open question.

## Negative responses — pattern check

None this batch (0 of 5, 0%). Too small a sample (5 replies, 4 people) to draw a messaging
pattern from on its own; see `post-mortem.md` for the pattern analysis run on the corrected,
per-campaign numbers (0 hostile replies across both Israel campaigns, and a targeting rather than
messaging explanation for the decline rate).

## Recommendations

1. **Answer Guy Sade inside the banned-claims boundary** — not FDA-cleared, not a medical device,
   HIPAA-compliant/GDPR-aligned, audit-ready. Draft above.
2. **Do not exclude TytoCare as a company.** Exclude Netanel Friedman only; Guy Sade's thread is
   still open.
3. **Manually verify the Yael Ben Atar / Yael Shaham record** before any re-approach, then follow
   up asking who the right Clalit contact is.
4. **Run `outbound-registry.py reply --campaign 2026-07-23-israel-telehealth --profile katya`
   (without `--dry-run`) on this 5-row classification**, joining on `linkedin_url`, so Gali Atar
   and Netanel Friedman are excluded and Yael Ben Atar is tagged for nurture in
   `workspace/outbound/exclusions/katya-registry.json`. This file only prepares that input; it
   does not write to the registry itself.
5. **Separately from this campaign's scope**, someone needs to work the four cold April leads
   (Olchov Zhanna, Ben Ron, Yaron Sheffer, Ron Weksler) — two have waiting email addresses,
   95-144 days old. They need their own campaign record (`125317` has none in this account) before
   they can be reported through this pipeline correctly; until then they should not be folded into
   this folder's numbers again.
6. **Fix the pull so this doesn't happen a fourth time.** Whatever produced the merged
   `responses-raw.csv` twice should filter on Closely `campaign_id` (or `created_at` within the
   campaign's launch window), not on contact overlap across campaigns.
