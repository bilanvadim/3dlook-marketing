---
title: "AI in Fitness: Structured Body Data for Progress Tracking"
description: "Structured body data underpins AI in fitness. See how mobile body scanning supports progress tracking, personalization, and digital coaching for fitness apps."
hub: fitness
cluster: body-data-progress-tracking
product: fitxpress
status: draft
last_revised: 2026-07-22
action_type: refresh-existing
priority: P0
author: Assel Sekerova
replaces_url: https://3dlook.ai/content-hub/ai-in-fitness-industry/
---

# AI in Fitness: How Structured Body Data Powers Progress Tracking, Personalization, and Digital Coaching

**Scope note:** This hub covers AI applications inside fitness apps, digital coaching platforms, and body-transformation programs. Body data also supports clinical weight-loss programs, telehealth, and insurance workflows; those use cases are covered in their respective hubs, not here.

## Fitness apps have solved tracking. Body change is a harder problem.

Fitness apps have gotten good at counting steps, logging workouts, and monitoring heart rate. Most still struggle to answer a simpler question a subscriber is quietly asking every few weeks: is my body actually changing?

Weight alone is a noisy way to answer it. It moves with hydration, meal timing, and hormonal cycles, so a user who loses fat and gains muscle in the same month can watch the scale barely shift. That mismatch between real physical change and what a tracker shows is one of several factors app teams point to when they explain early cancellations.

### What "AI in fitness" means

AI in fitness refers to the use of machine learning, computer vision, and related technologies to analyze fitness data, personalize digital experiences, monitor progress, and support coaching or workout decisions. In practice, it spans four functional categories that fitness products combine in different ways:

* **Workout personalization:** adapting programs from goals, activity, and performance data
* **Motion and form analysis:** computer vision that reads exercise technique from a camera
* **Wearable and recovery analytics:** physiological signals like heart-rate variability and sleep
* **Structured body data:** measurements, body-composition estimates, and 3D models captured from photos or scans

The first three categories are well established in consumer fitness. The fourth, structured body data, is the layer most fitness products still lack, and it is the layer that the rest of this page focuses on.

## Why AI in fitness matters now

