# How 3DLOOK Works

## Capture flow (end user)

1. User stands in front and side positions
2. Takes two photos with any smartphone, fully clothed, any background
3. AI-powered pose validation engine guides positioning in real-time (skeletal tracking)
4. Real-time clothing detection flags loose / oversized clothing and prompts user to adjust
5. Face is automatically obfuscated for privacy
6. Photos sent to API → 3D model + measurements returned in under 45 seconds

## Backend pipeline

1. **Computer vision detection** — algorithms detect human body under clothing
2. **AI clothing detector** — classifies fit type (sport / regular / oversized) and adjusts 3D output
3. **Statistical generative human body model** (proprietary, patented) — creates 3D model
4. **Measurement extraction** — 80+ body measurements computed from the 3D model
5. **Body composition** — BMI, BMR, fat %, lean mass, fat mass derived from model
6. **Smart Scales (beta)** — cross-validates self-reported weight against the AI estimate, flags mismatch

## Outputs

- 3D body model (5M+ points per model in source data)
- 80+ measurements (chest, waist, hips, thigh, knee, calf, neck, bicep, wrist, etc., plus heights and lengths)
- Body composition: BMI, BMR, body fat %, lean body mass, fat body mass, essential fat, beneficial fat
- Validation messages (pose quality, clothing flags)
- Smart Scales weight estimation (with mismatch flag)
- Optional 3D goal visualization (target weight body model)
- Side-by-side progress comparison (longitudinal scans)

## Integration options

| Option | Description | When to use |
|--------|-------------|-------------|
| **API** | REST API, customize outputs, control rate limits | Headless integration, server-to-server |
| **Mobile Camera SDK (iOS)** | Native iOS SDK with pose/tilt validation | iOS apps that want guided capture |
| **Mobile Camera SDK (Android)** | Native Android SDK | Android apps |
| **Camera SDK (React)** | Web/React component | Web apps, hybrid apps |

**Recommendation:** integrate the Camera SDK (not just API). The SDK handles guided capture and pose/tilt validation, which is the single biggest factor in measurement accuracy. Customers who skip the SDK and roll their own capture see meaningfully worse accuracy.

## White-label customization

- **Yours to customize:** onboarding, scan entry point, consent/instructions, progress/loading, error handling, post-scan messaging, output UI (which metrics to show / hide / explain)
- **Not customizable (protected):** photo capture layer (pose/tilt validation in SDK) — required to protect measurement accuracy

Two integration patterns:
1. **Customer-branded UX** — host app fully owns onboarding and result display (e.g., digital health dashboard)
2. **Customer workflow** — scan triggered from any flow (verification, onboarding, progress tracking) — e.g., online pharmacy BMI verification step

## Photo and data handling

> Source: the live [Data, Privacy, Security & Regulatory FAQ](https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/) via `compliance.md` (rebuilt 2026-09-18). Full wording and the "never say" list live there.

- Data travels over TLS; data in Amazon S3 is encrypted with SSE-S3 (S3-managed keys), on by default. Hosting: AWS, primarily US-West-2, partially US-East-1
- Photos deleted immediately after processing or within 30 days, per customer policy; retained photos are automatically blurred and faces are obfuscated at capture
- Measurements, body composition estimates and 3D models are stored on an ongoing basis unless the customer agreement says otherwise; deletion is requested by scan identifier
- Scan records carry anonymized, randomly generated IDs; 3DLOOK cannot identify an individual from stored scan records. Body Progress compares two customer-selected scans; 3DLOOK does not track individuals
- HIPAA: supports HIPAA-governed deployments under an executed BAA (framework, not a certification). GDPR: "In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR." DPA with SCCs, UK Addendum where UK GDPR applies
- SOC 2: working toward an attestation report (not certified). Production customer data is not used to train models
- Regulatory: independent assessment, not a medical device under UK MDR / EU MDR; not cleared, authorized or approved by the FDA
- Contacts: documentation requests legal@3dlook.me; end-user privacy privacy@3dlook.me

## Training data foundation

- Collected over 9+ years
- Locations: US, Europe
- Demographics: ages 16-78, weight 38-210 kg, height 150-220 cm, 48% male / 52% female (height range confirmed by Vadim 2026-09-02, superseding the 150-205 cm figure)
- Composition: 150,000+ photographs, 30,000+ 3D scans, 430,000+ individual measurements
- Hardware reference scanner: 4 dynamic cameras, 86 parameters per person, including sitting position and breathing variations, 5M+ points per 3D model
- Photo flow simulation: 34 different photo configurations per user (distance, angle, slope, lighting variations)

This breadth of training data is part of what makes the body shape estimation robust to real-world variation in clothing, lighting, background, and pose.
