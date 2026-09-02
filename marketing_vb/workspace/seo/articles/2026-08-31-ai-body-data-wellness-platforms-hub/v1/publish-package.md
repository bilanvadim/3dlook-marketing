---
slug: 2026-08-31-ai-body-data-wellness-platforms-hub
product: fitxpress
status: ready_for_review
created: 2026-08-31
checkpoint: 2 (final text + meta), awaiting Vadim
---

# Publish Package: AI Body Data for Wellness Platforms (Hub #8)

## Meta

**Title:** AI Body Data for Corporate Wellness Platforms | 3DLOOK (54 chars)
**Description:** How a corporate wellness platform can use measured body data for progress tracking, personalization, and member engagement, and what to ask a provider. (151 chars)
**URL slug:** `ai-body-data-wellness-platforms`
**Category:** Content Hub, Health / Wellness (Hub #8 main hub)
**Word count:** 3,450 (target 3,200, +7.8%)

> Note on the title: the H1 deliberately omits the head term and the meta title carries it.
> That split was the decision taken at checkpoint 1. The H1 stays the approved architecture
> label; `corporate wellness platform` (500/mo, KD 11) does the search work in the meta title,
> the first paragraph, one H2, and the routing block.

## SEO checklist

- [x] Primary keyword in first paragraph and in one H2 ("What a corporate wellness platform should evaluate in a body-data provider"). **Not in H1, by decision** at checkpoint 1: the approved H1 is the strategy-row title verbatim. 4 occurrences across 3,450 words.
- [x] Meta title 54 chars, primary keyword starts at char 18 of 54 (first half)
- [x] Meta description 151 chars, primary keyword once, no overlap with the title
- [x] Every number traceable to an approved claim (FX-001, 002, 003, 004, 006, 007, 008, 009, 010, 011, 014, 016). One invented illustrative figure was removed during editing.
- [x] No banned words (detector: 0 hard fails)
- [x] Word count within ±10% of target (+7.8%)
- [x] Intro hook in the first two sentences ("Most wellness programs know two things about a member's body: what the scale said and what the member typed into a form.")
- [x] CTA placement and type match the plan: evaluation CTA after H2.8 where the boundary section ends, layered routing block at H2.12. Intent is Hub, so no single hard demo ask.
- [x] No generic AI patterns (0 punch triads, 0 negative parallelism, 0 em dashes)
- [x] **Terminology guardrails**: 0 em dashes · 0 "objective" about our own output · 0 "reader/audience/following sections/below" · 0 "this article/this guide" · 0 "by hand" · 0 "let" · 0 "plus" as connector · 0 "so" as benefit connector · 0 "positioned as" · 0 presumed-reaction phrases · 0 behaviour attributed to concepts. Judgment rows walked manually: 0 "we/our/you/your", 0 corrective "rather than", 3 corrective negations found and rewritten.
- [x] **Abbreviations (M1 + exception)**: BMR, HIPAA, GDPR, API, SDK, DEXA and BIA each expanded at first use, short form thereafter. BMI, AI, US, EU left bare per the commonly-known exception. "Body Mass Index" appears 0 times.
- [x] **Medical framing stated directly**: "FitXpress is not a medical device." (x2). No "positioned as".
- [x] Links sit on meaningful anchor phrases; 0 bare URLs. No third-party citations at all, so no vendor-blog risk.
- [x] **Detector actually run** on `final.md`:
      `python3 brand-assets/style-guides/scripts/detect-ai-tells.py workspace/seo/articles/2026-08-31-ai-body-data-wellness-platforms-hub/final.md --channel article --summary`
      Actual output: **3,682 words · ai_density_per_1000_words 0.0 (budget 6.0) · severity low · hard_fails [] · house_rule_violations [] · em_dashes 0 · rhythm variation 0.51 (want >0.35) · punch_triads 0 · title_case_headings 0 · VERDICT CLEAN**. First run before editing was 0.55 with 1 hard fail.
- [ ] **Images / alt text: not produced.** Suggestions below; needs design.

**SEO checklist: 14/15.** The open item is images.

## Content strategy checklist

- [x] Correct hub: Wellness Platforms (Hub #8), main hub row from `content-plan.md`
- [x] Action type honored: `create-net-new`, and it is genuinely net-new (no broad Wellness Platforms page exists)
- [x] Does not duplicate `existing_urls`. Wellness Rewards keeps rewards verification and is linked as the deeper source; Beyond BMI keeps the BMI argument and is summarized in three sentences then linked.
- [x] Cannibalization guardrail held: wellness kept soft. No clinical, clearance, diagnostic or decisioning framing anywhere. No vendor comparison table (reserved for the P1 listicle). Named vendors: 0.
- [x] Vertical boundary held. Fitness product strategy stays with Hub #4 and is linked sideways; GLP-1 and insurance are not annexed. Wellness is not a sensitive vertical, so no heavy clinical scope note, but a soft scope note sits at the end of H2.2.
- [x] Internal links in all four directions: **up** ai-body-data-health-hub · **sideways** wellness-rewards-verification, beyond-bmi-business, ai-in-fitness-industry, how-to-measure-body-composition · **down** fitxpress/for-connected-and-digital-fitness · **trust** mobile-body-scanning-accuracy. 9 links, 7 distinct targets, all canonical trailing-slash form.
- [x] FAQ section present: 7 questions, answers 2 to 5 sentences, GEO/AEO shaped. Includes "Is body data used to make decisions about members, rewards, or eligibility?" and "What does FitXpress not do?"
- [x] "What FitXpress does not do" present as its own block in H2.8, five boundaries, written alongside the capability instead of as a footer
- [x] No unsupported medical, legal, underwriting or employment claims. HIPAA and GDPR stated only as posture (FX-014). SOC 2 not mentioned, because it is not certified.
- [x] Owns one distinct search intent: "what should a wellness platform do with body data, and what changes if it does"

**Strategy checklist: 10/10.**

## CMS tasks that ship with this article

These are publish-step tasks, not writing tasks. The first one is what makes the page rankable.

### 1. Inbound internal-link pass (required)

The backlink export (`workspace/research/backlinks/`, 2026-08-31) shows this hub inherits no
external authority: Beyond BMI has 1 backlink and Wellness Rewards has 0, absent from all 14,680
rows. Health is the smallest segment at 1,005 backlinks, and four URLs hold about 92% of it. So
the page has to be powered by internal links from those four.

| Donor page | Backlinks | Anchor context to add |
|---|---|---|
| `/content-hub/ai-in-fitness-industry/` | 326 | Where it separates training outcomes from wellbeing and corporate wellness programs |
| `/content-hub/the-potential-of-ai-in-telehealth/` | 263 | Where it covers remote capture outside clinical care |
| `/content-hub/glp-1-market/` | 183 | Where it discusses progress tracking beyond weight for non-clinical programs |
| `/content-hub/top-fitness-industry-trends/` | 36 | Corporate and employee wellness trend mentions |
| `/content-hub/weight-loss-industry-overview/` | 33 | Employer and insurer wellness program mentions |

Three of the five (fitness, telehealth, GLP-1) were refreshed in the last five weeks, so their
internal-link sections are current and cheap to amend. All links must use canonical
trailing-slash URLs: the export shows `?ref=` and non-slash variants in circulation.

### 2. Architecture re-parenting (approved at checkpoint 1)

`wellness-rewards-verification-employers-insurers-using-ai-3d-body-scanning/` stops being the
Wellness hub and becomes the employer/insurer sub-hub under this page. Required:

- Update `brand-assets/content-strategy/published-articles-inventory.md`: Hub #8 row, the Wellness section, and the Internal Linking Map, which currently draws Wellness Rewards as the hub node.
- Internal-link pass on the Wellness Rewards page itself so it points up to this hub.

### 3. Privacy FAQ dependency (2 placeholders in the text)

The Data, Privacy, Security & Regulatory FAQ is still an unpublished P0, so **short inline
answers were written instead of links**. Two `<!-- TODO(publish) -->` markers sit in the source,
in H2.9 and in FAQ Q5. Nothing is broken if the article ships as is. When the FAQ publishes, both
markers become links and the inline answers can shorten.

## Alt options

### Meta title variants
1. AI Body Data for Corporate Wellness Platforms | 3DLOOK (54 chars). **Recommended**: mirrors the H1 while carrying the head term
2. Corporate Wellness Platforms and AI Body Data | 3DLOOK (54 chars). Keyword at position 1, strongest for SEO, reads less like the H1
3. Body Data for Corporate Wellness Platforms | 3DLOOK (51 chars). Shortest, drops the "AI" association (`ai body`, 400/mo, KD 8)

### Meta description variants
1. How a corporate wellness platform can use measured body data for progress tracking, personalization, and member engagement, and what to ask a provider. (151 chars). **Recommended**
2. Measured body data gives wellness programs a progress signal the scale misses. What it improves, what it does not do, and how to evaluate a provider. (149 chars). More distinctive hook, no exact-match keyword
3. A guide for wellness platforms on using body measurement data for engagement and personalization, including what to evaluate before choosing a provider. (152 chars)

## Image / alt text suggestions

Not produced; these need design.

1. **Hero.** Baseline and follow-up 3D body models side by side with changed measurements called out. Alt: "Side-by-side 3D body model comparison showing measurement changes between two wellness check-ins."
2. **H2.4 workflow diagram.** Onboarding scan, personalization, repeat check-in, member comparison view, program record. Alt: "Wellness program workflow from baseline body scan through repeat check-ins to program reporting."
3. **H2.6.** Member-facing progress view where the scale is flat and measurements have moved. Alt: "Wellness app progress view showing waist measurement change while bodyweight stays flat."
4. **H2.9.** The evaluation criteria as a checklist card. Alt: "Evaluation checklist for wellness platforms selecting a body-data provider."

---

## Article

# AI Body Data for Wellness Platforms: Progress Tracking, Personalization, and Engagement

Most wellness programs know two things about a member's body: what the scale said and what the member typed into a form. Both signals are thin, and both age badly. Body data captured from a smartphone gives a wellness platform a third option, one that holds still enough to compare against itself three months later. What follows covers where that data fits in a program, what it improves, what it does not do, and how a corporate wellness platform should evaluate a provider.

## Wellness platforms lose members before the program works

Engagement in most wellness products peaks early and settles fast. The first weeks carry novelty. By roughly the ninety-day mark, the members who have not seen evidence that anything is changing start to drift, and drift is expensive: acquisition was paid for once, retention pays for itself every month. <!-- source: use-cases/fx-digital-fitness.md -->

The problem is rarely that nothing changed. It is that nothing visible changed.

A member who has held bodyweight steady while losing centimetres at the waist has made real progress. The scale reports failure. If the scale is the only instrument in the product, the program tells that member a discouraging and inaccurate story, and the member believes it.

Self-reported check-ins have a second failure mode. People estimate, round, and forget. A wellness platform building cohort reporting on self-reported numbers is building on data it cannot reproduce, which matters most at exactly the moment it matters most: when an employer, an insurer, or a board asks what the program actually delivered.

Personalization has a similar ceiling. In most wellness apps it means an onboarding survey, a stated goal, and a content track selected from three. That is segmentation by intention. It says nothing about where a member is starting from physically, and it does not update as they change.

None of this is a technology gap in the usual sense. Wellness platforms have solid engineering, good design, and often better content than the market gives them credit for. What they lack is a measured, repeatable input about the member's body that can be captured remotely, at scale, without a clinic visit or a device in the post.

## What body data means for a wellness platform

Body data, in this context, means a set of body measurements and body composition values captured remotely and consistently enough that two captures taken months apart can be compared.

A single scan from two smartphone photos, front and side, returns results in under 45 seconds. <!-- claim: FX-006 --> <!-- claim: FX-007 --> The output includes more than 80 body measurements <!-- claim: FX-008 --> along with body composition values: BMI, basal metabolic rate (BMR), body fat percentage, lean mass, fat mass, essential fat, and beneficial fat. <!-- claim: FX-009 --> A 3D body model is generated alongside the numbers, which is what allows a side-by-side visual comparison later.

The important word is comparable. A measurement is only useful for progress tracking if the same body, measured again under the same protocol, returns close to the same number. That property is repeatability, and it is separate from accuracy. A great deal of wellness measurement fails on repeatability while passing on accuracy, which produces a progress chart that moves for reasons the member did not cause.

Weight and BMI are coarse instruments. They compress a body into one or two numbers and discard the distribution. Two members with identical BMI can have materially different measurements, and a member's BMI can sit flat through a period of genuine change. The argument for looking past that single number is made in more depth in [Beyond BMI](https://3dlook.ai/content-hub/beyond-bmi-business/).

One boundary belongs at the front. Body data of this kind is an input to a wellness program. It is not an assessment of a person's health. The outputs describe measurements, and clinical interpretation stays outside the product.

## Why this matters now for wellness platforms

Four conditions changed at roughly the same time.

Workforces distributed. Corporate wellness was built around events: the biometric screening day, the onsite health fair, the clinic in the lobby. A hybrid or fully remote population makes that model expensive and patchy, and the members who most need the program are often the least likely to travel to it.

Budgets came under review. Wellness spend that once passed on goodwill is now asked to produce evidence, and self-reported participation data does not survive that question well. Programs need records they can stand behind when finance asks what changed.

Capture stopped requiring hardware. Body composition measurement used to mean a facility, a device, and a trained operator. Smartphone-based capture removed that constraint, which moved body data from something a program schedules to something a program can offer continuously.

The last change came from members themselves. People who track sleep, steps, and heart rate on a wrist expect more from a workplace wellness app than a number typed into a text field.

## Where body data fits in a wellness program workflow

The workflow is short, which is the point.

A member scans at onboarding, producing a baseline. The program uses that baseline to set targets and select content. The member scans again at intervals the program defines, with four to twelve weeks a practical range. Each new scan produces a comparison against the baseline and against the previous capture, and that comparison is what the member sees. Every capture is a timestamped, structured record, which is what the program later reports on.

Division of labour matters here, because getting it wrong is how these integrations become expensive. The wellness platform owns the program logic, the member relationship, the content, the incentives, and the interpretation. The body-data layer owns capture, measurement extraction, and the comparable record. It has no view on what a given member should do next, and it should not be asked for one.

Coaches and program administrators stay in the loop throughout. Where a program includes human coaching, the scan gives the coach a starting point and a change record to work from, which is a better conversation than asking a member how they think it is going. Where the program is fully automated, the scan feeds content selection and progress display, and any judgement about a member remains with a person.

Cadence deserves more thought than it usually gets. Scanning weekly produces a chart dominated by normal daily variation in the body, which is discouraging and slightly misleading. Scanning twice a year produces a record too sparse for a member to feel. The right interval depends on the program's own pace and on how much change the population is likely to show, and it is worth setting deliberately instead of defaulting to whatever the product already does with weigh-ins.

## Personalization: from stated goals to measured starting points

A wellness coach app that knows a member's goal knows their intention. A program that also knows their starting measurements can do several things a survey cannot support.

Targets become specific to the member instead of generic to the cohort. Content can be selected against where someone actually is, not only where they said they want to be. Cohort reporting can group members by measured starting point, which produces far more meaningful comparisons than grouping by self-declared goal, since two members with the same stated goal may be starting from very different places.

The second scan is where this stops being a data-capture feature. A baseline personalizes a program once. A repeated body record personalizes it continuously, because the program can see which direction things moved and adjust. That is the difference between a wellness tracker app that captures data and one that uses it.

Body data personalizes around a program. It does not design the program. A scan says nothing about a member's motivation, schedule, injury history, food environment, or preferences, and every one of those has more influence on outcomes than a waist measurement. Treating a scan as sufficient input for personalization produces a product that feels precise and lands wrong.

Nutrition and lifestyle coaching platforms use this input differently again, with body composition informing intake planning across longer horizons. That case is close enough to wellness to share the capture layer and different enough to deserve its own treatment.

## Progress visibility: what changes when members can see change

This is the mechanism that makes body data worth integrating into a wellness app, and it is simpler than it sounds.

A member who has been consistent for eight weeks opens the app. Instead of a weight number that has barely moved, they see their current 3D model beside the one from their baseline, with the measurements that changed listed next to it. Waist measurement down. Chest and shoulders holding. The story the product tells is now accurate, and accurate is more motivating than optimistic.

Repeatability is the property that determines whether this works at all. If scan-to-scan noise is larger than the change a member produced in eight weeks, the comparison invents movement that did not happen, or hides movement that did. In internal validation against expert manual measurement, variance across repeated scans is typically under 1 centimetre, with overall repeatability consistency above 95 percent. <!-- claim: FX-003 --> <!-- claim: FX-004 --> Those figures come from internal testing, with detailed methodology available under a non-disclosure agreement. Girth measurements vary by site: chest at 0.60 cm and waist at 0.89 cm behave differently from the extremities, where variance is smaller. <!-- claim: FX-016 -->

Which numbers to show a member is a product decision with real consequences. Showing everything produces a dashboard that reads as clinical and invites interpretation the program cannot support. A defensible default is to surface the small number of measurements tied to the member's own goal, keep the visual comparison prominent, and hold the full measurement set server-side for program reporting. Body fat percentage in particular deserves care in a wellness setting: it is a useful trend line and a poor headline number.

The limit here is real. Progress visibility supports engagement. It does not by itself retain anyone, and a program with weak content and a good progress screen is still a program with weak content. What the visual comparison changes is the failure mode where a member quits while succeeding.

## Employer and insurer wellness programs: participation, rewards, and reporting

A corporate wellness platform serving employers and insurers has the same capture problem with different stakes attached.

Participation drives everything, and participation in a distributed workforce is limited by how easy the check-in is. A remote capture that takes a minute on a member's own phone reaches populations that an onsite screening event never will, which changes the administrative economics of running the program at all. Verification that once required scheduling, staffing, and physical space becomes an in-app step.

Consistency matters more here than in a consumer wellness app, because incentives are attached. When an employee wellness program rewards a milestone, the fairness of that reward depends on every participant being measured the same way. Standardized remote capture produces timestamped, structured records that are consistent across a distributed population, which supports the review and reporting that wellness program software has to produce at plan-year end. Where a self-reported figure and a captured measurement disagree, the record supports a person looking at the case. The scan does not determine the reward. Eligibility, incentive tiers, and payment decisions sit with the program administrator, exactly where the program's own rules put them.

Rewards verification is a deeper topic than one section can carry, including dispute handling, incentive design, and audit trails for employers and insurers. It is covered in full in [wellness rewards verification for employers and insurers](https://3dlook.ai/content-hub/wellness-rewards-verification-employers-insurers-using-ai-3d-body-scanning/).

On procurement: FitXpress maintains Health Insurance Portability and Accountability Act (HIPAA) compliance in US healthcare contexts and follows General Data Protection Regulation (GDPR) principles for European processing. <!-- claim: FX-014 -->

## Where FitXpress fits, and what it does not do

FitXpress is the capture and structured-data layer inside a wellness platform's own product. Two photos in, more than 80 measurements and a body composition set out, in under 45 seconds. <!-- claim: FX-006 --> <!-- claim: FX-007 --> <!-- claim: FX-008 --> <!-- claim: FX-009 --> The platform keeps the member experience: onboarding, consent wording, the scan entry point, result display, and which metrics appear at all. Integration is through an application programming interface (API) or a camera software development kit (SDK), with the guided-capture layer supplied because capture quality is the largest single factor in what the measurements are worth.

The underlying model was trained on more than nine years of collected data, including over 150,000 photographs, more than 30,000 3D scans, and over 430,000 individual measurements. <!-- claim: FX-010 --> Coverage spans ages 16 to 78, weights from 38 to 210 kg, and heights from 150 to 205 cm, with a near-even split between male and female subjects, collected across the US and Europe. <!-- claim: FX-011 --> Population coverage is a fair question to ask any provider, because a model's behaviour at the edges of its training distribution is where wellness populations often sit.

What FitXpress does not do, stated plainly:

- It does not diagnose conditions or screen for them. FitXpress is not a medical device.
- It does not decide rewards, eligibility, incentive tiers, or program access. Those decisions stay with the program.
- It does not replace a clinician, a dual-energy X-ray absorptiometry (DEXA) scan, a bioelectrical impedance analysis (BIA) device, or a calibrated scale. Different reference methods answer different questions.
- It does not detect fraud. Consistent captured records support human review of a discrepancy.
- It does not make a wellness program compliant. It supports workflows that a compliant program defines.

Every one of those boundaries is load-bearing for a wellness product. A program that markets a body scan as a health check has changed what it is selling and taken on obligations it probably has not planned for.

Teams who want to see what the capture flow and output look like inside a live member-facing product can start with [FitXpress for connected and digital fitness](https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/).

## What a corporate wellness platform should evaluate in a body-data provider

Accuracy is the question everyone opens with and the least useful one asked in the abstract.

The better question is accuracy for which decision, measured against which reference method, under which capture protocol, for which population, and at what tolerance. A 2-centimetre waist tolerance is irrelevant for a wellness progress chart and unacceptable for garment fit. A provider who answers "accurate" with a single percentage has answered a different question. The full framework for asking this properly, including how internal benchmarks differ from standards-body benchmarks, is set out in the [body scanning accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/). For reference, internal validation against expert manual measurement puts overall accuracy at 96 to 97 percent with typical absolute error between 1.5 and 2.0 cm. <!-- claim: FX-001 --> <!-- claim: FX-002 -->

For a wellness platform specifically, repeatability outranks accuracy. Progress tracking compares a member to their own earlier scan, not to a reference standard, which means run-to-run consistency determines whether the feature works. Ask for repeatability figures separately and treat a provider who conflates the two as having answered neither.

Capture reliability across a real population is the next filter, and it is where integrations quietly fail. Phones vary, lighting varies, clothing varies, and members do not read instructions. Ask what happens with oversized clothing, what pose validation runs at capture time, what the retake rate looks like, and whether guided capture is available or whether the platform is expected to build it.

Privacy belongs in the evaluation at the same weight as the measurement questions. Establish what is stored and for how long, whether source photographs are retained or discarded, where processing happens geographically, how a member deletion request propagates, and what the HIPAA and GDPR posture actually is in writing. Face obfuscation at capture is worth asking about specifically for a wellness population. <!-- TODO(publish): link to the Data, Privacy, Security & Regulatory FAQ once it is published -->

Integration effort is the last filter. The question that matters is how long until a member can complete a check-in inside the existing product and see a comparison, which is a considerably longer project than calling the API.

## Adding body scanning to a wellness product

A sensible sequence starts narrow. Run a pilot cohort of members who already engage, add the capture flow to the existing app, ship the progress comparison view, then connect reporting, then widen.

The platform team owns onboarding, consent, the entry point, error handling, and every pixel of the result display, including which metrics are shown to members and which stay server-side. The provider supplies capture, measurement extraction, and the record. Attempting to build the capture layer independently is the most common way to end up with disappointing measurements, because guided capture with pose validation is what protects the numbers.

Capture quality is won or lost in the first ten seconds of the member's experience. Clear instructions, a guided pose, honest feedback when a capture is unusable, and a low-friction retake path account for most of the difference between a clean measurement set and a noisy one.

Worth instrumenting from the first pilot: check-in completion rate, the proportion of members who scan a second time, retake rate at capture, and whether members can explain what their progress view is telling them. That last one is qualitative and the most informative, since a progress screen a member cannot interpret produces no engagement regardless of how good the underlying data is.


## Frequently asked questions

**What is AI body data, and what does a wellness platform get from it?**
AI body data is a set of body measurements and body composition values derived from smartphone photographs using computer vision. For a wellness platform it provides a measured baseline at onboarding and a comparable record at every later check-in. That supports progress display, content personalization, and program reporting without a clinic visit or dedicated hardware. In practice it means body composition tracking on the program's own schedule, repeated remotely as often as the program needs.

**How does a remote body scan work for a wellness check-in?**
A member takes two photographs, front and side, fully clothed, using their own phone. Guided capture validates pose before the images are submitted. Results return in under 45 seconds, including more than 80 measurements, body composition values, and a 3D model that can be compared against previous captures. <!-- claim: FX-006 --> <!-- claim: FX-007 --> <!-- claim: FX-008 -->

**Can a body scan replace a DEXA scan, a BIA device, or a calibrated scale?**
No. These methods use different references and answer different questions, and a mobile scan does not replace any of them. Its value in a wellness program is frequency and consistency: it can be repeated remotely as often as the program needs, which supports comparison over time. Choosing between methods is covered in the accuracy framework.

**Is body data used to make decisions about members, rewards, or eligibility?**
No. The scan produces a measurement record. Decisions about rewards, incentive tiers, program access, or eligibility are made by the program according to its own rules, and a human administrator stays responsible for them. Structured records support that review; they do not perform it.

**What data is captured and stored, and what happens to the photos?**
Capture requires two photographs, which are processed to produce measurements, body composition values, and a 3D model. Faces are obfuscated automatically during capture. Retention periods, storage geography, and deletion handling are configurable and should be confirmed in writing during procurement, along with HIPAA and GDPR posture. <!-- claim: FX-014 --> <!-- TODO(publish): link to the Data, Privacy, Security & Regulatory FAQ once it is published -->

**How often should a wellness program run check-in scans?**
A practical range is four to twelve weeks. Weekly captures are dominated by normal daily variation in the body and tend to discourage members. Intervals longer than a quarter leave too little record for anyone to feel progress. The right cadence depends on the program's pace and the amount of change the population is likely to show.

**What does FitXpress not do?**
FitXpress is not a medical device. It does not diagnose or screen for conditions. Decisions about rewards and eligibility stay with the program. Reference methods such as a DEXA scan, a BIA device, or a calibrated scale remain the standard for the questions they answer. What FitXpress provides is structured, timestamped body measurement records that a wellness program uses inside its own workflow.

## Where to go next

Teams at a corporate wellness platform evaluating whether measured body data belongs in the product usually want one of three things next.

For teams comparing approaches to remote progress tracking, the [FitXpress product page](https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/) sets out integration options and the shape of the returned data.

For employers and insurers whose immediate question is rewards verification, the [wellness rewards verification](https://3dlook.ai/content-hub/wellness-rewards-verification-employers-insurers-using-ai-3d-body-scanning/) use case is the closer fit.

For a broader view of how body data is applied across health programs, the [AI body data hub](https://3dlook.ai/content-hub/ai-body-data-health-hub/) maps the verticals, and [AI in fitness](https://3dlook.ai/content-hub/ai-in-fitness-industry/) covers the training and coaching side of the same capture layer. Teams weighing measurement methods against each other can start with [how to measure body composition](https://3dlook.ai/content-hub/how-to-measure-body-composition/).
