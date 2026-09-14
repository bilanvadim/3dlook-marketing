# Target Companies — 2026-09-14-eu-erakulis-similar

## Summary

- **Total on the `olena` list: 15** (gate: ≥12 to proceed to step 3 — cleared; target was 15-20 — hit the floor of the target band).
- **Routed out: 1** (Simple → `katerina`, London product HQ; see `companies-routed-out.csv`).
- **Verification:** `web-verify.py` — 14 `verified-live`, 2 `verified-manual` (Lifesum, DoFasting, both JS-shell sites that block a plain HTTP fetch; cleared by a manual Google Play + jobs-page check, see Detailed notes). 0 `dead`, 0 unresolved `blocked` in the final file.
- **`validate-companies --profile olena --write-routed`: exit 0.** 15 proceed, 1 routed to `katerina`, 0 errors, 0 warnings. No "maps to no profile" warning was raised — Ukraine, Cyprus, Poland, Germany, Sweden, Czech Republic, Lithuania and the routed UK row all resolved cleanly against `PROFILE_GEO`.
- **Hypothesis fit: high.** Every row is a real consumer subscription app with a live paid tier, product HQ in Continental Europe (or Kyiv under the 2026-09-14 waiver), no camera-scan shipped, and 25+ employees confirmed or group-scale evidence that clears it.
- **Per-flavour counts:** flavour 1 (multi-pillar wellness) 3, flavour 2 (training / AI-coaching) 6, flavour 3 (nutrition / habit / GLP-1) 6.

## Company list

