@@@ matthew-wilton-49408544
hook: contract underwriting across several life assurance providers, now development underwriting at Legal & General
proof: 2 photos, Smart Scales estimate, threshold flag (card)
--- M1
Hi Matthew,

Contract underwriting for several life assurance providers means you have seen build handled in more than one rulebook. Now that you work on development at Legal & General, one more input may be worth a look.

FitXpress takes 2 photos in the application, and a flag is raised when a Smart Scales estimate differs from declared weight by more than Legal & General's own threshold.

When declared weight sits near a band edge, how much would a second source change what you do?

Katerina
--- M2
Hi Matthew,

Run prospectively on incoming applications, the evaluation would show how many cases each candidate threshold flags and how well those flags line up with build evidence gathered another way. Outputs stay out of decisions. In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes SCCs.

I can talk through the design on a call: https://meetings.hubspot.com/katerina-galich

Katerina
@@@ richard-whaley-2a4459132
hook: senior medical underwriter at Legal & General before development underwriting
proof: 3.5% mean absolute error under evaluated conditions (card Rules numbers, underwriting lane M2)
--- M1
Hi Richard,

You moved from senior medical underwriting into development. You know which cases arrive with little more than declared build.

FitXpress asks the applicant for 2 photos and puts a flag on the case when a Smart Scales estimate sits far from declared weight, past a threshold Legal & General sets.

On which declared builds would a second source have helped most when you were reading medical cases?

Katerina
--- M2
Hi Richard,

Under evaluated conditions, the Smart Scales estimate has approximately 3.5% mean absolute error and is not a scale reading. That is why a flag belongs well above it, at a line Legal & General sets. FitXpress is not a medical device and does not make underwriting decisions.

Shall we have a call to show the record a flag would carry? https://meetings.hubspot.com/katerina-galich

Katerina
@@@ donna-cowell-insurance
hook: runs reinsurance for Legal & General protection
proof: 2 photos, Smart Scales estimate, threshold flag (card)
--- M1
Hi Donna,

Your remit covers the treaties behind Legal & General's protection book, where a change in evidence meets a reinsurer's view as well as an underwriter's.

FitXpress would add one timestamped record to the application: a Smart Scales weight estimate from 2 photos, with a flag when its gap to declared weight crosses the threshold Legal & General sets.

When a new evidence source is proposed, how does it reach the reinsurance conversation?

Katerina
--- M2
Hi Donna,

Nothing in the underwriting decision moves: a flag refers a case to an underwriter, who decides as before, and the record shows the threshold applied. In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes SCCs.

Could we find time for a call on what the reinsurance side would want to see? https://meetings.hubspot.com/katerina-galich

Katerina
@@@ markmbird
hook: Chief Data Officer with an enterprise-wide data and AI strategy and control remit
proof: SDK, 2 photos, structured record, privacy FAQ (card)
--- M1
Hi Mark,

Data strategy and control across Legal & General sit in your remit.

FitXpress puts an SDK step in the application, which takes 2 photos. A flag is raised when the gap between declared weight and a Smart Scales estimate crosses the insurer's threshold, and one structured, timestamped record comes back.

Which data domain would you expect a record like that to belong to?

Katerina
--- M2
Hi Mark,

One record per applicant comes back through a REST API on a random identifier, with declared weight, the estimate, the threshold applied and a timestamp. FitXpress is not a medical device and does not make underwriting decisions.

Data handling is set out here:
https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/

Would a call on the field layout help? https://meetings.hubspot.com/katerina-galich

Katerina
@@@ 74lancater
hook: Head of Clinical Operations, cases with and without medical evidence
proof: 2 photos, Smart Scales estimate, threshold flag (card)
--- M1
Hi Wayne,

Clinical operations at Legal & General sits close to the cases where medical evidence is gathered, and to the ones where none is. For those decided at the point of sale, FitXpress takes 2 photos, and a flag is raised on the gap between declared weight and a Smart Scales estimate only above the insurer's threshold.

Which cases reach clinical operations with the least build information today?

Katerina
--- M2
Hi Wayne,

Cases with declared weight alone are where a timestamped record would sit on file first, giving declared and estimated weight in one place. FitXpress is not a medical device and does not make underwriting decisions. If medical underwriting sits elsewhere, a pointer to whoever leads it would help.

