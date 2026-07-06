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

- Photos sent over TLS, stored on AWS S3 with mandatory SSE-S3 server-side encryption
- Photos deleted immediately after processing or within 30 days, per client policy
- When stored, photos are automatically blurred for additional privacy
- No personal identifiers / contact details processed — photos cannot be linked to individuals
- HIPAA compliant (US healthcare), follows GDPR principles (EU)
- Privacy contact: privacy@3dlook.me
- Not a medical device — no medical device certifications applicable, since FitXpress does not provide medical advice / diagnosis / treatment recommendations

## Training data foundation

- Collected over 9+ years
- Locations: US, Europe
- Demographics: ages 16-78, weight 38-210 kg, height 150-205 cm, 48% male / 52% female
- Composition: 150,000+ photographs, 30,000+ 3D scans, 430,000+ individual measurements
- Hardware reference scanner: 4 dynamic cameras, 86 parameters per person, including sitting position and breathing variations, 5M+ points per 3D model
- Photo flow simulation: 34 different photo configurations per user (distance, angle, slope, lighting variations)

This breadth of training data is part of what makes the body shape estimation robust to real-world variation in clothing, lighting, background, and pose.
