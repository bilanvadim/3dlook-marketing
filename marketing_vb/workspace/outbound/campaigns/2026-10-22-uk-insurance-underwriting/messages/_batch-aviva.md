@@@ sue-hendry-a8415a17
hook: Aviva's June change to non-medical limits and the move of medical exams to nurse-led screening
proof: 2 photos; flag at insurer threshold; 3.5% line (proof-points / campaign rules)
--- M1
Hi Sue,

Saw the news on Aviva's non-medical limits and the move of medical exams to nurse-led screening. It leaves cases where build is declared and no screening follows.

FitXpress is a step for exactly those cases. Applicants take 2 photos, Smart Scales estimates their weight, and BMI is calculated from the declared height. A gap beyond Aviva's own threshold raises a flag, and Aviva's underwriters decide what follows.

On those cases, what does your team see today to judge build?

Katerina
--- M2
Hi Sue,

A shadow evaluation would count how many cases each candidate threshold flags and how often a flag matches separately collected build evidence. Smart Scales estimates weight at approximately 3.5% mean absolute error under evaluated conditions, and the estimate is not a scale reading.

In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes SCCs.

Happy to go through it: https://meetings.hubspot.com/katerina-galich

Katerina

@@@ james-whitty-05a1545a
hook: path from automation and philosophy into underwriting strategy and governance
proof: 2 photos; threshold flag; timestamped record
--- M1
Hi James,

Noticed your background, from automation and philosophy into underwriting strategy and governance at Aviva. Governance is where a new evidence source gets its rules.

What FitXpress returns is a record: a weight estimate from 2 photos, BMI worked out from the declared height, and a flag where the gap passes the threshold Aviva sets. It is timestamped and goes to Aviva's systems.

Where do you see gaps between declared and estimated weight mattering most for Aviva's build bands?

Katerina
--- M2
Hi James,

For governance, the evaluation comes before anything touches a case. Outputs stay out of decisions while a shadow run shows how many cases each threshold would flag.

In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes SCCs.

If a call would help, here is my diary: https://meetings.hubspot.com/katerina-galich

Katerina

@@@ michelle-cross-88958422
hook: moved from the philosophy and development desk to owning Aviva's underwriting philosophy
proof: 2 photos; 3.5% line; boundary sentence
--- M1
Hi Michelle,

Came across your work, from the philosophy and development desk to owning Aviva's underwriting philosophy. The evidence rules are yours to shape.

FitXpress works from 2 photos, and its flag appears only where Smart Scales and the declared weight differ by more than a threshold Aviva sets.

Which evidence would you want logged before a build flag ever reached an underwriter's desk?

Katerina
--- M2
Hi Michelle,

Smart Scales has approximately 3.5% mean absolute error under evaluated conditions and is not a scale reading. Any useful threshold would sit well above that error, and Aviva sets it.

FitXpress is not a medical device and does not make underwriting decisions.

I can walk through a design here: https://meetings.hubspot.com/katerina-galich

Katerina

@@@ tom-parkinson-03190190
hook: underwriter turned rules developer
proof: 2 photos; structured record; REST API and SDK
--- M1
Hi Tom,

Curious about your take, as someone who underwrote at Aviva and now codes its rules. A build rule is only as good as the input it reads.

FitXpress returns one timestamped, structured record per applicant. It holds a weight estimate from 2 photos, BMI from the declared height, and a flag if the gap crosses the threshold Aviva sets.

When a rule reads build today, which fields does it take, and where would one more fit?

Katerina
--- M2
Hi Tom,

The record arrives by REST API or SDK, with the threshold as a value Aviva owns and changes. A shadow run first shows how many cases a given value flags.

In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes SCCs.

Glad to show the record format: https://meetings.hubspot.com/katerina-galich

Katerina

@@@ sally-james-75186623
hook: senior development underwriting, where new evidence is tested
proof: 2 photos; threshold flag; evaluation counts flag agreement with separately collected evidence
--- M1
Hi Sally,

Made me think about development underwriting, where new evidence is tested before it reaches live cases at Aviva.

FitXpress takes 2 photos at the point of sale and estimates weight with Smart Scales. BMI follows from the declared height, and a flag fires only past a threshold Aviva sets. The record is timestamped and structured.

When you test a new rule, what usually decides that build evidence is good enough?

Katerina
--- M2
Hi Sally,

A first test can stay small: one set of cases and a few candidate thresholds, with a count of how often a flag agrees with build evidence collected separately. Outputs stay out of decisions throughout.

In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes SCCs.

Open to a conversation? https://meetings.hubspot.com/katerina-galich

