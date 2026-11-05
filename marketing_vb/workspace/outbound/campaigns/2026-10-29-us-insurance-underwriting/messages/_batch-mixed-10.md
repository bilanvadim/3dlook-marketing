@@@ laura-mckiernan
hook: Bestow's rules engine where carriers set their own thresholds
proof: two photos, flag at carrier threshold (card Rules, Account facts Bestow)
--- M1
Hi Laura,

Quick thought on Bestow's underwriting platform, where carriers set their own risk thresholds and decide which cases go to instant issue.

FitXpress adds two photos to the e-application and returns a Smart Scales weight estimate, BMI from the declared height, and a flag when the gap crosses the carrier's threshold, as one timestamped record.

Where would a build referral sit among those decision options?

Nick
--- M2
Hi Laura,

One integration could serve several carriers on your platform: API and web and mobile SDKs, with one timestamped record per applicant returned to Bestow. The page at https://3dlook.ai/for-insurance-underwriting/ shows how that record sits beside a carrier's own thresholds.

FitXpress is not a medical device and does not make underwriting decisions.

If you want to see how a build flag would slot into the engine's routing, here is my calendar: https://meetings.hubspot.com/nick-omelchak

Nick
@@@ malenoir
hook: his product work at MetaMap and Procore
proof: two photos, flag at threshold; speed sentence (card Rules)
--- M1
Hi David,

Noticed your product work at MetaMap and Procore.

A step of two photos is what FitXpress adds to the e-application. It returns a Smart Scales weight estimate, a flag at the carrier's threshold, and the BMI that follows from the height entered.

In Bestow's journeys for agents and for applicants, where would you try a step like that first?

Nick
--- M2
Hi David,

A scan runs under 45 seconds from the photos to structured results. Completion would be measured in an evaluation that keeps outputs out of live cases.

FitXpress is not a medical device and does not make underwriting decisions.

If a test of the step across those journeys sounds useful, I would be glad to plan it on a call: https://meetings.hubspot.com/nick-omelchak

Nick
@@@ ericwonsuklee
hook: Bestow Labs news, a team building AI-native products apart from production
proof: two photos, API and SDKs (card Rules, Account facts Bestow)
--- M1
Hi Eric,

Saw the news on Bestow Labs, the team building AI-native products fully apart from production systems.

Our scan, FitXpress, takes two photos in the e-application and sends back one timestamped record: a Smart Scales weight estimate, a BMI calculated from the applicant's height and a flag above the carrier's threshold.

For a new data input like that, what would it take to move from Labs into the production engine?

Nick
--- M2
Hi Eric,

FitXpress comes as an API with web and mobile SDKs, returning one timestamped record per applicant. A first try could sit in Labs, with outputs kept out of live decisions.

FitXpress is not a medical device and does not make underwriting decisions.

If integrations belong to a platform team, I would gladly speak with them first. Otherwise a call about trying it in Labs fits here: https://meetings.hubspot.com/nick-omelchak

Nick
@@@ david-peters-9b1b6898
hook: cases Bestow sends to instant issue
proof: two photos, flag at carrier threshold (card Rules)
--- M1
Hi David,

Got me thinking about the cases Bestow sends to instant issue.

FitXpress is a step of two photos we built: the declared height anchors the BMI, Smart Scales estimates weight, and the carrier's threshold decides whether a flag is raised. One timestamped record lands on the case.

On cases that go to instant issue, how is build looked at today?

Nick
--- M2
Hi David,

For an underwriter the value sits in the record: timestamped, on the case file, with a flag raised only above the threshold the carrier sets. A comparison with build from paramedical exam cases would show how the flag lines up.

FitXpress is not a medical device and does not make underwriting decisions.

If it helps to walk through that comparison for instant-issue cases, grab a time here: https://meetings.hubspot.com/nick-omelchak

Nick
@@@ dbelanger1
hook: review of a new data vendor
proof: data handling forms from compliance.md; privacy FAQ link
--- M1
Hi Dave,

Wanted to reach out about how Bestow reviews a new data vendor.

FitXpress is a capture of two photos inside the e-application. It sends the carrier's systems one timestamped record: a Smart Scales weight estimate, a BMI based on the height entered and a flag at the carrier's threshold.

When a vendor like that comes up for review, what does your team ask for first, the data flow or the retention terms?

Nick
--- M2
Hi Dave,

Data handling: TLS in transit and S3-managed encryption at rest. Photos are deleted after processing or within 30 days per the carrier's policy, retained photos are blurred, faces are obscured at capture, and scan records sit on random identifiers. Documents for your review go through legal@3dlook.me.

FitXpress is not a medical device and does not make underwriting decisions.

If a walk through the data flow and retention terms would help your review, this is my calendar: https://meetings.hubspot.com/nick-omelchak

