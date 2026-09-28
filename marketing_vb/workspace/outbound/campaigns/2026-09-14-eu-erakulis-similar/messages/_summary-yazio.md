# Messaging — 2026-09-14-eu-erakulis-similar — group: Yazio

- Product: fitxpress
- Profile: olena (calendar link: https://meetings.hubspot.com/olena-kudriavtseva)
- Total people (this batch): 22
- Total messages generated: 22 × 2 = 44
- Wave distribution: wave 1 = 20 (product/retention/technical-integration contacts), wave 2 = 2 (tobias-scheinert CFO, gráinne-o-connell Chief of Staff to the CPO — referral angle, sent only after wave-1 contacts at Yazio have gone out, per hypothesis.md "Sequencing" rule for pools C/G-exec/H)
- Avg char count Message 1: 448.0 / 600 (min 379, max 514)
- Avg char count Message 2: 345.5 / 550 (min 308, max 389)
- Distribution by angle: retention (10), product (6), technical-integration (4), referral (2)

## Proof points used (no client names, per hypothesis.md "Rules for steps 3-5")

- **"one platform ran 34,000 scans in 2025"** — anonymized, no client name, no geo, no vertical claim beyond what `case-studies/yazen.md` supports (weight-loss platform framed generically as "one platform"). Used in 9 of 22 M1/M2 pairs (retention-leaning contacts, closest fit to the weight-loss adjacency).
- **"112,100 scans in 2025 across all 3DLOOK customers"** (`proof-points.md:113`, cleared by Vadim 2026-09-14) — used in 7 of 22 pairs, mostly for scale/aggregate framing (CEO, co-founder, monetization PM, data analytics, habit-mechanic PM, interim head of user success).
- **80+ body measurements / under 45 seconds via SDK** (`proof-points.md`) — in every Message 1's product-intro line (all 22), phrased differently per person to avoid a repeated template sentence.
- **Body composition (BMI, fat mass, lean mass)** — named separately from "body measurements" per terminology-guardrails §2.13 (fixed after the AI-tells detector flagged "body measurements including BMI, fat mass" as a hard fail on first pass — annakosminkova and peterfkell).
- **2-4 week typical basic SDK integration** (`icp-detail.md`, authorized in hypothesis.md reason #3 as the build-vs-buy answer) — used in the 4 technical-integration Message 2s (alvaro-duran-tovar, artem-zasypalov, mariuskraemer, paul-woitaschek) to answer the "we could build this" objection without belittling in-house ML/engineering expertise.

## No client names, no pricing, no competitors

Grepped all 22 files for: Erakulis, Yazen, CR7, Ronaldo, UK Meds, Healthyr, Zing Coach, Prism Labs, Bodygram, Size Stream, `$`, `€`, `£` — 0 hits in every file (Context section included). "Yazio" (the prospect's own company) is named normally, which is expected and required by the 2026-09-28 sync (§2.14: name the company when known, don't default to "your organization").

## Hooks — 22 distinct, no repeats within this batch

Quick thought · Had a thought · Noticed overlap · Curious about your take · Spotted something · This stood out · Quick note · Wanted to reach out · Caught my eye · Quick idea for you · Made me think · Got me thinking · Thought I'd share · Noticed your background · Quick one · Came across your work · Saw your activity · Couldn't help but ask · Circling back · a direct quote from Paul's own profile line ("focused on strong teams and scalable systems") · Quick ask (referral, Tobias) · One quick ask (referral, Gráinne).

## Personalization sources

Every message is tied to something in the person's title, `reason` field (people-approved.csv), or their Headline/Bio/Experience from `sales-nav-raw/2026-09-28-sales-nav-olena.csv`:
- Talita Morato: named product-lead of "Tracking Experience" (per hypothesis.md, verbatim ownership).
- Victoria Kotlova: her own bio states she built progress visualization/streaks driving a "10% YoY increase in first-week retention" — quoted back to her directly (her own public claim, not a 3DLOOK proof point).
- Alvaro Duran Tovar: bio explicitly lists computer vision / production ML — addressed as the "we could build this" voice, respectfully (per hypothesis.md pool K instruction), not belittled.
- Carolin Thölke (Director of UA): framed around retention/payback of already-acquired users, not ad buying, per the task's explicit instruction.
- Michel Ziade, Guillem Arlàndez: gaming/habit-mechanic backgrounds used as the retention-mechanic analogy (streaks vs. real body change).
- Peter Kell: data-platform/personalization background used for a data-schema framing.
- Tobias Scheinert (CFO) and Gráinne O'Connell (Chief of Staff to the CPO): both wave-2, referral-only — short, honest "who owns this" ask, no pitch, per hypothesis.md pools H and C.

## Detector result

`detect-ai-tells.py --channel dm --summary` run on all 44 message BODIES ONLY (extracted to a scratch dir, never bare `/tmp`, header/context em dashes excluded to avoid the false-positive class documented in `2026-09-01-uk-erakulis-similar/STATUS.md`):

- **First pass:** 42/44 CLEAN, 2 hard fails (`body_measurement_terms`: "body measurements including BMI, fat mass" in annakosminkova-m1 and peterfkell-m1 — BMI/fat mass are body composition, not body measurements, per terminology-guardrails §2.13).
- **Fixed:** reworded both to "80+ body measurements and body composition (BMI, fat mass, lean mass)" — separates the two categories explicitly.
- **Final pass: 44/44 CLEAN, 0 hard fails.**

Also grepped for and confirmed zero occurrences of: em/en dash inside message bodies, `plus` as a benefit connector, `so` as a benefit connector, `let`, `rather than`, corrective "X, not Y" (2 instances of each found and rewritten pre-detector: weber2-m1, adriana-r-molero-m1 for "X, not Y"; alvaro-duran-tovar-2737062b-m2, mariuskraemer-m2 for "plus").

## Random sample for Vadim review (5 people)

- `tobias-scheinert.md` — CFO, wave 2, referral angle, no demo pitch.
- `adriana-r-molero.md` — Team Lead of Product Growth, retention angle, activation-window framing.
- `muggelberg.md` — Product Lead Monetization, retention angle, PRO-subscription framing.
- `guillemarlandez.md` — Senior PM, product angle, gaming/streak-mechanic hook.
- `weissenstein.md` — Co-Founder & President, retention angle, founder/mission voice.

Paths: `workspace/outbound/campaigns/2026-09-14-eu-erakulis-similar/messages/{person_id}.md`

## What I could not do / flagged

- None. All 22 rows had a LinkedIn URL match in `sales-nav-raw/2026-09-28-sales-nav-olena.csv` (0 missing joins), all messages fit within the 600/550 char limits on the first structural draft, and no compliance line was needed (ICP is consumer nutrition/fitness, not insurance/healthcare/clinical/online pharmacy, so the mandatory compliance-mention rule does not apply to this batch).
