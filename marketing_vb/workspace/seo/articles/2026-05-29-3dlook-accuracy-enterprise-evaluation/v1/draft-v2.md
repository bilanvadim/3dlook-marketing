---
title: "How Accurate Is 3DLOOK? An Enterprise Evaluation Framework"
slug: 3dlook-accuracy-enterprise-evaluation
author: Assel Sekerova
date: 2026-05-29
product: fitxpress
status: phase_4_self_critique_applied
target_keywords: [3dlook accuracy, body scanning accuracy, mobile body scanning evaluation, enterprise body measurement]
yurii_review_required: true
phase: 4_post_self_critique
parent_phases: [phase-1-data-audit.md, phase-1b-pdf-reverify.md, phase-2-outline.md, phase-4-self-critique.md]
---

# How Accurate Is 3DLOOK? An Enterprise Evaluation Framework

Enterprise buyers evaluating mobile body scanning rarely get a useful answer to the question that opens every sales call: how accurate is it? The number a vendor quotes — 95%, 96%, 98%, sometimes higher — depends on what they measured against, how often, and on what population. Two vendors quoting the same headline percentage can perform very differently in production.

This article is the framework 3DLOOK uses internally to evaluate its own measurement quality, and the same framework enterprise teams can use when comparing vendors. It walks through five dimensions of measurement quality, the dataset and methodology behind 3DLOOK's numbers, where the technology fits among other body-measurement methods, and what is explicitly outside its scope. Every number cited here sits inside a methodology disclosure. Where direct comparative validation against a reference method has not been completed, that is noted plainly.

## What enterprise buyers should actually evaluate

Headline accuracy is a starting point, not an answer. A vendor that quotes 97% accuracy against a scanner reference may underperform a vendor quoting 95% against a manual reference, because manual measurement is the harder benchmark to clear. A vendor with 99% repeatability across two scans in one session may still drift between months, which is what matters for longitudinal weight tracking, underwriting refreshes, or before-after compliance checks.

For an enterprise buyer, five dimensions matter together: measurement accuracy, scan-to-scan repeatability, real-world robustness, output breadth against the actual use case, and validation strength. Each is covered below with the relevant numbers from 3DLOOK's internal validation work, and the article closes with an eight-question evaluation checklist for the next vendor conversation.

## The five dimensions of measurement quality

### Dimension 1 — Measurement accuracy

Measurement accuracy is the gap between what the system outputs and what the reference says the true value is. The choice of reference matters more than most vendors disclose. A 3D scanner reference produces a different number than a manual measurement reference, because the two are measuring slightly different things — a scanner captures surface geometry, while a trained pattern-maker captures the circumference a garment will need to fit.

On 3DLOOK's internal validation benchmark — a real-world dataset of multiple customer scan events with five repeated scans per person, compared against expert pattern-maker manual measurements — measurement accuracy is approximately 96 to 97% across body metrics, with a typical absolute error margin of 1.5 to 2.0 cm. Demographic scope of that internal validation dataset: ages 16 to 78, heights 150 to 205 cm, weights 38 to 210 kg, US and Europe. That is the population the accuracy figure was measured against, not a universal "works for everyone" claim.

The figure varies meaningfully by body part. Smaller, joint-defined girths sit near 0.5 to 1.5 cm of typical error, while soft-tissue and posture-influenced measurements run higher. The table below shows the per-body-part absolute error from 3DLOOK's internal validation chart.

| Body part | Absolute error (cm) |
|-----------|----------------------|
| Wrist girth | 0.54 |
| Calf | 1.27 |
| Neck | 1.48 |
| Thigh | 1.64 |
| Back shoulder width | 1.72 |
| Knee | 1.73 |
| Chest | 1.74 |
| Waist height | 1.74 |
| Bicep | 1.85 |
| Back neck point to waist | 2.09 |
| Waist | 2.14 |
| Inside leg height | 2.21 |
| Hip | 2.25 |
| Back neck height | 2.37 |

*Source: 3DLOOK internal validation against expert pattern-maker manual measurements (February 2025). Five repeated scans per person across multiple real-world customer scan events.*

For most enterprise use cases, what matters is not the single headline number but whether the per-measurement error is acceptable for the workflow the data feeds into. A 1.74 cm waist error is well inside what made-to-measure tailoring can absorb in tolerance; whether the same error is acceptable for underwriting depends on the underwriting protocol. Without the per-measurement breakdown, that decision cannot be made on the headline number alone.

