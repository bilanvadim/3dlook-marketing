---
product: fitxpress
profile: katerina
market: UK
created: 2026-10-22
status: approved
use_case: fx-insurance-underwriting
cap_per_group: 50
banned_terms: [Yazen, UK Meds, Healthyr, Safariland, Burlington, Jim's Formal Wear, Generation Tux, Tailoor, Redthread, Prism, Bodygram, Size Stream, Fit:match, Mirrorsize, Bodd, Nuralogix, Anura, Lapetus, SelfieQuote, selfie, selfies, iGPR, LIMRA, AIG, HIPAA, SOC 2, FDA, MHRA, UKCA, CE mark, FCA, PRA, ABI, Consumer Duty, ombudsman, FOS, CIDRA, compliant, certified, certification, accredited, clinically validated, clinically proven, verify, verified, verifies, guarantee, guaranteed, fraud, fraudulent, misrepresent, misrepresented, misrepresentation, non-disclosure, liar, lying, dishonest, cheat, cheating, carrier, carriers, paramedical, paramed, APS, attending physician, face amount, obese, DEXA, DXA, BIA, bioimpedance, trial, acquisition, acquired, merger, generic figure, never a promise, not a promise, context only, writer note, Circling back, Following up, Saw your post]
---

# Outbound Hypothesis: 2026-10-22, UK protection underwriting (Katerina)

- **Campaign:** `2026-10-22-uk-insurance-underwriting`
- **Owner and sender:** Katerina Galich, CEO, profile `katerina`, market UK. Every message ends with `Katerina` alone on the last line; Message 2 calendar link https://meetings.hubspot.com/katerina-galich.
- **ICP:** `icp-detail.md` §3 (Life & Disability Insurance Underwriting). Its rule holds here: insurers buy defensibility (an audit trail, workflow integration, consistency), not accuracy as such.
- **Use-case file:** `use_case: fx-insurance-underwriting`. The live landing (https://3dlook.ai/for-insurance-underwriting/, HTTP 200 on 2026-10-22; text of record `workspace/pages/for-insurance-underwriting/published-live-2026-10-21.md`, stale on one point: its l.32 source label was corrected on the live page by 2026-10-22) is the newest approved wording and the angle source. A number on the landing is not an approved claim by being there: every figure in Rules traces to `proof-points.md` or to a source checked for this file (Sources).
- **Company list: researched** (step 2 runs `company-researcher`). This hypothesis names the candidate universe and the tests each company must pass; it does not hand over a list.
- **Registry, checked 2026-10-22** (`outbound-registry.py status` and a grep of all six registries): no UK insurer, reinsurer or underwriting platform is registered to any profile. `katerina` has 55 companies, all health, weight-management or fitness. Nearest slugs to watch: `phoenix-health` (katerina, a clinic, not Phoenix Group) and `bupa-australia` (vadim, out of scope here anyway).

> **Read this first.**
> 1. **One idea.** Most UK protection applications are decided at the point of sale with build (height and weight) as the applicant's own declaration. Declared build runs lighter than measured build in England's own survey data, and insurers meet the gap later, at claim, against GP records. FitXpress puts a second source of build evidence inside the application: two photos, a Smart Scales weight estimate, BMI from the declared height, a flag on the insurer's own threshold, and a timestamped record for the case file. The insurer's rules and underwriters decide.
> 2. **The market is small and concentrated.** About 13 major individual protection providers, five of them writing around 80% of new premium. UK insurers alone stop at 18 named candidates, which is why the sub-segment is the UK point-of-sale underwriting chain: the insurers, the London life reinsurers whose manuals and rules engines set build ratings, and the three platforms that host the adviser application. That is 28 companies named in all, with about 25 expected to pass step 2. Group risk, PMI, guaranteed over-50s, annuities and closed books are out (Anti-cases).
> 3. **No insurer is a 3DLOOK customer.** The proof is the landing's own anonymised line (production use in remote BMI-verification and weight-management workflows), "3DLOOK has worked with 100+ clients" and 112,100 scans in 2025 across all 3DLOOK customers. The offer is an evaluation, never a reference.
> 4. **Message 2 may carry the landing URL** (Vadim, 2026-10-22, decisions block below). Message 1 never carries a link.
> 5. **The flag works on large gaps only.** The average gap between declared and measured weight is smaller than the Smart Scales estimate's stated error. The case rests on the gaps big enough to change a build rating (Why this is plausible, Risk 3).

---

## Vertical

UK individual protection underwriting: term life, critical illness and income protection, sold mostly through advisers and decided at the point of sale by rules engines.

## Sub-segment

The companies that decide what evidence a UK protection application collects and how build is rated: 28 named candidates in three groups, about 25 of them expected to pass step 2. No company is added to reach a number. Every row has `hq_country` United Kingdom.

**A. UK insurers writing new underwritten individual protection in 2026 (target 16-19).** Candidates to verify: Aviva, Legal & General, Royal London, Liverpool Victoria (LV=), Zurich UK, VitalityLife, Scottish Widows, Guardian, The Exeter, Cirencester Friendly, Holloway Friendly, British Friendly, Shepherds Friendly, Scottish Friendly, OneFamily (underwriter of Beagle Street), Wesleyan, MetLife UK, National Friendly. The researcher confirms each one is open to new underwritten business in 2026 and drops any that is not.

**B. London life and health teams of the reinsurers that write UK protection (7):** Swiss Re UK, Munich Re UK Life Branch, Hannover Re UK Life Branch, Gen Re UK, RGA UK, SCOR UK, Pacific Life Re (London-headquartered). Group names are written as the UK entity so the registry records `swiss-re-uk`, not the global parent (Open question 1).

**C. Point-of-sale underwriting platforms used by UK protection insurers (3):** UnderwriteMe (Pacific Life Re subsidiary; two products: the Decision Platform for insurers, which runs point-of-sale underwriting rules, and the Protection Platform for advisers, checked on underwriteme.com 2026-10-22), Iress (The Exchange), iPipeline UK (SolutionBuilder, Advanced Underwriting). Partnership lane only.

**Why this cut, not a narrower or wider one:**
- **Narrower is too small.** UK individual protection is concentrated: 13 major providers in Health & Protection's in-force survey, and five firms write around 80% of new premium (FCA market overview, Sept 2025). Canada Life (2022), Aegon (2023) and AIG Life (to Aviva, 2024) left; HSBC Life UK went to Chesnara in February 2026. An insurer-only or income-protection-only list stops near 15.
- **Reinsurers co-own the build decision in the UK.** Underwriting manuals and rules engines come from them: AIG Life's rules engine was built on Swiss Re's Magnum Pure (2023); UnderwriteMe's engine, launched with The Exeter in 2014, is owned by Pacific Life Re. Reinsurers already test remote BMI estimates against nurse data (Hannover Re's 26-week pilot with 1,650 applicants). They are a buyer of the evaluation and a route to several insurers.
- **Platforms host the step where build is keyed.** Iress added height, weight and waist questions to The Exchange; iPipeline's Advanced Underwriting collects the most common disclosures before the application; UnderwriteMe's Protection Platform runs one application for several insurers, and UnderwriteMe launched an AI engine for post-issue misrepresentation audits in March 2026.
- **Wider dilutes the idea.** Group risk accepts most members within free cover limits, PMI underwrites by moratorium, guaranteed over-50s asks no health questions, and enhanced annuities reverse the incentive. None of them uses build evidence the way the landing describes.

**Size:** `icp-detail.md` §3 sets $5M+ revenue. Every candidate clears it on premium income; the smallest friendly societies are the ones to confirm.

## Use case (1 sentence)

A UK protection insurer adds a two-photo step to point-of-sale applications, and FitXpress flags any gap between declared and estimated weight that crosses the insurer's own threshold.

## Why this is plausible (3 reasons grounded in evidence)

1. **More UK decisions are made at the point of sale, and build is self-declared in all of them.** 2,003,907 new individual protection policies were sold in the UK in 2025, income protection up 11.9% to 266,994 (Swiss Re Term & Health Watch, reported 2026-05-21). Insurers keep moving evidence out of the journey: Royal London raised its non-medical limits so about 1,500 customers a year no longer need routine medical tests and replaced paramedical exams with mini-screens (2023); Zurich and Aviva raised theirs too. Disclosure is moving earlier: Scottish Widows' pre-application decision tool (May 2025), iPipeline's Advanced Underwriting, which collects the 20 most common disclosures up front, said to account for up to 80% of post-application loadings and changes in terms (whole market 2025, Scottish Widows joining in 2026), and Iress's height, weight and waist questions on The Exchange. In every one of these, height and weight are what the applicant or adviser types.
2. **Declared build runs light, most of all at the higher BMIs where build is rated, and UK insurers meet the large gaps at claim.** In Health Survey for England data on 38,940 adults who were both asked and measured, the average gap is modest: women understated weight by 2.1 kg and men by 1.5 kg, and men overstated height by 1.6 cm (BMJ Open, 2023). The spread is wide. The SD of the weight difference was 4.4 kg for men and 4.5 kg for women; about a quarter of adults gave a BMI more than 2 units from the measured one; understatement was larger in the higher BMI categories; and self-report put only 69% of men and 72% of women with measured obesity in the obese category. 30% of adults in England live with obesity and 66% are overweight or living with obesity (HSE 2024, published January 2026). The gaps that surface at claim are large. Financial Ombudsman decisions from 2024 to 2026 turn on weight declared at application against GP records at claim. At Aviva the GP record was 1½ to almost 2 stone (about 9.5 to 12.7 kg) above the declared weight; the critical illness claim was paid at 67% as a proportionate settlement, and a further £32,937 followed once Aviva corrected the height it had used. At Legal & General, 85.3 kg was declared against records of 125 kg (2017) and 140 kg (2019) either side of a 2018 application; the claim was declined and the policy cancelled, and the ombudsman found that fair. At Scottish Friendly, the declared weight was about 7 kg above the GP's figure, and the true BMI was too low for the policy to be offered. Where the gap was up to 6 kg, at Zurich, the ombudsman put it down to weight gained after the application and overturned the proportionate settlement. L&G described an application-stage check "for common areas of non-disclosure, such as weight, smoking and lifestyle information". The market is paying to find these gaps after issue: UnderwriteMe's AI engine for post-issue audits, tested with four UK insurers (March 2026). In US accelerated underwriting audits, build and BMI are the most common misclassification reason, though usually a small class difference per case (Munich Re). Market context only: none of this goes into copy (Rules).
3. **FitXpress closes the gap the way insurers want, as evidence and not a decision, and the evaluation path is ready.** From `proof-points.md` and the live landing: two photos (front and side), "under 45 seconds from the photos to structured results", Smart Scales predicted weight at about 3.5% mean absolute error under evaluated conditions (a software estimate, not a scale reading), BMI from the declared height, a flag on the insurer's threshold, one timestamped machine-readable record through the API, web and mobile SDKs, and results returning to the insurer's systems only. The landing's pilot is the walkthrough, then a shadow evaluation with outputs kept out of decisions, then comparison against independently collected build evidence on criteria agreed in advance. It quantifies completion and retake rates, agreement with reference evidence, how many cases each candidate threshold would flag and the effect on review volume. Reinsurers already run this kind of test: Hannover Re compared video-selfie BMI with nurse-collected data over 26 weeks and named "reduce BMI non-disclosure" as a use. Compliance fits UK buyers: FitXpress is not a medical device under UK MDR for its current intended purpose; GDPR roles, a DPA with SCCs and a UK Addendum (`compliance.md`). **Limits, stated honestly:** no insurer reference customer; hosting is AWS US-West-2 (and part US-East-1); the weight estimate is not equivalent to a calibrated scale; height is taken from the application, so an overstated height is not caught; performance for people with physical disabilities has not been established; no blood pressure or other screening values.

**What the flag can separate from estimate error, and what it cannot.** The average understatement (1.5 kg for men, 2.1 kg for women, that is 1.5% and 2.6% of their measured mean weights of 84.4 kg and 70.5 kg) is smaller than the Smart Scales estimate's stated error, about 3.5% mean absolute error under evaluated conditions, which is about 3.0 kg and 2.5 kg at those weights. The flag cannot tell a typical applicant's understatement from estimate error, and the average is not the reason the product would work. It can separate gaps several times larger than that error: the gaps that move a case across the insurer's own build band or referral threshold, like the claim-stage cases above. The insurer sets the threshold above the estimate's error. The shadow evaluation then counts how many point-of-sale cases each candidate threshold flags and how often a flag agrees with independently collected build evidence. Two limits stay with it. Product-info publishes the error as one average, not by BMI band, and the large gaps sit at higher BMI. Part of the BMI gap comes from overstated height, which FitXpress takes from the application and does not catch. How much this weakens the angle is in Risk 3.

**Why now (UK):** the FCA's pure protection market study final report (September 2026) calls for "renewed momentum and active regulatory engagement" on medical-evidence delays and plans an industry roundtable in Q1 2027. Royal London's chief underwriter launched an electronic GP report service on 2026-10-05, saying electronic reports cut waits "from around a month to little more than a week in many cases". Evidence workflows are being rebuilt now. FitXpress does not replace GP reports or screenings; it adds a build data point to the cases that never get either.

## What earlier campaigns teach this one

- **Katerina's UK baseline** (`2026-07-31-uk-telehealth-digital-health`, closed): 258 invites, 69 accepted (26.7%), 13 replies (18.8% of accepted), 12 of them to Message 1. Meetings came from owners of programmes and evidence, with a hook in their own scope. Here that means chief underwriters, underwriting philosophy and development teams, and reinsurer underwriting R&D.
- **Insurers do answer.** `2026-08-14-au-digital-fitness` sent to 114 people at AIA Australia, a life insurer, on its wellness programme. One partnerships manager accepted a call (reply to Message 2) and the GM Life Product and Pricing named a colleague. Pricing and product leads route; that is why `Protection Pricing` is in the pull.
- **Say what the record is, in plain words.** A September UK reply to a Smart Scales message asked "It's an app to calculate BMI from a photo?" (`2026-09-27-uk-bariatric-prequal`). Message 1 says what comes back, in plain words (Rules, What the scan is).
- **Since 2026-10-07:** Message 1 = context and one question, no call ask, no link; Message 2 = the call with Katerina's calendar link, every lane. Fix-round lessons that apply at Aviva- and L&G-sized pools: the theme may repeat, the wording, hook, structure and closer may not; card wording is never copy; one call-length rule for everyone.

## Target buyer persona

**Who buys:** the owner of underwriting philosophy and evidence requirements at a UK protection insurer, usually titled Chief Underwriter or Chief Underwriting Officer, and the development underwriting team that changes the rules engine. At a reinsurer, the UK life and health underwriting lead and the underwriting R&D or solutions team that designs client evaluations. The protection proposition and new-business owners decide where a step sits in the application; the chief medical officer signs off on what an estimated value may be used for.

- **Why these titles, not others:** in the UK the chief underwriter owns non-medical limits and the evidence process. Royal London's chief underwriter fronted both its 2023 non-medical-limit changes and its 2026 electronic GP report service; AIG Life's development underwriting team made its rules-engine changes. CRO, CIO and distribution heads are group-wide or adviser-facing and do not own the evidence a case collects. From the other `icp-detail.md` §3 titles, innovation, digital transformation and insurtech leads are pulled (the ICP's first trigger is digital transformation, and the use-case file names Head of Digital Innovation); product managers are reached through `Protection Proposition` and `Head of Product`, because a bare Product Manager filter at multi-line groups returns general insurance, wealth and IT product owners; population health (a US health-plan role) and compliance or financial-crime teams are not pulled, because neither owns the evidence a point-of-sale case collects.
- **What they care about (KPIs):** the share of cases decided at point of sale; referral volume and time to decision; evidence cost per case (nurse screenings, mini-screens, GP reports); how often terms change after application; post-issue audit findings; claims settled proportionately or declined over build (never in copy); adviser experience; fair outcomes across customer groups.
- **Objections they will likely raise, with the honest answer:**
  - An estimated weight is not a measured weight, and the typical gap is smaller than your error. True on both counts. Smart Scales is a software estimate at about 3.5% mean absolute error under evaluated conditions, about 2.5 to 3 kg at the measured mean adult weights in England, and the average understatement in survey data is 1.5 to 2.1 kg. The flag does not correct each applicant's weight. It refers the gaps well beyond that error, the ones large enough to move a case across the insurer's own build band or referral threshold, and the insurer sets that threshold. Flagged cases go to the existing referral queue; the rest stay on their current path.
  - How many of our cases would that catch? Not known until an evaluation runs on the insurer's own applicants. Survey data put the larger gaps at higher BMIs, where build is rated, and the shadow evaluation counts how many cases each candidate threshold flags and how often a flag agrees with independently collected build evidence, before any output reaches a case.
  - Does the error hold at higher BMI? Product-info publishes one average figure and no breakdown by BMI band. Agreement by build band is a criterion to agree before the evaluation starts; methodology under NDA.
  - We would never decline on photos. FitXpress does not make underwriting decisions; the insurer's rules and underwriters do. Cases under the threshold stay on their current path.
  - It adds friction for advisers and clients. Under 45 seconds from the photos to structured results; the insurer chooses where the step is offered; the evaluation measures completion and retake rates.
  - Where is the data? AWS, primarily US-West-2. GDPR roles and a DPA with SCCs and a UK Addendum; replies use `compliance.md` §10; documents through legal@3dlook.me.
  - Does it work fairly for everyone? Measurement validation covered ages 16 to 78, heights 150 to 220 cm, weights 38 to 210 kg, participants from the US and Europe; performance for people with physical disabilities has not been established, and the insurer keeps its current route for anyone who cannot or does not scan. Methodology under NDA.
  - Which insurers use it? None yet. The same capture, processing and integration run in production in remote BMI-verification and weight-management workflows; 3DLOOK has worked with 100+ clients.
  - Does it check height? No. Height comes from the application.
- **Tiers (order only; everyone goes in one import file):** P1 Chief Underwriting Officer, Chief Underwriter and deputy, Head of Underwriting, Chief Medical Officer, Head of Protection or Protection Director at an insurer; Head of Life and Health or UK underwriting lead at a reinsurer; CEO or CPO at a platform. P2 underwriting philosophy, development, rules, research and solutions leads, client underwriting managers, development underwriters, medical officers, protection proposition and new-business heads, protection pricing heads, and innovation, digital transformation or insurtech leads whose title or profile shows protection, life, underwriting or new-business scope. P3 underwriting managers, CTOs, heads of product, data protection officers, group-wide innovation and transformation leads. P4 referral.
- **Lanes by title:** `underwriting` (underwriting leadership, philosophy, development, rules, research, development underwriters, underwriting managers, new-business underwriting); `medical` (CMOs, medical officers); `proposition` (protection heads and directors, proposition, new business, product, pricing, and innovation, digital transformation or insurtech leads at an insurer whose title or profile shows protection, life, underwriting or new-business scope); `reinsurance` (everyone at group B except CMOs, CTOs and DPOs); `partnership` (everyone at group C except CTOs and DPOs); `technical-integration` (CTOs, architecture, DPOs, information security owners for new business); `referral` (anyone Vadim adds at step 4 from outside these functions, and group-wide innovation or transformation leads at an insurer).
- **Not the buyer (FAIL, or offered as a skipped pool at step 4):** individual underwriters, senior underwriters and underwriting assistants unless the title says development, philosophy, rules or research; claims handlers and claims heads (default, Open question 4); adviser-facing BDMs and distribution sales; anyone at a multi-line group outside protection or life and health (general insurance, pensions, annuities, investments, wealth, group risk, PMI); P&C staff at reinsurers; anyone located outside the UK. Standing decisions 3 and 4 below cover functions inside the protection business; a different business line is not a different function.

### Target buyer persona: Sales Navigator pull for step 3

**Pull by title filter inside the approved company list, never by company alone.** Add the Sales Navigator geography filter "United Kingdom" to every company: the reinsurers, Aviva, Zurich and the platforms have global pages, and `sales-nav-query` does not write a geography line. Several lines are phrases Sales Navigator matches inside longer titles (Underwriting Philosophy finds both Head of Underwriting Philosophy and Underwriting Philosophy Manager).

```titles
Chief Underwriting Officer
Chief Underwriter
Head of Underwriting
Underwriting Director
Director of Underwriting
Underwriting Philosophy
Development Underwriter
Underwriting Development
Underwriting Rules
Underwriting Research
Underwriting Manager
Head of Underwriting Solutions
Client Underwriting
Automated Underwriting
Chief Medical Officer
Medical Officer
Head of New Business
Head of Protection
Protection Director
Protection Proposition
Protection Pricing
Head of Life and Health
Chief Product Officer
Head of Product
Head of Innovation
Innovation Director
Innovation Manager
Underwriting Innovation
Digital Transformation
Insurtech
Chief Technology Officer
Data Protection Officer
```

**`cap_per_group: 50`** (default for every campaign; only Vadim changes it). After the title and geography filters no group is expected near 50; if Aviva or Legal & General comes back over it, the validator ranks by tier and Vadim decides.

## Message angle: lanes, account facts and the content asset

Every person gets exactly one lane, spelled as below. Numbers come only from Rules. Lane notes are instructions to the writer and never copy.

**The angle, for every lane (a target, reworded for each person):** the cases the company decides at the point of sale without medical evidence, where build is declared, and what a second source of build evidence inside the application would add there, on the company's own threshold, with the company's rules and underwriters deciding. What comes back is listed once, in Rules (What the scan is). For reinsurers, the same evidence as a candidate for a client evaluation and for the build section of a manual or rules engine. For platforms, the same evidence as a step their application could offer insurers through one integration.

**Lanes:**
- **`underwriting`** Target: how build is handled on point-of-sale cases today, and which gaps would change a build rating there. The flag is a referral trigger for gaps large enough to cross the company's own build band or referral threshold, set above the estimate's error; never suggest it settles small differences or corrects each applicant's weight. Question targets: how build is checked on cases that never see a nurse screening; at which build band edges a gap between declared and estimated weight would change the outcome; what the philosophy or development team needs to see in a shadow evaluation before any output reaches a case; how build is treated on income protection against life and CI. Message 2 value: the evaluation path, which counts how many cases each candidate threshold would flag and how often a flag agrees with independently collected build evidence.
- **`medical`** Target: what an estimated value may and may not be used for. The estimate's stated error is larger than the typical gap between declared and measured weight; its defensible use is a referral threshold set well above that error, on gaps that would change the build rating, and the questions start there. Question targets: what a medical officer would need to know about a software weight estimate before it enters referral rules; how far above the estimate's error a referral threshold would have to sit before a flag is worth an underwriter's time; how the manual's build guidance treats declared and measured weight. Message 2 value: the estimate's stated error under evaluated conditions, that it is not a scale reading, that the insurer sets the threshold, and the not-a-medical-device boundary.
- **`proposition`** Target: where the step sits in the journey. Question targets: at which point of the application a two-photo step could sit (adviser-keyed application, client declaration step, direct journey); how a new step is tested with advisers; how drop-off is measured; how build-related changes in terms after application show up in adviser feedback. Pricing heads: how build loadings and evidence cost are weighed. Message 2 value: under 45 seconds from the photos, results to the insurer's systems only, completion measured in the evaluation.
- **`reinsurance`** Target: evaluating new evidence with client insurers. Question targets: how the UK team tests a new remote evidence source with clients; whether any client has asked about remote build evidence; how a build flag would sit in the manual or the rules engine the team supports. Message 2 value: a shadow evaluation design the team could run with one client. Never mention another reinsurer's pilot or any client of theirs.
- **`partnership`** Target: one integration that several insurers could switch on. Question targets: how a new evidence step is added to the platform's application or decision journey; what insurer clients ask the platform for at the point of sale. Message 2 value: API and web and mobile SDKs, one timestamped record per applicant returned to the platform.
- **`technical-integration`** Target: integration and vendor review, technical tone. Question targets: how a new data processor is reviewed for the new-business journey; how an SDK step enters the e-application; how a structured record reaches the underwriting workbench. Message 2 value: REST API and SDKs, the UK compliance line, photo retention (deleted after processing or within 30 days, per the insurer's policy, retained photos blurred, faces obscured at capture) and scan records on random identifiers; documents through legal@3dlook.me. DPOs and security owners get the data handling; SDK detail goes to CTOs and architects.
- **`referral`** Message 1: what the record is and why it matters to this company's point-of-sale cases, then one question about the person's own work. Message 2: a value line that continues their question, the call offer with the calendar link, and an easy out that points to whoever owns underwriting philosophy or the new-business journey there, worded fresh for each person.

**Question bank discipline (big pools).** Each person gets one question nobody else at the company gets, built from their title. One topic serves at most about a fifth of a company's people. Wording, hook, structure, easy-out target and closer never repeat at one company.

### Account facts (filled after step 2)

`company-researcher` records for every IN company one to three public facts from the last 18 months about its underwriting, evidence or protection proposition, each with a source URL and date: a rules-engine change, a medical-evidence service, non-medical limits, a pre-application or point-of-sale tool, a new income protection or critical illness product, a platform it went live on. **Before step 5, a fresh `hypothesis-generator` round writes them here as one bullet per company (fact, source, Never: line).** Copy may use a company's own fact without its numbers. Never as a fact: claims-paid rates, ombudsman decisions, complaints, fines, ratings, market share, exits, deals, its reinsurers or its vendors.

### Content asset in Message 2

At most one 3DLOOK link next to the calendar link: the landing https://3dlook.ai/for-insurance-underwriting/ in any lane, or in `technical-integration` the privacy FAQ https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/ instead. Both HTTP 200 on 2026-10-22. Not linked: the hub article `/content-hub/mobile-body-scanning-insurance-underwriting/` (US sources and US terms) and `/fitxpress/for-insurance-underwriting/` (404 until `/fitxpress/` ships).

## Rules for steps 3-5

- **Sender and format:** Katerina, British English, `Katerina` alone on the last line. Connection request with no note. Message 1 ≤ 600 characters, Message 2 ≤ 550. CEO-to-chief-underwriter register: formal, short, specific, no enthusiasm words.
- **Message 1:** context about this company and one question; no call ask, no link of any kind. **Message 2:** a call offer and https://meetings.hubspot.com/katerina-galich as plain text, in every lane, referral included. No call length or minutes in any message.
- **Landing URL (Vadim, 2026-10-22).** Message 2 may carry https://3dlook.ai/for-insurance-underwriting/ as plain text, on its own, with no punctuation glued to it; the calendar link stays required. Optional per person: at one company no more than about half of the Message 2s carry it, and the sentence around it differs each time. Never in Message 1.
- **US-worded background in the card.** The use-case and ICP excerpts this card includes (`fx-insurance-underwriting.md`, `icp-detail.md`) are US-worded background. This campaign's UK idiom, compliance line and banned terms override them, and no message carries HIPAA wording.
- **Lanes are exactly** `underwriting`, `medical`, `proposition`, `reinsurance`, `partnership`, `technical-integration`, `referral`.
- **UK idiom.** Write insurer, application, point of sale, non-medical limits, nurse screening or mini-screen, GP report, referral to an underwriter, terms, loading. The landing's US terms (carrier, paramedical exam, face amount, APS, accelerated path) are not used.
- **What the scan is (a target, not wording).** Message 1 makes clear what comes back and who decides. The parts: two photos taken in the application, a Smart Scales weight estimate, BMI calculated from the height the applicant declared, a flag when the gap crosses the threshold the insurer sets, and one timestamped structured record returned to the insurer's systems. Every Message 1 carries the photos and the threshold flag; which other parts appear, in what order and in what words, varies between people at one company. A single label such as a BMI-from-a-photo app is never enough.
- **What it is not.** It does not make or recommend underwriting decisions, rate, price, accept or decline. It does not check height. It does not replace a GP report, nurse screening, mini-screen or any evidence the insurer's guidelines require; it adds evidence to cases that get none of these. It is never described as hidden, covert or mandatory for applicants: the insurer decides where it is offered and keeps its current route for anyone who cannot or does not scan.
- **Applicants are never suspects.** No message says or implies that applicants lie, hide or misstate anything, or that this company's applicants or advisers do. Talk about declared build and what the record adds. No claims, claim disputes, settlements, ombudsman, complaints or regulator, for any company.
- **Lead with the record,** which is what the ICP calls defensibility: timestamped, structured, on the case file, the insurer's threshold, the insurer's rules. No accuracy percentage opens a message or carries Message 1.
- **Numbers only from this list:** two photos (front and side), with "2 photos" as the numeric form; "under 45 seconds from the photos to structured results" (the only speed wording, as its own plain sentence and only where speed is the point); 80+ body measurements as an output, and a 3D model "when enabled for the deployment" (both secondary, never the lead); Smart Scales "approximately 3.5% mean absolute error under evaluated conditions", always with "not a scale reading" in the same sentence, Message 2 only, in `underwriting`, `medical` and `reinsurance` only; "3DLOOK has worked with 100+ clients"; "112,100 scans in 2025 across all 3DLOOK customers" as its own sentence, never tied to the UK, insurance or a client. No 96-97% or other measurement-accuracy figure, no repeatability figure, no validation-population figure in cold copy (replies use `accuracy-formulations.md`). No integration-time figure in any message. No market, obesity, survey, claims or prospect figures, and none of the landing's US statistics.
- **Smart Scales** is named without a "(beta)" label (public wording, `tech-spec.md`, Vadim 2026-10-21). It is a software estimate; never "weighs", never "measures weight". Never suggest the flag settles small weight differences or corrects each applicant's declared weight: it refers gaps above a threshold the insurer sets.
- **Proof without names.** No 3DLOOK client is named; the UK online-pharmacy 7,500 line is not used. The production line comes from the landing: "production infrastructure already deployed in remote BMI-verification and weight-management workflows". That quoted line is the only place the word verification may appear (it is left off `banned_terms` for this line alone); verify, verified and verifies stay banned. Never imply an insurer or reinsurer uses FitXpress.
- **Compliance line.** At most one per pair, Message 2 only, in `underwriting`, `medical`, `proposition`, `reinsurance` and `technical-integration`, verbatim: "In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes SCCs." The boundary sentence, verbatim, at most once per pair, any lane: "FitXpress is not a medical device and does not make underwriting decisions." Nothing about hosting location, UK data residency or data transfers in cold copy; replies use `compliance.md` §10 and legal@3dlook.me. Never "compliant", "certified" or a medical-device claim.
- **Data handling sentences.** Only the forms in `compliance.md`: photos deleted after processing or within 30 days per the insurer's policy, retained photos blurred, faces obscured at capture; scan records on random identifiers; outputs stored until deleted by scan identifier on the customer's request. Never "not stored", "no personal data" or "anonymous".
- **Several people at one company.** Name the company in every Message 1. Never mention colleagues, other teams or a conversation that did not happen. No two people at one company share an opener, a central question, an easy-out target, a Message 2 opener or a closer.
- **Never name one prospect in another prospect's copy,** including a reinsurer in an insurer's message, an insurer in a reinsurer's or platform's message, and any vendor or platform an insurer uses. A company's own product may be named in its own copy only (UnderwriteMe's Protection Platform to UnderwriteMe, Magnum to Swiss Re). Never mention ownership, deals or the parent of Aviva's former AIG Life business. The rule covers message text; the linked landing citing public research by Gen Re and Munich Re is not a message naming a prospect.
- **Former employers** may be named (standing decision) unless they are another account in this campaign, a competitor or a banned term.
- **Word traps.** Never "objective" about our data; no em or en dash; no "plus" as a connector; no "so" introducing a benefit; no corrective "X, not Y"; none of the buzzwords on the hard-bans card.
- **No pricing and no trial terms** anywhere; a price or pilot-terms question goes to the call.
- **Writer notes and card instructions are not copy.** Lane notes, targets and rule sentences are never pasted; quoted lines above are the only verbatim copy.
- **Message 1 gate.** Every message 1 carries at least one product specific from `proof-points.md` and one line that could only have been written to that company; each pair of messages cites at least one number. The gate recognises "two photos", "2 photos", "body measurements", "API" and "SDK" as product specifics (it does not recognise "two guided photos" or "weight estimate" alone), and "under 45", "2 photos", "80+", "3.5%" and "112,100 scans" as numbers. Referral people included.

## Anti-cases (where it does NOT work)

- **Group risk** (group life, group income protection, group CI): members are accepted within free cover limits without individual underwriting; build enters only above the limit.
- **Guaranteed-acceptance over-50s life** (SunLife, Post Office over-50s and similar): no health or build questions.
- **Private medical insurance** (Bupa, AXA Health, the health side of Vitality, WPA): moratorium or full medical underwriting where build is rarely rated. VitalityLife is in; VitalityHealth is not.
- **Enhanced and impaired-life annuities:** a higher BMI improves the rate, which reverses the incentive; it is also a retirement product.
- **Closed books and consolidators** (Phoenix, ReAssure, Chesnara Life since its February 2026 purchase of HSBC Life UK): no new protection business, or a recent acquisition (`icp-detail.md` universal exclusion).
- **Insurers that left individual protection:** Canada Life UK (2022), Aegon UK (2023).
- **Advisers, brokers and comparison sites** (LifeSearch, Drewberry, Reassured, CIExpert and the like): they do not underwrite.
- **Medical-evidence suppliers** (nurse-screening and GP-report firms): they sell the evidence FitXpress would be compared with; a partner conversation for later, outside this campaign.
- **Cases above non-medical limits or with disclosed conditions:** a nurse screening or mini-screen already measures height and weight; FitXpress adds nothing there.
- **Irish, Isle of Man and other offshore arms** (Irish Life, New Ireland, Canada Life International): not this profile's market.
- **Any company whose application already runs a remote body, face or BMI-from-image capture:** the researcher checks; if found, it is held for Vadim.

## Vadim's standing decisions (already applied above)

1. **No headcount floor** (2026-09-29); the segment revenue threshold stays ($5M+ for §3).
2. **`cap_per_group: 50` for every campaign, no waves** (2026-09-29): one closely.io import file.
3. **A lane for every function** at an IN company (2026-09-29), applied inside the protection or life-and-health business (Target buyer persona).
4. **FAIL only for the wrong company, people who left, identity collisions and duplicates,** along with this campaign's out-of-business-line and out-of-UK rules; company-named profiles are held for Vadim.
5. **Former employers may be named** (2026-09-29), within the Rules' limit.
6. **Live 3DLOOK pages may be linked as they are** (2026-09-29); copy uses only the approved wording.
7. **No 3DLOOK client is named;** 112,100 scans as 3DLOOK-wide scale (2026-09-29); "3DLOOK has worked with 100+ clients" (2026-09-30). For `katerina`, the UK 7,500-scan line is not used (2026-09-27).
8. **Message 1 asks, Message 2 calls** (2026-10-07), every lane.

## Vadim's decisions 2026-10-22

1. **Direction (Vadim, 2026-10-22, through the coordinator):** an outbound campaign built on the live landing https://3dlook.ai/for-insurance-underwriting/, market England / UK, sent from Katerina Galich's account; `product: fitxpress`, `profile: katerina`, `market: UK`, `use_case: fx-insurance-underwriting`, `cap_per_group: 50`. The sub-segment was left to this hypothesis.
2. **The landing URL is allowed in Message 2,** next to the required calendar link, as plain text on its own with nothing glued to it, optional per person, to keep one insurer's Message 2s from all repeating it. It stays banned in Message 1 (hard gate). Relayed by the coordinator on 2026-10-22; written into Rules.

## Vadim's decisions 2026-10-22 (2)

Vadim approved the hypothesis after the QC fix round («все так. спочатку сейлз навігатор а потім доберем через аполо»): every open question takes its default.

1. **Approved:** `status: approved`, research may start.
2. **Reinsurers:** group B goes out from `katerina` as UK entities (`Swiss Re UK` and so on). The global parents stay open for Olena and Nick.
3. **Smart Scales** is named in cold copy, in both messages. The 3.5% figure goes only in Message 2 of `underwriting`, `medical` and `reinsurance`, with "under evaluated conditions" and "not a scale reading".
4. **Platforms** (UnderwriteMe, Iress, iPipeline UK) are in, in the `partnership` lane.
5. **Claims heads are not pulled.** Protection Pricing is pulled as P2 `proposition`.
6. **Chesnara Life is OUT.** Aviva is IN, and the AIG Life deal is never mentioned.
7. **People source:** Sales Navigator first (`outbound_pack.py sales-nav-query`, with the United Kingdom geography filter added by hand), then an Apollo top-up (`apollo-pull.py search`, then `enrich`, with the credit count named to Vadim before `enrich` if it exceeds 100).

## Vadim's decisions 2026-10-22 (3)

After research, Vadim on the three displacement holds: «залишай всі». **Legal & General, Hannover Re UK Life Branch and Gen Re UK stay IN.** Their earlier face- or video-based estimates (L&G America's 2017 selfie quote, never launched in the UK; Gen Re's 2019 selfie-BMI prototype for the US and Asia; Hannover Re UK's face-scan study for vital signs, not build, and the group's video-BMI pilot in South Africa) are context for the company line only. The vendor and product names stay banned in copy.

## Validation criteria (Step 2 will check)

- **Companies.** 28 named candidates (18 + 7 + 3); target 25 IN rows from groups A, B and C. Fewer than 22: stop and report to Vadim; do not widen to group risk, PMI, brokers or evidence suppliers on your own, and do not add companies to reach a number. Each insurer is confirmed open to new underwritten UK individual protection in 2026 (adviser site, product page or 2026 trade press); each reinsurer row is the UK life and health team writing UK protection; each platform is used by UK protection insurers at the point of sale.
- **Schema.** `hq_country` United Kingdom on every row. Group names as the UK entity for groups B and C where the parent is abroad (`Swiss Re UK`, `Munich Re UK Life Branch`, `Hannover Re UK Life Branch`, `Gen Re UK`, `RGA UK`, `SCOR UK`). Name LV= as `Liverpool Victoria (LV=)` and check the two-letter key `lv` does not join unrelated rows. `icp_fit` high or medium only.
- **Registry.** `outbound-registry.py check --profile katerina` after extract; expect no hits. Watch `phoenix-health` against any Phoenix row (Phoenix is an anti-case anyway).
- **Account facts and displacement.** For every IN company: one to three dated underwriting or proposition facts with URLs (Message angle, Account facts), and a search of its site, adviser site and trade press for any remote body scan, face or video BMI estimate, selfie quote or image-based build tool. Hits are held for Vadim.
- **People.** UK-located only; protection or life-and-health only at multi-line groups; tiers and lanes as in Target buyer persona. Junior underwriters FAIL unless the title says development, philosophy, rules or research.
- **C-level availability.** Chief underwriters, heads of underwriting and CMOs are visible in Sales Navigator with the UK geography filter at most group A insurers and every group B reinsurer.
- **Proof in product-info.** Use-case file and live landing: yes. Insurance reference customer: none. Proof is the landing's production-use line, 100+ clients and 112,100 scans, used as Rules allow.
- **Message 1 gate.** As in Rules: every message 1 carries at least one product specific from `proof-points.md` and one line that could only have been written to that company; each pair cites at least one number. Zero client names, banned terms, links in Message 1, accuracy figures in Message 1, suspicion framing or decision claims. Kept as a failure, not a note: `2026-07-21` sent 307 first messages with no specific and drew 1 reply on 67 sends.

## Success metrics for this campaign

Denominators as in `metrics-final.json` (Closely event counters). Senior insurance underwriters accept less readily than the July health list, so targets sit below that baseline.

| Metric | Target | Floor | Basis |
|---|---|---|---|
| Invites sent | 150-250 | 100 | about 25 IN companies after title and UK filters |
| Connection acceptance | 22% | 15% | `katerina` UK July 26.7% |
| Replies per accepted person | 10% | 5% | July 18.8%; AIA Australia 2 replies on 114 sends |
| Positive replies (interest or a question) from P1-P2 | 4 | 1 | |
| Companies with at least one reply | 7 of about 25 IN | 4 | about a quarter of IN companies |
| Discovery calls | 3, at different companies | 1 within 8 weeks | |
| Shadow-evaluation conversations (insurer or reinsurer) | 1 | 0 | the landing's pilot step |

**Falsified if** three or more P1 or P2 replies say build is not a material gap on point-of-sale cases, that an estimated weight cannot enter their referral rules at any threshold, that gaps large enough to change a build rating are too rare at the point of sale to justify a step, or that US hosting rules a vendor out. **Inconclusive** if fewer than 25 people accept.

## Risks

1. **No insurer reference.** Underwriters may want a named UK insurer before a call; the offer is an evaluation, not a deployment.
2. **US hosting.** UK insurers' data protection reviews may ask for UK or EU hosting; the FAQ offers none.
3. **The flag works on large gaps, and nobody knows yet how many there are.** The estimate's stated error (about 3.5% MAE, about 2.5 to 3 kg at England's measured mean weights) is larger than the average understatement (1.5 to 2.1 kg). The flag separates only gaps well beyond that error, which survey data place among a minority of applicants at higher BMIs. This weakens the angle: the case rests on a minority of point-of-sale cases with large gaps, not on correcting the typical applicant, and a chief underwriter or CMO who knows the averages will raise it first. If a shadow evaluation finds few flags above the error at the insurer's band edges, the value case is thin. Product-info gives the error as one average, not by BMI band. The live landing's sample payload shows a flag on a +3.3% gap, inside that error (text of record l.114), and an underwriter who opens the page may read it as the intended use. Medical officers may also hold that only a measured weight counts; the flag-and-refer design and the shadow evaluation answer that.
4. **Fairness scrutiny.** Insurers must show fair outcomes across customer groups; the validation population and the disability limitation will come up.
5. **Reinsurer sensitivity.** Reinsurers and their client insurers talk; a message to both about the same idea is fine, a message that names the other is not (Rules).
6. **Landing in US idiom.** The linked page says carrier, paramedical examination and face amount and cites US statistics; UK underwriters will notice (Open question 6).
7. **Small universe.** 28 named companies, about 25 expected IN; one weak angle uses up the UK protection market for this profile.

## Open questions for Vadim

> Answered 2026-10-22: every default taken, see `Vadim's decisions 2026-10-22 (2)`.

1. **Reinsurers' UK teams from `katerina`.** Group B is recorded as UK entities (`swiss-re-uk` and so on), which leaves Olena (Swiss Re, Munich Re, Hannover Re, SCOR head offices) and Nick (Gen Re, RGA) free to work the parents. Default: yes, UK teams from Katerina, parents left open. Or register the global parents and block them for other profiles?
2. **Smart Scales in cold copy.** `2026-10-16-us-employer-obesity-care` kept it out; this landing is built on it. Default: named in both messages, the 3.5% figure only in Message 2 of `underwriting`, `medical` and `reinsurance`, with "under evaluated conditions" and "not a scale reading".
3. **Platforms as `partnership`** (UnderwriteMe, Iress, iPipeline UK). Default: in. Nurse-screening and GP-report suppliers stay out.
4. **Claims heads.** Default: not pulled (claims copy would touch disputes the Rules ban). `Protection Pricing` is pulled as P2 `proposition`. Add claims titles?
5. **Chesnara Life** (HSBC Life UK until February 2026): default OUT as a recent acquisition. Aviva's 2024 purchase of AIG Life UK is past that window: Aviva IN, the deal never mentioned.
6. **Landing UK wording (non-blocking note for Asel).** The live page (curl, 2026-10-22) still uses US terms: carrier ×7, paramedical ×4, face amount ×2. A UK wording pass (insurer, nurse screening, GP report) would suit UK underwriters now that Message 2 may send them there. None of these terms goes into copy (Rules, UK idiom), and the campaign does not wait for it.

## Sources

All read on 2026-10-22 unless marked.

- Swiss Re Term & Health Watch 2026 (2025 sales): https://healthcareandprotection.com/individual-protection-market-rebalancing-as-sales-drop-1-7-year-on-year-swiss-re/ (2026-05-21)
- FCA market overview, five firms ~80% of new premium: https://healthcareandprotection.com/fca-publishes-pure-protection-market-overview/ (2025-09-17)
- 13 major providers, 11.5M policies in force: https://healthcareandprotection.com/health-protection-individual-protection-report-market-recovers-with-in-force-members-up-and-new-business-driven-by-ip/
- Exits and "here to stay": https://healthcareandprotection.com/exclusive-remaining-protection-insurers-tell-advisers-they-are-here-to-stay/ (2026-01-16) · Aviva and AIG Life completion: https://healthcareandprotection.com/aviva-wraps-up-acquisition-of-aigs-uk-protection-business/ · Chesnara and HSBC Life UK: https://www.hsbc.com/news-and-views/news/media-releases/2025/hsbc-agrees-to-sell-its-uk-life-insurance-manufacturing-business-to-chesnara
- FCA final report on medical-evidence delays and Q1 2027 roundtable: https://healthcareandprotection.com/fca-targeting-medical-evidence-delays-to-improve-protection-sales/ (2026-09-21) · https://www.fca.org.uk/publications/market-studies/ms24-1-market-distribution-pure-protection
- Royal London electronic GP reports: https://healthcareandprotection.com/royal-londons-new-magic-service-aims-to-cut-delays-in-getting-gp-reports/ (2026-10-05) · non-medical limits: https://healthcareandprotection.com/royal-london-makes-changes-to-non-medical-limits-for-life-cover/ (2023-08-23)
- Zurich non-medical limits: https://www.zurichintermediary.co.uk/advice-matters/non-medical-underwriting-limits-for-under-50s · Aviva thresholds: https://healthcareandprotection.com/aviva-ups-medical-underwriting-thresholds-and-eases-covid-rules/
- Scottish Widows pre-application tool: https://healthcareandprotection.com/scottish-widows-launches-pre-application-underwriting-decision-tool/ (2025-05-28) · iPipeline Advanced Underwriting: https://ifamagazine.com/ipipeline-launches-advanced-underwriting-to-whole-of-market/ · https://ifamagazine.com/scottish-widows-to-add-protection-products-to-ipipelines-advanced-underwriting-platform/ · Iress BMI and waist questions: https://www.covermagazine.co.uk/news/3000211/iress-reforms-underwriting-capability-bmi (2016)
- UnderwriteMe: https://underwriteme.com/ (products: Decision Platform for insurers, Protection Platform for advisers) · https://underwriteme.com/our-story · AI post-issue audit engine: https://healthcareandprotection.com/underwriteme-launches-ai-engine-for-post-issue-audits/ (March 2026) · AIG Life rules engine on Swiss Re Magnum Pure: https://www.covermagazine.co.uk/analysis/4150670/aig-life-overhauls-underwriting-rules-engine (2023-11-27)
- Self-reported vs measured build, HSE: https://bmjopen.bmj.com/content/13/1/e061809 (2023) · its Tables 1-2 (measured mean weights 84.4 kg and 70.5 kg, obese-category sensitivity 69% and 72%) via Europe PMC: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9843181/fullTextXML · SD of the differences (4.4 and 4.5 kg), "about three-quarters" within 2 BMI units and larger understatement at higher BMI are in the article text · HSE 2024 obesity: https://digital.nhs.uk/data-and-information/publications/statistical/health-survey-for-england/2024/adults-overweight-and-obesity (read via nhsd-proxy.openprescribing.net mirror)
- Financial Ombudsman decisions on declared weight: L&G https://www.financial-ombudsman.org.uk/decision/DRN-6204112.pdf · Aviva https://www.financial-ombudsman.org.uk/decision/DRN-5974980.pdf · Zurich https://www.financial-ombudsman.org.uk/decision/DRN-4958834.pdf · Scottish Friendly https://www.financial-ombudsman.org.uk/decision/DRN-4947418.pdf · L&G https://www.financial-ombudsman.org.uk/decision/DRN-4614460.pdf · L&G https://financial-ombudsman.org.uk/decision/DRN-4559985.pdf
- Hannover Re video-selfie pilot: https://www.hannover-re.com/en/life-and-health/inspire/underwriting-case-studies/ai-video-technology-for-health-and-risk-insights/ (undated page) · Gen Re selfie prototype: https://www.dig-in.com/news/gen-re-pilots-selfie-based-life-insurance-underwriting (2019) · L&G SelfieQuote (US): https://www.insurancebusinessmag.com/us/news/technology/lga-launches-fun-and-simple-selfiequote-tool-90113.aspx
- Munich Re US misclassification: https://www.munichre.com/us-life/en/insights/future-of-risk/misclassification-driving-mortality-slippage-in-auw.html · Gen Re 2025 US Next Gen Underwriting Survey: https://www.businesswire.com/news/home/20251217204891/en/Gen-Re-Releases-2025-U.S.-Individual-Life-Next-Gen-Underwriting-Survey-Results · LIMRA 2020 (the landing's "9vs27"): https://www.limra.com/en/newsroom/industry-trends/2020/life-insurers-look-to-make-the-underwriting-process-easier-for-customers/
- Guardian 2026: https://healthcareandprotection.com/guardian-sets-sights-on-customers-who-dont-have-any-protection/ · Beagle Street underwriter: https://www.onefamily.com/life-insurance/ · Wesleyan income protection: https://www.wesleyan.co.uk/protection/income-protection
- Live landing re-fetched 2026-10-22 (~12:33 UTC): the "9 vs 27 days" line credits LIMRA and links to the 2020 article; the 59% line credits Gen Re and links to its 2025 survey PDF; sample payload +3.3%; carrier ×7, paramedical ×4, face amount ×2: https://3dlook.ai/for-insurance-underwriting/
- Product: `brand-assets/product-info/proof-points.md`, `compliance.md`, `accuracy-formulations.md`, `tech-spec.md`, `use-cases/fx-insurance-underwriting.md`, `icp-detail.md` §3; landing `workspace/pages/for-insurance-underwriting/published-live-2026-10-21.md` and `fact-sheet.md`.
