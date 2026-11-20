@@@ ajbednarek
hook: Caliber's app takes progress photo uploads and syncs body stats; Adam's React Native and native mobile background
proof: 2 photos, 80+ body measurements, scan ID (card Facts, Caliber Account facts)
--- M1
Hi Adam,

Caliber's app takes progress photo uploads and syncs body stats, and a photo shows visible change without giving the next progress review anything to measure against.

3DLOOK built FitXpress for that gap: a body scan SDK for iOS and Android. The member takes 2 photos, front and side, guided by pose and framing checks, and 80+ body measurements come back through the API as one timestamped record linked to the member by the scan ID.

With your React Native and native mobile background, what would building a capture SDK like that into the Caliber app take on your side?

Nick
--- M2
Hi Adam,

The capture layer stays fixed to protect measurement quality, and the onboarding, consent and results screens around it can be Caliber's own. The SDK and the API are meant to run together.

If that is worth a look, here is my calendar, or point me to whoever owns the progress screen in the app:
https://meetings.hubspot.com/nick-omelchak

Nick
@@@ thaovdoan
hook: Centr Coach tracks results and workout history; Thao's product development and quality engineering background
proof: 2 photos, 80+ body measurements, processing status, 100+ clients (card Facts, Centr Account facts)
--- M1
Hi Thao,

Training metrics show the work done and leave the body change unmeasured, and Centr Coach already tracks results and workout history.

FitXpress, from 3DLOOK, adds a body scan on the member's own phone: 2 photos with pose and framing guidance, and 80+ body measurements come back through the API as one record with its processing status.

With your product development and quality engineering background, what would it take to build that capture into Centr Coach as an SDK?

Nick
--- M2
Hi Thao,

A scan ID links each record to the member profile in Centr's own data. The web and mobile SDKs cover iOS and Android, with the screens around the capture in Centr's brand.

3DLOOK has worked with 100+ clients, including fitness teams.

Happy to walk through the setup on a call, or point me to whoever owns the Centr Coach member experience:
https://meetings.hubspot.com/nick-omelchak

Nick
@@@ thealexpoon
hook: Everfit's July 2026 release deepened synced data to body fat, weight and height
proof: 2 photos, 80+ body measurements, fat and lean mass estimates (card Facts, Everfit Account facts)
--- M1
Hi Alex,

Everfit's July release deepened synced data to body fat, weight and height, and those values exist only where a device or app sends them.

FitXpress, from 3DLOOK, fills that gap from the client's phone: 2 guided photos, front and side, return 80+ body measurements and fat and lean mass estimates through the API, one timestamped record per scan.

What would it take to build that capture SDK into the Everfit client app, with each coach's branding on the screens around it?

Nick
--- M2
Hi Alex,

Each record arrives with its processing status and a scan ID that your team links to the client profile. The coach and the client see the same record.

Pick a time here, or point me to whoever owns client progress in the product:
https://meetings.hubspot.com/nick-omelchak

Nick
@@@ philip-morton
hook: Exercise.com reworked its Measurements pages after user feedback (December 2025 changelog)
proof: 2 photos, 80+ body measurements, scan ID, 100+ clients (card Facts, Exercise.com Account facts)
--- M1
Hi Philip,

Exercise.com reworked its Measurements pages after user feedback, and typed fields hold only what a trainer or client enters.

FitXpress, from 3DLOOK, adds a body scan to the client's branded app: 2 photos, front and side, taken with pose and framing guidance, return 80+ body measurements as one timestamped record through the API, linked to the client profile by the scan ID.

Beyond typed fields and photos, what do trainers ask the platform to record about a client's progress?

Nick
--- M2
Hi Philip,

Fat and lean mass estimates come with the measurements, and a trainer can review them between sessions. 3DLOOK has worked with 100+ clients, including fitness teams.

Book a time here, or point me to whoever owns partner integrations at Exercise.com:
https://meetings.hubspot.com/nick-omelchak

Nick
@@@ sarah-miller-5960a690
hook: title only (Director of Trainer Success); the trainer's assessment with a new client
proof: 2 photos, 80+ body measurements, repeatability sentence (card Facts, Exercise.com Account facts)
--- M1
Hi Sarah,

