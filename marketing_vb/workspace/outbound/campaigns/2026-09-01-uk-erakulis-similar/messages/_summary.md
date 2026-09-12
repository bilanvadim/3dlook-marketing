---
product: fitxpress
profile: katerina
market: UK
campaign: 2026-09-01-uk-erakulis-similar
step: 5-message-sequencer
created: 2026-09-12
updated: 2026-09-12
---

# Messaging — 2026-09-01-uk-erakulis-similar

- **Total people:** 26 (9 PASS + 17 WEAK, per `people-approved.csv`, all approved by Vadim at the step-4 checkpoint)
- **Total messages generated:** 26 x 2 = 52 (Message 1 opener + Message 2 follow-up, no connection-request note)
- **Avg char count Message 1:** 429 / 600 (range 340-471)
- **Avg char count Message 2:** 437 / 550 (range 350-506)
- **Zero pricing mentions, zero client names of any kind** (grepped across all 26 files; see "No-names rule" below)
- **AI-tells sweep:** all 52 message **bodies** (not the file headers, which use em dashes structurally) run through `detect-ai-tells.py --channel dm --summary`, verdict `CLEAN` on every one. No em dash, no banned words (leverage/utilize/harness/robust/seamless/comprehensive/delve/tapestry/realm/etc.), no "so"/"plus"/"let" used as banned connectors, no triple parallelism, no "positioned as", no generic AI openers or outbound clichés.

## No-names rule (Vadim, 2026-09-12) — supersedes the earlier Yazen/case-study routing

**No client may be named in message copy at all**, in either message, for any contact. Anonymised
proof is allowed: a scan-volume figure with no company name, and a vertical/geo attached only
where a case study explicitly licenses it. This replaces the product-aware case-study routing
this campaign started with (Yazen-eligible vs. not); the routing logic by company still matters
for **which anonymised fact fits**, it just never surfaces a name.

Two facts in play, per `proof-points.md` / `case-studies/`:
- **34,000 scans in 2025 on one platform** (`case-studies/yazen.md`). No country is recorded for
  it, so no UK/geo claim is attached, and the vertical is capped at "a weight-loss platform" (not
  used at that level of specificity anywhere in this pass; every message using this fact stays
  vaguer than that ceiling, at "one platform" or "one customer").
- **7,500 scans in 2025 at a UK online pharmacy, for BMI verification** (`case-studies/uk-meds.md`).
  UK geo is licensed for this fact only, because `uk-meds.md` states it directly.

**What changed in the files:**
- The 9 messages that named Yazen were mechanically de-named by Vadim before this pass (Dr Zubair
  A., Oliver Brooks, Eliot Howes, Jeff Hadaway [no rename needed, no name used], Cordell Jopson,
  Rajive Patel, Jay Patel, Saqib Kayani, Kamran Ullah, Amish Patel — Medicspot and Infohealth
  Ltd/Limited contacts). Checked all 9: wording kept as Vadim wrote it, except two small legibility
  fixes (`cordell-jopson-724b301a2.md`, `jay-patel-43aa8a21.md` had a redundant "on FitXpress runs
  it" construction left over from the search-and-replace; left as found elsewhere since the meaning
  was already clear).
