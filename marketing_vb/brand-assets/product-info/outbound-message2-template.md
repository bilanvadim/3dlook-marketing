---
product: fitxpress
type: outbound-template
applies_to: message-sequencer (Message 2)
created: 2026-07-21
owner: Vadim
---

# Outbound - Message 2 Template & Style

> Source of truth for how `message-sequencer` writes **Message 2** of the 2-message company sequence.
> Message 2 is sent in **English** on LinkedIn **+5 days after Message 1**, and only when the prospect accepted the connection, received Message 1, and **did NOT reply**. (In Closely the sequence auto-stops on a reply, so this fires on silence only.)
> Set by Vadim, 2026-07-21.

## Hard constraints

- **Language:** English.
- **Length:** ≤ **550 characters** total (greeting + body + link + signature, everything counted).
- **First person**, from the sending profile owner (Katerina / Nick / Olena / Katya / Vadim).
- **Signature:** first name only, **no title / role**.
- Output **only the message**. No subject line, no preamble, no commentary.
- **Short, honest, expert, conversational.**

## Banned (hard FAIL, brand-checker enforces, CLAUDE.md §6), same as Message 1

- **No long dash of any kind (— or –).** Use a period, a comma, a colon, or a plain hyphen "-".
- **No triple parallelisms.** One or, at most, two concrete points.
- **No "It's not just X, it's Y"** (and avoid the casual "not just …" / "not only …" version too).
- **No banned words:** leverage, utilize, harness, robust, seamless, comprehensive, delve, navigate (figurative), tapestry, realm.
- **No generic AI openers, no clichés** ("I admire your mission", "excited about your journey").

## Purpose

The follow-up after silence. **Lead with the value we can bring to them and their company**: a concrete outcome for their world, grounded in what we've seen in their vertical, not a feature list. Frame from experience and observation, not selling. Close with a **demo-call offer + calendar link**.

## Structure (in this order)

1. `Hi {first_name},` (a light re-touch is fine; this is a follow-up, keep it natural).
2. **One or two sentences of concrete value** for them / their company: the outcome we help with, tied to their vertical and the campaign hypothesis. This is the core of the message.
3. **Demo-call offer + calendar link** as **plain text** (the sending profile's link, from the table below). Keep the offer short ("Worth 15 min?", "Grab a slot:").
4. **Signature**: first name only.

## Calendar links (per profile): use the SENDING profile's link

| profile | calendar link |
|---------|---------------|
| katerina | https://meetings.hubspot.com/katerina-galich |
| nick | TBD (ask Vadim) |
| olena | TBD (ask Vadim) |
| katya | TBD (ask Vadim) |
| vadim | TBD (ask Vadim) |

**If the sending profile's link is TBD → STOP and ask Vadim.** Never reuse another person's link, never invent one. Insert the link as plain text (no markdown, no shortener).

## Example (Katerina)
```
Hi Lynn,
Quick follow-up. Where we usually help platforms like yours: members stay engaged longer when they can see real body change between visits, so early GLP-1 drop-off softens. FitXpress adds that from a phone camera, straight into the member profile.
Worth 15 min to walk through it? Grab a slot here: https://meetings.hubspot.com/katerina-galich
Best,
Katerina
```

## Notes

- Personalize the value line **per contact / vertical**. All numbers / claims come from `proof-points.md`; don't invent stats.
- Don't repeat Message 1 verbatim; this message earns the reply with value, then offers the call.
- Only the follow-up style follows this template; brand no-go rules and product accuracy (FitXpress vs Mobile Tailor) still apply.
