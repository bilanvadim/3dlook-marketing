# 2026-11-19-us-connected-fitness: all 150 pairs (109 approved 2026-11-20 + 41 top-up for review)

######## Peloton (50)

=== meghiggins21 | Meg Higgins | VP of Product | angle product P2
--- M1
Hi Meg,

Pace, form and rep counts record the work done, and what that work did to the body stays outside them.

Run Analysis already reads running form from the camera on the Vision models. FitXpress would give the Peloton app a body-side counterpart: the member takes 2 photos on their own phone, and a record with 80+ body measurements and fat and lean mass estimates lands in Peloton's own screens.

How does your team test a new onboarding step before it reaches members?

Nick
--- M2
Hi Meg,

For a progress screen, the record holds girths such as waist and thigh, along with fat and lean mass estimates. Repeated scans typically differ by less than 1 cm for most evaluated measurements.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

Worth a call to see what that could look like on a Peloton screen?
https://meetings.hubspot.com/nick-omelchak

Nick

=== francisshanahan | Francis Shanahan | Chief Technology Officer | angle referral P3
--- M1
Hi Francis,

Adding a body capture SDK to the Peloton app is an engineering question first. Progress photos and typed tape readings leave a team nothing structured to store.

3DLOOK builds FitXpress, a body scan SDK with web and mobile versions for iOS and Android, and the SDK and the API together are the recommended setup. The member takes 2 guided photos on their phone, the capture layer stays fixed, and a scan comes back as one timestamped record with 80+ body measurements, linked to the member profile by the scan ID.

What would it take to build a capture SDK like that into the Peloton app?

Nick
--- M2
Hi Francis,

On effort, a basic integration typically takes 2-4 weeks. Onboarding, consent and results screens stay in Peloton's own design.

Happy to walk your team through the setup on a call, or point me to whoever owns the member app's progress experience.
https://meetings.hubspot.com/nick-omelchak

Nick

=== nickcaldwell | Nick Caldwell | Chief Product Officer | angle product P2
--- M1
Hi Nick,

Peloton IQ builds personalized guidance around each member, and a strength block feeds it weights and reps. On a strength program the scale can hold steady while waist and lean mass move, and a rep log cannot show that.

3DLOOK built FitXpress as an SDK and API pair. The Peloton app starts a guided capture of 2 photos, and the API returns 80+ body measurements with fat and lean mass estimates, under Peloton's brand.

What does a member see after a strength block today, beyond the weights and the scale?

Nick
--- M2
Hi Nick,

On setup, the SDK and the API run together. The capture layer stays fixed to protect measurement quality, and the onboarding, consent and results screens stay Peloton's own. There is no integration fee.

If you want to see how it would map to your roadmap, grab a slot:
https://meetings.hubspot.com/nick-omelchak

Nick

=== nompute | Michael Lai | Director Of Engineering | angle referral P3
--- M1
Hi Michael,

Founding engineer, then VP of Engineering, now Director of Engineering at Peloton: that path stood out. A separate scanning app puts the member and the result under another brand, and what comes back depends on that app.

FitXpress from 3DLOOK is an SDK inside the host app. The member takes 2 photos on their phone, and the API returns a timestamped record with 80+ body measurements, linked to the member profile by the scan ID.

If your team built a capture flow like that into the Peloton app, which part would take longest?

Nick
--- M2
Hi Michael,

On data handling, photos are deleted after processing or kept up to 30 days under the company's own policy, and each scan carries a randomly generated identifier.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

I can go through it on a call, or point me to whoever owns onboarding in the member app.
https://meetings.hubspot.com/nick-omelchak

Nick

=== kmcnabb | Katie McNabb | Senior Director of Engineering | angle referral P3
--- M1
Hi Katie,

A guided photo capture in the Peloton iOS app raises a few engineering questions. Photos taken at home vary in pose, distance and light between check-ins.

FitXpress from 3DLOOK ships an iOS and Android SDK. The member gets pose and framing guidance during capture, and 2 front and side photos come back as one record of 80+ body measurements through the API, tied to the member by the scan ID.

How would your engineers approach building a guided photo capture into the Peloton app?

Nick
--- M2
Hi Katie,

Speed shapes a capture flow. A scan returns 80+ body measurements, under 45 seconds from the photos to structured results.

Happy to walk through the iOS side on a call, or point me to the product owner for onboarding.
https://meetings.hubspot.com/nick-omelchak

Nick

=== eugenekwak | Eugene K. | Vice President of Product Management | angle product P2
--- M1
Hi Eugene,

FitXpress is a body scan that runs inside a company's own app. In the Peloton app, 2 photos from the member would come back as 80+ body measurements and fat and lean mass estimates, shown on Peloton's own screens.

IQ Pace Targets set speed ranges from recent runs. A check-in built on training metrics records the work done, and the body change stays unmeasured.

Would a body scan fit better at the start of a running program or at its first review?

Nick
--- M2
Hi Eugene,

Every record is timestamped, which gives a running program a dated reference to compare against at its first review.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

Happy to walk through it on a call:
https://meetings.hubspot.com/nick-omelchak

Nick

=== laurarivera-uxresearch | Laura Rivera | Senior Director, User Research & Field Testing | angle referral P3
--- M1
Hi Laura,

Research and field testing sit close to how members describe their own progress. A progress photo shows visible change, and nothing in it can be measured against the next one.

3DLOOK's FitXpress turns 2 photos from a phone into something testers can compare: a timestamped record of 80+ body measurements and fat and lean mass estimates, shown in Peloton's own screens.

When members in field testing explain how they know they are progressing, what do they point to?

Nick
--- M2
Hi Laura,

The platform chooses which two scans are compared, and a tester's change between those check-ins shows up as a number on the screen.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

A short call would show what a tester sees. If whoever owns the progress experience is the better contact, tell me who and I will start there.
https://meetings.hubspot.com/nick-omelchak

Nick

=== joncilley | Jon Cilley | Director, Product Management | angle product P2
--- M1
Hi Jon,

Weight on a strength program can hold steady while the waist and the fat and lean mass shift, and a log of weights lifted leaves that unmeasured.

Strength+ reached Android this August after nearly two years on iPhone only. FitXpress comes as web and mobile SDKs with iOS and Android support, which allows the same body scan to sit in Peloton's Strength+ app on both platforms: 2 photos in, a record of 80+ body measurements back through the API.

Which of the onboarding and results screens around the capture would the Strength+ team want in its own brand?

Nick
--- M2
Hi Jon,

The capture runs on the member's own phone, and the record comes back to the app through the API. For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm.

If that fits the Strength+ team's plans, here is my calendar:
https://meetings.hubspot.com/nick-omelchak

Nick

=== mirelacialai | Mirela C. | Director Growth, Revenue and GTM | angle membership P3
--- M1
Hi Mirela,

Strength+ is included in the All-Access and App+ plans, which makes strength programs part of the paid offer. FitXpress gives that offer a body check-in: the member's own phone captures 2 photos, and Peloton receives one timestamped record with 80+ body measurements and fat and lean mass estimates.

A scale total on a strength program may stay flat while the waist shifts, and a rep log has no view of that.

What do members upgrade for today?

Nick
--- M2
Hi Mirela,

3D Body Progress tracking and 3D Goal Visualization are features of FitXpress's Pro plan. In a pilot, one cohort scans at onboarding and a comparable cohort keeps the usual flow, and free-to-premium conversion is compared between them against success criteria agreed beforehand.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

If the paid plan is your territory, I would like to go through the design on a call:
https://meetings.hubspot.com/nick-omelchak

Nick

=== theodorelui | Ted Lui | VP, Strategy and Business Excellence | angle referral P3
--- M1
Hi Ted,

A separate body-scanning app puts the member and the result under another brand, and what returns to the company depends on that app.

Peloton is pushing into running and strength at once, and both could use a body check-in under Peloton's own brand. 3DLOOK built FitXpress for that: it runs inside the existing app, and the API returns one structured record per scan with 80+ body measurements from 2 photos.

How does Peloton decide whether a new member feature earns a pilot?

Nick
--- M2
Hi Ted,

3DLOOK has worked with 100+ clients, including fitness teams. The scan runs under Peloton's brand, with Peloton's own onboarding, consent and results screens around it.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

Happy to talk it through on a call. If the paid plan belongs to someone else, a name is all I need.
https://meetings.hubspot.com/nick-omelchak

Nick

=== yasminkothari | Yasmin Kothari | Senior Director of Product Management | angle product P2
--- M1
Hi Yasmin,

Strength+ logs weights and reps, which shows a member progress in the lifts. Lifts record the work done, and the body change it is for needs its own record.

That is the gap 3DLOOK built FitXpress for. Two guided photos, front and side, and the Peloton app gets back 80+ body measurements through the API, along with fat and lean mass estimates.

Where do members keep progress photos or body numbers in the Peloton app today?

Nick
--- M2
Hi Yasmin,

Each record comes back with its processing status, which allows the app to confirm that a scan is final before the member sees it.

Would a short call on how that fits the app help?
https://meetings.hubspot.com/nick-omelchak

Nick

=== raulesantos | Raúl Santos | Director, Engineering | angle referral P3
--- M1
Hi Raúl,

Your headline on leading engineering teams through defined goals made me think of scope. A body check-in at Peloton could start narrow: one capture step and one record returned.

FitXpress from 3DLOOK is built that way. 2 guided photos on the member's phone, through an SDK in the app, and the API returns a timestamped record of 80+ body measurements with its processing status. A form holds what the member types in. The record holds measured values.

What would building a capture SDK like that into the app take, from scoping to release?

Nick
--- M2
Hi Raúl,

A first release can stay small: the capture, the record, and a consent screen in Peloton's own wording.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

I can talk through scope on a call, or point me to whoever owns the member app's progress experience.
https://meetings.hubspot.com/nick-omelchak

Nick

=== bethraewendt | Beth Wendt | Director, User Research - Connected Fitness | angle referral P3
--- M1
Hi Beth,

Connected fitness research at Peloton needs a check-in that can be repeated session after session. A check-in form holds what the member enters, and nothing about the body is measured in it.

FitXpress guides the member through 2 photos with pose and framing guidance, and the Peloton app gets 80+ body measurements back in one timestamped record.

If a study could repeat that check-in, what would you want it to compare first?

Nick
--- M2
Hi Beth,

Each record is linked to the member profile through the scan ID, which allows a test to compare one tester's check-ins over time.

Happy to set up a call on how that would work in a test. If another team runs onboarding, a name from you works too.
https://meetings.hubspot.com/nick-omelchak

Nick

=== tworetzky | Brent Tworetzky | SVP Product | angle product P2
--- M1
Hi Brent,

A weigh-in gives one total, often self-reported, and where the body changed stays unknown.

Peloton IQ suggests weights from what a member lifts. A scan from FitXpress would give the product a second input: a timestamped record, linked to the member profile by the scan ID, with 80+ body measurements and fat and lean mass estimates from 2 photos.

Which roadmap item would a measured check-in serve first at Peloton?

Nick
--- M2
Hi Brent,

A pilot would compare day-90 retention between a member cohort that scans at onboarding and a comparable cohort on the usual flow, against success criteria agreed before it starts.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

If a call would help shape that design, here is my calendar:
https://meetings.hubspot.com/nick-omelchak

Nick

=== cole-shipley | Cole Shipley | Director of Product Management | angle product P3
--- M1
Hi Cole,

The Peloton member app's progress screen is where a body record would show up. FitXpress feeds that screen through the API, turning 2 photos taken on a phone into 80+ body measurements and fat and lean mass estimates, each record linked to the member profile by the scan ID.

A weigh-in gives one total with no map of where the body changed.

How does an idea for the progress screen travel from a platform team to the member app?

Nick
--- M2
Hi Cole,

The body scan returns 80+ body measurements, under 45 seconds from the photos to structured results.

A progress screen could show chest and thigh changes between two scans, with fat and lean mass estimates beside them.

Whoever owns the progress screen is welcome on the call too, and a name from your side is enough if that is easier:
https://meetings.hubspot.com/nick-omelchak

Nick

=== barbarathornethomsen | Barbara Thorne-Thomsen | Director, Strategy and Operations | angle referral P3
--- M1
Hi Barbara,

For program and transformation work, FitXpress is a contained piece to scope. It runs inside the Peloton app on 2 photos and returns 80+ body measurements and fat and lean mass estimates through the API.

Photos track how a member looks, and no figure sits behind them to compare at the next check-in.

When a new member capability is piloted at Peloton, how is the pilot scoped before it widens?

Nick
--- M2
Hi Barbara,

There were 112,100 scans in 2025 across all 3DLOOK customers.

A first piece can stay small: guided capture in the app, one structured record per scan through the API, and Peloton's own consent and results screens around it.

A short call could scope the first piece. If the paid plan is where it would live, a pointer to whoever runs it is all I need.
https://meetings.hubspot.com/nick-omelchak

Nick

=== sarah-rodenberg | Sarah Rodenberg | Director of Business Transformation & Strategic Projects | angle referral P3
--- M1
Hi Sarah,

Tape placement and lighting vary each time a member measures at home, which makes the numbers hard to line up.

Strength+ runs self-paced multi-week strength programs. FitXpress would give them a measured record at each check-in: 2 guided photos from a phone, and the Peloton app receives 80+ body measurements through the API.

When a member finishes a multi-week Strength+ program, what does the team look at to judge that it worked?

Nick
--- M2
Hi Sarah,

Photos are deleted after processing or kept up to 30 days under the company's policy, with blurring and face obfuscation.

Easy to go through on a call. If partner integrations are handled elsewhere, point me to that owner.
https://meetings.hubspot.com/nick-omelchak

Nick

=== kavitajv | Kavita Vemishetti | Vice President, Global Program Management | angle referral P3
--- M1
Hi Kavita,

Peloton has several member-facing programs in motion, from IQ running features to Strength+ on Android. 3DLOOK's FitXpress would join them as one more capability inside the Peloton app: 2 photos from a phone, and a record of 80+ body measurements and fat and lean mass estimates back through the API.

A standalone scanning app takes the member to another brand, and what returns to the platform depends on that app.

Across running and strength, where does a member most want to see body change?

Nick
--- M2
Hi Kavita,

