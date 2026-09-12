---
product: fitxpress
profile: katerina
market: UK
campaign: 2026-09-01-uk-erakulis-similar
step: 5-message-sequencer
created: 2026-09-12
---

# Messaging — 2026-09-01-uk-erakulis-similar

- **Total people:** 26 (9 PASS + 17 WEAK, per `people-approved.csv`, all approved by Vadim at the step-4 checkpoint)
- **Total messages generated:** 26 x 2 = 52 (Message 1 opener + Message 2 follow-up, no connection-request note)
- **Avg char count Message 1:** 419 / 600 (range 340-465)
- **Avg char count Message 2:** 375 / 550 (range 321-474)
- **Zero pricing mentions, zero Erakulis mentions** (grepped across all 26 files; hard requirement per this campaign's brief)
- **AI-tells sweep:** all 52 message bodies run through `detect-ai-tells.py --channel dm --summary`, verdict `CLEAN` on every file. No em dash, no banned words (leverage/utilize/harness/robust/seamless/comprehensive/delve/tapestry/realm/etc.), no "so"/"plus"/"let" used as banned connectors, no triple parallelism, no "positioned as", no generic AI openers or outbound clichés.

## Distribution by company

| Company | Contacts | Notes |
|---|---:|---|
| Nutracheck | 7 | 4 PASS + 3 WEAK. No Yazen (flavour 3, no nameable reference per hypothesis.md reason #2) |
| Infohealth Ltd / Limited (NowPatient) | 6 | All WEAK. Yazen used; HIPAA/GDPR in every sequence; medical-device line scoped to the BodyScan feature (Navin Khosla only), never to the NowPatient app, because of its MHRA Class I registration |
| Medicspot | 5 | 2 PASS + 3 WEAK. Yazen used; HIPAA/GDPR in every sequence |
| Fiit | 3 | 1 PASS + 2 WEAK. No Yazen (flavour 2, no nameable reference) |
| Coopah | 3 | 2 PASS + 1 WEAK. No Yazen |
| WithU | 2 | Both WEAK, both technical-integration. No Yazen |

Company-name spelling (`Medicspot` vs `MedicSpot`, `Infohealth Ltd` vs `Infohealth Limited`) is
carried through verbatim from `people-approved.csv` / `companies.md` — a source inconsistency,
not introduced here. Flagging in case it matters for the Closely import.

## Distribution by angle

| Angle | Count |
|---|---:|
| technical-integration | 9 |
| differentiation-ltv | 7 |
| build-vs-buy | 4 |
| retention-progress | 2 |
| partnership-integration | 2 |
| outcome-verification | 1 (Jeff Hadaway, Medicspot Head of Operations) |
| compliance | 1 (Navin Khosla, Infohealth Head of User Safety and Compliance) |

The 9 `technical-integration` contacts (Eoin Duffill, Ben Pratt — Nutracheck; Oliver Brooks,
Eliot Howes, Cordell Jopson — Medicspot; Saqib Kayani, Kamran Ullah — Infohealth; Daisy
Blackwood, Jonatan Tibarovsky — WithU) are written as implementers throughout: SDK, time to
integrate (days, not months, per `faq.md`), what the data flow looks like, no retention-economics
pitch. Oliver Brooks (PASS, CTO & co-founder) gets one build-vs-buy sentence in Message 2
because his co-founder hat gives him that authority per `icp-validation-summary.md`, but stays
technical-first.

## Yazen usage (hard constraint check)

Yazen ("Yazen uses FitXpress for member progress tracking, with 34K scans in 2025") appears in
9 of 52 messages, all at Medicspot or Infohealth Ltd/Limited — the two flavour-4 companies
`hypothesis.md` clears it for. It does **not** appear in any Nutracheck, Fiit, Coopah or WithU
message. Erakulis is not named anywhere, by any allusion.

## Same-company differentiation (anti-mail-merge check)

Every company with 2+ approved contacts got messages built on different hooks and different
specific claims, not a templated swap of `{first_name}`:
- **Nutracheck (7):** MD gets the churn/differentiation framing; Head of Data Product gets the
  build-vs-buy/data-feed framing; PM and Product Executive get retention-progress with different
  supporting detail; Partnerships Manager gets the partnership-packaging framing; the two
  developers get pure SDK/implementer copy with different technical details (backend response
  schema vs. mobile capture flow).
- **Medicspot (5):** CEO gets the clinician-program/outcomes framing with Yazen; CTO gets a
  build-vs-buy-flavoured technical message; Senior Engineer and Head of Engineering get distinct
  implementer copy; Head of Operations gets the operations/cost-control framing (`outcome-verification`),
  the only Medicspot message built around service delivery rather than the app itself.
- **Infohealth Ltd (6):** two "Director" contacts (Rajive Patel, Amish Patel) hold the same title
  and same angle, so they were deliberately split on argument: Rajive gets the
  existing-remote-monitoring-feature framing, Amish gets the market-pressure/GLP-1-demand framing.
  Navin Khosla (compliance) is the only message that leads with GDPR/photo-retention instead of a
  product hook. The two engineers get implementer copy with different phrasing.
- **Fiit (3) / Coopah (3) / WithU (2):** each contact's hook is tied to something specific to
  their role or, where available, their own profile text (Pete Cooper's "a coach, not a training
  plan" tagline; Jonatan Tibarovsky's "turning chaos into architecture" tagline) rather than a
  reused company-level line.

## Contacts written with an explicit caveat baked into the copy

- **Ian Carrington (Fiit, WEAK):** real employer is Cardlytics; his Fiit hat is "Strategic
  Advisor & Investor." Written to that seat (portfolio-level differentiation argument), not as
  if he sits inside the Fiit product org, per `icp-validation-summary.md`'s own read of the role.
- **Simon Knight (Fiit, WEAK):** flagged as a probable name-collision ("Owner" at VC-backed
  Fiit Technology Ltd is not a plausible title). Message is generic enough (fitness-product
  owner, build-vs-buy) to be defensible whether or not the LinkedIn profile is actually this Fiit.
- **Jay Patel (Infohealth, WEAK):** title/summary conflict (Senior Business Administrator vs.
  "Senior Partner"). Written broadly enough to hold under either reading, without asserting
  seniority the title doesn't support.

## Random sample for Vadim review (5 people)

1. Jay Patel — Senior Business Administrator, Infohealth Ltd — `differentiation-ltv` —
   `workspace/outbound/campaigns/2026-09-01-uk-erakulis-similar/messages/jay-patel-43aa8a21.md`
2. Daisy Ford — Partnerships Manager, Nutracheck — `partnership-integration` —
   `workspace/outbound/campaigns/2026-09-01-uk-erakulis-similar/messages/daisy-ford-4350b7373.md`
3. Daniel Hutson — Managing Director, Nutracheck — `differentiation-ltv` —
   `workspace/outbound/campaigns/2026-09-01-uk-erakulis-similar/messages/danielhutson1.md`
4. Amish Patel — Director, Infohealth Ltd — `differentiation-ltv` —
   `workspace/outbound/campaigns/2026-09-01-uk-erakulis-similar/messages/amish-patel-96b103259.md`
5. Oliver Brooks — CTO & Co-founder, MedicSpot — `technical-integration` —
   `workspace/outbound/campaigns/2026-09-01-uk-erakulis-similar/messages/oliverbrooks.md`

## Known gap, carried from step 4, not fixed here

`icp-validation-summary.md` flagged that PASS+WEAK together (26) still falls short of the
hypothesis's own 40-contact floor (target 60+). Step 5 wrote all 26 approved contacts; it did
not manufacture additional volume. That gap is a step 2-4 scoping question, not something a
message-writing pass can close.

## Where the no-Erakulis rule left an argument visibly weaker

Per `hypothesis.md` reason #2, Fiit, Coopah, WithU and Nutracheck (15 of 26 contacts) have no
nameable customer reference in their shape at all, Erakulis excluded and Yazen wrong-shaped for
them. Their messages carry proof-point numbers (80+ measurements, under-45-second scan, body
composition) and the churn/build-vs-buy logic, but no third-party validation that "this works at
scale for a company like you." That is the one place this campaign is structurally thinner than
a normal FitXpress sequence, and it is a hypothesis-level gap (recorded there already), not
something rewritten copy can paper over.
