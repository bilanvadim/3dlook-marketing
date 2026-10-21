---
product: fitxpress
profile: olena
market: Continental Europe (UK excluded)
created: 2026-10-19
status: approved
approved: 2026-10-19
inspiration: everlab.com.au (vadim target in 2026-08-14-au-digital-fitness, never a target here)
use_case: fx-telehealth-weight-loss
cap_per_group: 50
referral_call: yes
banned_terms: [Everlab, Neko, Lifesum, Lykon, Clinique La Prairie, Prism, InBody, Tanita, Withings, Seca, Technogym, Evolt, Styku, Fit3D, Oura, Whoop, Apple, Garmin, Dexcom, Libre, Abbott, Eurofins, Randox, Synlab, Unilabs, Cerba, HIPAA, SOC 2, FDA, MDR, CE mark, DiGA, compliant, certified, certification, accredited, clinically validated, clinically proven, reimbursed, reimbursement, verify, verified, verification, eligibility, eligible, Smart Scales, mismatch, fraud, self-reported, guesswork, unreliable, inaccurate, error-prone, tape measure, DEXA, DXA, MRI, BIA, bioimpedance, visceral, waist-to-height, Lancet, obesity, obese, overweight, weight loss, weight-loss, GLP-1, Ozempic, Wegovy, Mounjaro, semaglutide, tirzepatide, biological age, anti-aging, anti-ageing, reverse aging, live longer, early detection, diagnose, diagnosis, risk score, before and after, before-and-after, guarantee, guaranteed, ROI, funding, investors, investor, valuation, Series A, Series B, Series C, acquisition, acquired, merger, generic figure, never a promise, not a promise, context only, writer note, Circling back, Following up, Saw your post]
---

# Outbound Hypothesis: 2026-10-19, Continental European preventive-health and longevity memberships (Everlab look-alike, Olena)

- **Campaign:** `2026-10-19-eu-everlab-similar`. Sender: Olena Kudryavtseva, profile `olena`, market Continental Europe, UK excluded; geo = `PROFILE_GEO["olena"]` in `scripts/outbound-pipeline.py` (EU, EEA, Switzerland, Iceland, Liechtenstein, Ukraine). `Olena` alone on the last line of every message; calendar link https://meetings.hubspot.com/olena-kudriavtseva.
- **Seed account: Everlab** (everlab.com.au, Melbourne). Preventive health and longevity membership: 100+ biomarker blood panels, full-body MRI, bone density and DEXA, CGM, VO2 max, genetics, clinician messaging, a year-round programme in an app, 30+ wearable integrations, consumer plans and corporate executive health (notes: `2026-08-14-au-digital-fitness/companies.md`, "### 03. Everlab"). **Everlab is not a 3DLOOK client.** It is a `vadim` target in that AU campaign. It is the pattern this campaign clones, never a target here, and never named in copy (`banned_terms`).
- **Registry, checked 2026-10-19** (`outbound-registry.py status` and every `exclusions/*.json`): no Continental European preventive-health or longevity company is covered by any profile. Overlap is limited to Clinique La Prairie (`olena`, 2026-10-07, declined 2026-10-13), Lifesum (`olena`, 2026-09-14, owner of Lykon since June 2024), Thriva (`katerina`, UK), Superpower (`nick`, US) and Everlab and Vively (`vadim`, AU). Olena's other campaigns (2026-07-21 telehealth and weight loss, 2026-07-22 never sent, 2026-09-14 consumer apps, 2026-10-07 weight-loss networks) hold no company of this thesis apart from Clinique La Prairie.

## Vadim's decisions 2026-10-19

Vadim's brief, verbatim: «https://www.everlab.com.au/ на основі цієї компанії створи аутбаунд гіпотезу 10+ співробітників європа Лени акаунт. знайти 25-30 компаній».

1. **Seed: Everlab,** the pattern only, never a target here.
2. **Profile `olena`,** market Continental Europe (UK excluded).
3. **10+ employees.**
4. **25-30 companies** at step 2.
5. **Standing decisions carried over:** English only for `olena` (2026-09-14); `cap_per_group: 50`, one import file (2026-09-29); no 3DLOOK client named, anonymised proofs only (2026-09-29, 09-30, 10-07); Message 1 asks, Message 2 offers the call, referral included (`referral_call: yes`, 2026-10-07); a lane for every function, FAIL only for the wrong company, people who left, identity collisions and duplicates (2026-09-29); former employers may be named; live 3DLOOK pages may be linked as they are (2026-09-29).

## Vadim's decisions 2026-10-19 (2): company list review

Research found 18 companies. Vadim, verbatim: «бери 7. контакти я шукаю в сейлз навыгаторы потым ти доповнюэш з аполо якщо треба. всых а европу».

1. **The 18 companies stand; this is his review of the list and of the hypothesis.**
2. **Seven pool companies released into the list, this campaign only:** Prescan, Werlabs, Preventicum, Hello Inside, Dr.Dropin, Macromo, Biolytica. Each was out only by a default or an anti-case (re-test without an app, one-off checks, CGM-nutrition overlap, telehealth, consumer biomarker app, B2B platform); that exclusion is waived for these seven names and nowhere else. They take fit 3 unless the evidence shows more. 18 + 7 = 25.
3. **"всых в европу": every company stays on `olena`.** Axo Longevity stays Spain (Open question 4 closed); Preventicum's London site and any UK staff at listed companies do not route the account to `katerina`.
4. **People: Vadim exports Sales Navigator himself; Apollo tops up afterwards where Sales Nav is thin.**

## Coordinator's decisions 2026-10-19 (not Vadim's words)

1. **Status `approved` on 2026-10-19, which lets step 2 run.** Vadim asked for the hypothesis and the company list in one request. His review of the company list is the hypothesis review: cutting a segment or a company there is how this hypothesis gets reviewed.
2. **Gate: ≥20 verified companies → step 3.** Fewer than 20 stops at step 2 and goes back to Vadim with `companies.csv`. No padding with anti-cases.

## Coordinator's decisions 2026-10-21: people (not Vadim's words)

Vadim, verbatim: «https://docs.google.com/spreadsheets/d/1XIk3n6s8b7h5s2JzcjU6f9toUbMOSNh0CXV5D47oi9g … список для крайньої кампанії по європі для лени з сейдз навігатора. запусти наступні стадії та добери в аполо контакти по компаніях яких нема і які є в гіпотезі».

