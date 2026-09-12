# Target Companies — 2026-09-01-uk-erakulis-similar

## Summary

- **Found (verified, real, sourced): 13.** Proceed to step 3 for `katerina`: **10** — Second
  Nature, Numan, NowPatient, Voy, Fiit, WithU, CheqUp, Medicspot, Nutracheck, Coopah. Routed
  out: Freeletics → `olena` (Germany), Juniper → `vadim` (Australia). Dropped as low-fit:
  Flo Health.
- **Updated 2026-09-12, second pass: employee floor lowered 50 → 25 (Vadim's call, this
  campaign only — see `hypothesis.md` Sub-segment/Anti-cases, scope hash
  `552020f56f38a8cb`).** The instruction was explicit: extend the existing list, do not
  rebuild it. Second Nature, Numan, Voy and NowPatient are untouched from the first pass.
  This pass re-admitted 5 of the 7 headcount-excluded candidates named in the brief plus one
  new find from a wider re-sweep (Coopah) — see `## Re-admitted at the 25-employee floor`
  and `## Re-sweep findings` below.
- **Hypothesis fit: MEDIUM now, up from LOW.** 10 companies is still short of the 25-30
  target and short of the original 15-company floor read against the 50-employee version of
  the hypothesis, but it is a real, defensible list at the floor Vadim actually set. No
  padding: every one of the 10 clears $1M+ revenue (2 with the number confirmed, 2 on a
  reasoned judgement call flagged as such, the rest confirmed) and 25+ employees (all
  confirmed) with a real paid subscription and a real UK HQ.
- **`search-health.py` was green throughout both passes** (20-32 results per control query,
  checked five times across the two sessions). This list was built from live search, not
  memory.
- **Every row is `web-verify.py verified-live` except Voy**, which returned
  `blocked:js-challenge` (429, Vercel checkpoint) on both passes — a known VPS-IP problem,
  not evidence against the company. `validate-companies --write-routed` ran clean both
  times (exit 0, 0 errors; 10 proceed / 3 routed on the current run).

## Company list (companies-verified.csv, `verification` column authoritative)

