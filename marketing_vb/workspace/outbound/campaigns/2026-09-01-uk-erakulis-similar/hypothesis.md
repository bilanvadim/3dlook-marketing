---
product: fitxpress
profile: katerina
market: UK
created: 2026-09-01
rewritten: 2026-09-12
status: approved
---

# Hypothesis — UK Consumer Wellness / Fitness / Nutrition Apps (Erakulis look-alike)

- **Campaign:** `2026-09-01-uk-erakulis-similar`
- **Owner:** Katerina Galich (`katerina`, UK)
- **Seed account:** **Erakulis** — CR7's fitness + nutrition + mind subscription app, **an existing 3DLOOK client** running phone-camera BodyScan. It is the pattern we are cloning, never a target.

> **Rewritten 2026-09-12.** The 2026-09-01 version narrowed "similar to Erakulis" to private GLP-1 telehealth in England. That reading survived neither its own anti-cases (13 of 30 companies on the resulting list were the dispensing pharmacies the hypothesis excludes, leaving ~11 genuine matches against a stated floor of 15) nor the seed itself — Erakulis is a general wellness app, not a GLP-1 clinic. Scope decision by Vadim 2026-09-12: consumer wellness / fitness / nutrition apps, whole UK. Superseded artefacts and the full teardown: `_superseded-2026-09-12/README.md`.

---

## Vertical

UK-headquartered consumer **subscription wellness, fitness and nutrition apps** — the "Connected & Digital Fitness" ICP segment (`icp-detail.md` §8) read as the UK sibling of the closed `2026-08-07-us-digital-fitness` (nick) and `2026-08-14-au-digital-fitness` (vadim) campaigns. The job to be done is identical everywhere: retain paying subscribers by showing visible physical progress. This campaign is the UK slice, run on `katerina`.

## Sub-segment

UK-HQ consumer apps selling a paid subscription for fitness, nutrition, body transformation or multi-pillar wellness, with:

- **~$1M+ annual recurring revenue**, roughly Series B through public (the §8 floor),
- **25+ employees** — a deliberate campaign-level deviation from the `icp-detail.md` universal exclusion ("companies under 50 employees"), **Vadim's call 2026-09-12**. The 2026-09-12 research pass showed the 50 floor, not the product filter, was doing most of the killing in the UK: Fiit (32), WithU (31), CheqUp (11-50), Medicspot (34), Habitual (21-50) and Nutracheck (25-45) all have the right product shape and fail on headcount alone. The deviation applies to **this campaign only** — it does not amend the ICP document, and it does not carry to `nick`, `olena`, `katya` or `vadim` without Vadim saying so again. A 25-person app still has to clear the $1M revenue bar and have a real paid subscription;
  "small" is not the same as "no budget", but "no revenue" still is,
- **mobile-first delivery** — a real iOS/Android app that is the product, not a marketing shell,
- **body metrics already shipped but shallow** (self-reported weight, tape measurements, smart-scale import) **or a natural next feature**.

Four flavours inside the net, in rough priority order:

