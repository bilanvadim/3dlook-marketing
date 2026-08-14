---
product: fitxpress
market: Australia
created: 2026-08-14
status: draft
requested_count: 30
delivered_count: 26
inspiration: erakulis.com (existing customer, never a target)
---

# Outbound Hypothesis, 2026-08-14 (Australian Digital Fitness, Connected Health and AI Nutrition)

## Vertical

Australia-headquartered digital fitness, connected health and AI-nutrition companies: subscription consumer apps, connected-fitness hardware with a software layer, metabolic and longevity platforms, digital weight-management programs, B2B fitness and wellbeing software, and private wellness or insurer-run wellbeing programs.

The pattern we are copying is Erakulis (CR7 lifestyle app: AI food scanner, phone-camera BodyScan body composition, 300+ wearable integrations, AI assistant, adaptive nutrition, workout and sleep plans, one connected fitness-nutrition-wellness loop). Erakulis is an existing 3DLOOK customer, so it is the template for the search, never a target of it.

## Sub-segment

Australian-headquartered companies (registered and operationally based in Australia) that already run a recurring digital relationship with their users, and that already collect some body or activity data but have no phone-camera body-composition layer.

Three flavours inside the net:

1. **Consumer subscription apps (DTC).** Fitness, nutrition, weight-management and multi-pillar wellness apps sold to Australian consumers, where retention depends on visible physical progress.
2. **B2B health and fitness tech.** Platforms that sell to gyms, clinics, employers, insurers or elite sport, where a body-scan module becomes a feature the platform resells to its own customers.
3. **Private wellness and insurer-linked programs.** Health funds, life insurers and corporate wellbeing providers that already pay for activity data and health assessments and need a body-composition metric that is not self-reported.

## Feature screen (must match at least 2 of 4)

A company enters the list only if at least two of these four are documented on its own site, app listing, or a named public source:

| Code | Criterion | What counts as evidence |
|------|-----------|-------------------------|
| C1 | AI food scanner or photo-based meal logging | Photo or AI meal recognition in the app (plain barcode or manual logging is noted separately, it does not satisfy C1) |
| C2 | Mobile body-composition scan | Phone-camera or app-based body composition, measurements or 3D body capture |
| C3 | Wearable integrations | Named integrations (Apple Health, Apple Watch, Fitbit, Garmin, Google Fit, Strava, CGM) or a first-party wearable with its own data platform |
| C4 | Adaptive AI coaching | Plans or coaching that change based on the user's own data, or an AI coach or assistant in the product |

Companies matching exactly one criterion are kept only when they also run a documented multi-pillar loop (training plus nutrition plus recovery or clinical support in one product) or sell body-measurement technology already. Those are marked Tier B and are a build-the-case conversation, not a drop-in fit. Everything below that bar is listed in `companies.md` as excluded, with the reason.

## Company types in scope

- DTC consumer apps and celebrity or expert-led subscription programs
- Connected-fitness hardware companies with an app and a data layer
- Metabolic health, CGM and longevity platforms
- Digital weight-management and telehealth-adjacent programs that run ongoing check-ins
- B2B fitness software and member-app platforms (franchise and studio operators included when the digital layer is real)
- Corporate wellbeing platforms and insurer-run wellness programs
- Elite sport and musculoskeletal measurement companies (body-data adjacency)
- Nutrition software companies with a consumer food-logging app

## Exclusions

- **Public health entities.** Publicly funded agencies, state and federal health services, and public research bodies. CSIRO is the clearest case: the Total Wellbeing Diet is in scope only through its commercial licensee (Digital Wellness), not through CSIRO itself.
- **Gym chains with no digital layer.** A franchise or club network qualifies only if it ships its own member app with tracking or an owned digital program. Location count alone is not a qualifier.
- **Body-scanning competitors.** Advanced Health Intelligence (Perth), mPort (Sydney) and any company whose own product is body scanning or body measurement from images. Also anything they own (Wellteq, acquired by Advanced Health Intelligence in December 2022).
- **Existing 3DLOOK customers**, including Erakulis, plus everything in `marketing_vb/workspace/outbound/exclusions/global-company-registry.json`.
- **Companies already worked in prior campaigns.** The Australian telehealth campaigns (2026-07-16, 2026-07-27) already covered Medibank, Bupa Australia, HCF, Mosh, InstantScripts, Medmate, Qoctor, Hopstep and Amplar Health. Those and their subsidiaries stay out, which is why The Healthy Mummy (bought by Mosh in 2023, now trading as The Healthy Mummy by Moshy) is excluded from this list despite fitting the product profile.
- **Non-Australian headquarters.** New Zealand counts as out of scope for this campaign (Femmi, Les Mills), as does a UK or US head office on an ASX listing (Physitrack). Companies that moved their head office offshore are flagged rather than silently kept.
- **Medical-claims positioning.** Anything sold as a diagnostic or regulated device. FitXpress stays operational and non-diagnostic; Australian medical-device rules turn on the claim being made, so a candidate whose positioning is diagnostic is the wrong conversation.

