---
product: fitxpress
profile: olena
market: Continental Europe (UK excluded)
created: 2026-10-07
status: approved
approved: 2026-10-07
use_case: fx-telehealth-weight-loss
cap_per_group: 50
referral_call: yes
banned_terms: [Yazen, UK Meds, Healthyr, Safariland, Burlington, Jim's Formal Wear, Generation Tux, Tailoor, Redthread, Erakulis, Prism, Bodygram, Size Stream, InBody, Tanita, Withings, Evolt, Styku, Fit3D, Seca, Accuniq, Neo Health, Technogym, Mywellness, Oviva, Ozempic, Wegovy, Mounjaro, Zepbound, Saxenda, Rybelsus, Foundayo, semaglutide, tirzepatide, liraglutide, orforglipron, Novo Nordisk, Lilly, Pfizer, zanadio, aidhere, Diætisthuset, Momenta, Cambridge Weight Plan, Balance Company, Orkla, HIPAA, SOC 2, FDA, MDR, CE mark, DiGA, BfArM, Assurance Maladie, reimbursed, reimbursement, compliant, certified, certification, accredited, clinically validated, clinically proven, verify, verified, verification, eligibility, eligible, Smart Scales, mismatch, fraud, self-reported, guesswork, unreliable, inaccurate, error-prone, tape measure, beyond the scale, beyond weight, non-scale, scale weight, weight alone, weight only, just weight, obese, diabetics, before and after, before-and-after, bikini, summer body, burn fat, fat loss, fat reduction, cellulite, anti-aging, cryolipolysis, guarantee, guaranteed, ROI, reversal, cure, DEXA, DXA, BIA, bioimpedance, MRI, visceral, pregnancy, pregnant, postnatal, funding, investors, investor, valuation, acquisition, acquired, merger, royalties, franchise fee, generic figure, never a promise, not a promise, context only, writer note, Circling back, Following up, Saw your post]
---

# Outbound Hypothesis: 2026-10-07, Continental European weight-loss and nutrition programmes (fixed list, Olena)

- **Campaign:** `2026-10-07-eu-weight-loss-nutrition`
- **Owner and sender:** Olena Kudryavtseva, BD, profile `olena`, market Continental Europe (UK excluded). `OWNER["olena"] = "Olena"`: every message ends with `Olena` alone on the last line. Calendar link (Message 2, every lane): https://meetings.hubspot.com/olena-kudriavtseva.
- **Company list: fixed, not researched.** Vadim's closely.io enrichment of a Sales Navigator keyword search (filter in `export-summary.md`), `sales-nav-raw/export-1.csv`: 295 people, 110 groups, read with stdlib `csv`. No company-researcher step: step 2 is `companies.csv` (21 rows), written in this run from the verdict table.
- **ICP:** icp-detail.md §1 (Telehealth & GLP-1 / Weight Loss Programs) is the core: centre-based and app-based weight-management and nutrition-coaching programmes. §5 (bariatric / metabolic) covers FitForMe; §8 (Connected & Digital Fitness) covers the EMS and gym networks and the two software platforms. AMRA Medical matches no segment and is held for Vadim (Open question 11).
- **Use-case file:** `use_case: fx-telehealth-weight-loss` (the IN majority is weight-management programmes: 98 of 158 people). Its hero line ("Verify body progress ... prove program ROI"), its Smart Scales framing and its KPI list are not usable here (Rules).
- **Registry, checked 2026-10-07** (`outbound-registry.py check --profile olena`, dry run, and every registry): 28 export people were messaged from `olena` in `2026-07-21-eu-telehealth-weightloss`; 17 more sit at those companies. No export person is in another profile's registry, no IN account is covered by another profile or is a 3DLOOK customer. `2026-07-22-eu-telehealth` was never sent; `2026-09-14-eu-erakulis-similar` shares no company with this list.

> **Read this first.**
> 1. **158 people IN, 137 OUT, 295 in all. 21 accounts IN.** OUT: outside the ICP 66 (GymBeam 29, BioTechUSA 19, HSNG 6, TATOI Club 6, MM Sports 3, Body & Fit 3: product retail or a members club); `olena` registry 40 (Oviva 25; Sidekick 6 and Liva 2 already messaged; The Body Clinic 4; Nederlandse Obesitas Kliniek 1; the Dutch obesity foundation 1; Sword 1, also US-HQ); junk 23 (name collisions 6, unrelated businesses 7, single sites, freelancers and consultants 10); people at IN accounts 6 (4 duplicate profiles, 1 job-seeker, 1 identity collision); held for Vadim 2 (AMRA Medical, Open question 11). 66 + 40 + 23 + 6 + 2 = 137.
> 2. **13 OUT rows join an IN account by name** in `extract-people` and must be failed by name at validation (list under the verdict table). The other 124 join nothing (`extract-people --dry-run`, 2026-10-07: 171 kept, 124 dropped).
> 3. **Re-entry at two accounts Olena worked in July.** Sidekick Health (4 new people) and Liva Healthcare (1) are IN through new people only; `check` will flag them `company already worked from olena`, and Vadim clears them as he did at the 2026-09-28 checkpoint of `2026-09-27-uk-bariatric-prequal` (Open question 3). Oviva is OUT whole: 30 Oviva people were messaged in July and Oviva declined on 2026-08-27 (Open question 2).
> 4. **Franchise networks dominate.** RNPC 29, Dietplus 25, BODYHIT 20 and fitbox 12 are mostly unit owners: 107 of 158 people are `referral`, under Vadim's decision 4 and gated like every other lane (`referral_call: yes`).
> 5. **Apollo top-up: `apollo_topup=yes` on 19 accounts, `no` on 2** (SATISFEAT and Clinique La Prairie: the deciders are in the export); the flag and its reason are in each `companies.csv` row's `notes`. `search` queries every row with a website: drop the `no` accounts from `apollo-candidates.csv` before `enrich`. Sidekick and Liva take new people only; Apollo people outside Continental Europe are OUT (Open question 10).
> 6. **cap_per_group 50, unchanged** (largest: RNPC 29, Dietplus 25, BODYHIT 20; past 50, head-office people first).
> 7. **Overlap at eight accounts, displacement at none** (no phone-camera body scan found, 2026-10-07); dietplus.fr returned 403. **No client app at RNPC, Dietplus, Naturhouse France or Ysonut** (App Store searches, 2026-10-07): their copy never mentions an app (one line per account in Message angle).
> 8. **Lanes:** `referral` 107, `product` 32, `operations` 10, `technical-integration` 5, `partnership` 2, `clinical` 2. Tiers: P1 23, P2 21, P3 7, P4 107.

---

## Vertical

Continental European weight-management and nutrition-coaching programmes that follow a person over weeks or months (in a centre, with a coach, or in an app), together with the fitness networks and software platforms that run member progress for gyms, and one longevity clinic.

## Sub-segment

The 21 IN accounts, by segment:

- **A. Weight-management and nutrition-coaching networks (franchisor or head office is the buyer):** RNPC (Groupe Éthique et Santé, France), Dietplus (France, Spain, Belgium), Naturhouse France, NUTRIADAPT (Czechia), Het 1 op 1 Dieet (Netherlands and Belgium), Laboratorios Ysonut (Spain), Metabolic Balance (Germany), Nutrimed (Greece).
- **B. Digital programmes and nutrition technology:** Sidekick Health (Iceland, re-entry), Liva Healthcare (Denmark, re-entry), FitForMe (Netherlands, BariBuddy app), Nutrium (Portugal, dietitian software), maju (France), The Fabulous (France).
- **C. Fitness networks and fitness platforms:** BODYHIT and fitbox (EMS franchises), Keepcool and Vivafit (club networks), Virtuagym (gym software), SATISFEAT (partnership).
- **D. Longevity clinic:** Clinique La Prairie (Healthy Weight programme, Longevity Hubs).

**Size:** no headcount floor (2026-09-29). Revenue is not disclosed by most accounts and is not a FAIL reason on this list.

## Company types in scope: verdict table (one row per export group)

Matching in `extract-people` is on name keys, so collisions are failed by name. Checked with the pipeline's own `company_keys` / `shortlist_keys` on the export: 171 rows join an IN account (158 IN and the 13 fail-by-name rows), 124 join nothing, no key collides between two IN accounts, every account routes to `olena` with fit high or medium.

**Aliases** are written in `companies.csv` (`Canonical (alias / alias)`; the canonical is outside the parentheses). Export cells written with ` / ` (`RNPC / Groupe Ethique et Santé`, `BODYHIT Guérande/La Baule & Pornichet`) are aliased with ` - ` (the parser splits on `/`; both forms normalise to one key); `Indépendant` (Corinne Brunet, Directrice Centre RNPC), `Dsign.`, `LM2S Consulting` and `pure fitness&health GmbH` (fitbox franchise owners' own companies), `Balance Centrum` (Metabolic Balance Slovakia), `Duke University Advanced Hindsight Lab` (Sami B. of Fabulous) and `Bindinc.` (Nanda Zwart's employer) are each one person's cell; FITOMAT is fitbox GmbH's registered smart-gym brand (fitomat.com/de/impressum). Never aliased: `Bodyhit Lyon Brotteaux`, `ysonut`.

| # | Export group (rows) | IN | OUT | Account | Lanes | Apollo | Reason |
|---|---|---|---|---|---|---|---|
| 1 | gym-beam: `GymBeam` | 0 | 29 | - |  |  | Supplement, food and sportswear e-commerce; its app is a shop (App Store SK listing). Outside ICP (Open question 1) |
| 2 | oviva: `Oviva` | 0 | 25 | - |  |  | Worked from `olena` 2026-07-21 (30 people, 13 of these 25), declined 2026-08-27 (Open question 2) |
| 3 | groupe-ethique-et-sant-: `RNPC / Groupe Ethique et Santé`, `Réseau RNPC`, `Réseau RNPC / Groupe Ethique et Santé`, `Groupe Ethique et Santé`, `Groupe Ethique et Santé / RNPC` | 20 | 0 | RNPC | referral 18, product 2 | yes | Franchisor page; centre directors; no client app |
| 4 | biotechusa: `BioTechUSA`, `BioTech USA` | 0 | 16 | - |  |  | Supplement maker and shops; its app is a shop with loyalty points and a calorie log (App Store HU listing). Outside ICP (Open question 1) |
| 5 | clinique-la-prairie: `CLINIQUE LA PRAIRIE` | 13 | 0 | Clinique La Prairie | product 6, operations 4, referral 2, clinical 1 | no | Longevity clinic; Healthy Weight programme and Longevity Hubs |
| 6 | bodyhit: `BODYHIT` | 12 | 0 | BODYHIT | referral 11, operations 1 | yes | EMS franchise; club owners |
| 7 | dietplus: `dietplus`, `dietplus franchise` | 9 | 1 | Dietplus | referral 7, product 2 | yes | Franchisor page; no client app. OUT: duplicate profile |
| 8 | sidekick-health: `Sidekick Health` | 4 | 6 | Sidekick Health | technical-integration 2, operations 1, product 1 | yes | Re-entry, new people only (Open question 3). OUT: 6 already messaged 2026-07-21 |
| 9 | fitbox-gmbh: `fitbox GmbH - DIE FITNESS REVOLUTION` | 8 | 1 | fitbox | referral 8 | yes | EMS franchise; owners and studio heads. OUT: duplicate profile |
| 10 | virtuagym: `Virtuagym` | 7 | 0 | Virtuagym | product 3, referral 2, partnership 1, technical-integration 1 | yes | Gym software and white-label member apps |
| 11 | fitforme: `FitForMe` | 6 | 0 | FitForMe | product 2, referral 2, operations 1, technical-integration 1 | yes | Bariatric and weight-loss-medication supplements; BariBuddy app |
| 12 | naturhouse-france: `NATURHOUSE France` | 6 | 0 | Naturhouse France | referral 6 | yes | Centre managers; weekly follow-up in centre or by teleconsultation; no client app |
| 13 | nutriadapt: `NUTRIADAPT - Nutrition & Beauty Clinic`, `NUTRIADAPT - Weight Management Clinic` | 6 | 0 | NUTRIADAPT | referral 4, product 2 | yes | 50+ weight-management clinics; client app |
| 14 | 1op1dieet: `Het 1 op 1 Dieet`, `Cambridge Weight Plan Benelux BV`, `The 1:1 Diet by Cambridge Weight Plan Nederland & België` | 5 | 0 | Het 1 op 1 Dieet | referral 3, operations 1, product 1 | yes | Benelux licensee of The 1:1 Diet (Dutch BV); CEO, COO, consultants |
| 15 | hsng: `Health and Sports Nutrition Group AB` | 0 | 5 | - |  |  | Supplement e-commerce (Orkla). Outside ICP |
| 16 | tatoi-club: `TATOI Club` | 0 | 5 | - |  |  | Private members club. Outside ICP |
| 17 | `Centre RNPC` | 3 | 1 | RNPC | referral 3 | #3 | Centre directors. OUT: duplicate profile |
| 18 | thebodyclinic: `The Body Clinic` | 0 | 4 | - |  |  | All 4 messaged from `olena` 2026-07-21 (Open question 4) |
| 19 | body-and-fit: `fit&Body`, `Body & Fit`, `Body&Fit` | 0 | 3 | - |  |  | Sports-nutrition e-commerce. Outside ICP |
| 20 | livahealth: `Liva Healthcare` | 1 | 2 | Liva Healthcare | product | yes | Re-entry, new people only (Open question 3). OUT: CEO and CPTO already messaged |
| 21 | nutrium-company: `Nutrium`, `Nutrium - Personalised nutrition software` | 3 | 0 | Nutrium | product 2, clinical 1 | yes | Dietitian software and Nutrium Care |
| 22 | ysonut: `Laboratorios YSONUT` | 3 | 0 | Laboratorios YSONUT | product 2, referral 1 | yes | Nutrition programmes through health professionals; no app. Qnko Qnkov: identity check |
| 23 | amramedical: `AMRA Medical` | 0 | 2 | - |  |  | MRI body-composition analytics: no `icp-detail.md` segment, no partnership scope decision here. Held for Vadim (Open question 11) |
| 24 | mm-sports: `MM Sports`, `MM SPORTS` | 0 | 2 | - |  |  | Sports-nutrition retailer |
| 25 | vivafit: `VIVAFIT` | 2 | 0 | Vivafit | product 1, operations 1 | yes | Fitness-club franchise (Balance Company group); VivaFit App |
| 26 | balance-centrum: `Balance Centrum` | 1 | 0 | Metabolic Balance | referral | yes | Katarina Grich, Metabolic Balance Slovakia |
| 27 | bindinc-: `Bindinc.` | 1 | 0 | Het 1 op 1 Dieet | referral | #14 | Nanda Zwart, owner of a Het 1 op 1 Dieet practice (headline); the cell is her employer, aliased for her row |
| 28 | duke-university-behavioral-health: `Duke University Advanced Hindsight Lab` | 1 | 0 | The Fabulous | product | yes | Sami B., co-founder and CEO of Fabulous; cell is his former incubator |
| 29 | enseigne-keep-cool: `Keepcool` | 1 | 0 | Keepcool | product | yes | Gym network, 300+ clubs (group); Head of Com & Growth |
| 30 | fabulous-app: `The Fabulous` | 1 | 0 | The Fabulous | technical-integration | #28 | CTO |
| 31 | fitomat: `FITOMAT®` | 1 | 0 | fitbox | product | #9 | Ingo Huppenbauer, CEO of fitbox GmbH, founder of FITOMAT |
| 32 | footshop: `Footshop` | 0 | 1 | - |  |  | Streetwear retail |
| 33 | gynzy: `Gynzy` | 0 | 1 | - |  |  | Education software |
| 34 | lm2s-consulting: `LM2S Consulting` | 1 | 0 | fitbox | referral | #9 | Sanja Kuche, owner of fitbox Berlin Friedenau |
| 35 | maju-nutrition: `maju` | 1 | 0 | maju | product | yes | Connected portion bowl and app with dietitians |
| 36 | metabolic-balance: `Metabolic Balance® - Company` | 1 | 0 | Metabolic Balance | product | #26 | Geschäftsführer |
| 37 | mtbiker: `MTBIKER` | 0 | 1 | - |  |  | Cycling e-shop |
| 38 | `A FIT BODY` | 0 | 1 | - |  |  | Single site or freelancer |
| 39 | `Activepower` | 0 | 1 | - |  |  | Single site or freelancer |
| 40 | `BODYHIT BORDEAUX MÉRIADECK` | 1 | 0 | BODYHIT | referral | #6 | Company-named profile: identity check |
| 41 | `BODYHIT Guérande/La Baule & Pornichet` | 1 | 0 | BODYHIT | referral | #6 | Unit |
| 42 | `BODYHIT MA` | 1 | 0 | BODYHIT | referral | #6 | Unit |
| 43 | `BODYHIT NANTES` | 1 | 0 | BODYHIT | referral | #6 | Unit |
| 44 | `BODYHIT TOULOUSE CAPITOLE` | 1 | 0 | BODYHIT | referral | #6 | Unit |
| 45 | `BODYHIT Tours` | 1 | 0 | BODYHIT | referral | #6 | Unit |
| 46 | `BODYHIT Wagram - Paris 17ème` | 1 | 0 | BODYHIT | referral | #6 | Unit |
| 47 | `BW Consultancy` | 0 | 1 | - |  |  | HSNG engineer |
| 48 | `BioTechUSA Kft.` | 0 | 1 | - |  |  | BioTechUSA entity or shop |
| 49 | `Biotech Nutrition Germany GmbH` | 0 | 1 | - |  |  | BioTechUSA entity or shop |
| 50 | `Biotechusa echirolles` | 0 | 1 | - |  |  | BioTechUSA entity or shop |
| 51 | `Body Fit` | 0 | 1 | - |  |  | Single site or freelancer |
| 52 | `Body Fit Clinics` | 0 | 1 | - |  |  | Single site or freelancer |
| 53 | `Bodyhit` | 1 | 0 | BODYHIT | referral | #6 | Unit |
| 54 | `Bodyhit Lyon Brotteaux` | 0 | 1 | - |  |  | Samuel Combes-Ouragan, job-seeking; cell not aliased |
| 55 | `Centre RNPC Nîmes` | 1 | 0 | RNPC | referral | #3 | Unit |
| 56 | `Centre RNPC Salon-de-Provence` | 1 | 0 | RNPC | referral | #3 | Unit |
| 57 | `Centre rnpc` | 1 | 0 | RNPC | referral | #3 | Unit |
| 58 | `Clinique de Prairie` | 0 | 1 | - |  |  | Danish skin therapist, name collision |
| 59 | `DIETPLUS EYSINES` | 1 | 0 | Dietplus | referral | #7 | Unit |
| 60 | `DIETPLUS MORANGIS` | 1 | 0 | Dietplus | referral | #7 | Unit |
| 61 | `DIETPLUS ROYAN` | 1 | 0 | Dietplus | referral | #7 | Unit |
| 62 | `Dieet Coach Zwijndrecht` | 1 | 0 | Het 1 op 1 Dieet | referral | #14 | 1:1 Diet consultant |
| 63 | `Dietplus` | 1 | 0 | Dietplus | referral | #7 | Unit |
| 64 | `Dietplus Frouard` | 1 | 0 | Dietplus | referral | #7 | Unit |
| 65 | `Dietplus Grenade` | 1 | 0 | Dietplus | referral | #7 | Unit |
| 66 | `Dietplus Laval` | 1 | 0 | Dietplus | referral | #7 | Unit |
| 67 | `Dietplus forbach` | 1 | 0 | Dietplus | referral | #7 | Unit |
| 68 | `Dietplus la roche sur foron` | 1 | 0 | Dietplus | referral | #7 | Company-named profile: identity check |
| 69 | `Dsign.` | 1 | 0 | fitbox | referral | #9 | Dennis Krebs, fitbox Krefeld franchisee |
| 70 | `Fit Body` | 0 | 1 | - |  |  | Single site or freelancer |
| 71 | `Fit body Coaching` | 0 | 1 | - |  |  | Single site or freelancer |
| 72 | `Fit'forme` | 0 | 1 | - |  |  | French business. Normalises to `fitforme` and joins FitForMe: fail by name |
| 73 | `Indépendant` | 1 | 0 | RNPC | referral | #3 | Corinne Brunet, Directrice Centre RNPC |
| 74 | `Laboratoire YSONUT` | 1 | 0 | Laboratorios YSONUT | operations | #22 | Regional director, France |
| 75 | `Liva Food` | 0 | 1 | - |  |  | Food business, name collision |
| 76 | `MAJU` | 1 | 0 | maju | product | #35 | ludo glav, owner ('Chef d'entreprise, MAJU'), no page: identity check |
| 77 | `MM Sports` | 0 | 1 | - |  |  | Retail, or a name collision |
| 78 | `MM Sports Events` | 0 | 1 | - |  |  | Retail, or a name collision |
| 79 | `MM Sports Nutrition` | 0 | 1 | - |  |  | Retail, or a name collision |
| 80 | `MMSPORTS AB` | 0 | 1 | - |  |  | Retail, or a name collision |
| 81 | `Nederlandse Obesitas Stichting` | 0 | 1 | - |  |  | Messaged 2026-07-21; patient foundation |
| 82 | `Nutrimed` | 1 | 0 | Nutrimed | product | yes | Mihalis Atsalakis, owner, no page: identity check |
| 83 | `Private Body Fit` | 0 | 1 | - |  |  | Single site or freelancer |
| 84 | `RNPC` | 1 | 0 | RNPC | referral | #3 | Unit |
| 85 | `RNPC NICENTRE` | 1 | 0 | RNPC | referral | #3 | Unit |
| 86 | `RSV VITALIS` | 0 | 1 | - |  |  | Single site or freelancer |
| 87 | `S.A.R.L. NATURE FRANCHISE DIETPLUS` | 1 | 0 | Dietplus | referral | #7 | Unit |
| 88 | `SATISFEAT Ernährungsplaner` | 1 | 0 | SATISFEAT | partnership | no | White-label nutrition plans for gyms' member apps |
| 89 | `Self-employed` | 0 | 1 | - |  |  | Single site or freelancer |
| 90 | `TATOI CLUB` | 0 | 1 | - |  |  | Members club; outside ICP |
| 91 | `Ulrich Sports&Consulting GmbH` | 0 | 1 | - |  |  | Single site or freelancer |
| 92 | `VivaFit Sintra` | 1 | 0 | Vivafit | referral | #25 | Unit |
| 93 | `Vivafit Benfica` | 1 | 0 | Vivafit | referral | #25 | Unit |
| 94 | `Vivafit Carregado` | 1 | 0 | Vivafit | referral | #25 | Unit |
| 95 | `Vivafit Porto` | 1 | 0 | Vivafit | referral | #25 | Unit |
| 96 | `dietplus Cugnaux` | 1 | 0 | Dietplus | referral | #7 | Company-named profile: identity check |
| 97 | `dietplus Dunkerque` | 1 | 0 | Dietplus | referral | #7 | Unit |
| 98 | `dietplus Lozanne` | 1 | 0 | Dietplus | referral | #7 | Unit |
| 99 | `dietplus Luneville` | 1 | 0 | Dietplus | referral | #7 | Unit |
| 100 | `dietplus fontainebleau` | 1 | 0 | Dietplus | referral | #7 | Unit |
| 101 | `dietplus laon` | 1 | 0 | Dietplus | referral | #7 | Unit |
| 102 | `pure fitness&health GmbH` | 1 | 0 | fitbox | referral | #9 | Gunnar Mau, owner of fitbox Hamburg Poppenbüttel |
| 103 | `ysonut` | 0 | 1 | - |  |  | marc sarazin `/in/marc-sarazin-7385071b`, duplicate; cell not aliased |
| 104 | nederlandse-obesitas-kliniek: `Nederlandse Obesitas Kliniek` | 0 | 1 | - |  |  | Messaged from `olena` 2026-07-21 (Open question 4) |
| 105 | nutrimed: `nutrimed` | 0 | 1 | - |  |  | JOSEPH MAREK, France: a different 'nutrimed'. Joins Nutrimed: fail by name |
| 106 | qwinn-partners: `Qwinn Business Partners` | 0 | 1 | - |  |  | Consultancy |
| 107 | softpay: `Softpay` | 0 | 1 | - |  |  | Payments |
| 108 | swordhealth: `Sword` | 0 | 1 | - |  |  | US HQ; messaged 2026-07-21 |
| 109 | up-there-everywhere: `UP THERE, EVERYWHERE` | 0 | 1 | - |  |  | Agency |
| 110 | xpstudio: `Scenora` | 0 | 1 | - |  |  | Software tool |
| | **Total (295)** | **158** | **137** | 21 accounts | | 19 yes | |

**Fail by name at validation (13 rows that join an IN account in `extract-people`):** Harpa Arnardóttir, Sóley Valdimarsdóttir, Elías Freyr Guðmundsson, Hildur Gudmundsdottir, Thorkell Viktor Thorsteinsson, Marie-Theres Scharl (Sidekick Health, messaged from `olena` 2026-07-21); Martin Møller Paarse, Kenneth Jensen (Liva Healthcare, same); cynthia grosbois `/in/cynthia-grosbois-7406782bb`, Natacha Alonso `/in/natacha-alonso-a1568015b`, Ilija Bozic `/in/ilija-bozic-7660983ba` (duplicate profiles; the other profile of each stays IN); JOSEPH MAREK (cell `nutrimed`, France: a different Nutrimed); Antoine Poullain (cell `Fit'forme`, normalises to FitForMe's key). The registry check fails the first eight on its own.

**Identity and current-role checks (stay IN unless the check fails):** company-named profiles BODYHIT BORDEAUX MÉRIADECK, DIETPLUS la roche sur foron, dietplus CUGNAUX, "Centre RNPC Merignac" (`/in/thierry-bernabe`): send only if each reads as one person running the unit; "yogimad YOGIMAD" (Virtuagym, pseudonymous); Qnko Qnkov (Ysonut VP, empty profile, Bulgaria, where Ysonut lists no office); Mihalis Atsalakis (cell `Nutrimed`) and ludo glav (cell `MAJU`), both without a page: send only if the profile ties each to nutrimed.gr or maju-nutrition.com; Nanda Zwart (cell `Bindinc.`): send if her Het 1 op 1 Dieet practice is current; Virginie Bourgerie (BODYHIT, headline names BODY MINUTE); Rick Reinhard (fitbox, headline names Körperformen Idstein); Dennis Krebs (fitbox Krefeld through his own company Dsign.); Benjamin Horesnyi (Dietplus, role unclear: treated as a unit owner). A job-change check runs on all 158.

## Use case (1 sentence)

Weight-management and nutrition-coaching programmes in Continental Europe (centre networks, coaches and apps) can add a guided two-photo scan to their client app or a web page, so a client records 80+ body measurements and body composition estimates at home or in the centre between weekly check-ins, and the dietitian, coach or clinician gets a standardized, timestamped record to compare the scans they select; fitness networks and coaching platforms offer the same record inside the member app.

## Why this is plausible (evidence)

1. **Obesity care in Europe is widening, and medication is arriving in programmes' markets.** 59% of adults in the WHO European Region live with overweight or obesity ([WHO Europe, 2022](https://www.who.int/europe/news/item/03-05-2022-new-who-report--europe-can-reverse-its-obesity--epidemic)). Since 15 June 2026 France reimburses two weight-loss medicines for severe obesity, first initiated by specialists, the first EU country to do so ([Euronews, 2026-05-28](https://fr.euronews.com/sante/2026/05/28/france-devient-le-premier-pays-deurope-a-rembourser-les-medicaments-anti-obesite); [service-public.gouv.fr](https://www.service-public.gouv.fr/particuliers/actualites/A18932)). Context only, never copy; the criteria are BMI-based, one more reason the scan is never framed as eligibility.
2. **The accounts on this list already follow clients between visits: in centres, by teleconsultation or in an app.** Naturhouse follows clients weekly in a centre or by teleconsultation (naturhouse.fr); NUTRIADAPT, Het 1 op 1 Dieet, Metabolic Balance, Liva and FitForMe run client apps tied to a coach or specialist (App Store, 2026); Liva bought Denmark's largest dietitian-clinic network in 2025 to combine digital and in-person care ([Techleap](https://finder.techleap.nl/news/feed/liva-healthcare-acquires-di-tisthuset-network)). A phone scan, in an app or a web page, carries body data outside the centre or club, with nothing to ship.
3. **FitXpress fits as an in-app or web capture, with honest limits.** White-label API and web or mobile SDK, two photos, under 45 seconds to structured results, 80+ body measurements, body composition estimates, 3D model, sub-centimetre repeatability for most measurements; 34,000 scans at one anonymised weight-management platform and 112,100 across all customers in 2025 (`proof-points.md`). Limits: no named European weight-management reference; no published comparison of body composition estimates with bioimpedance or any reference method; validation population 38-210 kg; data hosted on AWS in US-West-2 and partly US-East-1; EU special-category and AI Act answers not approved (Open question 9).

## What Olena's earlier campaigns teach this one

- **`2026-07-21-eu-telehealth-weightloss`** (`metrics-final.json`, `responses-summary.md`): 292 invites, 73 accepted (25.0%), 4 replies (5.5% of accepted); 0 of 307 message-1 texts carried a product specific; 39% of sends went to one account. Oviva declined (2026-08-27); the Sidekick reply was a departure notice. Here: the message gate stays, 158 people over 21 accounts, Sidekick through new people, Oviva left alone.
- **`2026-09-14-eu-erakulis-similar`** (`responses-summary.md`, 2026-10-03): 2 replies; the interested one, a non-buyer at Welltech, asked for material to forward to his product team. The referral lane's best case: a short client-free, price-free one-pager ready to forward, and the easy out in every non-buyer message.
- **English only** was decided for `olena` on 2026-09-14 and the July replies all came back in English (Outreach language).

## Target buyer persona

**Who buys:** the owner of the programme, the client app or the client journey at the franchisor or head office (segment A), the product or clinical owner at digital programmes (B), the franchisor or product head at fitness networks and platforms (C), and leadership at Clinique La Prairie (D). Unit owners, centre directors, consultants and club managers are referral paths to head office. SATISFEAT and Virtuagym's country director get a partnership ask. Tiers only order the list; one import file. Apollo additions take the lane their title maps to below.

**P1, owners at core accounts (23), `product` unless marked:** RNPC: Patrick Gaytte, Rémy Legrand; Dietplus: Philippe L. (Philippe Langohr), Natacha Alonso Valckx; NUTRIADAPT: Marta Noskova, Eliška Čížková; Het 1 op 1 Dieet: Henk Willem Olivier, Tom Coenders (`operations`); Ysonut: Marc Sarazin, Yann Malaud; Metabolic Balance: Robert Buschbacher; Sidekick: Mathias Nick Andersen; FitForMe: Simon Hamer; Nutrium: André Santos, Diogo Alves; Fabulous: Sami B.; fitbox: Ingo Huppenbauer; BODYHIT: Frédéric Feret (`operations`); Virtuagym: Paul Braam, Nick van Schijndel; Clinique La Prairie: Simone Gibertoni, Arnaud Marche (`operations`), Massimo Caprino (`clinical`).

**P2, leads (21):** Clinique La Prairie 8 (5 `product`, 3 `operations`), FitForMe 2 and Vivafit 2 (one `operations` each), maju 2 (Julien Jané; ludo glav, identity check), and one each at Virtuagym, Sidekick (`operations`), Liva, Nutrium (`clinical`), Ysonut (`operations`), Keepcool and Nutrimed (`product` unless marked).

**P3, technical and partnership (7):** `technical-integration`: Alison MacNeil and Guðmundur Jón Viggósson (Sidekick), Amine Laadhari (Fabulous), Matthijs Hellendoorn (FitForMe), yogimad YOGIMAD (Virtuagym). `partnership`: Lars Beckmann (SATISFEAT), Mattijs Keess (Virtuagym country director).

**P4, referral (107):** RNPC 27, Dietplus 23, BODYHIT 19, fitbox 11, Naturhouse 6, NUTRIADAPT 4, 1:1 Diet 5, Vivafit 4, FitForMe 2, Virtuagym 2, Clinique La Prairie 2, Ysonut 1, Metabolic Balance 1.

**Lane by title, for Apollo additions:** founders, CEOs, managing directors, presidents, directeurs généraux, Geschäftsführer, product, digital, innovation, growth and strategy leads → `product`; medical, scientific, clinical, dietetic and nutrition leads → `clinical`; COOs, operations, network, franchise-network, programme and customer-operations leads → `operations`; CTOs and engineering or platform leads → `technical-integration`; partnerships and business development at SATISFEAT and Virtuagym → `partnership`; everyone else, unit staff and anyone below lead level → `referral`.

**Not the buyer (FAIL for the cold send):** only the 137 OUT rows in the verdict table. Every function at an IN account has a lane.

**KPIs they care about:** networks, what clients do between weekly visits and the tools every centre gets; digital programmes, what the coach sees at each check-in; fitness, member progress in their own app; Clinique La Prairie, continuity between stays.

**Likely objections and the honest answer:**
- "We weigh clients / our app logs weight / our club has a body-composition device." True; nothing replaces it. The scan adds body measurements and body composition estimates from the client's phone at home; a pilot runs next to what they record now. Never suggest their data is wrong.
- "Accuracy? Higher BMI?" `accuracy-formulations.md` §1.1 or §5, repeatability §1.2; validation ages 16-78, 150-220 cm, 38-210 kg; "Performance outside this scope has not been characterized."
- "GDPR, health data, EU hosting?" The GDPR sentence (`compliance.md` §2), DPA with SCCs, AWS US-West-2 and partly US-East-1, photos deleted after processing or within 30 days, outputs deletable by scan ID; the rest to legal@3dlook.me (Open question 9).
- "BMI for a prescription or reimbursement?" No: FitXpress does not decide eligibility, diagnose or recommend treatment (`compliance.md` §7, §10). "Medical device?" "FitXpress is not a medical device." (replies, or a `clinical` Message 2).
- "Our clients are not app people." The web SDK runs the capture in a browser page. "I only run one centre." Then the call is about who at head office owns it. "Price?" A call question, never in copy.

### Target buyer persona: Sales Navigator pull for step 3

**Pull by title filter inside the approved company list, never by company alone.** The export is the list. This block drives only the Apollo top-up (`apollo-pull.py search` takes each IN account's domain and these titles) on the 19 `apollo_topup=yes` accounts. Broad on purpose: the validator assigns lanes and fails what does not fit.

```titles
Chief Executive Officer
CEO
Founder
Co-Founder
Managing Director
General Manager
President
Directeur Général
Geschäftsführer
Chief Operating Officer
Operations Director
Head of Operations
Network Director
Franchise Director
Head of Franchise
Chief Medical Officer
Medical Director
Scientific Director
Chief Scientific Officer
Head of Nutrition
Head of Dietetics
Lead Dietitian
Clinical Director
Chief Product Officer
Head of Product
Product Director
Product Manager
Product Owner
Chief Digital Officer
Head of Digital
Digital Director
Head of Innovation
Head of Growth
Chief Technology Officer
Head of Engineering
Head of Partnerships
Partnerships Director
Business Development Director
Head of Business Development
Chief Marketing Officer
Head of Customer Experience
Head of Member Experience
Head of Programmes
```

**`cap_per_group: 50`** (default since 2026-09-29, unchanged). RNPC 29 (room for 21), Dietplus 25 (25), BODYHIT 20 (30), Clinique La Prairie 13, fitbox 12. If a top-up takes a network past 50, keep head-office people first.

## Message angle: segments, lanes, company facts and the content asset

Every person gets exactly one lane, spelled as below. Unit owners at one network talk to each other: Rules, "Several people at one company"; facts agree across all of them. Numbers in copy come only from `proof-points.md`. **Writer notes are instructions to the writer and are never copied into a message.**

### Segment angles (writer notes)

- **A. Weight-management and nutrition-coaching networks.** A body record the client takes on the phone at home between visits or teleconsultations (or in the centre), reviewed by the dietitian or coach at the next consultation. For the franchisor: a capability head office can switch on for every centre at once, nothing to ship. Where it runs follows the app list below: a web page the centre sends at the four no-app accounts, the client's app elsewhere. Use case `fx-telehealth-weight-loss`, without its hero line, Smart Scales framing or KPI list.
  - **RNPC** stands on what it runs (RN1, RN2): dietitian consultations in its centres, a doctor's recommendation, the GP kept informed, free follow-up afterwards. The angle: a standardized body record the client takes from a link the centre sends, between consultations or during the follow-up, for the dietitian to compare. Sober, clinical tone; never an app.
- **B. Digital programmes and nutrition technology.** The same capture inside the existing app through the SDK, white-label. For Nutrium: a capability its dietitians' client app could offer. For FitForMe: a record for BariBuddy users after surgery, never a medical claim. For Fabulous: a body-progress record a habit-coaching app could offer, never a weight-loss promise.
- **C. Fitness networks and platforms.** A member's body-progress record from the phone between sessions, inside the club's own app. For Virtuagym and SATISFEAT: something their gym clients could offer members in a white-label app (SATISFEAT is `partnership`). No appearance or weight-loss promises.
- **D. Clinique La Prairie.** A guided body record a guest can take at home between stays, for the clinic's team to compare with what they record on site, kept within the clinic's own experience. Luxury, discreet tone; no longevity, anti-aging or weight outcomes.

### Client app and what each account already records (writer notes; overlap, not displacement)

App Store, 2026-10-07 (store and version in `companies.csv` notes). **No app: the capture is a guided web page the centre or practitioner sends as a link; never write "app", "your app" or "in the app" to these accounts.** Where an app exists, never describe what it records.

- **RNPC:** no client app; consultations in its centres, then free follow-up.
- **Dietplus:** no client app. Weekly follow-up in its centres.
- **Naturhouse France:** no client app. Weekly follow-up in a centre or by teleconsultation.
- **Laboratorios Ysonut:** no app. Programmes run through health professionals.
- **Nutrimed:** a client app for chat with the dietitian, last updated 2023. Offer a web page or their own app; never describe it.
- **NUTRIADAPT:** app with progress and a photo food diary. Never mention either.
- **Het 1 op 1 Dieet:** app that stores progress photos. Never mention photos the client takes today.
- **Metabolic Balance:** Healthy Lifestyle Companion app; it tracks weight, body composition and well-being. Never mention what it tracks.
- **Sidekick Health:** programme apps. Never name them.
- **Liva:** Liva app; it sets goals and tracks progress, steps and diet. Never mention what it tracks.
- **FitForMe:** BariBuddy; it logs weight and body measurements with charts. Never mention what it logs.
- **Nutrium:** client app with the meal plan, a meal log and chat. Never mention the log.
- **maju:** maju app, paired with the portion bowl.
- **The Fabulous:** Fabulous app.
- **SATISFEAT:** a web app inside gyms' member apps.
- **BODYHIT:** BODYHIT app for bookings and subscriptions.
- **fitbox:** fitbox and FITOMAT apps, both from fitbox GmbH. fitbox publishes member-results totals: never quote or mention them.
- **Virtuagym:** white-label member apps; its Hub kiosk runs in-club body scans through body-composition devices. Never mention the kiosk, the devices or their makers; never compare.
- **Keepcool:** Keepcool app with video classes, goals and coaches.
- **Vivafit:** VivaFit App for class booking and payments.
- **Clinique La Prairie:** a Clinique La Prairie app; in-clinic diagnostics. Never compare; never describe the app.

### Lanes

- **`product`** (founders, CEOs, presidents, product, digital, innovation and growth leads). What the client app or a web page can ask a client for: a guided two-photo scan that returns 80+ body measurements, body composition estimates and a 3D model, white-label through API or web and mobile SDKs, nothing to ship. Message 1 = context and the person's own question, no call ask, no link; Message 2 = a 15-minute call offer with the calendar link.
- **`clinical`** (Massimo Caprino, Manuela Abreu, and Apollo medical, scientific and dietetic leads). The team gets a standardized, timestamped body record and compares scans it selects; values are measurements and estimates for the team to review; the repeatability sentence. Message 1 = context and one question, no call ask, no link; Message 2 = the call offer with the calendar link.
- **`operations`** (COOs, network and franchise-network directors, regional directors, operations and guest-experience leads). Nothing to ship, stock or install in centres; the capture follows the same guided sequence on any phone; the speed phrase. Never say or imply that centres or clubs measure differently today. Message 1 = context and one question about how their centres, clubs or guests run, no call ask, no link; Message 2 = the call offer with the calendar link and at most the segment article.
- **`technical-integration`** (CTOs, platform and engineering leads, head of IT). REST API with API-key authentication, web and mobile SDKs; photos deleted after processing or within 30 days; outputs stored and deletable by scan ID. No integration-time figure. Technical tone. Message 1 = context and one technical question, no call ask, no link; Message 2 = the call offer with the calendar link, and the FAQ link.
- **`partnership`** (SATISFEAT, Virtuagym's country director). Message 1: one line on what the scan returns, the company fact, and the question whether a partner capability has any place in what they offer; no call ask, no link. Message 2: the call offer with the calendar link, the easy out a pointer to whoever decides partnerships. No compliance line, no article.
- **`referral`** (P4). Vadim's decision 4: never a bare "who owns X?". Message 1: one line on what the scan returns and why it matters for this company's programme (from its fact and its app line), then one question about the person's own work (question themes); no "who" question, no call ask, no link. Message 2: a short call offer with the calendar link and an easy out that is a different ask: a pointer to the person who owns the topic (client follow-up at programme networks, member experience at fitness networks, the client app only where the account has one), worded fresh for each person: name the target, never a sample sentence (2026-10-07: a sample here went into ~30 messages). The gate checks the product specific and the number here too. Unit owners: the Rules' franchise limits, and never suggest head office knows about the message. Dietitians and coaches: brief, neutral copy (a writer instruction, not a phrase for the message); the scan is never framed as motivating or about body image.

### Company facts the copy may use

| Company | ID | Fact the copy may use | Writer notes |
|---|---|---|---|
| RNPC | RN1 | RNPC runs a dietitian-led nutritional and behavioural programme for people living with overweight or obesity, through a national network of centres in France. | Name it "RNPC"; no app |
| RNPC | RN2 | RNPC works on a doctor's recommendation, keeps the patient's GP informed through the programme, and offers free follow-up afterwards to help people keep their results. | Never mention medication, research cohorts or results figures |
| Dietplus | DP1 | Dietplus coaches rebalanced eating through centres in France, Spain and Belgium: a free first assessment, then personalised follow-up every week. | Never mention its products or centre counts; no app |
| Naturhouse France | NH1 | Naturhouse clients see a dietitian-nutritionist every week, in a centre or by teleconsultation, with a personalised diet plan. | Never mention products or the Spanish parent; no app |
| NUTRIADAPT | NA1 | NUTRIADAPT runs a network of weight-management clinics across the Czech Republic, pairing nutrition counselling with a personalised plan. | Never mention beauty or cellulite services |
| NUTRIADAPT | NA2 | NUTRIADAPT clients use the NUTRIADAPT app between consultations to follow their progress, watch exercise videos and message their specialist. | Never mention the food diary |
| Het 1 op 1 Dieet | OD1 | Het 1 op 1 Dieet pairs each client with a personal consultant for one-to-one coaching through the programme. | Never name the UK brand owner or meal products |
| Het 1 op 1 Dieet | OD2 | Clients use the Het 1 op 1 Dieet app for appointments, recipes and motivation. | Never mention progress photos |
| Laboratorios Ysonut | YS1 | Ysonut develops science-based nutritional programmes that health professionals deliver, with training through Ysonut Academy. | No product or country names; no app |
| Metabolic Balance | MB1 | Metabolic Balance builds a personalised nutrition plan that its trained coaches deliver, and its Healthy Lifestyle Companion app keeps clients in touch with their coach. | Never mention what the app tracks |
| Nutrimed | NM1 | Nutrimed's dietitians support nutrition and weight control from offices in Greece and online. | |
| Sidekick Health | SK1 | Sidekick Health builds digital programmes for people living with chronic conditions, metabolic health included. | Never name its products, pharma partners, deals or funding |
| Liva Healthcare | LV1 | Liva gives each person a personalised lifestyle plan and a human health coach in the Liva app, with video consultations. | |
| Liva Healthcare | LV2 | Liva combines app-based coaching with in-person dietitian clinics in Denmark. | Never name the clinic network or the deal |
| FitForMe | FF1 | FitForMe makes supplements for people after bariatric surgery and people taking weight-loss medication, and works with healthcare professionals. | "weight-loss medication" only, no drug names |
| FitForMe | FF2 | FitForMe's BariBuddy app supports people after weight-loss surgery with recipes, answers from clinicians and daily routines. | Never mention what it logs |
| Nutrium | NU1 | Nutrium gives dietitians software for appointments, meal plans and follow-up, with a mobile app their clients use between appointments. | |
| Nutrium | NU2 | Nutrium Care brings online dietitian appointments to employers' staff. | |
| maju | MJ1 | maju helps people rebalance what they eat with a portion bowl and an app designed with dietitians, who also use it in consultations. | |
| The Fabulous | FB1 | Fabulous builds habit-coaching apps grounded in behavioural science, with human coaching sessions on request. | No user counts |
| SATISFEAT | SF1 | SATISFEAT puts automated nutrition plans inside gyms' own member apps, under each gym's brand. | |
| BODYHIT | BH1 | BODYHIT runs a national network of EMS training clubs in France, and members book their sessions in the BODYHIT app. | No results, satisfaction or beauty claims |
| fitbox | FX1 | fitbox runs EMS personal training in studios across Germany, every session with a trainer and by appointment. | |
| fitbox | FX2 | fitbox members manage bookings and membership in the fitbox app, and fitbox GmbH also owns the FITOMAT smart-gym brand. | FITOMAT only in head-office copy (fitomat.com imprint; both apps from fitbox GmbH) |
| Virtuagym | VG1 | Virtuagym gives gyms, personal trainers and corporate health providers one platform for membership, coaching and a white-label member app. | Never mention the kiosk body scans |
| Keepcool | KC1 | Keepcool members train in clubs across France and use the Keepcool app for video classes, goals and their coaches. | |
| Vivafit | VF1 | Vivafit runs fitness clubs in Portugal, and members book classes in the VivaFit app. | Never name the group (App Store PT "VivaFit App") |
| Clinique La Prairie | CL1 | Clinique La Prairie's Healthy Weight programme is a medically supervised stay that builds a personalised weight-management plan. | No prices, no outcomes |
| Clinique La Prairie | CL2 | Longevity Hubs by Clinique La Prairie give members an urban centre to sustain their longevity journey between stays. | |

### Question themes for one company's people (writer notes)

Each person gets one question nobody else at the company gets, phrased from their title or unit and about their own work. In Message 1 it is never a "who" question; the pointer to head office is only Message 2's easy out.

- **RNPC centres (no app):** how clients are followed between consultations; what the dietitian has at hand at each consultation; how the free follow-up runs after the programme; how new tools reach centres and how teams are trained on them.
- **Dietplus and Naturhouse centres (no app):** what clients do between weekly visits; how the first assessment runs; how teleconsultation follow-up works (Naturhouse); how new centre tools are introduced.
- **NUTRIADAPT, Het 1 op 1 Dieet and Metabolic Balance consultants and clinic owners:** what clients use the app for between sessions; what the consultant looks at in each check-in.
- **BODYHIT, fitbox and Vivafit clubs:** what members see of their progress between sessions; how the club goes through progress with a member; how new services reach clubs.

### Content asset in Message 2 (at most one article link, plus the calendar link)

| Who | Link | Writer notes |
|---|---|---|
| Segments A and B, `product`, `clinical`, `operations` | https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/ | Do not quote figures from the page |
| Segment C, `product` and `operations` | https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/ | Do not quote figures from the page |
| `technical-integration`, every company | https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/ | Never restate it |
| `referral`, `partnership`, Clinique La Prairie | no article; calendar link only | |

All three links returned HTTP 200 on 2026-10-07.

## Outreach language

English only, every country (Vadim, 2026-09-14, for `olena`; the July replies all came back in English, and every gate works on English). Most of this list are French, Czech, Dutch and Portuguese unit owners reading in a second language: short sentences, plain words, no idioms, no wordplay (Open question 5).

## Rules for steps 3-5

- **Sender and format:** Olena, English, `Olena` alone on the last line. Connection request with no note. Message 1 ≤ 600 characters, median about 320; Message 1 carries no link. Message 2 ≤ 550 with https://meetings.hubspot.com/olena-kudriavtseva as plain text in every lane, and at most one article link (asset table). All people go in one import file; tiers only order the list.
- **Lanes are exactly** `product`, `clinical`, `operations`, `technical-integration`, `partnership`, `referral`.
- **Message 1 asks, Message 2 calls** (Vadim's decision 4, corrected 2026-10-07), every lane, referral included. No bare "who at your company owns X?". Message 1: context first (what the scan does and why it matters for this company's programme), then one question; no call ask and no link (this overrides step 5 of `outbound-message1-template.md`, the soft "quick chat?" CTA: Message 1 ends on the question). Message 2: a short call offer with the calendar link; people who are not the buyer get an easy out ("or point me to whoever runs X"). For them the Message 1 question is about their own work, never a "who" question, and the pointer lives only in the Message 2 easy out: never the same ask twice.
- **Apps.** Mention a client or member app only where "Client app and what each account already records" shows one; RNPC, Dietplus, Naturhouse France and Ysonut have none, and their copy offers a web page the centre sends.
- **Several people at one company.** Never mention colleagues, other centres, units, owners or consultants; never claim to have spoken with anyone there; never claim an interaction that did not happen. Name the company in every Message 1. No two people at one company share an opener, a central question, a closing ask, a Message 2 opener or a product sentence.
- **Message 1 makes an observation from the company fact or the person's role,** never about something the company lacks (the template's "what's missing" step does not apply).
- **Never put a prospect's own data next to ours.** No message names a prospect's weigh-ins, weight log, progress photos, device scans, measurements or records and then says what the scan returns.
- **Not verification, not eligibility.** Never offer the scan as weight, height or BMI confirmation, as a check before prescribing or reimbursement, or as anything that decides who can start or continue a programme or treatment. Never cite or paraphrase any regulator, insurer or reimbursement rule.
- **Medication.** Only in FitForMe copy, only as "weight-loss medication", only with FF1. No drug, molecule or pharma names anywhere; never tie the scan to prescribing or dosing.
- **Franchise networks.** Head office is the buyer; units are referral paths. Never pitch a unit to adopt anything; never mention franchise terms, fees, territories, unit counts or head-office plans.
- **Owners, deals, former employers.** Never mention funding, investors, valuation, acquisitions, group owners, revenue, prices, headcount or centre counts. A former employer may be named unless it is another account in this campaign or Oviva.
- **Fitness, EMS and Clinique La Prairie.** No appearance, shape, weight-loss, cellulite, longevity or anti-aging promises, no before-and-after, no device or treatment names, no prices. Writer note, not copy: the 3D model is shown only where the club or clinic chooses to show it, so never lead with it as the value (2026-10-07: this sentence went into 24 messages).
- **Compliance line.** At most one, only in Message 2, only in `product`, `clinical`, `operations` and `technical-integration` messages at segments A, B and D, verbatim from `compliance.md` §9: "In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes SCCs." "FitXpress is not a medical device." only in a `clinical` Message 2. Never "HIPAA compliant", "SOC 2 certified" or any certification claim.
- **No 3DLOOK client is named.** Anonymised proof allowed: "one weight-management platform ran 34,000 scans in 2025" (no client name, no geography: never "Nordic" or "Swedish"); "112,100 scans in 2025 across all 3DLOOK customers" (3DLOOK-wide scale, its own sentence); "3DLOOK has worked with 100+ clients" (all-time, both products; never "100+ clients use FitXpress" or "today").
- **Numbers and accuracy, only from `proof-points.md` and in its wording:** two photos (front and side); "under 45 seconds from the photos to structured results"; 80+ body measurements; body composition estimates (body fat %, lean mass, fat mass), BMI and BMR calculated; "96-97% accuracy against expert manual measurement" (body measurements only, never in a sentence with body composition, never opening Message 2) or `accuracy-formulations.md` §1.1 / §5; the §1.2 repeatability sentence; 38 to 210 kg (`clinical` only); the 34,000 and 112,100 lines. No integration-time, market, medication, reimbursement or prospect figures.
- **No outcome promises.** Never promise or imply more weight loss, retention, adherence, engagement, results or ROI. Describe what the scan returns, where it runs and how much it is used.
- **What the scan does not do.** It does not diagnose, decide eligibility, recommend treatment or interpret results. Say "the team compares scans it selects", never "tracks each client". No visceral fat output; never for anyone under 16 or in pregnancy. Person-first: "people living with obesity".
- **Word traps.** Never "objective" about our data (standardized, timestamped, structured, repeatable); never "comprehensive", "seamless", "leverage", "game-changer"; no em or en dash; no "plus" as a connector; no "so" introducing a benefit; no corrective "X, not Y".
- **Writer notes and card instructions are not copy.** "generic figure", "never a promise", "not a promise", "context only" and "writer note" are banned terms, so a leak fails the gate.
- **No pricing and no trial terms** anywhere. A price or trial question goes to the call.
- **Message 1 gate.** Every message 1 carries at least one product specific from `proof-points.md` and one line that could only have been written to that company; each pair of messages cites at least one number. The `referral` lane is not exempt here (`referral_call: yes`).

## Anti-cases (where it does NOT work)

- **Out, by name:** the 137 OUT rows of the verdict table, and the 13 of them that join an IN account (fail by name). AMRA Medical is held for Vadim (Open question 11). Match on the company LinkedIn page and website, never on the name alone.
- **Structural anti-cases:**
  - **Displacement:** an account that runs a phone-camera body scan or has signed a scanning vendor is held for Vadim. None found on 2026-10-07; dietplus.fr was unreadable (403).
  - **Partial overlap is not displacement:** weight logs, progress photos, in-club device scans and body data in client apps stay IN, and copy never sets them next to the scan.
  - **Product-only nutrition businesses** (GymBeam, BioTechUSA, HSNG, Body & Fit, MM Sports): no programme that follows a person. FitForMe is IN for its patient app and clinician work.
  - **Eligibility, prescribing and reimbursement checks:** never the use here.
  - **Children, pregnancy, and people outside the 16-78 / 38-210 kg validation scope:** never a scan context.
  - **Franchise units on their own:** a unit cannot add an SDK to the franchisor's app; units are referral paths only.
  - **People and entities outside Continental Europe:** US-HQ Sword; any Apollo addition located in the UK or outside Continental Europe (Open question 10).
  - **Accounts already worked from `olena`:** messaged people stay OUT; Oviva OUT whole; NOK and The Body Clinic have nobody new (Open question 4).
- **Stop conditions before send:** an IN account announces a merger, closure or a body-scanning partner (pause, Vadim decides); a profile shows the person has left (drop; replace only through the Apollo top-up).

## Vadim's standing decisions (built in, not open questions)

1. **No headcount floor** (2026-09-29).
2. **`cap_per_group: 50`, no waves** (2026-09-29): one closely.io import file.
3. **A lane for every function** (2026-09-29).
4. **FAIL only for the wrong company, people who left, identity collisions and duplicates;** company-named profiles are held for an identity check.
5. **Former employers may be named** (2026-09-29), within the Rules' limit.
6. **Live 3DLOOK pages may be linked as they are** (2026-09-29).
7. **No 3DLOOK client is named;** 34,000 scans without client or geography; 112,100 as 3DLOOK-wide scale; "3DLOOK has worked with 100+ clients", all-time (2026-09-29, 09-30, wording 10-07).
8. **A list Vadim brings has no company-researcher step.**
9. **Franchise networks:** the franchisor is the buyer; units are referral paths under its canonical name.
10. **Re-entry through new people only;** messaged people stay excluded; Vadim clears the `company already worked` flag (2026-09-28).
11. **English only for `olena`** (2026-09-14).

## Vadim's decisions 2026-10-07 (scope and copy)

1. Sender: `olena`. Market: Continental Europe, UK excluded.
2. Use as many contacts from the list as possible. Every non-junk person at an IN account goes in, any function or seniority; OUT only for companies outside the ICP, junk rows (freelancers with no company, name collisions, unrelated businesses), people outside Continental Europe or at UK/US-only entities, existing customers, and registry conflicts.
3. Apollo top-up where needed: an IN account whose decision-makers or relevant teams (product, digital, clinical/medical, operations, partnerships, leadership) are missing from the export gets `apollo_topup=yes`; the coordinator runs `apollo-pull.py search` then `enrich`. Accounts whose relevant people are already in the export get `apollo_topup=no`.
4. Copy: no bare "who at your company owns X?" messages. Message 1 = a bit of context (what the scan does and why it matters for THIS company's programme), then a question. No call ask and no link in Message 1. Message 2 = the call: a short call offer with Olena's calendar link https://meetings.hubspot.com/olena-kudriavtseva, in every lane, referral included (for people who are not the buyer, with an easy out: "or point me to whoever runs X"). (Vadim, 2026-10-07: «в первом сообщении вопрос а во втором звонок».)

## Vadim's decisions 2026-10-07 (approval)

Vadim approved the hypothesis on 2026-10-07 («апрув»), taking the default on every open question the coordinator put to him:

1. GymBeam, BioTechUSA, HSNG, MM Sports and Body & Fit stay OUT (outside the ICP); GymBeam's B2B director is not added as a partnership ask (Open question 1).
2. Oviva stays OUT whole, the 12 new people included, until at least February 2027 (Open question 2).
3. Sidekick Health and Liva Healthcare re-entry: clear the «company already worked from olena» flag and send to new people only (Open question 3).
4. Nederlandse Obesitas Kliniek and the Dutch The Body Clinic stay OUT (Open question 4).
5. Language: English (Open question 5).
6. Fitness networks and platforms stay IN at medium fit (Open question 6).
7. TATOI Club and AMRA Medical stay OUT (Open questions 7 and 11).
8. Identity holds: current-role check, send if it passes (Open question 8).
9. Nothing about special-category data, EU hosting or the AI Act in copy; such replies go to legal@3dlook.me (Open question 9).
10. Apollo additions located outside Continental Europe are OUT (Open question 10).
11. Apollo top-up stays title-filtered: 80 people enriched on 2026-10-07 for 82 credits from the ```titles block (Clinique La Prairie and SATISFEAT not topped up, 7 people Olena already messaged at Sidekick and Liva removed before enrichment); no all-functions pull (≈770 more people up to cap 50 were offered and declined by default).

## Vadim's decisions 2026-10-07 (validation)

Vadim approved the validated list on 2026-10-07 («апрув»), taking the coordinator's recommendation on every question:

1. **WEAK, 5 promoted after a current-role check before import:** Nanda Zwart (Het 1 op 1 Dieet, `referral`), Mihalis Atsalakis (Nutrimed, `product`), ludo glav (maju, `product`), Qnko Qnkov (Laboratorios YSONUT, `referral`), Rick Reinhard (fitbox, `referral`). **WEAK, 4 stay out:** yogimad YOGIMAD, BODYHIT BORDEAUX MÉRIADECK, dietplus CUGNAUX, Julie Coudry.
2. **Exception to approval §10 (location), for named head-office people of IN accounts:** the account's market decides, not where the person lives. Pool A: Ruben Visser (Virtuagym, `operations`) and Taylor Ling (The Fabulous, `product`) IN; Arnaud Souchon (Keepcool, Mauritius) and Zeki Kilic (FitForMe, Istanbul) stay out (may be local entities). Pool B, Liva Healthcare's UK team, IN: Jessica Bartlett `product`, Ellie Heath `clinical`, Hannah Pearman `operations`, Tom Fuller `product`. Pool C, Sidekick Health's US commercial team, IN as `partnership` (the lane is extended to Sidekick for these three): Kevin Johnston, Todd Peavey, Mischa Cohn. Pool D (Metabolic Balance licensees in Australia) stays out. Every other Apollo person outside Continental Europe stays OUT.
3. **Iceland:** olena's market is Europe without the UK; the three Sidekick people in Iceland stay IN.

## Vadim's decisions 2026-10-07 (messages)

Vadim approved the messages on 2026-10-07 («внеси пропоновані зміни потім апрув») after three opus QC rounds (10, 12, 13/20) and a fourth fix round checked by script. Defaults taken in the fix rounds, now standing for this campaign:

1. **At most one compliance sentence per Message 2.** `clinical`: only "FitXpress is not a medical device." `product`, `operations`, `technical-integration`: only the GDPR line. `referral`, `partnership`: none. A data-retention or deletion sentence counts as the compliance sentence and never sits in Message 1.
2. **"100+"** only as "3DLOOK has worked with 100+ clients" (now in `proof-points.md` and failed by `check-messages`).
3. **Speed** only inside a sentence whose subject is the scan or its output: "It returns 80+ body measurements, under 45 seconds from the photos to structured results."
4. **Card samples are not copy:** the referral easy out and the 3D-model display rule above were rewritten as targets on 2026-10-07 (the samples had gone into ~30 and 24 messages).
5. **Identity holds before import** follow approval §8 ("current-role check, send if it passes"): a person whose export row shows a current employer outside the account, or a different person, is held from the import file.

## Validation criteria (Step 2 will check)

No company research: step 2 is `companies.csv`; step 4 validates people against the persona.

- **Companies.** 21 rows, aliases as above, Continental European `hq_country`, `icp_fit` high (9) or medium (12), `apollo_topup` and its reason in `notes`. `record` registers the 21 canonical names, never an OUT company (AMRA is not in the file).
- **Registry.** `check --profile olena` should flag the 8 Sidekick and Liva people already messaged (FAIL) and the 5 new Sidekick and Liva people as `company already worked from olena` (cleared on Open question 3), and nothing else.
- **Displacement re-check** before import; retry dietplus.fr.
- **People.** 158 PASS: P1 23, P2 21, P3 7, P4 107; lanes as in "Read this first". FAIL: the 13 fail-by-name rows. Apollo additions: same lane-by-title rules, the geography rule, the 50 cap.
- **Message gate.** The Rules' Message 1 gate and "Message 1 asks, Message 2 calls", every lane; zero client names, pricing, `banned_terms`, verification framing, prospect data next to ours, outcome promises, app mentions at no-app accounts, or compliance lines outside the allowed lanes. A failure, not a note: `2026-07-21` wrote 307 first messages with no product specific and drew 4 replies from 73 accepted of 292 invites (`metrics-final.json`).

## Success metrics for this campaign

Closely event counters, as in `metrics-final.json`; read per segment.

| Metric | Target | Floor | Basis |
|---|---|---|---|
| Invites sent | 158 + Apollo | 140 | after identity checks |
| Connection acceptance | 25% | 15% | `olena` July 25.0% |
| Replies per accepted person | 10% | 5% | July 5.5%; referral-heavy list |
| Positive replies from P1-P3 or Apollo owners | 3 | 1 | 51 P1-P3 |
| Referral replies naming an owner or taking the call | 6 | 2 | 107 referral |
| Accounts with a reply | 6 of 21 | 3 | |
| Discovery calls | 3, different accounts | 1 in 8 weeks | |

**Falsified if** three or more P1 or P2 replies say a home body record has no place next to the weekly follow-up they run, or that US hosting rules it out. **Inconclusive** if fewer than 30 people accept.

## Risks

1. **Referral weight and language:** 107 of 158 are referral, mostly unit owners at four networks, written to in English; buyer reach depends on the Apollo top-up.
2. **Health-data questions:** special-category data and EU hosting will come up; FitXpress is hosted on AWS in the US.
3. **Weaker fit at fitness accounts** (read separately) and **no named European reference**.
4. **High BMI:** validation tops out at 210 kg.
5. **Re-entry:** a second touch at Sidekick and Liva can read as pressure.

## Open questions for Vadim

1. **GymBeam (29) and the other nutrition retailers** (BioTechUSA 19, HSNG 6, MM Sports 3, Body & Fit 3) are OUT as outside the ICP: e-commerce with no programme that follows a person. The two apps checked are shops (GymBeam; BioTechUSA adds a loyalty programme and calorie logging). Default: OUT. Bring GymBeam in anyway, or only its Director of B2B, Strategic Partnerships (Gergő Demjén) as a partnership ask?
2. **Oviva (25) is OUT whole:** 13 of them messaged on 2026-07-21 (30 Oviva people in all), decline on 2026-08-27; the other 12 are mostly engineering directors. Default: OUT until at least February 2027. Release the 12?
3. **Sidekick Health (4) and Liva Healthcare (1) re-entry.** New people only; `check` will flag them `company already worked from olena`. Default: clear the flags and send.
4. **Nederlandse Obesitas Kliniek and The Body Clinic (Netherlands).** Every export person was messaged in July. Default: OUT. Re-enter through new Apollo people only (the Medicspot precedent)?
5. **Language.** Default: English (2026-09-14). French copy for the French networks would need a gate and card change.
6. **Fitness networks and platforms (47 people: BODYHIT 20, fitbox 12, Virtuagym 7, Vivafit 6, Keepcool 1, SATISFEAT 1)** kept IN under §8 at medium fit. Default: keep.
7. **TATOI Club (6)** is OUT as a private members club. Release?
8. **Identity holds** (list under the verdict table). Default: current-role check, send if it passes.
9. **EU compliance answers** beyond the GDPR sentence (special-category health data, EU hosting, AI Act), open since 2026-09-14. Default: nothing in copy; replies go to legal@3dlook.me.
10. **Apollo additions outside Continental Europe** (for example FitForMe or Liva staff in the UK). Default: OUT (`katerina`'s market or no profile's).
11. **AMRA Medical (2: CTO and CSO), MRI fat and muscle analytics.** No `icp-detail.md` segment fits (§7 is CROs, sponsors, research networks and DCT platforms, not imaging vendors), and no partnership-only scope decision covers it here (the 2026-10-06 UK one named Perspectum). Default: OUT, not in `companies.csv`. Take it as partnership only? Then re-add the row (amramedical.com, Sweden, medium, `apollo_topup=yes`) and both people as `partnership`, P3.

## Sources

- Export `sales-nav-raw/export-1.csv` (stdlib `csv`) and `export-summary.md`; alias joins checked with `scripts/outbound-pipeline.py` (`company_keys`, `shortlist_keys`, `geo_profile`, `fit_of`); registry `outbound-registry.py check --profile olena` (dry run) and `status`.
- Market: [WHO Europe 2022](https://www.who.int/europe/news/item/03-05-2022-new-who-report--europe-can-reverse-its-obesity--epidemic) · [Euronews 2026-05-28](https://fr.euronews.com/sante/2026/05/28/france-devient-le-premier-pays-deurope-a-rembourser-les-medicaments-anti-obesite) · [service-public.gouv.fr](https://www.service-public.gouv.fr/particuliers/actualites/A18932)
- Accounts (read 2026-10-07): each row's site and `source_url` in `companies.csv`, and franchise.dietplus.fr · [toute-la-franchise (Dietplus)](https://www.toute-la-franchise.com/franchise/dietplus/news) · [Philippe Langohr, president](https://www.toute-la-franchise.com/news-lancer-franchise-dietplus-rencontre-president-lyon) · [zanadio listing (Sidekick Health Germany GmbH)](https://apps.apple.com/is/app/zanadio/id1499824614) · [Liva and Diætisthuset](https://finder.techleap.nl/news/feed/liva-healthcare-acquires-di-tisthuset-network) · [FITOMAT imprint](https://fitomat.com/de/impressum) · [Virtuagym Hub](https://business.virtuagym.com/virtuagym-hub/) · [Keepcool-Neoness](https://ac-franchise.com/article/keepcool-neoness-veut-renforcer-sa-presence-sur-le-marche-du-fitness-en-2025) · balancecompany.pt (vivafit.pt redirect) · AMRA LinkedIn About (site 403; Open question 11).
- App Store searches and listings (iTunes search API, 2026-10-07; store and version in `companies.csv` notes): no app found for RNPC, Dietplus, Naturhouse (FR) or Ysonut (ES); [GymBeam](https://apps.apple.com/sk/app/gymbeam/id6738916844) (shop), [BioTechUSA](https://apps.apple.com/hu/app/biotechusa-fitness-sport/id1582826850) (shop, loyalty, calorie log), [VivaFit App](https://apps.apple.com/pt/app/vivafit-app/id6496847672) (class booking).
- Internal: the UK 2026-10-06, EU 2026-07-21 and 2026-09-14, and UK 2026-09-27 campaign files named above; `icp-detail.md`, the use-case file, `proof-points.md`, `accuracy-formulations.md`, `compliance.md`, `competitors.md`; `scripts/outbound_pack.py`, `scripts/apollo-pull.py`.
