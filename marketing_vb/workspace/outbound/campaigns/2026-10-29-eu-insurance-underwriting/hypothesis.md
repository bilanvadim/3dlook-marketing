---
product: fitxpress
profile: olena
market: Continental Europe and Ireland (UK excluded)
created: 2026-10-29
status: approved
approved: 2026-10-29
use_case: fx-insurance-underwriting
cap_per_group: 50
referral_call: yes
banned_terms: [Yazen, UK Meds, Healthyr, Safariland, Burlington, Jim's Formal Wear, Generation Tux, Tailoor, Redthread, Prism, Bodygram, Size Stream, Fit:match, Mirrorsize, Bodd, Nuralogix, Anura, Lapetus, SelfieQuote, Binah, dacadoo, Alula, selfie, selfies, iptiQ, UnderwriteMe, iPipeline, Iress, Pacific Life Re, Appian, Chesnara, Viridium, Corebridge, Great-West, Helvetia, Baloise, Generali, Dazure, Bank of Ireland, BarmeniaGothaer, Barmenia, Gothaer, South Africa, Zurich UK, Swiss Re UK, Munich Re UK, Hannover Re UK, SCOR UK, Gen Re UK, RGA UK, Vitality, iGPR, LIMRA, AIG, HIPAA, SOC 2, FDA, MHRA, UKCA, CE mark, MDR, AI Act, Annex III, high-risk, EIOPA, BaFin, ACPR, DNB, AFM, Kifid, FSPO, Central Bank of Ireland, Consumer Protection Code, GDV, Verbond, Insurance Ireland, VVG, Anzeigepflicht, DORA, Data Privacy Framework, DPF, Schrems, data residency, AWS, US-West, FCA, PRA, ABI, Consumer Duty, ombudsman, FOS, CIDRA, compliant, certified, certification, accredited, clinically validated, clinically proven, verify, verified, verifies, guarantee, guaranteed, fraud, fraudulent, misrepresent, misrepresented, misrepresentation, non-disclosure, liar, lying, dishonest, cheat, cheating, carrier, carriers, paramedical, paramed, APS, attending physician, face amount, obese, DEXA, DXA, BIA, bioimpedance, trial, acquisition, acquired, merger, run-off, generic figure, never a promise, not a promise, context only, writer note, Circling back, Following up, Saw your post]
---

# Outbound Hypothesis: 2026-10-29, EU protection underwriting in Ireland, Germany and the Netherlands (Olena)

- **Campaign:** `2026-10-29-eu-insurance-underwriting`, the continental twin of `2026-10-22-uk-insurance-underwriting` (katerina, UK): same idea, landing and lanes. No UK market research is used as evidence; every market fact below was sourced for Ireland, Germany or the Netherlands on 2026-10-29.
- **Owner and sender:** Olena Kudryavtseva, profile `olena`, Continental Europe and Ireland, UK excluded (`PROFILE_GEO["olena"]`); signature and calendar link in Rules.
- **ICP:** `icp-detail.md` §3 (Life & Disability Insurance Underwriting): insurers buy defensibility (audit trail, workflow integration, consistency) more than accuracy. §3 lists Allianz DE among its EU examples.
- **Use-case file and landing:** `use_case: fx-insurance-underwriting`; angle source https://3dlook.ai/for-insurance-underwriting/ (HTTP 200 on 2026-10-29; text of record `workspace/pages/for-insurance-underwriting/published-live-2026-10-21.md`). Its US terms stay out of copy; a landing number is not an approved claim by being there.
- **Registry, checked 2026-10-29** (`outbound-registry.py status`, all six registries, the UK `people-approved.csv`): no insurer, reinsurer or platform in Ireland, Germany or the Netherlands is registered. `katerina` holds 22 UK protection companies, including `aviva`, `royal-london` and the London entities of all six reinsurers. The bare parents (`swiss-re`, `munich-re`, `hannover-re`, `scor`, `gen-re`) and `allianz` are registered to nobody. Defaults: Validation criteria, Open questions 2-4.

> **Read this first.**
> 1. **One idea, the UK one.** Many individual life and disability applications here go through without medical evidence, on declared height and weight, and build is priced at application (Germany decides many at the point of sale; Ireland's instant broker decisions are to confirm, Risk 10). Self-reported weight runs low (Robert Koch Institute). FitXpress adds a scan step: two photos, a Smart Scales weight estimate, BMI from the declared height, a flag on the insurer's threshold, a timestamped record. The insurer's rules and underwriters decide.
> 2. **Three markets, chosen for the mechanism:** Ireland (mortgage life cover required by law), Germany (BU and term-life risk checks at the point of sale), the Netherlands (one industry health declaration asking height and weight); plus four reinsurer head offices and three platforms.
> 3. **No insurer is a 3DLOOK customer.** The offer is an evaluation; proof only as Rules allow.
> 4. **English only** (Olena's standing decision); German and Dutch titles appear only in the pull.
> 5. **The flag works on large gaps only;** no adult European figure for the typical gap was found (Risk 3).
> 6. **Regulation is buyer context, never copy** (Risks).

---

## Vertical

Individual life and disability cover underwritten at application on declared height and weight in Ireland (mortgage protection, term life, specified illness, income protection), Germany (BU and term life, Risikoleben) and the Netherlands (term life, ORV, and self-employed disability, AOV), with the European reinsurers and point-of-sale platforms that set and host the build rating.

## Sub-segment

The companies that decide what evidence an application in these markets collects and how build is rated: 32 named candidates in five groups, about 27 expected to pass step 2. No company is added to reach a number; each insurer must write new individually underwritten business in 2026.

**A-IE. Irish life insurers writing underwritten protection (7), `hq_country` Ireland.** Irish Life Assurance; Zurich Life Ireland (Zurich Life Assurance plc); New Ireland Assurance; Aviva Life & Pensions Ireland (row `Aviva Ireland (Aviva)`, Open question 3); Royal London Ireland (Royal London Insurance DAC, 30.2% of the Irish broker life market in 2025; row `Royal London Ireland (Royal London)`); Acorn Life (Irish-owned, broker-sold); AXA Life Europe (Dublin; underwrites Laya Life policies incepted from 22 July 2026, after iptiQ).

**A-DE. German life insurers writing BU and term life with point-of-sale risk checks (12), `hq_country` Germany.** Allianz Lebensversicherungs-AG (on EQuot since 2016; Allianz split in Validation criteria); Alte Leipziger Lebensversicherung (e-Risiko for BU, July 2026: about 70% of risk checks end in a final decision during the advice meeting); Nürnberger Lebensversicherung (on EQuot); Swiss Life Deutschland (majority owner and leading user of vers.diagnose); HDI Lebensversicherung (real-time risk checks on EQuot and vers.diagnose, date to confirm); LV 1871 (BU health questions ask in particular about BMI; Quick Risk check, to confirm; vers.diagnose for selected tariffs); Die Bayerische (BU Protect: BMI and smoking checked automatically in the quote program, guide 10/2025); Hannoversche Lebensversicherung (VHV group; term life and invalidity new business €51.5m in 2025); Volkswohl Bund (biometric new business, mostly BU and Grundfähigkeit, up 8.7% to €801m premium sum in 2025, press release 1 June 2026); Europa Lebensversicherung (direct term life); CosmosDirekt and Dialog (Generali Deutschland: Cosmos led term life by running premium in 2023; Dialog runs a fully electronic term-life application, undated). **Reserve, only if Vadim asks:** BarmeniaGothaer, InterRisk, Stuttgarter, WWK, Canada Life Deutschland.

**A-NL. Dutch life insurers writing ORV and AOV (6), `hq_country` Netherlands.** Nationale-Nederlanden (NN Leven: applicants under 51 insuring up to €1,000,000 often fill in only an online health questionnaire; BMI drives its healthy-weight test and premium); a.s.r. (ORV and AOV, to confirm); Achmea (Centraal Beheer, FBTO and Interpolis ORV); Allianz Nederland Leven (ORV; risk carrier behind a Dazure mortgage ORV, to confirm); Scildon (Lifestyle Hypotheek ORV, 2025, to confirm); Onderlinge 's-Gravenhage (ORV and AOV mutual, to confirm). Labels with no risk of their own (TAF, Dazure, Hera Life) are not rows.

**B. European reinsurer head offices, life and health outside the UK (4 named, 2 in Open question 2).** Swiss Re, row `Swiss Re Switzerland` (Zurich: L&H underwriting, Magnum and Life Guide); Munich Re, row `Munich Re Germany` (German L&H market; co-developer of vers.diagnose, to confirm); Hannover Re, row `Hannover Re Germany` (L&H Germany; hr | ReFlex covers life, critical illness and disability); SCOR, row `SCOR France` (Paris: L&H). Open: Gen Re, row `Gen Re Germany` (General Reinsurance AG, Cologne: Life/Health Germany and Europe; EQuot co-developer) and RGA, row `RGA Ireland` (RGA International Re, Dublin; Cologne and Amsterdam branches). Country-suffixed rows keep the bare parents and US entities open for Nick (Validation criteria, Schema).

**C. Point-of-sale risk-check platforms and engines (3), partnership lane only.** vers.diagnose (Germany: about 280,000 risk checks in 2024, about 350,000 expected in 2025, from about 100,000 intermediaries; real-time final decisions for BU and term life); Morgen & Morgen (EQuot in M&M Office, built with insurers and Gen Re); Munich Re Automation Solutions (ALLFINANZ, Dublin; automated underwriting for Allianz applicants in the Netherlands, per Celent, undated).

**Count:** 7 + 12 + 6 + 4 + 3 = 32 named (34 with Open question 2). Expected IN: about 27.

**Why this cut, not another:**
- **Ireland: build is declared under non-medical limits; instant broker decisions are to confirm.** Mortgage protection "is required by law when taking out a mortgage in Ireland unless you cannot get cover due to age or health"; an existing life policy with enough cover can be used (CCPC). BPFI counted 46,358 mortgage drawdowns in 2025, including re-mortgage and switching loans and 3,280 top-ups: an upper bound on new protection applications. Zurich Life Ireland's current non-medical limits ask no routine medical evidence for life cover up to €1,000,000 to age 35 (€800,000 to age 40), so build there is declared. Laya Life's form asks height and weight; its site sells cover online "in minutes" with "no medical exam needed". Zurich Life runs an online route with the client present (undated); the latest source on immediate acceptance through brokers is New Ireland's, 2007 (Risk 10). Broker-sold and English-speaking.
- **Germany has the volume, and its risk checks moved to the point of sale.** Two in-force counts, different scopes: about 14.3 million BU policies at the 61 providers Morgen & Morgen rates, new business up about 10% (May 2025); market-wide, 5.63 million standalone disability policies plus 11.11 million riders (16.7 million, wider than BU) against 45.9 million people in work (Franke und Bornberg, 2026). Together about 14 to 17 million; never in copy. Brokers run risk checks on platforms that decide during the meeting (group C; Alte Leipziger 70%). Build is priced at the quote: Die Bayerische adds a 12% loading when BMI or smoking misses its preferred criteria, more further from normal BMI; LV 1871's BU health questions cover BMI in particular.
- **The Netherlands asks build on one industry form.** The Verbond van Verzekeraars standard health declaration (2025) asks height in centimetres and weight in kilograms. NN accepts many ORV applications on an online questionnaire alone and uses BMI for its healthy-weight test. Stable ORV market: 35 products, no new provider for six years (MoneyView, January 2026).
- **Reinsurers co-own the build rating.** Swiss Re's Magnum processes more than 12 million policies a year in 20+ markets; hr | ReFlex covers disability as well as life; Munich Re co-developed vers.diagnose (to confirm) and owns ALLFINANZ; Gen Re co-developed EQuot.
- **Out, and why.** France: since 1 June 2022 (Loi Lemoine) no health questionnaire when the insured share is €200,000 or less per borrower and the loan ends before age 60. Belgium, the Nordics, Switzerland and Austria: not researched in this round; second-wave candidates (Open question 1). Italy, Spain and Poland: protection sold mostly with mortgages through bank branches (a judgment, not researched). Helvetia and Baloise (merged 5 December 2025) stay out in any wave (recent-deal rule). Group and collective cover is out everywhere (Anti-cases).

**Size:** `icp-detail.md` §3 sets $5M+ revenue; every candidate clears it on premium income (Acorn Life and Onderlinge 's-Gravenhage to confirm).

## Use case (1 sentence)

An insurer in Ireland, Germany or the Netherlands adds a two-photo step to its point-of-sale application, and FitXpress flags any gap between declared and estimated weight that crosses the insurer's own threshold.

## Why this is plausible (3 reasons grounded in evidence)

1. **Many decisions are made at the point of sale, on typed-in build.** Figures in Sub-segment (Why this cut): German risk checks decided in real time on broker platforms (about 350,000 expected on vers.diagnose in 2025) or in the advice meeting (about 70% at Alte Leipziger); Dutch ORV often accepted on an online questionnaire alone (NN); Irish life cover within non-medical limits (Zurich Life Ireland), with height and weight on the application (Laya Life form). In each, height and weight are what the applicant or broker types.
2. **Declared build runs light, and build is priced at the quote with measured weight asked only afterwards.** RKI: with self-reported data "body weight is often underestimated compared to standardized measured values, while body height tends to be overestimated". Die Bayerische prices BMI in the quote program and removes a BMI loading only after two weighings six months apart by a doctor or pharmacy. NN: an overweight applicant pays a higher premium that a later healthy BMI does not lower. No German, Dutch or Irish court or ombudsman decision on declared weight was found. Market context only, never copy (Rules).
3. **FitXpress adds evidence, the insurer decides, and the evaluation path is ready.** Outputs and citable numbers: Rules (from `proof-points.md` and the landing). Pilot path (landing): walkthrough, shadow evaluation with outputs kept out of decisions, comparison with independent build evidence on criteria agreed in advance. EU fit (`compliance.md`): not a medical device under the EU MDR for its current intended purpose; GDPR roles, DPA with SCCs. **Limits:** no insurer reference; AWS hosting in US regions, no EU hosting; not a calibrated scale; overstated height not caught; performance for people with physical disabilities not established; no blood pressure or other screening values.

**What the flag can separate from estimate error.** At about 3.5% mean absolute error the typical error is about 2.5 kg at 70 kg and 3.5 kg at 100 kg (arithmetic on the product figure). The RKI gives the direction of self-report bias, not its size. Assume the typical gap sits inside that error: the flag does not correct a typical applicant's weight and is not sold that way. It refers gaps several times larger, across the insurer's own BMI band, preferred-tariff line or referral threshold, set above the error (Risk 3).

**Why now:** AXA Life Europe underwrites Laya Life from 22 July 2026; Alte Leipziger launched e-Risiko in July 2026; InterRisk joined vers.diagnose in November 2025. Life and health risk assessment and pricing is an EU AI Act Annex III use, high-risk obligations from 2 December 2027 (Regulation (EU) 2026/1744); EIOPA's August 2025 opinion covers third-party AI. Buyer context only.

## What earlier campaigns teach this one

- **Olena's baseline** (`2026-07-21-eu-telehealth-weightloss`): 292 invites, 73 accepted (25.0%), 4 replies (5.5% of accepted), no product specific in Message 1; specifics are now a gate.
- **A reply asked for something to forward** (`2026-09-14-eu-erakulis-similar`): Message 2 may carry the landing as the forwardable page.
- **Consistency is a stated objection** (`2026-10-07-eu-weight-loss-nutrition`, a decline): answered in the objections below.
- **The UK twin has no replies yet** (176 imported on 2026-10-26); Open question 10.
- **Insurers route** (`2026-08-14-au-digital-fitness`: at AIA Australia a life product and pricing lead named a colleague). Pricing and product leads stay in the pull.
- **Say what the record is, in plain words** (a UK reply asked if it was a BMI-from-a-photo app). Message 1 asks, Message 2 offers the call, every lane.

## Target buyer persona

**Who buys:** the owner of evidence requirements and the build rating for new individual business: chief underwriter or head of underwriting (Ireland), Leiter Antrags- und Risikoprüfung, Gesellschaftsarzt and the Biometrie product owner (Germany), head of medical acceptance, medisch adviseur and ORV and AOV product owners (Netherlands); L&H underwriting, R&D, automation and client-solutions heads at reinsurers; managing director, product or underwriting lead at platforms.

- **Why these titles, not others:** risk-assessment and medical-acceptance heads own which questions are asked, which answers trigger evidence and how build is rated; product owners place the step; the medical officer decides what an estimate may be used for. CRO, CIO and distribution heads are group-wide or broker-facing. Of the other `icp-detail.md` §3 titles, innovation, digital transformation and insurtech leads are pulled (P2 `proposition` with visible life, BU, protection or underwriting scope, else P3 `referral`); Population Health Director (a US health-plan role with no seat in European life new business) and compliance and fraud-prevention teams (they do not own the evidence a case collects, and fraud framing is banned in copy) are not. Product managers come through the Biometrie, protection and product lines; a bare product-manager filter at a multi-line group returns motor, home and pension owners.
- **What they care about (KPIs):** share of applications decided at the point of sale; time to decision; evidence cost per case (doctor's or internist examination, nurse or GP evidence in Ireland); terms changed after application; broker experience; consistent, documented and fair decisions; claims later contested over health answers (never in copy).
- **Objections they will likely raise, with the honest answer:**
  - An estimate is not a weighing, and the typical gap is probably inside your error. True: Smart Scales is a software estimate at about 3.5% mean absolute error under evaluated conditions, about 2.5 to 3.5 kg at 70 to 100 kg. The flag refers only gaps well beyond that, on the insurer's threshold; the rest keep their current path.
  - How many cases would that catch? Unknown until a shadow evaluation on the insurer's own applicants counts flags per threshold and agreement with independent build evidence.
  - A second source could make our data inconsistent. The declared answer stays as it is; the record sits beside it on the case file, and only the insurer's threshold turns a difference into a referral.
  - We would never decline on photos. FitXpress does not make underwriting decisions; the insurer's rules and underwriters do.
  - Body photos are health data, and where is the data? The insurer decides the legal basis and where the step is offered. GDPR roles, AWS hosting (primarily US-West-2, partly US-East-1, no EU hosting) and photo handling exactly as in `compliance.md`; documents through legal@3dlook.me.
  - Is this high-risk AI for us? FitXpress returns an estimate and a flag and decides nothing; classifying the workflow is the insurer's assessment.
  - Is it fair for everyone? Validation covered ages 16 to 78, heights 150 to 220 cm, weights 38 to 210 kg, US and European participants; performance for people with physical disabilities is not established, and anyone who does not scan keeps the current route.
  - Which insurers use it? None yet. The same capture, processing and integration run in production in remote BMI-verification and weight-management workflows; 3DLOOK has worked with 100+ clients.
  - Does it check height? No. Height comes from the application.
- **Tiers (order only; one import file):** P1 Chief Underwriting Officer, Chief Underwriter, Head of Underwriting, head of (Antrags- und) Risikoprüfung, head of medical acceptance, CMO or lead Gesellschaftsarzt, Head of Protection or Biometrie at an insurer; L&H underwriting head for Germany, the Netherlands, Ireland or Europe and head of underwriting R&D or automated underwriting at a reinsurer; managing director, CEO or CPO at a platform. P2 underwriting development, rules, philosophy, research, automation and solutions leads; client underwriting managers; medical officers and medisch adviseurs; BU, term-life, ORV, AOV and protection product managers; new-business heads; life and disability pricing heads (`proposition`); innovation, digital-transformation or insurtech leads with visible life, BU, protection or underwriting scope. P3 underwriting managers, CTOs, heads of product without visible life scope, DPOs, group-wide innovation, transformation and insurtech leads. P4 referral.
- **Lanes by title:** `underwriting` (underwriting and risk-assessment leadership, development, rules, philosophy, research, automation, underwriting managers); `medical` (CMOs, Gesellschaftsärzte, medical officers, medisch adviseurs, at group B too); `proposition` (protection and Biometrie heads, BU, term-life, ORV, AOV and mortgage-protection product managers, new business, pricing, and innovation, digital or insurtech leads with life scope at an insurer); `reinsurance` (everyone else at group B except CTOs and DPOs); `partnership` (group C except CTOs and DPOs); `technical-integration` (CTOs, architects, DPOs and Datenschutz owners, new-business security owners); `referral` (anyone Vadim adds at step 4 from outside these functions, and group-wide innovation or transformation leads at an insurer).
- **Location rule (step 4 applies it):** a group A person must be located in the entity's country (Ireland, Germany or the Netherlands; Allianz by the split in Validation criteria); a group B person in the row's head-office country (Switzerland for `Swiss Re Switzerland`, Germany for `Munich Re Germany`, `Hannover Re Germany` and `Gen Re Germany`, France for `SCOR France`, Ireland for `RGA Ireland`); a group C person in Germany or Ireland. Anyone outside the row's country is FAIL, including a reinsurer's German, Dutch or Irish market team outside its head-office country (count reported, Open question 12). Anyone in the UK is FAIL whatever the title says ("UK & Ireland", "Europe"): katerina already contacted the London teams. A group B head-office team serving a market outside this cut (France, Italy, Spain, the Nordics and others) is WEAK and offered to Vadim.
- **Not the buyer (FAIL, or a skipped pool at step 4):** individual underwriters, Risikoprüfer and acceptanten unless the title says development, rules, philosophy, research, automation or lead; claims heads and Leistungsprüfung (Open question 8); broker managers and sales (Maklerbetreuer, Vertrieb); anyone at a multi-line group outside life, disability or protection (motor, property, private health, occupational pensions, investments); P&C staff at reinsurers.

### Target buyer persona: Sales Navigator pull for step 3

**Pull by title filter inside the approved company list, never by company alone.** Geography is added by hand (`sales-nav-query` writes none): A-IE "Ireland", A-DE "Germany", A-NL "Netherlands", group B the row's head-office country (never the United Kingdom), group C "Germany" and "Ireland"; one export file per geography, which keeps the two Allianz rows apart. Several lines match inside longer titles (Risikoprüfung finds Leiter Antrags- und Risikoprüfung; Acceptatie finds Manager Medische Acceptatie). Group C leaders are added by name at step 3; a CEO line would pull every insurer's board.

**Life and BU filter for German multi-line groups and head offices** (Allianz, HDI, Die Bayerische, Nürnberger, Munich Re, Hannover Re, Gen Re). Under geography Germany the English underwriting and `Head of Product` lines likely return mostly P&C and specialty staff; German life underwriting sits under Risikoprüfung. For these seven add title exclusions `Property`, `Casualty`, `P&C`, `Motor`, `Kfz`, `Komposit`, `Schaden`, `Haftpflicht`, `Industrial`, `Specialty`, `Marine`, `Cyber`, `Engineering`, `Krankenversicherung`, and the keyword filter `Leben OR Life OR Biometrie OR Berufsunfähigkeit OR BU OR Risikoleben OR "L&H"` on the English lines. Volume (estimate, not measured): the UK Apollo title pulls gave 46 to 49 people at Aviva and Zurich UK and 13 to 15 at the largest London reinsurer branches, about 40% PASS; with the filter expect 30 to 60 rows per German company, 300 to 500 for the seven, several times that without. A company over 80 rows after the filter is narrowed before step 4.

```titles
Chief Underwriting Officer
Chief Underwriter
Head of Underwriting
Underwriting Director
Director of Underwriting
Underwriting Philosophy
Underwriting Development
Development Underwriter
Underwriting Rules
Underwriting Research
Underwriting Manager
Head of Underwriting Solutions
Automated Underwriting
Client Underwriting
Underwriting Innovation
Head of Life and Health
Head of Life & Health
Chief Medical Officer
Medical Officer
Head of New Business
Head of Protection
Protection Proposition
Protection Pricing
Risikoprüfung
Antragsprüfung
Gesellschaftsarzt
Biometrie
Medisch adviseur
Acceptatie
Chief Product Officer
Head of Product
Head of Innovation
Digital Transformation
Insurtech
Chief Technology Officer
Data Protection Officer
Datenschutzbeauftragter
```

**`cap_per_group: 50`** (default for every campaign; only Vadim changes it). After the title and geography filters no group is expected near 50; if Allianz, Swiss Re or Munich Re comes back over it, the validator ranks by tier and Vadim decides.

## Message angle: lanes, account facts and the content asset

Every person gets exactly one lane, spelled as below. Numbers come only from Rules. Lane notes are instructions to the writer; none of their sentences goes into a message.

**The angle, for every lane (a target; each writer finds new words for each person):** the company's applications that see no doctor's examination or weighing and carry declared build. Each message says in its own words what the scan record would add to those cases, and that the company's threshold, rules and underwriters decide. No stock label for the scan or the record repeats across people at one company. What comes back is listed once, in Rules (What the scan is). For reinsurers, the same evidence as a candidate for a client evaluation and for the build section of a manual or rules engine. For platforms, the same evidence as a step their risk check could offer insurers through one integration.

**Lanes:**
- **`underwriting`** Target: how build is handled on point-of-sale cases today and which gaps would change a build rating. The flag is a referral trigger for gaps large enough to cross the company's own BMI band, preferred-tariff line or referral threshold, set above the estimate's error; never suggest it settles small differences or corrects each applicant's weight. Question targets: how build is checked on cases that never see a doctor's examination; at which band edges a gap between declared and estimated weight would change the outcome; what the team needs to see in a shadow evaluation before any output reaches a case; how build is treated on BU against term life (Germany), on ORV against AOV (Netherlands), or on mortgage protection against specified illness (Ireland). Message 2 value: the evaluation path, which counts flags per candidate threshold and agreement with independently collected build evidence.
- **`medical`** Target: what an estimated value may and may not be used for. Its defensible use is a referral threshold set well above the estimate's error, on gaps that would change the rating. Question targets: what a medical officer would need to know about a software weight estimate before it enters referral rules; how far above the estimate's error a threshold would have to sit; how the company's medical guidance treats a declared weight against a doctor's or pharmacy weighing. Message 2 value: the estimate's stated error under evaluated conditions, that it is not a scale reading, that the insurer sets the threshold, and the not-a-medical-device boundary.
- **`proposition`** Target: where the step sits in the journey. Question targets: where a two-photo step could sit (the broker's risk check, the direct online journey, the online health questionnaire sent after the application in the Netherlands, the adviser's mortgage-protection application in Ireland); how a new step is tested with brokers; how drop-off is measured. Pricing heads: how build loadings and evidence cost are weighed. Message 2 value: under 45 seconds from the photos, results to the insurer's systems, completion measured in the evaluation.
- **`reinsurance`** Target: evaluating new evidence with client insurers in these markets. Question targets: how the team tests a new remote evidence source with a German, Dutch or Irish client; whether any client has asked about remote build evidence; how a build flag would sit in the manual or engine the team supports (its own product named only to its own team: Magnum and Life Guide to Swiss Re, hr | ReFlex to Hannover Re). Message 2 value: a shadow evaluation design the team could run with one client. Never mention another reinsurer, any client of theirs, any pilot, or the group's UK teams.
- **`partnership`** Target: one integration that several insurers could switch on. Question targets: how a new evidence step is added to the platform's risk check or decision journey; what insurer clients ask the platform for at the point of sale. Message 2 value: API and web and mobile SDKs, one timestamped record per applicant returned to the platform. Its own product (vers.diagnose, EQuot, ALLFINANZ) only in its own copy.
- **`technical-integration`** Target: vendor review and integration, technical tone. Question targets: how a new data processor is reviewed for the new-business journey; how an SDK step enters the e-application; how a structured record reaches the underwriting system. Message 2 value: REST API and SDKs, the GDPR compliance line, photo retention (deleted after processing or within 30 days, per the insurer's policy, retained photos blurred, faces obscured at capture) and scan records on random identifiers; documents through legal@3dlook.me.
- **`referral`** Message 1: what the record is and why it matters to this company's point-of-sale cases, then one question about the person's own work. Message 2: a value line that continues their question, the call offer with the calendar link, and an easy out that points to whoever owns risk assessment or the new-business journey there, worded fresh for each person.

**Question bank discipline (big pools).** Each person gets one question nobody else at the company gets, built from their title. One topic serves at most about a fifth of a company's people. Wording, hook, structure, easy-out target and closer never repeat at one company.

### Account facts (filled after step 2)

Not written yet. After step 2 a fresh `hypothesis-generator` round writes one bullet per IN group from `companies.md`, in the UK format: one to three dated facts with URLs, then `Use:` and `Never:`. Until then a writer uses no company fact beyond the person's title and the company's line of business, and treats these as standing Never items for every account (the names here that are not accounts are also in `banned_terms`):
- ownership, deals and group links, in either direction: Swiss Life Deutschland's stake in vers.diagnose, Munich Re's ownership of ALLFINANZ, Generali's ownership of CosmosDirekt and Dialog, AXA's purchase of Laya, Bank of Ireland and New Ireland, Allianz as risk carrier for a Dazure product, Chesnara and Scildon, the BarmeniaGothaer merger;
- the UK sister companies and their teams (Aviva, Royal London, Zurich UK, Swiss Re UK and the other London branches), UnderwriteMe at Aviva Ireland, and any former underwriter of a product (iptiQ at Laya);
- face or video BMI studies at any reinsurer (Hannover Re's South Africa study, Gen Re's 2019 prototype), named or not;
- a company's figures (premiums, policy counts, shares, the 70% or 12% figures), its vacancies, and any claims or court matter.

### Content asset in Message 2

At most one 3DLOOK link next to the calendar link: the landing https://3dlook.ai/for-insurance-underwriting/ in any lane, or in `technical-integration` the privacy FAQ https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/ instead. Both HTTP 200 on 2026-10-29. Not linked: the hub article `/content-hub/mobile-body-scanning-insurance-underwriting/` (US sources and terms) and `/fitxpress/for-insurance-underwriting/` (404 until `/fitxpress/` ships).

## Rules for steps 3-5

- **Sender and format:** Olena, English only, every country (standing decision 2026-09-14). Readers are German, Dutch and Irish underwriters and doctors, many in a second language: short sentences, one idea each, plain words, no idioms. `Olena` alone on the last line. Connection request with no note. Message 1 ≤ 600 characters, Message 2 ≤ 550. Register: peer to a senior underwriter, formal, specific, no enthusiasm words.
- **Message 1:** context about this company and one question; no call ask, no link of any kind. **Message 2:** a call offer and https://meetings.hubspot.com/olena-kudriavtseva as plain text, in every lane, referral included. No call length or minutes in any message.
- **Landing URL (Vadim's UK decision 2026-10-22, carried over).** Message 2 may carry https://3dlook.ai/for-insurance-underwriting/ as plain text, on its own, with no punctuation glued to it; the calendar link stays required. Optional per person: at one company no more than about half of the Message 2s carry it, and the sentence around it differs each time. Never in Message 1.
- **US-worded background in the card.** The use-case and ICP excerpts in the card are US-worded background. This campaign's idiom, compliance lines and banned terms override them; no message carries HIPAA wording.
- **Lanes are exactly** `underwriting`, `medical`, `proposition`, `reinsurance`, `partnership`, `technical-integration`, `referral`.
- **European idiom.** Write insurer, application, point of sale, risk check or risk assessment, medical evidence, doctor's or internist examination, referral to an underwriter, terms, loading. The market product may be named once in plain English with its local short name where the reader uses it: occupational disability cover (BU), term life (ORV in the Netherlands, Risikoleben in Germany), mortgage protection and specified illness cover (Ireland). The landing's US terms (carrier, paramedical exam, face amount, APS, accelerated path) are never used.
- **What the scan is (a target; the writer picks the words).** Message 1 makes clear what comes back and who decides. The parts: two photos taken in the application, a Smart Scales weight estimate, BMI calculated from the height the applicant declared, a flag when the gap crosses the threshold the insurer sets, and one timestamped structured record returned to the insurer's systems. Every Message 1 carries the photos and the threshold flag; which other parts appear, in what order and in what words, varies between people at one company. A single label such as a BMI-from-a-photo app is never enough.
- **What it is not.** It does not make or recommend underwriting decisions, rate, price, accept or decline. It does not check height. It does not replace a doctor's examination, internist examination, the weighings an insurer asks for to review a loading, or any evidence the insurer's guidelines require; it adds evidence to cases that get none of these. It is never described as hidden, covert or mandatory for applicants: the insurer decides where it is offered and keeps its current route for anyone who cannot or does not scan.
- **Applicants are never suspects.** No message says or implies that applicants or brokers lie, hide or misstate anything. Talk about declared build and what the record adds. No claims, claim disputes, payouts withheld, courts, ombudsmen, complaints or regulators, for any company.
- **Lead with the record,** which is what the ICP calls defensibility: timestamped, structured, on the case file, the insurer's threshold, the insurer's rules. No accuracy percentage opens a message or appears in Message 1.
- **Numbers only from this list:** two photos (front and side), with "2 photos" as the numeric form; "under 45 seconds from the photos to structured results" (the only speed wording, as its own plain sentence and only where speed is the point); 80+ body measurements as an output, and a 3D model "when enabled for the deployment" (both secondary, never the lead); Smart Scales "approximately 3.5% mean absolute error under evaluated conditions", always with "not a scale reading" in the same sentence, Message 2 only, in `underwriting`, `medical` and `reinsurance` only; "3DLOOK has worked with 100+ clients"; "112,100 scans in 2025 across all 3DLOOK customers" as its own sentence, never tied to a country, insurance, a product flow or a client. No 96-97% or other measurement-accuracy figure, no repeatability figure, no validation-population figure in cold copy (replies use `accuracy-formulations.md`). No integration-time figure in any message. No market, survey, obesity, claims or prospect figures, and none of the landing's US statistics.
- **Smart Scales** is named without a "(beta)" label. It is a software estimate; never "weighs", never "measures weight". Never suggest the flag settles small weight differences or corrects each applicant's declared weight: it refers gaps above a threshold the insurer sets.
- **Proof without names.** No 3DLOOK client is named. The production line comes from the landing: "production infrastructure already deployed in remote BMI-verification and weight-management workflows". That quoted line is the only place the word verification may appear; verify, verified and verifies stay banned. Never imply an insurer or reinsurer uses FitXpress.
- **Compliance line: exactly one per pair, in Message 2, never in Message 1, never two.** By lane, verbatim:
  - `underwriting`, `medical`, `reinsurance`, `referral`: "FitXpress is not a medical device and does not make underwriting decisions." (the landing's sentence; it opens with the `compliance.md` short form and counts as the compliance line).
  - `proposition`, `partnership`, `technical-integration`: "In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes SCCs."
  Message 1 may say who decides in its own words without either line. Nothing about hosting location, EU hosting, data transfers, the AI Act or special-category data in cold copy; replies use `compliance.md` §10 and legal@3dlook.me. Never "compliant", "certified" or a medical-device claim.
- **Data handling sentences.** Only the forms in `compliance.md`: photos deleted after processing or within 30 days per the insurer's policy, retained photos blurred, faces obscured at capture; scan records on random identifiers; outputs stored until deleted by scan identifier on the customer's request. Never "not stored", "no personal data" or "anonymous".
- **Several people at one company.** Name the company in every Message 1. Never mention colleagues, other teams, a sister company or a conversation that did not happen. No two people at one company share an opener, a central question, an easy-out target, a Message 2 opener or a closer.
- **Never name one prospect in another prospect's copy,** including a reinsurer in an insurer's message, an insurer in a reinsurer's or platform's message, a platform in an insurer's message, and any vendor an insurer uses. A company's own product may be named in its own copy only. The rule covers message text; the linked landing citing public research by Gen Re and Munich Re is not a message naming a prospect.
- **Former employers** may be named (standing decision) unless they are an account in this campaign or in `2026-10-22-uk-insurance-underwriting`, a competitor or a banned term.
- **Word traps.** Never "objective" about our data; no em or en dash; no "plus" as a connector; no "so" introducing a benefit; no corrective "X, not Y"; none of the buzzwords on the hard-bans card.
- **No pricing and no trial terms** anywhere; a price or pilot-terms question goes to the call.
- **Writer notes and card instructions are not copy.** Lane notes, targets and rule sentences are never pasted; the quoted lines above are the only verbatim copy.
- **Message 1 gate.** Every message 1 carries at least one product specific from `proof-points.md` and one line that could only have been written to that company; each pair of messages cites at least one number. The gate recognises "two photos", "2 photos", "body measurements", "API" and "SDK" as product specifics (not "two guided photos" or "weight estimate" alone), and "under 45", "2 photos", "80+", "3.5%" and "112,100 scans" as numbers. Referral people included.

## Anti-cases (where it does NOT work)

- **Group and collective cover** (Irish group schemes, German Kollektivverträge and company pension disability cover, Dutch collective AOV and verzuim cover): members are accepted within free-cover limits without individual build questions.
- **Products with no health questions** (German BU or term life without health questions for set groups, funeral cover such as Sterbegeld and uitvaartverzekering, guaranteed-acceptance over-50s plans).
- **Private health insurance** (German PKV, Dutch health insurers, VHI, Irish Life Health, Laya Healthcare). Laya Life (life cover, AXA Life Europe) is in.
- **Closed books, run-off and consolidators** (Viridium in Germany, iptiQ's EMEA life business in run-off since March 2026) and **recent mergers** (Helvetia Baloise, completed 5 December 2025; `icp-detail.md` universal exclusion).
- **Labels and distributors without their own risk** (TAF, Dazure, Hera Life) and **brokers, broker pools and comparison sites** (Check24, Clark, Fonds Finanz, BCA, Independer, bonkers.ie). Platforms that run the insurer's own risk check (group C) are in.
- **Medical-evidence suppliers** (examination networks, internist and GP-report firms): a later partner conversation.
- **Cases above medical-evidence limits or with disclosed conditions:** an examination already measures height and weight; FitXpress adds nothing there.
- **Markets outside the cut:** France, Belgium, Italy, Spain, Poland, the Nordics, Switzerland and Austria primary insurers.
- **Any company whose application already runs a remote body, face or BMI-from-image capture:** held for Vadim.

## Vadim's standing decisions (already applied above)

1. **No headcount floor** (2026-09-29); the segment revenue threshold stays ($5M+ for §3).
2. **`cap_per_group: 50` for every campaign, no waves** (2026-09-29): one closely.io import file.
3. **A lane for every function** at an IN company (2026-09-29), applied inside the life, disability or protection business.
4. **FAIL only for the wrong company, people who left, identity collisions and duplicates,** along with this campaign's business-line and location rules; company-named profiles are held for Vadim.
5. **Former employers may be named** (2026-09-29), within the Rules' limit. **Live 3DLOOK pages may be linked as they are** (2026-09-29).
6. **No 3DLOOK client is named;** 112,100 scans as 3DLOOK-wide scale (2026-09-29); "3DLOOK has worked with 100+ clients" (2026-09-30). **Message 1 asks, Message 2 calls** (2026-10-07), every lane (`referral_call: yes`).
7. **Olena:** English only, every country (2026-09-14); `Olena` alone on the last line; calendar link in every Message 2.
8. **UK twin defaults (Vadim 2026-10-22, 10-26):** landing URL in Message 2 only, optional; Smart Scales named, 3.5% only in Message 2 of `underwriting`, `medical`, `reinsurance` with its qualifiers; platforms in `partnership`; claims heads not pulled, pricing P2 `proposition`; a target bought or merged within about 12 months is OUT, older deals never mentioned; a Sales Navigator TITLE pull with geography first (the UK company-wide export gave 45 PASS of 1,006), then Apollo; one compliance rule per lane (Rules).

## Vadim's decisions 2026-10-29

Vadim approved the hypothesis after the QC fix round (QC 15/20, report `workspace/_quality/outbound/2026-10-29-hypothesis-generator-eu-insurance-underwriting.md`) with «ok» to the twelve open questions as sent: every default taken.

1. **Approved:** `status: approved`, research may start. The cut is Ireland, Germany and the Netherlands, the four reinsurer head offices and three platforms; Belgium, then the Nordics, Switzerland and Austria, are a second wave only on his word.
2. **Gen Re Germany (Gen Re) and RGA Ireland are IN** as EU entities; bare parents and US entities stay open for Nick.
3. **Aviva Ireland and Royal London Ireland are IN:** `outbound-registry.py check --waive-companies "Aviva,Royal London"` lifts katerina's coverage company-wide; UK-located people FAIL at step 4.
4. **Zurich Life Ireland is IN;** Zurich Deutscher Herold only with evidence and his OK.
5. **Single-line insurer CEO or COO as P3 `referral`** where no underwriting owner is found, single-line life or protection insurers only.
6. **English copy** to German insurers.
7. **Smart Scales and the 3.5% figure** as in the UK campaign.
8. **Claims heads not pulled;** pricing heads P2 `proposition`.
9. **Helvetia Baloise OUT;** BarmeniaGothaer stays on the reserve list; AXA Life Europe IN.
10. **Run now;** a clear objection in the UK read-out before step 5 adjusts these Rules first.
11. **Landing US wording** is a non-blocking note for Asel.
12. **Reinsurer market teams outside the head-office country FAIL,** count reported at step 4; a country row only on his OK.
13. **People source** (carried from the UK twin): Sales Navigator title pull with the geography filter first, then an Apollo top-up with the credit count named before `enrich` if it exceeds 100.

## Validation criteria (Step 2 will check)

- **Companies.** 32 named candidates (34 with Open question 2's default); target 26-30 IN. Fewer than 22: stop and report to Vadim; never widen on your own (reserve list, Belgium, France, brokers, evidence suppliers) or add companies to reach a number. Each insurer writes new individually underwritten life, disability or protection business in its market in 2026 (product page, broker site or 2026 trade press); each reinsurer row is the group's L&H head-office entity in the row's country; each platform is used by insurers at the point of sale.
- **Schema.** `hq_country` Ireland, Germany, Netherlands, Switzerland or France as applicable. `icp_fit` high or medium only. Row names follow three rules, checked on 2026-10-29 with `company_keys` against every row and registry (no collisions):
  1. **Country suffix, never a bracketed place.** Group B: `Swiss Re Switzerland`, `Munich Re Germany`, `Hannover Re Germany`, `SCOR France`, `Gen Re Germany`, `RGA Ireland`. `record` registers the name without its bracket (`swiss-re-switzerland`); bare parents and US entities stay open for Nick. A bracket is an alias: `Swiss Re (Zurich)` would alias the insurer Zurich.
  2. **Parent alias in brackets** where exports show the bare parent, only if its slug has 4+ letters and matches no other row: `Swiss Re Switzerland (Swiss Re)`, `Munich Re Germany (Munich Re)`, `Hannover Re Germany (Hannover Re)`, `SCOR France (SCOR)` (4 letters, kept), `Gen Re Germany (Gen Re)`. `RGA` (3 letters) is dropped by the parser: Apollo rows join on `RGA Ireland`, Sales Navigator rows reading RGA are relabelled (Coordinator notes). Anyone an alias pulls in from outside the row's country FAILs by location. Aliases equal to katerina's slugs need the waiver: `Aviva Ireland (Aviva)`, `Royal London Ireland (Royal London)`.
  3. **No two rows share a bracket text:** `group_map` makes a shared bracket the import's company, so two `(Allianz)` rows would register bare `allianz`. Hence `Allianz Lebensversicherungs-AG (Allianz / Allianz Deutschland)`, `Allianz Nederland Leven (Allianz Nederland)`, and CosmosDirekt and Dialog without `(Generali)`.
- **Allianz split.** The two Allianz rows are separate groups for `cap_per_group`, the several-people rule and the location rule. Germany and Netherlands pulls are separate files; a bare `Allianz` cell in the Netherlands file is relabelled `Allianz Nederland Leven` before `extract-people`, else the alias sends it to the German row. Step 4 PASSes the German row only for Germany-located people and the Dutch row only for Netherlands-located people; other Allianz people, and German Allianz staff outside life and BU (P&C, private health, asset management, trade credit, assistance), FAIL. Copy never mentions the other Allianz company.
- **Registry.** `outbound-registry.py check --profile olena` after extract. Expected hits: `aviva` and `royal-london` (katerina). Default (Open question 3): `--waive-companies "Aviva,Royal London"`, which lifts katerina's company-level exclusion for those two slugs company-wide, for everyone whose company reads Aviva or Royal London wherever located; it has no location filter. The Ireland-only limit holds only because step 4 FAILs every UK-located person; person-level exclusions are never waived. `lv` (katerina's LV=) does not join LV 1871 (`lv-1871`), and katerina's `*-uk` reinsurer slugs match neither the country rows nor their aliases. Then compare every person URL with `katerina-registry.json` and the UK `people-approved.csv`; any match is FAIL, since `check --profile olena` does not see katerina's people.
- **Account facts and displacement.** For every IN company: one to three dated underwriting or proposition facts with URLs, and a search of its site, broker portal and trade press for any remote body scan, face or video BMI estimate or selfie quote. Known: Hannover Re (video BMI study, South Africa) and Gen Re (2019 selfie-BMI prototype, US and Asia): default IN, names banned, held if anything newer in Europe appears. No German, Dutch or Irish insurer hit on 2026-10-29.
- **People.** Location and business-line rules as in Target buyer persona. `apollo-pull.py search` has **no location filter**: every Apollo row is location-filtered at step 4; credit count to Vadim before `enrich` if over 100.
- **C-level availability.** Irish chief underwriters and reinsurer L&H heads are expected in Sales Navigator. German risk-assessment heads and company doctors may be thin on LinkedIn (untested): if a German insurer returns no P1 or P2 owner, record it and offer Open question 5 instead of widening titles.
- **Proof in product-info.** Use-case file and live landing: yes. Insurance reference customer: none (proof as Rules allow).
- **Message 1 gate.** As in Rules: every message 1 carries at least one product specific from `proof-points.md` and one line that could only have been written to that company; each pair cites at least one number. Zero client names, banned terms, links in Message 1, accuracy figures in Message 1, suspicion framing or decision claims; exactly one compliance line per pair, in Message 2, by lane. The gate fails any pair that misses one of these; `2026-07-21` sent its first messages with no specific and drew 4 replies on 73 accepted.

## Success metrics for this campaign

Denominators as in `metrics-final.json`. Senior underwriters and company doctors accept less readily than Olena's health lists, and German readers get English copy, so acceptance and reply targets sit at or below her July baseline (25.0% accepted, 5.5% replies per accepted).

| Metric | Target | Floor | Basis |
|---|---|---|---|
| Invites sent | 180-280 | 120 | about 27 IN companies after title and geography filters |
| Connection acceptance | 20% | 12% | `olena` July 25.0% |
| Replies per accepted person | 5% | 3% | `olena` July 5.5%; about 2 to 3 replies on 36 to 56 accepted |
| Positive replies (interest or a question) from P1-P2 | 2 | 1 | |
| Companies with at least one reply | 3 of about 27 IN | 1 | |
| Discovery calls | 1 | 1 within 8 weeks | |
| Shadow-evaluation conversations (insurer, reinsurer or platform) | 1 | 0 | the landing's pilot step |

**Falsified if** three or more P1 or P2 replies say build is not a material gap on point-of-sale cases, that an estimated weight cannot enter referral rules at any threshold, that body photos cannot be collected in a life application in their market, or that US hosting rules a vendor out. **Inconclusive** if fewer than 25 people accept. Results are read market by market (IE, DE, NL, reinsurers).

## Risks

1. **No insurer reference.** Underwriters may want a named European insurer before a call; the offer is an evaluation.
2. **US hosting meets EU procurement.** AWS US regions, no EU hosting, transfers under SCCs only; privacy reviews and DORA requirements for ICT third-party providers may stop a vendor at the first call. Nothing beyond `compliance.md` may be promised.
3. **The flag works on large gaps, and nobody knows yet how many there are** (What the flag can separate). The landing's sample payload flags a +3.3% gap, inside the estimate's error, and an underwriter may read it as the intended use. If a shadow evaluation finds few flags above the error at band edges, the value case is thin.
4. **Special-category data and the AI Act.** Body photos and build in a life application are health data (legal basis, DPIA); from 2 December 2027 life and health risk assessment and pricing are high-risk under Annex III, and EIOPA expects governance over third-party AI. Some will see a new AI input as added compliance work; classifying the workflow is the insurer's call.
5. **Language and reach.** English to German underwriters and doctors, whose LinkedIn presence is untested: the German pull may be thin and acceptance lower.
6. **Group overlap with the UK twin.** katerina contacted Aviva, Royal London, Zurich and the London reinsurer teams from 2026-10-26; copy never refers to it.
7. **Fragmented Dutch market.** Labels sell ORV on other insurers' risk; the underwriting owner may sit at the risk carrier.
8. **Landing in US idiom** (Open question 11).
9. **Small universe per market:** seven Irish and six Dutch insurers.
10. **Ireland's point-of-sale decisions are partly assumed.** Irish sources show declared build within non-medical limits and instant online cover at Laya Life; none current shows instant decisions through brokers (latest: New Ireland, 2007). If Irish replies say most broker cases wait for an underwriter, the Irish angle moves to evidence cost within non-medical limits.

## Open questions for Vadim

> Answered 2026-10-29: every default taken, see `Vadim's decisions 2026-10-29`.

1. **The cut: Ireland, Germany and the Netherlands, with reinsurer head offices and three platforms.** Default: yes. Second wave after the read-out: Belgium, then the Nordics, Switzerland and Austria (none researched yet); France only above the Loi Lemoine threshold.
2. **Gen Re and RGA in Europe.** The UK file left their parents for Nick; their European L&H units (General Reinsurance AG, Cologne; RGA International Re, Dublin, with Cologne and Amsterdam branches) are outside Nick's US geography. Default: both IN from `olena` as `Gen Re Germany (Gen Re)` and `RGA Ireland`, Germany- and Ireland-located people only; the bare parent slugs and the US entities of all six reinsurers stay unregistered and open for Nick.
3. **Aviva Ireland and Royal London Ireland against katerina's `aviva` and `royal-london`.** Irish staff often list the group page. Default: both IN; the waiver lifts katerina's coverage of the two slugs company-wide, and step 4 FAILs UK-located people (Validation criteria, Registry); the UK business is never mentioned.
4. **Zurich.** Default: Zurich Life Ireland IN as an Irish entity (`zurich-uk` is katerina's). Zurich Deutscher Herold is not listed (no 2026 point-of-sale evidence; a third Zurich entity); only with evidence and your OK.
5. **Single-line insurer CEO or COO as P3 `referral`** where the export holds no underwriting owner (your UK widening, 2026-10-26). Default: same rule for single-line life or protection insurers only (Acorn Life, Onderlinge 's-Gravenhage, Hannoversche, Europa, LV 1871, Volkswohl Bund), offered at step 4, never pulled by title.
6. **English to German insurers.** Default: yes, your standing rule for Olena; German titles only in the pull.
7. **Smart Scales and the 3.5% figure** as in the UK campaign. Default: carried over unchanged.
8. **Claims heads.** Default: not pulled (claims copy would touch disputes the Rules ban); pricing heads P2 `proposition`.
9. **Recent deals.** Default: Helvetia Baloise OUT (merged 5 December 2025); BarmeniaGothaer (merged September 2024) stays on the reserve list, the merger never mentioned (if you pull it in, its three spellings leave `banned_terms`); AXA Life Europe IN (AXA bought Laya in October 2023).
10. **Timing against the UK twin** (no replies pulled yet). Default: run now, as you asked; a clear objection in the UK read-out before step 5 adjusts these Rules first.
11. **Landing wording (non-blocking note for Asel).** The live page uses US terms (carrier, paramedical, face amount) and a +3.3% sample flag; none of this goes into copy and the campaign does not wait.
12. **Reinsurer market teams outside the head-office country** (for example RGA's Cologne and Amsterdam branches). Default: FAIL under the location rule, count reported at step 4; a country row such as `RGA Germany` only with your OK.

## Coordinator notes (outside every card)

- **Compliance count.** Rules say exactly one compliance line per pair, as message-sequencer does; the UK card's "at most one" split the UK batches.
- **DORA and the first name Dora.** A recipient named Dora trips the `DORA` ban in `check-messages`; the coordinator waives that single hit by hand.
- **Relabels before `extract-people`:** bare `Allianz` in the Netherlands file to `Allianz Nederland Leven`; Ireland-located RGA rows to `RGA Ireland` (Validation criteria).

## Sources

All read on 2026-10-29 unless dated.

- Ireland: CCPC https://www.ccpc.ie/consumers/money/insurance/mortgage-protection-insurance/ · BPFI 2025 drawdowns https://bpfi.ie/publications/bpfi-mortgage-drawdowns-report-q4-2025/ · Zurich Life Ireland NMLs https://www.zurich.ie/broker-centre/broker-resources/underwriting/limits-and-guidelines/ (table https://www.zurichlife.ie/static/documents/LG_NON_GI_LIFE_COVER_LIMITS/Life_Cover_Limits.PDF) · Zurich Life client-present route (undated) https://www.zurichlife.ie/static/documents/DOC_10888/UW_Initiative.PDF · New Ireland immediate acceptance (2007-09-10) https://www.techcentral.ie/system-fast-tracks-applications/ · Royal London Ireland 30.2% https://www.ifsc.ie/news/royal-london-ireland-new-business-sales-up-62-in-2025 · AXA Life Europe and Laya Life https://www.irishexaminer.com/business/companies/arid-41927366.html · Laya Life, 22 July 2026 and no medical exam https://www.layalifeinsurance.ie/ and https://www.layalifeinsurance.ie/termsandconditions/ · Laya Life form, height and weight https://www.layalifeinsurance.ie/media/layalife/pdfs/LIFE-AppForm.pdf · AXA bought Laya, October 2023 https://www.businesswire.com/news/home/20231031951649/en/Corebridge-Financial-Completes-Sale-of-Laya-Healthcare-to-AXA · Aviva Ireland on UnderwriteMe (undated) https://www.lifeinsuranceinternational.com/news/aviva-underwriteme-ure
- Germany, market: https://www.cash-online.de/a/morgen-morgen-bu-rating-2025-immer-mehr-top-tarife-697071/ (2025-05-09) · https://www.cash-online.de/a/arbeitskraftabsicherung-neue-ideen-braucht-das-land-709801/ (2026) · Hannoversche https://www.experten.de/id/4949367/Hannoversche-waechst-in-Biometrie-und-staerkt-Marktposition-in-der-Risikolebensversicherung/index.pdf · Cosmos 2023 https://www.versicherungsbote.de/id/4941098/Risikolebensversicherung-Marktfuehrer-beim-wichtigen-Hinterbliebenenschutz/ · Volkswohl Bund 2025 (1 June 2026) https://druckstuecke.volkswohl-bund.de/api/products/3074/documents/Pressemeldung%3A_Gesch%C3%A4ftszahlen_2025.pdf · Dialog https://www.cash-online.de/a/dialog-voll-elektronischer-antragsprozess-in-der-risikolebensversicherung-552124/
- Germany, point of sale: Alte Leipziger https://www.cash-online.de/a/bu-antrag-alte-leipziger-verkuerzt-entscheidung-mit-digitaler-risikopruefung-721259/ (2026-07-01) · vers.diagnose volumes https://www.interrisk.de/wMedia/docs/pressemeldungen/2025/202511_PM-versdiagnose-interrisk-11.25-02.pdf (2025-11) · Swiss Life stake https://www.franke-bornberg.de/sites/franke-bornberg/files/pressemitteilungen/2022-12-15_pressemitteilung_swiss-life-deutschland-erwirbt-franke-und-bornberg-research-gmbh.pdf · HDI https://www.versicherungsbote.de/id/4820775/HDI-Risikopruefung-Risikovoranfrage-BU/ · EQuot and Gen Re https://www.cash-online.de/a/bu-risikopruefung-230463/ · Nürnberger https://www.cash-online.de/a/nuernberger-nutzt-risikovoranfrage-tool-von-morgen-morgen-324042/ · Allianz Leben (2016) https://www.experten.de/id/4942234/allianz-leben-entscheidet-sich-fuer-equot/index.pdf
- Germany, build: Die Bayerische BU guide 10/2025 §3.2.4 https://www.diebayerische.de/dam/jcr:ba2b0ab0-3318-494a-90d6-c6a5c05a0458/B%20660314%C2%A0Leitfaden_BU_1025_bf.pdf · LV 1871 https://www.lv1871.de/berufsunfaehigkeitsversicherung/fragen/uebergewicht/ · RKI self-report bias https://www.rki.de/EN/Topics/Noncommunicable-diseases/Physical-health/Overweight-and-obesity/overweight-and-obesity-node.html (page dated 2026-07-15)
- Netherlands: Verbond health declaration 2025 https://www.verzekeraars.nl/media/2sth05ee/vvv_gv_zonder-aov_2025.pdf · NN https://www.nn.nl/Particulier/Verzekeren/Overlijdensrisicoverzekering/Medische-acceptatie.htm · MoneyView ORV 2026 https://download.moneyview.nl/specialitem/2026/01_ORV/SI-187_01-2026_ORV_D.pdf
- Reinsurers and engines: Magnum https://www.swissre.com/reinsurance/life-and-health/underwriting-effectively.html · hr | ReFlex https://www.hannover-re.com/en/life-and-health/reinsurance-services/underwriting-automation · ALLFINANZ and Allianz NL (undated) https://celent.com/news/506755799 · Gen Re Cologne https://genre.com/contactus/branch/europe-middle-east/cologne-lh · RGA International Re https://www.rgare.com/global-presence/global-presence-landing/ireland · iptiQ run-off https://healthcareandprotection.com/swiss-re-completing-withdrawal-from-iptiq/
- Displacement: Hannover Re video BMI https://www.hannover-re.com/en/life-and-health/inspire/underwriting-case-studies/ai-video-technology-for-health-and-risk-insights/ · Gen Re (2019) https://www.dig-in.com/news/gen-re-pilots-selfie-based-life-insurance-underwriting
- Out of cut: Loi Lemoine https://www.banque-france.fr/system/files/import/ccsf/medias/documents/cp_bilan_ae_loi_lemoine_15012024.pdf · Helvetia Baloise https://www.helvetia-baloise.com/corporate/hb/en/home/news-stories/publications/media-releases/2025/20251205.html · BarmeniaGothaer https://www.versicherungsbote.de/id/4915751/Fusion-von-Barmenia-und-Gothaer-offiziell-abgeschlossen/
- Regulation: AI Act Annex III 5(c) https://eur-lex.europa.eu/eli/reg/2024/1689/oj · Regulation (EU) 2026/1744, Annex III from 2027-12-02 (law-firm summary; check EUR-Lex) https://cdp.cooley.com/digital-ai-omnibus-delays-key-deadlines-introduces-new-rules/ · EIOPA AI opinion (2025-08-06) https://www.eiopa.europa.eu/eiopa-publishes-opinion-ai-governance-and-risk-management-2025-08-06_en · DORA https://eur-lex.europa.eu/eli/reg/2022/2554/oj
- Internal: UK twin `sales-nav-raw/apollo-*.csv` and `icp-validation-summary.md` · `2026-07-21-eu-telehealth-weightloss/metrics-final.json` · `2026-09-14-eu-erakulis-similar/responses-summary.md` · `2026-10-07-eu-weight-loss-nutrition/responses-summary.md`