A call would allow me to show you the record itself: https://meetings.hubspot.com/katerina-galich

Katerina
@@@ james-jarman-3249891
hook: Chief Data and Analytics Officer for Legal & General Retail
proof: structured timestamped record, 2 photos, REST API, GDPR line (card)
--- M1
Hi James,

Your data and analytics remit covers Legal & General Retail, where protection applications generate records your team ends up holding. FitXpress returns a structured, timestamped record from 2 photos, with a flag when a Smart Scales estimate and declared weight differ by more than the insurer's threshold.

How do records from a new application step usually enter Retail's data estate today?

Katerina
--- M2
Hi James,

Fields can be mapped before anything reaches Retail's data estate: the record arrives through a REST API on a random identifier. In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes SCCs. FitXpress is not a medical device and does not make underwriting decisions.

I can go through the field list with your team on a call: https://meetings.hubspot.com/katerina-galich

Katerina
@@@ simonsheldonconsulting
hook: executive record in (re)insurance business transformation, IT-enabled change
proof: 2 photos, threshold flag, SDK (card)
--- M1
Hi Simon,

Large IT-enabled change in life and reinsurance gives you a view on which small steps survive a transformation portfolio. At Legal & General, one candidate sits at the point of sale: 2 photos from the applicant give a Smart Scales weight estimate. A flag follows where the gap to declared weight crosses the insurer's threshold.

What decides whether a step that size earns a slot in a change programme?

Katerina
--- M2
Hi Simon,

The case for a slot rests on footprint: one SDK integration in the application, with the current route kept for anyone who cannot or does not scan. If the protection application sits under a head of distribution, a name would help.

I would welcome a conversation to show the step: https://meetings.hubspot.com/katerina-galich

Katerina
@@@ david-stewart-080a6435
hook: Head of Group Data Science, how an outside data source is evaluated
proof: 2 photos, REST API (card)
--- M1
Hi David,

Group data science at Legal & General is where an outside data source gets its first hard look. FitXpress would supply one: from 2 photos comes a Smart Scales weight estimate, with a flag raised when its gap to declared weight crosses the insurer's threshold.

How does your team evaluate a new source before a model or rule depends on it?

Katerina
--- M2
Hi David,

Your team could judge the source on its own data: the record comes through a REST API with declared weight, the estimate and the threshold applied. FitXpress is not a medical device and does not make underwriting decisions.

I can set up a technical call on that: https://meetings.hubspot.com/katerina-galich

Katerina
@@@ judit-f-29664635
hook: Head of IT, IS and Data Risk for Legal & General Retail
proof: SDK, 2 photos, photo retention and random ids, GDPR line (card)
--- M1
Hi Judit,

Your remit spans IT, information security and data risk for Legal & General Retail. FitXpress would sit in the application as an SDK: 2 photos go to a Smart Scales estimate, and a timestamped record returns with a flag where the gap to declared weight crosses the insurer's threshold.

What would you look at first in a processor that handles photos and scan records?

Katerina
--- M2
Hi Judit,

The handling points are short. Photos are deleted after processing or within 30 days under the insurer's policy, and any retained photo is blurred with faces obscured at capture. Scan records sit on random identifiers. In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes SCCs.

I am happy to go through them on a call: https://meetings.hubspot.com/katerina-galich

Katerina
@@@ emese-simoradik-msc-asa-cera
hook: life actuarial record before product director
proof: 2 photos, threshold flag, GDPR line (card)
--- M1
Hi Emese,

A product director with an actuary's training reads a new application step as both a journey change and a pricing input. For Legal & General, FitXpress would add 2 photos to the application. A Smart Scales weight estimate comes back as one timestamped record, and a flag is raised only when its gap to declared weight crosses the insurer's threshold.

Would you place a step like that in the adviser-keyed application or in the client's own declaration step?

Katerina
--- M2
Hi Emese,

The same SDK serves either placement, and the application keeps the insurer's current route for anyone who does not scan. In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes SCCs.

Details on the step:
https://3dlook.ai/for-insurance-underwriting/

Would a conversation about placement be useful? https://meetings.hubspot.com/katerina-galich