Each record carries a scan ID that the platform maps to the member profile, which gives a program team one key across systems.

Glad to share the integration steps on a call. If onboarding is run by another team, an introduction would help.
https://meetings.hubspot.com/nick-omelchak

Nick

=== mottaqui-karim | Taq Karim | Sr. Director, Engineering | angle referral P3
--- M1
Hi Taq,

Your bio mentions a sequence of yours that the OEIS accepted. Here is a definition problem from my field: a weigh-in gives one total, and where the body changed stays unknown.

3DLOOK built FitXpress to return the where. The member takes 2 photos on their phone through an SDK in the app, and the API sends back a timestamped record with 80+ body measurements and fat and lean mass estimates, linked by the scan ID.

How would you size building a capture SDK like that into the Peloton app?

Nick
--- M2
Hi Taq,

On definitions, the 80+ body measurements are girths, lengths and widths. BMI and BMR are calculated metrics, and fat and lean mass are estimates derived from the measurements with height and, where provided, weight. Methodology is available under NDA.

Happy to go deeper on a call, or point me to whoever owns onboarding in the member app.
https://meetings.hubspot.com/nick-omelchak

Nick

=== lindsay-pontello | Lindsay Pontello | Senior Director, Strategy & BizOps | angle referral P3
--- M1
Hi Lindsay,

FitXpress could put a body scan inside the Peloton app. The member shoots 2 photos, and 80+ body measurements and fat and lean mass estimates return as one record through the API.

Peloton's strength push now spans Strength+ programs and IQ guidance. The scale reports one figure for the whole body and says little about where change happened.

What would a strength member need to see after a program block for the push to look like it is working?

Nick
--- M2
Hi Lindsay,

Fat and lean mass come as estimates derived from the measurements with height and, where provided, weight, and a progress view could show them beside waist and hip.

I can show it on a call. If the progress experience belongs to another team, just say who and I will go there.
https://meetings.hubspot.com/nick-omelchak

Nick

=== brad-fagan-8382a888 | Brad Fagan | VP, Global Head of Strategic Partnerships & Corporate Development | angle partnership P3
--- M1
Hi Brad,

One integration would bring 3DLOOK's FitXpress body scan to the Peloton app, with 2 photos in, 80+ body measurements out through the API, and the app's own screens around it.

An outside scanning app shows its own brand to the member, and the data that reaches the platform follows that app's format.

With product marketing for the Peloton App in your background, how does a partner capability get into the app today?

Nick
--- M2
Hi Brad,

The integration ships as web and mobile SDKs with iOS and Android support. FitXpress is not a medical device. It provides structured body data for coaching and program workflows.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

If it is worth a conversation, grab a time:
https://meetings.hubspot.com/nick-omelchak

Nick

=== jacob-wax-b2218295 | Jacob Wax | Director, Corporate Development and Strategic Partnerships | angle partnership P3
--- M1
Hi Jacob,

Strength and running both sit in the Peloton app, and one body-scan integration could serve both. FitXpress returns one structured record per scan through the API, from 2 photos, with 80+ body measurements inside it.

Side-by-side photos show the change by eye, with no measurement to check it against.

What do members ask for most around progress in the app?

Nick
--- M2
Hi Jacob,

In a pilot, onboarding completion would be compared for members who scan at the first check-in and a comparable group on the usual flow, with success criteria agreed up front.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

Open to a call on what an integration would look like?
https://meetings.hubspot.com/nick-omelchak

Nick

=== joeli-spencer-5bab67167 | Joeli Spencer | Director, Strategic Partnerships | angle partnership P3
--- M1
Hi Joeli,

Photos and tape taken at home shift with angle and light, which makes check-ins hard to compare.

Classes, outdoor activities and stats already fill the Peloton app. FitXpress is a partner capability that would sit beside them, a guided scan from 2 photos on a phone that returns 80+ body measurements in screens that carry Peloton's brand.

Where would a body record sit most naturally in the app, beside class stats or on a screen of its own?

Nick
--- M2
Hi Joeli,

There is no integration fee. The scan runs on the member's phone with no hardware, under Peloton's brand.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

Happy to compare notes on a call:
https://meetings.hubspot.com/nick-omelchak

Nick

=== ashlynmusillo | Ashlyn Musillo | Senior Director, Programming & Fitness Development | angle coaching P2
--- M1
Hi Ashlyn,

Your move from Programming to Fitness Development at Peloton comes at a good time. Strength+ now runs self-paced multi-week programs, and a weight reading is the usual way to see how a block went.

On a strength program that total can hold steady while waist and lean mass shift underneath it. 3DLOOK built FitXpress for that gap: 2 guided photos on the member's phone, front and side, return 80+ body measurements and fat and lean mass estimates as one timestamped record, linked to the member profile by the scan ID.

What does the programming team look at today to judge how a block landed?

Nick
--- M2
Hi Ashlyn,

Programs get judged on what the member did. A body scan adds what changed, as one timestamped record that the instructor and the member could both see from block to block.

Repeated scans typically differ by less than 1 cm for most evaluated measurements.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

Happy to walk through how it would fit a program block on a call.
https://meetings.hubspot.com/nick-omelchak

Nick

=== juliannaslaten | Julianna Slaten | Director, Programming | angle coaching P2
--- M1
Hi Julianna,

The Peloton app tracks classes, outdoor activities and stats, and those describe the work a member did.

They say little about the body change that work is for. FitXpress, built by 3DLOOK, adds a body scan inside the Peloton app. The member takes 2 photos on their own phone, and the app gets back 80+ body measurements along with body-fat and lean mass estimates, under Peloton's brand.

How does the programming team learn whether a schedule is moving members toward what they joined for?

Nick
--- M2
Hi Julianna,

For a program director, the useful part is the before and after of a block: waist and thigh girths with fat and lean mass estimates, returned through the API with the scan ID.

3DLOOK has worked with 100+ clients, including fitness teams.

I can show how that reads on a call.
https://meetings.hubspot.com/nick-omelchak

Nick

=== lauren-peters34 | Lauren Peters | Director of Product | angle product P2
--- M1
Hi Lauren,

Got me thinking, your path from Senior PM to Group PM to Director of Product at Peloton. New member steps usually get tested before a rollout, and a self-reported form is what most onboarding flows hold today.

FitXpress from 3DLOOK adds a body scan step: 2 guided photos on the member's phone, with pose and framing guidance, and the app receives 80+ body measurements as a timestamped record linked by the scan ID. Onboarding, consent and results screens stay Peloton's own, while the capture layer stays fixed.

How does your team test a new onboarding step before it ships?

Nick
--- M2
Hi Lauren,

On the build side, web and mobile SDKs cover iOS and Android, and the SDK and the API together are the recommended setup. A scan returns 80+ body measurements, under 45 seconds from the photos to structured results.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

If a call would help scope the onboarding step, my calendar is below.
https://meetings.hubspot.com/nick-omelchak

Nick

=== evie-mcquiston-2a417292 | Evie McQuiston | Group Product Manager | angle product P2
--- M1
Hi Evie,

Your headline on building products that scale across teams and surfaces. A body check-in would reach more than one surface, and photos or typed tape readings give those surfaces no measured comparison from one check-in to the next.

FitXpress from 3DLOOK returns one timestamped record per scan through the API, linked to the member profile by the scan ID, from 2 guided photos on the member's phone. 80+ body measurements sit in it, along with fat and lean mass estimates.

Which screens around a fixed capture, such as consent and results, would your team want in Peloton's own design?

Nick
--- M2
Hi Evie,

One detail for a platform owner: each record carries a processing status, which allows a surface to separate a finished scan from one still processing.

3DLOOK has worked with 100+ clients, including fitness teams. I would like to show the setup on a call.
https://meetings.hubspot.com/nick-omelchak

Nick

=== renato-moratore-b3089b134 | Renato Moratore | Principal Product Manager | angle product P3
--- M1
Hi Renato,

From Product Manager through Lead and Senior to Principal at Peloton is a long run. Progress in a member app often means photos, and a photo shows visible change with no measurement to compare at the next check-in.

FitXpress from 3DLOOK returns the measurement: 2 guided photos on the member's phone, and 80+ body measurements with fat and lean mass estimates come back through the API as one timestamped record.

How does the app keep progress photos or measurements today?

Nick
--- M2
Hi Renato,

Each scan record links to the member profile through the scan ID, and the platform chooses which scans a member sees compared.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

Happy to show it on a call, or point me to whoever owns the member app's progress experience.
https://meetings.hubspot.com/nick-omelchak

Nick

=== mario-joseph-pasquino | Mario Pasquino | Group Product Manager, Commerce | angle product P3
--- M1
Hi Mario,

Your headline on conversion and subscription growth got me thinking about what a premium plan at Peloton can show beyond workout stats and a weigh-in total.

3DLOOK built FitXpress for that. The member takes 2 guided photos on their phone, and the app gets 80+ body measurements back through the API. On the Pro plan, 3D Body Progress tracking and 3D Goal Visualization show measured change between check-ins.

How does your team judge a new paid feature before rollout?

Nick
--- M2
Hi Mario,

A pilot could compare day-30 retention between a cohort that scans at onboarding and a comparable cohort on the usual flow, against success criteria agreed before it starts.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

Happy to talk it through on a call, or point me to whoever owns the paid plan.
https://meetings.hubspot.com/nick-omelchak

Nick

=== allisonschloss | Allison Schloss | Director of Product Management | angle product P2
--- M1
Hi Allison,

You have moved through every PM level at Peloton, which means you know how the member app reads from the inside. A weigh-in is the usual progress marker next to workouts: one total, with no sign of where the body changed.

3DLOOK built FitXpress to show where. The member takes 2 photos, front and side, on their phone inside the app, and Peloton gets back 80+ body measurements and body composition estimates in one timestamped record. A progress screen could show waist and thigh change between check-ins.

What does a member see at a first check-in today beyond workouts and weight?

Nick
--- M2
Hi Allison,

A detail for the paid plan: on the Pro plan, 3D Body Progress tracking and 3D Goal Visualization show measured change between two scans that the platform selects.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

Glad to show it on a call.
https://meetings.hubspot.com/nick-omelchak

Nick

=== clarissa-woods-16a60b12 | Clarissa Woods | Senior Product Manager | angle product P3
--- M1
Hi Clarissa,

Your headline about technology and design connecting the world through fitness stood out. For a body check-in, design is the open question: photos taken at home vary in pose and light. The capture has to stay fixed, while the screens around it can be Peloton's own.

FitXpress from 3DLOOK works that way. The member takes 2 guided photos on their phone, with pose and framing guidance, and the API returns 80+ body measurements as a timestamped record linked by the scan ID.

Which screens around a fixed capture, such as consent and results, would your team want in Peloton's own design?

Nick
--- M2
Hi Clarissa,

Beyond the capture, the design work stays with Peloton. The record carries waist and thigh girths and fat and lean mass estimates for those screens.

3DLOOK has worked with 100+ clients, including fitness teams. Happy to talk it through on a call, or point me to whoever owns onboarding in the app.
https://meetings.hubspot.com/nick-omelchak

Nick

=== miranda-cl-evans | Miranda Evans | Senior Product Manager | angle product P3
--- M1
Hi Miranda,

Noticed that you started in member experience analysis before moving into product at Peloton. A weigh-in is a total that members often report themselves, and it says little about where the body changed.

FitXpress from 3DLOOK returns a measured record: 2 photos on the member's phone, 80+ body measurements with fat and lean mass estimates, and a scan ID that links the record to the member profile. On the Pro plan, 3D Body Progress tracking shows change between two scans the platform selects.

Which membership plans carry progress features in the app today?

Nick
--- M2
Hi Miranda,

For a paid membership, 3D Goal Visualization on the Pro plan sits beside 3D Body Progress tracking. The plan carries a goal view along with the comparison.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

I can show both on a call, or point me to whoever owns the paid plan.
https://meetings.hubspot.com/nick-omelchak

Nick

=== crystal-qin | Crystal Qin | Product | angle product P3
--- M1
Hi Crystal,

Quick idea for you, from your growth product background at Peloton: new steps in an onboarding flow earn their place through a test, and a form the member fills in is the usual data point there.

FitXpress from 3DLOOK is a body scan step that could go through the same test: 2 guided photos on the member's phone, 80+ body measurements back through the API, and a timestamped record linked by the scan ID.

How does your team test a new step in onboarding?

Nick
--- M2
Hi Crystal,

The step is short for the member. A scan returns 80+ body measurements, under 45 seconds from the photos to structured results.

If a call helps, calendar below, or point me to whoever owns onboarding.
https://meetings.hubspot.com/nick-omelchak

Nick

=== bfoncillas | Blanca Foncillas | Senior Product Manager | angle product P3
--- M1
Hi Blanca,

Had a thought after seeing your move from head of product at a wellness app to Senior PM at Peloton. Home photos and tape readings differ in pose, distance and light from one check-in to the next.

FitXpress from 3DLOOK guides a front and side capture on the member's phone and returns 80+ body measurements with body-fat and lean mass estimates as one timestamped record through the API.

In your view, does a scan belong at onboarding or at the first check-in?

Nick
--- M2
Hi Blanca,

Peloton's own onboarding, consent and results screens would wrap the capture, with the record landing under the member's profile through the scan ID.

3DLOOK has worked with 100+ clients, including fitness teams. Happy to show it on a call, or point me to whoever owns onboarding.
https://meetings.hubspot.com/nick-omelchak

Nick

=== nolan-bishop | Nolan Bishop | Senior Product Manager | angle product P3
--- M1
Hi Nolan,

Your headline on 0 to 1 software products in AI and IoT caught my eye. A separate scanning app puts the member and the result under another brand, and what comes back depends on that app.

FitXpress from 3DLOOK is an SDK inside the host app, with no hardware. The member takes 2 photos on their phone, and the API returns 80+ body measurements as one timestamped record.

When a new capability reaches a Peloton app, how does the team decide between building it and adding an SDK?

Nick
--- M2
Hi Nolan,

Web and mobile SDKs cover iOS and Android, and the SDK and the API together are the recommended setup.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

Happy to go through it on a call, or point me to whoever owns partner integrations.
https://meetings.hubspot.com/nick-omelchak

Nick