## Use case (1 sentence)

FitXpress as the embedded body-composition and progress-visualisation layer for Australian fitness and health platforms: two phone photos returning 80+ measurements, body composition and a 3D progress model through an API or SDK, so an Australian app ships the body-scan feature its wearable and nutrition data already implies, without building computer vision in-house.

## Why this is plausible (3 reasons grounded in evidence)

1. **Australian platforms have already wired up the wearable and scale side of the loop, and body composition is the missing input.** Juniper (Eucalyptus) ships a Bluetooth digital scale with the first medication delivery and its app connects to Apple, Fitbit and Garmin, then asks patients to track waist measurements by hand; that is a tape measure sitting inside an otherwise fully connected product, across 100,000+ Australian women. AIA Vitality accepts data from Fitbit, Garmin, Apple Health, Google Fit, Strava, Polar, Suunto and Misfit and awards points on steps, workouts, heart rate, mindful minutes and sleep, with no body-composition signal in that set. Sources: [Eucalyptus, Juniper app connects to health and fitness devices](https://www.eucalyptus.health/blog/wearables), [AIA Vitality devices and apps](https://www.aia.com.au/en/health-and-wellbeing/aia-vitality/devices-apps-troubleshooting).

2. **Capital is going into exactly this loop in Australia right now, which means product roadmaps are open.** Everlab raised AU$65M Series A (June 2026, led by Airtree) for a preventive health platform that already integrates 30+ wearable devices, 1,850+ provider locations and continuous AI care, and sells to corporates including BCG, BHP and Bain. Hapana raised a $17.3M Series A to build AI-powered tools into the platform behind Australian and international fitness brands, reaching more than a million members. Vively (North Sydney, 2021) built a CGM-plus-wearables-plus-nutrition platform to 30,000+ members. These are teams actively adding data layers, not teams defending a finished product. Sources: [Everlab Series A](https://www.everlab.com.au/press/everlab-raises-au-65m-series-a-to-make-world-class-preventative-healthcare-something-everyone-can-access), [Startup Daily on Hapana's Series A](https://www.startupdaily.net/topic/funding/fitness-software-startup-hapana-presses-17-3-million-series-a-for-global-push/), [Vively](https://www.vively.com.au/).

3. **The Australian market has strong consumer fitness brands with deep retention exposure and no body-data feature.** Sweat (Adelaide, repurchased by its founders from iFIT in 2023) reports 39M+ downloads and syncs to Apple Health and Apple Watch; Kic (Melbourne) reports a 2.8 million community across 1,000+ classes, recipes and mindset content; Centr (Melbourne) syncs workouts and mindful minutes to Apple Health and Google Fit and sells nutritionist-approved meal plans. All three sell a transformation outcome and none of them can measure the body they are transforming. That is the retention argument in its cleanest form, and the same one Erakulis answered with a phone-camera BodyScan. Sources: [Sweat](https://sweat.com/), [Kic](https://kicwellness.com/), [Centr on Apple Health and Google Fit](https://centr.com/article/show/14143/apple-health-and-google-fit).

## Target buyer personas

- **Founder or CEO (smaller DTC apps and scale-ups).** Owns differentiation and the retention bet. Cares about subscriber churn, LTV to CAC, app-store standing. Objection: "does a scan actually move retention?" Answer with the visible-progress argument and a scoped trial on one cohort.
- **Chief Product Officer or Head of Product.** Owns the build-versus-buy call on a body-scan feature. Cares about roadmap velocity and activation. Objection: "we could build this." Answer: pre-trained models through API or SDK, no in-house computer-vision team.
- **Head of Member Engagement, Retention or Growth.** Owns the metric this moves. Cares about month 2 to 3 drop-off and check-in cadence. Objection: "will users do a scan?" Answer: two photos, under a minute, framed as a 3D before-and-after.
- **Clinical or Program Lead (weight-management, metabolic and insurer programs).** Owns outcome reporting. Cares about defensible, repeatable measurement instead of self-reported waist and scale-only weight.
- **CTO or Head of Engineering (implementer, not the economic buyer).** Cares about API quality, time to integrate, and where photos live in the data flow.

## Anti-cases (where FitXpress does not fit)

- Equipment or apparel sellers with no recurring software surface.
- Content-only libraries (streamed classes with no measurement ambition).
- Clinical or diagnostic-positioned platforms (regulated-device conversation, out of scope).
- Companies whose core product is body scanning (competitors, see exclusions).
- Very small or unstable operations: pre-launch products and apps in the middle of a shutdown or migration (Baseline by Ashy Bines was dropped on this basis, its subscriptions were cancelled and the product moved).

## Data handling expectations (per-company note carried into `companies.md`)

Every Australian target handles health data under the Privacy Act 1988 and the Australian Privacy Principles. Beyond that baseline, three splits matter for how the FitXpress data story is told:

- **Certification present.** Perx Health states HIPAA and SOC 2 Type 2 (it sells to US health plans and government agencies). Sleepfit states ISO 27001. Sonder states ISO certification, GDPR compliance and UK Cyber Essentials. With these buyers, lead with architecture: photos processed and not retained, deletion timelines, encryption in transit and at rest, no personal identifiers required.
- **GDPR in scope through offshore operations.** Eucalyptus, Sonder, The Fast 800, Catapult, VALD and Physitrack-style multi-market players run UK or EU operations, so EU and UK data rules apply alongside the Australian ones.
- **Consumer apps with no published certification.** Most of the DTC list falls here; app-store privacy labels (identifiers, usage data, health and fitness data) are the only public signal. HIPAA is not the right lead for these buyers, it reads as clinical and off-topic. Australian Privacy Principles plus plain deletion and retention terms are.

For all of them: keep the pitch operational and non-diagnostic. Australian device rules follow the claim, so body-composition trend tracking stays a wellness and engagement feature, not a clinical measure.

## Validation criteria (checked while building `companies.md`)

- At least 25 Australian-headquartered companies clear the 2-of-4 feature screen or the Tier B bar. **Result: 26 delivered, 10 of them Tier A with two criteria verified.**
- No overlap with the US digital-fitness list (2026-08-07), the UK telehealth and digital-health list (2026-07-31), or the Australian telehealth campaigns (2026-07-16, 2026-07-27). **Result: clean, with two near-misses documented in `companies.md`.**
- No competitor and no existing customer in the list. **Result: clean; Advanced Health Intelligence, mPort and Wellteq excluded by name.**
- Every row has a live website and a source that verifies its features. **Result: yes; every claim in the list traces to a fetched page or a named public source, and gaps are written as gaps rather than filled in.**

## Success metrics for this campaign

- Acceptance rate: target >= 30%
- Reply rate: target >= 5%
- Positive replies: target >= 4
- Qualified leads: target >= 2

## Open questions for Vadim

1. **Erakulis as a named reference.** Can we say "the app behind a global football brand" or name Erakulis in outreach to Australian prospects? Default until confirmed: do not name the customer in cold copy.
2. **Tier A only, or Tier A plus B?** Tier A (10 companies) is a wearables-and-AI-native list where the missing body-composition input is obvious. Tier B (16) needs a build-the-case pitch. Confirm whether the first send goes deep on Tier A or wide across both.
3. **B2B platform play.** Hapana, VALD, Catapult and dorsaVi would resell or embed a scan for their own customers rather than consume it directly. That is a partnership motion with a longer cycle and a bigger footprint. Confirm whether it belongs in this campaign or a separate partnerships track.
4. **Insurer and corporate wellbeing angle.** AIA Australia, Springday, Sonder and Sleepfit sit next to the health funds already worked in the July telehealth campaigns. Confirm there is no channel conflict before contacting them.
5. **Companies with an offshore head office.** Centr (Melbourne origin, US private-equity owner, US workforce centralisation reported) and Perx Health (Sydney origin, New York head office listed) are Australian by history and operations but not cleanly Australian by head office. Keep, drop, or route to the US profile?

## Sources

- [Eucalyptus: Juniper app connects to health and fitness devices](https://www.eucalyptus.health/blog/wearables)
- [Eucalyptus: brands and patient numbers](https://www.eucalyptus.health/)
- [AIA Vitality: devices and apps](https://www.aia.com.au/en/health-and-wellbeing/aia-vitality/devices-apps-troubleshooting)
- [AIA Vitality: program overview](https://www.aia.com.au/en/health-and-wellbeing/aia-vitality)
- [Everlab: AU$65M Series A](https://www.everlab.com.au/press/everlab-raises-au-65m-series-a-to-make-world-class-preventative-healthcare-something-everyone-can-access)
- [Startup Daily: Hapana $17.3M Series A](https://www.startupdaily.net/topic/funding/fitness-software-startup-hapana-presses-17-3-million-series-a-for-global-push/)
- [Vively](https://www.vively.com.au/)
- [Sweat](https://sweat.com/)
- [Kic](https://kicwellness.com/)
- [Centr: Apple Health and Google Fit](https://centr.com/article/show/14143/apple-health-and-google-fit)
- [Perx Health: SOC 2 Type 2](https://www.perxhealth.com/post/perx-health-attains-soc-2-type-2-compliance)
- [Sleepfit](https://www.sleepfit.io/)
- [Sonder](https://www.sonder.io/)
- [PitchBook: Wellteq acquired by Advanced Health Intelligence (December 2022)](https://pitchbook.com/profiles/company/186650-47)
- [Business News Australia: Kayla Itsines sells Sweat to iFIT](https://www.businessnewsaustralia.com/articles/kayla-itsines-sells-women-s-fitness-platform-sweat-to-us-giant-for-a-reported--400m.html)
- [Glam Adelaide: Itsines and Pearce buy Sweat back](https://glamadelaide.com.au/kayla-itsines-and-tobi-pearce-buy-back-sweat-empire/)
- [Just Food: Halo sells The Healthy Mummy](https://www.just-food.com/news/halo-food-sells-the-healthy-mummy-weight-loss-business/)
