# Hypothesis — UK / Erakulis-similar

- **Campaign:** `2026-09-01-uk-erakulis-similar`
- **Owner:** Katerina Galich
- **Date:** 2026-09-01
- **Status:** approved
- **Seed account:** Erakulis (consumer health & wellness subscription app — fitness + nutrition + mind, app-first, D2C)

> Note on the seed: Erakulis is a Portugal-HQ general wellness app, not a GLP-1 clinic. The vertical below deliberately narrows "similar to Erakulis" to the UK slice where the same product surface (subscription app, remote user, progress tracking as the retention loop) exists but the willingness to pay is far higher. See Open questions #1.

---

## Vertical

Private GLP-1 / weight-loss telehealth. England-HQ, cash-pay (no NHS/ICB revenue), subscription-based.

## Sub-segment

D2C telehealth providers running a **branded mobile or web app** as the patient surface, selling a monthly GLP-1 or medically-supervised weight-loss programme direct to consumers at £100–£300/month. Roughly 20–250 employees, seed to Series B, UK-only or UK-first. They own the patient relationship end-to-end (prescriber + pharmacy + coaching + app) rather than acting as a pure dispensing pharmacy.

Shape of the list: Numan, Voy, SheMed, CheqUp, Juniper UK, Manual, Habitual, Second Nature, Yazen UK, Zoe-adjacent metabolic programmes, and the long tail of 2024–2026 UK GLP-1 entrants.

## Use case

Embed 3DLOOK's smartphone-photo body measurement into the provider's existing app so remote, cash-pay GLP-1 patients can see circumference and body-shape change between weigh-ins — giving the provider a non-scale progress signal to fight month-3 churn and to evidence that patients are losing fat rather than muscle.

## Why plausible

1. **Churn is the whole business model, and the scale stops moving.** Cash-pay GLP-1 subscriptions live or die on months 3–9, exactly when weight loss plateaus and the number on the scale stops rewarding the patient. Every provider in this segment is hunting for a second progress signal. Today they get it from a tape measure the patient uses wrong, or a smart scale with impedance body-fat readings nobody trusts. Waist and hip circumference plus a shape overlay is a stronger motivational artefact than either, and it maps to the outcome the patient actually bought.

2. **Lean-mass loss is the segment's live reputational problem.** The dominant clinical and press critique of GLP-1s is that a large share of the weight lost is muscle. Providers are already adding resistance-training and protein guidance in response, but they can't measure the result: they're fully remote, so DEXA and InBody are off the table, and sending patients to a clinic breaks the model. A photo-based measurement that shows limb and waist change is the only body-composition-adjacent evidence they can collect at zero marginal cost — and it feeds directly into the outcomes claims they publish.

3. **They already collect progress photos, and they can't build this.** Front/side progress photos with a consent flow are standard in this segment, so the patient behaviour, the camera permission and the legal basis already exist — we are upgrading an existing flow, not introducing one. Meanwhile these are lean product teams with no computer-vision capability; anything involving pose estimation and measurement extraction is a buy, not a build. Short procurement, single decision-maker, no committee.

## Target buyer persona

**Primary — Head of Product / VP Product / CPO.** Owns the app roadmap and the activation-to-retention funnel. Carries a retention or engagement number. Cares about: time-to-ship, SDK integration effort, whether it survives a bad-lighting bathroom photo.

**Primary (smaller cos, <50 people) — Founder / CEO / Co-founder.** In seed-stage providers this person still owns product and will take the meeting directly.

**Secondary / blocker — Medical Director or Chief Clinical Officer.** Will ask what the measurement error is and whether we make a body-composition claim. Must be neutralised, not sold: position as motivational and trend-tracking, not diagnostic.

**Secondary — Head of Growth / Retention.** Useful entry point when product is unresponsive; owns the LTV number the pitch is built on.

Not the buyer: Head of Engineering (evaluator, not decider), Head of Clinical Ops, marketing.

## Anti-cases

