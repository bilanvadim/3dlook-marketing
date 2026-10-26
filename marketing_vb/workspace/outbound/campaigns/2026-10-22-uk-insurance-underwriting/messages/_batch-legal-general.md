@@@ david-banks-9b750391
hook: move up to run underwriting at Legal & General; January rework of life and CI application questions aimed at fewer manual referrals
proof: 2 photos, Smart Scales (M1); GDPR line (M2)
--- M1
Hi David,

Noticed your move up to run underwriting at Legal & General. The January rework of the life and CI application questions aimed at fewer manual referrals, which made me think of cases decided with no nurse screening.

FitXpress flags only the gap between declared weight and a Smart Scales estimate, from 2 photos in the application, at a threshold Legal & General sets.

How is build checked on those cases today?

Katerina
--- M2
Hi David,

A shadow evaluation would count how many cases each candidate threshold flags and how often a flag agrees with build evidence collected separately, with outputs kept out of decisions.

In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes SCCs.

Would a call to design that be useful? https://meetings.hubspot.com/katerina-galich

Katerina
@@@ drtarungupta
hook: GP and NICE reference panel background, now Chief Medical Officer
proof: 2 photos, Smart Scales (M1); 3.5% sentence with not a scale reading, boundary sentence (M2)
--- M1
Hi Tarun,

Noticed your years as a GP and on NICE's reference panel, now as Chief Medical Officer at Legal & General. A question about what an estimated value may be used for.

FitXpress returns a Smart Scales weight estimate from 2 photos in the application, and a flag appears only above a threshold the insurer sets. The rules stay with Legal & General.

Before a weight estimate goes into referral rules, which questions would you want answered first?

Katerina
--- M2
Hi Tarun,

Smart Scales has approximately 3.5% mean absolute error under evaluated conditions, not a scale reading. Any flag should sit well beyond that figure, and Legal & General would choose where the line falls. FitXpress is not a medical device and does not make underwriting decisions.

Happy to walk through it: https://meetings.hubspot.com/katerina-galich

Katerina
@@@ pippa-barber-nee-keefe-487b64b6
hook: remit across Retail Protection and Retail Annuities; journey placement after the January question rework
proof: 2 photos, Smart Scales (M1); GDPR line (M2)
--- M1
Hi Pippa,

Quick thought, given your remit across Retail Protection and Retail Annuities. After Legal & General's January rework of the life and CI application questions, any new step has to earn its place in the journey.

FitXpress would sit in the application: the applicant takes 2 photos, and it returns a Smart Scales estimate and one timestamped record, with a flag above the insurer's threshold.

How do you judge whether a new application step is worth keeping?

Katerina
--- M2
Hi Pippa,

Completion of the photo step would be measured in the evaluation, showing drop-off before anything goes live.

In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes SCCs.

I can walk through the design: https://meetings.hubspot.com/katerina-galich

More on the step:
https://3dlook.ai/for-insurance-underwriting/

Katerina
@@@ nicki-plews-b037aa2b
hook: path from protection strategy to head of product and proposition; February plainer adviser policy documents
proof: 2 photos, Smart Scales (M1); GDPR line (M2)
--- M1
Hi Nicki,

Got me thinking about your path from protection strategy to leading product and proposition at Legal & General. February's plainer policy documents for advisers suggest the adviser experience is a live priority.

FitXpress is a step inside the application: 2 photos feed a Smart Scales estimate, and a flag goes to the insurer only above its own threshold.

How would you test a new step with advisers before it reached a live journey?

Katerina
--- M2
Hi Nicki,

Adviser testing would use the evaluation: completion of the photo step and how many cases a threshold would flag, with the record going to the insurer's systems only.

In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes SCCs.

Would a short call to plan an adviser test make sense? https://meetings.hubspot.com/katerina-galich

Katerina
@@@ sara-denyer-b81a2a92
hook: life and disability underwriter turned business analyst for the underwriting rules
proof: 2 photos, Smart Scales (M1); boundary sentence (M2)
--- M1
Hi Sara,

Spotted something in your background: life and disability underwriter first, now the business analyst for Legal & General's underwriting rules. You know the rule and the case it changes.