1. **Multi-pillar wellness apps — the literal Erakulis pattern.** Fitness + nutrition + sleep/mind in one subscription, adding a body-metrics pillar as a differentiator.
2. **Training / body-transformation and AI-coaching apps.** Live or die on visible progress; the before/after is the product's whole emotional payload.
3. **Nutrition, habit and calorie-tracking apps** with a paid tier, where the scale is currently the only outcome signal.
4. **App-first weight-management and GLP-1 companion programmes** — the legitimate remainder of the old hypothesis (Juniper, Second Nature, Voy, Numan, Piko, CheqUp, NowPatient, Medicspot, heySlim, Jood Life, Dr Frank's). One slice of four, not the whole campaign. Re-verify and score them; do not import the old rows unchanged.

**Geo: the whole UK** — England, Scotland, Wales and Northern Ireland. England-only is what starved the previous pass (it dropped Wales and Scotland companies mechanically, on a filter nobody needed). UK-HQ means product decisions sit in the UK, not that the company merely sells here.

## Use case

FitXpress as the embedded body-measurement and progress-visualisation layer inside a UK consumer wellness app — a 2-photo smartphone scan returning 80+ measurements, body composition (body fat %, lean mass, fat mass, BMI, BMR) and a 3D progress model in under 45 seconds via API/SDK — so the app ships the BodyScan feature its retention curve needs without building computer vision in-house. Exactly what Erakulis did.

## Why plausible

1. **Loss of motivation is the single largest churn driver in fitness subscriptions, and the scale is a bad motivator.** Fitness apps carry the steepest churn curve in consumer subscriptions, and the biggest named cancellation reason is goal abandonment — users stop seeing progress before they stop making it. Body recomposition is precisely the case where the scale lies: weight flat, waist down, and the subscriber quits during the month the product was working. Circumference change plus a 3D overlay is a stronger retention artefact than any number a smart scale produces, and it maps to the outcome the user actually bought. `icp-detail.md` §8 names this verbatim: "пользователи теряют мотивацию без visible progress".

2. **We have a nameable proof of scale — but only for half this list.** **Vadim's call 2026-09-12: Erakulis may NOT be named in outreach.** It is the pattern this campaign was built from, and it stays internal: it appears nowhere in `brand-assets/product-info/` — no case study, no proof-point row, not in the "Trusted by" line — so it was never an approved reference to begin with. What we can name instead is **Yazen**: "Yazen uses FitXpress for member progress tracking, with 34K scans in 2025" (`case-studies/yazen.md`, explicitly cleared for outbound to telehealth and weight-loss platforms). That lands cleanly on flavour 4 — Voy, Numan, CheqUp, Medicspot, NowPatient are the same shape of buyer. **It does not land on flavours 2 and 3.** Yazen is a clinical weight-loss platform; Fiit, Coopah, WithU and Nutracheck are consumer fitness and nutrition apps, and we have no nameable reference in that shape at all. For those five, the sequence leans on reason #3 (integration speed) and reason #1 (the churn argument), not on proof. Plan the messaging accordingly — this is a real asymmetry in the list, not a wording problem.

3. **They cannot build it, and AI personalisation no longer differentiates.** These are lean product teams; pose estimation and measurement extraction is a buy, not a build. Meanwhile AI coaching and personalised plans are table stakes across the category in 2026 — verified physical progress is not, and it is hard to fake. That is a defensible feature for a product team under pressure to justify next year's subscription price.

4. **Clean regulatory lane on the consumer side.** Body-composition trend tracking stays out of medical-device territory as long as it is non-diagnostic, tied to no disease claim and not used for clinical decisions — which matches 3DLOOK's "operational, not clinical" positioning. UK GDPR posture on photo processing is the first hard question from any CTO and our compliance story (photos deleted after extraction, no personal identifiers processed, encryption at rest and in transit) is a selling point, not an afterthought. Standard line where it comes up: **FitXpress is not a medical device.**

## Target buyer persona

- **Chief Product Officer / Head of Product / VP Product — primary.** Owns the roadmap and the build-vs-buy call on a BodyScan feature. Cares about feature velocity, activation, engagement. Objection: "we could build this" → pre-trained model via API/SDK, weeks not quarters, no CV team needed.
- **Founder / CEO — primary for sub-200-person apps.** Still owns product and takes the meeting directly. Cares about differentiation, LTV/CAC, standing out in the App Store.
- **VP Engagement / VP Retention / Head of Growth.** Owns the number this use case moves — month 2–3 drop-off, check-in cadence, retention curve.
- **CTO / VP Engineering — `technical-integration` angle, P3.** Evaluator and internal champion, not the economic buyer (per the 2026-07-22 IT policy: WEAK, not FAIL). Cares about SDK quality, time to integrate, data architecture.
- **Not the buyer:** marketing, content, community, fitness programming, customer support.

## Anti-cases

- **Already contacted on `katerina`.** The 2026-07-31 UK campaign burned 15 companies: Zoe, Vira Health, Peppy, Newson Health, Healthier Weight, Tonic Weight Loss Surgery, The Body Coach, Huma, Hertility, Physitrack / Champion Health, Thriva, Sweatcoin, Slimming World, UCL. Run `outbound-registry.py check --profile katerina` before the list ships — the registry is the authority, this list is a reminder.
- **Erakulis itself and any existing 3DLOOK customer.** Inspiration, never a target.
- **Free / freemium-only apps with no paid tier and no enterprise budget** — universal exclusion.
- **Sub-$1M revenue, sub-25-employee, pre-launch or no app in the stores.** No integration capacity, no budget. (Floor moved 50 → 25 on 2026-09-12; see Sub-segment.)
- **Gym chains, health clubs and fitness equipment makers with no software subscription layer.** PureGym, David Lloyd, Gymbox and peers went on the previous list and do not belong: membership is not an engagement surface, and there is no product team to sell to. A gym chain with a genuine first-party training app and a product org is the exception — score it, don't auto-include it.
- **Sports nutrition and supplement e-commerce** (MyProtein, The Protein Works, vitamin subscriptions). Selling powder is not a retention-through-progress problem.
- **Content-only platforms** — video libraries, streaming classes, PT course providers — with no measurement ambition and no body-data hook.
- **Pure dispensing pharmacies and online-doctor checkouts.** No app, no programme, nothing to embed into. This is what wrecked the previous pass; hold the line.
- **NHS / ICB-commissioned services** (Oviva, Reed Momenta, tier-2/3 weight management). Quarter-long procurement, DTAC and DSPT burden, no consumer churn problem — the commissioner pays regardless.
- **Anything positioned on medical claims or as a regulated device.** Pulls the feature out of the general-wellness lane.
- **Anyone who already shipped body scanning** or signed a scanning/hardware partnership → competitive-displacement track, not this one.
- **Recently acquired or merged** — ICP shifting, cycle stalls.
- **Non-UK-HQ — flag and route, do not discard.** FitXpress fits them fine; this is geo discipline for `katerina` only. US-HQ → `nick`, EU → `olena`, AU → `vadim`. Use `validate-companies --write-routed`.

## Validation criteria

**Validated** if:

- The researcher builds **≥25 UK-HQ companies** genuinely matching the sub-segment, none of them already burned on `katerina`. **Fewer than 15 → stop at step 2** and say so rather than padding the list with adjacent businesses. This is the rule the previous pass broke.
- Every row carries the full step-2 schema — `company_name, website, linkedin_url, hq_country, hq_city, employees, revenue_estimate, fit_score_1_to_5, fit_reason, source_url, notes` — and `verification=verified-live` from `web-verify.py`. The last list had no fit score, no LinkedIn URL and no headcount, so nothing could be prioritised and Sales Navigator had nothing to key on.
- ≥40 contacts pass ICP validation.
- ≥12% reply rate and ≥5% positive across the sequence.
- ≥3 discovery calls where the prospect names retention or progress visibility as a top-three product priority, unprompted.
- ≥1 pilot or paid POC inside 6 weeks of first send.

**Falsified** if:

- The list can't clear 15 qualified UK companies — the UK slice is too thin and this belongs in a pan-European campaign on `olena`.
- ≥3 calls independently say body data is a nice-to-have next to content and programming.
- ≥3 prospects have already shipped or committed to scanning → this is a displacement market, not a greenfield one.

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

## Open questions

1. ~~Can Erakulis be named in cold copy?~~ **Resolved 2026-09-12: no.** Yazen replaces it for the GLP-1 / weight-management half of the list. The consumer fitness and nutrition half has no nameable reference — see reason #2.
2. **UK GDPR on photo processing** — special-category health data or not in a consumer wellness context, retention periods, whether anyone will demand UK-region processing. First hard CTO question.
3. **Pricing stays out of the sequence entirely — Vadim's call 2026-09-12.** No price, no tier, no range hint, no "from $X" in any cold message on this campaign, including follow-ups. `pricing.md` already says lead with outcome and range-hint only if the buyer raises budget; on this campaign the range hint is off too. If a prospect asks about cost, that is a call, not a reply. `message-sequencer` (step 5): treat any pricing number as a hard fail, same as a fabricated claim.
   The reason it still matters, for the call rather than the copy: **there is no tier that fits this segment.** The published table (`pricing.md`) tops out at 20,000 requests/month for $10K and says "custom above 20K/mo". Yazen, our highest-volume FitXpress customer, ran 34,000 scans across all of 2025 — about 2,800/month. Voy claims >1M members: a 5% monthly scan rate puts it at 50,000 scans/month, roughly eighteen times Yazen's annual volume, on day one. Every serious company on this list is a custom-pricing conversation from the first call, and the price list cannot quote them.
   Worse, the tiers run backwards for the small end: the $2.00 entry rate is ~16% of a £12/month consumer subscription, while the $0.50 floor only unlocks at 20K/month. Fiit, Coopah, WithU and Nutracheck get the worst per-scan rate precisely because they are smallest.
   The lever that fixes it is cadence, and it is ours to set in the pitch: **quarterly check-in scans, not monthly.** That cuts per-user cost 4x, matches Yazen's own "periodic check-in" pattern, and is better product design anyway — body composition does not move meaningfully in 30 days, so a quarterly progress reveal is a stronger retention artefact than a monthly one showing noise. Needed before step 5: a consumer-volume answer Vadim is willing to say out loud when a Voy or Numan product lead asks what this costs at a million members.
4. **Overlap with `2026-07-31-uk-telehealth-digital-health`.** Fiit and Flo Health appeared on that list but were never contacted. Confirm they are fair game before including them.

---

## Next step

`company-researcher` (step 2) builds the 25–30 company list against the sub-segment and anti-cases above, whole UK, full step-2 schema, `web-verify` on every row.