Katerina
@@@ prakash-rautaray-a9b32219
hook: IT and Transformation Director for Retail Protection and Mortgage Services
proof: 2 photos, timestamped record, SDK (card)
--- M1
Hi Prakash,

Change for Retail Protection and Mortgage Services passes through your desk, including the protection application. FitXpress would be one small addition there: the applicant takes 2 photos, and a timestamped record with a Smart Scales weight estimate returns to Legal & General's systems. A flag appears only when the estimate and declared weight differ by more than the insurer's threshold.

How often can the protection application take a new step, and what sets that rhythm?

Katerina
--- M2
Hi Prakash,

Release rhythm decides when it could go in, and the step itself is a single SDK addition for web and mobile. If application priorities are set by the owner of the adviser portal, a name would help.

A call could trace where it connects: https://meetings.hubspot.com/katerina-galich

Katerina
@@@ cheryl-hinton-86598b1a
hook: Chief Technology Officer for innovation at Legal & General
proof: 2 photos, timestamped record, threshold flag (card)
--- M1
Hi Cheryl,

Innovation technology at Legal & General tests ideas before a business line takes them on. One worth a look for protection is FitXpress, which takes 2 photos in the application and returns one timestamped record, with a flag raised only when a Smart Scales estimate and declared weight differ by more than the threshold the insurer sets.

What does an idea need to show before you would hand it to a business line?

Katerina
--- M2
Hi Cheryl,

What a business line would want to see is the effect on its own cases, before anything reaches a decision. If a protection sponsor is the better first contact, a name would help.

Could we have a call to give you the shape of it? https://meetings.hubspot.com/katerina-galich

Katerina
@@@ martin-todd-755a0420
hook: Head of Strategy for Legal & General Retail, speed against evidence at the point of sale
proof: 2 photos, threshold flag (card)
--- M1
Hi Martin,

Strategy for Legal & General Retail involves a trade-off at the point of sale. Cases decided without medical evidence move fast, and build rests on what the applicant declares. FitXpress adds a second source of build evidence, with a flag appearing where a Smart Scales estimate from 2 photos crosses the insurer's threshold against declared weight.

How does Retail's strategy weigh faster decisions against extra evidence in the application?

Katerina
--- M2
Hi Martin,

Retail could test it on one journey first, with the insurer's current route kept for anyone who does not scan. If a product director owns the protection proposition roadmap, their name would help.

Would a conversation about a first test journey be useful? https://meetings.hubspot.com/katerina-galich

Katerina
@@@ james-mcmillan-b2795b59
hook: Head of Group Strategy, group view of point-of-sale decisions
proof: 2 photos, timestamped record (card)
--- M1
Hi James,

A group view of protection starts with how cases are decided at the point of sale. From 2 photos, FitXpress adds a Smart Scales weight estimate and a timestamped record to that application, with a flag only when the gap to declared weight crosses the insurer's threshold.

Which criteria does Group Strategy use to pick the small bets worth testing inside a business line at Legal & General?

Katerina
--- M2
Hi James,

FitXpress would add a timestamped record only to cases that carry declared build alone. FitXpress is not a medical device and does not make underwriting decisions. The insurer's own rules and underwriters decide what a flag means. If Retail's head of protection is the better contact, a name would be enough.

I would welcome a short conversation on where a test could sit: https://meetings.hubspot.com/katerina-galich

Katerina
@@@ steven-morrison-90425586
hook: Head of Product Management, the application as adviser and client meet it (title only)
proof: 2 photos, threshold flag, GDPR line (card)
--- M1
Hi Steven,

Product management at Legal & General sees the application as the adviser and client meet it. FitXpress would add a step there, taking 2 photos and returning a Smart Scales weight estimate, with a flag raised only when the gap to declared weight crosses the insurer's threshold.

How does your team find out how a new application step lands with advisers once it is live?

Katerina
--- M2
Hi Steven,

The applicant sees a short photo step in the application, taken on their own phone. In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes SCCs.

A short overview sits here:
https://3dlook.ai/for-insurance-underwriting/

Shall we talk it through on a call? https://meetings.hubspot.com/katerina-galich

