# Technical Spec (3DLOOK)

> For technical / integration-focused content. Used by `seo-section-writer` for technical articles, by `message-sequencer` when targeting technical buyers (VP Engineering, CTO, Head of Product Engineering).

## Integration options

### REST API
- Customize data outputs (which metrics returned)
- Control rate limits
- Server-to-server integration
- Authentication: API key
- Returns: 80+ measurements, BMI, BMR, fat %, lean mass, fat mass, predicted 3D model, validation messages, Smart Scales (beta)

### SDKs

| SDK | Platform | What it does |
|-----|----------|--------------|
| Mobile Camera SDK (iOS) | Native iOS (Swift) | Guided capture with real-time pose / tilt validation |
| Mobile Camera SDK (Android) | Native Android (Kotlin) | Same as iOS |
| Camera SDK (React) | React (web + hybrid) | Same capture experience for web apps |

**Key recommendation we always make:** integrate the SDK, not just API. Pose / tilt validation in the SDK is the single biggest factor in measurement accuracy. Customers who roll their own camera capture see meaningfully worse accuracy.

### What's customizable (white-label)

- **Onboarding** UX — fully yours
- **Scan entry point** — trigger from any flow (verification, onboarding, progress tracking)
- **Consent / instructions** — your wording, your flow
- **Progress / loading** screens — your design
- **Error handling** — your copy
- **Post-scan messaging** — fully yours
- **Output UI** — pick which metrics to display, hide, or only consume server-side

### What's NOT customizable (protected)

- **Photo capture layer** in the SDK — pose / tilt validation runs here
- This is by design — it protects measurement accuracy

## Capture flow technical details

### Real-time pose detection
- Skeletal tracking on-device or live in browser
- Validates body posture before each photo
- Reduces retakes
- Face obfuscation auto-applied for privacy

### Real-time clothing detection
- Classifies fit type per scan: `sport` / `regular` / `oversized`
- Flags inappropriate attire and prompts user
- Notifies clinical / business team via response payload
- Updated models coming Q3 2025

### Performance characteristics
- Time from photo to results: under 45 seconds
- Photos required: 2 (front + side)
- No background requirements (any background)
- Minimally affected by lighting
- Works on any smartphone camera

## Two integration patterns

### Pattern A: Customer-branded host app
Host app fully owns onboarding, scan entry, consent, progress display, results display. Scan triggered as one step in the broader user journey.

Examples:
- Digital health platform with internal patient assessment dashboard (3D model + 80+ measurements rendered in customer's UI)
- Online pharmacy embedding scan as a verification step in checkout

### Pattern B: Customer workflow (post-scan, no UI exposed to end user)
Customer collects scan, results consumed server-side only. End user sees "your photos are submitted" — body data feeds internal compliance / verification systems without being exposed.

Example: Online pharmacy BMI verification — user scans, results validate eligibility, body metrics never shown to user.

## Data and outputs in detail

### Measurements (80+)

Categories:
- **Circumferences (girth)**: chest, waist, mid-waist, lower waist, low hips, neck, bicep, knee, ankle, wrist, calf, thigh, mid-thigh, neck girth, neck girth relaxed, forearm, upper chest girth, elbow girth, abdomen, armscye girth, overarm girth
- **Front linear**: waist height, shoulders, waist linear, hips linear, body height, underarm length, neck linear, shoulder to waist, outseam, inseam, inside leg length, hip height, crotch length, sleeve length, shoulder centre back, nape to waist centre back, waist to low hips, waist to knees, bust height, shoulder slope, back neck height, back neck point to wrist length, upper hip height, across back width, outer ankle height, knee height, across back shoulder width, total crotch length, inside leg height, back neck to hip length, neck length, torso height, upper arm length, lower arm length, upper hip to hip length, back shoulder width, inside crotch length to mid-thigh, inside crotch length to knee, inside crotch length to calf, chest top, back crotch length, front crotch length, side neck point to armpit, side neck point to upper hip level, outseam from upper hip level, waist to upper knee length
- **Side linear**: side upper hip level to knee, side neck point to upper, neck to chest, chest to waist, waist to ankle, shoulders to knees, waist depth, neck side to waist back, axilla to waist side length

### Body composition outputs

- **BMI** (calculated from height + weight)
- **BMR** (basal metabolic rate, kcal/day)
- **Body fat %** (overall)
- **Lean body mass** (kg/lb)
- **Fat body mass** (kg/lb)
- **Essential fat** (% and kg)
- **Beneficial fat** (% and kg)
- **Unbeneficial fat** (% and kg)
- **Lean mass index** (kg/m²)
- **Fat mass index** (kg/m²)

### Validation outputs

- Pose quality score
- Clothing classification (sport / regular / oversized)
- Smart Scales weight estimate + mismatch flag (when self-reported weight provided)

### 3D model output

- 3D model in standard format
- Optional: target weight visualization (3D model at goal weight)
- Optional: side-by-side comparison (longitudinal scans)

## API endpoints (reference for technical articles)

(Specific endpoint paths are confidential — request from Vadim before publishing actual endpoint URLs in technical content. Use generic description: "POST scan endpoint accepting two photos, returns JSON with measurements + 3D model URL".)

## SDK examples (for technical content)

(Specific SDK code examples available on request from Vadim. Do not invent code.)

## Recommended capture environment

For best results (note in onboarding instructions):
- Phone placed vertically on a flat surface (table, counter)
- User stands in front and side positions
- Fully clothed (form-fitting or regular fit best — oversized gets flagged)
- Any background works
- Standard indoor lighting fine

## What to highlight in technical content

1. **No special hardware** — works with any smartphone camera
2. **Fast integration** — SDK in days, not months
3. **White-label flexibility** — you own the UX
4. **Privacy by design** — face obfuscation, photo deletion, no PII processing
5. **Production reliability** — 9+ years of training data, drift monitoring