=== emilygaffney | Emily Gaffney | Vice President, Content Programming & Operations | angle coaching P2
--- M1
Hi Emily,

Spotted that you run content programming and operations, after leading programming globally at Peloton. A series gets judged on what members complete, while body change usually shows up as a photo or a tape reading taken at home, where pose, distance and light vary.

FitXpress from 3DLOOK guides the capture instead of leaving it to the member: 2 photos in the Peloton app with pose and framing guidance, and 80+ body measurements come back through the API as one record.

When a series wraps, what tells the content team it did what it was built for?

Nick
--- M2
Hi Emily,

A series owner could see body change across a program in one view: the member's scans, picked by the platform, with waist and thigh girths next to fat and lean mass estimates.

There is no integration fee.

I can walk through it on a call.
https://meetings.hubspot.com/nick-omelchak

Nick

=== caitlin-borisjuk-20284723 | Caitlin Borisjuk | Senior Director, Membership Strategy and Engagement | angle membership P3
--- M1
Hi Caitlin,

Membership strategy at Peloton starts with what a new member sees in the first month. A new member's first month usually shows workout counts and a self-reported weight, and little that is measured about the body.

FitXpress from 3DLOOK adds a body scan to that month: 2 guided photos on the member's phone inside the app, 80+ body measurements, body-fat and lean mass estimates, and one timestamped record linked to the member profile by the scan ID.

Which moment in a member's first month does your team watch most closely?

Nick
--- M2
Hi Caitlin,

A pilot would put one member cohort through a scan at onboarding and at the first check-in, with a comparable cohort on the usual flow, assigned at random where practical. Day-30 and day-90 retention are compared, along with scan completion and retakes in the scan cohort, against success criteria agreed before it starts. It makes no decision about any member.

Happy to walk through it on a call, or point me to whoever owns the paid plan.
https://meetings.hubspot.com/nick-omelchak

Nick

=== kelsi-farmer-ba097a4b | Kelsi Farmer | Senior Product Manager, eComm | angle product P3
--- M1
Hi Kelsi,

Your route from finance transformation into eComm product at Peloton. Progress photos show visible change and carry no measurement that a member can compare at the next check-in.

FitXpress from 3DLOOK adds the measurement: 2 guided photos on the member's phone, 80+ body measurements and fat and lean mass estimates, returned through the API as a timestamped record.

What do members ask Peloton for most when it comes to seeing their progress?

Nick
--- M2
Hi Kelsi,

The recommended setup pairs the SDK with the API, and the same record can feed screens in more than one place in the app.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

I can walk through it on a call, or point me to whoever owns the paid plan.
https://meetings.hubspot.com/nick-omelchak

Nick

=== michaelnortiz | Michael Ortiz | Fitness Development, Content & Programming | angle coaching P3
--- M1
Hi Michael,

Peloton programs are described to members through class stats, which show the work done.

FitXpress from 3DLOOK adds the body side: the member takes 2 photos on their phone in the app, and 80+ body measurements come back as one timestamped record through the API, with fat and lean mass estimates.

What does a finished block give an instructor to review today?

Nick
--- M2
Hi Michael,

Between program blocks, a guided capture on the member's phone gives the instructor and the member one record to look at together.

Repeated scans typically differ by less than 1 cm for most evaluated measurements.

Calendar below if a call makes sense, or point me to whoever sets the program schedule.
https://meetings.hubspot.com/nick-omelchak

Nick

=== jamescarrozza | James Carrozza | SVP, Global Operations & Member Experience | angle referral P3
--- M1
Hi James,

The member-first line in your headline, and that member experience now sits with global operations at Peloton. When a member wonders whether a program is working, workout stats and a weigh-in total are the usual answers.

FitXpress from 3DLOOK adds a measured answer inside the app: 2 photos on the member's phone, 80+ body measurements and fat and lean mass estimates returned as one timestamped record linked by the scan ID.

When members ask about their results, what do they get pointed to today?

Nick
--- M2
Hi James,

Photos are deleted after processing or kept up to 30 days under the company's own policy, and each scan carries a randomly generated identifier.

Happy to explain the setup on a call, or point me to whoever owns the member app's progress experience.
https://meetings.hubspot.com/nick-omelchak

Nick

=== uclahill | Amanda Hill | Senior Vice President, Global Content Strategy & Programming | angle coaching P2
--- M1
Hi Amanda,

Came across your work on global content and instructor strategy at Peloton. Instructors lead the programs members follow, and the progress picture they work from today is the member's own report and the workout stats.

FitXpress, the body scan layer from 3DLOOK, gives a program a measured point as well: 2 photos on the member's phone, 80+ body measurements and fat and lean mass estimates, returned through the API as a timestamped record in Peloton's own screens.

What would you want instructor-led programs to show about a member's progress beyond the stats?

Nick
--- M2
Hi Amanda,

Programs would stay as they are, with a measured point beside the stats. Peloton's brand, consent text and results screens wrap a capture layer that stays fixed.

112,100 scans in 2025 across all 3DLOOK customers.

I can walk through the setup on a call.
https://meetings.hubspot.com/nick-omelchak

Nick

=== mollyhallahan | Molly Hallahan | Product Manager | angle product P3
--- M1
Hi Molly,

Curious about your take, given your earlier senior PM roles at member-facing health apps and now Peloton. Typed numbers differ from person to person, and a photo shows change without a measurement.

FitXpress from 3DLOOK puts a body scan in the app under Peloton's brand: 2 guided photos on the member's phone, and 80+ body measurements come back through the API as a timestamped record linked by the scan ID.

Which screens around a fixed capture would your team want in Peloton's own brand?

Nick
--- M2
Hi Molly,

The consent screen can carry Peloton's own wording, and the record returns fat and lean mass estimates for the results screen.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

I can show how that fits on a call, or point me to whoever owns onboarding.
https://meetings.hubspot.com/nick-omelchak

Nick

=== tobyj | Toby Jones | Product Manager | angle product P3
--- M1
Hi Toby,

Your route from lifecycle and CRM into product at Peloton got me thinking about what a member message can say about progress. Most of it comes from workouts and weigh-ins, which are totals.

3DLOOK built FitXpress to add measured change. The member takes 2 photos on their phone in the app, and the API returns 80+ body measurements as a timestamped record, linked to the member profile by the scan ID.

How do you judge a new member feature before rollout?

Nick
--- M2
Hi Toby,

If it helps to see it measured, a pilot could compare day-90 retention between a cohort that scans and a comparable cohort on the usual flow, against success criteria agreed before it starts.

Happy to talk it through on a call, or point me to whoever owns the paid plan.
https://meetings.hubspot.com/nick-omelchak

Nick

=== nimit-shah-b2b6a744 | Nimit Shah | Product | angle product P3
--- M1
Hi Nimit,

Reacting to your move from product work at Facebook to Peloton. A separate scanning app puts the member and the result under another brand, and what comes back depends on that app.

FitXpress from 3DLOOK runs inside the member app with white-label screens: 2 guided photos on the member's phone, 80+ body measurements through the API, and a scan ID that links each record to the member profile.

How does a partner capability enter the Peloton app today?

Nick
--- M2
Hi Nimit,

Mobile SDKs cover iOS and Android, with web as well, and the screens carry Peloton's branding.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

I can walk through it on a call, or point me to whoever owns partner integrations.
https://meetings.hubspot.com/nick-omelchak

Nick

=== greetingsmj | MJ Kim | Product | angle product P2
--- M1
Hi MJ,

Onboarding at Peloton is where a member first gives the app any data about their body. At that step the data is usually what the member types in, a goal and a weight, which covers only what the member enters.

FitXpress from 3DLOOK could add a body scan there: 2 guided photos on the member's phone, 80+ body measurements, and a timestamped record that the app links to the member profile through the scan ID.

In your view, does a scan belong at onboarding or at the first check-in?

Nick
--- M2
Hi MJ,

For onboarding, a pilot would compare onboarding completion between a cohort that scans and a comparable cohort on the usual flow, against success criteria agreed before it starts.

Calendar below if a call makes sense.
https://meetings.hubspot.com/nick-omelchak

Nick

=== jonanglee | Jonathan Lee | Product Manager | angle product P3
--- M1
Hi Jonathan,

Peloton generates a lot of data on training. Training metrics describe the work done and leave the body's response outside the data.

FitXpress from 3DLOOK adds a structured body record: 2 guided photos on the member's phone, 80+ body measurements, and fat and lean mass estimates that the API returns with the scan ID.

What would you need to see in a body record before it shaped a program?

Nick
--- M2
Hi Jonathan,

The measurements are girths, lengths and widths, and fat and lean mass are estimates derived from them with height and, where provided, weight.

Repeated scans typically differ by less than 1 cm for most evaluated measurements.

Calendar below if a call makes sense, or point me to whoever owns the coaching programs.
https://meetings.hubspot.com/nick-omelchak

Nick

=== jacquelyn-zaydel | Jacquelyn Zaydel | Product Manager, Workout Experience | angle product P2
--- M1
Hi Jacquelyn,

Your move into workout experience, after member-experience product roles in health, caught my eye. Workout stats describe the effort, and a progress screen that also shows body change needs a measured record.

FitXpress from 3DLOOK provides it: the member takes 2 photos on their phone in the Peloton app, and 80+ body measurements come back through the API in one timestamped record, with fat and lean mass estimates.

Does the app hold any body measurements for a member today, or only workout stats?

Nick
--- M2
Hi Jacquelyn,

A progress screen could show waist and thigh change next to fat and lean mass estimates, with Peloton's own consent screen in front of the capture.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

Happy to show a mock of that on a call.
https://meetings.hubspot.com/nick-omelchak

Nick

=== rebeccayou | Rebecca You | Product Manager, Content Tooling & Studio Platform | angle product P3
--- M1
Hi Rebecca,

You own Content Tooling and Studio Platform at Peloton, which sits next to programming. A program is usually judged on completion, and the body change behind it goes unmeasured.

FitXpress from 3DLOOK adds a body scan to a program's flow: the member takes 2 photos on their phone, and 80+ body measurements come back through the API as one timestamped record.

How often is a program block reviewed, and with what?

Nick
--- M2
Hi Rebecca,

A guided capture between program blocks gives the programming team a record to compare from one block to the next.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

I can show it on a call, or point me to whoever owns the program schedule.
https://meetings.hubspot.com/nick-omelchak

Nick

=== shirley-wang-9624abab | Shirley Wang | Product Manager | angle product P3
--- M1
Hi Shirley,

Your product background in a consumer subscription app before Peloton stood out. In a subscription app, progress often reads as one total, and a total hides where the body changed.

3DLOOK built FitXpress to show where: 2 guided photos on the member's phone, and 80+ body measurements come back through the API in one timestamped record. On the Pro plan, 3D Body Progress tracking shows change between check-ins.

What does a member see at a first check-in today?

Nick
--- M2
Hi Shirley,

The 3D tools sit on the Pro plan, and the platform chooses which scans a member compares.

I can walk through how that fits a paid plan on a call, or point me to whoever owns it.
https://meetings.hubspot.com/nick-omelchak

Nick

=== seung-jin-lee-0983643a | Seung Lee | Product Manager | angle product P3
--- M1
Hi Seung,

Your path from technical relationship work into product at Peloton got me thinking about how integrations land. Typed values and photos give an app little to compare between check-ins.

FitXpress from 3DLOOK is an SDK and API integration: 2 guided photos on the member's phone, and a timestamped record with 80+ body measurements returned through the API.

How does a partner capability enter the Peloton app?

Nick
--- M2
Hi Seung,

Each record maps to the member profile through the scan ID, which keeps the integration simple for the app.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

Happy to go through it on a call, or point me to whoever owns partner integrations.
https://meetings.hubspot.com/nick-omelchak

Nick


######## Trainerize (13)

=== ericreimers | Eric Reimers | VP Corporate Development | angle partnership P2
--- M1
Hi Eric,

Home photos and tape differ between check-ins in pose, distance, light and tape placement, and trainers compare unlike things.

Trainerize's client app already carries body stats, measurements and side-by-side progress photos.

FitXpress is a body scan Trainerize could integrate: 2 guided photos on the client's phone, 80+ body measurements and a timestamped record back through the API, under the trainer's brand.

When trainers ask for a measured body check-in, does Trainerize build it or look for an integration?

Nick
--- M2
Hi Eric,

Web and mobile SDKs cover iOS and Android. There is no integration fee.

Calendar for a call, or a pointer to whoever handles integrations:
https://meetings.hubspot.com/nick-omelchak

Nick

=== doug-reeder-3247511 | Doug Reeder | Sr. Director, Product Line Management | angle product P3
--- M1
Hi Doug,

A body measurement is only comparable when two check-ins were taken the same way.

A body scan inside the trainer's branded client app is what FitXpress adds. A client's 2 guided photos return 80+ body measurements, and the app receives one timestamped record per scan.

If Trainerize's product line sits with you, this would be packaged next to the progress tools clients already have.

Among the onboarding and results screens around the scan, which would trainers want in their own brand?

Nick
--- M2
Hi Doug,

On FitXpress's Pro plan, 3D Body Progress tracking and 3D Goal Visualization work as paid-plan features, which a product line could package for trainers.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

Packaging is a good topic for a call, or point me to whoever owns plan design:
https://meetings.hubspot.com/nick-omelchak

Nick

=== finn-hegarty-2871037 | Finn Hegarty | Chief Product Officer | angle product P3
--- M1
Hi Finn,

For Trainerize, a trainer could switch a body check-in on inside their own white-labeled client app, under the trainer's brand.

Tape measurements a client takes at home depend on who holds the tape and where.

With FitXpress switched on, the client takes 2 guided photos on their phone, and 80+ body measurements come back through the API as one timestamped record.

How does the product team decide which new capability trainers get to switch on?

Nick
--- M2
Hi Finn,

The capture layer stays fixed, and every other screen is Trainerize's own or the trainer's. No hardware is involved, since the client uses their phone.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

Book a time here, or point me to whoever owns the client progress experience:
https://meetings.hubspot.com/nick-omelchak

Nick

=== keegan-dowling-ba8aaa7 | Keegan Dowling | Vice President, Partnerships | angle partnership P2
--- M1
Hi Keegan,

Trainerize trainers can run the client app under their own brand.