Nick
@@@ nicholelmyers
hook: Ethos says its automated decisions are audited
proof: two photos, flag at threshold; shadow evaluation path (card Rules)
--- M1
Hi Nichole,

Noticed that Ethos audits its automated decisions.

FitXpress is a step of two photos for the application: it returns a Smart Scales weight estimate, BMI from the declared height, and a flag when the gap crosses a threshold your team sets, as one timestamped record.

In those audits, how does build get treated?

Nick
--- M2
Hi Nichole,

A shadow evaluation could count how many flags each candidate threshold raises, then compare them with build from paramedical exam cases, with no output reaching a case. That path is described on https://3dlook.ai/for-insurance-underwriting/ in the use-case summary.

FitXpress is not a medical device and does not make underwriting decisions.

If the audit angle is where to start, a call could shape the design around your audit sample: https://meetings.hubspot.com/nick-omelchak

Nick
@@@ spflan
hook: Ethos takes applications with no medical exams and a few health questions
proof: two photos; 3.5% sentence in M2 (underwriting lane, card Rules)
--- M1
Hi Sean,

Caught my eye that Ethos takes applications with no medical exams and just a few health questions.

Our FitXpress step takes two photos at application. A Smart Scales weight estimate comes back with a BMI worked out from the height entered, and a gap beyond the threshold you set raises a flag.

Where in the instant-decision rules would a build referral rule sit?

Nick
--- M2
Hi Sean,

Smart Scales gives a weight estimate with approximately 3.5% mean absolute error under evaluated conditions, not a scale reading. A referral threshold would sit well above that, on gaps that change the class.

FitXpress is not a medical device and does not make underwriting decisions.

I would be glad to go through where such a rule fits in your flow on a call: https://meetings.hubspot.com/nick-omelchak

Nick
@@@ vipulethos
hook: engineering background at Indeed before Ethos
proof: two photos, SDK, REST API (card Rules)
--- M1
Hi Vipul,

Curious about your take, given engineering at Indeed before Ethos.

FitXpress ships as an SDK step in the application. Two photos in, one timestamped structured record out, with a Smart Scales weight estimate and a flag at the threshold set in your rules.

How would a record like that reach your decisioning service, through a request at submission or as an event afterwards?

Nick
--- M2
Hi Vipul,

FitXpress comes as a REST API with SDKs. The record returns to your systems only, scan records sit on random identifiers, and photos are deleted after processing or within 30 days per your policy.

FitXpress is not a medical device and does not make underwriting decisions.

I can take you through the integration on a call: https://meetings.hubspot.com/nick-omelchak

Nick
@@@ ashwath-muralidharan-945a415
hook: Ethos's ChatGPT app for instant term estimates
proof: two photos; speed sentence (card Rules)
--- M1
Hi Ashwath,

Saw the news on Ethos's ChatGPT app for instant term estimates.

With FitXpress, two photos taken in the application return a Smart Scales weight estimate, the resulting BMI and a flag when a gap crosses the line Ethos's rules draw, in one timestamped record.

Would a step like that fit better right after the estimate or inside the application itself?

Nick
--- M2
Hi Ashwath,

In a flow that is already instant, completion matters most. The scan finishes under 45 seconds from the photos to structured results.

FitXpress is not a medical device and does not make underwriting decisions.

If tests of new steps in the agent channel run through another group, I am happy to speak with them first. Otherwise a call about where the step fits between estimate and application works well: https://meetings.hubspot.com/nick-omelchak

Nick
@@@ rmackillop
hook: Ladder's fully digital path and the at-home health check
proof: two photos, flag at threshold; shadow evaluation (card Rules)
--- M1
Hi Ryan,

Quick one on Ladder's fully digital path, with a few health questions and no medical exam.

FitXpress adds two photos and returns a Smart Scales weight estimate, BMI from the declared height and a flag when the gap crosses a threshold your team sets, as one timestamped record.

Where would a large gap route on that path, to an underwriter or to the at-home health check?

Nick
--- M2
Hi Ryan,

A shadow evaluation would run on applicants whose weight is measured anyway, compare the estimate with that measured weight, and count flags at each level you try, with outputs kept out of decisions. You can see the full path on https://3dlook.ai/for-insurance-underwriting/ in the use-case page.

FitXpress is not a medical device and does not make underwriting decisions.

I would welcome a call on how such an evaluation fits the fully digital path: https://meetings.hubspot.com/nick-omelchak

Nick
@@@ hale-laura
hook: Ebates employee number one, then co-founding Ladder
proof: two photos; speed sentence (card Rules)
--- M1
Hi Laura,

Noticed your path from Ebates employee number one to co-founding Ladder.

Two photos become one timestamped record with FitXpress: a Smart Scales weight estimate, a BMI calculated from the entered height and a flag above a threshold set in your rules.

In an application that takes minutes, would those photos go before or after the health questions?