- **NHS / ICB-commissioned weight management providers** (Oviva, Reed Momenta, tier-2/3 services). Procurement cycles measured in quarters, DTAC and DSPT burden, no consumer P&L, and no churn problem to solve — the commissioner pays regardless.
- **Pure dispensing pharmacies** selling Mounjaro or Wegovy scripts through a checkout with no app or programme. No engagement surface, no subscription to retain, nothing to embed into.
- **US-HQ'd providers with a UK entity** (Ro, Hims & Hers, Noom, Found). Product decisions sit in New York or San Francisco; a UK LinkedIn campaign reaches the wrong people.
- **In-person clinics and bariatric surgery providers.** Already measure patients physically, low patient volume, capex not SaaS budget.
- **Anyone who has already shipped body scanning** or signed a hardware partnership (smart-scale OEM, in-app scan feature). Move to a competitive-displacement track, not this one.
- **Pre-launch or pre-seed, under ~10 people, no app in the stores.** No integration capacity and no budget.
- **Employer- or insurer-funded B2B2C weight programmes.** Different buyer, different sales motion, different proof required — deserves its own hypothesis, don't dilute this one.
- **Scotland / Wales / NI-HQ providers** for this pass. Not a quality judgement — England-HQ is the stated filter and keeps the list tight.

## Validation criteria

The hypothesis is **validated** if, by the end of the sequence:

- The company-researcher can build a list of **≥25 companies** that genuinely match the sub-segment (app-first, cash-pay, England-HQ). Fewer than 15 means the segment is too thin to justify a campaign — stop at step 2.
- **≥12% reply rate** and **≥5% positive reply rate** across the sequence.
- **≥3 discovery calls** in which the prospect confirms, unprompted, that month-3+ retention or progress visibility is a top-three product priority.
- **≥1 prospect** discloses they are already building, buying or evaluating body measurement / body composition tracking.
- **≥1 pilot or paid POC agreed** within 6 weeks of first send.

The hypothesis is **falsified** if:

- ≥3 calls independently name price, side effects or supply as the churn driver and dismiss progress visibility as a minor factor.
- ≥3 clinical stakeholders block on measurement accuracy in a way no positioning change resolves — that reframes the whole vertical as a regulatory problem, not a product one.
- The list can't clear 15 qualified companies.

## Success metrics

| Metric | Target | Floor |
|---|---|---|
| Companies on validated list | 25–30 | 15 |
| Contacts passing ICP validation | 60+ | 40 |
| Connection acceptance rate | 40% | 30% |
| Reply rate (of accepted) | 15% | 12% |
| Positive reply rate | 7% | 5% |
| Discovery calls booked | 6–8 | 4 |
| Pilots / POCs agreed | 2 | 1 |
| Time from first send to first call | ≤14 days | ≤21 days |

Secondary, qualitative: how many prospects use the words "muscle" or "lean mass" without being prompted. That's the cleanest read on whether reason #2 is the real wedge or just a good-sounding one.

## Open questions

1. **Is the Erakulis analogy load-bearing, or just the trigger?** Erakulis is general wellness in Portugal; this hypothesis is GLP-1 telehealth in England. If Katya's actual intent is "more consumer wellness apps like Erakulis," this is the wrong segment and we should run a parallel hypothesis on UK wellness/fitness subscription apps instead. **Resolve before step 2.**
2. **Regulatory line.** Does presenting circumference or body-composition trends inside a medically-supervised programme pull the feature toward UKCA / MHRA software-as-a-medical-device territory? Need a defensible one-paragraph answer before any clinical stakeholder call — the answer shapes the messaging, not just the legal review.
3. **UK GDPR posture.** Photo processing, whether it counts as special-category health data in this context, retention periods, and whether providers will demand on-device or UK-region processing. Likely the first hard question from any CTO.
4. **Pricing model.** Per-scan, per-active-user, or flat platform fee — and what a subscription business with £100–£300/month ARPU will tolerate per patient per month. Unknown, and it will come up on call one.
5. **Accuracy bar.** What tolerance is acceptable when the use case is motivational trend-tracking rather than clinical measurement? We need a number we're willing to say out loud.
6. **Do we have a namable reference** in wellness or weight-loss? Without one, reason #3 does the heavy lifting and the sequence has to lean on integration speed rather than proof.
7. **Timing.** January is peak acquisition season for this segment; a September approach may land while teams are heads-down building for it. That could be ideal (they're scoping the roadmap now) or terrible (feature freeze). Worth asking the first two prospects directly.

---

## Next step

Approval from Katya → `company-researcher` (step 2) builds the 25–30 company list against the sub-segment and anti-cases above.