Through one FitXpress integration, every trainer's clients could take 2 guided photos inside that app and get back 80+ body measurements, one timestamped record per scan.

A separate scanning app puts the client and the result under another brand, and what comes back to Trainerize depends on that app.

When trainers raise client progress with Trainerize, which request comes up first?

Nick
--- M2
Hi Keegan,

The partner route would carry a single SDK and API integration to every trainer's clients. 3DLOOK has worked with 100+ clients, including fitness teams.

If the route makes sense, here is my calendar:
https://meetings.hubspot.com/nick-omelchak

Nick

=== jenniferannpelton | Jennifer Pelton | Director of Product Management | angle product P3
--- M1
Hi Jennifer,

Trainerize clients fill in an onboarding form and later the check-in forms their trainer sets.

A form holds only what the client enters.

A guided FitXpress scan could sit in the same step: 2 photos with pose and framing guidance, and 80+ body measurements and a timestamped record come back for the trainer.

Would the onboarding form or the check-in form be the better place for a body scan?

Nick
--- M2
Hi Jennifer,

A pilot could split clients into two groups: one scans at onboarding, the other keeps the form alone. Onboarding completion is the measure, set against criteria both sides agree beforehand.

Easier to show on a call, or point me to whoever runs onboarding:
https://meetings.hubspot.com/nick-omelchak

Nick

=== thekellycard | Kelly Card | Senior Vice President of Product | angle product P1
--- M1
Hi Kelly,

Your January roadmap post for ABC Trainerize lists continued work on check-in forms and a redesigned client app for 2026.

On a strength block, a client's weight can hold while the waist narrows and lean mass moves, and a form has no field to show it.

FitXpress adds a body check-in to that flow: the client takes 2 guided photos, front and side, in the trainer's branded app, and a timestamped record of 80+ body measurements comes back through the API.

Where in the redesigned client app would a body check-in sit?

Nick
--- M2
Hi Kelly,

A trainer would see waist and thigh changes between two check-ins, beside fat and lean mass estimates.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

On a call I can show where it fits in the redesigned app:
https://meetings.hubspot.com/nick-omelchak

Nick

=== tristanalexander | Tristan Alexander | Vice President Of Product Management | angle product P3
--- M1
Hi Tristan,

Progress photos show change a trainer can see, and they return no measurement to compare at the next check-in.

Trainerize already offers side-by-side photo comparison in the client app, next to body stats and tape measurements.

For the next check-in, FitXpress gives the trainer 80+ body measurements and fat and lean mass estimates from 2 guided photos, front and side, timestamped and under the trainer's brand.

Where do the tape measurements a client logs end up for the trainer to review?

Nick
--- M2
Hi Tristan,

A trainer comparing two check-ins would read the same set of body measurements from each. Repeated scans typically differ by less than 1 cm for most evaluated measurements.

A short call could cover it, or point me to whoever looks after trainers' program tools:
https://meetings.hubspot.com/nick-omelchak

Nick

=== vishuviswanathan | Vishu Viswanathan | Vice President of Software Engineering, Trainerize Platform | angle referral P3
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

=== zekebrustkern | Zeke Brustkern | Director of Product Management | angle product P3
--- M1
Hi Zeke,

Your headline treats data as the product, and a body-data type is only as useful as the way it was captured.

A separate scanning app would keep the scan in its own system, and Trainerize would see only what that app passes along.

FitXpress returns one timestamped record per scan through the API: 2 guided photos, front and side, give 80+ body measurements with a processing status.

How would a new body-data type join a client's profile in the Trainerize data model today?

Nick
--- M2
Hi Zeke,

The scan ID links each record to the client profile, which gives a new body-data type a clear key in the data model.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

Glad to go through the API on a call, or to meet the team that runs the partner route:
https://meetings.hubspot.com/nick-omelchak

Nick

=== len-bucchino | Len Bucchino | Chief Technology Officer | angle referral P3
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

=== laurietaylorkemp | Laurie Kemp, CMM | Product Management Director, Partner Solutions | angle partnership P2
--- M1
Hi Laurie,

A trainer sets the next program block from weight, photos and notes, with no measured change to compare.

The trainer reviews 80+ body measurements and fat and lean mass estimates before the next block, all from 2 guided photos on the client's phone through a FitXpress integration.

If Trainerize's partner integrations run through your team, a capability like this would reach the trainer and client apps through you.

How does a partner capability get from registration into the trainer's client app today?

Nick
--- M2
Hi Laurie,

Integration comes with white-label screens, which keep each trainer's own brand on the client's phone, and a scan ID ties every record to the client profile.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

Walking through the integration details is easiest on a call:
https://meetings.hubspot.com/nick-omelchak

Nick

=== kendall-wilson-aba17628 | Kendall Wilson | Director of Product Management | angle product P3
--- M1
Hi Kendall,

A weigh-in gives one total, and a weekly average smooths it, yet neither shows which part of the body changed.

Trainerize's Body Weight with Weekly Average graph, added in the September update, puts both on one line.

A body scan from FitXpress would sit beside that line, and 2 guided photos from the client's phone return 80+ body measurements and fat and lean mass estimates under the trainer's brand.

After a first check-in, what does a Trainerize client have to look at besides the weight line and logged workouts?

Nick
--- M2
Hi Kendall,

A client's waist and chest changes could sit next to the weight graph, one record per body scan.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

Here is my calendar, or point me to whoever owns what clients see after a weigh-in:
https://meetings.hubspot.com/nick-omelchak

Nick

=== elizabeth-gray-94237a106 | Elizabeth Gray | Senior Director of Product Management | angle product P3
--- M1
Hi Elizabeth,

The Trainerize dashboard became customizable on August 3, with Lean Mass and Progress Photo Comparison widgets.

On a strength program a client can add muscle and lose inches while the scale barely moves.

FitXpress gives a trainer's Insights Dashboard a measured record. A client takes 2 guided photos on their phone, and the trainer gets 80+ body measurements and fat and lean mass estimates, timestamped.

If a client's waist and hip changes were on record, what would a trainer do with them first?

Nick
--- M2
Hi Elizabeth,

A trainer could review girths and lengths next to fat and lean mass estimates in one view. For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm.

If a call helps, here is my calendar, or point me to whoever decides how trainers build programs:
https://meetings.hubspot.com/nick-omelchak

Nick


######## BODi (11)

=== marietta-p-9144112 | Marietta P. | Group Vice President | angle product P3
--- M1
Hi Marietta,

A weigh-in is one total, and it cannot say which part of the body moved.

3DLOOK's FitXpress would put a body scan under BODi's own brand, with 80+ body measurements and fat and lean mass estimates coming back to the platform from 2 photos taken on the member's phone.

On the BODi app roadmap, that would sit beside programs and workouts as the record of what changed.

Which part of the BODi app tells a member that their body is changing?

Nick
--- M2
Hi Marietta,

A member scans on their own phone with no extra hardware, and BODi chooses which scans its progress experience compares.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

A call works, or point me to whoever owns the progress experience in the app:
https://meetings.hubspot.com/nick-omelchak

Nick

=== stephaniessaunders | Stephanie Saunders | VP, Fitness Progamming | angle coaching P2
--- M1
Hi Stephanie,

P90X Generation Next went onto BODi's digital platform in February, and a program like that gets judged on what changes by the last week.

On a strength block, body weight can hold steady while waist and lean mass shift. The total says little about where the body changed.

At 3DLOOK we built FitXpress for that gap. A member takes 2 guided photos, front and side, on their own phone inside the BODi app, and the program gets back 80+ body measurements and fat and lean mass estimates as one timestamped record.

When a block of P90X Generation Next ends, what does the program use to judge how a member did?

Nick
--- M2
Hi Stephanie,

At the end of a block, a trainer and the member can look at one record, comparable to the one from the start. Repeated scans typically differ by less than 1 cm for most evaluated measurements.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

Happy to show how that would look in a P90X block on a call:
https://meetings.hubspot.com/nick-omelchak

Nick

=== jeffrey-scott-nasm-cpt-nasm-cnc-8b171447 | Jeffrey Scott | Group Vice President Fitness, Nutrition, Results | angle coaching P2
--- M1
Hi Jeffrey,

Training metrics record the work a member did, and the body change that work is for sits outside them.

Your title puts results beside fitness and nutrition, and BODi programs run step by step, with or without equipment.

FitXpress adds a body scan to the BODi app, and 2 guided photos from the member's phone return 80+ body measurements, including waist and thigh, with fat and lean mass estimates.

If a member's waist and thigh change were on record beside the program, what would your fitness team do with it first?

Nick
--- M2
Hi Jeffrey,

A program lead could review girths and lengths next to fat and lean mass estimates, all from one timestamped record per body scan. 3DLOOK has worked with 100+ clients, including fitness teams.

If it helps, my calendar is here for a call:
https://meetings.hubspot.com/nick-omelchak

Nick

=== robcanning | Rob Canning | Director of Product Management | angle product P2
--- M1
Hi Rob,

Your headline puts experimentation and subscription monetization side by side, which is how a new check-in step would get judged at BODi.

Members type their body measurements into the app, and the November 19 release made that faster. Tape placement, distance and light still differ from one home check-in to the next.

FitXpress swaps the tape for a body scan inside the BODi app. Front and side, 2 guided photos go in, and a timestamped record of 80+ body measurements comes back through the API.

How does your team test a new onboarding step before it reaches every member?

Nick
--- M2
Hi Rob,

A pilot can run like any other test. One member cohort takes the body scan at onboarding and at the first check-in, a comparable cohort keeps the usual flow, and the two are compared on onboarding completion and day-30 and day-90 retention. The criteria for a pass get set with BODi before anyone scans.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

If the design looks worth testing, pick a time here:
https://meetings.hubspot.com/nick-omelchak

Nick

=== nicholasrwilley | Nicholas Willey | Director of Product Management | angle product P3
--- M1
Hi Nicholas,

FitXpress is a body scan that runs inside an app under the platform's own brand. The member takes 2 guided photos on their own phone, and the app gets back 80+ body measurements through the API.

A separate scanning app puts the member and the result under another brand, and what comes back to the platform depends on that app.

Your headline pairs product strategy with experience, and a body check-in under BODi's own brand belongs in that conversation.

How does the BODi app roadmap decide where a new member feature goes?

Nick
--- M2
Hi Nicholas,

A body scan returns 80+ body measurements, under 45 seconds from the photos to structured results. The SDKs cover web, iOS and Android.

A call would cover it, or point me to whoever runs onboarding:
https://meetings.hubspot.com/nick-omelchak

Nick

=== jenny-parker-28b93516 | Jenny Parker | Vice President, Content Development | angle coaching P3
--- M1
Hi Jenny,

BODi programs are built around a promise of change, and production puts that promise on screen.

A progress photo shows visible change, though no measurement comes with it.

FitXpress would give a program 80+ body measurements and body composition estimates to show on BODi's own branded screens, from 2 guided photos taken on a phone.

Which photos or notes does a program's check-in collect from members today?

Nick
--- M2
Hi Jenny,

A program's check-in could repeat the same 2 photos at the start and at the end of a block, with a timestamp on each record for the comparison. Across all 3DLOOK customers, there were 112,100 scans in 2025.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

If program design sits with someone else, point me their way. Otherwise a call is easy to book here:
https://meetings.hubspot.com/nick-omelchak

Nick

=== mikefarrell | Mike Farrell | Executive Director of Product Management | angle product P2
--- M1
Hi Mike,

A measurement log holds whatever the member types, and a typed number carries no trace of how it was taken.

Your headline names digital consumer experiences and subscriptions, which is where a body check-in would live.

FitXpress puts a body scan in the same flow, with 2 photos taken in the app and one structured record, 80+ body measurements and a processing status, coming back through the API for BODi to keep.

Once a member types a measurement in today, where does it show up in the app afterwards?

Nick
--- M2
Hi Mike,

The setup is the SDK and the API together. The capture layer stays fixed, and BODi's own consent wording and results screens go around it.

A call could go through the setup in detail:
https://meetings.hubspot.com/nick-omelchak

Nick

=== howens | Hunter Owens | Senior Product Manager | angle product P3
--- M1
Hi Hunter,

A strength program can change the waist while the weight stays put, and a progress screen built on weight never shows it.

FitXpress supplies that with a body scan in the app: 2 guided photos, front and side, return 80+ body measurements in one timestamped record.

Besides the capture itself, which screens in the BODi app, onboarding or results, would the team want to brand its own way?

Nick
--- M2
Hi Hunter,

Each scan carries a scan ID, which BODi links to the member profile, and the progress screen can pull the right record for each member.

Happy to talk it through, or to be pointed to whoever owns progress screens:
https://meetings.hubspot.com/nick-omelchak

Nick

=== ashlei-mitchell-0a302a220 | Ashlei Mitchell | Senior Product Manager | angle product P3
--- M1
Hi Ashlei,

BODi's progress screens read from program data.

A hand measurement shifts with the person and the placement, which makes two check-ins hard to line up in data.

FitXpress returns one timestamped record per scan through the API: 80+ body measurements and fat and lean mass estimates, from 2 guided photos a member takes on their own phone.

Where does BODi keep body measurements today, and in what form do they reach the data?

Nick
--- M2
Hi Ashlei,

Each scan arrives as one record that can join the program data the progress screens already read. BMI and BMR come in the same record as calculated metrics.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

A call to compare notes, or a pointer to whoever owns the paid plan:
https://meetings.hubspot.com/nick-omelchak

Nick

=== vjmuthuraman | Vijay Muthuraman | Executive Director ★ Head of Commerce and Acquisition Product | angle product P3
--- M1
Hi Vijay,

A first weigh-in gives one self-reported total, and where the body changed stays unknown from day one.

FitXpress gives a new member a body scan at sign-up: 2 guided photos, front and side, on their own phone, and 80+ body measurements come back in BODi's own branded screens.

Acquisition product decides how a member steps into a digital plan, and onboarding is where that first record would sit.

What does a new BODi member do first after picking a digital plan?

Nick
--- M2
Hi Vijay,

Pose and framing guidance runs while the member captures, which helps first-day photos stay consistent. 3DLOOK has worked with 100+ clients, including fitness teams.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

