---
product: fitxpress
profile: nick
market: USA
created: 2026-11-19
status: approved
use_case: fx-digital-fitness
cap_per_group: 50
message_max_chars: 900/700
referral_call: yes
learnings: 2026-10-30
people_source: apollo-and-sales-navigator
source_page: https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/
banned_terms: [Zing Coach, Verv, Erakulis, Yazen, UK Meds, Healthyr, Safariland, Burlington Medical, Jim's Formal Wear, Generation Tux, Tailoor, Redthread, Prism, Prism Labs, Bodygram, Size Stream, MeThreeSixty, Fit:match, Mirrorsize, Bodd, Spren, Bodymapp, ZOZOFIT, Styku, Fit3D, InBody, Evolt, Withings, BodySpec, Visbody, DEXA, DXA, BIA, bioimpedance, FitnessAI, Noom, WeightWatchers, Weight Watchers, Personify, Virgin Pulse, Wellhub, Gympass, ClassPass, Freeletics, Gymondo, Fitify, Les Mills, Orangetheory, Equinox, Planet Fitness, Apple Fitness, Fitbit, Garmin, Whoop, Oura, Strava, Zwift, GLP-1, semaglutide, tirzepatide, Wegovy, Zepbound, Ozempic, Mounjaro, obesity, obese, Kidman, JMIR, churn, churned, churning, Smart Scales, liveness, Clothing Detector, voice prompts, voice guidance, HIPAA, BAA, FDA, SOC 2, GDPR, CCPA, compliant, certified, certification, clinically validated, clinically proven, medical-grade, lab-grade, gold standard, diagnose, diagnosis, accuracy, accurate, precise, precision, 96-97, verify, verified, verifies, verification, fraud, cheat, cheating, fake, selfie, selfies, guarantee, guaranteed, free trial, trial, tier, tiers, positioned as, not stored, no personal data, anonymous, as discussed, we spoke, reconnect, earlier message, my last message, in August, last summer, Circling back, Following up, Saw your post, I wanted to reach out, Thanks for connecting, thank you for connecting]
---

# Outbound Hypothesis: 2026-11-19, US connected fitness and coaching apps, a body check-in inside the member's app (Nick)

Vadim's direction (2026-11-19): outreach on the new use-case page
https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/ (H1 "A mobile gym body scanner
alternative for fitness apps") from four profiles in parallel: `nick` (USA, this file), `olena`
(EU), `katya` (LatAm and Mexico), `vadim` (Australia). Product claims in this file come from the
live text captured on 2026-11-19, `workspace/pages/for-connected-and-digital-fitness/published-live-2026-11-19.md`,
not from `page-final-2026-10-07`. This is Nick's second campaign in `icp-detail.md` §8. The
first, `2026-08-07-us-digital-fitness` (post-mortem 2026-09-02), explains most choices below.
Fix round 2026-11-19: the QC report (`workspace/_quality/outbound/2026-11-19-hypothesis-generator-us-connected-fitness.md`,
17/20), Vadim's decisions at the hypothesis checkpoint and the coordinator's rulings for the four
sibling campaigns are applied below; the first version is kept as `hypothesis-v1-2026-11-19.md`.

## Vertical

US-headquartered connected and digital fitness businesses (`icp-detail.md` §8) that sell a paid
membership or subscription and run their own member app with a progress check-in. Weight-loss
medicine, employer wellness, gym and studio chains (franchises included), fitness marketplaces and
aggregators, and content-only platforms are separate segments and are not in this campaign.

## Sub-segment

US-HQ companies with $1M+ revenue (the §8 floor; Series B to public) whose app already runs a
progress check-in (a weigh-in, progress photos, a measurements form or a coach review) and has
no body scan in it today. Four groups, one use case:

- **A. Connected-fitness hardware with a paid membership app** (bike, tread, rower, strength
  machine, boxing). The membership is the recurring revenue and the app is where progress shows.
- **B. Coaching apps with a human or AI coach** (remote personal training, strength
  programming). The coach or the algorithm sets the next program block from a check-in.
- **C. Coaching platforms that trainers use to run client check-ins** (B2B2C). One integration
  reaches every trainer's clients; the buyer is the platform's product or partnerships owner.
- **D. Workout and fitness-nutrition subscription apps with a premium plan and a progress screen
  of their own.** A class or video library with no progress check-in is content-only and out.

Expected list: 30 to 40 companies after exclusions, nine of them re-contacts from August
(Company types in scope); fewer than 30 IN after step 2 stops the run (Validation criteria). One ICP
segment only: in August, Personify Health (employer wellness) took 63 of 248 invites under §8 copy.

## Use case (1 sentence)

A US connected-fitness or coaching platform embeds FitXpress through its SDK and API, the member
takes 2 guided photos on their own phone at onboarding and at each check-in the program already
runs, and the platform gets back one timestamped record of 80+ body measurements and body
composition estimates, under its own brand, which its progress screen, its coaches and its paid
plan (3D Body Progress tracking and 3D Goal Visualization on the Pro plan) use to show measured
change between check-ins.

## Why this is plausible (3 reasons grounded in evidence)

1. **Connected fitness has moved its promise from minutes trained to body outcomes, under
   subscription pressure.** Peloton's CEO named GLP-1 medications in his January 2026 shareholder
   letter as a reason to prioritise "cardio plus strength", and the company reports about two
   million members strength training on the platform ([Athletech News](https://athletechnews.com/peloton-ceo-strength-training-wellness-will-be-key-to-brands-growth/));
   nearly half of active members engaged with Peloton IQ's personalised insights by the end of
   Q2 FY2026 ([Peloton Q2 FY2026 results](https://investor.onepeloton.com/news-releases/news-release-details/peloton-announces-q2-fy2026-financial-results)).
   In Q4 FY2026 Peloton's average net monthly paid churn rose to 2.2% from 1.8% a year earlier and
   paid subscriptions fell 9% year on year, while subscription revenue grew 7% on a price rise
   ([The Clip Out](https://theclipout.com/peloton-subscriber-churn-q4-fy26/)). WeightWatchers added
   strength-building plans to its GLP-1 program in December 2025 ([HIT Consultant](https://hitconsultant.net/2025/12/17/weight-watchers-launches-new-glp-1-program-and-ai-app-features/)).
   Strength and recomposition goals are where a weigh-in says least: waist and hip changes and fat
   and lean mass estimates are the change those members train for. (Context for this file only;
   no prospect figure goes into copy.)
2. **Members are lost before the program shows results, and members who want measured progress
   already scan elsewhere.** Health and fitness apps kept 24% of users on day 1 and 7% on day 30 in
   Adjust's 2023 benchmark, which uses 2022 data ([Adjust](https://www.adjust.com/blog/get-the-mobile-app-retention-benchmarks-for-2023/));
   a JMIR scoping review found a median 70% of users stopped using lifestyle and mental health apps
   within 100 days, with the sharpest drop soon after download (Kidman et al., 2024,
   [JMIR 26:e56897](https://www.jmir.org/2024/1/e56897)). The live page cites both; the "lack of
   personalization" reason it attaches to the second was not confirmed in this check, which is one
   more reason neither figure goes into copy (Rules). Meanwhile the 2026 app stores carry a wave of
   standalone phone body-scan apps ([PhysiqueAI](https://apps.apple.com/us/app/physiqueai/id6756671414),
   [Evoly AI](https://play.google.com/store/apps/details?id=com.evolyai.app),
   [Recomp AI](https://mwm.ai/apps/recomp-ai-3d-body-scanner/6752960004),
   [GainFrame](https://apps.apple.com/app/id6759252082)), and some platforms have embedded a scan:
   a competitor's SDK in Noom and WW (`competitors.md`, verified 2026-10-15), and earlier
   announcements of a competitor's SDK for Tempo in 2023 ([Business Wire](https://www.businesswire.com/news/home/20230628277318/en))
   and of FitnessAI's own BodyScan in an undated release
   ([Fitt Insider](https://insider.fitt.co/press-release/fitnessai-launches-innovative-bodyscan-technology-for-mobile-devices/));
   step 2 re-checks whether those two scans are still live.
   A platform without one leaves members to take the scan, the result and the brand moment to a
   separate app, which is the page's comparison table in one line. On coach platforms, client
   check-ins still run on forms, weights and photos ([Everfit's own comparison](https://blog.everfit.io/everfit-vs-trainerize-vs-truecoach), a vendor source).
3. **FitXpress is built for this step, and the page now says so publicly.** The live page
   (2026-11-19): the scan runs inside the platform's app on the member's own phone, with no
   hardware and no club visit; 2 guided photos with Real-Time Pose Validation; 80+ body
   measurements and body composition estimates under 45 seconds from the photos to structured
   results; one timestamped record per scan through the API, linked by the platform to the member
   profile; white-label screens and the platform's own consent wording; 3D Body Progress tracking
   and 3D Goal Visualization on the Pro plan; the coach reviews the same record before the next
   program block; an in-club scanner still suits club visits and FitXpress covers the check-ins
   between them; a cohort pilot measured on day-30 and day-90 retention and free-to-premium
   conversion against criteria agreed up front; no integration fee (`pricing.md`). The use case
   file `use-cases/fx-digital-fitness.md` names the same buyers and KPIs. Against the main
   competitor the difference is a two-photo capture instead of a timed 360° spin, and white-label
   embedding (`competitors.md`, for positioning only). Honest limit: no fitness client can be named
   and no body-fat accuracy figure exists until the December 2026 lab report (`roadmap.md`), so
   the case rests on the mechanism and on a measured pilot.

## What the 2026-08-07 campaign teaches this one

Nick's August campaign in this segment: 245 invites, 39 accepted (15.9%, against his baseline of
24.7%), 6 replies, 1 interested: iFIT's Chief Subscription & Content Officer, answering a Message 1
that tied visible progress to the reason members renew. What this file changes:

1. **48% of invites went into two accounts** (Personify Health 63, iFIT 56). Personify Health is
   out (employer wellness, §4). `cap_per_group` stays 50 (only Vadim changes it), so Peloton and
   iFIT can still take up to 100 of the 200 to 300 expected SEND; Risks 2 carries the stop rule and
   Open question 7 the soft-cap option.
2. **39% of invites went to the WEAK tier**: 0 interested, and 2 of the 3 WEAK replies came from
   people who had left. WEAK is fill only, marked, after a company's PASS people; the Account facts
   round re-checks every P1 on the web before step 5.
3. **`technical-integration` drew 0/60.** No technical lane; engineers are not pulled; a CTO only
   at a company under about 100 staff.
4. **Only 13 of 27 researched companies got any contact** (Noom, WW and Peloton got none). The
   pull is by title per company, Apollo first, with Hlib's Sales Navigator pull added when it
   arrives (Vadim 2026-11-19). Noom and WW are now out (they run a competitor's scan).
5. **Three segments in one list** (consumer apps, employer wellness, weight-loss medicine). One
   segment here.
6. **Smaller apps drew 0 replies on 81 invites; the large subscription brands gave all 6.** Not a
   reason to drop small companies, but a company goes in only with at least one P1 or P2 person
   whose profile shows product, subscription or coaching scope.
7. **Invites carried no note, so acceptance was the profile, not the copy** (HYP-7): Open question 8.

## Target buyer persona

**Who buys:** the person who owns what a member sees at a check-in and what the paid membership
includes. At connected-fitness brands and workout apps: the chief product officer and the product
heads for the member app, and the owner of the subscription or membership business (Chief
Subscription Officer, GM or head of subscription or membership). At coaching apps: the head of
coaching and the program owner. At coach platforms: the head of product and the partnerships or
integrations head. At companies under about 500 staff: the founder or CEO, added by name.

- **Why these titles, not others:** they decide where a new step sits (onboarding or the first
  check-in), what the progress screen shows, what goes into the paid plan, and whether a cohort
  pilot runs. The one interested reply in August came from a subscription owner. Engineering
  implements after a product owner says yes (`technical-integration` 0/60 in August). Growth,
  CRM, lifecycle and brand marketing do not own the check-in and drew 0/44 and 0/52 in the pooled
  data (`learnings.md` PPL-3), so the "Head of Growth" title in §8 is not pulled. Two more §8
  titles are departures. "VP User Engagement / VP Engagement / Retention" is pulled only where
  retention sits with the subscription or membership owner (Head of Subscription & Retention and
  similar, the title pattern the August post-mortem told the next search to look for, on N=1);
  engagement and retention marketing are not pulled (the `retention` lane drew 0/53, HYP-6).
  "Digital Experience Manager" has no title line: the member-app scope it stands for comes through
  the product lines, and step 4 sorts any digital-experience title by the profile. The other §8
  titles map to lines below: Fitness Program Director to the fitness and programming lines,
  Innovation & Partnerships to the partnership lines, Product Manager to the group, principal and
  senior lines (a bare Product Manager line would flood Peloton and iFIT), and the CTO only at a
  company under about 100 staff.
- **What they care about (KPIs):** day-30 and day-90 retention; free-to-premium (trial-to-paid)
  conversion and premium attach; monthly paid churn; onboarding completion; check-in completion and
  program adherence; coach time per client and clients per coach (trainer-to-member ratio);
  differentiation from content-only apps; build-versus-buy cost.
- **Objections they will likely raise, with the honest answer:**
  - Another onboarding step will cost completion. It can. The product team chooses onboarding or
    the first check-in; the pilot compares onboarding completion with the usual flow and measures
    scan completion separately.
  - We could build it, or members can use a scanning app. Building means a capture layer with pose
    and framing validation, 80+ body measurements and a structured API record. A separate app keeps
    the member, the result and the brand outside the platform's app. FitXpress is white-label, the
    record comes back to the platform, and there is no integration fee.
  - How good is body fat from photos? Body composition values are estimates derived from the
    measurements with height and, where provided, weight. For progress, consistency matters: the
    repeatability sentence in Rules. Methodology under NDA. No body-fat accuracy figure is public.
  - Members will not want to photograph their body. Form-fitting clothing; the platform's own
    consent wording; photos deleted after processing or kept up to 30 days under the platform's
    policy, with blurring and face obfuscation; each scan on a randomly generated identifier.
  - Is it a medical device, and FDA? FitXpress is not a medical device; the FDA answer comes from
    `compliance.md` §10, in replies only.
  - Does it sync to Apple Health or Health Connect? The platform's own team builds any sync;
    FitXpress returns structured data through the API.
  - We already have an in-club scanner. It still suits members who visit; FitXpress covers the
    check-ins between visits, on the member's phone.
  - Who in fitness uses it? 3DLOOK has worked with 100+ clients, including fitness teams; no names.
  - What does it cost? Plans from $1,000 a month for up to 500 API requests, with no integration
    fee: in replies and on the call only (Vadim 2026-11-19: no dollar figure in copy).
- **Tiers (order only; one import file).** P1 is never given for the title alone: the profile must
  show member-app, subscription or coaching scope.
  - P1: CPO; VP or head of product for the member app or platform; Chief Subscription Officer, GM,
    VP or head of subscription or membership; VP or head of coaching at group B; CPO or head of
    product at group C; founder or CEO at a company under about 500 staff (added by name at step 3).
  - P2: director of product; group, principal or senior product manager whose profile names
    progress, tracking, onboarding, personalization, member experience, coaching or the member app;
    head coach or coaching operations lead; head or VP of fitness, training, programming or content
    when the role owns programs; exercise or sports science lead; partnerships or integrations head
    at group C.
  - P3: product managers with unrelated or unclear scope (commerce, hardware, payments);
    member-experience leads whose profile is support or delivery; content heads without program
    scope; partnerships and business development heads at groups A, B and D; CTO at a company under
    about 100 staff.
  - P4: `referral`, anyone else at an IN company in a relevant function.
  - WEAK: fill only after the company's PASS people are placed, and marked as fill.
- **Lanes by title:** `product` (product leadership and product managers); `membership`
  (subscription and membership owners, and member-experience leads with product or program scope;
  a TEST lane, see Learnings applied, HYP-6); `coaching` (coaching, fitness, training, programming
  and program-content owners; coach-success leads at group C); `science` (exercise science, sports
  science, human performance); `leadership` (founders, CEOs, presidents, GMs and COOs of the
  company or of its app business, and founder-CTOs at small companies); `partnership`
  (partnerships, business development, integrations); `referral` (anyone else in a relevant
  function at an IN company, placed at step 4).
- **Location rule (step 4 applies it):** every person is located in the United States. People at
  US companies who are located in the UK, the EU, Canada, Australia, New Zealand or LatAm FAIL here;
  those markets belong to `katerina`, `olena`, `vadim` and `katya`, three of whom run this page now.
- **Not the buyer (not pulled; if they appear, a skipped pool listed at step 4, never SEND):**
  engineers, engineering managers and architects, and the CTO or VP engineering at a
  company over about 100 staff; data scientists and analysts; growth, CRM, lifecycle and retention
  marketing, brand, social, content marketing and PR; instructors and on-camera talent; hardware,
  supply chain, manufacturing, logistics, delivery, retail, showroom and sales roles; customer and
  member support; finance, legal, HR, talent and L&D; designers.

### Target buyer persona: Sales Navigator pull for step 3

**Pull by title filter inside the approved company list, never by company alone.** People come
from Apollo first (`apollo-pull.py search` with the titles below, per approved company, located in
the United States); Hlib's Sales Navigator pull with the same titles is added when it arrives
(Vadim 2026-11-19). In Sales Navigator, add the geography filter "United States" manually (`sales-nav-query` writes none): Peloton, iFIT, Tonal and
Hydrow have staff abroad. Lines match inside longer titles (`Head of Product` finds Head of Product,
Member App). Founders, CEOs, presidents and GMs are added by name at step 3, for companies under
about 500 staff only: a CEO line pulls every executive, and a President line pulls every Vice
President. **Exclusions for the whole search:** add to the generated `NOT (...)` list `Marketing`,
`Brand`, `Social`, `Creative`, `Production`, `Retail`, `Showroom`, `Sales`, `Commerce`,
`Supply Chain`, `Logistics`, `Manufacturing`, `Delivery`, `Finance`, `Legal`, `Talent`,
`Learning`, `Enablement`, `HR`, `UX`, `User Research`, `Data Scientist`, `Analyst`, `Instructor`,
`Lifecycle`, `CRM`, `Growth`, `Payments`, `Billing`, `Member Support`, `Customer Care`.
`Retention` is not excluded: `NOT Retention` would drop combined owners such as Head of
Subscription & Retention, the persona August pointed to; retention-marketing titles still drop on
`Marketing`, `Lifecycle` and `CRM`, and a bare retention title matches no line below.
`Member Experience` still comes through; at connected-hardware brands it often
names the support and delivery organisation, and step 4 sorts it by the profile (product or program
scope: `membership`; support or delivery: not the buyer). **Group C inside a parent:** Trainerize
(ABC Fitness) and TrueCoach (Xplor) people are pulled on the parent's page and kept only when the
profile names the coaching product; the parent's gym-software staff are out. **Volume (estimate,
not measured):** Peloton 60 to 120 rows, iFIT 30 to 60, each other company 3 to 25; about 350 to
700 rows in all and about 150 to 300 PASS. A company over 80 rows is re-run without the
`Senior Product Manager` and `Principal Product Manager` lines before step 4. A company with fewer
than 3 rows from Apollo waits for the Sales Navigator pull before it is dropped.

```titles
Chief Product Officer
VP Product
VP of Product
Vice President of Product
Vice President, Product
SVP Product
Head of Product
Director of Product
Product Director
Head of Digital Product
Group Product Manager
Principal Product Manager
Senior Product Manager
Head of Personalization
Director of Personalization
Chief Subscription Officer
Chief Subscription
Subscription & Retention
Subscription and Retention
Membership & Retention
Head of Subscription
Head of Subscriptions
VP Subscription
VP Subscriptions
Director of Subscription
GM Subscription
General Manager, Subscription
Head of Membership
VP Membership
Director of Membership
Chief Member Officer
Head of Member Experience
VP Member Experience
Director of Member Experience
Head of Coaching
VP Coaching
VP of Coaching
Director of Coaching
Head Coach
Coaching Lead
Coaching Operations
Chief Fitness Officer
Head of Fitness
VP Fitness
VP of Fitness
Director of Fitness
Head of Training
Head of Programming
Director of Programming
Fitness Programming
Head of Content
VP Content
Chief Content Officer
Exercise Science
Sports Science
Exercise Physiologist
Human Performance
Chief Science Officer
Head of Science
Head of Partnerships
VP Partnerships
VP of Partnerships
Director of Partnerships
Partnerships Director
Head of Business Development
VP Business Development
Director of Business Development
Head of Integrations
```

**`cap_per_group: 50`** (the default for every campaign; only Vadim changes it). At 50, Peloton and
iFIT can take up to 100 of the 200 to 300 expected SEND, a third to a half of the campaign; the
validator ranks their people by tier, and Risks 2 sets the stop rule. A soft cap stays Open
question 7.

## Company types in scope

### Groups and seed names (company-researcher verifies each; none is a confirmed lead)

- **A. Connected-fitness hardware with a paid membership app:** Peloton; iFIT (NordicTrack,
  ProForm); Tonal; Hydrow; Echelon; Ergatta; CLMBR and FORME (Interactive Strength); Bowflex (JRNY
  app; owned by Johnson Health Tech since 2024, check which entity runs the app in the US);
  FightCamp.
- **B. Coaching apps with a human or AI coach:** Future; Caliber; Trainwell; Ladder; Fitbod;
  RP Strength; Juggernaut AI.
- **C. Coaching platforms for trainers:** Trainerize (ABC Fitness); TrueCoach (Xplor); Everfit
  (check the HQ); Exercise.com; Playbook; CoachRx; TrainHeroic (Boulder, CO, per Dealroom); TeamBuildr
  (Silver Spring, MD, per its own site; it serves school and team strength coaches, so check that
  its users are adults, Anti-cases). For the last two, check that coaches record client body or
  check-in data, not only workout logs.
- **D. Workout and fitness-nutrition subscription apps with a premium plan:** MyFitnessPal;
  Lose It!; MacroFactor; Carbon Diet Coach; BODi (Beachbody); FitOn; obé; Alo Moves; Aaptiv; Jefit;
  V Shred; Centr (added by the coordinator 2026-11-19: the AU fix round found its head office in
  Los Angeles, [Athletech News](https://athletechnews.com/chris-hemsworth-fitness-app-centr-eyes-us-centralization-of-workforce/);
  no profile has contacted it). FitOn, obé and Alo Moves are class libraries first: IN only if the app runs a progress
  check-in of its own (Anti-cases, content-only). FitOn and obé were borderline on revenue in
  August, and Caliber (group B) had unverified revenue.
  **Aaptiv flag:** August's `companies.csv` (row 22) records its February 2026 pivot to an employer
  MSK product (AaptivMSK, [GlobeNewswire](https://www.globenewswire.com/news-release/2026/02/19/3241342/0/en/Aaptiv-Launches-New-MSK-App-in-Partnership-With-movr.html)).
  IN only if its consumer subscription app with a progress check-in still runs and the people
  pulled own it; the employer product is out (Anti-cases).
- **Step-2 re-checks, not exclusions:** Tempo (group A; a competitor's SDK announced in 2023: check
  that Tempo still trades and whether the scan is still in the member app) and FitnessAI (group B;
  its own BodyScan, from an undated release: check the current app listing). IN only if the scan is
  gone from the app; a live scan keeps the company out (Anti-cases).

Checks per company, each with a dated source: US HQ (not only US operations); a paid plan; a
progress or check-in feature in the app; not a marketplace, aggregator or content-only library; no
body scan in the member app today (app store listing, site, help centre); $1M+ revenue where it can
be estimated; not shut down. Give each company its
LinkedIn company URL: Future, Ladder and Echelon are common names, and Ladder Life (insurance, in
Nick's 2026-10-29 campaign) is a different company. A strong non-US fit is routed (UK `katerina`,
EU `olena`, LatAm and Mexico `katya`, Australia and New Zealand `vadim`), never force-fit. A
company with an ambiguous HQ (Everfit, or any company with two head offices) goes to one profile
only, agreed with the sibling campaigns. Centr is seeded in group D: the AU fix round found its
head office in Los Angeles. F45 is out in every sibling campaign (a gym
franchise; Anti-cases).

### Re-contact history (Vadim 2026-11-17: every company without a contract may be contacted again; 2026-11-19: new people only)

From `2026-08-07-us-digital-fitness` (nick); invites per company from the registry and the
post-mortem.

| Company | Group | August 2026 history | This campaign |
|---|---|---|---|
| iFIT | A | 56 invites; 2 replies: interested (Chief Subscription & Content Officer), referral (a senior content director, since laid off, who named a colleague) | IN, new people only. The interested person is not in this campaign; he goes to Nick for a personal follow-up (Vadim 2026-11-19). The named colleague is a new contact with normal qualification, if Nick has not messaged them before. Restructuring and a leadership change were reported in 2026: the Account facts round re-checks every P1 |
| Tonal | A | 21 invites, 0 replies | IN, new persona (no technical lane) |
| Hydrow | A | 17 invites, 0 replies | IN |
| Echelon | A | 10 invites, 0 replies | IN |
| Future | B | 13 invites, 0 replies | IN |
| Ladder | B | 9 invites, 0 replies | IN (not Ladder Life) |
| Fitbod | B | 6 invites, 0 replies | IN |
| Trainwell | B | 3 invites, 0 replies | IN |
| MyFitnessPal | D | 28 invites; 1 reply, from a director who had left | IN |

Not re-opened, because they are outside this segment: Personify Health (63 invites, 2 replies;
employer wellness), Calibrate (14 invites, 1 evaluation question; weight-loss medicine), Found
(6, 0) and Shotsy (2, 0). Researched in August and never contacted (no registry entry): Peloton,
Caliber, BODi, Aaptiv, FitOn, obé, Jefit, V Shred, Lose It!. Noom, WW and Ro were researched too
and are out (Anti-cases). Nick's other campaigns of 2026 (obesity medicine, cardiometabolic, Virta,
Options, employer obesity care, men's health, insurance underwriting) share no company with this
list. The company-level block for the nine re-contacts is lifted at step 4 with
`outbound-registry.py check --waive-companies "iFIT,Tonal,Hydrow,Echelon,Future,Ladder,Fitbod,Trainwell,MyFitnessPal"`
under Vadim's rule (2026-11-17, reconfirmed 2026-11-19: companies without a contract return with
their history shown).

### People-level exclusions

- Only new people (Vadim 2026-11-19): everyone `nick` has already messaged, in August (248 people)
  or in any other campaign, stays out; the registry check flags them.
- People who replied in August, such as the iFIT person who replied interested, are never in this
  campaign's import; they go to Nick for a personal follow-up.
- People who left or were FAIL in August stay out (registry).
- Staff of customers with a contract (Zing Coach, Verv, Erakulis): never.
- People at US companies located outside the United States: FAIL (Location rule).

## Outreach language

American English. Nick writes as a business development lead at 3DLOOK to a product, coaching or
subscription owner: peer register, plain and specific, first names, no enthusiasm words. No "thanks
for connecting" opener and no thanks for accepting. At the nine re-contact companies nothing refers
to an earlier message, campaign, reply or person; each message reads as a first message. Use the
reader's words: member, membership, check-in, program block, coach, paid or premium plan,
onboarding, progress screen, strength. Never clinical words: patient, clinician, treatment,
eligibility, BMI verification.

## Message angle: lanes and account facts

Every person gets exactly one lane, spelled as below. Lane notes and targets are instructions to the
writer; none of their sentences goes into a message.

**The angle, for every lane (topic targets, not copy; each writer finds new words for each
person).** Across a pair, the messages establish: (1) the check-in this company's members already
do and what that method leaves unmeasured (one pain target from Rules); (2) the mechanism: where
the scan runs, what the member does and what comes back to the company; (3) where the record is
used, chosen by lane: the progress screen, the coach's next program block, or the paid plan (the
Pro-plan 3D tools); (4) retention and free-to-premium conversion only as what a cohort pilot would
measure, never as an effect of the scan.

**Lanes:**
- **`product`** Target: where a body check-in would sit in this app and what it adds to the progress screen. Question targets: what a member sees at the first check-in today beyond weight and workouts; whether a scan belongs at onboarding or at the first check-in; how the team tests a new onboarding step; how the app keeps progress photos or measurements now; which screens around a fixed capture (onboarding, consent, results) the team would want in its own brand. Message 2 value targets (one or two that Message 1 did not use): the SDK and API setup (capture layer fixed; onboarding, consent and results screens the company's own); the scan ID that links each record to the member profile; the timestamped record with its processing status; the measurements a progress screen could show (waist, hip, chest, thigh, calf, fat and lean mass estimates); speed from the photos to structured results; the pilot design.
- **`membership`** (TEST: the rewritten retention angle, Learnings applied HYP-6) Target: what a measured check-in adds to the paid membership. Question targets: what the premium plan includes today and what members upgrade for; which first-month moment the team watches; how a new paid feature is judged before rollout; where progress features sit between the free and the paid plan. Message 2 value targets: the pilot design with free-to-premium conversion where 3D progress sits in the paid plan; the pilot design with day-30 and day-90 retention against a comparison cohort; 3D Body Progress tracking and 3D Goal Visualization as paid-plan features (Pro plan); success criteria agreed before the pilot starts; no integration fee (once, Message 2 only). Never a churn figure, never a claim that the scan lifts retention.
- **`coaching`** Target: what the coach or the program uses to set the next block. Question targets: what coaches look at in a check-in today (weight, photos, the member's notes); how often a program block is reviewed; what a coach would do with waist, hip and thigh changes and fat and lean mass estimates; at group C, what trainers ask the platform to record for their clients. Message 2 value targets: one timestamped record that the coach and the member both see, comparable from one check-in to the next; the repeatability sentence; the measurements a coach could review (girths and lengths, fat and lean mass estimates); guided capture on the member's phone between sessions; at group C, one integration that reaches every trainer's clients; the pilot design.
- **`science`** Target: what the record contains and what it is not. Question targets: what the team would need to see before body data shapes a program; how it treats estimates next to measured values; which measurements matter for its training method. Message 2 value targets: estimates derived from the measurements with height and, where provided, weight; the repeatability sentence; methodology under NDA; the boundary sentence; which of the 80+ body measurements are girths, lengths and widths, and that BMI and BMR are calculated metrics.
- **`leadership`** Target: a body check-in under the company's own brand, on the member's phone, as a feature the company owns, with a pilot before any rollout. Question targets: the member promise or roadmap item a measured check-in would serve; how the company decides on a new member feature. Message 2 value targets: the pilot design; no integration fee (once); the client-count line; white-label ownership of the scan and its record; no hardware and no club visit.
- **`partnership`** Target: one integration offered to members or, at group C, to every trainer on the platform. Question targets: how a partner capability enters the app or the integrations marketplace; what trainers or members ask for most around progress. Message 2 value targets: web and mobile SDKs with iOS and Android; one structured record per scan through the API; white-label screens; the scan ID linked to the member or client profile; the pilot design.
- **`referral`** Target: the angle targets above, built around the person's own work, and one question about it in Message 1. Message 2: a value point that continues their question, the call offer with the calendar link, and an easy out pointing to the owner of one topic, chosen by the company and the person's function: the member app's progress experience, onboarding, the paid plan, the coaching programs (group B) or partner integrations (group C). An easy-out target may repeat at one company when it fits (Vadim 2026-11-20); its wording is never repeated.

**Question bank discipline.** Each person gets their own question, built from their title and
profile; its wording is never reused at the company. A question target, pain target, Message 2
value point, easy-out target or order of Message 1's parts may repeat at one company when it fits
each person (Vadim 2026-11-20, the ratio is withdrawn); wording, hook, opener and closer never
repeat at one company (Rules, Several people at one company).

**Name forms for Message 1** come with Account facts: the form the person's own profile uses (iFIT
people may work under NordicTrack or ProForm; Trainerize people under ABC Fitness).

### Account facts

Company facts for message writers, one bullet per group with SEND people in `people-validated.csv` (22 groups), from the research of record `companies.md` (2026-11-19) and two parallel web re-checks on 2026-11-20 (coordinator merge). Writers take company facts only from here, lean only on what a bullet's Use: allows, and treat each Never: as a hard stop. A fact older than about 12 months, or a page with no date, is described as how the company works, never as news.

None of the 22 companies runs member clubs or studios: the in-club scanner pain and the "between club visits" point are off for every account; "between sessions" (coach or trainer sessions) stays allowed only where a bullet says so. In these apps "scan" already means a meal, barcode, label or equipment scan: copy always says "body scan" for ours.

Never as a fact, for every account: figures about the company (members, subscribers, churn, revenue, prices, valuations, staff, layoffs); funding, ownership, deals and investors in either direction; lawsuits, recalls and product safety notices; another prospect's name; the company's vendors, SDKs and hardware makers; any earlier contact with 3DLOOK. Prospects in this list are linked to each other, so each side is Never in the other's copy: Trainwell powers Peloton's personal-trainer product (2026-02-17) and partners with Lose It! (2026-06-04); MyFitnessPal is an integration partner of Trainerize (ABC Fitness) and of Everfit; Carbon publishes a Carbon-vs-MyFitnessPal comparison; iFIT and Ergatta share content licensing and racing cups; Echelon's gym white-label app integrates ABC Fitness; Tony Horton (BODi's P90X) returned to Tonal in March 2026. Interactive Strength owns FORME, CLMBR, Wattbike and Ergatta: copy names the brand the person works on, never the holding company, its ticker or the deal.

- **Peloton:** On September 22, 2026 Peloton launched three treadmills and new Peloton IQ features for runners, walkers and hikers, live from October 1: Run Analysis (running-form feedback from a movement-tracking camera on the Vision models), IQ Pace Targets (speed ranges set from recent runs) and ReRuns (https://athletechnews.com/peloton-all-in-on-running-new-treadmills-ai-powered-running-features/; https://secure.businesswire.com/news/home/20260922228360/en/Peloton-Launches-Foldable-Peloton-Tread-Flex-Its-Most-Affordable-Treadmill-Ever-and-New-AI-Powered-Coaching-Features-for-Runners-Walkers-and-Hikers). On August 20, 2026 its Strength+ app reached Android after nearly two years on iPhone: self-paced multi-week strength programs, a workout generator and in-ear form guidance (https://9to5google.com/2026/08/20/peloton-strength-plus-android-app-release/). Peloton IQ itself (personalised guidance, weight suggestions, form feedback and rep counts on camera-equipped hardware) launched on October 1, 2025 (https://www.axios.com/2025/10/01/peloton-cross-training-ai-bike): how Peloton works now, not news. Clubs or studios: no member clubs; its production studios and gym-floor equipment are not member check-in points, so no between-visits line. At a check-in today: the Peloton app (v15.137.0, 2026-11-16) tracks classes, outdoor activities, stats and progress (https://apps.apple.com/us/app/peloton-fitness-workouts/id792750948); Strength+ (v1.17.0, 2026-10-26) logs weights and reps to show progress (https://apps.apple.com/us/app/peloton-strength/id6476712925) and is included for All-Access, Guide and App+ members (https://www.onepeloton.com/blog/peloton-strength-plus-app, undated). No body measurement or body scan in either listing or in 2026 coverage. Role check: Nick Caldwell is Chief Product Officer on Peloton's leadership page (fetched 2026-11-20, https://www.onepeloton.com/company/team). No P1 in this group. Cole Shipley (enterprise platforms) is a stale-person risk: Peloton cut about 11% of staff on January 30, 2026, mostly engineers on technology and enterprise work (https://www.bnnbloomberg.ca/business/2026/01/30/peloton-cuts-11-per-cent-of-staff-in-cost-cutting-push-spokesperson-says/). Ben Schultz is not confirmed (WEAK, keep out). Name form: Peloton. Use: Peloton IQ's personalised guidance and what a member sees after a strength block, for Nick Caldwell and Brent Tworetzky (different angles); Strength+ weight and rep logging and its Android launch, for Yasmin Kothari and Jon Cilley; IQ Pace Targets and Run Analysis as training metrics (the work done, not the body change it is for), for Eugene K. and Meg Higgins; the member app's progress screen as a route to its owners, for Cole Shipley; what Strength+ adds to an All-Access or App+ membership, for Mirela C. (membership); how members describe progress in research and field testing, for Laura Rivera and Beth Wendt; the strength and running push as a strategy question, one angle each, for Ted Lui, Lindsay Pontello, Barbara Thorne-Thomsen, Sarah Rodenberg and Kavita Vemishetti; one partner capability inside the member app, for Brad Fagan, Jacob Wax and Joeli Spencer. Never: any figure (members, paid subscriptions, churn, the share of members using Peloton IQ, prices, revenue, staff); the January 2026 cuts and earlier restructurings; recalls and product safety; Precor, the Commercial Series, Peloton for Business and gym placements; Skop and any acquisition; shareholder letters, executive quotes and the GLP-1 framing; executive appointments (Peter Stern, Sarah Robb O'Hagan, Sid Thacker and others); Apple Watch, Apple Health, Strava, Zwift; former employers SoulCycle, Bumble, Asana, Parsley Health, Mez Foods; any other prospect (Echelon, Tonal, iFIT, Hydrow, Trainwell among them).
- **Tonal:** On July 22, 2026 Tonal made Tia, the Tonal Intelligent Assistant in its mobile app, available to all members: Tia works from each member's training data, reports volume, strength and power PRs, milestones and muscle readiness, recommends the next workout or program, and remembers goals and limitations; Tonal's own example prompt is a member who finished a lean program asking what to do next "to keep shifting body composition" (https://tonal.com/blogs/all/meet-tia-your-new-tonal-intelligent-assistant, update dated 7/22/26). On March 16, 2026 Tonal announced new coaches and a slate of structured progressive programs (a HIIT and strength hybrid, a muscle-building block, advanced Pilates, strength for performance, mobility and longevity, and women's strength across life stages) to help members train with purpose and track progress over time (https://athletechnews.com/tonal-tony-horton-new-coaching-roster-programming/). Tonal Rent launched in July 2026 (https://athletechnews.com/tonal-launches-rental-program-first-major-move-under-new-ceo/). Clubs or studios: no; no between-visits line. At a check-in today: the Tonal app (v8.44.0, 2026-11-05) tracks workouts, breaks progress down by muscle group and workout type, and syncs weight and height through HealthKit (https://apps.apple.com/us/app/tonal/id1437460744); Smart View form feedback on the machine; no body measurement or scan found. Role check: Jonathan Shottan is Chief Product and Content Officer on tonal.com/about (fetched 2026-11-20, https://www.tonal.com/about/); Jenna Moore spoke for Tonal on 2026-03-16 as senior manager of performance and talent (Athletech URL above), so she is still there (use her profile's current title). The CEO changed in February 2026 (already contacted, not in this list). No 2026 layoffs found. Name form: Tonal. Use: Tia's view of a member's PRs and muscle readiness, and members asking about body composition after a program, for Jonathan Shottan; progress by muscle group in the app, for Anna Furr; the 2026 progressive programs and how a block's result is judged, for Jenna Moore and Maureen Key (a different program each); the programs they lead and the point where members ask about results, for Joe Rodonis and Tanysha Smith (coaching, Vadim's pool C); member questions after a program ends, for Amar Tanna (referral). Never: any figure (members, program lengths in weeks, prices, rental prices, revenue, staff); the CEO change and earlier leaders; the 2022 and 2023 layoffs; funding, owners and valuations; the WeWork partnership; Tony Horton and other named coaches (Horton is tied to another prospect's program brand); the 2023 talks with another connected-fitness company; Apple Health; former employer Exos; any earlier contact (Tonal is a re-contact company); any other prospect.
- **iFIT:** iFIT's AI coach now has its own app, iFIT Personal Trainer (v2.0.0, 2026-11-11), which builds personalised workouts and a weekly plan around a member's goals, fitness level, schedule, health data and progress; the latest release adds a Consistency Accelerator (a streak built by finishing workouts within a week) and scheduling from the plan (https://apps.apple.com/us/app/ifit-personal-trainer/id6756594504). On July 23, 2026 iFIT announced that coach on a phone maker's health app (search result; ifit.com blocks this server): a partner deal, context for this file only. The main iFIT app (v3.9.0, 2026-08-06) bases future workouts on recent performance, runs multi-week trainer-led programs and shows personal workout stats and insights in the app and on iFIT-enabled machines; one iFIT Pro membership covers several household users (https://apps.apple.com/us/app/ifit-workouts/id1274601042). Clubs or studios: none of its own; no between-visits line. At a check-in today: workout stats, streaks, a weekly plan and insights; no body measurement or scan in either listing. Role check: no P1 or C-level person in this group; CEO Kevin Duffy was quoted in iFIT's April 7, 2026 announcement (https://www.ifit.com/blog/ifit-marc-washington-president-cfo-announcement; already contacted, not in this list). No 2026 layoffs found. Heather Guymon, Jordan Annis and Emily Baldwin are not confirmed (WEAK, keep out). Name form: iFIT (NordicTrack or ProForm only where the person's own profile uses it). Use: the AI coach's weekly plan built from progress, and where a measured check-in would feed it, for Shayne Jessop; the main app's progress tracking and stats, for Sarah Miles; trainer-led multi-week programs and how a series' result is judged, for Stephanie Raterman; the first weeks of an iFIT Pro membership (onboarding and the streak feature), for Danielle Peckskamp (membership); one partner capability inside iFIT Pro, for Danaé Hirsch. Write "iFIT's AI coach", never its product nickname. Never: any figure (members, subscribers, workouts in the library, users per membership, prices, revenue, staff); restructuring, layoffs, the 2022 capital raise, lawsuits and the founder's exit; executive appointments (Marc Washington, Jeremy McCarty and others); partners and licensors (Samsung, Google Maps, Tour de France, F45, Xponential, Club Pilates, YogaSix, marathon brands, Ergatta and its racing cups, MyFitnessPal, Apple Health); Freemotion; any earlier contact (iFIT is a re-contact company); any other prospect.
- **Echelon:** On August 10, 2026 Echelon launched Echelon Workout Builder AI, an app that builds adaptive strength and recovery programs around each user's goals, experience, readiness, time and equipment, adjusts future programming from performance and feedback, and works at home, while travelling or in a gym (https://apnews.com/press-release/ein-presswire-newsmatics/press-release-fcdb831f186f01b815ef98351e3a0936). On June 9, 2026 it launched the Meridian Reformer, a connected Pilates reformer with personalised programming (https://www.prnewswire.com/news-releases/echelon-unveils-the-meridian-reformer-redefining-connected-pilates-for-the-modern-home-302794854.html). Echelon Coach, its one-to-one virtual personal training and wellness coaching service, has carried that name since March 2025 (https://athletechnews.com/echelon-acquires-flexit-to-expand-personalized-training/): how Echelon works. Clubs or studios: no clubs of its own (it sells equipment to gyms and films classes in studios); no between-visits line. At a check-in today: the Echelon Fit app (v2.12.10, 2026-11-19) shows live, on-demand, scenic and FitPass classes, personal bests, global leaderboards and challenges (https://apps.apple.com/us/app/echelon-fit/id1262424186); Workout Builder AI adjusts the next week from performance; no body measurement or scan found. Role check: founder and CEO Lou Lentine was quoted in the August 10, 2026 release (already contacted, not in this list). Kevin Custer's Chief Content Officer appointment comes from a 2020 release (https://prnewswire.com/news-releases/echelon-fitness-expands-leadership-team-appointing-chief-marketing-officer-chief-content-officer-more-301120105.html) and was not re-confirmed by a 2025-2026 source; John Santo (co-founder, CPO) was not found on the web; both rest on their November 2026 Sales Navigator titles. Lisa Privitera: confirmed program-side (owner of the Echelon Coach service, not on-camera talent), promote to `coaching`; William Feroe: not confirmed, keep out. Name form: Echelon (William Feroe's profile uses Echelon Fit Multimedia LLC). Use: Workout Builder AI's adaptive week and where a body check-in would sit in it, for John Santo; personal bests and leaderboards in the Echelon Fit app as training metrics, for Patrick Matthews; the class and program library and how a program's result is judged, for Kevin Custer and Becca Valente (different angles); Echelon Coach's one-to-one trainers and what they review between sessions, for Lisa Privitera; one partner capability inside the membership, for Heidi Jones. Never: any figure (classes, prices, membership price, revenue, staff, beta-test strain scores); the FlexIt and Fortë acquisitions; the DOJ tariff settlement and any lawsuit; the gym white-label product and the club-software names it lists (ABC Fitness is another prospect's parent); gym access inside Echelon Coach; WHOOP, Apple Health, Primal, runDisney and other partners; supplements, plunges and saunas; former employers Peloton, Flywheel, FlexIt; any earlier contact (Echelon is a re-contact company); any other prospect.
- **Hydrow:** No dated 2025-2026 company news was found (hydrow.com blocks this server). Hydrow launched its Arc rower on September 16, 2025 and said strength training would follow in early 2026 (https://www.businesswire.com/news/home/20250916204390/en); its site now sells LYQUID, a freestanding adaptive strength platform used with the membership (https://hydrow.com/products/strength/lyquid/, undated), and a Core rower sold with no membership required (https://hydrow.com/blog/introducing-hydrow-core-a-premium-rower-no-membership-required, undated). All three are how Hydrow works, never news. Clubs or studios: no; no between-visits line. At a check-in today: the Hydrow app (v1.84.0, 2026-10-29) offers on- and off-rower workouts led by athletes, performance tracking, racing stats and teams, and Apple Health integration (https://apps.apple.com/us/app/hydrow/id1458653991); no body measurement or scan found. Role check: Matt Lehrer appears on Hydrow's team page as Chief Experience Officer (search snippet of https://hydrow.com/our-team, undated) while his Sales Navigator title is Chief Rowing Strategy Officer: he is at Hydrow; use his own profile's title. Rianita Ummah has no web footprint (WEAK, keep out). Name form: Hydrow. Use: rowing and strength programs led by athletes, and what a member sees after a block beyond stroke, split and racing metrics, for Matt Lehrer. Never: any figure (workouts in the library, prices, membership price, resistance figures, revenue, staff); funding rounds, investors and celebrity investors; Concept2, Strava, Apple Health; any earlier contact (Hydrow is a re-contact company); any other prospect.
- **Ergatta:** On October 14, 2026 Ergatta released two Push Programs: Endeavor: Proving Grounds, a path through Endeavor, its newest game, from beginner to intermediate opponents, and Classes: Cadence Control, in which instructors teach stroke-rate control; an August 27, 2026 rower update standardised in-game metrics across experiences and redesigned the pause screen, and new scenic rows and coached classes were added (all from a group update published in November 2026, https://finviz.com/news/406601/trnr-shares-q3-commercial-update-across-its-premium-portfolio, a source for this file only). Game-based rowing on its own connected rower is how Ergatta works (https://ergatta.com/pages/about-us). Clubs or studios: no; no between-visits line. At a check-in today: the Ergatta app (v2026.36.001, 2026-09-16) shows a dashboard, personal records, monthly, weekly and daily stats, rankings by age group, gender and weight group, and challenge progress (https://apps.apple.com/us/app/ergatta/id1573791266); no body measurement or scan. Role check: Tom Aulet is Co-Founder & CEO on ergatta.com (fetched 2026-11-20) and was presented as Ergatta's CEO on 2026-03-17 (https://www.newswire.com/news/trnr-exhibits-at-hfa-2026-with-all-four-brands-and-strong-leadership-presence). Alessandra Gotbaum (COO) and Prasanna Swaminathan (CTO) appear only in undated third-party profiles (https://crunchbase.com/person/alessandra-gotbaum; https://6895eddcc5a59a0008124e78--theorg.netlify.app/org/ergatta/org-chart/prasanna-swaminathan) and were not re-confirmed after the March 2026 ownership change. Name form: Ergatta. Use: the game-based programs and what a member sees beyond splits and rankings, for Tom Aulet; the program path from beginner to intermediate and how a member's progress along it is judged, for Alessandra Gotbaum; the in-game metrics update and where a body record would sit beside the stats dashboard, for Prasanna Swaminathan; the stats dashboard and the weight the rankings already ask members for, for An Li; member questions about results, for Luana Perez (referral). Never: the parent company, its name or ticker, the acquisition and its terms; FORME, CLMBR, Wattbike, STEPR and Sportstech; the content licensing and the virtual-racing cups with another connected-fitness company (iFIT, NordicTrack, ProForm); any figure (program lengths, battles, classes, prices, membership price, revenue) and any retention or engagement claim; Fortune and other rankings or awards; Concept2; any other prospect.
- **Interactive Strength (FORME, CLMBR):** The FORME app (v6.0, 2026-11-11) gives each member a dedicated trainer, live one-to-one sessions, messaging, a personalised plan every week and progress tracking toward goals (https://apps.apple.com/us/app/forme-personal-training/id1532950399); FORME's wall-mounted Studio (a smart fitness mirror for guided programming and live one-to-one personal training) and Lift (smart cable resistance) are described in a group update published in November 2026 (https://finviz.com/news/406601/trnr-shares-q3-commercial-update-across-its-premium-portfolio). On November 6, 2026 CLMBR's companion app was rebuilt as a native iOS app; it shows workouts, challenges and classes (https://apps.apple.com/us/app/clmbr/id1528650643). Clubs or studios: none of its own (both brands also sell into commercial settings); no between-visits line. At a check-in today: on FORME, the trainer's weekly plan and progress toward goals; on CLMBR, workouts, challenges and classes; no body measurement or scan. Role check: Trent Ward is CEO in the November 2026 update (URL above) and in the 2026-03-17 release (https://www.newswire.com/news/trnr-exhibits-at-hfa-2026-with-all-four-brands-and-strong-leadership-presence); Ben Bartlett, a FORME co-founder, became President and COO on June 14, 2025 (https://www.tipranks.com/news/company-announcements/interactive-strength-inc-appoints-new-coo-and-president); Deepak M. (Board Member, CTO) was not re-confirmed on the web. Name form: FORME or CLMBR, the brands members use; never the holding name or ticker. Use: FORME's trainer-led weekly plan and the check-in a trainer runs before the next plan, for Ben Bartlett; a body check-in that FORME and CLMBR own under their brands, piloted before rollout, for Trent Ward; the rebuilt CLMBR app and the FORME app's progress view, for Deepak M. Never: the holding name or ticker, revenue guidance, quarterly results and any figure; acquisitions done or pending and the M&A pipeline; Ergatta, Wattbike and STEPR; Rogue Fitness, EGYM and other retailers or partners; hardware and membership prices; any other prospect.
- **Centr:** Centr's site (fetched 2026-11-20, undated) calls its training app Centr Coach, on iOS and Android, with programs built around a member's goals, fitness level and equipment, and sells strength, cardio and recovery equipment that works with the app as one connected system (https://centr.com/about). The App Store listing (v10.9.1, 2026-11-16) describes personalised training by goal, preference and skill level, coached and self-guided workouts, a daily workout and meals selected for the member, results tracking, and Apple Watch and Apple Health support (https://apps.apple.com/us/app/centr-strength-fitness-app/id1382530817). No dated 2025-2026 company news was found; the Los Angeles head office rests on 2023 reporting (https://athletechnews.com/chris-hemsworth-fitness-app-centr-eyes-us-centralization-of-workforce/), and the app's publisher is an Australian entity. Clubs or studios: no; no between-visits line. At a check-in today: workout and meal plans, tracked results and workout history; no body measurement or scan found. Role check: Andrew Sugerman was CEO in 2023 and March 2025 reporting (https://www.fittechglobal.com/fit-tech-news/Chris-Hemsworth-app-Centr-unveils-new-strategy-to-broaden-reach/355300), not re-confirmed for 2026; Nicholas Robinson (President, Digital, P1) and John Rafferty (VP of Product, P1) were not found on the web and rest on their November 2026 Sales Navigator titles. Jeff Laborde is confirmed as President on the equipment side, not the app (keep out). Name form: Centr (Centr Coach for the app). Use: Centr Coach as the paid app that picks a member's daily workout and meals, and where a body check-in would show what that plan changed, for Nicholas Robinson; the app's results tracking and the point where a member finishes a program, for John Rafferty and Laura Ruiz (different angles); a check-in under Centr's own brand, piloted before rollout, for Andrew Sugerman; member questions about results, for Megan Johns (referral). Never: Chris Hemsworth and the named coaches; HighPost, the Bezos family and any owner or investor; HYROX and other partners; Inspire Fitness and equipment suppliers; the 2023 Australian job cuts and the publishing entity; prices and any figure; former employers Zero and Precor; any other prospect.
- **BODi (The Beachbody Company):** BODi's app release of November 19, 2026 makes logging measurements faster: members now type their numbers in instead of scrolling a picker (https://apps.apple.com/us/app/bodi-fitness-home-workouts/id1031660123); the app carries step-by-step fitness and nutrition programs and workouts with or without equipment. On February 3, 2026 BODi launched P90X Generation Next on its digital platform (https://www.businesswire.com/news/home/20260203008008/en/BODi-Unveils-P90X-Generation-Next-the-Next-Evolution-of-the-World%E2%80%99s-Most-Iconic-Extreme-Home-Fitness-Program). In 2026 it expanded its line of short 10 Minute BODi workouts (https://insider.fitt.co/press-release/bodi-expands-glp-1-support-and-longevity-driven-fitness-with-10-minute-bodi-workouts/), context for this file only because the release's framing is banned. Clubs or studios: no; no between-visits line. At a check-in today: members type body measurements into the app by hand (the November 2026 release), next to program progress; no body scan. Role check: no P1 or C-level person in this group; Carl Daikeler spoke as CEO in July 2026 (https://www.nutraingredients.com/Article/2026/07/31/nutracast-bodi-ceo-on-keeping-active-nutrition-simple-amid-ai-glp-1s-and-wellness-trends/). Nate Silva and Yi Chang are not confirmed (WEAK, keep out). Name form: BODi (Beachbody only where the person's own profile uses it). Use: the hand-typed measurement log and what one measured record per check-in would add to it, for Mike Farrell and Rob Canning (different angles); P90X Generation Next and how a program shows its result, for Jeffrey Scott and Stephanie Saunders; program progress screens, one angle each, for Hunter Owens, Ashlei Mitchell and Brandon Cowley; onboarding into a digital plan, for Vijay Muthuraman; what a program promises to show and how production supports it, for Jenny Parker; the app's roadmap, for Marietta P. and Nicholas Willey. At BODi "coach" long meant the former network sellers: write program, trainer or the member's own record, never "your coaches". Never: GLP-1 and the 10 Minute BODi framing; Q3 2026 results, subscription counts, revenue, prices and any figure (programs, workouts in the library); the network-marketing past, the rebrand and the CEO's interviews; supplements, Shakeology and other nutrition products; the Reebok app partnership and other partners; Tony Horton (now with another prospect); any other prospect.
- **Caliber:** Caliber's app (v5.18.0, 2026-11-03) is a free strength app with coach-designed plans, personalised progress tracking, nutrition targets, progress photo uploads (the latest release compresses them) and body stats synced from a wearable or connected device; Premium Coaching pairs a member with a personal trainer for a custom training and nutrition plan, chat and video messages, and weekly progress reviews (https://apps.apple.com/us/app/caliber-strength-training/id1482405410). On February 26, 2026 Athletech News described the model: a free app for logging and self-guided plans, with one-to-one coaching as the paid upgrade (https://athletechnews.com/age-of-ai-human-personal-trainers-might-become-a-luxury-future-caliber/). Clubs or studios: no; no between-visits line. At a check-in today: the coach's weekly progress review, built on logged training, synced body stats and progress photos; no body scan found. Role check: Chris Muir (CPO, P1), Justin Fauci (CTO) and Jared Cluff (CEO) are the co-founders (https://techcrunch.com/2020/10/13/caliber-with-2-2-million-in-seed-funding-launches-a-fitness-coaching-platform; https://www.crunchbase.com/organization/caliber-fitness); no 2025-2026 source re-confirms their roles, and the app was updated in November 2026. Name form: Caliber. Use: the weekly progress review and the photos and body stats it rests on, for Chris Muir; the step from the free app to paid coaching and what a measured check-in adds to the paid plan, for Jared Cluff; where synced body stats and photos sit in the app's data, for Justin Fauci; the progress tracking screen, for Anna Kate Davis. Never: prices and any figure (exercises, ratings, funding); funding and investors; ChatGPT, Claude, wearables and other integrations; Trustpilot; named coaches; Lean Muscle Project; Future (covered in the same article, another prospect); any other prospect.
- **Future:** On June 19, 2026 Athletech News reported that Future dropped its AI training beta and doubled down on human coaches through Future Pro: weekly check-ins, a monthly one-on-one call and a weekly food log review on the core plan, daily check-ins and weekly calls on the top plan, and a new service combining movement, nutrition, sleep, recovery and preventive health due later in 2026 (https://athletechnews.com/future-pulls-the-plug-on-ai-personal-training-commits-to-human-coaches/). Both plans also include lab body-composition scans (same source): Future already measures body composition outside the app, so copy never contrasts the scan with any lab measurement and never implies Future lacks body data. The Future Pro app (v2026.21, 2026-10-28): the coach checks in, monitors progress and refines the plan; visualized workout reports; Apple Watch (https://apps.apple.com/us/app/future-pro-personal-training/id1288178982). Clubs or studios: no; no between-visits line. At a check-in today: the coach's weekly check-in and workout reports in the app. Role check: no P1 in this group; future.co/about (fetched 2026-11-20) lists CEO Ali Jafari and CPTO Meredith Harris, both already contacted (registry). Name form: Future (Future Pro for the app; LinkedIn slug future-fit). Use: the weekly check-in and what the coach sees in it, for Jake Grundstein (membership); visualized workout reports and the progress view, for Jake Quan; one partner capability inside Future Pro, for Jason Hwang. Never: DEXA, labs, dietitians and supplements; the AI beta and its cancellation; the Autograph merger, Tom Brady and other investors or advisors; prices and plan prices and any figure; survey figures; Caliber (another prospect, same article); former employer Nextdoor; any earlier contact (Future is a re-contact company).
- **Trainerize (ABC Trainerize; parent ABC Fitness):** What it is, how it works: ABC Trainerize is personal-training software; trainers build workout, nutrition and habit programs, message clients and deliver all of it in a client app that can be the trainer's own white-labelled, custom-branded iOS and Android app (https://www.trainerize.com/about/, https://www.trainerize.com/features/, undated). Progress tools in the client app: body stats, body measurements, progress photos with side-by-side comparisons, weight and body-fat tracking, habits and workout adherence (July 14, 2026, https://www.trainerize.com/blog/client-progress-tracker/; App Store listing, version of 2026-11-14, https://apps.apple.com/us/app/fitness-app-abc-trainerize/id516851502). Dated 2026 facts: the January 18, 2026 roadmap product chat, with Kelly Card as SVP of Product at ABC Trainerize, lists Check-In Forms (shipped 2025) and "continued evolution of check-in forms and habit tracking" plus a redesigned client app for 2026 (https://www.trainerize.com/blog/abc-trainerize-2026-product-roadmap/); on August 3, 2026 the trainer's Insights Dashboard became customizable, with new Lean Mass, Resting Heart Rate and web Progress Photo Comparison widgets (https://www.trainerize.com/blog/july-2026-trainerize-updates-insights-business-nutrition/); on September 19, 2026 trainers got editing of a client's submitted check-in or onboarding form and Body Weight with Weekly Average on one graph (https://www.trainerize.com/blog/new-abc-trainerize-updates-august-2026-save-time-support-client-progress-and-keep-clients-engaged/); on November 9, 2026 the mobile app added Spanish and Portuguese (https://www.trainerize.com/blog/new-abc-trainerize-updates-coach-more-flexibly-stay-connected-and-get-more-done-with-ai-tools-you-already-use/). How partners get in: Trainerize's integrations page connects wearables, nutrition apps, payments, scheduling and automation (https://www.trainerize.com/integrations/); ABC Fitness runs a Partner Program and Partner Marketplace for native or API-based integrations with a partner registration route (https://abcfitness.com/partners/, undated). No body scan found in the client app, the integrations page or the partner page (2026-11-20). Clubs or studios: none of its own; gyms and studios are customers and many trainers coach in person and online, so "between sessions" is allowed, the in-club scanner and club visits are not (gyms are out of the segment). What a client's check-in shows today: a weigh-in on a weight-and-weekly-average graph, body stats and tape measurements, progress photos compared side by side, lean mass where a device syncs it, and the trainer's custom check-in form. Role check: Finn Hegarty is quoted as Chief Product Officer of ABC Fitness on March 16, 2026 (https://abcfitness.com/press-release/abc-fitness-ai-infrastructure/), CONFIRMED. Kelly Card is SVP of Product at ABC Trainerize in the January 18, 2026 roadmap post, CONFIRMED: he is the one person in pool A shown on Trainerize's product, so order him first. Keegan Dowling, Eric Reimers, Laurie Kemp, Doug Reeder, Jennifer Pelton, Tristan Alexander, Zeke Brustkern, Kendall Wilson and Elizabeth Gray have no public web record beyond LinkedIn (searched 2026-11-20); none found to have left. Name form: "ABC Trainerize" or "Trainerize"; "ABC Fitness" only as the reader's own employer, tied to Trainerize. Use (one topic per person, all about Trainerize and the trainers and clients on it): Kelly Card, the 2026 check-in-forms work and the redesigned client app, and where a body check-in would sit in that flow; Finn Hegarty, a body check-in that every trainer can switch on inside their branded client app, under the trainer's brand; Doug Reeder, how a body check-in and the Pro-plan 3D progress tools would be packaged in the Trainerize product line; Elizabeth Gray, what a measured record adds to the trainer's Insights Dashboard next to the lean-mass and photo-comparison widgets; Jennifer Pelton, a guided capture at the onboarding form or the check-in form; Zeke Brustkern, one timestamped record per scan through the API, linked to the client profile by the scan ID; Kendall Wilson, what the weight and weekly-average graph leaves unmeasured; Tristan Alexander, side-by-side progress photos that show change but return no measurement; Keegan Dowling, one integration through the partner route that reaches every trainer's clients; Laurie Kemp, what a partner integration brings (iOS and Android SDKs, white-label screens, the API record, the scan ID); Eric Reimers, building a body check-in versus integrating one, for Trainerize's clients. Never: ABC's club-management, billing, booking, payments and operator software and every other ABC brand or product, named or described; gyms, clubs, studios or operators as the audience; ABC's March 2026 AI-infrastructure launch for operators; the 2020 acquisition and any ABC investor or deal; any integration or partner by name or kind (the nutrition-app integration, the supplement affiliate program of 2025-10-30, education partners, wearable and scale makers, gym-software and automation connections, the November 2026 AI-assistant connection); MyFitnessPal and Everfit (prospects; MyFitnessPal is a Trainerize integration partner); every figure on Trainerize pages (trainers, clients, workouts, meals, hybrid share, Apple-device share, referral conversion, build-time reduction, client limits); Trainerize's Canadian origin and its non-US teams; the co-founder and president and ABC's chief strategy officer (colleagues); the FTC click-to-cancel item; prices, plans, trials.
- **MyFitnessPal:** Dated 2026 facts: on February 24, 2026 the Winter Release added Photo Upload to Meal Scan for Premium and Premium+ and Meal Planner improvements for Premium+ (https://markets.financialcontent.com/woonsocketcall/article/gnwcq-2026-2-24-myfitnesspal-debuts-its-2026-winter-release); in June 2026 the app added a Coach tab, an AI Coach that turns a member's food logs, goals, meals and habits into nutrition guidance, for Premium and Premium+ members (9to5Mac, June 16, 2026, https://9to5mac.com/2026/06/16/myfitnesspal-adds-ai-powered-coach-for-personalized-nutrition-guidance/); the Progress tab ("Progress Overview") turns daily tracking into weekly insights from app version 26.16.0 (support article, https://support.myfitnesspal.com/hc/en-us/articles/45246617814669, seen through search); the November 17, 2026 release notes describe a new Weight Log screen where a member adds a photo to a weigh-in, and a Progress tab fix (https://apps.apple.com/us/app/myfitnesspal-calorie-counter/id341232718). MyFitnessPal now also runs Cal AI, a photo-first calorie app, as a standalone product (announced March 2, 2026, https://athletechnews.com/myfitnesspal-cal-ai-acquisition): use only as Karl Mahrenholz's own remit, never the deal. How it works: progress photos attach to weigh-ins under Weight & Measurements and stay private to the member (https://support.myfitnesspal.com/hc/en-us/articles/360032625271-Progress-Photos-FAQs, undated); plans are Free, Premium and Premium+. No body scan in the app ("Meal Scan" is food logging). Clubs or studios: no. What a member's check-in shows today: a weigh-in on the Weight Log, optionally with a photo, typed measurements under Weight & Measurements, a weekly Progress tab, and an AI Coach that reads food logs, goals and habits, nothing measured about body shape. Role check: Ruth Sylvia, Karl Mahrenholz and Megan Overton (all P1) have no public web record beyond LinkedIn (searched 2026-11-20); their titles describe 2026 products (Cal AI joined MyFitnessPal at the end of 2025; the AI Coach launched in June 2026), which points to current roles; none found to have left. Re-contact account. Name form: "MyFitnessPal"; Karl's own message may name Cal AI as his product. Use (one topic per person): Ruth Sylvia, the Progress tab and what a weekly progress view could show beyond weight; Karl Mahrenholz, photo-first capture that returns structured data, applied to the body instead of the plate; Megan Overton, what the AI Coach could draw on if measured body change sat next to food logs; Ana Pischl, where 3D Body Progress tracking and 3D Goal Visualization would sit between Premium and Premium+ (pilot with free-to-premium conversion); Christina To, the new Weight Log screen and a photo that returns no measurement; Kelsey Van Ackeren, a body scan as an onboarding step and how onboarding completion would be compared in a pilot; Victoria Taylo, typed tape measurements under Weight & Measurements versus a guided record; Olivia Carlson (referral), member questions about logging weight and measurements, easy out to whoever owns the progress experience. Never: the Cal AI deal, its founders, price, revenue or downloads; the meal-planning acquisition and the ChatGPT Health integration; the owner (Francisco Partners) and any investor; Instacart, the athlete partnership, the Blue Check Collection and any partner; the weight-loss-medication support feature (banned terms); member, community and database figures; Premium and Premium+ prices; the CPO, CEO and CMO (colleagues; the CPO is in the registry); integrations with Trainerize, Everfit or any wearable or app; comparisons with Lose It!, MacroFactor, Carbon or Cronometer; anything about an earlier message.
- **Everfit:** HQ and US presence: Everfit's own site file names a San Francisco headquarters and founders Long Nguyen and Jonathan Wang (https://everfit.io/llms.txt, seen 2026-11-20); the App Store seller is Everfit Technologies Inc. (https://apps.apple.com/us/app/everfit-train-smart/id1438926364); LeadIQ lists San Francisco 94105 with staff across three continents as of March 2026 (https://leadiq.com/c/everfit/5e663fb21d6f06b382076a3b); Built In Toronto also lists it. Verdict: US presence real enough for Nick: San Francisco is the HQ of record, the operating entity is a US Inc., both founders and three other SEND people are US-located, and no other profile covers Everfit (global registry, 2026-11-20). What it is: a coaching platform for trainers, nutrition and lifestyle coaches and studios; clients use a custom-branded app; coaches run custom forms (intake, goal-setting, weekly progress check-ins), AI check-in analysis and automation (llms.txt; https://everfit.io/forms/, undated). Dated 2026 facts: on July 28, 2026 every task category got pre-built templates, progress-photo templates among them, and synced data deepened to body fat, weight and height "for fewer manual check-ins" (https://blog.everfit.io/july-2026-new-features); on October 14, 2026 the Master Planner began showing logged workouts beside assigned ones, framed as "coach on facts, not guesswork", with a tip to keep assigned values visible at check-ins (https://blog.everfit.io/october-2026-updates). No body scan found in the app or on the integrations page (https://everfit.io/integration/, 2026-11-20). Clubs or studios: no; studios and gym owners are customers, so "between sessions" is allowed, club visits are not. What a client's check-in shows today: body metrics, progress photos and notes in the client app, weekly check-in forms, and weight, body fat and BMI only where a device or app syncs them. Role check: Long Nguyen and Jonathan Wang, named as founders on Everfit's current site file, CONFIRMED. Name form: "Everfit". Use (one topic per person): Long Nguyen, one integration that puts a body check-in in front of every coach's clients; Jonathan Wang, the scan and its record under each coach's brand, build versus integrate; Robert Benjamin, what coaches learn to look for in a check-in and what measured change would add; Carly Bogatz, a guided capture at the intake form, as an onboarding and activation step; Elizabeth Palmer (coaching), what coaches ask the platform to record for their clients. Never: staff counts, offices outside the US and where engineering sits; funding and investors; integration partners by name (nutrition apps including MyFitnessPal, wearables, rings, scales); the March 2026 product-team blog post and its author's health details; MacroSnap and any food scanning; pricing, tiers, free trial, HSA/FSA; G2 or Capterra ratings and "140+ countries"; comparisons with Trainerize or TrueCoach; the coach marketplace.
- **Lose It!:** How it works (no dated 2025-2026 product release from the company found; April 22, 2025 is the last one, about AI photo and voice logging, https://www.newswire.com/news/lose-it-finds-ai-powered-logging-boosts-weight-loss-success-and-22557702, more than 12 months old): the App Store listing (version of 2026-11-19, https://apps.apple.com/us/app/lose-it-calorie-counter/id297368629) describes a weight-loss calorie counter where members set weight targets and a weight-loss schedule, log food, weight and activity, and in Premium track "body measurements" under Advanced Tracking alongside other health metrics, with photo and voice meal logging. Developer FitNow, Inc. (Boston). No body scan in the app ("scan" there means barcodes and meals). Clubs or studios: no. What a member's check-in shows today: a weigh-in against the weight-loss schedule and calorie budget, and typed body measurements for Premium members; no progress-photo feature in the official listing. Role check: Thos Niles (P1) has no public web record beyond LinkedIn (two searches, 2026-11-20); not found to have left. Sarah Molhan: NOT FOUND (no web record linking her, or the name in her LinkedIn slug, to Lose It! or FitNow): do not promote. Name form: "Lose It!". Use (one topic per person): Thos Niles, what a member sees at a weigh-in beyond the number, in a single-app tracker; Taylor Smyrnos, typed tape measurements in Premium versus a guided record with fat and lean mass estimates; Burton Hohman, where a body check-in fits beside the weight log and the weekly schedule; Billy Hulbert (partnership), a white-label capability inside the paid plan that keeps the member in Lose It!. Never: the weight-loss-medication tracking feature and medication (banned terms); weight-loss clinical framing (banned words); the Trainwell partnership (2026-06-04) and any partner; the parent company and any deal; the 2025 release's findings and figures, member counts, food-database size, ratings; Premium prices and trials; MyFitnessPal and other trackers.
- **MacroFactor:** Facts: MacroFactor's team page names five co-equal owners, among them Greg Nuckols, Cory Davis and Rebecca Kekelishvili, and says it launched MacroFactor Nutrition in 2021 and MacroFactor Workouts in 2026 (https://macrofactor.com/team/, seen 2026-11-20); the Workouts app went on the App Store on January 12, 2026 (https://apps.apple.com/us/app/macrofactor-workouts-tracker/id6737156524). How it works: the nutrition app runs a weekly check-in that adjusts calorie and macro targets from the food log and the weight trend (https://apps.apple.com/us/app/macrofactor-macro-tracker/id1553503471); Body Metrics and Progress Photos let members tape-measure sites such as shoulder, chest, waist and hips and take front, side and back photos compared side by side (https://macrofactor.com/body-metrics/, launched 2023, updated September 12, 2025); a customizable dashboard compares body metrics between dates (2025 annual report, https://macrofactor.com/annual-report-2025/). Company: Stronger By Science Technologies LLC, terms under North Carolina law (https://macrofactor.com/terms/). No body scan. Clubs or studios: no. What a member's check-in shows today: the weekly check-in on weight trend and intake, typed body measurements and front, side and back photos; lifts in the Workouts app. Role check: Greg Nuckols, Cory Davis and Rebecca Kekelishvili (Rebecca K.) are listed owners, CONFIRMED. Name form: "MacroFactor" (the Workouts app by its name). Use (one topic per person): Greg Nuckols, what a repeatable guided capture adds to tape and photo check-ins, for a science-led audience; Cory Davis, the SDK and API setup and the record it returns, and where it would land on the Body Metrics screen; Rebecca Kekelishvili, a guided front and side capture beside the existing photo views, with MacroFactor's own consent and results screens. Never: the other owners (colleagues), Stronger By Science content and podcasts, coaches and influencers; any count from MacroFactor pages (metrics, upvotes, users, team growth); claims about the expenditure algorithm; AI food photo logging; prices and trials; comparisons with Carbon, MyFitnessPal, Cronometer or RP.
- **Fitbod:** Facts: in a TechRadar interview published June 20, 2026, Fitbod's co-founder and CEO says the company is moving "from simply generating the right workout to helping members understand their data, interpret their progress, and get more active coaching inside the app", with a Coach Chat feature coming (https://techradar.com/health-fitness/fitness-apps/its-no-longer-enough-for-an-app-to-tell-you-what-to-do-people-want-to-know-why-fitness-app-fitbods-founder-on-the-reason-behind-the-ai-fitness-boom). How it works: AI-generated strength workouts from workout history and muscle recovery, adaptive to the member's edits (App Store, version of 2026-11-05, https://apps.apple.com/us/app/fitbod-gym-fitness-planner/id1041517543). No body scan. Clubs or studios: no (an undated help-centre "Clubs" feature at select gyms is not Fitbod's own). What a member's check-in shows today: strength progress, workout history and muscle recovery from logged sets; no weigh-in, photo or measurement check-in found in the listing or by search (2026-11-20), so pain targets are training metrics and weight on a strength program. Role check: Jesse Venticinque, co-founder and head of product on Crunchbase (https://crunchbase.com/person/jesse-venticinque); no 2026-dated record found; not found to have left. Re-contact account. Name form: "Fitbod". Use: Jesse Venticinque, the 2026 direction of helping members interpret progress, and where a body check-in would sit beside strength progress; Alisa Calderon (referral), member questions about seeing progress beyond lifts, easy out to the owner of the app's progress experience. Never: the CEO by name or his quotes verbatim (colleague, in the registry); price and price changes; integrations and partners (a tracking platform's 2026 strength partnership, wearables); App Store awards; the Clubs feature; Alisa Calderon's former body-composition-scan employer and her scan background; anything about an earlier message.
- **RP Strength:** Facts: the new RP Hypertrophy app (version 1.0.0) launched on iOS in the US on December 20, 2025 (RP help centre "What's new", https://help.rpstrength.com/hc/en-us/articles/34725726510999-RP-Hypertrophy-App-What-s-new, seen through search; App Store release date 2025-12-20, https://apps.apple.com/us/app/rp-hypertrophy/id1555614554), with weekly progression set from the member's pump, soreness and workload feedback; RP Diet Coach sets calories and macros, takes weigh-ins (also from Apple Health) and runs a weekly review with recommended adjustments (https://apps.apple.com/us/app/rp-diet-coach-planner/id1330041267; help articles on weigh-ins and the weekly review, https://help.rpstrength.com/hc/en-us/articles/35245670505879-Progress-and-Weekly-Review-RP-Diet-Coach-App). RP's About page says the two flagship apps came "thanks in part to our third partner, Andrew Zey" (https://rpstrength.com/pages/about, undated). Company: RP Strength, LLC, terms under Delaware law (city not confirmed). No body scan. Clubs or studios: no. What a member's check-in shows today: Diet Coach weigh-ins feeding a weekly review; in the Hypertrophy app, weekly feedback on pump, soreness and workload; no progress photos or measurements found. Role check: Andrew Zey, the partner behind the apps on RP's own About page, CONFIRMED (the CPO title is from his profile). Jacob S. (COO) is listed by initial only and could not be checked on the web. Do not confuse Andrew Zey with Arthur Zey, listed elsewhere as RP's head of product for diet (not in the list). Name form: "RP Strength"; the apps as "RP Hypertrophy" and "RP Diet Coach". Use: Andrew Zey, what a measured body record adds to the Diet Coach weekly review next to the weigh-in trend, or arm, chest and thigh girths for hypertrophy programs (one of the two); Jacob S., how RP judges a new paid feature before rollout, with the pilot design. Never: the founders and their content, channels and books (colleagues); Arthur Zey; prices, plan terms and subscriber counts; coaching services and supplements; comparisons with MacroFactor or Carbon.
- **Ladder:** Facts: on April 21, 2026 Ladder announced its first celebrity partnership, framed around getting more women into strength training (press release seen through search, https://www.wboc.com/online_features/press_releases/hilary-duff-partners-with-ladder-to-help-women-build-strength/article_d24f3cf6-7ed7-57b0-8876-cc8513d7f0f5.html). How it works: coach-built strength plans new each week, teams led by a named coach with a group chat, in-ear coaching and the Ladder Journal for rep and weight progress, PR alerts and training notes (App Store, version of 2026-11-16, https://apps.apple.com/us/app/ladder-strength-training-plans/id1502936453; https://joinladder.com/). Ladder Technologies, Inc., Austin, TX; LinkedIn slug ladder-app; not Ladder Life. No body scan. Clubs or studios: no. What a member's check-in shows today: the Journal's reps, weights and PRs and the team coach's chat; no body-weight, photo or measurement check-in found (listing, homepage, search, 2026-11-20), so pain targets are training metrics, weight on a strength program, and a team coach with no measured body change to look at. Role check: Brett Maloley, identity CONFIRMED as a co-founder of Ladder the Austin strength-training app (Wellworthy brand profile listing the founders, https://wellworthy.com/brand/ladder/, undated); his current operating role is not confirmed. Re-contact account. Name form: "Ladder". Use: Brett Maloley, a measured body check-in as a member feature Ladder would own under its brand; Ryan Mott (data product), one timestamped record per scan through the API with the scan ID, and what the data product would do with it. Never: Ladder Life, life insurance and Brett Maloley's advisory seat; the celebrity, other talent and coach names; funding rounds and investors; awards, rankings and ratings; Teams figures and prices; the CEO and the app VP of Product (registry, colleagues); anything about an earlier message.
- **Carbon Diet Coach:** Facts: Carbon's homepage (© 2026) names its co-founders, Layne Norton, PhD and Keith Kraker, RD, and describes weekly check-ins that analyse progress and refine nutrition targets (https://www.joincarbon.com/); the App Store listing (version of 2026-11-04, with Planner 2.0 in its latest notes, https://apps.apple.com/us/app/carbon-macro-coach-tracker/id1437820611) says members log food, weigh in or sync weight, check in weekly, read a check-in report that explains every adjustment, see charts for weight, body fat and lean body mass, and get a protein target based on lean body mass. John Ybarra wrote the Carbon blog's posts of October 19 to November 11, 2026 (https://www.joincarbon.com/blog). Operator Reform LLC, terms under Florida law (https://www.joincarbon.com/terms). No body scan ("Smart Logger" photographs meals). Clubs or studios: no. What a member's check-in shows today: the weekly check-in report from weight trend and food log; body fat and lean mass appear only as the member enters or syncs them. Role check: Keith Kraker, CONFIRMED co-founder (homepage founder markup and "Keith Kraker, RD, Carbon co-founder"): promote; John Ybarra, CONFIRMED active at Carbon (blog author through November 2026). Name form: "Carbon" or "Carbon Diet Coach". Use: Keith Kraker, where the lean body mass behind the protein target comes from at a check-in, and what a measured fat and lean mass estimate would change; John Ybarra, what a measured body record adds to a check-in report that explains each decision, with Carbon's own results screen. Never: the other co-founder and his book and channels (colleague); the blog's comparisons (MyFitnessPal, AI chatbots, other apps); ratings and member counts; prices; scale and device makers; any claim about body-fat accuracy.
- **Trainwell:** Facts: Trainwell's own July 3, 2026 post describes trainer-led daily and weekly check-ins, proactive outreach and streaks "built around showing up, not body composition", and says the trainer treats "consistency, not transformation, as the scoreboard" (https://www.trainwell.net/blog/best-fitness-accountability-apps-with-real-coaches-2026). How it works: a dedicated 1-on-1 trainer builds and adapts every workout, starting from an onboarding video call; unlimited messaging, video feedback, form-check reviews and live video check-ins; body recomposition is one of the trainer specialties; app progress tracking means streaks, workout history and form feedback (App Store, version of 2026-11-18, https://apps.apple.com/us/app/trainwell-personal-training/id1466445684). Founded 2018 by Matt Spettel and Gabe Madonna, formerly CoPilot (https://www.trainwell.net/about). No body scan. Clubs or studios: no; "between sessions" is allowed. What a member's check-in shows today: logged workouts, form videos and messages for the trainer, and nutrition goals reviewed with progress; no photo or measurement check-in found. The consistency-first stance is theirs: copy never argues against it, and offers the measured record to the trainer for members whose goal is body recomposition. Role check: Gabe Madonna, named co-founder on the current About page, CONFIRMED (CTO title from his profile). Re-contact account. Name form: "Trainwell". Use: Gabe Madonna (leadership, founder-CTO), the SDK and API setup with Trainwell's own screens, and the record a trainer reviews before the next program block for recomposition members. Never: the Peloton product powered by Trainwell (2026-02-17) and the Lose It! partnership (2026-06-04), both prospects; the other co-founder (colleague); member counts, ratings, the Forbes award, trainer hiring figures and employment model, prices and free trial; the weight-loss-medication specialty (banned term); comparisons with Future or Caliber; anything about an earlier message.
- **Jefit:** Facts: on April 15, 2026 Jefit introduced Adaptive Mesocycle Training, which builds three mesocycles when a member starts an adaptive progressive-overload plan (https://www.jefit.com/blog/adaptive-mesocycle-training-jefits-smarter-way-to-progress); in August 2026 periodization extended to plans members build themselves (https://www.jefit.com/blog/periodization-on-your-own-plan). How it works: members track body weight, body fat and tape measurements (waist, chest, arms, legs) and add notes and progress photos to any workout; the Jefit Elite paid plan adds the Adaptive AI Coach and a Premium Analytics Dashboard (App Store, version of 2026-11-19, https://apps.apple.com/us/app/jefit-workout-plan-gym-tracker/id449810000). Jefit Inc., Sunnyvale, CA. No body scan. Clubs or studios: no. What a member's check-in shows today: typed body weight, body fat and measurements, progress photos attached to workouts, and strength analytics. Role check: Nitin Bansal (P3) has no web record beyond LinkedIn (searched 2026-11-20); not found to have left. Name form: "Jefit". Use: Nitin Bansal, typed measurements and workout photos beside adaptive plans, and what a guided record would add to Elite. Never: comparisons with Fitbod or any other app; user counts, exercise-library size, ratings and testimonials; prices; watch and device integrations.

## Rules for steps 3-5

*This section is handed to `message-sequencer` verbatim. Lane notes and targets are instructions to
the writer, never copy.*

- **Sender and format.** Nick, American English, `Nick` alone on the last line of both messages,
  first names only. closely sends a connection request with no note; Message 1 goes after
  acceptance, Message 2 after the delay Vadim sets in closely. Message 1 at most 900 characters and
  Message 2 at most 700, links included (frontmatter `message_max_chars: 900/700`, Vadim
  2026-11-19).
- **Message 1: context, the pain, the fix, one question (Vadim 2026-10-07 and 2026-11-18).** Four
  parts, in an order that varies between people at one company: a company line from its Account
  facts bullet; the pain, said about the method in general and never about this company, its staff,
  its members or its numbers (next rule); how FitXpress fixes it, as the mechanism and what the
  company gets, in two to four sentences that use at least three parts from What the scan is, chosen
  for the person's lane; then one question, the message's only question mark. No call ask, no link of
  any kind. The product is never squeezed into one clause about photos.
- **The pain (the method, never the company): topic targets.** The pain line establishes one limit
  of a check-in method in general, picked for the company type and the lane and put in the writer's
  own words. Targets: the weigh-in (a single, often self-reported total; where the body changed
  stays unknown); weight on a strength or recomposition program (the total can hold while waist and
  fat and lean mass move); the progress photo (visible change, no measurement to compare at the next
  check-in); home photos and tape (pose, distance, light and tape placement differ between
  check-ins); the check-in form (only what the member enters); training metrics (the work done, not
  the body change it is for); the separate scanning app (member and result under another brand; what
  comes back to the platform depends on that app); the in-club scanner (a club visit for every
  repeat; brands with clubs or studios only); the coach's review at groups B and C (the next block
  set from weight, photos and notes, with no measured change to compare). A pain target may repeat
  at one company when it fits each person (Vadim 2026-11-20). Never say or imply that this company's members quit, lose
  motivation or fail, and never cite how many members any app loses.
- **What the scan is (both messages; the writer picks the parts and the words).** A scan inside the
  company's own app on the member's own phone, with no hardware and no club visit; 2 guided photos
  (front and side) with pose and framing guidance during capture (Real-Time Pose Validation); 80+
  body measurements, including waist, hip, chest, thigh and calf; body composition estimates
  (body-fat percentage, lean mass, fat mass); BMI and BMR as calculated metrics; one timestamped
  record per scan with its processing status, returned through the API and linked by the platform to
  the member profile through the scan ID; white-label: the platform's brand and its own onboarding,
  consent and results screens, while the capture layer stays fixed to protect measurement quality;
  web and mobile SDKs with iOS and Android support, with the SDK and the API together as the
  recommended setup; on the Pro plan, 3D Body Progress tracking and 3D Goal Visualization for the
  paid membership; the coach reviews the same record before setting the next program block; for
  brands with clubs or studios only, the check-ins between visits. Which parts appear, in what order
  and in what words varies between people at one company. A single label for the product is never
  enough.
- **What it is not.** It does not diagnose, treat or decide anything about a member; it provides
  structured body data for coaching and program workflows. On progress, the program compares scans
  it selects: the platform keeps each member's history and chooses which scans are compared and what
  the member and the coach see. Never say or imply that FitXpress or 3DLOOK tracks members. The
  basic scan is not a 3D product; the 3D progress tools are on the Pro plan. It is not a weight
  reading and not a scale. Never describe voice prompts, audio or spoken guidance during capture
  (`roadmap.md`: iOS and Android voice guidance is in testing, and fitness platforms integrate
  mostly through native apps; Open question 11), clothing detection or any anti-fraud check.
- **The retention argument, rewritten (a TEST, `learnings.md` HYP-6).** Retention appears only as
  something a pilot measures: day-30 and day-90 retention against a comparison cohort, and
  free-to-premium conversion where 3D progress sits in the paid plan. No category or market
  statistics in copy: the page's Adjust app-retention and Kidman (JMIR) app-abandonment figures are
  context for this file only. No claim that the scan improves retention, engagement, motivation or
  conversion.
- **A pilot in Message 2 is described whole or not at all.** On whom: one member cohort scans at
  onboarding and at the first check-in; a comparable cohort keeps the usual check-in flow; where
  practical, members are assigned at random before the pilot starts. What is compared between the two
  cohorts: day-30 and day-90 retention, onboarding completion, and free-to-premium conversion where
  3D progress sits in the paid plan. What is measured in the scan cohort: scan completion, retakes
  and repeat scans at the first check-in. Against what: success criteria agreed with the company
  before the pilot starts; if they are met, the scan goes live for members on the matching plan. What
  it does not touch: it makes no decision about any member. A writer who cannot fit the whole design
  names one compared outcome together with the comparison cohort and the criteria agreed up front,
  never a lone metric. Never say or imply that the pilot is free or unpaid; its terms go to the call.
- **What the scan adds to what they use now (`learnings.md` MSG-4).** At most one sentence per pair,
  from the page's comparison: a weight log records weight and its photos are not measured; a separate
  scanning app shows its own brand and returns data that depends on that app; an in-club device needs
  the club and shows the device maker's brand; FitXpress runs in the platform's app, under its brand,
  and returns a structured record through the API. Never name a device, an app, a scanner maker or a
  competitor, and never say what this company uses unless its Account facts bullet allows it.
- **Message 2 (it goes only after silence).** Never a repeat of Message 1 and never a follow-up
  formula: one or two value points Message 1 did not use, from the person's lane targets, in fresh
  words; at most one question; then the call offer with https://meetings.hubspot.com/nick-omelchak as plain
  text, alone on the last line before `Nick`, nothing glued to it. Every lane, referral included. No
  call length or minutes in any message. Never open Message 2 as if the person had answered.
- **Page link (Vadim 2026-11-19).** https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/
  as plain text with nothing glued to it, in Message 2 for about half of each company's people, on
  its own line before the call offer; never in Message 1. The calendar line stays the last line
  before `Nick`. Both links count toward the 700 characters.
- **Numbers only from this list:** two photos (front and side), with "2 photos" as the numeric form;
  "under 45 seconds from the photos to structured results" as its own plain sentence, at most once
  per pair and only where speed is the point; 80+ body measurements; "3DLOOK has worked with 100+
  clients", optionally with ", including fitness teams" (the live page); "112,100 scans in 2025
  across all 3DLOOK customers" as its own sentence, never tied to fitness, a country or one client;
  day-30 and day-90 only inside the pilot design. No accuracy percentage, error figure or body-fat
  figure; no market, category or retention statistic; no figure about the prospect.
- **Accuracy wording.** Only the repeatability sentence, verbatim, in Message 2, at most once per
  pair, in the `product`, `coaching` or `science` lane, in one of two forms: "Repeated scans
  typically differ by less than 1 cm for most evaluated measurements." (the live page) or "For most
  evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm."
  (`accuracy-formulations.md` §1.2). No other accuracy claim and no comparison with any device.
- **Body composition wording.** Always estimates. For `science`, or when it helps: derived from the
  measurements with height and, where provided, weight. Never "measures body fat". Body measurements
  are girths, lengths and widths; BMI and BMR are calculated metrics.
- **Proof without names.** No 3DLOOK client is named or hinted at (no fitness app, coaching app or
  celebrity app as a reference). Proof lines are the client-count line and the scans line above.
  Never imply that a prospect or any fitness brand uses FitXpress.
- **Compliance line.** At most one per pair, either message, verbatim: "FitXpress is not a medical
  device." The page's next sentence may follow it in the same message: "It provides structured body
  data for coaching and program workflows." No HIPAA, BAA, FDA, CCPA, SOC 2 or GDPR wording in cold
  copy: consumer fitness readers take it as clinical, and the US line in `compliance.md` carries a
  BAA clause meant for health buyers. Replies use `compliance.md` §10 and legal@3dlook.me. Never
  "compliant", "certified" or a medical-device claim.
- **Data handling sentences.** Only the page's and `compliance.md` forms: the program compares
  scans it selects (never that FitXpress or 3DLOOK tracks members); photos deleted after
  processing or kept up to 30 days under the company's policy, with blurring and face obfuscation;
  each scan on a randomly generated identifier; production data not used for model training without
  the company's documented authorization; the consent screen in the company's own wording. Never
  "not stored", "no personal data" or "anonymous".
- **Pricing.** No dollar figure and no plan price in either message (the gate fails a currency sign;
  Vadim 2026-11-19). Message 2 may say once, as its own sentence, that there is no integration fee;
  Message 1 never does. A
  price question goes to the call. Write paid plan, premium plan or membership for the company's own
  offer; the Pro plan is named only as where the 3D progress tools sit.
- **Several people at one company (a ratio rule, coordinator 2026-11-19).** Name the company in
  every Message 1, in a form from its Account facts bullet. Wording may be shared too when it fits
  each person (Vadim 2026-11-20: «і дослівно теж можна»); the gate notes a shared sentence and
  does not fail it. A company line may reuse a fact from
  the Account facts bullet. A pain target, a question target, a Message 2 value point, an easy-out
  target or an order of Message 1's parts MAY repeat at one company when it fits each person's
  company and role (Vadim 2026-11-20: the earlier "about a fifth" ratio is withdrawn); the
  wording of each sentence is still the person's own. Never mention colleagues, how many people
  were written to, or a conversation that did not happen.
- **Never name one prospect in another prospect's copy,** nor a company's parent, owner, investor,
  sister brand, hardware maker, content partner, competitor or supplier. A company's own brands and
  products may be named in its own copy only.
- **Re-contact companies.** At iFIT, Tonal, Hydrow, Echelon, Future, Ladder, Fitbod, Trainwell and
  MyFitnessPal nothing refers to an earlier message, campaign, reply or person; each message stands
  as a first message.
- **Word traps.** No em or en dash; no "plus" as a connector; no "so" introducing a benefit; no
  corrective "X, not Y"; no "positioned as"; no "objective" about our data; none of the
  hard-bans-card buzzwords; no follow-up or reach-out formulas. The page's headings are not copy.
- **Writer notes and card instructions are not copy.** Lane notes, targets and rule sentences are
  never pasted; the quoted lines above are the only verbatim copy.
- **Message 1 gate.** Every message 1 carries at least one product specific from `proof-points.md`
  and one line that could only have been written to that company; each pair of messages cites at
  least one number. The gate recognises "two photos", "2 photos", "body measurements", "body
  composition", "lean mass", "fat mass", "3D progress tracking", "API" and "SDK" as product
  specifics, and "under 45", "2 photos", "two photos", "80+ body measurements" and "112,100 scans" as
  numbers. Referral people included.

## Anti-cases (where it does NOT work)

- **Apps that already have a body scan in the member app**, from a vendor's SDK or built in-house:
  Noom and WW (`competitors.md`, verified 2026-10-15), and any company step 2 finds with one live.
  That is a replacement sale, and copy may make no comparison with another vendor. Tempo and
  FitnessAI are step-2 re-checks, not exclusions: their scans rest on a 2023 release and an undated
  one (Company types in scope).
- **GLP-1 companion apps and medical weight-loss programs** (Noom, WW, Calibrate, Found, Ro, Shotsy
  and peers): `icp-detail.md` §1, covered by Nick's clinical campaigns.
- **Employer wellness, employer MSK and corporate fitness networks** (Personify Health, Peerfit,
  Active&Fit, Aaptiv's employer MSK product and similar): paid by employers or health plans, with no
  member check-in of their own to put a scan in (Vadim 2026-11-19).
- **Fitness marketplaces and aggregators** (Wellhub, ClassPass, Urban Sports Club, Gymlib, MyClubs,
  TotalPass): they sell access to other operators' gyms and classes and run no progress check-in of
  their own. Wellhub is employer-paid; ClassPass is mainly a consumer credit subscription for booking
  classes. Out (Vadim 2026-11-19, and the coordinator's ruling for all four sibling campaigns).
- **Content-only platforms** (video or audio class libraries, streamed classes) with no progress
  check-in of their own; a content-first app in group D is IN only if step 2 finds one.
- **Gym and studio chains and franchises** (Life Time, Equinox, Orangetheory, Crunch, Planet
  Fitness, F45, Xponential): another buyer and an in-club scanner decision (Vadim 2026-11-19). F45
  (US head office) is a gym franchise and out in every sibling campaign, whichever profile its HQ
  points to.
- **Wearable-first and outdoor tracking platforms** (Whoop, Oura, Garmin, Fitbit, Strava, Zwift): no
  program check-in built on body shape.
- **Free content apps with no paid plan, apps under $1M revenue, and equipment makers with no
  subscription app.**
- **Apps for under-16s** (the validation population is 16 to 78) and apps that make medical or
  diagnostic claims.
- **Non-US HQ companies, and non-US-located staff of US companies:** routed to `katerina` (UK),
  `olena` (EU), `katya` (LatAm, Mexico) or `vadim` (Australia, New Zealand).
- **Customers with a contract and competitors:** Zing Coach, Verv and Erakulis (registry,
  2026-11-19); every body-scanning vendor in `competitors.md`.
- **Shut down or closing.** A company that announced a shutdown or the end of its app. A recent
  acquisition does not exclude a company (Vadim 2026-11-17 keeps every company without a contract);
  copy never mentions a deal.

## Learnings applied

- **HYP-2:** baseline for `nick`: accepted 192/777 (24.7%), replied 24/192 (12.5%), positive 5/104
  (4.8%). The targets below come from it. His August campaign in this segment was below it on
  acceptance (39/245, 15.9%).
- **HYP-1:** replied per accepted is flat whatever the message work (pooled 113/884); the new page
  and angle are not promised to lift replies above Nick's baseline.
- **HYP-4:** the segment is Vadim's choice (the page launch), not picked on past reply rates
  (digital fitness 14/98 replied per accepted).
- **Departure from HYP-6, marked TEST:** the page's argument is retention, and the `retention` lane
  drew 0/53. Rewritten twice over: the angle sells the measured check-in (the mechanism and what the
  company gets), and retention appears only as a pilot outcome measured against a comparison cohort,
  with no churn statistic or "keep members" copy (`churn` is a banned term); the subscription owners
  get a `membership` lane about the paid plan and the pilot, read separately at analysis with the
  minimum N and decision rule in Success metrics.
  `virtual-care`, `weight-management` and `digital-transformation` are not used.
- **HYP-7:** acceptance is decided by the sender's profile; Nick's headline is Open question 8.
- **HYP-3, HYP-5:** do not apply (USA).
- **PPL-1:** P1 needs scope on the profile, never the title alone; every IN company gets a route-in
  below C-level where one exists (director of product or a PM with member-app scope, head coach or
  coaching lead, exercise science, partnerships). Founders and CEOs only at companies under about
  500 staff.
- **PPL-2:** non-buyers in relevant functions at IN companies are `referral` PASS, not FAIL.
- **PPL-3, with one departure:** marketing, CRM, lifecycle, retention marketing, growth and
  engineering are not pulled (the titles block and its exclusions), which drops "Head of Growth" from
  the §8 buyer list; "VP User Engagement / VP Engagement / Retention" and "Digital Experience
  Manager" are declared departures too (Target buyer persona, Why these titles). Partnerships and
  business development stay (`partnership`: P2 at coach
  platforms, P3 elsewhere). Departure: sales roles are not pulled, because at connected-fitness
  brands sales means hardware retail and showrooms, which own no check-in.
- **PPL-4:** coaching leads and research roles were among the positive repliers; hence the
  `coaching` and `science` lanes.
- **PPL-5 [watch]:** no role-date filter; the Account facts round web-checks every P1.
- **MSG-1:** Message 1 carries the campaign: the company line, the method pain, the mechanism and
  what the company gets, the strongest product specific and a number.
- **MSG-2 [watch]:** the call ask stays in Message 2.
- **MSG-3:** no trimming for its own sake; 900 characters for Message 1 and 700 for Message 2 (Vadim
  2026-11-18 and 2026-11-19).
- **MSG-4:** at most one sentence per pair on what the scan adds to a weigh-in, progress photos, a
  separate scanning app or an in-club scanner, from the page's comparison; no device or maker named.
- **MSG-5 [watch]:** the page link goes in Message 2 for about half of each company's people (Vadim
  2026-11-19); the 2-pager goes only in replies.
- **MSG-6:** compliance and platform questions are answered from `compliance.md` §10 and the page's
  FAQ (Apple Health or Health Connect sync, iOS and Android SDKs).
- **MSG-7:** every Message 1 carries a company line from Account facts and a question built from
  the person's title.
- **Post-mortem 2026-08-07 (this profile's history, not in `learnings.md`):** no
  `technical-integration` lane (0/60); WEAK only as marked fill; one ICP segment (Personify Health
  out); a title pull (Apollo first, Sales Navigator added); a P1 role check before step 5.

## Vadim's standing decisions (already applied above)

1. **No headcount floor** (2026-09-29); the §8 revenue floor ($1M+) stays.
2. **`cap_per_group: 50` for every campaign, no waves** (2026-09-29): one closely import file.
3. **A lane for every function** at an IN company (2026-09-29), within the Not the buyer and
   Location rules.
4. **FAIL only for the wrong company, people who left, identity collisions and duplicates,** along
   with this campaign's Location rule.
5. **No 3DLOOK client is named** (2026-09-12); "3DLOOK has worked with 100+ clients" (2026-09-30);
   112,100 scans as 3DLOOK-wide scale (2026-09-29).
6. **Message 1 asks, Message 2 calls with the calendar link**, referral included (2026-10-07).
7. **Account facts are written by a fresh round before step 5** (2026-11-05).
8. **Every company without a contract may be contacted again;** history is listed, not filtered
   (2026-11-17).
9. **Message 1 explains the pain and how FitXpress solves it;** no rule shrinks the product to one
   clause; up to 900 characters for a campaign that sets it (2026-11-18).

## Vadim's decisions 2026-11-19 (hypothesis checkpoint)

Recorded by the coordinator from Vadim's answers at the hypothesis checkpoint (AskUserQuestion, 2026-11-19).

- **People: only new people** («Ні, тільки нові люди»). Anyone this profile already messaged stays excluded, whatever the campaign. Companies without a contract may return with their history shown; customers never (Erakulis added to the registry as a customer 2026-11-19).
- **Process:** Vadim's checkpoints are this hypothesis and the messages. The people list goes through validation and opus QC without stopping for him. People come from Apollo first; Hlib's Sales Navigator pull is added when it arrives.
- **Prices:** no dollar figures in copy. "No integration fee" may appear once, in Message 2 only.
- **Page link:** the page URL https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/ may appear in Message 2 for about half of each company's people, never in Message 1; the closing line stays last.
- **Length:** `message_max_chars: 900/700` (Message 1 / Message 2).
- **Segment approved as written** («Як запропонували»): connected-fitness hardware with a membership, coaching apps, coaching platforms for trainers, workout and fitness-nutrition subscriptions. Gym and studio chains stay out; marketplaces and corporate networks (Wellhub, ClassPass) stay out.
- People who replied in 2026-08-07 (e.g. the iFIT Chief Subscription & Content Officer, "interested") are not re-messaged here; they go to Nick for a personal follow-up.

## Vadim's decisions 2026-11-20 (step 4, pools)

Recorded by the coordinator from Vadim's answer on 2026-11-20 (AskUserQuestion, after validation and QC 17/20). People came from Hlib's Sales Navigator sheet (a seniority pull, 305 rows) and 66 Apollo rows (67 credits, «67 кредитів»). 79 were SEND and the registry removed 64. Vadim took every pool offered:

- **A: ABC Fitness, Trainerize not named (11).** These are product leaders (CPO, SVP and VP Product, 5 PM directors) and partnership owners (VP Partnerships, VP Corporate Development, Director Partner Solutions) at Trainerize's parent. They are the only US route to Trainerize: its own PMs are in Canada and Serbia. For this campaign only, the parent's product and partnership owners count as group C buyers even when the profile does not name Trainerize. Copy speaks to Trainerize and the trainers on it, never to ABC's club software (gyms stay out of the segment).
- **B: customer-experience heads (5)**, angle `referral` (MyFitnessPal, Ergatta, Centr, Tonal, Fitbod). This settles the card's contradiction: a department head of CX or post-sales counts as a P3 referral; support staff below head level stay Not the buyer.
- **C: Tonal Head Coaches (2)**, angle `coaching`. At Tonal, Head Coach counts as a program role even for on-camera coaches.
- **D: Peloton strategy, program management and user research (7)**, angle `referral`.
- **E: subscription growth and retention inside the subscription team (2)**, angle `membership` (Peloton, iFIT). Lifecycle and CRM marketing outside the subscription team stays out.
- Pools F (hardware, R&D, commercial equipment), G (C-level over 500 staff), H (engineering) and I (DTC, retail, international) were not offered and stay out.
- **WEAK rows (coordinator, under the 2026-11-19 «no stop at validate» rule):** Greg Nuckols goes to SEND, because his raw headline "Co-Owner of MacroFactor and Stronger By Science" confirms him (compact.csv had dropped it). The account-facts round web-checks the rest, and the confirmed ones are promoted: Ben Schultz, Emily Baldwin, Keith Kraker, Sarah Molhan, Heather Guymon, Jordan Annis, William Feroe, Nate Silva, Yi Chang, Rianita Ummah, Lisa Privitera and Jeff Laborde.
- **Outcome of the account-facts round (2026-11-20, coordinator):** two were promoted. Keith Kraker is confirmed as Carbon co-founder on joincarbon.com (`leadership`, P3). Lisa Privitera owns the Echelon Coach program and is not on-camera talent (`coaching`, P2). Kelly Card was raised to P1: the Trainerize 2026 roadmap post (2026-01-18) names him SVP of Product at ABC Trainerize. The other ten stay REVIEW and are not sent:
  - not found: Ben Schultz, Emily Baldwin, Sarah Molhan, Heather Guymon, William Feroe, Nate Silva, Yi Chang, Rianita Ummah;
  - probably left: Jordan Annis;
  - equipment side, not the app: Jeff Laborde.

  109 SEND.
- **Messages approved (Vadim 2026-11-20, «апрув по текстам»):** 109 pairs after QC r2 14/20 and the line-edit pass, gate 0 hard. On the same day: «і дослівно теж можна», so the same sentence for colleagues at one company is allowed too; the gate's "same sentence at one company" is a note now.
- **Repeats at one company (Vadim 2026-11-20):** «так а чого не можна повторів? якщо біль для цієї компанії і посади людини підходить то і можна повтор». The "about a fifth" ratio for pain targets, question targets, Message 2 value points, easy-out targets and the order of Message 1's parts is withdrawn: they may repeat when they fit each person's company and role. Only the wording stays each person's own (no twin sentences between colleagues).
- **Messages QC 11/20 (2026-11-20), Vadim «Раунд правок»:** a fix round instead of a rewrite. The coordinator fixed one card error. The `product` lane's last question target used to ask what a white-label capture would have to match in the app's design. That contradicts the capture layer staying fixed, so it now asks which screens around a fixed capture (onboarding, consent, results) the team would want in its own brand. The gate gained three checks (Vadim: hard for no product name in Message 1 and for the same Message 2 sentence or body at two companies; soft for labels before a number or link and for British spelling in a US campaign).

## Validation criteria (Step 2 will check)

- **At least 30 US-HQ companies** across groups A to D pass: a paid plan, a progress or check-in
  feature of its own (not a marketplace, aggregator or content-only library), no body scan in the
  app today, $1M+ revenue where it can be estimated, not shut down; each with a dated source.
  Re-contacts carry their August history in the `companies.csv` notes; Tempo and FitnessAI carry the
  result of their scan re-check, and Aaptiv the result of its pivot check.
- **List size, one gate.** At least 30 IN → step 3. Fewer than 30 → stop and report to Vadim with
  `companies.csv`; no padding with content-only libraries, marketplaces, gyms, employer products or
  apps under the revenue floor.
- **People:** at least 20 companies return a P1 or P2 person located in the United States from the
  title pull, Apollo first with Hlib's Sales Navigator pull added (August reached 13 of 27); a
  company under 3 rows from Apollo waits for the Sales Navigator pull before it is dropped.
- **Group C inside a parent:** the coaching product's own people are identifiable (Trainerize,
  TrueCoach).
- **Sibling campaigns:** HQ conflicts with `olena`, `katya` and `vadim` are settled as one company,
  one profile (Everfit, any company with two HQs). Centr is in the US list (Los Angeles head office, AU fix round 2026-11-19); F45 is out
  in every sibling campaign.
- **Proof:** the live page, `use-cases/fx-digital-fitness.md`, `proof-points.md` and `compliance.md`
  cover every claim in Rules; no named case study is needed and none is used.

## Success metrics for this campaign

Nick's baseline (`learnings.md` HYP-2): accepted 192/777 (24.7%), replied 24/192 (12.5%), positive
5/104 (4.8%). His August campaign in this segment: accepted 39/245 (15.9%), replied 6/39, positive
2/39.

- **Acceptance rate:** target 24.7% (192/777), his baseline. August's 15.9% is the floor this
  campaign has to beat before the title pull can be credited.
- **Reply rate (replied / accepted):** target ≥ 12.5% (24/192).
- **Positive replies:** target ≥ 4.8% of accepted (5/104). At the expected 200 to 300 SEND, that is
  about 50 to 75 accepted and 2 to 4 positive replies: target ≥ 3.
- **Qualified leads (a booked call or an explicit ask for one):** target ≥ 2.
- **Lane test (HYP-6):** the `membership` lane will hold about 5 to 15 people (few companies have a
  dedicated subscription or membership owner), too few to read alone. Minimum N: 10 accepted in the
  lane. At 10 or more, replies per accepted in `membership` against the rest of the campaign, with
  denominators, is one data point for the HYP-6 rewrite, never a confirmation; 0 replies on 10 or
  more accepted counts against the rewritten angle. Below 10 accepted, the counts are reported with
  no conclusion and pooled with the next fitness campaign's subscription lane. Also read: whether any
  reply engages with the pilot design.

## Risks

1. **Acceptance on Nick's account.** August reached 15.9% in this segment. **Stop rule:** below 20%
   acceptance after 150 invites, the remaining invites are paused in closely and Nick's profile
   (headline, Open question 8) is checked with Vadim before they go; at that point the cause is the
   profile or the US market, not the list.
2. **Concentration.** At `cap_per_group: 50`, which stays (only Vadim changes it), Peloton and iFIT
   can take up to 100 of the 200 to 300 expected SEND, a third to a half of the campaign; August put
   48% of its invites into two accounts. Step 4 reports their share of SEND. **Stop rule:** once
   either account has 30 invites out, if fewer than 6 have accepted (below 20%), or it has 0 replies
   on 15 accepted, its remaining invites are paused and Vadim decides whether they go. The soft-cap
   option is Open question 7.
3. **Stale people at restructured companies.** iFIT layoffs and leadership changes were reported in
   2026, and Tonal has changed leaders several times since 2023; the Account facts round checks P1s.
4. **Displacement found late.** A company that ships its own scan between research and send turns
   the message into a replacement pitch; the Account facts round re-checks the app.
5. **Body-fat questions.** No body-fat accuracy figure is public until the December 2026 lab report
   (`roadmap.md`); replies answer with the estimate wording and the methodology under NDA.
6. **Four profiles, one page, one week.** A US company's staff abroad could be reached twice; the
   Location rule and one-company-one-profile at step 2 prevent it.
7. **Common names.** Future, Ladder, Echelon and Found collide with other companies in Sales
   Navigator and Apollo; LinkedIn company URLs and aliases keep the groups clean.
8. **Thin list.** About 38 seeds, several flagged (Caliber's revenue, FitOn and obé on revenue and
   as content-first apps, Aaptiv's pivot, the Tempo and FitnessAI re-checks, TeamBuildr's users); the
   30-company gate in Validation criteria stops the run instead of padding it.

## Open questions for Vadim

Each open question carries the default the run follows until Vadim answers. Questions 1 to 6 and 9
were answered on 2026-11-19 (see Vadim's decisions 2026-11-19); their numbers stay so that references
elsewhere in this file hold.

1. **Pricing in copy.** Answered 2026-11-19, see Vadim's decisions: no dollar figures; "no
   integration fee" once, in Message 2 only.
2. **Page URL in Message 2.** Answered 2026-11-19, see Vadim's decisions: in Message 2 for about half
   of each company's people, never in Message 1, with the closing line last (Rules, Page link).
3. **The character cap.** Answered 2026-11-19, see Vadim's decisions: `message_max_chars: 900/700`.
4. **Corporate fitness platforms and Personify Health.** Answered 2026-11-19, see Vadim's decisions:
   marketplaces and corporate networks stay out (Anti-cases).
5. **US gym and studio chains.** Answered 2026-11-19, see Vadim's decisions: they stay out, F45
   included (Anti-cases).
6. **August people at the re-opened companies.** Answered 2026-11-19, see Vadim's decisions: only
   new people; August repliers, the iFIT Chief Subscription & Content Officer among them, go to Nick
   for a personal follow-up.
7. **Soft cap for Peloton and iFIT.** At `cap_per_group: 50` the two accounts can take up to 100 of
   the expected 200 to 300 SEND (a third to a half of the campaign); August put 48% of its invites
   into two accounts. Recommendation: 25 each, ranked by tier, which would hold them to 50 of 200 to
   300. Default: cap 50 for every company (only you change it), with the stop rule in Risks 2.
8. **Nick's headline (HYP-7).** Nick runs the US insurance underwriting campaign at the same time.
   Recommendation: a headline that names body data for both buyers (for example, mobile body
   scanning for insurers and fitness apps) for the length of this campaign. Your call.
9. **Waiver for the nine re-contacts.** Answered 2026-11-19, see Vadim's decisions: companies without
   a contract return with their history shown; `--waive-companies` applies at step 4.
10. **GLP-1 members as a hook** (Peloton's CEO names GLP-1 as a reason for strength; some apps run
    GLP-1 strength programs). Default: out of copy (`GLP-1` and drug names are banned terms), because
    it pulls the pitch toward weight-loss medicine and toward a muscle-preservation claim that the
    body composition estimates cannot yet back with a published figure.
11. **Voice prompts on the live page.** The page says Real-Time Pose Validation gives guidance "with
    voice prompts for a member scanning alone"; `roadmap.md` lists real-time voice guidance as ready
    on web and in testing on iOS and Android. Fitness platforms integrate mostly through native apps,
    so copy never mentions voice (coordinator ruling 2026-11-19). Should the page line say it is a
    web feature, or come off until native ships? Default: copy silent on voice; this campaign does not
    touch the page.

## Sources

- Live page text, 2026-11-19: `workspace/pages/for-connected-and-digital-fitness/published-live-2026-11-19.md` (https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/)
- `workspace/outbound/campaigns/2026-08-07-us-digital-fitness/post-mortem.md` and `hypothesis.md`; `workspace/outbound/exclusions/nick-registry.json`, `global-company-registry.json`
- `workspace/outbound/learnings.md` (version 2026-10-30)
- `brand-assets/product-info/`: `icp-detail.md` §8, `use-cases/fx-digital-fitness.md`, `proof-points.md`, `pricing.md`, `accuracy-formulations.md` §1.2, `compliance.md` §9-10, `roadmap.md`, `competitors.md`
- [Adjust: mobile app retention benchmarks for 2023](https://www.adjust.com/blog/get-the-mobile-app-retention-benchmarks-for-2023/)
- [Kidman et al., JMIR 2024, 26:e56897](https://www.jmir.org/2024/1/e56897)
- [Peloton Q2 FY2026 results](https://investor.onepeloton.com/news-releases/news-release-details/peloton-announces-q2-fy2026-financial-results)
- [The Clip Out: Peloton subscriber churn, Q4 FY26](https://theclipout.com/peloton-subscriber-churn-q4-fy26/)
- [Athletech News: Peloton CEO on strength training](https://athletechnews.com/peloton-ceo-strength-training-wellness-will-be-key-to-brands-growth/)
- [HIT Consultant: WeightWatchers GLP-1 program and app features, 2025-12-17](https://hitconsultant.net/2025/12/17/weight-watchers-launches-new-glp-1-program-and-ai-app-features/)
- [Business Wire: Prism Labs and Tempo, 2023](https://www.businesswire.com/news/home/20230628277318/en)
- [Fitt Insider: FitnessAI BodyScan](https://insider.fitt.co/press-release/fitnessai-launches-innovative-bodyscan-technology-for-mobile-devices/)
- App listings: [PhysiqueAI](https://apps.apple.com/us/app/physiqueai/id6756671414), [Evoly AI](https://play.google.com/store/apps/details?id=com.evolyai.app), [Recomp AI](https://mwm.ai/apps/recomp-ai-3d-body-scanner/6752960004), [GainFrame](https://apps.apple.com/app/id6759252082)
- [Everfit: Everfit vs Trainerize vs TrueCoach](https://blog.everfit.io/everfit-vs-trainerize-vs-truecoach) (vendor source)
- iFIT: [Jeremy McCarty joins as Chief Subscription Officer](https://www.ifit.com/blog/connect/jeremy-mccarty-joins-ifit-as-chief-subscription-officer); restructuring reports with unclear dates, for the Account facts round: [Front Office Sports](https://frontofficesports.com/ifit-ceo-reportedly-forced-out-by-investors), [SGI Europe](https://www.sgieurope.com/ifit-lays-off-another-300-of-its-workforce/99645.article)
- Tonal leadership changes: [Athletech News](https://athletechnews.com/?p=94261)
- Aaptiv's employer MSK pivot: [GlobeNewswire, 2026-02-19](https://www.globenewswire.com/news-release/2026/02/19/3241342/0/en/Aaptiv-Launches-New-MSK-App-in-Partnership-With-movr.html) (via `2026-08-07-us-digital-fitness/companies.csv` row 22)
- New group C seeds: TrainHeroic HQ [Dealroom](https://app.dealroom.co/companies/trainheroic/team); TeamBuildr HQ [its demo page](https://www.teambuildr.com/schedule-ams-demo) and [CB Insights](https://www.cbinsights.com/company/teambuildr)
- QC report: `workspace/_quality/outbound/2026-11-19-hypothesis-generator-us-connected-fitness.md` (17/20)
