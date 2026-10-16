---
product: fitxpress
profile: nick
market: USA
created: 2026-10-16
status: approved
approved: 2026-10-16
use_case: fx-telehealth-weight-loss
cap_per_group: 100
referral_call: yes
banned_terms: [Withings, Body Pro, Fitbit, Apple, Libre, Dexcom, Abbott, InBody, Prism, Size Stream, Bodygram, Wegovy, Zepbound, Ozempic, Mounjaro, Lilly, Novo, CVS, Caremark, Cigna, Evernorth, EncircleRx, Express Scripts, Welldoc, RxSaveCard, Alight, Aptia, Aon, Firefly, Premise Health, Costco, Grand Rounds, Doctor On Demand, Naturally Slim, sole prescriber, FDA, DEXA, DXA, visceral, obese, diabetics, generic figure, never a promise, writer note, context only, Premise, merger, merged, acquisition, acquired]
---

# Outbound Hypothesis — 2026-10-16 — US employer and health-plan obesity care (fixed account list)

- **Campaign:** `2026-10-16-us-employer-obesity-care`
- **Owner:** Nick Omelchak (`nick`, USA)
- **Company list: fixed, not researched.** Vadim brought his Sales Navigator list "Employer & Health Plan Obesity Care" (US): `sales-nav-raw/export-1.csv`, 376 people, all located in the US, 36 distinct `Company_name` values (summarised with a stdlib `csv` script, never read whole). There is **no company-researcher step**: step 2 builds `companies.csv` from the verdict table below. The export was pulled at director level and above by company, so every function is in it.
- **ICP:** `icp-detail.md` §1 (Telehealth & GLP-1 / Weight Loss Programs), which names "employer-sponsored metabolic health programs" and "insurance-supported obesity treatment". Two reporting lines, so averages stay readable: **line A, obesity and cardiometabolic programs** (Omada Health, Vida Health, eMed, Wondr Health, Digbi Health, Goodpath, MDLIVE) and **line B, virtual and advanced primary care platforms** (Included Health and Crossover Health, released from the merger exclusion by Vadim on 2026-10-16), which borrow the biometric-screening angle of `use-cases/fx-wellness-rewards.md`.
- **Use case file:** `brand-assets/product-info/use-cases/fx-telehealth-weight-loss.md`.
- **Registry:** the coordinator checked `exclusions/*.json` on 2026-10-16: none of these companies was ever contacted by any profile. `nick`'s other campaigns: `2026-08-07-us-digital-fitness`, `2026-09-29-us-obesity-medicine`, `2026-09-29-us-cardiometabolic`, `2026-10-01-us-options-medical-weight-loss`, `2026-10-02-us-virta-health`.

> **Read this first.**
> 1. **Nine accounts go.** Line A: Omada Health, Vida Health, eMed, MDLIVE, Wondr Health, Goodpath, Digbi Health (206 people, 211 with 5 conditional rows). Line B: Included Health (96) and Crossover Health (40, 42 with 2 conditional rows). **349 people in all: 342 IN and 7 conditional.** Included Health (agreement to acquire Firefly Health, 2026-07-28) and Crossover (merger with Premise Health completed 2026-03-12) fall under the `icp-detail.md` universal exclusion, "Companies that recently announced acquisition / merger (ICP shifting, sales cycle stalls)". Vadim released both on 2026-10-16 (checkpoint answers below); copy never mentions the merger, the acquisition, Premise or Firefly. 24 rows are OUT (identity collisions, people who left, different companies) and 3 are duplicate profiles.
> 2. **One pattern runs through line A.** Employers buy obesity and GLP-1 care through these programs, which run regular check-ins and report to the employer. The weight at a check-in comes from a scale that only some members receive (Omada, Vida, Wondr as a paid option), from phone health apps and trackers (Digbi's smart-scale sync, Wondr's app), or from a weight the member logs at a weekly check-in (eMed). MDLIVE does not publish how weight is captured. **The angle:** a guided two-photo capture inside the program's own app that every enrolled member can complete at the same check-in. It returns waist and 80+ body measurements, body composition estimates, BMI and BMR calculated and a 3D model, next to the weight the program already records. The care team decides what is used. Eligibility, coverage and continuation rules are context for Vadim and never reach copy (`audience.md` §1). Smart Scales (beta) stays out of cold copy (Vadim, 2026-10-16).
> 3. **No account was found running a phone-camera body scan** (sites, App Store listings, help centers, press; 2026-10-16). Omada and Vida already ship scales that can report body composition: partial overlap, never displacement, and copy never pitches body composition as new to them.
> 4. **Line B is primary care.** Included Health has no public obesity program: it runs virtual-first primary care and chronic-condition care (Included Care Clinic) along with its new health plans. Crossover runs advanced primary care onsite, near-site and virtual for employers, with workplace biometric screenings. Both have several angles under Message angle.
> 5. **Volume and expectations.** `nick`'s last closed campaign accepted 39 of 245 invites (15.9%) and drew 6 replies (15.4% of accepted). Of his four September and October campaigns, three have one reply each and `2026-10-01-us-options-medical-weight-loss` (14 rows) has none on file: 3 replies on 251 import rows, with acceptance not yet pulled (each campaign's `responses-classified.csv`, counted 2026-10-16). At 15.9%, 349 invites yield about 55 connections. This is a learning campaign across nine accounts. It is not a statistical test.

---

## Vertical

US employer- and health-plan-sold obesity and cardiometabolic care: virtual programs that employers and health plans buy to manage weight, GLP-1 access and related conditions for their employees and members, along with the virtual-first primary care platforms those same buyers use.

## Sub-segment

The nine accounts on Vadim's list:

- **Line A, obesity and cardiometabolic programs (7, all IN):** Omada Health (public, between-visit virtual care for prediabetes, diabetes, hypertension, weight and GLP-1 support); Vida Health (virtual cardiometabolic and obesity care with medication management); eMed (employer-sponsored GLP-1 population health); Wondr Health (behavioral weight program with Wondr Advanced clinician visits and configurable GLP-1 access); Digbi Health (precision-biology obesity and GI program with GLP-1 management); Goodpath (integrative virtual care that added weight management and GLP-1 access in 2025); MDLIVE (virtual care with weight-management care plans).
- **Line B, virtual and advanced primary care (2, both IN; released from the merger exclusion by Vadim on 2026-10-16):** Included Health (navigation, virtual-first primary care, new health plans; agreement to acquire Firefly Health); Crossover Health (onsite, near-site and virtual advanced primary care; merged with Premise Health).