FitXpress would give the rules one more input: a flag at the insurer's threshold on the gap between declared weight and a Smart Scales estimate from 2 photos.

When you test a change to the rules, which past cases would you run it against?

Katerina
--- M2
Hi Sara,

Those past cases are where a build flag would be counted: how many each candidate threshold would flag, and how often a flag agrees with build evidence collected separately. FitXpress is not a medical device and does not make underwriting decisions.

Is a call to scope that worthwhile? https://meetings.hubspot.com/katerina-galich

Landing page for reference:
https://3dlook.ai/for-insurance-underwriting/

Katerina
@@@ jenni-phillips-98892a24
hook: COVER Woman of the Year in underwriting 2026, development underwriter
proof: 2 photos, Smart Scales (M1); GDPR line (M2)
--- M1
Hi Jenni,

Wanted to reach out and congratulate you on Woman of the Year - Underwriting 2026 at the COVER awards. Development work at Legal & General sits close to the January changes in the life and CI application questions.

FitXpress would be a new source of build evidence for that work: 2 photos in the application give a Smart Scales estimate, flagged against a threshold the company sets.

As a development underwriter, which checks would FitXpress need to pass with you before it touched live cases?

Katerina
--- M2
Hi Jenni,

Keeping every output away from live cases is the point of a shadow evaluation: your team compares flags with the build evidence it already holds.

In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes SCCs.

I can sketch the design on a call: https://meetings.hubspot.com/katerina-galich

Katerina
@@@ john-redmond-884597a
hook: path from life and disability underwriter through training to development
proof: 2 photos, Smart Scales (M1); boundary sentence (M2)
--- M1
Hi John,

Noticed overlap with your path: underwriter, then training, now development at Legal & General. You see what happens when an application rule changes.

A build flag would be one such change, raised by FitXpress when a Smart Scales estimate from 2 photos sits far from declared weight, at a threshold the company sets.

When a rule change reaches your team, how do you test it before underwriters rely on it?

Katerina
--- M2
Hi John,

Underwriters would see the flag and the timestamped record on the case file, with Legal & General setting the threshold. A dry run on a sample of applications would show your team the effect before any live case. FitXpress is not a medical device and does not make underwriting decisions.

Open to a call on how your team would test it? https://meetings.hubspot.com/katerina-galich

Katerina
@@@ hai-luc-67306367
hook: move from pricing actuary to head of actuarial research for Retail Protection
proof: 2 photos, Smart Scales (M1); boundary sentence (M2)
--- M1
Hi Hai,

Quick note on your move from pricing to leading actuarial research for Retail Protection at Legal & General. The evidence on how build moves price sits with your team.

With FitXpress, each application carries one timestamped record: a Smart Scales estimate from 2 photos, BMI from the declared height and a flag at the insurer's threshold.

How do you weigh the cost of extra build evidence against the loadings it might change?

Katerina
--- M2
Hi Hai,

For research the record is the useful part: it is structured and timestamped, allowing declared and estimated build to be compared across applications. FitXpress is not a medical device and does not make underwriting decisions.

Would a call help to scope it? https://meetings.hubspot.com/katerina-galich

Details here:
https://3dlook.ai/for-insurance-underwriting/

Katerina
@@@ spiterimichael
hook: focus on applying AI and machine learning; SDK step in the application
proof: 2 photos, Smart Scales (M1); REST API and SDKs, GDPR line (M2), privacy FAQ link (M2)
--- M1
Hi Michael,

Curious about your take, given your focus on applying AI and machine learning at Legal & General. FitXpress is a smaller piece: an SDK step in the application.

The SDK captures 2 photos and returns one timestamped record to the insurer's systems, with a Smart Scales weight estimate and a flag above the insurer's threshold.

Who signs off a new vendor in the application path, and what do they ask for?

Katerina
--- M2
Hi Michael,

Integration is through a REST API and SDKs. In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes SCCs. Data handling is set out here:
https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/

Worth a call with your architects? https://meetings.hubspot.com/katerina-galich