| # | Company | HQ | Employees | Revenue | Fit | Why fit | Source |
|---|---------|-----|-----------|---------|-----|---------|--------|
| 1 | [BetterMe](https://betterme.world/) | Kyiv, Ukraine (legal seat Paphos, Cyprus) | 736-766 | Not disclosed | 5 | Literal multi-pillar app (fitness + nutrition + mindfulness) with a paid subscription and a Smart Scale add-on that ships shallow body-composition data, not a camera scan. | [Wikipedia](https://en.wikipedia.org/wiki/BetterMe) |
| 2 | [Gymondo](https://www.gymondo.com/) | Berlin, Germany | 82-100 | Not disclosed; 500,000+ paying subscribers (Gymondo+7Mind) | 5 | The clearest literal Erakulis pattern: fitness + nutrition + meditation in one subscription since the Dec 2023 7Mind acquisition; DACH's leading D2C fitness platform. | [Oakley Capital](https://www.oakleycapital.com/news-and-insights/7nxt-acquires-wellbeing-app-7mind-to-create-the-leading-platform-for-physical-and-mental-fitness) |
| 3 | [Activerse (Diet & Training by Ann)](https://healthyplanbyann.com/) | Poznan, Poland | 37 | $1M-$10M | 4 | Polish multi-pillar app (workouts, meal plans, Pilates, a relaxation/breathing pillar); closes the Poland sweep gap. | [LeadIQ](https://leadiq.com/c/activerse/5a1da70b2300005e009a7046) |
| 4 | [Freeletics](https://www.freeletics.com/) | Munich, Germany | 103-120 | Not disclosed; 54M+ users claimed | 4 | Hypothesis's flavour-2 anchor: AI-coaching training app (Coach+) with a large European subscriber base, now scored in its true home market. | [Wikipedia](https://en.wikipedia.org/wiki/Freeletics) |
| 5 | [Fitify](https://gofitify.com/) | Prague, Czech Republic | 27-29 | Not disclosed; 20M+ users claimed | 3 | Small but genuine AI-driven training app clearing the 25 floor; a CEE training-flavour company beyond Freeletics. | [PitchBook](https://pitchbook.com/profiles/company/504001-45) |
| 6 | [FitCoach (Welltech)](https://welltech.com/products/fit-coach/) | Kyiv, Ukraine (legal seat Limassol, Cyprus) | 793-810 (group) | Not disclosed; parent 220M+ installs | 4 | Personalized home-training coaching app, the training anchor of the Welltech portfolio. | [Google Play developer page](https://play.google.com/store/apps/dev?id=5137904782958257230&hl=en_US) |
| 7 | [Muscle Booster (Welltech)](https://musclebooster.welltech.com/) | Kyiv, Ukraine (legal seat Limassol, Cyprus) | 793-810 (group) | Not disclosed; parent 220M+ installs | 4 | Strength-training + meal-recommendation app; combines training and nutrition guidance in one subscription. | [musclebooster.welltech.com](https://musclebooster.welltech.com/) |
| 8 | [WalkFit (Welltech)](https://walkfit.welltech.com/) | Kyiv, Ukraine (legal seat Limassol, Cyprus) | 793-810 (group) | Not disclosed; parent 220M+ installs | 3 | Walking-programme app with an in-app step counter and a paid tier; thinner fit, body composition is not the core loop. | [walkfit.welltech.com](https://walkfit.welltech.com/) |
| 9 | [Yoga-Go (Welltech)](https://yogago.welltech.com/) | Kyiv, Ukraine (legal seat Limassol, Cyprus) | 793-810 (group) | Not disclosed; parent 220M+ installs | 3 | Yoga/mobility app with a real subscription; weakest body-metrics story in the portfolio. | [Cybernews review](https://cybernews.com/health-tech/yoga-go-app-review/) |
| 10 | [Omo (Welltech)](https://welltech.com/products/omo/) | Kyiv, Ukraine (legal seat Limassol, Cyprus) | 793-810 (group) | Not disclosed; parent 220M+ installs | 4 | Weight-tracking / nutrition Welltech brand; the portfolio's clearest flavour-3 fit. | [welltech.com/products/omo](https://welltech.com/products/omo/) |
| 11 | [Yazio](https://www.yazio.com/) | Erfurt, Germany | 144 | Not disclosed | 5 | Hypothesis's flavour-3 anchor; the largest confirmed single-app headcount on the list, with a clear paid Pro tier. | [Tracxn](https://tracxn.com/d/companies/yazio/__-VVSNx5bsv7s50vG9YnE1PoePeF8t3pgPMiAEBzSPSA) |
| 12 | [Fastic](https://fastic.com/) | Berlin, Germany | 51-100 | Not disclosed; 10M+ users in 150+ countries | 4 | Fasting and nutrition tracker with an AI chatbot and a paid Fastic Plus tier. | [Startbase](https://www.startbase.com/organization/fastic/) |
| 13 | [Lifesum](https://lifesum.com/) | Stockholm, Sweden | 50-70 (range) | Not disclosed | 4 | Hypothesis's flavour-3 anchor with a live GLP-1 companion mode; verified manually after a blocked automated check. | [Google Play](https://play.google.com/store/apps/details?id=com.sillens.shapeupclub) |
| 14 | [DoFasting (Kilo Health)](https://dofasting.com/) | Vilnius, Lithuania | 500+ (group) | Not disclosed; parent group revenue >€233M (2025) | 3 | Intermittent-fasting app, #1 US App Store Health & Fitness app in 2020, real paid tier. | [PR Newswire](https://www.prnewswire.com/news-releases/kilo-health-turns-kilo-backing-the-next-generation-of-global-startups-302611938.html) |
| 15 | [Keto Cycle (Kilo Health)](https://ketocycle.diet/) | Vilnius, Lithuania | 500+ (group) | Not disclosed; parent group revenue >€233M (2025) | 3 | Ketogenic-diet app with 270,000+ subscribers and a real paid plan; widens the Baltics/CEE sweep. | [ketocycle.diet/about](https://ketocycle.diet/about) |

**Routed out (not on the `olena` gate count):**

| Company | HQ resolution | Routes to | Why |
|---|---|---|---|
| [Simple](https://simple.life/) | Legal seat Limassol, Cyprus (2015); product HQ resolves to London per 2025-2026 funding coverage | `katerina` | TechCrunch, Vestbee and Tech.eu all call the $35M Series B "British"/"London-based" in Oct 2025; CEO Mike Prytkov is active in the London dietetics community in 2026; no evidence found of a Cyprus product team post-raise. |

## Detailed notes (top 10, by fit score)

### 1. BetterMe
- Website: https://betterme.world/
- LinkedIn: https://cy.linkedin.com/company/betterme-company
- Recent news / triggers: still actively hiring Kyiv-based product/engineering roles per its careers page while legally headquartered in Paphos, Cyprus — the exact "BetterMe/Welltech shape" the hypothesis names.
- Existing tech stack hints: ships its own Smart Scale hardware with app sync (weight, body fat %, muscle mass, sleep, heart rate, stress) — this is the shallow body-metrics floor the sub-segment wants, not a camera scan.
- Why fit: BetterMe is the single closest analogue to Erakulis on this list — one paid subscription spanning fitness, nutrition and mindfulness coaching, sold at real scale (700+ employees). It already treats body composition as a feature worth building hardware for, which is exactly the "visible progress" pain the use case addresses, and it has not shipped a camera-based scan. It also carries an optional clinician-prescribed GLP-1 add-on, which keeps it inside flavour 3's scoring signal even though it is scored here as the flavour-1 anchor. Kyiv product HQ is in scope under Vadim's 2026-09-14 waiver.

### 2. Gymondo
- Website: https://www.gymondo.com/
- LinkedIn: https://www.linkedin.com/company/gymondo-gmbh
- Recent news / triggers: acquired the Berlin meditation app 7Mind in December 2023 (Oakley Capital-backed deal), merging fitness + nutrition + mindfulness into one subscriber base of 500,000+.
- Existing tech stack hints: no evidence of smart-scale or camera-scan integration; progress tracking is self-reported inside workout/nutrition plans.
- Why fit: Gymondo is the most literal Erakulis pattern found in this pass — a training + nutrition platform that bought its way into the third pillar (mind) rather than building it, the exact "buy don't build" instinct FitXpress is selling into for body data. It is DACH's leading direct-to-consumer fitness subscription brand, well past the 25-employee and $1M floors, and the 7Mind deal is 33 months old, outside the 18-month recent-acquisition anti-case window.

### 3. Activerse (Diet & Training by Ann)
- Website: https://healthyplanbyann.com/
- LinkedIn: https://www.linkedin.com/company/activerse
- Recent news / triggers: none found this pass beyond steady growth (2.3-3M+ downloads); included primarily because it closes a real sweep gap (Poland), not because of a timing trigger.
- Existing tech stack hints: no smart-scale or camera-scan evidence; the app's "Balance" pillar (relaxation/breathing) plus meal plans plus workouts is a genuine three-pillar structure built around influencer Anna Lewandowska.
- Why fit: this is the Poland/CEE sweep's best find — a real multi-pillar consumer subscription business (37 employees, $1M-$10M revenue) that nobody on the desk pass had named. It also runs a B2B white-label app framework alongside its B2C brand, which is worth flagging to the buyer persona search in step 3 (the Head of Product for the B2C brand specifically, not the B2B framework team).

### 4. Freeletics
- Website: https://www.freeletics.com/
- LinkedIn: https://www.linkedin.com/company/freeletics
- Recent news / triggers: Coach+, an LLM-based coaching layer, is live; camera-based motion tracking was described as "experimental" in mid-2024 and its shipped status is unconfirmed.
- Existing tech stack hints: no camera body-scan found on the app listing; progress tracking is training-log and self-reported metrics.
- Why fit: named directly in `icp-detail.md` §8 as a Connected & Digital Fitness example and re-verified live for this campaign (Munich, 103-120 employees, source-conflict noted). This is its true home market — the UK list routed it out as a geo mismatch, so the fit score here (4, up from 3 on the UK list) reflects that it is now being evaluated on the market it actually serves. Ownership is left unconfirmed: this pass and the hypothesis's own desk pass surfaced two different, uncorroborated acquisition stories (a 2022 Infront Sports & Media deal vs. a 2018 investor consortium), neither backed by a primary source (Handelsregister or a company statement).

### 5. FitCoach (Welltech)
- Website: https://welltech.com/products/fit-coach/ (the app's own subdomain, `fitcoach.fit`, did not resolve from this VPS — DNS failure on first verification pass; the corporate product page is live and carries the same app)
- LinkedIn: https://www.linkedin.com/company/welltech (parent; no separate brand page found)
- Recent news / triggers: none specific to this brand; Welltech overall is expanding offices (Limassol, Warsaw, Barcelona, London, Kyiv).
- Existing tech stack hints: integrates with Apple Health and Fitbit for steps; no body-composition scan.
- Why fit: FitCoach is Welltech's flagship training brand (12.5M+ downloads) and the strongest flavour-2 fit inside the group. Per the hypothesis's multi-brand rule, the row is the app brand, never the Welltech holding company, and the buyer is that brand's product owner, not Welltech's group CEO.

### 6. Muscle Booster (Welltech)
- Website: https://musclebooster.welltech.com/
- LinkedIn: https://www.linkedin.com/company/welltech (parent)
- Recent news / triggers: none specific found this pass.
- Existing tech stack hints: combines a strength-training plan with meal recommendations; no body-scan evidence.
- Why fit: the second Welltech brand carried on this list because it pairs training with nutrition guidance under one subscription, closer to a multi-pillar structure than FitCoach alone, while still being sold as its own product with its own product owner.

### 7. Omo (Welltech)
- Website: https://welltech.com/products/omo/
- LinkedIn: https://www.linkedin.com/company/welltech (parent)
- Recent news / triggers: none specific found this pass.
- Existing tech stack hints: weight-tracking core loop; no smart-scale or camera-scan integration found.
- Why fit: Omo is the Welltech brand that sits most naturally in flavour 3 (nutrition/weight tracking), giving the group a spread across two flavours rather than concentrating every Welltech row in flavour 2.

### 8. Yazio
- Website: https://www.yazio.com/
- LinkedIn: https://www.linkedin.com/company/yazio-gmbh
- Recent news / triggers: none found this pass beyond continued growth to 144 employees (Jun 2026).
- Existing tech stack hints: manual weight and macro logging; a Pro subscription tier; no body-composition scan.
- Why fit: named directly in the hypothesis as the flavour-3 anchor, and it re-verifies as the largest single-company headcount on this list outside the multi-brand groups. A calorie-tracking category leader with a real paid tier and no scanning feature to displace.

### 9. Fastic
- Website: https://fastic.com/
- LinkedIn: https://www.linkedin.com/company/fastic/
- Recent news / triggers: none found this pass; steady scale (10M+ users, 150+ countries).
- Existing tech stack hints: an AI chatbot for nutrition/meal guidance sits alongside fasting-window and manual body-metric tracking; no scan.
- Why fit: a genuine fasting-and-nutrition subscription app clearing the 25-employee floor under either headcount source found (Startbase's 51-100 or the hypothesis desk pass's PitchBook ~30), with body metrics as a real but shallow part of the product.

### 10. Lifesum
- Website: https://lifesum.com/
- LinkedIn: https://www.linkedin.com/company/lifesum-app/
- Recent news / triggers: markets an "AI + GLP-1" positioning directly on its site, ahead of Germany becoming the first EU market for the Wegovy pill (Sep 2026) — a live instance of the flavour-3 GLP-1 scoring signal.
- Existing tech stack hints: manual weight/macro logging; no scan.
- Why fit: the hypothesis's second named flavour-3 anchor. `web-verify.py` returned `blocked:no-title-js-shell` (the site renders via JavaScript and did not return a `<title>` to a plain HTTP fetch), consistent with the same block recorded on the 2026-09-02 UK quarantine pass. Manually confirmed 2026-09-14: `lifesum.com` resolves and loads in a normal browser, the app has a live Google Play listing (`com.sillens.shapeupclub`) with 1/3/12-month auto-renewing Premium subscriptions, and product HQ is Stockholm per the company's own Stockholm jobs page. Headcount is a genuine three-way conflict (PitchBook 67 / jobs page "60+" / one aggregator's 11-50 band) but clears 25 under every source except the low end of the widest band.

## Excluded candidates and why

**Named by the hypothesis itself (re-confirmed, not re-researched):**
- **Erakulis** — existing 3DLOOK client running phone-camera BodyScan; it is the seed pattern for this campaign and is never a target or named in copy (hypothesis, "Seed account"). Not in any registry by design — excluded by name per the hypothesis.
- **Yazen** — existing 3DLOOK customer (`status: existing_customer_excluded`, `global-company-registry.json`).
- **Zing Coach** — already ships a two-photo AI Body Scan ("Zing Vision") with fat mass, lean mass and scan-to-scan comparison; the confirmed camera-scan-shipped anti-case (Zing Coach help centre; hypothesis reason #3).
- **Foodvisor** — acquired January 2026, 22 employees; inside the 18-month recent-acquisition window (Tracxn).
- **Fitatu** — acquired July 2025, 56 employees; inside the 18-month recent-acquisition window (Tracxn).

**Found and excluded this pass:**
- **FitActive** (Italy) — a 180-gym, 760-employee low-cost gym chain with €126-150M revenue; its "app" is a COVID-era live-stream add-on for members, not a first-party consumer subscription product. Anti-case: "gym chains and health-club operators with no first-party app and no product team."
- **Runtastic** (Austria, owned by Adidas) — Adidas is discontinuing the app and closing its Pasching/Vienna/Salzburg offices through 2026 (170 employees affected). Found dead this pass; not a going concern to sell into.
- **8fit** (Berlin, owned by Withings) — service ends 26 June 2026; Withings is folding its users into the Withings/Withings+ ecosystem. Found dead this pass.
- **Virtuagym** (Amsterdam) — named directly in the hypothesis's anti-case list as B2B gym software; confirmed in this pass as a personal-trainer/gym-facing platform, not a consumer subscription app.
- **EGYM** (Munich) — named directly in the hypothesis's anti-case list as B2B gym software/equipment; confirmed in this pass to have lost independent status as a subsidiary of US-based Playlist in 2024, which would also fail the geo/product-HQ test even if the B2B exclusion did not apply.
- **Noa** (Paris) — an AI-powered Pilates/fitness app that raised a €5M seed round and "officially launched" in 2026; no evidence found of 25+ employees or $1M+ revenue, and a just-launched seed-stage company reads as pre-scale. Excluded for insufficient evidence against both floors, not a confirmed fail — worth a fast re-check in 12-18 months.
- **Swoodie** (Poland) — an AI meal-planner/calorie app built solo by one indie developer since January 2026; explicitly single-founder, far under the 25-employee floor.
- **SportlerPlus** (Hamburg) — a genuine fitness/team-sports app with a paid tier, but no employee count could be confirmed from any public source in this pass (only a 140-follower LinkedIn showcase page was found). Excluded for insufficient evidence rather than a confirmed floor failure; worth a manual LinkedIn check if the list needs to grow.

**Registry check (code, not memory):**
- `workspace/outbound/exclusions/olena-registry.json` — the 54 slugs from `2026-07-21-eu-telehealth-weightloss` are all telehealth/clinical platforms (Terveystalo, Oviva, Qare, Medgate, Sidekick Health and similar); none overlap with the consumer fitness/nutrition/wellness apps in this list. No exclusions triggered.
- `workspace/outbound/exclusions/global-company-registry.json` — checked every candidate; only Yazen (above) matched. No candidate on this list is `active` under another profile.

**Routed, not excluded:** Simple (see Company list above) — routes to `katerina` on a London product-HQ read; it remains a qualified company, just not on this profile's list.

## Coverage gaps / risks

- **Flavour 1 (multi-pillar wellness) landed at 3, the low end of the hypothesis's own 3-5 estimate.** True fitness+nutrition+sleep/mind-in-one-subscription apps are rare outside the known multi-brand groups. Kilo Health's ~30-product portfolio, despite being Europe's largest health-app group by headcount, is almost entirely single-purpose brands (supplements like ColonBroom and Bioma, a fintech app RatePunk, a hardware device Pulsetto) rather than multi-pillar wellness apps — only two of its brands (DoFasting, Keto Cycle) cleared the sub-segment filter, and both landed in flavour 3, not flavour 1.
- **The regional sweep was uneven.** Poland/CEE produced a genuine new find (Activerse). The Nordics sweep reconfirmed Lifesum but surfaced no second Nordic candidate. France, Italy and Spain/Portugal produced no company that clears both the sub-segment filter and the 25-employee/$1M floor: France's best lead (Noa) is too new, Italy's best lead (FitActive) is a gym chain, and general searches for Spain/Italy returned only aggregator "best apps" lists dominated by US/UK brands already excluded elsewhere. Benelux surfaced only B2B anti-cases (Virtuagym) and sub-scale 2009-era apps (Fitmo, Relive) that do not fit the sub-segment. If step 3 people-pulls come up thin on Welltech or Kilo Health (large groups with fewer distinct buyer-type titles per brand than their headcount suggests), there is not an obvious backfill company waiting in these geographies from this pass.
- **Five rows (the four remaining Welltech brands and both Kilo Health brands) report group-level headcount and revenue, not brand-level.** Per-brand figures are not publicly disclosed for either group. This is consistent with how the hypothesis itself already treated Freeletics and Yazio's revenue as "not disclosed," but it is a thinner evidentiary base for five rows out of fifteen — flag if `icp-validation` needs brand-specific numbers.
- **Freeletics' ownership is still unresolved after two independent passes** (the hypothesis's 2026-09-14 desk pass and this campaign's research). Two different, uncorroborated stories exist (a 2022 Infront Sports & Media acquisition; a 2018 investor consortium), neither with a primary source. Do not name a parent company for Freeletics in outreach copy.
- **Simple's HQ call is a judgment call, not a certainty.** The evidence (funding-press language, CEO's London activity) points to London, but the company's registration and internal team structure were not directly observable from this box. `katerina`'s researcher should re-confirm before building a campaign around it.
- **Two dead companies found this pass (Runtastic, 8fit) are a market signal worth carrying into positioning, not just a research footnote:** both are single-pillar training/nutrition apps being folded into a hardware ecosystem (Adidas, Withings) rather than sustained as standalone subscription products, which is consistent with the "don't build, buy the scan" pitch this campaign is built around.
