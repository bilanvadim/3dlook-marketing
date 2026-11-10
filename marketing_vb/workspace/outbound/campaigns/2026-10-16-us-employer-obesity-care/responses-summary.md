# Responses Summary — 2026-10-16-us-employer-obesity-care (as of 2026-11-09)

## Counts
- Total responses: 4
- Interested: 0
- Maybe-later: 0
- Referrals: 0
- Decline: 1 (25%)
- Negative: 0
- Questions: 2 (50%) ← требуют личного ответа
- OOO: 0
- Other/unclear: 1 (25%) ← возможный referral, ещё без имени

## Interested — for sales handoff

None this round.

## Questions — Vadim needs to reply personally

### Ryan Adams — Pharmacist in Charge/Site Director — eMed
- Replied to: Message 1 (opener)
- Their message: «Hey Nick, thanks for connecting! 3DLOOK caught my eye. I have a kinesiology background and now work as a pharmacist, so body composition tracking, especially lean mass during weight management, is right in my wheelhouse. Curious how your health clients are using the scan data.»
- Question: how 3DLOOK's health clients actually use scan data (body composition, lean mass tracking during weight management).
- Why this is a strong signal despite being filed as "question" not "interested": he has direct domain expertise (kinesiology + pharmacy), volunteered it unprompted, and his ask is specific rather than generic — but he did not explicitly ask for a call, so per taxonomy rules this stays `question` (not `interested`) until he responds to a concrete next step.
- Suggested draft answer (Nick/Vadim, edit to taste):
> «Hi Ryan, good question. Programs like Yazen use the two-photo scan at each check-in, allowing coaches to see body composition changes alongside the logged weight and catch lean mass loss early during a weight-loss program. UK Meds uses the same scan for BMI verification at intake. Happy to walk through what a similar setup could look like for eMed: https://meetings.hubspot.com/nick-omelchak»
- Full thread: `messages/ryan-adams-3a5595120.md` + response in CSV

### Ryan Adams — follow-up — eMed (Unitree G1 robot camera question)
- Replied to: Message 1, per the thread export, though this is chronologically a later message (2026-11-04) from the same lead whose earlier scan-data question (2026-10-21) is analyzed above.
- Their message: «Could I stick the 3DLOOK into a Unitree G1 robot's camera (G1's are the humanoid robots you see online) and have it take an assessment in a clinical setting?» Sent in an informal tone, on his way into a meeting.
- Why this is unusual: it is a genuine, specific technical question, not a pitch objection or stall, so it is filed as `question`, not `other/unclear`. Confidence is `medium` (not `high`) because the right answer needs a technical read from product/engineering, not because the category itself is in doubt.
- Nothing in `outbound-reply-kit.md`'s existing answers (A1-A6) covers embedding FitXpress in a non-phone camera, so the draft below is flagged `[CHECK: ...]` rather than answered as settled fact.
- Suggested draft answer (Nick/Vadim, edit to taste — delete the CHECK line before sending):
> «[CHECK: confirm with product/eng whether the SDK's capture requirements could work with a non-phone camera feed like a robot's, before sending] Hi Ryan, that's a first for us. FitXpress runs as an SDK/API: two photos in, 80+ body measurements and body composition estimates out in under 45 seconds. We have not tested it against a robot's camera, so I cannot say yet if the G1's feed would meet our capture requirements. Want me to check with our product team and get back to you?»
- Full thread: `messages/ryan-adams-3a5595120.md` + response in CSV

## Decline

### Brent Hartman — Consultant Relations Director — Vida Health
- Replied to: Message 1 (referral/consultant-relations angle)
- Their message: «Nick, I'm the wrong person. You likely need someone on the product or clinical team. Bunch of new people there that I don't know.»
- Why `decline` and not `referral`: he names a function (product or clinical team) but explicitly says he doesn't know anyone there to point to, so there is no person to add to outbound. No suggested reply draft and no referral action per the reply-kit rule for this category — sheet marks it «не відповідаємо» unless Vadim decides otherwise.
- Full thread: `messages/brent-hartman.md` + response in CSV

## Other/unclear — possible referral, needs a human read

### Karen Olenski, MBA — Director, Client Success — MDLIVE
- Replied to: Message 1 (opener), which asked which parts of the MDLIVE app clients ask about during adoption reviews.
- Their message: «I don't manage our app»
- Why `other/unclear` and not `referral`: she corrected the premise of the opener (she isn't the app owner) but did not name anyone to redirect to, so there is nobody yet to add as a new outbound contact.
- Note: message 2 in her sequence already has a built-in fallback for exactly this case («Or tell me who owns the app roadmap.»), so the next outbound touch does not need a new draft from scratch — just needs to be sent, or answered now since she already replied.
- Suggested draft answer (Nick/Vadim, edit to taste):
> «Hi Karen, no problem, thanks for the quick reply. Could you point me to whoever owns the app roadmap or product side at MDLIVE? Happy to loop them in directly so this reaches the right person.»
- If she names someone: re-classify this response as `referral` and add the named contact to outbound per the one-profile-per-company-6-months rule.
- Full thread: `messages/karenolenski.md` + response in CSV

## Negative responses — pattern check

None this round (0 of 4 responses).

## Recommendations
- Reply to Ryan Adams personally and specifically — he has unusually relevant expertise (kinesiology + pharmacy, lean mass framing matches our body composition pitch almost exactly). Worth a direct, detailed answer rather than a generic template, and worth re-offering the call explicitly since he didn't ask for one yet.
- For Ryan Adams's robot-camera question, get a quick technical read from product/engineering before sending anything back — it's a genuine question, not a joke to brush off, but nothing in the reply kit covers it yet. Worth adding to `outbound-reply-kit.md` once an answer exists, since this kind of hardware-integration question may recur.
- Reply to Karen Olenski asking who owns the MDLIVE app roadmap. If she names a person, open a new outbound track for that contact instead of letting the thread die here.
- Brent Hartman needs no further reply; he has no name to give. Leave Vida Health open for a separately-sourced product/clinical contact rather than re-approaching Brent.
- Sample size is 4 — still too small to draw any messaging conclusions from this campaign.
