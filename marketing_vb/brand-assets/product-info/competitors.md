# Competitive Landscape (3DLOOK)

**Last verified: 2026-10-15** for Prism Labs, Size Stream, Fit:match, Mirrorsize and Bodd (desk research:
vendor sites, app stores, published studies, press, Wayback snapshots). **Bodygram** was last reviewed in the
March 2026 internal competitive deck and has not been re-verified.

Everything a vendor says about itself is a **claim**. This market moved a lot in 2026, so check the date
before relying on a fact. If "Last verified" is more than six months old, flag it to Vadim before using the
file for a comparison.

> **This repo is public.** Only public, sourced facts go here. Internal hands-on test results, deal context
> and anything from competitors' sales decks stay in the internal Google Doc
> "Body-scanning competitors: October 2026 refresh" (Vadim's Drive).

---

## Threat map (October 2026)

| Competitor | Health / telehealth API (FX) | Apparel & uniforms (MT) | Intimates / bra fitting | Why, in one line |
|---|---|---|---|---|
| **Prism Labs** | **High** | Low | Low | Health-first SDK, DXA-referenced studies, Noom and WW distribution, $500/month entry tier |
| **Size Stream** | **High** | Medium | Low | Health business unit since July 2026, SOC 2 Type 2 claim, research library; Formcut made-to-measure |
| **Fit:match** | Medium | Low | **Medium** | Self-serve SDK and BAA since 2026; past bra-fitting deployments; 2026 focus is youth sports |
| **Bodygram** | Medium | Medium | Low | Cross-vertical photo-based API with public docs (March 2026 view, not re-verified) |
| **Mirrorsize** | Low | Medium (uniforms, MTM) | Low | Cheap self-serve apparel tool, no accuracy data |
| **Bodd** | Low (Medium only for in-store kiosks) | Medium (enterprise uniforms) | Low | Hardware booth with strong uniform references, pharmacy push |

---

## What changed in 2026

1. **GLP-1 and clinical use became everyone's pitch.** Size Stream launched Size Stream Health (July 2026).
   Fit:match rewrote its health page around GLP-1 and hired clinical leadership. Prism was listed on Novo
   Nordisk's partner platform. Bodd raised A$15M with pharmacies and GLP-1 in the story. Mirrorsize showed a
   "two top-5 pharma clients" line on its technology page from February to May 2026, then removed it. Our
   health and telehealth positioning is no longer a lightly contested space.
2. **Compliance claims became table stakes.** Prism claims SOC 2 Type II and HIPAA BAAs, Size Stream
   announced SOC 2 Type 2 (March 2026), Fit:match offers a BAA and a SOC 2 report under NDA. Our own status
   comes only from `compliance.md`: BAA for HIPAA-governed deployments, SOC 2 attestation in progress (no
   report yet). Expect buyers to compare.
3. **Self-serve developer access spread.** Prism: published prices from $500/month and a 90-day sandbox.
   Fit:match: public SDK docs and a 14-day sandbox. Mirrorsize: $249 and $499 monthly plans with a $1 trial.
   Our path is demo → contract (`pricing.md`).
4. **Accuracy: many claims, no fully independent proof.** Prism and Size Stream publish DXA-referenced numbers,
   mostly from studies they funded or wrote. Fit:match, Mirrorsize and Bodd publish no error figures. Steer
   buyers to the reference-method question in `accuracy-formulations.md` §1.7 instead of a numbers duel.
5. **None of these six has a live bra-fitting product.** Fit:match's Macy's and Savage X Fenty work dates from
   2022–23.

---

## Direct competitors

### 1. Prism Labs (primary FitXpress competitor)

**Who they are:** prismlabs.tech. Prism Labs, Inc., Los Angeles, with an office in Austria. CEO Steve Raymond;
scientific advisor Grant Tinsley (Texas Tech). B2B only: no consumer app of its own; it runs inside partner
apps (Noom, WW "AI Body Scanner", Fitify, Tempo). Founding year is 2019 or 2021 depending on the source; the
company appears to descend from Naked Labs, a 3D-mirror maker.

**Product:**
- Capture: a 10-second 360° spin in front of the front camera (Prism says ~150 frames), processed in Prism's
  cloud on AWS in the US. Weight, height, sex and birth date are typed in.
- Outputs: 28 circumferences, waist-to-hip ratio, body volume, body fat %, lean and fat mass, visceral fat,
  appendicular lean mass, skeletal muscle mass, predicted BMI (added July 2026), health report, textured 3D
  avatar, "Future Me" shape prediction.
- iOS, Android and Web SDKs plus a REST API, with public docs and a public GitHub org. Tablet scanner SNAP
  with Fit3D.

**Their primary bets:** GLP-1 / weight loss, insurers, chronic disease, healthcare providers (remote-monitoring
billing), pharma trials, fitness, research, corporate wellness. Novo Nordisk partner-platform listing
(June–July 2026); FNIH REAL BODY study (December 2025).

**Evidence (their claims):**
- Website: "DEXA precision using a mobile device" (their wording for DXA).
- Validation site: body fat ±3.56 percentage points vs DXA (n=271); chest and waist about ±1.5% vs a
  multi-camera 3D scanner (n=78). White paper, April 2026, 550 subjects.
- The key peer-reviewed papers (2024) were funded by Prism, and the lead author discloses Prism stock options.
  A tape-referenced study (Pennington, 2024, n=44) reported a 3.4 cm mean absolute waist error.
- "40% more precise than 2-photo systems" is a repeat-scan precision result against one unnamed two-photo app
  (EJCN 2024), not an accuracy result.

**Commercial:** priced per monthly active user, unlimited scans. Startup (≤1,000 users) from $500/month (was
$1,000 until July 2026); Scale Up (≤10,000) from $5,000/month; Enterprise from $15,000/month (was $10,000).
A HIPAA BAA comes only with Scale Up and above. Free 90-day sandbox under evaluation terms (non-production,
no personal data).

**Compliance claims:** SOC 2 Type II, HIPAA BAAs, GDPR, encryption at rest and in transit. No public SOC 2
report found.

**Strengths:**
- The deepest published evidence base in health body composition
- Large consumer reach through partner apps
- Transparent, low entry pricing and a sandbox
- A clear "body composition beyond BMI" and GLP-1 muscle-preservation story

**Weaknesses (relative to us):**
- Users must complete a timed 360° spin in fitted clothing
- Most validation is vendor-funded
- The BAA starts at $5,000/month
- No apparel sizing, no bust outputs, no Mobile Tailor equivalent

**How we differentiate:**
- Two-photo capture with Real-Time Pose Validation (RTPV) and the Clothing Detector (`tech-spec.md` wording)
- Smart Scales (beta) weight-mismatch flag for verification use cases
- Two-product portfolio (FX + MT)
- BAA for HIPAA-governed deployments (`compliance.md` wording)
- Do not claim better accuracy; use `accuracy-formulations.md`

**When we lose to them:** buyers focused on clinical body-composition metrics (visceral fat, muscle mass,
DXA-referenced studies), or buyers who want self-serve sign-up at a published price.

---

### 2. Size Stream

**Who they are:** sizestream.com. Founded 2012, Research Triangle Park / Cary, North Carolina. A wholly owned
subsidiary of The Apparel Group; press links Size Stream and Formcut to TAL Apparel. (Older notes said
"TAG Holdings"; that was wrong.) CEO Jay Rudman; about 22 employees on LinkedIn.

**Products:**
- **MeThreeSixty** (consumer app, iOS and Android): front and side photos processed on the phone; body fat,
  lean mass, 3D avatar, progress view. GLP-1 dose tracking since August 2026; "FutureMe Moment" (October 2026)
  makes an AI video from an uploaded headshot. Premium $4.99/month.
- **Mobile Fit:** B2B white-label measurement app; users are registered by the employer.
- **Booth scanners:** 240+ measurements, under 60 seconds per person.
- **Formcut:** scan-to-factory made-to-measure.
- **Size Stream Health** (business unit launched 14 July 2026): telehealth, GLP-1 / obesity, clinical trials
  and CROs, remote patient monitoring, insurers, corporate wellness. Smartphone plus in-clinic scanning; SDK
  and API.

**Evidence (their claims):**
- "less than 3% mean absolute error" and "DXA-level accuracy".
- Their own paper (3DBODY.TECH Journal, December 2025, n=46): 95% limits of agreement for body fat vs DXA of
  ±6.9 percentage points; measurement error 1.3–5% scored against their own booth, not a tape measure.
- Academic studies: *Military Medicine* (April 2026, n=57) found the phone scan among the best field methods
  for tracking body-fat change vs DXA; a University of Alberta review (2026) found group-level results
  reliable but individual precision weaker; a Texas A&M–San Antonio abstract (2025, n=32) reported 6.3–14.8%
  error vs tape.
- Scale: "3M+ scans, 1M+ members".

**Commercial:** enterprise pricing not public; demo-led; pilots for "qualified" prospects; no public SDK docs
or sandbox.

**Compliance claims:** SOC 2 Type 2 (announced March 2026); GDPR; "no photos uploaded" (on-device
silhouettes). No HIPAA or BAA claim found.

**Strengths:**
- A research library and academic network
- Hybrid phone plus booth / clinic scanning
- A dedicated health unit
- Consumer app at scale

**Weaknesses (relative to us):**
- Small team
- No public developer path
- Marketing claims run ahead of their own published data
- A spread-out portfolio (consumer, apparel, research, health)

**How we differentiate:**
- Embed-first API/SDK with white-label (`tech-spec.md`)
- BAA for HIPAA-governed deployments
- Verification features: RTPV, Smart Scales (beta)

**When we lose to them:** customers with booth or in-clinic hardware already, research buyers who want a
publication list, and made-to-measure buyers who want a manufacturer behind the scan (Formcut).

---

### 3. Fit:match

**Who they are:** fitmatch.ai. Fort Lauderdale, Florida; founded 2018 on Cornell-licensed patents. $18M raised
to date (Series A extension, December 2025). About 28 staff (peak of 40 in 2023). Added a CRO, a Head of
Clinical & Scientific Affairs and a Medical Director in 2026.

**Products:**
- **QuadraScan:** 4 photos (front, back, left, right). iOS app (iOS 18+), web app, iOS and Web SDKs, API.
  Outputs: 3D avatar, "25+" measurements, lean mass, total fat, bone mineral content, predicted adult height.
  No Android.
- **Reflect:** an in-store kiosk with a depth sensor and a turntable (2024).

**Their primary bets:**
- Youth and pro sports: MLS Innovation Lab (April 2026), Playmaker Recruiting (May 2026), Pulse Technologies
  (August 2026)
- Digital health: GLP-1, bariatric, rehab
- Retail: Browzwear partnership (May 2026)

**Intimates:** bra fitting in 10 Macy's stores (2022, LiDAR devices held by associates), Savage X Fenty fitting
rooms (2022–23, Intel depth sensors), bra-sizing patents (US11430246B2, US12333595B2). Nothing new since; the
public SDK lists chest but no underbust.

**Evidence (their claims):**
- Homepage: "DEXA-validated body composition"; their own health page says outputs are "not equivalent to DEXA"
  (both are their spelling of DXA).
- Retail: "93% fitting accuracy", no method given. The "submillimeter accuracy" claim was removed in 2026.
- No published studies; "See Validation Studies" leads to a contact form.

**Commercial:** tiers Entry (≤1,000 scans/month), Pro (≤5,000) and Enterprise, with no published prices;
14-day sandbox; public SDK docs.

**Compliance claims:** a HIPAA badge and a BAA; GDPR; SOC 2 report under NDA. Their privacy policy gives two
different retention periods for biometric data.

**Strengths:**
- Retail and sports references
- Bra-sizing patents and past intimates deployments
- Self-serve SDK and sandbox

**Weaknesses (relative to us):**
- No published accuracy data
- iOS only
- Small team
- Intimates proof is old and ran on in-store hardware

**How we differentiate:** two-photo capture on iOS and Android, white-label SDK, verification features, FX + MT.

**When we lose to them:** sports scouting deals, and buyers who want one vendor across retail fit and sports
analytics.

---

### 4. Bodygram (last reviewed March 2026, not re-verified)

**Who they are:** bodygram.com. Founded 2019, Tokyo. Cross-vertical: retail, uniform sizing, health, insurance.

**Product:** two photos, scanning with clothes on. Outputs: 3D avatar, body measurements, posture analysis,
body-composition estimate. Documented APIs, no-code integrations, enterprise widget / SDK (Body2Fit).

**Commercial:** "start free" messaging; enterprise modules sales-led. Large public case-study list (Unicharm,
Kanko, insurers, clinics).

**Earlier notes (2025):** strong with fitness trainers, health professionals and dieticians; simple
trainer-focused UX; priced for SMB and solo professionals; weaker clinical and enterprise workflow; no strong
HIPAA story.

**How we differentiate:** verified body data (Smart Scales beta mismatch flag), BAA for HIPAA-governed
deployments, white-label depth, Mobile Tailor for apparel.

**When we lose to them:** SMB, single-trainer or boutique-gym deals where price dominates.

---

### 5. Mirrorsize

**Who they are:** mirrorsize.com. Mirrorsize US Inc., Plainsboro, New Jersey, with R&D in Noida, India.
Founded 2017; about 18 staff; no outside funding reported.

**Products:**
- MS GetMeasured: front and side photos; 31, 63 or unlimited measurement points by plan; 3D model view on
  higher plans
- Size2Fit (size recommendation), QuickSize (questionnaire), 3D Configurator, ShoeSizer
- Corpo3D: a consumer health app (it appeared in our March 2026 B2C review as a separate player)
- Cloud processing on AWS

**Their primary bets:** fashion, e-commerce, uniforms (a white-label app for Marlow White military uniforms),
tailoring and made-to-measure.

**Evidence:** none published. "World's Best Precision" and "Best in world accuracy" with no figures; the only
number is a 2019 founder quote ("as low as one centimeter"). The technology page says "patented", the FAQ
says "patent-pending".

**Commercial:** Small $249/month (100 scans, 31 points), Medium $499/month (300 scans, 63 points), Enterprise
custom; $1 seven-day trial; API/SDK plans carry a one-year term that cannot be cancelled.

**Compliance claims:** the homepage (since mid-2026) names GDPR and HIPAA and promises image deletion within
30 days; the privacy policy (effective 2022-10-01) says images are kept for 10 years and staff can access
them for R&D. No SOC 2, ISO 27001 or BAA.

**Strengths:** low, published prices; fast self-serve start; uniform references.

**Weaknesses (relative to us):** no accuracy data; contradictory privacy statements; small team.

**When we lose to them:** price-led uniform or made-to-measure deals with small budgets.

---

### 6. Bodd

**Who they are:** bodd.io. Bodd Technologies Pty Ltd, Melbourne (new Prahran HQ, July 2026). Raised A$15M in
December 2025 at a reported A$110M valuation; about 44 staff (September 2026). CEO Rob Fisher.

**Product:** hardware only.
- A Bosch-made 3D booth (Gen 2 "R2") with a turntable and infrared / time-of-flight sensors; 45–60 second scan.
  Needs about 1.25 m² of floor, clearance around it, constant lighting and a private changing area.
- No smartphone capture, no consumer app, no public API or SDK.
- Software: BoddHub portal, SizeMatch size recommendation, Bodd Wellness. Their wellness module estimates body
  composition from body shape ("not from a lab method like DEXA", in their words) and reads heart rate, HRV
  and an estimated blood pressure from a face video. Bodd states it is "not intended for use in clinical
  practice".

**Their primary bets:**
- Uniforms first: United Airlines (about 60,000 staff), Brooks Brothers, NZ Defence Force, Australian Defence
  Apparel, Stewart & Heaton, Portwest
- Pharmacy and GLP-1 wellness: pitched, no live pharmacy named yet
- Fitness and corporate wellness

**Evidence:** no accuracy numbers or studies published.

**Commercial:** leased SaaS with "zero capital outlay" and a fixed cost per scan; multi-year terms; no public
prices.

**Compliance claims:** ISO 27001 badge; Australian Privacy Act. No HIPAA, SOC 2 or GDPR claims.

**Strengths:** enterprise uniform references; fresh funding and a growing team; an in-person kiosk
experience.

**Weaknesses (relative to us):** hardware footprint, no remote capture, no API.

**How we differentiate:** two phone photos wherever the user is, Mobile Tailor for remote uniform measuring,
embedding in the buyer's own app.

**When we lose to them:** uniform programs that measure staff at a central site and want a booth experience.

---

## Watch list (not profiled)

- Phone-based: Spren, Bodymapp, ZOZOFIT, Body Volume Index (BVI), Nettelo, Esenca, SnapMeasureAI
- Apparel data: Bold Metrics, Sizer Technologies
- Hardware: Styku, Fit3D, InBody, Visbody, BodySpec

---

## Long-term strategic risk: Apple / Google native primitives

**Risk:** OS vendors may expose body / pose / measurement primitives at the platform level (similar to ARKit,
Vision framework). This could compress margins and make some "good enough" scanning use cases easy to replace.

**How we turn this into advantage:**
- We never lead with "best model". We lead with **outcomes + workflow + governance**.
- Apple/Google won't ship workflow integrations, audit logs, customer SLAs or drift monitoring.
- We invest in the **trusted workflow layer**: scan-to-scan comparison, audit logs, deep integration that is
  costly to swap.

**Messaging implication for outbound and content:**
- Avoid statements like "the most accurate scanning available". It undermines this defense, and no
  independent head-to-head supports it.
- Prefer "trusted infrastructure for verified body data in regulated workflows".

---

## Adjacent / not direct competitors but worth knowing

| Player | Why they appear | Our positioning |
|--------|-----------------|-----------------|
| Withings (smart scales) | Physical scale alternative for weight tracking | Different category — they need a device, we work with phone |
| InBody (BIA) | Body composition via bioimpedance | Hardware-based, in-clinic; we are remote/scalable |
| DXA scan providers | Gold-standard body comp | Different category; clinical-grade, expensive, not scalable |
| MyFitnessPal / generic fitness apps | Self-tracking | They lack verification — that's exactly where we win |

---

## How agents should use this

- **Never name competitors** in cold outbound or in articles. Compare by method and role.
- **Never quote a competitor's numbers or claims in public content.** This file is for positioning and
  hypothesis choice, not for copy.
- **Our side of any comparison** comes only from `compliance.md`, `accuracy-formulations.md`, `tech-spec.md`
  and the publishable rows of `proof-points.md`.
- **hypothesis-generator:** check the threat map. Where Prism or Size Stream lead (clinical body composition,
  research, booth-based clinics), sharpen the hypothesis to verification, two-photo remote capture, white-label
  embedding or FX + MT breadth.
- **seo-planner / seo-outline-builder:** use the gaps (reference-method transparency, two-photo remote capture,
  verification) for content angles, without naming vendors.
- **message-sequencer:** never name competitors. If a prospect names one in a reply, the `response-classifier`
  flow hands it to sales with the matching section of this file.
