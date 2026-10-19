---
product: fitxpress
profile: katya
market: South America + Mexico
created: 2026-10-19
status: approved
approved: 2026-10-19
inspiration: everlab.com.au (vadim target in 2026-08-14-au-digital-fitness, never a target here); template 2026-10-19-eu-everlab-similar
use_case: fx-telehealth-weight-loss
cap_per_group: 50
referral_call: yes
banned_terms: [Everlab, Clinique La Prairie, La Prairie, Sensorial, OrienteMe, Neko, Superpower, Function Health, Prenuvo, Biograph, Axo, Prism, InBody, Tanita, Withings, Seca, Technogym, Evolt, Styku, Fit3D, Oura, Whoop, Apple, Garmin, Dexcom, FreeStyle Libre, Abbott, Dasa, Sabin, Hermes Pardini, Multilab, Einstein, Sírio-Libanês, Colsanitas, Chopo, Salud Digna, Médica Sur, HIPAA, GDPR, LGPD, LFPDPPP, COFEPRIS, SOC 2, FDA, ANVISA, ANS, CFM, SUS, MDR, CE mark, medical device, compliant, certified, certification, accredited, clinically validated, clinically proven, peer-reviewed, reimbursed, reimbursement, verify, verified, verification, eligibility, eligible, Smart Scales, mismatch, fraud, self-reported, guesswork, unreliable, inaccurate, error-prone, tape measure, DEXA, DXA, MRI, BIA, bioimpedance, bioimpedância, bioimpedancia, visceral, waist-to-height, Lancet, obesity, obese, overweight, weight loss, weight-loss, GLP-1, Ozempic, Wegovy, Mounjaro, semaglutide, semaglutida, tirzepatide, tirzepatida, biological age, anti-aging, anti-ageing, reverse aging, live longer, early detection, diagnose, diagnosis, risk score, before and after, before-and-after, guarantee, guaranteed, ROI, funding, investors, investor, valuation, seed round, Series A, Series B, Series C, IPO, acquisition, acquired, merger, generic figure, never a promise, not a promise, context only, writer note, Circling back, Following up, Saw your post, Israel]
---

# Outbound Hypothesis: 2026-10-19, South American and Mexican preventive-health and longevity programmes (Everlab look-alike, Katya)

- **Campaign:** `2026-10-19-latam-everlab-similar`. Sender: Kateryna (Katya) Boichuk, profile `katya`, market South America and Mexico. Geo = the South American countries in `PROFILE_GEO["katya"]` (`scripts/outbound-pipeline.py`): Brazil, Argentina, Chile, Colombia, Peru, Ecuador, Bolivia, Uruguay, Paraguay, Venezuela; and Mexico, for this campaign only, which the tuple does not list (Vadim's decisions (2), 1). The same tuple still lists Israel and the Gulf from her previous market; they are not this campaign's market. `Kateryna` alone on the last line of every message (`OWNER["katya"]`); calendar link https://meetings.hubspot.com/kateryna-boichuk.
- **Template:** `2026-10-19-eu-everlab-similar/hypothesis.md` (approved 2026-10-19). Same vertical, segments, feature screen, persona, lanes, anti-cases, rules and validation criteria, re-grounded for South America and Mexico. None of its European evidence, examples or company names carries over.
- **Seed account: Everlab** (everlab.com.au, Melbourne). Preventive health and longevity membership: 100+ biomarker blood panels, imaging and body-composition assessments, clinician messaging, a year-round programme in an app, consumer plans and corporate executive health (notes: `2026-08-14-au-digital-fitness/companies.md`, "### 03. Everlab"). **Everlab is not a 3DLOOK client.** It is a `vadim` target in that AU campaign: the pattern this campaign clones, never a target here, never named in copy (`banned_terms`).
- **Registry, checked 2026-10-19** (`outbound-registry.py status`, every `exclusions/*.json`, a case-insensitive search for each lead named below): no South American preventive-health or longevity company is covered by any profile. `katya-registry.json` holds 38 South American company keys from `2026-10-05-latam-health-weightloss` (weight loss, corporate health, telehealth, aesthetics, partnership asks); the nearest to this thesis are GnTech (personalised health and genetics), N2B Brasil (body-composition exams) and Sensorial (health and cognitive performance; its CEO has an open question thread). **Step 2 excludes every one of them through the registry.** Axo Longevity also operates in Peru but sits on `olena`'s 2026-10-19 list (one company, one profile). Name collision: the `holi` key (`olena`, 2026-07-21) is a different company from Holi 4 Life (São Paulo); match on website and LinkedIn URL, never the name. Mexico (added by Vadim's decisions (2)): a case-insensitive search of every `exclusions/*.json` for Mexico, México, Previva, Lonvida and Koltin returned nothing on 2026-10-19; step 2 still checks each Mexican candidate by website and LinkedIn URL.

## Vadim's decisions 2026-10-19

Vadim's brief, verbatim: «а запусти таку ж гіпотезу на латам на акаунт Каті бойчук».

1. **The same hypothesis as `2026-10-19-eu-everlab-similar`:** Everlab look-alikes (preventive, longevity and membership health-check companies with a repeat relationship). **Everlab is the pattern only, never a target.**
2. **Profile `katya`,** market South America (the countries listed above).
3. **10+ employees** (from the EU brief, carried by «таку ж»).
4. **25-30 companies at step 2** (from the EU brief, carried by «таку ж»).
5. **Standing decisions carried over:** `cap_per_group: 50`, one import file, no waves (2026-09-29); no 3DLOOK client named, anonymised proofs only (2026-09-29, 09-30, 10-07); Message 1 asks, Message 2 offers the call, referral included (`referral_call: yes`, 2026-10-07); a lane for every function, FAIL only for the wrong company, people who left, identity collisions and duplicates (2026-09-29); former employers may be named; live 3DLOOK pages may be linked as they are (2026-09-29).
6. **South America defaults from Katya's first campaign there** (`2026-10-05-latam-health-weightloss`, defaults kept when Vadim said «продовжуй без апруву»): English cold copy, and no compliance line in any sequence. Taken again here (Open questions 2 and 3).
7. **Companies Katya already worked in South America** (2026-10-05) are excluded by the registry at step 2; none of them is re-approached through this campaign.

## Vadim's decisions 2026-10-19 (2): market scope

