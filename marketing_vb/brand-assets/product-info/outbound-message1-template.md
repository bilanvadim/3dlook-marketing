---
product: fitxpress
type: outbound-template
applies_to: message-sequencer (Message 1)
created: 2026-07-21
owner: Vadim
---

# Outbound - Message 1 Template & Style

> Source of truth for how `message-sequencer` writes **Message 1** of the 2-message company sequence.
> Message 1 is sent in **English** on LinkedIn **right after the prospect accepts the (note-less) connection request**.
> Set by Vadim, 2026-07-21.

## Hard constraints

- **Language:** English.
- **Length:** ≤ **600 characters** total (greeting + body + signature, everything counted).
- **First person**, from the sending profile owner (Katerina / Nick / Olena / Katya / Vadim).
- **Signature:** first name only, **no title / role**. A simple sign-off ("Best,") before the name is optional.
- Output **only the message**. No subject line, no preamble, no commentary around it.

## Banned (hard FAIL, brand-checker enforces, CLAUDE.md §6)

- **No long dash of any kind (— or –).** Use a period, a comma, a colon, or a plain hyphen "-" instead. Applies to the whole message, product intro included.
- **No triple parallelisms** (no three-item parallel lists such as "quick, visual, data-backed"). Make one or, at most, two concrete points.
- **No "It's not just X, it's Y"** construction.
- **No banned words:** leverage, utilize, harness, robust, seamless, comprehensive, delve, navigate (figurative), tapestry, realm.
- **No generic AI openers:** "I hope this finds you well", "I came across your profile", "I help companies like yours…".
- **No named clichés:** "I admire your mission", "excited about your journey", and anything in that register.

## Tone

- Confident, **not** pompous. The voice of someone who knows what they're doing and just wants to discuss what could genuinely be useful.
- Frame from **experience and observation**, not selling.

## Structure (in this order)

1. `Hi {first_name},`
2. **Light hook.** Briefly signal why you're writing. Pick and adapt one; vary it across contacts (never reuse the same hook in a batch):
   *Circling back · Saw your post · Quick thought · Noticed your background · Came across your work · Got me thinking · Curious about your take · Saw your activity · Quick note · Spotted something · Thought I'd share · Noticed overlap · Quick one · Had a thought · Quick idea for you · Caught my eye · Wanted to reach out · Had to say hi · This stood out · Made me think · Couldn't help but ask · Saw the news · Quick reaction.*
3. **Specific observation / question** about their world: what caught your eye, what's missing, what's interesting. Tie it to the campaign hypothesis and their vertical.
4. **Short product intro.** No self-promo, just what we built and for whom. Anchor on this framing (adapt the wording so the whole message stays ≤ 600 and fits the vertical, "in some form", not necessarily verbatim):
   > We've built a mobile body scanning layer that lets members capture consistent anthropometrics via smartphone (key circumferences / dimensions), producing structured, trackable metrics that drop into the patient record.
   - Non-clinical FX verticals (fitness, wellness): "patient record" becomes "member profile" or "progress tracking".
   - Mobile Tailor: reframe to fit/measurement dropping into the sizing / OMS workflow. **No** "patient record".
5. **Soft CTA.** Short and simple: "Might be worth a quick chat?", "Worth a quick chat to explore?", "Open to a quick chat?"
6. **Signature.** First name only.

## Style phrases that fit

- "Curious how you're thinking about…"
- "We're seeing a lot of [X] struggle with…"
- "Built [product] to solve exactly this. Fast and data-backed."
- "Might be worth a quick chat?"
- "Thought I'd share, in case helpful."
- "No pressure, just figured this might be up your alley."

## Examples (Katerina, UK / CEO profile)

**Example A**
```
Hi Lynn,
Circling back after connecting - curious how you're approaching user motivation without physical progress data. We're seeing more health platforms struggle with retention as GLP-1 users expect visible results.
At 3DLOOK we built FitXpress to give them that: precise body metrics and 3D progress tracking from the phone camera. Worth a quick chat to explore?
Best,
Katerina
```

**Example B**
```
Hi Marissa,
As CEO of 3DLOOK, I've noticed a big shift: users now expect real proof of progress, not only numbers. We built FitXpress to give them body data and visuals from just two photos.
Could be a fit for MyFitnessPal. Open to a quick chat?
Katerina
```

## Notes

- Personalize the hook + observation **per contact**. They carry the personalization; the product intro stays stable.
- All numbers / claims still come from `proof-points.md`. Don't invent stats.
- Only the **opener style** follows this template. It does **not** override the brand no-go rules: no long dash, no triple parallelisms, no banned words. `brand-checker` fails a message that breaks them.
