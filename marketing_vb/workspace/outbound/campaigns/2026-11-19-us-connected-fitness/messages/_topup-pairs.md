# 2026-11-19-us-connected-fitness: 41 top-up pairs for Vadim's review (2026-11-20)

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