The step-1 draft predicted a thin market: the desk pass found 1 likely company and 5 to check, roughly 2-5 verified rows, against the default gate of 20. The same hypothesis in Europe found 18 companies after two rounds of country searches and reached 25 only when Vadim released 7 pool companies, all fit 3 (`2026-10-19-eu-everlab-similar/companies.md`, "Pool for Vadim (needs his release)"). The coordinator put the levers to Vadim before step 2: (a) add Mexico, (b) widen segment C, (c) lower the gate, (d) release pool names. His answers, verbatim choices, as relayed by the coordinator: «Додати Мексику», «Розширити клініки», «Знизити поріг» and «Одразу шукати» (company research starts right after the step-1 fix round).

1. **Mexico is IN, for this campaign only, on `katya`.** Mexican rows write `hq_country=Mexico`. `geo_profile()` still returns no profile for Mexico, so `validate-companies` warns "maps to no profile" on every Mexican row. That warning is expected here: the rows proceed, and warnings do not change the exit code. Central America, the Caribbean, Guyana, Suriname and French Guiana stay OUT. The script warns on them the same way, so step 2 keeps them off the list by hand. The South America defaults (decision 6) apply to Mexico: English cold copy, no compliance line, no Mexican law or regulator named.
2. **Segment C is widened** to lifestyle-medicine and nutrology (nutrologia, nutriología) clinics that sell a membership or programme with a follow-up layer between visits. The line against `2026-10-05-latam-health-weightloss`: a clinic is IN when it sells healthy adults a preventive programme (periodic assessments with follow-up across the year). A clinic whose programme is weight loss (emagrecimento, bajar de peso), obesity treatment, GLP-1 or bariatric care is that campaign's thesis and stays OUT. A clinic that sells both is IN only on a preventive programme it publishes on its own, flagged `wl_overlap=yes`. Every company Katya worked on 2026-10-05 stays excluded by the registry.
3. **The gate is lowered: step 3 runs with however many companies verify.** Vadim gave no number; the coordinator took "no minimum" as the default (Coordinator's decisions, 2). The target stays 25-30, and no anti-case pads the list.
4. **The release pool stays.** Step 2 records every candidate dropped only by a default or an anti-case in "Pool for Vadim (needs his release)" (rule under Validation criteria). Lever (d), releasing pool names at the list review, stays open to Vadim.

## Coordinator's decisions 2026-10-19 (not Vadim's words)

1. **Status `approved` on 2026-10-19, which lets step 2 run.** Approved by the coordinator because Vadim chose to start research straight away («Одразу шукати»), as in the EU campaign. His review of the company list is the hypothesis review: cutting a segment, a country or a company there is how this hypothesis gets reviewed.
2. **Gate: no minimum.** Vadim chose «Знизити поріг» and gave no number. Step 3 runs with however many companies verify; a list under 25 goes to Vadim with `companies.csv` and the pool, and step 3 still runs.

## What the closest accounts taught this campaign

> 1. **Everlab declined** (AU): the founder called it interesting tech that they are not looking at right now (`2026-08-14-au-digital-fitness/responses-summary.md`).
> 2. **Clinique La Prairie declined** (`olena`, 2026-10-13): it already measures body composition on site with its own devices, and an overlapping device could introduce inconsistencies in its data (`2026-10-07-eu-weight-loss-nutrition/responses-summary.md`).
> 3. **Katya's South America list** (2026-10-05, 128 invites, 4 replies recorded by 2026-10-16; acceptance not yet exported): Sensorial's CEO, the account nearest this thesis, asked for studies on the technology; Inc Beauty's commercial head asked how it works; OrienteMe's commercial head named the Head of Product as the roadmap owner. Three of the four replies came in English, the fourth was a Portuguese greeting (`2026-10-05-latam-health-weightloss/responses-summary.md`).
>
> Design response: target models where the member spends most of the year away from the clinic (re-tests on a cycle, an app or a health team in between); offer the capture for the member at home between assessments, never as a second device next to what a clinic measures on site. Expect an evidence question and answer it only under the evidence rule in Rules for steps 3-5: `accuracy-formulations.md` §1.1, §1.2, §1.4 and §1.8, and from §1.9 only the sentence that carries neither "positioned as" nor a banned phrase. The product owner is the buyer. The Message 1 question stays about the person's own work (lane notes) and differs from person to person. The falsification test below names the known objections.

---

## Vertical

South American and Mexican preventive-health, longevity and lifestyle-medicine companies that sell healthy adults a repeat relationship (membership, programme, re-test plan or follow-up cycles) built on periodic health assessments, with an app, member portal or a clinician or health team following up between assessments.

## Sub-segment: company types in scope

**In scope = all five:** (1) sells proactive or preventive health assessments to healthy adults, consumer or employer-paid; (2) a repeat relationship: membership, a programme, a re-test plan (typically 6-12 months) or defined follow-up cycles after the assessment; (3) a member-facing app, portal or dashboard, or clinician or health-team follow-up between assessments (WhatsApp or another messaging channel counts only where the company publishes that its clinicians, nutritionists or coaches follow members up over it between assessments; a booking, sales or support chat never counts, and nearly every clinic has one); (4) 10+ employees and product HQ in the campaign geo (the South American `katya` countries or Mexico); (5) no shipped phone-camera body scan and no own body-scanning hardware as the core product.

**Fit:** 5 = membership with app and re-test cadence (the Everlab shape); 4 = assessment followed by app or clinician follow-up; 3 = assessment with a re-test offer but no member app found; in B only with clinician or coach follow-up (on the list, flagged `fit=3`, counts toward the 25-30 by default; Open question 7).

Four segments, as in the EU template; C is widened by Vadim's decisions (2), 2. Named companies are research leads from desk passes on 2026-10-19. Step 2 verifies each one, size first, before it becomes a row.

- **A. Biomarker-testing memberships (digital first, home collection or partner labs, re-test cycle).** To check: Centeni (Brazil; preventive subscription launched March 2026, two assessment cycles a year, home collection, a digital panel and a health team on WhatsApp between cycles; founded May 2025, size likely near or under 10); Vitaleo (Montevideo; launching in Uruguay and Argentina in 2026, early stage; its source calls it a personalised supplementation platform based on blood analysis and AI, with a blood re-test every six months or yearly and a personal dashboard; check against the supplement anti-case: IN only with clinician follow-up, OUT as a supplement subscription); Holi 4 Life (São Paulo; preventive medicine and healthy longevity with metabolic exams and nutritionists, per a directory listing seen in search, page not readable; model and size to check); Previva (Mexico; users upload lab results for a 65+ biomarker reading and book video consultations with doctors, per a founder's LinkedIn post seen in search, page not opened; early stage, repeat relationship and size to check). **Seen: 0 likely, 4 to check.**
- **B. Check-up and imaging assessment companies with follow-up between assessments.** Brazilian tech press covers whole-body MRI check-ups as a celebrity-promoted trend, with a US scan as its example, and reports experts warning that the evidence does not support it and that false positives are a risk ([Canaltech](https://canaltech.com.br/saude/ressonancia-do-corpo-inteiro-e-moda-arriscada-entre-celebridades-265231/), seen in search). The desk pass found no dedicated South American company. Executive check-ups in Colombia and Chile sit inside hospitals (anti-case). Companies of this type measure the body on site, the setting of the on-site measurement objection (persona, `clinical` lane). **A B company is IN only with a relationship between assessments:** a member app or portal, or clinician or coach follow-up after the check-up. A re-test offer alone is not enough for B. **Seen: 0.**
- **C. Longevity, lifestyle-medicine and nutrology clinics with a membership, programme or follow-up cycles and a follow-up layer between visits** (widened by Vadim's decisions (2), 2). Fleury Lifecare (São Paulo, opened 2026 by Grupo Fleury; assessment, individual recommendations, follow-up cycles monitored in its own app; dedicated brand inside a listed diagnostics group, Open question 4). To check: AIONIS (Buenos Aires; wellness and longevity centre with prevention, functional assessment, biomarkers, body composition and digital health tools, per a LinkedIn job-post snippet seen in search, source not opened; membership and size to check); Lonvida (Mexico City, Polanco; longevity and regenerative-medicine clinic with biomarker diagnostics and personalised preventive programmes, per a medical-tourism review seen in search, page not opened; check against the regenerative anti-case and for follow-up between visits); Koltin (Mexico; announced two longevity clinics in Monterrey and Mexico City in November 2025, per a startup-news snippet; its own model and the health-plan anti-case to check first). Nutrology and lifestyle-medicine clinics: no named lead yet; IN only on the preventive line in Vadim's decisions (2), 2, with `wl_overlap=` in `notes`. **Seen: 1 likely, 3 to check.**
- **D. Doctor-led executive and corporate prevention programmes with follow-up** (the Everlab corporate executive-health line). To check: hygia (Brazil; preventive health plans for employers with home-collection check-ups and an app; took its preventive programme to Bolivia with the insurer SudAmericana in January 2022; coverage is from 2022-2023, current model to check; its HR health score sits against the employer-data rule). Katya's 2026-10-05 corporate-health platforms are excluded by the registry. New corporate care platforms belong to the 2026-10-05 thesis and stay out of D. **Seen: 0 likely, 1 to check.**

**Research priority: A and C first, then D; B last,** as in the template. Brazil first (São Paulo, Rio de Janeiro, Belo Horizonte, Curitiba, Porto Alegre), then Mexico (Mexico City, Monterrey, Guadalajara), then Argentina, Chile, Colombia, Peru and Uruguay. The widened C is searched in every country, Brazil and Mexico first.

**Realistic count: ~1 likely and ~8 to check, which gives roughly 2-6 verified from the known names.** Reaching 25-30 needs step 2 to find about 20 new companies, mostly in Mexico and the widened C (Vadim's decisions (2)). The one likely account is also the riskiest shape: Fleury Lifecare measures body composition and abdominal circumference on site (the on-site measurement objection) and sits inside a diagnostics group whose labs are an anti-case (Open question 4). The South American desk pass suggests an early, thin segment. Chile and Colombia surfaced no membership model with an app (the Colombian longevity offers found were regenerative or aesthetic; executive check-ups sit in hospitals). Argentina and Uruguay gave two unconfirmed leads only: Vitaleo, early stage and described by its source as a supplementation platform, and AIONIS, known from one job-post snippet with no membership seen. Many Brazilian longevity clinics are single sites. The three Mexican leads come from search snippets only. Under-10 companies are cut by the floor, as expected. With no minimum gate, a short list goes to step 3 as it is, with the pool beside it.

**Size:** 10+ employees (Vadim's decision 3), for this campaign only; `icp-detail.md` is not amended. A headcount conflict that straddles 10 goes on the list with the range in `employees` and the conflict in `notes`. Revenue is undisclosed for most of these companies and is not a FAIL reason (Open question 8); `revenue_estimate` is recorded where public.

**Geo and HQ:** product HQ decides: CEO and CPO location on LinkedIn, then where product roles are advertised, then press. Write the country itself into `hq_country`, never "LATAM" or "South America" (both are `katya` needles and hide the real HQ); Mexican rows write `Mexico`. Where the legal seat differs, `legal_hq=...; product_hq=...` in `notes`. US product HQ routes to `nick`, UK to `katerina`, Continental Europe to `olena` (`validate-companies --write-routed`). Mexico returns no profile, so `validate-companies` warns "maps to no profile" on every Mexican row; that warning is expected (Vadim's decisions (2), 1). Central America, the Caribbean, Guyana, Suriname and French Guiana also return no profile and stay OUT. The script only warns on them, so step 2 keeps them off the list and out of the pool.

**ICP mapping:** `icp-detail.md` has no preventive-health or longevity segment and no South American or Mexican geo for any segment. The five in-scope conditions and the feature screen are the screen; the size, revenue and geo limits of the telehealth and weight-loss segment do not apply (Open question 10).

## Feature screen (step 2 writes it into `notes` on every row)

`segment=A|B|C|D` · `fit=3|4|5` · `retest=` (cadence as published, or none) · `member_app=yes|no|whatsapp` (App Store or Play listing checked; `whatsapp` only where the company publishes clinician, nutritionist or coach follow-up over it between assessments, with that page as the source; a booking or sales chat is `no`) · `body_measure_onsite=none|device|imaging|unknown` (what the company publishes) · `camera_scan=yes|no` (app listing and site; yes is an anti-case) · `b2b=yes|no` (employer offer) · `parent=` and date, where owned · `product_hq=` where it differs from the legal seat · `wl_overlap=yes|no` (C rows: the clinic also sells a weight-loss programme) · `lang=pt|es` (site language).

## Use case

South American and Mexican preventive-health, longevity and lifestyle-medicine programmes can offer members a guided two-photo scan at home between periodic assessments, in the programme's own app or through a web link. Each scan returns 80+ body measurements (waist and hip among them), body composition estimates and a 3D model, and the clinician or health team receives a standardized, timestamped body record.

## Why this is plausible (evidence)

1. **The preventive membership model reached South America in 2025-26, led by Brazil, and it runs on cycles.** Grupo Fleury opened Fleury Lifecare in São Paulo in 2026 with a R$35 million unit: an initial assessment, individual recommendations, then follow-up cycles monitored in an exclusive app where the client follows their health map over time ([Saúde Business, 2026-07-27](https://www.saudebusiness.com/mercado-da-saude/grupo-fleury-aposta-em-cuidado-continuo-para-ampliar-atuacao-alem-da-medicina-diagnostica/)). Centeni launched a preventive subscription in March 2026 with two full assessment cycles a year and its health team on WhatsApp between them, reporting 200+ subscribers before launch ([Exame, 2026-03-18](https://exame.com/casual/a-startup-que-quer-antecipar-doencas-com-plataforma-preventiva/)). Axo Longevity, a 100+ biomarker membership that operates in Europe and Peru, reported about 1,000 active memberships, a company-wide count across both ([Forbes Perú, 2026-09-16](https://forbes.pe/negocios/2026-09-16/conoce-al-peruano-detras-de-esta-startup-de-salud-preventiva-global-que-ha-levantado-us5-millones/); `olena`'s account and never a target here). Vitaleo, which Forbes Argentina describes as a personalised supplementation platform based on blood analysis and AI, is launching in Uruguay and Argentina with blood re-tests every six months or yearly and a personal dashboard ([Forbes Argentina, 2026-05-27](https://www.forbesargentina.com/innovacion/el-emprendedor-ahora-apuesta-longevidad-ia-martin-larre-su-nuevo-proyecto-vitaleo-n91444)); it shows the re-test cycle reaching the region, and it fits this campaign only with clinician follow-up (supplement anti-case). Mexico, added by Vadim's decisions (2), has no opened source yet: search snippets show a Mexico City longevity clinic with biomarker programmes and a health company opening longevity clinics in Monterrey and Mexico City in late 2025 (leads in C); step 2 opens the sources. The specialty is organising: the Brazilian Society of Longevity Medicine and Science (SBMCL) was founded on 2026-08-08 ([Viva, 2026-09-07](https://viva.com.br/saude-e-bem-estar/organizacoes-voltadas-a-longevidade-nascem-com-foco-em-prevencao-e-ciencia.html)). Saúde Business puts the Brazilian longevity segment at about R$38 billion a year (a press estimate). Context only, never copy: funding, prices, member counts and market sizes are banned in copy.
2. **The vertical already counts body measures as programme indicators, taken at the centre.** Fleury Lifecare's follow-up tracks muscle strength, cardiorespiratory capacity, body composition, abdominal circumference, sleep, stress and adherence to behaviour change ([Saúde Business](https://www.saudebusiness.com/mercado-da-saude/grupo-fleury-aposta-em-cuidado-continuo-para-ampliar-atuacao-alem-da-medicina-diagnostica/)). The blood-first memberships found (Centeni, Vitaleo) describe exam panels, dashboards and messaging, with no body-size measure in the coverage read on 2026-10-19 (step 2 records `body_measure_onsite` per account; absence is never stated in copy). Clinical guidance asks for body size next to BMI: the Lancet Commission on clinical obesity (January 2025) says BMI alone should not be used for individuals and that excess adiposity should be confirmed by direct body-fat measurement or at least one of waist circumference, waist-to-hip ratio or waist-to-height ratio ([STAT](https://www.statnews.com/2025/01/14/bmi-lancet-report-obesity-as-disease-spectrum-urges-body-fat-measurements/); doi 10.1016/S2213-8587(24)00316-4). That is evidence from obesity care, and "obesity" is banned in copy. No source found on 2026-10-19 shows members or clinicians asking for a body record at home between assessments: the demand is inferred from the cycle and from centres measuring body size on site, and this campaign tests the inference. Context only, never copy.
3. **FitXpress fits as a home capture inside the member app, with honest limits.** Two photos (front and side), under 45 seconds from the photos to structured results, 80+ body measurements including waist and hip, body composition estimates (body fat %, lean mass, fat mass), BMI and BMR calculated, a 3D model; white-label REST API and web and mobile SDKs; repeatability per `accuracy-formulations.md` §1.2; 34,000 scans at one anonymised platform and 112,100 across all 3DLOOK customers in 2025 (`proof-points.md`). Limits: no published comparison with DEXA, MRI or bioimpedance, and none is claimed; validation 16-78 years, 150-220 cm, 38-210 kg, with participants from the US and Europe, so performance on South American and Mexican populations has not been characterized separately; no approved Portuguese or Spanish wording; data on AWS US-West-2 and partly US-East-1; no Latin American customer and no named longevity reference.

## Target buyer persona

**Who buys:** the owner of the member experience and the member app. At startups (most of A and D) that is the founder or CEO, then the product lead; at clinics and longevity centres (B, C) the medical director and the head of operations or clinics; at a dedicated brand inside a large group (Fleury Lifecare) the brand's executive, medical and product leads; at nutrology and lifestyle-medicine clinics the founding physician and the clinic director; at corporate programmes (D) the head of corporate health or B2B. Brazilian titles are mostly Portuguese and Spanish-speaking titles Spanish (Mexican chief executives often write Director General); the titles block carries all three forms.

- **Founder, CEO, Managing Director, Diretor Executivo, Director Ejecutivo, Director General, Gerente General:** `product` lane, P1 at companies under ~200 people. Cares about members renewing and coming back for the next cycle, and what the app gives them between assessments. Objection: "not on our roadmap now" (the Everlab answer).
- **Chief Medical Officer, Medical Director, Diretor Médico, Director Médico, Coordenador Médico, Clinical Director, Head of Prevention or Longevity:** `clinical` lane, P1. Cares about what the care team reviews at each follow-up and the data quality of anything added. Objections: "an overlapping measurement could make our data inconsistent" (the reason a European clinic that measures on site gave on 2026-10-13; the answer to give: the scan covers the months away from the clinic, and everything measured on site stays as it is) and "do you have studies?" (asked on Katya's 2026-10-05 South America list; answered in a reply only under the evidence rule in Rules for steps 3-5).
- **CPO, Head of Product, Head de Produto, Product Lead, Gerente de Produto or de Producto; Product Manager at companies under ~200:** `product` lane, P1-P2. Owns the app roadmap and the build-or-buy call (a 2026-10-05 referral named this role). Objection: "we could build it"; answer: pre-trained model through API and SDK, no computer-vision team to hire.
- **Head of Member, Patient or Customer Experience, Head of Care or Health Coaching, Head of Growth or Retention:** `product` lane, P2. Owns what members do between assessments.
- **COO, Head of Operations, Diretor de Operações, Director de Operaciones, Head of Clinics:** `operations` lane, P2. Cares about adding a member step without new equipment or site work.
- **CTO, Head of Engineering, Diretor or Head de Tecnologia:** `technical-integration` lane, P3.
- **Head of Corporate Health, Diretor de Saúde Corporativa, Head of B2B, Head of Partnerships, Business Development Director, Diretor de Novos Negócios:** `product` lane at segment D and for the employer offer of A-C; `partnership` where the company resells or embeds third-party services.
- **Not the buyer, not pulled by the titles block:** marketing, brand, content and social, PR, sales representatives and account executives, recruiting and HR, finance below CFO, legal, laboratory and radiology staff, nurses, phlebotomists, nutritionists, front desk, staff physicians without a leadership title, investors and board members. At a large group (Fleury), people in other business units are not this account (Open question 4). If an export brings non-buyers anyway, the standing decision applies: `referral` lane, except investors, board members, freelancers and people whose current company is another one (FAIL).

### Target buyer persona: Sales Navigator pull for step 3

**Pull by title filter inside the approved company list, never by company alone.** At Fleury add the keyword Lifecare or longevidade to the pull (Open question 4). Geography: people located in the campaign geo, the ten South American countries and Mexico (Vadim's decisions (2), 1); head-office people elsewhere follow Open question 9.

```titles
Founder
Co-Founder
Fundador
Fundadora
Cofundador
Cofundadora
Sócio Fundador
Sócia Fundadora
Chief Executive Officer
CEO
Managing Director
General Manager
Diretor Executivo
Diretora Executiva
Director Ejecutivo
Directora Ejecutiva
Gerente General
Director General
Directora General
Chief Medical Officer
Medical Director
Diretor Médico
Diretora Médica
Director Médico
Directora Médica
Coordenador Médico
Coordenadora Médica
Clinical Director
Diretor Clínico
Diretora Clínica
Head of Medicine
Head of Prevention
Head of Longevity
Chief Scientific Officer
Chief Product Officer
Head of Product
Head de Produto
Product Director
Product Lead
Product Manager
Gerente de Produto
Gerente de Producto
Chief Digital Officer
Head of Digital
Chief Operating Officer
Head of Operations
Diretor de Operações
Diretora de Operações
Director de Operaciones
Gerente de Operaciones
Head of Clinics
Head of Member Experience
Head of Patient Experience
Head of Customer Experience
Head de Experiência do Paciente
Head of Care
Head of Health Coaching
Head of Growth
Head of Retention
Chief Technology Officer
Head of Engineering
Diretor de Tecnologia
Head de Tecnologia
Head of Corporate Health
Diretor de Saúde Corporativa
Head of B2B
Head of Partnerships
Partnerships Director
Business Development Director
Diretor de Novos Negócios
```

**`cap_per_group: 50`.** Most accounts here have 10-150 employees and the cap should not bind; if a group passes 50 (Fleury is the only likely case), leadership and product people first.

## Message angle: segments, lanes and the content asset

Every person gets exactly one lane: `product`, `clinical`, `operations`, `technical-integration`, `partnership` or `referral`. Company facts come from step 2 (`companies.md`), one or two per account, each with a source; never invent one. **Writer notes are instructions, never copy.**

### Segment angles (writer notes)

- **A. Biomarker memberships.** Members re-test on a cycle and live in the app or the messaging channel in between. The scan gives the member a body record taken at home from that app or a web link. Never name their labs, never set scan outputs against blood results, never imply the panel misses something.
- **B. Check-up and assessment companies.** The assessment happens on site; the phone capture belongs to the months after it, in their app or a web link they send. Never mention their imaging or devices, never compare, never present the scan as another device in the clinic.
- **C. Longevity, lifestyle-medicine and nutrology clinics.** The member's year between clinic days or consultations, in the clinic's own app or a web link. The centre's own indicators may be named as context only where `companies.md` cites them, never followed by what the scan returns. Discreet, premium tone; no longevity, age, weight, diet or appearance outcomes.
- **D. Executive and corporate prevention.** The follow-up between yearly check-ups, on the employee's own phone; the programme decides what employees see. Never mention employer reporting features we do not have, and never route body data to HR.

### Lanes

- **`product`:** what the member app or a web link can ask a member for: a guided two-photo scan returning 80+ body measurements, body composition estimates and a 3D model, white-label through API or SDKs. M1: context from the company fact and one question about the person's own work, no call ask, no link. M2: a short call offer with the calendar link.
- **`clinical`:** the target is the care team's view of a member between visits: a standardized, timestamped body record from each home scan; estimates for the team to review, never a diagnosis or a risk assessment. Repeatability only in the quoted sentence under Rules for steps 3-5 (Numbers and accuracy). Same M1 and M2 shape.
- **`operations`:** nothing to ship, stock or install; the same guided sequence on any phone; the speed phrase inside a sentence about the scan. Never say or imply sites measure differently today.
- **`technical-integration`:** REST API with API-key authentication, web and mobile SDKs; photos deleted after processing or within 30 days; outputs stored and deletable by scan ID. No integration-time figure. Technical tone.
- **`partnership`:** one line on what the scan returns, the company fact, and whether a partner capability has a place in what they offer. M2: the call offer; the easy out is a pointer to whoever decides partnerships.
- **`referral`:** M1: one line on what the scan returns and why it matters for this company's members, then one question about the person's own work; never a "who" question, no call ask, no link. M2: a short call offer with the calendar link and an easy out that points to the owner of the member app or the member experience, worded fresh for each person (name the target, never reuse a sample sentence).

### Content asset in Message 2 (at most one article link, along with the calendar link)

| Who | Link |
|---|---|
| `product`, `clinical`, `operations`, all segments | https://3dlook.ai/content-hub/ai-body-data-wellness-platforms/ |
| `technical-integration` | https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/ (it describes US and EU rules; never restate any of it in the message) |
| `referral`, `partnership` | no article; calendar link only |

Both links returned HTTP 200 on 2026-10-19. Never quote figures from the page.

## Outreach language

English, every country, Mexico included (the 2026-10-05 default for Katya's South America list, taken again; the messages card prints "language: English"). Readers are Portuguese- and Spanish-speaking founders and doctors reading in a second language: short sentences, plain words, no idioms. Never mention a prospect's country regulator or law, never mention one country to a prospect in another, and never assume a prospect's language beyond the default. A reply in Portuguese or Spanish is answered by Katya in the reply's language (Open question 2).

## Rules for steps 3-5

- **Sender and format:** Kateryna, English, `Kateryna` alone on the last line, first name only. Connection request with no note. Message 1 ≤ 600 characters with no link; Message 2 ≤ 550 with https://meetings.hubspot.com/kateryna-boichuk as plain text in every lane and at most one article link (asset table). One import file.
- **Message 1 asks, Message 2 calls** (`referral_call: yes`), every lane: Message 1 = context first (what the scan returns and why it matters for this company's members), then one question; no call ask, no link. Message 2 = a short call offer with the calendar link; people who are not the buyer get an easy out pointing to the owner of the topic. Never the same ask twice.
- **Message 1 gate.** Every message 1 carries at least one product specific from `proof-points.md` and one line that could only have been written to that company; each pair of messages cites at least one number. `referral` is not exempt.
- **Between assessments, at home.** The scan is always positioned for the member away from the clinic, between assessments or re-tests. Never present it as a second device next to what a clinic measures on site, never compare it with their imaging, body-composition devices or blood results, and never say or imply what the company lacks. Message 1 makes an observation from the company fact or the person's role.
- **Never put a prospect's own data next to ours.** No message names a prospect's panels, scans, scores, indicators or device data and then says what the scan returns. A company's assessment cadence or programme may be named as context.
- **Not a diagnosis, not a risk score, not an outcome.** The scan does not diagnose, assess risk, detect disease, decide eligibility or recommend treatment. No promises about longevity, age, health outcomes, renewals or retention. Who compares: the programme's care team chooses which scans to compare; no message says or implies that 3DLOOK or the scan follows a member over time. Never for anyone under 16 or in pregnancy.
- **Employer and HR data.** No message suggests that scan outputs reach HR, an employer, a corporate dashboard, a health score or health-plan analytics, and no question asks what an employer or HR would want to see. The scan serves the member and their care team.
- **Several people at one company:** never mention colleagues or claim a conversation that did not happen; name the company in every Message 1 (the brand, such as Fleury Lifecare, where the person works for the brand); no two people at one company share an opener, a central question, a closing ask or a product sentence.
- **Companies:** never mention funding, investors, valuation, listing, owners, acquisitions, prices, revenue, headcount, member counts, unit counts or locations counts. A former employer may be named unless it is another account in this campaign or a banned term.
- **Compliance line: none in any sequence, in any lane** (2026-10-05 default for South America, applied to Mexico by Vadim's decisions (2), 1). `compliance.md` §9 has a US line and a UK/EU line and neither fits a South American or Mexican prospect; this overrides the §9 instruction printed in the card. No data-protection, regulatory, jurisdiction or medical-device wording in cold copy (LGPD, ANVISA, LFPDPPP, COFEPRIS, GDPR, HIPAA, SOC 2, FDA, "compliant", "certified", "medical device" are banned). Never claim or imply compliance with any Latin American law. In replies: the data lifecycle from `compliance.md` §3 and §10, the FAQ link, and legal@3dlook.me for national-law, international-transfer and regulator questions.
- **No 3DLOOK client is named.** Anonymised proofs only: 34,000 scans in 2025 at one platform (no client name, no geography); 112,100 scans in 2025 across all 3DLOOK customers (its own sentence, never placed so it reads as Latin American scans); "3DLOOK has worked with 100+ clients" (all-time, both products; never "use FitXpress today").
- **Numbers and accuracy only from `proof-points.md` and in its wording:** two photos; "under 45 seconds from the photos to structured results"; 80+ body measurements; body composition estimates (body fat %, lean mass, fat mass), BMI and BMR calculated; accuracy only per `accuracy-formulations.md` §1.1 (body measurements only, never in a sentence with body composition); repeatability, in any lane, only as this sentence, word for word (the one rule sentence that goes into copy verbatim): "For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm." Never rebuild it from "< 1 cm"; 38-210 kg only in `clinical`. No integration time, market, prospect or medical figures.
- **Evidence questions in replies** ("do you have studies?", asked once on the 2026-10-05 list): answer only from `accuracy-formulations.md`, each sentence in its own wording: §1.1 (accuracy), §1.2 (repeatability), §1.4 (the validation population, US and Europe, and its scope: performance outside it has not been characterized) and §1.8 (methodology under NDA). From §1.9 use only the sentences that carry neither "positioned as" (§2.1, §2.3) nor a phrase this campaign bans; on 2026-10-19 that is the NCSU sentence alone. The other five §1.9 sentences carry "peer-reviewed", "clinically validated", "positioned as" or a named reference method, and they stay out of replies. Never "clinically validated", "peer-reviewed" or "proven" about our evidence (§3, item 5).
- **The 3D model** is shown only where the programme chooses to show it; never lead with it as the value.
- **Use-case file limits:** from `fx-telehealth-weight-loss` take only "What FitXpress is here", without Smart Scales. Its hero line, Why now, KPI list, weight-loss and GLP-1 framing do not apply to this audience.
- **Word traps:** no "objective" about our data (standardized, timestamped, structured, repeatable); no "comprehensive", "seamless", "leverage", "game-changer"; no em or en dash; no "plus" as a connector; no "so" introducing a benefit; no corrective "X, not Y". No pricing or trial terms anywhere; a price question goes to the call.

## Anti-cases (where it does NOT work)

- **Already worked or held:** every company in `katya-registry.json` (the 2026-10-05 South America accounts, GnTech and N2B Brasil among them) and in another profile's registry; Axo Longevity (`olena`, 2026-10-19 list, operates in Peru); existing customers. Everlab and other look-alikes outside South America and Mexico are not in this geo.
- **Own body-scanning hardware or a shipped camera scan:** any company whose app already runs a phone-camera body scan or has signed a scanning vendor; camera-analysis vendors selling into this category. That is a displacement sale and stays out of this campaign.
- **Clinic-only programmes where every measurement happens on site:** luxury spas, retreats and longevity spa brands with no member layer between visits. A European clinic's decline on 2026-10-13 (its own devices on site, and a fear of inconsistent data) is the evidence.
- **Laboratory chains and test sellers without a repeat relationship:** diagnostic lab groups as labs (Dasa, Sabin, Hermes Pardini, Multilab, Chopo, Salud Digna type), which supply these memberships; one-off home-test e-shops and DNA-only test sellers. A test seller is IN only with a membership or re-test plan and follow-up. A lab group's dedicated prevention brand with its own app follow-up is the one exception (Fleury Lifecare, Open question 4).
- **Check-up departments inside hospital groups** (Hospital Israelita Albert Einstein, Sírio-Libanês, Oswaldo Cruz, Fundación Santa Fe de Bogotá, Clínica Alemana, Clínica Las Condes, Médica Sur, Hospital Ángeles, Centro Médico ABC type): one service line, hospital procurement, no member layer (Open question 5).
- **Health plans, insurers and health-insurance startups, including their own prevention or longevity programmes** (Colsanitas, Metrus, MedSenior type): different sales, and the 2026-10-05 corporate-health ground.
- **Regenerative, hormone, aesthetic and anti-aging treatment clinics** (stem cells, IV drips, hormone protocols, aesthetics) without a diagnostics membership and follow-up; supplement, nutraceutical and mitochondrial-product subscriptions without clinician follow-up.
- **Other theses already run on `katya`:** weight-loss, GLP-1 and obesity programmes (nutrology and lifestyle clinics whose programme is weight loss included; the line is in Vadim's decisions (2), 2), corporate-health and benefit platforms, telehealth services, aesthetic clinic chains, tele-diagnostics, employee assistance and mental health (2026-10-05).
- **Statutory occupational medicine** (medicina do trabalho, salud ocupacional, fitness-for-work exams): a different use case (`fx-occupational-health`). Voluntary preventive check-ups paid by employers stay IN under D.
- **Societies, academies and research centres** (SBMCL, The Longevity Academy, hospital longevity science centres): no product and no member.
- **Structural:** under 10 employees; product HQ outside the campaign geo, the South American `katya` countries and Mexico (US, UK and Europe route to their profiles; Central America, the Caribbean, Guyana, Suriname and French Guiana stay OUT, Vadim's decisions (2), 1; Israel and the Gulf are not this market); acquired or merged in the last 18 months.

## Validation criteria (Step 2 will check)

- **List size:** 25-30 verified companies is the target. **No minimum: step 3 runs with however many companies verify** (Vadim's decisions (2), 3; Coordinator's decisions, 2). A list under 25 is reported to Vadim with `companies.csv` and the pool; do not pad with anti-cases. A row counts only when `web-verify.py` returns `verified*` with a `source_url`; a `blocked` row counts only after a manual check written as `verified-manual` with `manual_check=<who>, <date>, <what>` in `notes`.
- **Pool for Vadim (needs his release).** Every candidate dropped only by a default or an anti-case, not by evidence of poor fit, goes into a `## Pool for Vadim (needs his release)` list at the end of `companies.md`, as in the EU campaign. One line each: name, country, website, and the default or anti-case behind the drop (for example: fit 3 in B without clinician or coach follow-up; a hospital-group check-up centre, Open question 5; a supplement subscription; a regenerative clinic that also sells a diagnostics membership; a nutrology clinic with a membership whose programme is weight loss, the 2026-10-05 thesis). Pool names are not rows and count toward nothing until Vadim releases them. Not in the pool: registry hits and companies held by another profile (decision 7), rows routed to another profile, companies under 10 employees (decision 3), countries Vadim kept out (Vadim's decisions (2), 1), and candidates that fail an in-scope condition on evidence (no repeat relationship, a shipped camera scan or own scanning hardware, closed or merged).
- **Row schema:** `company_name, website, linkedin_url, hq_country, hq_city, employees, revenue_estimate, fit_score_1_to_5, fit_reason, source_url, notes`, with the feature screen in `notes`, one canonical name per company, the country itself in `hq_country`, and `validate-companies --campaign 2026-10-19-latam-everlab-similar --profile katya --write-routed` exiting 0.
- **Every row proves the five in-scope conditions** with a source: the assessment, the repeat relationship, the app, portal or follow-up, 10+ employees, and `camera_scan=no`.
- **Registry:** no company covered by any profile (the 2026-10-05 `katya` accounts included); match on website and LinkedIn URL, never the name alone (Holi 4 Life is not `holi`); `outbound-registry.py check --profile katya` on people before import.
- **People:** pulled by the titles block; a job-change check before import; aim for ≥40 contacts at PASS. With no company minimum, a shorter list gives fewer people; report the count and do not pad.
- **Proof:** no named reference in this vertical or region; the two anonymised scan figures are the proof. Each company gets one or two sourced facts in `companies.md` for Message 1.

## Success metrics for this campaign

| Metric | Target | Floor |
|---|---|---|
| Verified companies | 25-30 | none (gate lowered, Vadim's decisions (2), 3) |
| Contacts at PASS | 60+ | 40 |
| Connection acceptance | 20% (about 12 of 60) | 12% (`katya` Israel 2026-07: 29.9% with no language barrier; 2026-10-05 not yet exported) |
| Replies per accepted person | 10% (1-2 replies) | 5% |
| Positive replies (interested or call) | 1 | none set |
| Discovery calls | 1 within 8 weeks | none set |

**What this volume can show.** About 60 contacts at 20% acceptance is about 12 accepts, and 10% of those is 1-2 replies. The likely outcome is a small-sample read: directional, not a verdict. At the 40-contact floor the read is inconclusive by design.

- **Inconclusive** if fewer than 12 people accept.
- **Supported (directional)** if one P1 or P2 reply is positive or books a call.
- **Falsified** if 2 or more P1 or P2 replies give the same known objection: a home body record overlaps with what they measure on site, or body data is not on their roadmap. One such reply is noted, not a verdict. An evidence question ("do you have studies?") is neither: it is answered and counted as a question.
- **A language signal, not a falsification,** if two or more replies ask for Portuguese or Spanish or say English was the obstacle (Open question 2).

## Open questions for Vadim (default taken on each)

1. **Mexico. Closed 2026-10-19 by Vadim's decisions (2), 1:** Mexico is IN for this campaign on `katya`; Central America, the Caribbean, Guyana, Suriname and French Guiana stay OUT. `geo_profile()` still returns None for Mexico (checked 2026-10-19), so `validate-companies` warns on every Mexican row, as expected. Add Mexico to `PROFILE_GEO["katya"]` for later campaigns? **Update 2026-10-19, Vadim «додай назавжди»:** Mexico is now in `PROFILE_GEO["katya"]` for good (commit 595d496), so `geo_profile()` returns katya for Mexican rows and the warning above no longer fires; the question about later campaigns is closed.
2. **Language.** **Default: English** cold copy for Portuguese and Spanish speakers, Mexico included, as on 2026-10-05 (no Mexican reply data exists yet); the gates, bans and approved wording exist only in English, and three of the four 2026-10-05 replies came in English. Portuguese or Spanish copy would need translated bans and a gate that reads them.
3. **Compliance wording for South America and Mexico.** **Default: no compliance line in any sequence** and no claim about LGPD, LFPDPPP or any other national law, as on 2026-10-05; such questions in replies go to legal@3dlook.me.
4. **Fleury Lifecare** (dedicated longevity brand of Grupo Fleury, a listed diagnostics group). **Default: IN as one account (segment C)** under the template's dedicated-brand rule; people only in Lifecare, longevity, the B2C business unit and group digital or product roles; laboratory, hospital and B2B diagnostics people at Fleury are treated as another business and not sent. Cut it, or release the whole group?
5. **Hospital-group check-up centres** (Einstein, Sírio-Libanês, Fundación Santa Fe de Bogotá, Clínica Alemana type). **Default: OUT;** a dedicated prevention brand with its own membership or app can be IN. Release specific names at the list review.
6. **A thin market and the gate. Closed 2026-10-19 by Vadim's decisions (2):** the levers were (a) add Mexico, (b) widen C to lifestyle-medicine and nutrology clinics with a membership (overlapping the 2026-10-05 weight-loss thesis; the line is in Vadim's decisions (2), 2), (c) lower the gate, (d) release pool names. Vadim took (a), (b) and (c), with no minimum. Lever (d) stays open: he can release pool names at the list review.
7. **Fit-3 rows** (assessment and re-test offer, no member app found; in B only with clinician or coach follow-up; a WhatsApp channel counts as follow-up only under in-scope condition 3). **Default:** on the list, flagged `fit=3`, counted toward the 25-30. Count them on the list but not toward the target?
8. **Revenue floor.** **Default: not a FAIL reason;** 10+ employees is the only size gate.
9. **People outside the campaign geo (South America and Mexico) at IN companies.** **Default:** named head-office people stay on `katya` (one company, one profile); local staff of foreign sites OUT.
10. **ICP segment.** `icp-detail.md` has no preventive-health or longevity segment and no South American or Mexican geo. **Default:** the five in-scope conditions and the feature screen are the screen. Add a segment if either Everlab-similar campaign gets a positive reply?
11. **Katya's LinkedIn positioning** (the social table in `CLAUDE.md` §5 still reads Israel and the Gulf). **Default:** risk accepted, as on 2026-10-05; Vadim decides any profile change.
12. **Evidence replies without "peer-reviewed".** The reply rule (Rules for steps 3-5) keeps the §1.9 sentences that say the claims are not peer-reviewed out of replies, because this campaign bans the phrase. **Default:** §1.4, §1.8 and the NCSU sentence carry the boundary. License §1.9 sentences 1 and 2 for replies only?

## Sources

- Internal: `2026-10-19-eu-everlab-similar/hypothesis.md` (template), `companies.csv` (Axo Longevity) and `companies.md` (Pool for Vadim, 18 + 7); `2026-10-05-latam-health-weightloss/hypothesis.md`, `import-log.md` and `responses-summary.md`; `2026-08-14-au-digital-fitness/companies.md` (### 03. Everlab) and `responses-summary.md`; `2026-10-07-eu-weight-loss-nutrition/responses-summary.md`; `exclusions/*.json` and `outbound-registry.py status` (2026-10-19); `scripts/outbound-pipeline.py` (`PROFILE_GEO`, `geo_profile`); `scripts/outbound_pack.py` (`OWNER`, `referral_call`, `CARD_SECTIONS`); `icp-detail.md`; `use-cases/fx-telehealth-weight-loss.md`; `proof-points.md`; `accuracy-formulations.md`; `compliance.md`.
- Region and accounts: [Saúde Business, Fleury Lifecare](https://www.saudebusiness.com/mercado-da-saude/grupo-fleury-aposta-em-cuidado-continuo-para-ampliar-atuacao-alem-da-medicina-diagnostica/) · [Exame, Centeni](https://exame.com/casual/a-startup-que-quer-antecipar-doencas-com-plataforma-preventiva/) · [Forbes Perú, Axo Longevity in Europe and Peru](https://forbes.pe/negocios/2026-09-16/conoce-al-peruano-detras-de-esta-startup-de-salud-preventiva-global-que-ha-levantado-us5-millones/) · [Forbes Argentina, Vitaleo](https://www.forbesargentina.com/innovacion/el-emprendedor-ahora-apuesta-longevidad-ia-martin-larre-su-nuevo-proyecto-vitaleo-n91444) · [Viva, SBMCL and The Longevity Academy](https://viva.com.br/saude-e-bem-estar/organizacoes-voltadas-a-longevidade-nascem-com-foco-em-prevencao-e-ciencia.html) · [Startup Guide, hygia](https://www.startupguide.com/we-are-a-health-data-startup-to-make-people-live-longer) · [Medicina S/A, hygia in Bolivia](https://medicinasa.com.br/?p=61513)
- Search results used for leads and anti-cases, pages not opened: [Gust, Holi 4 Life](https://gust.com/companies/holi-4-life) · AIONIS (LinkedIn job-post snippet, no URL kept) · [Portafolio, executive check-ups in Colombian hospitals](https://www.portafolio.co/revista-portafolio/chequeos-ejecutivos-evolucionan-hospitales-apuestan-por-prevencion-y-tecnologia-para-altos-directivos-495549) · [Bookimed, Colombian longevity clinics](https://en.bookimed.com/clinics/country=colombia/direction=longevity-health) · [Canaltech, whole-body MRI check-ups as a risky celebrity trend](https://canaltech.com.br/saude/ressonancia-do-corpo-inteiro-e-moda-arriscada-entre-celebridades-265231/) · Mexico and widened C (fix round, 2026-10-19): [MTA review, Lonvida](https://www.better.medicaltourism.com/article/lonvida-mexico-city-review-better-by-mta-2026) · [descubre.vc, Koltin longevity clinics](https://www.descubre.vc/noticia/koltin-expande-su-modelo-de-prevenci-n-a-cl-nicas-de-longevidad-2025-11-19) · Previva (founder's LinkedIn post, https://mx.linkedin.com/in/kainara-oleg, snippet only)
- Clinical context: [STAT, Lancet Commission](https://www.statnews.com/2025/01/14/bmi-lancet-report-obesity-as-disease-spectrum-urges-body-fat-measurements/) · Rubino et al., Lancet Diabetes Endocrinol 2025;13:221-62, doi 10.1016/S2213-8587(24)00316-4.
