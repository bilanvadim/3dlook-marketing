---
product: fitxpress
profile: nick
market: USA
created: 2026-09-29
status: approved
approved: 2026-09-29
use_case: fx-telehealth-weight-loss
cap_per_group: 50
banned_terms: [Withings, InBody, SECA, Intellihealth, Prism, Wegovy, Zepbound, Ozempic, Mounjaro, obese]
---

# Outbound Hypothesis — 2026-09-29 — US physician-led obesity medicine practices (fixed account list)

- **Campaign:** `2026-09-29-us-obesity-medicine`
- **Owner:** Nick Omelchak (`nick`, USA)
- **Company list: fixed, not researched.** Vadim pulled it himself from his Sales Navigator account list "all clinics - Comprehensive Obesity Medicine" (US): `sales-nav-raw/export-1.csv`, 120 people, 20 company names, all US. There is **no company-researcher step**. This hypothesis is written for that list, and step 2 builds `companies.csv` from the verdicts in "Company types in scope" below. The export was pulled by company, not by title, so about 40% of it is engineering, finance and staff roles.
- **ICP:** `icp-detail.md` §1 (Telehealth & GLP-1 / Weight Loss Programs: "insurance-supported obesity treatment, employer-sponsored metabolic health programs"). §5 (Bariatric / Metabolic) applies only to Ilant Health's surgical pathway.
- **Use case file:** `brand-assets/product-info/use-cases/fx-telehealth-weight-loss.md`. It already names Form Health as an example target.
- **Content asset (live, checked 2026-09-29 with `curl -sL -o /dev/null -w "%{http_code}"`):** [GLP-1 Market Growth and the Need for Better Patient Progress Tracking](https://3dlook.ai/content-hub/glp-1-market/), HTTP 200, published 2026-08-28, modified 2026-09-16. Lane-specific alternates, also HTTP 200: the [bariatric pre-qualification article](https://3dlook.ai/content-hub/bariatric-pre-qualification-mobile-3d-body-scanning/) (Ilant only), the [obesity-trial anthropometrics article](https://3dlook.ai/content-hub/clinical-trial-anthropometric-measurement-software-obesity-trials/) (knownwell research only) and the [FitXpress privacy and security FAQ](https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/) (engineering lane only). Not live, do not link: the GLP-1 Progress Record article (`/glp-1-patient-progress-record-body-data/`, 404), the telehealth documentation article (`/telehealth-documentation-ai-body-scanning/`, 404) and `/glp-1-muscle-loss-fitness-apps/` (404).
- **Registry:** none of the 20 companies has been contacted by any profile (verified by the coordinator against all registries and imports; `grep` of `exclusions/*.json` on 2026-09-29 finds none of them either). `nick`'s only other campaign is `2026-08-07-us-digital-fitness` (closed).

> **Read this first.**
> 1. **The universe is 7 real accounts and 1 borderline one.** About 66 people are sendable under the persona below. Form Health (19) and knownwell (19) are 58% of them. That concentration is built into Vadim's list and cannot be designed away, so the per-company cap here guards the persona, not the spread (see `cap_per_group` in Target buyer persona).
> 2. **One pattern runs through the list.** These practices treat body composition as part of the obesity record, and the ones with clinics measure it on in-clinic hardware, while more of their care happens on video with a connected home scale. What those home scales report is verified for one account only: Form Health's published case study describes weight flowing into its app. FlyteHealth, knownwell and Enara name a "smart scale" without saying whether it estimates body fat, and some connected scales do, by bioimpedance (BIA). The angle is therefore built on what no scale returns: waist and other circumferences (80+ body measurements), a 3D record captured with the same guided sequence each time, and a capture that runs inside the practice's own app with no device to ship. Body composition estimates from the same scan come alongside, never as a claim that the practice "only has weight".
> 3. **Nick's account accepted 39 of 245 invites (15.9%) on the last US campaign.** At that rate 66 invites yield about 10 accepted connections. This is an account-based learning campaign, not a statistical test (Success metrics).

---

## Vertical

US physician-led obesity medicine practices: ABOM-certified physicians with dietitians and care teams, prescribing anti-obesity medication alongside lifestyle care, and treating obesity as a chronic disease over months or years.

## Sub-segment

The eight accounts on Vadim's list that deliver that care at scale, in two flavours:

- **V. Virtual-first practices sold to employers and health plans:** Form Health, FlyteHealth, Ilant Health. In-network or value-based contracts, employer AOM programs, outcomes reported to the payer. Their patients get a connected home scale. Form Health's case study describes weight flowing into its app; FlyteHealth's app listing names weight tracking and an optional smart scale. Whether any of these scales also estimates body fat is not stated anywhere we found.
- **H. Hybrid or clinic-based practices:** knownwell, JumpstartMD and The Center for Medical Weight Loss (CMWL) measure body composition in clinic (sources in the verdict table). Enara Health runs "monthly body composition tests" whose setting its current site does not state. Rivas Medical Weight Loss (borderline) has no body composition offer on its site. Each also has a virtual or telehealth track.

**Size rule for this campaign (needs Vadim's OK, Open question 1):** LinkedIn staff 25+ plus evidence of $2M+ revenue (funding, clinic count or visit volume). This is a campaign-level deviation from the `icp-detail.md` universal "<50 employees" exclusion, the same kind Vadim granted on 2026-09-14 (erakulis-similar, floor 25) and 2026-09-27 (UK bariatric, floor 10). Without it, Ilant Health (41 staff, $15M Series A in June 2026), Rivas (44, 15 clinics) and CMWL (29, a national physician network) drop out. It does not amend `icp-detail.md` and does not carry to other campaigns.

## Company types in scope: verdicts for the export

Step 2 builds `companies.csv` from this table, one row per canonical company. The `group` column is what `cap_per_group` counts. Counts are people in the export and the persona-based estimate of who is sent (Target buyer persona).

| # | Export `Company_name` (rows) | Canonical company = group | Verdict | Flavour | LI staff | Website / LinkedIn | Send est. | Evidence |
|---|---|---|---|---|---|---|---|---|
| 1 | `Form Health` (34), `Form Health │ Personalized Medical Weight Loss` (1), `FORM │ Virtual obesity medicine clinic` (1) | **Form Health** | IN | V | 268 | formhealth.co / linkedin.com/company/form-health | 19 of 36 | Virtual obesity medicine, ABOM physician plus dietitian, in-network with national plans; joined Lilly Employer Connect as a program administrator (March 2026); every patient gets a connected home scale; the Withings case study describes weight flowing into the Form app and does not mention body composition (scale model not stated). No body composition offer found on its site. |
| 2 | `knownwell` (28) | **knownwell** | IN | H | 126 | knownwell.co / linkedin.com/company/knownwellhealth | 19 of 28 | Hybrid obesity medicine and primary care, virtual care in all 50 states, clinics in MA, GA, IL, TX; its first Clinical Outcomes Report (Feb 2026) leads with lean-mass results "based on SECA body composition data" (an in-clinic device); "smart scale for home use" (model and outputs not stated); runs obesity clinical trials; $25M round led by CVS Health Ventures (Oct 2025). |
| 3 | `FlyteHealth` (14), `Intellihealth` (3; same LinkedIn page, linkedin.com/company/flytehealth) | **FlyteHealth** | IN | V | 113 | flytehealth.com / linkedin.com/company/flytehealth | 10 of 17 | Early cardio-kidney-metabolic platform for employers and health plans, "backed by two separate actuarial analyses"; members get a "Withings smart scale + blood pressure cuff, when needed" and the app listing names "weight, food, and activity tracking" (scale model and body-fat output not stated); CMS Health Tech Ecosystem, Diabetes & Obesity category (general availability July 2026). Intellihealth is the pre-2024 name; copy says FlyteHealth. |
| 4 | `Ilant Health` (11) | **Ilant Health** | IN | V | 41 | ilanthealth.com / linkedin.com/company/ilant-health | 5 of 11 | Value-based "single front door" for employers and payers: behavioral therapy, medication and bariatric surgery; $15M Series A (June 2026) to scale its precision analytics engine; promises "continuous insights from connected devices". Needs the size waiver. |
| 5 | `JumpstartMD` (8), `HeyNearby` (1: Conrad Lai, JumpstartMD co-founder) | **JumpstartMD** | IN | H | 98 | jumpstartmd.com / linkedin.com/company/jumpstartmd | 7 of 9 | Cash-pay physician-led weight loss, Northern California; "body-composition tracking in clinic" on an in-clinic analyzer (InBody, per its homepage), with online visits across California. Conrad Lai's row says HeyNearby; group him under JumpstartMD. |
| 6 | `Enara Health` (6) | **Enara Health** | IN | H | 80 | enarahealth.com / linkedin.com/company/enarahealth | 3 of 6 | Platform for medical groups to launch insurance-covered obesity programs; "monthly body composition tests" (setting not stated on its current site; a 2017 Enara blog describes an InBody "in our office"); "personalized smart scale that connects to the Enara app" (outputs not stated). CMO Lydia Alexander is a past president of the Obesity Medicine Association ([Healio](https://www.healio.com/authors/lyalexander)). |
| 7 | `The Center for Medical Weight Loss (CMWL)` (4) | **CMWL** | IN | H | 29 | centerformedicalweightloss.com / linkedin.com/company/the-center-for-medical-weight-loss-cmwl- | 2 of 4 | National network program run from Tarrytown, NY (420+ physicians, 46 states per its LinkedIn); body composition reading at center visits; a telemedicine-only Virtual plan. Buyer is HQ, not a location owner. Needs the size waiver. |
| 8 | `Rivas Medical Weight Loss` (1) | **Rivas Medical Weight Loss** | IN, borderline (Open question 2) | H | 44 | rivasweightloss.com / linkedin.com/company/rivas-medical-weight-loss | 1 of 1 | 15 clinics in MD and VA plus telehealth in MD, VA and FL, provider visits every 1-4 weeks. No body composition offer on its site, and it markets "human connection, not automated apps". One invite, VP Operations. Needs the size waiver. |
| 9 | `IntelliHealth` (1: Mitchell Greenberg, President) | none | **OUT** | - | none | no company page | 0 | **Not FlyteHealth.** No LinkedIn company page, profile located in Keego Harbor, MI, single line "President at IntelliHealth". The name differs from row 3 only by one capital letter: match on the company LinkedIn URL, never on the name. |
| 10 | `Fitness RX` (1) | none | OUT | - | 6 | fitnessrx.com | 0 | D2C longevity, GLP-1 and peptide start-up; one CEO. Below any floor. |
| 11 | `StretchMed Kent Island Md` (1) | none | OUT | - | none | none | 0 | Stretching-studio owner who also owns 24/7 gyms called Fitness Rx in Maryland (unrelated to row 10). Not obesity medicine. |
| 12 | `RX Fitness Coaching LLC` (1) | none | OUT | - | none | none | 0 | Solo online fitness coach. |
| 13 | `California Trim Clinic` (1) | none | OUT | - | 1 | californiatrimclinic.com | 0 | One-person compounded-peptide and GLP-1 telemedicine clinic; the contact is a peptide sales specialist. |
| 14 | `WeightlessRx` (1) | none | OUT | - | 1 | get.weightlessrx.com | 0 | One-person GLP-1 prescription-access site; the CEO sells AI automation consulting. |
| 15 | `Onyx Weight Loss Clinic` (1) | none | OUT | - | 1 | onyxweightloss.com | 0 | One-person clinic page; the contact is an administrative manager and coach. |
| 16 | `Olli Health` (1) | none | OUT | - | 27 | ollihomehealth.ai | 0 | Home-health coding and OASIS review service, not obesity care; the contact is a software engineer (ex-Form Health). |
| 17 | `HeyNearby` as a company | none | OUT (company) | - | 1 | heynearby.com | 0 | One-person software company. Its only row (Conrad Lai) moves to JumpstartMD, row 5. |

**Totals:** 8 groups in scope (7 plus borderline Rivas), about 66 people to send (48 in wave 1, 18 in wave 2), 46 people out by persona, 8 people out with their company (rows 9-16).

## Use case (1 sentence)

On video visits and between clinic visits, a physician-led obesity medicine practice sends a two-photo scan inside its own patient app and receives 80+ body measurements such as waist circumference, along with body composition estimates (under 45 seconds from the photos to structured results), giving the care team a record beyond scale weight.

## Why this is plausible (evidence)

1. **Employers now ask what AOM spend buys, and route coverage through programs like these.** The Business Group on Health 2026 GLP-1 survey of 105 self-funded employers found nearly 8 in 10 saying GLP-1s raise their health costs, and only 72% of employers that cover them for weight management likely to continue in 2027. Their guardrails include "validating clinical eligibility with objective biometric data" and "requiring participation in a weight management program". More than half expect clinical benefits but have not yet seen them in claims ([MedCity News](https://medcitynews.com/2026/05/glp1s-employers-coverage/), [Healthcare Dive](https://www.healthcaredive.com/news/glp-1s-weight-loss-employer-healthcare-cost-increase-business-group-on-health/819384/), [BGH release](https://www.businessgrouphealth.org/newsroom/news-and-press-releases/press-releases/2026-glp-1-survey)). The accounts on this list are those programs: Form Health and Ilant Health both work through Lilly Employer Connect ([Form](https://www.formhealth.co/press/form-health-joins-the-lilly-employer-connect-platform), [Ilant](https://www.businesswire.com/news/home/20251121143297/en/Ilant-Health-Enhances-Comprehensive-Cardiometabolic-Care-with-Direct-Contracting-for-Obesity-Management-Medicine-for-Employers)), and FlyteHealth sells on actuarial analyses. Payer renewals run on a documented baseline: the FEP Blue weight-loss medication policy 5.99.027 (effective 2026-01-01) renews only after at least 5% loss of baseline body weight plus program participation, and its change log records the same 5% continuation rule for Wegovy and Zepbound ([FEP Blue](https://www.fepblue.org/-/media/PDFs/Medical-Policies/2026/January/Pharmacy-Policies/Remove-and-Replace/5_99_027-Weight-Loss-Medications.pdf)). Context for Nick, never numbers in copy.
2. **Lean mass is a clinical priority and already a competitive claim for these practices.** The 2025 joint advisory of the American College of Lifestyle Medicine, the American Society for Nutrition, the Obesity Medicine Association and The Obesity Society lists body composition assessment among the priorities in GLP-1 care and names loss of muscle and bone mass as a limitation of the drugs ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12264624/)). knownwell's first Clinical Outcomes Report (2026-02-24) leads with "50% lower lean mass loss compared to published GLP-1 trial averages, based on SECA body composition data" ([Newswise](https://www.newswise.com/articles/knownwell-demonstrates-improved-obesity-outcomes-and-long-term-durability-in-first-clinical-outcomes-report)). JumpstartMD sells "InBody® body-composition tracking in clinic" (homepage, fetched 2026-09-29). Enara runs "monthly body composition tests" ([Enara](https://www.enarahealth.com/for-patients/journey)); its current site does not say where. CMWL takes a body composition reading at center visits ([CMWL](https://vcc.cmwl.com/how-it-works/what-to-expect/)).
3. **Care is moving to video, and the home device is a scale, which returns no body measurements.** knownwell extended virtual care to all 50 states ([MedCity News](https://medcitynews.com/2025/10/knownwell-obesity-medicine/)); JumpstartMD offers online visits across California; CMWL runs a telemedicine-only Virtual plan ([CMWL Direct](https://cmwldirect.com/pages/virtual-np-program-t-c)). What each home scale reports is verified only in part:
   - Form Health: the case study describes weight flowing from a connected scale into the Form app and does not mention body composition ([Withings case study](https://www.withings.com/us/en/health-solutions/insight-hub/improving-patient-onboarding-experience-and-reducing-scale-support-time-for-virtual-medical-weight-loss-program), via search; the page blocks scripted fetch).
   - FlyteHealth: "Withings smart scale + blood pressure cuff, when needed" and an app "to track weight, labs, and progress" ([FlyteHealth patients page](https://www.flytehealth.com/patients/), fetched 2026-09-29); the App Store listing names "weight, food, and activity tracking" and "optional remote monitoring devices (smart scale and blood pressure cuff)". Model and body-fat output not stated.
   - knownwell: "Smart scale for home use to keep track of progress" (homepage, fetched 2026-09-29). Model and outputs not stated.
   - Enara: a "personalized smart scale that connects to the Enara app" ([Enara](https://www.enarahealth.com/for-patients/journey)). Outputs not stated.

   Some connected scales estimate body fat by BIA. Withings' cellular Body Pro 2, the scale family behind the only evaluation question on Nick's last campaign, measures fat mass and muscle mass by multifrequency BIA ([Withings Body Pro](https://www.withings.com/us/en/health-solutions/body-pro), via search). The campaign therefore does not claim that the virtual record is weight only. What no scale returns is circumferences, and the Lancet Diabetes & Endocrinology Commission on clinical obesity (January 2025) recommends confirming excess adiposity with at least one body-size measurement (waist circumference, waist-to-hip ratio or waist-to-height ratio) in addition to BMI ([The Lancet Diabetes & Endocrinology](https://www.thelancet.com/journals/landia/article/PIIS2213-8587(24)00316-4/fulltext)). A home scale also does not replace the in-clinic body-composition step the hybrid practices sell.
4. **FitXpress fills that gap, with stated limits.** What it adds over any scale is the 80+ body measurements (waist included), a 3D model and a capture guided the same way each time, inside the practice's own app with no device to ship; its body composition estimates come from the same scan. From `proof-points.md`: 2 photos (front and side), under 45 seconds from the photos to structured results, 80+ body measurements, body composition outputs (BMI, BMR, fat %, lean mass, fat mass), typical scan-to-scan differences under 1 cm for most evaluated measurements, white-label API and SDK. The live GLP-1 hub describes this workflow in its own words: "A hybrid clinic may combine remote records with measurements collected during office visits" and "Employer-supported programs may require aggregate reporting". Honest limits: body composition values are estimates, not an in-clinic analyzer or DXA; there is no head-to-head body-composition study against BIA or DXA in `proof-points.md`; the validation population stops at 210 kg; and there is no obesity-medicine reference customer. The nearest proof is an anonymised weight-management platform that ran 34,000 scans in 2025.

## What Nick's last US campaign teaches this one

From `2026-08-07-us-digital-fitness/post-mortem.md` and `responses-summary.md`:

- **Acceptance was the loss, not the copy:** 39/245 (15.9%) accepted, then 6/39 (15.4%) replied, on par with UK and Israel. Invites went without a note. This list is too small to fix that; Open question 7 asks whether the profile audit (post-mortem H1) happened.
- **Cold `technical-integration` got 0 replies from 60 invites, and the WEAK tier (96/248) produced 0 interested.** 22 of those 60 were already PASS-level (post-mortem, "22 PASS + 38 WEAK"), so the zero covers engineering leaders too, not only engineers below director. Here engineers below director level are out, and engineering leaders go in wave 2 only; whether lane D should go cold at all is Open question 9.
- **The one interested reply came from the owner of the KPI in the title** (Chief Subscription & Content Officer, retention angle). Here that means the owners of practice operations, product and clinical outcomes.
- **The one evaluation question came from a clinical-research role on message 2 with proof points** (Calibrate, asking for a comparison with a smart scale). That supports the knownwell research lane and a proof point in every message 2, and it predicts the first objection here: "how does this compare with our in-clinic analyzer or home scale?"
- **Two "I no longer work there" replies.** A job-change check runs before import.
- **Mixing ICP segments made the averages unreadable.** This campaign stays in §1; the knownwell research lane is the one declared exception and is reported separately.

## Target buyer persona

**Who buys:** the owners of the program's clinical model, its patient app and its practice operations. They decide what is measured on a virtual visit and what the practice reports to employers and health plans. Titles below are as they appear in the export. Lanes are defined in "Message angle".

**P1, wave 1 (25 people):**
- Founders and CEOs: knownwell CEO & Founder; JumpstartMD CEO; Enara Co-Founder & CEO; CMWL CEO & Co-Founder.
- Chief Medical Officers and national medical leadership: Form Health CMO and National Medical Director; knownwell CMO; FlyteHealth CMO (row under `Intellihealth`, title "Chief Medical Officer - Flyte") and Senior Medical Director, Care Management and Clinical Operations; Ilant CMO; JumpstartMD Co-Founder & CMO; Enara CMO.
- Product owners: Form Health Chief Product Officer and Director of Product; FlyteHealth Chief Product and Technology Officer and Senior Director of Product Management; Ilant Senior Product Manager (the only product lead in the export at a 41-person company); JumpstartMD Director of Product Management; CMWL Chief Product and Operations Officer.
- Operations owners: Form Health VP, Practice Operations; knownwell SVP, Practice Operations; FlyteHealth Chief Clinical Operations Officer and VP of Patient Operations; Ilant VP of Strategic Operations; JumpstartMD Director of Clinical Operations.

**P2, wave 1 (23 people):**
- Product managers: Form Health Lead PM, Group PM, Senior PM, Senior PM Data, Reporting & Analytics (owns outcomes reporting); knownwell Senior PM and Senior PM [Automations]; Enara Product Manager (a clinical PM and dietitian).
- Clinical leaders: Form Health Clinical Lead and Regional Medical Director; knownwell NYC Market Physician Lead and Market Development Lead Physician; FlyteHealth Medical Director and Senior Director of Program Management.
- Nutrition leaders, lean-mass angle (they own the protein and resistance-training plan the advisory calls for): Form Health Director of Clinical Nutrition; knownwell Clinical Director, Nutrition Services; Ilant Director of Nutrition.
- Operations, analytics, patient services: Form Health Chief Administrative Officer and Director, Patient Services; knownwell Director of Operations and Head of Analytics; Rivas VP Operations.
- Research, lane C: knownwell VP of Clinical Research and Head of Research Operations.

**P3, wave 2, sent at least 7 days after wave 1 at the same company (18 people):**
- Practice and operations managers: Form Health Regional Practice Manager, Senior Manager Provider Operations, Manager, Enrollment; knownwell Director, Business Operations, Clinical Operations Lead (2), Practice Manager, Medical Practice Manager; FlyteHealth Patient Operations Manager; JumpstartMD Director of Systems Operations and Regional Operations Manager.
- Research, lane C: knownwell Clinical Trial Manager.
- Engineering leaders, lane D `technical-integration`: knownwell CTO; Form Health VP of Engineering and Director of Engineering; FlyteHealth Senior Director of Engineering; Ilant Director, Backend Engineering.
- Founder referral, lane E: Conrad Lai (JumpstartMD co-founder, export row `HeyNearby`).

**Where engineers stand.** The `icp-detail.md` IT section makes CTO / VP Engineering PASS P3 `technical-integration` and senior engineers WEAK rather than FAIL. This campaign applies the P3 half, **promotes Director / Senior Director of Engineering and Director, Backend Engineering from WEAK (the IT section lists "Director of Engineering" as WEAK + `technical-integration`) to P3**, and overrides the WEAK half for everyone below director, on `nick`'s own evidence (0 replies from 60 cold `technical-integration` invites, 22 of them PASS-level; 0 interested from 96 WEAK invites): **CTO, VP Engineering and Director / Senior Director of Engineering go in wave 2; senior, lead and staff software engineers, data engineers, data scientists and data analysts are FAIL for the cold send** and are listed as reserve pool R1 for Vadim. The Chief Product and Technology Officer at FlyteHealth is a product owner and stays P1.

**KPIs they care about:** what the practice can show an employer or health plan beyond pounds lost (lean mass, waist, durability); consistency of the record between clinic and video visits; retention in months 2-3 of treatment; renewal documentation for medication coverage; clinician time per follow-up; for hybrid clinics, keeping virtual patients inside the same outcomes dataset as clinic patients.

**Likely objections and the honest answer:**
- "We already measure body composition in clinic." The scan is for the visits that happen on video and the weeks between clinic visits. The in-clinic analyzer stays the method of record where the protocol requires it.
- "Our patients already have a smart scale" or "How does it compare with our analyzer, DXA or a smart scale?" A scale, BIA or not, returns no circumferences; the scan returns 80+ body measurements, waist included, and a 3D model, inside the practice's app with no device to ship. For body composition it is a different method. We publish accuracy against expert manual measurement (96-97%, typical error 1.5-2.0 cm) and scan-to-scan repeatability (under 1 cm for most measurements). There is no head-to-head body-composition study against BIA or DXA to quote; a pilot compares against their own clinic readings in hybrid patients. Do not improvise numbers.
- "Our patients include people above 210 kg, or with limited mobility." Real. Performance outside the 38-210 kg validation population has not been characterized; accessibility and fallback are pilot questions.
- "We practise weight-inclusive care" (knownwell). The practice's app decides what patients see; the scan adds context beyond the scale for the care team.
- "HIPAA? FDA?" HIPAA: the US compliance line from `compliance.md` §9. FDA, verbatim from the live trust FAQ: "FitXpress is not cleared, authorized, or approved by the U.S. Food and Drug Administration (FDA). 3DLOOK makes no representation as to whether FDA clearance, authorization, or approval is required for any particular customer's use case." The customer assesses its complete integrated workflow. Medical-device status, verbatim and with its scope: "An independent regulatory assessment concluded that FitXpress does not meet the definition of a medical device under the UK Medical Devices Regulations 2002 (UK MDR) or the EU Medical Devices Regulation (EU MDR)." The short form "FitXpress is not a medical device." rests on that UK/EU assessment. It is never the answer to an FDA question and never implies a US device determination.
- "Our app roadmap is full." API and SDK into their existing app; 2-4 weeks for a typical basic integration (a generic figure, never a promise).

**Not the buyer (FAIL for the cold send; the reserve pools are listed here for Vadim to decide at the validate checkpoint, not after):**
- **R1 engineering and data below director (14):** senior, lead and staff software engineers, Senior Technical Manager, data engineers, data scientists, data analysts, clinical systems specialists.
- **R2 frontline clinicians and behavioral health (7):** APNs, PAs, staff obesity-medicine physicians, clinical specialists, directors of behavioral health, Ilant's bariatric-surgeon clinical consultant (an advisor, not staff).
- **R3 finance, revenue cycle and credentialing (10):** CFOs (including CMWL's fractional CFO), SVP / VP Finance, accounting, FP&A, Head of Revenue Cycle Management, payer credentialing.
- **R4 other (15):** IT and security leads, EHR administrator, partnerships and consultant-relations sales roles, real estate, growth operations, staff services, operations specialists and team leads, Manager Business Operations (Form Health), JumpstartMD's wellness program specialist and the untitled row, CMWL's location owner.

### Target buyer persona: Sales Navigator pull for step 3

**Pull by title filter inside the approved company list, never by company alone.** The export Vadim already pulled is the list for this campaign. This block is for an optional top-up pull inside the 8 in-scope accounts only (Open question 4): the export has no CEO or founder for Form Health, FlyteHealth or Ilant Health, and no COO anywhere.

```titles
Chief Executive Officer
Founder
Co-Founder
President
Chief Operating Officer
Chief Medical Officer
Chief Clinical Officer
Chief Clinical Operations Officer
Chief Product Officer
Chief Product and Technology Officer
Chief Product and Operations Officer
National Medical Director
Medical Director
Vice President of Clinical Operations
Vice President, Practice Operations
Vice President of Patient Operations
Vice President of Operations
Head of Clinical Operations
Director of Clinical Operations
Vice President of Product
Head of Product
Director of Product
Director of Product Management
Group Product Manager
Head of Analytics
Head of Outcomes
Director of Clinical Nutrition
Director of Nutrition
Vice President of Clinical Research
Head of Research Operations
Chief Technology Officer
Vice President of Engineering
```

**`cap_per_group: 20`, and why.** Under this persona Form Health sends 19 and knownwell 19; every other group sends 10 or fewer. 20 fits both big accounts with one seat to spare. It deliberately does not fit the reserve pools: taking all of R1-R4 would put Form Health at 36 (its whole export) and knownwell at 28. On 2026-09-28 Vadim took every pool offered and the erakulis cap moved 5 → 25 → 30 → 35 in one day. The recommendation is not to take R1-R4 here (reason: `nick`'s 0/60 technical and 0-interested WEAK results). **If you do intend to take them, set the cap to 36 once, at the validate checkpoint, instead of stepping it up.**

## Message angle: lanes and the content asset

Every person gets exactly one lane. Numbers in copy come only from `proof-points.md` (see Rules). The company facts below may be used as the "only this company" line, **without their numbers**.

- **Lane A `virtual-body-composition`** (knownwell clinical, operations and product people; JumpstartMD; CMWL; Enara Health; Rivas). knownwell, JumpstartMD and CMWL measure body composition in clinic; video visits and the weeks between clinic visits depend on what the patient has at home. From the patient's phone and inside the practice's own app, FitXpress adds waist and other circumferences (80+ body measurements) that no scale returns, along with body composition estimates from the same scan, keeping virtual patients in one structured record. Enara: its body composition tests are monthly, their setting is not stated and its smart scale's outputs are unknown; lead with circumferences and the in-app capture. Rivas: no body composition offer; lead with a structured, timestamped record on telehealth visits, as a tool for its clinicians.
- **Lane B `outcomes-beyond-weight`** (Form Health, FlyteHealth, Ilant Health). Employers and health plans now ask what AOM spend buys. Each practice has a connected home scale, and whether it estimates body fat is verified for none of them. The lead is what no scale gives: waist and other circumferences between video visits, a 3D record captured with the same guided sequence each time, and a capture inside the practice's own app with no device to ship or support. Lean mass and fat mass estimates come from the same scan as a further line.
- **Lane C `clinical-research`** (knownwell VP of Clinical Research, Head of Research Operations, Clinical Trial Manager). Standardized, timestamped anthropometrics captured remotely in obesity and metabolic trials, the same workflow as the obesity-trial article.
- **Lane D `technical-integration`** (wave 2: knownwell CTO, Form Health VP and Director of Engineering, FlyteHealth Senior Director of Engineering, Ilant Director of Backend Engineering). White-label API and SDK inside their existing app, photos deleted after processing or within 30 days, 2-4 weeks for a typical basic integration (generic, never a promise). Tone: technical, no marketing.
- **Lane E `founder-referral`** (wave 2: Conrad Lai). A short ask for who owns JumpstartMD's patient app and virtual visits; no pitch; calendar link optional.

**Company facts the copy may use (no numbers, no device or drug brands):**
- Form Health: every patient gets a connected home scale whose readings flow into the Form app; joined Lilly Employer Connect as a program administrator; added diabetes care into one cardiometabolic program for employers; in-network with national health plans.
- knownwell: its first Clinical Outcomes Report leads with lean-mass results from in-clinic body composition data; hybrid care with virtual care nationwide; a smart scale for home use; weight-inclusive care; runs obesity clinical trials.
- FlyteHealth: early cardio-kidney-metabolic care for employers and health plans; outcomes backed by two separate actuarial analyses; members get a smart scale and a BP cuff when needed; selected for the CMS Health Tech Ecosystem, Diabetes & Obesity category.
- Ilant Health: a single front door to behavioral therapy, medication and surgery for employers and payers; a new Series A to scale its precision analytics engine; "continuous insights from connected devices".
- JumpstartMD: body-composition tracking in clinic, with online visits across California; physician-led and physician-referred.
- Enara Health: monthly body composition tests and a smart scale that syncs to the Enara app; a platform that lets medical groups launch insurance-covered obesity programs.
- CMWL: a body composition reading at center visits; a telemedicine-only Virtual plan delivered by network providers.
- Rivas: clinics in Maryland and Virginia plus telehealth; its promise is human care, not automated apps: pitch the scan as a tool for its clinicians, never as an app that replaces them.

**Content asset in message 2 (one article link per message 2, plus the calendar link):**
- Lanes A and B: the GLP-1 hub, https://3dlook.ai/content-hub/glp-1-market/ ("Why Scale Weight Alone Provides an Incomplete Progress Record", "What Scalable GLP-1 Progress Tracking Requires"). Frame it as "we wrote up what a progress record beyond scale weight needs, and where scanning does not help".
- Ilant Health CMO only, when the hook is its surgical pathway: https://3dlook.ai/content-hub/bariatric-pre-qualification-mobile-3d-body-scanning/
- Lane C: https://3dlook.ai/content-hub/clinical-trial-anthropometric-measurement-software-obesity-trials/
- Lane D: https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/
- Lane E: no article.

## Rules for steps 3-5

- **Sender and format:** Nick, first name only as the last line, English. Connection request without a note. Message 1 ≤ 600 characters, message 2 ≤ 550 with Nick's calendar link as plain text. Wave 2 (P3) goes at least 7 days after wave 1 at the same company.
- **No 3DLOOK client is named anywhere in cold copy:** Yazen, UK Meds, Healthyr and every other client. The only anonymised proof allowed: "one weight-management platform ran 34,000 scans in 2025", with no client name and no geography. The UK Meds 7,500-scan fact is not used.
- **Numbers only from `proof-points.md`.** Allowed: two photos (front and side); "under 45 seconds from the photos to structured results"; 80+ body measurements; body composition estimates (body fat %, lean mass, fat mass) with BMI and BMR as calculated metrics; "96-97% accuracy against expert manual measurement" or the full sentence from `accuracy-formulations.md` §1.1; repeatability only as "For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm."; the 34,000-scan line; lane D only, 2-4 weeks for a typical basic integration. **No other number**, including the prospect's own published results (knownwell's lean-mass percentage, clinic counts, funding amounts), market statistics and payer thresholds.
- **Compliance wording only as the live trust FAQ allows it (`compliance.md`).** One compliance line per sequence, in message 2, the US variant verbatim: "We support HIPAA-governed deployments under a BAA, encrypt data in transit and at rest, and delete photos after processing or within 30 days." Cold copy does not raise regulatory status. If a medical-device or FDA question has to be touched, use only the live trust FAQ sentences, verbatim: "FitXpress is not cleared, authorized, or approved by the U.S. Food and Drug Administration (FDA). 3DLOOK makes no representation as to whether FDA clearance, authorization, or approval is required for any particular customer's use case." and, for device status, "An independent regulatory assessment concluded that FitXpress does not meet the definition of a medical device under the UK Medical Devices Regulations 2002 (UK MDR) or the EU Medical Devices Regulation (EU MDR)." The short form "FitXpress is not a medical device." rests on that UK/EU assessment: it never stands alone as an answer about the FDA. **Hard fails:** "HIPAA compliant", "HIPAA-compliant", "HIPAA certified", "SOC 2 certified", "SOC 2 compliant", anything FDA-cleared or FDA-approved, "processed, not stored", "no personal data", "no personal identifiers".
- **What the scan does, and does not do.** It returns estimates and measurements for the care team. It does not diagnose, decide eligibility, approve prior authorization, preserve lean mass or improve outcomes by itself. Say "the practice compares scans it selects" or "scan-to-scan comparison", never "tracks each patient". Say "alongside", "between clinic visits", "on video visits"; never "replace your analyzer" or "replace the scale".
- **Never state or imply what a prospect's home scale measures.** No "weight only", "just weight", "your scale only tells you pounds". Some home scales estimate body fat. The claim is what no scale returns: waist and other circumferences (80+ body measurements) and a 3D model, captured inside the practice's own app.
- **No brands other than the prospect's own.** Competitors are never named (Prism Labs, Bodygram, Size Stream). Device brands the prospects use and drug brands are banned for this campaign (`banned_terms`). Say "your in-clinic body composition", "the home scale", "GLP-1" or "anti-obesity medication".
- **Person-first, non-stigmatizing language for this audience:** "patients with obesity", "people living with obesity". Never "obese" (banned), no before-and-after framing, no "burn fat", no body-shaming. knownwell brands itself on weight-inclusive care.
- **Word traps this vertical invites:** never "comprehensive" (a hard-banned word, even though the account list is named "Comprehensive Obesity Medicine"; say "physician-led obesity medicine"); never "objective" about our data (say "standardized", "timestamped", "structured", "repeatable"), even though the employer survey says "objective biometric data".
- **No pricing and no trial terms** anywhere in the sequence. A price or trial question goes to the call.
- **Company names in copy:** Form Health, knownwell (lowercase, as they write it), FlyteHealth (never Intellihealth, which is banned), Ilant Health, JumpstartMD, Enara, CMWL or The Center for Medical Weight Loss, Rivas.
- **Message 1 gate.** Every message 1 carries at least one product specific from `proof-points.md` and one line that could only have been written to that company; each pair of messages cites at least one number. The referral lane (E) is exempt from the product specific.

## Anti-cases (where it does NOT work)

- **Companies in the export that are out, by name:** IntelliHealth (Mitchell Greenberg, Keego Harbor, MI; **not FlyteHealth**, match on the company LinkedIn URL, never the name), Fitness RX, StretchMed Kent Island Md, RX Fitness Coaching LLC, California Trim Clinic, WeightlessRx, Onyx Weight Loss Clinic, Olli Health, and HeyNearby as a company (its one person moves to JumpstartMD). Reasons in the verdict table.
- **Structural anti-cases for this list:**
  - One-person or sub-25-staff clinics and D2C GLP-1 or compounded-peptide prescribing sites: no product team, no integration capacity, no payer reporting.
  - Fitness studios, gyms and coaches: not obesity medicine (ICP §8 is a different campaign).
  - Any account found to already run a phone-camera body scan or to have signed a scanning vendor: displacement, flag for Vadim, do not send the standard copy.
  - Existing 3DLOOK customers (`existing_customer_excluded`): none on this list; the registry check still runs.
  - Mergers: an account announcing an acquisition or merger before send is paused.
- **People-level anti-cases:** the "Not the buyer" list and reserve pools R1-R4 in Target buyer persona. Behavioral health leaders and frontline clinicians are out because they neither own the record nor the app. Finance and revenue-cycle roles are out because the documentation angle stays context, not the pitch (FitXpress does not decide payer acceptance).

## Validation criteria (Step 2 will check)

There is no company research. Step 2 is: build `companies.csv` from the verdict table, then validate people against the persona.

- **Companies.** 8 rows (7 if Vadim drops Rivas), canonical names and groups as in the table: the three Form Health spellings → Form Health; `Intellihealth` rows with `linkedin.com/company/flytehealth` → FlyteHealth; `IntelliHealth` without a company URL → out; Conrad Lai (`HeyNearby`) → JumpstartMD. `outbound-registry.py check --profile nick` runs on the export anyway and must come back clean.
- **Size waiver.** Ilant Health, CMWL and Rivas stay in only if Vadim approves the 25+ LinkedIn-staff floor (Open question 1).
- **People.** At least 40 contacts reach PASS (P1 + P2) across at least 6 of the 8 groups. P3 goes in wave 2. Reserve pools R1-R4 go out only if Vadim takes them by name at the validate checkpoint. A job-change check runs on every contact before import.
- **Message 1 gate.** Every message 1 carries at least one product specific from `proof-points.md` and one line that could only have been written to that company; each pair of messages cites at least one number. Zero client names, zero pricing, zero `banned_terms`. Kept as a failure, not a note: `2026-07-21` sent 307 message 1 texts with no specific and drew 1 reply on 67 sends.
- **Proof in product-info.** Use-case file and live article: yes. Reference customer in obesity medicine: none; the adjacent anonymised weight-management proof (34,000 scans) is accepted, not hidden.

## Success metrics for this campaign

Denominators as in `metrics-final.json` (Closely event counters). Expected volume: about 66 invites.

| Metric | Target | Floor | Basis |
|---|---|---|---|
| Contacts at PASS (P1 + P2) | 45 | 40 | persona estimate 48 |
| Connection acceptance rate | 25% | 16% | `nick` on 08-07: 39/245 = 15.9% |
| Replies per accepted person | 15% | 10% | `nick` 08-07: 6/39 = 15.4% |
| Positive replies (interested + question) | 3 | 1 | |
| Accounts with at least one reply | 3 of 8 | 2 | account-based campaign |
| Discovery calls booked | 2, at different accounts | 1 | |
| Pilots / POCs agreed within 8 weeks | 1 | 0 (learning campaign) | |

**Falsified if:** 3 or more P1/P2 replies say body composition on virtual visits is not a priority, or that the home scale plus clinic visits is enough; or discovery calls stall on the comparison with in-clinic analyzers twice with no pilot path. **Inconclusive, and the post-mortem says so, if fewer than 20 people accept:** at `nick`'s rate that is the likely outcome, and a zero-reply result on so few acceptances does not reject the segment.

## Risks

1. **Acceptance on `nick`.** 15.9% last time. Invites are few, so every missed acceptance is a missed account.
2. **Comparison with hardware they already own.** These practices bought in-clinic analyzers and ship scales, some of which may already estimate body fat; for them the body composition estimates are not new, and the circumferences carry the pitch. The first technical question will be agreement with their analyzer or DXA, and we have no study to quote.
3. **Population.** Patients with severe obesity may sit above the 38-210 kg validation range, and standing capture can be hard with limited mobility.
4. **Tone.** Obesity medicine is sensitive to stigmatizing language; one careless line to knownwell or to Enara's CMO (a past president of the Obesity Medicine Association, per [Healio](https://www.healio.com/authors/lyalexander)) ends the thread.
5. **Budgets.** Employer retreat from GLP-1 coverage could shrink these programs before a pilot starts.
6. **Competitor.** Prism Labs markets muscle-preservation body composition to GLP-1 programs; an account may already be evaluating it (displacement anti-case).

## Open questions for Vadim

1. **Size floor 25+ LinkedIn staff for this campaign only**, keeping Ilant Health (41), CMWL (29) and Rivas (44)? Without it the campaign is 5 accounts.
2. **Rivas Medical Weight Loss:** keep (one invite, hybrid telehealth angle) or drop (no body composition offer, brand is "not automated apps")?
3. **knownwell research lane (C):** keep the three research people with the obesity-trial angle inside this §1 campaign, reported separately? Recommended: the only evaluation question on `nick`'s last campaign came from a clinical-research role.
4. **Top-up Sales Navigator pull by title** (the `titles` block) inside the 8 accounts, to add the missing CEOs and founders of Form Health, FlyteHealth and Ilant Health and any COO? Small, and these are the likeliest P1 contacts.
5. **Cap:** 20 as proposed, or 36 now if you already know you will take reserve pools R1-R4?
6. **Second anonymised proof:** is "112,100 scans in 2025 across all 3DLOOK customers" (cleared for `olena` on 2026-09-14) cleared here too? Until then, only the 34,000-scan line.
7. **Nick's profile:** did the post-mortem's H1 audit (connections, headline, pending invites) happen? If not, this list will likely produce about 10 accepted connections.
8. **Cap against the post-mortem rule.** Nick's 08-07 post-mortem (recommendation 2) set at most 15 invites per company and at least 10 companies. This list has at most 8 companies, and `cap_per_group: 20` puts 38 of about 66 invites (58%) into Form Health and knownwell, the pattern that post-mortem blamed (48% into two accounts). Keep 20, or cap at 15, which drops 4 wave-2 (P3) people at each of the two and still leaves them at 30 of 58 (52%)? The persona and cap are unchanged in this draft; this is your call at the checkpoint.
9. **Engineering leaders (lane D).** Director / Senior Director of Engineering and Director, Backend Engineering are WEAK in the `icp-detail.md` IT section and are promoted to P3 here. On 08-07, 22 of the 60 zero-reply `technical-integration` invites were already PASS-level, so the same evidence counts against sending lane D cold to leaders. Keep lane D as a cold wave 2 (5 people), send it only after a product or clinical person at the same company replies, or drop it?

## Sources

- Live 3DLOOK assets (HTTP 200 on 2026-09-29): https://3dlook.ai/content-hub/glp-1-market/ · https://3dlook.ai/content-hub/bariatric-pre-qualification-mobile-3d-body-scanning/ · https://3dlook.ai/content-hub/clinical-trial-anthropometric-measurement-software-obesity-trials/ · https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/
- Business Group on Health 2026 GLP-1 survey: https://www.businessgrouphealth.org/newsroom/news-and-press-releases/press-releases/2026-glp-1-survey · https://medcitynews.com/2026/05/glp1s-employers-coverage/ · https://www.healthcaredive.com/news/glp-1s-weight-loss-employer-healthcare-cost-increase-business-group-on-health/819384/
- FEP Blue policy 5.99.027, Weight Loss Medications (effective 2026-01-01): https://www.fepblue.org/-/media/PDFs/Medical-Policies/2026/January/Pharmacy-Policies/Remove-and-Replace/5_99_027-Weight-Loss-Medications.pdf
- Joint advisory, Nutritional priorities to support GLP-1 therapy for obesity (ACLM, ASN, OMA, TOS, 2025): https://pmc.ncbi.nlm.nih.gov/articles/PMC12264624/
- Form Health: https://www.formhealth.co/press/form-health-joins-the-lilly-employer-connect-platform · https://www.formhealth.co/press/form-health-launches-cardiometabolic-solution · https://www.withings.com/us/en/health-solutions/insight-hub/improving-patient-onboarding-experience-and-reducing-scale-support-time-for-virtual-medical-weight-loss-program
- knownwell: https://www.newswise.com/articles/knownwell-demonstrates-improved-obesity-outcomes-and-long-term-durability-in-first-clinical-outcomes-report · https://medcitynews.com/2025/10/knownwell-obesity-medicine/ · https://www.knownwell.co/
- FlyteHealth: https://www.prnewswire.com/news-releases/intellihealth-rebrands-as-flytehealth-to-reflect-focus-on-delivery-of-cost-effective-care-for-obesity-and-related-conditions-302191261.html · https://www.prnewswire.com/news-releases/flytehealth-achieves-general-availability-in-the-cms-health-technology-ecosystem-recognized-at-one-year-anniversary-event-in-washington-dc-302836748.html · https://www.flytehealth.com/patients/
- Ilant Health: https://www.businesswire.com/news/home/20260602971156/en/Ilant-Health-Raises-$15M-to-Replace-Fragmented-Obesity-Care-With-AI-supported-Precision-Care · https://www.businesswire.com/news/home/20251121143297/en/Ilant-Health-Enhances-Comprehensive-Cardiometabolic-Care-with-Direct-Contracting-for-Obesity-Management-Medicine-for-Employers · https://www.ilanthealth.com/
- JumpstartMD: https://jumpstartmd.com/ · Enara Health: https://www.enarahealth.com/for-patients/journey · CMWL: https://vcc.cmwl.com/how-it-works/what-to-expect/ · https://cmwldirect.com/pages/virtual-np-program-t-c · Rivas: https://rivasweightloss.com/
- IntelliHealth (Mitchell Greenberg): https://www.linkedin.com/in/mitchell-greenberg-03279810
- Prism Labs GLP-1 positioning: https://www.prismlabs.tech/solutions/weight-loss-glp-1-programs
- Home scales and circumferences: https://www.flytehealth.com/patients/ · FlyteHealth App Store listing (id1585026163, via the iTunes lookup API) · https://www.withings.com/us/en/health-solutions/body-pro (Body Pro 2 BIA, via search) · https://www.thelancet.com/journals/landia/article/PIIS2213-8587(24)00316-4/fulltext · https://enarahealth.com/putting-body-composition-to-the-test/ (2017, InBody "in our office") · https://www.healio.com/authors/lyalexander
- Ilant Series A total funding is not used: only the $15M Series A is cited.
- Internal: `sales-nav-raw/export-1.csv` (summarised with a stdlib `csv` script, not read whole) · `2026-08-07-us-digital-fitness/{post-mortem.md,responses-summary.md}` · `icp-detail.md` §1, §5, IT & Technical Roles · `use-cases/fx-telehealth-weight-loss.md` · `proof-points.md` · `accuracy-formulations.md` · `messaging.md` · `compliance.md`

## Approval note 2026-09-29

Approved to run on Vadim's instruction of 2026-09-29 («для цього списку ще нічого не запускали, треба на основі нього зробити гіпотезу і всі інші кроки»), after opus QC 15/20 and the six QC fixes. This is approval to run, not a decision on the Open questions: the size floor, Rivas, the cap and the engineering lane are Vadim's decisions at the step-4 (validate) checkpoint, and none of them is taken here.

## Vadim's decisions 2026-09-29 (step-4 checkpoint)

Answers to the Open questions and to the validation report, in Vadim's words where quoted. These override anything above that says otherwise.

1. **Size floor: removed for good.** «беремо всіх. скасуй це правило взагалі». The "<50 employees" universal exclusion is deleted from `icp-detail.md`; Ilant Health, CMWL and Rivas are in scope with no waiver. Segment revenue thresholds still apply.
2. **Rivas Medical Weight Loss: IN.** Hao-Ping Chai (VP Operations) moves from WEAK to PASS, wave 1, `operations` angle.
3. **Cap: 50 per group**, the default for every campaign. Vadim first set 30 («ліміт ставимо 30 для всіх кампаній»), then raised it the same day to 50 («підніми ліміти до 50 на компанію»). At 50 all 36 Form Health candidates go, including the 6 held out at 30: Lindsay Dages, Max Wolf, Matt Hamil, Francis Nju (Senior Software Engineers) and Leigh Doner (Sr Data Analyst), all R1 `technical-integration`; Sharon Vallee (Operations Specialist), R4 `referral`.
4. **Engineering leaders (lane D): all sent** as proposed, P3 wave 2.
5. **knownwell research lane (C): kept.**
6. **All reserve pools R1-R4 taken**, all wave 2, sent after wave 1 at the same company:
   - R1 engineering and data below director: `technical-integration`.
   - R2 frontline clinicians and behavioral health: `referral` (ask for an introduction to the CMO or clinical lead; they do not own the record or the app).
   - R3 finance, revenue cycle, credentialing: `referral` (route to the CMO or operations lead; renewal documentation stays context, never the pitch).
   - R4 other: partnerships and consultant-relations VPs (Pete Moen, Jenn Roberts) `referral` with the "outcomes beyond pounds to show employers" line; IT, security and EHR roles `technical-integration`; everyone else `referral`.
7. **No top-up Sales Navigator pull:** the missing CEOs and COOs of Form Health, FlyteHealth and Ilant were not found.
8. **"112,100 scans in 2025 across all 3DLOOK customers" is cleared for cold copy in every campaign** («так, це всіх стосується»). It can be used alongside or instead of the 34,000-scan line. Use it only as 3DLOOK-wide scale: never split by client, never tied to a geography. Recorded in `proof-points.md`.
9. **Nick's profile audit has not been done yet.** Acceptance risk accepted as is (last campaign: 15.9%).


## Vadim's decisions 2026-09-29 (step-5 checkpoint, messages)

1. **Messages approved** («апрув»).
2. **Referral lane: no compliance line.** The 29 referral sequences (pools R2-R4 and Conrad Lai) carry no HIPAA/BAA line; the "one compliance line per sequence" rule above applies to every other lane. This overrides the rule in "Rules for steps 3-5" for referral only.
3. **Former employers may be named** in copy (e.g. a hook on a prospect's earlier company).
4. **Elizabeth Lacarra is greeted "Hi Beth,"**, the name she uses in her bio.
5. **Thin or possibly stale profiles stay on the list** (Steven Marchette, Jerusha Stahl, Marsha Rose).
6. **No waves** («хвиль робити не потрібно, давай всіх в один файл, прибери це правило з хвилями»). Everyone goes in one closely.io import file at the same time. This supersedes "Wave 2 (P3) goes at least 7 days after wave 1" and every wave split in this file; the `wave` values in the lists are history, not a send order. The rule is removed from the pipeline for all campaigns.