- **17 messages that previously had no scan figure at all** (because Erakulis was barred and Yazen
  was the wrong shape for consumer fitness/nutrition) now carry an anonymised proof line, added to
  Message 2 in all 17 cases (Message 1 either had no headroom or the hook/product-intro structure
  didn't have a natural seam for it). List, fact used, and framing:

| Person | Company | Fact used | Framing angle |
|---|---|---|---|
| Ben Pratt | Nutracheck | 34K, one platform | mobile capture flow in production |
| Daisy Blackwood | WithU | 34K, one platform | SDK production readiness |
| Daisy Ford | Nutracheck | 34K, one platform | live, named partnership feature |
| Daniel Hutson | Nutracheck | 34K, one platform | not an early-stage tool |
| Eleanor Bennett | Nutracheck | 34K, one platform | API handles real production load |
| Ellie Hitchmough | Coopah | 34K, one platform | shipped as a co-branded partnership feature elsewhere |
| Eoin Duffill | Nutracheck | 34K, one platform | production volume, past pilot load |
| Ian Carrington | Fiit | 34K, one platform | portfolio-lens commercial scale |
| Jack Yaxley | Nutracheck | 34K, one platform | volume that tests whether tracking holds up |
| James Charalambous | Fiit | 34K, one platform | past a pilot run |
| Jeff Hadaway | Medicspot | 7.5K, UK online pharmacy | checkout-step scan with a compliance audit trail |
| Jonatan Tibarovsky | WithU | 34K, one platform | backend load, for reference |
| Navin Khosla | Infohealth Ltd | 7.5K, UK online pharmacy | live precedent under UK data-protection scrutiny, audit trail |
| Pete Cooper | Coopah | 34K, one platform | someone already reached that scale |
| Ryan Sherreard | Coopah | 34K, one platform | real volume, same integration |
| Sid Lale | Nutracheck | 34K, one platform | member-side only, no extra hardware |
| Simon Knight | Fiit | 34K, one platform | plain scale data point |

**Why the split:** the 15 Nutracheck/Fiit/Coopah/WithU contacts (consumer fitness/nutrition) all
get the 34K/one-platform fact, kept vaguer than "weight-loss platform" throughout, since that is
the safer distance for a consumer-fitness reader and the fact carries no geo to begin with. Jeff
Hadaway (Medicspot) and Navin Khosla (Infohealth) get the UK-pharmacy/7,500 fact instead, per
Vadim's explicit steer that it is the better fit for those two companies, and because both
messages are built around an operational/compliance audit-trail argument that the UK-pharmacy
case (checkout-step verification, "compliance team has audit trail," per `uk-meds.md`) matches
directly. The other Medicspot/Infohealth contacts already carry the 34K fact from Vadim's
mechanical pass; that mix (34K at some Medicspot/Infohealth desks, 7.5K at others) is intentional
and also helps the same-company differentiation goal.

**17 different sentences, not one template:** no two of the 17 new lines share the same opening
or structure (see the table above for the framing angle each takes). Two pairs land on adjacent
ideas by necessity (Daniel Hutson / James Charalambous both use a "past a pilot"-style contrast;
Ryan Sherreard / Ellie Hitchmough both lean on "real volume elsewhere"), but neither pair shares a
sentence, a company, or identical wording.

**Terminology-guardrails cleanup done in the same pass.** Fixing the corrective-negation /
corrective-"rather than" instances in the files this pass touched (`terminology-guardrails.md`
Part 1, rules 8-9): `ian-carrington-0869a91.md` ("not a roadmap commitment"),
`james-charalambous-9b955328.md` ("rather than built"), `pete-cooper-coopah.md` ("not a roadmap
risk") and `eleanor-bennett-a3229957.md` Message 1 ("not a weekend project") were rewritten to
state the point directly instead of through a corrective contrast. Vadim had already fixed the
same category in three files before this pass (`daisy-ford-4350b7373.md`,
`ellie-hitchmough-06b1b2251.md`, `rajive-patel.md`) while de-naming Yazen. While re-sweeping all 26
for the pattern, two more turned up outside the 17-message-list and were fixed as a low-risk,
same-rule cleanup: `cordell-jopson-724b301a2.md` ("not a quick add-on") and
`kamran-ullah-a0ba94104.md` ("rather than building it from scratch"). The remaining "X, not Y"
hits left in the corpus are licensed: "days, not months" (the canonical FAQ phrasing for
integration time, `faq.md`), "FitXpress is not a medical device" (the mandated direct-form
sentence, Navin Khosla only), and Pete Cooper's own bio line "a coach, not a training plan"
(a quote of his words, not our construction).

**What this closes, and what it doesn't.** De-identified, the "no nameable reference" gap
flagged after step 5's first pass mostly dissolves: all 26 contacts now carry at least one
concrete scan-volume figure. It doesn't fully equalize the two halves of the list, though — the
Medicspot/Infohealth contacts who kept the 34K fact from Vadim's mechanical pass, or got the 7.5K
UK-pharmacy fact, are citing a number from a company in their own general shape (weight-loss /
health platforms), while the Nutracheck/Fiit/Coopah/WithU contacts are citing the same 34K figure
from a platform in a different vertical (weight-loss, not consumer fitness/nutrition). The number
is honest and now nameless, but it is still evidence from an adjacent category, not their own.

## Distribution by company

| Company | Contacts | Notes |
|---|---:|---|
| Nutracheck | 7 | 4 PASS + 3 WEAK. All 7 carry the anonymised 34K/one-platform fact (added this pass; none had a usable reference before) |
| Infohealth Ltd / Limited (NowPatient) | 6 | All WEAK. 5 carry the anonymised 34K fact (from Vadim's mechanical de-naming); Navin Khosla carries the 7.5K UK-pharmacy fact instead. HIPAA/GDPR in every sequence; medical-device line scoped to the BodyScan feature (Navin Khosla only), never to the NowPatient app, because of its MHRA Class I registration |
| Medicspot | 5 | 2 PASS + 3 WEAK. 4 carry the anonymised 34K fact (from Vadim's mechanical de-naming); Jeff Hadaway carries the 7.5K UK-pharmacy fact instead. HIPAA/GDPR in every sequence |
| Fiit | 3 | 1 PASS + 2 WEAK. All 3 carry the anonymised 34K/one-platform fact (added this pass) |
| Coopah | 3 | 2 PASS + 1 WEAK. All 3 carry the anonymised 34K/one-platform fact (added this pass) |
| WithU | 2 | Both WEAK, both technical-integration. Both carry the anonymised 34K/one-platform fact (added this pass) |

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

## Same-company differentiation (anti-mail-merge check)

Every company with 2+ approved contacts got messages built on different hooks and different
specific claims, not a templated swap of `{first_name}`:
- **Nutracheck (7):** MD gets the churn/differentiation framing; Head of Data Product gets the
  build-vs-buy/data-feed framing; PM and Product Executive get retention-progress with different
  supporting detail; Partnerships Manager gets the partnership-packaging framing; the two
  developers get pure SDK/implementer copy with different technical details (backend response
  schema vs. mobile capture flow). All 7 now also carry the anonymised 34K fact, each in its own
  sentence (see table above).
- **Medicspot (5):** CEO gets the clinician-program/outcomes framing with the 34K fact; CTO gets a
  build-vs-buy-flavoured technical message with the 34K fact; Senior Engineer and Head of
  Engineering get distinct implementer copy, also 34K; Head of Operations gets the operations/
  cost-control framing (`outcome-verification`) built around the 7.5K UK-pharmacy fact instead,
  the only Medicspot message on the other proof point and the only one built around service
  delivery rather than the app itself.
- **Infohealth Ltd (6):** two "Director" contacts (Rajive Patel, Amish Patel) hold the same title
  and same angle, so they were deliberately split on argument: Rajive gets the
  existing-remote-monitoring-feature framing, Amish gets the market-pressure/GLP-1-demand framing;
  both cite the 34K fact. Navin Khosla (compliance) is the only Infohealth message built on the
  7.5K UK-pharmacy fact, tied directly to his compliance remit. The two engineers get implementer
  copy with different phrasing, both citing 34K.
- **Fiit (3) / Coopah (3) / WithU (2):** each contact's hook is tied to something specific to
  their role or, where available, their own profile text (Pete Cooper's "a coach, not a training
  plan" tagline; Jonatan Tibarovsky's "turning chaos into architecture" tagline) rather than a
  reused company-level line. All 8 now carry the anonymised 34K fact, each phrased differently
  (see table above: portfolio lens, pilot-run contrast, production readiness, backend load, etc).

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

## Where the argument is still the thinnest, after the no-names fix

The no-names rule closes most of the gap the first pass reported ("15 of 26 contacts have no
nameable reference"): every contact now cites a real, sourced scan-volume figure, anonymised.
What it does not close: for the 15 Nutracheck/Fiit/Coopah/WithU contacts (consumer fitness and
nutrition apps), the only figure available (34,000 scans/2025) still comes from a platform in a
different vertical (weight-loss), because that is the only scan-volume figure `proof-points.md`
records with no geo attached. It is honest and now nameless, but it is still an adjacent-category
proof point, not one from their own shape of business. That asymmetry was flagged at the
hypothesis stage (`hypothesis.md` reason #2) and is now smaller, not gone.
