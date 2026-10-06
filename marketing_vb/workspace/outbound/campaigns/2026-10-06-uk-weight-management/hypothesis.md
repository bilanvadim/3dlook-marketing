---
product: fitxpress
profile: katerina
market: UK
created: 2026-10-06
status: approved
approved: 2026-10-06
use_case: fx-telehealth-weight-loss
cap_per_group: 75
banned_terms: [Yazen, UK Meds, Healthyr, Safariland, Burlington, Jim's Formal Wear, Generation Tux, Tailoor, Redthread, Prism, Bodygram, Size Stream, InBody, Tanita, Withings, Evolt, Styku, Fit3D, Seca, Ozempic, Wegovy, Mounjaro, Zepbound, Saxenda, Rybelsus, Foundayo, semaglutide, tirzepatide, liraglutide, orforglipron, Novo Nordisk, Lilly, Voy, Menwell, Doctor Care Anywhere, DCA, Outcome Diagnostics, Hallo, Aurelius, Expert Health, Leeds Beckett, Affidea, Protein Supplies, PronoKal Group, HIPAA, SOC 2, FDA, MHRA, GPhC, CQC, DTAC, DSPT, UKCA, CE mark, compliant, certified, certification, accredited, NHS-approved, NHS approved, clinically validated, clinically proven, verify, verified, verification, eligibility, eligible, Smart Scales, mismatch, fraud, self-reported, guesswork, unreliable, inaccurate, error-prone, tape measure, beyond the scale, beyond weight, non-scale, scale weight, weight alone, weight only, just weight, obese, diabetics, before and after, before-and-after, bikini, summer body, burn fat, fat loss, fat reduction, 3D-Lipo, cryolipolysis, guarantee, guaranteed, ROI, reversal, cure, DEXA, DXA, BIA, bioimpedance, MRI, visceral, pregnancy, pregnant, antenatal, postnatal, funding, investors, investor, valuation, acquisition, acquired, merger, royalties, franchise fee, generic figure, never a promise, not a promise, context only, writer note, Circling back, Following up, Saw your post]
---

# Outbound Hypothesis: 2026-10-06, UK weight-management programmes (fixed list, Katerina)

- **Campaign:** `2026-10-06-uk-weight-management`
- **Owner and sender:** Katerina Galich, CEO, profile `katerina`, market UK. `OWNER["katerina"] = "Katerina"`: every message ends with `Katerina` alone on the last line. Message 2 calendar link: https://meetings.hubspot.com/katerina-galich.
- **Company list: fixed, not researched.** Vadim's closely.io enrichment of a Sales Navigator list, `sales-nav-raw/export-1.csv`: 166 people, 64 groups (company LinkedIn page, or the typed company name where a row has no page). Read through `export-summary.md` and short stdlib `csv` scripts; the file was not read whole. There is no company-researcher step: step 2 is `companies.csv`, written in this run from the verdict table.
- **ICP:** `icp-detail.md` §1 (Telehealth & GLP-1 / Weight Loss Programs) is the core; its UK examples sit next to this list's accounts. Metabolic and Tier 3 clinicians fall under §5 (bariatric / metabolic clinics). Partnership-only accounts match no segment and go in on Vadim's scope decision.
- **Use-case file:** `use_case: fx-telehealth-weight-loss` (in the card). Its hero line ("Verify body progress ... prove program ROI"), its Smart Scales mismatch framing and its KPI list are not usable here (Rules).
- **Registry, checked 2026-10-06:** no person in the export is in any profile's registry and no IN account is registered to another profile, with two exceptions found manually. (1) The five Medicspot people were in Katerina's `2026-09-01-uk-erakulis-similar/closelyhq-import.csv`; that campaign was sent (Nutracheck replied on 2026-10-01) but was never folded into `katerina-registry.json`, which lists only `2026-07-31` and `2026-09-27`. (2) The Stourbridge "The Body Clinic" normalises to `body-clinic`, which Olena's 2026-07-21 campaign registered for a different, Dutch company (bodyclinic.nl).

> **Read this first.**
> 1. **126 people IN, 40 OUT, 166 in all.** 18 accounts are IN: 17 have people in the export, and Medicspot is IN for an Apollo top-up only. OUT: 24 people outside the UK or at non-UK companies (PronoKal Group staff in Portugal, Italy, Belgium and the Netherlands 4, the Weight Doctors family 8, Elysee Life 4, Reset Health staff in Italy and Hungary 3, the Irish LighterLife master franchise 2, Clínica Terrace, INEM, SDM_Kalibra); 9 junk rows (Habitual Wealth, Habitual Café and Bakehouse, Habitual Ventures, RESET Health Bar, Reset Health & Wellbeing Services, Hara Marketing, MaxyLogic, a self-employed counsellor, a "Director at Counterweight" who is not on Counterweight Limited's register); 1 HealthHero row (Olena's registry); the 5 Medicspot people already contacted from `katerina`; 1 duplicate profile (Maxine Phillips-Smith). 24 + 9 + 1 + 5 + 1 = 40. Philip Bazire is IN: PronoKal UK is Protein Supplies Ltd t/a PronoKal, a company registered in England and Wales (Companies House 07168388), and he has been one of its directors since 2018.
> 2. **15 OUT rows still join an IN account by name** in `extract-people` and must be failed by name at validation (list under the verdict table). The other 25 OUT rows match no IN account.
> 3. **Two core accounts changed hands in 2026.** Voy bought MoreLife (announced June 2026) and Voy has been manually excluded for `katerina` since 2026-09-12. Doctor Care Anywhere bought Medicspot's weight-loss business (8 May 2026). `icp-detail.md` excludes recently acquired companies by default; Vadim's scope keeps both in, with Open questions 1 and 2.
> 4. **Coordinator, before step 3:** run `scripts/outbound-registry.py record --campaign 2026-09-01-uk-erakulis-similar` so the 26 people of that send (Medicspot five included) are excluded by the registry, not only by this file. Expect `check` to flag Kate Sykes ("company covered by olena"): a name collision, cleared by default (Open question 4).
> 5. **Apollo top-up, Vadim's rule as he wrote it: every IN account whose staff are not all in the list gets the missing people, junk aside.** The coordinator's free all-functions search on 2026-10-06 (the first draft's 17 accounts, 658 candidates, 75 already in the export) found new non-junk people at Reset Health 31, MoreLife 29, LighterLife 32, Counterweight 20, Habitual 10 and Medicspot 6. `apollo_topup: yes` on those six and on PronoKal UK, which that search did not cover (7 accounts). The other accounts are complete or returned no non-junk people (Vadim's decisions 2026-10-06, item 3). `apollo-pull.py search` queries every `companies.csv` row that has a website; search is free, so drop the `apollo_topup=no` accounts from `apollo-candidates.csv` before `enrich` (the flag is in each row's `notes`). Medicspot staff may now list Doctor Care Anywhere as employer and fall to the previous-employer filter.
> 6. **cap_per_group 50, unchanged.** Export people: LighterLife 43, MoreLife 36, Reset Health 26. With every non-junk Apollo addition they would be 75, 65 and 57, all over the cap; the room under 50 is 7, 14 and 24. Open question 5: raise the cap for these three, or fill each to 50 by seniority.
> 7. **Overlap at eight accounts, displacement at none.** No phone-camera body scan was found at any IN account. Partial overlap is listed under "Message angle"; the closest is PronoKal UK, which gives new clients body composition scales. Copy never lists a prospect's data and then adds ours. lighterlife.com and pronokal.co.uk were read on 2026-10-06 (lighterlife.com with a browser user agent, after a first 403). Not readable: counterweight.org (429), thebodyclinic.uk.com (does not resolve); their app listings or third-party pages were used instead.
> 8. **Lanes:** `referral` 76, `product` 13, `operations` 12, `clinical` 12, `partnership` 7, `technical-integration` 6. Tiers: P1 15, P2 22, P3 13, P4 76.

---

## Vertical

UK weight-management programmes that deliver care remotely or between sessions: NHS-commissioned behaviour-change and diet-replacement providers, private GLP-1 services and online prescribers, and a counsellor-led meal-replacement network, together with the clinicians and practitioners around them.

## Sub-segment

The 18 IN accounts, by segment:

- **A. NHS-commissioned and digital programme providers (app-based):** Reset Health (Roczen app; specialist obesity and type 2 diabetes care; GLP-1 wraparound care for an online pharmacy), MoreLife (adult Tier 3 and community programmes, children's services; patient app for referred adults), Counterweight (NHS Type 2 Diabetes Path to Remission, Counterweight-Plus in Scotland; own app).
- **B. Private GLP-1 services and online prescribers:** Habitual (medication plan and soups-and-shakes plan, own app), LloydsPharmacy Online Doctor (weight-loss injections and tablets with Nutrition Coaching), Medicspot (weekly online coach check-ins; Apollo people only), PronoKal UK (UK licensee of a medical weight-loss method, Protein Supplies Ltd in Quorn, Leicestershire: each client has a dedicated doctor and nutrition specialist, consultations by Zoom or telephone).
- **C. Counsellor-led meal-replacement network:** LighterLife (franchisor in Harlow; 41 of its 43 people are unit counsellors, now called Mentors on lighterlife.com, and head-office staff). Each client has a personal Mentor who hosts a small weekly group, mostly online; clients have a web account on lighterlife.com; head office also offers weight-loss medication by consultation. LighterLife has no client app on the UK App Store or Google Play (searched 2026-10-06).
- **D. Clinicians at NHS and private services:** Essex Endocrine Clinic (Tier 3 obesity lead clinician), Homerton Healthcare NHS FT (specialist weight management and bariatric surgery service), North West Anglia NHS FT, Lanarkshire Medical Group.
- **E. Partnership only:** Perspectum (obesity imaging and body-composition research), Exchange Health (behaviour-change training for practitioners), Saira Nutrition (12-week small-group programme), Archvale (GP-practice succession and partnership services), The Body Clinic Leominster (holistic health centre).
- **F. Aesthetic clinic with weight-loss programmes:** The Body Clinic Stourbridge.

**Size:** no headcount floor (Vadim, 2026-09-29). Revenue is not disclosed by most accounts and is not a FAIL reason on this list.

## Company types in scope: verdict table (one row per export group)

Step 2 is `companies.csv` (written in this run, 18 rows). Matching in `extract-people` is on name keys, so the name collisions below are failed by name, never matched.

**Aliases written in `companies.csv` (`Canonical (alias / alias)`; the group is the part outside the parentheses):**
- `LighterLife (LIGHTERLIFE / Lighterlife / lighterlife / LighterLife UK Limited / LighterLife Dundee / LighterLife Edinburgh / LighterLife Hinckley / LighterLife - Blackpool&Preston / Mind & Body Centre Ltd & LighterLife - Cornwall / LighterLife Counsellor / Lighterlife Counsellor / LighterLife-Maida Vale / LighterLife Hampstead / Lighterlife, Beverley, East Yorkshire / C Graves Weight Management Consultancy Ltd / Lighterlife Wycombe / Lighterlife solihull / LighterLife Mexborough / lighterlife taunton / Lighterlife - Chesterfield / LighterLife Billericay / LighterLife - Hereford / LighterLife - Telford / LighterLife - Brentwood & Ongar / LighterLife Mansfield / LighterLife Aberdeen & Shire with Sandra)`. Never aliased: `Letting Go Ltd - LighterLife Master Franchise Republic of Ireland`.
- `MoreLife (MoreLife UK Ltd)`: the export cell is `MoreLife (UK) Ltd.`; nested parentheses would break the alias parser, and the cell matches through the `morelife` and `morelife-uk` keys.
- `PronoKal UK (PronoKal Group)`: both export cells, `PronoKal Group` and `Pronokal`, reduce to the `pronokal` key (the pipeline drops "Group" as a legal suffix), so all five PronoKal rows join and the four outside the UK are failed by name. `record` registers `PronoKal UK`, not the Barcelona group.
- `Medicspot (MedicSpot)`, `Perspectum (Perspectum Ltd)`, `LloydsPharmacy (LloydsPharmacy Online Doctor)`, `The Body Clinic Leominster (The Body Clinic, Leominster)`, `The Body Clinic Stourbridge (The Body Clinic)`.
- Checked with the pipeline's own `shortlist_keys` / `company_keys` on the export: 141 rows join an IN account (126 IN and the 15 fail-by-name rows below), 25 join nothing, no key collides between two IN accounts.

| # | Export group (rows) | IN | OUT | Canonical account | Lanes | apollo_topup | Reason |
|---|---|---|---|---|---|---|---|
| 1 | morelife-uk: `MoreLife (UK) Ltd.` (36) | 36 | 0 | MoreLife | product 2, operations 6, clinical 3, referral 25 | **yes**: 29 new non-junk people in the coordinator's 2026-10-06 search; 65 with them, over the cap (Open question 5) | NHS-commissioned weight-management provider, Leeds. Bought by Voy, June 2026 (Open question 1) |
| 2 | reset-health-clinic: `Reset Health` (29) | 26 | 3 | Reset Health | product 6, clinical 7, operations 4, technical-integration 5, referral 4 | **yes**: 31 new non-junk people in the coordinator's search (32 of its 61 LinkedIn staff are not in the export); 57 with them, over the cap (Open question 5) | Obesity and type 2 diabetes care through the Roczen app. OUT: Luca Visini, Davide Morelli (Italy), Benedek Szulyovszky (Hungary), outside the UK (Open question 3) |
| 3 | lighterlife: `LighterLife` (11), `Lighterlife`, `lighterlife`, `LIGHTERLIFE`, `LighterLife Dundee`, `LighterLife Edinburgh`, `Letting Go Ltd - LighterLife Master Franchise Republic of Ireland` (1 each) | 15 | 2 | LighterLife | product 2, referral 13 | **yes**: 32 new non-junk people in the coordinator's search; 75 with them, over the cap (Open question 5) | Franchisor, Harlow. OUT: Katrina Timmis and Richard Tansley, Republic of Ireland master franchise |
| 4 | medicspot: `Medicspot` (4), `MedicSpot` (1) | 0 | 5 | Medicspot | none in the export | **yes**: 6 new non-junk people in the coordinator's search (new people only) | All five were in Katerina's 2026-09-01 import, which was sent. Weight-loss business bought by Doctor Care Anywhere, May 2026 (Open question 2) |
| 5 | counterweight: `Counterweight` (5) | 5 | 0 | Counterweight | product 2, partnership 1, referral 2 | **yes**: 20 new non-junk people in the coordinator's search | NHS Type 2 Diabetes Path to Remission and Counterweight-Plus provider with its own app |
| 6 | pronokal: `PronoKal Group` (3), `Pronokal` (2) | 1 | 4 | PronoKal UK | clinical 1 | **yes**: not in the coordinator's search; pronokal.co.uk, UK staff only | Philip Bazire IN: Medical Director of PronoKal UK, which is Protein Supplies Ltd t/a PronoKal, registered in England and Wales (Companies House 07168388, director since 2018), "an independent British business" and a licensed affiliate of the Barcelona group (pronokal.co.uk). OUT, outside the UK (Olena's geo): Joana Rosado (Portugal), Laura Milani (Italy), charlotte van vracem (Belgium), Elien Laseure (Netherlands) |
| 7 | NOPAGE `LighterLife` (4) | 4 | 0 | LighterLife | referral | see #3 | Unit owners |
| 8 | weight-doctors-worldwide: `Weight Doctors` (3) | 0 | 3 | none | | | Germany and Netherlands; Weight Doctors Nederland is in Olena's registry |
| 9 | elysee-life: `Elysee Life`, `Elysee Life - Medical Weight Loss`, `A-Brand` (1 each) | 0 | 3 | none | | | Amsterdam, all people in the Netherlands |
| 10 | tryhabitual: `Habitual` (3) | 3 | 0 | Habitual | operations 2, technical-integration 1 | **yes**: 10 new non-junk people in the coordinator's search | GLP-1 medication plan and soups-and-shakes plan, own app |
| 11 | NOPAGE `Lighterlife` (2) | 2 | 0 | LighterLife | referral | | Unit owners |
| 12 | NOPAGE `LighterLife Counsellor` (2) | 1 | 1 | LighterLife | referral | | Bridget Egglesfield IN. Maxine Phillips-Smith (`/in/maxine-phillips-smith-b172a019`) OUT, duplicate of #27 |
| 13 | NOPAGE `LighterLife Hinckley` (1) | 1 | 0 | LighterLife | referral | | Counsellor |
| 14 | NOPAGE `LighterLife - Blackpool&Preston` (1) | 1 | 0 | LighterLife | referral | | Counsellor |
| 15 | NOPAGE `Clínica Terrace Dra Mara Marques` (1) | 0 | 1 | none | | | Portugal |
| 16 | NOPAGE `Counterweight` (1) | 0 | 1 | none | | | Dave Cumming: not an officer of Counterweight Limited (Companies House 11278617 lists Naomi Brosnahan and Justin Slabbert); headline says staffing and recruiting. Likely a different Counterweight (Open question 8) |
| 17 | NOPAGE `Hara Marketing` (1) | 0 | 1 | none | | | Dutch marketing agency |
| 18 | the-body-clinic: `The Body Clinic` (1) | 1 | 0 | The Body Clinic Stourbridge | product | no: searched, no non-junk additions | Aesthetic clinic with weight-loss programmes, owner Kate Sykes. Not Olena's Dutch The Body Clinic (Open question 4) |
| 19 | NOPAGE `Mind & Body Centre Ltd & LighterLife - Cornwall` (1) | 1 | 0 | LighterLife | referral | | Counselling psychologist, LighterLife in Cornwall |
| 20 | NOPAGE `Lighterlife Counsellor` (1) | 1 | 0 | LighterLife | referral | | Unit owner |
| 21 | NOPAGE `LighterLife-Maida Vale` (1) | 1 | 0 | LighterLife | referral | | Unit owner |
| 22 | NOPAGE `Self-employed` (1) | 0 | 1 | none | | | Nicola Bonell: self-employed psychotherapeutic counsellor; her MoreLife role is past; no account (Open question 8) |
| 23 | NOPAGE `lighterlife` (1) | 1 | 0 | LighterLife | referral | | Unit owner |
| 24 | NOPAGE `LighterLife Hampstead` (1) | 1 | 0 | LighterLife | referral | | Unit owner |
| 25 | healthhero: `HealthHero . Freelance` (1) | 0 | 1 | none | | | HealthHero is in Olena's registry (2026-07-21); freelance locum GP |
| 26 | NOPAGE `The Body Clinic, Leominster` (1) | 1 | 0 | The Body Clinic Leominster | partnership | no | Holistic health centre (Bruce Howes Ltd); clinical director |
| 27 | NOPAGE `Lighterlife, Beverley, East Yorkshire` (1) | 1 | 0 | LighterLife | referral | | Maxine Phillips-Smith (`/in/maxine-phillips-smith-86859844`), the profile kept |
| 28 | NOPAGE `C Graves Weight Management Consultancy Ltd` (1) | 1 | 0 | LighterLife | referral | | Carol Graves, "Director at LighterLife": a counsellor's own company |
| 29 | homerton-healthcare-nhs-foundation-trust (1) | 1 | 0 | Homerton Healthcare NHS Foundation Trust | referral | no | Psychologist in its specialist weight management and bariatric surgery service |
| 30 | NOPAGE `Habitual Wealth` (1) | 0 | 1 | none | | | Financial adviser, name collision |
| 31 | NOPAGE `Lighterlife Wycombe` (1) | 1 | 0 | LighterLife | referral | | Unit owner |
| 32 | NOPAGE `Lighterlife solihull` (1) | 1 | 0 | LighterLife | referral | | Unit owner |
| 33 | archvale: `Archvale . Part-time` (1) | 1 | 0 | Archvale | partnership | no | GP-practice succession and partnership services for NHS primary care; part-time COO |
| 34 | sdm-kalibra (1) | 0 | 1 | none | | | Italy |
| 35 | lanarkshire-medical-group: `Lanarkshire Medical Group . undefined` (1) | 1 | 0 | Lanarkshire Medical Group | referral | no | Glasgow medical group; locum GP with a lifestyle-medicine interest |
| 36 | NOPAGE `Weight Doctors Worldwide` (1) | 0 | 1 | none | | | Netherlands |
| 37 | NOPAGE `LighterLife Mexborough` (1) | 1 | 0 | LighterLife | referral | | Unit owner |
| 38 | NOPAGE `Bürgerspital Wertheim gGmbH` (1) | 0 | 1 | none | | | Germany |
| 39 | perspectum-ltd: `Perspectum Ltd` (1) | 1 | 0 | Perspectum | partnership | no: searched, no non-junk additions in the coordinator's count | Oxford imaging company with obesity body-composition research; partnership only |
| 40 | NOPAGE `lighterlife taunton` (1) | 1 | 0 | LighterLife | referral | | Unit owner |
| 41 | NOPAGE `Lighterlife - Chesterfield` (1) | 1 | 0 | LighterLife | referral | | Unit owner |
| 42 | NOPAGE `LighterLife Billericay` (1) | 1 | 0 | LighterLife | referral | | Unit owner |
| 43 | NOPAGE `LighterLife - Hereford` (1) | 1 | 0 | LighterLife | referral | | Counsellor |
| 44 | NOPAGE `CGCE Group` (1) | 0 | 1 | none | | | Germany; group behind Weight Doctors |
| 45 | maxylogic (1) | 0 | 1 | none | | | Polish IT services firm, CEO in Estonia |
| 46 | inem (1) | 0 | 1 | none | | | Portugal |
| 47 | NOPAGE `LighterLife - Telford` (1) | 1 | 0 | LighterLife | referral | | Counsellor |
| 48 | NOPAGE `LighterLife - Brentwood & Ongar` (1) | 1 | 0 | LighterLife | referral | | Counsellor |
| 49 | medisch-centrum-waalre: `QUOLE Medisch Centrum Waalre` (1) | 0 | 1 | none | | | Dutch clinic, person in Germany; QUOLE is in Olena's registry |
| 50 | exchangehealth: `Exchange Health` (1) | 1 | 0 | Exchange Health | partnership | no | Behaviour-change training for healthcare practitioners |
| 51 | NOPAGE `LighterLife UK Limited` (1) | 1 | 0 | LighterLife | referral | | Head-office accounts assistant |
| 52 | NOPAGE `LighterLife Mansfield` (1) | 1 | 0 | LighterLife | referral | | Counsellor |
| 53 | NOPAGE `Reset Health & Wellbeing Services LTD` (1) | 0 | 1 | none | | | Osteopathy and massage practice, name collision with Reset Health |
| 54 | NOPAGE `Weight Doctors GmbH` (1) | 0 | 1 | none | | | Germany |
| 55 | NOPAGE `Habitual Café and Bakehouse LTD` (1) | 0 | 1 | none | | | Café |
| 56 | NOPAGE `Essex Endocrine Clinic` (1) | 1 | 0 | Essex Endocrine Clinic | clinical | no | Dr Roselle Herring's practice; she leads the Essex Tier 3 obesity service |
| 57 | NOPAGE `Elysee Life - Medical Weight Loss` (1) | 0 | 1 | none | | | Netherlands |
| 58 | saira-nutrition (1) | 1 | 0 | Saira Nutrition | partnership | no | 12-week weight programme for small groups |
| 59 | lloydspharmacy: `LloydsPharmacy . Part-time` (1) | 1 | 0 | LloydsPharmacy (Online Doctor) | referral | no: searched, the domain returns retail-pharmacy staff; no non-junk additions in the coordinator's count | Online prescriber of weight-loss medication with Nutrition Coaching |
| 60 | NOPAGE `The Body Clinic Leominster ` (1) | 1 | 0 | The Body Clinic Leominster | partnership | | Managing director |
| 61 | NOPAGE `RESET Health Bar` (1) | 0 | 1 | none | | | Chef-owned restaurant, name collision |
| 62 | NOPAGE `LighterLife Aberdeen & Shire with Sandra` (1) | 1 | 0 | LighterLife | referral | | First name only ("Sandra"; the last name field reads "undefined") |
| 63 | nwangliaft (1) | 1 | 0 | North West Anglia NHS Foundation Trust | referral | no | NHS acute trust; midwife with a behaviour-change background |
| 64 | NOPAGE `Habitual Ventures` (1) | 0 | 1 | none | | | Bartender |
| | **Total (166)** | **126** | **40** | 18 accounts | | 7 yes | |

**Fail by name at validation (15 rows that join an IN account in `extract-people`):** Joana Rosado, Laura Milani, charlotte van vracem, Elien Laseure (`Pronokal` / `PronoKal Group`, outside the UK); Richard Tansley (cell `LighterLife`, Ireland); Luca Visini, Davide Morelli, Benedek Szulyovszky (`Reset Health`, outside the UK); Dave Cumming (`Counterweight`, not on the register); Dr Zubair A., Oliver Brooks, Jeff Hadaway, Cordell Jopson, Eliot Howes (`Medicspot`, already contacted from `katerina` on 2026-09-01); Maxine Phillips-Smith `/in/maxine-phillips-smith-b172a019` (duplicate profile).

**Identity and current-role checks (stay IN unless the check fails):** LighterLife Admin (company-named profile: send only if it reads as a person or a monitored head-office account, else hold); Sandra at LighterLife Aberdeen (first name only); Georgia Miller and Richard Ruff (MoreLife titles, headlines say "Healthy You"); Anthony Hardley (MoreLife title, headline says ReedMomenta); David Wong (Reset Health, blank headline); Kate Sykes (clinic website no longer resolves); Dr Sahira Dar and Bhavini Shah (locum and part-time GP roles). A job-change check runs on all 126.

## Use case (1 sentence)

UK weight-management programmes that run their sessions and check-ins remotely can add a guided two-photo scan to their own app or online client account, giving the person a way to record 80+ body measurements and body composition estimates at home before a check-in, and giving the coach or clinician a standardized, timestamped record to compare scans they select.

## Why this is plausible (evidence)

1. **Medication volume is rising and the care around it is moving to digital services.** NHS England's phased tirzepatide rollout begins with procurement of "digital weight management support services to accommodate some of the dietetic and psychological care needed" ([Pulse](https://pulsetoday.co.uk/news/clinical-areas/gastroenterology-obesity/nhse-plans-phased-rollout-of-tirzepatide-for-weight-loss-to-avoid-profound-impact-on-gps)). An estimated 1.6 million adults in Great Britain used weight-loss drugs between early 2024 and early 2025, most of them privately ([Pulse on the UCL study in BMC Medicine](https://www.pulsetoday.co.uk/news/clinical-areas/gastroenterology-obesity/around-1-6-million-uk-adults-use-weight-loss-drugs-research-finds/)). Online pharmacies now buy that care from programme providers: since Q1 2026 Reset Health delivers monthly consultations, nutrition counselling, behavioural coaching and psychological support through a remote care platform for Pharmacy2U's GLP-1 patients ([Pharmaceutical Commerce, 2026-02-18](https://www.pharmaceuticalcommerce.com/view/pharmacy2u-partners-with-reset-health-glp-1-weight-management)). Context for Katerina; no market numbers go in copy.
2. **The accounts on this list already deliver remotely, and two were bought in 2026 to scale technology-enabled care.** Counterweight-Plus holds its 1:1 and group appointments virtually ([NHS Lothian](https://services.nhslothian.scot/awmt2d/type-2-diabetes-remission-through-counterweight-plus/)); Medicspot gives members weekly 1-to-1 online coach check-ins ([medicspot.co.uk](https://www.medicspot.co.uk/how-it-works)); MoreLife's referred adults have a patient app (App Store, 2026); Habitual runs a 16-week course in its app (App Store). Voy bought MoreLife to support "more technology-enabled care pathways" ([BusinessCloud / LaingBuisson, June 2026](https://www.laingbuissonnews.com/healthcare-markets-content/voy-acquires-morelife-to-expand-digital-delivery-of-nhs-weight-management-services/)); Doctor Care Anywhere bought Medicspot's GLP-1 business on 8 May 2026 ([HTN](https://htn.co.uk/2026/05/12/doctor-care-anywhere-acquires-outcome-diagnostics-limited-and-medic-spot-limited/)). In a remote session nobody in the room takes a body measurement; FitXpress gives the person a guided way to capture one at home.
3. **FitXpress fits as an in-app capture, with honest limits.** White-label API and web or mobile SDK; two photos; under 45 seconds from the photos to structured results; 80+ body measurements; body composition estimates (BMI and BMR calculated); 3D model; repeatability under 1 cm for most evaluated measurements (`proof-points.md`, `accuracy-formulations.md`). Proof: an anonymised weight-management platform ran 34,000 scans in 2025, and 112,100 scans in 2025 across all 3DLOOK customers. Limits: no UK weight-management reference customer; no published comparison of body composition estimates with bioimpedance or any reference method; validation population 38-210 kg; data hosted on AWS in US-West-2 and partly US-East-1 (a likely question from NHS-commissioned providers, Open question 6).

**Constraint that shapes the angle:** since February 2025 the GPhC requires online prescribers to verify weight, height or BMI independently (video consultation, in person, or GP and medical records); photos sent in are not enough ([ITV](https://www.itv.com/news/2025-02-03/weight-loss-jabs-patients-to-face-more-stringent-checks)). This campaign therefore never offers the scan as BMI or eligibility verification for prescribing. It is a body record for check-ins after care has started.

## What Katerina's earlier UK campaigns teach this one

From `2026-07-31-uk-telehealth-digital-health/post-mortem.md` and `metrics-final.json`, and the response summaries of `2026-09-27-uk-bariatric-prequal` and `2026-09-01-uk-erakulis-similar`:

- **Baseline:** 258 invites, 69 accepted (26.7%), 13 replies (18.8% of accepted); Message 1 drew 12 of the 13 replies.
- **What earned meetings:** an owner persona, a hook in the person's own scope, the capability block, and an explicit 15-minute ask (3 of 3 interested replies). Two of the three came from programme or evidence owners (Director of Global Clinical Programs; Head of Nutrition, Research & Health at Slimming World), not the named personas. Here that points at MoreLife's Head of Systems Implementation, Evaluation & Innovation and Reset Health's science and clinical-intelligence leads.
- **What did not:** a member-engagement angle sent to franchise consultants (Slimming World WEAK tier) returned one PR forward; technical-integration as a first touch got replies and no interest. Vadim keeps every function in this list, so the 76 `referral` invites are scored on replies that name an owner, not on interest.
- **September UK sends:** one decline (bariatric) and one maybe-later from a partnerships manager (Nutracheck). Too thin to change the approach.

## Target buyer persona

**Who buys:** the owner of the programme's app or patient flow, of its clinical model, or of service operations, at accounts in segments A and B. At LighterLife the buyer is the franchisor's head office; unit counsellors and owners are referral paths to it. Clinicians in segment D can sponsor a pilot inside their service but rarely own a budget. Segment E has no buyer for this use case: its people get a partnership ask. Tiers only order the list; everyone goes in one import file (standing decision). Apollo additions take the lane their title maps to below.

**P1, owners at core accounts (15):**
- Reset Health (7): Oliver McGuinness, CEO (`product`); Rochelle Morris, CPO (`product`); David Wong, Executive Chairman (`product`); Laura Newson, Director of Partnerships and Propositions (`product`); Dr Laura Falvey, Executive Clinical Director (`clinical`); Ling Chow, Operations Director (`operations`); Jessie Ravenscroft, Director of Strategic Delivery (`operations`).
- MoreLife (2): Sophie Edwards, COO (`operations`); Dr George Sanders, Head of Systems Implementation, Evaluation & Innovation (`product`).
- Counterweight (2): Naomi Brosnahan, CEO; Justin Slabbert, Executive Chairman (both `product`).
- LighterLife (2): Sarah Kelly, Business Development Director; Tina Horsnell, Director of Business Development (both `product`, asked who at head office owns the online programme and the client's online account).
- Habitual (1): Elliott Silver, Head of Strategy and Operations (`operations`).
- PronoKal UK (1): Dr Philip Bazire, Medical Director and a director of the company (`clinical`).

**P2, leads (22):**
- Reset Health (10): Rebecca Ryan, Head of Product, and Rachel Dreycroft, Product Manager (`product`); Dr Claudia Ashton, Head of Clinical Services; Thomas Curtis, Head of Clinical Development; Thomas Godec, Director of Data Science & Clinical Intelligence; David Plans, CSO; Dr Sarah Oldfield, metabolic health doctor; Deborah Evans, Metabolic Health Lead (all `clinical`); Ciara Cook, Head of Programmes and Clinical Operations, and Lauren Sien, Governance Lead (`operations`).
- MoreLife (9): Grant Westermann, Digital Projects & Systems Manager (`product`); Georgia Miller, Service Manager; Matthew Buckley and Alaa Adwan, Service Leads; Emily Costelloe, Practitioner Manager; Amy Broadhurst, Client Services Lead (all `operations`); Juli Mey, Tier 3 Practitioner Lead; Keisha C., Specialist Weight Management Dietitian; Susan Brennan, GP in Weight Management (all `clinical`).
- Habitual (1): Rebecca Tessier, Patient Operations Lead (`operations`). Essex Endocrine Clinic (1): Dr Roselle Herring (`clinical`). The Body Clinic Stourbridge (1): Kate Sykes, owner (`product`).

**P3, technical and partnership (13):** Reset Health: Alex Nancekievill (Group CTO), Andrew Liles (CTO), Yousaf Ahmad (Head of Technical Delivery), Gareth Bartley (Backend Technical Lead), Alasdair Yorke (Lead Front End Developer); Habitual: Pip Young (Head of Engineering): all `technical-integration`. Partnership (7, `partnership`): Anna Bell Higgs (Counterweight, Partnerships Manager), Joanna Bruce MBE and Luana Howes (The Body Clinic Leominster), Mike Pallett (Archvale), Sarah Le Brocq (Perspectum), Dr Lauren Rockliffe (Exchange Health), Saira Mashru (Saira Nutrition).

**P4, referral (76):** everyone else at an IN account: LighterLife unit counsellors and owners and head-office finance and admin (41), MoreLife practitioners, coordinators, nutritionists, therapists, behaviour-change and smoking-cessation specialists, children's practitioners, client services and the partnership and engagement officer (25), Reset Health's CFO, graduate commercial associate, behaviour-change specialist and consultant health psychologist (4), Counterweight's two nutritionists (2), and the four clinicians at Homerton, North West Anglia, Lanarkshire Medical Group and LloydsPharmacy (4).

**Lane by title, for Apollo additions:** founders, CEOs, managing directors, chairs, product and digital leads, propositions directors → `product`; medical, clinical, dietetic and nutrition leads, research and evaluation leads → `clinical`; COOs, operations, programmes, services and patient-operations leads, superintendent pharmacists → `operations`; CTOs and engineering → `technical-integration`; partnerships and business development at Perspectum → `partnership`; commercial, finance and anyone below lead level → `referral`.

**Not the buyer (FAIL for the cold send):** only the 40 OUT rows in the verdict table. Every function at an IN account has a lane.

**KPIs they care about:** for NHS-commissioned providers, outcomes they report to commissioners and keeping people in the programme; for GLP-1 services, what the clinician sees at each monthly or weekly check-in and support after treatment ends; for LighterLife head office, the client experience between group sessions; for clinicians, a usable record in their service; for partnership accounts, what they can offer their own clients.

**Likely objections and the honest answer:**
- "We already weigh people / members log their weight / our app has a progress chart" (MoreLife, Counterweight, Habitual, LighterLife). True, and nothing replaces it. The scan adds body measurements and body composition estimates from the same phone; a pilot can run it next to what they record now. Never suggest their data is wrong.
- "Our clients already have body composition scales" (PronoKal UK). True, and nothing replaces them. The scan adds 80+ body measurements and a 3D model from the phone; never compare its body composition estimates with the scales.
- "How accurate is it? Does it work at higher BMI?" `accuracy-formulations.md` §1.1 or §5; repeatability §1.2; validation population ages 16 to 78, heights 150 to 220 cm, weights 38 to 210 kg; "Performance outside this scope has not been characterized."
- "Where is the data? NHS DSPT, DTAC, UK hosting?" Copy says nothing about it. In a reply: the GDPR role sentence from `compliance.md` §2, hosting on AWS in US-West-2 and partly US-East-1, photos deleted after processing or within 30 days, outputs deletable by scan ID; national-law, NHS assurance and transfer questions go to legal@3dlook.me (Open question 6).
- "Can it confirm BMI for prescribing?" No. FitXpress does not decide eligibility, diagnose or recommend treatment (`compliance.md` §7, §10).
- "Is it a medical device?" In a reply only, `compliance.md` §1 UK/EU MDR wording.
- "We are a franchise unit / I only deliver sessions." Correct: the referral asks who at head office or in the service owns the online programme, the app or the model.
- "Price?" Never in copy; a call question.

### Target buyer persona: Sales Navigator pull for step 3

**Pull by title filter inside the approved company list, never by company alone.** The export is the list. This block drives only the Apollo top-up that Vadim asked for (`apollo-pull.py search` takes each IN account's domain and these titles), on the seven `apollo_topup: yes` accounts. Broad on purpose: the validator assigns lanes and fails what does not fit.

```titles
Chief Executive Officer
CEO
Managing Director
Founder
Co-Founder
Chair
Executive Chairman
Chief Operating Officer
Operations Director
Director of Operations
Head of Operations
Chief Medical Officer
Medical Director
Clinical Director
Head of Clinical Services
Head of Clinical Operations
Clinical Lead
Chief Product Officer
Head of Product
Product Director
Product Manager
Chief Digital Officer
Head of Digital
Digital Director
Chief Technology Officer
Head of Programmes
Programme Director
Head of Services
Service Director
Chief Commercial Officer
Commercial Director
Head of Partnerships
Partnerships Director
Business Development Director
Head of Business Development
Head of Nutrition
Head of Dietetics
Lead Dietitian
Head of Weight Management
Superintendent Pharmacist
Head of Research
Head of Evaluation
```

**`cap_per_group: 50`** (default since 2026-09-29, unchanged). LighterLife 43 (room for 7), MoreLife 36 (room for 14), Reset Health 26 (room for 24). Nothing is capped out before Apollo; the coordinator's non-junk Apollo counts (32, 29, 31) would take all three over 50 (Open question 5).

## Message angle: segments, lanes, company facts, questions and the content asset

Every person gets exactly one lane, spelled as below. LighterLife (43), MoreLife (36) and Reset Health (26) send many people at once, and franchise owners and practitioners talk to each other, so no two people at one company share an opener, a central question, a closing ask, a Message 2 opener or a product sentence; facts agree across all of them. Numbers in copy come only from `proof-points.md` (Rules). **Writer notes are instructions to the writer and are never copied into a message.**

### Segment angles (writer notes)

- **A. NHS-commissioned and digital providers** (Reset Health, MoreLife, Counterweight). A body record the person takes at home inside the programme's app, before a remote session, for the practitioner or clinician to review. For research, evaluation and data roles: a standardized, timestamped body measure their outcome reporting could include. Use case `fx-telehealth-weight-loss`, without its hero line, Smart Scales framing or KPI list.
- **B. Private GLP-1 services and online prescribers** (Habitual, LloydsPharmacy Online Doctor, Medicspot via Apollo, PronoKal UK). The same body record at the monthly or weekly check-in after treatment starts, and during support after treatment. Never at the point of prescribing; never as BMI or weight confirmation. At PronoKal UK lead with the 80+ body measurements and the 3D model and leave body composition estimates out: its clients already get body composition scales.
- **C. LighterLife.** Head office owns the programme and the client's online experience: weekly Mentor-led groups, mostly online, a web account on lighterlife.com, and a weight-loss medication service by consultation. LighterLife has no client app (UK App Store and Google Play, 2026-10-06), so no message says "your app". The angle for head office: a guided two-photo scan a client takes at home before the weekly online session, which can run in a web page through the web SDK, with nothing to ship. For every unit person it is a referral question about who at head office owns the online programme, the client's online account or the medication service.
- **D. Clinicians** (Essex Endocrine Clinic, Homerton, North West Anglia, Lanarkshire Medical Group, and the GP at LloydsPharmacy). A short note on what the scan returns and one question about who in their service would look at a tool like this, or (Dr Herring, `clinical`) whether a home body record has a place in a Tier 3 pathway.
- **E. Partnership only** (Perspectum, Exchange Health, Saira Nutrition, Archvale, The Body Clinic Leominster) and Counterweight's partnerships manager. Ask whether a partner capability has any place in what they offer, and who would decide. No pitch, no claim their clients need body scanning, no comparison with their own product. Accept a no.
- **F. The Body Clinic Stourbridge.** A body record taken on the phone before a consultation and between treatment sessions in the clinic's own client flow. No appearance outcomes, no treatment or device names, no before-and-after.

### What the accounts already record (writer notes; overlap, not displacement)

- **MoreLife:** its patient app logs weight and shows a progress chart (App Store "Morelife by Voy", 1.0.14, 2026-05-21). Never name the app's publisher, its weight log or chart.
- **Counterweight:** its app logs weight, mood, blood glucose, HbA1c "measurements and more" and imports step data (App Store 2.5.36, 2026-09-29). Never name any of it.
- **Habitual:** its app tracks sleep, weight and mood (App Store 2.6.19, 2026-09-30). Never name them.
- **LighterLife:** each client's Mentor monitors their weekly weight loss (lighterlife.com/mentor-support, 2026-10-06), and third-party descriptions have counsellors weighing and measuring clients. Never mention either, and never say or imply units measure differently, inconsistently or not at all.
- **PronoKal UK:** new clients get free body composition scales with an app that shares reports with their specialist (pronokal.co.uk, 2026-10-06). Never mention the scales, their brand, bioimpedance or that app; never set body composition estimates next to them.
- **LloydsPharmacy Online Doctor:** BMI and ID checks at consultation. Never mention them.
- **Saira Nutrition:** her site reports waist results from her programme. Never mention them.
- **Perspectum:** sells imaging-based body composition for research and care. Never compare; partnership only.
- **Everyone else** (Reset Health's Roczen app listing included): nothing body-related verified. Describe the capability; say nothing about what they record today.

### Lanes

- **`product`** (founders, CEOs, chairs, product and propositions leads, LighterLife's business development directors, clinic owner). Say what the app or online account can ask a person for: a guided two-photo scan at home that returns 80+ body measurements, body composition estimates and a 3D model, white-label through API or web and mobile SDKs, with no hardware to ship. Ask the person's own question, then an explicit 15-minute ask (the July opener).
- **`clinical`** (clinical directors and heads of clinical services, PronoKal UK's medical director, metabolic doctors, consultant endocrinologist, Tier 3 lead, specialist dietitian, GP in weight management, science and clinical-intelligence leads). The care team gets a standardized, timestamped body record and compares scans it selects; values are measurements and estimates for the team to review; the repeatability sentence. Research and data roles: what a standardized body measure adds to the outcomes they evaluate. One question, then a 15-minute ask.
- **`operations`** (COO, operations and strategic-delivery directors, programmes and clinical operations, service managers and leads, practitioner manager, client services lead, governance lead, patient operations). Nothing is shipped, stocked or supported; the capture follows the same guided sequence every time; the speed phrase. Message 2 may carry the UK compliance line (Rules).
- **`technical-integration`** (CTOs, technical delivery, engineering leads, developers at Reset Health and Habitual). REST API with API-key authentication, web and mobile SDKs; photos deleted after processing or within 30 days; outputs stored and deletable by scan ID. No integration-time figure: "2-4 weeks for basic integration" is internal guidance in `icp-detail.md`:597, not a `proof-points.md` number, so a timing question goes to the call. Technical tone. Message 2 links the FAQ.
- **`partnership`** (segment E, Counterweight's partnerships manager). One line on what the scan returns, the company fact, and the question whether a partner capability has any place and who would decide. No compliance line, no article; Message 2 carries the calendar link.
- **`referral`** (P4). The person's own question, naming the owner they could point to; one line on what the scan returns; the company fact. No pitch, no compliance line, no article, calendar link optional. LighterLife units: who at head office owns the online programme, the client's online account or the medication service (never "app": LighterLife has none); never ask a unit to adopt anything, never mention other units, owners or counsellors, never suggest head office knows about the message. MoreLife practitioners: who owns the patient app or programme design for adult services. Psychologists and therapists (Reset Health, MoreLife, LighterLife, Homerton): short and neutral; never suggest the scan helps motivation, body image or mood.

### Company facts the copy may use

| Company | ID | Fact the copy may use | Writer notes |
|---|---|---|---|
| Reset Health | RH1 | Reset Health helps people manage obesity and type 2 diabetes through the Roczen app, combining specialist clinicians, diet and lifestyle plans, prescription medication, 1:1 clinical care and a dedicated mentor. | LinkedIn About |
| Reset Health | RH2 | Since early 2026 Reset Health has provided the wraparound care (monthly consultations, nutrition counselling, behavioural coaching, psychological support) for Pharmacy2U's patients on weight-loss medication, through its remote care platform. | Pharmacy2U may be named only in Reset Health messages, only with this fact |
| MoreLife | ML1 | MoreLife delivers specialist weight-management programmes for children, families and adults in healthcare, community and workplace settings, including adult Tier 3 services. | Adult services only as a scan context |
| MoreLife | ML2 | MoreLife has its origins in research and has delivered weight-management programmes since 1999. | more-life.co.uk/about-us. Never name the university or the founder; never mention the 2026 change of owner |
| MoreLife | ML3 | Adults referred to a MoreLife programme get a patient app for their programme. | Never name the publisher or what the app records |
| Counterweight | CW1 | Counterweight's programmes come from research begun in 2000 with academics at seven UK universities. | |
| Counterweight | CW2 | Counterweight delivers the NHS Type 2 Diabetes Path to Remission Programme, and Counterweight-Plus in Scotland, where 1:1 and group appointments are held virtually. | "remission" only as the programme's name, never as anything 3DLOOK does |
| Counterweight | CW3 | The Counterweight app gives members guidance from the programme's dietitians every fortnight and goals for the length of the programme. | App Store listing. Never name anything the app logs, imports or shows as progress |
| Habitual | HB1 | Habitual runs two structured programmes: a medication plan and a soups-and-shakes plan. | |
| Habitual | HB2 | The Habitual app carries a 16-week behaviour-change course with new content every day. | |
| LloydsPharmacy | LP1 | LloydsPharmacy Online Doctor offers weight-loss injections and tablets alongside Nutrition Coaching. | Never mention consultations, BMI checks or prescribing |
| Medicspot | MS1 | Medicspot members get weekly 1-to-1 online check-ins with a health coach, and support continues after they finish treatment. | Apollo people only; never mention the 2026 sale |
| Medicspot | MS2 | Medical weight management has been Medicspot's only service since October 2024. | |
| LighterLife | LL1 | LighterLife has run weight-loss and weight-management programmes for over 30 years, pairing a structured plan with counselling on the reasons behind overeating. | LinkedIn About |
| LighterLife | LL2 | Each LighterLife client has a personal Mentor who hosts a small weekly group session, and most clients join those sessions online. | lighterlife.com/mentor-support (2026-10-06). Never mention units, territories, the network's size, the Mentor's weight monitoring or the WhatsApp and Facebook groups |
| LighterLife | LL3 | LighterLife offers weight-loss medication by consultation, alongside its Foodpacks and Mentor support. | lighterlife.com/how-it-works (2026-10-06). Head-office people only; no drug names; never tie the scan to the consultation, prescribing or who can start treatment |
| PronoKal UK | PK1 | PronoKal UK runs medically supervised weight-loss programmes in which each client has a dedicated doctor and nutrition specialist, with consultations by Zoom or telephone. | pronokal.co.uk (2026-10-06). Call it "PronoKal UK"; never name its legal entity, the Barcelona group, other countries, the scales it gives clients, the diet method or injections |
| PronoKal UK | PK2 | PronoKal UK is an independent British business and a licensed affiliate of a global weight-management brand. | pronokal.co.uk/about-pronokal. Never quote the group's doctor or customer numbers |
| The Body Clinic Stourbridge | BC1 | The Body Clinic in Stourbridge brings together body treatments and weight-loss programmes, run by Kate Sykes since 2015. | No treatment, device or outcome |
| Essex Endocrine Clinic | EE1 | Dr Roselle Herring leads the Essex Tier 3 obesity service and runs the Essex Endocrine Clinic. | |
| Homerton Healthcare | HO1 | Homerton runs a specialist weight management and bariatric surgery service. | From her title |
| North West Anglia NHS FT | NW1 | The trust runs Hinchingbrooke, Peterborough City and Stamford and Rutland hospitals. | Never use pregnancy or maternity as a scan context |
| Lanarkshire Medical Group | LM1 | Dr Dar combines general practice with lifestyle medicine and coaching. | From her headline |
| Perspectum | PE1 | Perspectum works on obesity imaging and body-composition research for clinical care and drug development. | Never compare, never name its methods |
| Exchange Health | EX1 | Exchange Health trains healthcare practitioners in psychology-led behaviour change and reflective practice. | |
| Saira Nutrition | SN1 | Saira runs Transform, a 12-week programme for small groups of five women. | |
| Archvale | AV1 | Archvale works with GP partners on succession, transitions and the future of their practices. | |
| The Body Clinic Leominster | BL1 | The Body Clinic Leominster offers holistic therapies, including health MOTs and healthy-eating support. | A message that mentions a health MOT says blood pressure, cholesterol and blood tests stay outside the scan |

### Question themes for one company's people (writer notes)

Each person gets one question nobody else at the company gets. Themes, to be phrased per person from their title or unit:
- **LighterLife (41 referral, 2 product):** who owns the client's online account on lighterlife.com; what clients use between weekly online sessions; Mentor and counsellor training and programme content; new programme development; the medication service (head-office people only); online groups; technology partners; client experience; head-office support for Mentors and counsellors; clinical oversight of the plans; finance or procurement route for a supplier (Natalie Cowie, Lyn Obeney); the head-office account itself (LighterLife Admin).
- **MoreLife (25 referral):** who owns the adult patient app; programme design for Tier 3; outcome reporting to commissioners; workplace programmes; programme evaluation; client-services systems; new service bids; practitioner tools; digital inclusion for adults who rarely use apps. Children's practitioners (Chad Haefele, Evan Robertson) are asked only about adult services.
- **Reset Health (4 referral):** finance route for a new supplier (CFO); commercial propositions (graduate associate); behaviour-change design; psychology team's view of body data in the app.
- **Peers most likely to compare notes:** Reset Health's executive team and its clinical leaders; MoreLife's Sussex Tier 3 practitioners and its service leads; LighterLife's two business development directors; the Body Clinic Leominster pair; LighterLife owners in the same region.

### Content asset in Message 2 (at most one article link, plus the calendar link)

| Who | Link | Writer notes |
|---|---|---|
| Reset Health, Habitual, LloydsPharmacy, Medicspot, PronoKal UK: `product`, `clinical`, `operations` | https://3dlook.ai/content-hub/glp-1-market/ | Do not quote its "approximately 30 to 45 seconds", its scale-weight sections or its US compliance wording |
| `technical-integration`, every company | https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/ | Never restate it in the message |
| Everyone else (MoreLife, Counterweight, LighterLife, segments D to F, every `partnership` and `referral`) | no article | |

Both links returned HTTP 200 on 2026-10-06. The `/fitxpress/for-...` landing pages returned 404 and are not linked.

## Rules for steps 3-5

- **Sender and format:** Katerina, English, `Katerina` alone on the last line. Connection request with no note. Message 1 ≤ 600 characters, median about 320 in 4 short paragraphs; Message 2 ≤ 550 with https://meetings.hubspot.com/katerina-galich as plain text (required in every lane except `referral`, where it is optional) and at most one article link (asset table). All 126 go in one import file; tiers only order the list.
- **Lanes are exactly** `product`, `clinical`, `operations`, `technical-integration`, `partnership`, `referral`.
- **Several people at one company.** Never mention colleagues, other units, counsellors or practitioners; never claim to have spoken with anyone there; never claim an interaction that did not happen. Name the company in every Message 1. No two people at one company share an opener, a central question, a closing ask, a Message 2 opener or a product sentence.
- **Message 1 makes an observation from the company fact or the person's role,** never about something the company lacks. The template's "what's missing" step does not apply.
- **Never put a prospect's own data next to ours.** No message names a prospect's weigh-ins, weight log, progress chart, measurements, BMI checks or records and then says what the scan returns. Describe the scan on its own.
- **Not verification.** Never offer the scan as weight, height or BMI confirmation, as a check before prescribing, or as anything that decides who can start or continue treatment. It is a record for check-ins after care has started. Never cite or paraphrase GPhC, MHRA, NICE or any regulator or guidance.
- **GLP-1.** Say "GLP-1" or "weight-loss medication" only; no drug, molecule or pharma names. Never tie the scan to prescribing, dosing or treatment decisions.
- **NHS.** Never imply NHS endorsement, approval, assurance or hosting; never mention commissioners' contracts, tenders or values; never suggest NHS patient data goes anywhere.
- **Children and pregnancy.** The scan is never offered for anyone under 16 (the validation population starts at 16) and never in a pregnancy or maternity context. Children's practitioners and the midwife get referral questions about adult services only.
- **Owners and deals.** Never mention that MoreLife or Medicspot changed owner, never name their buyers, and never mention funding, investors, valuation, revenue, prices, headcount or unit counts.
- **Former employers.** A person's former employer may be named (standing decision) unless it is another account in this campaign (MoreLife, Reset Health, Medicspot, LighterLife, Counterweight, Habitual, PronoKal UK and the rest): never name one prospect in another prospect's copy. Pharmacy2U appears only in Reset Health copy, with RH2.
- **Psychologists, therapists and counsellors:** short and neutral; the scan is never framed as motivating, reassuring or about body image.
- **LighterLife units:** referral only, as in the lane; never pitch the unit, never mention franchise terms, fees or territories, never suggest head office is behind or ahead on anything.
- **Aesthetic clinic:** no before-and-after, no appearance or shape promises, no treatment or device names. The 3D model is a view the clinic chooses to show.
- **Compliance line.** At most one, only in Message 2, only in `product`, `clinical`, `operations` and `technical-integration` messages at Reset Health, MoreLife, Counterweight, Habitual, LloydsPharmacy, Medicspot and PronoKal UK, verbatim from `compliance.md` §9: "In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes SCCs." Nothing about UK hosting, DSPT, DTAC or NHS assurance. Never "HIPAA compliant", "SOC 2 certified" or a medical-device claim in cold copy; replies use `compliance.md` §10.
- **No 3DLOOK client is named.** Anonymised proof allowed: "one weight-management platform ran 34,000 scans in 2025" (no client name, no geography); "112,100 scans in 2025 across all 3DLOOK customers" (3DLOOK-wide scale, its own sentence, never tied to the UK, a client or patients); "100+ clients". The UK online-pharmacy 7,500 line is not used (Vadim, 2026-09-27).
- **Numbers only from `proof-points.md`:** two photos (front and side); "under 45 seconds from the photos to structured results" (the only speed wording); 80+ body measurements; body composition estimates (body fat %, lean mass, fat mass) with BMI and BMR as calculated metrics; "96-97% accuracy against expert manual measurement" or the full `accuracy-formulations.md` §1.1 or §5 sentence; repeatability only as "For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm."; validation weights 38 to 210 kg (in `clinical` only); the 34,000 and 112,100 lines. No integration-time figure in any lane: "2-4 weeks" comes from `icp-detail.md`:597, not from `proof-points.md`. No market, obesity, prescription or prospect figures in copy.
- **Accuracy wording.** "96-97% accuracy against expert manual measurement" describes body measurements; it never shares a sentence with lean mass, fat mass, body fat or body composition, and never opens Message 2. Measurements are measurements; body composition values are estimates. No ISO 0.40 cm figure.
- **No outcome promises.** Never promise or imply more weight loss, retention, adherence, engagement, remission, outcomes for commissioners or ROI. Describe what the scan returns, where it runs and how much it is used.
- **What the scan does not do.** It does not diagnose, decide eligibility, recommend or adjust medication, or interpret results. Say "the team compares scans it selects", never "tracks each patient". No visceral fat output.
- **Body language.** Person-first: "people living with obesity". Never "obese" or "diabetics".
- **Word traps.** Never "objective" about our data (use standardized, timestamped, structured, repeatable); never "comprehensive", "seamless", "leverage", "game-changer"; no em or en dash; no "plus" as a connector; no "so" introducing a benefit; no corrective "X, not Y".
- **Writer notes and card instructions are not copy.** "generic figure", "never a promise", "not a promise", "context only" and "writer note" are banned terms, so a leak fails the gate.
- **No pricing and no trial terms** anywhere. A price or trial question goes to the call.
- **Message 1 gate.** Every message 1 carries at least one product specific from `proof-points.md` and one line that could only have been written to that company; each pair of messages cites at least one number. The `referral` lane is exempt (the gate skips it), and still names the company and uses its fact.

## Anti-cases (where it does NOT work)

- **Out, by name:** the 40 OUT rows of the verdict table, and the 15 of them that join an IN account (fail by name). Match on the company LinkedIn page and website, never on the name alone.
- **Structural anti-cases:**
  - **Displacement:** an account that runs a phone-camera body scan or has signed a scanning vendor is held for Vadim. None found on 2026-10-06; three sites unreadable (Read this first, item 7).
  - **Partial overlap is not displacement:** weight logs, progress charts, counsellor weigh-ins, BMI checks and body composition scales (PronoKal UK) stay IN, and copy never sets them next to the scan.
  - **Eligibility and prescribing checks:** never the use here (GPhC regime; `compliance.md` §7).
  - **Children, pregnancy, and people outside the 16-78 / 38-210 kg validation scope:** never a scan context.
  - **Franchise units on their own:** a unit cannot add an SDK to the franchisor's app; units are referral paths only.
  - **Non-UK people and companies:** Olena's geo (PronoKal Group staff on the Continent, Weight Doctors, QUOLE, Elysee Life, CGCE) or out of every market; UK-company staff abroad are OUT under this scope. PronoKal UK, the group's UK licensee, is IN.
  - **Another profile's account:** HealthHero (Olena). Name collisions in the registry (The Body Clinic) are checked by website, not by name.
  - **Recently acquired accounts:** MoreLife and Medicspot are IN on Vadim's scope, with copy that never mentions the deal; pause either if the new owner announces a platform consolidation before send.
- **Stop conditions before send:** an IN account announces a merger, closure or a body-scanning partner (pause, Vadim decides); a profile shows the person has left (drop; replace only through the Apollo top-up).

## Vadim's standing decisions (built in, not open questions)

1. **No headcount floor** (2026-09-29).
2. **`cap_per_group: 50` for every campaign, no waves** (2026-09-29): one closely.io import file.
3. **A lane for every function** (2026-09-29): every person at an IN company gets one of the six lanes.
4. **FAIL only for the wrong company, people who left, identity collisions and duplicates;** company-named profiles are held, not failed.
5. **Former employers may be named** (2026-09-29), within the Rules' limit.
6. **Live 3DLOOK pages may be linked as they are** (2026-09-29); copy still uses only the approved wording.
7. **No 3DLOOK client is named;** 34,000 scans without client or geography; 112,100 scans as 3DLOOK-wide scale (2026-09-29); "100+ clients" publicly (2026-09-30). For `katerina`, the UK 7,500-scan line is not used (2026-09-27).
8. **A list Vadim brings has no company-researcher step** (Vadim's playbook).
9. **Franchise networks:** the franchisor is the buyer; units are referral paths, grouped under the franchisor's canonical name.
10. **Re-entering an account already worked from `katerina` goes through new people only;** people already messaged stay excluded (Healthier Weight and Tonic, 2026-09-27).

## Vadim's decisions 2026-10-06 (scope)

Vadim, 2026-10-06: «по англії профіль Каті Галіч. В гіпотезі максимально більше контактів взяти та відсіяти тільки мусор. Якщо по деяким компаніям не всі співробітники, добрати іх в аполо.» ("England, Katya Galich's profile [Katerina Galich, `katerina`]. Take as many contacts as possible in the hypothesis and filter out only the junk. Where some companies do not have all their staff, top them up in Apollo.") Applied as follows:

1. **Maximum contacts.** Every UK-located person at a UK weight-management, obesity, metabolic or health account is IN, junior and front-line people included (they get the `referral` lane). 126 of 166.
2. **Only junk and out-of-market rows are OUT:** different businesses with a colliding name (Habitual Wealth, Habitual Café and Bakehouse, Habitual Ventures, RESET Health Bar, Reset Health & Wellbeing Services), an unrelated agency and IT firm (Hara Marketing, MaxyLogic), a self-employed counsellor with no account, a "Counterweight" director not on Counterweight Limited's register; people outside the UK and non-UK companies (Olena's geo or no profile's market); HealthHero (Olena's registry); people already contacted from `katerina`; one duplicate profile. Each judgement call was checked on the web (Sources).
3. **Apollo top-up wherever an IN account's staff are not all in the list, junk aside** (Vadim's wording; the first draft narrowed it to "where the list does not reach decision-makers"). The coordinator's free all-functions search on 2026-10-06 covered the first draft's 17 accounts (658 candidates, 75 already in the export) and found new non-junk people at Reset Health 31 (32 of its 61 LinkedIn staff are not in the export), MoreLife 29, LighterLife 32, Counterweight 20, Habitual 10 and Medicspot 6 (new people only). `apollo_topup: yes` on those six and on PronoKal UK, which the search did not cover (pronokal.co.uk, UK staff only). `no` elsewhere: complete (Exchange Health, Saira Nutrition), no LinkedIn page and no Apollo match (Essex Endocrine Clinic, The Body Clinic Leominster), or searched with no non-junk people in the coordinator's count (Homerton, North West Anglia, Archvale, Lanarkshire Medical Group, The Body Clinic Stourbridge, LloydsPharmacy, Perspectum). Titles in `apollo-candidates.csv` closest to the line, if Vadim reads junk more narrowly: Perspectum's chief executive, chief strategy officer, medical directors and business development staff; Homerton's bariatric surgeon and its diabetes and endocrinology staff; North West Anglia's consultant endocrinologist. The cap stays 50 (Open question 5).
4. **LighterLife** is one group under the franchisor; UK counsellors and owners are `referral`, each with a different question about who at head office owns the online programme, the client's online account or the medication service (LighterLife has no client app); the Republic of Ireland master franchise is OUT.
5. **Name variants** of LighterLife, MoreLife, Medicspot, Perspectum, LloydsPharmacy, PronoKal UK and The Body Clinic Leominster are grouped under one canonical account each (aliases above the verdict table). The Stourbridge The Body Clinic is a separate account from both The Body Clinic Leominster and Olena's Dutch The Body Clinic.

## Vadim's decisions 2026-10-06 (approval)

Vadim approved the hypothesis on 2026-10-06, answering the open questions in the chat:

1. **Cap raised for LighterLife, MoreLife and Reset Health** («Підняти ліміт для трьох»): every non-junk Apollo person is added, LighterLife up to 75 (43 + 32), MoreLife 65 (36 + 29), Reset Health 57 (26 + 31). `cap_per_group` in the frontmatter is one number per campaign, so it is 75 (LighterLife, the largest group); no other group comes near it. Open question 5 is closed.
2. **MoreLife goes, all of it** (Open question 1): it is treated as an operationally independent provider after the Voy acquisition, and the copy never mentions the deal or Voy.
3. **Every other open question takes its default** («Апрув з дефолтами»): Medicspot only through new Apollo people, Doctor Care Anywhere not an account (2); UK-company staff abroad stay OUT, Philip Bazire IN (3); clear the name-only Olena flag on The Body Clinic Stourbridge and send to Kate Sykes after a current-role check (4); nothing about UK hosting, DSPT or DTAC in copy, replies on that go to legal@3dlook.me (6); the 9 low-fit people go as `partnership` or `referral` (7); Nicola Bonell and Dave Cumming stay OUT (8).

## Vadim's decisions 2026-10-06 (validation)

Vadim approved the validated list on 2026-10-06 (checkpoint after step 4), answering in the chat:

1. **SEND = the 203 PASS plus three WEAK:** David Wong (Executive Chairman, Reset Health; empty profile, strong title), Anthony Hardley (MoreLife; headline names the ReedMomenta agency, treated as a contractor at MoreLife) and Kate Sykes (The Body Clinic Stourbridge; the clinic website no longer resolves, her profile still lists her as owner). The other five WEAK stay out: LighterLife Admin (company account), "Saira Nutrition" (Saira Mashru's second profile), Emily Macleod (moving to the Netherlands), Emma Walker (now an independent Cambridge Weight Plan consultant), Samantha Oon (latest role at HeliosX).
2. **Two staff pools abroad are taken** («Взяти обидва пули»), which changes the UK-only rule of the scope block for these two pools only: Counterweight's team in South Africa (11 people) and Reset Health Malaysia (6 people). Every one of them is `referral`, sent from `katerina` because no profile owns South Africa or Malaysia. The ask is internal: who at the UK head office (Counterweight Ltd, Reset Health in London) owns the programme, the patient experience or the app, never a pitch to the local team. Nothing in their copy about local regulation, local market or compliance in South Africa or Malaysia; no compliance line. Whether the South Africa team serves UK clients is not confirmed: copy does not claim it.

## Validation criteria (Step 2 will check)

There is no company research. Step 2 is `companies.csv`; step 4 validates people against the persona.

- **Companies.** 18 rows, one per IN account, aliases as above, `hq_country` United Kingdom, `icp_fit` high or medium only (`low` is dropped by `extract-people`), `apollo_topup` flag in `notes`. `record` registers the 18 group names (the part outside the parentheses) and never an OUT company.
- **Registry.** Record `2026-09-01-uk-erakulis-similar` first; then `outbound-registry.py check --profile katerina` should flag the Medicspot five (already contacted) and Kate Sykes (name collision, cleared by default) and nothing else.
- **Displacement re-check** before import: no IN account shows a phone-camera body scan or a scanning vendor; retry counterweight.org and the Stourbridge clinic (lighterlife.com and pronokal.co.uk were read on 2026-10-06).
- **People.** 126 PASS with the tiers and lanes in "Target buyer persona": P1 15, P2 22, P3 13, P4 76; lanes `referral` 76, `product` 13, `operations` 12, `clinical` 12, `partnership` 7, `technical-integration` 6. FAIL: the 15 fail-by-name rows (the other 25 OUT rows never reach `people-raw.csv`). Apollo additions are validated with the same lane-by-title rules and the 50 cap.
- **Message 1 gate.** As in Rules: zero client names, pricing, `banned_terms`, verification or eligibility framing, prospect data next to ours, outcome promises, or compliance lines outside the allowed lanes. Kept as a failure, not a note: `2026-07-21` sent 307 first messages with no specific and drew 1 reply on 67 sends.
- **Proof in product-info.** Use-case file and live GLP-1 article: yes. UK weight-management reference customer: none; the anonymised 34,000-scan platform and 3DLOOK-wide 112,100 scans are the proof, used openly.

## Success metrics for this campaign

Denominators as in `metrics-final.json` (Closely event counters). 126 invites before Apollo, 83 of them `referral` or `partnership`: read per segment.

| Metric | Target | Floor | Basis |
|---|---|---|---|
| Invites sent | 126 + Apollo additions | 115 | after job-change and identity checks |
| Connection acceptance | 25% | 15% | `katerina` UK July: 69/258 = 26.7% |
| Replies per accepted person | 12% | 6% | July: 13/69 = 18.8%, owner-heavy list; this one is referral-heavy |
| Positive replies (interest or question) from P1, P2 or Apollo owners | 3 | 1 | 37 P1-P2 in the export |
| Referral replies naming an owner | 6 | 2 | 76 referral invites, 41 of them LighterLife |
| Accounts with at least one reply | 6 of 18 | 3 | |
| Discovery calls | 2, at different accounts | 1 within 8 weeks | |

**Falsified if** three or more P1 or P2 replies say a home body record has no place in remote weight-management care next to what they record now, or that UK data hosting rules it out. **Inconclusive** if fewer than 20 people accept.

## Risks

1. **New owners.** MoreLife (Voy) and Medicspot (Doctor Care Anywhere) may move app and supplier decisions to the parent; Voy is already excluded for `katerina`.
2. **NHS data assurance.** NHS-commissioned providers may require UK hosting, DSPT or DTAC evidence; FitXpress is hosted on AWS in the US and copy has no approved answer.
3. **Referral volume.** 76 referral invites, 41 at one franchisor; the July Slimming World franchise tier produced one PR forward.
4. **Regulatory reading.** A UK online prescriber may read any body-from-photos tool as a verification claim; Rules keep the scan to check-ins.
5. **High BMI.** Validation tops out at 210 kg; obesity services will ask.
6. **No UK reference** in weight management; proof is anonymised.
7. **Dormant or tiny accounts:** the Stourbridge clinic's website no longer resolves; several segment E accounts are one-person businesses.

## Open questions for Vadim

1. **MoreLife after the Voy acquisition (June 2026).** Voy is manually excluded for `katerina` (already outreached before 2026-09-12), and `icp-detail.md` excludes recently acquired companies. Default: send to all 36 as an operationally independent provider; the copy never mentions the deal. Hold MoreLife instead?
2. **Medicspot.** The five export people were in Katerina's 2026-09-01 send, so they are OUT. Default: re-enter only through new Apollo people (the Healthier Weight and Tonic precedent). Drop Medicspot instead? And should Doctor Care Anywhere, its new owner, become an account? Default: no.
3. **UK-company staff abroad.** Reset Health's Luca Visini (Head of European Commercial Strategy), Davide Morelli and Benedek Szulyovszky (Italy, Hungary) are OUT under this scope. Flip any of them to `katerina`? Philip Bazire is IN: PronoKal UK is a company registered in England and Wales; the four PronoKal Group staff on the Continent stay OUT for Olena's geo.
4. **The Body Clinic (Stourbridge).** The registry will flag it as covered by `olena` on name alone; Olena's is the Dutch bodyclinic.nl. Its own website no longer resolves. Default: clear the flag and send to Kate Sykes after a current-role check.
5. **Three accounts over the cap after Apollo.** `cap_per_group` stays 50. With every non-junk addition from the coordinator's search, LighterLife would be 75 (43 + 32), MoreLife 65 (36 + 29) and Reset Health 57 (26 + 31). Raise the cap for these three, or fill each to 50 by seniority (LighterLife takes 7 of its 32, MoreLife 14 of 29, Reset Health 24 of 31)? Default: fill to 50 by seniority, every export person kept.
6. **NHS data assurance.** Is there an approved answer on UK hosting, DSPT or DTAC for MoreLife, Counterweight and Reset Health? Default: nothing in copy; replies go to legal@3dlook.me.
7. **Low-fit accounts kept on "maximum contacts":** Archvale, The Body Clinic Leominster, Exchange Health, Saira Nutrition, Perspectum, Lanarkshire Medical Group and the two NHS trusts (9 people). Default: send as `partnership` or `referral`.
8. **Two health-adjacent rows put OUT:** Nicola Bonell (self-employed counsellor, formerly at MoreLife) and Dave Cumming ("Director at Counterweight", not on the register). Release either?

## Sources

- Export: `sales-nav-raw/export-1.csv` (166 rows, read with stdlib `csv` scripts) and `export-summary.md`. Alias matching checked with `scripts/outbound-pipeline.py` (`shortlist_keys`, `company_keys`, `norm_company`).
- Market and regulation: https://pulsetoday.co.uk/news/clinical-areas/gastroenterology-obesity/nhse-plans-phased-rollout-of-tirzepatide-for-weight-loss-to-avoid-profound-impact-on-gps (fetched 2026-10-06) · https://www.pulsetoday.co.uk/news/clinical-areas/gastroenterology-obesity/around-1-6-million-uk-adults-use-weight-loss-drugs-research-finds/ · https://www.itv.com/news/2025-02-03/weight-loss-jabs-patients-to-face-more-stringent-checks · https://www.chemistanddruggist.co.uk/news/regulation/weight-loss-jabs-gphc-sets-out-targeted-actions-for-pharmacies-SAVDNZ43VZAFRLRMQBRFJA2YHM/
- Reset Health: https://www.pharmaceuticalcommerce.com/view/pharmacy2u-partners-with-reset-health-glp-1-weight-management (fetched 2026-10-06) · https://www.pharmacy2u.co.uk/about/media-centre/news/pharmacy2u-and-reset-health-form-strategic-partnership-to-transform-the-delivery-of-obesity-treatment-and-care-in-the-uk · App Store "Roczen" id1617630456 (1.55, 2026-08-26)
- MoreLife: https://www.laingbuissonnews.com/healthcare-markets-content/voy-acquires-morelife-to-expand-digital-delivery-of-nhs-weight-management-services/ (2026-06-04, read via search; the page is behind a JavaScript check) · https://businesscloud.co.uk/?p=186388 · App Store "Morelife by Voy" id6759441992 (1.0.14, 2026-05-21) · https://www.more-life.co.uk · https://www.more-life.co.uk/about-us/ (1999 origin, read 2026-10-06)
- Medicspot: https://www.medicspot.co.uk/how-it-works (fetched 2026-10-06: "Since May 2026 Medicspot has been part of the Doctor Care Anywhere Group") · https://htn.co.uk/2026/05/12/doctor-care-anywhere-acquires-outcome-diagnostics-limited-and-medic-spot-limited/ · `2026-09-01-uk-erakulis-similar/closelyhq-import.csv`, `responses-raw.csv`
- Counterweight: https://services.nhslothian.scot/awmt2d/type-2-diabetes-remission-through-counterweight-plus/ · https://ukspending.com/contracts/109675 · App Store "Counterweight" id6444675809 (2.5.36, 2026-09-29; description read 2026-10-06 through the iTunes lookup API) · Companies House 11278617 officers (fetched 2026-10-06) · counterweight.org returned 429
- Habitual: https://www.tryhabitual.com/ (fetched 2026-10-06) · App Store "Habitual" id1573575516 (2.6.19, 2026-09-30)
- LighterLife: https://www.lighterlife.com/mentor-support/ · https://www.lighterlife.com/meetings/online/ · https://www.lighterlife.com/how-it-works/ · https://www.lighterlife.com/faqs/ (all read 2026-10-06 with a browser user agent; the first attempt returned 403) · https://www.weightlossresources.co.uk/diet/lighter_life_diet.htm · https://www.trustpilot.com/review/lighterlife.com?page=2 · no LighterLife app on the UK App Store (iTunes search API, country gb) or Google Play (store search, GB), both 2026-10-06
- PronoKal UK: https://www.pronokal.co.uk · https://www.pronokal.co.uk/about-pronokal · https://www.pronokal.co.uk/privacy-policy and /terms-of-business ("Protein Supplies Limited (whose trading name is PronoKal) ... registered company in England and Wales with registration number 07168388") · Companies House 07168388 officers (Dr Philip James Bazire, director since 2 January 2018; fetched 2026-10-06) · https://www.topdoctors.co.uk/doctor/philip-bazire
- LloydsPharmacy Online Doctor: https://onlinedoctor.lloydspharmacy.com/uk/weight-loss (fetched 2026-10-06) · https://en.wikipedia.org/wiki/LloydsPharmacy
- Smaller accounts: https://www.essexendocrineclinic.co.uk · https://www.worldobesity.org/news/dr-roselle-herring-awarded-scope-national-fellowship/ · https://www.spirehealthcare.com/spire-hartswood-hospital/consultants/dr-roselle-herring-c6027855 · https://www.thebodyclinicleominster.co.uk · https://www.prnewswire.co.uk/news-releases/shaping-the-future-with-the-latest-non-surgical-fat-reduction-treatments-508961091.html (Stourbridge; thebodyclinic.uk.com does not resolve) · https://perspectum.com/for-professionals/body-composition · https://www.exchangehealth.co.uk · https://sairanutrition.co.uk · https://www.archvale.co.uk
- Olena's The Body Clinic: `2026-07-21-eu-telehealth-weightloss/contacts_filtered.csv` (Netherlands and Germany) · https://www.trustpilot.com/review/bodyclinic.nl/location/heerenveen
- Live 3DLOOK assets (HTTP 200 on 2026-10-06): https://3dlook.ai/content-hub/glp-1-market/ · https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/ · 404: https://3dlook.ai/fitxpress/for-glp-1-programs/, https://3dlook.ai/fitxpress/for-telehealth/, https://3dlook.ai/content-hub/glp-1-patient-progress-record-body-data/
- Internal: `2026-07-31-uk-telehealth-digital-health/post-mortem.md`, `metrics-final.json`, `responses-summary.md` · `2026-09-27-uk-bariatric-prequal/hypothesis.md`, `responses-summary.md` · `2026-09-01-uk-erakulis-similar/responses-summary.md`, `companies.md` · `2026-10-05-latam-health-weightloss/hypothesis.md` (format and standing decisions) · `exclusions/katerina-registry.json`, `global-company-registry.json` · `icp-detail.md` §1, §5, universal exclusions, IT roles · `use-cases/fx-telehealth-weight-loss.md` · `proof-points.md` · `accuracy-formulations.md` · `compliance.md` · `scripts/outbound_pack.py` (`OWNER`, `CARD_SECTIONS`, banned-term gate) · `scripts/apollo-pull.py` (`targets`)
