---
product: fitxpress
type: source-transcript
vertical: connected-and-digital-fitness
source: Drive "fitxpress-connected-fitness-final.html" (id 1vzIe1SmZH79lQ9b3uIQkgiXUFNarwaNG, uploaded by Vadim 2026-10-06 18:31), Nika's iteration on page.md v2
date: 2026-10-06
---

<!-- Visible text extracted from nika-final-2026-10-06.html for review and diffing. The HTML wins. -->

3DLOOK Book a demo
Home / FitXpress / FitXpress for Connected and Digital Fitness
FitXpress for connected and digital fitness
# Accurate body scanning for fitness apps that makes member progress measurable
A mobile alternative to the in-gym body scanner, built into your app. Two smartphone photos return 80+ body measurements and body composition estimates in under 45 seconds, giving members a clear, measured view of their progress.
Book a demo See what each scan returns →
A walkthrough on a phone, with a sample progress record.
Progress record Scan 4 · week 12
|  | Week 1 | Week 12 | Change |
| Entered weight | 82.4 kg | 82.1 kg | −0.3 kg |
| Body-fat estimate | 27.1% | 25.3% | −1.8 pts |
| Lean mass estimate | 60.1 kg | 61.3 kg | +1.2 kg |
| Waist | 92.0 cm | 88.6 cm | −3.4 cm |
The scale moved 0.3 kg. The waist moved 3.4 cm.
Pose passed Framing passed 2 photos
Illustrative member. Weight is entered; body composition values are estimates. Your platform configures what the member and the coach see.
2 photos front and side, on the member's own phone
Under 45 sec from the photos to structured results
Your app you decide what the member and the coach see
No integration fee plans from $1,000 a month
For your members
## Show members clear, measured progress at every check-in
Each scan gives members measured proof of change, even when the scale barely moves.
### Change the scale can't show
Waist, fat and lean-mass change appear in your app while weight stays flat.
### Progress kept in your app
A measured, comparable record replaces progress photos in the camera roll.
### Programs built on body data
Coaches and programs adjust to measured data along with the member's stated goal.
### A premium feature of its own
3D progress tracking and goal visualization give your paid tier a clear reason to upgrade.
Body data in fitness apps, in depth: AI in fitness →
Accuracy
## Measurements accurate enough to track real change
Each member is compared with their own earlier scans. Repeat scans differ by less than 1 cm, which keeps every comparison reliable.
< 1 cm
difference between repeat scans for most measurements, with 95%+ consistency
96–97%
accuracy against expert manual measurement
1.5–2.0 cm
typical absolute error, depending on the body part
| Measurement | Repeatability | Absolute error |
| Chest | 0.60 cm | 1.74 cm |
| Waist | 0.89 cm | 2.14 cm |
| Knee | 0.12 cm | 1.73 cm |
| Calf | 0.12 cm | 1.27 cm |
Conditions: form-fitting clothing, guided capture completed, height entered within 2 cm, and the same capture conditions between scans.
Figures from internal validation of body measurements across ages 16–78, heights 150–220 cm and weights 38–210 kg. They don't cover body composition estimates and haven't been peer-reviewed. Methodology is available under a non-disclosure agreement (NDA).
How to evaluate mobile body scanning accuracy →
Why 3DLOOK
## A body scanning partner your product team can rely on
100+ clients using 3DLOOK body scanning since 2016
99.5% uptime SLA, with service credits
2 days integration at its fastest, depending on your team's availability
- Under your brand. White-label by default. Members scan and see results inside your app, with no second app to install.
- Guided capture. Real-Time Pose Validation (RTPV) corrects pose and framing during the scan, reducing retakes with no manual review on your side.
- No hardware. Members scan on their own phone, at home or in the club, on iOS 15+ and Android, including older models.
- Every platform you ship on. API, native iOS and Android software development kits (SDKs), a React Native kit and web components.
- Hands-on support. Guided implementation on every plan, with a dedicated customer success manager.
How it works
## A two-photo scan inside your member flow
The scan fits into the check-ins your program already runs.
### The member scans at a moment the program already has, such as onboarding or a check-in week.
The consent screen belongs to your platform, in your own wording.
### Guided capture validates each photo.
Real-Time Pose Validation pauses capture until pose and framing requirements are met, with voice guidance for a member scanning alone. FitXpress returns clothing-related information for review.
### The progress screen shows the change.
FitXpress returns the record through its application programming interface (API) to the member profile, and the progress screen places two scans your platform selects side by side. In online coaching apps , the coach reviews the same record before setting the next program block.
Guided capture in detail: how the technology works →
The scan record
## What each scan returns to your platform
One timestamped record per scan, compared with earlier scans. You choose what the member and the coach see.
| Field | Returned output |
| Body measurements | 80+ measurements, including waist, hip, chest, thigh and calf |
| Body composition estimates | Body-fat percentage, lean mass and fat mass, which can change while weight stays flat |
| Calculated metrics | BMI and basal metabolic rate (BMR), an input for nutrition plans |
| 3D body model | A 3D model per scan. Pro adds 3D Body Progress tracking and 3D Goal Visualization |
| Quality and status | Pose and framing validation results, clothing-related information surfaced for review, and a timestamp |
FitXpress is not a medical device. It provides structured body data for coaching and program workflows.
Request a sample payload
Compare
## How FitXpress compares with other ways to track body progress
| Dimension | FitXpress | Weight log and progress photos | Standalone scanning app | In-gym body scanner |
| Where it happens | Inside your app, on the member's phone | At home | In a separate app | At the device, in the club |
| What it records | 80+ measurements, body composition estimates, a 3D model | Weight; photos aren't measured | Depends on the app | Circumferences, body composition or both, depending on the device |
| Your brand | White-label by default | In your app, unmeasured | The app's own brand | The device maker's interface |
| Data back to your platform | A structured record through the API | Self-reported weight | Depends on the app | Depends on the device |
FitXpress can also complement an in-gym scanner, covering check-ins at home and between club visits.
Data handling
## How member body data is handled
- Photos. Deleted right after processing or kept up to 30 days, per your contract. Faces are obfuscated at capture, and retained photos are blurred.
- IDs and GDPR roles. Each scan gets a random ID that your platform links to the member. In most deployments, you act as data controller and 3DLOOK as processor.
- Encryption and region. TLS in transit and encryption at rest. Data is processed and stored in AWS US West (Oregon).
- Model training. Customer data isn't used for training without your explicit, documented authorization.
Privacy contact: privacy@3dlook.me · Data, Privacy, Security & Regulatory FAQ →
Pricing
## Start with a pilot, then scale on a fixed monthly plan
Starter. $1,000 a month for up to 500 scans, with all body measurements, body composition estimates, API access, and web and mobile kits.
Pro. $1,500 a month for up to 1,000 scans, adding 3D Body Progress tracking and 3D Goal Visualization.
Custom plans cover higher volumes. No integration fee on any plan.
See pricing →
### Walkthrough.
We show the member flow on a phone, a sample payload and how FitXpress fits your app.
### Pilot cohort.
A group of members scans at your check-ins, with success criteria agreed upfront.
### Rollout.
The scan goes live across your member base on the plan that fits your volume.
Book a demo
FAQ
## Questions fitness and coaching teams ask
### Will adding a scan step reduce onboarding completion?
Capture takes two guided photos, and processing takes under 45 seconds. Real-Time Pose Validation guides pose and framing during capture, which reduces retakes. The scan runs inside a flow your platform already has.
### What is a body scan at the gym?
A body scan at the gym is a measurement taken on hardware in the club, such as a 3D camera booth or a bioelectrical impedance platform. Each repeat needs a club visit. FitXpress measures on the member's own phone instead.
### What body scanning SDKs work for fitness apps with remote users?
FitXpress offers web and mobile SDKs built for members who scan at home on their own phones. The platform designs onboarding, consent and results screens; the photo-capture layer, where pose validation runs, stays fixed to protect measurement quality.
### How large is the SDK, and which devices are supported?
The iOS device binary is about 40 MB (the arm64 slice is about 104 MB), with the machine learning models inside the framework. FitXpress supports iOS 15+ and Android, including older models, which may show lower frames per second during capture. Native kits capture offline; the web widget needs a connection.
### How are results delivered?
Each scan returns a structured record through the API, with JSON, CSV and 3D model export. Results arrive through webhook events. Webhooks have no automatic retries or signature verification today, and polling is the recommended backup.
### How often should members scan?
Members scan at each progress check-in the program already runs. Consistent conditions matter more than frequency: form-fitting clothing, the same place and the phone on a stable surface each time.
### Does the data sync to Apple Health or Health Connect?
The platform's own team builds and controls any sync to Apple Health or Health Connect. FitXpress returns structured data to the platform through the API, ready for that sync.
Book a demo
## See FitXpress in your member flow
A 30-minute demo: capture on a phone, the outputs your platform receives, and how integration fits your release schedule.
Not ready for a call? Start with AI in fitness .
Select
Under 500
500-1,000
1,000-5,000
Over 5,000
Not sure yet
I agree to 3DLOOK processing my details to respond to this request, as described in the privacy policy .
[BUTTON] Book a demo
Prototype mock. The live page embeds the shared HubSpot form.
© 2026 3DLOOK · FitXpress for connected and digital fitness Procurement and security documentation: legal@3dlook.me