### Dimension 2 — Repeatability

Repeatability is scan-to-scan consistency for the same person, taken under the same conditions, within a short interval. It is the dimension that matters most for longitudinal use cases: weight tracking in a GLP-1 program, underwriting refreshes year-over-year, before-and-after compliance checks in clinical trials.

Internal repeatability testing across five repeated scans per person, on a real-world customer dataset, shows scan-to-scan consistency above 95%, with a variance of less than 1 cm across repeated scans for most measurements. The full per-body-part variance breakdown is covered in the repeatability deep-dive section.

For a buyer, the question to ask any vendor is not "is your system repeatable?" but "how is repeatability measured, over how many sessions, and what is the variance per body part?" A vendor without a per-measurement answer has not done the work.

### Dimension 3 — Real-world robustness

Production conditions are not lab conditions. Users stand in odd lighting, wear sweaters over t-shirts, hold the phone at the wrong angle, or stand slightly off-axis. A measurement system that only works under controlled conditions produces a workflow problem at scale — every borderline scan becomes a retake, a support ticket, or a silent error in the data.

3DLOOK's production pipeline includes three real-world robustness layers. Real-time AI-driven skeletal tracking dynamically evaluates posture during capture, surfacing red markers for incorrect positioning and turning them green as the user adjusts to voice prompts. AI clothing detection classifies what the user is wearing — sport, regular, or oversized — and applies garment-aware corrections to the 3D output so that loose clothing does not pull the body shape estimate outward. The training dataset itself was generated with 34 different photo configurations per user, covering variations in distance, angle, slope, and lighting, so the underlying model is trained to absorb the messiness of real-world capture.

The full production reliability layer is covered in a dedicated section later in the article.

### Dimension 4 — Output breadth and use-case fit