Katerina
@@@ tariq-surty-8911101
hook: CTO of Retail, owner of the systems a new application step would plug into
proof: 2 photos, Smart Scales (M1); REST API and SDKs, photo retention and random identifiers, GDPR line (M2)
--- M1
Hi Tariq,

Noticed your CTO role for Retail at Legal & General, which owns the systems a new application step would plug into.

FitXpress is an SDK step: the applicant's 2 photos go in, and one timestamped record with a Smart Scales estimate and a threshold flag comes back to the insurer's systems.

Where would a capture step like this connect to your e-application: the front end, or a service behind it?

Katerina
--- M2
Hi Tariq,

For the review pack: REST API and SDKs, photos deleted after processing or within 30 days per the insurer's policy, scan records on random identifiers. In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes SCCs. Documents come through legal@3dlook.me.

Shall we go through it on a call? https://meetings.hubspot.com/katerina-galich

Katerina
@@@ jennyreeve
hook: Group transformation seat; record on point-of-sale protection cases
proof: 2 photos, Smart Scales (M1); boundary sentence (M2)
--- M1
Hi Jenny,

Quick idea from your Group transformation seat at Legal & General. The record from FitXpress sits on the case file: timestamped, structured, built from 2 photos and a Smart Scales estimate, with a flag only above the threshold the insurer sets.

It matters for point-of-sale protection cases decided without medical evidence. When a new step like that is proposed, how does it get through Group governance?

Katerina
--- M2
Hi Jenny,

I would like to show the record and the evaluation path, which counts flags per threshold before anything touches a live case. FitXpress is not a medical device and does not make underwriting decisions. If underwriting philosophy belongs to someone else, point me to whoever owns it.

A short call: https://meetings.hubspot.com/katerina-galich

Katerina
@@@ gary-m-3b7b913b
hook: Transformation Director for Retail, the division writing individual protection
proof: 2 photos, Smart Scales (M1); boundary sentence (M2)
--- M1
Hi Gary,

Caught my eye: Transformation Director for Retail at Legal & General, the division writing individual protection. FitXpress adds a step to that application: 2 photos give a Smart Scales weight estimate, and the insurer's threshold decides whether a flag is raised.

Which parts of the Retail protection journey are open to change this year?

Katerina
--- M2
Hi Gary,

A call would show where the step could sit in the Retail journey. FitXpress is not a medical device and does not make underwriting decisions. If the new-business journey belongs to someone else, a name is all I need.

https://meetings.hubspot.com/katerina-galich

The step in more detail:
https://3dlook.ai/for-insurance-underwriting/

Katerina
@@@ sdavis2
hook: Group Director of Transformation with a digital proposition background
proof: 2 photos, Smart Scales (M1); boundary sentence (M2)
--- M1
Hi Steve,

This stood out: a Group Director of Transformation with a background in digital proposition development, now at Legal & General. FitXpress would sit inside the protection application: 2 photos and a Smart Scales estimate, with the insurer's threshold deciding when a flag is raised.

Legal & General's rules and underwriters decide what happens next. When the protection application changes, who sets the evidence a new step must carry?

Katerina
--- M2
Hi Steve,

A walk-through would cover the record and the shadow evaluation design, which keeps outputs away from live cases. FitXpress is not a medical device and does not make underwriting decisions. If a colleague owns the build rules in protection underwriting, I would gladly be pointed their way.

Calendar: https://meetings.hubspot.com/katerina-galich

Katerina
@@@ crissaunders
hook: leads groupwide digital products; protection application is one of those journeys
proof: 2 photos, Smart Scales (M1); boundary sentence (M2)
--- M1
Hi Cris,

Made me think: you lead digital products across Legal & General, and the protection application is one of those journeys. FitXpress is a camera step in it: the applicant takes 2 photos, and a Smart Scales estimate is flagged only above a threshold the insurer sets, with one timestamped record returned.

Where in a digital protection journey would you test a step like that first?

Katerina
--- M2
Hi Cris,

I can show the step as an applicant would meet it, and the record the insurer receives. FitXpress is not a medical device and does not make underwriting decisions. If the adviser-facing application sits with another team, a pointer to its owner works just as well.