Slots for a call are here, and a pointer to the owner of the membership offer works too:
https://meetings.hubspot.com/nick-omelchak

Nick

=== brandoncowley | Brandon Cowley | Product Manager | angle product P3
--- M1
Hi Brandon,

Before and after photos show visible change, and nothing measured sits behind them.

A member scans with FitXpress on their own phone, 2 guided photos, and BODi gets back 80+ body measurements, including chest and calf.

That would sit on the program progress screen beside workouts finished.

Where would a body scan fit best for a BODi member, on day one or at a later check-in?

Nick
--- M2
Hi Brandon,

A progress screen could show how chest and hip changed between two scans, set beside the photos.

Pick a time for a call, or send me toward the owner of the sign-up flow:
https://meetings.hubspot.com/nick-omelchak

Nick


######## MyFitnessPal (9)

=== oaktownolivia | Olivia Carlson | Vice President of Customer Happiness | angle referral P3
--- M1
Hi Olivia,

Tape and home photos differ between check-ins in pose, distance, light and tape placement, which makes typed measurements hard to compare.

FitXpress puts a guided body scan inside the app: 2 photos, front and side, with pose and framing guidance, and 80+ body measurements come back as one timestamped record.

MyFitnessPal members attach progress photos to weigh-ins, and those stay private to them.

What do members ask about most when they log weight and measurements?

Nick
--- M2
Hi Olivia,

A member's record carries a timestamp, allowing two check-ins to be compared in whatever way the app chooses to show them.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

Pick a time for a call here, or point me to whoever owns progress in the app:
https://meetings.hubspot.com/nick-omelchak

Nick

=== karl-mahrenholz | Karl Mahrenholz | Head of Cal AI | angle product P1
--- M1
Hi Karl,

Cal AI already makes a photo return structured data about the plate.

A progress photo of the body returns no numbers.

FitXpress applies the same photo-first capture to the body, and a member takes 2 guided photos, front and side, and MyFitnessPal gets back 80+ body measurements and fat and lean mass estimates as one structured record.

Around the photo capture itself, which onboarding and results screens would MyFitnessPal want to style in its own look?

Nick
--- M2
Hi Karl,

The SDK and API together are the recommended setup. The capture layer stays fixed, and MyFitnessPal's own onboarding and consent screens go around it.

If it is worth a conversation, my calendar:
https://meetings.hubspot.com/nick-omelchak

Nick

=== sgaat | Sucharita G. | Head of Platform Engineering | angle referral P3
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

=== ruth-sylvia-a1238417 | Ruth Sylvia | VP, Product Management | angle product P1
--- M1
Hi Ruth,

MyFitnessPal's Progress tab turns daily tracking into weekly insights.

A weigh-in gives a single total, and it says nothing about which part of the body changed.

FitXpress adds a body scan to that view: 2 guided photos from the member's phone return 80+ body measurements, including waist and hip, with fat and lean mass estimates, under MyFitnessPal's own brand.

Beyond weight and logged meals, what does a member see in the Progress tab each week?

Nick
--- M2
Hi Ruth,

Each record is tied to the member profile through a scan ID, allowing a weekly view to pull the right scan, and it carries a processing status.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

Here is my calendar if a call would help:
https://meetings.hubspot.com/nick-omelchak

Nick

=== christina-to | Christina To | Senior Product Manager | angle product P3
--- M1
Hi Christina,

FitXpress is a body scan for apps, and under MyFitnessPal's brand it would return 80+ body measurements and a timestamped record from 2 guided photos on the member's phone.

A photo added to a weigh-in shows change you can see, and carries no measurement.

MyFitnessPal's new Weight Log screen, from the November 17 release, carries that photo.

What happens to a photo once it is attached to a weigh-in, and where does it show afterwards?

Nick
--- M2
Hi Christina,

A body scan returns 80+ body measurements, under 45 seconds from the photos to structured results, allowing a photo on the Weight Log to sit beside a measured record.

Open to a call, or to pointing me to whoever owns progress features:
https://meetings.hubspot.com/nick-omelchak

Nick

=== kelsey-van-ackeren | Kelsey Van Ackeren | Senior Product Manager | angle product P3
--- M1
Hi Kelsey,

Your growth background puts onboarding close to your work at MyFitnessPal, where a first weigh-in goes to the Weight Log.

A form can only collect what a member types or taps.

FitXpress can add a body scan as one more step: 2 guided photos, front and side, taken by the member, and a timestamped record of 80+ body measurements comes back, which the platform links to the member profile through the scan ID.

How does the team test a new onboarding step today?

Nick
--- M2
Hi Kelsey,

A pilot could add the scan step for one group of new members and leave a comparable group on today's flow, then compare how many finish onboarding in each. The two teams settle the criteria before anyone scans.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

Happy to design the test together on a call, or to be pointed to the owner of onboarding:
https://meetings.hubspot.com/nick-omelchak

Nick

=== vptaylo | Victoria Taylo | Senior Product Manager | angle product P3
--- M1
Hi Victoria,

MyFitnessPal members can type their measurements under Weight & Measurements, next to the weigh-in.

A weigh-in is one total, and a waist that has narrowed can leave it nearly unchanged.

FitXpress gives the same slot a guided record: 2 photos with pose and framing guidance return 80+ body measurements and fat and lean mass estimates.

Which typed measurement do members log most under Weight & Measurements?

Nick
--- M2
Hi Victoria,

A body scan record can show waist and hip changes from one check-in to the next, wherever MyFitnessPal keeps the typed log.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

Book a call here, or send me to whoever owns Premium:
https://meetings.hubspot.com/nick-omelchak

Nick

=== meganstaggoverton | Megan Overton | Head of AI Nutrition Coach | angle product P1
--- M1
Hi Megan,

Food logs, goals and habits are all things the member enters, and none of them is measured body change.

MyFitnessPal's AI Coach, which arrived in the Coach tab in June, turns those inputs into guidance.

A FitXpress body scan gives it one more input that is measured: 2 guided photos, front and side, from the member's phone return 80+ body measurements and fat and lean mass estimates, as a timestamped record the AI Coach could read.

What would the AI Coach need to see before measured body change shapes its guidance?

Nick
--- M2
Hi Megan,

Fat and lean mass estimates are derived from the measurements with height and, where provided, weight. For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm.

A call to go through what the AI Coach could read:
https://meetings.hubspot.com/nick-omelchak

Nick

=== anapischl | Ana Pischl | Product, Monetization & Expansion | angle product P2
--- M1
Hi Ana,

Monetization and expansion put you at the question of what goes into Premium and Premium+ at MyFitnessPal.

FitXpress offers 3D Body Progress tracking and 3D Goal Visualization on its Pro plan, built on a body scan from 2 guided photos with 80+ body measurements, all under MyFitnessPal's brand.

A separate scanning app would put the member and the result under another brand.

Where do progress features sit between the free plan and the paid ones today?

Nick
--- M2
Hi Ana,

A pilot could compare a scan cohort with a comparable cohort on free-to-premium conversion and day-30 and day-90 retention, with the criteria for success set up front.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

Pilot design is easiest to cover live, calendar here:
https://meetings.hubspot.com/nick-omelchak

Nick


######## Tonal (7)

=== amartanna-cpa-ca | Amar Tanna, CPA, CA | Senior Director, Post-Sales Operations & Customer Success | angle referral P3
--- M1
Hi Amar,

Post-sales and customer success at Tonal sit where members ask about results once a program ends.

FitXpress from 3DLOOK gives that question a measured answer inside the Tonal app. The member's 2 photos go to the API, which returns one timestamped record with 80+ body measurements. A check-in form, by comparison, holds only what the member types in.

What do members ask Tonal once a program ends?

Nick
--- M2
Hi Amar,

Each record is timestamped and linked to the member profile by a scan ID, which gives a post-program question a figure to answer with.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

A call would show how it reads in the Tonal app, or send me to whoever runs the member app's progress experience.
https://meetings.hubspot.com/nick-omelchak

Nick

=== maureen-key-96362830 | Maureen Key | Senior Fitness Programming Specialist | angle coaching P3
--- M1
Hi Maureen,

Tonal's strength for performance program is built to help members track progress over time, and home photos and tape differ in pose and light between check-ins.

For a performance block, FitXpress would add measured values: 80+ body measurements and fat and lean mass estimates, timestamped and returned through the API from the member's 2 guided photos in the Tonal app.

Which body measurements would you want beside a performance block's training data?

Nick
--- M2
Hi Maureen,

A coach could read girths such as waist and thigh next to the fat and lean mass estimates, from one timestamped scan before the block and one after.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

A call would show the record against a Tonal block, or point me to whoever reviews program results.
https://meetings.hubspot.com/nick-omelchak

Nick

=== josephrodonis | Joe Rodonis | Head Coach | angle coaching P3
--- M1
Hi Joe,

A progress photo shows the change by eye, and the coach has nothing measured to compare at the next check-in.

FitXpress would give the coach of your programs a single record to read. It arrives through the API after the member's 2 guided photos in the Tonal app, timestamped, with 80+ body measurements and fat and lean mass estimates. A member who asks about results gets an answer from that record.

What would you do with a member's waist, hip and thigh changes?

Nick
--- M2
Hi Joe,

The member captures on their own phone with pose and framing guidance on screen, and the coach reviews one record afterward.

Happy to show the capture screen on a call, and whoever runs the coaching programs is welcome on it.
https://meetings.hubspot.com/nick-omelchak

Nick

=== tanysha-smith | Tanysha Smith | Head Coach | angle coaching P3
--- M1
Hi Tanysha,

A weigh-in is a single total, and a member who asks about results at the end of a block is asking where the body changed.

FitXpress from 3DLOOK adds a body scan to the Tonal app. The member provides 2 guided photos, and a timestamped record with 80+ body measurements returns through the API.

When a program you lead wraps up, what does a member see that shows the block worked?

Nick
--- M2
Hi Tanysha,

A coach and a member would open the same timestamped record, and a later scan gives them a second figure to set beside the first.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

A call would cover how a block's first and last scans line up, or send me to whoever owns progress in the Tonal app:
https://meetings.hubspot.com/nick-omelchak

Nick

=== jshottan | Jonathan Shottan | Chief Product and Content Officer | angle product P2
--- M1
Hi Jonathan,

Tonal's own example for Tia is a member who finished a lean program and asks what to do next to keep shifting body composition. Tia reads training data, and the weight total beside it can sit flat while the waist changes.

FitXpress would add a body record to the Tonal app under Tonal's brand. After 2 guided photos on the member's phone, the API returns one timestamped record with 80+ body measurements and fat and lean mass estimates.

At which point in a member's first weeks on Tonal would a body scan fit best?

Nick
--- M2
Hi Jonathan,

Tonal would add it through the SDK and the API together, with its own onboarding and consent screens around the capture.

FitXpress returns 80+ body measurements, under 45 seconds from the photos to structured results.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

Worth a call to look at it against the Tonal app?
https://meetings.hubspot.com/nick-omelchak

Nick

=== jenna-moore-ms-cscs-a99827a1 | Jenna Moore | Director, Performance (Programming) & Talent | angle coaching P2
--- M1
Hi Jenna,

Tonal's 2026 programs include a muscle-building block, and judging whether a block did its work asks for more than lifts logged. A block review that rests on weight, photos and the member's notes has no measurement of the body in it.

With FitXpress, a coach would review a record from the member's own phone: 2 guided photos return 80+ body measurements, including waist and thigh, and fat and lean mass estimates, as one timestamped record through the API.

How does your team review a program block after members finish it?

Nick
--- M2
Hi Jenna,

A block-to-block comparison depends on how stable each scan is. For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm.

A call would be the easy way to go through it:
https://meetings.hubspot.com/nick-omelchak

Nick

=== annafurr | Anna Furr | Staff Product Manager | angle product P3
--- M1
Hi Anna,

The Tonal app breaks progress down by muscle group and workout type. That describes the work done and leaves the body itself unmeasured.

Through an SDK and the API, FitXpress adds a body scan to the app. The member takes 2 photos on their own phone, and Tonal gets one timestamped record with 80+ body measurements and body composition estimates.

How does the Tonal app hold progress photos or body measurements today?

Nick
--- M2
Hi Anna,

Thigh and chest changes, with fat and lean mass estimates beside them, could appear on a progress screen between two timestamped scans.

Grab a time here, or point me to the owner of the paid plan:
https://meetings.hubspot.com/nick-omelchak

Nick


######## Centr (6)

=== andrew-sugerman | Andrew Sugerman | CEO | angle leadership P2
--- M1
Hi Andrew,

Centr builds programs around a member's goals, fitness level and equipment, and a check-in under Centr's own brand would show what they changed. A progress photo shows the change by eye and leaves nothing to compare numerically at the next check-in.

With FitXpress, Centr's members take 2 photos on their own phone and the API returns one timestamped record with 80+ body measurements, on white-label screens that Centr controls. It would start as a pilot before any rollout.

What member promise would a measured check-in serve at Centr?

Nick
--- M2
Hi Andrew,

The scan runs under Centr's brand, and the record returns to Centr's own member profile through the API. Centr chooses which scans a member sees.

3DLOOK has worked with 100+ clients.

Happy to walk through it on a call:
https://meetings.hubspot.com/nick-omelchak

Nick

=== nicholasjrobinson | Nicholas Robinson | President, Digital | angle leadership P1
--- M1
Hi Nicholas,

Centr Coach picks a member's daily workout and meals, and a weigh-in is the usual way to see what that plan did. It is a single total, and where the body changed stays unknown.

FitXpress, the 3DLOOK body scan, would sit inside the Centr app under Centr's own brand. One timestamped record with 80+ body measurements and body composition estimates comes back through the API after a member's 2 photos.

How does Centr decide which new member features get piloted before rollout?

Nick
--- M2
Hi Nicholas,

A pilot would test it: one cohort of Centr members scans at onboarding and at the first check-in, and a comparable cohort keeps the usual flow. Day-30 and day-90 retention are compared between the two, and you and I would set the success criteria before the first member scans.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

Worth a call to shape the design?
https://meetings.hubspot.com/nick-omelchak

Nick

=== thaovdoan | Thao Doan, JD, MS, MBA | Vice President of Engineering | angle referral P3
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

