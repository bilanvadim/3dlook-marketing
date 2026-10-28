---
product: fitxpress
type: vertical-page
vertical: wellness-programs
status: review
source: Nika's two drafts + Asselya's chat-edited version (Slack #marketing, thread 1793092164.544279, 2026-10-27)
---

# Gate reports: wellness landing, review of three drafts (2026-10-28)

Inputs, all from the #marketing thread of 2026-10-27:

| Draft | File | Angle | Canonical |
|---|---|---|---|
| A, Nika v1 | `nika-v1-2026-10-27.html` | wellness apps: show members the body progress the scale misses (built on the hub "AI Body Data for Wellness Platforms") | `/fitxpress/for-wellness-platforms/` |
| B, Nika v2 | `nika-v2-2026-10-27.html` | wellness rewards verification for employers and insurers (built on the rewards article) | `/fitxpress/for-health-plans-and-employer-wellness/` |
| C, Asselya v3 | `asselya-v3-2026-10-27.html` | remote biometric screening for employee wellness programs, rewards as one use case; Asselya: "use v3 as the new working version" | `/fitxpress/for-wellness-programs/` |

Nika's question in the thread: the wellness page overlaps the fitness landing, and the difference between the two ICPs
is unclear.

## G-I · should the page exist: PASS on the standing FX waiver

- Use-case file: `use-cases/fx-wellness-rewards.md`, with the "Biometric screening angle (Vadim, 2026-09-29)" section:
  the slot is remote biometric screening for employer programs; FitXpress covers the body-measurement part only;
  no ADA / GINA / EEOC / HIPAA wellness-program compliance claims.
- Cases: `G-I: standing FX waiver 2026-09-27`. No wellness client (Nika's own note on B).
- Demand: the strongest of the planned FX slots after occupational health. Keyword map §6: at home biometric
  screening 80, company 100, onsite 150, companies 90, wellness rewards program 200, corporate wellness platform 500,
  employee wellness app 200 (US, KD 1-15).
- Facts not on the parent: screening components and what FitXpress does not cover, onsite vs remote screening,
  incentive programs and administrator review, employer / health plan / platform roles, alternative paths for
  people who cannot scan. Enough for the 60% rule.
- BD owner: not asked.

## G-A · architecture: A and B FAIL placement, C PASS

- **URL.** Landing map: `/fitxpress/for-wellness-programs/`, angle remote biometric screening (Vadim 2026-09-29).
  Only C uses it. A's `/for-wellness-platforms/` and B's `/for-health-plans-and-employer-wellness/` are new slots
  nobody approved.
- **Cannibalisation.**
  - A: its title "Body Progress Tracking for Wellness Platforms" retells the wellness hub
    (`ai-body-data-wellness-platforms`, live title "AI Body Data for Wellness Platforms"), and its buyer (wellness
    and coaching apps, member progress) is the fitness landing's buyer (`body scanning for fitness apps`). This is
    the overlap Nika felt: consumer wellness apps belong to the fitness page and the hub, not to a second landing.
  - B: its title "Wellness Rewards Verification | FitXpress by 3DLOOK" collides with the live rewards article
    ("Wellness Rewards Verification for Employers & Insurers"), which the keyword map keeps as the owner of
    "wellness incentives". Rewards stays a use case on this page, as C does.
  - C: "remote / at-home biometric screening" is owned by nothing live; the informational "biometric screening"
    belongs to the planned Hub 5 article (5.x1). Low risk.
- Inbound links: landing map "Demo button now" for Hub 5 is `/fitxpress/for-connected-and-digital-fitness/`; relink the
  wellness hub and the rewards article here when the page is live.
- `/fitxpress/` is not live: root URL until it ships (insurance precedent). GSC baseline: new URL.

## Mechanical checks

| Check | A (Nika v1) | B (Nika v2) | C (Asselya v3) | Rule |
|---|---|---|---|---|
| Visible words, hero to form, table once | ~2,610 | ~2,770 | ~1,470 | 1,100-1,600 |
| FAQ | 9 | 9 | 6 | 4-6 |
| H2 count | 11 | 12 | 9 | kit: 10 blocks |
| you/your per 1,000 | **14.2** | 8.3 | 6.1 | ≤ 12.5 |
| H1 = product + audience + outcome | yes | yes (17 words) | no product in H1 | kit sales rule 1 |
| Yoast title / description | 57 / 142 | 51 / 150 | 59 / **161**, title ends "\| 3DLOOK" | ≤ 60 / ≤ 155, "\| FitXpress" |
| Service `audience` / `areaServed` | yes / yes | yes / yes | **no / no** | G-T |
| Detector `--channel page` (visible copy) | "platform decides" x3 | clean | 1 en dash | 0 hard fails |
| `[PLACEHOLDER]` comments | 2 | 2 | 0 | 0 |
| Form | `/contact-us/` `f227f5ce` | same | same | shared `FX \| LP \| Demo` |
| Dead links | hub placeholder | `/fitxpress/for-connected-fitness/`, `/fitxpress/for-telehealth-and-weight-loss/`, `/content-hub/` | none | 0 |
| Price signal | tiers, "scans" | tiers, "scans" | tiers, "requests" | live `/pricing/` says scans (2026-10-28) |
| Client count / logos | 100+ / none | 100+ / none | none / none | |
| Hero at 1280×800, layout at 375 | not measured | OK / OK | OK / OK | |

## Fact check against the product files (detail in `fact-sheet.md`)

- Unsourced again in A and B: iOS 15+, older Android frame rate, standing only, wheelchair / amputee limits, two gender
  options, "height, weight and gender are required inputs" (weight is optional), "entered height within 2 cm"; B also
  webhooks without retries or signature verification.
- "Voice and visual prompts" (B, C) and "no gallery upload" (B, C): not in product docs. Gallery comes from the live
  rewards article; Nika's own note asks product to confirm.
- A and B publish per-measurement figures (waist repeatability 0.89 cm, waist error 2.14 cm). `accuracy-formulations.md`
  rule 6 keeps them for technical material; they were cut from the wellness hub for that reason.
- C: "input photos are not stored after processing" contradicts `compliance.md` (deleted immediately or kept up to 30
  days under the customer's policy). C drops the validation population and "under NDA" from the accuracy block. C
  labels Smart Scales "beta" (public wording since 2026-10-21: no beta label). C's pricing unit "requests" does not match
  today's `/pricing/`.
- GDPR: none of the three uses the canonical sentence.

Third-party statistics (B only): `sources-problem-block.md`.
