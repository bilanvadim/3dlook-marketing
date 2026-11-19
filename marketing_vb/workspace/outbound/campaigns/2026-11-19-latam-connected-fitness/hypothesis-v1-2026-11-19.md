---
product: fitxpress
profile: katya
market: South America + Mexico
created: 2026-11-19
status: draft
use_case: fx-digital-fitness
cap_per_group: 50
message_max_chars: 900/700
referral_call: yes
learnings: 2026-10-30
banned_terms: [Yazen, UK Meds, Healthyr, Safariland, Burlington, Jim's Formal Wear, Generation Tux, Tailoor, Redthread, Zing Coach, Verv, Prism, Bodygram, Size Stream, Fit:match, Mirrorsize, Bodd, Evolt, Styku, Fit3D, InBody, Tanita, Withings, Seca, Visbody, ShapeScale, BodyLoop, Bodymapp, Spren, ZOZOFIT, Technogym, Smart Fit Body, Kidman, Journal of Medical Internet Research, TotalPass, Wellhub, Gympass, Fitpass, Face Doctor, Nordic Fitness, Profeco, LGPD, LFPDPPP, ANPD, ANVISA, COFEPRIS, CONFEF, CREF, HIPAA, BAA, GDPR, SOC 2, FDA, MDR, CE mark, AWS, data residency, compliant, certified, certification, accredited, clinically validated, clinically proven, peer-reviewed, medical-grade, guarantee, guaranteed, accuracy, accurate, 96-97, 1.5-2.0, API requests, free trial, voice prompts, voice guidance, Smart Scales, verify, verified, verification, fraud, mismatch, eligibility, anonymous, not stored, no personal data, churn, obese, obesity, overweight, weight loss, weight-loss, fat loss, burn fat, bikini, summer body, before and after, before-and-after, shred, beyond the scale, non-scale, GLP-1, Ozempic, Wegovy, Mounjaro, semaglutide, tirzepatide, DEXA, DXA, visceral, diagnose, diagnosis, pregnant, pregnancy, children, kids, teens, ROI, acquisition, acquired, merger, IPO, funding, investors, valuation, Series A, Series B, Series C, largest chain, leading chain, Israel, generic figure, never a promise, not a promise, context only, writer note, Circling back, Following up, Saw your post, Thanks for connecting, thank you for connecting]
---

# Outbound Hypothesis: 2026-11-19, gym chains in South America and Mexico that run their own member app (connected-fitness page, Katya)

- **Campaign:** `2026-11-19-latam-connected-fitness`, one of four parallel campaigns on the new use-case page (nick for the US, olena for Europe, vadim for Australia, katya here). The siblings share the page and never appear in copy. Direction: Vadim, 2026-11-19, relayed by the coordinator: outreach on https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/ from four profiles; ICP = `icp-detail.md` §8 Connected & Digital Fitness; in Latin America look beyond pure apps where the evidence supports it.
- **Sender:** Kateryna (Katya) Boichuk, profile `katya`. Market = `PROFILE_GEO["katya"]` in `scripts/outbound-pipeline.py`: Brazil, Argentina, Chile, Colombia, Peru, Ecuador, Bolivia, Uruguay, Paraguay, Venezuela and Mexico. Central America and the Caribbean belong to no profile. `OWNER["katya"] = "Kateryna"`; calendar https://meetings.hubspot.com/kateryna-boichuk (`outbound-message2-template.md`). This is her first fitness campaign.
- **Product claims come from the live page only:** `workspace/pages/for-connected-and-digital-fitness/published-live-2026-11-19.md` (curl, HTTP 200, captured 2026-11-19; H1 "A mobile gym body scanner alternative for fitness apps"), with numbers from `proof-points.md`. Not `page-final-2026-10-07`.
- **Registry, checked 2026-11-19.** `outbound-registry.py status`; a search of `global-company-registry.json` for gym, fitness, coaching and gym-software names; and a run of `outbound-registry.py check --profile katya` on 46 candidate and reserve names (scratch input, nothing recorded). All clear except the control row Face Doctor (`katya`, `2026-10-05-latam-health-weightloss`). No Latin American gym chain, gym-software platform or fitness app is covered by any profile. `vadim` holds Australian country rows (Anytime Fitness Australia, Planet Fitness Australia, Snap Fitness Australia, Les Mills Asia Pacific); the Mexican franchise rows here are separate country rows and did not collide. Customers with a contract stay out: Zing Coach and Verv (`existing_customer_excluded`), neither in this market.
- **Re-contact (Vadim 2026-11-17: every company without a contract may come back).** None of `katya`'s 77 registered companies is a gym chain, gym-software platform or fitness app, so none is re-contacted in this cut. Nearest, with history, all outside this sub-segment (weight-loss and aesthetic franchises, clinics and corporate health, Anti-cases), not dropped by the registry: Emagrecentro, Magrass, Siluets, Lipocenter, Pró-Corpo, Grupo 5S, N2B Brasil (body-composition exams), Grupo Wellness Latina, Wellbe, Vidalink, Salvia Saúde Corporativa (all `2026-10-05-latam-health-weightloss`, 2026-10-05); Fleury Lifecare, Care Club and the other longevity accounts (`2026-10-19-latam-everlab-similar`, 2026-10-19). Any of them comes back only on Vadim's word (Open question 15). One link to watch: Selfit's founder also founded Face Doctor (Times Brasil); Selfit is not registered, and Face Doctor is never mentioned.

> **Read this first.**
> 1. **One sub-segment: gym and fitness-club chains in South America and Mexico that run a member app and a body assessment as a member service** (avaliação física, evaluación física, valoración; often bioimpedance on a device in the club). Plus a small partner group: the gym-software and assessment platforms whose member apps carry that assessment for independent gyms. Pure fitness apps, online-coaching tools and corporate gym networks were checked and left out (Why this cut).
> 2. **The pain, about the method:** the assessment lives in the club. It needs a device and a trainer, so it repeats only when the member comes in; between assessments the member app shows classes, workouts and access, and nothing about body change. **The fix, from the live page:** a two-photo scan on the member's own phone inside the chain's app, white-label, returning 80+ body measurements and body composition estimates as one timestamped record linked to the member profile; "An in-gym scanner still suits members who visit the club; FitXpress covers the check-ins between visits."
> 3. **Retention is the page's argument and a lane that drew 0/53 (learnings HYP-6).** Here it is a marked test: never the pain or the opener in Message 1, only the measured outcome of the pilot design in Message 2, and in at most about half of each company's Message 2s.
> 4. **No gym-chain or Latin American customer, no named fitness reference.** Validation participants were from the US and Europe. Body composition values are estimates with no published comparison with bioimpedance.
> 5. **English cold copy by default** (the 2026-11-05 decision for Katya's latest campaign); language, pricing, the page link, the 900-character cap and the boundary line are Open questions with recommendations.

---

## Vertical

Gym and fitness-club chains headquartered in South America or Mexico (company-owned networks and franchise networks with one head office) that give members a branded member app and run a body assessment as a member service, measured in the club: avaliação física in Brazil, evaluación física or valoración in Spanish-speaking markets, frequently bioimpedance on a device in the club. With the gym-software and assessment platforms whose member apps show that assessment to members of independent gyms.

## Sub-segment

Chains with about 20 or more clubs (or a published US$1M+ revenue) in `katya`'s countries, a member app in the brand's name on the App Store or Google Play in the row's country, and a published body assessment, body-composition service or in-app training plan; plus five platforms. 24 named rows, 6 reserve; expected IN about 16 (range 12 to 20). Every row's `hq_country` is the row's own country (Brazil, Mexico, Colombia, Argentina), never "Latin America", "LatAm" or "Americas": `geo_profile()` matches "america" to `nick`.

**A-BR. Brazilian chains (8).** Smart Fit (São Paulo; 2,170 gyms and 5.6 million members by June 2026 across its markets; the Bio Ritmo App keeps each member's physical-assessment history, weight, bioimpedance and body-fat %, and the Smart Fit Nutri app offers a bioimpedance service; evidence in hand; one row and one group for Smart Fit and Bio Ritmo, people in any `katya` country); Bluefit (BlueUp, an app built with the assessment platform FitMass, shows bioimpedance charts and reports and lets members share assessments; evidence in hand); Skyfit (about 600 units, second network by units; app to confirm); Panobianco (400+ units; app to confirm); Selfit (200+ units; app to confirm); Academia Gaviões 24h (100+ units and about 400,000 active members, its own statement; app to confirm); Bodytech Brasil (to confirm; a different company from Bodytech Colombia, row names keep them apart); Pratique Fitness (expanding into Argentina in 2026; app to confirm).

**A-MX. Mexican chains (6).** Sports World (member app with clubs, class booking, daily diets and workouts; personal-training sessions confirmed with a code in the app, January 2026 terms; evidence in hand); UFC GYM MX (app tracks the evolution of body composition, App Store listing; size to confirm); Planet Fitness México (50 clubs and 300,000+ members, September 2026; operator entity and app publisher to confirm); Anytime Fitness México (to confirm; app likely the franchisor's); Sport City (to confirm); Energy Fitness México (to confirm). Smart Fit's Mexican business sits in the Smart Fit row.

**A-CO. Colombian group (1) and chains (2).** Bodytech Colombia (Bodytech, Athletic and Sportlife brands, 150+ sites in Colombia and Chile with Peruvian sites too, per trade press; aims at half a trillion pesos of revenue in 2026, per Portafolio, date to re-check; a freemium App Bodytech reported in development; evidence in hand; Sportlife Chile and Bodytech Peru people sit in this row); Spinning Center (to confirm); Stark Smart Gym (to confirm).

**A-AR. Argentine chains (2).** Megatlon (app with access credential, class grid and bookings, and M-Play workouts; evidence in hand); SportClub (app with QR access, 500+ on-demand classes and meal plans; evidence in hand).

**B. Gym-software and assessment platforms (5), lane `partnerships`.** Tecnofit (its student app shows each member the physical assessments the gym registers; evidence in hand); EVO (W12) (branded member apps for gyms on its software carry the physical assessment, e.g. Academia 360 Club; to confirm); Pacto Soluções (to confirm); Nextfit (to confirm); FitMass (assessment platform behind Bluefit's BlueUp; never named in Bluefit's copy; to confirm size). One integration here reaches independent gyms that will never run their own SDK.

**Reserve, only on Vadim's word:** Befit (Brazilian fitness app; R$13 million revenue in its first 15 months to March 2026 and 2 million users, per O Povo); Just Fit, Cia Athletica, Academia Corpo e Saúde (Brazilian chains, no evidence gathered); Fitco (gym software, Peru, not checked); Smart Fit's TotalPass (see Out).

**Out:** Wellhub (Gympass): headquartered in New York (`nick`'s market) though about 65% of its staff are in South America; an aggregator whose check-in is a gym visit (Open question 9). TotalPass: Smart Fit's aggregator, same reason; its staff FAIL inside the Smart Fit row. Fitpass: no evidence found. Energy Pacific (Chile): club closures reported in June 2026 (Open question 10). Online-coaching tools for individual trainers (MFIT and similar): no LatAm platform with published US$1M+ revenue found, and single-trainer deals are where price-led rivals win (`competitors.md`). Pure fitness apps other than Befit: none with published revenue found.

**Count:** 8 + 6 + 3 + 2 + 5 = 24 named. Evidence in hand for 9 (Smart Fit, Bluefit, Sports World, UFC GYM MX, Bodytech Colombia, Megatlon, SportClub, Tecnofit, and Planet Fitness México on size); 15 to confirm at step 2. Step 2 may add chains in Chile, Peru, Colombia and Mexico that meet the same definition (about 20+ clubs or US$1M+, own branded app, assessment or in-app training plan), flagged as additions, never to reach a number. Expected IN about 16 (range 12 to 20), a judgment.

**Why this cut, not another:**
- **Chains are where the money and the members are.** Smart Fit alone reports 2,170 gyms and 5.6 million members (June 2026) and plans 330 to 350 openings in 2026; recurring net profit rose 40% in Q3 2026. Panobianco opened more gyms than Smart Fit in a recent period (Citi, via Bloomberg Línea). Smart Fit plans about 70 openings in Mexico in 2026; Planet Fitness México reached 50 clubs in September 2026.
- **The chains already put body data in the member app, measured in the club.** Bio Ritmo App, Smart Fit Nutri, BlueUp, Tecnofit's student app and the EVO-based Academia 360 Club app all show assessments taken in the club. The page's comparison table has an "in-gym body scanner" column and the line about check-ins between visits: the page argues this exact case.
- **Retention is now the open fight in Brazilian fitness** (Estado de Minas, July 2026), with ACAD Brasil citing average annual drop-out of 40% to 60%. Buyer context only, never copy (HYP-6, Rules).
- **Most gyms are independents on gym software.** Brazil had 62,718 active fitness centres in 2025 (Panorama Setorial Fitness Brasil 2025). The five largest networks' published unit counts (986 + about 600 + 400+ + 200+ + 200+) add up to about 2,400, under 4% of that (arithmetic on trade-press rankings). Their members see assessments in the software vendor's app, hence group B.
- **Pure apps are thin here.** The `icp-detail.md` §8 examples are US and European; one Brazilian app with published revenue turned up (Befit, reserve). Smart Fit Nutri and the chains' own apps carry most of the digital fitness use in this market.

**Size:** `icp-detail.md` §8 sets US$1M+ revenue. Every A-BR chain listed clears it on unit count (judgment); A-MX, A-AR and group B rows confirm at step 2.

## Use case (1 sentence)

A gym chain in South America or Mexico adds a white-label two-photo FitXpress scan to its own member app, allowing members to repeat a body check-in on their own phone between club visits, and each scan returns 80+ body measurements and body composition estimates as one timestamped record linked to the member profile, next to the in-club assessment the chain already runs.

## Why this is plausible (3 reasons grounded in evidence)

1. **Large, growing chains run their own member apps.** Smart Fit: 2,170 gyms, 5.6 million members (June 2026), 330 to 350 openings planned in 2026 (Investidor10; Mercado & Consumo). Mexico: Smart Fit 395+ gyms and 1 million+ users, about 70 openings and MXN 1,500 million+ investment in 2026 (Expansión; Emprendedor); Planet Fitness México 50 clubs, 300,000+ members (El Financiero; Forbes México). Colombia: Bodytech Group 150+ sites across Bodytech, Athletic and Sportlife (Forbes Argentina via search; Portafolio). Apps verified in this round: Smart Fit Nutri, Bio Ritmo App, BlueUp (Bluefit), Sports World, UFC GYM MX, Megatlon, SportClub (App Store listings and El Cronista).
2. **The body assessment lives in the club, and the app only shows its result.** Bio Ritmo App holds the history of physical assessments (weight, bioimpedance, body-fat %); Smart Fit Nutri offers a bioimpedance service; Smart Fit Colombia's contract describes bioimpedance tests; BlueUp shows bioimpedance reports; Tecnofit's student app shows an assessment only after the gym registers it. The page's FAQ: "A body scan at the gym is a measurement taken on hardware in the club... Each repeat needs a club visit." Between visits the apps show access, classes, workouts and meal plans (Megatlon, SportClub, Sports World). Retention is the stated battleground in Brazilian fitness in 2026 (Estado de Minas, ACAD Brasil 40% to 60% annual drop-out). No phone-based body scan was found in any Latin American chain's app (search, 2026-11-19); in-club scanners are what vendors market here. Context only, never copy.
3. **FitXpress covers exactly the check-in between visits** (live page): the scan runs on the member's own phone inside the chain's app, with no hardware and no club visit, under the chain's brand and consent wording; Real-Time Pose Validation (RTPV) guides the capture; under 45 seconds from the photos to structured results; 80+ body measurements (waist, hip, chest, thigh, calf), body composition estimates (body-fat %, lean mass, fat mass), BMI and BMR calculated; one timestamped record per scan through the API, linked by scan ID to the member profile; trainers review the same record before the next block; 3D Body Progress tracking and 3D Goal Visualization for a premium tier; a pilot with a comparison cohort; no integration fee. **Limits:** no gym-chain or Latin American customer; validation participants from the US and Europe ("Locations: US, Europe", `proof-points.md`), Latin American populations not characterized separately (a Brazilian dissertation on 3D scanning notes the same gap for Brazil); body composition values are estimates, with no published comparison with bioimpedance (a reference-device report is due December 2026, `roadmap.md`); Portuguese and Spanish capture screens not confirmed (`roadmap.md`: localization planned Q4 2026); native voice guidance in testing; data hosted in the US.

## What earlier campaigns teach this one

- **Katya in Latin America** (learnings data 2026-10-31): `2026-10-05-latam-health-weightloss` 56/127 accepted, 5/56 replied (three questions, one referral, one courtesy; a CEO asked for the studies behind the technology; a commercial head named the head of product); `2026-10-19-latam-everlab-similar` 28/47 accepted, 2/28 replied. Three of the first four 2026-10-05 replies came in English. `2026-11-05-latam-insurance-underwriting`: 126 imported, no reply data yet.
- **Digital fitness elsewhere** (pooled 99/491 accepted, 14/99 replied): `2026-08-07-us-digital-fitness` drew its one interested reply from a subscription owner on Message 1; `technical-integration` drew 0/60; large brands replied and small apps did not (0/81). `2026-10-11-au-sport-fitness`, the gym-chain template, is too young to read (9/96 accepted, 0/9 replied at 19 days).
- **"How is this different from what we already use?"** (MSG-4) here means the in-club bioimpedance device. One sentence may say what the phone adds; the device is never named or criticised.
- **Card samples get copied** (`2026-10-07`, `2026-10-11`): Rules give targets, never sentences.

## Target buyer persona

**Who buys:** at a chain's head office, the owner of the member app (product or digital head) and the owner of the body assessment and training method (the technical or fitness director: Diretor Técnico, Gerente Técnico Nacional, Director de Fitness), with operations and partnerships heads as route-ins; at a group B platform, the founder, product head or partnerships head who decides what the member app offers gyms. Club managers, franchise owners and staff are referral paths to head office.

- **Why these titles:** the product head owns where a scan step sits in the app and how a new feature is tested on a member cohort; the technical director owns the assessment protocol and what trainers look at before changing a programme (PPL-4: coaching and practitioner leads replied positively); operations heads own how assessments run across clubs; partnerships heads drew the most replies of any function (PPL-3, 6/83).
- **What they care about (KPIs):** members who keep coming and renew; what members see of their progress; uptake of higher membership plans; trainer time per member; app use and rating; for platforms, features their gym clients pay for.
- **Likely objections, with the honest answer:**
  - "We already measure in the club." True, and it stays. The phone scan covers the check-ins between visits, under the chain's brand, with 80+ measurements and a record in the chain's app.
  - "How accurate is it next to our bioimpedance?" No published comparison exists; body composition values are estimates derived from measurements. Replies use `accuracy-formulations.md` §1.1 and §1.2 for body measurements and say the reference-device work is under way, without a date in writing.
  - "Our members won't scan at home." The pilot measures scan completion and retakes against a comparison cohort before any rollout.
  - "Will a scan step hurt onboarding?" The page's own answer: it can; the product team chooses where the scan sits, and the pilot compares onboarding completion with the usual flow.
  - "Price at our scale?" A call question (Open question 2).
  - "Is it in Portuguese or Spanish? Where is the data?" Replies only: language to confirm with product (Open question 13); data questions from `compliance.md` §10 and legal@3dlook.me.
- **Tiers (order only; one import file):** P1 head-office owner of the member app or the assessment with visible scope (Chief Product Officer, Diretor or Head de Produto, Head of Digital, Diretor Técnico, Gerente Técnico Nacional, Head of Fitness, Director de Fitness); at group B, founder, CEO or CPO. P2 chain CEOs, founders, managing directors and country managers (P1 only where the export has no product or technical owner, PPL-1); product managers and owners of the member app; national or regional technical and training coordinators; nutrition programme heads; COO and operations directors; partnerships and business-development heads. P3 CTO, CIO, heads of technology, engineering, data and innovation; customer-experience heads. P4 referral: regional and club managers (at most 10 per company), franchise unit owners, board members, staff below lead level in the functions above.
- **Lanes (exactly one per person):** `product` (product, digital, app, CEO and founder at chains); `training` (technical, fitness, training, assessment, personal-training and nutrition programme heads); `operations` (COO, operations, franchise operations, regional directors); `partnerships` (partnerships, alliances, BD at chains; everyone at group B except technology owners); `technical-integration` (CTO, CIO, technology, engineering, data); `referral` (everyone else at an IN company).
- **Route-in below C-level (PPL-1):** every IN chain gets at least one P2 product, training or operations person when the export has one.
- **Location rule (step 4):** people located in `katya`'s countries only. US-located people FAIL (`nick`; franchisor staff at Planet Fitness and Anytime included); Spain- and Europe-located people FAIL (`olena`); Central America and the Caribbean FAIL (no profile; Smart Fit operates there). Counts reported.
- **Not the buyer (FAIL, or a skipped pool at step 4):** marketing, CRM, growth, social media and brand roles (PPL-3: 0/52 and 0/44); membership sales consultants, receptionists, instructors, professors and individual personal trainers; finance, legal, HR, procurement, expansion and real estate, facilities and maintenance, investor relations; TotalPass and Wellhub staff.

### Target buyer persona: Sales Navigator pull for step 3

**Pull by title filter inside the approved company list, never by company alone and never by seniority alone.**

**Default source (Open question 8): the located Apollo method** of `2026-11-05-latam-insurance-underwriting`: free `apollo-pull.py search` per IN domain through the coordinator's wrapper with `person_locations[]` set to the row's countries in `katya`'s market (Smart Fit: all of them); a free title pre-filter with the exclusions below; rank by tier and keep at most 15 per company (Smart Fit 30); `enrich` only those, with the credit count named to Vadim first. Then a Sales Navigator title pull by Hlib only for companies left with no P1 or P2 owner. **Exclusions for the whole search** (added to the generated `NOT (...)`): `Marketing`, `CRM`, `Growth`, `Social Media`, `Brand`, `Vendas`, `Ventas`, `Sales`, `Consultor`, `Consultora`, `Recepção`, `Recepcionista`, `Recepción`, `Professor`, `Professora`, `Instrutor`, `Instructor`, `Estagiário`, `Intern`, `Financeiro`, `Finanzas`, `Contábil`, `Jurídico`, `Legal`, `RH`, `Recursos Humanos`, `Talent`, `Compras`, `Procurement`, `Expansão`, `Expansión`, `Real Estate`, `Obras`, `Manutenção`, `Mantenimiento`, `Facilities`, `Relações com Investidores`, `Investor Relations`, `TotalPass`. Geography set by hand to `katya`'s countries (`sales-nav-query` writes none). **Volume (estimate):** about 16 IN rows; Smart Fit fills 30 to 50, larger chains 8 to 15, platforms and smaller chains 3 to 8: about 150 to 220 to send.

```titles
Chief Executive Officer
Founder
Co-Founder
Managing Director
Country Manager
Chief Product Officer
Head of Product
Product Manager
Product Owner
Chief Digital Officer
Head of Digital
Chief Operating Officer
Head of Operations
Head of Fitness
Fitness Director
Head of Training
Head of Personal Training
Head of Nutrition
Head of Partnerships
Partnerships
Business Development
Chief Technology Officer
Chief Information Officer
Head of Technology
Head of Data
Head of Innovation
Diretor de Produto
Gerente de Produto
Head de Produto
Diretor Digital
Diretor de Operações
Gerente de Operações
Diretor Técnico
Diretora Técnica
Gerente Técnico
Gerente Técnica
Coordenador Técnico
Coordenadora Técnica
Avaliação Física
Nutrição
Parcerias
Diretor de Tecnologia
Inovação
Director General
Director de Producto
Gerente de Producto
Director Digital
Director de Operaciones
Gerente de Operaciones
Director Técnico
Director de Fitness
Gerente de Fitness
Gerente de Entrenamiento
Jefe de Entrenamiento
Coordinador de Entrenamiento
Alianzas
Director de Tecnología
Innovación
```

## Outreach language

English, every country, by default (Open question 4; the latest Katya campaign, `2026-11-05`, was decided English only by Vadim). Readers are Portuguese- and Spanish-speaking product heads, technical directors and founders reading in a second language: short sentences, plain words, no idioms, American spelling (program, center). Portuguese or Spanish words appear only as proper names: the company, its own app, the person's own title, and "avaliação física" or "evaluación física" where the person's own company uses the term. Never mention a prospect's country regulator or law, never mention one country to a prospect in another, never comment on the prospect's language or nationality. Replies in Portuguese or Spanish are answered by Katya in that language from the approved English facts.

## Message angle: lanes, account facts and the content asset

Every person gets exactly one lane, spelled as above. Lane notes are instructions to the writer; none of their sentences goes into a message.

**The angle, for every lane (a target; each writer finds new words for each person):** the check-in between club visits. The chain measures bodies in the club and shows the result in its app; FitXpress adds a body check-in the member can take on their own phone, inside the chain's app and under its brand, which returns a record the chain and its trainers can use. For group B: the same check-in as a capability the platform offers its gyms inside the member app it already ships.

- **`product`.** Target: where a scan would sit in the member app (joining, the first check-in, a programme block, a higher plan) and what the app shows members about body change between assessments. Question targets: at which point in a member's first months the app asks for a check-in today; what the app shows between in-club assessments; how the app team tests a new feature on one member cohort; whether 3D progress would sit in a higher plan. Message 2 value: white-label SDK and API, consent in the chain's own words, scan ID linked to the member profile, 3D progress and goal visualization for a premium tier, the pilot design.
- **`training`.** Target: what trainers and the technical team see of a member's body change between assessments, and how a record from home would sit next to the in-club assessment. Question targets: how often members repeat the assessment and what triggers a repeat; what the training team looks at before changing a member's programme; whether a check-in from home between assessments would be useful to trainers; how assessment results reach the member's app. Message 2 value: the measurements named (waist, hip, chest, thigh, calf), body composition estimates, the repeatability sentence, trainers reviewing the same record before the next block.
- **`operations`.** Target: a check-in that needs no device, no trainer slot and no club visit. Question targets: how assessments are scheduled across clubs; what a member check-in that runs outside the club would change for club teams. Never say or imply that clubs run short of devices or staff. Message 2 value: no hardware to ship or install, under 45 seconds from the photos to structured results, the pilot in one club or cohort first.
- **`partnerships`.** Chains: whether a body-scan capability from a partner has a place in what the chain offers members. Group B: whether a scan in the member app has a place in what the platform offers its gyms, and how third-party capabilities enter its app. Message 2 value: one SDK integration, white-label, the platform decides where it appears, a structured record through the API.
- **`technical-integration`.** Target: SDK and API integration, technical tone. Question targets: how a third-party SDK enters the member app; how a structured record would reach the member profile; how a new data vendor is reviewed. Message 2 value: web and mobile SDKs with supported iOS and Android integrations, the recommended SDK-plus-API setup (pose and framing validation runs in the SDK's capture layer), processing status and timestamps in the API response, one or two data-handling sentences (Rules).
- **`referral`.** Message 1: the company line, a short pain and fix, then one question about the person's own work (their club, region or function). Message 2: a value line that continues their question, the call offer with the calendar link, and an easy out that points to whoever owns the member app or the assessment protocol at head office, worded fresh each time.

**Question bank discipline.** Each person gets one question nobody else at the company gets, built from their title. One topic serves at most about a fifth of a company's people. Wording, hook, structure, easy-out target and closer never repeat at one company.

### Account facts

Placeholder until step 2. Before step 5 a separate fresh round fills it: one bullet per group with people to send, `- **Group:** facts with dates and URLs. Use: … Never: …`, built from `companies.md` and a web re-check that every P1 is still in post. It records for each chain whether the member app is its own, a gym-software vendor's or an overseas franchisor's (Rules, Whose app), which assessment the chain publishes, and the name forms Message 1 may use. `card --for messages` does not build while this is a placeholder.

### Content asset in Message 2

At most one 3DLOOK link next to the calendar link (default of Open question 3): the page https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/ in any lane, or in `technical-integration` the privacy FAQ https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/ instead. Optional per person: at one company no more than about half of the Message 2s carry it, and the sentence around it differs. The page is written for fitness apps, in US English, priced in dollars and cites app benchmarks; never describe it as written for gyms or for the reader's country.

## Rules for steps 3-5

- **Sender and format.** Kateryna, English (Outreach language), `Kateryna` alone on the last line, first names only. Connection request with no note. Each message at most 900 characters, links included (frontmatter `message_max_chars: 900`; Open question 5). Register: peer to a head-office product, technical or operations lead; short sentences for second-language readers; no enthusiasm words.
- **Message 1 (Vadim 2026-10-07 and 2026-11-18).** Four parts: a company line from Account facts; the pain, about the METHOD; how FitXpress fixes it, as mechanism and what the chain gets; then ONE question, the message's only "?". No call ask and no link of any kind. The order of the parts and their wording differ between people at one company.
- **The pain is about the method, never the company, its staff, trainers, devices or members.** Targets: an assessment taken on a device in the club needs the member in the club and a trainer free, so it repeats only when the member comes in; between assessments the app can show classes, workouts and access, and has nothing on body change; a weight entry or a progress photo gives no measurements to compare. Never say or imply that the chain measures badly, that its device or trainers fall short, or that its members quit, struggle or fail. No churn, drop-out or retention talk in Message 1 (HYP-6).
- **The fix, from the live page (pick three to five parts the lane cares about; never a one-clause scan and never "two photos" alone).** The member takes 2 photos on their own phone inside the chain's app, with no hardware and no club visit; the app shows the chain's brand and its own consent wording (white-label); Real-Time Pose Validation (RTPV) guides pose and framing during capture; under 45 seconds from the photos to structured results; 80+ body measurements, including waist, hip, chest, thigh and calf, and body composition estimates (body-fat %, lean mass, fat mass), with BMI and BMR as calculated metrics; one timestamped record per scan returned through the API and linked by scan ID to the member profile; trainers review the same record before setting the next block; 3D progress tracking and goal visualization a chain can place in a premium tier; the in-club assessment stays for members who visit, and the phone scan covers the check-ins between visits. Which parts appear, in what order and in what words varies between people at one company.
- **Message 2.** Not a repeat and not a "following up": one or two value points Message 1 did not use, the boundary line, optionally the page link (Content asset), optionally the pilot design (next rule), an easy out where the person is not the owner, then a call offer with https://meetings.hubspot.com/kateryna-boichuk as plain text on the last line before the signature. Every lane, referral included. No call length or minutes. At most one question.
- **Pilot design in Message 2 (HYP-6 test, whole design, one target).** At most about half of the Message 2s at one company offer it; the others use a different value point, so replies can be read both ways. When offered, name all parts. **Who scans:** one cohort of members (new members, or one club or one plan) scans at onboarding and at the first check-in; a comparable cohort keeps the usual flow, with the in-club assessment as it runs today; members are assigned randomly before the pilot where practical. **What is counted:** scan completion and retake rates; repeat scans at the first check-in; onboarding completion against the usual flow; day-30 and day-90 retention against the comparison cohort; upgrades to the plan where 3D progress sits, where the chain puts it in a higher plan. **How it is judged:** against criteria agreed before the pilot; if they are met, the scan goes live for all members on the matching plan. **What it does not touch:** the in-club assessment, trainers' decisions and any member who does not scan. Never promise or predict a retention effect, never cite the page's app statistics (the day-1 and day-30 activity figures or the 100-day quit figure), and never use the pilot as the opener.
- **What it is not.** FitXpress does not diagnose, give medical or nutrition advice, or set a training programme; trainers and the chain do. It does not replace the in-club assessment, a trainer or a nutrition consultation. It is never mandatory or hidden: the chain decides where the scan sits and keeps its usual route for members who do not scan. 3DLOOK does not track members: the chain's app shows the comparisons the chain chooses.
- **Members are never the problem.** No body image: no weight-loss, fat-loss or appearance promise, no before-and-after, no "transformation", no shape talk. Write about body measurements and body composition estimates. The scan is for adults; never children or teens.
- **What the scan adds to the device in the club (MSG-4).** At most one sentence per pair: the phone scan covers the check-ins between visits, at home, under the chain's brand, with 80+ measurements and a record in the chain's app. Never name the chain's device, its maker or its service name; never compare FitXpress with bioimpedance or say either is more or less exact; never suggest the chain's data is wrong.
- **Numbers only from this list:** two photos (front and side), with "2 photos" as the numeric form; "under 45 seconds from the photos to structured results" (the only speed wording, as its own plain sentence, at most once per pair); "80+ body measurements"; "3DLOOK has worked with 100+ clients" (the page's "including fitness teams" may follow); "112,100 scans in 2025 across all 3DLOOK customers" as its own sentence, never tied to fitness, a country or a client; "day-30 and day-90" inside the pilot design. No accuracy percentage or error figure anywhere. Repeatability only as the page's sentence, in Message 2, at most once per pair, whole or cut after "measurements": "Repeated scans typically differ by less than 1 cm for most evaluated measurements, making it possible to track changes against each member's previous scans." No market, churn, survey or prospect figures (clubs, members, revenue, openings), and none of the page's statistics.
- **Not in copy (`roadmap.md`).** Voice prompts or voice guidance (the page mentions them; native SDKs are in testing); Clothing Detector; liveness or anti-fraud; any promise about every Android device; Portuguese or Spanish capture screens (unconfirmed, Open question 13); any weight-accuracy figure; the body-composition reference study.
- **Proof without names.** No 3DLOOK client is named and no chain or platform is implied to use FitXpress. The proof lines are "3DLOOK has worked with 100+ clients" and the 112,100-scan sentence. The page's production line (weight-management and BMI-verification workflows) stays out: it reads clinical to a gym reader, and "verification" is banned.
- **Pricing (default of Open question 2).** No prices, plan prices, request counts or plan names with prices. "No integration fee" may appear once per pair, Message 2 only. Never "free trial" or trial terms; price questions go to the call.
- **Boundary line: exactly one per pair, in Message 2, every lane, verbatim from the page:** "FitXpress is not a medical device. It provides structured body data for coaching and program workflows." (the first sentence may stand alone; Open question 6). No law, regulator, certification or hosting place in cold copy; never "compliant" or "certified".
- **Data-handling sentences (`technical-integration` Message 2 only, one or two, verbatim from the page):** "Photos are deleted after processing or retained for up to 30 days under the customer's policy, with blurring and face obfuscation." · "Data is encrypted both during transmission and while stored, helping protect member information throughout processing and storage." · "Production customer data is not used for model training unless the customer provides explicit, documented authorization for that purpose." Never "anonymous", "not stored" or "no personal data"; never where the data is hosted; never that it stays in the country or only with the chain.
- **Whose app.** Where Account facts say the member app is published by a gym-software vendor or an overseas franchisor, never write "your app" and never name the app: write about the chain's members and clubs and "the app members use". Never name a gym-software vendor in a chain's copy.
- **Several people at one company.** Name the company in every Message 1, in a form Account facts allow. No two people at one company share an opener, a company line, a central question, a Message 2 value point, an easy-out target or a closer. Never mention colleagues, other teams or a conversation that did not happen.
- **Never name one prospect in another prospect's copy,** nor a company's parent, owner, aggregator partner, sister brand or supplier (TotalPass, Wellhub, FitMass and gym-software vendors included). No rankings or market positions ("largest", "leading"), no deals, no complaints. A company's own brands and apps may be named in its own copy only.
- **Former employers** may be named (standing decision) unless they are an account here, a competitor or a banned term.
- **Easy out (a target, not a sentence).** Every referral Message 2, and any Message 2 to someone who is not the owner, points to a named function at the person's company: whoever owns the member app at head office, or whoever owns the physical-assessment protocol. Worded fresh for each person.
- **Word traps.** No em or en dash; no "plus" as a connector; no "so" introducing a benefit; no corrective "X, not Y"; none of the hard-bans-card buzzwords; no "Circling back", "Following up" or "Saw your post".
- **Writer notes and card instructions are not copy.** Lane notes, targets and rule sentences are never pasted; the quoted lines above are the only verbatim copy.
- **Message 1 gate.** Every message 1 carries at least one product specific from `proof-points.md` and one line that could only have been written to that company; each pair of messages cites at least one number. The gate recognises "two photos", "2 photos", "body measurements", "API" and "SDK" as product specifics, and "under 45", "2 photos", "80+" and "112,100 scans" as numbers. Referral people included. The strict gate applies by date.

## Anti-cases (where it does NOT work)

- **Gym aggregators and corporate fitness networks** (Wellhub, TotalPass, Fitpass): their check-in is a visit to a partner gym, and they own no member assessment.
- **Independent single gyms and studios:** reached through group B, never one by one.
- **Chains with no member app in their own name and no gym-software app**, or whose app only books classes and opens turnstiles with no programme, training plan or assessment: nowhere for the record to land. Held for Vadim if the chain is large.
- **Chains in contraction:** closures or a restructuring reported in the last 12 months (Energy Pacific, June 2026, by default).
- **Recent deals within about 12 months** (`icp-detail.md` universal exclusion): a chain bought or merged is OUT and never mentioned; a chain that bought others stays IN, the deal never mentioned.
- **Weight-loss, aesthetic and body-treatment clinics and franchises, longevity clinics and corporate health providers:** Katya's 2026-10-05 and 2026-10-19 segments, different use cases.
- **Individual-trainer tools and marketplaces:** single-trainer deals where price-led rivals win (`competitors.md`).
- **Any chain or platform whose app already runs a phone-based body scan:** held for Vadim (none found on 2026-11-19).
- **Entities and people outside `katya`'s countries:** US franchisor offices, Spain and Europe, Central America and the Caribbean.
- **Children's and teen programmes, pregnancy and postnatal programmes, rehabilitation and physiotherapy services.**

## Learnings applied

- **HYP-2:** baseline for `katya`: accepted 94/254 (37.0%), replied 9/94 (9.6%), positive 5/94 (5.3%). Targets below come from it, not from the pooled figures or the digital-fitness segment (99/491 accepted, 14/99 replied).
- **HYP-1:** reply rate is flat (pooled 113/884 replied per accepted); the new page and angle do not raise the reply target.
- **HYP-5:** LatAm accepts most and replies least (56/127 and 28/47 accepted, 5/56 replied). Planned for: Message 1 carries the campaign (MSG-1); the list aims at 150 to 220 invites for 3 positives.
- **HYP-4:** the segment is Vadim's direction (the new page), not chosen on past reply rates.
- **Departure from HYP-6 (marked TEST):** the `retention` lane drew 0/53. There is no `retention` lane and no retention pain in Message 1; retention appears only as a measured outcome of the pilot design, in at most about half of each company's Message 2s, and the read-out compares replies with and without it (Success metrics).
- **HYP-7:** the sender's profile decides acceptance; Katya's headline is checked before import (Open question 14).
- **HYP-3:** does not apply (Australia).
- **PPL-1:** chain CEOs and founders are P2 by default, P1 only where no product or technical owner is in the export; every IN chain gets a P2 route-in below C-level.
- **PPL-2:** club managers, franchise owners and staff in relevant functions are `referral` PASS (club managers capped at 10 per company).
- **PPL-3:** marketing, CRM and growth stay out of the pull; engineering only as P3 `technical-integration`; partnerships and BD get their own lane. **Departure:** membership sales roles stay out although sales replied well elsewhere: at a gym chain they sell memberships at the desk and do not own the app or the assessment.
- **PPL-4:** technical and training directors, the gym-world counterpart of the coaching and practitioner leads who replied positively, are P1 in the `training` lane.
- **PPL-5 [watch]:** not acted on.
- **MSG-1:** the strongest product specifics and a number go in Message 1 (Rules, the fix).
- **MSG-2 [watch]:** the Message 2 call ask stays.
- **MSG-3:** no trimming for its own sake; the 900-character ceiling is Vadim's call (Open question 5).
- **MSG-4:** one sentence on what the phone adds to the in-club device, never naming it (Rules).
- **MSG-5 [watch]:** the 2-pager only in replies.
- **MSG-6:** compliance and platform questions answered from `compliance.md` §9-§10; Latin American legal questions to legal@3dlook.me.
- **MSG-7:** every Message 1 carries a company line from Account facts.

## Vadim's standing decisions (already applied above)

1. **`cap_per_group: 50` for every campaign, one import file, no waves** (2026-09-29).
2. **A lane for every function at an IN company** (2026-09-29); FAIL only for the wrong company, people who left, identity collisions, duplicates and this campaign's location and function rules.
3. **Former employers may be named; live 3DLOOK pages may be linked as they are** (2026-09-29).
4. **No 3DLOOK client is named;** "3DLOOK has worked with 100+ clients" and 112,100 scans as 3DLOOK-wide scale (2026-09-29, 2026-09-30).
5. **Message 1 asks, Message 2 calls** (2026-10-07), every lane, referral included (`referral_call: yes`).
6. **Message 1 explains the pain and how FitXpress solves it** (2026-11-18): the method's problem, then mechanism and what the buyer gets; never a rule that shrinks the product to one clause. Caps may be raised per campaign (`message_max_chars`).
7. **Companies without a contract may be re-contacted, with their history shown** (2026-11-17); only customers with a contract stay out.
8. **Katya's Latin America defaults** (2026-10-05, 2026-10-19, 2026-11-05): never mention a prospect's country regulator or law; never mention one country to a prospect in another; English cold copy (decided for 2026-11-05; Open question 4 here).

## Vadim's decisions 2026-11-19 (hypothesis checkpoint)

Recorded by the coordinator from Vadim's answers at the hypothesis checkpoint (AskUserQuestion, 2026-11-19).

- **People: only new people** («Ні, тільки нові люди»). Anyone this profile already messaged stays excluded, whatever the campaign. Companies without a contract may return with their history shown; customers never (Erakulis added to the registry as a customer 2026-11-19).
- **Process:** Vadim's checkpoints are this hypothesis and the messages. The people list goes through validation and opus QC without stopping for him. People come from Apollo first; Hlib's Sales Navigator pull is added when it arrives.
- **Prices:** no dollar figures in copy. "No integration fee" may appear once, in Message 2 only.
- **Page link:** the page URL https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/ may appear in Message 2 for about half of each company's people, never in Message 1; the closing line stays last.
- **Length:** `message_max_chars: 900/700` (Message 1 / Message 2).
- **Segment approved as written** («Як запропонували»): gym and fitness-club chains in South America and Mexico with their own member app and a body assessment, plus gym-software platforms.
- **Capture language:** Vadim confirms the FitXpress capture screens exist in Portuguese and Spanish («Так, є PT/ES»). The go/no-go on localization is closed; copy still does not mention languages, Katya answers if asked.

## Validation criteria (Step 2 will check)

- **Companies.** 24 named rows; target 12 to 20 IN. Fewer than 10: stop and report to Vadim; never widen on your own. Each chain: head office in `katya`'s countries; about 20+ clubs or published US$1M+ revenue in 2025-2026; a member app in the brand's name on the App Store or Google Play in the row's country (record the publisher: own, gym-software vendor or overseas franchisor, and the first-release date); and a published body assessment, body-composition service or in-app training plan or coaching (site, app listing, contract or 2025-2026 press). Each group B platform: a member app that shows gyms' assessments or training plans, gym clients in `katya`'s countries, US$1M+ revenue or a published client count.
- **Schema.** `hq_country` is Brazil, Mexico, Colombia, Argentina (or the added row's country); never "Latin America", "LatAm" or "Americas". Row names: `Bodytech Brasil` and `Bodytech Colombia` (never a bare `Bodytech`); `Planet Fitness México`, `Anytime Fitness México`, `Energy Fitness México` (country suffix keeps them apart from `vadim`'s Australian rows); `Smart Fit` covers Bio Ritmo, and a `TotalPass` cell FAILs.
- **Registry.** `outbound-registry.py check --profile katya` after extract; expected hits: none (dry run 2026-11-19 on 46 names). Then compare every person URL with the other four registries.
- **Recent deals and contraction.** For every IN company, a search of November 2025 to November 2026 for a sale, merger, change of control, closures or restructuring: a bought or merged company is OUT and never mentioned; closures are reported to Vadim.
- **Displacement.** For every IN company, a search of its app listing and site for a phone-based body scan or a third-party body-scan partner; any hit is held for Vadim. In-club devices are not displacement.
- **People.** Location and function rules as in Target buyer persona; credit count to Vadim before `enrich`.
- **C-level availability.** Chain founders, product and technical directors are on LinkedIn, mostly with Portuguese or Spanish titles. A chain with no P1 or P2 owner after Apollo goes to Hlib's Sales Navigator gap pull.
- **Proof in product-info.** Use-case file (`fx-digital-fitness`) and the live page: yes. Gym-chain or Latin American customer: none.
- **Message 1 gate.** As in Rules; zero client names, banned terms, links in Message 1, accuracy figures, retention talk in Message 1 or decision claims; exactly one boundary line per pair, in Message 2.

## Success metrics for this campaign

Denominators are Closely's invite and acceptance counters, never import rows. Baselines: learnings HYP-2 and HYP-5 (`katya`).

| Metric | Target | Floor | Basis |
|---|---|---|---|
| Invites sent | 150-220 | 100 | about 16 IN; Smart Fit 30-50, others 3-15 |
| Connection acceptance (accepted / invites) | 37% (about 67/180) | 25% | `katya` 94/254 (37.0%); her LatAm lists 56/127 and 28/47 |
| Replies per accepted | 9.6% | 5% | `katya` 9/94; LatAm 5/56; pooled 113/884 |
| Positive replies per accepted | 5.3% | 2.5% | `katya` 5/94 |
| Positive replies (interest or a question) | 3 | 1 | about 180 × 37% × 5.3% ≈ 3.5 |
| Companies with at least one reply | 4 of about 16 IN | 2 | about 67 accepted × 9.6% ≈ 6 replies |
| Discovery calls | 1 | none set | |
| Pilot conversations (chain or platform) | 1 | 0 | the page's pilot step |

**HYP-6 test read-out:** replies to pairs whose Message 2 carried the pilot design (detected by "day-90") against pairs whose Message 2 did not, with denominators; directional only below 15 replies. **Falsified if** three or more P1 or P2 replies say a body check-in between club visits has no place in their member app, that members will not scan on their phone, that the in-club assessment already covers it, or that the chain owns no app it can change. **A language signal, not a falsification,** if two or more replies say English was the obstacle. **Inconclusive** if fewer than 25 people accept. Results are read by group (chains, platforms) and by country.

## Risks

1. **English to second-language readers.** Technical and training directors (physical-education professionals) may read English less often than product heads; the `training` lane is the most exposed (Open question 4).
2. **Whose app it is.** Many chains' apps are built and published by gym-software vendors or overseas franchisors; a chain may not control the SDK. Account facts record the publisher; group B covers the vendor route.
3. **The in-club device as the answer.** Chains with bioimpedance services (Smart Fit, Bluefit) may see no gap. The page's line on check-ins between visits is the answer; the device is never criticised.
4. **Body composition proof.** No published comparison with bioimpedance or any reference method; a technical director may ask first. Replies say so plainly.
5. **Population fit.** Validation participants from the US and Europe; Latin American populations not characterized separately.
6. **Language of the capture screens.** The fixed capture layer may not yet run in Portuguese or Spanish (`roadmap.md`: localization planned Q4 2026). A chain cannot ship an English-only capture to members (Open question 13).
7. **Price at chain scale.** Per-request plans meet member bases in the millions; the pilot cohort fits a small plan, rollout needs a custom plan (Open question 2).
8. **Data location and law.** FitXpress data is hosted on AWS in the US; body composition may count as sensitive data under Brazilian and Mexican law. Never in copy; replies go to legal@3dlook.me.
9. **The retention test may repeat HYP-6.** Retention stays out of Message 1 and out of half the Message 2s.
10. **Sibling campaigns.** Franchisor head offices (Planet Fitness, Anytime Fitness) may hear from `nick` in the same weeks; copy never refers to it.
11. **Stale or narrow pulls.** Smart Fit's LinkedIn page lists thousands of club staff; the title filter and exclusions keep the pull to head office.

## Open questions for Vadim

1. **The cut.** Gym chains with a member app and an assessment (19 rows in Brazil, Mexico, Colombia and Argentina) plus 5 gym-software and assessment platforms; 24 named, about 16 IN expected; step 2 may add same-definition chains in Chile, Peru, Colombia and Mexico. **Recommendation: yes.** Reserve (Befit, Just Fit, Cia Athletica, Academia Corpo e Saúde, Fitco) only on your word. Alternative: chains only, no group B.
2. **Pricing in copy.** The page shows "plans from $1,000 a month" and "No integration fee". **Recommendation:** no dollar figures in cold copy (US-dollar entry plans read oddly to chains with millions of members, and price talk belongs on the call); "No integration fee" allowed once per pair in Message 2. Applied in Rules as the default. Alternative: the page's "plans from $1,000 a month" once in Message 2.
3. **Page URL in Message 2.** **Recommendation:** yes, optional, in at most about half of each company's Message 2s, plain text, never in Message 1, never described as written for gyms or for their country (the page is app-framed and US-English). Applied as the default.
4. **Language.** **Recommendation:** English, as you decided for the 2026-11-05 LatAm campaign: gates, bans and approved wording exist only in English, and three of the first four 2026-10-05 replies came in English. Risk 1 applies most to the `training` lane. Alternative: Portuguese for Brazil-located and Spanish for Spanish-speaking readers (needs translated bans and a manual gate).
5. **The 900-character cap** (both messages, as set in the frontmatter). **Recommendation:** keep 900 as a ceiling, aiming Message 1 at about 600 to 850 so the pain and the fix fit (your 2026-11-18 call), with short sentences for second-language readers; MSG-3 finds no length effect within the limits. Alternative: 900/700.
6. **Boundary line.** Your 2026-11-19 direction keeps "FitXpress is not a medical device." Katya's 2026-11-05 LatAm campaign dropped that clause because its basis is the UK MDR and EU MDR assessment, with nothing under Brazilian or Mexican rules. **Recommendation:** keep the page's own sentence, verbatim, once per pair in Message 2 ("FitXpress is not a medical device. It provides structured body data for coaching and program workflows."): it sets the coaching boundary for a fitness reader and names no law. Alternative: drop it, as on 2026-10-05.
7. **Retention test (HYP-6).** **Recommendation:** the pilot design in at most about half of each company's Message 2s, never in Message 1, read out separately. Alternative: no retention anywhere in copy.
8. **People source.** **Recommendation:** the located Apollo method first (free search with `person_locations[]`, title pre-filter, at most 15 per company and 30 at Smart Fit, credit count to you before `enrich`, about 150 to 250 credits), Hlib's Sales Navigator title pull only for gaps. Alternative: Sales Navigator first.
9. **Wellhub.** HQ New York (`nick`'s market), about 65% of staff in South America. **Recommendation:** OUT here (aggregator, Anti-cases; avoids a collision with `nick`). Alternative: a Brazil-only Wellhub row on `katya` if `nick` does not take it.
10. **Energy Pacific (Chile).** Club closures reported in June 2026. **Recommendation:** OUT. Alternative: to confirm at step 2.
11. **Franchise rows whose app belongs to a US franchisor** (Planet Fitness México, Anytime Fitness México). **Recommendation:** IN with Mexico-located people only and the "Whose app" rule. Alternative: OUT.
12. **Group B platforms.** **Recommendation:** IN, lane `partnerships`, with FitMass never named in Bluefit's copy and no vendor named in any chain's copy. Alternative: OUT.
13. **Capture-screen language (for product, not copy).** Can the FitXpress SDK capture layer run in Portuguese and Spanish today? `roadmap.md` lists localization as planned for Q4 2026 (written for Mobile Tailor and measurement guides). **Recommendation:** ask product before step 5; copy never claims it either way, and replies give product's answer.
14. **Katya's profile (HYP-7).** **Recommendation:** before import, confirm it shows 3DLOOK as current employer and a headline naming a buyer's problem; no fitness-specific rewrite.
15. **Re-contact.** None of Katya's past accounts fits this cut (list at the top). **Recommendation:** none added. Name any you want back.
16. **Voice prompts.** The live page says the capture has "voice prompts for a member scanning alone"; `roadmap.md` says native voice guidance is in testing (web ready). **Recommendation:** leave voice out of copy (applied), and tell whoever owns the page that a native-app reader may take it as live.

## Coordinator notes (outside every card)

- **Relabels before `extract-people`:** bare `Bodytech` cells to `Bodytech Brasil` or `Bodytech Colombia` by location (Brazil-located to Brasil; Colombia-, Chile- and Peru-located to Colombia); `Bio Ritmo` cells to `Smart Fit`; `Sportlife` (Chile) and `Athletic` cells to `Bodytech Colombia`; `TotalPass` cells FAIL.
- **`hq_country`** is the row's country, never "Latin America" or "Americas" (`geo_profile()` substring "america" routes to `nick`).
- **Banned names that may be former employers** (TotalPass, Wellhub, Gympass, Face Doctor, any competitor): drop them from that person's copy; do not waive the ban.
- **Pricing:** `check-messages` hard-fails any currency sign followed by a digit (`PRICE_HARD`) and notes "price", "pricing" and "tier" (`PRICE_SOFT`), so dollar figures need no campaign ban. If Vadim picks the alternative in Open question 2, the page's phrase will still hard-fail: the coordinator records the waiver in this file and accepts those hits by hand. "Premium tier" from the page draws a soft note, not a failure.
- **Boundary line:** if Vadim drops it (Open question 6), take the boundary-line rule out of Rules; `medical device` is not banned now.
- **Strict gate** applies by date (created 2026-11-19).

## Sources

Read 2026-11-19 through web search unless marked opened; context for reviewers, never linked in messages.

- Live page capture: `workspace/pages/for-connected-and-digital-fitness/published-live-2026-11-19.md`
- Smart Fit, 2,170 gyms and 5.6 million members by June 2026; TotalPass in "Other" revenue: https://investidor10.com.br/noticias/smart-fit-smft3-lucra-r-204-milhoes-no-2-trimestre-de-2026-alta-de-8-121889/ and https://www.analisedeacoes.com/noticias/smartfit-smft3-registra-lucro-liquido-recorrente-de-248-milhoes-no-3-trimestre-de-2026-alta-de-40/
- Smart Fit Q3 2026 and 2026 openings: https://mercadoeconsumo.com.br/05/11/2026/noticias/smart-fit-tem-lucro-de-r-248-mi-no-3o-trimestre-alta-de-40/ ; https://mercadoeconsumo.com.br/11/03/2026/franquias/smartfit-preve-aberturas-liquidas-de-330-a-350-academias-em-2026/amp/
- Bio Ritmo App: https://apps.apple.com/us/app/-/id1515318103 ; Smart Fit Nutri: https://apps.apple.com/app/id1442126612 ; BlueUp (Bluefit with FitMass): https://apps.apple.com/br/app/blueup/id6448286019 ; Academia 360 Club (EVO): https://apps.apple.com/us/app/id1547688018
- Smart Fit Colombia contract (bioimpedance tests): https://www.smartfit.com.co/files/store/85d02bce004552223503da511a944011a6ed93ce340792044670b675bb85.pdf
- Tecnofit student app and physical assessments: https://ajuda.tecnofit.com.br/pt-BR/support/solutions/articles/67000669802-como-verificar-as-minhas-avaliac%C3%B5es-f%C3%ADsicas-no-aplicativo-tecnofit-box- ; https://apps.apple.com/app/id1109478634
- Brazilian chain rankings (Skyfit, Panobianco, Selfit, Bluefit, Gaviões 24h): https://maquinadoesporte.com.br/?p=239316 ; https://www.bloomberglinea.com.br/negocios/panobianco-supera-smart-fit-em-novas-academias-e-avanca-em-cidades-menores-diz-citi/ ; https://trademap.com.br/noticias/news-8279195
- Retention in Brazilian gyms, ACAD Brasil drop-out, Panorama Setorial 2025 centre count: https://www.em.com.br/networking-e-negocios/2026/07/7469486-retencao-de-alunos-vira-novo-campo-de-batalha-das-academias-no-brasil.html
- Selfit and Face Doctor founder: https://timesbrasil.com.br/empresas-e-negocios/brasil-ainda-usa-pouco-academias-e-mercado-wellness-tem-amplo-espaco-para-crescer-diz-fundador-da-face-doctor-e-selfit/
- Befit revenue and users: https://www.opovo.com.br/noticias/tecnologia/opovotecnologia/2026/05/05/amp/criado-por-cearense-app-de-fitness-e-um-dos-que-mais-cresceu-no-mundo.html
- Sports World app and January 2026 terms: https://apps.apple.com/MX/app/id610768211 ; https://sportsworld.com.mx/uploads/documentos_generales/descargas/deportiva-enero-2026-02.pdf
- UFC GYM MX app: https://apps.apple.com/es/app/ufc-gym-mx/id6744074860
- Smart Fit Mexico: https://expansion.mx/empresas/2026/01/06/quien-es-el-dueno-de-smart-fit ; https://emprendedor.com/smart-fit-acelera-su-expansion-en-mexico-invertira-mas-de-1500-mdp-y-abrira-70-gimnasios/
- Planet Fitness México: https://www.elfinanciero.com.mx/mundo-empresa/2026/09/17/planet-fitness-llega-a-50-clubes-en-mexico/ ; https://forbes.com.mx/?p=1432365
- Bodytech Colombia: https://www.portafolio.co/negocios/empresas/esto-le-cuesta-el-alza-del-minimo-a-bodytech-que-aspira-al-medio-billon-de-pesos-en-ingresos-y-lanza-marketplace-486726 ; https://lanotaeconomica.com.co/movidas-empresarial/transformacion-digital-impulsa-la-reactivacion-de-los-centros-deportivos-en-colombia/ ; https://www.forbesargentina.com/negocios/gimnasios-expansion-grandes-cadenas-regionales-eligen-argentina-como-operan-marcas-locales-exterior-n100762
- Argentina market, Megatlon, SportClub, Pratique: https://www.iprofesional.com/negocios/459456-cadena-de-gimnasios-brasilena-llega-a-argentina-para-competir-con-megatlon-y-sportclub ; https://apps.apple.com/uy/app/megatlon/id1531151799 ; https://www.cronista.com/informacion-gral/experiencia-digital-a-otro-nivel-la-nueva-actualizacion-de-la-app-sportclub
- Energy Pacific closures: https://www.theclinic.cl/2026/06/13/por-que-algunos-gimnasios-se-quedaron-sin-musculo-el-dilema-que-desato-en-la-industria-los-cierres-de-energy-pacific-y-cardiopilates/
- Displacement check (in-club scanners, no phone scan found): https://www.cartacapital.com.br/?p=599783 ; https://visbody.com/es/fitness-sports ; Brazilian dissertation on 3D scanning against BIA: https://repositorio.ufms.br/jspui/retrieve/161e8570-2f6e-4194-81e1-0341fc30eef1/Defesa%20de%20Disserta%c3%a7%c3%a3o%20%282%29.pdf
- Wellhub HQ and staff split: https://www.reveliolabs.com/companies/wellhub/employees ; https://builtin.com/company/wellhub/faq/work-life-balance-wellbeing