=== megan-johns-72b40818a | Megan Johns | Director of Customer Experience | angle referral P3
--- M1
Hi Megan,

You run customer experience at Centr, where questions about a member's results get asked.

A check-in form holds only what the member types in. FitXpress from 3DLOOK adds a measured answer inside the Centr app. Once the member has taken 2 photos, the API returns one timestamped record with 80+ body measurements and fat and lean mass estimates.

When members write in about their results, what are they usually asking to see?

Nick
--- M2
Hi Megan,

Member and team could look at the same timestamped scan record, and a second scan later gives them a figure to set beside the first.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

Would a call be useful? If the progress experience sits with someone else, a pointer to them works too.
https://meetings.hubspot.com/nick-omelchak

Nick

=== jrafferty | John Rafferty | VP of Product | angle product P1
--- M1
Hi John,

Centr's app tracks results and workout history, and the end of a program is where a measured number would matter. Home photos and tape differ in pose and light between check-ins, which makes the comparison drift.

Through an SDK and the API, FitXpress from 3DLOOK puts a body scan inside the app. The member takes 2 photos, front and side, with pose and framing guidance on screen, and the API returns 80+ body measurements and fat and lean mass estimates.

What does a member see at a check-in in the Centr app today, beyond weight and workouts?

Nick
--- M2
Hi John,

For setup, Centr would use the SDK and the API together, with the capture layer fixed and its own onboarding and consent screens around it.

The scan returns 80+ body measurements, under 45 seconds from the photos to structured results.

If it helps to see it in the app, grab a time here:
https://meetings.hubspot.com/nick-omelchak

Nick

=== productobsessedlaura | Laura Ruiz | Product Manager | angle product P3
--- M1
Hi Laura,

Centr Coach offers coached and self-guided workouts, and training metrics show the work done and say little about how the body changed.

FitXpress from 3DLOOK would add a body record next to the workout history in the app. Each member's 2 photos, taken in the Centr app, come back through the API as one timestamped record with 80+ body measurements and body composition estimates.

Would the team put a body record at sign-up, or leave it for later in the Centr Coach plan?

Nick
--- M2
Hi Laura,

Every record comes back with a scan ID, and the Centr app attaches it to the member profile that already holds the workout history.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

Open to a call? Or tell me who owns onboarding.
https://meetings.hubspot.com/nick-omelchak

Nick


######## Everfit (6)

=== jondwang | Jonathan Wang | Co-Founder | angle leadership P2
--- M1
Hi Jonathan,

A separate scanning app shows the client another brand, and what returns to the platform depends on that app.

Under each coach's own brand, FitXpress runs inside the Everfit app, with Everfit's own onboarding and consent screens. From 2 client photos, the API returns 80+ body measurements and body composition estimates as one timestamped record.

Everfit sits between the coach and the client, which makes build or integrate a real question for a body check-in.

What would you want a measured check-in to do for Everfit's coaches next year?

Nick
--- M2
Hi Jonathan,

Building a body scan in-house means owning the capture and the measurement model. Integrating FitXpress leaves Everfit with each client's history and the choice of which scans a coach and client see, while the capture layer stays fixed.

3DLOOK has worked with 100+ clients, including fitness teams.

Glad to compare build and integrate on a call:
https://meetings.hubspot.com/nick-omelchak

Nick

=== thealexpoon | Alex P. | Director of Engineering | angle referral P3
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

=== longdnguyen | Long Nguyen | Co-Founder | angle leadership P2
--- M1
Hi Long,

Coaches on Everfit review progress through weekly check-in forms under their own brand, and the next block is set from weight, photos and written notes. Nothing in that set is a measurement of the body itself.

FitXpress would be one integration that reaches every coach's clients. A client takes 2 photos on their own phone, and one timestamped record with 80+ body measurements comes back through the API on white-label screens.

How does Everfit decide which new capability to offer every coach's clients?

Nick
--- M2
Hi Long,

Everfit would integrate once with the SDK and the API, and the scan ID ties each record to the client profile. There is no integration fee.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

Would a call make sense?
https://meetings.hubspot.com/nick-omelchak

Nick

=== robert-benjamin-a7906b104 | Robert Benjamin | Product Manager | Head of Everfit Academy | angle product P2
--- M1
Hi Robert,

Your background as a strength and conditioning coach means you know what a coach actually opens at a check-in.

Home photos and tape differ in pose and light from one check-in to the next. FitXpress, built by 3DLOOK, puts a guided scan inside the Everfit app: the client takes 2 photos and the API returns one timestamped record with 80+ body measurements and fat and lean mass estimates.

What do you teach coaches at Everfit Academy to look for in a check-in?

Nick
--- M2
Hi Robert,

A coach reviewing a check-in would see girths and lengths with fat and lean mass estimates. FitXpress returns 80+ body measurements, under 45 seconds from the photos to structured results.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

Grab a time if you want to go through it:
https://meetings.hubspot.com/nick-omelchak

Nick

=== elizabeth-palmer-97820997 | Elizabeth Palmer | Head of Customer Success | angle coaching P3
--- M1
Hi Elizabeth,

A weigh-in is a single, often self-reported total, and where the body changed stays unknown.

In July 2026 Everfit gave every task category pre-built templates, progress-photo templates among them. FitXpress turns a client's 2 photos, taken on their own phone in the Everfit app, into one timestamped record through the API with 80+ body measurements and body composition estimates for the coach.

What do coaches ask Everfit to record for their clients beyond weight and photos?

Nick
--- M2
Hi Elizabeth,

Coaches and clients would both see one timestamped record, and Everfit links it to the client profile through the scan ID. A second scan gives a coach a figure to set against the first.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

A call would cover it, or point me to whoever handles Everfit integrations.
https://meetings.hubspot.com/nick-omelchak

Nick

=== bogatzproductmanager | Carly Bogatz | Senior Product Manager | angle product P2
--- M1
Hi Carly,

Everfit's intake and goal-setting forms capture what the client types, and a form holds only what the client enters.

FitXpress would put a guided capture at the intake step in the Everfit app. The client takes 2 photos on their own phone, and the SDK and API return one timestamped record with 80+ body measurements and fat and lean mass estimates.

How does your team test a new step in client onboarding?

Nick
--- M2
Hi Carly,

A pilot could compare onboarding completion between two groups of new Everfit clients: one scans at the intake form, the other keeps the usual form, and the success bar is set before anyone is enrolled.

Happy to show the intake step on a call:
https://meetings.hubspot.com/nick-omelchak

Nick


######## Echelon (6)

=== heidi-jones-ny | Heidi Jones | SVP Strategic Partnerships, Echelon | angle partnership P3
--- M1
Hi Heidi,

A separate scanning app puts the member and the result under another brand, and what comes back to the platform depends on that app.

FitXpress from 3DLOOK would run inside the Echelon app under Echelon's brand and return one timestamped record through the API, with 80+ body measurements from the member's 2 photos.

Partnerships at Echelon bring capabilities into the membership, and this one would be Echelon's to offer.

How does a new partner capability get into the Echelon app today?

Nick
--- M2
Hi Heidi,

Web and mobile SDKs cover iOS and Android, and the screens are white-label.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

Worth a call? Or point me to whoever owns the paid membership.
https://meetings.hubspot.com/nick-omelchak

Nick

=== lisa-privitera | Lisa Privitera | Vice President of Fitness & Wellness | Echelon Coach | angle coaching P2
--- M1
Hi Lisa,

Echelon Coach pairs members with a one-to-one trainer, and between sessions the trainer's view of progress comes from what the member reports. The next block then rests on weight, photos and notes, and none of those is a measurement of the body.

With FitXpress inside the Echelon app, the trainer would open one record per scan: 80+ body measurements and fat and lean mass estimates from 2 guided photos the member took on their own phone, under Echelon's brand.

What does an Echelon Coach trainer look at in a check-in today?

Nick
--- M2
Hi Lisa,

A trainer could open the same timestamped record the member sees, then set a later scan beside the earlier one when planning the next block.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

Open to a call on how it would fit Echelon Coach?
https://meetings.hubspot.com/nick-omelchak

Nick

=== kevin-j-custer-14a2b76 | Kevin Custer | Chief Content Officer | angle coaching P2
--- M1
Hi Kevin,

Echelon's class and program library sets what members train, and judging how a program worked asks for a body record beside the class history. A progress photo shows change by eye and leaves no measurement to set against the next check-in.

FitXpress, the 3DLOOK body scan, turns 2 photos in the Echelon app into one timestamped record through the API, with 80+ body measurements and body composition estimates.

How often does a program block get reviewed once it is live?

Nick
--- M2
Hi Kevin,

A program owner could review girths and lengths along with the fat and lean mass estimates for each scan. Repeated scans typically differ by less than 1 cm for most evaluated measurements.

Calendar, if you want to talk it through:
https://meetings.hubspot.com/nick-omelchak

Nick

=== becca-valente-31b59424 | Becca Valente | Senior Director, Content & Programming | angle coaching P2
--- M1
Hi Becca,

The Meridian Reformer brought personalized programming to connected Pilates at Echelon, and programming like that raises the question of what changed in a member's body after a block. Home photos and tape differ in pose and light between check-ins, which makes that comparison drift.

In the Echelon app, a member would take 2 guided photos with FitXpress on their own phone, and the API returns one timestamped record with 80+ body measurements and fat and lean mass estimates.

After a Reformer block, which body changes would a coach want to see?

Nick
--- M2
Hi Becca,

A pilot would compare one cohort that scans at onboarding and at the first check-in with a comparable cohort on the usual flow. Onboarding completion and day-30 retention are the comparison, scan completion and repeat scans are tracked in the scan cohort, and both sides sign off the success criteria up front.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

Want to build the pilot design together on a call?
https://meetings.hubspot.com/nick-omelchak

Nick

=== patmatthews | Patrick Matthews | Senior Technical Product Manager | angle product P3
--- M1
Hi Patrick,

Personal bests and leaderboard rank describe effort. The body itself stays unmeasured.

FitXpress would put a body record next to personal bests in the Echelon Fit app. It takes 2 guided photos on the member's phone and returns one timestamped record through the API, with 80+ body measurements and fat and lean mass estimates.

What does an Echelon Fit member see about their body today?

Nick
--- M2
Hi Patrick,

Each scan arrives with a timestamp and a processing status, and the app can show a member the latest record next to the personal bests.

If it is useful, pick a time here, or point me to whoever owns the progress experience:
https://meetings.hubspot.com/nick-omelchak

Nick

=== john-santo-096310149 | John Santo | Co-Founder and CPO at EchelonFit | angle product P2
--- M1
Hi John,

Workout Builder AI adjusts the next week from performance and feedback, and a weigh-in is a single total that says little about where the body changed.

FitXpress goes into the Echelon app through an SDK and the API, with the capture layer fixed. The member takes 2 guided photos on their own phone, and Echelon gets one timestamped record with 80+ body measurements and body composition estimates.

Which screens around a fixed capture would Echelon want in its own brand?

Nick
--- M2
Hi John,

Each scan comes back with a scan ID, which the Echelon app uses to link the record to the member profile.

It returns 80+ body measurements, under 45 seconds from the photos to structured results.

Easiest is a call, here is my calendar:
https://meetings.hubspot.com/nick-omelchak

Nick


######## iFIT (5)

=== danaehirsch | Danaé Hirsch | Director, Product Partnerships | angle partnership P3
--- M1
Hi Danaé,

A separate scanning app puts the member and the result under another brand, and what comes back depends on that app.

FitXpress would run inside the iFIT app under iFIT's brand. A member shoots 2 photos on a phone, and the API sends back one timestamped record with 80+ body measurements.

As Director of Product Partnerships you see which capabilities fit a membership.

How does a partner capability reach members of iFIT Pro today?

Nick
--- M2
Hi Danaé,

iFIT keeps its own brand and wording on the screens around the capture, and the record lands where members already look at progress in the iFIT app.

A call is the easiest route, and a name works just as well if the progress experience belongs to a colleague.
https://meetings.hubspot.com/nick-omelchak

Nick

=== stephanie-raterman | Stephanie Raterman | Director of Development and Production | angle coaching P3
--- M1
Hi Stephanie,

iFIT runs multi-week trainer-led programs, and judging a series from progress photos alone leaves no measurement to compare at the next check-in.

FitXpress from 3DLOOK would give each series a measured record: 2 guided photos in the iFIT app become 80+ body measurements and fat and lean mass estimates, returned through the API as one timestamped record.

When a trainer-led series ends, what does the team look at to judge it?

Nick
--- M2
Hi Stephanie,

The capture is guided on the member's own phone, with pose and framing help during the scan. Repeated scans typically differ by less than 1 cm for most evaluated measurements.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

Happy to go through it on a call, or point me to whoever owns coaching programs:
https://meetings.hubspot.com/nick-omelchak

Nick

=== daniellepeckskamp | Danielle Peckskamp | Subscription Retention Manager, Onboarding & Engagement | angle membership P3
--- M1
Hi Danielle,

A weigh-in is a single total, and in the first weeks of a membership it is often the only body number there is.

FitXpress would put a body scan into the iFIT onboarding flow. A new member's 2 photos return 80+ body measurements through the API, as one timestamped record.

Which moment in the first weeks of an iFIT Pro membership does the team watch most?

Nick
--- M2
Hi Danielle,

A pilot with new members would compare day-90 retention against a comparable cohort on the usual flow, with the pass mark set together beforehand.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

A call would cover the design, or point me to whoever runs new-member onboarding.
https://meetings.hubspot.com/nick-omelchak

Nick

=== shayne-k-jessop | Shayne Jessop | Senior Product Manager | angle product P2
--- M1
Hi Shayne,

iFIT's AI coach builds a weekly plan around a member's goals and progress, and much of that progress is workout data, which says little about the body change behind it.

FitXpress would give the plan a body check-in to draw on. From 2 guided photos in the iFIT app, the API returns one timestamped record with 80+ body measurements and body composition estimates.

Would a body check-in sit at the start of the AI coach plan or at its weekly review?

Nick
--- M2
Hi Shayne,

Each record arrives through the API with its processing status, and a scan ID ties it to the member profile.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

Want to walk through the AI coach fit on a call?
https://meetings.hubspot.com/nick-omelchak

Nick