1. **Sales Nav sheet → `sales-nav-raw/export-1.csv`** (45 rows, 40 kept). Aliases added in `companies.csv` / `companies-verified.csv`: `Zoī (Zoi)` (the macron made the slug `zo`), `Longevity Center Poland (Longevity Center Europe)`, `Preventicum (preventicum international group)`, `Dr.Dropin (Dr.Dropin Psykologi)`, `Macromo (science studio)` (Michal Pohludka, Macromo co-founder via the parent studio). Dropped as not this company: SoFa (ex-Zoī), WORKOFO (Werlabs board seat), Edda.ai (Dr.Dropin board seat), Deloitte (aeon advisory board), Pactos (non-acting YEARS founder).
2. **Apollo top-up only for the 8 companies with nobody in the sheet:** Lucis, Loovi, AYUN, CARE Preventive, Longevia Medical Clinic, Mavie Work, Circle Health, Biolytica; 42 people, 42 credits (`apollo-log.md`). The other 17 companies' Apollo candidates were left unenriched (`skipped-covered-by-sales-nav`).
3. **Circle Health registry hit is a name collision, still excluded, question to Vadim:** `katerina` worked Circle Health Group (UK private hospitals) in `2026-09-27-uk-bariatric-prequal`, and the global company registry keys it as `circle-health` ("Group" is stripped as a legal suffix); this row is circle.health (Berlin). Nobody at circle.health is in any registry. `--waive-companies` lifts only a same-profile burn, not another profile's coverage, so the 2 Apollo people (Peter Malmqvist, Theresa Spiegelberger) stay `company covered by katerina` until Vadim decides.
4. **Dr.Dropin stays excluded:** 6 of the 7 sheet people were contacted from `olena` in `2026-07-21-eu-telehealth-weightloss`; the 7th (a board member) falls under the company burn. Lifting it is Vadim's call (`--waive-companies`), and only people never contacted would come back.
5. **Three websites corrected** (found while writing Account facts; web-verify had read them as "JS shell"): YEARS years.health → years.co (parked), Concierge Medicine Europe conciergemedicine.eu → conciergemedicine.cz (parked), Blue Health Intelligence blue.health → bluehealth.co (blue.health is BlueDigital, a pharmacy-loyalty company). biolytica.com is a domain-for-sale page; Biolytica has no live site found and nobody to send. No one was enriched from the wrong domains.

## What the closest accounts taught this campaign

> 1. **Everlab declined** (AU): the founder called it interesting tech that they are not looking at right now (`2026-08-14-au-digital-fitness/responses-summary.md`).
> 2. **Clinique La Prairie declined** (`olena`, 2026-10-13): it already measures body composition on site with its own devices, and an overlapping device could introduce inconsistencies in its data (`2026-10-07-eu-weight-loss-nutrition/responses-summary.md`).
> 3. **Superpower** (US, 21 people, 2026-09-29): no reply recorded as of 2026-10-19.
>
> Design response: target models where the member spends most of the year away from the clinic (blood re-tests on a cycle, an app in between); offer the capture for the member at home between assessments, never as a second device next to what the clinic measures on site. The Message 1 question stays about the person's own work (lane notes) and differs from person to person. The falsification test below names these two objections.

---

## Vertical

Continental European preventive-health and longevity companies that sell healthy adults a repeat relationship (membership, re-test plan or follow-up programme) built on periodic health assessments, with an app, member portal or clinician follow-up between them.

## Sub-segment: company types in scope

**In scope = all five:** (1) sells proactive or preventive health assessments to healthy adults, consumer or employer-paid; (2) a repeat relationship: membership, a re-test plan (typically 6-12 months) or a follow-up programme after the assessment; (3) a member-facing app or portal, or clinician follow-up between assessments; (4) 10+ employees and product HQ in the `olena` geo; (5) no shipped phone-camera body scan and no own body-scanning hardware as the core product.

**Fit:** 5 = membership with app and re-test cadence (the Everlab shape); 4 = assessment followed by app or clinician follow-up; 3 = assessment with a re-test offer but no member app found (on the list, flagged `fit=3`, counts toward the 25-30 and the gate by default; Open question 7).

Four segments. Named companies are research leads from a desk pass on 2026-10-19, not verified rows; step 2 re-checks each one.

- **A. Biomarker-testing memberships (digital first, partner labs, re-test cycle).** Lucis (Paris), Aware (Berlin), Axo Longevity (Madrid and London; product HQ to resolve, Open question 4). To check: Hello Inside (Vienna; CGM programme; check against the nutrition anti-case: IN only as a re-test membership with follow-up, OUT as a metabolic nutrition programme), Werlabs (Stockholm; membership or one-off tests), Holo (Spain; size), Loovi (origin unknown). **Seen: 3 likely, 4 to check.**
- **B. Full-body scan and imaging check-up companies with follow-up between assessments.** Aeon (Zurich; Germany and UK expansion), YEARS (Berlin), Prescan (Baarn, Netherlands), Preventicum (Essen). These companies measure the body on site, the setting of the Clinique La Prairie objection. **A B company is IN only with a relationship between assessments:** a member app or portal, or clinician or coach follow-up after the scan. A re-test offer alone is not enough for B. **Seen: 4, of which Prescan and Preventicum may be fit 3 or OUT.**
- **C. Longevity clinics with a membership and a digital follow-up layer.** Zoï (Paris), Kor (France), AYUN by Maximon (Zurich, annual subscriptions), Blue Longevity Clinic (Athens and Sofia; white-label app). To check: Longevia Medical Clinic (Rome), The Longevity Suite (Italy; diagnostics membership versus spa treatments), VIMED (Poland). **Seen: 4 likely, 3 to check.**
- **D. Doctor-led executive and corporate prevention programmes with follow-up** (the Everlab corporate executive-health line). Wellabe (Munich; workplace check-ups with an app and doctor video follow-up; majority owned by Mavie since August 2024). The B2B arms of Zoï, Aware and Prescan count under their own segment. **Seen: 1-2.**

**Research priority: A and C first, then D; B last.** B fills the list only after A and C are worked.