Nick
--- M2
Hi Laura,

Speed decides whether a step stays in a flow like Ladder's. Each scan completes under 45 seconds from the photos to structured results.

FitXpress is not a medical device and does not make underwriting decisions.

If you would like to look at where the step fits in the application, my calendar is here: https://meetings.hubspot.com/nick-omelchak

Nick
@@@ keerthi-mandala
hook: consumer risk and growth remit
proof: two photos, flag at threshold (card Rules)
--- M1
Hi Keerthi,

Made me think about your split of consumer risk and growth at Ladder.

On our side, FitXpress turns two photos into a Smart Scales weight estimate, the matching BMI and a flag once a gap passes the line your risk rules draw, kept as one timestamped record.

How would you read drop-off from a new step in Ladder's instant flow?

Nick
--- M2
Hi Keerthi,

The evaluation we would propose measures completion, and results go back to the carrier only. Nothing reaches a decision during the test.

FitXpress is not a medical device and does not make underwriting decisions.

A short call to plan that test across the instant flow and the advisor channel would suit me: https://meetings.hubspot.com/nick-omelchak

Nick
@@@ katie-kahl-15049526
hook: iGO Evolve launch on an API-enabled architecture
proof: two photos, API/SDKs (card Rules)
--- M1
Hi Katie,

Saw the news on iPipeline's iGO Evolve and its API-enabled architecture.

FitXpress is a step of two photos for the e-application. It returns a Smart Scales weight estimate, BMI from the declared height, and a flag when the gap crosses the carrier's threshold, as one timestamped record.

Where in iGO Evolve would a carrier switch on a step like that?

Nick
--- M2
Hi Katie,

Carriers on your e-application could switch the step on through one integration: API and web and mobile SDKs, with one timestamped record per applicant returned to the platform. On https://3dlook.ai/for-insurance-underwriting/ you can see the build record a carrier would receive.

FitXpress is not a medical device and does not make underwriting decisions.

If mapping the step onto iGO Evolve is worth a conversation, my calendar is here: https://meetings.hubspot.com/nick-omelchak

Nick
@@@ chriscella
hook: Resonant and XRAE on iPipeline's site
proof: two photos, structured record (card Rules)
--- M1
Hi Chris,

Caught the Resonant and XRAE pages on iPipeline's site.

Two photos in the e-application return a Smart Scales weight estimate, the BMI it implies and a flag above the carrier's threshold, as one timestamped structured record from FitXpress.

Would that build record land best in Resonant's case management or in XRAE's field underwriting?

Nick
--- M2
Hi Chris,

The record is made to be read by a workbench: structured, timestamped, one per applicant, with the flag present only above a threshold the carrier sets.

FitXpress is not a medical device and does not make underwriting decisions.

If you would like to talk through the data mapping into Resonant or XRAE, here is my calendar: https://meetings.hubspot.com/nick-omelchak

Nick
@@@ alexctompkins
hook: Novera API Hub launch in August 2026
proof: two photos, REST API and SDKs (card Rules)
--- M1
Hi Alex,

Spotted the Novera API Hub, where API workflows get built and tested at iPipeline.

FitXpress takes two photos in the e-application and returns a timestamped record with a Smart Scales weight estimate, a calculated BMI and a flag above the carrier's threshold.

Would an outside evidence step like that connect through Novera, or through iGO's own configuration?

Nick
--- M2
Hi Alex,

On the technical side, FitXpress is a REST API with web and mobile SDKs, returning one timestamped record per applicant.

FitXpress is not a medical device and does not make underwriting decisions.

If another group curates what the Hub lists, I am glad to speak with them first. Otherwise a call on connecting it through Novera would suit me: https://meetings.hubspot.com/nick-omelchak

Nick
@@@ paul-greene-40b337a4
hook: April 2026 expansion of Foresters' accelerated underwriting, fluidless cases
proof: two photos; 3.5% sentence in M2 (underwriting lane, card Rules)
--- M1
Hi Paul,

Saw the news on the April expansion of accelerated underwriting at Foresters, with more applicants going fluidless.

FitXpress adds two photos to the e-App and returns a Smart Scales weight estimate, BMI from the declared height, and a flag when the gap crosses the threshold Foresters sets, as one timestamped record.

Where does build enter a fluidless case once tele-med, exam and labs are out?

Nick
--- M2
Hi Paul,

Smart Scales gives a weight estimate with approximately 3.5% mean absolute error under evaluated conditions, not a scale reading. A flag would refer only gaps well above that, at a threshold you set. The page at https://3dlook.ai/for-insurance-underwriting/ lists the evaluation steps.

FitXpress is not a medical device and does not make underwriting decisions.

I can take you through a shadow evaluation for the fluidless program on a call: https://meetings.hubspot.com/nick-omelchak

Nick
