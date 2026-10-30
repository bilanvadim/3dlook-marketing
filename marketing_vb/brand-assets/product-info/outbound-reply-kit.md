---
product: fitxpress
version: 2026-10-30
status: v1 — Hlib sends drafts built from it and asks Vadim when unsure (Vadim, 2026-10-30: «від мене не треба погодження»)
read_by: response-classifier (suggested_reply_draft, followup_draft, followup_draft_2)
---

# Outbound reply kit

Building blocks for replies to leads on LinkedIn. `response-classifier` writes the drafts from
this file into the sheet «3DLOOK Outbound — відповіді лідам»; Hlib sends them in Closely from the
sender's account and asks Vadim only when unsure. Named referrals are not sent by hand: the next
campaign of the same sender imports them with `followup_draft` and `followup_draft_2`. Why it exists: the pooled analysis of 2026-10-30
(`workspace/outbound/learnings/2026-10-30-pooled-analysis.md`) found the same four questions in
replies and no ready answer to any of them.

## Rules for every draft

- **Written as the sender**, signed with the first name only: Katerina, Nick, Olena, Kateryna,
  Vadim (the campaign's `profile`). Never "we at 3DLOOK are excited".
- **Reply in the lead's language** (LatAm leads write Portuguese or Spanish). English otherwise.
- **Under 500 characters.** One question answered, one next step. No em dashes. Hard bans and
  banned terms of the campaign apply (`brand-assets/style-guides/hard-bans-card.md`).
- **No client names.** "100+ clients" and "112,100 scans in 2025 across all 3DLOOK customers"
  are cleared; nothing else about customers.
- **Links only from this file.** Closely cannot attach files, so the overview goes as a Drive link.
- Facts only from the blocks below or `proof-points.md`. Anything to verify before sending goes
  on the first line of the draft as `[CHECK: …]`. Hlib deletes that line before sending, and an
  import refuses a referral message that still has one.

## Links

| What | Link | State |
|---|---|---|
| FitXpress overview (2-pager PDF, Drive) | `PENDING` | Refresh of the Feb 2025 2-pager in review with Vadim. Until this row has a link, offer "a short overview by email" instead of a link |
| Privacy, security and regulatory FAQ | https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/ | live |
| Sender calendars | `brand-assets/product-info/outbound-message2-template.md` (table by profile) | `vadim` has none: offer two time slots instead |

## Answers to the questions leads actually ask

**A1. "How is this different from our scale / body-composition device / a BMI-from-photo app?"**
(asked by 4 of 34 positive repliers). Never name the device or its maker.
> A scale or a device in the clinic gives a reading at the visit. FitXpress runs inside your own
> app: the person takes two photos at home, and you get 80+ body measurements, body composition
> estimates and a 3D model, under 45 seconds from the photos to structured results. That gives
> you data between visits, without hardware.

**A2. "Do you have FDA / CE approval?"**
> FitXpress is not cleared, authorized, or approved by the FDA. An independent regulatory
> assessment concluded that FitXpress does not meet the definition of a medical device under the
> UK MDR or EU MDR for its current intended purpose. The details are in our FAQ: {FAQ link}

**A3. "iOS and Android, or Android only?"**
> Both. We provide iOS and Android SDKs, a React SDK for web, and a REST API.

**A4. "Send me something I can share with the team."**
> Here is a two-page overview you can forward: {overview link}. Happy to walk the team through it
> on a short call if useful.
(while the overview link is PENDING: "Happy to send a short overview by email, what address
works best?")

**A5. "Is this an automated message?"** Answer honestly.
> Fair question. The first note went out through a sequencing tool; this reply is me. {one line
> on why their company}

**A6. Data, HIPAA, GDPR, SOC 2, AI training.** Only the ready answers in
`brand-assets/product-info/compliance.md` §10, shortened, never rephrased into a stronger claim.

## By category

| category | `suggested_reply_draft` | `followup_draft` |
|---|---|---|
| interested | thank them; the sender's calendar link (or two slots for `vadim`); one line on what the call covers (15-20 minutes on their use case) | — |
| question | the matching answer above in 1-3 sentences, then a soft next step (overview or call) | — |
| referral | thank them; say you will reach out to the person they named; ask whether they are comfortable making an intro | **Message 1 to the named person** (sent automatically right after they accept the invite): who suggested them, why their role, one product specific, a soft ask, ≤ 600 characters. Plus **`followup_draft_2`, Message 2** five days later if no reply: ≤ 550 characters, one light new detail or a soft question, the sender's calendar link (two slots for `vadim`), never a repeat of Message 1, no "circling back / following up / just checking in". Use `{First name}` when the lead named a team, not a person |
| maybe-later | thank them; say you will check back in a few months; no pitch | **90-day check-in**: refers to what they said then, one new reason to talk (if there is none, just ask whether timing changed), a soft ask, the overview link if it exists |
| decline · negative · out-of-office · other/unclear | empty: the sheet marks it «не відповідаємо» unless Vadim decides otherwise | — |

**Left the company** (5 of 72 repliers): if they name a successor, the category is `referral`
and `referral_to` holds the successor. Otherwise `other/unclear`.

**`referral_to`**: the person the lead named, as they wrote it, plus role and company when the
reply says it (`Naeem Witbooi, Counterweight`). A team with no name (`product team`, `the Field
CEOs`) goes in as written, prefixed `team:`.