Slot here: https://meetings.hubspot.com/katerina-galich

Katerina
@@@ brian-kemp-0467b898
hook: customer underwriter to desk manager in Edinburgh, the desk taking applicants' disclosures
proof: 2 photos, Smart Scales (M1); GDPR line (M2)
--- M1
Hi Brian,

Noticed your path from customer underwriter to team manager in Edinburgh, on the desk at Legal & General that takes disclosures from applicants.

In the application the applicant takes 2 photos, and FitXpress returns a Smart Scales estimate. Above the insurer's threshold a flag appears on the case for your underwriters.

When a phone conversation gives a build near a band edge, what does your team do next?

Katerina
--- M2
Hi Brian,

Underwriters on your desk would see the flag beside what they already ask on the call, and each case would keep its own timestamped record.

In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes SCCs.

Open to a call? https://meetings.hubspot.com/katerina-galich

Landing page:
https://3dlook.ai/for-insurance-underwriting/

Katerina
@@@ scott-wallace-b608b49b
hook: move from operations management into running an underwriting team
proof: 2 photos, Smart Scales (M1); GDPR line (M2)
--- M1
Hi Scott,

Quick reaction to your move from operations management into running an underwriting team at Legal & General. You see the referral workload first-hand.

On each application, FitXpress takes 2 photos and a Smart Scales weight estimate, flagging only gaps to declared weight above a threshold the insurer sets.

How do manual referrals on build reach your team today?

Katerina
--- M2
Hi Scott,

The evaluation counts how many referrals each candidate threshold would create before anything goes live, giving your team the workload in advance.

In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes SCCs.

Worth a call? https://meetings.hubspot.com/katerina-galich

Katerina
@@@ nicky-mcrae-a4a3b5206
hook: move from administration management into leading an underwriting team
proof: 2 photos, Smart Scales (M1); boundary sentence (M2)
--- M1
Hi Nicky,

Had a thought about your move from administration management into leading an underwriting team at Legal & General.

Each application would carry a timestamped FitXpress record: 2 photos, a Smart Scales estimate and a flag only above the insurer's threshold.

What would make a flag useful to your team when a case reaches the desk?

Katerina
--- M2
Hi Nicky,

The record sits on the case file, with declared and estimated build shown together against the threshold used. FitXpress is not a medical device and does not make underwriting decisions.

A short call would show what a record looks like. https://meetings.hubspot.com/katerina-galich

Katerina
@@@ bethan-shepherd-12a39763
hook: pre-sale and senior medical underwriting background before managing the team
proof: 2 photos, Smart Scales (M1); GDPR line (M2)
--- M1
Hi Bethan,

Couldn't help but notice the pre-sale and senior medical underwriting in your background before managing the team at Legal & General.

FitXpress works on cases with no medical screening: 2 photos in the application give a Smart Scales estimate, flagged above a threshold Legal & General sets.

When a case arrives with declared weight and nothing measured, what do your underwriters lean on?

Katerina
--- M2
Hi Bethan,

The scan sits beside what your team already reviews and replaces none of it. A flag refers only gaps above the threshold.

In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes SCCs.

Could we talk it through? https://meetings.hubspot.com/katerina-galich

Further reading:
https://3dlook.ai/for-insurance-underwriting/

Katerina
@@@ andrew-greatbanks-9712b03b
hook: former head of customer underwriting, now service delivery; owns the operation receiving flagged cases
proof: 2 photos, Smart Scales (M1); GDPR line (M2)
--- M1
Hi Andrew,

Quick one, given you ran underwriting at Legal & General and now run its service delivery: your operation would receive any flagged case.

FitXpress flags a gap between declared and estimated weight when it crosses a threshold the insurer sets, from 2 photos in the application and a Smart Scales weight estimate.

If a flag added referrals, what would you need to see first to plan for it?

Katerina
--- M2
Hi Andrew,

The evaluation answers with counts: how many cases each candidate threshold would flag, before any flag reaches a live case.

In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes SCCs.

A call could set out the numbers: https://meetings.hubspot.com/katerina-galich

Katerina