Katerina
@@@ andy-bergin-389278109
hook: Head of Product and Delivery, effort to add one SDK step (title only)
proof: SDK, 2 photos, REST API (card)
--- M1
Hi Andy,

Product and delivery meet when a new step has to be scheduled into an application. FitXpress is an SDK step that takes 2 photos and returns a timestamped record: a Smart Scales estimate, with a flag when its gap to declared weight crosses the insurer's threshold.

What does the delivery side need before it can schedule a new step in a protection application at Legal & General?

Katerina
--- M2
Hi Andy,

The SDK covers web and mobile with a REST API behind it, and applicants who cannot or do not scan continue on the insurer's current route. In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes SCCs.

I can talk through the integration points on a call: https://meetings.hubspot.com/katerina-galich

Katerina
@@@ kannansundarraj
hook: leads the Retail Protection portfolio at Legal & General Retail
proof: SDK, 2 photos, timestamped record (card)
--- M1
Hi Kannan,

You lead the Retail Protection portfolio at Legal & General Retail, which is where a new application step lands first. FitXpress adds one: an SDK takes 2 photos in the application, and a flag is raised on the gap between declared weight and a Smart Scales estimate when it crosses the insurer's threshold.

Which parts of the portfolio's roadmap would a new application step have to compete with?

Katerina
--- M2
Hi Kannan,

Nothing in the current application is replaced, and the step can be switched on for one journey before wider use. If the underwriting workbench has its own delivery owner, a name would help.

I would welcome a call to look at the integration with you: https://meetings.hubspot.com/katerina-galich

Katerina
@@@ jonathan-saggers-4ab31918
hook: ran the Protect journey at HSBC, now product and commercial risk
proof: 2 photos, threshold flag (card)
--- M1
Hi Jonathan,

You have run a protection journey from the distribution side at HSBC and now hold product and commercial risk at Legal & General. FitXpress would add a record to that journey, built by Smart Scales from 2 photos, with a flag where the gap to declared weight crosses the insurer's threshold.

Where does a commercial risk view sit when a new evidence step is proposed for the application?

Katerina
--- M2
Hi Jonathan,

A commercial risk view starts with scope: the insurer sets the threshold, and a flag refers only gaps above it. FitXpress is not a medical device and does not make underwriting decisions. If product governance for protection sits with someone else, I would gladly take the role name.

Further detail:
https://3dlook.ai/for-insurance-underwriting/

Would a call on the record a flag leaves on a case be useful? https://meetings.hubspot.com/katerina-galich

Katerina
@@@ sarah-holifield-454023211
hook: Customer Underwriting Team Manager (title only, empty profile)
proof: 2 photos, threshold flag, GDPR line (card)
--- M1
Hi Sarah,

Running a customer underwriting team at Legal & General means your team sees what each case arrives with. For build, some arrive with declared height and weight only. FitXpress would add a second source: 2 photos and a Smart Scales weight estimate, with a flag raised when its gap to declared weight crosses the threshold the insurer sets.

If a flag reached your queue, where would your team want to see it: on the case summary or inside the file?

Katerina
--- M2
Hi Sarah,

A flag would arrive with the threshold that raised it and a timestamp, and the underwriter decides what follows. In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes SCCs.

Where it is described:
https://3dlook.ai/for-insurance-underwriting/

I can walk your team through it on a call: https://meetings.hubspot.com/katerina-galich

Katerina
@@@ choi-justin
hook: Group Head of Digital Channels and Innovation, channels background
proof: 2 photos, timestamped record (card)
--- M1
Hi Justin,

Digital channels and innovation at group level means judging which journey steps deserve a test. In the Legal & General protection application, 2 photos from the applicant return a Smart Scales weight estimate and a timestamped record, with a flag raised when its gap to declared weight exceeds the insurer's threshold.

How does your team judge whether a camera step in a journey adds value or only friction?

Katerina
--- M2
Hi Justin,

Friction is measured in the evaluation: completion of the photo step is counted before any live use, and the record goes to the insurer's systems only. If the direct-to-client protection journey belongs to another team, I would value a pointer to the role.

Overview of the step:
https://3dlook.ai/for-insurance-underwriting/

Could we have a call to look at it together? https://meetings.hubspot.com/katerina-galich

Katerina
