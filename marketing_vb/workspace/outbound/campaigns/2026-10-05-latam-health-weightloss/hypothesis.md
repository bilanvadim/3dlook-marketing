---
product: fitxpress
profile: katya
market: South America
created: 2026-10-05
status: approved
approved: 2026-10-05
use_case: fx-telehealth-weight-loss
cap_per_group: 50
banned_terms: [Yazen, UK Meds, Healthyr, Safariland, Burlington, Jim's Formal Wear, Generation Tux, Tailoor, Redthread, Prism, Bodygram, Size Stream, InBody, Tanita, Withings, Evolt, Styku, Fit3D, Ozempic, Wegovy, Mounjaro, Zepbound, Saxenda, Olire, Rybelsus, semaglutide, semaglutida, tirzepatide, tirzepatida, liraglutide, liraglutida, Novo Nordisk, Lilly, EMS, Biomm, Hypera, CVS, Capgemini, Telefonica, Telefónica, Sabin, ArcelorMittal, Belgo Bekaert, Aperam, Paul Wurth, EPharma, Go Laser, Monashees, funding, investors, investor, valuation, seed round, IPO, LGPD, ANVISA, ANS, CFM, CFN, Asbran, Conitec, SUS, NR-1, HIPAA, GDPR, SOC 2, FDA, compliant, certified, medical device, DEXA, DXA, BIA, bioimpedance, bioimpedância, visceral, Smart Scales, mismatch, fraud, eligibility, eligible, verify, verification, Método 5S, 5S method, 5S Emagrecimento, obese, diabetics, bikini, summer body, before and after, before-and-after, burn fat, fat loss, remission, reversal, guarantee, guaranteed, ROI, beyond weight, beyond the scale, scale weight, weight alone, weight only, only weight, just weight, more than weight, non-scale, tape measure, guesswork, unreliable, inaccurate, error-prone, generic figure, never a promise, not a promise, context only, Circling back, Following up, Israel]
---

# Outbound Hypothesis — 2026-10-05 — Brazil weight-management and corporate-health programmes (fixed list, Katya's first South America campaign)

- **Campaign:** `2026-10-05-latam-health-weightloss`
- **Owner:** Kateryna (Katya) Boichuk, profile `katya`. Her outbound market is South America from 2026-10-05 (Vadim); Israel is closed. This is her first South America campaign.
- **Sender in the card:** `scripts/outbound_pack.py` sets `OWNER["katya"] = "Kateryna"`, so every message ends with `Kateryna` alone on the last line. `calendar_link("katya")` reads `outbound-message2-template.md` and returns https://meetings.hubspot.com/kateryna-boichuk.
- **Company list: fixed, not researched.** Vadim pulled it from Sales Navigator: `sales-nav-raw/export-1.csv`, 211 people (Brazil 180, Argentina 12, Colombia 6, Ecuador 6, Chile 5, Bolivia 1, Uruguay 1), 58 company LinkedIn pages and 42 rows with no company page (39 distinct names), 97 in all. There is **no company-researcher step**: step 2 builds `companies.csv` from the verdict table below. The export was pulled by company, so every function is in it. Summarised with stdlib `csv` scripts grouped by company LinkedIn URL; the file was not read whole.
- **Scope widened by Vadim on 2026-10-05** («всі крім шуму»): every health-related account goes, and only noise stays out (see "Vadim's decisions 2026-10-05 (scope)"). The first version of this file sent 84 people from 16 accounts; this one sends 163 from 41.
- **Countries.** The 163 people to send are in Brazil (142), Argentina (6), Ecuador (6), Chile (4), Colombia (4) and Bolivia (1). All of them are in Katya's market: `outbound-pipeline.py` `PROFILE_GEO["katya"]` covers Brazil, Argentina, Chile, Colombia, Ecuador, Bolivia, Uruguay, Paraguay, Peru and Venezuela. The Spanish-speaking accounts are Llamando al Doctor (AR), Grupo Wellness Latina (AR, one person in Bolivia), Reliv, Céntriqo and Ihealthy (EC), holadr. IPS and Perfect clinic (CO), Saluta and Terapia Online (CL).
- **ICP:** `icp-detail.md` §1 (Telehealth & GLP-1 / Weight Loss Programs) is the core segment: it names "coaching apps treating obesity / weight management", "GLP-1 prescription platforms with ongoing care" and "employer-sponsored metabolic health programs". Other segments on the list: §4 (its list includes employer benefit platforms, wellness program administrators and population health tech providers) for the corporate-health platforms; §5 (metabolic clinics) for Grupo Endos; §9 (plastic surgery clinics and aesthetic medicine centers) for the aesthetic chains. Tele-diagnostics, employee-assistance and mental-health services match no segment; they go in on Vadim's scope decision with a partnership or referral ask only. No segment lists South America as a geo; the compliance status of the region is Open question 2.
- **Use case files:** `use_case: fx-telehealth-weight-loss` (in the card). Its hero line, its "Smart Scales" mismatch framing and its KPI list are not usable here (Rules). The corporate-health platforms take the body-measurement boundary of `use-cases/fx-wellness-rewards.md`; the aesthetic chains take `icp-detail.md` §9, which has no use-case file. Both are restated under "Message angle", because neither file is in the card.
- **Content assets (HTTP 200 on 2026-10-05 12:07 UTC, `curl -sL -o /dev/null -w "%{http_code}"`):** [GLP-1 Market Growth and the Need for Better Patient Progress Tracking](https://3dlook.ai/content-hub/glp-1-market/), [AI Body Data for Wellness Platforms](https://3dlook.ai/content-hub/ai-body-data-wellness-platforms/), [Bariatric Pre-Qualification and Patient Progress Tracking](https://3dlook.ai/content-hub/bariatric-pre-qualification-mobile-3d-body-scanning/), the [FitXpress privacy and security FAQ](https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/). The telehealth hub `the-potential-of-ai-in-telehealth` is live but its FAQ says "HIPAA-compliant implementations" and "not positioned as a medical device", so it is not linked. Which company and lane gets which page is under "Message angle".
- **Registry:** none of these companies or people was ever contacted by any profile (verified by the coordinator). Re-checked here on 2026-10-05: a case-insensitive search of `exclusions/*.json` for every account name returns only substring false positives. `katya-registry.json` holds Israel only; `exclusions/README.md` still lists `katya` as Israel (stale, not this campaign's job).

> **Read this first.**
> 1. **43 accounts are IN, 163 people to send.** 41 accounts send by default; Grupo Endos and Clínica Lev Vida each have only a company-named row, held at validation. 12 company-named rows (no person's name) are held at validation, 33 rows are noise and stay OUT, 3 rows are duplicates. 163 + 12 + 33 + 3 = 211.
> 2. **One pattern runs through the core.** Brazil's GLP-1 market widened in 2026: semaglutide and liraglutide have no patent protection, 14 of the 25 registered weight-loss pens were registered in 2026, prices fell 70% in under a year, and in September 2026 the Ministry of Health asked Conitec to assess them for the public system ([Agência Gov](https://agenciagov.ebc.com.br/noticias/202609/ministerio-da-saude-protocola-na-conitec-pedido-de-analise-para-incorporacao-de-canetas-emagrecedoras-no-sus)). The core accounts pay for, deliver or manage weight-related care and run their own app; FitXpress offers a guided phone body record inside it. Context for Katya, never numbers in copy.
> 3. **Five segments, five angles.** Weight-loss programmes and clinics, and corporate and health-plan care platforms: a body record in their own app. Generalist telehealth and medical centres: body measurements for consults that need them. Aesthetic chains: a body record before the in-person evaluation and between body-treatment sessions. Tele-diagnostics, employee-assistance and mental-health services, plus N2B, GnTech and Sensorial: a partnership or referral ask only, never a pitch that implies they need body scanning.
> 4. **Overlap at four accounts, displacement at none.** Liti's connected scale returns body composition to its app and its kit has included a measuring tape; Magrass Club tracks weight and measurements; Emagrecentro records waist; N2B sells in-gym body-composition exams. No phone-camera body scan was found at any account whose site and App Store listing could be read (three sites could not be read: "Displacement check"). Copy never lists a prospect's data and then adds ours.
> 5. **Franchise networks: the franchisor is the buyer.** FitXpress is an API and SDK that lives in an app, and the client app belongs to the franchisor. Every Magrass, Emagrecentro, Siluets, Lipocenter and Face Doctor row looks like a unit owner or unit staff, except three rows the validator must resolve (Gabriela Biazus at Magrass, Flaminio Dalul at Siluets, aline caio at Lipocenter). Unit people get `referral`, each with a different question about who at the franchisor owns the app or the protocol.
> 6. **Vidalink: the scan stays away from the pen benefit.** No Vidalink message mentions Peso Saudável, weight-loss pens, prescriptions, the audit or the balance; the scan sits in Bem-estar 360º or the app in general.
> 7. **Defaults Vadim left (built in):** English cold copy and no compliance line in any sequence. Nothing in copy claims compliance with any Latin American law.
> 8. **Katya's Israel campaign accepted 38 of 127 invites (29.9%)** and drew 4 replies on 73 messages; across both Israel sends the first message after acceptance replied at 15.4% and follow-ups at 2.3% (432 messages). This list is cold English outreach to Portuguese and Spanish speakers, half of it referral and partnership asks: expect lower acceptance.

---

## Vertical

Latin American (mostly Brazilian) health programmes that pay for, deliver or manage weight-related, primary or remote care and run their own member or patient app: corporate health and benefit platforms, online obesity programmes, weight-loss and aesthetic clinic networks, and telehealth services. Adjacent health services (tele-diagnostics, employee assistance, mental health, body-composition and genetic-testing businesses) are approached for partnership only.

## Sub-segment

The 43 IN accounts, by segment:

- **Weight-loss programmes and clinics (`fx-telehealth-weight-loss`):** Liti, MedTrue (MedSlim), Instituto GL, Instituto Lumiere, Clínica da Obesidade, Grupo Endos, Grupo 5S; franchise networks Magrass, Emagrecentro, Lipocenter.
- **Corporate and health-plan care (`fx-wellness-rewards` boundary):** Vidalink, OrienteMe, Salvia Saúde Corporativa, GESmed, Atrys Brasil (AxisMed), iMND, Wellbe, Nilo Saúde, Amparo Saúde, Abertta Saúde.
- **Generalist telehealth and medical centres:** L2D Saúde Digital, Llamando al Doctor (AR), Reliv (EC), holadr. IPS (CO), Céntriqo (EC), SPDM.
- **Aesthetic clinics (`icp-detail.md` §9):** Pró-Corpo, Siluets, Face Doctor, Inc Beauty, Ihealthy (EC), Perfect clinic (CO), Clínica Lev Vida.
- **Partnership or referral only:** tele-diagnostics (RWE Telemedicina, Telecárdio); employee assistance and health coaching (TELUS Health Brazil, Grupo Wellness Latina); mental health (Saluta, Zínea, Terapia Online); body composition, genetics and cognition (N2B Brasil, GnTech, Sensorial).

**Size:** no headcount floor (Vadim, 2026-09-29). Revenue is not disclosed by most accounts and is not a FAIL reason on this list.

## Company types in scope: verdicts for the export

Step 2 builds `companies.csv` from this table, one row per canonical company. The `group` is the canonical name: it is what `cap_per_group` counts and what `build-import` writes into the registry. **Matching is on the company LinkedIn URL and website, never on the name alone:** `extract-people` joins on name keys, so the name collisions named below match an IN account's key and must be failed by name.

**Aliases for step 2 (write them in the `company_name` cell as `Canonical (alias / alias)`, so every raw cell matches and the group stays the canonical name):**
- `Vidalink (Vidalink do Brasil SA / Vidalink do Brasil S-A / Vidalink do Brasil)`. Write `S-A`, not `S/A`: the slash splits aliases. Checked: `Vidalink do Brasil S/A` normalises to the `S-A` key.
- `Magrass (Magrass Montenegro / Magrass Moinhos de Vento / Magrass rio preto / Magrass Assis / Magrass Paulínia / Magrass Contagem / Magrass Cascavel / Magrass Macaé / Magrass Pindamonhangaba / MagraSS - Maringá / MagraSS Maringá / Magrass Vila Olimpia / G3 Treinamento Personalizado)`. Checked: every raw cell matches. G3 is an alias only, so that its one person (a Magrass unit co-owner) lands in the group.
- `Siluets (Siluets Franchising / Siluets Estética / Siluets Estética Aracaju / Siluets Estética Unidade Santo André)`; `Lipocenter (LIPOCENTER FRANQUIA / lipocenter / Lipocenter Perdizes)`; `Pró-Corpo (Pró-Corpo Estética Avançada)` (never alias the Argentine `Pró Corpo Plástica e Estética`, a collision); `Face Doctor (Face Doctor Franchising - Oficial)`.
- `Atrys Brasil (AxisMed / AxisMed - Garantia em Saúde Populacional / AxisMed Gestão Preventiva da Saúde)`; `TELUS Health Brazil (CARE by TELUS Health / Chestnut Global Partners do Brasil / Care Global Partners)`; `Grupo 5S (Grupo 5S - Serviços, Produtos, Franchising e Tecnologia / Brand's)`; `Céntriqo (Céntriqo - Centro Médico Integral / Quirurgic - Centro de Cirugía Ambulatoria)`; `Saluta (Saluta - Centro de Innovación en Salud / Saluta - Centro de Salud Digital)`; `L2D Saúde Digital (L2D Telemedicine Network)`; `Reliv (Reliv - Healthcare made simple / Reliv 500 LatAm B15)`; `Sensorial (Sensorial Sports)`; `GnTech (GnTech - Saúde Personalizada)`; `Grupo Wellness Latina (grupowellnesslatina)`; `RWE Telemedicina (RWE Telemedicina e Diagnósticos)`; `SPDM (SPDM - Associação Paulista para o Desenvolvimento da Medicina)`; `Inc Beauty (Inc Beauty Dermatology Institute)`; `Ihealthy (Ihealthy Centro Estetico Integral)`. Checked: every raw cell of an IN row matches its group, and no collision cell matches except the four named below.
- `Clínica da Obesidade (Hotel A Casa das Portas Velhas / Viva Salute)`, `Nilo Saúde (Nilo / MGL Consultoria / Aché Laboratórios)`, `Liti (Find.AI)`: the other companies are aliases only, so that a re-grouped person lands in the right group.
- `Emagrecentro (Emagrecentro Centro de Emagrecimento e Estética)`, `MedTrue (MedTrue - Health Tech / MedSlim)`, `GESmed (GESmed Healthtech Full Solution)`, `N2B Brasil (MyNutri)`.
- **Never registered:** G3 Treinamento Personalizado, MGL Consultoria, Aché Laboratórios, Find.AI, Hotel A Casa das Portas Velhas, Viva Salute, Brand's, Atrys Health, TELUS Health (global), and every OUT company.

| # | Export `Company_name` (rows) | Company page on the row | Canonical company = group | Verdict | Send | Why (source) |
|---|---|---|---|---|---|---|
| 1 | `Vidalink` (13), `Vidalink do Brasil` (3), `Vidalink do Brasil SA` (1), `Vidalink do Brasil S/A` (1, no page) | vidalink · 253 staff · São Caetano do Sul | **Vidalink** | IN | 18 | Corporate medicines and wellbeing benefit with its own employee app ([vidalink.com.br](https://vidalink.com.br/); App Store v5.10.8, 2026-09-22). |
| 2 | `orienteme` (5), `OrienteMe` (2) | orienteme · 189 staff | **OrienteMe** | IN | 7 | Psychology, nutrition and physical orientation by video, text or audio in its app (App Store, 2026-10-04; [orienteme.com.br](https://www.orienteme.com.br)). |
| 3 | `GESmed` (3), `GESmed Healthtech Full Solution` (1) | gesmedhealthtech · Belo Horizonte | **GESmed** | IN | 4 | Corporate health management on the Modelo GES, a primary-care model (LinkedIn; [Diário do Comércio](https://diariodocomercio.com.br/negocios/healthtech-mineira-aposta-na-saude-corporativa/)); AppGES (App Store). |
| 4 | `Salvia Saúde Corporativa` (3) | salviasaudecorporativa · 202 staff · Florianópolis | **Salvia Saúde Corporativa** | IN | 3 | Digital and in-person primary care for companies and operators; telenutrition in its app ([salviasaude.com.br](https://salviasaude.com.br/)). |
| 5 | `Atrys Brasil` (3), `AxisMed - Garantia em Saúde Populacional` (1); `AxisMed` (1, no page), `AxisMed Gestão Preventiva da Saúde` (1, no page) | atrys-brasil · 176 staff | **Atrys Brasil** | IN | 5 (+1 company-named, held) | Population health management for health plan operators (LinkedIn); acquired from the Telefónica group by Atrys Health (Spain) in 2020 ([Medicina S/A](https://medicinasa.com.br/atrys-axismed/)). Brazilian operating company with its own executive director: `katya`'s account. |
| 6 | `Wellbe` (3) | wellbehealth · 62 staff · Curitiba | **Wellbe** | IN | 3 | Health intelligence for corporate health plans; started as a habits app ([Revista Apólice](https://www.revistaapolice.com.br/2022/07/wellbe-aposta-em-nova-area-de-gestao-de-saude-para-clientes/), [Startupi](https://startupi.com.br/tags/wellbe/)). |
| 7 | `iMND HealthTech` (1) | imndsaude · Rio de Janeiro | **iMND** | IN | 1 | Online physical and mental health care for companies, brokers and insurers (App Store; [imnd.com.br](https://imnd.com.br)). |
| 8 | `Nilo` (8), `Nilo Saúde` (3); advisors on `MGL Consultoria` and `Aché Laboratórios` rows | nilo-saude · 110 staff | **Nilo Saúde** | IN | 13 | AI and automation for health institutions; care journeys on WhatsApp or video; HL7 FHIR APIs ([nilosaude.com.br](http://nilosaude.com.br)). |
| 9 | `Liti` (7); advisor on the `Find.AI` row | liti-saúde · 70 staff | **Liti** | IN | 8 | Online obesity programme; app with connected-scale readings, prescriptions and medication delivery (App Store 4.56.0, 2026-10-02). Partial overlap. |
| 10 | `MedTrue - Health Tech` (2) | medtrue · 14 staff · founded 2025 | **MedTrue** | IN | 2 | MedSlim: online start with virtual medical follow-up, treatment at licensed units ([MedSlim](https://emagrecer.soumedslim.com.br)). |
| 11 | Magrass unit pages (10 rows), no-page Magrass rows (4), `G3 Treinamento Personalizado` (1) | eight unit pages; no franchisor page | **Magrass** | IN | 14 (+1 duplicate) | Weight-loss and aesthetics franchise, all units franchised, HQ in Santa Catarina, Magrass Club app ([franchise listing, 09/2026](https://franquias.portaldofranchising.com.br/franquia-magrass-estetica/)). Partial overlap. |
| 12 | `Emagrecentro Centro de Emagrecimento e Estética` (2) | page HQ Curitiba, 20 staff | **Emagrecentro** | IN | 2 | Weight-loss franchise on the Método 4 Fases, founded in São Bernardo do Campo ([Portal do Franchising, 2025-11-27](https://www.portaldofranchising.com.br/noticias/emagrecentro-forca-e-inovacao/)); client app (App Store, 2025-06-24). Partial overlap. |
| 13 | `Instituto GL` (1) | instituto-gl · 39 staff | **Instituto GL** | IN | 1 | Medical weight-loss clinic with units in Moema and Tatuapé ([institutogl.com.br](https://www.institutogl.com.br)). |
| 14 | `Grupo Endos` (1) | grupo-endos · 18 staff | **Grupo Endos** | IN | 0 (company-named row, held) | Endoscopic obesity treatment and injectable weight-loss therapies ([endosfit.com.br](https://endosfit.com.br/)). |
| 15 | `Amparo Saúde` (3) | amparo-saude · 164 staff | **Amparo Saúde** | IN | 2 (+1 company-named, held) | Primary-care clinic network with remote and in-person care and its own telehealth centre (LinkedIn); part of Grupo Sabin since 2021 ([Exame](https://exame.com/negocios/grupo-sabin-compra-rede-de-atencao-primaria-amparo-saude/)). |
| 16 | `Abertta Saúde` (1) | aberttasaude · 538 staff | **Abertta Saúde** | IN | 1 | Self-managed employee health plan with its own Health Promotion Centres and app (App Store 3.5.4, 2026-09-28). |
| 17 | `Pró-Corpo \| Estética Avançada` (9 of its 10 rows; the tenth is Silbia Díaz, a collision), `Pró-Corpo Estética Avançada` (1); the page also carries two other collisions (row 49) | pro-corpo-estetica · 398 staff · HQ São Paulo | **Pró-Corpo** | IN | 9 (+1 company-named, held) | Aesthetics and plastic-surgery chain of owned units in São Paulo, Rio, Londrina, Santos and Campinas (LinkedIn; [procorpoestetica.com.br](http://www.procorpoestetica.com.br)). §9. Its founder's bio says the units are owned, so the "Proprietário / Empreendedor / Empresária" rows get identity checks. |
| 18 | `Siluets Estética ` (5), `Siluets Franchising` (2), `Siluets Estética` (2); no page: `Siluets Estética Aracaju`, `Siluets Estética Unidade Santo André`, `Siluets Estética` (1 each); 2 `Mulher Estética` rows are collisions (row 49) | siluetsestetica · website on the page is an unrelated fertility clinic | **Siluets** | IN | 7 (+5 company-named, held) | Aesthetic franchise, "a 1ª Franquia a combinar a Fotodepilação (IPL) com tratamentos corporais e emagrecimento" (LinkedIn). Franchisor status unverified: siluets.com.br did not resolve on 2026-10-05 and the latest press found is from 2017-2018 ([Portal do Franchising](https://www.portaldofranchising.com.br/noticias/siluets-franchising-apresenta-dois-modelos-de-negocios-no-abf-expo/)). §9. |
| 19 | `LIPOCENTER FRANQUIA` (3); no page: `lipocenter` (2), `Lipocenter Perdizes` (1), `Lipocenter` (1) | lipocenter-franquia · 73 staff | **Lipocenter** | IN | 6 (+1 company-named, held) | Weight-loss and aesthetics franchise, founded in 2005 as an Instituto de Emagrecimento (LinkedIn). Franchisor status unverified: lipocenter.com.br did not resolve on 2026-10-05, no press found. |
| 20 | `Face Doctor Franchising - Oficial` (1) | facedoctor-franchising · 124 staff | **Face Doctor** | IN | 1 | Premium franchise for facial and body rejuvenation (LinkedIn). §9. |
| 21 | `N2B Brasil` (1 on page, 1 no page) | n2b-brasil · São Paulo | **N2B Brasil** | IN (partnership) | 2 | MyNutri: in-gym body-composition kiosks with an app ([n2bbrasil.com](http://www.n2bbrasil.com)). Body composition is its own product: partnership ask only. |
| 22 | `Clínica da Obesidade` (1, no page), `Hotel A Casa das Portas Velhas` (1: Indira Cruz), `Viva Salute` (1: Ulysses Maciel) | none | **Clínica da Obesidade** | IN | 3 (with checks) | Weight-loss clinic named on all three rows; which "Clínica da Obesidade" it is cannot be told from the rows. The validator identifies it before send. |
| 23 | `Grupo 5S - Serviços, Produtos, Franchising e Tecnologia` (2, the same person twice), `Brand's` (1: the CEO) | 5sgrupo · 11 staff | **Grupo 5S** | IN | 2 (+1 duplicate) | A holding that makes nutraceuticals for weight loss and runs franchise brands (LinkedIn). Risk: Brazil's Federal Nutrition Council published the professional association's 2017 technical opinion rejecting its weight-loss method ([CFN](https://cfn.org.br/parecer-tecnico-da-asbran-reprova-metodo-5s/)); copy never references the method. |
| 24 | `Instituto Lumiere` (1) | instituto-lumiere · São Luís | **Instituto Lumiere** | IN | 1 | Weight-loss and nutrology centre; nutrition plan in an app ([institutolumiere.com.br](https://institutolumiere.com.br/lumiere/)). Its site also lists in-clinic body-composition assessment: overlap, not displacement. |
| 25 | `RWE Telemedicina e Diagnósticos` (7) | rwe-telemedicinaediagnosticos · 87 staff | **RWE Telemedicina** | IN (partnership) | 6 (+1 duplicate) | Tele-diagnostic reports and medical equipment on loan for clinics and hospitals (LinkedIn). |
| 26 | `Telecárdio` (5) | telecárdio · 85 staff | **Telecárdio** | IN (partnership) | 5 | Telemedicine since 1993: remote ECG, EEG, spirometry, Holter and blood-pressure monitoring reports by cardiologists, 24 hours a day (LinkedIn). |
| 27 | `L2D Saúde Digital` (3), `L2D Telemedicine Network` (1) | l2dsaudedigital · 71 staff | **L2D Saúde Digital** | IN | 4 | Telehealth since 2016 with its own teleconsultation platform and 24-hour support for doctors and care units (LinkedIn); l2d.com.br did not resolve. |
| 28 | `Llamando al Doctor` (3), `Llamando Al Doctor` (1) | llamando-al-doctor · 106 staff · Buenos Aires | **Llamando al Doctor** | IN | 4 | Immediate video consultations 24 hours a day, serving Latin America, Europe and the US in three languages (LinkedIn; [llamandoaldoctor.com](https://www.llamandoaldoctor.com)). |
| 29 | `Reliv` / `Reliv - Healthcare made simple` / `Reliv \| 500 LatAm B15` (3) | reliv-healthcare · 37 staff · Quito | **Reliv** | IN | 3 | A digital ecosystem connecting patients with doctors, hospitals, pharmacies, labs and insurers, in Ecuador and Mexico (LinkedIn). |
| 30 | `holadr. IPS` (2) | holadr-ips · Medellín | **holadr. IPS** | IN | 2 | Interactive telemedicine across specialities including nutrition and occupational medicine (LinkedIn; [holadr.com.co](https://holadr.com.co/)). |
| 31 | `Céntriqo - Centro Médico Integral` (1), `Quirurgic - Centro de Cirugía Ambulatoria` (1) | centriqouio · 27 staff · Quito · founded 2026 | **Céntriqo** | IN | 2 | Integrated medical centre: specialist consultations, day hospital, ambulatory surgery, laboratory, imaging, physiotherapy, pharmacy (LinkedIn). |
| 32 | `TELUS Health Brazil` (1, no page), `CARE by TELUS Health`, `Chestnut Global Partners do Brasil`, `Care Global Partners` (1 each) | telus-health-by-care · 56 staff · São Paulo | **TELUS Health Brazil** | IN (partnership) | 3 (+1 company-named, held) | Employee assistance, plus health coaching, post-check-up coaching and physical-activity coaching (LinkedIn specialities). The Brazilian operation of a Canadian group; Canada is no profile's market, and the Brazilian entity is recorded under its own name. |
| 33 | `Grupo Wellness Latina` (2), `grupowellnesslatina ` (1) | grupowellnesslatina · Argentina | **Grupo Wellness Latina** | IN (partnership) | 3 | Employee assistance across Latin America, with wellness programmes and habit-change coaching (LinkedIn; [grupowellnesslatina.com](http://www.grupowellnesslatina.com)). |
| 34 | `Saluta - Centro de Innovación en Salud` (2), `Saluta - Centro de Salud Digital` (2) | salutadigital · 79 staff · Santiago | **Saluta** | IN (partnership) | 4 | Mental health through an app and telemedicine (LinkedIn). |
| 35 | `Zínea` (2) | zinea-saudemental · 83 staff | **Zínea** | IN (partnership) | 2 | Mental-health management at work (LinkedIn). |
| 36 | `Terapia Online` (1, CL); the Brazilian `Terapia Online` row is a collision (row 49) | terapiaonline-cl · Santiago | **Terapia Online** | IN (referral) | 1 | Psychology and other mental-health specialities by telemedicine, nutrition among them (LinkedIn). |
| 37 | `Sensorial` (2), `Sensorial Sports` (1) | sensorialhealthtech · Ribeirão Preto | **Sensorial** | IN (partnership) | 3 | Neuroscience-based technology for health and cognitive performance, up to sports performance (LinkedIn). Health-related, so in. |
| 38 | `GnTech - Saúde Personalizada` (1), `GnTech` (1) | gntechtests · Florianópolis | **GnTech** | IN (partnership) | 2 | Pharmacogenetic testing, "Saúde personalizada" (LinkedIn). |
| 39 | `SPDM - Associação Paulista para o Desenvolvimento da Medicina` (1) | spdmoficial · 19,721 staff | **SPDM** | IN (referral) | 1 | Philanthropic association running primary, secondary and tertiary care (LinkedIn); the person is technical director of an outpatient centre for older people. |
| 40 | `Inc Beauty Dermatology Institute` (1) | inc-beauty-dermatology-institute · 3 staff | **Inc Beauty** | IN (referral) | 1 | Dermatology institute for regenerative and aesthetic skin, hair and body treatments (LinkedIn). §9. |
| 41 | `Ihealthy Centro Estetico Integral` (1, EC) | none | **Ihealthy** | IN | 1 | Aesthetic centre (name on the row); its partner-manager also runs an outpatient-care company. §9. |
| 42 | `Perfect clinic` (1, CO) | none | **Perfect clinic** | IN (referral) | 1 (identify first) | Clinic named on the row; type unknown. The validator identifies it before send. |
| 43 | `Clínica Lev Vida` (1) | none | **Clínica Lev Vida** | IN | 0 (company-named row, held) | Single clinic; the only row is the clinic's own profile. |
| 44 | `Spring Health` (1) | spring-health · New York | none | **OUT** | 0 | US headquarters: one company, one profile, and the US belongs to `nick`. |
| 45 | `Takahashi Centro Oftalmológico` (1) | 4 staff | none | **OUT** (noise) | 0 | A four-person eye clinic where body measurements play no part; treated as a one-person practice. |
| 46 | `Microsoft`, `Bank of America`, `ArcelorMittal Brasil`, `Softplan`, `PrimeUp`, `Soluciones Activ` (AR), `REVOS - AOS` (CL) | various | none | **OUT** (noise) | 0 | Non-health companies. |
| 47 | `M F Ferro consultoria`, `Mucipalidad Las Heras, Mendoza` (AR) | none | none | **OUT** (noise) | 0 | Former staff of IN accounts now elsewhere (Magna Ferro, ex-Salvia; Sebastian Follis, ex-AxisMed in Argentina). |
| 48 | `Clínica Carolina Malta`, `mi consultorio`, `consultorio` (AR) | none | none | **OUT** (noise) | 0 | One-person practices. |
| 49 | Name collisions (19): `liti` (AR), `GRUPO LITI`, `3GFOODS`, `Nilo` (CO: Claudia Posada), `Psiu Artesanato`, `Psiu Design` (2), `Psiu Consultoria`, `Psiu Class`, `Sensorial Informática`, `Sensorial Club`, `Sensorial Stick`, `sensorial moda` (CO), `Pró Corpo Plástica e Estética` (AR), Silbia Díaz on the Pró-Corpo page (UY), `Clarear O estetica`, `Mulher Estética` (2), `Terapia Online` (BR: Cristina Nanin) | none or wrong page | none | **OUT**, people FAIL | 0 | A different business with a similar name. Four of them match an IN group's name key in `extract-people` and must be failed by name: Marta Larti (`liti`), Claudia Posada (`Nilo`), Cristina Nanin (`Terapia Online`, Brazil) and Silbia Díaz (`Pró-Corpo \| Estética Avançada`, Uruguay). |

**Totals:** 43 IN groups, 163 people to send from 41 of them. Held at validation, company-named rows with no person's name: 12. OUT: 33 (14 noise, 19 name collisions). Duplicates: 3. 163 + 12 + 33 + 3 = 211.

**Re-grouped rows** (step 2 writes them with the IN company's name and URL, so `record` registers the IN company and never the row's company):
- Nadia Panow → Vidalink. Alejandro Gorissen and Silvia Lima → Atrys Brasil. Luiz dos Santos Nunes Filho → Magrass (row G3; he co-owns Magrass Moinhos de Vento). Sandra Geres Alves Panza, Gabriela Biazus, Renata Assuncao → Magrass. Lívia Sales, Elaine Tadiello → Siluets. Milena Espinha, lisete espindola, Mônica Melli → Lipocenter. ligia antunes pinto ferreira → TELUS Health Brazil. Fabrícia Dias → N2B Brasil. Dra Edivana Poltronieri → Grupo 5S (row `Brand's`; her headline: "CEO Grupo 5S").
- **Clínica da Obesidade:** Jacques Maciel (no page); Indira Cruz (row is a hotel; headline "Gerente Operacional na CLÍNICA DA OBESIDADE"); Ulysses Maciel (row is Viva Salute, where he is CEO; his experience also lists "Diretor executivo at CLINICA DA OBESIDADE"). Indira Cruz and Ulysses Maciel are sent only if the validator finds the clinic role current; otherwise they FAIL as former staff.
- **Advisors, `referral` only, after a current-role check** (precedent: Superpower's medical advisor, 2026-09-29): Ana Claudia Pinto → Liti; Fabio Katayama and Rafael L. Ribeiro → Nilo Saúde; Graziela Heusser Azeredo → Zínea. If the role cannot be confirmed as current, the person is held, not failed.

**Rows the validator must resolve before send (each has a branch):**
- **Gabriela Biazus** ("Sócia-fundadora at Magrass", no unit named, no page, a nutrition degree). If she is a founding partner of the franchisor, move her to `product` P1 and use her as the HQ path; if she co-owns a unit, she stays `referral` P4; if neither can be shown, hold.
- **Flaminio Dalul** ("Sócio proprietário at Siluets Franchising", headline "Siluets rio preto"). The headline points to the Rio Preto unit, so default `referral` P4; if the validator finds a franchisor role, move him to `product` P2.
- **aline caio** ("Diretor at LIPOCENTER FRANQUIA", the franchisor's page, no unit named). Default `referral` P4; if the validator finds a franchisor role, move her to `operations` P2.
- **Emagrecentro:** if Viviane Lins or Wesley Denardin works for the franchisor rather than a unit, move that person to `operations` P1.
- **Clínica da Obesidade and Perfect clinic:** identify the clinic (site, location, type). If it cannot be identified, hold its people; if it is not a health clinic, they FAIL as wrong company.
- **Pró-Corpo:** Patricia Coutinho (CEO title, with "Atendente at Pró-Corpo" as her only other role) and the five owner-titled rows with empty profiles (Solange Bader, Clovis Clodovil, Josemar Silva, Michelly Carneiro de Araujo, Rita Santos), since Pró-Corpo's units are owned. Unconfirmed rows are held.

**Company-named profiles (no person's name, so no greeting is possible), held at validation:** GRUPO ENDOS (Grupo Endos); AxisMed Telefónica (Atrys Brasil); Amparo Agência de cuidados (Amparo Saúde); Siluets Casa Verde, Siluets Estética Unidade Brooklin, Clínica Siluets Vila Nova, Siluets Estética Unidade Santo André, Dermish Clínica médica e estética (Siluets); Lipocenter Emagrecimento E Estética (Lipocenter); Clínica Ferraz Ferraz (Pró-Corpo); Eap Brasil (TELUS Health Brazil); Clínica Lev Vida. Sent only if the validator can name the person behind the profile; then `referral` P4 (`product` P2 for Grupo Endos and Clínica Lev Vida).

**Duplicates (FAIL):** `sandra-panza` (keep `sandra-geres-alves-panza-89323611a`, Magrass Maringá); `paulo-almança-5215083b2` (keep `paulo-almança-4bb7026a`, Grupo 5S); `luana-barreto-139b8638b` (keep `luana-barreto-43819922b`, RWE, whose headline names her commercial role).

### What the accounts with verified body data already have (2026-10-05)

| Account | Verified (source) | Not verified: never claim either way | What FitXpress offers |
|---|---|---|---|
| **Liti** | The connected scale "envia automaticamente suas pesagens ao seu time de saúde", and the app shows weigh-ins and indicators "como percentual de gordura corporal, massa muscular e gordura visceral" (App Store "Liti Saúde" 4.56.0, 2026-10-02). A bioimpedance scale is sent to the patient ([Bloomberg Línea, 2023-06-14](https://www.bloomberglinea.com.br/2023/06/14/na-onda-ozempic-esta-startup-elegeu-como-foco-o-sobrepeso-e-a-obesidade/)). A 2023 review (modified 2024-03-20) lists a measuring tape, a food scale and a bioimpedance scale in the "Litibox" kit, and the app as showing "o progresso das suas medidas" ([Vitat](https://vitat.com.br/liti-vale-a-pena-assinar/)). | Whether measurement tracking is still part of the programme in 2026; which measurements; progress photos. | Partial overlap. The capability is the guided two-photo capture and what it returns, inside the Liti app. |
| **Magrass** | Magrass Club: "registrar cada refeição, acompanhar a evolução de peso e medida", recipes from Magrass nutritionists ([franchise listing, 09/2026](https://franquias.portaldofranchising.com.br/franquia-magrass-estetica/)); follow-up by "a nutricionista da sua unidade Magrass" (App Store "Magrass Club" description). | How units take measurements; any in-unit body-composition device; the app's current version (iOS listing last updated 2022-03-07). | Partial overlap. A guided capture clients take at home between unit visits, inside Magrass Club. |
| **Emagrecentro** | Its peer-reviewed study of the Método 4 Fases reports weight, BMI and waist from client records ([Healthcare, 2022, PMC9332815](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9332815/)). Its app: "Acompanhe sua evolução na Clínica Emagrecentro e veja todos os seus resultados" (App Store, 2025-06-24). The founder: technology "nos permite manter o mesmo padrão de atendimento em todas as clínicas" ([Portal do Franchising, 2025-11-27](https://www.portaldofranchising.com.br/noticias/emagrecentro-forca-e-inovacao/)). | How waist is measured in clinics today. | Partial overlap. The same guided capture in every clinic and at home, inside its app (tied to the founder's own point). |
| **N2B Brasil** | MyNutri: body-composition kiosks in gyms, exam history comparable over time, menu suggestions by goal, inside an app ([n2bbrasil.com](http://www.n2bbrasil.com)). | Anything beyond the site. | Body composition is its product. Partnership ask only. |
| **Instituto Lumiere** | Its site lists body-composition assessment in the clinic, blood tests, a sleep assessment, a strength test and a nutrition plan in an app ([institutolumiere.com.br](https://institutolumiere.com.br/lumiere/)). | Which app the nutrition plan uses. | Overlap, not displacement. A record patients take at home between visits. |
| **Everyone else** | Nothing body-related verified. | What they record today. | The capability only. |

**Displacement check:** a search of each IN account's site, App Store listing and press for a phone-camera body scan, a body-scan vendor or a 3D body model found none on 2026-10-05. Not every source could be read: gesmed.com.br, atrys.com.br, l2d.com.br, siluets.com.br, lipocenter.com.br and 5sgrupo.com.br did not resolve, emagrecentro.com.br returned 403 and reliv.la returned 429. For those accounts the check rests on App Store listings, LinkedIn and press only. The validator repeats the check before import.

## Use case (1 sentence)

Inside its own app or patient flow, a Latin American health programme (a weight-loss programme or clinic network, a corporate or health-plan care platform, a telehealth service or an aesthetic clinic chain) asks the person for a guided two-photo scan and receives 80+ body measurements (waist and hip included), body composition estimates and a 3D model in under 45 seconds from the photos to structured results: a standardized, timestamped body record that its care team, nutritionist, doctor or evaluator compares across scans it selects, with nothing to ship.

## Why this is plausible (evidence)

1. **GLP-1 treatment became cheaper, national and employer-funded in Brazil in 2026, so programmes carry patients through months of treatment.** Semaglutide and liraglutide have no patent protection in Brazil; 25 weight-loss pens are registered, 14 of them in 2026, including nationally produced and generic versions; prices fell 70% in under a year; and in September 2026 the Ministry of Health asked Conitec to assess them for the public system ([Agência Gov](https://agenciagov.ebc.com.br/noticias/202609/ministerio-da-saude-protocola-na-conitec-pedido-de-analise-para-incorporacao-de-canetas-emagrecedoras-no-sus), fetched 2026-10-05). On 2026-06-02 the first Brazilian semaglutide pen was announced "com preços a partir de R$ 452 e chegada às farmácias em 15 de junho" ([Olhar Digital](https://olhardigital.com.br/2026/06/02/medicina-e-saude/ems-anuncia-precos-da-primeira-caneta-nacional-de-semaglutida/), article text fetched 2026-10-05). Accounts on this list moved with it: Vidalink launched Vidalink+ Peso Saudável, "o primeiro benefício corporativo focado em canetas emagrecedoras" ([Vidalink](https://conteudo.vidalink.com.br/vidalink-peso-saudavel)); Magrass sells "Medicina Evolutiva", whose formula names a GLP-1-class drug ([franchise listing](https://franquias.portaldofranchising.com.br/franquia-magrass-estetica/)); Liti's app now handles prescriptions and medication delivery (App Store 4.56.0, 2026-10-02). Context for Katya; no numbers and no drug or pharma names in copy.
2. **The obesity burden is large and growing, and the programmes already treat body measurements as a progress record.** Vigitel 2025: obesity reached 25.7% of adults and excess weight 62.6% in 2024, against 42.6% excess weight in 2006 ([Afya, on Vigitel 2025](https://portal.afya.com.br/saude/vigitel-2025-aponta-piora-do-sono-entre-brasileiros-e-avanco-de-doencas-cronicas)). Emagrecentro's peer-reviewed study reports its method's results in weight, BMI and waist ([Healthcare, 2022](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9332815/)); Magrass Club tracks "evolução de peso e medida"; Liti's kit has carried a measuring tape and a bioimpedance scale ([Vitat](https://vitat.com.br/liti-vale-a-pena-assinar/)). The Lancet Diabetes & Endocrinology Commission on clinical obesity (January 2025) says excess adiposity should be confirmed by direct body-fat measurement or by at least one anthropometric criterion (waist circumference, waist-to-hip or waist-to-height ratio) in addition to BMI ([Lancet Diabetes & Endocrinology](https://www.thelancet.com/journals/landia/article/PIIS2213-8587(24)00316-4/fulltext); as verified for `2026-09-29-us-cardiometabolic`). FitXpress body composition values are estimates and are never presented as the direct body-fat route.
3. **These programmes already run their own apps or remote flows, and a phone capture needs no device.** Vidalink, OrienteMe, Salvia, GESmed (AppGES), iMND, Abertta, Liti, Magrass (Magrass Club) and Emagrecentro publish member apps (App Store, checked 2026-10-05); Nilo runs journeys on WhatsApp and video and integrates through HL7 FHIR APIs; L2D builds its own teleconsultation platform; Llamando al Doctor runs video consults through an app and the web; Pró-Corpo sells treatments online before an in-person evaluation. FitXpress ships as an API with web and mobile SDKs, white-label inside the host flow (`tech-spec.md`). Franchise networks need the same record taken the same way in every clinic: Emagrecentro's founder says technology "nos permite manter o mesmo padrão de atendimento em todas as clínicas".
4. **What FitXpress brings, with its limits.** From `proof-points.md`: two photos (front and side); under 45 seconds from the photos to structured results; 80+ body measurements; body composition outputs (BMI and BMR as calculated metrics; fat %, lean mass, fat mass as estimates); typical scan-to-scan differences under 1 cm for most evaluated measurements; white-label API and SDK. Honest limits: no visceral fat output; no published comparison of the body composition estimates with bioimpedance or any reference method; validation population 38-210 kg; training data from the US and Europe ("Locations: US, Europe", `proof-points.md`), so performance on Latin American populations has not been characterized separately; no Latin American customer; no Portuguese or Spanish wording. The nearest proof is an anonymised weight-management platform that ran 34,000 scans in 2025, and 3DLOOK-wide scale of 112,100 scans in 2025.

## What Katya's last campaign and the recent QCs teach this one

From `2026-07-23-israel-telehealth/post-mortem.md` and `metrics-final.json`, the QC reports of `2026-09-29-us-cardiometabolic`, `2026-10-02-us-virta-health` and `2026-08-14-au-digital-fitness`, and this campaign's own QC (`_quality/outbound/2026-10-05-hypothesis-generator-latam-health-weightloss.md`, 15/20, 21 fixes applied below):

- **Katya's account accepts well; replies come from the first message.** 38 of 127 accepted (29.9%); 4 replies on 73 messages; first message 15.4% against follow-ups 2.3% across both Israel sends. Message 1 carries the weight.
- **A third of Israel's repliers said "wrong person".** Here 95 of 163 people are `referral` by design, each with one "who owns X" question, so a "wrong person" reply still names an owner.
- **Overlap is verified per account and quoted, and copy never lists a prospect's data before adding ours** (this QC, fixes 5-6).
- **Card wording leaked into copy on 2026-10-02.** Every instruction now sits in a "Writer notes" column, apart from the facts and questions; "generic figure", "never a promise", "not a promise" and "context only" are banned terms, so a leak fails the gate (this QC, fixes 12-14).
- **Same-company near-duplicates were the top QC issue on both 2026-10-02 runs.** Every person has an assigned hook and a question only they get; peer groups are named.
- **Employer data and the pen benefit are hard lines** (this QC, fixes 1-4): no Vidalink copy touches Peso Saudável, and no question routes body data to HR, employers or health-plan analytics.
- **Name-alikes are failed by name** (Psiu, Sensorial, liti, Nilo, Pró Corpo outside Brazil), never matched on a company name.

## Target buyer persona

**Who buys:** the owners of the member or patient app, of the care, nutrition or evaluation model, and of operations at each IN account. At franchise networks the buyer is the franchisor (HQ), which owns the client app and the protocol; unit owners and unit staff are referral paths to HQ. At tele-diagnostics, employee-assistance, mental-health, body-composition, genetics and cognition companies there is no buyer for this use case: their leaders get a partnership ask. Tiers only order the list; everyone goes in one import file (standing decision). Lanes are defined in "Message angle"; each person's hook and question are there too.

**P1, owners at the core accounts (15):**
- Vidalink (4): Luis Gonzalez, CEO and co-founder (`product`); Edson Ferreira Augusto Corrêa, Senior Product Manager, AI & Intelligent Systems (`product`); Jorge Sousa, COO (`operations`); Eliane Simeão, Diretora de Operações (`operations`).
- OrienteMe (3): Bruno Haidar, CoFounder & CEO (`product`); Fernanda Maluf, Co-Founder (`product`); Fernanda Mondin, Head of Nutrition (`clinical`).
- GESmed (1): Fernando Marques, Sócio Fundador e CEO (`product`). Salvia (1): Mirian Maria Marques Pinheiro, CEO (`product`). Atrys Brasil (1): Tiago Vieira, Diretor Executivo (`product`). Wellbe (1): Lucas Vieira Werner, Co-founder & CTO (`product`). Nilo Saúde (2): Victor Marcondes, Founder; Rafael Alves Martins, Head of Product (both `product`). Liti (1): Fernando Vilela, Co-Founder (`product`). MedTrue (1): Lucas Quintella, CEO (`product`).

**P2, programme leads at the core and owners at the widened direct-use accounts (20):**
- Core leads (5): Karen Ribeiro, Vidalink (`operations`); Thiara Amanda Corrêa de Almeida, GESmed (`operations`); Marcela Ferreira Lima Guimarães, GESmed (`clinical`); Lucas Lau, GESmed (`operations`); Carolina Beltramini, Nilo Saúde (`operations`).
- Aesthetic chains (4): Marisa Peraro, Founder, Pró-Corpo (`product`); Patricia Coutinho, CEO, Pró-Corpo (`product`, identity check); Simone Fatima Amaral Martins, gestora geral, Pró-Corpo (`operations`); Javier Rhea, socio gerente, Ihealthy (`product`).
- Weight-loss clinics (3): Jacques Maciel, Diretor, Clínica da Obesidade (`product`, clinic to identify); Dra Edivana Poltronieri, CEO, Grupo 5S (`product`); Abilio Costa, owner, Instituto Lumiere (`product`).
- Telehealth and medical centres (8): Janiel José Zioti, group executive director, and Lucas Schneider, COO, L2D (`product`, `operations`); Guillermo Gonzalez, CEO, and Ricardo Gordillo, COO, Llamando al Doctor (`product`, `operations`); Paola Almeida, co-founder and COO, and Sebastián Guarderas-Castro, CMO, Reliv (`product`, `clinical`); Paola Cristina Giraldo Osorio, CEO, holadr. IPS (`product`); Martin Samaniego, CEO, Céntriqo (`product`).

**P3, technical and partnership (33):**
- Technical (17): Vidalink: Tiago Soares, Daniela Junqueira, Bruno Menendes, Lucas Mateus Silva de Souza; OrienteMe: Alessi Soncini; Nilo Saúde: Cesar Nobre, Diego Freire, Rodolfo Stangherlin, Iasmini Gomes, and Filipe Firmino (`operations`); Liti: Bruno Silva, Maycon Soligo, William Weckl; Wellbe: William Bin Falinski; L2D: Fernando P.; Llamando al Doctor: Martín Lucas Golini; Reliv: Mauricio Padilla. All `technical-integration` except Filipe Firmino.
- Partnership (16, all `partnership`): RWE Telemedicina: Vinicius Cuerci de Souza, Luana Barreto, Emerson Goulart, Eduarda Cuerci; Telecárdio: Roberto Stryjer, Marcelo Lapa Espiga, Alexandre Pimentel; TELUS Health Brazil: ligia antunes pinto ferreira; Grupo Wellness Latina: Andrea Lardani; Saluta: Luis Hincapié, María Alejandra Silva Castro; Zínea: Anderson Baldissera; N2B Brasil: Fabrícia Dias, João Murackami; GnTech: Paula Pedrassani Boabaid May; Sensorial: Milton Ávila.

**P4, referral (95):** people who do not own the app, the care model or a partnership decision get a short ask for the owner. Order inside P4: franchisor paths first, then advisors, then the rest.
- Franchise units and Pró-Corpo staff (36): Magrass 14 (Marina Michaelsen Deriggi, Marcio Jorge Pinho Deriggi, Janaina Possebon, Luiz dos Santos Nunes Filho, Fabricio Pires, Rodrigo Baroni, Rafaela Klein, Regina Alves Ribeiro, Roberta Mascarenhas, Tami Bianca, Rhúã Robson D´Cézares Rodrigues de Oliveira das Chagas Netto, Sandra Geres Alves Panza, Gabriela Biazus, Renata Assuncao); Siluets 7 (Flaminio Dalul, Adrielle Dalul, Meire Satelite, Jackeline Lopes, Regiane Viana de Oliveira, Lívia Sales, Elaine Tadiello); Lipocenter 6 (aline caio, Sandra Baldassari, Cristiane Aguilar, Milena Espinha, lisete espindola, Mônica Melli); Emagrecentro 2 (Viviane Lins, Wesley Denardin); Face Doctor 1 (Monique Diana Martins); Pró-Corpo 6 (Andreza Zatorre Pereira, Solange Bader, Clovis Clodovil, Josemar Silva, Michelly Carneiro de Araujo, Rita Santos).
- Advisors (4, after a current-role check): Ana Claudia Pinto, MD, PhD (Liti); Fabio Katayama, Rafael L. Ribeiro (Nilo Saúde); Graziela Heusser Azeredo (Zínea).
- Core and clinic accounts (35): Vidalink 9 (Alessandro Dourado da Silva, Daniel Oliveira, Abi Nogueira, Aline Dos Santos, Paulo Gonçalves, Nadia Panow, Susana Augusto de Camargo Silva, garga Mel, Renan Schonton); OrienteMe 3 (Renata Tavolaro, Maurício Lima, Jessica Rayane); Salvia 2 (Bárbara Carvalho, Renise M.); Atrys Brasil 4 (Alejandro Gorissen, Luciana Ito, Matheus Rodrigues, Silvia Lima); Nilo Saúde 3 (Vitor Honda, Steffany C., Geovana Dorys); Liti 3 (Rodrigo Casale Abe, Ana Paula Moraes, Gabriela Teixeira); Wellbe 1 (Sidnei Salmaso); iMND 1 (Isabelle Ferraz); MedTrue 1 (Ramon Guedes); Instituto GL 1 (Arthur Silva Da Ros); Amparo Saúde 2 (Paty Marques, Marcus Nunes); Abertta Saúde 1 (Daniele Araujo); plus Clínica da Obesidade 2 (Indira Cruz, Ulysses Maciel, current-role checks), Grupo 5S 1 (Paulo Almança) and Perfect clinic 1 (Valentina Sanabria, clinic to identify).
- Widened accounts (20): RWE Telemedicina 2 (Paulo Castilho, Carlos Coelho); Telecárdio 2 (Flavio Svaiter, Amanda Micaela Alves); L2D 1 (Juliana Faure); Llamando al Doctor 1 (Viviana Salazar); holadr. IPS 1 (Ana Maria Restrepo Gomez); Céntriqo 1 (Natalia Dezerega Molina); TELUS Health Brazil 2 (Sonia Maria Figueiredo, Carlos Prestes); Grupo Wellness Latina 2 (Ángeles Dubini, Jimena Maldonado de Chazal); Saluta 2 (Ricardo Perales Aravena, Gabriela Galvis); Terapia Online 1 (Rodrigo Alvarez Diaz); Sensorial 2 (Victor Cavallari, Kevin Lucas); GnTech 1 (Adriano Oliveira); SPDM 1 (Adriana Bottoni); Inc Beauty 1 (Paula Tecchio).

**Held at validation (12 company-named profiles):** listed under the verdict table.

**Checks the validator runs by name:** the six branches under the verdict table (Gabriela Biazus, Flaminio Dalul, aline caio, Emagrecentro, Clínica da Obesidade and Perfect clinic, Pró-Corpo identities); identity checks on garga Mel and Renan Schonton (Vidalink), Geovana Dorys (Nilo), Fabricio Pires and the one-line Magrass profiles; current-role checks on the four advisors, Indira Cruz and Ulysses Maciel; Martin Samaniego (CEO of Céntriqo; his experience also lists "CEO at Reliv": he goes to Céntriqo only, and never gets Reliv copy); the three duplicates. A job-change check runs on all 163.

**Not the buyer (FAIL for the cold send):** only the 33 OUT rows (verdict rows 44-49: Spring Health, Takahashi, non-health companies, former staff, one-person practices, name collisions) and the 3 duplicates. Every function at an IN company has a lane.

**KPIs they care about:** for Vidalink, client companies adopting Bem-estar 360º; for care platforms, engagement between consultations and health-plan cost; for Liti, MedSlim and the clinics, patients staying through treatment; for franchisors, the same standard of care in every unit; for telehealth, consult quality and time; for aesthetic chains, the free evaluation converting into a treatment plan; for partnership accounts, what they can offer their own clients.

**Likely objections and the honest answer:**
- "We already measure: our scale gives body composition, our nutritionists or evaluators take measurements, we run bioimpedance" (Liti, Magrass, Emagrecentro, Instituto Lumiere, N2B, most clinics). True, and nothing replaces it. There is no published comparison of FitXpress estimates with bioimpedance or with staff measurements; a pilot can compare them in the same people. Never suggest their scale or their staff's measurements are wrong.
- "How accurate is it?" "96-97% accuracy against expert manual measurement" describes body measurements, not body composition; or the full `accuracy-formulations.md` §1.1 sentence; repeatability as the §1.2 sentence; validation population 38-210 kg, training data from the US and Europe; "Performance outside this scope has not been characterized."
- "LGPD? Our country's data-protection law? Where is the data?" Cold copy says nothing about it (default). In a reply: the data lifecycle from `compliance.md` §3 and §10 (photos deleted after processing or within 30 days, faces obscured at capture, outputs stored until deleted by scan ID, hosting on AWS in US-West-2 and partly US-East-1), and legal@3dlook.me for any national-law or international-transfer question. Never claim compliance with any Latin American law (Open question 2).
- "Is this a medical device? Does ANVISA (or our regulator) need to approve it?" In a reply only: "An independent regulatory assessment concluded that FitXpress does not meet the definition of a medical device under the UK Medical Devices Regulations 2002 (UK MDR) or the EU Medical Devices Regulation (EU MDR)." It says nothing about Latin American rules; nobody improvises one.
- "Can it decide who gets a benefit, a treatment or a procedure?" No. FitXpress does not decide eligibility, diagnose or recommend treatment (`compliance.md` §7).
- "Price? In reais or pesos?" Never in copy; a call question.
- "We are a franchise unit, not HQ." Correct: the referral asks who at the franchisor owns the app or the protocol.
- "Why would a mental-health (or diagnostics, or EAP) company want body scanning?" It may not; the message asks whether a partner capability has any place in their service, and accepts a no.

### Target buyer persona: Sales Navigator pull for step 3

**Pull by title filter inside the approved company list, never by company alone.** The export Vadim pulled is the list for this campaign. This block is only for an optional top-up pull inside the IN companies (Open question 3): the export has no confirmed franchisor executive at Magrass, Emagrecentro, Siluets, Lipocenter or Face Doctor, no medical or nutrition lead at Liti, Vidalink, Salvia or MedTrue, and no product owner at Salvia, GESmed or Atrys Brasil. Brazilian profiles mostly carry Portuguese titles, so both forms are listed.

```titles
Chief Executive Officer
CEO
Fundador
Fundadora
Sócio Fundador
Chief Operating Officer
Diretor de Operações
Diretora de Operações
Diretor de Expansão
Diretora de Expansão
Diretor de Franquias
Gerente de Franquias
Gerente de Suporte ao Franqueado
Chief Medical Officer
Diretor Médico
Diretora Médica
Coordenador Médico
Coordenadora Médica
Head de Nutrição
Coordenadora de Nutrição
Head of Product
Head de Produto
Chief Product Officer
Gerente de Produto
Product Manager
Chief Technology Officer
Head de Tecnologia
Diretor de Tecnologia
Head de Saúde
Diretor de Saúde Corporativa
```

**`cap_per_group: 50`** (Vadim's default since 2026-09-29). The largest group is Vidalink at 18, then Magrass 14 and Nilo Saúde 13. Nothing is capped out.

## Message angle: segments, lanes, company facts, per-person hooks and the content asset

Every person gets exactly one lane, spelled exactly as below. Several companies send many people at once (Vidalink 18, Magrass 14, Nilo Saúde 13, Pró-Corpo 9, Liti 8), and franchise owners talk to each other, so no two people at one company share an opener, a central question, a closing ask, a Message 2 opener or a product sentence; facts agree across all of them. Numbers in copy come only from `proof-points.md` (see Rules). Company facts are used without numbers. **Writer notes in the tables below are instructions to the writer; they are never copied into a message.**

### Segment angles (writer notes)

- **Weight-loss programmes and clinics** (Liti, MedTrue, Instituto GL, Instituto Lumiere, Clínica da Obesidade, Grupo Endos, Grupo 5S; franchise networks Magrass, Emagrecentro, Lipocenter). Use case: `fx-telehealth-weight-loss` (in the card), without its hero line, Smart Scales framing or KPI list. The angle is a body record the patient or client takes on the phone between visits, inside the programme's app.
- **Corporate and health-plan care** (Vidalink, OrienteMe, Salvia, GESmed, Atrys Brasil, iMND, Wellbe, Nilo Saúde, Amparo Saúde, Abertta Saúde). Use case: the body-measurement boundary of `fx-wellness-rewards.md` (next section). The angle is an optional body record inside the member app, for the care or nutrition team.
- **Generalist telehealth and medical centres** (L2D, Llamando al Doctor, Reliv, holadr. IPS, Céntriqo, SPDM). Use case: the telehealth part of `fx-telehealth-weight-loss`. The angle is body measurements for consults that need height, weight, BMI or waist, taken by the patient before or between consults. The scan does not triage, diagnose or decide anything.
- **Aesthetic clinics** (Pró-Corpo, Siluets, Face Doctor, Inc Beauty, Ihealthy, Perfect clinic, Clínica Lev Vida). Use case: `icp-detail.md` §9, which has no use-case file; its points restated here: a body record taken on the phone before the in-person evaluation, and between body-treatment sessions, in the clinic's own booking or client flow (web or mobile SDK). The 3D model is a view the clinic chooses to show. Never appearance outcomes, never before-and-after, never surgical eligibility (BMI and risk before surgery are the surgeon's call).
- **Partnership only** (RWE Telemedicina and Telecárdio, tele-diagnostics; TELUS Health Brazil and Grupo Wellness Latina, employee assistance and health coaching; Saluta, Zínea and Terapia Online, mental health; N2B Brasil, body composition; GnTech, genetics; Sensorial, cognition). There is no use case for these services and copy does not invent one. The ask is whether a partner capability has any place in what they offer, and who would decide. Never imply that their service needs body scanning or lacks anything; accept a no.

### Accounts that already record body data (writer notes)

- **Liti** already records weight and body composition from its connected scale and has tracked body measurements. Never name the scale, the readings or the measurements in copy. Describe only the capture (two photos, guided, at home, inside the Liti app) and what it returns, without saying what is new to Liti.
- **Magrass** already tracks weight and measurements in Magrass Club. Describe the scan as a capture clients take at home between unit visits, inside Magrass Club. Never say or imply that units measure differently, inconsistently or not at all.
- **Emagrecentro** records waist and shows clients their evolution in its app. Tie the scan only to the founder's own point (fact EM2); never present waist or progress tracking as new.
- **N2B Brasil** sells body-composition exams at gym kiosks. Never compare the scan with the kiosk exam; partnership ask only.
- **Instituto Lumiere** offers body-composition assessment in the clinic. Never mention or compare it.
- **Everyone else:** nothing body-related is verified. Describe the capability; say nothing about what they record today.

### Corporate-health boundary (`fx-wellness-rewards.md`, "Biometric screening angle")

FitXpress covers the body-measurement part of a health check: waist and 80+ body measurements from two photos, BMI calculated from height and weight, body composition as estimates, timestamped and structured. It does not cover blood pressure, cholesterol, glucose, A1c or any blood test, and it does not interpret results or assign health risk. **When a message mentions a health check, check-up, screening or assessment, it says in the same message that blood pressure, cholesterol, glucose, A1c and other blood tests stay outside the scan** (the source file's rule: "the copy must say so"). Applies to Vidalink, OrienteMe, Salvia, GESmed, Atrys Brasil, iMND, Wellbe, Nilo Saúde, Amparo Saúde, Abertta Saúde and TELUS Health Brazil.

### Lanes

- **`product`** (founders, CEOs, product leads, clinic owners). Say what the app or patient flow can ask a person for: a guided two-photo scan that returns 80+ body measurements, body composition estimates and a 3D model, white-label through API or web and mobile SDKs, with nothing to ship. Ask the person's own question below.
- **`clinical`** (heads of nutrition, health-management leads, medical officers). Say that the care team gets a standardized, timestamped body record and compares scans it selects; the values are measurements and estimates for the team to review. Ask the person's own question below.
- **`operations`** (COOs, operations directors, implementation, process, clinic managers). Say that nothing is shipped, stocked or supported, that the capture follows the same guided sequence every time, and use the speed phrase. For multi-client platforms (Vidalink, GESmed, Nilo Saúde, L2D), one SDK serves every client.
- **`technical-integration`** (CTOs, tech leads, engineers, data). Describe the REST API with API-key authentication and the web and mobile SDKs; photos deleted after processing or within 30 days; outputs stored and deletable by scan ID. Give integration time only as "a typical basic integration takes 2-4 weeks". Technical tone. Message 2 links the FAQ.
- **`partnership`** (leaders at the partnership-only accounts). Ask whether a partner capability would have any place in their service, and who would decide. Add one line on what the scan returns and the company fact. No pitch, no claim about their clients' needs, no compliance line, no article; Message 2 carries the calendar link.
- **`referral`** (commercial, finance, frontline staff, advisors, franchise owners and unit staff). Ask the person's one question, add one line on what the scan returns, name the company and use its fact. No pitch, no compliance line, no article, calendar link optional. For franchise owners and unit staff: ask who at the franchisor owns the app or the protocol; never ask them to adopt anything for their own unit, never mention other units or owners, never suggest HQ already knows about the message.

### Company facts the copy may use

| Company | ID | Fact the copy may use | Writer notes |
|---|---|---|---|
| Vidalink | VL1 | Bem-estar 360º brings personalised meal plans, an activity app and mental-health content into one benefit. | |
| Vidalink | VL2 | Vidalink describes its benefits as covering mental and physical wellbeing and personal and professional growth, in one app. | App Store description. |
| Vidalink | VL3 | Vidalink combines humanisation and technology in a new generation of integrated benefits. | App Store description. |
| Vidalink | VL4 | Vidalink has a plan built for smaller companies. | Site menu. No headcount figure. |
| OrienteMe | OM1 | Psychology, nutrition and physical orientation by video, text or audio in the orienteme app. | |
| OrienteMe | OM2 | Guided content trails in the app on stress, anxiety and sedentary habits. | Never use eating disorders as a scan context. |
| OrienteMe | OM3 | The orienteme journey starts with the person taking the lead in their own life. | App Store description, "protagonista". |
| GESmed | GS1 | Corporate health management on the Modelo GES, built on primary-care principles. | |
| GESmed | GS2 | AppGES gives each member a reference nurse, personalised guidance, shared health documents and video calls with nurses, doctors, nutritionists and psychologists. | |
| GESmed | GS3 | GESmed has worked from Belo Horizonte since 2014. | The year only as a year. |
| Salvia Saúde Corporativa | SV1 | APS Digital: a family doctor coordinates the whole journey from the app. | |
| Salvia Saúde Corporativa | SV2 | Telemedicine, telepsychology and telenutrition in the Salvia app, with a nutrition programme. | Never use the pregnancy programme as a scan context. |
| Salvia Saúde Corporativa | SV3 | Digital and in-person primary care for companies and health plan operators. | |
| Atrys Brasil | AX1 | Population health management for health plan operators: prevention, health promotion and care coordination. | Name "Atrys Brasil" where the row says Atrys Brasil and "AxisMed" where it says AxisMed. |
| Atrys Brasil | AX2 | Chronic-patient programmes in Brazil since 2002. | The year only as a year. Never the acquisition or the owners. |
| Wellbe | WB1 | Wellbe started in Curitiba as an app for activity, sleep, food and mental health. | |
| Wellbe | WB2 | Online programmes aimed at helping people live free of chronic disease. | |
| iMND | IM1 | Online physical and mental health care for companies, brokers and insurers. | |
| iMND | IM2 | Follow-up programmes for physical and mental health. | |
| Nilo Saúde | NL1 | NiloCare and AI agents that automate operations for health institutions. | |
| Nilo Saúde | NL2 | Patients are cared for on WhatsApp or video, with no app to download. | |
| Nilo Saúde | NL3 | HL7 FHIR APIs and integration with an institution's own app. | Never claim that FitXpress supports FHIR. |
| Nilo Saúde | NL4 | Care lines for chronic and oncology patients. | |
| Nilo Saúde | NL5 | Operational and clinical indicators across patient portfolios and care lines. | Never connect scan outputs to insurance pricing. |
| Liti | LT1 | "Seu companheiro diário para emagrecer": Liti's daily companion for losing weight. | |
| Liti | LT2 | An online team of doctors, nutritionists and behavioural specialists. | |
| Liti | LT3 | Liti was founded by a nutrologist and sports doctor together with a former Rappi executive. | |
| MedTrue | MS1 | MedSlim starts online with virtual medical follow-up and applies treatment in person at licensed units when indicated. | Name the brand "MedSlim"; the company is MedTrue. |
| MedTrue | MS2 | Doctors in endocrinology, nutrology and aesthetic medicine prescribe and follow each treatment. | |
| Instituto GL | GL1 | A team of doctors and nutritionists trained by founder Dr. Gustavo de Oliveira Lima. | |
| Instituto GL | GL2 | Units in Moema and Tatuapé. | Never use the hormone-replacement protocols as a scan context. |
| Emagrecentro | EM1 | The Método 4 Fases, created by founder Dr. Edson Ramuth. | |
| Emagrecentro | EM2 | Dr. Ramuth's point that technology keeps the same standard of care in every clinic. | Paraphrase; never quote figures. |
| Emagrecentro | EM3 | A peer-reviewed study of the method was published in 2022. | Never its results; never the word waist. |
| Emagrecentro | EM4 | The "Emagrecentro - Método 4 Fases" app, where clients follow their evolution and results. | |
| Emagrecentro | EM5 | International units under the Best Shape brand. | |
| Magrass | MG1 | Magrass Club, the client app with meal logging, recipes from Magrass nutritionists and follow-up by the unit nutritionist. | Never mention the app's weight and measurement tracking. |
| Magrass | MG2 | Every Magrass unit is a franchise, with the head office in Santa Catarina. | |
| Magrass | MG3 | "Medicina Evolutiva". | Name only; never its formula. |
| Magrass | MG4 | Protocols that combine nutrition, body and facial aesthetics, medical follow-up and genetic science. | |
| Magrass | MG5 | Magrass Advanced, the smaller-format franchise. | |
| Lipocenter | LP1 | Founded in 2005 as an Instituto de Emagrecimento, later adding aesthetic protocols. | |
| Lipocenter | LP2 | A franchise network built around accessible prices. | Never prices. |
| Grupo Endos | GE1 | Endoscopic obesity treatment (endoscopic sleeve gastroplasty, gastric balloons) and injectable weight-loss therapies, in Rio, São Paulo, Belo Horizonte and Espírito Santo. | Only if its company-named row is released. |
| Clínica da Obesidade | CL1 | Supplied by the validator once the clinic is identified. | Hold if it cannot be identified. |
| Grupo 5S | GF1 | A holding that develops and makes nutraceutical products for weight loss and wellbeing. | Never name, describe, reference or endorse the group's weight-loss method. |
| Grupo 5S | GF2 | Franchise brands sold through stores and e-commerce. | |
| Instituto Lumiere | IL1 | A weight-loss and nutrology centre in São Luís. | |
| Instituto Lumiere | IL2 | Patients follow a nutrition plan in an app. | |
| Amparo Saúde | AM1 | A primary-care clinic network focused on prevention, with remote and in-person care and its own telehealth centre. | Never the owners or the number of people served. |
| Abertta Saúde | AB1 | A self-managed health plan with its own Health Promotion Centres, booked in person or by video in the app. | Never name the employers it serves. |
| Abertta Saúde | AB2 | Bertta, Abertta Saúde's AI assistant in the app. | |
| Abertta Saúde | AB3 | Preventive programmes such as VIVAequilíbrio. | |
| Pró-Corpo | PC1 | Aesthetics and plastic surgery, with the head office near Avenida Paulista and units in Rio, Londrina, Santos and Campinas. | |
| Pró-Corpo | PC2 | A free evaluation before every aesthetic procedure. | |
| Pró-Corpo | PC3 | Body treatments such as cryolipolysis, enzymes and lymphatic drainage. | Never appearance outcomes. |
| Pró-Corpo | PC4 | Treatments can be bought online ("Compre sem sair de casa"). | |
| Siluets | SI1 | By its own description, the first franchise to combine IPL hair removal with body treatments and weight loss. | |
| Siluets | SI2 | The Método Siluets for cryolipolysis. | |
| Siluets | SI3 | A network of aesthetic centres born in Brazil. | |
| Face Doctor | FD1 | A premium franchise network specialised in facial and body rejuvenation. | Never unit or client counts. |
| Face Doctor | FD2 | Exclusive protocols and its own skincare line. | |
| Inc Beauty | IB1 | A dermatology institute for regenerative and aesthetic skin, hair and body treatments. | |
| Ihealthy | IH1 | An integral aesthetic centre in Ecuador. | The validator confirms its services before send. |
| Perfect clinic | PF1 | Supplied by the validator once the clinic is identified. | Hold if it cannot be identified. |
| L2D Saúde Digital | LD1 | Telehealth since 2016, across Brazil and in international projects. | The year only as a year. |
| L2D Saúde Digital | LD2 | L2D runs its own teleconsultation platform and 24-hour support for doctors and care units. | |
| L2D Saúde Digital | LD3 | Teleconsultancy and telediagnosis, neurology and cardiology among them. | |
| Llamando al Doctor | LL1 | Immediate video consultations, 24 hours a day. | |
| Llamando al Doctor | LL2 | Services in Latin America, Europe and the US, in Spanish, English and Portuguese. | |
| Llamando al Doctor | LL3 | Telemedicine for travel assistance. | |
| Reliv | RL1 | A digital ecosystem connecting patients with doctors, hospitals, pharmacies, labs and insurers. | |
| Reliv | RL2 | Present in Ecuador and Mexico. | |
| holadr. IPS | HD1 | Interactive telemedicine across specialities, nutrition and occupational medicine among them. | |
| holadr. IPS | HD2 | Based in Medellín. | |
| Céntriqo | CQ1 | Specialist consultations, a day hospital, ambulatory surgery, laboratory, imaging, physiotherapy and pharmacy in one place in Quito. | Never surgical eligibility. |
| SPDM | SP1 | A philanthropic association working across primary, secondary and tertiary care. | |
| RWE Telemedicina | RW1 | Remote reports with medical equipment on loan for clinics and hospitals. | |
| RWE Telemedicina | RW2 | Specialists available 24 hours a day. | |
| Telecárdio | TC1 | Telemedicine across Brazil since 1993, with cardiologists and two call centres, 24 hours a day. | The year only as a year. |
| Telecárdio | TC2 | Remote reports for ECG, EEG, spirometry, visual acuity, Holter and blood-pressure monitoring. | |
| TELUS Health Brazil | TH1 | Psycho-emotional support, legal guidance, financial advice and social service for companies, employees and families. | Name the company as the row does (TELUS Health Brazil or CARE by TELUS Health); never the global group. |
| TELUS Health Brazil | TH2 | Health coaching, post-check-up coaching and physical-activity coaching among its programmes. | If "check-up" appears in copy, the corporate-health boundary applies. |
| Grupo Wellness Latina | GW1 | Employee assistance across Latin America, following EAPA and EAEF standards. | |
| Grupo Wellness Latina | GW2 | Psychological, legal, financial, nutritional, parenting and pet-care support lines. | |
| Grupo Wellness Latina | GW3 | Wellness programmes and habit-change coaching across psychological, physical and relational areas. | |
| Saluta | SA1 | Mental-health prevention, education and care through an app and telemedicine. | |
| Saluta | SA2 | Tele-education, telemedicine and telepsychiatry. | |
| Zínea | ZN1 | Mental-health management at work through its programme, the PGSM. | Never the regulation it serves or legal conformity. |
| Terapia Online | TO1 | Psychology and other mental-health specialities by telemedicine, nutrition among its services. | |
| Terapia Online | TO2 | Part of the Centro de Terapia del Comportamiento. | Never its years of experience. |
| N2B Brasil | NB1 | MyNutri: body-composition exams at gym kiosks, with results and menu suggestions in an app. | Never compare the scan with the exam. |
| N2B Brasil | NB2 | N2B's mission: make nutrition easier, more accessible and smarter. | |
| GnTech | GT1 | Pharmacogenetic testing for personalised health ("Saúde personalizada"). | Never tie the scan to medication choice. |
| Sensorial | SN1 | Neuroscience-based technology for health and cognitive performance, from academic development to rehabilitation and sports performance. | |

**Facts kept out of copy:**
- Vidalink+ Peso Saudável, weight-loss pens, the prescription and its validation, the AI audit, the balance, and the September 2026 press on pens as a corporate benefit (QC fixes 1-3).
- HR's real-time data at Vidalink, OrienteMe's Corporate Portal and team mapping, Wellbe's health-plan intelligence, iMND's sick-leave management (QC fix 4).
- Liti's scale and body-composition readings and its measurement tracking, Magrass Club's weight and measurement tracking, Emagrecentro's waist records, N2B's exam data, Instituto Lumiere's in-clinic body composition (QC fixes 5-6).
- Unit, client, patient and staff counts, prices, investment and royalties at every company; Grupo 5S's method; the owners of Atrys Brasil, Amparo Saúde and TELUS Health Brazil; Magrass's "Medicina Evolutiva" formula.

### Per-person hooks and questions

Each Message 1 stands on the person's hook (a fact from their own export row) and one company fact; the question is that person's alone. Every former employer, title, headline or bio line in the hook column was read from that person's row in `sales-nav-raw/export-1.csv` on 2026-10-05. Name no other employer or title.

| Person | Company | Lane, tier | Person hook (from the row) | Fact | Question only this person gets | Writer notes |
|---|---|---|---|---|---|---|
| Luis Gonzalez | Vidalink | `product`, P1 | CEO and co-founder; his bio says he helped establish BCG's first office in Brazil | VL1 | Would an optional body record for employees fit Bem-estar 360º, next to the meal plans and the activity app? | |
| Edson Ferreira Augusto Corrêa | Vidalink | `product`, P1 | Senior Product Manager, AI & Intelligent Systems; Group Product Manager at Laborit before | VL2 | Would structured body measurements be useful input for the AI work in the Vidalink app? | |
| Jorge Sousa | Vidalink | `operations`, P1 | COO | VL3 | What would operations need in place to offer an optional scan in the Vidalink app, with nothing shipped to employees? | No former-employer hook. |
| Eliane Simeão | Vidalink | `operations`, P1 | Diretora de Operações; HSBC and Itaú Unibanco before | VL2 | Where in the Vidalink app would an optional guided scan sit least in the way of what employees come for? | |
| Karen Ribeiro | Vidalink | `operations`, P2 | Headline "Gerente de Implantação"; Mondial Assistance Brasil before | VL1 | Would an SDK inside the Vidalink app change anything in how Bem-estar 360º is rolled out at a new client company? | |
| Tiago Soares | Vidalink | `technical-integration`, P3 | Tech Lead; HPE do Brasil before | VL3 | What would engineering require of a two-photo capture SDK, such as size and permissions, before it shipped in the Vidalink app? | |
| Daniela Junqueira | Vidalink | `technical-integration`, P3 | Tech Lead, Data Engineering and Analytics; Wiz Co before | VL2 | What shape would your data platform want scan outputs in: keyed to a scan ID, or something else? | |
| Bruno Menendes | Vidalink | `technical-integration`, P3 | Senior Data Engineer; Semantix Brasil before; his bio: integrations between data sources and the analytics layer | VL3 | Would a REST API that returns body measurements and estimates be simple to bring into those integrations? | |
| Lucas Mateus Silva de Souza | Vidalink | `technical-integration`, P3 | Senior Data Analyst; Santander Brasil before | VL4 | Which fields would product analytics look at first in a scan record: circumferences, composition estimates or timestamps? | |
| Alessandro Dourado da Silva | Vidalink | `referral`, P4 | Headline "I'm Vidalinker"; VAGAS.com before | VL4 | Who on the product side looks at new features for the employee app? | |
| Daniel Oliveira | Vidalink | `referral`, P4 | Headline: pharmacy network expansion and PBM | VL3 | Who decides what goes into the employee journey in the Vidalink app? | Never connect the scan to medicines or pharmacies. |
| Abi Nogueira | Vidalink | `referral`, P4 | RevOps manager; SAP before | VL2 | Who would evaluate a third-party capability for the app: product or the AI team? | |
| Aline Dos Santos | Vidalink | `referral`, P4 | Leads contract negotiations; procurement at LongPing High-Tech before | VL3 | Who runs onboarding when a new technology partner joins the app? | |
| Paulo Gonçalves | Vidalink | `referral`, P4 | Head of Controllership and Finance; NotreDame Intermédica and Affix Administradora de Benefícios before | VL4 | Who would sponsor a small pilot of a new app capability: product or operations? | |
| Nadia Panow | Vidalink | `referral`, P4 | Administrative and finance manager | VL1 | Who leads Bem-estar 360º? | No former-employer hook. |
| Susana Augusto de Camargo Silva | Vidalink | `referral`, P4 | CS lead | VL2 | Who collects client companies' feature requests for the app? | No former-employer hook. |
| garga Mel | Vidalink | `referral`, P4 | Title "Diretor" | VL4 | Who owns the plan for smaller companies? | Identity check at validation. |
| Renan Schonton | Vidalink | `referral`, P4 | Title "Chefe" | VL1 | Who handles partnerships for the app's wellbeing features? | Identity check at validation. |
| Bruno Haidar | OrienteMe | `product`, P1 | CoFounder and CEO; Associate Lawyer at Demarest Advogados before | OM1 | Does a guided body scan belong in the orienteme app, next to the nutrition and physical orientation sessions? | |
| Fernanda Maluf | OrienteMe | `product`, P1 | Co-Founder; Heidrick & Struggles before | OM2 | Could a body record be part of a trail on sedentary habits that the member chooses to start? | |
| Fernanda Mondin | OrienteMe | `clinical`, P1 | Head of Nutrition and Physical Orientation; SulAmérica's coordinated-care nutrition team and Teladoc Health before | OM1 | Would the nutritionists use a standardized body record the member captures at home between video sessions? | |
| Alessi Soncini | OrienteMe | `technical-integration`, P3 | Co-founder and CTO; headline "AI in practice: less hype, more results"; his bio: a wellness ecosystem serving some of Brazil's largest insurers | OM1 | What would you want to see in an SDK's documentation before adding a camera capture to the orienteme app? | |
| Renata Tavolaro | OrienteMe | `referral`, P4 | Head of Psychology; 4Champions before | OM1 | Who on the nutrition and physical side would look at a new body-measurement tool? | Short and neutral. |
| Maurício Lima | OrienteMe | `referral`, P4 | Head Comercial; life planner with Prudential (Hope MD) before | OM3 | Who owns the roadmap for the orienteme app? | |
| Jessica Rayane | OrienteMe | `referral`, P4 | Senior Account Analyst; MPJ Solutions before | OM2 | Who handles technology partnerships at orienteme? | Greet as Jessica. |
| Fernando Marques | GESmed | `product`, P1 | Founder and CEO; Gerdau and Usiminas before | GS1 | Where would a phone body record fit the Modelo GES care cycle for insured employees? | |
| Thiara Amanda Corrêa de Almeida | GESmed | `operations`, P2 | Her bio: she standardizes the Modelo GES and its tools; a nurse | GS2 | Would a guided phone capture fit the tools reference nurses use in AppGES? | |
| Marcela Ferreira Lima Guimarães | GESmed | `clinical`, P2 | Health-management lead and nurse; research at Fiocruz before | GS1 | Which body measurements matter most in GES care for employees living with obesity? | |
| Lucas Lau | GESmed | `operations`, P2 | Head of process and management technology; Falconi before | GS3 | What would process and technology want proven before a new capture went into AppGES? | |
| Mirian Maria Marques Pinheiro | Salvia Saúde Corporativa | `product`, P1 | CEO; Head of Operation, Clinical Engineering and Quality at Vision One before | SV2 | Would a guided body scan in the Salvia app support the nutrition programme between telenutrition consults? | |
| Bárbara Carvalho | Salvia Saúde Corporativa | `referral`, P4 | Commercial director; Qualirede before | SV3 | Who owns the Salvia app roadmap? | |
| Renise M. | Salvia Saúde Corporativa | `referral`, P4 | Head Comercial; TopMed Saúde Digital before | SV1 | Who leads the nutrition programme clinically? | |
| Tiago Vieira | Atrys Brasil | `product`, P1 | Executive Director; headline on transformation and digitalization in health | AX1 | Where would a guided home body record fit the prevention and care-coordination programmes run for health plan operators? | |
| Alejandro Gorissen | Atrys Brasil | `referral`, P4 | CFO (row: AxisMed) | AX2 | Who leads product for the chronic-patient programmes? | Name AxisMed. |
| Luciana Ito | Atrys Brasil | `referral`, P4 | Client relationship manager; Tempo Assist before | AX1 | Who decides which tools reach members in the programmes operators buy? | Never name her other former employer, which is another prospect. |
| Matheus Rodrigues | Atrys Brasil | `referral`, P4 | Senior accountant; PwC before | AX2 | Who on the clinical side looks at new data-collection methods? | |
| Silvia Lima | Atrys Brasil | `referral`, P4 | Psychologist (row: AxisMed) | AX2 | Who coordinates the multidisciplinary team in the chronic-patient programmes? | Name AxisMed. Short and neutral. |
| Lucas Vieira Werner | Wellbe | `product`, P1 | Co-founder and CTO; co-founded StillGood before | WB1 | Where do Wellbe's online programmes meet the member today, and could a guided scan sit there? | |
| William Bin Falinski | Wellbe | `technical-integration`, P3 | Tech Lead; his bio: data engineer at Wellbe | WB2 | What would engineering want from a body-scan API before a member-facing pilot? | |
| Sidnei Salmaso | Wellbe | `referral`, P4 | Senior business consultant; AdviceHealth and Mongeral Aegon before | WB2 | Who owns Wellbe's programmes for chronic conditions? | |
| Isabelle Ferraz | iMND | `referral`, P4 | Partner and CFO; Santander before | IM2 | Who leads the physical-health programmes at iMND? | |
| Victor Marcondes | Nilo Saúde | `product`, P1 | Founder; co-founded Cosmedical before | NL1 | Could a phone body record be one step in NiloCare journeys for operators' chronic care lines? | |
| Rafael Alves Martins | Nilo Saúde | `product`, P1 | Head of Product; invited professor at Hospital Sírio-Libanês before | NL2 | With patients on WhatsApp and no app to download, would a web capture link fit Nilo's journeys? | |
| Carolina Beltramini | Nilo Saúde | `operations`, P2 | Head of Customer Experience; her bio: she leads implementation, customer success and support | NL5 | What would implementation need to switch on a new capture for one operator's care line? | |
| Filipe Firmino | Nilo Saúde | `operations`, P3 | Customer experience coordinator; Rabbot before | NL4 | What do care teams ask CX for first when a new feature reaches their patients? | |
| Cesar Nobre | Nilo Saúde | `technical-integration`, P3 | CTO; Director of Engineering at will bank before | NL3 | Where would structured scan outputs from an API land in Nilo's FHIR-based data model? | |
| Diego Freire | Nilo Saúde | `technical-integration`, P3 | Senior Software Engineer; headline: event-driven architecture, integrations and APIs | NL3 | How would a third-party scan API fit the integrations you build between systems? | |
| Rodolfo Stangherlin | Nilo Saúde | `technical-integration`, P3 | Staff Software Engineer, Python/Django and TypeScript/React; Geekie before | NL2 | Would a web SDK suit Nilo's front end better than a native mobile one? | |
| Iasmini Gomes | Nilo Saúde | `technical-integration`, P3 | Senior Software Engineer, backend Python; SiLex Sistemas before | NL5 | What would the backend need from a scan API first: authentication, request limits or deletion by scan ID? | |
| Vitor Honda | Nilo Saúde | `referral`, P4 | Head of Business Analytics; Gympass before | NL5 | Who owns the care-line indicators product? | |
| Steffany C. | Nilo Saúde | `referral`, P4 | Enterprise business development; CondoLivre before | NL1 | Who handles technology partnerships at Nilo? | |
| Geovana Dorys | Nilo Saúde | `referral`, P4 | General manager | NL4 | Who designs the chronic care-line journeys? | Thin profile; identity check. |
| Fabio Katayama | Nilo Saúde | `referral`, P4 | Advisory board member at Nilo (row: MGL Consultoria); CEO of Hospital Samaritano before | NL4 | Who at Nilo would you suggest for a conversation about body data in chronic care lines? | Advisor: current-role check. |
| Rafael L. Ribeiro | Nilo Saúde | `referral`, P4 | "Strategic Advisor at Nilo Saúde" on his profile | NL1 | Would Nilo's product team or its clinical team be the right place for this? | Advisor: current-role check. Never name his current employer. |
| Fernando Vilela | Liti | `product`, P1 | Co-Founder; CMO at Rappi before | LT1 | Would a guided two-photo capture have a place in the Liti app's daily routine? | |
| Bruno Silva | Liti | `technical-integration`, P3 | CTO; Director of Engineering at Betterfly before | LT3 | Would a camera SDK raise any permission or app-size concerns for the Liti app? | |
| Maycon Soligo | Liti | `technical-integration`, P3 | Full Stack Engineer; GrowthHackers before | LT1 | Would a web SDK or a native mobile SDK fit the Liti app better? | |
| William Weckl | Liti | `technical-integration`, P3 | Staff Software Engineer; Mercado Livre before | LT2 | How much of the capture guidance would the app want to own, and how much would it leave to the SDK? | |
| Rodrigo Casale Abe | Liti | `referral`, P4 | CFO; BCG and Creditas before | LT3 | Who owns the Liti app roadmap? | |
| Ana Paula Moraes | Liti | `referral`, P4 | Nutritionist; Hospital Alemão Oswaldo Cruz before | LT2 | Who leads the clinical protocol the nutrition team follows? | |
| Gabriela Teixeira | Liti | `referral`, P4 | Clinical nutritionist; Nutrir Corphus before | LT2 | Who on the medical team decides what the programme records? | |
| Ana Claudia Pinto | Liti | `referral`, P4 | Advisory board member at Liti (row: CEO of Find.AI); endocrinologist; Chief Medical Officer for digital health at Grupo Fleury before | LT1 | Who at Liti would be the right person for a conversation about body measurements in obesity care? | Advisor: current-role check. |
| Lucas Quintella | MedTrue | `product`, P1 | CEO | MS1 | Would a home scan fit the online start of the MedSlim journey, before a patient visits a licensed unit? | No former-employer hook. |
| Ramon Guedes | MedTrue | `referral`, P4 | Head of Revenue; Wise Up before | MS2 | Who designs the patient journey at MedSlim? | |
| Arthur Silva Da Ros | Instituto GL | `referral`, P4 | CFO; Kroton before | GL1 | Would Dr. Gustavo or the medical coordination be the right person for a conversation about body measurements between visits? | |
| Viviane Lins | Emagrecentro | `referral`, P4 | Diretora Geral | EM4 | Who at the franchisor owns the Método 4 Fases app? | Branch: franchisor role moves her to `operations` P1. |
| Wesley Denardin | Emagrecentro | `referral`, P4 | Diretor | EM2 | Who at the franchisor looks after the technology behind the same standard of care in every clinic? | Branch: franchisor role moves him to `operations` P1. |
| Paty Marques | Amparo Saúde | `referral`, P4 | Sales manager | AM1 | Who owns the digital tools the telehealth centre and the clinics use with patients? | |
| Marcus Nunes | Amparo Saúde | `referral`, P4 | Reception agent | AM1 | Who coordinates the prevention programmes across Amparo's clinics? | |
| Daniele Araujo | Abertta Saúde | `referral`, P4 | Regulation and relationship manager | AB3 | Who runs the preventive programmes such as VIVAequilíbrio? | |
| Marina Michaelsen Deriggi | Magrass | `referral`, P4 | Co-owner of Magrass Montenegro; HR at Seara before | MG1 | Who at the franchisor decides what goes into Magrass Club? | |
| Marcio Jorge Pinho Deriggi | Magrass | `referral`, P4 | Co-owner of Magrass Montenegro; JBS before | MG2 | Does a new tool for the units reach the franchisor through operations or through franchisee support? | |
| Janaina Possebon | Magrass | `referral`, P4 | Managing partner, Magrass Moinhos de Vento; Grupo RBS before | MG4 | Who at HQ owns the client protocol that combines nutrition, aesthetics and medical follow-up? | |
| Luiz dos Santos Nunes Filho | Magrass | `referral`, P4 | Co-owner of Magrass Moinhos de Vento and of G3 Treinamento Personalizado | MG5 | Who at HQ decides which tools a new unit starts with? | |
| Fabricio Pires | Magrass | `referral`, P4 | His row: Magrass rio preto | MG2 | Who at HQ handles partnerships with technology companies? | Thin profile; confirm the unit. |
| Rodrigo Baroni | Magrass | `referral`, P4 | Owns Magrass Paulínia, Cascavel, Gravataí and Mogi das Cruzes; Sicredi before | MG2 | Is there a franchisee forum where owners of several units raise new tools with HQ, and who runs it? | |
| Rafaela Klein | Magrass | `referral`, P4 | Clinical nutritionist at Magrass Cascavel; Hospital Nove de Julho before | MG1 | Who at HQ sets the routine unit nutritionists follow with clients? | |
| Regina Alves Ribeiro | Magrass | `referral`, P4 | Partner, Magrass Contagem | MG3 | Who at HQ leads Medicina Evolutiva on the medical side? | |
| Roberta Mascarenhas | Magrass | `referral`, P4 | Managing partner, Magrass Macaé | MG4 | Who at HQ owns the client experience across the network? | |
| Tami Bianca | Magrass | `referral`, P4 | Owner, Magrass Pindamonhangaba | MG1 | Who maintains the Magrass Club app for the network? | |
| Rhúã Robson D´Cézares Rodrigues de Oliveira das Chagas Netto | Magrass | `referral`, P4 | General manager, Magrass Assis; Ibmec before | MG4 | Who at HQ trains unit teams when a new client tool arrives? | |
| Sandra Geres Alves Panza | Magrass | `referral`, P4 | Director of MagraSS Maringá; faculty at Unicesumar | MG4 | Does HQ test new methods in a few pilot units first, and who chooses them? | |
| Gabriela Biazus | Magrass | `referral`, P4 | "Sócia-fundadora at Magrass"; nutrition degree at UFCSPA | MG1 | Who at HQ runs marketing for Magrass Club and the client journey? | Branch: if she is a founding partner of the franchisor, move her to `product` P1 and ask instead whether a body record clients take at home has a place in Magrass Club. |
| Renata Assuncao | Magrass | `referral`, P4 | Vice-director, Magrass Vila Olimpia | MG2 | Who at HQ in Santa Catarina handles purchasing and supplier approval for the network? | |
| Marisa Peraro | Pró-Corpo | `product`, P2 | Founder; her bio: she created "360 Gestão para Clínicas", a management mentoring for clinic owners | PC1 | Where would a two-photo body record fit at Pró-Corpo: before the free evaluation, or between body-treatment sessions? | |
| Patricia Coutinho | Pró-Corpo | `product`, P2 | CEO (her headline) | PC2 | Would a body record taken on the phone before the free evaluation be useful to Pró-Corpo's evaluators? | Identity check. |
| Simone Fatima Amaral Martins | Pró-Corpo | `operations`, P2 | General manager (gestora geral) | PC3 | What would unit teams need to offer a guided phone capture, with nothing to install in the clinic? | |
| Andreza Zatorre Pereira | Pró-Corpo | `referral`, P4 | Aesthetics consultant; dermato-functional physiotherapist; Corporal Shape before | PC3 | Who at Pró-Corpo decides which tools the evaluation team uses? | |
| Solange Bader | Pró-Corpo | `referral`, P4 | Headline "Empressaria na Pró-Corpo" | PC1 | Who at the São Paulo head office handles new technology for the units? | Identity check. |
| Clovis Clodovil | Pró-Corpo | `referral`, P4 | Title "Empreendedor" | PC4 | Who runs the online sales side of Pró-Corpo? | Identity check. |
| Josemar Silva | Pró-Corpo | `referral`, P4 | Title "Proprietário" | PC1 | Who at Pró-Corpo's head office looks at partnerships? | Identity check. |
| Michelly Carneiro de Araujo | Pró-Corpo | `referral`, P4 | Title "Pequeno empresário" | PC2 | Who coordinates the free evaluations across units? | Identity check. |
| Rita Santos | Pró-Corpo | `referral`, P4 | Title "Empreendedor" | PC3 | Who leads the body-treatment side at Pró-Corpo? | Identity check. |
| Flaminio Dalul | Siluets | `referral`, P4 | "Sócio proprietário at Siluets Franchising"; headline "Siluets rio preto"; finance manager at LHD before | SI1 | Who at Siluets Franchising supports units with new client tools? | Branch: a franchisor role moves him to `product` P2. |
| Adrielle Dalul | Siluets | `referral`, P4 | Executive sales director at Siluets Estética | SI2 | Who at the franchisor decides on new services for the units? | |
| Meire Satelite | Siluets | `referral`, P4 | Headline "Empresaria na Siluets Jundiaí" | SI3 | Who at the franchisor approves suppliers for the units? | |
| Jackeline Lopes | Siluets | `referral`, P4 | General manager at Siluets Estética; Pertech do Brasil before | SI3 | Who at the franchisor trains unit teams on new services? | |
| Regiane Viana de Oliveira | Siluets | `referral`, P4 | General manager at Siluets Estética | SI2 | Who at the franchisor owns the body-treatment protocols? | |
| Lívia Sales | Siluets | `referral`, P4 | President-director of Siluets Estética Aracaju; micropigmentation artist (headline) | SI3 | Who at the franchisor handles partnerships with technology companies? | |
| Elaine Tadiello | Siluets | `referral`, P4 | General manager at Siluets Estética | SI1 | Who at the franchisor would review a new body-measurement tool for the network? | |
| aline caio | Lipocenter | `referral`, P4 | "Diretor at LIPOCENTER FRANQUIA" | LP1 | Who at Lipocenter's franchisor decides on new client tools? | Branch: a franchisor role moves her to `operations` P2. Greet as Aline. |
| Sandra Baldassari | Lipocenter | `referral`, P4 | Businesswoman at LIPOCENTER FRANQUIA | LP2 | Who supports franchisees with technology at Lipocenter? | |
| Cristiane Aguilar | Lipocenter | `referral`, P4 | Title "Proprietário" | LP1 | Who at the franchisor owns the weight-loss protocol? | |
| Milena Espinha | Lipocenter | `referral`, P4 | Headline "proprietária na lipocenter" | LP1 | Who at Lipocenter would review a phone body-measurement tool for the network? | |
| lisete espindola | Lipocenter | `referral`, P4 | Headline "proprietaria na lipocenter" | LP2 | Is there a franchisee channel where new tools are proposed, and who runs it? | Greet as Lisete. |
| Mônica Melli | Lipocenter | `referral`, P4 | Administrative director, Lipocenter Perdizes | LP2 | Who at the franchisor handles supplier and partner onboarding? | |
| Monique Diana Martins | Face Doctor | `referral`, P4 | Co-owner, Face Doctor Perdizes | FD1 | Who at Face Doctor's franchisor looks after the body-treatment protocols? | Never name her other former employer, which is another prospect. |
| Fabrícia Dias | N2B Brasil | `partnership`, P3 | Head of expansion at N2B Brasil | NB1 | Is a partnership on phone-based body measurement something N2B would consider, and who would decide? | |
| João Murackami | N2B Brasil | `partnership`, P3 | Senior Analytics Engineer; PwC and Sharecare Brasil before | NB2 | What would N2B's data team want to know first about a body-scan API offered as a partner capability? | |
| Jacques Maciel | Clínica da Obesidade | `product`, P2 | Director at Clínica da Obesidade | CL1 | Would a body record patients take on their phone between visits fit the clinic's follow-up? | Identify the clinic first. The row reads "Sr. Jacques Maciel": greet as Jacques. |
| Indira Cruz | Clínica da Obesidade | `referral`, P4 | Headline "Gerente Operacional na CLÍNICA DA OBESIDADE" | CL1 | Who at the clinic decides on new tools for patient follow-up? | Current-role check; her row's company is a hotel. |
| Ulysses Maciel | Clínica da Obesidade | `referral`, P4 | "Diretor executivo at CLINICA DA OBESIDADE" on his profile | CL1 | Who runs the clinic's patient programmes? | Current-role check; FAIL as former staff if past. Never name his other company. |
| Dra Edivana Poltronieri | Grupo 5S | `product`, P2 | CEO of Grupo 5S (her headline) | GF2 | Would a phone body record fit the client journey in the group's franchise brands? | Greet as Edivana. Never the method or its name. |
| Paulo Almança | Grupo 5S | `referral`, P4 | Head of Finance; Vale before | GF1 | Who runs operations for the franchise brands? | |
| Abilio Costa | Instituto Lumiere | `product`, P2 | Owner of Instituto Lumiere | IL2 | Would a body record patients take on their phone between visits fit alongside the nutrition plan they follow in the app? | |
| Vinicius Cuerci de Souza | RWE Telemedicina | `partnership`, P3 | Operations director; headline: operations, processes, quality and technology in health and telemedicine | RW1 | Do client clinics ever ask RWE for remote services beyond reports, and who would weigh a partner offering? | |
| Luana Barreto | RWE Telemedicina | `partnership`, P3 | Commercial director (headline) | RW1 | Is a remote body-measurement capture something RWE's commercial team could offer clinics, or outside your lines? | |
| Emerson Goulart | RWE Telemedicina | `partnership`, P3 | Director; headline: medical equipment on loan plus remote reports for clinics and hospitals | RW1 | Does RWE ever add software-only services to what it offers clinics and hospitals? | |
| Eduarda Cuerci | RWE Telemedicina | `partnership`, P3 | Operations director; nurse; telemedicine and audit (headline) | RW2 | Who at RWE looks at new telehealth services before they reach clients? | |
| Paulo Castilho | RWE Telemedicina | `referral`, P4 | General manager; earlier commercial coordinator at RWE | RW2 | Who decides on new partner services at RWE? | |
| Carlos Coelho | RWE Telemedicina | `referral`, P4 | Executive at RWE | RW1 | Who handles partnerships with technology companies at RWE? | |
| Roberto Stryjer | Telecárdio | `partnership`, P3 | CEO and co-founder (headline) | TC1 | Has Telecárdio ever offered client clinics a remote service outside its reports, through a partner? | |
| Marcelo Lapa Espiga | Telecárdio | `partnership`, P3 | Co-CEO; McKinsey before | TC2 | Is a partnership on remote body measurement something the Co-CEOs would weigh, or a clear no? | |
| Alexandre Pimentel | Telecárdio | `partnership`, P3 | Director, earlier administrative director at Telecárdio | TC1 | Who at Telecárdio looks at new services for clinics and operators? | |
| Flavio Svaiter | Telecárdio | `referral`, P4 | Finance director; iMusica before | TC2 | Who should hear a partnership idea at Telecárdio: the CEOs or commercial? | |
| Amanda Micaela Alves | Telecárdio | `referral`, P4 | Senior commercial executive; headline: telediagnosis for clinics, hospitals and operators | TC2 | Do clinics you serve ever ask about body measurements, and who at Telecárdio would hear that? | |
| Janiel José Zioti | L2D Saúde Digital | `product`, P2 | Group executive director at L2D Saúde Digital | LD2 | Would a guided two-photo body record have a place in L2D's teleconsultation platform, for consults that need height, weight or waist? | |
| Lucas Schneider | L2D Saúde Digital | `operations`, P2 | COO, L2D Telemedicina (headline); procurement coordination in the Brazilian Army before | LD1 | In L2D's projects, how are a patient's body measurements taken before a teleconsultation today? | |
| Fernando P. | L2D Saúde Digital | `technical-integration`, P3 | Head of Technology and Processes; headline "Technology Director, Healthtech" | LD2 | Since L2D builds its own teleconsultation platform, would an SDK inside it be straightforward? | |
| Juliana Faure | L2D Saúde Digital | `referral`, P4 | Medical doctor (telemedicine) | LD3 | Who decides which tools doctors see in the teleconsultation platform? | |
| Guillermo Gonzalez | Llamando al Doctor | `product`, P2 | CEO; Swiss Medical Group before | LL2 | Would a body record from the phone be useful in any of the countries Llamando al Doctor serves? | |
| Ricardo Gordillo | Llamando al Doctor | `operations`, P2 | COO; emergency physician; Presidential Medical Unit before | LL1 | In a 24-hour video consult, when would a doctor want weight, BMI or waist before the call, if ever? | |
| Martín Lucas Golini | Llamando al Doctor | `technical-integration`, P3 | CTO; Bricks before | LL1 | Would a web SDK work inside both the Llamando al Doctor app and the web platform? | |
| Viviana Salazar | Llamando al Doctor | `referral`, P4 | CFO and director of administration, finance and HR; Telecentro before | LL3 | Who would look at a partner capability for the app: the CEO or the medical team? | |
| Paola Almeida | Reliv | `product`, P2 | Co-founder and COO; a physician | RL1 | Where in Reliv's patient journey would a phone body record be useful to the doctors on the platform? | |
| Sebastián Guarderas-Castro | Reliv | `clinical`, P2 | Chief Medical Officer; medical auditor before | RL1 | Which body measurements would Reliv's doctors want before a consultation? | Never an insurer or audit framing. |
| Mauricio Padilla | Reliv | `technical-integration`, P3 | Tech Lead | RL2 | What would the platform need from a capture SDK to work in both Ecuador and Mexico? | |
| Paola Cristina Giraldo Osorio | holadr. IPS | `product`, P2 | CEO; Connect Bogotá Región before | HD1 | Would a home body record help holaDr's nutrition and occupational-medicine consults? | |
| Ana Maria Restrepo Gomez | holadr. IPS | `referral`, P4 | Communications lead | HD2 | Who leads the nutrition service at holaDr? | |
| Martin Samaniego | Céntriqo | `product`, P2 | CEO of Céntriqo; a medical doctor; his bio: digital transformation in healthcare | CQ1 | Would a body record patients take at home before a specialist consultation fit Céntriqo's scheduled care? | Never mention Reliv to him. |
| Natalia Dezerega Molina | Céntriqo | `referral`, P4 | Chief of Staff (row: Quirurgic) | CQ1 | Who at Céntriqo decides on new patient-intake tools? | Never mention Reliv. |
| ligia antunes pinto ferreira | TELUS Health Brazil | `partnership`, P3 | Director of Operation, TELUS Health Brazil; EAP operations at Chestnut Global Partners and MindSolutions before | TH2 | Would a phone body record be useful in post-check-up or physical-activity coaching, as a partner capability? | Greet as Ligia. Corporate-health boundary applies. |
| Sonia Maria Figueiredo | TELUS Health Brazil | `referral`, P4 | Consultant and speaker at CARE by TELUS Health; neuropsychologist | TH1 | Who runs the health-coaching programmes in Brazil? | |
| Carlos Prestes | TELUS Health Brazil | `referral`, P4 | International Account Manager; Juno before | TH2 | Who decides on partner services for the coaching programmes? | Never name his other former employer, which is another prospect. |
| Andrea Lardani | Grupo Wellness Latina | `partnership`, P3 | Director and co-founder; member of the EAPA Communications Advisory Panel | GW3 | In the habit-change coaching programmes, could a body record ever help, or is that outside an EAP's scope? | |
| Ángeles Dubini | Grupo Wellness Latina | `referral`, P4 | Senior Account Manager | GW1 | Who designs the wellness programmes Grupo Wellness Latina offers companies? | |
| Jimena Maldonado de Chazal | Grupo Wellness Latina | `referral`, P4 | Nutrition counselor; clinical nutritionist at Hospital Arco Iris before | GW2 | Who coordinates the nutrition line across countries? | |
| Luis Hincapié | Saluta | `partnership`, P3 | Co-founder and operations manager (headline); GoToNext before | SA1 | Does Saluta partner with physical-health services for its app users, and who decides? | |
| María Alejandra Silva Castro | Saluta | `partnership`, P3 | Director; IntegraMédica before | SA2 | Is physical health ever part of Saluta's programmes, or strictly mental health? | |
| Ricardo Perales Aravena | Saluta | `referral`, P4 | Commercial director; Hospital de Parral before | SA1 | Who looks at partnership proposals at Saluta? | |
| Gabriela Galvis | Saluta | `referral`, P4 | Digital sales lead | SA2 | Who owns Saluta's app roadmap? | |
| Anderson Baldissera | Zínea | `partnership`, P3 | Co-founder and CTO | ZN1 | Would Zínea ever pair its programme with physical-health data, or keep it strictly mental health? | |
| Graziela Heusser Azeredo | Zínea | `referral`, P4 | Advisory board member at Zínea | ZN1 | Who at Zínea would be the right person for a partnership question? | Advisor: current-role check. |
| Rodrigo Alvarez Diaz | Terapia Online | `referral`, P4 | Patient-area supervisor | TO1 | Who leads the nutrition service at Terapia Online? | |
| Milton Ávila | Sensorial | `partnership`, P3 | CEO and founder; his bio: a PhD in neuroscience | SN1 | In sports-performance work, do Sensorial's clients ever combine cognitive and body data? | |
| Victor Cavallari | Sensorial | `referral`, P4 | Co-founder and COO (headline); sports psychologist before | SN1 | Who at Sensorial handles partnerships in sports performance? | |
| Kevin Lucas | Sensorial | `referral`, P4 | Backend software engineer at Sensorial Sports; Flashvolve before | SN1 | Who leads product for Sensorial Sports? | |
| Paula Pedrassani Boabaid May | GnTech | `partnership`, P3 | Founder and vice-president (headline); lawyer at Unimed Grande Florianópolis before | GT1 | Does GnTech partner with other personalised-health services, and who decides? | |
| Adriano Oliveira | GnTech | `referral`, P4 | Technical lead | GT1 | Who owns GnTech's digital products? | |
| Adriana Bottoni | SPDM | `referral`, P4 | Technical director of the AME Idoso Oeste (headline); A.C.Camargo Cancer Center before | SP1 | Who at SPDM looks at digital tools for outpatient care? | Public institution: any interest goes through its own procurement. |
| Paula Tecchio | Inc Beauty | `referral`, P4 | Head Comercial; Seven Clínica before | IB1 | Who decides on new technology for the body treatments at Inc Beauty? | Never name her other former employer, which is another prospect. |
| Javier Rhea | Ihealthy | `product`, P2 | Partner-manager of Ihealthy; CEO of Innoclinica, an outpatient-care company (headline) | IH1 | Would a body record clients take on their phone before a treatment plan fit Ihealthy's evaluations? | The validator confirms Ihealthy's services. |
| Valentina Sanabria | Perfect clinic | `referral`, P4 | General manager of Perfect clinic | PF1 | Who at the clinic decides on new tools for patient evaluations? | Identify the clinic first. |

**Peers most likely to compare notes** (no shared hook, sentence, context line, question or closing ask inside each group): all 14 Magrass rows, and in particular Marina and Marcio Deriggi (one unit), Janaina Possebon and Luiz dos Santos Nunes Filho (one unit), Rodrigo Baroni and Rafaela Klein (the Cascavel unit); the 7 Siluets rows, with Flaminio and Adrielle Dalul; the 6 Lipocenter rows; the 9 Pró-Corpo rows; Vidalink operations (Jorge Sousa, Eliane Simeão, Karen Ribeiro), data (Tiago Soares, Daniela Junqueira, Bruno Menendes, Lucas Mateus Silva de Souza), commercial (Alessandro Dourado da Silva, Daniel Oliveira, Abi Nogueira, Aline Dos Santos, Susana Augusto de Camargo Silva) and finance (Paulo Gonçalves, Nadia Panow); OrienteMe's co-founders and Fernanda Mondin; GESmed's four; Nilo's engineers and its two advisors; Liti's engineers, its nutritionists and its advisor; RWE's directors, with Vinicius and Eduarda Cuerci; Telecárdio's co-CEOs; Saluta's four; Reliv's three with Céntriqo's two (shared history).

### Content asset in Message 2 (at most one article link, plus the calendar link)

| Who | Link | Writer notes |
|---|---|---|
| Liti, MedTrue, Instituto GL, Instituto Lumiere, Clínica da Obesidade: `product`, `clinical`, `operations` | https://3dlook.ai/content-hub/glp-1-market/ | Do not quote or paraphrase its sections on scale weight; do not use its "approximately 30 to 45 seconds"; do not name its section titles. |
| Vidalink, OrienteMe, Salvia, GESmed, Atrys Brasil, Wellbe, Nilo Saúde: `product`, `clinical`, `operations` | https://3dlook.ai/content-hub/ai-body-data-wellness-platforms/ | |
| Grupo Endos, only if its row is released | https://3dlook.ai/content-hub/bariatric-pre-qualification-mobile-3d-body-scanning/ | Do not quote its Smart Scales or eligibility passages. |
| `technical-integration`, every company | https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/ | It describes US and EU rules; never restate any of it in the message. |
| Everyone else: the telehealth and aesthetic accounts, Grupo 5S, every `partnership` and every `referral` sequence | no article | The telehealth hub carries retired compliance wording; there is no aesthetics page; no page is linked for Grupo 5S. |

No other 3DLOOK page is linked.

## Rules for steps 3-5

- **Sender and format:** Kateryna, English, `Kateryna` alone on the last line, first name only, no title. Connection request with no note. Message 1 ≤ 600 characters; Message 2 ≤ 550 with https://meetings.hubspot.com/kateryna-boichuk as plain text (required in every lane except `referral`, where it is optional) and at most one article link (the asset table). All 163 go in one import file at the same time; tiers only order the list.
- **Lanes are exactly** `product`, `clinical`, `operations`, `technical-integration`, `partnership`, `referral`.
- **Several people at one company.** Never mention that colleagues, other units or other franchisees were contacted; never claim to have spoken with anyone there; never claim an interaction that did not happen ("Circling back", "Saw your post", "Following up", "after connecting"; the Message 1 template lists some of these as hooks, and they are banned here). Name the company in every Message 1 (MedSlim for MedTrue, AxisMed or Atrys Brasil as the person's row says). No two people at one company share an opener, a central question, a closing ask, a Message 2 opener or a product sentence; facts agree across all of them.
- **The Message 1 template's "what's missing" step does not apply.** Message 1 makes an observation from the company fact, never about something the company lacks.
- **Never put a prospect's own data and ours in one message.** No message names a prospect's scale, readings, measurements, exams, devices or records and then says what the scan returns: no "next to your scale", no "alongside the measurements you take", no list of their data followed by ours. Describe the scan on its own. Banned framings are in `banned_terms` ("beyond weight", "beyond the scale", "weight only", "non-scale", "tape measure", "guesswork", "unreliable", "inaccurate").
- **Vidalink.** No Vidalink message mentions Peso Saudável, weight-loss pens, GLP-1, prescriptions, their validation, the audit, the balance or anyone's access to a benefit. The scan is an optional body record in Bem-estar 360º or in the Vidalink app in general.
- **Employer, HR and health-plan data.** No message suggests that scan outputs reach HR, an employer, a corporate portal, team indicators, health-plan analytics, pricing, claims, loss ratios or sick-leave management, and no question asks what an employer or HR would want to see. The scan serves the member and their care or nutrition team.
- **Corporate-health boundary.** If a message mentions a health check, check-up, screening or assessment, the same message says that blood pressure, cholesterol, glucose, A1c and other blood tests stay outside the scan. The scan never interprets results or assigns health risk.
- **Partnership lane.** Ask whether a partner capability has any place in the service and who would decide. Never claim the prospect's clients need body scanning, never pitch the scan into a mental-health, counselling or diagnostic workflow, and never compare it with a prospect's own product (N2B's exams, GnTech's tests, Telecárdio's or RWE's reports).
- **Telehealth and medical centres.** The scan returns measurements and estimates the doctor may use; it does not triage, diagnose, decide eligibility for a consult or a procedure, or replace an in-person examination.
- **Aesthetic clinics.** No before-and-after framing, no appearance or shape promises, no "summer body", "bikini", "burn fat" or "fat loss" (banned). The 3D model is a view the clinic chooses to show. The scan never decides whether someone can have surgery or a procedure.
- **Grupo 5S.** Never name, describe, reference or endorse the group's weight-loss method, never use its method's name (banned terms: "Método 5S", "5S method", "5S Emagrecimento"), and never imply 3DLOOK supports any weight-loss method. Address the group as a holding with nutraceutical products and franchise brands only.
- **Franchise networks (Magrass, Emagrecentro, Siluets, Lipocenter, Face Doctor).** Every unit owner or unit staff member is `referral`: one question about who at the franchisor owns the app or the protocol, one line about what the scan returns, the company fact. Never pitch the franchisee on their own unit, never mention other units, owners or the network's size, never suggest HQ is behind or ahead on anything, never mention franchise fees, royalties or investment, and never comment on any app's version history.
- **Spanish- and Portuguese-speaking prospects get English copy** (default). Never mention their country's regulator or law, never mention Brazil to a prospect outside Brazil, and never assume a prospect's language beyond the default.
- **Compliance line: none in any sequence** (default). This overrides the `compliance.md` §9 "Outbound" instruction printed further down in the card: its two lines are written for US and UK/EU deployments and neither fits a Latin American prospect. No compliance, data-protection, regulatory or jurisdiction wording in cold copy: no LGPD, ANVISA, ANS, HIPAA, GDPR, SOC 2, FDA, "compliant", "certified" or medical-device status (all in `banned_terms`). Never claim or imply compliance with any Latin American law, and never mirror a prospect's own wording. Privacy questions in replies are answered from `compliance.md` §10 and the FAQ link; national-law, international-transfer and regulator questions go to legal@3dlook.me.
- **No 3DLOOK client is named anywhere in cold copy.** Anonymised proof allowed: "one weight-management platform ran 34,000 scans in 2025" (no client name, no geography), and "112,100 scans in 2025 across all 3DLOOK customers" (3DLOOK-wide scale only, in its own sentence, never split by client, never tied to a geography or one platform, never placed so it reads as patient or Latin American scans).
- **Numbers only from `proof-points.md`, plus one from `icp-detail.md`.** Allowed: two photos (front and side); "under 45 seconds from the photos to structured results" (the only speed wording, verbatim, every time); 80+ body measurements; body composition estimates (body fat %, lean mass, fat mass) with BMI and BMR as calculated metrics; "96-97% accuracy against expert manual measurement" or the full `accuracy-formulations.md` §1.1 sentence; repeatability only as "For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm."; the 34,000 and 112,100 lines; in `technical-integration` only, "a typical basic integration takes 2-4 weeks". No other number: no prospect's patient, client, unit, staff, revenue, price or result figures, no study results, no medicine prices, no market or obesity statistics, no founding years except as a year ("since 2014").
- **Accuracy wording.** "96-97% accuracy against expert manual measurement" describes body measurements. It never opens Message 2 and never shares a sentence with lean mass, fat mass, body fat or body composition. No ISO 0.40 cm figure. Body measurements are measurements; body composition values are estimates.
- **No outcome promises.** Never promise or imply more weight loss, adherence, retention, engagement, conversions from free evaluations, lower health-plan cost, fewer sick days, ROI or results for a unit. The use-case file's hero line, its "Smart Scales" mismatch and fraud framing and its KPI list are not usable. Describe what the scan returns, where it runs and how much it is used (the two scan-volume lines).
- **What the scan does, and does not do.** It returns measurements and estimates for the care team, nutritionist, doctor, evaluator or member. It does not diagnose, decide eligibility for a treatment, benefit or procedure, recommend or adjust medication, or interpret results. Say "the programme compares scans it selects" or "scan-to-scan comparison", never "tracks each patient". No visceral fat output (banned term).
- **GLP-1.** Outside Vidalink, say "GLP-1" or "weight-loss pens" only; no drug, molecule or pharma names (banned). Never tie the scan to prescribing, dosing or treatment decisions, and never mention prices or price changes.
- **Body image and tone.** Person-first language: "people living with obesity"; never "obese" or "diabetics" (banned). Do not use pregnancy, hormone-replacement, eating-disorder or mental-health programmes as a scan context. With psychologists and mental-health services, keep the message short and neutral.
- **Brands.** Only the prospect's own company, product and programme names, as listed in the facts table. People's former employers may be named, as listed per person (standing decision). Never name one prospect in another prospect's copy. Device, drug, pharma, competitor, client, parent, investor and regulator names are banned (`banned_terms`).
- **Never mention** funding, investors, valuation, revenue, prices, headcount, unit counts, acquisitions or owners.
- **Word traps.** Never "objective" about our data (say "standardized", "timestamped", "structured", "repeatable"); never "comprehensive", "seamless", "leverage", "game-changer"; no em or en dash; no "plus" as a connector; no "so" introducing a benefit; no corrective "X, not Y".
- **Writer notes and card instructions are not copy.** Never paste a sentence or a qualifier from a writer-notes column, a lane description or a script note. "generic figure", "never a promise", "not a promise" and "context only" are banned terms, so a leak fails the gate.
- **No pricing and no trial terms** anywhere in the sequence. A price or trial question goes to the call.
- **Message 1 gate.** Every message 1 carries at least one product specific from `proof-points.md` and one line that could only have been written to that company (a company fact or the person's own hook); each pair of messages cites at least one number. The referral lane is exempt from the product specific.

## Anti-cases (where it does NOT work)

- **Out, by name:** the 33 OUT rows in the verdict table (rows 44-49): Spring Health (US headquarters, `nick`'s market), Takahashi (a four-person eye clinic), non-health companies, former staff, one-person practices and name collisions. Match on the company LinkedIn URL and website, never on the name.
- **Structural anti-cases:**
  - **Displacement:** an account that already runs a phone-camera body scan or has signed a scanning vendor is held for Vadim, never sent standard copy. None on 2026-10-05, with the unread sites noted under "Displacement check".
  - **Partial overlap, not displacement:** an account that already measures by another route stays IN, and copy describes the scan on its own, never next to the prospect's data (Liti, Magrass, Emagrecentro, Instituto Lumiere).
  - **Body composition, diagnostics, counselling or genetics as the prospect's own product:** partnership ask only, never a pitch (N2B Brasil, RWE, Telecárdio, TELUS Health Brazil, Grupo Wellness Latina, Saluta, Zínea, Terapia Online, GnTech, Sensorial).
  - **Franchise units on their own:** a unit cannot integrate an SDK into the franchisor's app; units are referral paths, never buyers.
  - **Methods rejected by a professional body:** the account may be contacted, but copy never references or endorses the method (Grupo 5S).
  - **Head office outside Katya's market:** the account belongs to that market's profile (Spring Health, US). A local subsidiary with its own leadership and page stays with `katya` and is recorded under its own name (Atrys Brasil, TELUS Health Brazil).
  - **Advisors whose role cannot be confirmed as current, investors and former staff:** not at the company.
  - **Public institutions:** SPDM is contacted by referral only; any interest goes through its own procurement.
- **Stop conditions before send:** an account announces an acquisition, a merger or a shutdown (pause, Vadim decides); a phone-camera body scan appears at an IN account (hold); a profile shows the person has left (drop; do not replace from outside the export).

## Vadim's standing decisions (built in, not open questions)

From the step-4 and step-5 checkpoints of `2026-09-29-us-obesity-medicine`, `2026-09-29-us-cardiometabolic` and `2026-10-02-us-virta-health`, the 2026-09-30 client-count rule, and Vadim's brief for this campaign:

1. **No headcount floor** (2026-09-29). Revenue thresholds are not disclosed on this list and are not a FAIL reason.
2. **`cap_per_group: 50`, the default for every campaign; no waves** (2026-09-29). Everyone goes in one closely.io import file at the same time.
3. **A lane for every function, because Vadim takes every pool** (2026-09-29). Every person at an IN company gets one of the six lanes, in priority tiers so the list is ordered.
4. **FAIL only for the wrong company, people who left the company, identity collisions and duplicates.** Company-named profiles and unconfirmed advisors are held, not failed.
5. **Former employers may be named in copy** (2026-09-29), as listed per person.
6. **Live 3DLOOK pages are fine to link as they are** (2026-09-29). Copy still uses only the approved wording in Rules, never a page's variant.
7. **No 3DLOOK client is ever named.** The 34,000-scan line goes with no client name and no geography; "112,100 scans in 2025 across all 3DLOOK customers" is cleared as 3DLOOK-wide scale (2026-09-29). Publicly, "100+ clients" is the only client count (2026-09-30).
8. **No company-researcher step.** The list is Vadim's Sales Navigator export; nobody on it was ever contacted by any profile (verified by the coordinator).
9. **Franchise networks:** the franchisor is the buyer; unit owners and unit staff are referral paths to HQ, grouped under the franchisor's canonical name, which is what `build-import` writes into the registry (this campaign's brief).

## Vadim's decisions 2026-10-05 (scope)

Vadim, 2026-10-05: «всі крім шуму» ("everyone except the noise"). Applied as follows:

1. **IN, from the first version's HELD list:** Siluets, Pró-Corpo, Lipocenter, N2B Brasil, Clínica da Obesidade, Face Doctor. A franchisor is pitched where one exists; units go `referral` to HQ.
2. **IN, from the first version's OUT-on-scope list:** RWE Telemedicina and Telecárdio (tele-diagnostics); L2D, Llamando al Doctor (AR), Reliv (EC) and holadr. IPS (CO) (generalist telehealth); TELUS Health Brazil and Grupo Wellness Latina (employee assistance); Saluta (CL), Zínea and Terapia Online (CL) (mental health); Grupo 5S, with the rule that copy never references or endorses its method and the CFN rejection noted as a risk; Instituto Lumiere.
3. **The health-related rows of the earlier "misc" group, decided per row:** IN: Sensorial (health and cognitive performance), GnTech (personalised health), Céntriqo (medical centre), SPDM (care provider), Inc Beauty (dermatology and aesthetics). OUT: Takahashi (a four-person eye clinic with no use for body data, treated as a one-person practice) and Viva Salute (a natural-products shop; its one person goes to Clínica da Obesidade only if his clinic role is current). The single clinics with staff that the first version had grouped with one-person practices are IN under the same reading: Ihealthy (EC), Perfect clinic (CO), Clínica Lev Vida (company-named row only).
4. **Still OUT, as noise:** non-health corporates (Microsoft, Bank of America, ArcelorMittal Brasil, Softplan, PrimeUp, Soluciones Activ, REVOS), one-person practices, name collisions, former staff, and the duplicates. Company-named rows with no person are held at validation, as before.
5. **Spring Health stays OUT:** its headquarters is in the US, and one company goes to one profile (`nick`).
6. **Accounts outside Brazil are in Katya's market:** Argentina, Chile, Colombia, Ecuador and Bolivia are all in `PROFILE_GEO["katya"]`.
7. **Segments without a use case** (tele-diagnostics, employee assistance, mental health) get a partnership or referral ask, never a pitch that implies they need body scanning; this is the new `partnership` lane. Aesthetic clinics use `icp-detail.md` §9; weight-loss clinics use `fx-telehealth-weight-loss`.

## Defaults Vadim left (decisions taken by default on 2026-10-05; he did not answer)

1. **Language: English** cold copy, for Portuguese- and Spanish-speaking prospects alike. The gates, bans, proof points and approved wording exist only in English, and the card tells the sequencer "language: English". Open question 1.
2. **Compliance: no compliance line in any sequence, in any lane.** `compliance.md` has no LGPD or Latin American wording; its §9 lines are a US line and a UK/EU line. Copy never claims compliance with any Latin American law. Open question 2.
3. **Sender:** `Kateryna` (from `OWNER` in `scripts/outbound_pack.py`) with https://meetings.hubspot.com/kateryna-boichuk (from `outbound-message2-template.md`).
4. **Company-named profiles and unconfirmed advisors are held, not failed** (follows standing decision 4).
5. **No top-up pull.** The list stays as Vadim pulled it; Open question 3 offers one for franchisor HQs.

## Validation criteria (Step 2 will check)

There is no company research. Step 2 builds `companies.csv` from the verdict table, then step 4 validates people against the persona.

- **Companies.** 43 rows, one per IN group, written with the aliases above the verdict table, `hq_country` as on the page (Brazil, Argentina, Ecuador, Colombia or Chile), LinkedIn URL and website from the verdict table. OUT accounts go to `companies-routed-out.csv` with their reasons. `outbound-registry.py check --profile katya` runs on the export and must come back clean; `record` registers only the 43 canonical names, never an alias-only company or any OUT company.
- **Displacement re-check.** Before import, confirm that no IN account shows a phone-camera body scan or a scanning vendor; for the eight accounts whose site could not be read, try again. Known overlap (Liti, Magrass, Emagrecentro, Instituto Lumiere, N2B) is not displacement.
- **Branches and checks, by name:** listed under the verdict table and in "Target buyer persona" (Gabriela Biazus, Flaminio Dalul, aline caio, the Emagrecentro directors, Clínica da Obesidade, Perfect clinic, Ihealthy, the Pró-Corpo identities, the four advisors, Indira Cruz and Ulysses Maciel, Martin Samaniego, the 12 company-named profiles, the 3 duplicates). A job-change check runs on all 163.
- **Name collisions to fail by name** (they match IN name keys in `extract-people`): Marta Larti (`liti`, Argentina), Claudia Posada (`Nilo`, Colombia), Cristina Nanin (`Terapia Online`, Brazil; the account is the Chilean service) and Silbia Díaz (on the Pró-Corpo page, Uruguay; Pró-Corpo has no Uruguayan unit).
- **People.** 163 PASS with the tiers and lanes in "Target buyer persona": P1 15, P2 20, P3 33, P4 95. Lanes: `referral` 95, `product` 23, `technical-integration` 16, `partnership` 16, `operations` 10, `clinical` 3. FAIL only for the rows named in "Not the buyer".
- **Message 1 gate.** Every message 1 carries at least one product specific from `proof-points.md` and one line that could only have been written to that company or that person; each pair of messages cites at least one number. Zero client names, zero pricing, zero `banned_terms`, zero compliance lines, zero messages that put a prospect's data next to ours, zero Vidalink mentions of the pen benefit, zero routing of body data to HR, zero outcome promises. Kept as a failure, not a note: `2026-07-21` sent 307 message 1 texts with no specific and drew 1 reply on 67 sends.
- **Proof in product-info.** Use-case file and live articles: yes. Reference customer in Latin America: none; the anonymised weight-management proof (34,000 scans) and 3DLOOK-wide scale (112,100 scans) are used openly, not hidden.

## Success metrics for this campaign

Denominators as in `metrics-final.json` (Closely event counters). 163 invites across 41 accounts, 111 of them `referral` or `partnership` asks: read per segment, not only as rates.

| Metric | Target | Floor | Basis |
|---|---|---|---|
| Invites sent | 163 | 145 | after the job-change and identity checks |
| Connection acceptance rate | 20% (about 33) | 12% (about 20) | `katya` in Israel: 38/127 = 29.9%, with no language barrier |
| Replies per accepted person | 10% | 5% | `katya` in Israel: 4/38 = 10.5% |
| Positive replies from P1 or P2 (interest or question) | 3 | 1 | 35 people at P1-P2 |
| Referral replies naming an owner | 5 | 2 | 95 referral invites, 36 of them franchise or chain paths |
| Partnership replies (any answer, yes or no) | 2 | 0 | 16 partnership invites |
| Accounts with at least one reply | 6 of 41 | 3 | |
| Discovery calls | 2, at different accounts | 1 within 8 weeks | |
| Pilot | not a target | | data-protection and procurement questions are open (Risks) |

**Falsified if** three or more P1 or P2 replies say a phone body record is not a priority next to the scale, bioimpedance or staff measurements they already use, or that body measurements have no place in their programme. **A language signal, not a falsification,** if two or more replies ask for Portuguese or Spanish or say English was the obstacle: that answers Open question 1. **Inconclusive, and the post-mortem says so, if fewer than 20 people accept.** Read the partnership segments separately: a polite no from them is an expected outcome.

## Risks

1. **Language.** Cold English to Portuguese and Spanish speakers, many of them franchise owners and frontline staff.
2. **Katya's profile.** `CLAUDE.md` §5 still lists `linkedin-katya` as "Israel + Gulf" for social; if her LinkedIn headline or activity still points at Israel, Latin American prospects may not accept. Profile audit not done (Open question 5).
3. **Volume on one account.** 163 invites at once on Katya's profile, against her 127 in Israel; Closely pacing and LinkedIn's weekly invitation limits will stretch the send over several weeks (Open question 6).
4. **Data protection.** FitXpress is hosted on AWS in the US. Buyers handling health data will ask about LGPD and the data-protection laws of Argentina, Chile, Colombia and Ecuador, and about international transfer; there is no approved answer beyond `compliance.md` and legal@3dlook.me.
5. **Eligibility drift at Vidalink.** A prescription-validated pen benefit invites the reading "the scan checks who qualifies"; the Rules keep every Vidalink message away from the benefit.
6. **"We already measure."** Liti, Magrass, Emagrecentro, Instituto Lumiere and N2B already measure, and bioimpedance is common in Latin American clinics. There is no published comparison of FitXpress estimates with bioimpedance.
7. **Grupo 5S.** Brazil's Federal Nutrition Council published the 2017 opinion of the national nutrition association rejecting the group's weight-loss method ([CFN](https://cfn.org.br/parecer-tecnico-da-asbran-reprova-metodo-5s/)). Any reply or deal there must not associate 3DLOOK with the method.
8. **Unverified franchisors and identities.** Siluets and Lipocenter have no reachable website; Pró-Corpo's owner-titled rows may not be owners; Clínica da Obesidade and Perfect clinic are unidentified.
9. **Low-fit segments.** Tele-diagnostics, employee assistance, mental health, genetics and cognition have no use case; their replies, if any, will mostly be no.
10. **Population scope.** Training data from the US and Europe; validation 38-210 kg; performance on Latin American populations has not been characterized separately.
11. **Franchise dynamics.** 30 franchise-network invites across five networks may reach HQs as noise. Mitigation: referral only, a different question each, no unit pitch; Open question 3 offers an HQ pull.
12. **Public procurement and small budgets.** SPDM buys through its own procurement; MedTrue, Instituto Lumiere, Ihealthy and Inc Beauty are small; prices are in US dollars.

## Open questions for Vadim

1. **Language: English (default), Brazilian Portuguese, or Spanish for the Spanish-speaking accounts?** Portuguese or Spanish copy would need translated bans, approved wording and a gate that reads those languages, and Katya would have to answer replies in them. Default: English.
2. **Compliance and regulatory wording for Latin America.** No line in any sequence by default. Should legal prepare answers on LGPD, the other national data-protection laws and international transfer (and say whether anything is needed for ANVISA or other regulators) before replies come in? Default: none in copy; replies go to legal@3dlook.me.
3. **Top-up pull for franchisor HQs** (the `titles` block, through Sales Navigator or Apollo) inside Magrass, Emagrecentro, Siluets, Lipocenter and Face Doctor, and for the missing medical and product leads at Liti, Vidalink, Salvia and MedTrue? Magrass's expansion director was named in 2023 press. Default: no pull; franchise people go as referral.
4. **A use-case file for aesthetic clinics** (`use-cases/fx-plastic-surgery.md`, flagged as missing in `INDEX.md`). This campaign restates `icp-detail.md` §9 in the card instead. Create the file before the next aesthetic campaign? Default: restatement only.
5. **Katya's LinkedIn profile** still framed for Israel? Audit before send, or accept the risk as on `nick` (2026-09-29)? Default: accept as is.
6. **163 invites in one file:** keep the standing one-file rule and let Closely pace it, or send the core accounts first? Default: one file, as decided on 2026-09-29.

## QC fix round 2026-10-05 (QC 15/20, all 21 fixes applied, together with the scope widening)

Report: `workspace/_quality/outbound/2026-10-05-hypothesis-generator-latam-health-weightloss.md`.

1. Luis Gonzalez's question no longer places the scan next to the pen prescription; it places it in Bem-estar 360º.
2. The Vidalink fact that carried the prescription validation and the balance is out of copy; Vidalink facts are now Bem-estar 360º, the one-app description, humanisation and technology, and the smaller-company plan.
3. The AI-audit fact is out of copy, and Jorge Sousa's question no longer mentions the prescription check; a Vidalink rule bans the pen benefit from every Vidalink message.
4. No question or fact routes body data to HR: Daniela Junqueira's and Fernanda Maluf's questions were rewritten, and HR, corporate-portal, health-plan-intelligence and sick-leave facts are out of copy, with a matching rule.
5. Fernando Vilela's question no longer lists Liti's scale readings before adding ours; a rule bans putting a prospect's data and ours in one message.
6. The Liti card line no longer foregrounds waist and hip; Liti, Magrass, Emagrecentro, N2B and Instituto Lumiere data are all kept out of copy.
7. Magrass is no longer pitched as "the same way in every unit"; the scan is a capture clients take at home between unit visits.
8. Thiara's question no longer presupposes that AppGES records body measurements.
9. Alessi Soncini has a company fact (OM1).
10. The corporate-health boundary now includes A1c and the source's rule that the copy must say so, as a condition on any message that mentions a health check.
11. Luis Gonzalez's hook quotes his bio: he "helped establish BCG's first office in Brazil" (no co-founding, no city).
12. Every instruction that sat inside a fact string moved to a separate "Writer notes" column.
13. "visceral" and every other banned term are gone from the fact strings.
14. "As a general resource" and similar paste-able wording are gone; the asset table carries writer notes instead.
15. "No franchisor executive is in the export" is no longer asserted: Gabriela Biazus, Flaminio Dalul and aline caio each have a validator branch, and Open question 5 of the first version is resolved by the scope decision.
16. The Magrass asks no longer repeat each other: Rafaela Klein asks about the nutrition routine and Gabriela Biazus about marketing; Fabricio Pires asks about technology partnerships and Renata Assuncao about purchasing.
17. The displacement check now names the eight sites that could not be read.
18. The Olhar Digital claim now quotes the article text fetched on 2026-10-05 ("chegada às farmácias em 15 de junho").
19. Instituto Lumiere is IN; its in-clinic body-composition assessment is treated as overlap, not a reason to exclude.
20. "Brazil's GLP-1 market opened in 2026" now reads "widened in 2026", consistent with 14 of 25 pens registered that year.
21. The banned term "tape measure" no longer appears in any card line written for the writer.

## Sources

- Export: `sales-nav-raw/export-1.csv` (211 rows, summarised with stdlib `csv` scripts grouped by company LinkedIn URL; not read whole). Company descriptions and specialities for Siluets, Pró-Corpo, Lipocenter, N2B, Face Doctor, RWE, Telecárdio, L2D, Llamando al Doctor, Reliv, holadr. IPS, Céntriqo, TELUS Health Brazil, Grupo Wellness Latina, Saluta, Zínea, Terapia Online, Grupo 5S, Instituto Lumiere, Sensorial, GnTech, SPDM, Inc Beauty, Amparo Saúde, Abertta Saúde and Wellbe come from the `Company description` and `Company specialities` columns of that file.
- Market context: https://agenciagov.ebc.com.br/noticias/202609/ministerio-da-saude-protocola-na-conitec-pedido-de-analise-para-incorporacao-de-canetas-emagrecedoras-no-sus (fetched 2026-10-05) · https://olhardigital.com.br/2026/06/02/medicina-e-saude/ems-anuncia-precos-da-primeira-caneta-nacional-de-semaglutida/ (fetched 2026-10-05) · https://portal.afya.com.br/saude/vigitel-2025-aponta-piora-do-sono-entre-brasileiros-e-avanco-de-doencas-cronicas · Lancet Commission as verified for `2026-09-29-us-cardiometabolic`: https://www.thelancet.com/journals/landia/article/PIIS2213-8587(24)00316-4/fulltext
- Vidalink: https://vidalink.com.br/ · https://conteudo.vidalink.com.br/vidalink-peso-saudavel · App Store id979258786 (v5.10.8, 2026-09-22)
- OrienteMe: https://www.orienteme.com.br · App Store id1300163763 (3.3.3, 2026-10-04)
- GESmed: https://diariodocomercio.com.br/negocios/healthtech-mineira-aposta-na-saude-corporativa/ · App Store "AppGES" id1660037045
- Salvia: https://salviasaude.com.br/ · App Store id1594370524
- Atrys Brasil / AxisMed: https://medicinasa.com.br/atrys-axismed/ · https://www.atryshealth.com/en/nota-de-prensa/atrys-grows-in-the-first-half-of-2025/
- Wellbe: https://www.revistaapolice.com.br/2022/07/wellbe-aposta-em-nova-area-de-gestao-de-saude-para-clientes/ · https://startupi.com.br/tags/wellbe/
- iMND: https://imnd.com.br · App Store "iMND Saúde" id6744750210
- Nilo Saúde: http://nilosaude.com.br
- Liti: https://liti.com.br/ · App Store "Liti Saúde" id1616229381 (4.56.0, 2026-10-02) · https://www.bloomberglinea.com.br/2023/06/14/na-onda-ozempic-esta-startup-elegeu-como-foco-o-sobrepeso-e-a-obesidade/ · https://vitat.com.br/liti-vale-a-pena-assinar/ (2023-09-18, modified 2024-03-20) · https://latamlist.com/brazilian-healthtech-liti-raises-4m-seed-round-to-fight-obesity/
- MedSlim: https://emagrecer.soumedslim.com.br
- Magrass: https://franquias.portaldofranchising.com.br/franquia-magrass-estetica/ (09/2026) · https://www.magrass.com.br/ · https://www.portaldofranchising.com.br/noticias/nova-microfranquia-da-magrass-vende-12-unidades-em-1-mes/ (2023-08-21) · App Store "Magrass Club" id1450531454
- Emagrecentro: https://www.portaldofranchising.com.br/noticias/emagrecentro-forca-e-inovacao/ (2025-11-27) · https://www.portaldofranchising.com.br/noticias/emagrecentro-impulsiona-expansao-sob-a-bandeira-best-shape/ (2024-01-24) · https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9332815/ · App Store id6478176820
- Instituto GL: https://www.institutogl.com.br · Grupo Endos: https://endosfit.com.br/ · Amparo Saúde: https://exame.com/negocios/grupo-sabin-compra-rede-de-atencao-primaria-amparo-saude/ · Abertta Saúde: http://www.aberttasaude.com.br · App Store id1579515747 (3.5.4, 2026-09-28)
- Widened accounts: http://www.procorpoestetica.com.br · https://www.portaldofranchising.com.br/noticias/siluets-franchising-apresenta-dois-modelos-de-negocios-no-abf-expo/ · http://www.n2bbrasil.com · https://cfn.org.br/parecer-tecnico-da-asbran-reprova-metodo-5s/ (2017-09-19) · https://institutolumiere.com.br/lumiere/ · https://www.llamandoaldoctor.com · https://holadr.com.co/ · http://www.grupowellnesslatina.com · unreachable on 2026-10-05: siluets.com.br, lipocenter.com.br, 5sgrupo.com.br, l2d.com.br, gesmed.com.br, atrys.com.br (did not resolve), emagrecentro.com.br (403), reliv.la (429)
- Live 3DLOOK assets (HTTP 200 on 2026-10-05): https://3dlook.ai/content-hub/glp-1-market/ · https://3dlook.ai/content-hub/ai-body-data-wellness-platforms/ · https://3dlook.ai/content-hub/bariatric-pre-qualification-mobile-3d-body-scanning/ · https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/ · checked and not linked: https://3dlook.ai/content-hub/the-potential-of-ai-in-telehealth/ (retired compliance wording) · not live (404): https://3dlook.ai/content-hub/glp-1-patient-progress-record-body-data/
- Internal: `2026-07-23-israel-telehealth/post-mortem.md` and `metrics-final.json` · `2026-10-02-us-virta-health/hypothesis.md` · `2026-09-29-us-cardiometabolic/hypothesis.md` · `2026-08-14-au-digital-fitness/hypothesis.md` · `_quality/outbound/2026-10-02-{hypothesis-generator,message-sequencer}-{us-virta-health,au-digital-fitness}.md` · `_quality/outbound/2026-10-05-hypothesis-generator-latam-health-weightloss.md` · `icp-detail.md` §1, §4, §5, §9 and IT & Technical Roles · `use-cases/fx-telehealth-weight-loss.md` · `use-cases/fx-wellness-rewards.md` · `proof-points.md` · `accuracy-formulations.md` · `compliance.md` · `tech-spec.md` · `scripts/outbound_pack.py` (`OWNER`, `calendar_link`, `CARD_SECTIONS`) · `scripts/outbound-pipeline.py` (`PROFILE_GEO`, `company_keys`, alias matching checked on the raw names)

## Vadim's decisions 2026-10-05 (run without checkpoints)

Vadim: «продовжуй без апруву» (2026-10-05), after choosing the scope «всі крім шуму». Opus QC still runs after the validate and messages stages, and its fixes go back to the agent that wrote the artifact. Defaults taken on the open questions:

1. **Language: English** cold copy.
2. **No compliance line** in any sequence, and no claim about LGPD or other local law.
3. **No top-up pull** for franchisor HQ leaders. Unit owners go referral to HQ, as written.
4. **Aesthetic clinics** use icp-detail §9 as paraphrased in this file. There is no separate use-case file.
5. **Katya's LinkedIn profile positioning:** the risk is accepted, and Vadim decides any profile change.
6. **One import file** for every IN person (no waves).
The hypothesis was re-scoped after its QC (15/20; the 21 fixes were applied in the same pass). It was not re-QC'd as a whole: the validate and messages QCs cover the new lanes.