Different verticals need different outputs. A telehealth program for GLP-1 retention needs verified BMI and longitudinal progress visualization; a uniform manufacturer needs a specific subset of girth and length measurements; a [life underwriter](https://3dlook.ai/content-hub/mobile-body-scanning-insurance-underwriting/) needs BMI plus waist circumference plus a body fat estimate. The same scan event can serve any of these, but the outputs and limitations differ.

| Vertical | Primary 3DLOOK output | Why it matters | Limitation to disclose |
|----------|-------------------------|----------------|--------------------------|
| Telehealth and weight-loss (GLP-1, coaching apps) | BMI from height plus estimated weight; longitudinal scan-to-scan progress; body composition trends | Verified BMI without requiring the user to own a scale; 3D progress visualization supports adherence | Not a clinical diagnosis; not a replacement for calibrated bioimpedance or DEXA |
| Online pharmacy and digital prescriber | BMI verification at intake or refill | Anti-fraud check against self-reported weight; eligibility screening | Designed for screening, not standalone clinical determination |
| Life and disability underwriting | BMI plus waist circumference plus body fat estimate | Faster underwriting decisions; remote intake without a lab visit | Internal validation only — not a replacement for medical examination where required |
| Made-to-measure apparel | 80+ body measurements with girth plus linear dimensions | Reduces remakes and returns; remote measuring at scale | Typical absolute error 1.5 to 2.5 cm per measurement; pattern-makers should hold tolerance against this |
| Uniform, PPE, and workwear | Subset of girth and length measurements relevant to the garment block | Measurement consistency across a distributed workforce | Same per-measurement tolerance as above |
| Clinical trials and decentralized screening | Body composition trends as a secondary endpoint | Decentralized measurement at low burden | Not third-party validated; not peer-reviewed; not a primary clinical endpoint |

The right way to read this table is row-first: the limitation column is non-optional. Any output 3DLOOK produces sits inside the workflow constraints listed alongside it. A vendor that does not surface comparable limitations is asking the buyer to do that disclosure work themselves, often after a procurement decision has been made. For the employer-wellness and insurance-rewards angle, see our deep-dive on [wellness rewards verification](https://3dlook.ai/content-hub/wellness-rewards-verification-employers-insurers-using-ai-3d-body-scanning/).

### Dimension 5 — Validation strength

Validation strength is the dimension most vendors blur. The honest version is a three-part picture for 3DLOOK: the internal validation benchmark covered above; an ISO 8559-1:2017 multi-company benchmark study from 2022/2023; and a 2022 academic partnership for dataset enrichment.

The ISO benchmark study involved 14 companies across 8 countries, 27 participants, 72 subjects measured, and 1,152 data points gathered, using the average of multiple 3D scanner measurements as the reference. On that benchmark — a different reference than the internal pattern-maker comparison — 3DLOOK's session-to-session repeatability came in at 0.40 cm, the lowest of the three measurement methods compared in the study (manual experts: 0.94 cm; hardware 3D scanners: 0.57 cm). That is a near-independent validation signal, but the reference is different from the Feb 2025 internal study, so the accuracy numbers from the two studies should not be combined.

Through a 2022 partnership with North Carolina State University's Wilson College of Textiles — publicly listed as a funding-partner project on NCSU's [3D Body Scanning research projects page](https://3dbodyscan.textiles.ncsu.edu/projects/) — 3DLOOK's training dataset was expanded with ground-truth scans from the university's body scanning lab. This was dataset enrichment work conducted in partnership with NCSU, not independent validation of 3DLOOK's measurement claims, and no peer-reviewed publication on the collaboration is on file.

Where direct comparative validation against a specific reference method has not been completed, 3DLOOK should not be positioned as equivalent to that method.

## How the 3DLOOK pipeline actually works

[3DLOOK's mobile body scanning](https://3dlook.ai/content-hub/3dlook-turns-two-photos-structured-body-data/) is powered by a proprietary statistical generative human body model — a different approach from 3D reconstruction methods that depend on depth sensors or structured-light hardware. The model was trained on the dataset described in the next section, and it produces a 3D body model plus 80+ measurements from two smartphone photos.

The capture-to-result pipeline runs in four steps. First, the user takes two photos with any smartphone camera on any background, fully clothed, with real-time pose validation guiding alignment. Second, computer vision algorithms detect the body under the clothing, with AI clothing detection adjusting the 3D output for garment interference. Third, statistical modeling and 3D matching algorithms construct a 3D body model — generated in under 30 seconds. Fourth, 80+ body measurements plus BMI, BMR, body fat percentage, lean body mass, and fat body mass are computed from the model, with the full capture-to-results pipeline completing in under 45 seconds.

The body shape segmentation step is patented. It is what allows the system to accept photos of fully clothed users on any background as input, rather than requiring undressed or tight-garment reference capture.

## Ground-truth dataset and validation methodology

The model is trained on 3DLOOK's proprietary dataset of 5,000+ participants, comprising 150,000+ photographs, 30,000+ ground-truth 3D scans, and 430,000+ individual measurements. The geographic scope of the dataset is US and Europe; the demographic scope covers ages 16 to 78, heights 150 to 205 cm, weights 38 to 210 kg, with a 48% male and 52% female gender mix. Where 3DLOOK quotes a "works against this population" figure, this is the population.

Ground-truth 3D scans were generated using a hardware capture rig with 4 dynamic cameras, capturing approximately 1 million polygons per 3D model at 1 mm spatial resolution. Each participant was scanned for 80+ anatomical parameters, including measurements in sitting position and during inhale and exhale breathing cycles, supporting analysis of how soft tissue moves across postures. The training data was augmented through a Photo Flow Simulation step generating 34 different photo configurations per participant, varying distance, angle, slope, and lighting — the variations that show up in real-world smartphone capture.

The dataset was expanded in 2022 through the NCSU Wilson College of Textiles partnership described in Dimension 5 above. Additional ground-truth 3D scans were captured using the university's Size Stream Body Scanner, with participants photographed in both casual or sports clothing and tight-fitting athletic clothing, and metadata recorded for height, weight, age, gender, ethnicity, and occupation. This work extended dataset diversity; for the validation-vs-enrichment framing, see Dimension 5.

## Repeatability and per-body-part stability

Repeatability is not a single number. It varies meaningfully by body part, and the variation pattern itself is informative for buyers thinking about which measurements to rely on in a given workflow.

Internal repeatability testing across multiple customer scan events indicates that small, joint-defined girth measurements tend to carry the lowest scan-to-scan variance — wrist girth at 0.11 cm, ankle at 0.07 cm, knee at 0.12 cm, calf at 0.12 cm. Linear measurements anchored to defined anatomical points also show high stability: neck linear at 0.05 cm, shoulder-length-centre-back at 0.05 cm, outer ankle height at 0.04 cm. Soft-tissue and posture-influenced areas carry the highest variance — waist at 0.89 cm, low hips at 0.86 cm, abdomen at 0.82 cm, with overarm girth at 1.29 cm as the highest single value in the internal dataset.

The pattern is consistent with what would be expected from any vision-based measurement system: defined skeletal landmarks are easier to track scan-to-scan than soft tissue that moves with breathing, posture, or hydration. Most measurements sit comfortably under 0.5 cm session-to-session variance, which supports the above-95% overall repeatability figure and the under-1-cm variance claim made in the accuracy benchmark.

The ISO 8559-1:2017 multi-company benchmark referenced in Dimension 5 is consistent with this pattern. On 11 ISO-compatible measurements, 3DLOOK's average session-to-session repeatability was 0.40 cm, the lowest of the three methods tested.

## Body composition outputs

3DLOOK's body composition outputs are BMI, BMR, body fat percentage, lean body mass, fat body mass, and a Smart Scales weight estimation. Each is computed from the 3D model and a small set of user-provided values; each has a defined scope and a limitation that should be disclosed alongside the number.

BMI is calculated as weight in kg divided by height in metres squared. When the user supplies their own weight, BMI is the standard formula; when the user does not supply a weight, the Smart Scales weight estimation feeds the BMI calculation. Internal testing of BMI calculated from estimated weight shows 89% accuracy against reference, with 76% of users falling within 5% deviation. For workflows that allow user-provided weight, the standard formula applies without estimation overhead.

BMR is calculated using the Mifflin-St Jeor formula, the established anthropometric equation that uses weight, height, age, and biological sex. 3DLOOK does not modify the formula; the output is the Mifflin-St Jeor calculation against the inputs.

Body fat percentage uses the U.S. Navy formula, selected through internal comparative evaluation of established anthropometric methods. The Navy formula uses height plus neck and waist (or, for women, neck, waist, and hip) circumferences, which 3DLOOK's measurement pipeline produces directly from the 3D model. The choice of formula is a workflow decision: 3DLOOK does not position the Navy estimate as equivalent to a DEXA or BIA reading, and where a study or program requires a specific body composition methodology, that methodology should be specified at protocol design.

Smart Scales is a weight estimation aid. It computes body weight from the 3D body model by summing per-segment volume against calibrated density coefficients derived from 3DLOOK's internal ScanLab dataset. Internal testing shows a mean absolute error of 2.1 kg, a mean relative error of 3.11%, and an average prediction error of approximately 3.5%. Smart Scales is designed for contexts where a calibrated scale is unavailable or impractical — early-stage telehealth onboarding, remote screening, multi-month longitudinal tracking where the user does not own a scale. It is not designed as a replacement for a calibrated scale in clinical, compliance, or underwriting workflows where calibrated weight is the requirement.

## Where 3DLOOK fits among body-measurement methods

Different body-measurement methods exist because they answer different questions, and the broader landscape is covered in our [body scanning technology comparison](https://3dlook.ai/content-hub/body-scanning-technology-comparison/). Each method below is described in its own terms with notes on what 3DLOOK is and is not designed to do alongside it.

Dual-energy X-ray attenuation imaging, commonly called DEXA, is the clinical reference for body composition. It produces highly accurate fat mass, lean mass, and bone density data, requires specialized in-clinic equipment, uses ionizing radiation, and is typically used in research and clinical contexts. Bioelectrical impedance analysis, used in InBody devices and similar systems, estimates body composition by passing low-level electrical current through the body and is sensitive to hydration state. Consumer smart scales use impedance through the feet to produce daily weight and rough body composition estimates, calibrated for convenience rather than clinical precision. Manual anthropometric measurement, performed by a trained anthropometrist or pattern-maker with a tape, is the gold standard for circumferences when done by certified personnel, and carries its own session-to-session and inter-rater variability — visible in the ISO benchmark study, where manual experts showed 0.94 cm session-to-session repeatability against the same subjects.

3DLOOK is a mobile vision-based body measurement system. It produces 80+ measurements plus body composition outputs from two smartphone photos, in under 45 seconds, with no hardware setup. Its design point is remote, repeated, longitudinal measurement at scale — the conditions where in-clinic DEXA, in-pharmacy BIA, or trained-tape manual measurement become impractical to operate. Mobile body measurement systems in this category typically operate in a 1.5 to 2.2 cm waist-circumference error range, with 3DLOOK's internal validation placing it at the lower end.

Where a study, regulatory protocol, or clinical workflow requires direct comparative validation against a specific reference method, 3DLOOK should not be positioned as equivalent to that method. The honest sentence to use in any vendor evaluation is: different methodologies serve different purposes.

## Compliance, privacy, and governance

Compliance posture matters as much as measurement quality for any healthcare, insurance, or pharma deployment. The 3DLOOK FitXpress data and privacy framework is structured around five principles.

Storage. All data is stored in Amazon S3 with mandatory server-side encryption using S3-managed keys (SSE-S3). Storage encryption is always on and cannot be disabled.

Encryption in transit. All data is encrypted in transit using TLS, enforced by default.

Photo retention and deletion. Photos are permanently removed either immediately after processing or within 30 days of generating results, configured against the client's data retention requirements. When temporary storage is selected, retained photos are automatically blurred to add an additional layer of privacy protection. Users may exercise their privacy rights by contacting `privacy@3dlook.me`.

Data minimization. 3DLOOK does not process user names, contact details, or other personal identifiers that would link a photo or measurement output to a specific individual. End-user images are never shared with third parties.

Regulatory framework. FitXpress maintains HIPAA compliance for US healthcare contexts and follows GDPR principles for European deployments. Continuous security monitoring is in place.

One framing point worth stating directly: "Since FitXpress does not provide medical advice, diagnosis, or treatment recommendations, medical device certifications do not apply." That is a deliberate positioning decision rather than a gap. 3DLOOK is built as a workflow and data layer that feeds clinical or compliance workflows downstream — it is not built to make a clinical decision itself, and medical device certifications are not the relevant regulatory framework for what it does.

For procurement teams, that distinction matters: 3DLOOK's compliance evaluation runs on data privacy frameworks (HIPAA, GDPR, SOC 2 where applicable), not on medical device frameworks (FDA Class II, CE-MDR), which do not apply to the product as designed.

## Production reliability features

The accuracy and repeatability numbers earlier in this article describe what the model produces. Production reliability is the layer that decides which scans reach the model in the first place — and which get sent back to the user for a retake before they ever become a measurement.

Real-time AI-driven skeletal tracking dynamically evaluates body posture during capture, using subpixel keypoint detection to flag misalignment as it happens. The user sees red markers on misaligned joints; voice prompts walk the user through the adjustment; markers turn green as alignment improves. The system does not accept the scan until alignment is correct, which prevents a class of measurement errors that would otherwise show up downstream as outlier values.

AI clothing detection classifies the user's clothing as sport, regular, or oversized, using a neural network trained on labeled clothing data. During 3D reconstruction, garment-aware corrections compensate for visual obstruction — the shape under a loose sweater is not the shape of the sweater. This is the layer that lets 3DLOOK accept fully clothed users on any background, rather than requiring tight reference garments.

Face obfuscation is applied automatically to support user privacy: the user's face is blurred at capture, before any image leaves the device, so that downstream processing operates on anonymous body imagery. This pairs with the data minimization principle described in the previous section.

The full stack runs cross-platform on Android and iOS, from older devices through current models, with no depth-sensor or accessory hardware required. Enterprise deployments typically encounter device fragmentation; a system that only works on flagship phones produces a coverage problem at scale.

## Enterprise evaluation checklist

The questions below are the framework 3DLOOK uses to evaluate its own measurement quality. They work as a framework for evaluating any body-measurement vendor.

1. **What reference method was used to measure accuracy, and what is the typical error margin?**
   3DLOOK uses expert pattern-maker manual measurements as the reference, with a typical absolute error of 1.5 to 2.0 cm. The per-body-part error table is the substantive answer — see Dimension 1.

2. **How is repeatability measured, and over how many sessions?**
   Five repeated scans per person across a real-world customer dataset, with greater than 95% repeatability and variance under 1 cm across repeated scans. The per-body-part variance pattern is covered in the repeatability section.

3. **What real-world conditions has the system been tested under?**
   34 photo configurations per user in dataset training (distance, angle, slope, lighting), plus production-time AI pose validation, clothing detection, and lighting adaptability — see the production reliability section.

4. **What outputs does the vendor produce, and how do they map to my use case?**
   80+ measurements plus BMI, BMR, body fat percentage, lean body mass, and fat body mass. The use-case mapping table in Dimension 4 shows which outputs fit which vertical, and what to disclose alongside each.

5. **What external validation exists, and what is its scope?**
   A 2022 partnership with NCSU Wilson College of Textiles for dataset enrichment, publicly listed on the university's research projects page, and a 2022/2023 ISO 8559-1:2017 multi-company benchmark covering 14 companies and 8 countries. Not peer-reviewed, not third-party validated, not clinically certified.

6. **What is the data privacy and compliance posture?**
   HIPAA maintained, GDPR principles followed, TLS in transit, AWS S3 SSE-S3 at rest (always on), photo deletion immediate or within 30 days per client policy, no personal identifiers processed, auto-blur on retained photos.

7. **What catches a bad scan before it becomes a bad measurement?**
   Real-time skeletal tracking with red and green marker feedback and voice prompts, AI clothing detection with garment-aware shape correction, face obfuscation at capture.

8. **What is explicitly outside the scope of this product?**
   Medical advice, diagnosis, or treatment recommendations; medical device certifications (intentionally not pursued because the framework does not apply to what the product does); DEXA or InBody equivalence; peer-reviewed clinical validation. These are not gaps to be closed later — they are explicit scope boundaries.

---

## Disclaimer

3DLOOK's accuracy and repeatability figures cited throughout this article are derived from internal validation testing against 3DLOOK's proprietary datasets and reference measurements. They have not been externally validated through peer-reviewed research, third-party clinical studies, or independent regulatory evaluation. 3DLOOK measurements are designed to support workflow integration, longitudinal tracking, and use-case-specific decisions; they are not intended as a substitute for clinical examination, medical diagnosis, treatment recommendation, or any decision that requires a medical device under applicable regulatory frameworks. The demographic scope of 3DLOOK's internal validation dataset (ages 16 to 78, heights 150 to 205 cm, weights 38 to 210 kg, US and Europe) defines the population the accuracy figures apply to; performance outside this scope has not been characterized. Where direct comparative validation against a specific reference method (e.g., DEXA, BIA, calibrated scale, certified manual anthropometry) has not been completed, 3DLOOK should not be positioned as equivalent to that method.

---

## Frequently asked questions

**Is 3DLOOK clinically validated?**
No. 3DLOOK is not clinically validated, not peer-reviewed, not third-party validated, and not classified as a medical device. Internal validation against expert pattern-maker manual measurements shows approximately 96 to 97% measurement accuracy and above 95% repeatability — see Dimensions 1 and 2.

**Is 3DLOOK comparable to DEXA?**
No. DEXA is dual-energy X-ray attenuation imaging and serves as a clinical reference for body composition. 3DLOOK is a mobile vision-based measurement system designed for remote, repeated, longitudinal use. Different methodologies, different purposes — see the methods comparison section.

**Is 3DLOOK comparable to InBody or bioimpedance scales?**
No. Bioelectrical impedance analysis (including InBody) measures body composition through electrical impedance, while 3DLOOK estimates from body shape using the U.S. Navy formula — different operational contexts. See the body composition section.

**Can 3DLOOK replace a calibrated scale?**
No. Smart Scales is a weight estimation aid with an internal mean absolute error of 2.1 kg and 3.11% relative error. It is intended for contexts where a calibrated scale is unavailable or impractical, not as a replacement for one where calibrated weight is the requirement.

**What is the typical measurement error margin?**
1.5 to 2.0 cm typical absolute error per body part, with per-body-part variation from 0.54 cm at the wrist to 2.37 cm at back neck height on 3DLOOK's internal validation benchmark — see the Dimension 1 table for the full breakdown.

**Has the technology been peer-reviewed or third-party validated?**
No peer-reviewed publication specific to 3DLOOK's accuracy claims is on record. The 2022 NCSU partnership is dataset enrichment work, not independent validation. The ISO 8559-1:2017 multi-company benchmark is 3DLOOK-led — see Dimension 5.

**Does 3DLOOK work for every body type, age, and ethnicity?**
3DLOOK's internal validation dataset covers ages 16 to 78, heights 150 to 205 cm, weights 38 to 210 kg, US and Europe, with multi-ethnic and multi-occupation metadata — the disclosed population the measurement quality figures apply to. Use cases for populations outside this scope should be evaluated separately.

**Is patient data HIPAA-compliant?**
Yes. FitXpress maintains HIPAA compliance and follows GDPR principles. All data is encrypted in transit (TLS) and at rest (AWS S3 SSE-S3, always on). Photos are deleted immediately or within 30 days per client policy; retained photos are auto-blurred. Personal identifiers are not processed.

**Why no medical device certification?**
Since FitXpress does not provide medical advice, diagnosis, or treatment recommendations, medical device certifications do not apply. 3DLOOK is intentionally positioned as a workflow and data layer, not a medical device — see the compliance section.

---

*Author: Assel Sekerova. Last reviewed: May 2026.*