**Realistic count: ~12 likely and ~7 to check, which gives roughly 14-19 verified from the known names.** Reaching 25-30 needs step 2 to find about 10 more, A and C first, mainly in France, DACH, Iberia, the Nordics, Benelux, Italy and CEE. Many longevity clinics are single sites under 10 employees; the floor will cut them, and that is expected.

**Size:** 10+ employees (Vadim's decision 3), for this campaign only; `icp-detail.md` is not amended. A headcount conflict that straddles 10 goes on the list with the range in `employees` and the conflict in `notes`. Revenue is undisclosed for most of these companies and is not a FAIL reason (Open question 3); `revenue_estimate` is recorded where public.

**Geo and HQ:** product HQ decides, as on 2026-09-14: CEO and CPO location on LinkedIn, then where product roles are advertised, then press. Write the country into `hq_country`; where the legal seat differs, `legal_hq=...; product_hq=...` in `notes`. UK product HQ routes to `katerina`, US to `nick` (`validate-companies --write-routed`). Russia and Belarus are excluded.

**ICP mapping:** `icp-detail.md` has no preventive-health or longevity segment, and the validate card carries none. The five in-scope conditions and the feature screen are the screen; the size, revenue and geo limits of the telehealth and weight-loss segment do not apply (Open question 9).

## Feature screen (step 2 writes it into `notes` on every row)

`segment=A|B|C|D` · `fit=3|4|5` · `retest=` (cadence as published, or none) · `member_app=yes|no` (App Store or Play listing checked) · `body_measure_onsite=none|device|imaging|unknown` (what the company publishes) · `camera_scan=yes|no` (app listing and site; yes is an anti-case) · `b2b=yes|no` (employer offer) · `parent=` and date, where owned · `product_hq=` where it differs from the legal seat.

## Use case

Continental European preventive-health and longevity programmes can offer members a guided two-photo scan at home between periodic assessments, in the programme's own app or through a web link. Each scan returns 80+ body measurements (waist and hip among them), body composition estimates and a 3D model, and the clinician or health coach receives a standardized, timestamped body record.

## Why this is plausible (evidence)

1. **Money and members are flowing into European preventive-health memberships in 2025-26, and the model is periodic.** Lucis (Paris) raised a €17.3M Series A in May 2026, analyses 110+ blood biomarkers through partner labs in France, the UK, Ireland and Portugal, and reports 10,000+ users ([EU-Startups](https://www.eu-startups.com/2026/05/yc-backed-french-preventive-health-platform-lucis-raises-e17-3-million-series-a-led-by-singular/), [Lucis](https://www.lucis.life/blog/lucis-raises-20m-series-a)). Axo Longevity raised a $5M seed in September 2026; its core plan is €490 a year for two 100+ biomarker panels, re-tested six months apart, live in six markets ([Business Wire](https://www.businesswire.com/news/home/20260910642125/en/)). Aware (Berlin) sells two blood tests a year along with its app on subscription, with labs in Germany, Austria and the Netherlands ([Sifted](https://sifted.eu/articles/aware-amsterdam-lakestar-healthtech-news), [tech.eu](https://tech.eu/2023/10/31/healthtech-startup-aware-launches-publicly-now-live-in-berlin-and-hamburg-with-frankfurt-opening-soon/)). Aeon (Zurich) raised €8.2M in June 2025 for full-body check-ups and plans 10+ new locations ([IT Brief](https://itbrief.co.uk/story/aeon-raises-eur-8-2-million-to-expand-ai-driven-health-checks)); YEARS (Berlin) more than doubled bookings within a year ([Berliner Wirtschaft](https://www.berliner-wirtschaft.de/branchentrends/longevity-markt-berlin-geschaeftsmodelle)); Neko Health raised $700M in July 2026, and about 75% of its members book the next annual scan before leaving ([Medical Device Network](https://www.medicaldevice-network.com/news/neko-health-raises-700m-as-us-market-entry-draws-closer/)). Context only, never copy: funding and prices are banned terms.
2. **Between assessments, members have blood results, an app and wearable data, and no body-size record.** The European offers above are built on blood panels on a six-month or yearly cycle (Axo, Aware, Lucis) or an annual on-site assessment (Aeon, YEARS, Neko); the coverage found on 2026-10-19 for the blood-first memberships describes panels, health scores and wearable sync, and no body-size measure (step 2 records `body_measure_onsite` per account; absence is never stated in copy). Clinical guidance now asks for body size next to BMI: the Lancet Commission on clinical obesity (January 2025) says BMI alone should not be used for individuals and that excess adiposity should be confirmed by direct body-fat measurement or at least one of waist circumference, waist-to-hip ratio or waist-to-height ratio ([STAT](https://www.statnews.com/2025/01/14/bmi-lancet-report-obesity-as-disease-spectrum-urges-body-fat-measurements/), [Healio](https://www.healio.com/news/endocrinology/20250214/lancet-report-offers-a-new-reframing-for-defining-diagnosing-obesity); doi 10.1016/S2213-8587(24)00316-4). That is evidence from obesity care, not from this vertical, and "obesity" is banned in copy. No source from preventive-health memberships found on 2026-10-19 shows members or clinicians asking for a body record between assessments: the demand is inferred from the gap, and this campaign tests the inference. Everlab itself sells clinical body composition (bone density, physical performance assessment) at facility cost with visit-level frequency (AU notes). Context only, never copy.
3. **FitXpress fits as a home capture inside the member app, with honest limits.** Two photos (front and side), under 45 seconds from the photos to structured results, 80+ body measurements including waist and hip, body composition estimates (body fat %, lean mass, fat mass), BMI and BMR calculated, a 3D model; white-label REST API and web and mobile SDKs; repeatability per `accuracy-formulations.md` §1.2; 34,000 scans at one anonymised platform and 112,100 across all 3DLOOK customers in 2025 (`proof-points.md`). Limits: no published comparison with DEXA, MRI or bioimpedance, and none is claimed; validation 16-78 years, 150-220 cm, 38-210 kg; data on AWS US-West-2 and partly US-East-1; no named European longevity reference; "FitXpress is not a medical device."

## Target buyer persona

**Who buys:** the owner of the member experience and the member app. At startups (most of A, C and D) that is the founder or CEO, then the product lead; at clinics and check-up companies (B, C) the medical director and the head of operations or clinics; at corporate programmes (D) the head of corporate health or B2B.

- **Founder, CEO, Managing Director, Geschäftsführer, Directeur Général:** `product` lane, P1 at companies under ~200 people. Cares about members renewing and coming back for the next assessment, and what the app gives them between assessments. Objection: "not on our roadmap now" (the Everlab answer).
- **Chief Medical Officer, Medical Director, Head of Medicine or Prevention, Clinical Director, Chief Scientific Officer:** `clinical` lane, P1. Cares about what the care team reviews at each follow-up and the data quality of anything added. Objection: "an overlapping measurement could make our data inconsistent" (the Clinique La Prairie answer); the honest answer is that the scan is for the months away from the clinic and nothing on site changes.
- **CPO, Head of Product, Product Lead, Head of Digital; Product Manager at companies under ~200:** `product` lane, P1-P2. Owns the app roadmap and the build-or-buy call. Objection: "we could build it"; answer: pre-trained model through API and SDK, no computer-vision team to hire.
- **Head of Member, Patient or Customer Experience, Head of Care or Health Coaching, Head of Growth or Retention:** `product` lane, P2. Owns what members do between assessments.
- **COO, Head of Operations, Head of Clinics:** `operations` lane, P2. Cares about adding a member step without new equipment or site work.
- **CTO, Head of Engineering:** `technical-integration` lane, P3.
- **Head of Corporate Health, Head of B2B, Head of Partnerships, Business Development Director:** `product` lane at segment D and for the employer offer of A-C; `partnership` where the company resells or embeds third-party services.
- **Not the buyer, not pulled by the titles block:** marketing, brand, content and social, PR, sales representatives and account executives, recruiting and HR, finance below CFO, legal, laboratory and radiology staff, nurses, phlebotomists, front desk, staff physicians without a leadership title, investors and board members. If an export brings them anyway, the standing decision applies: `referral` lane, except investors, board members, freelancers and people whose current company is another one (FAIL).

### Target buyer persona: Sales Navigator pull for step 3

**Pull by title filter inside the approved company list, never by company alone.**

```titles
Founder
Co-Founder
Chief Executive Officer
CEO
Managing Director
General Manager
Geschäftsführer
Directeur Général
Chief Medical Officer
Medical Director
Head of Medicine
Clinical Director
Chief Scientific Officer
Head of Prevention
Head of Preventive Medicine
Head of Longevity
Chief Product Officer
Head of Product
Product Director
Product Lead
Product Manager
Chief Digital Officer
Head of Digital
Chief Operating Officer
Head of Operations
Head of Clinics
Head of Member Experience
Head of Patient Experience
Head of Customer Experience
Head of Care
Head of Health Coaching
Head of Growth
Head of Retention
Chief Technology Officer
Head of Engineering
Head of Corporate Health
Head of B2B
Head of Partnerships
Partnerships Director
Business Development Director
```

**`cap_per_group: 50`.** Most accounts here have 10-150 employees and the cap should not bind; if a group passes 50, leadership and product people first.

## Message angle: segments, lanes and the content asset

Every person gets exactly one lane: `product`, `clinical`, `operations`, `technical-integration`, `partnership` or `referral`. Company facts come from step 2 (`companies.md`), one or two per account, each with a source; never invent one. **Writer notes are instructions, never copy.**

### Segment angles (writer notes)

- **A. Biomarker memberships.** Members re-test on a cycle and live in the app in between. The scan gives the member a body record taken at home from that app. Never name their labs, never set scan outputs against blood results, never imply the panel misses something.
- **B. Full-body scan and check-up companies.** The assessment happens on site; the phone capture belongs to the months after it, in their app or a web link they send. Never mention their imaging, never compare, never present the scan as another device in the clinic.
- **C. Longevity clinics with a membership.** The member's year between clinic days, in the clinic's own app or a web link. Discreet, premium tone; no longevity, age or appearance outcomes.
- **D. Executive and corporate prevention.** The follow-up between yearly check-ups, on the employee's own phone; the programme decides what employees see. Never mention employer reporting features we do not have.

### Lanes

- **`product`:** what the member app or a web link can ask a member for: a guided two-photo scan returning 80+ body measurements, body composition estimates and a 3D model, white-label through API or SDKs. M1: context from the company fact and one question about the person's own work, no call ask, no link. M2: a short call offer with the calendar link.
- **`clinical`:** the target is the care team's view of a member between visits: a standardized, timestamped body record from each home scan; estimates for the team to review, never a diagnosis or a risk assessment. Repeatability only in the quoted sentence under Rules for steps 3-5 (Numbers and accuracy). Same M1 and M2 shape.
- **`operations`:** nothing to ship, stock or install; the same guided sequence on any phone; the speed phrase inside a sentence about the scan. Never say or imply sites measure differently today.
- **`technical-integration`:** REST API with API-key authentication, web and mobile SDKs; photos deleted after processing or within 30 days; outputs stored and deletable by scan ID. No integration-time figure. Technical tone.
- **`partnership`:** one line on what the scan returns, the company fact, and whether a partner capability has a place in what they offer. M2: the call offer; the easy out is a pointer to whoever decides partnerships.
- **`referral`:** M1: one line on what the scan returns and why it matters for this company's members, then one question about the person's own work; never a "who" question, no call ask, no link. M2: a short call offer with the calendar link and an easy out that points to the owner of the member app or the member experience, worded fresh for each person (name the target, never reuse a sample sentence).

### Account facts (writer notes: may be the "only this company" line, never copied word for word)

From step 2 (`companies.md`, 2026-10-19), re-read on each company's live site on 2026-10-21 (links below). One or two per Message 1, in fresh words; cadence in words; no prospect counts (biomarkers, members, check-ups, findings, bookings, sites, staff); name the brand the person works for.

- **Lucis (A).** An annual membership: one lab visit for a baseline panel, results in the Lucis app reviewed by a doctor, a doctor-reviewed plan that runs for twelve months with an AI coach in the app, and a follow-up panel whenever the member wants to see what changed ([lucis.life/membership](https://www.lucis.life/membership)). Never: a fixed re-test cadence ("twice a year" is no longer on the site), biomarker or member counts, the Lucis score, price, the scan feeding the AI coach, the scan next to blood results.
- **Axo Longevity (A).** Axo Longevity Care, a yearly membership: a short lab visit twice a year, a prioritised plan for nutrition, sleep, movement and supplements, and every six months the check is repeated and the plan adapted to the member's progress, in the member platform ([axolongevity.com/en-gb](https://www.axolongevity.com/en-gb)). Both people sit in the UK; the account stays on `olena` (Vadim's decisions (2), 3). Never: any country or market list, the lab network, the advisers' former clubs, biomarker or health-area counts, price, the platform's weight and body-fat area next to the scan.
- **speak23 (A).** An annual membership with two or four lab visits a year; after each visit the member gets a report that explains the values and turns them into concrete next steps, and follows progress over time in the member login ([speak23.com/at](https://www.speak23.com/at/)). Never: the sample report's body values (BMI, waist, waist-to-height) or any scan next to them, biological age, biomarker counts, lab cities, price.
- **Loovi (A).** One membership that tests, explains and coaches year after year: a blood draw and physical tests guided in the app, results on the Loovi platform, a doctor consultation, a personal plan, chat with the health team between check-ins, and retests on the programme's schedule ([loovi.health](https://loovi.health/)). Never: the app-guided physical tests (VO2 max, strength, mobility) or the site's comparison table with body scans next to our scan, member outcome figures, clinic counts, price.
- **Aeon (B).** After the check-up an Aeon doctor walks the member through the results and recommends next steps; with the Aeon membership the member retests once a year and follows health trends over time in the customer portal ([aeon.life/en-de](https://aeon.life/en-de/)). Never: MRI or any imaging, the number of findings, the AI body-composition analysis in a higher-tier package, early detection, Aware or any acquisition, funding, locations.
- **YEARS (B).** One day of check-ups in Berlin, then a doctor-built action plan and a year of follow-up: guidance in the YEARS app, a personal concierge, referrals to specialists, and check-ins once or three times a year depending on the programme ([years.co/en](https://www.years.co/en)). The `website` in `companies.csv` (years.health) is a parked domain; years.co is the clinic's site. Never: the whole-body MRI or any imaging, bone density, VO2 max, liquid biopsy, biological age, prices or insurer cover, biomarker counts.
- **Ahead Health (B).** Blood check-ups at partner clinics with a doctor's report; the member's online health report holds the results, an action plan and referrals, and once a baseline exists the member books follow-up tests to see how the values develop over time ([aheadhealth.com/de/en](https://www.aheadhealth.com/de/en/)). Never: MRI or imaging, risk scores, check-up counts, expansion plans or cities, funding, prices.
- **Zoī (C).** Paris check-up centre: the referring physician reviews every result and builds the action plan; between check-ups the Zoī app helps the member put the recommendations into practice, with a dedicated medical concierge, and the member comes back each year to measure progress ([zoi.com/en](https://www.zoi.com/en/)). Write Zoī or Zoi. Never: the DEXA scans in some follow-up options, imaging, check-up or data-point counts, prices, names of its corporate clients.
- **AYUN (C).** Zurich clinic: after the check-up the member gets a personal protocol (nutrition, training, recovery), the medical and scientific team keeps tracking progress and adapting it, and the AYUN digital platform holds biomarkers, progress and the plan ([ayun.ch](https://www.ayun.ch/)). Never: the clinic's body composition analysis (body fat, muscle mass, bone density), crowdinvesting or Maximon, insurer cover, customer counts, anti-aging.
- **CARE Preventive (C).** Check-ups at partner labs; results and recommendations are reviewed by specialist doctors and kept in the care app for long-term monitoring of values ([care.health/ch-de](https://care.health/ch-de/)). The brand on the site and in the app is written "care". Never: the medical weight-loss programme and its muscle-fat analysis, the whole-body MRI, biological age, insurer cover, member or location counts, prices.
- **MDConcierge (C).** Milan membership: each member has a Medical Tutor, an internist who builds a personal prevention plan, along with a dedicated conciergerie and MDConcierge's own digital tools between visits (the Hygea health record; the Active Care app per `companies.md`) ([mdconcierge.it/en](https://www.mdconcierge.it/en/)). Never: member or company counts, the Health Center's treatments, longevity outcomes, the first-in-Italy claim.
- **Longevity Center Poland (C).** Write Longevity Center (the person's profile says Longevity Center Europe). After a 360 assessment the member gets a personal plan carried out at home or in the centre; a dedicated doctor and team follow progress with digital tools and regular feedback, through annual programmes or quarterly check-ins ([longevity-center.eu/longevity-plan](https://longevity-center.eu/longevity-plan/)). Never: the assessment's body composition and functional testing, biological age, hallmarks of aging, the therapies (hormonal, hyperbaric), the Zurich site or any site count.
- **Longevia Medical Clinic (C).** Rome: the Longevia Protocol runs from a one-day 360 check-up to a plan built with the member's Longevity Specialist, with periodic check programmes, lifestyle advice (sleep, food, activity, stress) and ongoing dialogue with the team ([longevia.it/protocollo-longevia](https://longevia.it/protocollo-longevia/)). No app found: the scan reaches patients by web link. Never: the aesthetic and body-contouring treatments, IV therapy, cryotherapy, the postural or functional tests on check-up day, biological age, weight.
- **Blue Health Intelligence (C).** Amsterdam: a one-hour health check with the results discussed with a doctor straight away; afterwards the results and a personal action plan sit in the Blue app until the next check, and the site frames the check as yearly ([bluehealth.co/en](https://bluehealth.co/en/)). The `website` in `companies.csv` (blue.health) belongs to another company; bluehealth.co is Blue's site. The check includes a 3D body scan on site ([Amsterdam Now](https://www.amsterdamnow.com/en/lifestyle/blue-health-intelligence-health-check/)), the on-site measurement setting behind the 2026-10-13 decline. Never: the 3D body scan, ECG, ultrasound or any on-site test, the phone scan as a second or cheaper scan, price, booking counts, plans for new cities.
- **Kor (D).** Proactive check-ups that employers, complementary health insurers and brokers offer to their people, followed by continuous medical follow-up on the Kor platform, which keeps the person's health data in one place, follows how it changes over time and makes it easy to share with health professionals ([kor.care](https://www.kor.care/)). Never: company or user counts, living longer, the employer or insurer seeing individual results.
- **Mavie Work (D).** UNIQA's Mavie, Vienna; the list holds people at Mavie Work, at Mavie Next and at the Mavie group (mavie.care, Mavie Gesundheit) and its brands. Mavie Work runs workplace health programmes for employers: on-site prevention checks, psychosocial counselling, coaches and Mavie Move, a daily digital fitness programme ([work.mavie.care/de-at](https://work.mavie.care/de-at)). Mavie Next builds and scales Mavie's new health businesses; MavieMe sells home tests with doctor-explained reports and online doctor consultations ([mavie.care/de-AT/ueber-uns](https://www.mavie.care/de-AT/ueber-uns)). Name the unit the person works for, or Mavie where the profile says only that. Never: UNIQA or Raiffeisen, investment, the old Wellabe name, company or patient counts, the on-site check's values next to the scan, sick-leave or turnover claims, the employer seeing individual results, what Mavie Med clinics measure.
- **Concierge Medicine Europe (C).** Prague membership clinic: each member has a personal doctor with time for prevention, a medical concierge, a member portal and a lifestyle-medicine team (medicine, nutrition, fitness) under one roof, in its 360° Prevention & Care programme ([conciergemedicine.cz/en](https://conciergemedicine.cz/en/)). The `website` in `companies.csv` (conciergemedicine.eu) is a parked domain. No app found: the scan reaches members by web link. Never: the free body composition analysis on a clinic tour, patients-per-doctor or specialist counts, paediatrics, living longer.
- **Circle Health (C).** No people in this run: the registry name collision with Circle Health Group (`katerina`) keeps both people out until Vadim decides (Coordinator's decisions 2026-10-21, 3).
- **Prescan (B).** A one-day preventive examination in Baarn with lifestyle advice; a specialist goes through the results right after, and the results stay available at any time in the client's online portal ([prescan.nl/en/information](https://www.prescan.nl/en/information); the site was offline on 2026-10-21, read from the search copy). The person is listed at Prescan (UK) Ltd: write Prescan. Never: MRI, cardiology or any imaging, a re-test cadence (the every-two-years story is one customer's habit), the scan next to its examinations.
- **Werlabs (A).** Doctor-reviewed health checks: a Werlabs doctor comments on every result, results and the doctor's statement sit in the member's Werlabs journal, and members get a reminder when the yearly health check is due and can ask medical staff about their results ([werlabs.se/medlemskap](https://werlabs.se/medlemskap/)). Never: the MR and DEXA offers, the partner labs, health age, customer or sampling-site counts, prices.
- **Preventicum (B).** One-day, doctor-led health assessments with the results consultation on the day, a written report and a client portal; corporate clients get a dedicated account manager ([preventicum.co.uk/questions-and-answers](https://preventicum.co.uk/questions-and-answers)). No follow-up programme or app found: the scan would reach clients by web link between assessments. The live site is Preventicum UK Ltd in London, and a German head office is unproven (`companies.md`). Never: Essen or Germany, MRI, cardiac tests or any imaging, early detection, prices, the tax treatment of corporate assessments.
- **Hello Inside (A).** Women's metabolic health app: a glucose sensor linked to the Hello Inside app, step-by-step programmes for each life stage (cycle, menopause), personalised recommendations and a dashboard of the lifestyle factors behind them ([helloinside.com/en-de](https://helloinside.com/en-de)). Never: weight or weight management, glucose data next to the scan, the app's front-camera face scan, user outcome figures, insurer cover or BARMER.
- **Dr.Dropin (D).** No people in this run: the company was worked from `olena` on 2026-07-21 (Coordinator's decisions 2026-10-21, 4).
- **Macromo (A).** Prague biomarker app: a baseline blood test, results explained in the Macromo app, a personal plan (food, supplements, lifestyle), past lab results and wearables in one place, and a retest once a year to see what changed ([macromo.com](https://macromo.com/)). Michal Pohludka (science studio, the parent studio) is listed as Macromo's co-founder on the site: write to him about Macromo. Never: DEXA or the weight-loss goal, the partner labs, customer or testing-location counts, TCF Capital or any ownership, the scan next to blood results.
- **Biolytica (C).** Only 2023 sources: NEXUS, a health-data platform that preventive clinics and longevity centres use to build personal plans for their clients, and AIME, Biolytica's own concierge programmes with personal guidance from its experts ([Startupticker, 2023](https://www.startupticker.ch/en/news/biolytica-raises-chf5-25-million-for-its-health-data-platform)). biolytica.com shows a domain-for-sale page and no live site was found on 2026-10-21: state nothing as current. Never: the website, team size, Maximon or funding, insurer clients, lifespan claims.

### Content asset in Message 2 (at most one article link, along with the calendar link)

| Who | Link |
|---|---|
| `product`, `clinical`, `operations`, all segments | https://3dlook.ai/content-hub/ai-body-data-wellness-platforms/ |
| `technical-integration` | https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/ |
| `referral`, `partnership` | no article; calendar link only |

Both links returned HTTP 200 on 2026-10-19. Never quote figures from the page.

## Outreach language

English only, every country (Vadim, 2026-09-14, a standing decision). Many readers are French, German, Italian and Spanish doctors and founders reading in a second language: short sentences, plain words, no idioms.

## Rules for steps 3-5

- **Sender and format:** Olena, English, `Olena` alone on the last line. Connection request with no note. Message 1 ≤ 600 characters with no link; Message 2 ≤ 550 with https://meetings.hubspot.com/olena-kudriavtseva as plain text in every lane and at most one article link (asset table). One import file.
- **Message 1 asks, Message 2 calls** (`referral_call: yes`), every lane: Message 1 = context first (what the scan returns and why it matters for this company's members), then one question; no call ask, no link. Message 2 = a short call offer with the calendar link; people who are not the buyer get an easy out pointing to the owner of the topic. Never the same ask twice.
- **Message 1 gate.** Every message 1 carries at least one product specific from `proof-points.md` and one line that could only have been written to that company; each pair of messages cites at least one number. `referral` is not exempt.
- **Between assessments, at home.** The scan is always positioned for the member away from the clinic, between assessments or re-tests. Never present it as a second device next to what a clinic measures on site, never compare it with their imaging, body-composition devices or blood results, and never say or imply what the company lacks. Message 1 makes an observation from the company fact or the person's role.
- **Never put a prospect's own data next to ours.** No message names a prospect's panels, scans, scores or device data and then says what the scan returns. A company's assessment cadence or programme may be named as context.
- **Not a diagnosis, not a risk score, not an outcome.** The scan does not diagnose, assess risk, detect disease, decide eligibility or recommend treatment. No promises about longevity, age, health outcomes, renewals or retention. Who compares: the programme's care team chooses which scans to compare; no message says or implies that 3DLOOK or the scan follows a member over time. Never for anyone under 16 or in pregnancy.
- **Several people at one company:** never mention colleagues or claim a conversation that did not happen; name the company in every Message 1; no two people at one company share an opener, a central question, a closing ask or a product sentence.
- **Companies:** never mention funding, investors, valuation, owners, acquisitions, prices, revenue, headcount, member counts or locations counts. A former employer may be named unless it is another account in this campaign.
- **Compliance line:** at most one, only in Message 2. `product`, `operations`, `technical-integration`: only the GDPR line verbatim from `compliance.md` §9 (UK / EU). `clinical`: only "FitXpress is not a medical device." `referral`, `partnership`: none. Never "HIPAA compliant", "SOC 2 certified" or any certification claim. EU hosting, special-category data and AI Act questions are not answered in copy (Open question 8).
- **No 3DLOOK client is named.** Anonymised proofs only: 34,000 scans in 2025 at one platform (no client name, no geography); 112,100 scans in 2025 across all 3DLOOK customers (its own sentence); "3DLOOK has worked with 100+ clients" (all-time, both products; never "use FitXpress today").
- **Numbers and accuracy only from `proof-points.md` and in its wording:** two photos; "under 45 seconds from the photos to structured results"; 80+ body measurements; body composition estimates (body fat %, lean mass, fat mass), BMI and BMR calculated; accuracy only per `accuracy-formulations.md` §1.1 (body measurements only, never in a sentence with body composition); repeatability, in any lane, only as this sentence, word for word (the one rule sentence that goes into copy verbatim): "For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm." Never rebuild it from "< 1 cm"; 38-210 kg only in `clinical`. No integration time, market, prospect or medical figures.
- **The 3D model** is shown only where the programme chooses to show it; never lead with it as the value.
- **Use-case file limits:** from `fx-telehealth-weight-loss` take only "What FitXpress is here", without Smart Scales. Its hero line, Why now, KPI list, weight-loss and GLP-1 framing do not apply to this audience.
- **Word traps:** no "objective" about our data (standardized, timestamped, structured, repeatable); no "comprehensive", "seamless", "leverage", "game-changer"; no em or en dash; no "plus" as a connector; no "so" introducing a benefit; no corrective "X, not Y". No pricing or trial terms anywhere; a price question goes to the call.

## Anti-cases (where it does NOT work)

- **Already worked or held:** Clinique La Prairie (`olena`, declined 2026-10-13); Lykon (Lifesum group, Lifesum worked from `olena` 2026-09-14; Open question 2); AMRA Medical (held out 2026-10-07, imaging analytics vendor); every company in `olena-registry.json` and in another profile's registry; existing customers. Everlab and other non-European look-alikes are not in this geo.
- **Own body-scanning hardware or a shipped camera scan:** Neko Health (Stockholm; 70-sensor scanner with 2D and 3D photography; Open question 1); any company whose app already runs a phone-camera body scan or has signed a scanning vendor; camera-analysis vendors selling into this category (YOU(th) Health Tech type). Displacement, not this campaign.
- **Clinic-only programmes where every measurement happens on site:** luxury residential retreats and destination spas (Lanserhof, Chenot, SHA, Buchinger Wilhelmi, Progevita type). The Clinique La Prairie decline is the evidence.
- **Lab and test-kit sellers without a repeat relationship:** one-off home-test e-shops and DNA-only test sellers (Cerascreen, N-Gene type); laboratory chains (Synlab, Unilabs, Cerba, Eurofins), which supply these memberships. A test seller is IN only with a membership or re-test plan and follow-up.
- **Check-up departments inside hospital groups** (Hirslanden, Swiss Medical Network, Hannover Medical School executive check-ups, Sana type): one service line, hospital procurement, no member layer (Open question 6).
- **Aesthetic, anti-aging and biohacking treatment networks** selling drips, cryotherapy or aesthetics without a diagnostics membership and follow-up.
- **Other theses already run on `olena`:** weight-loss, GLP-1 and nutrition programmes (2026-07-21, 2026-10-07), telehealth and online pharmacies, consumer fitness and nutrition apps (2026-09-14), DiGA or CE-marked apps.
- **Statutory occupational medicine** (fitness-for-work, Arbeitsmedizin): a different use case (`fx-occupational-health`). Voluntary preventive check-ups paid by employers stay IN under D.
- **Insurers and wearable or smart-scale makers:** different sales (wellness rewards; device businesses).
- **Structural:** under 10 employees, product HQ outside the `olena` geo (route, do not discard), Russia or Belarus (exclude), acquired or merged in the last 18 months.

## Validation criteria (Step 2 will check)

- **List size:** 25-30 verified companies is the target. **≥20 verified → step 3** (coordinator's decision 2). Fewer than 20 → stop at step 2 and report to Vadim with `companies.csv`; do not pad with anti-cases. A row counts only when `web-verify.py` returns `verified*` with a `source_url`; a `blocked` row counts only after a manual check written as `verified-manual` with `manual_check=<who>, <date>, <what>` in `notes`.
- **Row schema:** `company_name, website, linkedin_url, hq_country, hq_city, employees, revenue_estimate, fit_score_1_to_5, fit_reason, source_url, notes`, with the feature screen in `notes`, one canonical name per company, and `validate-companies --campaign 2026-10-19-eu-everlab-similar --profile olena --write-routed` exiting 0.
- **Every row proves the five in-scope conditions** with a source: the assessment, the repeat relationship, the app, portal or follow-up, 10+ employees, and `camera_scan=no`.
- **Registry:** no company covered by any profile; `outbound-registry.py check --profile olena` on people before import.
- **People:** pulled by the titles block; a job-change check before import; ≥40 contacts at PASS across ≥15 companies.
- **Proof:** no named reference in this vertical; the two anonymised scan figures are the proof. Each company gets one or two sourced facts in `companies.md` for Message 1.

## Success metrics for this campaign

| Metric | Target | Floor |
|---|---|---|
| Verified companies | 25-30 | 20 (coordinator's gate) |
| Contacts at PASS | 60+ | 40 |
| Connection acceptance | 25% (about 15 of 60) | 15% (`olena` July: 25.0%) |
| Replies per accepted person | 10% (1-2 replies) | 5% |
| Positive replies (interested or call) | 1 | none set |
| Discovery calls | 1 within 8 weeks | none set |

**What this volume can show.** About 60 contacts at 25% acceptance is about 15 accepts, and 10% of those is 1-2 replies. The likely outcome is a small-sample read: directional, not a verdict. At the 40-contact floor the read is inconclusive by design.

- **Inconclusive** if fewer than 15 people accept.
- **Supported (directional)** if one P1 or P2 reply is positive or books a call.
- **Falsified** if 2 or more P1 or P2 replies give the same known objection: a home body record overlaps with what they measure on site, or body data is not on their roadmap. One such reply is noted, not a verdict.

## Open questions for Vadim (default taken on each)

1. **Neko Health** (Stockholm product HQ; its own 70-sensor scanner with 2D and 3D photography; UK and US clinics). **Default: OUT** (own hardware, displacement). Release as a partnership ask?
2. **Lykon** (Berlin home blood tests; owned by Lifesum since June 2024; Lifesum worked from `olena` 2026-09-14). **Default: OUT.**
3. **Revenue floor.** The nearest `icp-detail.md` segments set $2M+; most targets do not disclose revenue. **Default: not a FAIL reason;** 10+ employees is the only size gate.
4. **Axo Longevity product HQ** (press datelined London and Madrid, jobs in Barcelona, operates in the UK). **Default:** product-HQ rule; Spain → `olena`, London → route to `katerina`.
5. **People in the UK or outside Continental Europe at IN companies** (Lucis, Aeon, Axo UK teams). **Default:** named head-office people stay on `olena` (one company, one profile; the 2026-10-07 validation exception); local UK clinic staff OUT.
6. **Hospital-group check-up centres** (Hirslanden, Swiss Medical Network type). **Default: OUT;** a dedicated prevention brand with its own membership or app can be IN. Release specific names at the list review.
7. **Fit-3 rows** (assessment and re-test offer, no member app found; in B only with clinician or coach follow-up; Prescan and Preventicum may land here). **Default:** on the list, flagged `fit=3`, counted toward the 25-30 and the ≥20 gate. Count them on the list but not toward the gate?
8. **EU compliance answers** beyond the GDPR line (special-category data, EU hosting, AI Act), open since 2026-09-14. **Default:** nothing in copy; such replies go to legal@3dlook.me.
9. **ICP segment.** `icp-detail.md` has no preventive-health or longevity segment, and the validate card carries none. **Default:** the five in-scope conditions and the feature screen are the screen; nothing is borrowed from the telehealth and weight-loss segment (its 50-5000 employees and its geo do not fit). Add a segment to `icp-detail.md` if this campaign gets a positive reply?

## Sources

- Internal: `2026-08-14-au-digital-fitness/companies.md` (### 03. Everlab) and `responses-summary.md`; `2026-10-07-eu-weight-loss-nutrition/hypothesis.md` and `responses-summary.md`; `2026-09-14-eu-erakulis-similar/hypothesis.md`; `2026-09-29-us-cardiometabolic/hypothesis.md`; `exclusions/*.json` and `outbound-registry.py status` (2026-10-19); `icp-detail.md` (telehealth and weight-loss, employer wellness and digital fitness segments; universal exclusions); `use-cases/fx-telehealth-weight-loss.md`; `proof-points.md`; `accuracy-formulations.md`; `compliance.md`; `competitors.md`.
- Market and accounts: [EU-Startups, Lucis Series A](https://www.eu-startups.com/2026/05/yc-backed-french-preventive-health-platform-lucis-raises-e17-3-million-series-a-led-by-singular/) · [Lucis blog](https://www.lucis.life/blog/lucis-raises-20m-series-a) · [Business Wire, Axo Longevity seed](https://www.businesswire.com/news/home/20260910642125/en/) · [Sifted, Aware Amsterdam](https://sifted.eu/articles/aware-amsterdam-lakestar-healthtech-news) · [tech.eu, Aware launch](https://tech.eu/2023/10/31/healthtech-startup-aware-launches-publicly-now-live-in-berlin-and-hamburg-with-frankfurt-opening-soon/) · [IT Brief, Aeon seed](https://itbrief.co.uk/story/aeon-raises-eur-8-2-million-to-expand-ai-driven-health-checks) · [Berliner Wirtschaft, longevity in Berlin](https://www.berliner-wirtschaft.de/branchentrends/longevity-markt-berlin-geschaeftsmodelle) · [StartingUp, Longevity Start-up Report 2026](https://www.starting-up.de/geschaeftsideen/trends/longevity-start-up-report-2026.html) · [Medical Device Network, Neko Health Series C](https://www.medicaldevice-network.com/news/neko-health-raises-700m-as-us-market-entry-draws-closer/) · [Prescan for business](https://www.prescan.nl/en/business) · [Maddyness, Zoï, Kor and Lucis](https://www.maddyness.com/?p=1433868) · [Maximon, AYUN subscription](https://www.maximon.com/news/ayun-offers-a-long-life-subscription) · [tech.eu, Blue Longevity Clinic](https://tech.eu/2025/07/22/blue-longevity-clinic-raises-eur2m-to-launch-next-gen-health-centers-in-se-europe/) · [Forbes Italia, Longevia Medical Clinic](https://forbes.it/2026/08/05/longevia-medical-clinic-modello-medicina-preventiva/) · [tech.eu, Hello Inside and BARMER](https://tech.eu/2026/04/21/hello-inside-pushes-metabolic-health-into-mainstream-care-with-barmer-deal/) · [tech.eu, Wellabe](https://tech.eu/2020/12/04/wellabe-series-a/) · [Athletech News, Lifesum acquires Lykon](https://athletechnews.com/lifesum-acquires-lykon-adds-biomarker-testing/)
- Clinical context: [STAT, Lancet Commission](https://www.statnews.com/2025/01/14/bmi-lancet-report-obesity-as-disease-spectrum-urges-body-fat-measurements/) · [Healio](https://www.healio.com/news/endocrinology/20250214/lancet-report-offers-a-new-reframing-for-defining-diagnosing-obesity) · Rubino et al., Lancet Diabetes Endocrinol 2025;13:221-62, doi 10.1016/S2213-8587(24)00316-4.