Katerina

@@@ victoria-francis-09949480
hook: bio puts customer outcomes beside risk management
proof: 2 photos; under 45 seconds from the photos to structured results (scan returns the record)
--- M1
Hi Victoria,

Got me thinking: your bio puts customer outcomes next to risk management, the balance a new application step has to hit.

The record FitXpress sends to Aviva's systems comes from 2 photos: a Smart Scales weight estimate, BMI from the declared height, and a flag when the gap crosses a threshold Aviva sets.

Where in the application journey would a two-photo step sit best, with advisers or at the client's declaration?

Katerina
--- M2
Hi Victoria,

Completion decides whether a step stays, and an evaluation would measure it. The scan returns the record, under 45 seconds from the photos to structured results.

In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes SCCs.

Shall we find a time? https://meetings.hubspot.com/katerina-galich

Katerina

@@@ nicholas-john-austin
hook: Protection Commercial Director seat where terms, adviser feedback and cost meet
proof: 2 photos; threshold flag
--- M1
Hi Nick,

This stood out: Protection Commercial Director is the seat where terms, adviser feedback and cost meet.

FitXpress puts 2 photos into the application and records a Smart Scales weight estimate against the declared height, with a flag at a threshold Aviva sets. Aviva's underwriters decide what a flag changes.

Where do advisers tell you terms moved after application, and how often?

Katerina
--- M2
Hi Nick,

The commercial case sits in cases that get no screening and later see terms change. A shadow run on Aviva's own threshold would size that before anyone commits.

In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes SCCs.

My calendar is here: https://meetings.hubspot.com/katerina-galich

Katerina

@@@ rahannon
hook: transformation scope across UK Life, which takes in the protection application journey
proof: 2 photos; API and SDK
--- M1
Hi Rachel,

Spotted something in your title: transformation across UK Life, which takes in Aviva's protection application journey.

For that journey we built FitXpress: 2 photos, a weight estimate from Smart Scales, BMI from the declared height, and a flag once the gap passes a threshold Aviva sets. A timestamped record goes back to Aviva's systems.

How is a new step in the application tested with advisers before it joins a journey?

Katerina
--- M2
Hi Rachel,

A shadow pilot suits a change of this kind: advisers see the step while outputs stay out of decisions. It connects to the application by API or SDK.

In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes SCCs.

Time to talk it over? https://meetings.hubspot.com/katerina-galich

Katerina

@@@ liliburdass
hook: Head of Transformation, Protection, carrying change across the protection journey
proof: 2 photos; threshold flag
--- M1
Hi Lili,

Quick note on your role as Head of Transformation, Protection at Aviva: the application journey is where much of that change lands.

In the protection application, FitXpress takes 2 photos and estimates weight with Smart Scales. Aviva's threshold decides when a flag is raised, and one timestamped record comes back.

How is drop-off measured when a new step joins the protection application?

Katerina
--- M2
Hi Lili,

A pilot would give you a completion count before any rollout, from a sample offered the step with outputs kept out of decisions.

In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes SCCs.

Would a call suit? https://meetings.hubspot.com/katerina-galich

Katerina

@@@ daryl-warren-a773a64a
hook: from the actuarial coding hub into individual protection pricing
proof: 2 photos; threshold flag; evaluation counts flags and flag agreement with separately collected evidence
--- M1
Hi Daryl,

Quick one, given your move from the actuarial coding hub to individual protection pricing at Aviva. Build loadings depend on how well declared build is evidenced.

FitXpress has applicants take 2 photos in the application. Smart Scales estimates weight, BMI is calculated from the declared height, and a flag is raised at a threshold Aviva chooses. The timestamped record is returned to Aviva's systems.

How are build loadings and the cost of evidence weighed on point-of-sale cases?

Katerina
--- M2
Hi Daryl,

An evaluation gives you a count before anything is decided: how many cases a candidate threshold flags, and how often a flag agrees with separately collected build evidence.

In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes SCCs.

Easiest to discuss live: https://meetings.hubspot.com/katerina-galich

Katerina

@@@ marina-belezina-2451b0
hook: strategy and innovation remit across Aviva, with point-of-sale cases that carry no medical evidence
proof: 2 photos; threshold flag
--- M1
Hi Marina,

Wanted to reach out given your strategy and innovation remit across Aviva. One place it touches protection: point-of-sale cases where build is declared and no medical evidence is collected.

FitXpress is built for that gap. It takes 2 photos in the application and uses Smart Scales to estimate weight, flagging a difference from declared weight above Aviva's threshold. Aviva's rules decide what happens next.