At Exercise.com, a trainer's assessment with a new client usually rests on typed numbers and photos, and a photo shows change without a measurement to compare at the next progress update.

3DLOOK built FitXpress to put a guided body scan on the client's phone, inside the trainer's branded app. 2 photos return 80+ body measurements, including waist, hip and thigh, as one timestamped record.

When a trainer finishes an assessment, what do they use to set the first program?

Nick
--- M2
Hi Sarah,

The trainer and the client open the same record, and it can be compared from one progress update to the next, between sessions as well as at the assessment.

Repeated scans typically differ by less than 1 cm for most evaluated measurements.

Book a time to see it here:
https://meetings.hubspot.com/nick-omelchak

Nick
@@@ pete-wierzbinski-38153610
hook: Pete has been the primary Android developer at Lose It! since 2012 (bio); Premium typed body measurements
proof: 2 photos, 80+ body measurements, SDKs for iOS and Android (card Facts, Lose It! Account facts)
--- M1
Hi Pete,

Lose It! Premium members can type body measurements under Advanced Tracking, and tape placement varies from one weigh-in to the next.

FitXpress, from 3DLOOK, replaces typing with a guided body scan: 2 photos, front and side, return 80+ body measurements through the API, one timestamped record per scan, with SDKs for iOS and Android.

As the primary Android developer at Lose It! since 2012, what would building a capture SDK into the app take?

Nick
--- M2
Hi Pete,

The capture layer is fixed, and Lose It! would own the onboarding, consent and results screens around it. Each record carries its scan ID and processing status.

Book a time here, or point me to whoever owns Premium tracking features:
https://meetings.hubspot.com/nick-omelchak

Nick
@@@ sgaat
hook: MyFitnessPal's November 17 Weight Log release lets a member add a photo to a weigh-in; Sucharita's platform engineering title
proof: 2 photos, 80+ body measurements, API, scan ID (card Facts, MyFitnessPal Account facts)
--- M1
Hi Sucharita,

MyFitnessPal's new Weight Log allows a member to add a photo to a weigh-in, and a photo shows change without a measurement to compare later.

3DLOOK's FitXpress is a body scan SDK for the same moment: 2 guided photos, front and side, return 80+ body measurements through the API as one timestamped record.

What would building a capture SDK into the app take on the platform side?

Nick
--- M2
Hi Sucharita,

Each record comes back with a processing status and a scan ID that the platform links to the member profile. The web and mobile SDKs support iOS and Android.

Pick a time here, or point me to whoever owns progress in the app:
https://meetings.hubspot.com/nick-omelchak

Nick
@@@ vishuviswanathan
hook: the Trainerize client app already holds tape measurements and side-by-side progress photos
proof: 2 photos, 80+ body measurements, scan ID (card Facts, Trainerize Account facts)
--- M1
Hi Vishu,

The Trainerize client app already holds tape measurements and side-by-side progress photos, and photos show visible change without a measurement to compare.

3DLOOK's FitXpress adds a body scan SDK for iOS and Android: 2 guided photos, front and side, return 80+ body measurements through the API as one timestamped record, which Trainerize links to the client by the scan ID.

Which parts of the client app would a capture SDK touch first?

Nick
--- M2
Hi Vishu,

The capture layer stays fixed while the screens around it, onboarding, consent and results, carry the trainer's brand.

A call would settle the details, and if another team owns this, point me to whoever runs client progress tools in the product:
https://meetings.hubspot.com/nick-omelchak

Nick
@@@ len-bucchino
hook: trainers on Trainerize can run their own white-labeled iOS and Android client apps
proof: 2 photos, 80+ body measurements, API record (card Facts, Trainerize Account facts)
--- M1
Hi Len,

Trainers on Trainerize can run their own white-labeled iOS and Android client apps, and tape measurements typed there depend on where each client places the tape.

FitXpress, from 3DLOOK, offers one body scan integration for them: 2 photos taken with pose and framing guidance, front and side, return 80+ body measurements as one record through the API, with the screens around the capture in each trainer's brand.

What would it take to ship one capture SDK across every trainer's branded app?

Nick
--- M2
Hi Len,

Each record carries a processing status and a scan ID, and the SDKs support iOS and Android.

Book a time here, or point me to whoever owns partner integrations for Trainerize:
https://meetings.hubspot.com/nick-omelchak

Nick