**Size:** no headcount floor (Vadim, 2026-09-29). The §1 revenue threshold ($2M+) is cleared on public signals: Omada reported 42% revenue growth and more than one million members in Q1 2026 ([Q1 2026 results](https://www.barchart.com/story/news/1784598/omada-health-reports-first-quarter-2026-results)); eMed announced a $200M raise in March 2026 ([pulse2](https://pulse2.com/emed-200-million-at-2-billion-valuation-raised-for-digital-healthcare-platform/amp/)); Included Health (1,741 staff on LinkedIn) and MDLIVE (part of Evernorth, 499 staff) are enterprise; Vida (668 staff) raised $28.5M with its CEO appointment ([Vida](https://www.vida.com/news/vida-health-announces-28-5-million-in-funding-appoints-joe-murad-ceo/)); Wondr sells to large employers and the University of Texas System ([sell sheet, Sept 2025](https://go.wondrhealth.com/hubfs/Wondr%20Health_All%20Solutions%20Sell%20Sheet_092025.pdf)); Goodpath (84 staff) and Digbi (82 staff) hold employer and public-sector contracts. Revenue of the private companies is not disclosed; these are inferences.

## Company types in scope: verdict table

Step 2 builds `companies.csv` from this table, one row per canonical company. The `group` is what `cap_per_group` counts. **Matching is on the company LinkedIn URL and website, never on the name alone.** "Domain for Apollo" is the primary domain `companies.csv` / `companies-verified.csv` carries in the website column (`scripts/apollo-pull.py search` searches each IN company's domain by the `titles` block). Apollo top-up is allowed for this campaign (Vadim, 2026-10-16: «добери через аполо контакти якщо треба»); the coordinator runs search (free) and enrichment.

| # | Canonical company = group | Export `Company_name` values (rows) | Company LinkedIn / site on the rows | Domain for Apollo | Verdict | Send | Apollo top-up |
|---|---|---|---|---|---|---|---|
| 1 | **Included Health** | `Included Health` (98), alias `Doctor On Demand` (1: Allison Treftz; the page lists includedhealth.com, Doctor On Demand is a legacy brand of Included Health) | linkedin.com/company/includedhealth · includedhealth.com · 1,741 staff · San Francisco | includedhealth.com | **IN** (line B; released 2026-10-16) | 96 (3 OUT: identity collisions) | **No:** the export already holds the CEO, CMO, product, virtual care, care delivery, operations and engineering owners. |
| 2 | **Omada Health** | `Omada Health` (68) | linkedin.com/company/omada-health · omadahealth.com · 992 staff · San Francisco | omadahealth.com | **IN** (line A) | 67 (1 duplicate held) | **Yes, narrow:** Chief Medical Officer and medical directors. Product (CPGO, VP Product Management Medical, product directors), clinical product and engineering are covered. |
| 3 | **Vida Health** | `Vida Health` (38), aliases `Vida Health, Inc.` (2, same page) | linkedin.com/company/vida-health · vida.com · 668 staff · San Francisco | vida.com | **IN** (line A) | 37 + 1 conditional (2 OUT) | **Yes:** medical leadership (CMO, medical directors, the medical PC lead) and product (one product director in the export). |
| 4 | **eMed** | `eMed` (31), aliases `eMed Digital Healthcare` (2), `eMed Health` (2), all on the same page | linkedin.com/company/emeddigitalhealthcare · emed.com · 295 staff · Miami | emed.com | **IN** (line A) | 34 (1 OUT) | **Yes:** clinical (CMO, medical director, obesity-medicine clinical lead) and product (CPO or VP Product). The export has the CEO, CTO (no engineering top-up), VP Operations, a consumer product director, IT and security, and 24 commercial people. |
| 5 | **MDLIVE** | `MD Live by Evernorth` (14), `MDLIVE, by Evernorth` (10), `MDLIVE, an Evernorth company` (5), `MDLIVE, Inc.` (4), all on the same page; `MDLive` (1, no page: Stephanie Anderson); `MDLIVE` (1, no page: Allan Voss) | linkedin.com/company/mdlive-inc- · mdlive.com · 499 staff · Miramar, FL | mdlive.com | **IN** (line A) | 32 + 1 conditional (1 OUT, 1 duplicate held) | **No:** two heads of new product development, product strategy and management, VPs of clinical operations, medical directors and engineering are in the export. |
| 6 | **Wondr Health** | `Wondr Health` (18); `Naturally Slim` (4: Wondr's name until 2021; 2 rows on the Wondr page, 2 with no page); `Forbes Business Council` (1: Scott Paddock, CEO of Wondr Health) | linkedin.com/company/wondrhealth · wondrhealth.com · 122 staff · Dallas | wondrhealth.com | **IN** (line A) | 20 + 3 conditional | **Yes:** Chief Medical Officer and clinical leads (none in the export beyond the SVP Clinical Solutions) and product managers. |
| 7 | **Goodpath** | `Goodpath` (9) | linkedin.com/company/goodpath · goodpath.com · 84 staff · Cambridge, MA | goodpath.com | **IN** (line A) | 9 | **Yes:** medical leadership (CMO or medical director, obesity medicine) and product. The export is the CEO, CTO (no engineering top-up), five sales and business-operations people, pharmacy and MSK. |
| 8 | **Digbi Health** | `Digbi Health` (7) | linkedin.com/company/digbihealth · digbihealth.ai on the row (canonical site digbihealth.com) · 82 staff · Mountain View | digbihealth.com | **IN** (line A) | 7 | **Yes:** a CTO (the export has no technical owner), product, medical director. The export is the CEO, Chief of Care, a wellness director and four sales people. |
| 9 | **Crossover Health** | `Crossover Health` (43; 1 row with no page: Robyn Guillen) | linkedin.com/company/crossover-health · crossoverhealth.com · 960 staff · San Clemente | crossoverhealth.com | **IN** (line B; released 2026-10-16) | 40 + 2 conditional (1 duplicate held) | **No:** product (Head of Product, Director of Product Management), clinical (Chief Nursing Officer, national, division and site medical directors), operations (COO, medical group and practice operations, implementation) and engineering (VP Technology, engineering, data science) are covered. The export has no Chief Medical Officer; the clinical lane is covered without one. |
| 10 | none | `eMed Labs, LLC` (2: David Foxon, Abhinav Raj) | no page | none | **OUT: identity collision** | 0 | n/a |
| 11 | none | `Emed Associates` (1: Harpreet Singh, MD) | no page | none | **OUT: different company** | 0 | n/a |
| 12 | none | `Vida Health Clinic` (1: Anastacio Da Re), `Vida Health Strategies` (1: Candice hidegkuti) | no page | none | **OUT: different companies** | 0 | n/a |
| 13 | none | `MacroHealth` (1: David Angelone; "Partner at VIDA Health Group", a different VIDA) | linkedin.com/company/macrohealth | none | **OUT: different company** | 0 | n/a |
| 14 | none | `Insight Global` (Velma F.), `none` (Rhonda Routh, retired), `Sandrow Medical` (Cherisa Sandrow), `University of Colorado` (Steven Motarjeme): former MDLIVE | various | none | **OUT: left MDLIVE** | 0 | n/a |
| 15 | none | `RetireeFirst` (Diane Everett), `Aditum Bio` (Yousef Badran), `Broad Institute of MIT and Harvard` (Roukoz Abou Karam): former Goodpath | various | none | **OUT: left Goodpath** (Abou Karam lists Goodpath as an older role; the validator may release him only if the Goodpath role shows as current) | 0 | n/a |
| 16 | none | `Relativity` (Nicole Sar, former Omada), `Avalara` (Justin Strait, former Included Health) | various | none | **OUT: left** | 0 | n/a |
| 17 | none | `Horizon Media` (Marlowe Sidney; an older "CEO at eMed" line that does not match eMed's leadership) | linkedin.com/company/horizon-media | none | **OUT: not at the company** | 0 | n/a |
| 18 | none | `Blue Moon Farm` (Dr. Jennifer Frangos; lists "Medical PC President at Vida Health" below her current role) | no page | none | **OUT unless current:** the validator releases her to Vida, `clinical`, P2, only if the Vida position shows as current | 0 | n/a |

**Totals:** 342 IN, 7 conditional (in groups 3, 5, 6, 9), 3 duplicate profiles held (Omada, MDLIVE, Crossover), 24 OUT (17 rows in groups 10-18 and 7 identity collisions inside groups 1, 3, 4, 5). 342 + 7 + 3 + 24 = 376. 138 of the 349 sendable people (40%) are at the two merger-touched accounts (Included Health 96, Crossover 42).

**People re-grouped from another `Company_name`.** Step 2 writes them with the canonical company's name, LinkedIn URL and domain, so `outbound-registry.py record` registers Included Health and Wondr Health, never Doctor On Demand, Forbes Business Council or Naturally Slim:
- **Scott Paddock** → Wondr Health, P1 `product`. Row company "Forbes Business Council" (a membership); headline "CEO, Wondr Health", current role "Chief Executive Officer at Wondr Health"; Wondr names him CEO since 2022 ([Wondr people page](https://www.wondrhealth.com/company/our-people)).
- **Allison Treftz** → Included Health, P4 `referral`. Row company "Doctor On Demand", whose page points to includedhealth.com; her experience also lists "Director, Client Success at Included Health".
- **Naturally Slim rows:** Cindy Woods (Director of Cash, Wondr page) → Wondr, `referral`, job-change check. Candice Burgess (EVP, Wondr page, thin profile whose history is graduate internships), Marcia Upson (President, no page; listed as President of Naturally Slim in 2017 University of Texas at Dallas materials, while Wondr's CEO since 2022 is Scott Paddock) and Elyzabeth Gonzalez (VP, no page, one-line profile) → Wondr, **conditional**: sent only if the validator confirms a current Wondr role.

**OUT inside in-scope groups (identity collisions):** celianny C. (Included Health "CEO", headline "Anything"), Clayton Martin (Included Health "President", one-line profile), Seth Taylor (Included Health "CEO", one-line profile; Owen Tripp is the CEO and is in the export); Stephanie Tilenius (Vida "CEO", one-line profile; she stepped down as CEO in November 2023 when Joe Murad was appointed, [Vida](https://www.vida.com/news/vida-health-announces-28-5-million-in-funding-appoints-joe-murad-ceo/)); Jose Moreno ("Owner at Vida Health", one line); Allan Voss ("CEO at MDLIVE", one line, no company page); Will Wes ("Owner at eMed", no page). David Foxon and Abhinav Raj (row 10) carry word-for-word identical profiles naming no eMed role; eMed Labs, LLC is eMed's real entity (it publishes the eMed Population Health app), so the OUT is about identity, not the company.

**Duplicates (one person, one invite):** Kathryn Wintermantel (Omada): send `kathryn-wintermantel-8b6a4732`, hold the one-line `kathryn-wintermantel-2b7a183b9`. Patrick Lawrence (MDLIVE): send `patrick-lawrence-47840756` (Senior Director of IT), hold `patrick-lawrence-4550659` unless the validator finds two different people. Elizabeth Chavez (Crossover): send `elizabethgraychavez`, hold `elizabeth-chavez-4a7787249`.

### What each account already has, and what FitXpress offers (verified 2026-10-16)

| Account | What it already collects or runs (verified) | Not verified: never claim either way | What FitXpress offers (the only claim copy makes) |
|---|---|---|---|
| **Omada Health** | A wireless scale in the Welcome Kit for clinically eligible members; members with a BMI in the healthy range may not get the scale and can enter weights manually ([help center, updated 2026-10-15](https://support.omadahealth.com/hc/en-us/articles/115015679407-What-will-I-receive-in-the-program)). Some employers require GLP-1 patients to enroll in Omada and meet engagement requirements on a rolling 31-day window, counting app activities and weigh-ins on the Omada scale; Omada checks monthly and notifies the pharmacy benefit when requirements are met ([help center, created 2025-10-30, updated 2026-10-12](https://support.omadahealth.com/hc/en-us/articles/46059174300947-Learn-more-about-your-requirements-for-GLP-1-Coverage-with-CVS-Caremark)). The GLP-1 Care Track is built to protect muscle mass; in its 12-week study both groups used an at-home scale that tracks weight and body composition ([Omada, 2026-04-17](https://www.omadahealth.com/resource-center/omada-health-helps-members-on-glp-1s-lose-more-fat-preserve-muscle-mass-and-improve-mental-health-new-study-finds)). Program administrator in a drug maker's direct employer program since May 2026 ([Omada](https://www.omadahealth.com/resource-center/omada-health-joins-lilly-employer-connect-expanding-its-access-pathways-for-glp-1-care-as-patients-seek-more-lifestyle-support)). App: lessons, meals with photos, steps, progress chart, CGM and BP-monitor connections. | Whether every GLP-1 Care Track member gets a body-composition scale. Whether Omada records waist or any circumference (help-center searches for "waist" and "measurement" return none). | **Waist, hip and 80+ body measurements and a 3D model inside the Omada app, next to the weigh-ins**, for the care team to compare between scans it picks. Body composition estimates are a second method, **never pitched as new to Omada**. No weight estimate or mismatch flag (Smart Scales stays out of cold copy at every account; Vadim, 2026-10-16). |
| **Vida Health** | A cellular body-composition scale and a cellular blood-pressure monitor for eligible members since November 2023, with drop-shipment through the device partner ([Vida, 2023-11-07](https://www.vida.com/?p=2362)); device eligibility depends on Vida's clinical criteria and the employer's or plan's offering, with at most two devices per member ([help center](https://support.vida.com/hc/en-us/articles/45913368661907-Understanding-Your-Eligibility-for-Vida-Health-Devices), read through search, the page refuses scripted access). The app integrates with 100+ devices and apps and has GLP-1 support (App Store id917397071, v5.18.4, 2026-10-14). MASH care added February 2026 ([HLTH](https://hlth.com/insights/news/vida-health-expands-cardiometabolic-portfolio-to-include-mash-care-2026-02-11)); a self-pay GLP-1 pathway for employers January 2026. | What members outside device eligibility record; whether Vida records waist. | **An in-app capture any member can take, whatever their device eligibility:** waist and 80+ body measurements, body composition estimates, BMI and BMR calculated and a 3D model. Never say members lack data; body composition is never new to Vida. |
| **eMed** | The eMed Population Health app (publisher eMed Labs, LLC): eligibility through an at-home test kit with clinically reviewed results; weekly check-ins where the member logs weight (listing re-read 2026-10-16: "Log your weight"); progress visuals; clinician reminders; 24/7 support (App Store id6741202488, v24.4.2, 2026-10-12). Sold to employers, with an employer pathway through a pharmacy benefit (February 2026, [Axios](https://www.axios.com/2026/02/17/employers-new-option-workers-glp-1-demand)) and a benefits-platform partnership (August 2026, [release](https://www.alight.com/about/newsroom/alight-and-emed-join-forces-to-expand-access-to-glp-1-therapies-for-employers)). | What the kit tests; whether any scale is shipped; whether waist is recorded; whether the weekly weight is typed or photographed (a June 2025 App Store review mentions a picture step). | **A guided two-photo capture at the weekly check-in:** waist and 80+ body measurements, body composition estimates, BMI and BMR calculated and a 3D model, recorded next to the weight the member logs. No weight estimate or mismatch flag in cold copy (Vadim, 2026-10-16). Never at the test kit or the qualification step. Never say or imply logged weights are wrong. |
| **Wondr Health** | Wondr+ (digital skills program, coaching, community) and Wondr Advanced (clinician visits, medical weight-loss content); configurable options: GLP-1 access (self-pay, cost-share or covered), in-network nutrition, **connected scales as an option** ([sell sheet, Sept 2025](https://go.wondrhealth.com/hubfs/Wondr%20Health_All%20Solutions%20Sell%20Sheet_092025.pdf)). The app tracks weight and steps through HealthKit and fitness trackers (App Store id1521728956). GLP-1 utilization controls in Wondr Advanced: a prior-authorization program, step therapy and a deprescribing protocol ([launch release, April 2025](https://wondrhealth.com/news/wondr-health-launches-industry-first-advanced-weight-and-obesity-management-solution-with-flexible-cost-sharing-options-to-control-glp-1-and-total-benefits-spend/), read through search). | How many employers buy the scale option; whether waist is recorded. | **An always-on capture inside the Wondr app that does not depend on the scale option:** waist and 80+ body measurements, body composition estimates, BMI and BMR calculated and a 3D model. |
| **Digbi Health** | An at-home kit with a genetic test, a gut-microbiome test and a CGM ([employer flyer](https://www.csulb.edu/sites/default/files/2025/documents/document_fnd_digbi_flyer_journey.pdf)); the app tracks blood pressure and weight, connecting to smart scales through phone health apps, for people with a BMI of 25+ (App Store id1436497868; re-read 2026-10-16: smart scales connect through a phone health app and a wearable account). At one public employer from 2026 it is the only prescriber of non-diabetic GLP-1s, with BMI paths for eligibility and continued coverage that requires 5% weight loss, new users having 90 days ([county employee Q&A, Oct 2025](https://www.tehama.gov/wp-content/uploads/2025/10/Digbi-Employee-QA.pdf), read through search). Employer-subsidized and cash-pay GLP-1 pathways since March 2026 ([release](https://frontiervc.com/news/2026/3/25/digbi-health-capitalizes-on-glp-1-market-shift-expands-glp-compass-and-introduces-employer-subsidized-and-cash-pay-pathways-via-digbi-rxfund)). | Whether members can also type a weight; which weight source the program uses at its check-ins; whether waist is recorded. | **A body record at the start of the program and at regular check-ins, inside the Digbi app:** waist and 80+ body measurements, body composition estimates, BMI and BMR calculated and a 3D model, next to the weight its synced scales send. Decisions stay with Digbi's clinicians. |
| **Goodpath** | Integrative virtual care for back and neck pain, insomnia and IBS (App Store id1559304441); weight management with GLP-1 access since February 2025, direct-to-employer pricing and self-pay pathways ([Goodpath](https://www.goodpath.com/learn/goodpath-employer-glp1-weight-management-cost-control)); its GLP-1 FAQ asks whether coaching or weight tracking is required for a prescription, answer not published ([FAQ](https://goodpath.com/enroll/glp1-faq)). | How weight is captured; any device. | **An in-app body record for the weight program** at the points Goodpath's clinicians set: waist and 80+ body measurements, body composition estimates, BMI and BMR calculated and a 3D model. |
| **MDLIVE** | Virtual urgent, primary and behavioral care and dermatology (App Store id839671393). Weight-management care plans with regular check-ins, digital tools and coaching; results reported for patients "who reported weight loss at six months" ([one-pager dated 2026-06-16](https://www.evernorth.com/media/25266)), a results phrase footnoted to a partner's internal data that does not say how weight is captured (re-read 2026-10-16). MDLIVE physicians prescribe inside the parent company's weight program, whose supports include connected scales ([Evernorth, 2021](https://www.evernorth.com/articles/evernorth-expand-weight-management-program-include-wegovy)). Asynchronous care announced in 2023 for rollout from 2024, with a stated plan to extend it to chronic disease and wellness visits ([TechTarget](https://www.techtarget.com/virtualhealthcare/news/366596906/Evernorth-Adds-Asynchronous-Telehealth-Options-to-MDLIVE)); a "Primary+" asynchronous primary care service has its own medical director (export). | Which weight-care patients receive a connected scale; whether waist is recorded. | **A two-photo capture inside MDLIVE's virtual primary care and weight-care plans that also fits asynchronous visits:** waist and 80+ body measurements, BMI and BMR calculated, body composition estimates and a 3D model for the clinician. Copy is about MDLIVE only. |
| **Included Health** | Navigation and advocacy; Included Care Clinic, virtual-first care with preventive check-ups, screenings, refills and labs and longitudinal support for diabetes and hypertension ([Care Clinic](https://includedhealth.com/organizations/solutions/care-clinic/)); its heart-health page lists BMI among the numbers members should know ([page](https://includedhealth.com/members/know-your-numbers-heart-health/)). Acquired Firefly Health (agreement 2026-07-28) and launched Included Health Plans on 2026-10-01 for the 2028 plan year, with 2,000+ in-person partner sites ([announcement](https://includedhealth.com/announcements/included-health-launches-included-health-plans/)). **No obesity or GLP-1 program found** (site, sitemap, App Store, newsroom, search; 2026-10-16). | Whether Included Health records weight, BMI or waist in virtual visits. | **Body measurements from two photos in the member app, before a virtual check-up or between chronic-condition visits:** BMI calculated, waist and 80+ body measurements, body composition estimates. Blood pressure and labs stay with its existing workflow. |
| **Crossover Health** | Advanced primary care onsite, near-site and virtual for employers; biometric screenings at the workplace (height and weight, blood pressure, a blood draw or finger stick), in an article by Sarah Pickell, Director, Medical Group Operations, who is in this export ([Crossover](https://crossoverhealth.com/blog/biometric-screenings/)); GLP-1s inside its primary care model ([Crossover](https://crossoverhealth.com/blog/chronic-condition-management-and-glp-1-medications-weight-management/)); occupational medicine. Merger with Premise Health completed 2026-03-12 ([release](https://digital-release.wboy.com/business/press-releases/cision/20260312CL08991/premise-health-and-crossover-health-complete-merger-embark-on-transformation)). | How screening data reaches its care teams. | **A phone capture for employees who are remote or between clinic visits, alongside its workplace screenings:** waist and 80+ body measurements, BMI calculated, body composition estimates. Never blood pressure or labs, never a replacement for onsite screening. |

The displacement search (each account's site, App Store listing, help center where public, press, along with a search for the main phone-scanning competitor's partners) found no phone-camera body scan at any of the nine on 2026-10-16. The validator repeats it before import.

## Use case

An employer-sponsored obesity or cardiometabolic program adds a guided two-photo scan to its own member app. Members take it when they start the program and at its regular check-ins. Each scan returns 80+ body measurements, with waist among them. It also returns body composition estimates, BMI and BMR calculated, and a 3D model. It sits next to the weight the program already records, from a scale, a synced app or a member's log. The care team chooses which scans to compare and decides what to do with them. Virtual-first and advanced primary care work the same way (Included Health, Crossover Health). Members take the scan before a virtual visit or between clinic and chronic-condition visits. The clinician sees the member's body measurements when the visit starts.

## Why this is plausible (evidence)

1. **Employer GLP-1 coverage now runs through programs with checkpoints.** A Business Group on Health survey of 105 self-funded employers (May 2026) found about 67% cover GLP-1s for weight management, and lists among their cost strategies "validating clinical eligibility with objective biometric data" and "requiring participation in a weight management program" ([MedCity News](https://medcitynews.com/2026/05/glp1s-employers-coverage/)). The accounts on this list run those checkpoints: Omada's monthly engagement and weigh-in check for employer GLP-1 coverage (help center above); Digbi's BMI paths and 5% continuation rule at a public employer (county Q&A above); Wondr Advanced's prior-authorization program (launch release above). This is market context. Copy stays on the check-ins and never touches the eligibility or coverage side (`audience.md` §1).
2. **Body data at check-ins reaches only part of the membership through a device.** Omada's scale goes to clinically eligible members and the others may enter weights manually; Vida's devices are gated by clinical criteria and the employer's offering, two at most; Wondr's connected scales are a configurable option and its app reads weight from phone health apps and trackers; Digbi reads weight from smart scales synced through phone health apps; eMed's weekly check-in asks the member to log weight (App Store listings re-read 2026-10-16). MDLIVE does not publish how weight is captured: its one-pager's "who reported weight loss" names a results subgroup (sources in the table). A phone capture reaches every enrolled member at the same check-in, whatever device they have.
3. **Clinical guidance asks for a body-size measure beyond weight and BMI.** The Lancet Diabetes & Endocrinology Commission on clinical obesity (January 2025) confirms excess adiposity by direct body-fat measurement or by at least one anthropometric criterion (waist circumference, waist-to-hip or waist-to-height ratio) in addition to BMI ([Lancet Diabetes & Endocrinology](https://www.thelancet.com/journals/landia/article/PIIS2213-8587(24)00316-4/fulltext); criteria summarised in [PLOS Medicine](https://journals.plos.org/plosmedicine/article?id=10.1371%2Fjournal.pmed.1004749)). Two accounts already invest in body composition beyond weight (Omada's muscle-preservation study, Vida's body-composition scale), which shows the value is recognised; circumferences are the route a phone capture serves, and FitXpress estimates are never presented as the direct body-fat route.
4. **FitXpress offers this with stated limits.** From `proof-points.md`: two photos (front and side), "under 45 seconds from the photos to structured results", 80+ body measurements, body composition outputs (BMI, BMR, fat %, lean mass, fat mass), typical scan-to-scan differences under 1 cm for most evaluated measurements, white-label API and SDK; Smart Scales (beta) cross-checks a self-reported weight against the scan's estimate (`how-it-works.md`, `tech-spec.md`); this campaign keeps it out of cold copy (Vadim, 2026-10-16). Limits: body composition values are estimates; there is no head-to-head study against members' scales; no visceral fat output; the validation population stops at 210 kg; there is no employer-program reference customer. Proof available: an anonymised weight-management platform that ran 34,000 scans in 2025, and 112,100 scans in 2025 across all 3DLOOK customers.

## What earlier campaigns teach this one

- **Acceptance is where the loss sits.** `2026-08-07-us-digital-fitness`: 39/245 accepted (15.9%), then 6/39 replied. Three of the four later US campaigns (`2026-09-29-us-obesity-medicine`, `2026-09-29-us-cardiometabolic`, `2026-10-02-us-virta-health`) have one reply each; `2026-10-01-us-options-medical-weight-loss` (14 rows) has no responses file and no reply on file. None of the four has acceptance pulled yet. All share Nick's account and its invite pacing.
- **The one substantive reply named the measurement workflow.** On 2026-09-29 a clinic replied that patients need a separate medical-assistant appointment for measurements and scale readings, and asked what the FitXpress process involves. The checkpoint angle here stays on that ground: who takes the measurement, where, and how often.
- **Two "I no longer work there" replies** (2026-08-07, 2026-09-29). A job-change check runs on every contact; thin profiles are named in Validation criteria.
- **Referral asks drew an emoji and a "not sure who".** Since 2026-10-07 every lane gets context and a question in Message 1 and the call in Message 2 (`referral_call: yes`), with no bare "who owns X?".

## Target buyer persona

**Who buys:** in line A, the owners of the program's member app, its clinical protocol and its member operations, who decide what a member is asked to capture at the start and at each check-in and what the program reports to employers and plans. In line B, the owners of virtual and advanced primary care delivery, its screenings and its product. Tiers only order the list; everyone goes in one import file (standing decision). Every function at an IN company gets one lane (standing decision 3, 2026-09-29, with Vadim's «максимально використай весь список»; confirmed 2026-10-16). Counts below cover all nine accounts, IN and conditional (349). Line A people are named by tier below; line B tiers and lanes are in the account pools after the named cases.

**P1, owners (36: line A 23 below, Included Health 7 and Crossover 6 in the line B pools):**
- Omada Health (6): Sean Duffy, Co-Founder and CEO; Wei-Li Shao, President; Danika Harrison, Chief Product and Growth Officer; Ellery Cook, VP Product Management, Medical; Britt Buntman, VP, GLP-1 and Cardiometabolic Health (all `product`); Jennifer Becker, Chief Care Delivery Operations Officer (`operations`).
- Vida Health (4): Joe Murad (row "Joe M."), President and CEO; Ashish Nag, Director of Product Management (both `product`); Shane Giuliani, COO; Amy Mushlin, SVP Clinical Operations and Strategy (both `operations`).
- eMed (3): Linda Yaccarino, CEO; Alex C., Director, Consumer Product (both `product`); Duane Kingston, VP Operations (`operations`; his bio says he oversees customer experience and clinical operations).
- MDLIVE (4): Rachel Rhodes, Head of New Product Development, AI Strategy and Provider Experiences; Ali Krafft, Head of New Product Development and AI Strategy, Virtual and Emerging Care (both `product`); Jennifer Lord, VP Clinical and Operations; Mac Davis, VP Clinical Operations (both `operations`).
- Wondr Health (3): Scott Paddock, CEO (export row Forbes Business Council); Jeff Serrano, Chief Product and Experience Officer (both `product`); Lisa Talamini, SVP Clinical Solutions (`clinical`).
- Goodpath (1): Bill Gianoukos, CEO and Co-Founder (`product`).
- Digbi Health (2): Ranjan Sinha, Founder and CEO (`product`); Dr. Garima Sharma, Chief of Care (`clinical`).

**P2, program leads (94: line A 43, Included Health 31, Crossover 20).** Line A: product directors and managers (Omada's senior directors of product management and Director of Product, Michael Becker excepted, see below; MDLIVE's Director Product Strategy Asim Ilyas, whose headline is interoperability and eligibility, and Director of Product Management; Wondr's Director of Product - Platform), clinical product and clinical strategy (Omada's directors of clinical product, clinical strategy, clinical services, clinical affairs), medical and clinical directors (MDLIVE's medical directors, including Christina Chen, Medical Director of Asynchronous Care for Primary+; Vida's Senior Director, Clinical Dietetics and Director Clinical Solutions; Digbi's Health and Wellness Director), and operations owners (member and clinical operations, care navigation, implementation and onboarding, member experience and engagement, client reporting and data analytics, pharmacy operations at eMed and Goodpath).

**P3, engineering, data, security and compliance (41: line A 26, Included Health 10, Crossover 5).** Line A: every CTO in the export (Omada, Vida, eMed, Wondr, Goodpath; Digbi has none), engineering, platform, AI, ML and data-engineering leads, IT, and the security, privacy and compliance owners (Omada's VP Compliance and Privacy and Compliance Director; MDLIVE's CISO; eMed's Director of Information Security; Wondr's SVP IT and Security). All `technical-integration`; security, privacy and compliance people get the privacy-architecture emphasis of that lane.

**P4, referral (178):** sales, account management, client success, partnerships and alliances, consultant relations, proposals, business development, growth and commercial operations, finance (CFOs, FP&A, revenue cycle, SOX), supply chain, strategy and corporate development, legal, facilities and capital projects, project management, creative and production, customer service and experience, MSK program leads, advisors (Gary Earl, Board of Advisors, Vida), and unclear roles ("VP", "Director", "Senior Vice President"). By account: Included Health 48, Omada 35, Vida 25, eMed 24, MDLIVE 13, Wondr 12, Crossover 11, Goodpath 6, Digbi 4. Each sub-role has its own question target under Message angle.

**Lane totals (349):** `referral` 178, `operations` 57, `clinical` 44, `technical-integration` 41, `product` 29. Line A (211): `referral` 119, `operations` 29, `technical-integration` 26, `product` 23, `clinical` 14. Included Health (96): `referral` 48, `clinical` 18, `operations` 17, `technical-integration` 10, `product` 3. Crossover (42): `clinical` 12, `operations` 11, `referral` 11, `technical-integration` 5, `product` 3.

**Named cases for the validator:**
- **Michael Becker** (Omada, "National Vice President, GLP-1 Strategy"): `referral`, with the employer line; his history is employer sales (former SVP Employer Growth at Wondr Health).
- **Conditional (sent only if the validator confirms a current role at the account):** Kristin Grunzweig (Vida, no page), Stephanie Anderson (MDLIVE, no page; "Operations Executive", former VP at the parent's pharmacy business), Marcia Upson, Elyzabeth Gonzalez, Candice Burgess (Naturally Slim rows, see the verdict table). Crossover: Robyn Guillen (no page), Joe Ennesser (one-line "Chief Operations Officer" while Crossover's site lists Sarah Lord as COO).
- **Thin profiles with a company page (job-change check by name):** Muhammad H. (Omada, "VP"), Perry Ankney (MDLIVE, "Director"), Madison Green (Digbi), Cindy Woods (Wondr, Naturally Slim row); Crossover: Burkie Smith, Rebecca Carbajal.
- **A client in the title:** Steven Watts (Crossover) is medical director for one named client account. Copy never names that client.
- **Former employer is another account here (never name it in copy):** Michael Becker (Omada; ex-Wondr), Meredith Sparrow (Vida; ex-Wondr), Kerryanne Shuler (Vida; ex-Included Health), Brent Hartman (Vida; ex-Grand Rounds, now Included Health), Shannon Abel (MDLIVE; ex-Grand Rounds), Heather W. (Included Health; ex-Crossover).

**Crossover Health pool (42, line B; P2 lane split recounted from the export 2026-10-16):** P1 Scott Shreeve, CEO and Founder; Anna Nachamie, Senior Director, Head of Product (both `product`); Sarah Lord, COO; Sarah Pickell, Director, Medical Group Operations (author of its biometric-screening article) (both `operations`); Sumeet Batra, National Medical Director of Occupational Medicine and Employee Health; Sally Larwood, Chief Nursing Officer (both `clinical`). P2 20: 10 medical directors, physician leads and the primary care program director (`clinical`); 9 practice, clinic, process and implementation directors, with the conditional Robyn Guillen and Joe Ennesser (`operations`); the Director of Product Management (`product`). P3 5 (technology, engineering, data science, IT, security). P4 11 (account management, finance, legal, facilities, capital projects, client success, project management, two thin "Director" profiles). Lanes: `clinical` 12, `operations` 11, `referral` 11, `technical-integration` 5, `product` 3. No Apollo top-up.

**Included Health pool (96, line B; tier and lane split recounted from the export 2026-10-16):** P1 7: Owen Tripp, CEO; Mary Reynolds, Senior Director of Product Management (both `product`); Alexandra Yurkovic, CMO and SVP Clinical Services and Delivery; Vibin Roy, VP of Virtual Care (both `clinical`); Heather Johnson, VP Practice Operations; Meher Iqbal, Senior Director and GM, Care Delivery; Katie Robinson, Senior Director, Virtual Care Strategy and Operations (all three `operations`). P2 31: Director, Product (`product`); 16 associate, senior, medical and clinical directors in primary, specialty, complex and urgent care, clinical affairs, triage, case management and utilization management (`clinical`); 14 operations owners in member care, advocacy, care navigation, population health, HEOR, analytics and implementation and onboarding (`operations`). P3 10: engineering leads, technology services, digital workplace, the Chief Compliance Officer, the CISO and the Director of Healthcare Compliance. P4 48. Lanes: `referral` 48, `clinical` 18, `operations` 17, `technical-integration` 10, `product` 3. No Apollo top-up.

**Where engineers stand.** Every engineer, data and AI lead at an IN company is `technical-integration`, P3, after owners and program leads: `nick`'s 2026-08-07 campaign got 0 replies from 60 cold technical invites. IT, infrastructure and security roles get a lane under standing decision 3 (2026-09-29), which overrides the `icp-detail.md` IT roles section, where IT support and InfoSec are FAIL; confirmed by Vadim on 2026-10-16. Their message carries the privacy architecture and leaves out SDK detail.

**Not the buyer (FAIL for the cold send):** only the 24 OUT rows and the held duplicates. Every function at an IN company has a lane.

**KPIs they care about:** what the program records about a member's body at the start and at each check-in, and what it shows an employer or plan beyond a weight; how many enrolled members actually complete a check-in; device logistics and cost; for Omada and Vida, what their scales cover and for whom; for eMed, Digbi and Wondr, how members complete regular check-ins in their GLP-1 programs; for MDLIVE and Included Health, what a virtual visit can take in about the body; for Crossover, how screenings reach employees who are remote or between clinic visits.

**Likely objections and the honest answer:**
- "We already send a scale" (Omada, Vida, Wondr's option). True. The scan adds circumferences and a 3D model at the same check-in, and reaches members who have no scale; it does not replace the scale. There is no study comparing the scan with members' scales; a pilot can compare them in the same members.
- "Members log their own weight" (eMed; Digbi syncs smart scales). The scan adds waist, other measurements, body composition estimates and a 3D model at the same check-in, next to the logged or synced weight. If the prospect asks whether the scan can check an entered weight: Smart Scales, a beta feature, shows the scan's own weight estimate beside the entered weight for the care team to review. No accuracy figure. It decides nothing about eligibility or coverage; those decisions stay with the program's clinicians and the employer's rules (`compliance.md` §7). Smart Scales stays out of cold copy (Vadim, 2026-10-16).
- "We are not an obesity program" (Included Health). The scan gives a virtual visit body measurements: BMI calculated, waist and other measurements. Blood pressure and labs are outside it.
- "We already screen employees onsite" (Crossover). True. The scan reaches employees who are remote or between clinic visits. It never replaces onsite screening, and blood pressure and labs stay with the clinic.
- "How accurate is it?" "96-97% accuracy against expert manual measurement" (body measurements, never body composition), or the full `accuracy-formulations.md` §1.1 sentence; repeatability as the §1.2 sentence; validation population 38-210 kg.
- "HIPAA? SOC 2? FDA?" The US compliance line; SOC 2 verbatim: "3DLOOK is working toward obtaining a SOC 2 Attestation Report and has completed an initial readiness assessment aligned with SOC 2 Trust Services Criteria." FDA, verbatim from the trust FAQ: "FitXpress is not cleared, authorized, or approved by the U.S. Food and Drug Administration (FDA). 3DLOOK makes no representation as to whether FDA clearance, authorization, or approval is required for any particular customer's use case."
- "Vendor review" (Omada as a public company, MDLIVE inside its parent, Included Health). Security overview on request; architecture, pen-test summary, incident-response and BC/DR summaries under NDA; DPA and BAA in contracting; requests to legal@3dlook.me.
- "Our roadmap is full." API and SDK into the existing app; 2-4 weeks for a typical basic integration (`technical-integration` Message 2 only).

### Target buyer persona: Sales Navigator pull for step 3

**Pull by title filter inside the approved company list, never by company alone.** The export Vadim pulled is the list for this campaign. This block feeds the Apollo top-up (`scripts/apollo-pull.py search`, which searches each IN company's domain by these titles) and any Sales Navigator top-up. It names only the roles the verdict table's top-up column asks for: medical and clinical leadership, product, and a CTO for Digbi, the one account with no technical owner in the export. Engineering titles are left out: `nick`'s 60 cold technical invites drew 0 replies, and every other account already has its CTO or engineering leads. The coordinator enriches only candidates at the accounts marked "Apollo top-up: yes" and drops any CTO match outside Digbi. Included Health and Crossover get no top-up.

```titles
Chief Medical Officer
Medical Director
Associate Medical Director
Clinical Lead
Head of Clinical Operations
Director of Clinical Operations
Chief Product Officer
Vice President of Product
Head of Product
Director of Product
Senior Product Manager
Product Manager
Chief Technology Officer
```

**`cap_per_group: 100`** (confirmed by Vadim on 2026-10-16). Largest groups: Included Health 96, Omada 67, Crossover 42. Nothing is capped out at 100.

## Message angle: lanes, account facts and the content asset

Every person gets exactly one lane, spelled exactly as below. Numbers in copy come only from `proof-points.md` (see Rules). The account facts below may be used as the "only this company" line, **without their numbers**. **Writer notes are instructions to the writer and are never copied into a message.**

**Angle by line (writer notes):**
- **Line A (Omada, Vida, eMed, Wondr, Digbi, Goodpath, MDLIVE).** The regular check-ins the program already runs, and what a member could add at them from a phone inside the program's app: waist and 80+ body measurements, body composition estimates, BMI and BMR calculated, a 3D model. The result sits next to the weight the program already records. The program and its clinicians decide what is used and how. Copy never ties the scan to eligibility, enrollment approval, coverage, continuation, prior authorization, refills or reviews of GLP-1 use.
- **Line B, Included Health.** Several angles, one per person, picked by function: measurements taken before a virtual primary-care visit; change in body size between diabetes and hypertension visits; a health assessment at the start of a new health plan; preventive-care numbers in employer reporting; a guided capture step inside the member app; the commercial targets under `referral`. Never weight-loss or GLP-1 framing: no such program was found.
- **Line B, Crossover Health.** Advanced primary care for employers, onsite, near-site and virtual, with workplace biometric screenings. The angle is a phone capture for employees who are remote or between clinic visits, alongside the screenings: waist and other measurements, BMI calculated, body composition estimates. Angles by function: what employees away from a clinic complete between visits; how practice and medical group operations run screenings across client sites; how occupational medicine and employee health record body measurements at intake; how primary care follows chronic conditions between visits. The scan never replaces onsite screening and never covers blood pressure or labs. Never pitch it as a weight-loss program.

**What each account already has. Never contradict it, never pitch it as new:**
- **Omada** sends a wireless scale in its welcome kit, counts weigh-ins in its program and studied body composition on GLP-1s with at-home scales. Never write or imply "weight only", "just a scale", or that body composition is new to Omada. Lead with waist, hip and other measurements and a 3D model next to the weigh-ins.
- **Vida** ships a body-composition scale and a blood-pressure monitor to members who qualify for devices, and integrates 100+ devices and apps. Never say members lack data or devices. The point is a capture any member can take.
- **eMed** runs an at-home test kit with clinically reviewed results and weekly check-ins where members log weight. The scan belongs at the weekly check-in, never at the test kit or the qualification step. Never say or imply that logged weights are wrong or that members misreport.
- **Wondr** offers connected scales as an option and reads weight from phone health apps and trackers. Never imply Wondr lacks body data. The point is a capture that does not depend on the option.
- **Digbi** ships a genetic test, a gut-microbiome test and a CGM, and tracks weight and blood pressure, with smart scales connected through phone health apps. It runs GLP-1 programs for employers. Never mention eligibility, continuation or any criteria, and never name an employer.
- **Goodpath** treats weight alongside MSK, sleep and GI; how it records weight is not known. Say nothing about its current data.
- **MDLIVE** runs weight-care plans with check-ins and coaching, and asynchronous visits. Say nothing about which patients have a scale or how weight is recorded.
- **Included Health** runs virtual-first primary care with check-ups, screenings and chronic-condition support. Say nothing about whether it records BMI or waist today.
- **Crossover** runs advanced primary care onsite, near-site and virtual for employers, with workplace biometric screenings that include height and weight, blood pressure and a blood draw or finger stick, and occupational medicine. Never imply it lacks body data or that its screenings miss anything. The point is employees who are remote or between clinic visits.

**Lanes:**
- **`product`** (CEOs, presidents, founders, CPOs, product heads, directors and managers, the GLP-1 business owner at Omada). What the member app can ask for at the program's check-ins: a guided two-photo scan returning the outputs above, white-label through the API or web and mobile SDKs, with no device for the program to manage. Question targets: the point in a member's year where body measurements would matter most in the employer report; how the check-in flow in the app is built today; (Included Health) where body measurements sit in a virtual visit today; (Crossover) what employees away from a clinic complete between visits.
- **`clinical`** (CMO, medical, clinical and nursing directors, clinical product and clinical strategy, dietetics). Waist and other circumferences as a body-size measure next to the program's weights and labs. Body composition values are estimates for the care team. Progress comparisons use two scans the care team picks. The scan never diagnoses and never decides anything about a member. Question targets: what the care team looks at beyond the weight at a check-in; how change in body size is recorded between visits.
- **`operations`** (COOs, operations, clinical and member operations, care navigation, implementation and onboarding, member experience and engagement, analytics, client reporting, pharmacy operations; at Included Health also population health, HEOR, triage and case management; at Crossover practice, clinic and medical group operations). A capture every enrolled member can finish from a phone at the same check-in, with no device logistics for this step (put it in your own words); one SDK across employer clients; a timestamped result for the check-in record or the employer report. Question targets: how a check-in is completed and recorded today and who completes it; how many members finish one; what device logistics take; what the employer report shows about members. Pharmacy roles: how the pharmacy team and the care team share a member's progress. Never refills or dosing.
- **`technical-integration`** (CTOs, engineering, platform, AI, ML, data, IT, security, privacy, compliance). White-label REST API with API-key authentication and web and mobile SDKs; technical tone. Security, privacy and compliance people hear the privacy architecture and the vendor-review path (BAA, scan records on random IDs, documents through legal@3dlook.me), without SDK detail. Message 2 only: the 2-4 weeks figure (engineering people only), the US compliance line from Rules and the privacy FAQ link, which carries retention detail (measurements and other outputs stay stored until deleted by scan ID on the customer's request).
- **`referral`** (178 people). Never a bare "who owns X?". Message 1: one line on what the scan returns and why it matters to this program's clients (from the account fact), then one question about the person's own work, taken from their sub-role's target below. Message 2: a value line that continues the person's own question, a call offer with the calendar link, and an easy out that points to whoever owns the member app or the clinical program, worded fresh for each person. Each target names a point where a body scan enters the program.
  - **Sales (enterprise, mid-market, channel, union and public-sector) and business development:** what employer, plan or union buyers ask about the member app or member check-ins in late-stage evaluations.
  - **Account management and client success:** what employer and plan clients ask to see about member progress in quarterly reviews or at renewal.
  - **Partnerships, alliances, partner enablement and health-plan or payer partnerships:** how a capability inside the member app gets chosen for partner or plan clients; what partners ask about member results.
  - **Consultant relations and solutions consulting:** what benefits consultants ask about member participation, outcome measures and devices when they evaluate programs.
  - **Proposals and RFPs:** which RFP questions cover member data capture, devices or measures beyond weight.
  - **Growth, commercial, revenue and sales operations, GTM enablement, sales performance and forecasting:** how many enrolled members reach their first check-in; what sellers can show of the member app.
  - **Finance (CFO, FP&A, strategic finance, finance systems, cash) and supply chain:** what member devices cost to ship and replace across clients; how a usage-priced app capability is weighed against fixed device spend.
  - **Revenue cycle, SOX and internal controls:** which member records billing to employer clients rests on; how a new member-data vendor passes internal review.
  - **Strategy, corporate development and strategic planning:** which member capabilities the company builds and which it adds through partners; where body measurements sit in the plan for employer and plan products.
  - **Legal (deputy general counsel):** how the company reviews a member-data vendor's terms, such as a BAA, before a pilot.
  - **Facilities and capital projects (Crossover):** how onsite and near-site clinics are set up for screenings; how employees far from a clinic are served.
  - **Project management:** how a new capability is rolled out across client sites.
  - **Creative and production (creative directors, executive producer):** how member-facing content walks a member through a check-in or a capture step; how the app shows members their own progress visually. The 3D model is the link. Never before-and-after, never appearance.
  - **Customer service and customer experience:** what members contact support about around check-ins and device setup; what helps a member finish a check-in.
  - **MSK program leads (Omada, Goodpath):** how the MSK and weight programs share one member record.
  - **Advisors (Gary Earl, Vida):** how the company evaluates a new member capability.
  - **Unclear roles** ("VP", "Director", "Senior Vice President", "Executive Vice President" or "President" on a thin profile): the default target is the account management one (what employer clients ask to see about member progress). If the profile shows a function, the validator records it and the person takes that function's target.

**Account facts the copy may use (no numbers, no device, drug, pharmacy-benefit or partner brands, no funding):**
- **Omada Health:** between-visit virtual care for prediabetes, diabetes, hypertension, weight and joint and muscle health; a GLP-1 Care Track built to protect muscle mass, with a study on body composition this spring; a wireless scale in the welcome kit.
- **Vida Health:** virtual cardiometabolic and obesity care for employers and health plans; coaches, dietitians, therapists and medical providers; connected devices for members who qualify and 100+ device and app integrations; GLP-1 support in the app; MASH care added this year.
- **eMed:** employer-sponsored GLP-1 weight management; an at-home test kit with clinically reviewed results; weekly check-ins in its app; new employer pathways this year through benefits partners (unnamed).
- **Wondr Health:** a skills-based weight program employers have offered for years; Wondr Advanced with clinician visits; configurable GLP-1 access and cost-sharing; connected scales as an option.
- **Digbi Health:** precision-biology care for weight, GI and metabolic conditions built on genetic and gut-microbiome tests and a CGM; GLP-1 programs with employer-subsidized and cash-pay pathways.
- **Goodpath:** integrative, whole-person virtual care for MSK, sleep and GI that added weight management with GLP-1 access; direct-to-employer and self-pay pathways.
- **MDLIVE:** virtual urgent, primary and behavioral care; weight-management care plans with regular check-ins and coaching; asynchronous visits, including Primary+.
- **Included Health:** navigation, advocacy and virtual-first primary care (Included Care Clinic) with check-ups, screenings and support for diabetes and hypertension; new Included Health Plans for self-insured employers.
- **Crossover Health:** advanced primary care for employers, onsite, near-site and virtual; biometric screenings at the workplace; chronic-condition care inside primary care; occupational medicine and employee health.
- **People's former employers may be named** (standing decision), except another account in this campaign (named cases above), a competitor or a banned term.

**Content asset in Message 2 (at most one article link, along with Nick's calendar link):**
- Line A accounts, lanes `product`, `clinical`, `operations`: https://3dlook.ai/content-hub/glp-1-market/ (HTTP 200 on 2026-10-16; covers employer-supported programs; privacy paragraph matches the trust FAQ; says "It is not a medical device"). Linked as a general resource, no section pointer; never quote or paraphrase its "scale weight" passages to Omada, Vida or Wondr.
- Included Health, lanes `product` and `operations`: https://3dlook.ai/content-hub/ai-body-data-wellness-platforms/ (HTTP 200; clean privacy and speed wording; covers employee wellness programs). `clinical` at Included Health: no article.
- Crossover: Sarah Pickell and `operations` and `product`: the wellness-platforms article above; Sumeet Batra and occupational-medicine roles: https://3dlook.ai/content-hub/manual-vs-digital-intake-occupational-health-screening/ (HTTP 200; "FitXpress is not a medical device."; BAA wording matches the FAQ).
- `technical-integration`, every account: https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/
- `referral`: no article.
- **Live but not linked in this campaign:** `/for-bmi-verification/` ("30 seconds", written for pharmacies), `/content-hub/wellness-rewards-verification-employers-insurers-using-ai-3d-body-scanning/` ("under a minute", "under 40 seconds"), the homepage ("HIPAA Compliant", "never link photos to personal identifiers"). Live pages may stay as they are (standing decision); cold copy uses only the wording in Rules. Not live (404 on 2026-10-16): `/fitxpress/for-glp-1-programs/`, `/fitxpress/for-wellness-programs/`, the GLP-1 progress-record and telehealth-documentation articles.

**Question topics by account (writer notes; each line is a target).** Each person gets one question nobody else at the company gets, built from their title and about their own work. One topic serves at most about a fifth of a company's people: Omada about 13, Vida 7, eMed 7, MDLIVE 6, Wondr 4, Goodpath 2, Digbi 1, Included Health 19, Crossover 8. Wording, hook, structure and closer never repeat. The lane is in brackets. At Included Health the UM director and the claims director (Sharon Johnson, Heather Conroy) take a documentation or referral topic. Never a review, a claim or a coverage topic.
- **Omada (67; 18 topics):**
  1. [product] what a GLP-1 Care Track member's check-in shows beyond the weigh-in
  2. [product] where waist and hip measurements would sit next to the progress chart
  3. [product, referral] how growth and product operations measure a member's first weeks in the app
  4. [clinical] how muscle-preservation coaching shows members their own progress
  5. [clinical] which body-size measure clinical product and clinical strategy use beside weight and labs
  6. [clinical] how clinical affairs and clinical writing explain a new member measure
  7. [operations] how care-team operations keep members active between visits
  8. [operations] what client reporting and analytics show employers about member progress
  9. [operations, referral] what shipping and replacing member devices takes across clients (member operations, supply chain)
  10. [technical-integration] how member-experience engineering adds a capture step to the app
  11. [technical-integration] how data, AI and applied-statistics teams take in a new member data type
  12. [technical-integration, referral] how privacy, compliance, SOX and IT review a new member-data vendor
  13. [referral] what employers, consultants and jumbo or strategic accounts ask about in finalist meetings or at renewal
  14. [referral] how alliances and partner enablement pick capabilities for partner clients
  15. [referral] what members ask customer service and customer experience about around weigh-ins and devices
  16. [referral] how corporate strategy and strategic finance weigh a usage-priced capability across clients
  17. [referral] how creative shows member progress in member-facing content
  18. [referral] how GLP-1 sales and employer sales describe the member experience to employers
- **Vida (38; 13 topics):**
  1. [product] what members outside device eligibility capture at a check-in
  2. [product] how the app's device and app integrations come together in one member view
  3. [clinical] how dietitians and medical providers look at change in obesity and MASH care
  4. [clinical] which body-size measure clinical dietetics uses beside weight
  5. [operations] how clinical operations, therapy and care navigation run check-ins across employer and plan clients
  6. [operations] the step members find hardest at a check-in (member experience)
  7. [technical-integration] how front-end, AI and data engineering add a capture flow
  8. [referral] what employers and plans ask client success to report at renewal
  9. [referral] what enterprise, mid-market and union buyers ask about the member experience
  10. [referral] how consultant relations and proposals answer RFP questions on member data and devices
  11. [referral] how strategy, partnerships, payer and finance teams weigh a capability added across clients
  12. [referral] how creative shows member progress in member content
  13. [referral] what sales enablement and revenue operations equip sellers to show of the app
- **eMed (34; 12 topics):**
  1. [product] how the weekly check-in flow is built and what it asks the member for
  2. [product] what consumer product sees members complete week to week
  3. [operations] how operations, delivery and customer experience support members through weekly check-ins
  4. [operations] what data and analytics show employer clients about member progress each quarter
  5. [operations] how the pharmacy team and the care team share a member's progress
  6. [technical-integration] how IT and information security review a capture SDK inside the app
  7. [referral] what employer, health-plan and public-sector clients ask account directors and client success to show
  8. [referral] what strategic partners and benefits partners ask about the member app and member results
  9. [referral] how business development and go-to-market operations present the weekly check-in to prospects
  10. [referral] how sales operations and channel sales track member participation for clients
  11. [referral] how finance weighs a usage-priced capability across employer clients
  12. [referral] how enterprise strategy sees the member app developing
- **MDLIVE (33; 13 topics):**
  1. [product] what an asynchronous primary-care visit can take in about the body (Primary+)
  2. [product] how new product development evaluates a capture capability for virtual and emerging care
  3. [product] how product strategy and interoperability bring member data into the visit record
  4. [clinical] how weight-care check-ins are recorded for the clinician
  5. [clinical] what a clinician knows about body size before a virtual visit
  6. [operations] how clinical operations and network operations run weight-care check-ins across clients
  7. [operations] how implementation rolls a feature out to clients; how member engagement tracks weight-care plans
  8. [technical-integration] how platform development, software engineering, IT and security add a capture step
  9. [referral] what clients ask client success to report about weight-care plans
  10. [referral] how account management shows clients that members use virtual primary care
  11. [referral] what enterprise buyers ask about virtual weight care in sales cycles
  12. [referral] how strategy, partnerships and provider development evaluate a new member capability
  13. [referral] how financial analysis looks at the cost of a per-visit capability
- **Wondr (23; 11 topics):**
  1. [product] what the Wondr app records at a check-in for members without the scale option
  2. [product] how the platform team adds a step to the skills-program journey
  3. [clinical] how Wondr Advanced clinician visits look at progress
  4. [operations] how live services and participant success support members through check-ins
  5. [operations] what data analytics shows clients about participant progress
  6. [technical-integration] how software, data engineering and IT and security take in a new capture flow
  7. [referral] what employer clients ask client success to show at renewal
  8. [referral] what health-plan partners and sales prospects ask about the member experience
  9. [referral] how finance, FP&A and cash teams weigh a capability added across clients
  10. [referral] how creative and production show member progress in the program's videos and app
  11. [referral] how sales operations and operating excellence measure member participation
- **Goodpath (9; 8 topics):**
  1. [product] how the weight program records progress next to MSK, sleep and GI care
  2. [technical-integration] how the app adds a capture step for the weight program
  3. [operations] how the pharmacy team and the care team share a GLP-1 member's progress
  4. [referral] what employers ask for in a direct-to-employer GLP-1 arrangement
  5. [referral] what self-pay members expect from the app in their first weeks
  6. [referral] what benefits consultants ask about the weight program in evaluations
  7. [referral] how business operations measure member participation across employer clients
  8. [referral] how the MSK and weight programs share one member record
- **Digbi (7; 7 topics, one per person):**
  1. [product] where body measurements would sit next to genetic, gut-microbiome and CGM data in the member view
  2. [clinical] what the care team reviews beside the CGM and test results at a check-in
  3. [clinical] how coaches walk members through progress check-ins
  4. [referral] what self-insured employers ask at renewal
  5. [referral] what mid-market and enterprise buyers ask about the member app
  6. [referral] how sales operations track member participation reported to clients
  7. [referral] how the company evaluates a new member capability (the unclear SVP role)
- **Included Health (96; 18 topics across six angles):**
  1. [product] virtual visit: what a virtual check-up records about the body before the clinician joins
  2. [clinical] virtual visit: what primary, urgent and specialty clinicians know about body size in a video visit
  3. [clinical] virtual visit: what clinical affairs and medical directors document about body size in a visit record
  4. [clinical] chronic care: how diabetes and hypertension care follows change in body size between visits
  5. [operations] chronic care: how care and case management, navigation and triage follow members between visits
  6. [product, referral] health plans: what a new health plan asks members to complete in the first year
  7. [operations] employer reporting: what population health, HEOR and analytics report to employers about preventive care
  8. [referral] employer reporting: what employer clients ask client success to show at renewal about preventive care
  9. [operations] member app: how member care and advocacy teams guide a member to a preventive step
  10. [product] member app: where a guided capture step would sit in the member app
  11. [operations] member app: how implementation and onboarding roll a new member capability out to clients
  12. [referral] commercial: what consultants, channel partners and enterprise buyers ask about virtual primary care in evaluations
  13. [referral] commercial: how proposals, solutions consulting and value-based-care commercialization answer RFP questions on preventive measures
  14. [referral] commercial: how growth operations, GTM enablement and sales performance equip sellers to show the member experience
  15. [referral] commercial: how finance, FP&A and corporate development weigh a capability added across employer clients
  16. [referral] commercial: how the Communities business explains member services to its clients
  17. [technical-integration] how care-platform engineering adds a capture step
  18. [technical-integration] how the CISO and the compliance teams review a member-data vendor
- **Crossover Health (42; 12 topics). Steven Watts serves one named client account: never name it.**
  1. [product] what employees away from a clinic complete between visits
  2. [product] where a guided capture step would sit in the member app for virtual care
  3. [clinical] what national, division and site medical directors look at about body size during a visit
  4. [clinical] how primary care follows chronic conditions between clinic visits
  5. [clinical] how occupational medicine and employee health record body measurements at intake
  6. [clinical] how nursing teams and physician leads run the measurement part of a screening
  7. [operations] how medical group and practice operations run biometric screenings across client sites
  8. [operations] how practice and clinic directors reach employees who are remote at screening time
  9. [operations] how process and implementation teams roll a new step out to client sites
  10. [technical-integration] how technology, engineering, data science, IT and security take in a capture step from a member-data vendor
  11. [referral] what employer clients ask account management and client success to show about screening participation
  12. [referral] how finance, facilities, capital projects, legal and project management plan a new capability across client sites

## Outreach language

English, every message. Short sentences, plain words, US context.

## Rules for steps 3-5

- **Sender and format:** Nick, English, "Nick" alone on the last line, first names only (never "Dr"). Connection request without a note. Message 1 ≤ 600 characters, no link. Message 2 ≤ 550, Nick's calendar link as plain text (https://meetings.hubspot.com/nick-omelchak) and at most one article link from the asset list. Everyone goes in one import file at the same time; tiers only order the list.
- **Lanes are exactly** `product`, `clinical`, `operations`, `technical-integration`, `referral`.
- **Message 1 asks, Message 2 calls, in every lane, referral included** (`referral_call: yes`). Message 1: context from the account fact and what the scan returns, then one real question about the person's own work; no call ask, no link. Message 2: a value line that continues the person's own Message 1 question, then the call offer with the calendar link; people who are not the buyer get an easy out that points to whoever owns the member app or the clinical program, named as a target and worded fresh for each person. Never the same ask twice. No call length (no minutes).
- **Message 1 gate.** Every message 1 carries at least one product specific from `proof-points.md` and one line that could only have been written to that company; each pair of messages cites at least one number. The `referral` lane is not exempt (`referral_call: yes`).
- **Compliance line.** Every non-referral Message 2 carries the US line verbatim: "We support HIPAA-governed deployments under a BAA, encrypt data in transit and at rest, and delete photos after processing or within 30 days." Referral sequences carry none. `technical-integration` carries the same line; never shorten it, never drop the 30-day option. No other compliance wording in cold copy.
- **No 3DLOOK client is named.** Fixed proof lines, used as written, each a plain sentence of its own: "one weight-management platform ran 34,000 scans in 2025" (no client, no geography); "112,100 scans in 2025 across all 3DLOOK customers" (3DLOOK-wide scale, never "ran", never "so far"); "3DLOOK has worked with 100+ clients" (all-time, both products; never "use FitXpress" or "today"). At one company each of these lines and the speed wording appears for at most about one person in five.
- **Numbers and accuracy, only from `proof-points.md` and in its wording:** two photos (front and side); "under 45 seconds from the photos to structured results" (only where speed is the point, whole, its subject the scan or its result); 80+ body measurements; body composition estimates (body fat %, lean mass, fat mass) with BMI and BMR calculated; "96-97% accuracy against expert manual measurement" (body measurements only, never in a sentence with body composition or weight); the §1.2 repeatability sentence; the fixed proof lines; `technical-integration` Message 2 only, 2-4 weeks for a typical basic integration. **No other number:** no weight accuracy figure, no prospect results, member counts, savings, criteria, prices, funding or market statistics.
- **Smart Scales (beta) stays out of cold copy** at every account: no weight estimate, no mismatch flag and no weight cross-check in Message 1 or Message 2 (Vadim, 2026-10-16). Replies only: if a prospect asks whether the scan can check an entered weight, the answer names Smart Scales as a beta feature that shows the scan's own weight estimate beside the entered weight for the care team, with no accuracy figure. Never "verified weight", "verified BMI", "proof of weight" or anything that decides eligibility, coverage or refills. Never imply that members misreport, cheat or game a program. This rule overrides the Smart Scales, fraud and "verify" wording in the use-case and positioning excerpts later in the card.
- **What the scan does, and does not do.** It returns measurements and estimates for the program's clinicians or the member. It does not diagnose, decide eligibility or coverage, approve a refill, interpret results, lower weight, preserve muscle or measure blood pressure or labs. Progress comparisons use scans the program picks (`compliance.md` §4); never claim that FitXpress tracks a person over time. Never say or imply that the scan replaces the program's scale. No visceral fat output.
- **Never state or imply what a prospect's devices or data do not measure** (see "What each account already has"). No "weight only", "just a scale", "no body data", "members without data". Never put a prospect's device next to ours as a comparison.
- **Employers and coverage.** The program, its clinicians and the employer's rules decide. Copy never ties the scan to eligibility, enrollment approval, coverage, continuation, prior authorization, refills or reviews of GLP-1 use (`audience.md` §1). Never suggest the scan helps deny or cut coverage, never mention an employer by name, never quote eligibility criteria or percentages, never mention the coverage retreat in the market.
- **Regulatory.** Cold copy never mentions the FDA (banned term) or medical-device status. If a reply asks, use only the trust FAQ sentences quoted under objections; "FitXpress is not a medical device." rests on the UK/EU MDR assessment and never answers an FDA question. Hard fails: "HIPAA compliant", "HIPAA-compliant", "HIPAA certified", "SOC 2 certified", "SOC 2 compliant", anything FDA-cleared or FDA-approved, "processed, not stored", "no personal data", "no personal identifiers".
- **No brands other than the prospect's own** (banned terms enforce it): no device, wearable, drug, pharmacy-benefit, benefits-platform, investor or partner names, no competitors, and never a prospect's employer or plan clients. Say "your scale", "the CGM", "phone health apps", "GLP-1", "a pharmacy benefit", "a benefits partner". **The ban also covers former employers** that are drug makers, pharmacy benefits, MDLIVE's parent group, investors or benefits partners of these accounts (for example a past role at a drug maker, a pharmacy benefit manager or a benefits consultancy): leave them out even as a hook. Other former employers may be named.
- **Parents and deals.** MDLIVE copy is about MDLIVE: never its parent company, never a parent-wide pitch, never an introduction request upward. Never mention funding, investors, valuations, acquisitions, mergers (Included Health's acquisition of Firefly and Crossover's merger with Premise included; never name either), sale processes, headcount or revenue.
- **Company names in copy:** Included Health, Omada, Vida, eMed, MDLIVE, Wondr, Goodpath, Digbi, Crossover. Every Message 1 names the company. Never "Naturally Slim" or "Doctor On Demand".
- **Several people at one company** (Included Health 96, Omada 67, Crossover 42, Vida 38, eMed 34, MDLIVE 33, Wondr 23). Never mention colleagues or claim to have spoken with anyone there; never "circling back", "following up", "saw your post". No two people at one company share an opener (first three words), a central question, a Message 2 value line, an easy-out sentence, a closer shape or a product sentence. Rotate the product specific: two photos (front and side); a guided capture on any phone; 80+ body measurements, waist and hip among them; body composition estimates with BMI and BMR calculated; a 3D model; white-label API and SDKs; the phone as the only hardware, in your own words; the fixed proof lines.
- **Person-first language and tone.** "People living with obesity", "members", "patients". Never "obese" or "diabetics" (banned), no before-and-after, no "burn fat", no appearance words, no weight-loss promises.
- **People the scan is not for.** Never offer it for people under 16, in pregnancy, or with physical disabilities (performance not established); validation covers 38-210 kg.
- **Word traps.** Never "objective" about our data (standardized, timestamped, structured, repeatable); never "comprehensive", "seamless", "leverage", "robust"; no em or en dash; no "plus" as a connector; no "so" introducing a benefit; no corrective "X, not Y", "rather than", "instead of"; no presumed reactions; no thanks in Message 2; never "pitch"; no sentence opening "As [a role],".
- **Card lines are targets.** Write each person's question, value line, call sentence, easy out and closer in your own words. "generic figure", "never a promise", "writer note" and "context only" are banned terms; the gate fails any message that carries one.
- **No pricing and no trial terms** anywhere. A price or trial question goes to the call.

## Anti-cases (where it does NOT work)

- **Merger and acquisition stay out of copy:** Included Health (agreement to acquire Firefly Health, 2026-07-28) and Crossover Health (merger with Premise Health completed 2026-03-12) fall under the `icp-detail.md` exclusion "Companies that recently announced acquisition / merger (ICP shifting, sales cycle stalls)". Vadim released both on 2026-10-16. Copy never mentions the merger, the acquisition, Premise or Firefly; banned terms enforce it.
- **Out, by name:** the 24 OUT rows of the verdict table (identity collisions, people who left, different companies). Match on the company LinkedIn page and the person's own row, never on the name alone.
- **Partial overlap, not displacement:** Omada (wireless scale for eligible members; at-home body-composition scales in its GLP-1 study), Vida (body-composition scale for eligible members), Wondr (connected scales as an option), Digbi (smart-scale sync), MDLIVE (connected scales in the parent's weight program), Crossover (height and weight in its workplace screenings). All stay IN; copy never pitches what they have as new and never sets their devices beside the scan.
- **Structural anti-cases:**
  - Any account found to run a phone-camera body scan, or to have signed a phone-scanning vendor: displacement, held for Vadim, standard copy never sent. None found on 2026-10-16.
  - Corporate parents (the parent of MDLIVE): different buyer and procurement; copy stays on MDLIVE.
  - Employers and benefits platforms named in sources (no employer in this export): a different segment (`icp-detail.md` §4).
  - Investors, board members of other companies, advisors at other companies: not at the company. Gary Earl (Board of Advisors at Vida) is `referral` as an advisor of an IN account.
  - Existing 3DLOOK customers: none on this list; the registry check still runs.
- **Stop conditions before send:** an IN account announces it is being acquired, a new merger beyond the two known ones, a closure or a body-scanning partner (pause, Vadim decides); a profile shows the person has left (drop).

## Validation criteria (Step 2 will check)

There is no company research. Step 2 builds `companies.csv` from the verdict table, then step 4 validates people against the persona.

- **Companies.** Nine rows, each with its LinkedIn URL and the primary domain from the verdict table: Included Health (includedhealth.com), Omada Health (omadahealth.com), Vida Health (vida.com), eMed (emed.com), MDLIVE (mdlive.com), Wondr Health (wondrhealth.com), Goodpath (goodpath.com), Digbi Health (digbihealth.com), Crossover Health (crossoverhealth.com). Re-grouped people carry the canonical name and URL. `outbound-registry.py check --profile nick` runs on the export and must come back clean; `record` must never register Doctor On Demand, Forbes Business Council, Naturally Slim or any OUT company.
- **Apollo top-up.** `apollo-pull.py search` with the `titles` block, then enrichment only for candidates at Omada, Vida, eMed, Wondr, Goodpath and Digbi (verdict table); a CTO candidate is enriched only at Digbi. New people get a lane by the persona rules and pass the same validation. Included Health and Crossover get no Apollo additions. Enrichment stops at 60 credits (Vadim, 2026-10-16).
- **Displacement re-check.** Before import, confirm no IN account shows a phone-camera body scan (site, App Store listing, help center, press).
- **Identity and job-change checks, by name:** the conditional people and thin profiles listed under "Named cases"; the duplicates; Roukoz Abou Karam and Dr. Jennifer Frangos only if their account role shows as current. A job-change check runs on every contact.
- **People.** At least 100 contacts at P1 or P2 across the nine groups (persona count 130). Every IN person has one of the five lanes. FAIL only for the OUT rows and held duplicates.
- **Message 1 gate.** Every message 1 carries at least one product specific from `proof-points.md` and one line that could only have been written to that company; each pair of messages cites at least one number. Zero client names, zero pricing, zero `banned_terms`, zero claims about what a prospect's device or data does not measure. A missing specific counts as a failure: `2026-07-21` sent 307 message 1 texts with no specific and drew 1 reply on 67 sends.
- **Proof in product-info.** Use-case file and live articles: yes. Reference customer in employer-sold obesity care: none; the anonymised weight-management proof (34,000 scans) and 3DLOOK-wide scale (112,100 scans) are accepted, not hidden.

## Success metrics for this campaign

Denominators as in `metrics-final.json` (Closely event counters). Expected volume: 349 invites (342 IN and 7 conditional), with Apollo additions on top.

**Reply history on `nick`** (counted 2026-10-16 from each campaign's `responses-classified.csv` with a stdlib `csv` script; import rows from `closelyhq-import.csv`):
- `2026-08-07-us-digital-fitness`: 245 invites sent, 39 accepted (15.9%), 6 replies (15.4% of accepted, 2.4% of invites): 1 interested, 1 question, 2 referrals, 1 maybe-later, 1 "no longer there".
- `2026-09-29-us-obesity-medicine` (112 import rows): 1 reply, a question about the measurement process.
- `2026-09-29-us-cardiometabolic` (75 rows): 1 reply, from a person who had left the company.
- `2026-10-01-us-options-medical-weight-loss` (14 rows): no responses file and no reply on file.
- `2026-10-02-us-virta-health` (50 rows): 1 reply, an emoji.
- The four later campaigns together: 3 replies on 251 import rows (1.2%), 1 of them positive. None has a `metrics-final.json`: their acceptance and replies per accepted are unknown, and import rows overstate sends.

| Metric | Target | Floor | Basis |
|---|---|---|---|
| Contacts at P1 or P2 | 130 | 100 | persona count |
| Connection acceptance rate | 20% | 12% | 2026-08-07: 15.9%; no later campaign has acceptance pulled |
| Replies per invite sent | 2% | 1% | 2026-08-07: 2.4% (6/245); the four later campaigns: 1.2% of import rows (3/251) |
| Replies per accepted person | 12% | 6% | 2026-08-07: 15.4% (6/39). If the later campaigns accepted at 15.9%, their 1.2% per row would be about 7.5% per accepted (inference; acceptance not pulled) |
| Positive replies (interested + question) | 3 | 1 | 2026-08-07: 2 on 245 invites; the four later campaigns: 1 on 251 rows. At those rates 349 invites yield about 1.4 to 2.9 |
| Accounts with at least one reply | 4 of 9 | 2 | account-based |
| Discovery calls booked | 3, at different accounts | 1 | Omada, MDLIVE, Included Health and Crossover: a call is the realistic ceiling in 8 weeks |
| Pilots / POCs agreed within 8 weeks | 1 (eMed, Wondr, Digbi, Goodpath or Vida) | 0 (learning campaign) | |

**Falsified if:** 3 or more P1/P2 replies in line A say the scale or the weight they already record covers what their check-ins need, with no interest in circumferences or in a capture for members without a device; or the P1/P2 replies at eMed, Digbi and Wondr all say the logged or synced weight is all their check-ins need. **Inconclusive, and the post-mortem says so, if fewer than 40 people accept** (349 invites at the 12% floor give about 42). Line A and line B are reported separately.

## Risks

1. **Acceptance on `nick`:** 15.9% last measured; five campaigns now share the account and its pacing.
2. **Devices in place.** Omada and Vida already ship body-composition-capable scales; if circumferences and a capture for members without a device do not land, they hear "another way to get data we already have", and there is no head-to-head study to answer it.
3. **Employer coverage is moving both ways.** Some employers are dropping weight-loss GLP-1 coverage (BGH: 10% say they likely will not continue in 2027); the Massachusetts state plan moved Vida out of GLP-1 prescribing on 2026-07-01 ([Mass.gov](https://www.mass.gov/news/june-update-on-vida-health-program-and-glp-1-coverage)). Where coverage tightens, checkpoints grow; where it ends, the checkpoint angle weakens. Copy never mentions either.
4. **Enterprise drag.** Omada (public), MDLIVE (inside its parent's procurement), Included Health (integrating an acquisition) and Crossover (after its merger) run formal vendor reviews. The SOC 2 attestation is in progress and has not been issued.
5. **Volume at one company.** 96 people at Included Health, 67 at Omada and 42 at Crossover, about half of them `referral` at the first two; sameness across messages is the main quality risk (Rules: several people at one company; topic banks under Message angle).
6. **Competitor.** The main phone-scanning competitor markets to corporate wellness and chronic-disease programs (`competitors.md`); any account may be evaluating it (displacement anti-case). Answer on method and published figures only; never name it.
7. **Smart Scales is beta.** It stays out of cold copy (Vadim, 2026-10-16). A reply that asks about entered weights gets the beta answer, with no published figure.
8. **Tone.** Weight stigma; person-first language is a hard rule.
9. **Merger-touched accounts.** 138 of 349 people (40%) sit at Included Health and Crossover. The ICP exclusion's two reasons, a shifting ICP and stalled sales cycles, are an accepted risk (Vadim, 2026-10-16); line B is reported separately.

## Open questions for Vadim

All six were answered on 2026-10-16 («все погоджую»). The answers are in "Vadim's decisions 2026-10-16 (checkpoint answers)" below.

1. **Crossover Health: held or released?** Answered: released.
2. **Included Health: held or released?** Answered: released. Exposure when asked: 138 people at merger-touched accounts, 40% of 349.
3. **Conditional people (5 in line A, 2 at Crossover):** answered: sent only if the validator confirms a current role.
4. **Smart Scales (beta) in cold copy:** answered: stays out of cold copy; replies only.
5. **Apollo enrichment budget:** answered: cap 60 credits.
6. **The coordinator's reading of the two scope quotes:** answered: confirmed.

## Vadim's decisions 2026-10-16 (scope)

What Vadim said in the campaign brief, quoted.

1. «максимально використай весь список» (use the whole list to the maximum).
2. «добери через аполо контакти якщо треба» (top up contacts through Apollo if needed).

### Coordinator's reading of the two quotes, confirmed by Vadim on 2026-10-16 («все погоджую»)

- **Lanes for every function.** Quote 1, read with standing decision 3, gives every function at an IN company one lane: product, clinical, operations, engineering, IT, security, privacy and compliance, and commercial roles as `referral`.
- **`cap_per_group: 100`, because of the list size.** Included Health has 96 sendable people, Omada 67 and Crossover 42; the default cap of 50 would cut all three.
- **Apollo scope.** Quote 2 is read as a top-up only where the export lacks medical, clinical or product owners, and a CTO at Digbi. The coordinator runs `apollo-pull.py search` (free) and enrichment, capped at 60 credits; the hypothesis agent does not run Apollo.
- **Fixed list.** The export "Employer & Health Plan Obesity Care" (US) is the company list, with no company-researcher step (standing decision 8).

## Vadim's decisions 2026-10-16 (checkpoint answers)

Vadim answered the checkpoint with «все погоджую», as relayed by the coordinator on 2026-10-16: he takes every recommendation in the checkpoint summary.

1. **Crossover Health: RELEASED** (Open question 1). IN on line B.
2. **Included Health: RELEASED** (Open question 2). IN on line B.
   For both: copy never mentions the merger, the acquisition, Premise or Firefly (banned terms enforce it).
3. **Conditional people** (Open question 3): sent only if the validator confirms a current role at the account.
4. **Smart Scales (beta)** (Open question 4): stays out of cold copy at every account; replies only, as the Rules describe.
5. **Apollo enrichment** (Open question 5): cap 60 credits.
6. **Coordinator's reading confirmed** (Open question 6): a lane for every function at an IN company, IT, security, privacy and compliance included; `cap_per_group: 100`; the export is the whole company list.

## Vadim's decisions 2026-10-16 (validate checkpoint)

«приймаю всі твої рекомендації» (validation summary and QC 18/20 presented by the coordinator):

1. **SEND approved: 367 people** (344 from the export, 23 from the Apollo top-up), as in `people-validated.csv`.
2. **Geography.** People located outside the US who work on a company's US program stay PASS: Samantha Wu (Goodpath, London), Christelle Younes (Goodpath, Montreal), Rajan Bhuyan (Digbi, Bengaluru). The two eMed people in London (Matthew Noble, CMO Global Clinical Services; Cameron Pugh, Clinical Operations Lead) work in eMed's UK business: not sent by nick (WEAK, never promoted); a later UK campaign may route them to katerina.
3. **The 5 conditional WEAK** (Stephanie Anderson, Marcia Upson, Elyzabeth Gonzalez, Candice Burgess, Joe Ennesser) stay out, under the checkpoint answer to Open question 3.
4. **Job-change check on the thin profiles: risk accepted**, no Apollo credits spent on it. Displacement was re-checked on the web by the hypothesis agent on 2026-10-16 (none found).

## Vadim's standing decisions (built in)

1. **No headcount floor** (2026-09-29).
2. **One closely.io import file, no waves** (2026-09-29). The default cap of 50 is raised to 100 for this campaign (confirmed 2026-10-16).
3. **A lane for every function at an IN company** (2026-09-29). FAIL only for the wrong company, people who left, identity collisions, duplicates and people already messaged.
4. **Referral-lane sequences carry no compliance line;** every other lane carries the US line in Message 2 (2026-09-29).
5. **Former employers may be named** (2026-09-29), within the Rules' limits.
6. **No 3DLOOK client is named;** 34,000 scans without client or geography; 112,100 as 3DLOOK-wide scale; "3DLOOK has worked with 100+ clients", all-time (2026-09-29, 2026-09-30, wording 2026-10-07).
7. **Live 3DLOOK pages may be linked as they are** (2026-09-29); cold copy keeps to the Rules' wording.
8. **A list Vadim brings has no company-researcher step** (2026-10-07).
9. **Message 1 asks, Message 2 calls, in every lane, referral included** (2026-10-07).
10. **Card lines are targets** (2026-10-07): writers never copy a card sample as text.
11. **Nick's profile audit has not been done;** the acceptance risk is accepted as is (2026-09-29).

## Sources

- Live 3DLOOK assets (HTTP 200 on 2026-10-16): https://3dlook.ai/content-hub/glp-1-market/ · https://3dlook.ai/content-hub/ai-body-data-wellness-platforms/ · https://3dlook.ai/content-hub/manual-vs-digital-intake-occupational-health-screening/ · https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/ · checked and not linked: https://3dlook.ai/for-bmi-verification/ · https://3dlook.ai/content-hub/wellness-rewards-verification-employers-insurers-using-ai-3d-body-scanning/ · https://3dlook.ai/ · 404: https://3dlook.ai/fitxpress/for-glp-1-programs/ · https://3dlook.ai/fitxpress/for-wellness-programs/
- Omada: https://support.omadahealth.com/hc/en-us/articles/115015679407-What-will-I-receive-in-the-program · https://support.omadahealth.com/hc/en-us/articles/46059174300947-Learn-more-about-your-requirements-for-GLP-1-Coverage-with-CVS-Caremark · https://support.omadahealth.com/hc/en-us/articles/46059365206931-Pharmacists-Providers-Supporting-CVS-Caremark-Patients-Omada-for-GLP-1-Coverage (help-center articles read through the Zendesk API) · https://www.omadahealth.com/resource-center/omada-health-helps-members-on-glp-1s-lose-more-fat-preserve-muscle-mass-and-improve-mental-health-new-study-finds · https://www.omadahealth.com/resource-center/the-relationship-between-glp-1s-and-body-composition-its-complicated-1 · https://www.omadahealth.com/resource-center/omada-health-joins-lilly-employer-connect-expanding-its-access-pathways-for-glp-1-care-as-patients-seek-more-lifestyle-support · https://www.barchart.com/story/news/1784598/omada-health-reports-first-quarter-2026-results · App Store id805711008
- Vida: https://www.vida.com/?p=2362 · https://support.vida.com/hc/en-us/articles/45913368661907-Understanding-Your-Eligibility-for-Vida-Health-Devices · https://www.vida.com/news/vida-health-announces-28-5-million-in-funding-appoints-joe-murad-ceo/ · https://hlth.com/insights/news/vida-health-expands-cardiometabolic-portfolio-to-include-mash-care-2026-02-11 · https://www.mass.gov/news/june-update-on-vida-health-program-and-glp-1-coverage · App Store id917397071
- eMed: App Store id6741202488 (publisher eMed Labs, LLC; re-read 2026-10-16: "Weekly check-ins - Log your weight") · https://www.axios.com/2026/02/17/employers-new-option-workers-glp-1-demand · https://www.alight.com/about/newsroom/alight-and-emed-join-forces-to-expand-access-to-glp-1-therapies-for-employers · https://pulse2.com/emed-200-million-at-2-billion-valuation-raised-for-digital-healthcare-platform/amp/ (emed.com refuses scripted access)
- Wondr: https://go.wondrhealth.com/hubfs/Wondr%20Health_All%20Solutions%20Sell%20Sheet_092025.pdf · https://wondrhealth.com/news/wondr-health-launches-industry-first-advanced-weight-and-obesity-management-solution-with-flexible-cost-sharing-options-to-control-glp-1-and-total-benefits-spend/ · https://www.wondrhealth.com/company/our-people · https://www.tamus.edu/safety/naturally-slim-is-now-wondr-health/ · App Store id1521728956
- Digbi: App Store id1436497868 (re-read 2026-10-16: "Blood pressure and weight tracking (connects to smart scales via" a phone health app and a wearable account) · https://www.tehama.gov/wp-content/uploads/2025/10/Digbi-Employee-QA.pdf · https://www.csulb.edu/sites/default/files/2025/documents/document_fnd_digbi_flyer_journey.pdf · https://frontiervc.com/news/2026/3/25/digbi-health-capitalizes-on-glp-1-market-shift-expands-glp-compass-and-introduces-employer-subsidized-and-cash-pay-pathways-via-digbi-rxfund · canonical domain from https://digbihealth.ai (rel=canonical → digbihealth.com)
- Goodpath: https://www.goodpath.com/learn/goodpath-employer-glp1-weight-management-cost-control · https://goodpath.com/enroll/glp1-faq · https://www.goodpath.com/direct-to-employer-glp1 · App Store id1559304441
- MDLIVE: https://www.evernorth.com/media/25266 (one-pager dated 2026-06-16; re-read 2026-10-16 with `pdftotext`: "27.4 lbs average weight loss for those who reported weight loss at six months", footnoted to a partner's internal data) · https://www.evernorth.com/articles/evernorth-expand-weight-management-program-include-wegovy · https://www.techtarget.com/virtualhealthcare/news/366596906/Evernorth-Adds-Asynchronous-Telehealth-Options-to-MDLIVE · App Store id839671393
- Included Health: https://includedhealth.com/organizations/solutions/care-clinic/ · https://includedhealth.com/members/know-your-numbers-heart-health/ · https://includedhealth.com/announcements/included-health-signs-agreement-to-acquire-firefly-health/ · https://includedhealth.com/announcements/included-health-launches-included-health-plans/ · sitemap https://includedhealth.com/sitemap_index.xml (no weight or GLP-1 page) · App Store id907304333
- Crossover: https://crossoverhealth.com/blog/biometric-screenings/ · https://crossoverhealth.com/blog/chronic-condition-management-and-glp-1-medications-weight-management/ · https://crossoverhealth.com/leaders/sarah-lord/ · https://digital-release.wboy.com/business/press-releases/cision/20260312CL08991/premise-health-and-crossover-health-complete-merger-embark-on-transformation · https://www.lw.com/en/news/2026/03/latham-watkins-advises-crossover-health-in-merger-with-premise-health · App Store id1611653959
- Employer and clinical context: https://medcitynews.com/2026/05/glp1s-employers-coverage/ · https://www.thelancet.com/journals/landia/article/PIIS2213-8587(24)00316-4/fulltext · https://journals.plos.org/plosmedicine/article?id=10.1371%2Fjournal.pmed.1004749 · competitor marketing to corporate wellness: https://prismlabs.tech/solutions/corporate-wellness-platforms
- Internal: `sales-nav-raw/export-1.csv` (stdlib `csv` script) · `2026-08-07-us-digital-fitness/post-mortem.md` · `responses-classified.csv` of `2026-08-07-us-digital-fitness`, `2026-09-29-us-obesity-medicine`, `2026-09-29-us-cardiometabolic`, `2026-10-02-us-virta-health` (none exists for `2026-10-01-us-options-medical-weight-loss`), counted 2026-10-16 · `closelyhq-import.csv` row counts of the four later campaigns · `2026-09-29-us-cardiometabolic/hypothesis.md` (structure) · `2026-10-11-au-sport-fitness/hypothesis.md` (message rules) · `icp-detail.md` §1, §4, exclusions, IT roles · `use-cases/fx-telehealth-weight-loss.md`, `fx-wellness-rewards.md` · `proof-points.md` · `compliance.md` · `competitors.md` · `how-it-works.md` · `tech-spec.md` · `scripts/apollo-pull.py`, `scripts/outbound_pack.py`