The fitness app market is a large and growing target for this kind of capability. Global fitness-app revenue was estimated at roughly $12.1 billion in 2025 and is projected to reach approximately $33.6 billion by 2033, a compound annual growth rate of about 13% ([Grand View Research](https://www.grandviewresearch.com/industry-analysis/fitness-app-market)). Growth at that scale is happening alongside a persistent retention problem: industry benchmarking shows most fitness apps retain only a low single-digit share of users by day 30, with even top-performing apps in the category reaching roughly a quarter of installs still active a month in ([Business of Apps, Health & Fitness App Benchmarks](https://www.businessofapps.com/data/health-fitness-app-benchmarks/)). Separate research into health-app usage patterns has found that roughly seven in ten users stop using a fitness app within the first three months, with lack of personalization and difficulty judging whether progress is happening cited among the leading reasons ([Sahha](https://sahha.ai/blog/health-app-churn-retention/)).

For subscription fitness products, priced commonly in the $10 to $40 per month range ([My PT Hub](https://www.mypthub.net/blog/fitness-coaching-app-pricing-compared/)), early cancellation has an outsized effect on unit economics: acquisition costs typically take several months of active subscription to recover, so the first few months determine whether a user is profitable at all.

Three shifts explain why AI, and structured body data specifically, are becoming more relevant to that retention problem:

* **Smartphone cameras are capable enough.** The same device that logs a workout can now capture structured body measurements from two photos, processed through computer vision models trained on large sets of scans and manual measurements.
* **User expectations have moved.** Consumers accustomed to personalized recommendations from other consumer apps increasingly expect fitness products to adapt to them individually rather than assign a generic plan.
* **Retention economics reward visible progress.** In subscription fitness, giving users a way to see change that a scale cannot show creates opportunities for recurring progress check-ins that support continued engagement, though it is not a guaranteed fix for churn on its own.

## AI fitness capability landscape

The table below groups the main AI-enabled capabilities used across fitness products today. Categories are complementary rather than competing: most mature fitness platforms combine two or more of them, and a platform that only uses one category typically has a corresponding gap in what it can measure or personalize.

| AI fitness capability | Typical data input | Primary application | Main limitation |
|---|---|---|---|
| Workout personalization | Goals, activity, and performance data | Program recommendations and adaptation | Quality depends on the breadth and reliability of user data |
| Motion analysis | Camera-based movement data | Form feedback and repetition tracking | Captures movement rather than longitudinal body change |
| Wearable analytics | Activity and physiological signals | Readiness, recovery, and training-load insights | Does not provide full-body measurements |
| Nutrition support | Food logs, goals, and behavioral data | Meal tracking and nutrition guidance | User-entered data may be incomplete or inconsistent |
| Mobile body scanning | Smartphone images and user inputs | Measurements, estimated composition, and progress tracking | Requires guided capture and consistent conditions |

Illustrative examples exist in each category today, though this is not an exhaustive list and inclusion does not imply endorsement or a product integration:

* **Workout personalization:** platforms such as Spurfit analyze goals, activity history, and workout preferences to rebalance a training program over time.
* **Motion analysis:** [Kemtai](https://kemtai.com/) and [asensei](https://asensei.ai/) use computer-vision motion tracking, delivered through a webcam or smartphone camera, to give real-time feedback on exercise form and repetition counts.
* **Wearable analytics:** devices such as Whoop interpret heart-rate variability, sleep, and recovery signals into training-readiness guidance, without capturing body measurements.
* **Nutrition support:** apps such as FitGenie generate macro and meal targets from goals and logged food data.
* **Mobile body scanning:** solutions such as FitXpress capture body measurements, estimated composition, and a 3D model from two smartphone photos.

## Structured body data: the foundation layer

Most fitness apps already collect three kinds of data: activity (steps, workout minutes, calories), biometric snapshots (weight, heart rate), and self-reported inputs (goals, preferences). What is usually missing is structured body data: measurements, shape, and estimated composition, tracked as they change over weeks and months.

A smart scale gives one number, weight, sometimes paired with a body-fat estimate from bioelectrical impedance that varies with hydration. Neither a scale nor a wearable captures how a user's body dimensions are changing in specific regions, such as the waist, chest, arms, or thighs. Mobile body scanning fills that gap. From two smartphone photos, a fitness app can receive:

* 80+ body measurements (circumferences, lengths, widths, heights)
* Body-composition estimates (body fat percentage, lean mass, fat mass)
* Calculated metrics such as Body Mass Index (BMI) and Basal Metabolic Rate (BMR)
* A 3D body model for visual comparison across scans
* Posture and proportion data as an input for personalization

This data layer gives a fitness product something a step counter or a scale cannot: a record of changes in body dimensions and estimated composition over time, alongside a visual 3D comparison. Establishing whether a given change came from fat loss, muscle gain, hydration, posture, or another factor still depends on trends, context, and, where a coach is involved, professional judgment.

The table below places mobile body scanning alongside the other common ways fitness products currently capture body-related data, to show where each fits and where each is limited.

| Data source | What it captures | Best suited to | Main limitation |
|---|---|---|---|
| Wearables | Activity, recovery, and physiological signals | Training readiness and daily monitoring | Does not capture full-body dimensions |
| Smart scales | Weight and estimated composition | Frequent home check-ins | Estimates may vary with hydration and measurement conditions |
| Motion tracking | Exercise movement and form | Real-time workout feedback | Does not track body dimensions |
| Mobile body scanning | Measurements, estimated composition, and 3D body data | Remote longitudinal progress tracking | Requires standardized capture |
| Dual-energy X-ray absorptiometry (DEXA) | Imaging-based composition and bone data | Periodic reference assessment | Facility-based and unsuitable for frequent remote use |

For a closer look at how two-photo capture compares with video-based and hardware-based methods, see [Body Scanning Technology: 2-Photo vs Video vs Hardware](https://3dlook.ai/content-hub/body-scanning-technology-comparison/). For how the capture and measurement pipeline works end to end, see [AI-powered body scanning for fitness](https://3dlook.ai/content-hub/ai-body-scanning-for-fitness/).

## Progress tracking: scan-to-scan comparison

Weight is a composite number. It combines fat, muscle, bone, water, and waste, so two people at the same weight can have very different body compositions, and one person can gain weight while getting leaner or lose weight while getting weaker. Treating weight change as the primary progress signal tends to work for the first few weeks of a calorie deficit and becomes less informative once body recomposition begins.

Scan-to-scan comparison is designed to show what changed, not just whether a single number moved:

* Circumference changes by body region: waist, hips, chest, arms, and thighs tracked independently
* Body-fat percentage trend over multiple scans, rather than a single-point estimate
* 3D overlay comparison showing where body volume shifted between two scans
* Measurements plotted across weeks and months, smoothing out daily fluctuations

For fitness apps, this gives the progress tab a way to show body change directly rather than relying on weight alone, which can give users additional ways to assess progress during periods when the scale does not move. For digital coaching platforms, structured measurements give coaches a consistent input for program review, distinct from a client's self-reported sense of progress and less invasive than requiring in-person measurement.

The underlying technology is mobile body scanning: a user takes two photos with a smartphone, and computer vision models reconstruct a 3D body model with measurements. Scan-to-scan repeatability of under 1 cm means the system can detect genuine change without being thrown off by ordinary measurement noise, which matters for tracking gradual recomposition across weeks. For the full accuracy and repeatability framework, including how it varies by use case and capture condition, see [Body Scanning Accuracy: A Framework for Enterprise Decisions](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/).

## Personalization: body data as additional context

Most fitness-app personalization today relies on self-reported inputs: age, weight, stated goals, and preferences. That produces a plan fit to a demographic profile rather than an individual body.

Structured body data adds a different kind of input, though it works alongside other inputs rather than replacing them:

* **Body shape and proportions** can inform how an exercise is cued or modified. A user with different limb-to-torso proportions may need a different setup for the same movement pattern. Body measurements and estimated composition can provide additional context alongside goals, mobility, fitness level, performance, recovery, and professional judgment; they are not, on their own, a basis for prescribing or ruling out specific exercises.
* **Body-composition trends over time** give a program a second signal beyond weight. A change in estimated lean mass, for example, may prompt a coach to review nutrition, training load, recovery, and measurement conditions before deciding whether to adjust the program. Confirming whether a calorie deficit is too aggressive or protein intake is insufficient still requires weighing that broader picture, rather than reading the lean-mass number alone.
* **Regional measurement changes** can surface changes in waist, chest, arm, or thigh circumference that a single weight reading would report as no change. Whether that regional change reflects the intended training effect is something a program, a coach, or the user still needs to interpret.

Fitness apps that use body data this way are adding a measurement layer to their existing personalization inputs, not replacing goals, mobility assessments, and professional judgment with a body scan.

## Digital coaching: virtual trainers and human coaches

Digital coaching generally falls into two categories: AI-driven virtual trainers that give automated feedback, and human coaches who work with clients remotely through a platform. Structured body data is relevant to both, in different ways, and the two should not be conflated.

**AI virtual trainers** use computer vision to analyze exercise form in real time, reading joint angles and movement patterns against a reference model. Platforms such as Kemtai and asensei already do this today using a webcam or smartphone camera, independent of any body-scanning product. Combining that kind of motion analysis with a user's body measurements, so that a reference model accounts for individual proportions, is a plausible way the two data types could complement each other; it is not a documented FitXpress integration with a named motion-tracking platform today, and should be read as an illustration rather than a current capability.

**Human coaches on digital platforms** face a different constraint: they cannot physically measure a remote client. Progress assessment typically relies on self-reports, progress photos, and scale weight, all of which vary in reliability. A coach managing a large remote caseload has limited ability to confirm whether a reported measurement change reflects the body or the way it was measured.

Structured body data from a mobile scan gives remote coaches a more standardized input. Guided capture, pose validation, and consistent anatomical landmarks help standardize measurement collection across remote settings, though clothing, pose, and camera positioning still affect results, which is why capture guidance matters. For platforms that employ coaches, this generally means:

* Coaches can review more clients' data without collecting measurements themselves
* Program-adjustment discussions can reference a measurement trend rather than a client's recollection
* A scan creates a timestamped record that supports accountability between check-ins

For a closer look at how this fits into a connected or digital fitness product, see [FitXpress for connected and digital fitness](https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/).

## Bias and accessibility considerations

AI-driven capture and analysis do not automatically make a fitness product more accessible or less biased; that depends on how the underlying system was built and validated. Before adopting any AI-based measurement or coaching tool, fitness businesses should assess:

* Whether the validation data represents the intended user population, across body types, ages, and skin tones
* Whether capture guidance works across different body types and mobility levels, including users who cannot stand in a specific pose unassisted
* Device and camera requirements, and whether they exclude users with older or lower-end smartphones
* Clothing and pose requirements, and how clearly these are communicated before capture
* Language and instruction accessibility for the markets the product serves
* Whether an alternative workflow exists for users who cannot complete the standard capture process

FitXpress's guided capture and pose-validation steps are designed to support consistent measurement collection across a range of users; broader questions about population coverage, device support, and alternative workflows for a specific deployment should be confirmed directly rather than assumed. For data handling and regulatory detail, see the [FitXpress privacy documentation](https://3dlook.ai/fitxpress-privacy-policy/).

## Implementation and evaluation considerations for fitness companies

Adding an AI-driven body-data capability to a fitness product involves product, privacy, and user-experience decisions that are largely the same regardless of vendor.

**Integration approach.** Body-data capture is typically delivered through an application programming interface (API) or software development kit (SDK), so the fitness company controls where and how it appears: at onboarding as a baseline, on a recurring schedule, or on demand. It tends to work better designed as a native part of the product experience than as a separate, disconnected step.

**User adoption.** Two photos and a fast result are only part of adoption. Products that show users their measurements, 3D model, or composition dashboard immediately after a scan tend to see users complete the capture step; when a scan feels like a data-collection exercise for the company rather than something the user gets value from, completion tends to suffer.

**Privacy communication.** Users commonly ask what happens to their photos and who sees their data. Clear, visible answers at the point of capture reduce drop-off, and should route to a full privacy policy rather than being handled ad hoc.

**Coach workflow integration.** For platforms with human coaches, structured body data shifts coach time from collecting measurements to reviewing them. Platforms should plan who reviews scan data, how often, and what triggers a program-adjustment conversation.

**Measurement cadence.** The appropriate scanning cadence depends on program duration, expected rate of change, user experience, and measurement variability. A short transformation program might use more frequent checkpoints than a year-round fitness app; neither is a universal best practice, and cadence should be set against the specific program rather than a fixed rule.

Beyond integration mechanics, fitness businesses evaluating any AI-driven body-data or fitness-AI tool should weigh:

* Relevance of the outputs to the intended fitness workflow
* Measurement accuracy and repeatability, and how each is defined and tested
* Performance under real-world capture conditions, not only controlled demos
* Integration options and the implementation effort they require
* User guidance and the scan- or capture-completion experience
* Privacy, data retention, and consent configuration
* Accessibility across body types, devices, and user environments
* Whether accuracy, repeatability, or outcome claims are backed by stated validation evidence

## Who can use structured body data in fitness?

Structured body data is relevant to several kinds of fitness products, each with a different workflow:

* **Digital fitness and workout apps** typically add a recurring scan checkpoint, for example monthly, so users can see a 3D comparison and composition trend alongside their workout log instead of relying on the scale alone.
* **Remote coaching platforms** commonly use a scan at client onboarding to establish a baseline, then schedule periodic rescans so the coach can review measurement trends between sessions.
* **Connected fitness products** (equipment paired with a companion app) can embed scanning into the companion app so equipment users get a body-composition view alongside their workout metrics, in addition to device-generated data.
* **Personal-training and transformation programs** often use a scan at the start and end of a defined program, or at set intervals through it, to give clients a visual and numerical record of change over the program length.
* **Fitness clubs offering a digital member experience** can offer scanning as a periodic member benefit, giving staff and members a shared, structured record to discuss instead of a single weight reading.

A corporate wellness platform may use structured body data in the context of a specific fitness feature, such as a step or activity challenge with a scan-based progress check-in; broader corporate wellness program design sits outside the scope of this hub.

## Where FitXpress fits

FitXpress is a mobile body-scanning solution that provides the structured body-data layer described above for fitness applications. It is not a fitness app; it is measurement infrastructure that a fitness app or platform integrates.

What it provides:

* **Capture:** two photos from a smartphone camera, processed into 80+ body measurements, estimated body-composition outputs (including body fat percentage, lean mass, and fat mass), and a 3D body model, with results available in under 45 seconds.
* **Progress tracking:** scan-to-scan comparison with measurement trends plotted over time, and 3D model overlay showing where the body changed between two scans, where this longitudinal view is enabled for the integration.
* **Integration:** supported through API and SDK options, so the fitness company retains its own user experience and embeds the capture and results flow into onboarding, check-ins, or progress tracking.
* **Accuracy and repeatability:** internal validation against expert manual measurements shows approximately 96 to 97% agreement with a typical absolute error of 1.5 to 2.0 cm, and scan-to-scan repeatability of under 1 cm. Accuracy depends on capture conditions such as lighting, clothing, and following the guided pose. For the full framework behind these figures, see [Body Scanning Accuracy: A Framework for Enterprise Decisions](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/).

For product detail, implementation options, and privacy specifics, see [FitXpress for connected and digital fitness](https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/).

## What FitXpress does not do

FitXpress is an intake and documentation layer. It:

* Provides measurements and body-composition estimates; it does not diagnose or treat medical conditions.
* Does not independently prescribe workouts or nutrition plans.
* Does not replace a coach's judgment or a reference clinical assessment method such as DEXA.

The distinction that matters: FitXpress provides the measurement data. The fitness company, coach, or user decides what to do with it. For data handling, security, and regulatory detail, see the [FitXpress privacy documentation](https://3dlook.ai/fitxpress-privacy-policy/).

## FAQ

**What is AI in fitness?**
AI in fitness refers to the use of machine learning, computer vision, and related technologies to analyze fitness data, personalize digital experiences, monitor progress, and support coaching or workout decisions. It spans virtual trainers, wearable analytics, motion tracking, nutrition support, and mobile body scanning.

**How does mobile body scanning work for fitness?**
A user takes two photos with a smartphone camera. Computer vision models trained on large sets of scans and manual measurements reconstruct a 3D body model and extract 80+ measurements along with body-composition estimates, typically in under 45 seconds. Results are available for progress tracking, personalization inputs, and coach review.

**Can AI body scanning replace a personal trainer?**
No. It provides structured measurement data that can support a trainer's assessment. The trainer interprets the data, adjusts the program, and provides guidance; the technology does not prescribe workouts, diagnose issues, or make training decisions on its own.

**What data does a mobile body scan capture?**
Typically 80+ body measurements (circumferences, lengths, widths), body-composition estimates (body fat percentage, lean mass, fat mass), calculated metrics such as BMI and BMR, and a 3D body model. Weight can also be estimated from visual data when a connected scale is not used, with a typical error of approximately 3.5%.

**How accurate is mobile body scanning compared with manual measurements?**
For FitXpress specifically, internal validation against expert manual measurements shows approximately 96 to 97% agreement with a typical absolute error of 1.5 to 2.0 cm, and scan-to-scan repeatability of under 1 cm. Accuracy depends on capture conditions such as lighting, clothing, and following the guided pose. See the [full accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) for how this varies by use case and decision tolerance.

**What does FitXpress not do?**
FitXpress does not diagnose medical conditions, prescribe workouts or nutrition plans, or replace a coach's judgment or a reference clinical method such as DEXA. It is an intake and documentation layer that provides structured measurement data for review.

**Can structured body data help with fitness-app retention?**
Body scanning can give users additional ways to see change, through 3D comparisons, measurement trends, and composition dashboards, during periods when the scale does not move, and this may help some users remain motivated. It is a product capability, not a guaranteed retention outcome, and its effect depends on how it is implemented and communicated.

**Is mobile body scanning private and secure?**
FitXpress processes photos to extract measurements, then deletes them immediately or within 30 days, with faces obfuscated at capture and no names or personal identifiers stored alongside scan data. Data is encrypted in transit and at rest. Full detail is in the [FitXpress privacy documentation](https://3dlook.ai/fitxpress-privacy-policy/).

---

Explore [FitXpress for connected and digital fitness](https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/) to see how structured body data fits into an existing fitness product.

<!--
FINAL QUALITY CHECKLIST (publisher pass, 2026-07-22)

[a] Repeated arguments eliminated — each idea (definition, landscape, foundation, progress, personalization, coaching, implementation, FitXpress) has exactly one section; "the scale doesn't tell the full story" argument appears once (intro), not repeated in every section or the FAQ. DONE.
[b] Body data reframed as the foundation layer, not a fourth equal pillar — new H1 + explicit "layer most fitness products still lack" framing + dedicated "Structured body data: the foundation layer" section that progress tracking/personalization/coaching sections explicitly build on. New title proposed. DONE.
[c] Legacy SEO coverage preserved: workout personalization, motion/form analysis, wearable/recovery analytics, digital coaching, nutrition support, mobile body scanning, privacy/responsible use, accessibility/inclusivity — all present, reorganized under the new framework. DONE.
[d] Heading/topic map against current page completed (see changelog delivered alongside this file); no topic dropped without being relocated, linked out, or intentionally cut per [h]/[s]. DONE.
[e] Contextual internal links added inline (not just footer) to: AI-powered body scanning for fitness, FitXpress for connected and digital fitness, Body Scanning Accuracy framework, Body Scanning Technology comparison, FitXpress privacy documentation. DONE.
[f] Data-source comparison table added (Wearables / Smart scales / Motion tracking / Mobile body scanning / DEXA) in "Structured body data" section — distinct from the AI-capability table. DONE.
[g] Retention/engagement claims qualified throughout (opening, "why this matters now," progress tracking, FAQ) using "can support," "additional ways to," "may help," "creates opportunities for." No absolute causal claims remain. DONE.
[h] Removed: genetic fitness recommendations (Alter.me cut entirely), injury prediction/prevention, mental-health treatment, VR, medical-condition management, broad wellness predictions, generic future-of-AI speculation. DONE.
[i] Evergreen definition added near the top, verbatim, followed immediately by the four functional categories. DONE.
[j] Every externally verifiable statistic carries a direct inline source link (Grand View Research for market size/CAGR, Business of Apps + Sahha for retention/abandonment/churn reasons, My PT Hub for subscription pricing). Unverifiable stats (adoption-growth-since-2021, fixed CAC payback window) removed rather than left unlinked. DONE.
[k] Dated company catalogue replaced with the AI fitness capability landscape table; named examples (Kemtai, asensei, Whoop, FitGenie, Spurfit, FitXpress) verified for current functionality via live search; Alter.me and Bodygee dropped (genetic scope + inaccurate "smartphone-only" fit). DONE.
[l] Agent-generated commercial phrasing removed: no "retention infrastructure," "body intelligence layer," "retention defensible," "the companies that win," "the apps that keep users are the ones that...," "changes the retention equation." Replaced with concrete capability descriptions. DONE.
[m] Tissue-change inferences removed — no "where muscle is building / fat is decreasing / shoulder gain / regional fat-loss tracking." Replaced with "changes in individual body measurements / waist, chest, arm, or thigh circumference / body dimensions and estimated composition over time." DONE.
[n] Unsupported exercise/nutrition conclusions removed from the Personalization section; body data is framed as "additional context alongside goals, mobility, fitness level, performance, recovery, and professional judgment," with the lean-mass example rewritten to avoid asserting a specific cause. DONE.
[o] Existing vs. potential integrations separated — Kemtai/asensei described as real, independent products today; combining their motion data with FitXpress body measurements is explicitly flagged as illustrative, not a documented integration. DONE.
[p] Absolute standardization claim removed ("regardless of who holds the phone...") and replaced with the specified "guided capture, pose validation, and consistent anatomical landmarks help standardize..." language, with clothing/pose/camera caveats retained. DONE.
[q] "What FitXpress does not do" reduced to the four specified points; FDA/DEXA/hiring detail moved out, replaced by a link to FitXpress privacy documentation for further detail. DONE.
[r] Bias/accessibility reframed as provider-assessment questions (population representativeness, capture guidance across body types/mobility, device/camera requirements, clothing/pose requirements, language accessibility, alternative workflows); no "AI eliminates bias" claim; only verified FitXpress-specific claim (guided capture/pose validation) stated as fact. DONE.
[s] Fitness boundary kept clean — no GLP-1 treatment, medical diagnosis, insurance, employment eligibility, clinical decision-making, or occupational health content; corporate wellness appears only tied to a specific fitness feature example, not as a use-case category. DONE.
[t] "What fitness businesses should evaluate" section added with all 8 specified criteria, framed as vendor-neutral. DONE.
[u] Scanning cadence framed as configurable ("depends on program duration, expected rate of change, user experience, and measurement variability"), with illustrative (not prescriptive) examples. DONE.
[v] Internal ICP section replaced with public-facing "Who can use structured body data in fitness?" — revenue thresholds, geography, job titles, and sales-readiness signals removed; five categories with workflow explanations (absorbing the former "how companies use FitXpress" examples). DONE.
[w] FitXpress given one focused section covering two-photo capture, <45s results, 80+ measurements, estimated composition outputs, 3D model, longitudinal visualization (flagged as integration-dependent), SDK/API integration, and approved accuracy/repeatability figures, then routes to the connected/digital fitness page; admin panel and detailed privacy architecture moved to linked pages. DONE.

Terminology/editor pass: no "objective," "reader/audience," "this article/this guide," "by hand," " plus " as connector; no em dash; DEXA and API/SDK expanded at first use (M1); two stacked-negation sentences rewritten to positive scoping (M2); no unlinked "according to Statista"-style claims; no banned AI-signature words or clichés found.

OPEN ITEMS FOR VADIM / ASSELYA:
1. New title proposed per [b] — confirm before publish, since it changes the page's existing meta title.
2. "Vadim" is a manually appended byline placeholder; frontmatter defaults to Assel Sekerova per section 15 hard requirement #3 — confirm this is not a Katerina founder-voice piece.
3. Retention/churn statistics (day-30 retention, 90-day abandonment, churn reasons) came from Business of Apps and Sahha rather than the original draft's Statista citation, because a direct, checkable Statista source for those exact figures could not be located; the market-size/CAGR figure similarly moved to Grand View Research for the same reason. Flagging in case Vadim has a licensed Statista source with matching numbers that should be used instead.
4. Bodygee and Alter.me were dropped as named examples (Bodygee's current product is iPad-plus-hardware-sensor based, not pure smartphone photos; Alter.me is a genetic-testing platform, out of scope per [h]). Confirm no commercial reason to keep either.
5. "Longitudinal visualization... where approved" and "where this longitudinal view is enabled for the integration" language in the FitXpress section is a placeholder qualifier since the brief did not specify which integrations currently ship this feature — confirm exact phrasing with product before publish.
-->
