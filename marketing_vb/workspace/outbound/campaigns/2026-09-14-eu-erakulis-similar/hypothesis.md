---
product: fitxpress
profile: olena
market: Continental Europe (UK excluded)
created: 2026-09-14
status: approved
approved: 2026-09-14
---

# Hypothesis: Continental European Consumer Wellness, Fitness and Nutrition Apps (Erakulis look-alike)

- **Campaign:** `2026-09-14-eu-erakulis-similar`
- **Owner:** Olena Kudryavtseva (`olena`, Continental Europe, UK excluded)
- **Seed account:** **Erakulis**, CR7's fitness + nutrition + mind subscription app. It is **an existing 3DLOOK client** running phone-camera BodyScan. It is the internal pattern this campaign clones. It is never a target and it is never named in copy.
- **Template:** `2026-09-01-uk-erakulis-similar/hypothesis.md` (2026-09-12 rewrite, `katerina`). Structure mirrored, UK facts not reused.
- **Same ICP segment, other markets:** `2026-08-07-us-digital-fitness` (`nick`, closed), `2026-08-14-au-digital-fitness` (`vadim`), `2026-09-01-uk-erakulis-similar` (`katerina`).

## Vadim's decisions 2026-09-14

Approved, with these answers to the draft's open questions:

1. **Employee floor 25, this campaign only.** `icp-detail.md` is not amended. Companies with 25-49 employees go on the main list, and there is no separate file. Gate: ≥12 companies at 25+ proceeds to step 3; fewer than 12 stops at step 2 and goes back to Vadim. Target 15-20.
2. **No exclusivity with Erakulis.** Its competitors are fair targets.
3. **Ukrainian-founded apps with product decisions in Kyiv are in scope on `olena`,** tagged `product_hq=UA` in `notes`. This is Vadim's waiver of the `icp-detail.md:563` licensed-markets exclusion, for this campaign only. Product decisions in Russia or Belarus stay excluded.
4. **Cyprus, Malta, Luxembourg, Iceland and Liechtenstein route to `olena`,** and are being added to `PROFILE_GEO` in `scripts/outbound-pipeline.py`.
5. **Flavour 4 (app-first weight-management and GLP-1 programmes) is out of scope.** It is now an anti-case, as 07-21 territory. GLP-1 mode stays a scoring signal inside flavour 3.
6. **English only** for outreach.
7. **"112,100 scans in 2025"** (`proof-points.md:113`, 3DLOOK's total across all customers) **is cleared for cold copy** as the second anonymous proof, with no client name and no geography.

Only Open question #7 (EU compliance answers) remains open.

> **What the UK run teaches this one.**
> 1. At a 50-employee floor the UK list came out at 4 companies, and 10 at 25. The floor, not the product filter, did most of the killing, and it took three research passes to find that out. Vadim set this campaign's floor at 25 from the start (2026-09-14), so step 2 builds one list in one pass, with no floor rebuild.
> 2. Pulling Sales Navigator by company returned whole staff lists: 72 of 98 UK people were never candidates. The 81 Freeletics rows in that same export hold 21 buyer-type titles, mostly engineering. Step 3 here pulls by title.
>
> **What `olena`'s last campaign teaches it.** `2026-07-21-eu-telehealth-weightloss` sent 307 contacts. It accepted at 25.0% (73/292), then drew 1 reply from 67 message-1 sends. The post-mortem found three causes:
> - The text: 0 of 307 message-1 texts carried a product specific.
> - The list was built without step 2, and 39% of sends went to one out-of-thesis account.
> - 173 WEAK contacts were sent without review.
>
> All three are closed off in Validation criteria below. The account itself accepted invites at a normal rate. The list, the message and the WEAK tier failed.

---

## Vertical

Consumer subscription wellness, fitness and nutrition apps whose product decisions sit in Continental Europe. This is the "Connected & Digital Fitness" ICP segment (`icp-detail.md` §8, which names Germany and the Nordics as target geos and Freeletics as an example account), run as the European slice on `olena`. The job to be done is the same as in the US, AU and UK campaigns: keep paying subscribers by showing them visible physical progress.

## Sub-segment

Consumer apps with product HQ in Continental Europe (defined below) that sell a paid subscription for fitness, nutrition, body transformation or multi-pillar wellness, with:

- **~$1M+ annual recurring revenue** (the §8 floor). §8 says "Series B-public". Here revenue decides and funding stage does not: a privately held group with nine-figure revenue and no venture round is in, and a well-funded app with no revenue is out.
- **25+ employees, a deliberate campaign-level deviation** from the `icp-detail.md` universal exclusion ("companies under 50 employees"), **Vadim's call 2026-09-14**. The UK run found the 50 floor doing most of the killing and needed three research passes to learn it, so this campaign sets 25 from the start. The deviation applies to **this campaign only**: it does not amend the ICP document, and it does not carry to other campaigns or profiles without Vadim saying so again. A 25-person app still has to clear the $1M revenue bar and sell a real paid subscription.
  - **Headcount conflicts across the 25 floor** (one source above 25, another below) go on the list. Write `employees` as the range and record the conflict in `notes`. Explain the call in `companies.md`.
- **mobile-first delivery.** A real iOS/Android app that is the product, not a marketing shell.
- **body metrics already shipped but shallow** (self-reported weight, tape measurements, smart-scale import) **or a natural next feature.** An app that already ships a phone-camera body scan is an anti-case.

### Sub-segment: three flavours, with a realistic count

Each estimate is the number of companies likely to survive step 2 at the 25+ floor, from a desk pass on 2026-09-14, re-summed after Vadim set the floor at 25 and removed flavour 4. Named companies are research leads. Re-verify and re-score every one, and import nothing unchanged.

1. **Multi-pillar wellness apps, the literal Erakulis pattern.** Fitness, nutrition, sleep or mind in one subscription, with body metrics as the missing pillar. This is the strongest flavour in Europe, because the category's biggest players are multi-brand app groups:
   - **BetterMe:** founded in Kyiv in 2017, Cyprus HQ, 665-800 employees depending on source ([Wikipedia](https://en.wikipedia.org/wiki/BetterMe), [LinkedIn](https://cy.linkedin.com/company/betterme-company)).
   - **Welltech:** Ukrainian origin, based in Limassol. Its apps include FitCoach, WalkFit, Omo, Muscle Booster and Yoga-Go ([Welltech](https://welltech.com/about-us/)).
   - **Kilo:** Vilnius. A portfolio across digital weight management, wellness and chronic conditions ([Kilo portfolio](https://kilo.co/portfolio/)).
   - **Gymondo / 7NXT:** Berlin, with the 7Mind acquisition reported ([Tracxn](https://tracxn.com/d/companies/gymondo/__jESGihy3WMAqMLaEbD8HYEf8W2j7yLEGEhcO5qxwQWE)). Check the deal date against the acquisition anti-case.

   For a group, the target is the app brand that sells the subscription, and that brand's product owner. It is never the holding company. **Estimate: 3-5.**
2. **Training, body-transformation and AI-coaching apps.** These live or die on visible progress. Freeletics (Munich, seed candidate, see the table at the end) is the anchor. Zing Coach is named in §8 as an example, but it now ships its own two-photo body scan, so it is an anti-case. Fitify (Prague, 27-29 employees, [PitchBook](https://pitchbook.com/profiles/company/504001-45)) clears the 25 floor. **Estimate: 2-6.** This stays the thinnest flavour.
3. **Nutrition, habit and calorie-tracking apps with a paid tier,** including consumer apps that added a GLP-1 companion mode.
   - **Anchors:** Lifesum (seed candidate, see the table at the end) and Yazio (Erfurt, 144 employees in June 2026, [Tracxn](https://tracxn.com/d/companies/yazio/__-VVSNx5bsv7s50vG9YnE1PoePeF8t3pgPMiAEBzSPSA)).
   - **Clears the 25 floor:** Fastic (Berlin, ~30 employees, [PitchBook](https://pitchbook.com/profiles/company/442287-28)).
   - **Found and excluded:** Foodvisor and Fitatu (see Anti-cases).
   - **HQ conflict to resolve:** Simple. 2025 funding coverage calls it London-based ([TechCrunch](https://techcrunch.com/2025/10/01/kevin-harts-vc-firm-leads-35m-series-b-for-weight-loss-app-simple/), [Vestbee](https://www.vestbee.com/insights/articles/simple-life-secures-35-m)), while the 2026-08-07 US research recorded Limassol. If product decisions sit in London it routes to `katerina`.
   - **GLP-1 is a scoring signal inside this flavour.** Germany is the first EU market for the Wegovy pill, in September 2026 ([FoodNavigator](https://www.foodnavigator.com/Article/2026/08/06/germany-first-to-launch-wegovy-pill/)), and Lifesum already markets GLP-1 support ([Lifesum](https://lifesum.com/page/ai-glp-1-the-future-of-personalised-weight-loss)).

   **Estimate: 3-7.**

**Realistic total: 8-18 companies at the 25+ floor** (the sum of the three flavour estimates above). Research will surface names this desk pass does not know, above all in France, Italy, Iberia, Poland and the Nordics. Treat these numbers as a floor for the known market, not a ceiling.

### Sub-segment: geo and HQ resolution

**Continental Europe = EU + EEA + Switzerland:** DACH, Nordics (Iceland included), Benelux, France, Iberia, Italy, CEE, the Baltics, Cyprus and Malta. Other markets route to their own profile through `validate-companies --write-routed`: UK to `katerina`, US to `nick`, AU/NZ to `vadim`, Israel to `katya`. Route these companies. Never discard them.

**HQ means where product decisions sit, the same rule as on the UK campaign.** The registered office alone never decides. For every row, step 2 establishes where product decisions sit, checking in this order:

1. Where the CEO and the CPO / Head of Product are located on LinkedIn.
2. Where product and engineering roles are advertised.
3. How press coverage places the company ("Munich-based").

Write that country into `hq_country`. Where the legal seat differs, record both in `notes` as `legal_hq=...; product_hq=...; hq_basis=...`.

| Situation | Route |
|---|---|
| EU legal seat, product decisions in the EU | `olena` |
| Cyprus / Malta / Luxembourg / Ireland legal seat, product team in another EU state (Poland, Lithuania, Spain, Portugal and so on) | `olena`, `hq_country` = the state where the product team sits |
| Product decisions genuinely in Cyprus, Malta, Luxembourg, Iceland or Liechtenstein | `olena` (Vadim, 2026-09-14). `hq_country` = the true country |
| **Ukrainian-founded, EU-registered, product decisions in Kyiv** (the BetterMe / Welltech shape) | **`olena`, tagged `product_hq=UA` in `notes`,** so the whole block can be pulled out in one move. Ukraine is outside the EU + EEA + Switzerland definition and outside the licensed markets in the ICP universal exclusion (`icp-detail.md:563`). **Vadim waived that exclusion on 2026-09-14, for this campaign only.** `icp-detail.md` is not amended, and the waiver does not carry to other campaigns or profiles |
| Ukrainian-founded, product leadership relocated to an EU city | `olena`, `hq_country` = that EU state, no tag |
| EU legal seat, product decisions in the US / UK / Israel / AU | the profile for that market |
| US-incorporated parent with the product organisation in Continental Europe | `olena`. On the UK run, Flo Health's Delaware parent did not move it out of London either |
| EU brand of a foreign group whose product decisions sit at the parent (the Juniper shape) | the parent's profile |
| Product decisions in Russia or Belarus | Excluded (confirmed by Vadim, 2026-09-14). No profile covers these markets. List as excluded with the reason. Do not route |

## Use case

FitXpress becomes the embedded body-measurement and progress-visualisation layer inside a European consumer wellness app. A 2-photo smartphone scan returns 80+ measurements, body composition (body fat %, lean mass, fat mass, BMI, BMR) and a 3D progress model in under 45 seconds via API/SDK. The app gets the BodyScan feature its retention curve needs without building computer vision in-house. That is what Erakulis did.

## Why plausible

1. **Retention in this category is front-loaded, and visible progress is a lever the app controls.**
   - Health & Fitness is an annual-plan category: 68% of its subscriptions are annual. Across all categories, nearly 30% of annual subscriptions are cancelled in the first month ([RevenueCat, State of Subscription Apps 2025](https://www.revenuecat.com/state-of-subscription-apps-2025)).
   - Body composition has barely started to move in those first weeks, and the scale is the worst instrument for that window: weight stays flat while the waist shrinks. A circumference change and a 3D overlay give the subscriber something to see before they decide.
   - `icp-detail.md` §8 names this pain verbatim: "пользователи теряют мотивацию без visible progress".
   - The audience is growing. European gym memberships reached 75.5 million at the end of 2025, up 5.8%, on €39.1 billion of revenue ([Deloitte / EuropeActive, European Health & Fitness Market Report 2026, via HCM](https://www.healthclubmanagement.co.uk/health-club-management-news/EHFF-underway-with-results-of-European-Health-and-Fitness-Market-Report-2026-being-presented/362794)).

2. **The European category has what the UK list lacked: product organisations big enough to buy.** The UK list that reached step 4 was five companies of 27-36 people, where the whole product team was two or three people, plus a pharmacy-shaped company with no product organisation (UK `STATUS.md`). The Continental European category is concentrated in a few large groups:
   - **Kilo:** its release dated 12 November 2025, issued before the year closed, says revenue will "surpass €233 million this year" and that Kilo employs over 500 people ([PR Newswire](https://www.prnewswire.com/news-releases/kilo-health-turns-kilo-backing-the-next-generation-of-global-startups-302611938.html)). This is the company's own in-year statement. Full-year 2025 results are not in the release.
   - **Welltech:** 220 million+ installs across its apps ([Welltech](https://welltech.com/about-us/)) and 810 employees ([Tracxn](https://tracxn.com/d/companies/welltech/__82HtCEoyc_qWvIOuutyArQ2qHiuUe8Y6zwbQkgQhQ3Y)).
   - **Yazio:** 144 employees.
   - **Freeletics:** ~103 employees ([Tracxn](https://tracxn.com/d/companies/freeletics/__pKobGicdeA1yr3K6c-R6ujJ2aNB8IZhFSIGr5ZQKRy8)).

   Headcounts other than Kilo's come from aggregators, and step 2 re-checks every one.

   **The UK run's proof gap shrinks here.** No client may be named. Two anonymous proofs are licensed, both with no client name and no geography: "one platform ran 34,000 scans in 2025" (`case-studies/yazen.md`), and 112,100 scans in 2025 across all 3DLOOK customers (`proof-points.md:113`, cleared by Vadim on 2026-09-14). They answer different questions. 34,000 shows one integration running at volume, and 112,100 shows the platform's total production volume. The UK Meds 7,500-scan fact is licensed only as "a UK online pharmacy". It is not used on this campaign: `olena`'s brief excludes UK references, and a pharmacy checkout is the wrong product shape for a consumer app. Against a group with 220 million installs, neither figure shows their scale. The sequence leads with reasons #1 and #3 and uses a scan figure as supporting evidence.

3. **AI coaching no longer differentiates in Europe, and a European competitor already ships the camera scan.**
   - Freeletics launched Coach+, an LLM coach built on its user data ([Fitt Insider](https://insider.fitt.co/press-release/freeletics-unveils-a-new-era-in-digital-fitness-with-the-launch-of-coach/)). In June 2024 ISPO described the next step as motion tracking through the phone camera, to analyse and correct the user's movements, "at an advanced stage, but is still experimental" ([ISPO](https://www.ispo.com/news-article/sportstech/fitness-apps-take-off-ai-coach-with-human-communication)). Whether it shipped is unknown; step 2 checks the app listing.
   - Zing Coach's CEO describes the category moving from apps to AI agents ([Tech.eu, August 2025](https://tech.eu/2025/08/07/from-workout-apps-to-ai-companions-a-paradigm-shift-in-fitness-tech/)).
   - Zing already ships a two-photo AI Body Scan with fat mass, lean mass and scan-to-scan comparison, marketed as its own "Zing Vision" model ([Zing help centre](https://zingcoach.zendesk.com/hc/en-us/articles/15325477532316-Body-Scan)). It raised a $10M Series A in 2024 ([Healthcare IT Today](https://www.healthcareittoday.com/2024/07/08/ai-fitness-app-zing-coach-raises-10-million-in-series-a-funding-to-combat-inactivity-and-build-healthy-habits/)).

   This cuts two ways, and both matter for the campaign:
   - **It helps.** Every product lead at a European training or nutrition app can watch a direct competitor sell body composition as a retention feature, so the category needs no education.
   - **It raises the build objection.** Zing presents the scan as its own model, and that is the example the objection will cite. The answer: a pre-trained model via API/SDK, with no computer-vision team to hire and keep. `icp-detail.md` gives 2-4 weeks as the typical time for a basic integration. That figure is generic, and no customer-specific timeline is claimed.

   Competitors are never named in cold copy (`competitors.md`).

4. **The consumer-side regulatory lane is clear, and EU guidance says so directly.**
   - EU guidance on medical device software states that software intended for lifestyle and well-being purposes is not a medical device ([MDCG 2019-11](https://health.ec.europa.eu/system/files/2020-09/md_mdcg_2019_11_guidance_en_0.pdf), revised June 2025, per [Emergo by UL](https://www.emergobyul.com/news/european-revision-primary-software-guidance-mdcg-2019-11-revision-1-small-changes-meaningful)). Body-composition trend tracking with no disease claim and no clinical decision stays in that lane.
   - The same line defines an anti-case. A German DiGA is by definition a CE-marked medical device ([BfArM](https://www.bfarm.de/EN/Medical-devices/Tasks/DiGA-and-DiPA/Digital-Health-Applications/Interesting-facts/_node.html)): originally class I or IIa, and also class IIb since the Digital Act (DigiG) took effect on 26 March 2024 ([reuschlaw](https://www.reuschlaw.de/en/news/digital-act-new-regulations-on-digital-health-applications/)). Either way it is a different sale.
   - GDPR applies EU-wide. Beyond the roles sentence, the answers on Article 9, the DPA, SCCs and the EU AI Act are not approved yet (Open question #7). This hypothesis makes no claim about country-level rules.
   - The first hard question from any CTO will be photo processing. The approved answers are: photos deleted immediately or within 30 days per client policy, no personal identifiers processed, encryption at rest and in transit. On roles, verbatim: **"In most enterprise deployments, the customer acts as controller and 3DLOOK acts as processor under GDPR."** Where medical status comes up, the standard line is: **"FitXpress is not a medical device."**

## Target buyer persona

- **Head of Product / VP Product / Chief Product Officer, primary.** Owns the roadmap and the build-vs-buy call on a BodyScan feature. Cares about feature velocity, activation and engagement. Likely objection: "we could build this", which is sharper in Europe than in the UK (reason #3). The answer: a pre-trained model via API/SDK, with no CV team to hire; `icp-detail.md` gives 2-4 weeks as the typical basic integration.
- **Titles with subscription, retention or engagement in the name (Head of Retention, VP Engagement, Head of Growth, Chief Subscription Officer), primary.** Owns the number this use case moves. On the US digital-fitness campaign, the only interested reply came from this kind of title (a Chief Subscription & Content Officer, answering the retention angle). N=1, so treat it as a search priority, not a rule.
- **Founder / CEO / Managing Director, primary for single-app companies under ~200 people.** At multi-brand groups (Kilo, Welltech, BetterMe) the group CEO is not the buyer. The GM or product lead of a specific app brand is.
- **CTO / VP Engineering, `technical-integration` angle, P3, never a cold first touch.** The US campaign got 0 replies from 60 cold `technical-integration` invites. They evaluate and champion internally once a product owner is engaged.
- **Not the buyer:** marketing, brand, content, community, social / PR, partnerships and sales, HR, finance, fitness programming, coaches and nutritionists, customer support, privacy and legal counsel, board and supervisory-board members, investors, freelancers and translators. The 07-21 compliance message went to Oviva's Head of Privacy and got a flat "Not interested".

### Target buyer persona: Sales Navigator pull for step 3

**Pull by title filter inside the approved company list, never by company alone.**

- **Titles to include:** Founder, Co-Founder, CEO, Managing Director, General Manager; Chief Product Officer, VP / Head / Director of Product, Group Product Manager, Product Lead; Head / VP / Director of Growth, Retention, Engagement or Subscription; CTO and VP Engineering (tagged P3).
- **Product Manager titles** only at companies under 200 employees.
- **Invite caps:**
  - ≤5 invites per company.
  - For multi-brand groups, ≤5 per app brand and ≤12 per group.
  - No company or group above 15% of the campaign's invites. On 07-21, 39% of sends went to one account; the US campaign put 48% of its invites into two.
- The 81 Freeletics rows already in the UK export (`2026-09-01-uk-erakulis-similar/sales-nav-raw/people_raw.csv`) were pulled by company and are **not reused**.

## Anti-cases

- **Already contacted on `olena`.** 07-21 wrote 54 company slugs into the registry: Oviva, Wellster, Sidekick Health, Liva Healthcare, Nederlandse Obesitas Kliniek, The Body Clinic, Weight Doctors Nederland, Holi, Annette, LevaHealth, myDiabby, mySugr, Terveystalo (all variants), Doktor.se, Min Doktor, Doktor24, Dr.Dropin, Qare, Medgate, hellocare.ai, Doktr, Doctor.One, HealthHero, MediQuo, Mehiläinen, Capio, Hjemmelegene and the rest. Its 63 accepted-but-silent connections are that post-mortem's re-test group and stay off this list. Run `python3 scripts/outbound-registry.py check --profile olena` before the list ships. The registry is the authority. This bullet is a reminder.
- **Existing 3DLOOK customers:** Yazen, UK Meds, Healthyr and the Mobile Tailor accounts (`status: existing_customer_excluded` in the global registry). **Erakulis is a client but is not seeded in any registry, so the registry check will not catch it. Exclude it by name.** Its competitors are fair targets: there is no exclusivity (Vadim, 2026-09-14).
- **Companies covered by another profile in `global-company-registry.json`,** whatever geo they claim.
- **Apps that already ship phone-camera body scanning or have signed a scanning partner.** Zing Coach is the confirmed case (reason #3). These belong to a competitive-displacement track, not this one. Step 2 fills in `body_metrics` for every row, checking the app listing as well as the homepage.
- **Acquired or merged in the last 18 months.** The buyer's priorities are shifting and the sales cycle stalls. Found on the desk pass:
  - Foodvisor: acquired January 2026, 22 employees ([Tracxn](https://tracxn.com/d/companies/foodvisor/__TrHrEdghLfy6XL02BOeaWJOvg4dicn3SzSp4JlLU59E)).
  - Fitatu: acquired July 2025, 56 employees ([Tracxn](https://tracxn.com/d/companies/fitatu/__QUd0sB_T5f7F9-CBWJG2c7Xa8L1hqWJ7HLaUHrQ4msw)).

  Older ownership changes do not count as recent, but they go in `notes`, because the parent may control the budget. Freeletics' ownership is one to settle in step 2: aggregator summaries conflict on whether Infront Sports & Media acquired it in 2022, and no primary source was found on 2026-09-14.
- **DiGA-listed or CE-marked medical-device apps, and anything sold on medical claims.** A different regulatory sale (reason #4).
- **Free or freemium-only apps with no paid tier.** Universal exclusion.
- **Under $1M revenue, under 25 employees, pre-launch, or no app in the stores.** No integration capacity, no budget. (Floor set at 25 for this campaign only, Vadim 2026-09-14; see Sub-segment.)
- **Gym chains and health-club operators with no first-party app and no product team** (Basic-Fit, RSG Group and similar). A chain with a genuine training app and a product org is scored, not added automatically.
- **B2B gym software, corporate-wellness aggregators and equipment platforms** (EGYM, Virtuagym, Technogym, Urban Sports Club, Wellhub). They embed or resell for their own customers, which is a partnership sale with a different cycle. Wellhub is also Erakulis's corporate-wellness distribution partner ([Wellhub](https://wellhub.com/en-us/blog/press-releases/wellhub-and-erakulis/)).
- **Hardware-first wearables and smart-scale makers** (Withings, Oura, Polar, Suunto). These are device businesses, and Withings sells a competing measurement product.
- **Sports nutrition and supplement e-commerce,** including supplement lines inside app groups. Selling capsules does not depend on showing progress.
- **Content-only platforms:** video libraries, streamed classes and PT course providers with no plan to measure anything.
- **App-first weight-management and GLP-1 programmes: 07-21 territory, not this campaign** (removed from scope by Vadim, 2026-09-14). `2026-07-21-eu-telehealth-weightloss` already wrote the European pure-plays into `olena-registry.json`: Oviva, Wellster (GoLighter), Sidekick Health, Liva Healthcare, Nederlandse Obesitas Kliniek, The Body Clinic, Weight Doctors Nederland, Holi, Annette, LevaHealth, myDiabby and mySugr. Yazen is a customer. The visible remainder is owned outside Olena's market: ZAVA by Hims & Hers, US ([Hims & Hers](https://investors.hims.com/news/news-details/2025/Hims--Hers-Announces-Plans-to-Acquire-ZAVA-Accelerating-Major-European-Growth-Across-the-UK-Germany-France-and-Ireland/default.aspx)); Juniper by Eucalyptus, AU; WeightWatchers' GLP-1 programme under a US parent ([WeightWatchers](https://www.weightwatchers.com/uk/how-it-works/glp-1-programme)); Second Nature, UK-HQ. Consumer nutrition apps with a GLP-1 companion mode stay in flavour 3, where that mode is a scoring signal.
- **Telehealth platforms, online pharmacies and digital-therapeutics companies** (Kry, TeleClinic, Livi, ZAVA and others from the unsent 07-09 and 07-22 lists). That is the EU telehealth thesis, which waits for the 07-21 re-test. Do not bring it in under a fitness label.
- **Public-sector bodies and national nutrition services.**
- **Product decisions outside Continental Europe: route them, do not discard them** (see "Sub-segment: geo and HQ resolution"). Product decisions in Russia or Belarus: exclude, with the reason recorded.

## Validation criteria

**Validated** if all of the following hold:

- **List size: one gate, no gap.** Count companies at the 25+ floor with product HQ in Continental Europe (Kyiv product HQ included under the 2026-09-14 waiver), genuinely matching the sub-segment, none already contacted on `olena`, none a customer, and each one verified as defined in the next bullet.
  - **≥12 → proceed to step 3.**
  - **Fewer than 12 → stop at step 2** and report to Vadim with `companies.csv`.
  - **15-20 is the target, not a gate.** A list of 12-14 proceeds and is reported as under target.
  - Do not pad the list with telehealth, gyms, B2B platforms or supplement brands.
- **Row schema.** Every row carries the full step-2 schema: `company_name, website, linkedin_url, hq_country, hq_city, employees, revenue_estimate, fit_score_1_to_5, fit_reason, source_url, notes`.
  - Every row goes through `web-verify.py`, and only rows whose `verification` starts with `verified` count toward the gate. What the code accepts (`scripts/outbound-pipeline.py`, `validate-companies`):
    - an empty verdict or any `unverified*` value is an error;
    - a `verified*` row with no `source_url` is an error;
    - every other value, `blocked:*` and `dead` included, is only a warning ("not usable as proof"), and the row still passes to step 3.

    The script does not enforce the count, so the researcher does.
  - **A `blocked` row counts only after a manual check.** A person opens the site and the app listing and confirms product HQ, the paid tier and the app. They set `verification=verified-manual` in `companies-verified.csv`, with a `source_url`, and add `manual_check=<who>, <date>, <what was confirmed>` to `notes` in `companies.csv`. `validate-companies` accepts `verified-manual` because it starts with `verified`. `web-verify.py` rewrites the verdict of every row it processes, so a re-run clears the manual verdict; the `notes` entry in `companies.csv` survives and is what allows it to be re-applied. A `blocked` row with no manual check stays listed for a human and does not count.
  - `notes` carries these fields on every row:
    - `legal_hq`, `product_hq` and `hq_basis`, where legal seat and product HQ differ.
    - `body_metrics=`: none / manual / smart-scale / camera-scan-shipped.
    - `glp1_mode=`: yes / no.
    - `parent=` and the acquisition date, where there is one.
    - `flavour=`: 1-3.
- **Company names are canonicalised once** in `companies.csv`. 07-21 sent to Terveystalo under six spellings. For a multi-brand group, the row is the app brand and the group goes in `notes`.
- **Routing check.** `validate-companies --campaign 2026-09-14-eu-erakulis-similar --profile olena --write-routed` exits 0, and every "maps to no profile" warning is resolved in `companies.md`. None is ignored.
- **People.** Step 3 pulls by title (see Target buyer persona), and a job-change check runs before import. **≥30 contacts reach PASS.** WEAK contacts go out only after Vadim reviews them as a separate block. 07-21 sent 173 without review.
- **Message 1 gate.** Every step-5 message 1 carries:
  - at least one product specific from `proof-points.md`, with accuracy wording verbatim from `accuracy-formulations.md`;
  - one line that could only have been written to that company;
  - zero client names and zero pricing.

  This closes 07-21's failure, where 0 of 307 message-1 texts carried a specific.
- **Replies:** ≥10% reply rate and ≥4% positive reply rate, both measured on accepted invites, across the whole sequence.
- **Calls:** ≥3 discovery calls where the prospect names retention or progress visibility as a top-three product priority, unprompted.
- **Pilot:** ≥1 pilot or paid POC within 6 weeks of first send.

**Falsified** if any of the following holds:

- **The segment is too thin.** Fewer than **12** qualified companies at the 25+ floor. Then the Erakulis look-alike segment is too thin for a single-profile campaign in Europe as well as the UK. The next step would be one cross-market campaign by segment, which needs Vadim to set geo discipline aside.
- **It is a displacement market.** ≥3 of the first 15 verified companies already ship a camera body scan or have signed a scanning partner.
- **It is the segment, not the text.** Every message 1 passed the gate, and 14 or more days after the last message 2 went out, ≥30 accepted invites have produced ≤1 reply. The threshold follows from the other profiles' 15.4-18.8% replies on accepted: at a true 15% rate, 30 accepted invites give ≤1 reply only about 5% of the time (binomial). With fewer than 30 accepted at close, the test is inconclusive and cannot falsify, and the post-mortem says so. Under the invite caps above, 30 accepted needs roughly 100-120 invites at 25-30% acceptance, so an inconclusive result is possible.
- **Body data is secondary.** ≥3 calls independently say body data is a nice-to-have next to content and coaching.

## Outreach language

**Decided: English only, in every country, DACH and France included** (Vadim, 2026-09-14). The evidence behind it:

- `2026-07-21-eu-telehealth-weightloss` sent all 307 message-1 texts in English (checked against its `closelyhq-import.csv`) across 12 countries. All 5 replies came back in English (`responses-summary.md`), and none objected to the language. The campaign's measured failure was content: 0 of 307 message-1 texts carried a specific.
- `outbound-message1-template.md` sets Message 1 in English (Vadim, 2026-07-21).
- Every check the copy passes works on English: `detect-ai-tells.py --channel dm`, `terminology-guardrails.md` and the brand checkers. German or French copy would go out unchecked.

## Success metrics

| Metric | Target | Floor |
|---|---|---|
| Companies on validated list (25+) | 15-20 | 12 (the step-2 gate) |
| Contacts at PASS | 45+ | 30 |
| Connection acceptance rate | 30% | 25% (`olena` on 07-21: 73/292 = 25.0%, no note) |
| Reply rate (of accepted) | 15% | 10% (`olena` on 07-21: 4/73 = 5.5%; US, UK and Israel campaigns: 15.4-18.8%) |
| Positive reply rate (of accepted) | 6% | 4% |
| Discovery calls booked | 5-6 | 3 |
| Pilots / POCs agreed | 2 | 1 |

## Rules for steps 3-5 (Vadim, 2026-09-12 and 2026-09-14)

- **No client is named anywhere in cold copy:** Erakulis, Yazen, UK Meds, Healthyr, all of them. Two anonymous proofs are permitted, each stated with no client name and no geography: "one platform ran 34,000 scans in 2025", and 112,100 scans in 2025 across all 3DLOOK customers (`proof-points.md:113`, cleared by Vadim 2026-09-14). The UK Meds 7,500-scan fact is not used on `olena` (reason #2).
- **No pricing anywhere in the sequence:** no price, tier, range hint or "from $X", follow-ups included. A price question goes to a call. For `message-sequencer`, any pricing number is a hard fail.
- **"FitXpress is not a medical device."** and the GDPR roles sentence are both used verbatim.
- **Competitors are never named in cold copy,** Zing Coach included.
- **Context for the call, not the copy:** the published price table stops at 20,000 requests/month. The larger groups on this list are custom-pricing conversations from the first call. The UK run's lever carries over: offer quarterly check-in scans rather than monthly.

## Open questions

1. ~~Employee floor: 50 as written, or 25 as on the UK run?~~ **Resolved 2026-09-14: 25, this campaign only.** `icp-detail.md` is not amended. One list at 25+, no separate file.
2. ~~Geo edge cases: Kyiv product HQ; Cyprus, Malta, Luxembourg, Iceland and Liechtenstein.~~ **Resolved 2026-09-14.** (a) Ukrainian-founded apps with product decisions in Kyiv are in scope on `olena`, tagged `product_hq=UA`. This is Vadim's waiver of the `icp-detail.md:563` licensed-markets exclusion, for this campaign only. Russia and Belarus stay excluded. (b) The five countries route to `olena` and are being added to `PROFILE_GEO`.
3. ~~Flavour 4: confirm the shrink.~~ **Resolved 2026-09-14: removed from scope.** App-first weight-management and GLP-1 programmes are an anti-case (07-21 territory). GLP-1 mode stays a scoring signal in flavour 3.
4. ~~Outreach language: English only?~~ **Resolved 2026-09-14: English only.**
5. ~~Channel conflict with Erakulis.~~ **Resolved 2026-09-14: no exclusivity.** Erakulis's competitors are fair targets.
6. ~~Proof at this scale: is 112,100 scans in 2025 cleared for cold copy?~~ **Resolved 2026-09-14: cleared** as the second anonymous proof, with no client name and no geography (Rules for steps 3-5).
7. **EU compliance answers beyond the roles sentence.** None of these is approved in `compliance.md`, and EU CTOs will ask about all of them: whether body photos count as special-category data under Article 9 in a consumer wellness context, the DPA, SCCs, and any EU AI Act classification question. Needed before discovery calls, not before step 2.

## Seed candidates: status on 2026-09-14

| Company | Came from | Registry | Desk re-check 2026-09-14 | Step-2 treatment |
|---|---|---|---|---|
| **Freeletics** (Munich) | Routed to `olena` from the UK list on 2026-09-12: fit 3, `verified-live`, 103-120 employees | Not in `olena-registry.json` or any other registry | ~103 employees in May 2026 ([Tracxn](https://tracxn.com/d/companies/freeletics/__pKobGicdeA1yr3K6c-R6ujJ2aNB8IZhFSIGr5ZQKRy8)); ownership unconfirmed (aggregator summaries conflict on a 2022 Infront Sports & Media acquisition); Coach+ LLM coach; camera motion tracking described as experimental in June 2024 | Flavour 2 anchor. Re-verify live. Re-score, because fit 3 was scored against the UK question. Record `body_metrics`, and `parent=` only once a primary source (commercial register or company statement) confirms the owner |
| **Lifesum** (Stockholm) | Routed to `olena` from the UK quarantine list on 2026-09-02: `blocked:no-title-js-shell`, never verified | Not in any registry. The 07-09 EU telehealth list excluded it ("B2C, no clinical component") under a different thesis, so it is free here | 67 employees ([PitchBook](https://pitchbook.com/profiles/company/62386-12)), "60+" on its [jobs page](https://jobs.lifesum.com/locations/stockholm), 11-50 at another aggregator, a range that straddles the 25 floor. Markets GLP-1 support | Flavour 3 anchor. `web-verify` will probably block again, so verify it manually and settle headcount on LinkedIn. Per the Sub-segment rule, it stays on the main list with the range and the conflict in `notes`. It counts toward the step-2 gate only once its verdict is `verified-manual` (Validation criteria) |

---

## Next step

Approved by Vadim on 2026-09-14. The sequence: `hypothesis-gate --stamp` (run by the coordinator), then `search-health.py`, then `company-researcher` (step 2). Step 2 produces one list at the 25+ floor, with the full schema, `web-verify` on every row, and `validate-companies --profile olena --write-routed`. None of this runs from step 1.

## Sources

- [RevenueCat, State of Subscription Apps 2025](https://www.revenuecat.com/state-of-subscription-apps-2025)
- [HCM on the Deloitte / EuropeActive European Health & Fitness Market Report 2026](https://www.healthclubmanagement.co.uk/health-club-management-news/EHFF-underway-with-results-of-European-Health-and-Fitness-Market-Report-2026-being-presented/362794)
- [PR Newswire, Kilo Health turns Kilo (12 November 2025 release)](https://www.prnewswire.com/news-releases/kilo-health-turns-kilo-backing-the-next-generation-of-global-startups-302611938.html)
- [Kilo portfolio](https://kilo.co/portfolio/)
- [Welltech, about us](https://welltech.com/about-us/)
- [Tracxn, Welltech](https://tracxn.com/d/companies/welltech/__82HtCEoyc_qWvIOuutyArQ2qHiuUe8Y6zwbQkgQhQ3Y)
- [Wikipedia, BetterMe](https://en.wikipedia.org/wiki/BetterMe)
- [LinkedIn, BetterMe](https://cy.linkedin.com/company/betterme-company)
- [Tracxn, Gymondo](https://tracxn.com/d/companies/gymondo/__jESGihy3WMAqMLaEbD8HYEf8W2j7yLEGEhcO5qxwQWE)
- [Tracxn, Freeletics](https://tracxn.com/d/companies/freeletics/__pKobGicdeA1yr3K6c-R6ujJ2aNB8IZhFSIGr5ZQKRy8)
- [Tracxn, Yazio](https://tracxn.com/d/companies/yazio/__-VVSNx5bsv7s50vG9YnE1PoePeF8t3pgPMiAEBzSPSA)
- [PitchBook, Fitify](https://pitchbook.com/profiles/company/504001-45)
- [PitchBook, Fastic](https://pitchbook.com/profiles/company/442287-28)
- [PitchBook, Lifesum](https://pitchbook.com/profiles/company/62386-12)
- [Lifesum jobs, Stockholm](https://jobs.lifesum.com/locations/stockholm)
- [Lifesum, AI and GLP-1](https://lifesum.com/page/ai-glp-1-the-future-of-personalised-weight-loss)
- [Tracxn, Foodvisor](https://tracxn.com/d/companies/foodvisor/__TrHrEdghLfy6XL02BOeaWJOvg4dicn3SzSp4JlLU59E)
- [Tracxn, Fitatu](https://tracxn.com/d/companies/fitatu/__QUd0sB_T5f7F9-CBWJG2c7Xa8L1hqWJ7HLaUHrQ4msw)
- [TechCrunch, Simple $35M Series B](https://techcrunch.com/2025/10/01/kevin-harts-vc-firm-leads-35m-series-b-for-weight-loss-app-simple/)
- [Vestbee, Simple Life $35M](https://www.vestbee.com/insights/articles/simple-life-secures-35-m)
- [FoodNavigator, Germany first EU market for the Wegovy pill](https://www.foodnavigator.com/Article/2026/08/06/germany-first-to-launch-wegovy-pill/)
- [Hims & Hers, plans to acquire ZAVA](https://investors.hims.com/news/news-details/2025/Hims--Hers-Announces-Plans-to-Acquire-ZAVA-Accelerating-Major-European-Growth-Across-the-UK-Germany-France-and-Ireland/default.aspx)
- [WeightWatchers, GLP-1 programme](https://www.weightwatchers.com/uk/how-it-works/glp-1-programme)
- [Fitt Insider, Freeletics Coach+](https://insider.fitt.co/press-release/freeletics-unveils-a-new-era-in-digital-fitness-with-the-launch-of-coach/)
- [ISPO, AI coach fitness apps](https://www.ispo.com/news-article/sportstech/fitness-apps-take-off-ai-coach-with-human-communication)
- [Tech.eu, from static workouts to AI companions](https://tech.eu/2025/08/07/from-workout-apps-to-ai-companions-a-paradigm-shift-in-fitness-tech/)
- [Zing Coach help centre, Body Scan](https://zingcoach.zendesk.com/hc/en-us/articles/15325477532316-Body-Scan)
- [Healthcare IT Today, Zing Coach Series A](https://www.healthcareittoday.com/2024/07/08/ai-fitness-app-zing-coach-raises-10-million-in-series-a-funding-to-combat-inactivity-and-build-healthy-habits/)
- [European Commission, MDCG 2019-11](https://health.ec.europa.eu/system/files/2020-09/md_mdcg_2019_11_guidance_en_0.pdf)
- [Emergo by UL, MDCG 2019-11 Rev. 1](https://www.emergobyul.com/news/european-revision-primary-software-guidance-mdcg-2019-11-revision-1-small-changes-meaningful)
- [BfArM, DiGA facts](https://www.bfarm.de/EN/Medical-devices/Tasks/DiGA-and-DiPA/Digital-Health-Applications/Interesting-facts/_node.html)
- [reuschlaw, Digital Act (DigiG) and DiGA risk class IIb](https://www.reuschlaw.de/en/news/digital-act-new-regulations-on-digital-health-applications/)
- [Wellhub and Erakulis partnership](https://wellhub.com/en-us/blog/press-releases/wellhub-and-erakulis/)
