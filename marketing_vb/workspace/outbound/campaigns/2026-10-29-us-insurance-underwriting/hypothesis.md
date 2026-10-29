---
product: fitxpress
profile: nick
market: USA
created: 2026-10-29
status: approved
approved: 2026-10-29
use_case: fx-insurance-underwriting
cap_per_group: 50
referral_call: yes
banned_terms: [Yazen, UK Meds, Healthyr, Safariland, Burlington, Jim's Formal Wear, Generation Tux, Tailoor, Redthread, Prism, Bodygram, Size Stream, Fit:match, Mirrorsize, Bodd, Nuralogix, Anura, Lapetus, SelfieQuote, Binah, dacadoo, Alula, Life Lens, selfie, selfies, facial, MIB, LexisNexis, Milliman, IntelliScript, ExamOne, Quest Diagnostics, Portamedic, Clareto, Human API, TransUnion, Verisk, Equifax, credit-based, Legal & General, Banner Life, William Penn, Meiji Yasuda, Brighthouse, Aquarian, Hexure, FireLight, iCapital, Nippon Life, Bain Capital, Manulife, Dai-ichi, Sumitomo, Roper, AIG, MetLife, Haven Life, Policygenius, Lantern, Vitality, Aviva, Royal London, Zurich UK, VitalityLife, UnderwriteMe, Iress, Swiss Re UK, Munich Re UK, Hannover Re UK, SCOR UK, Gen Re UK, RGA UK, Pacific Life Re, LIMRA, 9 vs 27, 27 days, NAIC, DFS, Circular Letter, ECDIS, Colorado, unfair discrimination, disparate impact, regulator, regulators, FCRA, GLBA, HIPAA, BAA, FDA, SOC 2, CCPA, CPRA, GDPR, SCCs, MDR, compliant, certified, certification, accredited, clinically validated, clinically proven, verify, verified, verifies, guarantee, guaranteed, fraud, fraudulent, misrepresent, misrepresented, misrepresentation, misclassification, misclassified, slippage, non-disclosure, nondisclosure, liar, lying, dishonest, cheat, cheating, rescind, rescission, contestable, contestability, incontestable, obese, obesity, GLP-1, semaglutide, tirzepatide, Wegovy, Zepbound, Ozempic, Mounjaro, DEXA, DXA, BIA, bioimpedance, trial, acquisition, acquired, merger, run-off, adviser, advisers, programme, GP report, nurse screening, mini-screen, generic figure, never a promise, not a promise, context only, writer note, Circling back, Following up, Saw your post]
---

# Outbound Hypothesis: 2026-10-29, US accelerated life and disability underwriting (Nick)

- **Campaign:** `2026-10-29-us-insurance-underwriting`, the US twin of `2026-10-22-uk-insurance-underwriting` (katerina, UK, sent) and `2026-10-29-eu-insurance-underwriting` (olena, IE/DE/NL, approved today): same idea, landing and lanes. No UK or EU market fact is used as evidence; every US market fact below was sourced on the web on 2026-10-29 (Sources).
- **Owner and sender:** Nick Omelchak, profile `nick`, USA (`PROFILE_GEO["nick"]`); signature and calendar link in Rules.
- **ICP:** `icp-detail.md` §3 (Life & Disability Insurance Underwriting): insurers buy defensibility (audit trail, workflow integration, consistency) more than accuracy. §3 and the use-case file name Prudential, Guardian Life, New York Life and Lincoln Financial as US examples; MetLife, also named there, no longer sells retail individual life in the US (Anti-cases). Lemonade, a §3 insurtech example, is OUT: its agency sells term life as agent of Banner Life, which underwrites and issues the policies (Sub-segment, Out; Open question 10).
- **Use-case file and landing:** `use_case: fx-insurance-underwriting`; angle source https://3dlook.ai/for-insurance-underwriting/, re-fetched live on 2026-10-29 (curl, HTTP 200; the coordinator's fetch the same day agrees). The text of record `workspace/pages/for-insurance-underwriting/published-live-2026-10-21.md` is stale on one point: its l.32 credits the "9 vs 27 days" line to Gen Re, and the live page credits LIMRA (corrected by 2026-10-22, UK twin). The landing is written in US terms (carrier, accelerated path, paramedical exam, APS, face amount), which are native here. A landing number is not an approved claim by being there: its 59%, "#1" and "9 vs 27 days" lines stay out of copy (Rules, Risk 6).
- **Registry, checked 2026-10-29** (`outbound-registry.py status`, `global-company-registry.json`, all six registries): no US insurer, reinsurer or underwriting platform is registered to anyone. `katerina` holds 22 UK protection companies, among them `legal-general`, `guardian-financial-services`, `pacific-life-re`, `ipipeline-uk` and the London entities of the six reinsurers (`swiss-re-uk`, `munich-re-uk-life-branch`, `hannover-re-uk-life-branch`, `gen-re-uk`, `rga-uk`, `scor-uk`). The bare parents (`swiss-re`, `munich-re`, `hannover-re`, `scor`, `gen-re`, `rga`, `ipipeline`) are registered to nobody; olena's EU file will register only country-suffixed rows. `nick` holds 45 health and fitness companies; one slug to watch is `ladder` (the Ladder strength-training app, `2026-08-07-us-digital-fitness`), which is not Ladder Life (Validation criteria, Schema).

> **Read this first.**
> 1. **One idea, the twins' idea in US terms.** About 6 in 10 US individual life applications now qualify for an accelerated path (Gen Re, December 2025) that waives the paramedical exam and fluids, so build on those cases is what the applicant types. Build is the leading reason accelerated cases land in a different risk class when carriers check them later (Munich Re, January 2025). FitXpress adds a step inside the e-application: two photos, a Smart Scales weight estimate, BMI from the declared height, a flag on the carrier's threshold, one timestamped record. The carrier's rules and underwriters decide.
> 2. **Four groups:** US individual life and DI carriers with an accelerated or fluidless path; digital-first life companies that own an instant-decision journey; the US life entities of six reinsurers; three new-business and underwriting platforms. 34 named, about 28 expected IN.
> 3. **No carrier is a 3DLOOK customer.** The offer is an evaluation; proof only as Rules allow.
> 4. **The flag works on large gaps only.** Munich Re's own flag line for a material BMI understatement is 6%; at the same height that is a 6% weight gap, under twice the estimate's ~3.5% mean absolute error (Risk 3).
> 5. **HIPAA stays out of cold copy.** Life and DI underwriting sits outside HIPAA's covered-entity definitions (45 CFR 160.103), so the US compliance line's BAA clause is off-target here (Rules, Open question 4).
> 6. **Regulation is buyer context, never copy** (Risks).

---

## Vertical

US individual life insurance (term, universal and whole life) and individual disability income insurance underwritten on an accelerated or fluidless path, where build is the applicant's declared height and weight; with the US life reinsurers whose rules engines and manuals set the build rating and the platforms that host the e-application and the decision.

## Sub-segment

The companies that decide what evidence a US accelerated application collects and how build is rated: 34 named candidates in four groups, about 28 expected to pass step 2. No company is added to reach a number; each carrier must write new individually underwritten business with an accelerated, fluidless or no-exam path in 2026. Every row has `hq_country` United States except where marked.

**A. US individual life and DI carriers with an accelerated or fluidless path (22), candidates to verify.** Prudential Financial; New York Life; Northwestern Mutual; MassMutual; Guardian Life (row `Guardian Life (Guardian)`, life and individual DI); Lincoln Financial; John Hancock (US business of Manulife; Canada-located people FAIL); Pacific Life (the insurer; `Pacific Life Re` is katerina's); Protective Life; Transamerica; Principal Financial (life and individual DI); Nationwide; Securian Financial; Corebridge Financial; Symetra; Penn Mutual; Mutual of Omaha; Ameritas; Foresters Financial (US business; its US newsroom, 28 April 2026: accelerated underwriting in the US up to $2 million for ages 18 to 60 from 26 April 2026, with more applicants fluidless; Canadian head office, row `Foresters Financial US (Foresters Financial)`, US-located people only); Sammons Financial (North American Company); Thrivent; The Standard (individual DI). **Reserve, only if Vadim asks:** Equitable, Western & Southern, OneAmerica, Assurity, Illinois Mutual, Globe Life, Primerica.

**B. Digital-first life companies that own an instant-decision journey (3).** Ethos (Nasdaq: LIFE; instant decisions with no medical exam, cover up to $3 million on its site; policies issued by partner carriers); Ladder Life (row `Ladder Life`, never bare `Ladder`, Schema); TruStage (direct no-exam term, to confirm). Their founders and product heads own the application flow end to end.

**C. US life entities of the six reinsurers (6).** `RGA US (Reinsurance Group of America)` (Chesterfield, Missouri; RGA's US individual life underwriting and its AURA engine); `Gen Re US (Gen Re)` (Stamford, Connecticut; L&H US, author of the Next Gen Underwriting Survey); `Munich Re Life US (Munich Re)` (Atlanta, to confirm; author of the accelerated-underwriting monitoring studies and owner of alitheia); `Hannover Life Re America (Hannover Re)` (Orlando, Florida); `SCOR Life Americas (SCOR)` (Charlotte, North Carolina; Velogica; entity name to confirm); `Swiss Re Americas (Swiss Re)` (Armonk, New York; Magnum). Country rows keep katerina's `*-uk` slugs and olena's EU rows apart (Schema).

**D. New-business and underwriting platforms (3), partnership lane only.** `iPipeline US (iPipeline)` (iGO e-application; a Roper Technologies business; `ipipeline-uk` is katerina's); Zinnia (The Policy Processor, which Zinnia calls its underwriting platform for life and annuity carriers; version 8.0 launched on 4 November 2025, in use at more than 15 of the largest North American carriers); Bestow (carrier software with a configurable rules-and-decision engine; sold its own carrier to Sammons in 2024). **Out:** Hexure (FireLight), agreed to be acquired by iCapital on 17 March 2026 (recent-deal rule).

**Count:** 22 + 3 + 6 + 3 = 34 named. Expected IN: about 28.

**Why this cut, not another:**
- **The accelerated path is the US mainstream, and build on it is declared.** Gen Re's 2025 survey (released 17 December 2025): on average 59% of US individual life applications qualify for an accelerated path. Munich Re defines accelerated underwriting as waiving fluids and medical exams for a subset of applicants in an otherwise fully underwritten process. Limits keep rising: Foresters lifted its US accelerated limit to $2 million (ages 18 to 60) from 26 April 2026; Ethos sells up to $3 million with no exam. LIMRA: individual life new annualized premium topped $17.5 billion in 2025, up 10%, policy count up 7%.
- **Carriers already measure the gap after issue, and build leads it.** Carriers monitor accelerated programs with random holdouts (cases sent to full underwriting before the decision) and post-issue audits (APS or electronic health records after the offer). Munich Re (16 January 2025): build and BMI is the leading reason a case lands in a different class, equally common in both methods. Munich Re (21 July 2020): BMI understatement of 20% or more of applicants in fully underwritten programs, expected higher on the accelerated path; BMI is the second-largest disclosure concern after tobacco; the likelihood rises with true BMI but is flat across declared BMI, so the declaration alone cannot show who is off.
- **Reinsurers co-own the build rating.** Their engines and manuals sit inside carriers' accelerated programs (RGA's AURA NEXT runs inside FireLight, 2021; Swiss Re's Magnum, SCOR's Velogica, Munich Re's alitheia). They run the monitoring studies above and are a route to several carriers.
- **Platforms host the step where build is keyed:** the e-application (iPipeline iGO; Foresters put its new accelerated pre-screen checklist into iGO in April 2026) and the underwriting workbench (Zinnia's The Policy Processor, Bestow).
- **Individual DI is in** because build is rated there too and the same carriers (Guardian, MassMutual, Northwestern Mutual, Principal, The Standard) write it; the pull reaches DI underwriting and product heads by title.
- **Out, and why:** group life and group benefits (MetLife's US business, worksite voluntary), guaranteed and simplified-issue final expense, annuity-only writers, health plans (UnitedHealthcare, Humana, Cigna, Aetna, Oscar: `icp-detail.md` §3 lists them, but they do not rate build at application), brokers, BGAs and IMOs, exam and evidence vendors (Anti-cases). Lemonade (an `icp-detail.md` §3 insurtech example) is OUT on the brokers' ground: its life page (read 2026-10-29) says its agency acts as agent of Banner Life, whose products Banner Life underwrites and issues, which leaves the build rule and the decision with a carrier that is itself OUT as a recent deal (Open question 10). Recent deals: Legal & General America (Banner Life, William Penn) completed its sale to Meiji Yasuda on 2 February 2026; Brighthouse is being acquired by Aquarian (pending regulatory approval, Q2 2026 10-Q); Hexure by iCapital (17 March 2026). All three are OUT, never mentioned.

**Size:** `icp-detail.md` §3 sets $5M+ revenue; every group A and C candidate clears it on premium; Ladder Life and the platforms are to confirm.

## Use case (1 sentence)

A US life or DI carrier adds a two-photo step to its accelerated e-application, and FitXpress flags any gap between declared and estimated weight that crosses the carrier's own threshold, as structured build evidence on accelerated files that otherwise hold only the applicant's declared height and weight.

## Why this is plausible (3 reasons grounded in evidence)

1. **Most US applications can skip the exam, and on those cases build is typed in.** 59% of US individual life applications qualify for an accelerated path on average (Gen Re 2025 survey, December 2025); accelerated limits reach $2 million at Foresters (April 2026) and $3 million at Ethos. Accelerated underwriting waives fluids and medical exams (Munich Re definition), so height and weight are the applicant's declaration.
2. **Declared build runs light, and build is the leading reason accelerated cases are reclassified.** In US national survey data from 1999 to 2016, self-reported BMI ran below measured BMI and self-reported height above measured height in all three federal surveys (Flegal et al., Obesity 2019); in NHANES the measured average BMI was 29.23 against 28.49 self-reported (USDA ERS); about one in six or seven adults with obesity is classed non-obese on self-report (Hattori and Sturm, NHANES 1999-2008). 40.3% of US adults live with obesity (CDC NCHS Data Brief 508, August 2021 to August 2023). In carriers' own monitoring, build and BMI is the leading reclassification reason (Munich Re, 2025), and Munich Re's 2020 study used a 6% BMI understatement as the flag that "is typically large enough to cause a shift in assigned underwriting class". Market context only, never copy (Rules).
3. **FitXpress adds evidence, the carrier decides, and the evaluation path is ready.** Outputs and citable numbers: Rules (from `proof-points.md` and the landing). Pilot path (landing): walkthrough, shadow evaluation with outputs kept out of decisions, comparison with independently collected build evidence on criteria agreed in advance; it counts completion and retake rates, agreement with reference evidence, flags per candidate threshold and the effect on review volume. US fit (`compliance.md`): AWS hosting in US-West-2 and US-East-1; TLS in transit, SSE-S3 at rest; photos deleted after processing or within 30 days; does not make underwriting decisions. **Limits:** no insurer reference; not a calibrated scale; overstated height not caught; performance for people with physical disabilities not established; no blood pressure, lab or tobacco values; not cleared, authorized or approved by the FDA (replies only).

**What the flag can separate from estimate error (the Smart Scales honesty point).** At about 3.5% mean absolute error the typical estimate error is about 2.8 kg at 80 kg and 3.5 kg at 100 kg (arithmetic on the product figure). The average US self-report gap (29.23 against 28.49 BMI, about 2.5%, part of it from overstated height) sits inside that error: the flag does not correct a typical applicant's weight and is never sold that way. Munich Re's material-gap line is a 6% BMI understatement; at the same height that is a 6% weight gap, less than twice the mean error. `proof-points.md` publishes only the mean error, not its spread or its behaviour by BMI band, so how many accurately declared applicants a 6% threshold would flag is unknown. Assume the carrier's threshold must sit above 6% and catches only the larger understatements, which Munich Re places at higher true BMI. The shadow evaluation measures both (Risk 3).

**Why now:** accelerated limits keep rising (Foresters, April 2026); carriers keep expanding fluidless underwriting to larger cases; about 25 states and Washington, D.C. have adopted the NAIC model bulletin on insurers' use of AI systems (NAIC map, May 2026), and New York's Circular Letter No. 7 (11 July 2024) covers AI and external data in underwriting and pricing. A new evidence source enters a governed process: the record, the carrier's threshold and the carrier's decision are the defensible parts. Buyer context only.

## What earlier campaigns teach this one

- **Nick's baseline:** `2026-08-07-us-digital-fitness`, 245 invites sent to 248 contacts, 15.9% accepted, 2.4% replies per invite (`metrics-final.json`). The six later `nick` campaigns (`2026-09-29` to `2026-10-22`) sent 405 invites, with 94 accepted (about 23%) and 7 replies (about 1.7% per invite), per the Closely stats snapshot of 2026-10-28; two of them are still sending (`2026-10-16-us-employer-obesity-care`, 130 invites to 358 contacts; `2026-10-22-us-mens-health-weight`, 30 to 73). Acceptance was Nick's loss point on `2026-08-07`; in the later campaigns most of the loss came after acceptance (7 replies on 94 accepted).
- **The UK twin has no replies pulled yet** (176 rows imported on 2026-10-26; 11 invites sent and none accepted in the 2026-10-28 snapshot); Open question 9.
- **Insurers route** (`2026-08-14-au-digital-fitness`: at AIA Australia a life product and pricing lead named a colleague). Pricing and product leads stay in the pull.
- **Say what the record is, in plain words** (a UK reply asked if it was a BMI-from-a-photo app). Message 1 asks, Message 2 offers the call, every lane.
- **Easy outs need a target** (`2026-10-16`: "I don't manage our app" with no name). Referral Message 2 points to a named function.

## Target buyer persona

**Who buys:** the owner of the accelerated program's evidence rules and the build rating: Chief Underwriting Officer, head of underwriting, VP or AVP of underwriting, underwriting innovation, strategy and research leads; the carrier medical director who decides what an estimate may be used for; the term, life or DI product and new-business owners who place the step in the e-application; at reinsurers, the US individual life underwriting, R&D, client-solutions and automated-underwriting heads; at digital-first companies, founders and heads of product and underwriting; at platforms, product and partnerships leads.

- **Why these titles, not others:** CUOs and underwriting research teams own random holdouts, post-issue audit design and build rules; medical directors sign off on non-measured inputs; new-business and product heads own the e-application and agent experience. CRO, CIO and distribution heads are group-wide or agent-facing. From the other §3 titles, innovation, digital transformation and insurtech leads are pulled (P2 `proposition` with visible life, DI or underwriting scope, else P3 `referral`); Population Health Director (a health-plan role) and compliance or fraud-prevention teams are not (they do not own a case's evidence, and fraud framing is banned in copy). A bare "Product Manager" at a multi-line carrier returns annuity, retirement and group owners; product heads come through life, term, DI and new-business lines.
- **What they care about (KPIs):** share of applications on the accelerated path; straight-through rate; time to decision; evidence cost per case (paramedical exam, fluids, APS); placement and not-taken rates; the share of holdout and post-issue cases that land in a different class, and on build in particular; agent experience; consistent, documented decisions; contestable-period claims (never in copy).
- **Objections they will likely raise, with the honest answer:**
  - An estimate is not a weighing, and the typical gap is inside your error. True: Smart Scales is a software estimate at about 3.5% mean absolute error under evaluated conditions. The flag refers only gaps well beyond that, on the carrier's threshold; the rest stay on the accelerated path.
  - How many cases would that catch? Unknown until a shadow evaluation on the carrier's own applicants counts flags per threshold and agreement with holdout or exam build.
  - We already have holdouts and EHR audits. They sample after or beside the decision; the scan adds a record on every case where the carrier switches it on, before the decision. The evaluation compares the two.
  - We would never rate on photos. FitXpress does not make underwriting decisions; the carrier's rules and underwriters do.
  - Agents will hate another step. Under 45 seconds from the photos to structured results; the carrier decides where it is offered; the evaluation measures completion and retakes.
  - Is it fair, and is it AI we have to govern? Validation covered ages 16 to 78, heights 150 to 220 cm, weights 38 to 210 kg, US and European participants; performance for people with physical disabilities is not established, and anyone who does not scan keeps the current route. FitXpress returns an estimate and a flag; how the carrier classifies and governs the input is its own assessment.
  - Where is the data, and HIPAA? AWS, primarily US-West-2, partly US-East-1; photo handling as in `compliance.md`; HIPAA answer from `compliance.md` §10 only if asked; documents through legal@3dlook.me.
  - Which carriers use it? None yet. The same capture, processing and integration run in production in remote BMI-verification and weight-management workflows; 3DLOOK has worked with 100+ clients.
  - Does it check height? No. Height comes from the application.
- **Tiers (order only; one import file):** P1 Chief Underwriting Officer, Chief Underwriter, Head of Underwriting, SVP or VP Underwriting, Chief or lead Medical Director at a carrier; head of individual life or DI new business; at a reinsurer the US individual life underwriting head, head of underwriting R&D or automated underwriting; founder, CEO, CPO or head of underwriting at group B; CPO or head of underwriting product at group D. P2 AVP and director of underwriting, underwriting innovation, strategy, research, rules, philosophy and analytics leads; accelerated or automated underwriting leads; medical directors; term, life and DI product heads; new-business heads; life pricing heads (`proposition`); client underwriting and underwriting solutions leads at reinsurers; innovation, digital or insurtech leads with visible life, DI or underwriting scope. P3 underwriting managers, CTOs, CISOs, chief privacy officers, heads of product without visible life scope, group-wide innovation leads. P4 referral.
- **Lanes by title:** `underwriting` (underwriting leadership, innovation, strategy, research, rules, philosophy, analytics, accelerated and automated underwriting, underwriting managers); `medical` (CMOs and medical directors, at group C too); `proposition` (life, term, DI and new-business product heads, pricing, innovation, digital or insurtech leads with life scope, and group B founders and product heads); `reinsurance` (everyone else at group C except CTOs and privacy owners); `partnership` (group D except CTOs and privacy owners); `technical-integration` (CTOs, architects, CISOs, chief privacy officers, new-business technology owners); `referral` (anyone Vadim adds at step 4 from outside these functions, and group-wide innovation or transformation leads at a carrier).
- **Location rule (step 4 applies it):** every person must be located in the United States. UK-located people FAIL whatever the title says (katerina contacted the London teams from 2026-10-26); EU-located people FAIL (olena's file); Canada-located people at John Hancock, Foresters, RGA or Munich Re FAIL (outside the cut, count reported).
- **Not the buyer (FAIL, or a skipped pool at step 4):** individual underwriters, senior underwriters and case managers unless the title says innovation, strategy, research, rules, philosophy, automation or lead; claims heads (Open question 7); agent-facing sales, brokerage, BGA and wholesaler roles; anyone at a multi-line carrier outside individual life or DI (annuities, retirement, group benefits, dental, Medicare supplement, P&C, asset management); P&C staff at reinsurers.

### Target buyer persona: Sales Navigator pull for step 3

**Pull by title filter inside the approved company list, never by company alone.** Add the geography filter "United States" manually to the search (`sales-nav-query` writes none); the reinsurers, John Hancock, Foresters and iPipeline have global pages. Lines match inside longer titles (`Underwriting Innovation` finds Head of Underwriting Innovation; `President, Individual Life` finds Senior Vice President, Individual Life; `AVP Disability Income` finds AVP, Disability Income Underwriting). **Business-line lines are head-level only.** New business, individual life, life underwriting, term life, individual disability, life product and life pricing appear only after Head of, VP, SVP, AVP, President or Director: the bare phrases return the individual underwriters, case managers, new-business specialists and wholesalers that the Not the buyer rule FAILs. **Line-of-business and function exclusions for the whole search.** Almost every group A carrier also writes annuity, retirement, group or wealth business, and the Swiss Re, Gen Re, SCOR, Munich Re and Hannover Re pages carry US property and casualty underwriting staffs that match every underwriting line, CUO included. Add to the generated `NOT (...)` list: `Annuity`, `Annuities`, `Retirement`, `Group`, `Worksite`, `Workplace`, `Voluntary`, `Dental`, `Medicare`, `Investment`, `Wealth`, `Asset`, `Property`, `Casualty`, `P&C`, `Personal Lines`, `Commercial Lines`, `Specialty`, `Marine`, `Cyber`, `Surety`, `Mortgage`, `Liability`, `Claims`, `Distribution`, `Sales`, `Wholesaler`, `Brokerage`, `Business Development`, `Marketing`, `Compliance`. Delete `Assistant` from the generated list for this search: it drops every spelled-out Assistant Vice President, and the `AVP` lines catch only the abbreviation. `Group` also drops anyone who types a company name such as Principal Financial Group into the title; accepted. Still coming through, for step 4 to judge by business line and role: a reinsurer P&C leader whose title names no line (Chief Underwriting Officer, Reinsurance), and analysts under the function lines (`Underwriting Analytics`, `Underwriting Rules`, `Digital Transformation`, `Insurtech`). Group D leaders and group B founders are added by name at step 3; a CEO line would pull every carrier's executives. **Length:** the title Boolean is about 1,800 characters and the exclusions about 600. If Sales Navigator rejects it, run the same company list twice (the lines down to `Medical Director`, then the rest) and save both exports in `sales-nav-raw/`, where `extract-people` keeps one row per person. **Volume (estimate, not measured):** the UK Apollo title pulls gave 46 to 49 rows at Aviva and Zurich UK and 13 to 15 at the largest London reinsurer branches, about 40% PASS (EU twin). US home offices are larger, and the director, manager and medical-director layers repeat across regions and product lines. Expect 50 to 120 rows at each of Prudential, New York Life, Northwestern Mutual, MassMutual, Lincoln and Guardian; 15 to 50 at each other group A carrier; 15 to 40 at each reinsurer US entity with the exclusions (RGA, a life and health reinsurer headquartered in Missouri, up to about 80; Swiss Re, Gen Re and SCOR about double without them); under 15 at each group B and D company. In all about 700 to 1,900 rows, about 280 to 760 PASS at the UK rate before the cap. A company over 80 rows is re-run alone without `Underwriting Manager`, then without the function lines above, before step 4.

```titles
Chief Underwriting Officer
Chief Underwriter
Head of Underwriting
VP Underwriting
SVP Underwriting
Vice President of Underwriting
Vice President, Underwriting
AVP Underwriting
Underwriting Director
Director of Underwriting
Director, Underwriting
Head of Life Underwriting
VP Life Underwriting
President, Life Underwriting
AVP Life Underwriting
Director, Life Underwriting
Underwriting Innovation
Underwriting Strategy
Underwriting Research
Underwriting Rules
Underwriting Philosophy
Underwriting Analytics
Accelerated Underwriting
Automated Underwriting
Algorithmic Underwriting
Underwriting Solutions
Client Underwriting
Underwriting Manager
Chief Medical Officer
Medical Director
Head of New Business
VP New Business
President, New Business
AVP New Business
Director, New Business
Director of New Business
Head of Individual Life
President, Individual Life
VP Individual Life
SVP Individual Life
AVP Individual Life
Director, Individual Life
Head of Term Life
VP Term Life
Director, Term Life
Head of Individual Disability
Head of Disability Income
President, Individual Disability
VP Individual Disability
VP Disability Income
AVP Disability Income
Director, Disability Income
Director, Individual Disability
Head of Life Product
VP Life Product
Director, Life Product
Head of Product
Chief Product Officer
Head of Life Pricing
VP Life Pricing
Director, Life Pricing
Head of Innovation
Digital Transformation
Insurtech
Chief Technology Officer
Chief Information Security Officer
Chief Privacy Officer
```

**`cap_per_group: 50`** (default for every campaign; only Vadim changes it). If a carrier comes back over 50 after the filters, the validator ranks by tier and Vadim decides.

## Message angle: lanes, account facts and the content asset

Every person gets exactly one lane, spelled as below. Numbers come only from Rules. Lane notes are instructions to the writer; none of their sentences goes into a message.

**The angle, for every lane (a target; each writer finds new words for each person):** the company's accelerated or fluidless cases, where no paramedical exam measures build and height and weight are what the applicant types. Each message says in its own words what the scan record would add to those cases, and that the carrier's threshold, rules and underwriters decide. No stock label for the scan or the record repeats across people at one company. What comes back is listed once, in Rules (What the scan is). For reinsurers, the same evidence as a candidate for a client evaluation and for the build section of the engine or manual the team supports. For platforms, the same evidence as a step their e-application or workbench could offer carriers through one integration. For group B, the same evidence inside a journey that is already instant.

**Lanes:**
- **`underwriting`** Target: how build is handled on accelerated cases today and which gaps would change a risk class. The flag is a referral trigger for gaps large enough to cross the carrier's own build chart line or preferred-class boundary, set above the estimate's error; never suggest it settles small differences or corrects each applicant's weight. Question targets: how the team checks build today on accelerated files; at which build-chart edges a gap between declared and estimated weight would change the class; how the program's random holdouts or post-issue reviews treat build (never asking for results or rates); what the team needs to see in a shadow evaluation before any output reaches a case; how build is treated on DI against life. Message 2 value: the evaluation path, which counts flags per candidate threshold and agreement with independently collected build evidence.
- **`medical`** Target: what an estimated value may and may not be used for. Its defensible use is a referral threshold set well above the estimate's error, on gaps that would change the class. Question targets: what a medical director would need to know about a software weight estimate before it enters accelerated rules; how far above the estimate's error a threshold would have to sit; how the carrier's build guidance treats a declared weight against an exam weight. Message 2 value: the estimate's stated error under evaluated conditions, that it is not a scale reading, that the carrier sets the threshold, and the decision boundary.
- **`proposition`** Target: where the step sits in the journey. Question targets: where a two-photo step could sit (agent-assisted e-application, the applicant's own section after the agent hands off, the direct online journey, the DI application); how a new step is tested with agents and BGAs; how drop-off and placement are measured. Pricing heads: how build credits and evidence cost are weighed. Group B: how a step is tested inside an instant-decision flow. Message 2 value: under 45 seconds from the photos, results to the carrier's systems only, completion measured in the evaluation.
- **`reinsurance`** Target: evaluating new evidence with client carriers. Question targets: how the US team tests a new remote evidence source with a client's accelerated program; whether any client has asked about remote build evidence; how a build flag would sit in the engine or manual the team supports (its own product named only to its own team: AURA to RGA, Magnum to Swiss Re, Velogica to SCOR, alitheia to Munich Re). Message 2 value: a shadow evaluation design the team could run with one client. Never mention another reinsurer, any client of theirs, any pilot, their published research or the group's UK or European teams.
- **`partnership`** Target: one integration several carriers could switch on. Question targets: how a new evidence step is added to the platform's e-application or decision workbench; what carrier clients ask the platform for on accelerated cases. Message 2 value: API and web and mobile SDKs, one timestamped record per applicant returned to the platform. Its own product (iGO, The Policy Processor, Bestow's platform) only in its own copy.
- **`technical-integration`** Target: vendor review and integration, technical tone. Question targets: how a new data vendor is reviewed for the new-business journey; how an SDK step enters the e-application; how a structured record reaches the underwriting workbench or case-management system. Message 2 value: REST API and SDKs, the decision boundary line, and data handling in `compliance.md` forms (TLS in transit and S3-managed encryption at rest; photos deleted after processing or within 30 days per the carrier's policy, retained photos blurred, faces obscured at capture; scan records on random identifiers); documents through legal@3dlook.me.
- **`referral`** Message 1: what the record is and why it matters to this company's accelerated cases, then one question about the person's own work. Message 2: a value line that continues their question, the call offer with the calendar link, and an easy out that points to whoever owns underwriting rules or the new-business journey there, worded fresh for each person.

**Question bank discipline (big pools).** Each person gets one question nobody else at the company gets, built from their title. One topic serves at most about a fifth of a company's people. Wording, hook, structure, easy-out target and closer never repeat at one company.

### Account facts (filled after step 2)

Not written yet. After step 2 a fresh `hypothesis-generator` round writes one bullet per IN group from `companies.md`, in the UK format: one to three dated facts with URLs, then `Use:` and `Never:`. Until then a writer uses no company fact beyond the person's title and the company's line of business, and treats these as standing Never items for every account (names that are not accounts are also in `banned_terms`):
- ownership, deals and group links in either direction: Manulife and John Hancock, Dai-ichi and Protective, Sumitomo and Symetra, Meiji Yasuda and The Standard, Nippon Life and Corebridge, Bain Capital and Lincoln, Roper and iPipeline, Sammons and Bestow's former carrier, Corebridge's former parent, Ethos's issuing carriers (its FAQ names Banner Life, Ameritas and TruStage);
- the UK and European sister companies and their teams, and any former 3DLOOK prospect contact there;
- face, selfie or video BMI work at any company (Gen Re's 2019 selfie prototype, Hannover Re's video study, the 2017 SelfieQuote at Banner Life), named or not;
- a reinsurer's published research quoted to anyone (the Gen Re survey, the Munich Re studies), including to its own team;
- a company's figures (premiums, sales, accelerated share, limits), its vacancies, and any claims, contestable-period, court or regulatory matter.

### Content asset in Message 2

At most one 3DLOOK link next to the calendar link: the landing https://3dlook.ai/for-insurance-underwriting/ in any lane, or in `technical-integration` the privacy FAQ https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/ instead. Not linked: `/fitxpress/for-insurance-underwriting/` (404 until `/fitxpress/` ships). The hub article `/content-hub/mobile-body-scanning-insurance-underwriting/` is US-worded but frames "fraud-prevention support" (landing link text), which Rules ban; not linked.

## Rules for steps 3-5

- **Sender and format:** Nick, American English, `Nick` alone on the last line, first names only. Connection request with no note. Message 1 ≤ 600 characters, Message 2 ≤ 550. Register: peer to a senior underwriter or medical director, plain, specific, no enthusiasm words.
- **Message 1:** context about this company and one question; no call ask, no link of any kind. **Message 2:** a call offer and https://meetings.hubspot.com/nick-omelchak as plain text, in every lane, referral included. No call length or minutes in any message.
- **Landing URL (Vadim's UK decision 2026-10-22, carried over).** Message 2 may carry https://3dlook.ai/for-insurance-underwriting/ as plain text, on its own, with no punctuation glued to it; the calendar link stays required. Optional per person: at one company no more than about half of the Message 2s carry it, and the sentence around it differs each time. Never in Message 1.
- **Lanes are exactly** `underwriting`, `medical`, `proposition`, `reinsurance`, `partnership`, `technical-integration`, `referral`.
- **US idiom.** Write carrier or insurer, e-application, accelerated or fluidless underwriting, paramedical exam, fluids, APS, risk class, build chart, preferred and standard classes, agent or advisor, new business. Face amount and case size only without figures. UK and EU terms (GP report, nurse screening, non-medical limits as a UK phrase, adviser, protection) are not used.
- **What the scan is (a target; the writer picks the words).** Message 1 makes clear what comes back and who decides. The parts: two photos taken in the e-application, a Smart Scales weight estimate, BMI calculated from the height the applicant declared, a flag when the gap crosses the threshold the carrier sets, and one timestamped structured record returned to the carrier's systems. Every Message 1 carries the photos and the threshold flag; which other parts appear, in what order and in what words, varies between people at one company. A single label such as a BMI-from-a-photo app is never enough.
- **What it is not.** It does not make or recommend underwriting decisions, assign risk classes, rate, price, approve or decline. It does not check height. It does not replace a paramedical exam, fluids, an APS, electronic health records or any evidence the carrier's guidelines require; it adds evidence to cases that get none of these. It is never described as hidden, covert or mandatory for applicants: the carrier decides where it is offered and keeps its current route for anyone who cannot or does not scan.
- **Applicants are never suspects.** No message says or implies that applicants or agents lie, hide or misstate anything. Talk about declared build and what the record adds. No claims, contestable-period reviews, rescissions, courts, complaints or regulators, for any company. Holdouts and post-issue reviews may be named as the carrier's own program monitoring, never with a result, rate or outcome.
- **Lead with the record,** which is what the ICP calls defensibility: timestamped, structured, on the case file, the carrier's threshold, the carrier's rules. No accuracy percentage opens a message or appears in Message 1.
- **Numbers only from this list:** two photos (front and side), with "2 photos" as the numeric form; "under 45 seconds from the photos to structured results" (the only speed wording, as its own plain sentence and only where speed is the point); 80+ body measurements as an output, and a 3D model "when enabled for the deployment" (both secondary, never the lead); Smart Scales "approximately 3.5% mean absolute error under evaluated conditions", always with "not a scale reading" in the same sentence, Message 2 only, in `underwriting`, `medical` and `reinsurance` only; "3DLOOK has worked with 100+ clients"; "112,100 scans in 2025 across all 3DLOOK customers" as its own sentence, never tied to the US, insurance, a product flow or a client. No 96-97% or other measurement-accuracy figure, no repeatability figure, no validation-population figure in cold copy (replies use `accuracy-formulations.md`). No integration-time figure in any message. No market, survey, obesity, audit, claims or prospect figures, and none of the landing's statistics (59%, "#1", "9 vs 27 days").
- **Smart Scales** is named without a "(beta)" label. It is a software estimate; never "weighs", never "measures weight". Never suggest the flag settles small weight differences or corrects each applicant's declared weight: it refers gaps above a threshold the carrier sets.
- **Proof without names.** No 3DLOOK client is named. The production line comes from the landing: "production infrastructure already deployed in remote BMI-verification and weight-management workflows". That quoted line is the only place the word verification may appear; verify, verified and verifies stay banned. Never imply a carrier, reinsurer or platform uses FitXpress.
- **Compliance line: exactly one per pair, in Message 2, never in Message 1, every lane, verbatim:** "FitXpress is not a medical device and does not make underwriting decisions." (the landing's sentence; it opens with the `compliance.md` short form and counts as the compliance line). No HIPAA, BAA, FDA, CCPA, SOC 2 or GDPR wording in cold copy: life and DI underwriting is outside HIPAA's covered-entity definitions, so the US line's BAA clause does not fit these readers (Open question 4). `technical-integration` adds data-handling sentences (next rule); they are not a second compliance line. Replies use `compliance.md` §10 and legal@3dlook.me. Never "compliant", "certified" or a medical-device claim beyond the line above.
- **Data handling sentences.** Only the forms in `compliance.md`: TLS in transit, S3-managed encryption at rest; photos deleted after processing or within 30 days per the carrier's policy, retained photos blurred, faces obscured at capture; scan records on random identifiers; outputs stored until deleted by scan identifier on the customer's request. Never "not stored", "no personal data" or "anonymous".
- **Several people at one company.** Name the company in every Message 1. Never mention colleagues, other teams, a sister company or a conversation that did not happen. No two people at one company share an opener, a central question, an easy-out target, a Message 2 opener or a closer.
- **Never name one prospect in another prospect's copy,** including a reinsurer in a carrier's message, a carrier in a reinsurer's or platform's message, a platform in a carrier's message, an issuing carrier in Ethos's message, and any vendor a carrier uses. A company's own product may be named in its own copy only. The rule covers message text; the linked landing citing public research by Gen Re and Munich Re is not a message naming a prospect.
- **Former employers** may be named (standing decision) unless they are an account in this campaign or in either twin, a competitor or a banned term.
- **Word traps.** Never "objective" about our data; no em or en dash; no "plus" as a connector; no "so" introducing a benefit; no corrective "X, not Y"; none of the buzzwords on the hard-bans card.
- **No pricing and no trial terms** anywhere; a price or pilot-terms question goes to the call.
- **Writer notes and card instructions are not copy.** Lane notes, targets and rule sentences are never pasted; the quoted lines above are the only verbatim copy.
- **Message 1 gate.** Every message 1 carries at least one product specific from `proof-points.md` and one line that could only have been written to that company; each pair of messages cites at least one number. The gate recognises "two photos", "2 photos", "body measurements", "API" and "SDK" as product specifics (not "two guided photos" or "weight estimate" alone), and "under 45", "2 photos", "80+", "3.5%" and "112,100 scans" as numbers. Referral people included.

## Anti-cases (where it does NOT work)

- **Group life, group DI and worksite voluntary benefits** (MetLife's US business, group carriers): members are accepted within guaranteed-issue limits without individual build questions.
- **Guaranteed-issue and final-expense products** with no or few health questions; simplified-issue mass-market writers are reserve only (Globe Life, Primerica).
- **Health plans** (UnitedHealthcare, Humana, Cigna, Aetna, Oscar): they do not rate build at application; a different FitXpress use case.
- **Annuity-only writers and closed blocks** (Athene, Jackson, F&G, consolidators) and **recent deals** within about 12 months (Legal & General America and Meiji Yasuda, February 2026; Brighthouse and Aquarian, pending; Hexure and iCapital, March 2026; `icp-detail.md` universal exclusion).
- **Brokers, BGAs, IMOs and comparison sites** (Policygenius, Quotacy, SelectQuote and the like): they do not underwrite. Group B companies that run their own instant-decision journey are in. Lemonade's life agency, which sells as agent of the carrier that underwrites and issues its policies, is out on the same ground (Open question 10).
- **Exam and evidence vendors** (paramedical networks, lab, Rx, MIB, credit-based and EHR data firms): a later partner conversation.
- **Cases above accelerated limits or with disclosed conditions:** an exam already measures height and weight; FitXpress adds nothing there.
- **Canadian, UK and European entities** of any account (other profiles or outside the cut).
- **Any company whose application already runs a remote body, face or BMI-from-image capture:** held for Vadim.

## Vadim's standing decisions (already applied above)

1. **No headcount floor** (2026-09-29); the segment revenue threshold stays ($5M+ for §3).
2. **`cap_per_group: 50` for every campaign, no waves** (2026-09-29): one closely.io import file.
3. **A lane for every function** at an IN company (2026-09-29), applied inside the individual life or DI business.
4. **FAIL only for the wrong company, people who left, identity collisions and duplicates,** along with this campaign's business-line and location rules; company-named profiles are held for Vadim.
5. **Former employers may be named** (2026-09-29), within the Rules' limit. **Live 3DLOOK pages may be linked as they are** (2026-09-29).
6. **No 3DLOOK client is named;** 112,100 scans as 3DLOOK-wide scale (2026-09-29); "3DLOOK has worked with 100+ clients" (2026-09-30). **Message 1 asks, Message 2 calls** (2026-10-07), every lane (`referral_call: yes`).
7. **Nick:** English, `Nick` alone on the last line, first names only, calendar link in every Message 2.
8. **Twin defaults (Vadim 2026-10-22, 10-26, 10-29):** landing URL in Message 2 only, optional; Smart Scales named, 3.5% only in Message 2 of `underwriting`, `medical`, `reinsurance` with its qualifiers; platforms in `partnership`; claims heads not pulled, pricing P2 `proposition`; a target bought or merged within about 12 months is OUT, older deals never mentioned; single-line insurer CEO or COO as P3 `referral` only where no underwriting owner is found; a Sales Navigator TITLE pull with geography first (the UK company-wide export gave 45 PASS of 1,006), then an Apollo top-up with the credit count named before `enrich` if it exceeds 100; reinsurer rows as country or US entities, bare parents never registered.

## Vadim's decisions 2026-10-29

Vadim approved the hypothesis after the QC fix round (QC 17/20, report `workspace/_quality/outbound/2026-10-29-hypothesis-generator-us-insurance-underwriting.md`) with «ок» to the twelve open questions as sent: every default taken.

1. **Approved:** `status: approved`, research may start. The cut is 22 carriers, 3 digital-first companies, 6 reinsurer US entities and 3 platforms; the reserve list (Equitable, Western & Southern, OneAmerica, Assurity, Illinois Mutual, Globe Life, Primerica) only on his word.
2. **Reinsurer US entities from `nick`:** `RGA US`, `Gen Re US`, `Munich Re Life US`, `Hannover Life Re America`, `SCOR Life Americas`, `Swiss Re Americas`, US-located people only; bare parents stay unregistered.
3. **Recent deals OUT and never mentioned:** Legal & General America, Brighthouse, Hexure. Older ownership links never mentioned.
4. **Compliance line:** the landing's decision-boundary sentence, once per pair, in Message 2, every lane; HIPAA, BAA and FDA stay in `banned_terms` and appear only in replies.
5. **Digital-first group B IN** (Ethos, Ladder Life, TruStage); Ethos's issuing carriers never named to it.
6. **Individual DI in the pull,** The Standard as a row.
7. **Claims heads not pulled;** pricing heads P2 `proposition`.
8. **Smart Scales and the 3.5% figure** as in the twins; the 6% honesty note stays out of copy.
9. **Run now;** a clear objection in the UK read-out before step 5 adjusts these Rules first.
10. **Lemonade OUT.**
11. **Canada-located people FAIL,** count reported at step 4.
12. **People source:** Sales Navigator title pull with the United States geography filter and the line-of-business exclusions on the whole search first, then an Apollo top-up with the credit count named before `enrich` if it exceeds 100.

## Validation criteria (Step 2 will check)

- **Companies.** 34 named candidates; target 26-30 IN. Fewer than 22: stop and report to Vadim; never widen on your own (reserve list, simplified issue, brokers, evidence vendors, health plans) or add companies to reach a number. Each carrier writes new individually underwritten life or DI business with an accelerated, fluidless or no-exam path in 2026 (agent or producer guide, underwriting guide, product page or 2026 trade press); each reinsurer row is the group's US L&H entity; each platform is used by US carriers for e-application or new-business underwriting.
- **Schema.** `hq_country` United States (Foresters: Canada head office, US row, US people only). `icp_fit` high or medium only. Row names follow the EU twin's three rules, checked on 2026-10-29 against every registry:
  1. **US entity or suffix, never a bracketed place:** `RGA US`, `Gen Re US`, `Munich Re Life US`, `Hannover Life Re America`, `SCOR Life Americas`, `Swiss Re Americas`, `iPipeline US`, `Foresters Financial US`. `record` registers the name without its bracket (`swiss-re-americas`); the bare parents stay unregistered.
  2. **Parent alias in brackets** only where exports show the bare parent and the slug has 4+ letters: `(Swiss Re)`, `(Munich Re)`, `(Hannover Re)`, `(SCOR)`, `(Gen Re)`, `(iPipeline)`, `(Reinsurance Group of America)`, `(Guardian)`, `(Foresters Financial)`. `RGA` (3 letters) is dropped by the parser: Sales Navigator rows reading RGA and US-located are relabelled `RGA US` before `extract-people` (Coordinator notes). Anyone an alias pulls in from outside the US FAILs by location.
  3. **No two rows share a bracket text.**
  **Collisions to watch:** `Ladder Life` against nick's own `ladder` (the fitness app): a Sales Navigator row reading bare `Ladder` is kept only if the profile shows Ladder Life (insurance), relabelled `Ladder Life` before `extract-people`, else FAIL; never register bare `ladder`. `Pacific Life` against katerina's `pacific-life-re`: any person whose company reads Pacific Life Re FAILs. `Guardian Life (Guardian)` against katerina's `guardian-financial-services`: no slug match; the UK Guardian's staff FAIL by location.
- **Registry.** `outbound-registry.py check --profile nick` after extract; expected hits: none (no waiver needed). Then compare every person URL with `katerina-registry.json`, `olena-registry.json` and the UK `people-approved.csv`; any match is FAIL (the RGA global underwriting philosophy people Emma Jones and Rebecca Abayakoon in London are katerina's).
- **Account facts and displacement.** For every IN company: one to three dated underwriting or new-business facts with URLs, and a search of its site, producer portal and trade press for any remote body scan, face or video BMI estimate or selfie quote. Known and historic: Banner Life's 2017 SelfieQuote (OUT anyway), Gen Re's 2019 selfie prototype, Hannover Re's video study (not US). Default IN for Gen Re US and Hannover Life Re America, names banned, held if anything newer in the US appears. No 2025-2026 US carrier pilot found on 2026-10-29.
- **People.** Location and business-line rules as in Target buyer persona. `apollo-pull.py search` has **no location filter**: every Apollo row is location-filtered at step 4; credit count to Vadim before `enrich` if over 100.
- **C-level availability.** US CUOs, VPs of underwriting and medical directors are well represented on LinkedIn; reinsurer US underwriting R&D heads and platform product leads are expected in Sales Navigator.
- **Proof in product-info.** Use-case file and live landing: yes (US-worded). Insurance reference customer: none (proof as Rules allow).
- **Message 1 gate.** As in Rules: every message 1 carries at least one product specific from `proof-points.md` and one line that could only have been written to that company; each pair cites at least one number. Zero client names, banned terms, links in Message 1, accuracy figures in Message 1, suspicion framing or decision claims; exactly one compliance line per pair, in Message 2. The gate fails any pair that misses one of these; `2026-07-21` sent its first messages with no specific and drew 4 replies on 73 accepted.

## Success metrics for this campaign

Denominators are Closely's invite and acceptance counters (`metrics-final.json` for `2026-08-07`, the 2026-10-28 stats snapshot for the later campaigns), never import rows. Senior US underwriters and medical directors are a colder list than Nick's health programs; targets sit at or below his baseline.

| Metric | Target | Floor | Basis |
|---|---|---|---|
| Invites sent | 250-400 | 150 | about 28 IN companies; US carriers are larger than UK or EU ones |
| Connection acceptance | 18% | 12% | `nick` `2026-08-07` 15.9%; six later `nick` campaigns about 23% |
| Replies per invite | 2% | 1% | `2026-08-07` 2.4%; six later `nick` campaigns about 1.7% (7 on 405 invites) |
| Positive replies (interest or a question) from P1-P2 | 2 | 1 | |
| Companies with at least one reply | 4 of about 28 IN | 2 | |
| Discovery calls | 2, at different companies | 1 within 8 weeks | |
| Shadow-evaluation conversations (carrier, reinsurer or platform) | 1 | 0 | the landing's pilot step |

**Falsified if** three or more P1 or P2 replies say build is not a material gap on accelerated cases, that an estimated weight cannot enter accelerated rules at any threshold, that existing holdouts, EHR or data scores already settle build, or that photos cannot be collected in a US life e-application. **Inconclusive** if fewer than 25 people accept. Results are read by group (carriers, digital-first, reinsurers, platforms).

## Risks

1. **No insurer reference.** Underwriters may want a named carrier before a call; the offer is an evaluation.
2. **Competing evidence.** Carriers already buy Rx, MIB, credit-based mortality scores and EHRs for accelerated cases, and Munich Re models BMI understatement from application and geographic data; a reader may see build as solved by data. The scan is direct build evidence on the case, and the evaluation compares it with what they have.
3. **The flag works on large gaps, and nobody knows yet how many there are** (What the flag can separate). Munich Re's 6% material-gap line is under twice the estimate's mean error, and the error spread is unpublished; a 6% threshold may flag accurately declared applicants, and a threshold well above it catches fewer cases. The landing's sample payload flags a +3.3% gap, inside the error, and an underwriter may read it as the intended use. If a shadow evaluation finds few flags above the error at build-chart edges, the value case is thin.
4. **AI governance and fairness.** About 25 states apply the NAIC AI bulletin, New York applies Circular Letter No. 7 to AI and external data in underwriting, and Colorado regulates life insurers' use of external data and models; a new image-based input may be read as added governance work and tested for unfair discrimination. Classifying the input is the carrier's assessment; FitXpress decides nothing.
5. **Agent friction.** Most US life applications are agent-assisted; a photo step may be seen as slowing the sale. The step's place and completion are evaluation criteria.
6. **Landing numbers.** The live landing (2026-10-29) credits its "9 vs 27 days" line to LIMRA's automated and accelerated underwriting study and links to a 2020 LIMRA article; its "#1" and 59% lines quote Munich Re and Gen Re, both prospects here. None goes into copy, and a reader who opens the page will see them, the age of the 2020 source included.
7. **Acceptance.** `nick` accepted 15.9% on `2026-08-07` and about 23% across the six later campaigns; senior underwriters may accept less.
8. **Overlap with the twins.** The same reinsurer groups hear from katerina (London) and olena (EU head offices) within weeks; copy never refers to it.

## Open questions for Vadim

1. **The cut: 22 carriers, 3 digital-first companies, 6 reinsurer US entities, 3 platforms.** Default: yes. Reserve (Equitable, Western & Southern, OneAmerica, Assurity, Illinois Mutual, Globe Life, Primerica) only on your word.
2. **Reinsurer US entities from `nick`.** Default: all six IN as US rows (`RGA US`, `Gen Re US`, `Munich Re Life US`, `Hannover Life Re America`, `SCOR Life Americas`, `Swiss Re Americas`), US-located people only; bare parents stay unregistered.
3. **Recent deals.** Default: Legal & General America (Meiji Yasuda, completed 2 February 2026), Brighthouse (Aquarian, pending) and Hexure (iCapital, 17 March 2026) OUT, never mentioned. Older ownership (Corebridge and Nippon Life, Lincoln and Bain Capital, Ladder, Bestow and Sammons) never mentioned.
4. **Compliance line.** Life and DI underwriting is outside HIPAA's covered-entity definitions (45 CFR 160.103; disability income is an excepted benefit), so `compliance.md`'s US line ("We support HIPAA-governed deployments under a BAA, encrypt data in transit and at rest, and delete photos after processing or within 30 days.") reads off-target to a CUO. Default: the landing's decision boundary line as the one compliance line in every lane; `technical-integration` adds `compliance.md` data-handling sentences; HIPAA, BAA and FDA only in replies. Or use the US line verbatim in `technical-integration` (then `HIPAA` and `BAA` leave `banned_terms`)? (The use-case file's "HIPAA mention essential" note predates this; a note for its owner.)
5. **Digital-first group B** (Ethos, Ladder Life, TruStage). Default: IN, founders and heads of product and underwriting by name, `proposition` or `underwriting`. Ethos's issuing carriers are never named to it.
6. **Individual DI in the pull** (the head-level disability title lines, The Standard as a row). Default: yes.
7. **Claims heads.** Default: not pulled (claims copy would touch contestable-period reviews the Rules ban); pricing heads P2 `proposition`.
8. **Smart Scales and the 3.5% figure** as in the twins. Default: carried over unchanged, with the 6% honesty note kept out of copy.
9. **Timing against the UK twin** (no replies pulled yet). Default: run now; a clear objection in the UK read-out before step 5 adjusts these Rules first.
10. **Lemonade** (an `icp-detail.md` §3 insurtech example). Default: OUT. Its life page (2026-10-29) says its agency acts as agent of Banner Life, which underwrites and issues the policies, and Banner Life's group completed its sale to Meiji Yasuda on 2 February 2026. If you say IN, step 2 checks whether a Lemonade team owns the underwriting rules in its term journey.
11. **Canada-located people** at John Hancock (Manulife, Toronto), Foresters and RGA Canada. Default: FAIL, count reported at step 4.
12. **People source.** Default (twins): Sales Navigator title pull with the United States geography filter and the line-of-business exclusions on the whole search first, then an Apollo top-up with the credit count named before `enrich` if it exceeds 100.

## Coordinator notes (outside every card)

- **Compliance count.** Rules say exactly one compliance line per pair (the boundary sentence), every lane, as in the EU twin. `check-messages` skips the HIPAA line in its near-duplicate check but not this sentence; its repetition across colleagues is mandated and is waived manually.
- **Relabels before `extract-people`:** US-located RGA rows to `RGA US`; bare `Ladder` rows to `Ladder Life` only after a profile check (Schema).
- **`59%` is not in `banned_terms`:** the gate matches `\bterm\b`, which never fires after a `%`; the Rules' number list keeps the landing's 59% out, and the message gate's number check catches it.
- **`Colorado` and `Quest Diagnostics` in `banned_terms`** can trip on a recipient's location or former employer; the coordinator waives a hit that is not a regulatory or vendor mention.

## Sources

All read on 2026-10-29 unless dated.

- Accelerated share: Gen Re 2025 U.S. Individual Life Next Gen Underwriting Survey (2025-12-17) https://www.businesswire.com/news/home/20251217204891/en/Gen-Re-Releases-2025-U.S.-Individual-Life-Next-Gen-Underwriting-Survey-Results · summary https://www.genre.com/content/dam/generalreinsuranceprogram/documents/surveylhilnextgen25-en.pdf
- Monitoring and build: Munich Re, misclassification in AUW (2025-01-16) https://www.munichre.com/us-life/en/insights/future-of-risk/misclassification-driving-mortality-slippage-in-auw.html · Munich Re, BMI understatement and the 6% flag (2020-07-21) https://www.munichre.com/us-life/en/insights/clinical-knowledge/predictive-analytics-mortality-impacts-bmi-misrepresentation.html
- Sales: LIMRA 2025 individual life (2026) https://www.limra.com/en/newsroom/news-releases/2026/limra-u.s.-individual-life-insurance-new-premium-tops-$17.5-billion-to-set-new-sales-record-in-2025/
- Limits: Foresters US release (2026-04-28; US AUW to $2 million for ages 18 to 60 from 2026-04-26, pre-screen checklist on iPipeline iGO) https://www.foresters.com/en/about-us/newsroom/news-releases/foresters-financial-revamps-accelerated-underwriting-program · Ethos (Nasdaq LIFE, up to $3 million, issuing carriers) https://www.ethos.com/ · https://research.contrary.com/report/ethos · https://www.spglobal.com/market-intelligence/en/news-insights/articles/2026/2/ethos-plans-to-expand-carrier-partners-explore-more-complex-products-post-ipo-97930932 · Ethos issuing carriers (agent FAQ) https://ethos.com/agents/faq/what-carriers-does-ethos-work-with · Lemonade life (legal note: its agency acts as agent of Banner Life, which underwrites and issues) https://www.lemonade.com/life
- Self-report and obesity: Flegal et al., Obesity 2019 https://stacks.cdc.gov/view/cdc/89163 · USDA ERS (NHANES BMI 29.23 measured vs 28.49 self-reported) https://www.ers.usda.gov/amber-waves/2023/november/researchers-adjust-self-reported-estimates-of-obesity-in-scanner-data · Hattori and Sturm (RAND) https://www.rand.org/pubs/external_publications/EP51462.html · CDC NCHS Data Brief 508 https://www.cdc.gov/nchs/products/databriefs/db508.htm
- HIPAA scope: 45 CFR 160.103 "health plan" https://www.law.cornell.edu/cfr/text/45/160.103 · 42 U.S.C. 300gg-91(c)(1) excepted benefits https://www.law.cornell.edu/uscode/text/42/300gg-91 (hhs.gov FAQ 364 blocks the VPS)
- Regulation: NAIC AI bulletin map (status 2026-05-01) https://content.naic.org/sites/default/files/legal-adoption-map-ai-model-bulletin.pdf · NY DFS Circular Letter No. 7 (2024-07-11) https://www.dfs.ny.gov/industry-guidance/circular-letters/cl2024-07
- Deals: L&G America to Meiji Yasuda completed https://group.legalandgeneral.com/en/newsroom/press-releases/l-g-completes-transaction-with-meiji-yasuda · Brighthouse and Aquarian, Q2 2026 10-Q https://www.sec.gov/Archives/edgar/data/0001685040/000168504026000028/bhf-20260630.htm · Hexure and iCapital, definitive agreement (iCapital release, 2026-03-17) https://icapital.com/newsroom/press-releases/icapital-acquires-hexure-to-create-the-industrys-first-end-to-end-annuity-and-insurance-technology-platform/
- Platforms: Zinnia TPP 8.0, its life and annuity underwriting platform (Zinnia release, 2025-11-04) https://zinnia.com/news/zinnia-unveils-the-policy-processor-8-0-an-ai-powered-leap-forward-in-la-underwriting · Bestow https://www.bestow.com/carriers · Bestow Series D and carrier sale https://techcrunch.com/2025/05/13/insurtech-bestow-lands-120m-series-d-from-goldman-sachs-smith-point-capital · RGAX AURA NEXT in FireLight (2021) https://www.businesswire.com/news/home/20210818005162/en/ · iPipeline and Roper https://insurancenewsnet.com/press-releases/ipipeline-to-be-acquired-by-roper-technologies
- Displacement: Gen Re selfie prototype (2019) https://www.dig-in.com/news/gen-re-pilots-selfie-based-life-insurance-underwriting · L&G America SelfieQuote (2017) https://coverager.com/power-selfie-legal-general-america-launches-selfiequote-com-engaging-new-way-receive-life-insurance-quote-simply-uploading-selfie/ · Hannover Re video study https://www.hannover-re.com/en/life-and-health/inspire/underwriting-case-studies/ai-video-technology-for-health-and-risk-insights/ · Prism Labs insurance page (no named carrier) https://www.prismlabs.tech/solutions/insurance-population-health
- Live landing re-fetched 2026-10-29 (curl, HTTP 200): the "9 vs 27 days" line credits "LIMRA, automated and accelerated underwriting study" and links to https://www.limra.com/en/newsroom/industry-trends/2020/life-insurers-look-to-make-the-underwriting-process-easier-for-customers/ ; the 59% line credits Gen Re; sample payload +3.3%: https://3dlook.ai/for-insurance-underwriting/
- Internal: both twins' `hypothesis.md`; `2026-08-07-us-digital-fitness` `metrics-final.json`; the Closely stats snapshot `~/.hermes/outbound-stats/2026-10-28.json` (the `nick` account's campaigns since 2026-09-29); `proof-points.md`, `compliance.md`, `tech-spec.md`, `use-cases/fx-insurance-underwriting.md`, `icp-detail.md` §3; landing text of record.