=== sarah-miles-product | Sarah Miles | Product Manager | angle product P3
--- M1
Hi Sarah,

The main iFIT app shows personal workout stats and insights. Home photos and tape differ in pose and light between check-ins, which makes a body comparison drift.

FitXpress would add a body record to the stats and insights in the main iFIT app. A member takes 2 photos on their own phone, and the API returns one timestamped record with 80+ body measurements and fat and lean mass estimates.

What does a member see in the main iFIT app, beyond stats, to know their body changed?

Nick
--- M2
Hi Sarah,

The record keeps waist, hip and thigh values next to the fat and lean mass estimates, and a scan ID links all of it to the member profile in the iFIT app.

Grab a time here, or point me to the owner of the paid plan:
https://meetings.hubspot.com/nick-omelchak

Nick


######## Lose It! (5)

=== billy-hulbert | Billy Hulbert | Vice President, Commerce Partnerships | angle partnership P3
--- M1
Hi Billy,

A body scan from a separate app places the member and the result under another brand, and what comes back depends on that app.

FitXpress works inside the partner's own app. The member takes 2 guided photos on their phone, and the API returns one timestamped record with 80+ body measurements and fat and lean mass estimates.

A white-label body scan inside Lose It!'s paid plan keeps the member in Lose It!.

How does a new capability from a partner get into the Lose It! app?

Nick
--- M2
Hi Billy,

For a partner, the point is a capability the member meets inside the Lose It! paid plan, with Lose It!'s own screens around it. It goes in through the SDK and the API.

3DLOOK has worked with 100+ clients.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

Book a call here, or point me to whoever decides what goes onto the app roadmap:
https://meetings.hubspot.com/nick-omelchak

Nick

=== thosniles | Thos Niles | Senior Vice President Product Management | angle product P1
--- M1
Hi Thos,

In Lose It!, a weigh-in is read against the member's weight target and schedule.

A weigh-in gives one total, and where the body changed stays unknown. At that moment FitXpress could add a body scan inside the Lose It! app, and the member would see 80+ body measurements and fat and lean mass estimates from 2 guided photos next to the number, as one timestamped record.

Beyond the number and the schedule, what does a member see after a weigh-in?

Nick
--- M2
Hi Thos,

A pilot could put one member cohort through a body scan at onboarding while a comparable cohort keeps the usual flow, and compare onboarding completion and day-30 retention against criteria agreed before it starts.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

If a conversation helps, my calendar is here:
https://meetings.hubspot.com/nick-omelchak

Nick

=== pete-wierzbinski-38153610 | Pete Wierzbinski | VP of Engineering | angle referral P3
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

=== taylor-smyrnos | Taylor Smyrnos | Senior Director, Product | angle product P2
--- M1
Hi Taylor,

Lose It! Premium members can type in body measurements under Advanced Tracking.

Tape and photos taken at home differ in pose and light between check-ins. FitXpress would add a guided record to that area of the app: a member takes 2 photos, front and side, with pose guidance, and the record that returns carries 80+ body measurements and fat and lean mass estimates.

Once a Premium member types in body measurements, where do they show up in the app?

Nick
--- M2
Hi Taylor,

A Premium member's typed measurements could sit beside a scan's waist and hip values on the same screen. Repeated scans typically differ by less than 1 cm for most evaluated measurements.

I can take you through it on a call. Slots here, or point me to whoever runs onboarding:
https://meetings.hubspot.com/nick-omelchak

Nick

=== burtonhohman | Burton Hohman | Principal Product Manager | angle product P2
--- M1
Hi Burton,

Your headline is about helping people track what they eat, and Lose It! also tracks weight and activity next to food.

A FitXpress scan would add one more entry beside them, built from 2 guided photos taken inside the app, with 80+ body measurements and fat and lean mass estimates in a timestamped record.

A progress photo shows visible change and leaves no measurement to compare at the next check-in.

Would a body scan belong at onboarding in Lose It!, or at a member's first weigh-in?

Nick
--- M2
Hi Burton,

The scan returns 80+ body measurements, under 45 seconds from the photos to structured results. Waist and hip change could then sit beside the weight log.

A short call would cover it. Open times are here, or point me to whoever owns Premium:
https://meetings.hubspot.com/nick-omelchak

Nick


######## Caliber (5)

=== jmcluff | Jared Cluff | Co-Founder and CEO | angle leadership P2
--- M1
Hi Jared,

A weigh-in is a single total, and where the body changed stays out of sight.

Caliber runs a free app for logging and self-guided plans, with Premium Coaching as the paid step. FitXpress would sit at that step in Caliber's own app, where 2 guided photos taken by the member become a timestamped record of 80+ body measurements and fat and lean mass estimates for the program, under Caliber's brand.

When something new is considered for Premium Coaching, how does the team decide?

Nick
--- M2
Hi Jared,

A pilot could compare free-to-premium conversion between a cohort that sees 3D Body Progress tracking and 3D Goal Visualization as paid-plan features and a comparable cohort on the usual flow, against success criteria agreed before it starts.

The integration runs on the SDK and the API together. There is no integration fee.

A call is easy to set up here:
https://meetings.hubspot.com/nick-omelchak

Nick

=== ajbednarek | Adam B. | Director of Engineering | angle referral P3
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

=== annakatedavis | Anna Kate Davis | Director of Product | angle product P2
--- M1
Hi Anna Kate,

Caliber's progress tracking screen brings logged training and progress photos into one view.

At 3DLOOK we built FitXpress to add a body check-in to that view. The member takes the guided photos inside the Caliber app, and the screen receives one timestamped record with 80+ body measurements and fat and lean mass estimates.

Photos and tape taken at home vary in pose and light between check-ins, which makes two readings hard to compare.

What does a member see on the progress screen after the first check-in, beyond weight and workouts?

Nick
--- M2
Hi Anna Kate,

Between two check-ins the screen could show how waist and hip moved, next to fat and lean mass estimates.

The scan returns 80+ body measurements, under 45 seconds from the photos to structured results.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

Pick a time that suits you, or point me to whoever runs onboarding:
https://meetings.hubspot.com/nick-omelchak

Nick

=== justin-fauci | Justin Fauci | Co-Founder and CTO | angle leadership P3
--- M1
Hi Justin,

A check-in form holds only what the member types in.

Through the API, FitXpress hands the platform one timestamped record per body scan, linked to the member profile and holding 80+ body measurements and body composition estimates from 2 guided photos on the member's phone.

Caliber's app holds body stats and progress photos already, which leaves the question of where a new record would sit beside them.

Where do body stats and photos sit in Caliber's data today?

Nick
--- M2
Hi Justin,

The SDK comes for web and mobile, on iOS and Android, and Caliber keeps its own screens around a capture layer that stays fixed for measurement quality.

Open slots are on my calendar:
https://meetings.hubspot.com/nick-omelchak

Nick

=== chris-muir | Chris Muir | Co-Founder and CPO | angle product P1
--- M1
Hi Chris,

Caliber's weekly progress review rests on logged training, synced body stats and progress photos.

A photo shows that something changed, but it leaves the next review nothing measured to compare against.

When the coach opens the review, FitXpress can have a timestamped record waiting beside the photos: 80+ body measurements and fat and lean mass estimates, from 2 guided photos the member took on their own phone inside the Caliber app.

At the weekly review today, what body data sits next to the photos?

Nick
--- M2
Hi Chris,

Caliber links each record to the member profile through the scan ID. Repeated scans typically differ by less than 1 cm for most evaluated measurements.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

If a call helps, my calendar is here:
https://meetings.hubspot.com/nick-omelchak

Nick


######## Ergatta (5)

=== luanaperez | Luana Perez | Sr. Director of Customer Experience | angle referral P3
--- M1
Hi Luana,

On a strength or rowing program, body weight can hold steady while the waist and the fat and lean mass move.

Ergatta's app shows members rankings by age group and weight group, along with personal records and weekly stats.

With 3DLOOK's FitXpress, the app could add a body scan: a member takes 2 guided photos and the app receives one timestamped record with 80+ body measurements and fat and lean mass estimates.

When members ask about their results, what are they usually asking Ergatta to show them?

Nick
--- M2
Hi Luana,

The record includes waist and thigh girths, and Ergatta decides which scans a member sees next to their rankings.

Here is my calendar, or point me to whoever owns the member app's progress experience:
https://meetings.hubspot.com/nick-omelchak

Nick

=== prasanna-swaminathan-6bbb4713 | Prasanna Swaminathan | Co-Founder & CTO | angle leadership P3
--- M1
Hi Prasanna,

Ergatta's recent rower update standardized in-game metrics across experiences, and the app keeps them on a stats dashboard.

A check-in form holds only what the member enters, and the dashboard holds in-game metrics. FitXpress would add a body scan: through the API the platform receives one timestamped record with its processing status, linked to the member profile by the scan ID, carrying 80+ body measurements and body composition estimates from 2 guided photos on the member's phone.

How does a new data source reach the stats dashboard today?

Nick
--- M2
Hi Prasanna,

Web and mobile SDKs are available for iOS and Android. The scan returns 80+ body measurements, under 45 seconds from the photos to structured results.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

Calendar for a call is here:
https://meetings.hubspot.com/nick-omelchak

Nick

=== alessandra-gotbaum | Alessandra Gotbaum | Co-Founder & COO | angle leadership P2
--- M1
Hi Alessandra,

Photos and tape measures taken at home vary in pose and light between check-ins, which makes two readings hard to compare.

With pose and framing guidance during capture, a member takes 2 photos, front and side, on their phone inside the app, and FitXpress returns 80+ body measurements and body composition estimates as a timestamped record.

Ergatta's program paths run from beginner to intermediate opponents.

What does a member see about their own body as they move up that path?

Nick
--- M2
Hi Alessandra,

A member's waist and hip at the first scan and again a few weeks up the path could sit side by side in the Ergatta app.

3DLOOK has worked with 100+ clients.

You can book a call with me here:
https://meetings.hubspot.com/nick-omelchak

Nick

=== tom-aulet-85493127 | Tom Aulet | Co-Founder & CEO | angle leadership P2
--- M1
Hi Tom,

Ergatta members row against opponents, and splits and rankings describe the work done in the game.

Under Ergatta's own brand, FitXpress turns 2 guided photos from the member's phone into one timestamped record with 80+ body measurements and fat and lean mass estimates.

What is Ergatta promising its members next, and where would a measured body check-in fit?

Nick
--- M2
Hi Tom,

Ergatta's brand and screens carry the scan and its record, with the capture layer fixed for measurement quality. It goes in through the SDK and the API. There is no integration fee.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

If it fits, reserve a time here:
https://meetings.hubspot.com/nick-omelchak

Nick

=== an-li-5662b365 | An Li | Group Product Manager | angle product P3
--- M1
Hi An,

A progress photo shows visible change and gives the next check-in nothing measured to compare.

In Ergatta's app, a member could take 2 guided photos on their phone and FitXpress would return 80+ body measurements and fat and lean mass estimates as one timestamped record.

Ergatta's app asks members for their weight to place them in rankings, and its dashboard shows personal records and weekly stats.

Beyond weight, what body information does Ergatta hold about a member today?

Nick
--- M2
Hi An,

A progress screen could line up two records side by side, each tied to the member profile through the scan ID. Repeated scans typically differ by less than 1 cm for most evaluated measurements.

Pick a slot here, or point me to whoever owns the progress screens:
https://meetings.hubspot.com/nick-omelchak

Nick


######## MacroFactor (3)

=== rkekelis | Rebecca K. | Co-Founder & Developer | angle leadership P3
--- M1
Hi Rebecca,

MacroFactor's Body Metrics allows members to tape-measure sites such as waist and hips and take front, side and back photos to compare side by side.

A photo shows visible change and gives the next check-in no measurement to compare.

Beside those photo views, a guided capture of 2 photos, front and side, could sit inside MacroFactor, and FitXpress would return 80+ body measurements and fat and lean mass estimates as one timestamped record.

Which of the screens around that capture would you want built in MacroFactor's own look?

Nick
--- M2
Hi Rebecca,

Each scan carries a scan ID that links its record to the member profile, and the capture layer stays fixed to protect measurement quality.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

Calendar link for a call is below:
https://meetings.hubspot.com/nick-omelchak

Nick

=== greg-nuckols-92545595 | Greg Nuckols | Co-Owner | angle science P3
--- M1
Hi Greg,

Home photos and tape differ in pose and light between check-ins, which limits how far two readings can be compared.

As co-owner of MacroFactor you decide what body data earns a place in a check-in. FitXpress guides a repeatable capture inside MacroFactor, with 2 photos, front and side, on the member's phone, and a timestamped record returns 80+ body measurements and fat and lean mass estimates.

What would the team need to see before body data shapes a check-in?

Nick
--- M2
Hi Greg,

Fat and lean mass are estimates derived from the measurements with height and, where provided, weight.

Repeated scans typically differ by less than 1 cm for most evaluated measurements.

A call is easy to set up here:
https://meetings.hubspot.com/nick-omelchak

Nick

=== corydavisprofile | Cory Davis | Co-Founder & Developer | angle leadership P3
--- M1
Hi Cory,

Your bio puts you in the MacroFactor app and its community at every hour of the day.

A body scan from a separate app puts the member and the result under another brand. Inside MacroFactor, FitXpress would be an SDK and the API, and the member's 2 guided photos on their phone come back as one timestamped record with 80+ body measurements and fat and lean mass estimates.

When a body capture comes up, how do you weigh building it against integrating one?

Nick
--- M2
Hi Cory,

Setup starts with the web or mobile SDK for iOS and Android, with the API alongside, and each record comes back with its processing status.

My calendar is open here:
https://meetings.hubspot.com/nick-omelchak

Nick


######## Interactive Strength (3)

=== deepakmm | Deepak M. | Board Member, Chief Technology Officer | angle product P2
--- M1
Hi Deepak,

CLMBR's companion app was rebuilt as a native iOS app earlier this month, and the FORME app has its own progress view.

A body scan from a separate app puts the member and the result under another brand, and what returns to the platform depends on that app. FitXpress would run inside the CLMBR and FORME apps themselves. Inside the apps, the API returns one timestamped record with 80+ body measurements and body composition estimates after the member's 2 guided photos.