Where would new evidence steps like this sit in your protection strategy?

Katerina
--- M2
Hi Marina,

I can show what the record looks like and how a shadow evaluation would run on Aviva's own threshold. If this belongs elsewhere, point me to whoever owns underwriting philosophy for protection.

FitXpress is not a medical device and does not make underwriting decisions.

https://meetings.hubspot.com/katerina-galich

More detail: https://3dlook.ai/for-insurance-underwriting/

Katerina

@@@ arslanhannani
hook: scaling innovative propositions across the group
proof: 2 photos; threshold flag
--- M1
Hi Arslan,

Quick reaction to your headline: innovation and new ventures at Aviva. A practical test case sits in protection, at the point of sale with no medical evidence.

We built FitXpress for it: 2 photos, a Smart Scales estimate of weight, BMI from the declared height, and a flag above the threshold Aviva sets. The output is one timestamped record in Aviva's systems.

How does a new capability get from the innovation team into a protection journey?

Katerina
--- M2
Hi Arslan,

Worth a short call on what the record contains and why an evaluation precedes any live use. If someone else runs the protection new-business journey, a pointer to them would do.

FitXpress is not a medical device and does not make underwriting decisions.

https://meetings.hubspot.com/katerina-galich

Katerina

@@@ manjudevinatarajan
hook: digital product management background applied to group digital portfolio
proof: 2 photos; threshold flag; timestamped structured record; REST API
--- M1
Hi Manju,

Quick thought from your digital product background: a portfolio decision often comes down to which application steps are worth changing at Aviva.

For protection, FitXpress takes 2 photos in the application. A flag appears when the Smart Scales weight estimate differs from the declared figure by more than Aviva's threshold, and each applicant gets one timestamped, structured record.

Which changes to protection applications sit in your digital portfolio at the moment?

Katerina
--- M2
Hi Manju,

Technically it is a REST API call and a capture step, with the threshold held by the insurer. I can take you through it live, or you could point me to whoever owns the adviser application experience.

FitXpress is not a medical device and does not make underwriting decisions.

https://meetings.hubspot.com/katerina-galich

Katerina

@@@ joel-manstoff
hook: transformation described as a mindset in his bio
proof: 2 photos; threshold flag
--- M1
Hi Joel,

Couldn't help but ask after reading that you treat transformation as a mindset. Protection at Aviva has a concrete case: point-of-sale applications where build is only declared.

FitXpress takes 2 photos and returns a Smart Scales weight estimate with a threshold flag set by Aviva, all on a timestamped record.

How would you sequence a small evidence step like this against other change in protection?

Katerina
--- M2
Hi Joel,

The scope can stay small: a shadow run on one set of cases, with outputs kept out of decisions. A call would show what it asks of a team. Whoever owns the protection change roadmap might be the better first conversation.

FitXpress is not a medical device and does not make underwriting decisions.

https://meetings.hubspot.com/katerina-galich

Katerina

@@@ amanhayer
hook: headline on efficiency and effectiveness of transformation and operations
proof: 2 photos; threshold flag
--- M1
Hi Aman,

Caught my eye: your headline on the efficiency and effectiveness of operations. In Aviva protection, referrals to an underwriter are one place that shows.

FitXpress asks for 2 photos and returns a Smart Scales weight estimate with BMI from the declared height. Only a gap beyond Aviva's threshold produces a flag, on a timestamped record.

Which measures does the transformation team use to judge whether a referral step earns its place?

Katerina
--- M2
Hi Aman,

An evaluation would count how many cases a candidate threshold flags, which gives a measure to judge the step against. If that sits with someone else, whoever leads protection underwriting day to day is the person to ask.

FitXpress is not a medical device and does not make underwriting decisions.

https://meetings.hubspot.com/katerina-galich

Katerina

@@@ hannah-spiro-27b12b106
hook: Head of Innovation Engagement taking in outside capabilities, earlier innovation work at a health insurer
proof: 2 photos; threshold flag; boundary sentence; landing link
--- M1
Hi Hannah,

Quick idea for you on protection applications at Aviva, where build is declared and no medical evidence follows.

FitXpress covers those with 2 photos and a Smart Scales weight estimate, with a flag where the estimate differs from declared weight by more than Aviva's threshold. The timestamped record returns to Aviva's systems.

When an outside capability reaches you, what does it need to show before it goes to a protection team?

Katerina
--- M2
Hi Hannah,

The part a protection team can judge quickly is the evaluation design, run on Aviva's threshold with outputs kept out of decisions. I can walk through it on a call, or you could point me to whoever in protection underwriting would assess new evidence.