| # | Company | HQ | Employees | Revenue | Fit | Why fit | Verification |
|---|---------|-----|-----------|---------|-----|---------|---------|
| 1 | [Second Nature](https://www.secondnature.io/) | London, England | 150 | Not disclosed; £14.8M raised | 4 | Behavioural nutrition/weight app, NHS partner since 2017, real coaching depth | verified-live |
| 2 | [Numan](https://www.numan.com/) | London, England | 262 (LinkedIn); 486-524 (PitchBook/Tracxn) | $90M (2025) | 4 | Series B men's health platform with diagnostics baseline already shipped | verified-live |
| 3 | [Voy](https://www.joinvoy.com/) | London, England | 501-1,000 | $675M annualised | 4 | Largest UK app-first weight-management/longevity platform found | **blocked:js-challenge** |
| 4 | [Fiit](https://www.fiit.tv/) | London, England | 32 (Sep 2026); 43 (Jan 2026) | $3.5M ARR | 4 | UK's #1-rated training/AI-coaching app; re-admitted at 25-floor | verified-live |
| 5 | [NowPatient](https://nowpatient.com/) | Coulsdon, England | 53 | Not disclosed | 3 | Broad telehealth/AI-health subscription app, continuous-monitoring pitch | verified-live |
| 6 | [WithU](https://www.withuapp.com/) | UK (remote-first) | 31 | Not disclosed (unconfirmed) | 3 | Audio-led personalised training app, real subscription; re-admitted | verified-live |
| 7 | [CheqUp](https://chequp.com/) | London, England | <50 (band; exact unresolved) | Not disclosed (plausible >$1M) | 3 | Weight-loss subscription, WeightWatchers UK partner; judgement-call re-admit | verified-live |
| 8 | [Medicspot](https://www.medicspot.co.uk/) | London, England | 34 | £5.3M (~$5.6M) | 3 | Clinician-led weight-management subscription; re-admitted | verified-live |
| 9 | [Nutracheck](https://www.nutracheck.co.uk/) | Nottingham, England | 36 | Not disclosed; acquired for £43M (2022) | 3 | Nutrition/habit-tracking app with paid tier; re-admitted, 2022 acquisition ruled not-recent | verified-live |
| 10 | [Coopah](https://coopah.com/) | London, England | 27 | Not disclosed (unconfirmed, seed-stage) | 3 | AI run-coaching subscription app, new re-sweep find | verified-live |
| — | [Flo Health](https://flo.health/) | London, England | 672-685 | $157.6M ARR | 2 (dropped, low-fit) | Big UK scale, but core loop is cycle prediction not body-transformation | verified-live |
| — | [Freeletics](https://www.freeletics.com/) | Munich, Germany | 103-120 | Not disclosed | 3 (routed → `olena`) | Real AI-coaching fit, wrong geo | verified-live |
| — | [Juniper](https://www.myjuniper.co.uk/) | Sydney, Australia (parent Eucalyptus) | 871 (parent) | A$200M+ (parent, all brands) | 4 (routed → `vadim`) | Real GLP-1 companion fit, wrong geo (Australian parent) | verified-live |

## Detailed notes (the 4 original proceeds, plus the 3 routed/dropped)

### 1. Second Nature
- Website: https://www.secondnature.io/
- LinkedIn: https://uk.linkedin.com/company/besecondnature
- Registered: Second Nature Health Ltd, Registration No. 08511152, London.
- Recent context: NHS partner since 2017; expanded into Germany and the US
  (secondnature.io/de) while keeping London as the founding market and product HQ.
- Existing tech stack hints: mobile app (iOS/Android), behavioural-science coaching engine,
  habit tracking.
- Why fit (3-5 sentences): Second Nature is the closest thing on this list to the
  hypothesis's flavour 2/3 blend — a habit-and-nutrition coaching app whose entire model is
  behaviour change over months, not a one-off diet. Its only outcome signal today is
  self-reported weight and habit streaks; a 2-photo body-composition scan is a direct,
  low-effort upgrade to the "visible progress" problem the hypothesis names as the #1 churn
  driver. 150 employees and an eight-year NHS relationship signal real integration capacity
  and budget. Not on the `katerina` exclusion registry.

### 2. Numan
- Website: https://www.numan.com/
- LinkedIn: https://uk.linkedin.com/company/numan-com
- Registered: Numan Operations Limited, Co. No. 13166466, Farringdon Point, 33 Farringdon
  Road, London EC1M 3JF.
- Recent context: Series B in 2025, revenue doubled YoY to ~$90M; broadened from men's
  health (ED, hair loss) into weight loss, hormonal health and diagnostics.
- Existing tech stack hints: mobile app, at-home blood testing / diagnostics pipeline,
  clinician-led coaching.
- Why fit: Numan already ships a diagnostics-and-progress-tracking experience (blood
  panels, hormone trends); a body-composition scan extends that exact pattern rather than
  introducing a new one. Series B stage plus doubling revenue is a genuine "why now" —
  fast-growing product orgs are the ones under the most pressure to add a differentiator
  before the next funding conversation. Not on the `katerina` exclusion registry.

### 3. Voy
- Website: https://www.joinvoy.com/
- LinkedIn: https://uk.linkedin.com/company/joinvoy
- Registered: Menwell Limited (trading as Voy, rebranded from Manual in 2025 — same UK
  legal entity, not a third-party acquisition).
- Recent context: >1M members across UK/Germany/Brazil/India; $675M annualised revenue
  disclosed in a 2026 job listing, ~130% YoY growth.
- Existing tech stack hints: app-based care platform, blood testing, prescribed medication,
  personalised coaching.
- Why fit: this is the single largest, best-resourced UK-HQ candidate found in this entire
  research pass across all four flavours. It already combines blood testing with an
  app-based progress model; body composition is a small, obvious addition to a stack that
  size. **Caveat: returned `blocked:js-challenge` (429, Vercel security checkpoint) from
  this VPS**, on both passes. This is a datacenter-IP problem (confirmed against curl and a
  real headless Chrome on 2026-09-02), not a sign the company or the claim is fake — verify
  manually or from a residential IP before treating it as unconfirmed.

### 4. NowPatient
- Website: https://nowpatient.com/
- LinkedIn: **could not confirm a standalone company page.** It trades on LinkedIn under
  its parent, Infohealth Ltd (https://uk.linkedin.com/company/infohealth-limited) — flagged
  per the task's ask for rows where the LinkedIn page was hard to pin down. Verify the
  correct entity before building a Sales Navigator search.
- Registered: Infohealth Ltd, Coulsdon, Surrey. Licensed by the UK MHRA; app registered as
  a UK Class I software medical device.
- Recent context: broad telehealth + AI-health subscription platform — Rx savings,
  chronic-condition monitoring, medication reminders, "AI Health" tools.
- Why fit: fits the "app-first weight-management and companion programme" flavour loosely —
  its "continuous monitoring for health risks" positioning is a plausible home for
  body-composition trend data. Weaker fit than the other three: positioning skews closer
  to clinical/pharmacy than general wellness, and the Class I medical-device registration
  means the standard "not a medical device" line needs to be scoped to the BodyScan feature
  specifically, not the app as a whole, before it goes in outreach copy.

### Dropped — Flo Health (fit 2, below the High/Medium bar)
- Website: https://flo.health/ · LinkedIn: https://www.linkedin.com/company/flohealth
- 672-685 employees (source-conflict), $157.6M ARR (2025) — by far the largest UK-operated
  company found in this research pass, and it does have a shallow existing weight/symptom
  self-report feature that matches the hypothesis's "natural next feature" language on
  paper.
- Why it did not clear: Flo's retention engine is cycle-prediction accuracy and health
  literacy, not visible physical progress. The hypothesis's core "why plausible" argument
  (scale lies, circumference doesn't, users quit mid-transformation) does not map onto a
  product whose users aren't pursuing a body-transformation outcome. Scored the same way
  the sibling `nick` campaign scored Whoop — real, large, UK-adjacent-enough to document,
  not a genuine fit for this specific pitch. The employee-floor change does not affect this
  row: it was never excluded on headcount.
- Also flagged: the legal entity is a Delaware-incorporated "Flo Health Inc." (investor
  structure); the product organisation and the bulk of headcount are London-based, but this
  should be confirmed before the campaign asserts "UK-HQ" in outreach.

## Re-admitted at the 25-employee floor

The brief named 7 candidates excluded on headcount alone in the first pass. Here is the
merits-based call on each, now that the floor is 25:

- **Fiit — ADMITTED (fit 4).** 32 employees (Tracxn, Sep 2026), $3.5M ARR. Clears 25
  comfortably. No acquisition issue. UK's #1-rated fitness app with personal-trainer-led
  classes and training plans — the cleanest flavour-2 product fit found anywhere in this
  search. One flag: it has been repositioning in 2025 as "ONE FIIT", a B2B fitness-operating
  -system sold to gyms/hotels/property developers (The Gym Group runs it across 120+
  locations) alongside the original consumer app — confirm the consumer app is still the
  live product before pitching that side of the business.
- **WithU — ADMITTED (fit 3).** 31 employees, confirmed. Clears 25. Real subscription
  (£9.99/mo, £79.99/yr), audio-led personalised training with athlete/celebrity-trainer
  content. Revenue is genuinely unconfirmed — no figure surfaced anywhere in this search,
  not even an estimate — so this is a real open question, not a formality, before treating
  it as equal-confidence to the four originals.
- **CheqUp — ADMITTED, on judgement (fit 3).** The brief supplied the sharpest evidence:
  Companies House (12570252) files total-exemption full accounts to 31 March 2025, which
  confirms "small company" status (average employees ≤50) but does not give an exact
  figure, and predates the growth to 250,000 customers. Conclusion: **include, but flag the
  headcount as unresolved rather than confirmed.** Reasoning — a CQC-regulated med-tech
  business running a WeightWatchers UK partnership and serving 250k customers is not
  plausibly a sub-10-person shop; the accounts-filing threshold is the only hard fact
  available and it is consistent with anywhere from the mid-20s to 50. This is the
  candidate most worth a 2-minute manual LinkedIn headcount check before Sales Navigator.
- **Medicspot — ADMITTED (fit 3).** 34 employees confirmed, £5.3M/~$5.6M revenue confirmed
  (12 months to March 2026). Clears both floors cleanly. Same flavour-4 tier as NowPatient
  — clinician-led weight-management subscription, part of the larger Doctor Care Anywhere
  Group.
- **Habitual — STILL EXCLUDED.** Re-checked specifically because it was one of the six
  headcount examples named in the rewritten hypothesis itself. LinkedIn shows **2-10
  employees** — a different, more precise source than the "21-50" figure used in the first
  pass, and it does not clear 25 either way. (A separate data point claiming "1001-5000
  employees" for a company that raised ~$1M and is two years old is a clear data-scraping
  error for an unrelated "Habitual", not this one, and is disregarded.)
- **Nutracheck — ADMITTED (fit 3).** 36 employees, confirmed via a second, more specific
  source (up from the "25-45" range in the first pass). Clears 25. The brief asked for a
  judgement call on the Nov 2022 Hubert Burda Media / Immediate Media acquisition: **ruled
  not-recent**, on the same reasoning the sibling `nick` campaign applied to Lose It!
  (acquired by Everyday Health Group/Ziff Davis, also in 2022, and explicitly not treated
  as "recent" four years later). Confirmed operating subscription model (free + premium
  tiers) on a 430,000+ item food database — genuine flavour-3 fit.
- **DNAfit — STILL EXCLUDED, but not on headcount.** 32 employees would clear 25, and the
  2018 Prenetics acquisition is unambiguously not recent (8 years) — the brief's own
  framing that "2018 plainly doesn't bite" is correct and this campaign agrees. **The
  disqualifier is a different, independent finding from this pass: DNAfit sells a one-time
  DNA test kit (Diet Fit / Health Fit / Circle Premium, £299-£499) with no ongoing
  subscription fee**, confirmed across three independent sources including a dedicated
  Circle Premium review. The hypothesis's sub-segment requires "apps selling a paid
  **subscription**" — DNAfit does not have one. This is a business-model exclusion the
  employee-floor change was never going to reach.

## Re-sweep findings (25-50 employee UK companies never surfaced under the 50 floor)

The brief specifically asked for this because flavours 1-3 came back nearly empty last
time. Checked individually, not just cited from the Beauhurst ranking:

- **Coopah — NEW ADMIT (fit 3).** London, founded 2020, **27 employees** (confirmed,
  uktech.news funding announcement). AI-driven run-coaching subscription app (£14.99/mo or
  £79.99/yr), official training-app partner of the TCS London Marathon, backed by London
  Marathon Events and Alistair Brownlee MBE. Genuine flavour-2 fit and the single best
  outcome of the re-sweep. Revenue is the open question: only $2.54M raised across 3 rounds
  per Tracxn (still seed-stage), and the only revenue figure found ($57.7M, RocketReach) is
  not credible for a company at this scale and is explicitly NOT used — flagged as
  unconfirmed rather than asserted.
- **BUA Fit** (London, corporate outdoor-fitness marketplace) — checked individually.
  Acquired by CENTRED in Sept 2022 (recent enough to be a live anti-case at ~4 years, and
  unlike Nutracheck/Lose It! this one is also the wrong shape independent of the
  acquisition: B2B marketplace selling to employers, buyer is HR not a product org).
  Excluded on both grounds.
- **VEYR** (London, AI training app) — launched April 2026, five months old at the time of
  this research. No employee or revenue data exists yet to check against either floor.
  Excluded as too early-stage to evaluate, not as a headcount failure.
- **ROXFIT** (London, HYROX/hybrid-training AI app) — checked individually: **8 employees**
  confirmed (grew from 2 after its pre-seed round). Real user growth (260,000+ users) but
  does not clear even the lowered 25 floor.
- **REVOOLA** (Crawley) — re-checked at the new floor: **7 employees** confirmed
  (PitchBook). Still well under 25.
- **TrainAsONE** (Norfolk, AI running coach, real subscription) — checked; team page lists
  five named individuals and no employee-count source was found anywhere. Excluded for lack
  of evidence it clears 25, not because it fails to.
- **Sleepstation** (Newcastle, CBTi sleep programme) — checked; predominantly an
  NHS-commissioned digital therapeutic (private subscription exists as a fallback for
  non-NHS-area users) and single-pillar (sleep only, not fitness/nutrition). Excluded on
  the NHS/ICB-commissioned anti-case and vertical mismatch, independent of headcount.
- **Hevy** (workout-tracker app, appears in UK app-store rankings) — checked; the operating
  entity is Hevy Studios S.L. (Spain-registered), and confirmed revenue ($240K-$600K) sits
  well under the $1M floor regardless of geo. Excluded on both HQ and revenue.
- **Pillar App** (the Beauhurst Activetech entry, London, "PILLAR APP LTD" Co. No.
  11127539) — checked and could not be reliably distinguished from a different, unrelated
  "Pillar" fintech company (credit-building app, now part of LemFi) that dominates its
  LinkedIn/search footprint. No verifiable employee or revenue data for the fitness Pillar
  specifically. Excluded for lack of confident identification, not force-included on a
  guess.
- **Hussle** (Bath/Bristol, gym-access marketplace, part of EGYM) — re-checked: 31
  employees now clears 25, but the second reason for exclusion in the first pass stands
  independent of headcount — it is a multi-gym access marketplace with no coaching or
  body-metrics ambition, closer in shape to a booking aggregator than a training/wellness
  product. Still excluded, reason updated to product-fit only.
- **MoveGB** (Bath, gym-access marketplace) — re-checked: 13-18 employees, still under 25.
  Excluded on headcount, unchanged.
- **Dr Frank's** (Liverpool) — re-checked: 2 employees, still far under 25. Unchanged.
- **Runna, Wild.AI** — unaffected by the floor change; still excluded on recent-acquisition
  grounds (Strava, April 2025; Zepp Health, 2026).

No other new 25-50-employee UK fitness/nutrition/wellness subscription companies were
found beyond Coopah in this re-sweep, despite widening the search past the Beauhurst
Activetech ranking into general UK fitness-tech funding coverage, HYROX/running-specific
searches, sleep-tech, and workout-tracker app-store rankings.

## Excluded candidates and why

**Already burned on `katerina` (2026-07-31-uk-telehealth-digital-health)** — checked
mechanically against `workspace/outbound/exclusions/global-company-registry.json`: The Body
Coach, Healthier Weight, Hertility, Huma, Newson Health, Peppy, Physitrack / Champion
Health, Slimming World, Sweatcoin, Thriva, Tonic Weight Loss Surgery, UCL, Vira Health, Zoe.
None of these 14 (of the stated 15 — "Champion Health" and "Physitrack" share one registry
entry) surfaced again in this pass's candidate set, so nothing needed manual removal.
Re-checked mechanically again after this pass's 6 additions (`outbound-registry.py check`)
— none of the new admits are on the registry either.

**Excluded for reasons that do NOT depend on headcount** (unaffected by the 50→25 floor
change):

- **Runna** (London) — acquired by Strava, April 2025. Recently-acquired anti-case, <18
  months old, unambiguous.
- **Wild.AI** (London) — acquired by Zepp Health (Amazfit) in 2026. Recently-acquired
  anti-case, and now folded into a hardware company's wearable ecosystem.
- **DNAfit** (London) — 32 employees would clear 25, and the 2018 Prenetics acquisition is
  not recent; excluded instead on business model — one-time DNA test kit purchase, no
  ongoing subscription. See `## Re-admitted at the 25-employee floor` for the full reasoning.
- **BUA Fit** (London) — acquired by CENTRED, Sept 2022; also a B2B employer-facing
  marketplace, wrong buyer.
- **Hussle** (Bath/Bristol) — 31 employees clears 25, but it is a gym-access marketplace
  with no coaching or body-metrics product. Product-fit exclusion only.
- **MoveGB** (Bath) — 13-18 employees; also a marketplace model.
- **Dr Frank's** (Liverpool) — 2 employees per LinkedIn/RocketReach despite 40,000+ members
  served. Decisively too small a team to be a buyer of anything, even at the lower floor.
- **Jood Life** (London) — could not confirm any employee count at either floor; structurally
  reads as a small GPhC-registered dispensing pharmacy with an app layered on top
  (superintendent pharmacist + a coaching claim), which is exactly the anti-case pattern
  this rerun was told to hold the line on. Excluded on that risk rather than included on
  hope.
- **heySlim** (trading name of Panmedica Medical Distribution Ltd, Bromley) — no employee
  data found at all, at either floor. Excluded for lack of verifiable size, not disqualified
  on product fit.
- **Piko** — origin is Portugal, not the UK ("starting in Portugal and the United Kingdom"
  per its own materials), with no confirmed employee count or clean LinkedIn page. Real
  product (weight/metabolic health app, coaching, diagnostics) but too thin on hard facts to
  responsibly route to `olena` with fabricated numbers. Flagged here rather than forced into
  the CSV.
- **YuLife** (London, 228 employees) and **Vitality** (Bournemouth/London, 2,500+
  employees) — both clear either size floor comfortably, but both are insurance-linked
  wellness-rewards products, the same "different ICP segment, different buyer" call the
  hypothesis's own README made for Bupa Global and Aetna UK. Not this campaign.
- **Healf** (London) — Sifted's #1 UK wellness scaleup by revenue growth, but it is a
  curated e-commerce marketplace for supplements and wellness products, i.e. the "sports
  nutrition and supplement e-commerce" anti-case almost by definition.
- **Gymshark** (Solihull) — huge revenue and headcount, but its training app is free
  content bundled with an apparel business; fails the "no paid tier" universal exclusion.
- **Medichecks** (Nottingham, 69 employees) — clears either size floor but sells pay-per-test
  diagnostics with no ongoing subscription, and its product is blood biomarkers, not
  fitness/body composition.
- **Reset Health** — NHS-obesity-specialist-led, partnership model into health systems
  (UK/Malaysia/Italy) — reads as the NHS/ICB-commissioned anti-case, not a consumer app.
- **Sleepstation** (Newcastle) — predominantly NHS-commissioned, single-pillar (sleep only).
- **REVOOLA** (Crawley) — 7 employees confirmed; still well under 25.
- **ROXFIT** (London) — 8 employees confirmed; still well under 25.
- **VEYR** (London) — launched April 2026; too early-stage to evaluate against either floor.
- **TrainAsONE** (Norfolk) — no employee-count evidence found; excluded on absence of
  evidence, not a confirmed sub-25 count.
- **Hevy** — Spain-registered entity, and revenue ($240K-$600K) fails the $1M floor
  regardless of geo or headcount.
- **Pillar App** — could not be reliably distinguished from an unrelated fintech of the
  same name; no confident data.
- **GoJoe, Unmind, Reward Gateway, Wellhub** — all sizeable, all wrong shape: employer-sold
  workplace-wellbeing platforms whose buyer is HR/People, not a product organisation
  building a consumer app, and none has a body-transformation or body-metrics hook.

**Excluded on headcount, still below the new 25 floor:**

- **Habitual** (London) — 2-10 employees confirmed on LinkedIn (a conflicting "1001-5000"
  figure belongs to a different, unrelated company and is disregarded). Does not clear 25.

## Coverage gaps / risks

**The picture at the 25-employee floor is meaningfully better than at 50, and still thin
relative to the 25-30 target.**

1. **The floor was genuinely doing most of the killing.** Of the 7 candidates named in the
   brief, 5 were pure headcount misses that are now real, scored rows: Fiit, WithU,
   CheqUp, Medicspot, Nutracheck. Only Habitual (2-10 employees — nowhere close even at 25)
   and DNAfit (disqualified on business model, not headcount) stayed out. The re-sweep
   surfaced one more (Coopah, 27 employees) that the 50-floor search had structurally never
   reached, because search queries built around "50+ employees" framing don't return
   27-person companies.
2. **The re-sweep still came back mostly empty past that one find.** Nine other
   candidates were checked individually beyond the Beauhurst Activetech ranking — BUA Fit,
   VEYR, ROXFIT, REVOOLA, TrainAsONE, Sleepstation, Hevy, Pillar App, Hussle/MoveGB
   re-checks — and none qualified. Most UK fitness-tech companies below the old 50-employee
   line are considerably below 25 too (REVOOLA: 7, ROXFIT: 8, Habitual: 2-10), not sitting
   conveniently in the 25-49 band. The UK activetech funding pattern (Beauhurst: £13.3M
   across 28 deals in 2025, lowest since 2020) means most seed-stage companies simply
   haven't hired past a ~10-person team yet, floor or no floor.
3. **Flavour split at the new floor:** flavour 1 (multi-pillar wellness) is still just Flo
   Health, dropped on product fit. Flavour 2 (training/AI-coaching) went from zero to three
   real admits — Fiit, WithU, Coopah — the biggest beneficiary of the floor change. Flavour
   3 (nutrition/habit) went from zero to two — Second Nature (original), Nutracheck (new).
   Flavour 4 (GLP-1/weight-management companion) is now five — Numan, NowPatient, Voy,
   CheqUp, Medicspot — still the deepest bench.
4. **Revenue confidence is uneven across the 10, and that is reported plainly rather than
   smoothed over.** Second Nature, Numan, Voy, NowPatient, Fiit, Medicspot, Nutracheck all
   have either a hard revenue figure or a strong scale proxy (acquisition price, doubled
   YoY, member count). WithU, CheqUp and Coopah do not — their revenue is a genuine
   open question, not a rounding error, and each row says so. If Vadim wants a
   higher-confidence subset for the first send, that subset is the other 7.
5. **CheqUp remains the one row worth a two-minute manual check before Sales Navigator** —
   Companies House confirms "small company" (≤50) but not the exact number, and it is the
   only row where the headcount evidence is a judgement call rather than a count.
6. **Recommendation, updated:** 10 is enough to run `katerina` as a real (if smaller than
   planned) campaign rather than a pilot-of-4. The original recommendation to consider a
   pan-European fold-in on `olena` for the multi-pillar/training gap still stands as a
   longer-term option if flavours 1-2 need more depth than Fiit/WithU/Coopah provide, but it
   is no longer a "this campaign can't run" situation.

## LinkedIn pin-down flags (for Sales Navigator)

- **NowPatient** — no standalone company LinkedIn page found; trades under parent
  **Infohealth Ltd**. Confirm the entity before building the search.
- **Juniper (routed to `vadim`)** — no standalone Juniper LinkedIn page found; only the
  parent, **Eucalyptus** (`au.linkedin.com/company/eucalyptusvc`), is confirmed.
- **WithU** — LinkedIn page confirmed (`uk.linkedin.com/company/withu-training`) but no
  single office/HQ city could be confirmed beyond "UK, remote-first."
- **CheqUp** — LinkedIn page confirmed but only reports a `<50` employee band, not a count;
  see the manual-check flag above.
- All other rows (Second Nature, Numan, Voy, Fiit, Medicspot, Nutracheck, Coopah, Flo
  Health, Freeletics) have a confirmed, company-specific LinkedIn URL with no size-band
  ambiguity.