Around the guided capture itself, which screens, such as onboarding and results, would you want in the CLMBR and FORME look?

Nick
--- M2
Hi Deepak,

On the build side, the SDK and the API together are the recommended setup. The capture layer stays fixed to protect measurement quality, the screens around it stay yours, and each record links to the member profile through the scan ID.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

My calendar is here, or point me to whoever owns the FORME app roadmap:
https://meetings.hubspot.com/nick-omelchak

Nick

=== bentbartlett | Ben Bartlett | President & Chief Operating Officer | angle leadership P2
--- M1
Hi Ben,

A coach who sets the next block from weight and photos has no measured change to compare.

At FORME each member has a dedicated trainer and a personalized plan every week. FitXpress would give the trainer a record to open before the next plan. Under the FORME brand, the member's 2 guided photos become a record with 80+ body measurements and fat and lean mass estimates, timestamped.

What does a FORME trainer have in front of them at the weekly check-in besides the member's own notes?

Nick
--- M2
Hi Ben,

The trainer and the member can look at the same record, and the next plan can start from the measured change between two check-ins.

Integration runs on the iOS and Android SDKs with the API. There is no integration fee.

To talk it through, book here:
https://meetings.hubspot.com/nick-omelchak

Nick

=== trent-ward-12b992b2 | Trent Ward | Founder & CEO | angle leadership P2
--- M1
Hi Trent,

Members train through the FORME and CLMBR apps, and a body check-in could live there under your own brands.

FitXpress needs only the member's phone. Two guided photos taken in the app are enough for the apps to receive one timestamped record, with 80+ body measurements and fat and lean mass estimates.

A weigh-in gives one total and says little about where the body changed.

How do you decide which member features get a pilot at FORME and CLMBR?

Nick
--- M2
Hi Trent,

Members could be split at random where practical: one group scans at onboarding and at the first check-in, the other keeps today's flow. Onboarding completion and day-30 and day-90 retention are compared against success criteria agreed beforehand, and if those are met, the scan goes live for members on the matching plan.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

A call would cover the details. Slots are here:
https://meetings.hubspot.com/nick-omelchak

Nick


######## Future (3)

=== jasonbhwang | Jason Hwang | VP of Partnerships | angle partnership P3
--- M1
Hi Jason,

A body scan from a separate app puts the member and the result under another brand, and what comes back to the platform depends on that app.

You lead partnerships across product and distribution at Future, and Future Pro is the app where members meet their coach each week.

As a white-label body scan inside that app, FitXpress takes 2 guided photos on the member's phone and sends the platform one timestamped record through the API, with 80+ body measurements and body composition estimates.

How does a partner capability get into the Future Pro app today?

Nick
--- M2
Hi Jason,

The integration is web and mobile SDKs for iOS and Android, with one structured record per scan through the API, linked to the member profile by the scan ID.

3DLOOK has worked with 100+ clients.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

Book a call here, or point me to whoever on the product side decides what enters the app:
https://meetings.hubspot.com/nick-omelchak

Nick

=== jake-grundstein | Jake Grundstein | Head of Member Operations | angle membership P3
--- M1
Hi Jake,

Future Pro members check in with their coach every week, and the coach monitors progress and refines the plan from it.

A check-in form holds only what the member enters. FitXpress would give the coach a body scan to review beside the plan: the member takes 2 guided photos in the Future Pro app, and the coach gets a timestamped record with 80+ body measurements.

Which moment in a member's first month does the team watch most closely?

Nick
--- M2
Hi Jake,

One cohort of new members could get a body scan at onboarding and again at the first check-in, while a matched cohort keeps today's flow. Day-30 and day-90 retention would be read against criteria both sides agree on up front.

If the coach side belongs to someone else, point me to whoever runs it. Here is a link to my calendar:
https://meetings.hubspot.com/nick-omelchak

Nick

=== jakequan | Jake Quan | Product Manager | angle product P3
--- M1
Hi Jake,

Future Pro shows members visualized workout reports and a view of their progress.

A progress photo shows visible change and gives the next check-in nothing measured to compare.

FitXpress can feed that view a body check-in under the Future brand. The member takes 2 guided photos on their phone, and the record that comes back is timestamped and holds 80+ body measurements and fat and lean mass estimates.

What does a member see in the progress view after the first check-in, beyond workout reports?

Nick
--- M2
Hi Jake,

A progress view could show waist and thigh change between two check-ins. The scan returns 80+ body measurements, under 45 seconds from the photos to structured results.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

Grab a time here if it is useful, or point me to whoever owns onboarding:
https://meetings.hubspot.com/nick-omelchak

Nick


######## Fitbod (2)

=== jessventicinque | Jesse Venticinque | Co-Founder, CPO | angle product P1
--- M1
Hi Jesse,

Fitbod has been putting more weight on helping members read their own progress inside the app.

Training metrics show the work done and say little about how the body changed. With FitXpress, the member takes 2 guided photos on their phone under Fitbod's brand, and the API returns one timestamped record with 80+ body measurements and fat and lean mass estimates.

Would a body scan belong at onboarding in Fitbod, or later, once a member has a few weeks of logged sets?

Nick
--- M2
Hi Jesse,

The SDK and the API together are the recommended setup, and Fitbod keeps its own screens around the capture.

The scan returns 80+ body measurements, under 45 seconds from the photos to structured results.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

Book a call here if it fits:
https://meetings.hubspot.com/nick-omelchak

Nick

=== alisa-aguirre | Alisa Calderon | Head of Customer Success | angle referral P3
--- M1
Hi Alisa,

Your headline mentions turning feedback into impact, and Fitbod members see their strength progress through logged sets and workout history.

On a strength program, body weight can hold while the waist and the fat and lean mass move, and lifts alone do not show that.

3DLOOK's FitXpress is a body scan members run on their own phone inside the Fitbod app, from 2 guided photos, and its record carries 80+ body measurements and fat and lean mass estimates.

When members write in about progress, how often is it about their lifts and how often about their body?

Nick
--- M2
Hi Alisa,

Each scan is tied to the member profile through the scan ID. A progress question from a member can be answered from two records side by side.

My calendar is below if a call is easier than typing. If someone else owns the app's progress experience, point me to them:
https://meetings.hubspot.com/nick-omelchak

Nick


######## RP Strength (2)

=== andrewzey | Andrew Zey | Co-Founder & Chief Product Officer | angle product P1
--- M1
Hi Andrew,

At RP Strength, RP Diet Coach takes a member's weigh-ins into a weekly review with recommended adjustments.

A weigh-in gives one total and says little about where the body changed. Next to the trend, FitXpress would put a measured record in the weekly review. The member's 2 guided photos in the RP app become 80+ body measurements and fat and lean mass estimates, timestamped.

Beyond the weigh-in trend, what does a member see in the weekly review about their body?

Nick
--- M2
Hi Andrew,

A weekly review could set one scan's waist and hip values beside the next review's. Repeated scans typically differ by less than 1 cm for most evaluated measurements.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

Easiest to show on a call, and my calendar is here:
https://meetings.hubspot.com/nick-omelchak

Nick

=== js531 | Jacob S. | Chief Operating Officer | angle leadership P3
--- M1
Hi Jacob,

On a strength program, body weight can hold while the waist and the fat and lean mass move.

RP Strength's apps are paid products, and a new feature in them needs a way to be judged before rollout. FitXpress would give them a body check-in to test, with 2 guided photos on the member's phone returning 80+ body measurements and body composition estimates as a timestamped record.

How does RP Strength judge a new paid feature before rollout?

Nick
--- M2
Hi Jacob,

A pilot could read onboarding completion and day-30 retention in a cohort that scans at the first check-in against a comparable cohort on the usual flow, with success criteria agreed before it starts. The scan makes no decision about any member.

The scan goes in through the iOS and Android SDKs with the API. There is no integration fee.

A call can be booked here, or point me to whoever owns the roadmap for RP's paid apps:
https://meetings.hubspot.com/nick-omelchak

Nick


######## Ladder (2)

=== ryan-mott-51660a11 | Ryan Mott | VP, Product | angle product P3
--- M1
Hi Ryan,

Your title covers data product at Ladder, where the Journal holds reps, weights and PR alerts.

Logged reps and weights describe the work done in training, and a body signal needs a record of its own. A FitXpress scan brings that in through 2 guided photos, which return 80+ body measurements and body composition estimates through the API as one timestamped record, linked to the member by the scan ID.

Which fields would a data product need on each record to use it next to Journal data?

Nick
--- M2
Hi Ryan,

Each record carries a processing status, which allows a data job to tell a finished scan from one still processing. The scan returns 80+ body measurements, under 45 seconds from the photos to structured results.

Calendar link for a call, or point me to whoever owns the member app and its progress screens:
https://meetings.hubspot.com/nick-omelchak

Nick

=== bmaloley | Brett Maloley | Founder | angle leadership P2
--- M1
Hi Brett,

A coach planning the next block from training logs and body weight has no measured body change to compare.

In Ladder, a member's team coach follows reps, weights and PRs through the Ladder Journal. A FitXpress scan in the Ladder app would hand that coach one timestamped body record from 2 guided photos, with 80+ body measurements and fat and lean mass estimates, under Ladder's own brand.

How does Ladder decide which new features reach members?

Nick
--- M2
Hi Brett,

A pilot could compare onboarding completion between a cohort that scans at the first check-in and a comparable cohort that does not, against criteria agreed beforehand.

3DLOOK has worked with 100+ clients.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

A call can go on my calendar here:
https://meetings.hubspot.com/nick-omelchak

Nick


######## Carbon Diet Coach (2)

=== john-ybarra-mba | John Ybarra | Vice President Operations | angle product P2
--- M1
Hi John,

Carbon's check-in report explains every adjustment it makes to a member's targets.

That explanation rests on a weight trend, and a weigh-in trend is a single total where the body's changes stay unknown.

FitXpress could add a measured input. Inside Carbon's own app a member takes 2 guided photos, and the scan returns 80+ body measurements and fat and lean mass estimates, shown on Carbon's own results screen.

How would the team test a new input to the weekly check-in before members see it?

Nick
--- M2
Hi John,

On Carbon's results screen, waist and hip change between two check-ins could sit next to the explanation of each adjustment. The scan ID links each record to the member profile.

3DLOOK has worked with 100+ clients, including fitness teams.

Calendar for a call below, and if the check-in report belongs to someone else, point me to them:
https://meetings.hubspot.com/nick-omelchak

Nick

=== keith-kraker | Keith Kraker | Co-Founder | angle leadership P3
--- M1
Hi Keith,

On a strength or recomposition program, body weight can hold steady while the waist and the fat and lean mass move.

Carbon sets a member's protein target from lean body mass, and body fat and lean mass appear only where members enter or sync them.

FitXpress can return fat and lean mass estimates, derived from 80+ body measurements, after 2 guided photos taken in Carbon's own app, as a timestamped record.

Where does the lean body mass behind a protein target come from for most members today?

Nick
--- M2
Hi Keith,

A pilot could compare day-30 retention between a cohort that scans at onboarding and a comparable cohort that keeps the usual flow, against success criteria agreed before it starts.

The iOS and Android SDKs and the API are the way in. There is no integration fee.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

A call can work around your schedule. Open times sit on my calendar here:
https://meetings.hubspot.com/nick-omelchak

Nick


######## Exercise.com (2)

=== philip-morton | Philip Morton | Director of Customer Success | angle referral P3
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

=== sarah-miller-5960a690 | Sarah Miller | Director of Trainer Success | angle coaching P3
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


######## Hydrow (1)

=== matt-lehrer-67664014 | Matt Lehrer | Chief Rowing Strategy Officer | angle coaching P2
--- M1
Hi Matt,

Hydrow's programs are led by athletes, in rowing and on the strength side, and your background in coaching education fits that.

Stroke rate, splits and racing stats describe the work done in a block. Next to them, a body scan from FitXpress records where the body stands at each check-in: a member takes 2 guided photos on their own phone in the Hydrow app, and a timestamped record returns 80+ body measurements and fat and lean mass estimates.

When a member finishes a block, how do they see where their body stands compared with the start?

Nick
--- M2
Hi Matt,

The member and the athlete leading a program can look at the same timestamped record. Repeated scans typically differ by less than 1 cm for most evaluated measurements.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

Happy to take you through it on a call. Times are here, or point me to whoever runs the member app's progress side:
https://meetings.hubspot.com/nick-omelchak

Nick


######## Trainwell (1)

=== gabe-madonna | Gabe Madonna | Co-Founder & CTO | angle leadership P3
--- M1
Hi Gabe,

Every Trainwell member starts with an onboarding session on video, and the trainer builds and adapts each workout from there.

On a recomposition program, body weight can hold while the waist and the fat and lean mass move. Through an SDK and the API, with Trainwell's own screens, FitXpress would hand the trainer a timestamped record to review before the next program block. The member takes 2 guided photos on their phone, and the record holds 80+ body measurements and fat and lean mass estimates.

For members who come in for body recomposition, what would a trainer do with waist and thigh changes?

Nick
--- M2
Hi Gabe,

Between sessions the member captures on their own phone, with pose and framing guidance during capture. 3DLOOK has worked with 100+ clients, including fitness teams.

https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/

To walk through it, book a time here:
https://meetings.hubspot.com/nick-omelchak

Nick


######## Jefit (1)

=== bansal-nitin | Nitin Bansal | Product Manager | angle product P3
--- M1
Hi Nitin,

Your headline mentions growth and monetization, and Jefit's paid Elite plan adds the Adaptive AI Coach and an analytics dashboard. Members already type in body weight, body fat and tape measurements.

Tape and photos taken at home differ in pose and light between check-ins. On Jefit's own results screen, a FitXpress body scan would show 80+ body measurements and fat and lean mass estimates from 2 guided photos, returned as a timestamped record.

What do members upgrade to Elite for today?

Nick
--- M2
Hi Nitin,

On the FitXpress Pro plan, 3D Body Progress tracking and 3D Goal Visualization could sit in Elite as paid-plan features. A pilot could compare free-to-premium conversion between a cohort with the scan and a comparable cohort without it, against criteria agreed before it starts.

Book a slot here, or point me to whoever owns Elite:
https://meetings.hubspot.com/nick-omelchak

Nick
