---
product: fitxpress
profile: nick
market: USA
created: 2026-10-01
status: approved
approved: 2026-10-01
use_case: fx-telehealth-weight-loss
cap_per_group: 50
banned_terms: [InBody, CoachCare, Zenoti, Thurston, Withings, Prism, Wegovy, Zepbound, Ozempic, Mounjaro, semaglutide, tirzepatide, phentermine, compounded, obese, visceral, FDA, DXA, DEXA, closed, closure, closures, closing, permanently, shut down, fewer clinics, fewer locations, consolidation, consolidating, consolidated, restructuring, new CEO, new leadership, leadership change, move to telehealth, moved to telehealth, moving to telehealth, shift to telehealth, shifting to telehealth, Not Just an App, not just pounds]
---

# Outbound Hypothesis — 2026-10-01 — Options Medical Weight Loss (fixed account list, one account)

- **Campaign:** `2026-10-01-us-options-medical-weight-loss`
- **Owner:** Nick Omelchak (`nick`, USA)
- **Company list: fixed, not researched.** Vadim's own Sales Navigator pull, saved as `sales-nav-raw/export-1.csv`: 7 people, all US, three company names. Vadim asked for Options Medical Weight Loss; the other two rows came in on the name. There is no company-researcher step. Step 2 builds `companies.csv` from "Company types in scope" below.
- **ICP:** `icp-detail.md` §1 (Telehealth & GLP-1 / Weight Loss Programs: "subscription weight-loss programs", "cash-pay telehealth with repeat engagement").
- **Use case file:** `brand-assets/product-info/use-cases/fx-telehealth-weight-loss.md`.
- **Base campaign:** `2026-09-29-us-obesity-medicine` (approved, imported 2026-09-29). Options is that campaign's "Flavour H": an in-clinic body composition test plus a telehealth track. It differs in two ways. Options is mostly cash-pay and consumer-facing: "No insurance required", HSA/FSA eligible. It offers employer group packages ([employers page](https://optionsmedicalweightloss.com/employers/)), but no payer contracts or employer outcome reporting were found. And it is moving patients from clinics to telehealth right now.
- **Content asset:** [GLP-1 Market Growth and the Need for Better Patient Progress Tracking](https://3dlook.ai/content-hub/glp-1-market/), HTTP 200 on 2026-10-01 11:44 UTC (`curl -sL -o /dev/null -w "%{http_code}"`). The privacy FAQ is also 200. The GLP-1 Progress Record and telehealth documentation articles are still 404.
- **Registry:** no hits for the three companies, seven surnames or seven LinkedIn slugs anywhere in `workspace/outbound/` (coordinator and re-check, 2026-10-01). Nick's other campaigns: `2026-08-07-us-digital-fitness` (closed); `2026-09-29-us-obesity-medicine` and `2026-09-29-us-cardiometabolic` (imported 2026-09-29).

> **Read this first.**
> 1. **One account, five people.** All five sendable people work at Options. Of the other two rows, one is a different company that matched on the name and the other cannot be verified; both are OUT.
> 2. **Options is moving patients from clinics to telehealth.** On 2026-08-19 it published 16 pages saying a clinic is "permanently closed" and that patients "can continue with Options Medical through Telehealth". Its locator lists 11 open clinics, against 39 at the end of 2024. Every clinic consultation includes the "Metabolic InBody Test". The telehealth page offers "Labs and metabolic analysis" without saying what that includes. The app can sync Apple Health devices that may report body fat, and the app vendor sells a body-fat scale. So whether telehealth patients get a body composition reading is **unverified either way**. The copy offers an at-home capture inside Options' own app (works wherever the patient is, between visits, same guided sequence each time). It never states or implies a gap, never contrasts clinic and telehealth care and never mentions the closures.
> 3. **Nick's account accepted 39 of 245 invites (15.9%) on the last closed US campaign.** At that rate, five invites yield about one accepted connection. This is an account play, not a test (Success metrics).

---

## Vertical

US physician-supervised, cash-pay medical weight-loss clinic chains that sell GLP-1 programs with an in-clinic body composition test and are moving care to telehealth.

## Sub-segment

One account: **Options Medical Weight Loss**, St. Petersburg, FL. Founded 2014, 133 staff on LinkedIn, physician, PA or NP care with weekly coaching. It sells GLP-1 and other prescription programs, nutrition products, hormone therapy and longevity services. It runs 11 open clinics (AZ 1, FL 1, IL 6, OH 3, per its locator) and a telehealth GLP-1 program whose page went live in December 2025. No revenue figure is published. Current scale: 11 open clinics, a telehealth program and 133 LinkedIn staff. Nicholas Foy's bio reports one clinic's monthly revenue in the tens of thousands of dollars, which puts 11 clinics above the §1 $2M+ threshold. In 2024 Options had 39 clinics and more than 20,000 new patients (company release, February 2025). Inference, not verified.

## Company types in scope: verdicts for the export

Step 2 builds `companies.csv` from this table. The `group` column is what `cap_per_group` counts.

| # | Export `Company_name` (people) | Canonical company = group | Verdict | Company page / website | Send | Evidence |
|---|---|---|---|---|---|---|
| 1 | `Options Medical Weight Loss` (5: Jeremy Castle, Jory Del Cecato, Jessica Tarnawa, Joshua Hicks, Nicholas Foy) | **Options Medical Weight Loss** | **IN** | linkedin.com/company/optionsmedicalweightloss / optionsmedicalweightloss.com | 5 of 5 | The account Vadim asked for. A physician-supervised GLP-1 chain with an in-clinic body composition test at every consultation. It runs a telehealth program and a patient app (Options Health Coach), and sends patients of closed clinics to telehealth. Sources under "Why this is plausible". |
| 2 | `Precision Medical Weight Loss` (1: Jeremy Osborne, MD, DABFM, Owner) | none | **OUT: unverifiable** | none in the row | 0 | A different company from Options; it matched on "Medical Weight Loss". The person is real: NPI 1699302208 lists Jeremy Osborne, MD, Family Medicine, at 411 N Section St, Fairhope, AL, and his LinkedIn shows family medicine at South Baldwin Regional Medical Center. The practice is not: searches on 2026-10-01 found no website, no LinkedIn company page, no NPI organisation record and no directory listing under that name. Similarly named but unrelated businesses exist: Precision Weight Loss Center LLC (bariatric surgery, Atlanta) and Precision Health & Wellness (Worthington, OH). Even if the practice is real, nothing shows a patient app, a telehealth program or $2M+ revenue. |
| 3 | `Weight Loss Options Firm` (1: Alberto Ortega, Founder, CEO) | none | **OUT: different company, leaked in on the name** | none in the row | 0 | Not a clinic. His LinkedIn bio describes a patient-acquisition service for weight-loss companies: "helping Weight Loss Companies acquire clients", "1 firm per city". His earlier roles are physician jobs in Panama. No website or company page was found. A marketing vendor to clinics, not a FitXpress buyer. |

**Totals:** 1 group in scope, 5 people to send, 2 people out with their company. Match rows on the company LinkedIn URL, never on the name: all three company names contain "Weight Loss" and two contain "Options".

## Use case (1 sentence)

Options Medical Weight Loss adds a guided two-photo scan to its own patient app that patients take at home, on telehealth or between clinic visits, with the same guided sequence each time, returning 80+ body measurements such as waist and hips, a 3D model and body composition estimates (under 45 seconds from the photos to structured results), alongside Options' in-clinic body composition test.

## Why this is plausible (evidence)

1. **Body composition is part of what Options sells.** The in-clinic Metabolic InBody Test "is included with every complimentary consultation". It reports body fat %, skeletal muscle mass, visceral fat level, BMR and hydration; the analyzer model is not stated ([InBody Analysis](https://optionsmedicalweightloss.com/services/inbody-analysis/)). "Every patient begins with comprehensive blood work and InBody® body composition testing" ([St. Petersburg](https://optionsmedicalweightloss.com/locations/florida/st-petersburg/)). Both premium plans include it ([GLP-1 plan](https://optionsmedicalweightloss.com/programs/glp-1-premium/), [Rx plan](https://optionsmedicalweightloss.com/programs/prescription-premium/)). Results are reported as fat lost, visceral fat and total body weight.
2. **Its patients are moving to telehealth.** The [telehealth page](https://optionsmedicalweightloss.com/telehealth/) went live on 2025-12-10 (WordPress API). It offers video visits from home, GLP-1 medication shipped home, "Labs and metabolic analysis", coaching and regular follow-ups; intake is "a brief health questionnaire" plus a video visit. It says "telehealth doesn't mean 'less care'" and lists no states. It does not use the words "body composition", and its "metabolic analysis" may or may not include a body composition step (Options calls its in-clinic test the "Metabolic InBody Test"): unverified. On 2026-08-19 Options published 16 "Location Has Closed" pages (Collegeville PA; Tampa FL; Roswell, Snellville GA; Schaumburg, Park Ridge, Willowbrook, South Loop IL; Carmel, Indianapolis IN; Canton, Rochester Hills MI; Raleigh NC; Grove City, Westlake, University Heights OH), each pointing patients to telehealth ([example](https://optionsmedicalweightloss.com/collegeville-pa-location-closed/)). The [locator](https://optionsmedicalweightloss.com/locations/) lists 11 open clinics, against 39 at the end of 2024 ([February 2025 release](https://optionsmedicalweightloss.com/news/transformative-year-for-options-medical-weight-loss-in-2024/)). Leadership changed: the 2024-25 releases quote CEO Dr. Matthew Walker. The [leadership page](https://optionsmedicalweightloss.com/our-leadership-team/), created 2025-12-19, lists CEO Jeremy Castle, CMO Roscoe Nelson, MD (a urologist), COO Mark Wolbert and marketing CMO Sarah Romotsky. Castle's start date is not verified.
3. **The app a scan would sit in already exists, but a vendor builds it.** Options Health Coach is on [Google Play](https://play.google.com/store/apps/details?id=com.coachcare.optionsweightloss) under developer Coachcare, LLC, a white-label RPM vendor: 1K+ downloads, updated 2025-08-25, live video coaching, coach messaging, progress charts. Its [terms](https://optionsmedicalweightloss.com/options-health-coach-terms-and-conditions/) say it syncs Apple Health devices that "may" collect "weight, body fat percentage, and blood pressure". The vendor sells a body-fat smart scale ([device page](https://coachcare.com/device-features), via search); whether Options ships one is not stated. The iOS listing (id6450678162, "Options Medical Clinical, P.A.", per search) returned 404 on 2026-10-01: unverified. Back office: Zenoti is the "single source of truth" with an open API, feeding a Redshift and Power BI warehouse ([Zenoti story](https://zenoti.com/success-stories/options-medical-weightloss), quoting CDTO Manish Goomar, who also says Options now sells memberships and packages; he is not on the current leadership page). The app terms say features depend on the program a patient signed up for. Options sends referring physicians "regular reports on patient progress, treatment compliance, and lab results" ([Health Systems](https://optionsmedicalweightloss.com/health-systems-providers/)).
4. **Context, never numbers in copy.** The 2025 ACLM/ASN/OMA/TOS advisory lists body composition assessment among GLP-1 care priorities ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12264624/)). The Lancet Commission on clinical obesity recommends a body-size measurement, such as waist circumference, alongside BMI ([Lancet](https://www.thelancet.com/journals/landia/article/PIIS2213-8587(24)00316-4/fulltext)). KFF Health News (2026-06-01) reports critics saying some telehealth providers prescribe GLP-1s with "little or no follow-up care", and notes that some patients "may also benefit from blood work or muscle mass screening" ([KFF Health News](https://kffhealthnews.org/health-industry/glp1-weight-loss-drugs-telehealth-oversight-regulation-compounded-semaglutide/), opened 2026-10-01). Options' own [safety page](https://optionsmedicalweightloss.com/safety/) tells patients to ask about "doctor-supervised care, or just an app-based prescription".
5. **FitXpress fits, with stated limits.** From `proof-points.md`: 2 photos, under 45 seconds from the photos to structured results, 80+ body measurements, body composition estimates, typical scan-to-scan differences under 1 cm for most evaluated measurements, web and mobile SDKs and an API. **Limits:** body composition values are estimates; there is no head-to-head study against BIA or DXA; the validation population stops at 210 kg, and Options' published results include a patient who lost 148.6 lbs ([results page](https://optionsmedicalweightloss.com/results/josephine/)), so some patients may start near or above that limit (not verified); there is no clinic-chain reference customer (nearest proof: 34,000 scans in 2025 on one weight-loss platform); the integration route through the app vendor or a web flow is a pilot question. **Do not claim** that Options' analyzer lacks circumferences: some InBody models report waist circumference and waist-hip ratio ([InBody 570 result sheet](https://shop.inbodyusa.com/products/inbody570-result-sheets), via search).

## What Nick's last campaigns teach this one

From `2026-08-07-us-digital-fitness/post-mortem.md` and the two approved 2026-09-29 hypotheses:

- **Acceptance is the loss, not the copy.** 39/245 (15.9%) accepted, then 6/39 (15.4%) replied. Invites went without a note. The profile audit has not been done (Vadim, 2026-09-29). With five invites, acceptance decides the campaign (Open question 2).
- **The one interested reply came from the owner of the KPI in the title.** Here that is the CEO (operations and growth) and the Director of Medical Operations (what providers see on follow-ups).
- **The one evaluation question asked how the scan compares with a smart scale**, on message 2 with proof points. At Options the first question will be how it compares with the in-clinic analyzer. Every non-referral message 2 carries a proof point.
- **Two "I no longer work there" replies.** Both Clinic Director profiles read as stale or job-seeking; the job-change check runs on all five before import.
- **Cold `technical-integration` got 0 of 60.** Options has no engineer in the export, so there is no technical lane.

## Target buyer persona

**Who buys:** the CEO, who runs all operations and partners with the board, and the leader of medical operations, who owns the clinical workflow on clinic and telehealth visits. The COO, CMO and technology lead are not in the export. The referral asks to the two Clinic Directors are meant to reach them.

| Person (export) | person_id | Title | Tier | Lane | Why | Flag |
|---|---|---|---|---|---|---|
| Jeremy Castle | jeremyncastle | Chief Executive Officer | P1 | `at-home-scan` | Sets strategy and "oversees all operations"; multi-site operator (ex-COO The Oncology Institute, VP Operations OneOncology, COO Arizona Urology Specialists). Owns the clinic-to-telehealth shift. | none |
| Jessica Tarnawa | jessicatarnawa | Director of Medical Operations (NCO) | P1 | `at-home-scan`, clinical register | Nurse practitioner leading medical operations; the most likely owner of what providers record at follow-ups (inferred from the title). Licensed in many states, which fits multi-state telehealth. | "NCO" meaning unknown (copy note in Message angle). |
| Jory Del Cecato | jdelcecato | Senior Director | P2 | `program-feature` | Headline: growth through operational efficiency, sales strategy and revenue; background in "prescription medication programs" and sales teams. Owns growth and sales strategy; skills list "Product Launch". Inferred, not verified. | The title names no function (copy note in Message angle). |
| Joshua Hicks | joshua-hicks-10ab2014a | Clinic Director | P3 | `referral` | Runs one clinic. Does not own the app or the telehealth program. | Bio reads like a student-era profile: job-change check. |
| Nicholas Foy | nicholasfoy34 | Clinic Director | P3 | `referral` | Runs operations and revenue at two clinics' GLP-1 programs. | His bio says he is "now exploring opportunities in pharmaceutical/medical device sales": job-change check. Stays on the list per Vadim's 2026-09-29 decision on thin or stale profiles. |

**KPIs they care about (context for Nick, not copy):** keeping patients through the move from clinics to telehealth; what Options' programs include and sell; patient retention in months 2-3; provider time per follow-up; one record across clinic and telehealth patients.

**Likely objections and the honest answer:**
- "We do body composition in clinic." The scan is something patients take at home, between visits or on telehealth. The in-clinic test stays as it is.
- "Our telehealth program already includes metabolic analysis." Ask what it includes before saying anything about it. The scan adds 80+ body measurements and a 3D model from the phone, alongside whatever the program already uses.
- "Patients can sync a smart scale to our app." Connected scales report weight and, on some models, body composition estimates. The scan adds 80+ body measurements, such as waist and hips, and a 3D model from the phone, with no device to ship. Never say what their scale or analyzer does not do.
- "How does it compare with our analyzer?" Accuracy is published against expert manual measurement: "96-97% accuracy against expert manual measurement", typical error 1.5-2.0 cm. Repeatability: typical scan-to-scan differences under 1 cm for most evaluated measurements. There is no head-to-head body composition study against BIA or DXA. Options can run that comparison itself: in a pilot, patients at an open clinic scan alongside their in-clinic test. Do not improvise numbers.
- "Patients above 210 kg or with limited mobility?" A real limit. Performance outside the 38-210 kg validation population has not been established.
- "Our app is built by a vendor." There are web and mobile SDKs and an API. The integration route is scoped on a call; give no timeline.
- "HIPAA? FDA?" For HIPAA, use the US line from `compliance.md` §9. For the FDA, only the trust FAQ sentences, verbatim (Rules).

**Not the buyer:** nobody else at Options is in the export. Out with their companies: Jeremy Osborne and Alberto Ortega (verdict table).

### Target buyer persona: Sales Navigator pull for step 3

**Pull by title filter inside the approved company list, never by company alone.** Vadim's export already holds everyone his pull found at Options, and this list is not stretched. The block is here for an optional title pull inside Options only (Open question 4): the COO, the CMO and a technology lead are on Options' leadership page but not in the export.

```titles
Chief Operating Officer
Chief Operations Officer
Chief Medical Officer
Chief Technology Officer
Chief Digital Technology Officer
Chief Information Officer
Vice President of Technology
```

## Message angle: lanes, company facts and the content asset

Every person gets exactly one lane. Five people at one company receive these at the same time and may compare notes. Write each sequence for its role, keep the facts consistent across all five, and give no two the same opener.

- **Lane `at-home-scan`** (Jeremy Castle; Jessica Tarnawa in a clinical register). Options builds its program on body composition, with the in-clinic test at every consultation. FitXpress adds a guided two-photo scan the patient takes at home, inside Options' own app. It works wherever the patient is, between visits and on telehealth, with the same guided sequence each time, and returns 80+ body measurements (waist, hips and more), a 3D model and body composition estimates from the same scan. Present it as an addition that travels with the patient. Do not contrast clinic and telehealth care, and do not say or imply that patients seen by video go without a body test. Castle: the operating view, one guided capture used the same way for every Options patient, wherever they are. Tarnawa: standardized, timestamped results providers can review at a follow-up; scans the practice selects for comparison; structured results that can sit alongside the progress reports Options sends referring physicians.
- **Lane `program-feature`** (Jory Del Cecato). The hook is his role in growth and sales strategy, and the question is product: whether a body scan from the phone belongs in what Options sells. Options sells programs as memberships and packages that include body composition analysis, coaching and an app. A guided at-home scan inside that app, with 80+ body measurements and a 3D model the care team can compare scan to scan, is a program feature patients can use wherever they are. Proof of scale, not outcomes: 34,000 scans in 2025 on one weight-loss platform, or 112,100 across all 3DLOOK customers.
- **Lane `referral`** (Joshua Hicks, Nicholas Foy). A short ask: who at Options looks after the Health Coach app and the telehealth program? One line of context (a guided two-photo body scan patients take at home inside the app), no pitch, no compliance line, no article, calendar link optional.

**Per-person copy notes:**
- **Jessica Tarnawa:** call her title "Director of Medical Operations". Never expand or guess "NCO"; its meaning is unknown.
- **Jory Del Cecato:** his title is only "Senior Director". Write to the growth and sales-strategy role in his headline, and never invent a function title for him.
- **Jeremy Castle:** his former employers may be named (The Oncology Institute, OneOncology, Arizona Urology Specialists). Never refer to when he joined.
- **Nicholas Foy:** never use the revenue figures or job-search line in his bio.
- **Joshua Hicks:** his profile is thin; write to his current title only.

**Company facts the copy may use (no numbers, no device, vendor or drug brands):**
- An in-clinic body composition test is included with every free consultation; programs include body composition analysis, blood work and weekly coaching.
- Options reports patient results in body composition terms (fat lost), alongside total weight.
- A physician-led telehealth GLP-1 program: video visits from home, medication shipped to the door, nutrition and behavior coaching, regular follow-ups.
- The Options Health Coach app: live video coaching calls, coach messaging, progress charts, device sync. Prefer "your patient app"; name "Options Health Coach" only together with the telehealth program (iOS status unverified).
- Weight loss and hormone care "under one roof" (the CEO's line on Options' site). This is the only Options line copy may quote, verbatim and at most once per sequence.
- Options sends referring physicians regular reports on patient progress, treatment compliance and lab results (for Tarnawa).
- Physician-supervised since 2014, St. Petersburg, Florida. Jeremy Castle's former employers may be named: The Oncology Institute, OneOncology, Arizona Urology Specialists.

**Content asset in message 2 (lanes `at-home-scan` and `program-feature`; one link plus the calendar link):** https://3dlook.ai/content-hub/glp-1-market/. Point to its part on clinic and telehealth workflows ("In-person and hybrid clinics combine scheduled office visits with remote intervals... professional measurements during clinic visits and an appropriate remote method between appointments"), or link it as a general resource. Do not quote its "approximately 30 to 45 seconds"; copy uses only "under 45 seconds from the photos to structured results". `referral`: no article. **Link no other 3DLOOK page.** In particular, never the body-composition comparison and "remote body composition tools" articles (they name device brands and frame a replacement) or the visual-progress article ("HIPAA-aligned").

## Rules for steps 3-5

- **Sender and format:** Nick, first name only, as the last line; English. Connection request without a note, unless Vadim decides otherwise (Open question 2). Message 1 ≤ 600 characters; message 2 ≤ 550 with Nick's calendar link as plain text. All five go in one import file at the same time.
- **One company, five people.** Never mention that colleagues were contacted, and never claim to have spoken with anyone at Options. Facts must agree across all five sequences.
- **No 3DLOOK client is named anywhere in cold copy.** The only anonymised proof: "112,100 scans in 2025 across all 3DLOOK customers" (3DLOOK-wide scale only, never split by client or tied to a geography) and "34,000 scans in 2025 on one weight-loss platform" (no client name, no geography).
- **Numbers only from `proof-points.md`.** Allowed: two photos (front and side); "under 45 seconds from the photos to structured results"; 80+ body measurements; body composition estimates (body fat %, lean mass, fat mass) with BMI and BMR as calculated metrics; "96-97% accuracy against expert manual measurement" or the full sentence from `accuracy-formulations.md` §1.1; repeatability only as "For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm."; the two scan-volume lines above. **No other number:** no Options clinic, state, patient or staff counts, no outcome figures, no prices, no years of history.
- **Compliance wording only as the live trust FAQ allows (`compliance.md`).** Lanes `at-home-scan` and `program-feature` carry one compliance line in message 2, the US variant verbatim: "We support HIPAA-governed deployments under a BAA, encrypt data in transit and at rest, and delete photos after processing or within 30 days." Referral carries none. Cold copy does not raise regulatory status (hence `FDA` in `banned_terms`). If a reply asks about the FDA or device status, answer with only these sentences, verbatim: "FitXpress is not cleared, authorized, or approved by the U.S. Food and Drug Administration (FDA). 3DLOOK makes no representation as to whether FDA clearance, authorization, or approval is required for any particular customer's use case." and "An independent regulatory assessment concluded that FitXpress does not meet the definition of a medical device under the UK Medical Devices Regulations 2002 (UK MDR) or the EU Medical Devices Regulation (EU MDR)." The short form "FitXpress is not a medical device." rests on that UK/EU assessment and never answers an FDA question. **Hard fails:** "HIPAA compliant", "HIPAA-compliant", "HIPAA certified", "SOC 2 certified", "SOC 2 compliant", anything FDA-cleared or FDA-approved, "processed, not stored", "no personal data", "no personal identifiers". Options' own site says "HIPAA-compliant"; never echo it.
- **Never state or imply what Options' equipment, app or telehealth program measures or lacks.** Do not write that telehealth patients have no body composition data, only weight, or lose the clinic test. Do not write that the in-clinic analyzer or any scale lacks circumferences. Do not set up a clinic-versus-telehealth contrast ("in clinic X, online Y"). Offer the capability: "a two-photo scan patients take at home inside your app returns..., wherever they are and between visits". The in-clinic test is described only as what Options says it is.
- **Never mention clinic closures or the shift itself:** no "closed", "fewer clinics", "consolidation", "moving patients to telehealth", "new leadership", "new CEO", ownership or investors. Say "patients you see by video" or "your telehealth program". The closures are the reason for this campaign, not a line in it; the gate fails these phrasings through `banned_terms`.
- **What the scan does, and does not do.** It returns estimates and measurements for the care team. It does not diagnose, decide eligibility, set dosing, preserve muscle or produce weight loss. Say "the practice compares scans it selects" or "scan-to-scan comparison", never "tracks each patient". Say "alongside", "on video visits", "between clinic visits"; never "replace your analyzer" or "instead of the clinic test". Weight loss only: no pitch for hormone therapy, TRT or longevity outcomes.
- **No outcome promises.** Never promise or imply gains in retention, engagement, adherence, drop-off, conversion, revenue or ROI, or better patient results. The use-case file's hero line ("boost retention, reduce drop-off, and prove program ROI") is not usable in this campaign. Describe what the scan returns, where it runs and how much it is used (the two scan-volume lines).
- **Brands:** only Options' own ("Options Medical Weight Loss", "Options", "Options Health Coach"). Device, app-vendor, scheduling-vendor, drug and competitor brands are banned (`banned_terms`). Say "your in-clinic body composition test", "your patient app", "GLP-1" or "anti-obesity medication". Never touch medication sourcing (compounded or branded).
- **Person-first, non-stigmatizing language:** "patients with obesity", "people living with obesity". Never "obese", no before-and-after framing, no "burn fat". Options' site sells "Fat Burners"; never echo it. Never quote Options' lines against apps or about telehealth care levels.
- **Word traps Options' site invites:** "comprehensive", "revolutionary" and "seamless" (all three appear on its pages) are hard-banned. Never "objective" about our data; say "standardized", "timestamped", "structured", "repeatable". Do not use "metabolic scan" for FitXpress: that is Options' name for its in-clinic test.
- **No pricing and no trial terms** anywhere. A price or trial question goes to the call.
- **Message 1 gate.** Every message 1 carries at least one product specific from `proof-points.md` and one line that could only have been written to Options or to that person; each pair of messages cites at least one number. The referral lane is exempt from the product specific.

## Anti-cases (where it does NOT work)

- **Rows out, by name:** Precision Medical Weight Loss (Jeremy Osborne, MD: practice unverifiable) and Weight Loss Options Firm (Alberto Ortega: a patient-acquisition vendor, not a clinic). Match on the company LinkedIn URL, never on the name.
- **Pitching the scan as a replacement** for Options' in-clinic body composition test, or as equivalent to it. It is for video visits and between clinic visits.
- **Hormone therapy, TRT, menopause and longevity programs:** not the use case; do not pitch body data for them.
- **Options' employer partners (group packages) and referring physicians:** not contacted in this campaign.
- **Stop conditions before send:** Options turns out to already run a phone-camera body scan, or to have signed a scanning vendor (displacement: flag for Vadim); Options announces a sale, merger or wider shutdown (pause, Vadim decides); a profile shows the person has left (drop; do not replace from outside the export).
- **Not a BMI-verification or eligibility campaign:** the scan does not decide who qualifies for GLP-1.

## Vadim's decisions 2026-09-29 carried over (standing, built in: not open questions)

From the step-4 and step-5 checkpoints of `2026-09-29-us-obesity-medicine` and `2026-09-29-us-cardiometabolic`. They apply here as written.

1. **No headcount floor.** The "<50 employees" exclusion is removed from `icp-detail.md`. Segment revenue thresholds still apply (§1: $2M+).
2. **`cap_per_group: 50`**, the default for every campaign. **No waves:** everyone goes in one closely.io import file at the same time.
3. **Every function at an in-scope company gets a lane.** FAIL is reserved for the wrong company, identity collisions and people not actually at the company.
4. **Referral-lane sequences carry no compliance line.** Every other lane gets one compliance line in message 2, the US variant verbatim from `compliance.md`.
5. **Former employers may be named in copy.**
6. **"112,100 scans in 2025 across all 3DLOOK customers" is cleared for cold copy** as 3DLOOK-wide scale only. The 34,000-scan line is cleared with no client name and no geography. No 3DLOOK client is ever named.
7. **Thin or possibly stale profiles stay on the list** (step-5 decision, obesity-medicine). This covers Joshua Hicks and Nicholas Foy, unless the job-change check shows they have left.
8. **Live 3DLOOK pages are fine as they are** (step-4, cardiometabolic): the GLP-1 hub's "approximately 30 to 45 seconds" is not a defect to fix. Cold copy still uses only the approved wording in Rules.
9. **Nick's profile audit has not been done.** Acceptance risk accepted as is.

## Validation criteria (Step 2 will check)

There is no company research. Step 2 builds `companies.csv` from the verdict table, then validates people against the persona.

- **Companies.** One row: Options Medical Weight Loss, group `Options Medical Weight Loss`, `linkedin.com/company/optionsmedicalweightloss`. Precision Medical Weight Loss and Weight Loss Options Firm go to routed-out with their reasons. `outbound-registry.py check --profile nick` runs on the export and must come back clean.
- **People.** All five PASS with the tiers and lanes in Target buyer persona (P1: Castle, Tarnawa; P2: Del Cecato; P3 referral: Hicks, Foy). A job-change check runs on all five before import, flagging Hicks and Foy by name. Anyone who has left is dropped, not replaced.
- **Message 1 gate.** Every message 1 carries at least one product specific from `proof-points.md` and one line that could only have been written to Options or to that person; each pair of messages cites at least one number. Zero client names, zero pricing, zero `banned_terms`, no closure language. Kept as a failure, not a note: `2026-07-21` sent 307 message 1 texts with no specific and drew 1 reply on 67 sends.
- **Proof in product-info.** Use-case file and live article: yes. Reference customer among clinic chains: none. The adjacent anonymised weight-loss proof (34,000 scans) is used openly, not hidden.

## Success metrics for this campaign

Five invites. Read these per person, not as rates.

| Metric | Target | Floor | Basis |
|---|---|---|---|
| Invites sent | 5 | 4 | after the job-change check |
| Accepted | 2 | 1 | `nick` 08-07: 15.9%, about 0.8 expected |
| Replies | 1 | 0 | |
| Positive reply from P1 or P2 (interest or question) | 1 | 0 | |
| Discovery call with Castle or Tarnawa, or a referred COO or technology lead | 1 within 6 weeks | 0 | |
| Pilot | not a target | | account in restructuring |

**Falsified for Options if** a P1 or P2 reply says telehealth patients do not need a body record beyond what they send in, that the current set-up covers it, or that Options is leaving telehealth. **Inconclusive if fewer than two accept**, which is the likely outcome; that says nothing about the segment.

## Risks

1. **Acceptance.** Five invites at 15.9%.
2. **Restructuring.** Sixteen clinic pages went to "closed" on 2026-08-19. New vendor spend may be frozen, or the shift to telehealth may make this the right moment. The cold copy cannot tell which.
3. **The app belongs to a vendor.** Integration may need the vendor's cooperation or a web flow, and iOS availability is unverified.
4. **Comparison with the in-clinic analyzer,** with no study to quote; and patients above the 210 kg validation range.
5. **Business-model exposure.** The telehealth prices on Options' site are for compounded medications (its own disclaimer). This is background only; copy never touches it.
6. **Five people at once** in a small company: one careless or inconsistent message is seen by the CEO.

## Open questions for Vadim

1. **The two no-page rows: confirm OUT.** Osborne's practice cannot be verified (NPI shows a family physician in Fairhope, AL; no web trace of "Precision Medical Weight Loss"). Ortega runs a patient-acquisition service, not a clinic.
2. **Connection note for this one account?** The pipeline sends invites without a note, and at Nick's rate about one of five accepts. A short note on the Castle and Tarnawa invites is the only lever left on a five-person list. Your call; the draft assumes no note.
3. **Clinic Directors as `referral`** (recommended: they do not own the app or the telehealth program, and both profiles look stale or job-seeking), or a clinic-operations pitch?
4. **Title pull inside Options only?** The COO (Mark Wolbert) and CMO (Roscoe Nelson, MD) are on Options' leadership page but not in the export. The technology lead's status is unclear (Manish Goomar's bio is still live, but he is not on the leadership page). Not added, because the list stays as Vadim pulled it. The `titles` block is ready if you want them.

## Sources

Claims about Options carry their URL inline above. Not linked inline:

- Options pages also read on 2026-10-01: https://optionsmedicalweightloss.com/ · /our-leadership-team/jeremy-castle-bio-page/ · /our-leadership-team/manish-goomar-bio-page/ · /employers/ · /careers/ ("40+ clinics", stale) · /news/options-medical-weight-loss-plans-major-expansion-in-2024/ (Thurston Group portfolio company, 23 clinics, telehealth and app launched in 2023) · closure-page dates from `/wp-json/wp/v2/pages?search=location closed`
- Context source opened: https://kffhealthnews.org/health-industry/glp1-weight-loss-drugs-telehealth-oversight-regulation-compounded-semaglutide/ (KFF Health News, 2026-06-01) · Options results page https://optionsmedicalweightloss.com/results/josephine/
- Rows out: NPI registry API, Jeremy Osborne (NPI 1699302208); web searches on 2026-10-01 for "Precision Medical Weight Loss" (Fairhope, Alabama, LLC) and "Weight Loss Options Firm" found no matching business
- Live 3DLOOK assets (HTTP 200 on 2026-10-01): https://3dlook.ai/content-hub/glp-1-market/ · https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/
- Internal: `sales-nav-raw/export-1.csv` · `2026-09-29-us-obesity-medicine/{hypothesis.md,decisions.md}` · `2026-09-29-us-cardiometabolic/hypothesis.md` · `icp-detail.md` §1 · `use-cases/fx-telehealth-weight-loss.md` · `proof-points.md` · `compliance.md` · `tech-spec.md`

## Vadim's decisions 2026-10-01 (no checkpoints for this campaign)

- **Vadim, 2026-10-01: «продовжуй без апруву».** This campaign runs hypothesis → validate → messages → import without his checkpoints. Opus QC still runs after hypothesis, validate and messages; a score below 12/20 stops the run.
- The open questions above are closed with the hypothesis's own defaults, applied by the coordinator under that waiver:
  1. Jeremy Osborne (Precision Medical Weight Loss) and Alberto Ortega (Weight Loss Options Firm): **OUT**.
  2. **No connection note.** Invites go without a note, as in every campaign.
  3. **Clinic Directors** (Joshua Hicks, Nicholas Foy): `referral` lane, P3.
  4. **No extra title pull.** The list stays as Vadim pulled it (5 people at Options). The COO and CMO join only if Vadim pulls them. New rows go through `outbound-registry.py check`, `compact`, a row in `decisions.md` and `apply-decisions`: `promote` only changes people already in `people-validated.csv`.

## Vadim's decisions 2026-10-01 (widening: Apollo leadership pull)

- **Vadim, 2026-10-01: «додай всіх».** Every Options leader Apollo returned at seniority owner/founder/c_suite/partner/vp/head/director goes into this campaign. That is 9 people beyond the 5 from his Sales Navigator list (`sales-nav-raw/apollo-2026-10-01.csv`, 9 credits; search and log in `apollo-log.md`). This supersedes decision 2026-10-01 #4 ("no extra title pull"). The COO (Mark Wolbert) and a technology lead are not in Apollo. No checkpoints, as before; opus QC still runs.
- **Lanes for the new roles** (same lanes as the first five):
  - Matthew Walker, Founder and board member: `at-home-scan`, P1.
  - Roscoe Nelson, Chief Medical Officer (since 2026-03): `at-home-scan` in the clinical register, P1.
  - Joe Pflanz, Chief Marketing Officer: `program-feature` (what Options sells and markets), P2. His angle differs from Del Cecato's; both ask about the offer, from different seats.
  - Krystle Collins, Regional Clinical Operations Director (nurse practitioner): `at-home-scan` in the clinical register, P2, distinct from Tarnawa's follow-up question.
  - Regional Directors (Kenny Scott, Kaytee Stevens, Jami Waclawski), Clinical Director (Justin Leflore), Clinic Director (Jacob Ruff): `referral`, P3.
- **Single-account rule (messages QC 2026-10-01):** everyone at Options gets invites at once. Each person in a shared lane gets a distinct question. The referral asks must differ from each other and from Hicks's (who decides the app) and Foy's (who leads telehealth).
- **Job-change flags:**
  - Kenny Scott's Apollo record lists two current roles: Regional Director of Sales & Operations at Fitness Ventures (Crunch Fitness), and the same title at Options. Drop him if the profile shows he left Options.
  - Justin Leflore's Apollo record was last refreshed 2025-10-27, so it may be stale.
- **Registry:** this campaign is already recorded for nick, so the widening is checked with `outbound-registry.py check --campaign 2026-10-01-us-options-medical-weight-loss`. The campaign's own record is not an exclusion, while every other exclusion still applies.