FitXpress is not a medical device and does not make underwriting decisions.

https://meetings.hubspot.com/katerina-galich

The landing page has the rest: https://3dlook.ai/for-insurance-underwriting/

Katerina

@@@ paul-welsh-a27b7a61
hook: lab and venture path into group innovation, with a product and proposition past
proof: 2 photos; threshold flag
--- M1
Hi Paul,

Your path through product, proposition and venture work into group innovation at Aviva is a useful lens on this.

One candidate is FitXpress: 2 photos in a protection application, Smart Scales for the weight estimate, BMI from the declared height, and a flag at Aviva's own threshold. The result is a single structured, timestamped record.

What turns an idea from the innovation lab into a test inside protection?

Katerina
--- M2
Hi Paul,

If the idea fits, the first test is a shadow evaluation with outputs kept out of decisions. I would be glad to take you through the record on a call. If protection propositions sit with someone else, a name would be welcome.

FitXpress is not a medical device and does not make underwriting decisions.

https://meetings.hubspot.com/katerina-galich

Katerina

@@@ harriet-granville-jones-innovation
hook: start-up scouting for Aviva Group Innovation
proof: 2 photos; threshold flag
--- M1
Hi Harriet,

You scout start-ups for Aviva Group Innovation. This one is narrow: protection point-of-sale cases where build is declared.

FitXpress takes 2 photos in the application and gives a Smart Scales weight estimate. A gap from declared weight over a threshold Aviva sets is flagged on a timestamped record.

What does a start-up in insurance evidence have to show before you take it to a business unit?

Katerina
--- M2
Hi Harriet,

The test I would propose runs in shadow on Aviva's threshold, with outputs kept out of decisions until the counts are in. A call would show it. The underwriter who would sit on that evaluation may be the better contact.

FitXpress is not a medical device and does not make underwriting decisions.

https://meetings.hubspot.com/katerina-galich

Katerina

@@@ suzanne-lawson-2368623
hook: Group Innovation partnerships role with earlier work alongside UK Life and Savings leadership
proof: 2 photos; threshold flag
--- M1
Hi Suzanne,

Your time alongside Aviva's UK Life and Savings leadership, now in Group Innovation partnerships, gives you a view of how protection ideas get picked up.

The idea is FitXpress: 2 photos in a protection application and a Smart Scales weight estimate, with a flag only when the gap passes a threshold Aviva sets. Aviva's systems receive one timestamped record.

When an idea touches the application, who in protection usually sponsors a first test?

Katerina
--- M2
Hi Suzanne,

A first test would be modest: a shadow run, Aviva's threshold, no effect on any case. I would welcome a call on it, or the name of the sponsor you had in mind for a protection pilot.

FitXpress is not a medical device and does not make underwriting decisions.

https://meetings.hubspot.com/katerina-galich

Katerina

@@@ steve-lister-87b0671
hook: bio on interactions between components, people and technology, developer start
proof: 2 photos via SDK; REST API and SDKs; photo retention wording; GDPR line
--- M1
Hi Steve,

Noticed overlap with your bio: how components, people and technology interact. A capture step in an application is one more component in Aviva's protection journey.

FitXpress is an SDK step capturing 2 photos. Back comes one timestamped record with a Smart Scales weight estimate, BMI from the declared height, and a flag above a threshold Aviva sets.

Who reviews a new capture component before it goes into Aviva's protection application journey?

Katerina
--- M2
Hi Steve,

REST API and SDKs, with photos deleted after processing or within 30 days per the insurer's policy, retained photos blurred and faces obscured at capture. Security documents go through legal@3dlook.me.

In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes SCCs.

Walk-through? https://meetings.hubspot.com/katerina-galich

Katerina

@@@ jon-oneal
hook: Head of IT Aviva Protection UK, long career in regulated environments
proof: 2 photos; threshold flag; REST API and SDKs; random scan identifiers; privacy FAQ; GDPR line
--- M1
Hi Jon,

Thought I'd share something relevant to Head of IT for Aviva Protection UK, given your years in regulated insurance environments.

FitXpress is a capture step with 2 photos. The returned record carries a Smart Scales weight estimate, BMI from the declared height and a threshold flag that Aviva configures.

Which formats does Aviva's underwriting workbench accept for evidence from outside systems?

Katerina
--- M2
Hi Jon,

Integration is a REST API and SDKs, and scan records sit on random identifiers. The data handling answers are in the privacy FAQ: https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/

In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes SCCs.

A technical call: https://meetings.hubspot.com/katerina-galich

Katerina
