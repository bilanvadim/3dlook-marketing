# Full dump after fix rounds 1-2: 2026-10-29-us-insurance-underwriting, 277 people, grouped by company

## Penn Mutual (14)

### Dean Galgano · Director, Underwriting Strategy and Governance · lane underwriting · P2 · `dean-galgano-aalu-fmli-i-6279595`

**M1**

Hi Dean,

Couldn't help but ask about governance on accelerated cases at Penn Mutual, where a new evidence input needs an owner and a record.

Two photos taken in the e-application give FitXpress a Smart Scales weight estimate. The flag is raised only above a threshold Penn Mutual sets, and the result lands as one timestamped record.

What steps does an input go through before it reaches a rule on accelerated cases?

Nick

**M2**

Hi Dean,

The record is what governance can review: threshold, flag and timestamp sit on the case file, and the rules stay with your underwriters.

FitXpress is not a medical device and does not make underwriting decisions.

The page shows the boundary in full, from flag to underwriter: https://3dlook.ai/for-insurance-underwriting/

Walking a governance reviewer through it would take one call: https://meetings.hubspot.com/nick-omelchak

Nick

### Jack Nance · Director of Underwriting · lane underwriting · P2 · `jack-nance-a02ba649`

**M1**

Hi Jack,

Got me thinking about what accelerated cases at Penn Mutual leave on file for build: the declared figures from the application.

FitXpress adds a Smart Scales estimate and BMI from the declared height after two photos in the e-application. A flag fires only above the carrier's own threshold.

In program monitoring, how is build treated on accelerated cases?

Nick

**M2**

Hi Jack,

One more thought on monitoring: a record carrying the flag, its threshold and a timestamp gives a post-issue review something to read back, with no result attached.

FitXpress is not a medical device and does not make underwriting decisions.

A call to talk through how monitoring would read it is open here: https://meetings.hubspot.com/nick-omelchak

Nick

### Chris Feldges · Director of Underwriting · lane underwriting · P2 · `chris-feldges-falu-flmi-mba-acs-501083a5`

**M1**

Hi Chris,

Spotted your brokerage underwriting background. On Penn Mutual's accelerated files the build evidence is the declared height and weight on the application.

Using two photos from the e-application, FitXpress returns a Smart Scales weight estimate and a flag once the estimate departs from declared weight by more than the threshold Penn Mutual sets.

What would a shadow run have to show before any output reached a case?

Nick

**M2**

Hi Chris,

An evaluation runs in shadow: outputs stay out of decisions, and your team compares the flags with build evidence from paramedical exam cases.

FitXpress is not a medical device and does not make underwriting decisions.

Booking a slot to design that shadow run takes a minute here: https://meetings.hubspot.com/nick-omelchak

Nick

### Michele Ohler · Vice President of New Business · lane proposition · P2 · `micheleohler`

**M1**

Hi Michele,

Caught your earlier work implementing automated underwriting. ACE now handles client invitation and tracking at Penn Mutual.

The step is two photos in the e-application, returning a Smart Scales weight estimate with a flag above a threshold Penn Mutual sets.

How would you introduce a step like that to the field before a wider rollout?

Nick

**M2**

Hi Michele,

A practical angle for new business: completion is measured during the evaluation, and applicants who skip the scan carry on through the existing path.

FitXpress is not a medical device and does not make underwriting decisions.

The page describes where such a step can sit in an application: https://3dlook.ai/for-insurance-underwriting/

Talking through an ACE rollout order would suit a call: https://meetings.hubspot.com/nick-omelchak

Nick

### Matthew Clark · Chief Information Security Officer · lane technical-integration · P3 · `matthew-lawrence-clark`

**M1**

Hi Matthew,

Wondering how a photo step in Penn Mutual's e-application would pass through security review.

FitXpress takes two photos through an API or SDK and returns a Smart Scales weight estimate with a flag above a threshold the carrier sets, as one structured record.

What does a new data vendor have to clear before it joins the new-business journey?

Nick

**M2**

Hi Matthew,

For the review: TLS in transit and S3-managed encryption at rest. Photos are deleted after processing or within 30 days per the carrier's policy, retained photos are blurred, and faces are obscured at capture.

FitXpress is not a medical device and does not make underwriting decisions.

Documents go through legal@3dlook.me, and the FAQ covers data handling: https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/

A call with security would cover the rest: https://meetings.hubspot.com/nick-omelchak

Nick

### Michael Clark · Chief Medical Officer · lane medical · P1 · `michael-clark-61006a107`

**M1**

Hi Michael,

Curious how weight is treated on Penn Mutual's accelerated cases that have no exam, where it is the number the applicant declares.

A Smart Scales weight estimate comes back from two photos taken in the e-application, with a flag only when the gap crosses a threshold Penn Mutual's team sets.

Which safeguards would you want around a weight estimate used only for referral?

Nick

**M2**

Hi Michael,

On the estimate: Smart Scales runs at approximately 3.5% mean absolute error under evaluated conditions, and it is not a scale reading. A flag is a referral, and Penn Mutual's team sets the line.

FitXpress is not a medical device and does not make underwriting decisions.

If you want to go through the evaluation conditions, a call works: https://meetings.hubspot.com/nick-omelchak

Nick

### Bill Bell · Chief Product Officer · lane proposition · P2 · `billbellpml`

**M1**

Hi Bill,

This stood out about your product remit at Penn Mutual. An added step in the e-application has a cost as well as a benefit.

FitXpress returns a Smart Scales weight estimate from two photos, with a flag above a threshold Penn Mutual sets, as one structured record.

What would an added evidence step need to show before it belongs in an accelerated journey?

Nick

**M2**

Hi Bill,

On cost against value, an evaluation shows what each threshold would flag before anything is built into a product journey.

FitXpress is not a medical device and does not make underwriting decisions.

The page gives the wider picture of the record and its limits: https://3dlook.ai/for-insurance-underwriting/

A call would help us size the evaluation against your product plans: https://meetings.hubspot.com/nick-omelchak

Nick

### Amzad Hossain · Chief Technology Officer · lane technical-integration · P3 · `amzadhossain`

**M1**

Hi Amzad,

Thought I'd share a question about ACE at Penn Mutual: if it carries a photo step, the SDK has to sit somewhere and the record has to land somewhere.

Two photos go through an SDK or API, and FitXpress returns a Smart Scales weight estimate with a flag above a threshold the carrier sets, as one timestamped structured record.

Where would a new SDK step enter ACE, and where would that record go?

Nick

**M2**

Hi Amzad,

On the integration side: REST API and web and mobile SDKs, with one timestamped record per applicant returned to the system you choose.

FitXpress is not a medical device and does not make underwriting decisions.

If integrations belong to a specific architect, send me their way. A walkthrough with your engineers would fit on a call: https://meetings.hubspot.com/nick-omelchak

Nick

### Gretchen Dinucci · VP, Chief Underwriter · lane underwriting · P1 · `gretchen-dinucci-74b33b45`

**M1**

Hi Gretchen,

Noticed your mortality management background at Penn Mutual. On ACE's accelerated route, build rests on the height and weight the applicant enters.

We built FitXpress to add two photos to the e-application and flag a gap between declared and estimated weight, only when it crosses a threshold Penn Mutual sets.

Where would that gap have to land against your build chart to change a preferred or standard class?

Nick

**M2**

Hi Gretchen,

For an evaluation we count the flags each candidate threshold would raise on accelerated files, then compare them with build evidence gathered separately from paramedical exam cases.

FitXpress is not a medical device and does not make underwriting decisions.

The page shows how the flag and its timestamp sit on a case file: https://3dlook.ai/for-insurance-underwriting/

If a short call on your threshold question helps, here is my calendar: https://meetings.hubspot.com/nick-omelchak

Nick

### Sharon Garner · AVP, Associate Chief Underwriter · lane underwriting · P2 · `sharon-garner-certified-falu-flmi-8a587980`

**M1**

Hi Sharon,

Quick one on build for Penn Mutual's accelerated files. With no paramedical exam, height and weight are the numbers the applicant enters.

Two photos from the e-application go to FitXpress, which returns a Smart Scales weight estimate. It flags a gap against declared weight only when it crosses a threshold your team sets, in one timestamped record.

Who looks at build on an accelerated file, and at what point in the case?

Nick

**M2**

Hi Sharon,

Picture a referral reaching your queue with the flag, the threshold and a timestamp attached. Underwriters decide what happens next, as they do now.

FitXpress is not a medical device and does not make underwriting decisions.

If it helps to see how that referral would read, I can show it here: https://meetings.hubspot.com/nick-omelchak

Nick

### Jakki Velez · Director, Life New Business · lane proposition · P2 · `velezjacqueline`

**M1**

Hi Jakki,

Wanted to reach out about ACE, which your earlier account manager role at Penn Mutual touched.

FitXpress would add a step of two photos in the e-application and return a Smart Scales weight estimate and one structured record, with a flag only above a threshold Penn Mutual sets.

How is drop-off tracked at each step in ACE?

Nick

**M2**

Hi Jakki,

Placement is the part worth testing, and the evaluation measures completion alongside it.

FitXpress is not a medical device and does not make underwriting decisions.

The page shows where the step can sit in the flow: https://3dlook.ai/for-insurance-underwriting/

If agent feedback on ACE sits elsewhere, I would gladly hear who handles it. A call on how completion gets measured fits here: https://meetings.hubspot.com/nick-omelchak

Nick

### Marianne Cumming · Vice President, Chief Medical Director · lane medical · P1 · `marianne-cumming-9b85442b`

**M1**

Hi Marianne,

Made me think about your years in insurance medicine, including the AAIM presidency. On Penn Mutual's accelerated cases there is no exam weight, only the weight the applicant declares.

Two photos in the e-application give FitXpress a Smart Scales weight estimate and BMI from the declared height. A flag appears only when the gap crosses a threshold Penn Mutual sets.

In build guidance, how does an exam weight rank against a declared one?

Nick

**M2**

Hi Marianne,

A short note on the line: the estimate is software and never a scale reading, and the margin a threshold keeps above its error is Penn Mutual's call.

FitXpress is not a medical device and does not make underwriting decisions.

The page spells out the boundary between the flag and the decision: https://3dlook.ai/for-insurance-underwriting/

A conversation about that margin would be easy to set up here: https://meetings.hubspot.com/nick-omelchak

Nick

### Brent Ricci · AVP, Life New Business & ACE at Penn Mutual · lane proposition · P2 · `brent-ricci-7b922a132`

**M1**

Hi Brent,

Had a thought since ACE appears in your title. Where an application carries height and weight as the applicant enters them, a photo step could sit near the start or just before submission.

FitXpress would return a Smart Scales weight estimate from two photos, with a flag above a threshold Penn Mutual sets.

Would ACE take that step earlier in the flow or just before submission?

Nick

**M2**

Hi Brent,

On ACE the step is a short addition to the e-application, and the result returns to Penn Mutual as one timestamped record.

FitXpress is not a medical device and does not make underwriting decisions.

Mapping that onto ACE is the call I would suggest: https://meetings.hubspot.com/nick-omelchak

Nick

### Jacqueline Fallon · VP, Product Management · lane proposition · P3 · `jacqueline-fallon-977295173`

**M1**

Hi Jacqueline,

Worth raising: accelerated cases at Penn Mutual give a build input little to compare against, because height and weight are entered by the applicant.

FitXpress turns two photos in the e-application into a Smart Scales weight estimate and a flag above a threshold the carrier sets.

What would product management want measured before a step like this reaches the field?

Nick

**M2**

Hi Jacqueline,

Product gets a view too: an evaluation counts flags per threshold, showing what a step would touch before it ships.

FitXpress is not a medical device and does not make underwriting decisions.

Pointing me to the actuary who reviews underwriting inputs would also help. A short call on what to measure fits here: https://meetings.hubspot.com/nick-omelchak

Nick

## Sammons Financial (14)

### Kory Petoske · Director, Underwriting Rules and Innovation · lane underwriting · P2 · `kory-petoske-15a70194`

**M1**

Hi Kory,

Spotted a fit with accelerated rules at Sammons: a build rule reads the figures typed into the application.

For a rule to use it, FitXpress returns a Smart Scales weight estimate from two photos, with a flag above a threshold Sammons sets, as one structured record.

What evidence would a shadow run need to produce before a rule could read it?

Nick

**M2**

Hi Kory,

In shadow, the record sits beside the case, counts flags per threshold and changes nothing.

FitXpress is not a medical device and does not make underwriting decisions.

The page shows what the record holds for a rule to read: https://3dlook.ai/for-insurance-underwriting/

Setting up that shadow run starts with a call: https://meetings.hubspot.com/nick-omelchak

Nick

### Amy Rider · Vice President, Underwriting Strategy and Mortality Management · lane underwriting · P1 · `amy-rider-falu-flmi-ab466944`

**M1**

Hi Amy,

Noticed your mortality management background at Sammons. WriteAway cases are decided without an exam, which leaves build as the height and weight the applicant enters.

Two photos taken in the e-application give FitXpress a Smart Scales weight estimate. A gap against declared weight is flagged only above a threshold Sammons sets, and the record carries a timestamp.

In post-issue reviews, is build looked at separately from the rest of the file?

Nick

**M2**

Hi Amy,

Evaluation first: flags counted per candidate threshold and compared with build evidence from cases that did have an exam, with outputs kept out of decisions.

FitXpress is not a medical device and does not make underwriting decisions.

The page shows how the record reads on a case file: https://3dlook.ai/for-insurance-underwriting/

If post-issue reviews are a fit for a call, here is my calendar: https://meetings.hubspot.com/nick-omelchak

Nick

### Pat Grashel · AVP, New Business · lane proposition · P3 · `pat-grashel-46202a8b`

**M1**

Hi Pat,

Quick one on new business at Sammons. When a life application reaches intake, height and weight are the build information it carries.

Intake would receive a Smart Scales weight estimate from two photos, with a flag above a threshold Sammons sets.

Does anyone look at height and weight at intake before underwriting?

Nick

**M2**

Hi Pat,

At intake the difference is one record: flag, threshold and timestamp, ready when the case reaches underwriting.

FitXpress is not a medical device and does not make underwriting decisions.

If life intake sits elsewhere, I would value an introduction. Happy to cover intake handling on a call: https://meetings.hubspot.com/nick-omelchak

Nick

### Beth Abbott · AVP New Business and Policy Change · lane proposition · P3 · `beth-abbott-1b495925`

**M1**

Hi Beth,

Worth raising for new business at Sammons: an optional step in a life application needs a plan for applicants who skip it.

Two photos taken at application return a Smart Scales weight estimate and a flag above a threshold Sammons sets.

What happens to a case today when an applicant cannot finish a step?

Nick

**M2**

Hi Beth,

Skipping the scan changes nothing downstream: the existing path stays, and a record exists only for cases that scanned.

FitXpress is not a medical device and does not make underwriting decisions.

Skipped steps are a fine topic for a call: https://meetings.hubspot.com/nick-omelchak

Nick

### Nicole Duncan · Director, Underwriting Operations · lane underwriting · P2 · `nicole-duncan-falu-flmi-airc-acs-03992313`

**M1**

Hi Nicole,

Came across your work in underwriting operations at Sammons. WriteAway cases decided without an exam rely on declared height and weight alone.

Two photos in the e-application, then FitXpress returns a Smart Scales estimate and a flag when a gap against declared weight crosses a threshold Sammons sets.

At what point in the case flow does build get a first look?

Nick

**M2**

Hi Nicole,

For case flow, a referral arrives with the flag, the threshold and a timestamp attached.

FitXpress is not a medical device and does not make underwriting decisions.

The page lists what travels with a referral: https://3dlook.ai/for-insurance-underwriting/

A call on routing would take little time: https://meetings.hubspot.com/nick-omelchak

Nick

### Matt Rise · Director, Underwriting Operations · lane underwriting · P2 · `mattrise`

**M1**

Hi Matt,

Wanted to reach out about WriteAway cases at Sammons, which skip the exam. Build on those cases comes from the numbers the application form carries.

FitXpress sends back one timestamped record from two photos, with a Smart Scales estimate and a flag only above a threshold Sammons sets.

Who picks up a build referral once it is raised?

Nick

**M2**

Hi Matt,

Each flag comes with one timestamped record, and whoever picks it up reads the same file.

FitXpress is not a medical device and does not make underwriting decisions.

A call about how referrals would move through your flow fits here: https://meetings.hubspot.com/nick-omelchak

Nick

### Christie Brammer · Vice President - Life Product · lane proposition · P2 · `christie-brammer-92b2a467`

**M1**

Hi Christie,

Caught your path through life product development and reinsurance at Sammons. Accelerated cases carry height and weight as the applicant enters them.

FitXpress would add a step of two photos to the e-application, returning a Smart Scales weight estimate and a flag above a threshold Sammons sets.

How would drop-off at a new step get measured, and by whom?

Nick

**M2**

Hi Christie,

By design the step is optional: Sammons chooses where it is offered, and applicants who skip it continue on the usual path.

FitXpress is not a medical device and does not make underwriting decisions.

The page shows where the step can sit in a life application: https://3dlook.ai/for-insurance-underwriting/

If application design belongs to someone else, I would be glad to be introduced. Placement and drop-off are easy to cover on a call: https://meetings.hubspot.com/nick-omelchak

Nick

### Elizabeth Alexander · AVP - Life Product Management · lane proposition · P2 · `elizabeth-alexander-5a6a0b235`

**M1**

Hi Elizabeth,

Got me thinking about how a new step in a life application gets tested before agents see it at Sammons.

FitXpress returns a Smart Scales weight estimate and a flag above a threshold Sammons sets, from two photos in the e-application.

How would a new step reach agents at Sammons, one channel first or all together?

Nick

**M2**

Hi Elizabeth,

For rolling it out, an evaluation can begin in a single channel and leave the others as they are.

FitXpress is not a medical device and does not make underwriting decisions.

The product owner for agent channels is welcome to join instead. Shaping a first channel together is a good next step: https://meetings.hubspot.com/nick-omelchak

Nick

### Paul Mocarski · Chief Information Security Officer (CISO) and Vice President IT Infrastructure · lane technical-integration · P3 · `pjmocarski`

**M1**

Hi Paul,

Wondering how Sammons reviews a new data vendor: a photo step in the e-application would bring one into the new-business journey.

Through an SDK or API, two photos give FitXpress a Smart Scales weight estimate and a flag above a threshold the carrier sets, returned as one structured record.

Which checks does a new data vendor go through before launch at Sammons?

Nick

**M2**

Hi Paul,

TLS in transit and S3-managed encryption at rest. Photos are deleted after processing or within 30 days per the carrier's policy, with retained photos blurred and faces obscured at capture.

FitXpress is not a medical device and does not make underwriting decisions.

Security documents go through legal@3dlook.me, and the FAQ covers data handling: https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/

A call would cover the rest: https://meetings.hubspot.com/nick-omelchak

Nick

### Courtney Jacobson · AVP, Life New Business, Policy Change and Jet Underwriting · lane proposition · P2 · `courtney-jacobson-certified-falu-almi-acs-6a4b9096`

**M1**

Hi Courtney,

Had a thought about Jet underwriting at Sammons. A build input on Jet cases is what the life application declares.

FitXpress adds two photos to the life application and returns a Smart Scales weight estimate with a flag above a threshold Sammons sets.

Where in the life application, ahead of Jet, would a photo step sit best?

Nick

**M2**

Hi Courtney,

Jet keeps its route; the step adds a record the underwriter sees alongside the file.

FitXpress is not a medical device and does not make underwriting decisions.

The page shows how that record looks on a case: https://3dlook.ai/for-insurance-underwriting/

Talking Jet placement through is easy to arrange: https://meetings.hubspot.com/nick-omelchak

Nick

### Roger Hofer · Director, Mortality Management · lane underwriting · P2 · `roger-hofer-79065019`

**M1**

Hi Roger,

Curious how a case reads in a post-issue review at Sammons when no exam was part of the decision.

FitXpress flags a gap between declared and estimated weight, above a threshold Sammons sets, from two photos in the e-application.

Which build fields does a reviewer see on such a case?

Nick

**M2**

Hi Roger,

A flag only refers cases, set above the estimate's error, and the class stays with your underwriters. A reviewer later reads the flag, its threshold and a timestamp from the same record.

FitXpress is not a medical device and does not make underwriting decisions.

A call to see what a reviewer would read is easy to book here: https://meetings.hubspot.com/nick-omelchak

Nick

### Matt Webster · Chief Medical Director · lane medical · P2 · `matt-webster-389321228`

**M1**

Hi Matt,

This is a note on accelerated cases at Sammons with no exam, where weight is the number the applicant declares.

A Smart Scales weight estimate comes back from two photos taken in the e-application, flagged only when the gap against declared weight crosses a threshold Sammons sets.

What would make a weight estimate from software acceptable as a referral input?

Nick

**M2**

Hi Matt,

The estimate is software and never a scale reading. Sammons sets the threshold, and a flag only refers a case to an underwriter.

FitXpress is not a medical device and does not make underwriting decisions.

The page states where the boundary sits between flag and decision: https://3dlook.ai/for-insurance-underwriting/

I can go through the referral use with you here: https://meetings.hubspot.com/nick-omelchak

Nick

### Norma Davis · Vice President and Medical Director · lane medical · P2 · `norma-davis-9064212b`

**M1**

Hi Norma,

Looking at accelerated cases at Sammons with no exam: weight rests on the applicant's declaration.

FitXpress takes two photos in the e-application and returns a Smart Scales estimate. It raises a flag only when the gap crosses a threshold Sammons sets.

How wide should the margin be between the estimate's error and a referral threshold?

Nick

**M2**

Hi Norma,

Setting the margin is Sammons's call, and an evaluation shows how many flags each margin raises.

FitXpress is not a medical device and does not make underwriting decisions.

The page describes the shadow evaluation path: https://3dlook.ai/for-insurance-underwriting/

Choosing a margin together is a good use of a call: https://meetings.hubspot.com/nick-omelchak

Nick

### Katrisha Neisse · VP & Actuary, Life Insurance Product Development · lane proposition · P2 · `katrishaneisse`

**M1**

Hi Katrisha,

Thought I'd share an idea on accelerated cases at Sammons, where extra evidence has a cost and build is the applicant's entry today.

From two photos in the e-application, FitXpress returns a Smart Scales weight estimate with a flag above a threshold Sammons sets, as one structured record.

How is the cost of added evidence weighed against its use on a case?

Nick

**M2**

Hi Katrisha,

Cost and value show up together in an evaluation: flags per threshold against the cases each one would have touched.

FitXpress is not a medical device and does not make underwriting decisions.

Pointing me to the actuarial reviewer of underwriting inputs works too. Weighing that cost together suits a call: https://meetings.hubspot.com/nick-omelchak

Nick

## Prudential Financial (13)

### Bryan Flynn · Vice President, Underwriting · lane underwriting · P2 · `bryan-flynn-21866b9`

**M1**

Hi Bryan,

Quick thought on PruFast Track, which removes medical exams and lab work at Prudential Financial. On those cases the build evidence is the applicant's own declared figures.

FitXpress adds a step with two photos in the application: a Smart Scales weight estimate, and a flag against Prudential's threshold when the gap from declared weight is large enough. One timestamped record goes to the case file.

Before any flag touched a live PruFast Track case, what would a shadow evaluation have to show your team?

Nick

**M2**

Hi Bryan,

The evaluation compares flags with build evidence gathered separately, showing where they agree before a rule moves. Outputs stay out of decisions throughout.

FitXpress is not a medical device and does not make underwriting decisions.

A short walkthrough of that comparison is available through my calendar at https://meetings.hubspot.com/nick-omelchak

Nick

### Michael Farrell · Vice President, Underwriting · lane underwriting · P2 · `michael-farrell-5611685`

**M1**

Hi Michael,

Saw the news on Just Ask, the advisor tool that returns an underwriting quote from basic client details. FitXpress sits a step later, at the application.

From two photos it returns a Smart Scales weight estimate, and flags a gap against declared weight when it crosses Prudential Financial's threshold. The record is timestamped.

Once a quote from basic details becomes an application, where is declared build reconciled with anything else on the file?

Nick

**M2**

Hi Michael,

A flag raised on the application would sit in the case file beside the quote it followed, structured and timestamped. Underwriters and Prudential's rules decide what happens next.

FitXpress is not a medical device and does not make underwriting decisions.

The landing page sets out where such a record fits at https://3dlook.ai/for-insurance-underwriting/

If the quote-to-application hand-off is worth a conversation, a time can be booked at https://meetings.hubspot.com/nick-omelchak

Nick

### Matt Burrill · Vice President, Underwriting · lane underwriting · P2 · `matthewburrill`

**M1**

Hi Matt,

Noticed your actuarial career before underwriting at Prudential Financial. On accelerated files decided without an exam, build rests on the height and weight the applicant enters.

From two photos, FitXpress returns a Smart Scales weight estimate and raises a flag only where the gap against declared weight would cross a build chart line or preferred class boundary Prudential sets.

Which class boundaries would a flagged gap have to cross before it matters to risk selection?

Nick

**M2**

Hi Matt,

An evaluation could tally flags by build chart line and class boundary, which gives a class-boundary review something concrete to read. Rules and underwriters decide, and the flag is a referral.

FitXpress is not a medical device and does not make underwriting decisions.

If a tally by class boundary is useful to see, pick a slot at https://meetings.hubspot.com/nick-omelchak

Nick

### Brian Pemberton · Vice President, New Business Underwriting · lane underwriting · P3 · `brian-pemberton-09ba289`

**M1**

Hi Brian,

Got me thinking about new business underwriting at Prudential Financial, whose term suite pairs an online applicant interview with a Life Case Tracker. An added photo step would sit inside that flow.

Two photos in FitXpress yield a Smart Scales weight estimate, and a flag appears when the gap against declared weight crosses the carrier's threshold. A timestamped record goes with it.

At which point in a case would an underwriter want to see such a flag?

Nick

**M2**

Hi Brian,

The flag arrives as one structured, timestamped record for whoever picks the case up. Rating and classing remain with that underwriter.

FitXpress is not a medical device and does not make underwriting decisions.

Where new business underwriting for term lives with a different team, a pointer works. Could we look at where the flag would sit in a case, with my calendar at https://meetings.hubspot.com/nick-omelchak

Nick

### David Wexler · Vice President, New Business Operations · lane proposition · P3 · `david-wexler-47978554`

**M1**

Hi David,

This stood out: Prudential Financial's term suite pairs an online applicant interview with a Life Case Tracker. A step added to that flow changes how files move through new business operations.

FitXpress would add two photos, a Smart Scales weight estimate and a flag on gaps against declared weight above the carrier's threshold. The record is timestamped.

What would you track to tell whether the step slows files down or speeds them up?

Nick

**M2**

Hi David,

Placement is the thing to test: the same step at different points of the flow, with completion measured each time. Underwriters and the carrier's rules decide everything after the flag.

FitXpress is not a medical device and does not make underwriting decisions.

A conversation about testing placement is simple to book at https://meetings.hubspot.com/nick-omelchak

Nick

### Ashley Destito · Vice President and Head of Individual Life Financial Planning and Analysis · lane referral · P3 · `ashley-destito-a636194b`

**M1**

Hi Ashley,

Thought I'd share something for the individual life side of Prudential Financial, where you lead financial planning and analysis. It concerns the cost of extra evidence on accelerated cases.

FitXpress adds two photos, a Smart Scales weight estimate and a flag for any estimate that departs from declared weight beyond the carrier's threshold, with one timestamped record per case.

How does your team weigh what extra evidence on an accelerated file costs against what it returns?

Nick

**M2**

Hi Ashley,

The cost question belongs in a shadow evaluation, which counts flags per threshold before any rule changes.

FitXpress is not a medical device and does not make underwriting decisions.

The landing page lays out the evaluation step by step at https://3dlook.ai/for-insurance-underwriting/

If underwriting rules or the new-business journey rest with someone else, send me their way. To compare notes on evidence cost, a time can be found at https://meetings.hubspot.com/nick-omelchak

Nick

### Salene Hitchcock-Gear · President, Individual Life Insurance, · lane proposition · P2 · `salene-hitchcock-gear-a8207a12`

**M1**

Hi Salene,

Wanted to reach out about the individual life buying experience at Prudential Financial. A step added there needs a place where applicants meet it, and where it goes is a business decision.

FitXpress's step takes two photos and returns a Smart Scales weight estimate, with a flag where the estimate sits beyond the carrier's threshold from declared weight. The carrier chooses where it is offered.

Where in the individual life buying journey would you try a step like that first?

Nick

**M2**

Hi Salene,

A placement test could measure how many applicants complete the step at each point it is offered, and that completion rate would show where it belongs. Anyone who prefers the current route can keep it.

FitXpress is not a medical device and does not make underwriting decisions.

Should the journey placement belong to a colleague, a name would be a great help. For a conversation about placement, times are open at https://meetings.hubspot.com/nick-omelchak

Nick

### Dan Manley · Chief Information Security Officer · lane technical-integration · P3 · `dan-manley-b15759`

**M1**

Hi Dan,

Couldn't help but ask how a vendor handling applicant photos reaches your review at Prudential Financial. An accelerated e-application step with photos would come through it.

FitXpress takes two photos, returns a Smart Scales weight estimate and flags a gap against declared weight above the carrier's threshold. Scan records sit on random identifiers.

What does your vendor review ask about photo retention and data flow?

Nick

**M2**

Hi Dan,

Photos are deleted after processing or within 30 days per the carrier's policy, retained photos are blurred, and faces are obscured at capture. Scan records stay on random identifiers.

FitXpress is not a medical device and does not make underwriting decisions. Documents go through legal@3dlook.me.

The privacy FAQ answers the data-handling questions at https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/

For a walkthrough of photo handling, reserve a time at https://meetings.hubspot.com/nick-omelchak

Nick

### Joel Larson · Vice President, Chief Underwriter · lane underwriting · P2 · `joel-larson-31339b223`

**M1**

Hi Joel,

Spotted that Prudential Financial's EssentialTerm qualifies for PruFast Track, which removes exams and lab work. For those files, build comes from the applicant's own height and weight entries.

Two photos give FitXpress a Smart Scales weight estimate, with a flag whenever the estimate and the declared weight diverge past a threshold your team sets. One timestamped record lands on the case.

When no exam or labs are ordered, who looks at build, and at which point in the case?

Nick

**M2**

Hi Joel,

A shadow evaluation would count the accelerated files each proposed threshold flags, with every output held away from decisions. That shows volume before any rule changes.

FitXpress is not a medical device and does not make underwriting decisions.

Whenever time allows, I can take you through that volume view, with the booking link at https://meetings.hubspot.com/nick-omelchak

Nick

### Karna Trautman · Chief Product Officer - Simplified Solutions · lane proposition · P2 · `karnatrautman`

**M1**

Hi Karna,

Curious how Simplified Solutions at Prudential Financial fits new steps into an instant-decision flow. FitXpress adds one: two photos in the e-application, a Smart Scales weight estimate, and a flag if declared weight and the estimate part ways beyond the carrier's threshold.

The carrier decides where it is offered, and a timestamped record follows each flag.

How would you test a step like that for drop-off before it reaches every applicant?

Nick

**M2**

Hi Karna,

FitXpress returns 80+ body measurements, under 45 seconds from the photos to structured results. In the evaluation, completion is measured step by step.

FitXpress is not a medical device and does not make underwriting decisions.

The landing page shows how that evaluation is staged at https://3dlook.ai/for-insurance-underwriting/

For testing in an instant journey, a slot is open at https://meetings.hubspot.com/nick-omelchak

Nick

### Naishami Patel · VP & Medical Director · lane medical · P2 · `naishami-patel-do-6788267`

**M1**

Hi Naishami,

Caught that you have practiced as an attending physician. Prudential Financial's PruFast Track removes medical exams and lab work, which leaves weight to the applicant's own entry.

Two photos produce a Smart Scales weight estimate in FitXpress, and a flag appears only when the gap against declared weight crosses a threshold the carrier sets. Guidelines and underwriters still decide.

Which uses of an estimated weight would you accept in accelerated rules, and which would you rule out?

Nick

**M2**

Hi Naishami,

Smart Scales gives a weight estimate with approximately 3.5% mean absolute error under evaluated conditions, and it is not a scale reading. The threshold belongs to Prudential's rules and sits above that error.

FitXpress is not a medical device and does not make underwriting decisions.

To go through those evaluation conditions, you can choose a time at https://meetings.hubspot.com/nick-omelchak

Nick

### Jill Fallon · VP Medical Director · lane medical · P2 · `jill-fallon-944a9812`

**M1**

Hi Jill,

Had a thought about weight on Prudential Financial's accelerated cases, where medical direction shapes what an estimate may do.

FitXpress turns two photos into a Smart Scales weight estimate and flags a gap against declared weight only above a threshold the carrier sets. A timestamped record accompanies each flag.

What gap between declared and estimated weight would you consider large enough to refer, given the estimate's stated error?

Nick

**M2**

Hi Jill,

The conditions the estimate was evaluated under are the useful starting point, and the carrier sets the threshold above its error. Each record is timestamped for the file.

FitXpress is not a medical device and does not make underwriting decisions.

Should a call on those conditions be useful, booking is open at https://meetings.hubspot.com/nick-omelchak

Nick

### Vikram Balwani · Chief Technology Officer at Simplified Solutions - Individual Life Insurance · lane technical-integration · P3 · `vikrambalwani`

**M1**

Hi Vikram,

Your headline, Simplified Solutions Start Up, made me think about how Prudential Financial's e-application takes new steps. FitXpress is an SDK step: two photos, a Smart Scales weight estimate, and a flag when estimated weight lands outside the carrier's threshold around declared weight.

One timestamped record comes back for the case.

How would an SDK step like that enter your application stack, and who signs it off?

Nick

**M2**

Hi Vikram,

Integration runs through a REST API and web and mobile SDKs, and the record comes back timestamped on a random identifier. The carrier decides where in the journey the step appears.

FitXpress is not a medical device and does not make underwriting decisions.

A call with your engineers could cover the SDK step end to end, and a slot can be taken at https://meetings.hubspot.com/nick-omelchak

Nick

## Northwestern Mutual (13)

### Nicole Lund · VP Underwriting Solutions · lane underwriting · P2 · `nicole-lund-4055466`

**M1**

Hi Nicole,

Wanted to reach out about the tools and vendors behind Northwestern Mutual's underwriting. Accelerated approvals there carry no medical tests, and the client completes an online questionnaire.

FitXpress returns one structured, timestamped record from two photos taken in the e-application, with a Smart Scales weight estimate and a flag for any difference between declared and estimated weight beyond the carrier's threshold. The record goes back to your systems.

What does your team ask of a new evidence source before it joins the tools underwriters work in?

Nick

**M2**

Hi Nicole,

On the tooling side, FitXpress connects through a REST API and SDKs, with each record timestamped and keyed to a random identifier.

FitXpress is not a medical device and does not make underwriting decisions.

For a technical walkthrough that fits your vendor review, times are open at https://meetings.hubspot.com/nick-omelchak

Nick

### Julia Oleson · Vice President, Underwriting Operations · lane underwriting · P2 · `julia-oleson-547066106`

**M1**

Hi Julia,

Curious how your client services background shapes the way you run underwriting operations. Northwestern Mutual's accelerated route has the client complete an online questionnaire, with no medical tests for approved cases.

A step with two photos could sit next to that questionnaire. FitXpress returns a Smart Scales weight estimate and flags a gap against declared weight only when it crosses the carrier's threshold, adding a timestamped record to the file.

Where in that flow would an added step create work for your team, and where could it remove some?

Nick

**M2**

Hi Julia,

Referral volume is what a shadow evaluation would show your team: how many files a proposed threshold would refer, before anything reaches a live case. That is the workload figure operations plans around.

FitXpress is not a medical device and does not make underwriting decisions.

To size that referral volume with you, you can book a time at https://meetings.hubspot.com/nick-omelchak

Nick

### Jaime Pulsfus · Vice President of Underwriting Operations · lane underwriting · P2 · `jaime-pulsfus`

**M1**

Hi Jaime,

Your supervision programs background got me thinking about how Northwestern Mutual monitors accelerated cases. Those approvals carry no medical tests, and the client completes the questionnaire online.

FitXpress adds two photos, returns a Smart Scales weight estimate and flags a gap against declared weight above the carrier's threshold. Each flag arrives as a timestamped record that monitoring can read later.

How does the program's monitoring look at build on those files, holdouts and post-issue review included?

Nick

**M2**

Hi Jaime,

Because each record is timestamped and structured, whoever reviews the program can read the flag and the threshold behind it long afterwards. Nothing about how a case is decided changes.

FitXpress is not a medical device and does not make underwriting decisions.

The pilot path from walkthrough to evidence comparison is on the page at https://3dlook.ai/for-insurance-underwriting/

Should you want to look at the monitoring angle live, the booking page is https://meetings.hubspot.com/nick-omelchak

Nick

### Kari Turtinen · VP Underwriting Risk Analytics, Standards, and Partnerships · lane underwriting · P1 · `kari-turtinen-31a178133`

**M1**

Hi Kari,

Spotted that your remit covers build standards and evidence partners at Northwestern Mutual. Its accelerated cases rest on a client-completed online questionnaire, which puts build in the height and weight entered there.

FitXpress adds a step to the e-application that takes two photos. It returns a Smart Scales weight estimate and a flag once declared and estimated weight drift apart by more than your team's threshold, as one timestamped record on the case file.

Which results from a shadow evaluation would make that threshold something your standards could adopt?

Nick

**M2**

Hi Kari,

A shadow evaluation keeps every flag out of decisions while counting how many each proposed threshold raises. The counts then sit beside build evidence gathered separately, such as paramedical exam cases.

FitXpress is not a medical device and does not make underwriting decisions.

The landing page walks through the evaluation path at https://3dlook.ai/for-insurance-underwriting/

To go through the evaluation design with you, a slot can be taken at https://meetings.hubspot.com/nick-omelchak

Nick

### Tim Ranfranz · VP Chief Life Underwriter (Underwriting Excellence) · lane underwriting · P1 · `tim-ranfranz-falu-fmli-81559b1a`

**M1**

Hi Tim,

Noticed your time as AHOU president. Northwestern Mutual approves some accelerated cases with no medical tests, and for those build comes from the height and weight the client enters.

Two photos in the e-application give FitXpress a Smart Scales weight estimate and BMI calculated from the declared height. A flag goes to your team only when the gap against declared weight reaches the build chart line or class boundary you set, with a timestamped record behind it.

Where on your build chart would a gap between declared and estimated weight start to move a class?

Nick

**M2**

Hi Tim,

The case file would carry one timestamped record per applicant: declared weight, the estimate, and the threshold in force. Your rules and your underwriters decide what any flag means.

FitXpress is not a medical device and does not make underwriting decisions.

A call could walk through how that record reads beside a class decision, and my calendar is at https://meetings.hubspot.com/nick-omelchak

Nick

### Brandon May · Vice President - Chief Medical Officer · lane medical · P1 · `brandon-may-do-dbim-ms-4288a5150`

**M1**

Hi Brandon,

Caught your headline pairing insurance medicine with data science. At Northwestern Mutual, accelerated approvals carry no medical tests, and weight reaches the file as the figure the client entered.

Two photos feed FitXpress, which returns a Smart Scales weight estimate. It raises a flag only when the gap against declared weight crosses a threshold the carrier sets, leaving guidelines and underwriters in charge.

Which uses of a weight estimate would you be comfortable writing into medical guidance, and which would you rule out?

Nick

**M2**

Hi Brandon,

Medical use of the estimate stays inside the carrier's rules: a referral on large gaps, a threshold set well above the estimate's error, and the declared weight left as entered.

FitXpress is not a medical device and does not make underwriting decisions.

The decision boundary is stated on the landing page at https://3dlook.ai/for-insurance-underwriting/

If useful, we could talk through where medical use of the estimate ends, and booking runs through https://meetings.hubspot.com/nick-omelchak

Nick

### Judy Finney · VP Medical Director · lane medical · P2 · `judy-finney-md-1882a34`

**M1**

Hi Judy,

Your years practicing cardiology before insurance medicine stood out. At Northwestern Mutual, accelerated approvals carry no medical tests, and weight comes from the client's questionnaire entry.

Two photos allow FitXpress to return a Smart Scales weight estimate, with a flag for differences from declared weight that exceed the carrier's referral level. The carrier's guidelines remain in charge of what follows.

What margin between estimate and declared weight would you want before calling a gap meaningful enough to refer?

Nick

**M2**

Hi Judy,

The Smart Scales estimate has a stated error of approximately 3.5% mean absolute error under evaluated conditions, and it is not a scale reading. Where a referral threshold sits against that error is a medical judgement for the carrier.

FitXpress is not a medical device and does not make underwriting decisions.

If you would like to go through the evaluation conditions behind that figure, you are welcome to choose a time at https://meetings.hubspot.com/nick-omelchak

Nick

### Dupe Adewunmi · Vice President, Medical Director · lane medical · P2 · `dupe-adewunmi`

**M1**

Hi Dupe,

Quick thought on disability. Northwestern Mutual extended accelerated underwriting to a subset of disability applicants.

FitXpress turns two photos into a Smart Scales weight estimate and a flag for declared-versus-estimated differences beyond the carrier's own limit. A timestamped record sits behind each flag.

Does DI underwriting read a build gap differently from life underwriting?

Nick

**M2**

Hi Dupe,

On DI files the flag would act as a referral on larger gaps only, with the carrier setting the threshold and a timestamped record going to the file.

FitXpress is not a medical device and does not make underwriting decisions.

The line between evidence and decision is stated at https://3dlook.ai/for-insurance-underwriting/

If DI needs its own treatment, time for it is open at https://meetings.hubspot.com/nick-omelchak

Nick

### Gregory Soltner · Vice President - Medical Director · lane medical · P2 · `gregory-soltner-do-dbim-falu-flmi-210a6632`

**M1**

Hi Gregory,

Thought I'd share an idea with someone trained in both family practice and insurance medicine. Northwestern Mutual approves a subset of disability applicants with no medical tests.

FitXpress takes two photos and returns a Smart Scales weight estimate, with a flag where estimated weight sits further from declared weight than the carrier's threshold allows. Each flag comes with a timestamped record.

Who reviews a build gap on those files today, and which guidance do they follow?

Nick

**M2**

Hi Gregory,

A reviewer would see the declared weight, the estimate and the threshold side by side on the record, with your guidance deciding how far a gap must reach to matter.

FitXpress is not a medical device and does not make underwriting decisions.

To see how that record would read in a DI review, pick a time at https://meetings.hubspot.com/nick-omelchak

Nick

### Joel Weiner · VP, Medical Director · lane medical · P2 · `joel-weiner-md-facp-flmi-18b07151`

**M1**

Hi Joel,

Had a thought about weight at Northwestern Mutual. Accelerated applicants complete an online questionnaire with no medical tests for approved cases, while exam cases carry a weight someone measured.

FitXpress would add two photos to the first kind, returning a Smart Scales weight estimate and a flag against the carrier's threshold. The record is timestamped.

How does your guidance weigh a declared weight against an exam weight?

Nick

**M2**

Hi Joel,

The narrow use on offer is a referral flag on gaps wide enough to change a class, with the declared weight left as the applicant gave it.

FitXpress is not a medical device and does not make underwriting decisions.

Happy to go through how that boundary would read against exam weights, with my calendar at https://meetings.hubspot.com/nick-omelchak

Nick

### Chris Yiannias · VP, Medical Director · lane medical · P2 · `chris-yiannias-000427116`

**M1**

Hi Chris,

Your internal medicine background made me think of this. Northwestern Mutual's accelerated approvals carry no medical tests, which leaves build to questionnaire entries.

FitXpress would give those files two photos, a Smart Scales weight estimate and a flag if estimated weight departs from the declared figure past the carrier's threshold. A timestamped record documents each flag.

What would medical sign-off on an estimated input have to cover?

Nick

**M2**

Hi Chris,

A sign-off file could hold the conditions the estimate was evaluated under, the threshold the carrier chose and the timestamped record for each flag. Underwriters keep every decision.

FitXpress is not a medical device and does not make underwriting decisions.

If a call on sign-off contents would help, one can be scheduled at https://meetings.hubspot.com/nick-omelchak

Nick

### Jonathan McAllister · VP, Medical Director · lane medical · P2 · `jonathan-mcallister-a91a5647`

**M1**

Hi Jonathan,

Saw that your clinical background includes years as a hospitalist. Northwestern Mutual's accelerated approvals carry no medical tests, and weight comes from the client's own entry.

Two photos in FitXpress produce a Smart Scales weight estimate, with a flag only above the carrier's threshold. The flag arrives as a timestamped record.

When a declared weight and an exam weight diverge, what size of gap does your guidance treat as worth a second look?

Nick

**M2**

Hi Jonathan,

The threshold stays with the carrier and sits well above the estimate's error. A flag is a referral for a second look, and the declared weight stays as entered.

FitXpress is not a medical device and does not make underwriting decisions.

Whenever a conversation suits you, I can go through how that boundary is evaluated, and you can choose a slot at https://meetings.hubspot.com/nick-omelchak

Nick

### Allyson Schrader · Chief Digital and Technology Officer · lane technical-integration · P3 · `allysonschrader`

**M1**

Hi Allyson,

Couldn't help but ask how a new SDK step reaches your technology review at Northwestern Mutual. Accelerated approvals there carry no medical tests, and the e-application is where a step would go.

FitXpress's SDK captures two photos and returns a Smart Scales weight estimate, with one timestamped record sent to underwriting systems when the gap against declared weight crosses the carrier's threshold.

Which checks does your review run on an SDK step before it enters the new-business journey?

Nick

**M2**

Hi Allyson,

Integration runs on a REST API and SDKs, with the record returned on a random identifier. Photos are deleted after processing or within 30 days per the carrier's policy.

FitXpress is not a medical device and does not make underwriting decisions. Documents go through legal@3dlook.me.

The privacy FAQ answers the data-handling questions at https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/

For a call on the SDK review, booking is open at https://meetings.hubspot.com/nick-omelchak

Nick

## John Hancock (13)

### Helen Colberg · Director, Underwriting Research and Development · lane underwriting · P2 · `helen-colberg-05a71153`

**M1**

Hi Helen,

Noticed your background in underwriting R&D at John Hancock. ExpressTrack cases are decided without an exam or labs, with the applicant's own height and weight as the build on file.

FitXpress adds two photos to the e-application. It returns a Smart Scales weight estimate and BMI from the declared height, raises a flag only when the gap crosses a threshold John Hancock sets, and leaves one timestamped record on the case file.

What would your team want build evidence to show first in an ExpressTrack study?

Nick

**M2**

Hi Helen,

For an R&D team the useful first step is a shadow evaluation with outputs kept out of decisions. The team counts how many cases each threshold under test would flag, then compares that with build from paramedical exam cases or from any holdouts the program runs.

FitXpress is not a medical device and does not make underwriting decisions.

If it would help to plan that study around ExpressTrack, here is my calendar: https://meetings.hubspot.com/nick-omelchak

Nick

### Laurie Borowski · Director, Underwriting Research & Development · lane underwriting · P2 · `laurie-borowski`

**M1**

Hi Laurie,

Came across your work in chief underwriter roles and now in R&D at John Hancock. ExpressTrack, the exam- and lab-free program, runs on the JH eApp, which is where a step for an evidence study would be offered.

FitXpress would take two photos there and return a Smart Scales weight estimate and a timestamped record, with a flag where the gap passes a threshold the carrier chooses.

What would a shadow evaluation have to show before any output reaches a live case?

Nick

**M2**

Hi Laurie,

A shadow evaluation can stay small. Flags are tallied against the carrier's thresholds, then read next to build from cases that did have a paramedical exam.

FitXpress is not a medical device and does not make underwriting decisions.

For the evaluation steps in order, see https://3dlook.ai/for-insurance-underwriting/

If a call would help shape the study, pick a time here: https://meetings.hubspot.com/nick-omelchak

Nick

### Andrew Langemeier · Director, Underwriting Research & Development · lane underwriting · P2 · `andrew-langemeier-falu-flmi-b7398813a`

**M1**

Hi Andrew,

Got me thinking about your technical underwriting background, now in R&D at John Hancock. On cases that never meet a paramedical examiner, build rests on the height and weight the applicant enters.

FitXpress turns two photos into a Smart Scales weight estimate and one timestamped record, with a referral flag raised only above the carrier's threshold.

If you lined that up against other build evidence, which comparison would convince you it agrees?

Nick

**M2**

Hi Andrew,

Agreement is the part worth testing first. One route lines the estimate up against exam-collected build from cases that had a paramedical exam, then reads the flags against it.

FitXpress is not a medical device and does not make underwriting decisions.

If you would like to settle which comparison to run first, the calendar is open at https://meetings.hubspot.com/nick-omelchak

Nick

### Jordan Jonassen · General Director - Life Underwriting · lane underwriting · P2 · `jordanjonassen`

**M1**

Hi Jordan,

Saw the news on Quick Quote, which gives distribution partners a preliminary assessment on less complex cases.

Two photos in the e-application give FitXpress what it needs to return a Smart Scales weight estimate, and the flag appears only where that estimate and the declared weight differ by more than a threshold John Hancock sets.

Does declared build already feed that early view, and would a large gap change what a partner is told?

Nick

**M2**

Hi Jordan,

A shadow run is the low-risk way to see it. Outputs stay out of decisions while flags are tallied at several thresholds and compared with build from paramedical cases.

FitXpress is not a medical device and does not make underwriting decisions.

What a shadow run covers is outlined at https://3dlook.ai/for-insurance-underwriting/

Grab a slot here if Quick Quote's early view is worth a conversation: https://meetings.hubspot.com/nick-omelchak

Nick

### David Moon · General Director, Life Underwriting · lane underwriting · P2 · `david-moon-045b748`

**M1**

Hi David,

Caught my eye while reading about ExpressTrack, John Hancock's exam- and lab-free program. Risk management on a program like that works from whatever the file holds on build.

From two photos added to the JH eApp, FitXpress returns a Smart Scales weight estimate, BMI from the declared height and a flag past a threshold John Hancock sets, all in one timestamped record.

How does risk management monitor build on ExpressTrack cases once they are issued?

Nick

**M2**

Hi David,

Monitoring needs a record to look at. Each case would carry the declared and estimated values side by side, with the threshold that applied on file.

FitXpress is not a medical device and does not make underwriting decisions.

If monitoring is where this matters most for ExpressTrack, a call can start there: https://meetings.hubspot.com/nick-omelchak

Nick

### Eric Kaiser · AVP, New Business Transformation · lane proposition · P2 · `ericskaiser`

**M1**

Hi Eric,

Made me think of your background in distribution operations and enterprise IT, now in new business transformation. Any step added to the JH eApp at John Hancock has to work for the people sending applications as well as for applicants.

FitXpress would add two photos to that application and return one timestamped record: a Smart Scales weight estimate, BMI from the declared height and a flag past a threshold the carrier sets.

Which signal tells your team a new JH eApp step is working for distribution?

Nick

**M2**

Hi Eric,

A placement test answers that with data. Completion is measured during the evaluation, and results go to John Hancock's systems only.

FitXpress is not a medical device and does not make underwriting decisions.

To see where a step fits an e-application, read https://3dlook.ai/for-insurance-underwriting/

To plan a test around the JH eApp, you can book a walkthrough here: https://meetings.hubspot.com/nick-omelchak

Nick

### Jasvinder Khera · Chief Information Security Officer · lane technical-integration · P3 · `jasvinder-khera-10bbb620a`

**M1**

Hi Jasvinder,

Thought I'd share something that starts as a vendor-review question, given your cyber defense background before John Hancock. A new evidence step in the e-application raises that question first.

FitXpress is an SDK step: two photos from the applicant's phone return a Smart Scales weight estimate and a flag past the carrier's threshold, with BMI from the declared height in one timestamped record.

What does a vendor review at John Hancock ask of a new SDK step in new business?

Nick

**M2**

Hi Jasvinder,

The technical side: REST API and SDKs, TLS in transit and S3-managed encryption at rest. Photos are deleted after processing or within 30 days per the carrier's policy, retained photos are blurred, and scan records use random identifiers.

FitXpress is not a medical device and does not make underwriting decisions.

Documents for the review go through legal@3dlook.me, and if a call helps with the integration questions, here is a time: https://meetings.hubspot.com/nick-omelchak

Nick

### Mike Link · Associate Chief Underwriter · lane underwriting · P2 · `mike-link-679151134`

**M1**

Hi Mike,

Had a thought about Quick Quote, John Hancock's preliminary assessment tool for less complex cases, given your years in underwriting management. A gap between declared and estimated weight could be one thing that makes a case more complex.

We built FitXpress to turn two photos into a Smart Scales weight estimate and one timestamped record, with a flag where John Hancock's threshold is exceeded.

Where on the build chart would a gap between declared and estimated weight change a risk class?

Nick

**M2**

Hi Mike,

Class-boundary gaps are the ones worth flagging. A flag is a referral trigger set above the estimate's error and read by an underwriter, who decides.

FitXpress is not a medical device and does not make underwriting decisions.

If a build-chart review would be useful, a slot is open at https://meetings.hubspot.com/nick-omelchak

Nick

### Katie Kermode · Medical Director · lane medical · P2 · `katie-kermode-md-428495330`

**M1**

Hi Katie,

Spotted your background as an associate medical director before John Hancock. Where ExpressTrack decides a case without an exam, the weight on file is the declared one.

In the e-application, two photos produce a Smart Scales weight estimate from FitXpress, and a reviewer sees a flag only when the gap crosses a threshold John Hancock sets.

What would you want documented about a Smart Scales estimate's limits before your team uses it on any accelerated case?

Nick

**M2**

Hi Katie,

The limits are stated up front: Smart Scales returns an estimate with approximately 3.5% mean absolute error under evaluated conditions, not a scale reading. Any threshold would be John Hancock's to set, placed well above that.

FitXpress is not a medical device and does not make underwriting decisions.

If it is useful to go through the evaluation conditions together, my calendar is at https://meetings.hubspot.com/nick-omelchak

Nick

### Elaine Szewc · Assistant Chief Medical Director · lane medical · P2 · `elaine-szewc-80785530b`

**M1**

Hi Elaine,

Curious about your take on weight evidence where no exam happens at John Hancock. On an exam-free accelerated case, a declared weight stands alone on the file.

Our scan returns a weight estimate from Smart Scales after two photos in the e-application, with a flag only past the carrier's threshold.

What margin over the estimate's stated error would you want built into a referral threshold?

Nick

**M2**

Hi Elaine,

The error is stated and the decision boundary belongs to the carrier. The Smart Scales estimate carries approximately 3.5% mean absolute error under evaluated conditions, and it is not a scale reading; underwriters decide on any referral.

FitXpress is not a medical device and does not make underwriting decisions.

If the numbers are worth a conversation, you can find a time here: https://meetings.hubspot.com/nick-omelchak

Nick

### Sheila Macdonnell · AVP, Medical Director · lane medical · P2 · `sheila-macdonnell-a762b22b`

**M1**

Hi Sheila,

Quick one on build guidance at John Hancock. With no exam on an accelerated case, there is no exam weight to set a declared weight against.

On an exam-free case, FitXpress could take two photos and return a Smart Scales weight estimate in one timestamped record, with a flag if the carrier's threshold is passed.

How does John Hancock's build guidance treat a declared weight against an exam weight today?

Nick

**M2**

Hi Sheila,

The record adds evidence where an accelerated case has none, and the threshold, the guidance and the decision stay with John Hancock.

FitXpress is not a medical device and does not make underwriting decisions.

If your guidance on declared versus exam weight is a good place to start, a call is bookable at https://meetings.hubspot.com/nick-omelchak

Nick

### Christopher Lintecum · Assistant Vice President, Digital Operations - New Business · lane proposition · P2 · `christopherlintecum`

**M1**

Hi Christopher,

Wanted to reach out given your background as lead product owner for digital applications at John Hancock. Any step added to a digital application is judged on completion.

FitXpress is one such step: two photos return a Smart Scales weight estimate and a flag past the carrier's threshold.

How do you measure placement and drop-off when a step is added to the application?

Nick

**M2**

Hi Christopher,

Completion is the number that matters here. In an evaluation it is measured alongside the flags, with applicants who cannot scan staying on the standard application.

FitXpress is not a medical device and does not make underwriting decisions.

The steps from walkthrough to evidence comparison are laid out at https://3dlook.ai/for-insurance-underwriting/

To talk through placement and completion, a slot can be booked at https://meetings.hubspot.com/nick-omelchak

Nick

### Kevin Hill · VP, Product Management · lane proposition · P3 · `kevin-hill-2429849`

**M1**

Hi Kevin,

Couldn't help but ask how John Hancock's product team thinks about the JH eApp, the application behind ExpressTrack's exam-free route.

FitXpress would add one step: two photos in, a Smart Scales weight estimate out, and a flag reserved for gaps beyond the limit the carrier chooses.

Which application journey would your product team test a photo step in first?

Nick

**M2**

Hi Kevin,

Starting small is straightforward. One journey can try the step while the rest of the application stays as it is.

FitXpress is not a medical device and does not make underwriting decisions.

For a product view of the step, see https://3dlook.ai/for-insurance-underwriting/

For a short conversation on where to test first, book here: https://meetings.hubspot.com/nick-omelchak

Nick

## Principal Financial (13)

### Frank Mikalonis · Regional Vice President- Disability Income · lane referral · P3 · `frank-mikalonis-594b3816`

**M1**

Hi Frank,

Thought I'd share a point about the business owners you work with. Principal's accelerated route has no exam for qualified clients, and the build on file is the height and weight the client declares.

FitXpress puts two photos into the application and returns a Smart Scales weight estimate and BMI from the declared height, with a flag past a threshold Principal sets.

When owners ask you about accelerated underwriting, which application step do they ask about first?

Nick

**M2**

Hi Frank,

A short walkthrough shows where the step sits. Principal decides where it is offered, and clients who prefer not to scan stay on the usual route.

FitXpress is not a medical device and does not make underwriting decisions.

Happy to be pointed to whoever owns Principal's accelerated underwriting rules if they are a better home for owner questions.

If owners' questions about steps are useful to you, a walkthrough can be booked here: https://meetings.hubspot.com/nick-omelchak

Nick

### Michele Ramsey · AVP - Chief Privacy Officer · lane technical-integration · P3 · `michele-ramsey-cipp-us-814877a`

**M1**

Hi Michele,

Couldn't help but ask, given your background in privacy and AI governance. A new evidence step in the application is a data-handling question first.

FitXpress takes two photos through an SDK and returns a weight estimate from Smart Scales, BMI from the declared height and a flag past a threshold Principal sets, with scan records on random identifiers.

What does Principal's privacy review ask of a new photo-based step?

Nick

**M2**

Hi Michele,

TLS in transit, S3-managed encryption at rest, photos deleted after processing or within 30 days per the carrier's policy, retained photos blurred, faces obscured at capture.

FitXpress is not a medical device and does not make underwriting decisions.

The handling answers are written out at https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/

If a call on photo handling would help the review, a slot can be booked at https://meetings.hubspot.com/nick-omelchak

Nick

### Terry Huisman · Regional Chief Underwriter · lane underwriting · P2 · `terry-huisman-91231b48`

**M1**

Hi Terry,

Wanted to reach out given your brokerage underwriting background before Principal. For qualified clients, an online application or interview is all the accelerated route takes, with no exam.

FitXpress would add two photos there and return a Smart Scales weight estimate, BMI from the declared height and a flag when the gap passes a threshold Principal sets.

On the online route, where would a gap between declared and estimated weight move a client into a different class?

Nick

**M2**

Hi Terry,

A flag is set above the estimate's error and refers only the gaps that would change class.

FitXpress is not a medical device and does not make underwriting decisions.

How the flag sits against a build chart is shown at https://3dlook.ai/for-insurance-underwriting/

If the regional build chart is where this matters, I can go through it with you here: https://meetings.hubspot.com/nick-omelchak

Nick

### Josh Heidemann · Assistant Chief Underwriter · lane underwriting · P2 · `josh-heidemann-6a89a34`

**M1**

Hi Josh,

Had a thought after seeing your years in technical underwriting and consulting at Principal. Qualified clients there can go through an online application or interview alone.

Our scan, FitXpress, returns a Smart Scales weight estimate from two photos, and its timestamped record carries a flag past Principal's threshold.

What does the accelerated route rely on for build when no exam happens?

Nick

**M2**

Hi Josh,

On a file with no exam, a reviewer gets the declared and estimated values together, with Principal's threshold on record.

FitXpress is not a medical device and does not make underwriting decisions.

To see how that record reads on a case, we can set a call here: https://meetings.hubspot.com/nick-omelchak

Nick

### Cody Schiffer · Assistant Chief Underwriter · lane underwriting · P2 · `cody-schiffer-falu-flmi-53b84385`

**M1**

Hi Cody,

This stood out: your technical underwriting director background at Principal. The online application route has no exam or lab requirement for qualified clients.

Two photos on that route give FitXpress what it needs for a Smart Scales weight estimate and a flag when Principal's own threshold is exceeded.

What would a shadow evaluation have to show you first?

Nick

**M2**

Hi Cody,

A shadow evaluation keeps outputs out of decisions while flags are counted and compared with build from exam cases.

FitXpress is not a medical device and does not make underwriting decisions.

The path from walkthrough to comparison is described at https://3dlook.ai/for-insurance-underwriting/

If sign-off criteria are the first thing to settle, we can talk it through here: https://meetings.hubspot.com/nick-omelchak

Nick

### Bob Herman · Disability Income Regional Vice President · lane referral · P3 · `hermanbob`

**M1**

Hi Bob,

Made me think about the key employees you meet through Principal Business Solutions. For qualified clients the accelerated route needs no exam.

FitXpress adds a short step to the application: two photos in, and a Smart Scales weight estimate and a threshold flag out.

When key employees ask about a new application step, what do they want to know first?

Nick

**M2**

Hi Bob,

What advisors tell clients is short: Principal decides where the step is offered, and clients who would rather not scan stay on the usual application.

FitXpress is not a medical device and does not make underwriting decisions.

If the new-business journey is the better home for this, a name is welcome.

To go through what advisors would tell key employees, grab a time here: https://meetings.hubspot.com/nick-omelchak

Nick

### Nate Berns · AVP & Chief Underwriter Life · lane underwriting · P2 · `nate-berns-61472a216`

**M1**

Hi Nate,

Quick note on Principal's in-house accelerated model for business owners and key employees. Where qualified clients need no exam, the file carries the height and weight the applicant enters.

Two photos in FitXpress return a Smart Scales weight estimate, and a flag marks only the cases above a threshold Principal sets.

On owner and key-employee cases, is the build chart line the same as on the rest of accelerated business?

Nick

**M2**

Hi Nate,

For owner cases the record is one extra entry on the file, and the threshold and the underwriter's decision stay Principal's.

FitXpress is not a medical device and does not make underwriting decisions.

How the record sits on an accelerated case is shown at https://3dlook.ai/for-insurance-underwriting/

If owner and key-employee cases are the place to try this, a call is easy to set up here: https://meetings.hubspot.com/nick-omelchak

Nick

### Kris Vanderkooy · Chief Medical Director · lane medical · P1 · `kris-vanderkooy-md-dbim-flmi-aa751b122`

**M1**

Hi Kris,

Noticed your background in medical direction before Principal. For qualified clients, the accelerated route needs an online application or interview and no exam; the weight on file is the declared one.

FitXpress adds two photos and returns a Smart Scales weight estimate, with a flag only when the gap crosses a threshold Principal sets.

Which limits of a Smart Scales estimate would you want written down before Principal considers it for accelerated cases?

Nick

**M2**

Hi Kris,

The limits are stated: Smart Scales gives approximately 3.5% mean absolute error under evaluated conditions, not a scale reading. Principal sets the threshold, and a case is referred only when the gap is larger than the estimate's error.

FitXpress is not a medical device and does not make underwriting decisions.

If the evaluation conditions are the right place to begin, I can walk through them: https://meetings.hubspot.com/nick-omelchak

Nick

### Marian Coffey · Disability Income Regional Vice President · lane referral · P3 · `mariancoffey`

**M1**

Hi Marian,

Curious about your view from years as a disability income regional VP at Principal. For DI, the Online Part B is completed by the client.

FitXpress could sit beside that step: two photos give a Smart Scales weight estimate and a flag on cases beyond a threshold Principal sets.

Which part of the Online Part B do advisors raise with you most?

Nick

**M2**

Hi Marian,

The client's own part of the DI application is a natural home for a step like this, and Principal decides if and where it is offered.

FitXpress is not a medical device and does not make underwriting decisions.

If the Online Part B sits elsewhere in Principal, tell me who looks after it.

To compare notes on what advisors raise about Part B, pick a slot here: https://meetings.hubspot.com/nick-omelchak

Nick

### Mike Sir · Disability Income Regional VP · lane referral · P3 · `mike-sir-84b7b610`

**M1**

Hi Mike,

Got me thinking about DI applications in your region at Principal. The Online Part B there is completed by the client.

On the client's side of the application, FitXpress takes two photos and returns a Smart Scales weight estimate and a timestamped record, with a flag past a threshold Principal sets.

In your region, does the client's section of the application need fewer steps or more clarity?

Nick

**M2**

Hi Mike,

Adding anything to the DI client's section is Principal's design choice, with the threshold and the decisions staying with underwriting.

FitXpress is not a medical device and does not make underwriting decisions.

If whoever sets DI guidelines is a better fit, send me their way.

Here is my calendar if a short talk on DI applications would help: https://meetings.hubspot.com/nick-omelchak

Nick

### Jeff Kruger · AVP - Business Owner and Chief Underwriter · lane underwriting · P1 · `jeff-kruger-9a130b24`

**M1**

Hi Jeff,

Caught my eye that Principal has the client complete the Online Part B for disability income. Build there is the height and weight the client enters.

FitXpress would sit in that step: two photos return a weight estimate from Smart Scales, BMI from the declared height and one timestamped record, with a flag past a threshold Principal sets.

How do you treat build on DI differently from life?

Nick

**M2**

Hi Jeff,

On DI, the evaluation question is which gaps would change a class. A shadow evaluation tallies flags at the thresholds under test and compares them with build from exam cases, with outputs kept out of decisions.

FitXpress is not a medical device and does not make underwriting decisions.

If you want to compare notes on DI build, my calendar is at https://meetings.hubspot.com/nick-omelchak

Nick

### Heather Dawson · Head of Product Strategy, Income Solutions · lane proposition · P3 · `heatherdawson33`

**M1**

Hi Heather,

Spotted your background in workplace solutions and superannuation before Principal. For qualified clients, accelerated underwriting at Principal takes only an online application or interview.

Two photos in the application would allow FitXpress to return a Smart Scales weight estimate, with a flag reserved for cases past a threshold Principal sets.

How does Principal test a new application step with advisors before it goes live?

Nick

**M2**

Hi Heather,

Advisor testing can run in one channel first, with everyone else on the current application.

FitXpress is not a medical device and does not make underwriting decisions.

The product side of a test is described at https://3dlook.ai/for-insurance-underwriting/

If testing with advisors is on your list, a short call can map out the first channel: https://meetings.hubspot.com/nick-omelchak

Nick

### Bryant Fuller · MD, Head of Product for Individual Solutions · lane proposition · P3 · `bryantfuller`

**M1**

Hi Bryant,

Came across your work across wealth management and product strategy before Principal. For qualified clients, the online application route has no exam, and the build on file is declared.

FitXpress is a step with two photos, returning a Smart Scales weight estimate and flagging only what lies beyond a threshold Principal sets.

Where does an extra step cost the most in Principal's individual journey, and where the least?

Nick

**M2**

Hi Bryant,

Placement can be tested in one journey at a time, with Principal setting the threshold and everything else unchanged.

FitXpress is not a medical device and does not make underwriting decisions.

What a placement test covers is described at https://3dlook.ai/for-insurance-underwriting/

To pick the first journey to test, find a time here: https://meetings.hubspot.com/nick-omelchak

Nick

## Pacific Life (12)

### Jennifer Glessner · AVP Underwriting Transformation and Customer Journey · lane underwriting · P2 · `jenniferglessner`

**M1**

Hi Jennifer,

Quick thought on Pacific Life's PAL+, where an online health history can stand in for the phone interview. On a path with no exam after it, the declared height and weight carry build.

Two photos taken in the e-application become a Smart Scales weight estimate in FitXpress, and a flag is raised when the gap crosses the threshold Pacific Life sets. A timestamped record of it goes on the file.

When a flag like that fires, which class boundaries would it matter for?

Nick

**M2**

Hi Jennifer,

An evaluation could run in shadow, with each flag read beside build from PAL+ exam cases. Smart Scales shows approximately 3.5% mean absolute error under evaluated conditions and is not a scale reading, which places any referral line well above that error.

FitXpress is not a medical device and does not make underwriting decisions.

The evaluation steps are laid out at https://3dlook.ai/for-insurance-underwriting/

If a call on where such a flag matters is useful, book at https://meetings.hubspot.com/nick-omelchak

Nick

### Tee Sun · Assistant Vice President - New Business Model Development · lane referral · P3 · `teesun`

**M1**

Hi Tee,

Wanted to reach out about new business model development at Pacific Life. A neighbor of that work is the accelerated path, which carries no paramedical exam.

FitXpress adds a step to the e-application: two photos return a Smart Scales weight estimate, flagged above a threshold Pacific Life sets.

When a new evidence step comes up in your area, who at Pacific Life usually gets pulled in first?

Nick

**M2**

Hi Tee,

The shape is a shadow evaluation: flags counted beside live files, one timestamped record per applicant, nothing reaching a decision.

FitXpress is not a medical device and does not make underwriting decisions.

Pointing me to whoever owns underwriting rules at Pacific Life works just as well.

If a quick call on where this could land is easier, the calendar is at https://meetings.hubspot.com/nick-omelchak

Nick

### TJ Doan · VP, Head of Underwriting Operations and Assistant Chief Underwriter · lane underwriting · P2 · `tj-doan-a8042597`

**M1**

Hi TJ,

Noticed that PAL+ routes each application to the least invasive method. The accelerated path carries no paramedical exam, and build there rests on the height and weight the applicant enters.

FitXpress is two photos in the e-application. The weight estimate is marked for referral if it departs from the declared figure by more than a threshold Pacific Life sets, and BMI is calculated from the declared height.

When an application lands on the accelerated route, what happens with build in operations?

Nick

**M2**

Hi TJ,

A shadow run would allow operations to watch the flags beside live files while underwriters decide exactly as they do now. Each applicant gets one timestamped record.

FitXpress is not a medical device and does not make underwriting decisions.

Booking a call to walk through PAL+ routing takes one click at https://meetings.hubspot.com/nick-omelchak

Nick

### Christopher Hall · Chief Privacy Officer · lane technical-integration · P3 · `christopher-hall-898635277`

**M1**

Hi Christopher,

Couldn't help but ask what privacy review looks like when Pacific Life adds two photos to an e-application.

FitXpress returns a Smart Scales weight estimate with a flag at the carrier's threshold, as one timestamped record.

Which documents does your team ask for first when a new vendor touches applicant data?

Nick

**M2**

Hi Christopher,

Handling: TLS in transit, S3-managed encryption at rest, photos deleted after processing or within 30 days per the carrier's policy. Retained photos are blurred, faces are obscured at capture, and scan records sit on random identifiers.

FitXpress is not a medical device and does not make underwriting decisions.

Documents go through legal@3dlook.me. To walk through the review path live, book at https://meetings.hubspot.com/nick-omelchak

Nick

### Ernest Armijos · AVP Life Pricing · lane proposition · P2 · `ernest-armijos-270aa9378`

**M1**

Hi Ernest,

Got me thinking about PAL+: its modified path rests on a recent physical with labs, which gives a measured weight, and the accelerated path has none.

With FitXpress the applicant takes two photos in the e-application, and a Smart Scales weight estimate comes back flagged only above a threshold Pacific Life sets.

How does life pricing think about the value of a build signal on files that carry no measured weight?

Nick

**M2**

Hi Ernest,

The evaluation would report how often the flag fires and how completion goes, which gives pricing real counts to work from.

FitXpress is not a medical device and does not make underwriting decisions.

If this sits elsewhere, tell me who owns the new-business journey.

To go through how pricing would read those counts, my calendar is at https://meetings.hubspot.com/nick-omelchak

Nick

### Alan Bub · Chief Technology Officer · lane technical-integration · P3 · `alanbub`

**M1**

Hi Alan,

Made me think: Pacific Life's PAL+ routes each application to the least invasive method. A new evidence step would need a place in that routing.

FitXpress comes as web and mobile SDKs and a REST API: two photos go in, and one timestamped record with a Smart Scales weight estimate and a threshold flag comes back.

Where would an SDK step slot into the e-application you run?

Nick

**M2**

Hi Alan,

Integration is a REST API call or the SDKs, with the record handed to the underwriting workbench or case system of Pacific Life's choosing.

FitXpress is not a medical device and does not make underwriting decisions.

An architecture call on the SDK step can be booked at https://meetings.hubspot.com/nick-omelchak

Nick

### Victoria Liu · AVP Life Product Strategy, Product Development · lane proposition · P2 · `victoria-liu-fsa-fcia-98519a14`

**M1**

Hi Victoria,

Spotted that Pacific Life's accelerated route is where the buying experience gets shortest, which makes every added step visible.

At a step the carrier picks, FitXpress takes two photos. A Smart Scales weight estimate follows, with a flag only when the gap crosses Pacific Life's threshold.

Where in the journey would a photo step meet the least pushback from applicants?

Nick

**M2**

Hi Victoria,

Placement is the carrier's choice, and the evaluation would watch completion before any rollout. Anyone who skips the scan stays on the usual route.

FitXpress is not a medical device and does not make underwriting decisions.

A product overview built for insurance teams is at https://3dlook.ai/for-insurance-underwriting/

If the agent channel owns this, send me to that lead.

Happy to discuss journey placement on a call via https://meetings.hubspot.com/nick-omelchak

Nick

### Mark Vincent · Medical Director · lane medical · P2 · `mark-vincent-0946a624`

**M1**

Hi Mark,

Curious about your view on Pacific Life's PAL+ cases that take the accelerated path: with no recent physical, weight comes from the declared figure.

The FitXpress scan returns a Smart Scales weight estimate from two photos, with a flag raised only for a gap above a threshold the carrier sets.

Which parts of an evaluation would make a weight estimate credible for medical review on those cases?

Nick

**M2**

Hi Mark,

The estimate carries approximately 3.5% mean absolute error under evaluated conditions and is not a scale reading. That error is the floor for any referral line, and the line itself stays with Pacific Life's underwriters.

FitXpress is not a medical device and does not make underwriting decisions.

A call to go through the error figure and the decision boundary is open at https://meetings.hubspot.com/nick-omelchak

Nick

### John Dieck · Senior Vice President & Chief Product Officer - Consumer Markets Division · lane proposition · P2 · `john-dieck-a2310036`

**M1**

Hi John,

This stood out: Pacific Life's Consumer Markets Division is where the application has to feel short.

The Smart Scales weight estimate in FitXpress arrives from two photos, and a flag is raised only above a threshold the carrier sets.

How would your team test a new step like that before it reaches every applicant?

Nick

**M2**

Hi John,

Speed is the point for a consumer division. The scan itself is under 45 seconds from the photos to structured results. Anyone who declines the scan carries on as before.

FitXpress is not a medical device and does not make underwriting decisions.

If testing the step on a small slice of applicants is worth discussing, a time is free at https://meetings.hubspot.com/nick-omelchak

Nick

### David McNamara · AVP, Life New Business · lane proposition · P2 · `david-mcnamara-jd-cfp%c2%ae-5b584912`

**M1**

Hi David,

Came across your background in advanced markets underwriting, which sits close to new-business intake at Pacific Life.

Inside the e-application, FitXpress takes two photos and returns a Smart Scales weight estimate with a flag at a threshold Pacific Life sets.

If the agent hands an application to the applicant to finish, how would you tell whether a photo step costs completions?

Nick

**M2**

Hi David,

Completion is what an evaluation would measure first, giving new business a read on drop-off before any wider rollout. One timestamped record per applicant goes back to the carrier.

FitXpress is not a medical device and does not make underwriting decisions.

What the scan returns for each applicant is described at https://3dlook.ai/for-insurance-underwriting/

A short call on measuring completion in new business is easy to book at https://meetings.hubspot.com/nick-omelchak

Nick

### Tristan Fontugne · Head of Product R&D and Analytics - Consumer Markets Division · lane proposition · P2 · `tristan-fontugne-5477b89`

**M1**

Hi Tristan,

Had a thought on analytics in Consumer Markets: PAL+ sends applications down different paths, and the accelerated one carries no measured weight.

FitXpress turns two photos from the e-application into a weight estimate. Only a departure beyond a threshold Pacific Life sets raises a flag.

Which comparisons across PAL+ paths would show whether a flag carries information?

Nick

**M2**

Hi Tristan,

The analysis is a table: flag rates by threshold on one axis and agreement with exam-based build on the other, limited to accelerated cases.

FitXpress is not a medical device and does not make underwriting decisions.

A pointer to the pricing actuaries is welcome if the table is theirs.

Sketching that table together takes one booking at https://meetings.hubspot.com/nick-omelchak

Nick

### Matt Winegar · AVP Actuary, New Business Repricing & Regulatory · lane proposition · P3 · `matt-winegar-68303421`

**M1**

Hi Matt,

Caught my eye: new business repricing at Pacific Life, and the evidence that comes in at application on accelerated cases.

What we built, FitXpress, takes two photos in the e-application and returns a Smart Scales weight estimate. A flag is raised above a threshold the carrier sets.

What would a repricing review want to see from an evaluation before treating that flag as evidence?

Nick

**M2**

Hi Matt,

Case by case, an evaluation would show how often the flag fires and how it lines up with exam-based build. Repricing would then have counts to weigh.

FitXpress is not a medical device and does not make underwriting decisions.

The overview aimed at insurers is at https://3dlook.ai/for-insurance-underwriting/

If this belongs with the actuary who owns evidence assumptions, tell me who that is.

Time to talk through what repricing would need is open at https://meetings.hubspot.com/nick-omelchak

Nick

## Protective Life (12)

### Alex Crawford · AVP Underwriting at Protective Life · lane underwriting · P2 · `alex-crawford-17205223`

**M1**

Hi Alex,

Caught my eye: your career in life underwriting. Protective Life said 2025 measures improved cycle times on accelerated work.

With two photos from the e-application, FitXpress returns a weight estimate and a flag, raised when the gap crosses a threshold Protective sets.

How large would a gap need to be before an underwriter wanted a second look at the file?

Nick

**M2**

Hi Alex,

In a shadow set, an underwriter could read the timestamped record next to the declared figures. The weight estimate has approximately 3.5% mean absolute error under evaluated conditions and is not a scale reading; only gaps well beyond that error are worth a look.

FitXpress is not a medical device and does not make underwriting decisions.

If another underwriting VP should see it first, send me their way.

I can share the evaluation design on a call; availability is listed at https://meetings.hubspot.com/nick-omelchak

Nick

### Shawn Fourez · Vice President of Underwriting · lane underwriting · P2 · `shawn-fourez-72628142`

**M1**

Hi Shawn,

Saw the news from January that 2025 work expanded accelerated underwriting ages and face amounts at Protective Life. A wider route raises the question of how build is handled when no exam happens.

The FitXpress scan is two photos in the e-application. Smart Scales returns a weight estimate, flagged only above a threshold Protective sets.

As the route widens, what does the underwriting team lean on for build when no exam is ordered?

Nick

**M2**

Hi Shawn,

For a widening route, the comparison to run is flag rates against build from exam cases, limited to accelerated files. FitXpress returns a timestamped record for each applicant.

FitXpress is not a medical device and does not make underwriting decisions.

Details on what the record contains are at https://3dlook.ai/for-insurance-underwriting/

A conversation on how that comparison would run is open at https://meetings.hubspot.com/nick-omelchak

Nick

### Stephen Lininger · 2nd Vice President, Underwriting · lane underwriting · P2 · `stephen-lininger-392aa332`

**M1**

Hi Stephen,

Got me thinking about the files that clear Velocity: they qualify on height and weight within a healthy build chart at Protective Life.

FitXpress takes two photos in the e-application and returns a Smart Scales weight estimate. Protective sets the threshold, and a flag appears only above it.

What would your team want a shadow evaluation to demonstrate before any flag touches a case file?

Nick

**M2**

Hi Stephen,

The scan would run beside live files and leave decisions with underwriters. Each applicant gets one timestamped record, and the flag counts show how often a gap crosses a given line.

FitXpress is not a medical device and does not make underwriting decisions.

If scoping sits elsewhere, tell me who sets it.

If you want to shape the evaluation together, the calendar is at https://meetings.hubspot.com/nick-omelchak

Nick

### Mark Barnum · 2nd Vice President Underwriting · lane underwriting · P2 · `mark-barnum-b3041619`

**M1**

Hi Mark,

Had a thought on Protective Life's note that accelerated work continues in 2026. For files built on declared height and weight, a second source could sit beside them.

With FitXpress the applicant takes two photos in the e-application, and a Smart Scales weight estimate follows, flagged at a threshold Protective sets.

On a file, where would an underwriter expect a timestamped record like that, beside the interview answers or in a separate view?

Nick

**M2**

Hi Mark,

On the file it is one record: the photos from the e-application, the weight estimate and whether the gap crossed the threshold. Nothing else about the case changes, and underwriters decide as before.

FitXpress is not a medical device and does not make underwriting decisions.

If a call on where the record should show suits you, book at https://meetings.hubspot.com/nick-omelchak

Nick

### Brad Gabel · Vice President and Chief Underwriting Officer · lane underwriting · P1 · `bradgabel`

**M1**

Hi Brad,

Noticed your time as president of AHOU. Protective Life's Velocity checklist asks for height and weight within a healthy build chart.

Two photos in the e-application become a Smart Scales weight estimate in FitXpress, and a flag is raised when the gap crosses a threshold Protective sets.

Where would a gap between declared and estimated weight start to change a class on those files?

Nick

**M2**

Hi Brad,

Smart Scales shows approximately 3.5% mean absolute error under evaluated conditions and is not a scale reading, which places any referral line well above that error. A shadow run would count flags next to exam-based build.

FitXpress is not a medical device and does not make underwriting decisions.

The evaluation outline for underwriting teams is at https://3dlook.ai/for-insurance-underwriting/

A call to design the shadow run around Velocity files can be booked at https://meetings.hubspot.com/nick-omelchak

Nick

### Frances Freeman · 2nd Vice President, New Business Operations · lane proposition · P3 · `frances-freeman-69582136`

**M1**

Hi Frances,

Wanted to reach out about new business operations at Protective Life. On accelerated cases no paramedical exam is ordered, which leaves the declared height and weight as the build input.

Our FitXpress scan asks the applicant for two photos in the e-application. A weight estimate comes back, flagged only above a threshold Protective sets.

What happens in intake when the declared figures are the only build information on a file?

Nick

**M2**

Hi Frances,

Intake would not change at first. An evaluation runs beside live files, with each applicant getting one timestamped record.

FitXpress is not a medical device and does not make underwriting decisions.

Pointing me to whoever owns underwriting rules works too.

Times for a quick call about intake handling are open at https://meetings.hubspot.com/nick-omelchak

Nick

### Justin Allen · Chief Information Security Officer · lane technical-integration · P3 · `justintallen`

**M1**

Hi Justin,

Came across your work in cloud security engineering and attack surface reduction. At Protective Life, Online Part II opens from a personalized link. Any new step in that journey goes through security review.

FitXpress asks for two photos at that step and returns a Smart Scales weight estimate with a threshold flag, as one timestamped record delivered to Protective.

What does a first-pass security review ask a vendor to show?

Nick

**M2**

Hi Justin,

Handling: TLS in transit, S3-managed encryption at rest, photos deleted after processing or within 30 days per the carrier's policy, retained photos blurred, faces obscured at capture. Scan records use random identifiers.

FitXpress is not a medical device and does not make underwriting decisions.

Integration runs on a REST API and SDKs, and documents go through legal@3dlook.me. For a review call, pick a time at https://meetings.hubspot.com/nick-omelchak

Nick

### Lindsay Hackney · Vice President, Life Product Strategy · lane proposition · P2 · `lindsayhackney`

**M1**

Hi Lindsay,

Quick idea for you, prompted by your early work in customer authentication. Online Part II at Protective Life collects height and weight among its first disclosures.

FitXpress puts two photos into the e-application. The Smart Scales weight estimate comes with a flag, raised only above a threshold Protective sets.

What would you test first to see whether a photo step helps or hurts term applications?

Nick

**M2**

Hi Lindsay,

Product would choose the placement, and an evaluation would show completion before any rollout. The scan returns one timestamped record per applicant.

FitXpress is not a medical device and does not make underwriting decisions.

How the scan fits into an e-application is covered at https://3dlook.ai/for-insurance-underwriting/

To discuss testing term applications on a call, grab a time at https://meetings.hubspot.com/nick-omelchak

Nick

### Jamie Lane · Vice President Head of New Business Operations and Enterprise Shared Services · lane proposition · P2 · `jamie-lane-4b923091`

**M1**

Hi Jamie,

Spotted something in how Protective Life's Online Part II starts: applicants open the interview from a personalized link. Height and weight come early in it.

FitXpress could be two photos taken in the e-application, returning a Smart Scales weight estimate and a flag above a threshold Protective sets.

Which moment in that journey would be the smoothest for a photo step?

Nick

**M2**

Hi Jamie,

Placement is the open point, and the carrier picks it. A test on a small slice would show how applicants move through the step.

FitXpress is not a medical device and does not make underwriting decisions.

The page describing the scan for accelerated programs is at https://3dlook.ai/for-insurance-underwriting/

Talking placement through takes a booking at https://meetings.hubspot.com/nick-omelchak

Nick

### Susan Sucha · Medical Director · lane medical · P2 · `susan-sucha-219b9016a`

**M1**

Hi Susan,

Curious about your take: Protective Life's accelerated checklist ties eligibility to a healthy build chart, with height and weight as the inputs.

In the e-application FitXpress asks the applicant for two photos. A Smart Scales weight estimate comes back, and a flag is raised only for a gap above a threshold Protective sets.

When guidance compares a declared weight with an exam weight, which differences count as meaningful?

Nick

**M2**

Hi Susan,

The estimate has approximately 3.5% mean absolute error under evaluated conditions and is not a scale reading. A medical reviewer would set any referral line well beyond it, with the decision boundary kept with underwriters.

FitXpress is not a medical device and does not make underwriting decisions.

Setting up a call on the error figure is possible at https://meetings.hubspot.com/nick-omelchak

Nick

### Kenneth Byrd · VP, Head of Protection New Business Operations · lane proposition · P1 · `kennethbyrd`

**M1**

Hi Kenneth,

This stood out: Protective Life's Online Part II has applicants complete required disclosures first, height and weight among them. That makes it a place worth examining for a photo step.

What we built, FitXpress, is two photos inside that flow, answered by a Smart Scales weight estimate and a flag above a threshold Protective sets.

How does operations measure completion when a step is added to that flow?

Nick

**M2**

Hi Kenneth,

Completion is the first thing to measure. An evaluation on a sample would show it before any wider rollout.

FitXpress is not a medical device and does not make underwriting decisions.

A look at what the record holds is at https://3dlook.ai/for-insurance-underwriting/

To plan the completion measurement together, you will find times at https://meetings.hubspot.com/nick-omelchak

Nick

### Russell Kolmin · SVP, Chief Product Officer - Protection Division · lane proposition · P2 · `russell-kolmin`

**M1**

Hi Russell,

Couldn't help but ask, given your years in life pricing. Protective Life's term application starts with required disclosures, height and weight among them.

FitXpress uses two photos from the e-application to produce a Smart Scales weight estimate, with a flag only above a threshold Protective sets.

What would an additional build signal have to deliver to justify itself in term pricing?

Nick

**M2**

Hi Russell,

An evaluation would count how often the flag fires on accelerated term files and compare that with exam-based build, showing pricing what the additional record adds.

FitXpress is not a medical device and does not make underwriting decisions.

To talk through what pricing would measure, pick any open time at https://meetings.hubspot.com/nick-omelchak

Nick

## Ameritas (12)

### Keith Beckman · Managing Director, Individual Life Underwriting · lane underwriting · P2 · `keith-beckman-flmi-falu-a6592677`

**M1**

Hi Keith,

Ameritas accelerates eligible individual life cases, and those files rest on the applicant's declared height and weight.

FitXpress returns a Smart Scales weight estimate from two photos, with a flag only when it departs from the declared weight by more than Ameritas's threshold.

How is build reviewed on an accelerated file at Ameritas?

Nick

**M2**

Hi Keith,

A shadow evaluation counts flags at each candidate threshold and sets them against build from paramedical exam cases. Nothing reaches a case during it. FitXpress is not a medical device and does not make underwriting decisions.

I can lay out the evaluation design if you pick a time: https://meetings.hubspot.com/nick-omelchak

Nick

### Al Barth · Director Life Underwriting · lane underwriting · P2 · `al-barth-a486292a`

**M1**

Hi Al,

Ameritas describes a consistent approach to underwriting decisions. On accelerated cases, a dated record of build would support that.

Two photos through FitXpress produce a timestamped record of a Smart Scales weight estimate and BMI from the declared height. A flag shows only when the gap to the declared weight crosses Ameritas's threshold.

Where do you see a documented build record helping an underwriter most?

Nick

**M2**

Hi Al,

The evaluation would set the flag beside build from exam cases, with no effect on any decision. FitXpress is not a medical device and does not make underwriting decisions.

The page at https://3dlook.ai/for-insurance-underwriting/ shows what the dated record contains.

I would like to hear where a dated build record helps most, at a time that suits you: https://meetings.hubspot.com/nick-omelchak

Nick

### Beverley Sloley · Director of Underwriting · lane underwriting · P2 · `beverley-sloley-flmi-mba-ba112027`

**M1**

Hi Beverley,

Consistency across underwriters is part of how Ameritas describes its approach to decisions, and build is one input on accelerated cases.

FitXpress adds a step of two photos that records a Smart Scales weight estimate, timestamped, and flags it against Ameritas's threshold for gaps to the declared weight.

When two underwriters read the same accelerated file, what keeps the build read identical?

Nick

**M2**

Hi Beverley,

The record would put the flag, the threshold and the time on the file. If Ameritas runs random holdouts, they show how those flags line up with build gathered separately. FitXpress is not a medical device and does not make underwriting decisions.

If you would like to see how that fits your review practice, the calendar is here: https://meetings.hubspot.com/nick-omelchak

Nick

### Daniel Buchholz · Managing Director, Underwriting · lane underwriting · P2 · `daniel-dan-buchholz-certified-falu-clu-flmi-acs-3613a216`

**M1**

Hi Daniel,

Financial professionals at Ameritas get direct access to the underwriter.

On an accelerated file, two photos through FitXpress give the underwriter a Smart Scales weight estimate beside the declared weight, flagged only past Ameritas's threshold.

What would your team want to see from a shadow evaluation before the flag reached an underwriter's desk?

Nick

**M2**

Hi Daniel,

The first read-out would be counts only, with nothing sent to a decision. FitXpress is not a medical device and does not make underwriting decisions.

An analyst who would run the numbers could join instead.

I can sketch the read-out on a call if that is useful: https://meetings.hubspot.com/nick-omelchak

Nick

### Scott Delisi · Vice President - Disability Income Distributions · lane referral · P3 · `scott-delisi-4a855b7`

**M1**

Hi Scott,

DI distribution sits between advisors and the Ameritas application.

FitXpress adds two photos to a DI application and returns a Smart Scales weight estimate with a flag where it differs from the declared weight past the carrier's threshold.

How do advisors you work with usually respond when a form gains a step?

Nick

**M2**

Hi Scott,

What advisors say is what the evaluation would capture first, as completion with and without the step. FitXpress is not a medical device and does not make underwriting decisions.

A plain description of the step for advisors sits at https://3dlook.ai/for-insurance-underwriting/ if useful.

Whoever owns DI underwriting rules or the new-business journey is welcome to take this over, and a pointer from you would do it.

A call could cover what advisors would see in the step: https://meetings.hubspot.com/nick-omelchak

Nick

### Pete Kaczmar · Director - Underwriting National Accounts & National Partners · lane underwriting · P3 · `pete-kaczmar-78a6816`

**M1**

Hi Pete,

Your remit at Ameritas is national accounts and partners. If that includes individual life, accelerated cases from partner firms go through the same e-application.

Through FitXpress, two photos return a Smart Scales weight estimate, and a flag marks cases where it departs from the declared weight by more than Ameritas's threshold.

Which partner firms submit accelerated individual cases today?

Nick

**M2**

Hi Pete,

A partner firm's cases could be the place to start, in a read-only run beside live cases that sends nothing to a decision. FitXpress is not a medical device and does not make underwriting decisions.

How a partner firm's cases would be covered is described at https://3dlook.ai/for-insurance-underwriting/ in more detail.

If individual life channels sit under someone else, route me to them.

Comparing notes on partner cases in a call would be useful, and my calendar is open: https://meetings.hubspot.com/nick-omelchak

Nick

### Kyle O'Donnell · Vice President, Life Product Development · lane proposition · P2 · `kyle-o-donnell-a7b9918`

**M1**

Hi Kyle,

Life product design at Ameritas decides what the application asks of an applicant.

A step of two photos would give the file a Smart Scales weight estimate and a flag at Ameritas's threshold, inside FitXpress's timestamped record.

How do you try out a new application step with distribution before it reaches a form?

Nick

**M2**

Hi Kyle,

Distribution partners would take the step beside live cases, with completion measured and nothing sent to a decision. FitXpress is not a medical device and does not make underwriting decisions.

Should distribution testing run through another team, forward me their way.

I will bring a testing outline to a call if that would help: https://meetings.hubspot.com/nick-omelchak

Nick

### Lynn Saddoris · Director, Product Management, Underwriting & Exchange Solutions · lane proposition · P3 · `lynn-saddoris-mba-b188749`

**M1**

Hi Lynn,

Product management for underwriting solutions at Ameritas means judging each evidence input on what it adds to the application.

A FitXpress step of two photos returns a timestamped Smart Scales weight estimate and a flag only past the carrier's threshold, with BMI from the declared height.

How would you measure drop-off and placement once a step like that is in?

Nick

**M2**

Hi Lynn,

Completion would be read inside the evaluation, and the record returns to Ameritas's systems only. FitXpress is not a medical device and does not make underwriting decisions.

Whoever owns the e-application roadmap may be the better reader, and an introduction would help.

I can walk through how completion is read on a call: https://meetings.hubspot.com/nick-omelchak

Nick

### Scott Corbett · Vice President and Chief Underwriter · lane underwriting · P2 · `scott-corbett-6b32469`

**M1**

Hi Scott,

Eligible cases can go through accelerated underwriting at Ameritas.

FitXpress returns one timestamped record from two photos: a Smart Scales weight estimate and a flag where it departs from the declared weight by more than your build line.

Does build get weighed differently on DI than on life in your accelerated rules?

Nick

**M2**

Hi Scott,

On DI the record serves documentation as one dated entry. On life the same entry sits on cases without a paramedical exam. FitXpress is not a medical device and does not make underwriting decisions.

A call would allow me to show both entries side by side: https://meetings.hubspot.com/nick-omelchak

Nick

### Timothy Steffen · Vice President and Medical Director · lane medical · P1 · `timothy-steffen-md-dbim-469092256`

**M1**

Hi Timothy,

Where Ameritas accelerates an eligible case, the build in the file is the height and weight the applicant enters.

FitXpress takes two photos in the e-application and returns a Smart Scales weight estimate, with a flag only when the gap to the declared weight crosses a threshold your team sets.

What would your sign-off look like for a software weight estimate that only triggers a referral?

Nick

**M2**

Hi Timothy,

Smart Scales has approximately 3.5% mean absolute error under evaluated conditions and is not a scale reading. Any referral threshold would sit well above that error, and Ameritas sets it. FitXpress is not a medical device and does not make underwriting decisions.

If it helps your sign-off thinking, I can go through the boundary at a time you choose: https://meetings.hubspot.com/nick-omelchak

Nick

### Michelle Visconti · 2nd VP, Individual Underwriting Operations · lane underwriting · P2 · `michelle-visconti-44752189`

**M1**

Hi Michelle,

Ameritas takes electronic applications, and intake data reaches underwriting operations first.

FitXpress would send back a timestamped record with a Smart Scales weight estimate from two photos, flagged when it differs from the declared weight beyond Ameritas's threshold.

Where would a flag like that need to show up for operations to route the file?

Nick

**M2**

Hi Michelle,

The record returns as structured data and a flag can appear as a field in the existing queue. FitXpress is not a medical device and does not make underwriting decisions.

What the record carries for operations is laid out at https://3dlook.ai/for-insurance-underwriting/ for anyone who wants it.

If the intake queue belongs to another team, tell me whom to ask.

I can show the field layout in a call whenever operations has a free slot: https://meetings.hubspot.com/nick-omelchak

Nick

### Kelly Halverson · Executive Vice President, Individual Division · lane proposition · P1 · `kelly-halverson-2a8a467`

**M1**

Hi Kelly,

Electronic applications are where the individual division meets the applicant first.

FitXpress would add a step with two photos that returns a Smart Scales weight estimate and a flag when the gap to the declared weight crosses the carrier's threshold, on one timestamped record.

At which point in the application would you want to try a step like that first?

Nick

**M2**

Hi Kelly,

Completion follows effort. The scan returns 80+ body measurements, under 45 seconds from the photos to structured results.

An evaluation would read completion with the step offered, and nothing goes to a decision. FitXpress is not a medical device and does not make underwriting decisions.

Worth a call on how completion would be read in your journey: https://meetings.hubspot.com/nick-omelchak

Nick

## Guardian Life (11)

### Jennifer Black · VP, Underwriting · lane underwriting · P2 · `jennifer-black-b1034649`

**M1**

Hi Jennifer,

Health Advantage takes height and weight from a recent physical in the APS instead of an insurance exam. Accelerated cases without a physical have only the numbers the applicant enters.

Two photos in the e-application give FitXpress what it needs for a Smart Scales weight estimate, and a flag appears past Guardian's threshold.

What would a shadow evaluation have to show your team before any flag reached a case?

Nick

**M2**

Hi Jennifer,

The evaluation would run beside live cases, and its first report is flag counts per threshold, kept out of decisions. FitXpress is not a medical device and does not make underwriting decisions.

I am happy to share the report format on a call here: https://meetings.hubspot.com/nick-omelchak

Nick

### Robert Shourds · Head of Life Underwriting · lane underwriting · P1 · `robert-shourds-falu-flmi-7904aaa4`

**M1**

Hi Robert,

Guardian's accelerated underwriting for term, whole and universal life weighs the health questionnaire and other data in place of an exam. Height and weight are among what the applicant enters.

FitXpress adds two photos to the e-application and returns a Smart Scales weight estimate, flagged against Guardian's threshold when it differs from the declared weight.

Which step on an accelerated file puts build in front of the underwriter?

Nick

**M2**

Hi Robert,

A shadow evaluation counts flags at each candidate threshold, with nothing sent to a decision, and compares them with build from paramedical exam cases. FitXpress is not a medical device and does not make underwriting decisions.

The record layout is described at https://3dlook.ai/for-insurance-underwriting/ for the underwriting team.

I can take you through the evaluation design on a call: https://meetings.hubspot.com/nick-omelchak

Nick

### Greg Faux · Head of Life Product Development, Individual Life · lane proposition · P2 · `greg-faux-51396437`

**M1**

Hi Greg,

Guardian accelerates term, whole and universal life, and a step added to the application touches all three.

A FitXpress step takes two photos and returns a Smart Scales weight estimate with a flag past Guardian's threshold.

Which journey would you try it in first, the direct online one or the one with an agent?

Nick

**M2**

Hi Greg,

Completion is the product question, and a test group offered the step would answer it. FitXpress is not a medical device and does not make underwriting decisions.

I would bring a test-group outline to a call: https://meetings.hubspot.com/nick-omelchak

Nick

### Andy Gordon · Head of Individual Life Insurance · lane proposition · P2 · `andy-gordon-0b813423`

**M1**

Hi Andy,

Guardian's DI-to-Life certificate program reuses recent IDI underwriting. That puts DI and life applications on shared evidence.

FitXpress would add two photos to an application and return a Smart Scales weight estimate, flagged where it differs from the declared weight past the carrier's threshold.

How would you read drop-off on either application once a step is added?

Nick

**M2**

Hi Andy,

Either application has to stay short. The scan returns 80+ body measurements, under 45 seconds from the photos to structured results.

The evaluation would measure completion on each. FitXpress is not a medical device and does not make underwriting decisions.

The record on a DI file is shown at https://3dlook.ai/for-insurance-underwriting/ for reference.

If the DI application belongs to another team, tell me whom to ask.

Worth a call on how drop-off would be read on both: https://meetings.hubspot.com/nick-omelchak

Nick

### Anthony Perez · Vice President and Chief Underwriting Officer · lane underwriting · P2 · `anthony-perez-6083812a`

**M1**

Hi Anthony,

Guardian's no-medical-exam page describes accelerated underwriting built on the health questionnaire and other data.

The FitXpress step is two photos and a Smart Scales weight estimate, with a flag set against Guardian's own threshold.

Which gaps between declared and estimated weight would move a case from one class to another?

Nick

**M2**

Hi Anthony,

Agreement between the flag and build from paramedical exam cases is what the evaluation measures, with no effect on any decision. FitXpress is not a medical device and does not make underwriting decisions.

The agreement measure is easy to go through together, and a time can be picked here: https://meetings.hubspot.com/nick-omelchak

Nick

### Smitha Jagalur · Head of Life New Business and Underwriting Technology-IM New Business · lane technical-integration · P3 · `smitha-jagalur-b61b1a131`

**M1**

Hi Smitha,

Guardian's e-application is where life new business meets underwriting technology.

The FitXpress SDK puts a two-photo step inside it. A Smart Scales weight estimate and a flag past Guardian's threshold come back on one timestamped record.

How does a new SDK step enter an e-application release on your stack?

Nick

**M2**

Hi Smitha,

Integration is a REST API or web and mobile SDKs, and photos are deleted after processing or within 30 days per Guardian's policy. Scan records sit on random identifiers. FitXpress is not a medical device and does not make underwriting decisions.

If the SDK step should be mapped onto your release process, my calendar is open: https://meetings.hubspot.com/nick-omelchak

Nick

### Beth Denning · VP, Life Product Developement · lane proposition · P2 · `beth-denning-2a1706159`

**M1**

Hi Beth,

Term, whole and universal life each reach the same Guardian application. A step added there is a product decision.

Two photos through FitXpress return a Smart Scales weight estimate and a timestamped record, flagged past Guardian's threshold.

How do you gauge distribution's reaction to a new step before it ships?

Nick

**M2**

Hi Beth,

Completion across the three lines would be measured in the evaluation. FitXpress is not a medical device and does not make underwriting decisions.

Should distribution testing sit with someone else, an introduction would be welcome.

A call could cover how that measurement would work for you: https://meetings.hubspot.com/nick-omelchak

Nick

### Micah Pace · Head of Underwriting Operations · lane underwriting · P3 · `micah-pace-36b1b721`

**M1**

Hi Micah,

Underwriting operations at Guardian see each case as the e-application hands it over. A flag would need a place to show up.

FitXpress would return a timestamped Smart Scales weight estimate from two photos, with a flag past Guardian's threshold.

Where in your queue would that flag be most useful to route on?

Nick

**M2**

Hi Micah,

The flag arrives as one field on the structured record, in the queue the team already works. FitXpress is not a medical device and does not make underwriting decisions.

If intake workflow is run elsewhere, forward me there.

A short call to walk through the field layout works for me whenever your team has a free slot: https://meetings.hubspot.com/nick-omelchak

Nick

### Don Kidd · Head of Underwriting Operations · lane underwriting · P2 · `don-kidd-00a43852`

**M1**

Hi Don,

Risk and capacity planning in underwriting operations depends on how many cases get referred. A build flag would add to that count.

FitXpress takes two photos in the Guardian e-application and returns a Smart Scales weight estimate, flagged only past Guardian's threshold.

How would extra referrals from a build flag fit your capacity plan?

Nick

**M2**

Hi Don,

Flag counts at the thresholds you consider would give a referral-volume forecast before anything goes live. FitXpress is not a medical device and does not make underwriting decisions.

I can bring the counting method to a call: https://meetings.hubspot.com/nick-omelchak

Nick

### Mark Woolley · Head of DI New Business and Underwriting Technology · lane technical-integration · P3 · `smarkw`

**M1**

Hi Mark,

DI new business technology at Guardian touches every IDI file that a DI-to-Life certificate later reuses.

Through a REST API, FitXpress returns a timestamped Smart Scales weight estimate from two photos, with a flag past the carrier's threshold.

How does a structured record reach DI case management in your systems today?

Nick

**M2**

Hi Mark,

The record arrives as one entry per applicant over TLS, and it rests under S3-managed encryption. FitXpress is not a medical device and does not make underwriting decisions.

Documents go through legal@3dlook.me.

If it is easier, a call on the record format works for me: https://meetings.hubspot.com/nick-omelchak

Nick

### Steve Rullo · Chief Digital and Technology Officer · lane technical-integration · P3 · `steverullo`

**M1**

Hi Steve,

A new data vendor for the Guardian new-business journey passes through technology review.

FitXpress is an SDK and API step: two photos in, a Smart Scales weight estimate and a flag past the carrier's threshold on one timestamped record out.

How does Guardian review a new data vendor for that journey?

Nick

**M2**

Hi Steve,

The privacy FAQ at https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/ covers data handling. In short it is TLS in transit, S3-managed encryption at rest, retained photos blurred and faces obscured at capture. FitXpress is not a medical device and does not make underwriting decisions.

If vendor reviews run through a separate risk team, I would be glad to be pointed there.

A call on what your reviewers would ask for is easy to arrange: https://meetings.hubspot.com/nick-omelchak

Nick

## Lincoln Financial (11)

### Heather Milligan · SVP Underwriting & New Business Life Solutions · lane underwriting · P1 · `heather-milligan-b602601a`

**M1**

Hi Heather,

TermAccel's rules engine waives lab work for qualifying clients. Where it does, height and weight are what the client enters.

FitXpress adds a step with two photos to the e-application and returns a Smart Scales weight estimate, flagged against Lincoln's threshold.

How do you read build on a lab-waived TermAccel case?

Nick

**M2**

Hi Heather,

An evaluation would run beside the rules engine, counting flags and comparing them with build from the cases where Lincoln orders vitals and physical measurements. FitXpress is not a medical device and does not make underwriting decisions.

The evaluation steps are listed at https://3dlook.ai/for-insurance-underwriting/ in order.

I would be glad to walk through the evaluation on a call: https://meetings.hubspot.com/nick-omelchak

Nick

### Katie Klod · AVP - Life Underwriting & New Business IT · lane technical-integration · P3 · `katie-klod-76b65219`

**M1**

Hi Katie,

Every input to the TermAccel rules engine has to arrive from somewhere, and the engine decides which clients skip lab work.

From two photos, FitXpress returns one timestamped record: a Smart Scales weight estimate and a flag past Lincoln's threshold.

How would a structured record like that be delivered to the rules engine?

Nick

**M2**

Hi Katie,

Integration is a REST API and SDKs, and the record is returned to Lincoln's systems only. Photos are deleted after processing or within 30 days per Lincoln's policy. FitXpress is not a medical device and does not make underwriting decisions.

I can map the delivery path with you on a call: https://meetings.hubspot.com/nick-omelchak

Nick

### Helena Roberts · Vice President, Underwriting & New Business · lane underwriting · P2 · `helena-roberts-7b87a694`

**M1**

Hi Helena,

When a TermAccel case misses the lab waiver, Lincoln orders vitals and physical measurements. Waived cases carry the height and weight the client enters.

Two photos in the e-application give FitXpress a Smart Scales weight estimate to set beside the declared weight, with a flag at Lincoln's threshold.

Could the measurements Lincoln orders serve as a reference for judging a gap?

Nick

**M2**

Hi Helena,

Agreement with those measurements is the yardstick, and a shadow evaluation would read the flag against them with no decision attached. FitXpress is not a medical device and does not make underwriting decisions.

A call would give me room to show how that comparison is built: https://meetings.hubspot.com/nick-omelchak

Nick

### Deborah Lineberry · AVP, New Business Technology · lane technical-integration · P3 · `deborah-lineberry-a6b713202`

**M1**

Hi Deborah,

New business technology at Lincoln covers the path from eTicket onward.

The FitXpress SDK adds a step of two photos and returns a timestamped Smart Scales weight estimate, with a flag past Lincoln's threshold.

Which release path would a web and mobile SDK step go through?

Nick

**M2**

Hi Deborah,

The step lives inside the application, with no separate app for the applicant, over TLS with S3-managed encryption at rest. FitXpress is not a medical device and does not make underwriting decisions.

The release path is easy to talk through, at a time that suits your team: https://meetings.hubspot.com/nick-omelchak

Nick

### Nathan Brown · VP, New Business Technology · lane technical-integration · P3 · `nathan-brown-b1698990`

**M1**

Hi Nathan,

At the e-delivery end of the path, the case file holds the data the application collected. A new data source adds to that.

FitXpress sends back one timestamped record from two photos: a Smart Scales weight estimate, flagged where it departs from the declared weight past Lincoln's threshold.

What does Lincoln ask of a new data vendor before it touches the new-business journey?

Nick

**M2**

Hi Nathan,

A vendor review usually covers where the data lives and for how long. Retained photos are blurred, faces are obscured at capture, and scan records use random identifiers. FitXpress is not a medical device and does not make underwriting decisions.

Review questions are best answered in a call, at a time you pick: https://meetings.hubspot.com/nick-omelchak

Nick

### Rachael Maurer · VP, Chief Privacy Officer · lane technical-integration · P3 · `rachael-maurer`

**M1**

Hi Rachael,

A photo step starts a privacy review with one question about the photos.

FitXpress takes two photos in the e-application and returns a timestamped Smart Scales weight estimate, flagged past Lincoln's threshold. Photos are deleted after processing or within 30 days per the carrier's policy.

What would your review ask for before a step like that went near a Lincoln application?

Nick

**M2**

Hi Rachael,

Retained photos are blurred, faces are obscured at capture, and scan records sit on random identifiers. FitXpress is not a medical device and does not make underwriting decisions.

The privacy FAQ at https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/ covers the rest of the data handling questions a review would raise.

Walking through the handling with you would suit me, at a time of your choosing: https://meetings.hubspot.com/nick-omelchak

Nick

### Patrick Sullivan · VP, InsurTech | Strategy | Enablement · lane referral · P3 · `patrick-d-sullivan-5812b78`

**M1**

Hi Patrick,

InsurTech and enablement work at Lincoln often starts where a new input meets a business line.

FitXpress is two photos in the e-application returning a Smart Scales weight estimate, with a flag past the carrier's threshold, for accelerated life cases.

How does your team decide which business line should look at a new evidence input?

Nick

**M2**

Hi Patrick,

A business line would try an input like this beside live cases, with the record kept out of every decision. FitXpress is not a medical device and does not make underwriting decisions.

A business line can read the short version at https://3dlook.ai/for-insurance-underwriting/ before deciding.

If underwriting rules or the new-business journey sit with another team, a name would help.

A call could pick it up from there whenever you are ready: https://meetings.hubspot.com/nick-omelchak

Nick

### Jonathan Applewhite · VP, Core Life Product Development · lane proposition · P2 · `jonathan-applewhite-fsa-5b826911`

**M1**

Hi Jonathan,

WealthProtector, Lincoln's protection-focused IUL launched in February, keeps product design close to the application.

FitXpress would turn two photos into a timestamped Smart Scales weight estimate, with a flag past Lincoln's threshold.

How do you weigh the effort of an added application step against what it adds?

Nick

**M2**

Hi Jonathan,

The cost is one application step, and an evaluation would count how often the flag fires before anything goes to a decision. The record returns to your own systems. FitXpress is not a medical device and does not make underwriting decisions.

The step as an applicant meets it is described at https://3dlook.ai/for-insurance-underwriting/ for reference.

Where application design lives with another owner, route me to them.

The cost side is quick to go through, and my calendar is open: https://meetings.hubspot.com/nick-omelchak

Nick

### Eric Pahl · VP, Core Life Product Development · lane proposition · P2 · `ericpahlfsa`

**M1**

Hi Eric,

Core Life product choices at Lincoln end up as questions and steps in the e-application.

Two photos would be the whole step, and FitXpress returns a Smart Scales weight estimate with a flag past Lincoln's threshold.

Where in the journey could a step like that sit without lengthening the part clients already know?

Nick

**M2**

Hi Eric,

On timing, the scan returns 80+ body measurements, under 45 seconds from the photos to structured results.

Completion would be measured in the evaluation, once for each placement. FitXpress is not a medical device and does not make underwriting decisions.

Worth a call on how placement and completion would be read: https://meetings.hubspot.com/nick-omelchak

Nick

### Ewelina Mroczek · VP, Digital Product Transformation · lane referral · P3 · `emroczek`

**M1**

Hi Ewelina,

The online client interview is the default start for MoneyGuard applications at Lincoln.

A step of two photos in that interview would return a Smart Scales weight estimate and a flag past the carrier's threshold.

How do you measure drop-off when a digital journey gains a step?

Nick

**M2**

Hi Ewelina,

A step that needs no separate app for the applicant would be the one to try: web and mobile SDKs, with completion measured in the evaluation. FitXpress is not a medical device and does not make underwriting decisions.

Whoever owns the journey can see the step described at https://3dlook.ai/for-insurance-underwriting/ in a few lines.

Should the individual life journey belong to someone else, send me their way.

A call about the interview step would be easy to arrange: https://meetings.hubspot.com/nick-omelchak

Nick

### Mike Hamilton · VP, Head of MoneyGuard Product Solutions · lane proposition · P3 · `mike-hamilton-6029653`

**M1**

Hi Mike,

Lincoln's MoneyGuard e-application guide has producers check height and weight limits before submission.

FitXpress brings two photos to that e-application and returns a Smart Scales weight estimate, flagged past the carrier's threshold.

How would you test a photo step with producers before submission?

Nick

**M2**

Hi Mike,

Producer reaction is the first thing the evaluation would measure, along with completion. FitXpress is not a medical device and does not make underwriting decisions.

If the e-application roadmap is run by another group, forward me there.

I can cover producer testing in a call whenever it suits you: https://meetings.hubspot.com/nick-omelchak

Nick

## Transamerica (11)

### Terri Drahn · VP Underwriting · lane underwriting · P2 · `terri-drahn-9743a099`

**M1**

Hi Terri,

Quick one on build charts for Transamerica's fluidless cases.

Applicants take two photos in the e-application, and the carrier receives a weight estimate from Smart Scales and a timestamped flag when the gap passes its threshold.

For fluidless cases, where does your chart separate preferred from standard, and how wide a gap would cross it?

Nick

**M2**

Hi Terri,

The flag is a single line on the file for gaps above the chart line you choose, and your underwriters decide what follows. FitXpress is not a medical device and does not make underwriting decisions.

A time for walking through the chart question can be booked at https://meetings.hubspot.com/nick-omelchak

Nick

### Neal Hasty · Director Life Underwriting · lane underwriting · P2 · `neal-hasty-a8b356231`

**M1**

Hi Neal,

Spotted something on Transamerica's fluidless page: many cases are decided without individual review, by rules using external data.

The scan returns a Smart Scales estimate from two photos, with a flag above the carrier's threshold, as a timestamped record.

How do program reviews at Transamerica treat build on cases decided by rules alone?

Nick

**M2**

Hi Neal,

The flag works as a referral line ahead of a rules-based decision, and the carrier's rules and underwriters stay in charge. FitXpress is not a medical device and does not make underwriting decisions.

If you would rather point me to whoever runs program monitoring, that works too. If a short call on how reviews treat build is of interest, schedule it at https://meetings.hubspot.com/nick-omelchak

A rules-based case picking up a flag is walked through here: https://3dlook.ai/for-insurance-underwriting/

Nick

### Tracy Regier · Director of Underwriting · lane underwriting · P2 · `tracy-regier-72866a38`

**M1**

Hi Tracy,

Had a thought about your years as a senior underwriting consultant at Transamerica Life and Protection.

Inside the e-application, applicants would take two photos. Smart Scales returns a weight estimate, and a flag fires above the carrier's threshold, in one timestamped record.

Before a live case saw any of it, what would your team want from a shadow evaluation?

Nick

**M2**

Hi Tracy,

A shadow evaluation keeps outputs out of decisions and counts flags at a few thresholds. Underwriters read the counts, and the route stays as it is. FitXpress is not a medical device and does not make underwriting decisions.

I would be glad to talk through the evaluation design, with my calendar here https://meetings.hubspot.com/nick-omelchak

Nick

### Aniton William · Director Underwriting · lane underwriting · P2 · `aniton-william-61399344`

**M1**

Hi Aniton,

Made me think about Transamerica's new e-App, which puts clearer questions up front for term and IUL.

A step FitXpress offers sits after those questions: two photos, a Smart Scales weight estimate and a flag above the carrier's threshold, as one timestamped record.

With the questions up front, which build details do underwriters still wait for?

Nick

**M2**

Hi Aniton,

The record arrives once per applicant after the questions are answered, and an underwriter sees a flag only above the carrier's threshold. FitXpress is not a medical device and does not make underwriting decisions.

If the e-App question set belongs to someone else, I would value an introduction. Should a conversation help, you can find a slot at https://meetings.hubspot.com/nick-omelchak

Nick

### Tricia Wood · Chief Privacy Officer · lane technical-integration · P3 · `tricia-wood-a730745`

**M1**

Hi Tricia,

This stood out: your years in global privacy at Liberty Mutual before Transamerica.

FitXpress asks an applicant for two photos in the e-application and returns a Smart Scales weight estimate and a threshold flag, as one timestamped record.

What would a privacy review at Transamerica need to see before applicants are asked for photos?

Nick

**M2**

Hi Tricia,

Photos are deleted after processing or within 30 days per the carrier's policy, retained photos are blurred, faces are obscured at capture, and scan records sit on random identifiers. Documents go through legal@3dlook.me. FitXpress is not a medical device and does not make underwriting decisions.

I can take your questions live, through the scheduling page at https://meetings.hubspot.com/nick-omelchak

The privacy FAQ lays out retention and roles: https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/

Nick

### Andrew Vigar · Head of Underwriting · lane underwriting · P1 · `andrew-vigar-falu-flmi-74579219`

**M1**

Hi Andrew,

Noticed your leadership of life underwriting and new business at earlier carriers. Transamerica's fluidless page says some clients get an accelerated decision without blood and urine.

FitXpress puts two photos into the e-application and adds a Smart Scales weight estimate, BMI from the declared height and a flag above the threshold you set, in one timestamped record.

On those fluidless files, what is the first thing your team looks at for build?

Nick

**M2**

Hi Andrew,

A first evaluation would count flags on fluidless files and set them beside build evidence from cases that did have an exam. FitXpress is not a medical device and does not make underwriting decisions.

If a call on fluidless rules makes sense, my calendar is here https://meetings.hubspot.com/nick-omelchak

Where the step sits in a fluidless e-application is mapped here: https://3dlook.ai/for-insurance-underwriting/

Nick

### Steve Jensen · Global Chief Information Security Officer · lane technical-integration · P3 · `sgjense`

**M1**

Hi Steve,

Couldn't help but ask a security question, given your years as CISO at Scottrade and Ameriprise.

The step is an SDK in the e-application with a REST API behind it: two photos return a Smart Scales weight estimate, BMI from the declared height, a threshold flag and one timestamped record. Data moves over TLS in transit and S3-managed encryption at rest.

What does your security review ask of an SDK step before it reaches an e-application?

Nick

**M2**

Hi Steve,

Retention: photos are deleted after processing or within 30 days per the carrier's policy, and scan records sit on random identifiers. Documents go through legal@3dlook.me. FitXpress is not a medical device and does not make underwriting decisions.

I can bring the technical details to a call arranged through https://meetings.hubspot.com/nick-omelchak

Security and data handling points for an SDK step are listed in the FAQ here: https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/

Nick

### Virginia Greene · Medical Director · lane medical · P2 · `virginiagreene`

**M1**

Hi Virginia,

Curious about your years as an assistant medical director and underwriting specialist before Transamerica.

On fluidless cases a carrier could add two photos to the e-application. The Smart Scales estimate arrives with BMI from the declared height and a flag when the gap crosses a threshold the carrier sets.

What margin over a weight estimate's error would you want before a gap triggers a referral?

Nick

**M2**

Hi Virginia,

On the error side, Smart Scales shows approximately 3.5% mean absolute error under evaluated conditions and is not a scale reading. The carrier sets the threshold. FitXpress is not a medical device and does not make underwriting decisions.

For a conversation on that margin, a time can be chosen through https://meetings.hubspot.com/nick-omelchak

The page spells out the decision boundary for the medical side: https://3dlook.ai/for-insurance-underwriting/

Nick

### Michael K · Medical Director · lane medical · P2 · `michael-k-469910295`

**M1**

Hi Michael,

Caught my eye that you trained as an endocrinologist. Transamerica's FFIUL II Express has a fully digital application with an instant decision.

A carrier could add two photos to that flow, returning a Smart Scales weight estimate and a threshold flag.

What would make a weight estimate from two photos usable in that flow, in your judgment?

Nick

**M2**

Hi Michael,

The decision boundary stays with the carrier: a threshold set well above the estimate's error, and a flag for gaps above it. FitXpress is not a medical device and does not make underwriting decisions.

A short exchange on that boundary can start from https://meetings.hubspot.com/nick-omelchak

Nick

### Christine Kor-Aronski · Medical Director - Remote · lane medical · P2 · `christine-kor-aronski-14784125`

**M1**

Hi Christine,

Wanted to reach out about your remote medical director role at Transamerica.

FitXpress would give a fluidless case two photos in the e-application and return a flag when the Smart Scales estimate and the declared weight differ by more than the carrier's threshold.

How does Transamerica's build guidance read a declared weight against an exam weight?

Nick

**M2**

Hi Christine,

An estimate has a narrow use here: a referral line on gaps that would change the class. It is not a scale reading. FitXpress is not a medical device and does not make underwriting decisions.

I would like to talk through where that line sits, and a slot is open at https://meetings.hubspot.com/nick-omelchak

The page states the decision boundary in the carrier's terms: https://3dlook.ai/for-insurance-underwriting/

Nick

### Ben Wadsley · Head of Product Development & Pricing - Individual Solutions · lane proposition · P2 · `ben-wadsley-62460413`

**M1**

Hi Ben,

Got me thinking about your years in proposition and solution development at Transamerica.

A fully digital IUL application with an instant decision, like FFIUL II Express, could carry a step of two photos. FitXpress returns a Smart Scales weight estimate and a flag above the carrier's threshold, as a timestamped record.

How would you measure drop-off for a new step in an instant-decision flow?

Nick

**M2**

Hi Ben,

Completion would be measured in the evaluation, and the record returns to the carrier alone. FitXpress is not a medical device and does not make underwriting decisions.

If the digital application sits elsewhere, I am glad to go to its owner. To look at placement together, grab a time at https://meetings.hubspot.com/nick-omelchak

Placement options for a digital application are laid out here: https://3dlook.ai/for-insurance-underwriting/

Nick

## RGA US (11)

### Jennifer Johnson · Vice President of Underwriting Innovation · lane reinsurance · P2 · `jennifer-johnson-certified-falu-clu-flmi-b5155b42`

**M1**

Hi Jennifer,

Caught my eye: Aura Next on RGA's underwriting page uses reflexive interview questions.

A flag from FitXpress could feed the same logic. Taken in the e-application, two photos give a Smart Scales weight estimate and a flag when the gap from declared weight crosses the carrier's threshold.

Could that flag trigger a follow-up question inside an Aura Next interview?

Nick

**M2**

Hi Jennifer,

The flag arrives as a structured, timestamped field that a reflexive rule can read. FitXpress is not a medical device and does not make underwriting decisions.

To look at how that field would be used in Aura Next, pick a slot at https://meetings.hubspot.com/nick-omelchak

Nick

### Jacqueline Waas · Vice President of Underwriting Research & Development · lane reinsurance · P2 · `jacqueline-waas-05a79145`

**M1**

Hi Jacqueline,

Quick thought for underwriting R&D at RGA. The Global Underwriting Manual has a build section.

One candidate input is FitXpress: two photos in the e-application, kept as a timestamped record with a Smart Scales weight estimate and a threshold flag.

How would R&D weigh evidence like that for the manual's build guidance?

Nick

**M2**

Hi Jacqueline,

For the manual's build section, an evaluation could set flags beside build evidence gathered separately, such as paramedical exam cases. FitXpress is not a medical device and does not make underwriting decisions.

If build guidance sits with another owner, point me to them. I am glad to go through it live, and the scheduling page is at https://meetings.hubspot.com/nick-omelchak

The page describes that comparison with exam-case evidence: https://3dlook.ai/for-insurance-underwriting/

Nick

### Colin Deforge · Vice President, Underwriting · lane reinsurance · P2 · `colin-deforge-0639701`

**M1**

Hi Colin,

Couldn't help but ask about client conversations on accelerated cases.

For context, FitXpress takes two photos in the e-application and returns a Smart Scales weight estimate and a flag where the gap crosses the carrier's threshold, as one timestamped record.

Has any RGA client asked about remote build evidence for accelerated cases?

Nick

**M2**

Hi Colin,

If a client asked, the design is a shadow evaluation with nothing reaching a case, counting flags at a few thresholds. FitXpress is not a medical device and does not make underwriting decisions.

If a client raises it, I can walk your team through the design, with my calendar here https://meetings.hubspot.com/nick-omelchak

Nick

### Caroline Specter · Vice President, Delivery - Automated Underwriting · lane reinsurance · P2 · `caroline-specter-a9b8ab57`

**M1**

Hi Caroline,

Spotted your product delivery background ahead of a practical integration question.

FitXpress runs as an SDK step in the e-application: two photos produce a structured, timestamped record with a Smart Scales weight estimate, BMI from the declared height and a threshold flag.

How does a new evidence field from a client's e-application reach RGA's automated underwriting delivery?

Nick

**M2**

Hi Caroline,

Integration is an API and web and mobile SDKs, with one timestamped record per applicant returned to the carrier. FitXpress is not a medical device and does not make underwriting decisions.

If integration intake sits elsewhere at RGA, I would gladly go to whoever runs it. A time for the integration walk-through can be booked at https://meetings.hubspot.com/nick-omelchak

Nick

### Mark Brann · VP, New Business Enablement · lane reinsurance · P3 · `mark-brann-ab79a322`

**M1**

Hi Mark,

Curious about your take on new business enablement for clients.

One step FitXpress offers is two photos in the e-application, returned as a timestamped record with a Smart Scales weight estimate and a threshold flag.

When a client wants a new e-application step, what does your team set up with it first?

Nick

**M2**

Hi Mark,

For a client's team the setup is an SDK step in the e-application and a threshold the carrier chooses. FitXpress is not a medical device and does not make underwriting decisions.

I can also go straight to whoever supports client e-applications. If a short call suits you, a time can be set up through https://meetings.hubspot.com/nick-omelchak

Nick

### Michael Hill · Vice President, Fac Underwriting Strategy and Data Analytics · lane reinsurance · P2 · `michaelhillunderwriter`

**M1**

Hi Michael,

Had a thought about RGA's record facultative year in 2025 and the workbench's production and risk selection data review.

Each applicant takes two photos in the e-application, and FitXpress hands the carrier a timestamped record: Smart Scales weight estimate, BMI from the declared height and a threshold flag.

Where in production and risk selection data would a structured build field give you the most?

Nick

**M2**

Hi Michael,

The record is one timestamped line per applicant, which a data team can count by threshold against build evidence gathered separately. FitXpress is not a medical device and does not make underwriting decisions.

Whoever runs analytics intake at RGA is welcome to join. The counting is easiest to show on a call, which you can arrange at https://meetings.hubspot.com/nick-omelchak

What the record holds for a data team to count is listed here: https://3dlook.ai/for-insurance-underwriting/

Nick

### Nathan Hill · VP & Actuary, Individual Life Pricing · lane reinsurance · P2 · `nathan-hill-24b77626`

**M1**

Hi Nathan,

Got me thinking about how RGA weighs the cost of new evidence in individual life pricing.

A carrier could add a step of two photos to the e-application, where FitXpress returns a Smart Scales weight estimate and a flag above its threshold as one timestamped record.

What would pricing look at first when a new source of build evidence is proposed?

Nick

**M2**

Hi Nathan,

The flag adds build evidence on accelerated cases that carry none, and the carrier sets the threshold. FitXpress is not a medical device and does not make underwriting decisions.

If evidence-cost reviews belong to another desk, whoever leads them can join too. Happy to compare notes live, and a time is yours to choose at https://meetings.hubspot.com/nick-omelchak

One record's contents, for judging how a new source is weighed, are described here: https://3dlook.ai/for-insurance-underwriting/

Nick

### Nick Sontheimer · VP & Managing Actuary, Pricing, US Individual Life · lane reinsurance · P2 · `nick-sontheimer-b01084178`

**M1**

Hi Nick,

Wanted to reach out about pricing data at RGA, where a shadow evaluation of build evidence produces counts a pricing team can read.

The scan is two photos in the e-application, returned by FitXpress as one timestamped record with a Smart Scales weight estimate and a flag above the carrier's threshold.

Which counts from a shadow evaluation would be worth pricing's time?

Nick

**M2**

Hi Nick,

An evaluation gives pricing a count of flags at a few thresholds across a client's accelerated files. FitXpress is not a medical device and does not make underwriting decisions.

If pricing studies are led elsewhere, send me to whoever leads them. To go through the counts, a time is open at https://meetings.hubspot.com/nick-omelchak

Nick

### Dave Rengachary · Senior Vice President, Head of Underwriting, U.S. Mortality Markets · lane reinsurance · P1 · `dave-rengachary`

**M1**

Hi Dave,

Noticed your earlier years as RGA's chief medical director and your lead of underwriting for US individual life.

RGA's Strategic Underwriting Program connects carriers with new tools. FitXpress is a tool of that kind: a Smart Scales weight estimate from two photos in the e-application, BMI from the declared height, a flag above the carrier's threshold and one timestamped record.

What path would a tool like that take through the program to reach a carrier's accelerated cases?

Nick

**M2**

Hi Dave,

A sensible first step with one carrier is a shadow evaluation, with outputs kept out of decisions. Smart Scales shows approximately 3.5% mean absolute error under evaluated conditions and is not a scale reading. FitXpress is not a medical device and does not make underwriting decisions.

I can walk through that route on a call, and my calendar is here https://meetings.hubspot.com/nick-omelchak

Placement inside a carrier's accelerated e-application is illustrated here: https://3dlook.ai/for-insurance-underwriting/

Nick

### Ron Hollowell · SVP, Chief Technology Officer · lane technical-integration · P3 · `ron-hollowell-92b1861b`

**M1**

Hi Ron,

This stood out: RGA's new workbench handles evidence ordering and review.

A build record would be one more evidence type, arriving through a REST API or SDK from FitXpress: a Smart Scales weight estimate from two photos in the e-application, a threshold flag and one timestamped record.

What does RGA's review of a new data vendor look like before it reaches the workbench?

Nick

**M2**

Hi Ron,

Data handling: TLS in transit, S3-managed encryption at rest, photos deleted after processing or within 30 days per the carrier's policy, scan records on random identifiers. Documents go through legal@3dlook.me. FitXpress is not a medical device and does not make underwriting decisions.

I can speak with your technical team at a time picked through https://meetings.hubspot.com/nick-omelchak

The privacy FAQ covers vendor review points: https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/

Nick

### Braam Kruger · Vice-President & Chief Risk Officer, US Individual Life · lane reinsurance · P3 · `braam-kruger-35771576`

**M1**

Hi Braam,

Made me think about how risk is owned for US individual life at RGA.

FitXpress would give a client's program two photos in the e-application, a timestamped record and a flag above the carrier's threshold, with a Smart Scales weight estimate.

What does risk management need in hand before new evidence like that joins a client's program?

Nick

**M2**

Hi Braam,

For a risk view the evaluation runs in shadow first, with outputs kept out of decisions. FitXpress is not a medical device and does not make underwriting decisions.

A discussion on framing it for a client can start at https://meetings.hubspot.com/nick-omelchak

The page lays out the shadow-first path a risk review would follow: https://3dlook.ai/for-insurance-underwriting/

Nick

## Hannover Life Re America (10)

### Jeremy Vest · Vice President, Underwriting · lane reinsurance · P2 · `jeremy-vest-59167291`

**M1**

Hi Jeremy,

Got me thinking about your years as chief life underwriter at Alfa Insurance.

Two photos in the e-application give FitXpress what it needs to return a timestamped record with a flag above the carrier's threshold, next to a Smart Scales weight estimate.

When a Hannover Life Re client runs an accelerated case with no exam, how is build looked at for that file?

Nick

**M2**

Hi Jeremy,

A flag refers only gaps above the carrier's threshold, and the carrier's underwriters decide what follows. FitXpress is not a medical device and does not make underwriting decisions.

If you would like to compare that with how your clients treat build, we can find a time through https://meetings.hubspot.com/nick-omelchak

The insurance underwriting page walks through the evaluation path for a client program: https://3dlook.ai/for-insurance-underwriting/

Nick

### Renee McClintic · AVP Underwriting Auditor · lane reinsurance · P3 · `renee-mcclintic-falu-flmi-hiaa-acs-66954113`

**M1**

Hi Renee,

Curious about your take on audit: accelerated cases with no exam leave the file with the declared height and weight.

Applicants would take two photos in the e-application, and FitXpress would put a timestamped record on the case: a Smart Scales weight estimate and a flag where the gap crosses the carrier's threshold.

When your audits at Hannover Life Re review build after issue, what would you want the file to show?

Nick

**M2**

Hi Renee,

Each record carries a timestamp and sits on the case file, giving a later review one fixed reference. FitXpress is not a medical device and does not make underwriting decisions.

If audit standards belong to another desk, whoever sets them is welcome too. A call about what an audit would want to see is easy to arrange at https://meetings.hubspot.com/nick-omelchak

For later review, the record appears on the case as described here: https://3dlook.ai/for-insurance-underwriting/

Nick

### Eric Flender · VP, Underwriting · lane reinsurance · P2 · `eric-flender-b4b198172`

**M1**

Hi Eric,

Quick one on build charts. Accelerated cases with no paramedical exam rest on the height and weight the applicant enters.

The FitXpress step is two photos in the e-application. Smart Scales estimates weight, a flag marks a gap above the carrier's threshold, and BMI is calculated from the declared height.

On a client's chart, which gaps between declared and estimated weight would take a case from preferred to standard?

Nick

**M2**

Hi Eric,

The first evaluation counts how often a gap would reach a chart edge across a client's accelerated files, which shows where a threshold belongs. FitXpress is not a medical device and does not make underwriting decisions.

If you want to walk through the counting, a slot is open at https://meetings.hubspot.com/nick-omelchak

Nick

### Brian Hiserote · VP Underwriting · lane reinsurance · P2 · `brian-hiserote-640575b3`

**M1**

Hi Brian,

Caught my eye that Hannover Life Re's ReFlex page says the team works with clients on their accelerated programs.

From two photos, FitXpress returns one timestamped record to the carrier, holding a threshold flag and a Smart Scales weight estimate.

What would your team want in front of it before a shadow evaluation with a client could start?

Nick

**M2**

Hi Brian,

An evaluation in shadow can stay small: one client, nothing from the scan reaching a decision, flags counted at a few thresholds. FitXpress is not a medical device and does not make underwriting decisions.

To go through how that would run, a time can be set at https://meetings.hubspot.com/nick-omelchak

The page for underwriting lays the shadow evaluation out step by step: https://3dlook.ai/for-insurance-underwriting/

Nick

### James McArdle · Vice President- Reflex Underwriting Solutions at Hannover Life Reassurance Company · lane reinsurance · P2 · `james-mcardle-590a9663`

**M1**

Hi James,

Spotted something on Hannover's ReFlex page: rules and question sets can be customized without IT development.

FitXpress takes two photos and returns a flag when the Smart Scales weight estimate and the declared weight differ by more than the carrier's threshold, with a timestamped record.

Could a flag like that open the next ReFlex question on a client's accelerated case?

Nick

**M2**

Hi James,

On the integration side FitXpress is a REST API or an SDK step, and one timestamped record per applicant returns to the client's flow. FitXpress is not a medical device and does not make underwriting decisions.

To see where the flag would sit in a question set, choose a time at https://meetings.hubspot.com/nick-omelchak

Nick

### Susan Mayer · Vice President, Chief Underwriter · lane reinsurance · P1 · `susan-l-mayer-falu-flmi-07601824`

**M1**

Hi Susan,

Noticed your years on the SEHOUA executive board, alongside your work at Hannover Life Re.

FitXpress adds a step of two photos to the e-application and returns a Smart Scales weight estimate. A flag fires when the gap from the declared weight crosses the carrier's threshold, with BMI from the declared height and one timestamped record.

How would you set up a first test of a source like that inside one client's accelerated program?

Nick

**M2**

Hi Susan,

A shadow evaluation with one client would be the natural first step: flags counted at a few thresholds, nothing reaching a case. Smart Scales carries approximately 3.5% mean absolute error under evaluated conditions and is not a scale reading. FitXpress is not a medical device and does not make underwriting decisions.

If a first evaluation with one client sounds useful, my calendar is here https://meetings.hubspot.com/nick-omelchak

Nick

### Sean Conrad · Senior Vice President, Head of Traditional Life Pricing and Data Analytics · lane reinsurance · P2 · `seanconrad`

**M1**

Hi Sean,

Made me think about how traditional life pricing and data analytics meet accelerated and automated underwriting in your headline.

FitXpress returns one timestamped record per applicant from two photos, holding a Smart Scales weight estimate, BMI from the declared height and a flag above the carrier's threshold.

Where in pricing and analytics would a structured build field be of use at Hannover Life Re?

Nick

**M2**

Hi Sean,

Each applicant gets one timestamped record, which makes build available to analyse beside the rest of the application data. FitXpress is not a medical device and does not make underwriting decisions.

Whoever handles client analytics at Hannover Life Re would be welcome on the call too. To talk it through, you can reach me through https://meetings.hubspot.com/nick-omelchak

A structured record looks like this on a case file: https://3dlook.ai/for-insurance-underwriting/

Nick

### Elena Strunk · Vice President, Medical Director · lane medical · P2 · `elena-a-s-4a902718b`

**M1**

Hi Elena,

Wanted to reach out given your emergency medicine background and your medical director role at Hannover Re US.

The scan is two photos taken inside the e-application. FitXpress returns a Smart Scales weight estimate, BMI from the declared height and a flag if the gap crosses a carrier-set threshold.

Which questions would you put to a software weight estimate before a carrier's accelerated rules used it?

Nick

**M2**

Hi Elena,

The Smart Scales figure is approximately 3.5% mean absolute error under evaluated conditions, and the estimate is not a scale reading. A carrier would set any threshold well above that. FitXpress is not a medical device and does not make underwriting decisions.

I would welcome a conversation on where you would draw that line, and my calendar is here https://meetings.hubspot.com/nick-omelchak

Nick

### Kevin Bettis · VP, Facultative Underwriting · lane reinsurance · P3 · `kevin-bettis-certified-falu-flmi-ara-acs-airc-a7809a25`

**M1**

Hi Kevin,

Had a thought reading your headline on large-case risk and underwriting innovation.

FitXpress sits inside the e-application as a step taking two photos. The carrier receives a Smart Scales weight estimate and a threshold flag as one timestamped record.

Where does a large case end and an accelerated one begin for Hannover Life Re clients, and does build mark that line?

Nick

**M2**

Hi Kevin,

One use of the flag is a referral from the accelerated route into a fuller review when the gap is large, with the threshold set by the carrier. FitXpress is not a medical device and does not make underwriting decisions.

If that boundary is one you discuss with clients, a conversation can start at https://meetings.hubspot.com/nick-omelchak

The page sets out where the step sits before a fuller review: https://3dlook.ai/for-insurance-underwriting/

Nick

### Laura Cutshall · Assistant Vice President, ReFlex Underwriting Solutions · lane reinsurance · P2 · `laura-cutshall-25543627`

**M1**

Hi Laura,

This stood out: your underwriting design and configuration background, and the ReFlex role.

On a client's accelerated cases FitXpress would add two photos to the e-application, returning a timestamped record with a threshold flag and a Smart Scales weight estimate.

What would a client have to define in ReFlex before a build flag like that went live?

Nick

**M2**

Hi Laura,

Setup for a client comes down to the carrier's threshold and the route a flagged file takes, through an API or SDK step. FitXpress is not a medical device and does not make underwriting decisions.

If client configuration sits elsewhere at Hannover Life Re, I would gladly speak with whoever handles it. A call on the configuration questions can be booked at https://meetings.hubspot.com/nick-omelchak

Nick

## SCOR Life Americas (10)

### Patrick Scanlon · AVP, Underwriting Solutions, SCOR · lane reinsurance · P2 · `patrick-scanlon-8774a417b`

**M1**

Hi Patrick,

Noticed that your team built SMART and FAST for SCOR Life Americas. On client accelerated cases, the application supplies declared build.

FitXpress is an API and SDK step: two photos give a Smart Scales weight estimate and one timestamped record, with a flag above a threshold the client sets.

How does your team decide which new evidence sources get built into those tools?

Nick

**M2**

Hi Patrick,

What would travel into a tool like SMART or FAST is one timestamped record per applicant, delivered by API or SDK, with a flag against the client's threshold.

The step and its record are described at https://3dlook.ai/for-insurance-underwriting/

FitXpress is not a medical device and does not make underwriting decisions.

We could trace the record into your tools on a call at https://meetings.hubspot.com/nick-omelchak

Nick

### Michelle Spevak · AVP, Underwriting Research · lane reinsurance · P2 · `michelle-spevak-50476213`

**M1**

Hi Michelle,

Got me thinking about the research behind SOLEM's build guidance at SCOR Life Americas. Client accelerated cases without a paramed exam carry only declared figures for build.

Two photos in the e-application give FitXpress a Smart Scales weight estimate, with a flag above a threshold the client sets. One timestamped record is kept.

What evidence would you want behind a gap between declared and estimated weight before it informs build guidance?

Nick

**M2**

Hi Michelle,

Flag counts at the thresholds a client picks, set beside paramed exam cases, would give the build guidance something to read against, with outputs kept out of every case.

FitXpress is not a medical device and does not make underwriting decisions.

A call about what a useful research readout looks like is open at https://meetings.hubspot.com/nick-omelchak

Nick

### Brooke Morgan · Director, Underwriting Solutions · lane reinsurance · P2 · `brooke-morgan-of-cincinnati`

**M1**

Hi Brooke,

Spotted your underwriting automation background at SCOR Life Americas, which fits a question about Velogica. A build rule there needs an input to read.

A FitXpress step of two photos produces a Smart Scales weight estimate and a flag above the threshold the client sets, returned by API as one timestamped record.

Where in Velogica would a build referral rule like that go?

Nick

**M2**

Hi Brooke,

A Velogica rule would receive little: the flag, raised only above the client's threshold, and the timestamped record behind it.

FitXpress is not a medical device and does not make underwriting decisions.

If Velogica rule changes sit elsewhere, a name there would help. A walk through the API is open at https://meetings.hubspot.com/nick-omelchak

Nick

### Ed Sheehan · AVP, Underwriting · lane reinsurance · P2 · `ed-sheehan-36768718a`

**M1**

Hi Ed,

Quick thought on SCOR Life Americas' client accelerated programs. Where no paramedical exam happens, build rests on the height and weight the applicant enters.

The scan behind FitXpress takes two photos and returns a Smart Scales weight estimate, with a flag when the gap crosses the threshold the client sets. One timestamped record goes back to the carrier.

How do client programs without a paramed exam treat build today?

Nick

**M2**

Hi Ed,

A shadow evaluation can run with one client: outputs stay out of decisions, and flags are counted at the thresholds the client picks.

FitXpress is not a medical device and does not make underwriting decisions.

Together we could draft the one-client design after you pick a time at https://meetings.hubspot.com/nick-omelchak

Nick

### James Atkins · AVP-Underwriting-Quality Assurance · lane reinsurance · P2 · `james-atkins-flmi-falu-a919a564`

**M1**

Hi James,

Curious about your take on SMART, the SCOR Life Americas dashboard that monitors accelerated programs. Build flags could be one more view in it.

A step of two photos in FitXpress gives a Smart Scales weight estimate and BMI from the declared height. A flag appears only above a threshold the client sets, with one timestamped record per applicant.

How would you want a build flag to appear in SMART's view of a client program?

Nick

**M2**

Hi James,

Flag counts per client program would sit next to the monitoring SMART already does, and each record carries a timestamp.

FitXpress is not a medical device and does not make underwriting decisions.

If someone else owns SMART's data feeds, send me to them. Walking through the flag fields is simple to schedule at https://meetings.hubspot.com/nick-omelchak

Nick

### Stacy Stauffer · Director - Underwriting Partnerships · lane reinsurance · P2 · `stacy-stauffer-falu-flmi-b922b384`

**M1**

Hi Stacy,

Thought I'd share something close to your focus on innovation and automation at SCOR Life Americas. FitXpress is a step of two photos for carriers' e-applications that returns a Smart Scales weight estimate and a flag above the client's threshold, with one timestamped record.

How does SCOR Life Americas vet a partner's evidence before a client sees it?

Nick

**M2**

Hi Stacy,

For vetting, the package is short: what the scan returns, what the client's threshold flags, and a shadow evaluation design that keeps outputs out of decisions.

What the scan returns, and where the carrier's threshold applies, is described at https://3dlook.ai/for-insurance-underwriting/

FitXpress is not a medical device and does not make underwriting decisions.

A call to go through the package can be booked at https://meetings.hubspot.com/nick-omelchak

Nick

### Ashley Hunt · Director - Underwriting Partnerships · lane reinsurance · P2 · `ashley-hunt-768031272`

**M1**

Hi Ashley,

Caught my eye that SCOR Life Americas' underwriting partnerships sit near the questions clients bring. The FitXpress step of two photos adds a Smart Scales weight estimate and flags gaps above the client's threshold.

Has remote build evidence come up in client conversations on accelerated programs?

Nick

**M2**

Hi Ashley,

If clients start asking, a read-only comparison on one client's own cases answers it: flag counts, with outputs kept out of decisions.

How the step looks in an application is shown at https://3dlook.ai/for-insurance-underwriting/

FitXpress is not a medical device and does not make underwriting decisions.

If those client questions go through another team, a name there is welcome. Could we compare notes about those client questions? A time is open at https://meetings.hubspot.com/nick-omelchak

Nick

### Jessica Lenhard · SVP, Head of U.S. Client Solutions for Individual Life & Annuities · lane reinsurance · P2 · `jessica-lenhard-fsa-4b216047`

**M1**

Hi Jessica,

This stood out: SCOR Life Americas offers clients an AI Assistant that leaves the final risk assessment with human experts. A build flag works the same way, as a referral only.

Through FitXpress, two photos return a Smart Scales weight estimate and one timestamped record, with a flag above the client's threshold.

How would you set up one client evaluation so that the final assessment stays with underwriters?

Nick

**M2**

Hi Jessica,

A single client evaluation keeps that stance intact: the flag refers a case, and the final assessment stays with the underwriters reading it.

Where the flag sits in a client's application is described at https://3dlook.ai/for-insurance-underwriting/

FitXpress is not a medical device and does not make underwriting decisions.

Booking a call to scope one client evaluation is easy at https://meetings.hubspot.com/nick-omelchak

Nick

### Regina Rosace · VP Medical Director · lane medical · P2 · `regina-rosace-m-d-faap-dbim-33836715`

**M1**

Hi Regina,

Made me think about what a weight estimate from two photos may be used for on client accelerated cases at SCOR Life Americas.

In FitXpress, Smart Scales produces the estimate and a flag appears only above a threshold the client sets. One timestamped record is kept for each applicant.

Which use of such an estimate would you consider defensible?

Nick

**M2**

Hi Regina,

The stated limits come first. Smart Scales has approximately 3.5% mean absolute error under evaluated conditions and is not a scale reading.

The client sets the threshold, and the flag refers only gaps well above that error.

FitXpress is not a medical device and does not make underwriting decisions.

Where the estimate may and may not be used is worth a conversation, which you can start at https://meetings.hubspot.com/nick-omelchak

Nick

### David Elias · VP and Deputy Head of Inforce Management, Pricing and Underwriting · lane reinsurance · P3 · `david-elias-ph-d-005aa8b`

**M1**

Hi David,

Had a thought about the in-force side of SCOR Life Americas: build at application is a stated height and weight, and it stays on the file for years.

Two photos at application give FitXpress a Smart Scales weight estimate and a timestamped record, with a flag only above a threshold the client sets.

How much does build at application matter to in-force pricing and underwriting work?

Nick

**M2**

Hi David,

A build record timestamped at application stays on the file, which an in-force view could use later. The evaluation can start with new business alone.

FitXpress is not a medical device and does not make underwriting decisions.

In-force needs could be covered over a conversation booked at https://meetings.hubspot.com/nick-omelchak

Nick

## MassMutual (9)

### Warner Shue · Head of Underwriting · lane underwriting · P2 · `warnershue`

**M1**

Hi Warner,

Spotted the FALU and FLMI in your headline. MassExpress decides cases without an exam or labs. Build on those files is the applicant's own declared figures.

In FitXpress, two photos return a Smart Scales weight estimate and one timestamped record. A flag appears when the declared-versus-estimated gap crosses the threshold MassMutual sets.

On MassExpress files, which gaps between declared and estimated weight would change a risk class?

Nick

**M2**

Hi Warner,

A shadow run on MassExpress cases would count flags at several thresholds and compare them with the build measured on paramedical exam cases.

FitXpress is not a medical device and does not make underwriting decisions.

If the evaluation design interests you, a time to plan it together is open at https://meetings.hubspot.com/nick-omelchak

Nick

### Dhru Swadia · Head of New Business Technology · lane technical-integration · P3 · `dhru-swadia-50b57469`

**M1**

Hi Dhru,

Got me thinking about how MassMutual's new-business technology takes in a new evidence step. Accelerated applications carry declared height and weight for build.

FitXpress is an SDK and API: two photos in, a Smart Scales weight estimate and one structured record out, with a flag above a threshold MassMutual sets.

What does review of a new SDK step in the e-application involve on your side?

Nick

**M2**

Hi Dhru,

Integration is a REST API with web and mobile SDKs. Data moves over TLS and rests under S3-managed encryption.

The privacy FAQ at https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/ covers data handling

FitXpress is not a medical device and does not make underwriting decisions.

If vendor review runs through another team, send me their way. Going through the integration steps together is easy to arrange at https://meetings.hubspot.com/nick-omelchak

Nick

### Jason Paine · Head of Disability Underwriting and New Business · lane underwriting · P1 · `jason-paine-a0a76416`

**M1**

Hi Jason,

Noticed MassMutual's January DI update. On DI applications decided without an exam, build rests on the declared figures.

FitXpress takes two photos in the e-application. Smart Scales estimates weight, BMI is calculated from the declared height, and the threshold MassMutual sets decides when a flag is raised.

How does your team handle build on DI differently from life?

Nick

**M2**

Hi Jason,

For DI, the first step is a dry run: outputs stay out of decisions while flags are counted at each candidate threshold and set against paramedical exam cases, where build is measured.

FitXpress is not a medical device and does not make underwriting decisions.

I would be glad to compare DI and life build handling with you on a call at https://meetings.hubspot.com/nick-omelchak

Nick

### Tasha Boland · Head of New Business Analysis and Pricing Review · lane proposition · P3 · `tasha-boland-fsa-cera-4632a3109`

**M1**

Hi Tasha,

Made me think of MassMutual's practices page: risk class from MassExpress may differ from traditional underwriting.

Taken in the e-application, two photos give FitXpress a Smart Scales weight estimate, and a flag appears when the gap crosses the threshold MassMutual sets. One timestamped record goes to the file.

Which class movements would pricing review want counted before an input like that is judged worthwhile?

Nick

**M2**

Hi Tasha,

For pricing review, a parallel run reports how many files a flag would refer at the thresholds MassMutual chooses, allowing the shift in class placement to be compared with paramedical exam cases.

What the step returns, and where it sits in the application, is shown at https://3dlook.ai/for-insurance-underwriting/

FitXpress is not a medical device and does not make underwriting decisions.

How pricing review could use those flag counts is worth a call at https://meetings.hubspot.com/nick-omelchak

Nick

### Lynn Brown · Executive Liaison to Head of Protection New Business & Underwriting · lane referral · P3 · `lynn-brown-0b27474`

**M1**

Hi Lynn,

Wanted to reach out because your role sits between new business and underwriting at MassMutual. Cases decided without an exam carry declared build figures.

Through FitXpress, two photos return a Smart Scales weight estimate, and a flag appears for gaps above a threshold the carrier sets. One timestamped record goes to the file.

When a new evidence idea needs a hearing at MassMutual, how does it get one?

Nick

**M2**

Hi Lynn,

The useful next step is a read-only comparison: nothing reaches a decision while flags are counted and set against paramedical exam cases.

FitXpress is not a medical device and does not make underwriting decisions.

If someone else hears new evidence ideas first, point me to them. Talking it through is simple to arrange at https://meetings.hubspot.com/nick-omelchak

Nick

### Kathleen Coughlin · DI Chief Underwriter, AVP · lane underwriting · P2 · `kathleen-coughlin-38415319`

**M1**

Hi Kathleen,

Had a thought after seeing New DI Enhancements, MassMutual's January update. DI applications without an exam carry the applicant's own declared build.

FitXpress returns a Smart Scales weight estimate from two photos, with BMI calculated from the declared height. A flag appears for gaps above a threshold MassMutual sets, and one record lands on the case.

What would a shadow evaluation have to show your DI team before you trusted any output near a case?

Nick

**M2**

Hi Kathleen,

A shadow evaluation keeps outputs out of DI decisions and reports how often a flag fires, compared with the build measured on cases that did have an exam.

FitXpress is not a medical device and does not make underwriting decisions.

Booking a time to outline the DI evaluation is easy at https://meetings.hubspot.com/nick-omelchak

Nick

### Alycia Bellody · Head of Life New Business · lane proposition · P1 · `alycia-bellody-055726335`

**M1**

Hi Alycia,

Quick one on MassMutual's life application, where underwriting and new business meet. Accelerated cases without an exam run on the height and weight the applicant enters.

Two photos in the e-application give FitXpress a Smart Scales weight estimate, and a flag appears only when the gap crosses the threshold MassMutual sets. One timestamped record goes back to the case.

Where in the life application would a photo step cost applicants the least effort?

Nick

**M2**

Hi Alycia,

Completion is the open point on any new step. Placement and drop-off get measured first, with outputs kept away from every case.

A walk through where the step sits in an accelerated application is at https://3dlook.ai/for-insurance-underwriting/

FitXpress is not a medical device and does not make underwriting decisions.

A call on where the photo step costs applicants least is open at https://meetings.hubspot.com/nick-omelchak

Nick

### Brandon Smithhart · Underwriting Platform Head · lane underwriting · P2 · `brandon-smithhart-b6184485`

**M1**

Hi Brandon,

Caught my eye: the rules and automation behind MassMutual's accelerated cases are where a new evidence flag would land. Build there arrives as stated figures from the application.

The FitXpress step takes two photos and returns a Smart Scales weight estimate and a timestamped record, raising a flag only above a threshold MassMutual sets.

Would that flag fit your platform as a referral rule or as an item for the underwriter's screen?

Nick

**M2**

Hi Brandon,

One timestamped record per applicant arrives through an API, with web and mobile SDKs covering the capture step. A platform takes in the flag and the record behind it.

The record, the API and the SDKs are laid out at https://3dlook.ai/for-insurance-underwriting/

FitXpress is not a medical device and does not make underwriting decisions.

A time for going through the record fields and the referral rule can be chosen at https://meetings.hubspot.com/nick-omelchak

Nick

### Dan Garant · Head of Data Science - Underwriting · lane underwriting · P2 · `danielgarant`

**M1**

Hi Dan,

Curious about your take on MassExpress, where some eligible applicants are held out at random for control and audit. Cases outside the holdout carry declared build only.

A FitXpress scan of two photos adds a Smart Scales weight estimate, with a flag raised only for gaps above a threshold MassMutual sets.

How would you want agreement with the holdouts scored for a signal like that?

Nick

**M2**

Hi Dan,

The holdouts are the control. A shadow evaluation can score flag agreement against them alone, with outputs kept out of every decision.

FitXpress is not a medical device and does not make underwriting decisions.

Outlining a scoring design for the holdouts together starts with a time from https://meetings.hubspot.com/nick-omelchak

Nick

## Swiss Re Americas (9)

### Eric Hoerr · Vice President, Underwriting · lane reinsurance · P2 · `eric-hoerr-certified-falu-flmi-071b77b1`

**M1**

Hi Eric,

Quick thought on client accelerated cases where no paramedical exam takes place. Build there rests on the height and weight the applicant enters.

In FitXpress, two photos give a Smart Scales weight estimate and a timestamped record. A flag appears when the gap crosses a threshold the client sets.

How do those cases treat build today at Swiss Re Americas?

Nick

**M2**

Hi Eric,

On accelerated client cases with no paramed, a shadow evaluation compares flag counts with the build measured on the client's exam cases.

FitXpress is not a medical device and does not make underwriting decisions.

A conversation about running it for a client is open at https://meetings.hubspot.com/nick-omelchak

Nick

### Kevin O'Hanlon · Vice President & Underwriting Client Relationship Lead · lane reinsurance · P2 · `kevin-m-o-hanlon`

**M1**

Hi Kevin,

Curious about your take, given your life and disability background. On DI cases without an exam, build comes down to declared figures.

FitXpress returns a Smart Scales weight estimate from two photos, with a flag above a threshold the client sets.

Does build carry the same weight on DI as on life at Swiss Re Americas?

Nick

**M2**

Hi Kevin,

DI and life can take different thresholds, since each client sets its own. An evaluation counts flags separately for each line before any output reaches a case.

FitXpress is not a medical device and does not make underwriting decisions.

Comparing the two lines is a fair topic for a conversation at https://meetings.hubspot.com/nick-omelchak

Nick

### Cynthia Landry · Vice President of Life Underwriting at Swiss Re Life and Health · lane reinsurance · P2 · `cynthia-landry-922908a2`

**M1**

Hi Cynthia,

Got me thinking about Life Guide, where build guidance sits at Swiss Re Americas. On accelerated cases the weight on file is the applicant's entry.

Two photos in the e-application give FitXpress a Smart Scales weight estimate and a BMI from the declared height. A flag appears only above a threshold the client sets.

How would a gap between declared and estimated weight read against Life Guide's build guidance?

Nick

**M2**

Hi Cynthia,

The flag refers gaps well above the estimate's error. If a client wanted it read against the build guidance in Life Guide, the client would set the threshold and the underwriter would decide.

FitXpress is not a medical device and does not make underwriting decisions.

I can walk through that reading on a call at https://meetings.hubspot.com/nick-omelchak

Nick

### Mandy Bovan · Vice President, Manager Underwriting Solutions · lane reinsurance · P2 · `mandy-bovan-almi-acs-33055198`

**M1**

Hi Mandy,

Caught my eye: Magnum Select allows insurers to configure selected rules at Swiss Re Americas. Build is one place a configured rule needs an input.

A step of two photos in FitXpress returns a Smart Scales weight estimate and a flag above the threshold the client sets.

Where in Magnum would a build referral rule belong?

Nick

**M2**

Hi Mandy,

A rule needs only the flag and one timestamped record, delivered by API. A read-only run then shows how many cases a given threshold would refer.

What the API returns is described at https://3dlook.ai/for-insurance-underwriting/

FitXpress is not a medical device and does not make underwriting decisions.

If configuration lives with another team, a name there would help. I would be glad to cover the rule once a time is set at https://meetings.hubspot.com/nick-omelchak

Nick

### Bess Ganeff · Senior Vice President and Head of Underwriting Americas · lane reinsurance · P1 · `bess-ganeff-07a5b022`

**M1**

Hi Bess,

Noticed that Magnum runs on Life Guide at Swiss Re Americas. On accelerated cases, the build input is a declared height and weight.

FitXpress takes two photos in a carrier's e-application. Smart Scales estimates weight, and a flag appears when the gap crosses a threshold the client sets, with one timestamped record.

How would you design a one-client shadow evaluation of build evidence?

Nick

**M2**

Hi Bess,

The design for one client is short: flags counted at the thresholds the client chooses, compared with the build measured on its paramedical exam cases, with outputs out of decisions throughout.

How the step looks inside an application is shown at https://3dlook.ai/for-insurance-underwriting/

FitXpress is not a medical device and does not make underwriting decisions.

I would welcome shaping that evaluation with you, and a time can be found at https://meetings.hubspot.com/nick-omelchak

Nick

### Vicki Garrett · Vice President, U.S. Facultative Underwriting Manager · lane reinsurance · P2 · `vicki-garrett-54256920`

**M1**

Hi Vicki,

Spotted something in your remit: client relationships on facultative underwriting at Swiss Re Americas. Accelerated cases bring a height and weight that the applicant enters.

From two photos, FitXpress adds a Smart Scales weight estimate and a flag above the client's threshold, with one timestamped record.

Is remote build evidence a topic clients have raised with you on accelerated cases?

Nick

**M2**

Hi Vicki,

If a client does ask, the answer can be concrete: a record per applicant with a flag above the carrier's threshold, and a read-only comparison that keeps outputs out of decisions.

FitXpress is not a medical device and does not make underwriting decisions.

If those questions land with another team first, send me their way. Preparing an answer to that client question together starts at https://meetings.hubspot.com/nick-omelchak

Nick

### Dave Loparco · Vice President, Head of U.S. Underwriting Risk Management · lane reinsurance · P2 · `dave-loparco-3604241ab`

**M1**

Hi Dave,

Couldn't help but ask about program monitoring at Swiss Re Americas: a build flag could be one more thing it counts. In those programs the build field holds declared figures.

From FitXpress, two photos give a Smart Scales weight estimate and a flag above a threshold the client sets, kept as one timestamped record.

How does risk management look at build in a client's monitored program?

Nick

**M2**

Hi Dave,

The record carries a timestamp and a threshold, allowing program monitoring to count build flags beside its other checks with no outcome attached.

FitXpress is not a medical device and does not make underwriting decisions.

A call on how monitoring could use those counts can be booked at https://meetings.hubspot.com/nick-omelchak

Nick

### Samrat Dua · Chief Digital & Technology Officer, Swiss Re Reinsurance · lane technical-integration · P3 · `samrat-dua`

**M1**

Hi Samrat,

This stood out: Magnum is offered in three forms, which makes the API boundary of any new evidence step matter at Swiss Re Americas.

FitXpress is an API and SDKs step in a carrier's e-application: two photos in, a Smart Scales weight estimate and one timestamped record out. A flag appears above a threshold the client sets.

How is a new data vendor's API reviewed before it sits next to Magnum?

Nick

**M2**

Hi Samrat,

Integration runs on a REST API with web and mobile SDKs. Data moves over TLS and rests under S3-managed encryption.

Photos are deleted after processing or within 30 days per the carrier's policy. The privacy FAQ at https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/ covers the rest of the data handling

FitXpress is not a medical device and does not make underwriting decisions.

Walking through the integration is easy to arrange at https://meetings.hubspot.com/nick-omelchak

Nick

### Kimberly Poulopoulos · Head Mortality Innovation & Transformation, Senior Vice President · lane reinsurance · P2 · `kimberly-poulopoulos`

**M1**

Hi Kimberly,

Made me think about mortality innovation at Swiss Re Americas: a new evidence source has to travel from an idea to a client's accelerated program. Those cases carry declared build figures.

The FitXpress scan takes two photos and returns a Smart Scales weight estimate, with a flag above a threshold the client sets.

What has to be true for a new evidence source to move into a client program?

Nick

**M2**

Hi Kimberly,

One route from innovation to a client program is a shadow evaluation with a single client: outputs stay out of decisions, and flag counts are the readout.

The step in an application is shown at https://3dlook.ai/for-insurance-underwriting/

FitXpress is not a medical device and does not make underwriting decisions.

Book a time to plan that route at https://meetings.hubspot.com/nick-omelchak

Nick

## Mutual of Omaha (8)

### Kurtis Stewart · Senior Vice President, Underwriting · lane underwriting · P2 · `kurtis-stewart-50446643`

**M1**

Hi Kurtis,

Noticed that Mutual of Omaha's accelerated program asks build to sit within its own accelerated build chart.

Two photos in the e-application give FitXpress a Smart Scales weight estimate, and a flag reaches underwriting only when the gap to declared weight crosses the carrier's threshold.

Where on that chart would a gap between declared and estimated weight start to matter?

Nick

**M2**

Hi Kurtis,

A shadow evaluation counts how often flags appear against that chart on accelerated files, then compares them with build from fluidless and paramedical cases. FitXpress is not a medical device and does not make underwriting decisions.

The landing page shows how that comparison is set up: https://3dlook.ai/for-insurance-underwriting/

Worth a call on how the chart and the flag would meet? My calendar is at https://meetings.hubspot.com/nick-omelchak

Nick

### Marty Johnson · Vice President Life Underwriting · lane underwriting · P2 · `marty-johnson-a25b8ab8`

**M1**

Hi Marty,

Curious how electronic drop tickets move accelerated cases at Mutual of Omaha, where no paramed is required.

FitXpress takes two photos in the e-application, returns a Smart Scales weight estimate with BMI from the declared height, and flags a gap past the carrier's threshold in one timestamped record.

What would an underwriter want to see attached to a drop-ticket file from a step like that?

Nick

**M2**

Hi Marty,

Each applicant would have one timestamped record returned to Mutual of Omaha's systems only, and the carrier's rules decide what follows. FitXpress is not a medical device and does not make underwriting decisions.

Open to a call on what that record should look like? Times are listed at https://meetings.hubspot.com/nick-omelchak

Nick

### Timothy Tse · VP & Medical Director · lane medical · P2 · `timothy-tse-md-mba-1b328a3b`

**M1**

Hi Timothy,

Caught the line in Mutual of Omaha's underwriting guide about unisex build charts.

Smart Scales turns two photos into a weight estimate for FitXpress, and the carrier sets the gap that raises a flag in the timestamped record.

What would you want an estimate to demonstrate before it sits beside those charts?

Nick

**M2**

Hi Timothy,

Where an estimate sits beside a build chart, the figure to weigh is approximately 3.5% mean absolute error under evaluated conditions, and the estimate is not a scale reading. FitXpress is not a medical device and does not make underwriting decisions.

Time for a call on how that figure should be read is open at https://meetings.hubspot.com/nick-omelchak

Nick

### Anjali Masand · VP & Medical Director · lane medical · P2 · `anjali-masand-md-dbim-44966a7a`

**M1**

Hi Anjali,

Spotted that Mutual of Omaha's build charts are unisex.

FitXpress estimates weight with Smart Scales from two photos taken in the e-application, then flags the gap to the declared weight only above the carrier's threshold.

How wide a gap between declared and estimated weight would you want before a file is referred?

Nick

**M2**

Hi Anjali,

The flag only refers a file to an underwriter, and Mutual of Omaha sets the threshold and keeps the decision. FitXpress is not a medical device and does not make underwriting decisions.

The landing page sets out the decision boundary in plain terms: https://3dlook.ai/for-insurance-underwriting/

A call on where the boundary should sit is easy to arrange at https://meetings.hubspot.com/nick-omelchak

Nick

### Tracey Schifferdecker · Chief Individual Life Underwriter · lane underwriting · P3 · `tracey-schifferdecker-55584a72`

**M1**

Hi Tracey,

Had a thought about fit credits, where Mutual of Omaha lists preferred or better build among the characteristics.

A step of two photos in the e-application gives FitXpress a Smart Scales weight estimate and a BMI calculated from the declared height, with a flag at the carrier's threshold.

Where does build evidence come from for a no-paramed case that is considered for fit credits?

Nick

**M2**

Hi Tracey,

For fit credit files, a shadow run would show how the flags line up with the preferred or better build criterion. FitXpress is not a medical device and does not make underwriting decisions.

A short call on that criterion would cover it, at https://meetings.hubspot.com/nick-omelchak

Nick

### Thomas Ferguson · Chief Underwriter · lane underwriting · P3 · `thomas-ferguson-33b4521b`

**M1**

Hi Thomas,

Quick thought: Mutual of Omaha sets out accelerated, fluidless and fit credit programs in one guide.

With a step of two photos, FitXpress produces a timestamped record holding a Smart Scales weight estimate, and a flag appears when it differs from the declared weight by more than the carrier set.

What would a shadow evaluation need to demonstrate before an underwriter saw a record like this?

Nick

**M2**

Hi Thomas,

The evaluation path keeps outputs away from decisions and compares flags with paramedical exam cases, where build was measured. FitXpress is not a medical device and does not make underwriting decisions.

The landing page outlines the evaluation path step by step: https://3dlook.ai/for-insurance-underwriting/

Want to compare notes on the design? A slot is bookable at https://meetings.hubspot.com/nick-omelchak

Nick

### Donna Rogers · Supervising, Chief Underwriter · lane underwriting · P3 · `donna-rogers-98304012`

**M1**

Hi Donna,

Got me thinking: Mutual of Omaha's fluidless program for larger cases leans on a recent annual or executive physical.

Two photos taken in the e-application give FitXpress a Smart Scales weight estimate, flagged against the carrier's threshold and stored as one timestamped record.

What fills the gap on a fluidless file where no recent physical exists?

Nick

**M2**

Hi Donna,

On fluidless files without a physical, one timestamped record would add build evidence, and the carrier's rules stay in charge. FitXpress is not a medical device and does not make underwriting decisions.

The landing page shows where such a record sits for fluidless files: https://3dlook.ai/for-insurance-underwriting/

Here is my calendar for a call on that gap: https://meetings.hubspot.com/nick-omelchak

Nick

### Mike Bauer · Supervising Chief Underwriter · lane underwriting · P3 · `mike-bauer-582a2481`

**M1**

Hi Mike,

Made me think: Mutual of Omaha's accelerated program has no paramed requirement and its own build chart.

Smart Scales gives FitXpress a weight estimate from two photos in the e-application, and the carrier's threshold decides when a flag is raised.

Who would take a build flag first on your team, and what would they do with it?

Nick

**M2**

Hi Mike,

A flag is a referral only, and it appears above the threshold Mutual of Omaha picks. FitXpress is not a medical device and does not make underwriting decisions.

A time for a call on the referral route is open at https://meetings.hubspot.com/nick-omelchak

Nick

## Thrivent (8)

### Rebecca Severson · Chief Underwriter · lane underwriting · P2 · `rebecca-severson-certified-falu-flmi-ara-acs-5536552b`

**M1**

Hi Rebecca,

Caught that Thrivent's term page says every applicant is underwritten into the most appropriate risk class.

FitXpress turns two photos into a Smart Scales weight estimate, and the carrier sets the gap that raises a flag in the timestamped record.

Which gaps between declared and estimated weight would move a case to a different class?

Nick

**M2**

Hi Rebecca,

A shadow run would count the files that produce a flag while underwriting carries on as usual. FitXpress is not a medical device and does not make underwriting decisions.

Time for a call on those gaps is open at https://meetings.hubspot.com/nick-omelchak

Nick

### Kenny Membreno · Chief Information Security & Privacy Officer · lane technical-integration · P3 · `kenny-membreno-582a091a`

**M1**

Hi Kenny,

Had a thought about Thrivent's term journey, which starts with an online quote and finishes with a financial professional.

FitXpress returns, from two photos, a Smart Scales estimate on a random identifier, flagged at the carrier's threshold. Photos are deleted after processing or within 30 days per the carrier's policy.

How is a new data vendor reviewed before it joins the new-business journey?

Nick

**M2**

Hi Kenny,

Data handling is TLS in transit and S3-managed encryption at rest. Retained photos are blurred, faces are obscured at capture and scan records sit on random identifiers. FitXpress is not a medical device and does not make underwriting decisions.

The privacy FAQ covers these points for a security review: https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/

Calendar time is open for a call on vendor review at https://meetings.hubspot.com/nick-omelchak

Nick

### Ryan Hawkins · Chief Technology Officer · lane technical-integration · P3 · `ryanphawkins`

**M1**

Hi Ryan,

Quick thought on Thrivent's paramed split: some applicants need an exam and some do not.

Through an SDK step, FitXpress takes two photos in the e-application and returns a Smart Scales weight estimate, with a flag when the gap to declared weight passes the carrier's threshold.

How are new steps scoped for the e-application?

Nick

**M2**

Hi Ryan,

Integration is a REST API or web and mobile SDKs, with one record per applicant coming back. FitXpress is not a medical device and does not make underwriting decisions.

I can walk through the SDK on a call, and my calendar is at https://meetings.hubspot.com/nick-omelchak

Nick

### Jeffrey Einhorn · Chief Technology Officer · lane technical-integration · P3 · `jeffrey-einhorn`

**M1**

Hi Jeffrey,

Got me thinking about Thrivent's online quote, which starts the term application before a financial professional completes it.

With two photos from the e-application, FitXpress returns a structured record holding a Smart Scales weight estimate and a threshold flag.

Where would a structured record land in the underwriting workbench or case system?

Nick

**M2**

Hi Jeffrey,

The record returns through the API with a timestamp, ready for case management. FitXpress is not a medical device and does not make underwriting decisions. Security documents go through legal@3dlook.me.

The privacy FAQ shows how that record is handled end to end: https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/

A call on the case system side is open at https://meetings.hubspot.com/nick-omelchak

Nick

### Rhonda Steffel-Heling · Associate Medical Director · lane medical · P2 · `rhonda-steffel-heling-30b798a6`

**M1**

Hi Rhonda,

Spotted that Thrivent's term page notes some applicants need a paramed exam and others do not.

Two photos in the e-application give FitXpress a Smart Scales weight estimate, flagged against the carrier's threshold in one timestamped record.

What gap between declared and estimated weight would you want referred?

Nick

**M2**

Hi Rhonda,

The carrier sets the threshold, the flag refers a file and an underwriter decides. FitXpress is not a medical device and does not make underwriting decisions.

If thresholds are decided above your seat, a pointer to who decides is welcome.

A call to look at where the line sits is open at https://meetings.hubspot.com/nick-omelchak

Nick

### Ronelle Moe · Chief Medical Director · lane medical · P1 · `ronelle-moe-7a4a70280`

**M1**

Hi Ronelle,

Noticed that Thrivent's term page says some applicants may need no medical exam and complete a Declaration of Insurability instead.

A step of two photos in the e-application gives FitXpress a Smart Scales weight estimate and a BMI calculated from the declared height, with a flag at the carrier's threshold.

What use of a software weight estimate would you consider reasonable where no paramed happens?

Nick

**M2**

Hi Ronelle,

Smart Scales gives an estimate of approximately 3.5% mean absolute error under evaluated conditions; the estimate is not a scale reading, and Thrivent sets any threshold. FitXpress is not a medical device and does not make underwriting decisions.

The landing page lays out the decision boundary in a few lines: https://3dlook.ai/for-insurance-underwriting/

I would value a call on how that error should be read, and a time can be picked at https://meetings.hubspot.com/nick-omelchak

Nick

### Jean Pfundtner · Chief Life Underwriter · lane underwriting · P1 · `jean-pfundtner-58626076`

**M1**

Hi Jean,

Curious how Thrivent's term cases decided without an exam rely on the Declaration of Insurability.

FitXpress takes two photos in the e-application, returns a Smart Scales weight estimate with BMI from the declared height, and flags a gap past the carrier's threshold in one timestamped record.

What does underwriting review for build on Declaration of Insurability cases?

Nick

**M2**

Hi Jean,

A shadow evaluation would show the flags next to build from paramedical exam cases, with the carrier's rules unchanged. FitXpress is not a medical device and does not make underwriting decisions.

The landing page describes how the evaluation compares those two sources: https://3dlook.ai/for-insurance-underwriting/

Worth a call on how the comparison would work? Times are open at https://meetings.hubspot.com/nick-omelchak

Nick

### Brett Brunick · Chief Digital & Technology Officer · lane technical-integration · P3 · `bbrunick`

**M1**

Hi Brett,

Made me think: Thrivent's term policy is finished with a financial professional after the online start.

Smart Scales estimates weight from two photos in the journey, and FitXpress raises a flag only above the carrier's threshold.

Where would a photo step sit relative to the hand-off to the financial professional?

Nick

**M2**

Hi Brett,

Web and mobile SDKs can place the step at either point, with the record returned to Thrivent alone. FitXpress is not a medical device and does not make underwriting decisions.

For a call on where the step belongs, book through my calendar at https://meetings.hubspot.com/nick-omelchak

Nick

## The Standard (8)

### Kevin Erdahl · Vice President, Underwriting · lane underwriting · P3 · `kevinerdahl1`

**M1**

Hi Kevin,

Spotted that The Standard's underwriting toolkit shows when lab work or physical measurements are needed.

FitXpress estimates weight with Smart Scales from two photos taken in the e-application, then flags the gap to the declared weight only above the carrier's threshold.

What leads to an order for physical measurements on an IDI case?

Nick

**M2**

Hi Kevin,

Where no measurements are ordered, a timestamped record adds build evidence to the file, and the carrier's rules decide its use. FitXpress is not a medical device and does not make underwriting decisions.

The landing page shows what that record contains for an IDI file: https://3dlook.ai/for-insurance-underwriting/

If measurement orders are set by a medical team, a name there would help.

A call on where orders and flags meet is easy to book at https://meetings.hubspot.com/nick-omelchak

Nick

### Jim Teague · Regional Director Individual Disability Income · lane referral · P3 · `teague-jim-481208a`

**M1**

Hi Jim,

Got me thinking about what applicants meet in The Standard's online medical questionnaire for IDI.

Smart Scales turns two photos into a weight estimate for FitXpress, and the carrier sets the gap that raises a flag in a timestamped record.

What do advisors in your region hear most about that questionnaire?

Nick

**M2**

Hi Jim,

Advisors' feedback on the questionnaire is the best guide to where a step of two photos could fit, and the record stays with the carrier. FitXpress is not a medical device and does not make underwriting decisions.

The landing page shows what applicants would be asked to do: https://3dlook.ai/for-insurance-underwriting/

If underwriting rules for the questionnaire sit with another team, I would welcome a pointer to them.

Your region's view would shape the call, and my calendar is at https://meetings.hubspot.com/nick-omelchak

Nick

### Jeremy Horner · Vice President, Individual Disability Insurance and Corporate Development · lane proposition · P2 · `jeremy-horner-b549853`

**M1**

Hi Jeremy,

Curious how the eApp and the online medical questionnaire fit together for IDI applicants at The Standard.

FitXpress takes two photos in the e-application, returns a Smart Scales weight estimate with BMI from the declared height, and flags a gap past the carrier's threshold in one timestamped record.

Where in the IDI application would a two-photo step sit best for an applicant?

Nick

**M2**

Hi Jeremy,

The scan completes under 45 seconds from the photos to structured results. The record goes only to the carrier. FitXpress is not a medical device and does not make underwriting decisions.

The landing page shows the step inside an application journey: https://3dlook.ai/for-insurance-underwriting/

If a call on step placement is useful, times are open at https://meetings.hubspot.com/nick-omelchak

Nick

### Jeffrey Nattis · Director of Medical Underwriting · lane underwriting · P3 · `jeffrey-nattis-35a8964`

**M1**

Hi Jeffrey,

This stood out: the IDI toolkit at The Standard separates cases needing lab work or measurements from the rest.

A step of two photos in the e-application gives FitXpress a Smart Scales weight estimate and a BMI calculated from the declared height, with a flag at the carrier's threshold.

How does medical underwriting weigh a declared weight against a measured one?

Nick

**M2**

Hi Jeffrey,

The Smart Scales weight is a software estimate, the carrier sets the threshold and underwriters decide. FitXpress is not a medical device and does not make underwriting decisions.

Should another team own the comparison of declared and measured weight, send me their way.

Calendar time for a call on that comparison is open at https://meetings.hubspot.com/nick-omelchak

Nick

### Jody Pfeifer · Chief Product Officer · lane proposition · P3 · `jody-pfeifer-70629215`

**M1**

Hi Jody,

Quick thought on the online medical questionnaire in The Standard's IDI application.

FitXpress returns, from two photos, a Smart Scales estimate in one timestamped record, flagged when the gap to declared weight passes the carrier's threshold.

How would you test a new application step with advisors and judge its drop-off?

Nick

**M2**

Hi Jody,

Completion would be measured inside the evaluation, and the carrier keeps every decision. FitXpress is not a medical device and does not make underwriting decisions.

If the IDI journey belongs to a business lead instead, tell me who.

I can set aside time for a call on how the step would be tested, at https://meetings.hubspot.com/nick-omelchak

Nick

### Michael Ash-Dollowitch · Director & Chief Underwriter, IDI · lane underwriting · P1 · `michael-ash-dollowitch`

**M1**

Hi Michael,

Noticed that Simplified Underwriting at The Standard drops lab tests and income documentation for eligible IDI applicants.

Two photos in the e-application give FitXpress a Smart Scales weight estimate, and a flag reaches underwriting only when the gap to declared weight crosses the carrier's threshold.

On simplified files, which evidence would you compare a weight estimate with?

Nick

**M2**

Hi Michael,

A shadow evaluation compares the flags with build from IDI cases where measurements were ordered, leaving every rule as it is. FitXpress is not a medical device and does not make underwriting decisions.

The landing page walks through that comparison for a rules owner: https://3dlook.ai/for-insurance-underwriting/

Worth a call on how that comparison would run? A time can be booked at https://meetings.hubspot.com/nick-omelchak

Nick

### Rajesh Mondkar · AVP Digital Transformation · lane referral · P3 · `rajesh-mondkar-12a1293a`

**M1**

Hi Rajesh,

Wanted to ask about IDI new business at The Standard, where applicants can use the eApp or a phone interview.

Two photos taken in the e-application give FitXpress a Smart Scales weight estimate, returned with a timestamped record and a flag above the carrier's threshold.

When a new step joins the IDI eApp, what does digital transformation look at first?

Nick

**M2**

Hi Rajesh,

Integration runs through a REST API and web and mobile SDKs, returning one record per applicant. FitXpress is not a medical device and does not make underwriting decisions.

If intake for new steps runs through someone else, point me to them.

I am glad to cover the eApp integration on a call, at https://meetings.hubspot.com/nick-omelchak

Nick

### Tony Fung · Assistant Vice President, IDI Underwriting and GSI · lane underwriting · P2 · `tony-fung-9129169`

**M1**

Hi Tony,

Caught that simplified IDI cases at The Standard go without income documentation.

With a step of two photos, FitXpress produces a timestamped record holding a Smart Scales weight estimate, and a flag appears when it differs from the declared weight by more than the carrier set.

What would your team want a shadow evaluation to show before any output reached a case?

Nick

**M2**

Hi Tony,

An evaluation would count how many simplified files produce a flag, with nothing shown to underwriters meanwhile. FitXpress is not a medical device and does not make underwriting decisions.

Happy to talk through the design on a call whenever it suits, at https://meetings.hubspot.com/nick-omelchak

Nick

## Munich Re Life US (7)

### Jennifer Dalton · Director of Accelerated Underwriting · lane reinsurance · P2 · `jennifer-dalton-9408a339`

**M1**

Hi Jennifer,

Noticed that alitheia at Munich Re Life US has a customizable rules designer and can be used whole or in parts.

Two photos in the e-application give FitXpress a Smart Scales weight estimate, and a flag goes out only when the gap to the declared weight passes a threshold the carrier sets.

Where in that rules designer would you place a build referral rule for accelerated cases?

Nick

**M2**

Hi Jennifer,

A shadow evaluation would run on one client's accelerated files, count the flags at each candidate threshold and keep every output away from the case. FitXpress is not a medical device and does not make underwriting decisions.

The landing page shows how an evaluation like that is laid out for a rules team: https://3dlook.ai/for-insurance-underwriting/

If a call on where the rule would sit is useful, a slot can be booked at https://meetings.hubspot.com/nick-omelchak

Nick

### Greg Dewey · 2nd VP, Underwriting Services · lane reinsurance · P2 · `greg-dewey-982920221`

**M1**

Hi Greg,

Curious about the underwriting workbench in alitheia at Munich Re Life US and the order its requirements arrive in.

FitXpress takes two photos in the e-application, returns a Smart Scales weight estimate with BMI from the declared height, and flags a gap past the carrier's threshold in one timestamped record.

Where in that order could a build record slot in, for a client that wants it?

Nick

**M2**

Hi Greg,

A shadow run could place the record beside the requirements the workbench already orders, with underwriters seeing nothing until the client carrier decides. FitXpress is not a medical device and does not make underwriting decisions.

My calendar is open for a call on where the record would sit in that order, at https://meetings.hubspot.com/nick-omelchak

Nick

### Shane Banks · Director, Underwriting Pricing and Client Support · lane reinsurance · P2 · `shane-banks-2a7a2852`

**M1**

Hi Shane,

Caught that alitheia at Munich Re Life US can be used whole or in parts.

With a step of two photos, FitXpress produces a timestamped record holding a Smart Scales weight estimate, and a flag appears when it differs from the declared weight by more than the carrier set.

What does your side need to see in a new source before a client's accelerated program tries it?

Nick

**M2**

Hi Shane,

The evaluation could run with one client carrier over a fixed period: their accelerated files pass through the scan in shadow, flags are counted and no underwriter sees them. FitXpress is not a medical device and does not make underwriting decisions.

The landing page lists what a client evaluation covers: https://3dlook.ai/for-insurance-underwriting/

A call to compare that design with how you run evaluations is easy to set up at https://meetings.hubspot.com/nick-omelchak

Nick

### Patti Arellano · Head of Individual Life New Business · lane reinsurance · P2 · `pattiarellano`

**M1**

Hi Patti,

Spotted that alitheia at Munich Re Life US draws on EHRs and a growing suite of data sources.

FitXpress estimates weight with Smart Scales from two photos taken in the e-application, then flags the gap to the declared weight only above the carrier's threshold. The record comes back timestamped.

When a client carrier's new business team asks about extra evidence on accelerated cases, what comes up first?

Nick

**M2**

Hi Patti,

A build record at application gives new business files a second source for height and weight, and the client carrier sets every threshold. FitXpress is not a medical device and does not make underwriting decisions.

Happy to walk through what a build record means for those files on a call, at https://meetings.hubspot.com/nick-omelchak

Nick

### Robert Lund · Vice President and Medical Director · lane medical · P2 · `robert-lund-56708349`

**M1**

Hi Robert,

This stood out: alitheia at Munich Re Life US is described as a rapid risk assessment and decisioning platform.

A step of two photos in the e-application gives FitXpress a Smart Scales weight estimate and a BMI calculated from the declared height, with a flag at the carrier's threshold.

What would make you comfortable with a weight estimate from two photos inside a client's accelerated rules?

Nick

**M2**

Hi Robert,

Smart Scales returns a weight estimate with approximately 3.5% mean absolute error under evaluated conditions, which is not a scale reading. FitXpress is not a medical device and does not make underwriting decisions.

I am free for a call on what would settle your questions about that figure, at https://meetings.hubspot.com/nick-omelchak

Nick

### Gina Guzman · Vice President & Chief Medical Director · lane medical · P2 · `gina-guzman-67396b148`

**M1**

Hi Gina,

Got me thinking about the rules designer inside alitheia at Munich Re Life US and who signs off on what goes into it.

Smart Scales turns two photos in the e-application into a weight estimate for FitXpress, and the carrier sets the gap that raises a flag in the timestamped record.

At what gap between declared and estimated weight would you want a file referred to an underwriter?

Nick

**M2**

Hi Gina,

The threshold belongs to the client carrier, and the flag refers a file to an underwriter for review. FitXpress is not a medical device and does not make underwriting decisions.

The landing page shows where the decision boundary sits in the flow: https://3dlook.ai/for-insurance-underwriting/

Time on my calendar is open for a call on where a threshold belongs, at https://meetings.hubspot.com/nick-omelchak

Nick

### Brad Heltemes · VP and Medical Director, R&D · lane medical · P2 · `brad-heltemes-109a342b`

**M1**

Hi Brad,

Quick thought: alitheia at Munich Re Life US draws on EHRs and a growing suite of data sources, which makes R&D intake a real question.

FitXpress returns, from two photos, a Smart Scales estimate as a timestamped record, flagged when the gap to declared weight passes the carrier's threshold.

What would R&D want to see from a new source like this before any client carrier evaluates it?

Nick

**M2**

Hi Brad,

Flags from the scan would be compared with build from paramedical exam cases a client carrier runs, leaving every decision where it is. FitXpress is not a medical device and does not make underwriting decisions.

Would a call to map that evaluation for R&D be useful? Times are open at https://meetings.hubspot.com/nick-omelchak

Nick

## Securian Financial (7)

### Gay Kemmis · 2nd VP, Life Underwriting Operations · lane underwriting · P2 · `gay-kemmis-76523410`

**M1**

Hi Gay,

Spotted something in the WriteFit submission guide: WriteFit runs only on eApp, and clients who do not qualify move to traditional underwriting with labs.

FitXpress adds its own step at the eApp: two photos, a weight estimate from Smart Scales, BMI from the declared height and, above the carrier's threshold, a flag on a timestamped record.

Between the eApp and the tele-interview, is there a point where build gets reviewed in life underwriting operations?

Nick

**M2**

Hi Gay,

For case flow, what matters is what lands on the case: one timestamped record, with any referral arriving as a queue item the underwriters own.

FitXpress is not a medical device and does not make underwriting decisions. You can arrange a call on how that queue item would travel through Securian's case flow at https://meetings.hubspot.com/nick-omelchak

Nick

### Robert Reynolds · Director Individual Life Financial Management · lane referral · P3 · `robert-reynolds-77626a8`

**M1**

Hi Robert,

Had a thought on Securian's accelerated route for individual life, where the weight on file is the one the applicant enters.

FitXpress returns, from two photos in the eApp, one timestamped record with a Smart Scales weight estimate, BMI from the declared height and a flag above the carrier's threshold.

How does individual life finance get a first view of a new evidence step before accelerated cases use it?

Nick

**M2**

Hi Robert,

A step like this arrives as one record per applicant, and during evaluation its outputs stay outside decisions, which leaves time for finance to review it before any plan depends on it.

FitXpress is not a medical device and does not make underwriting decisions. If this belongs with whoever owns underwriting rules or the new-business journey, point me to them. Otherwise a call on how finance would review such a step can be booked at https://meetings.hubspot.com/nick-omelchak

Nick

### Jeffrey Noren · Actuarial Director - Life Product Development · lane proposition · P2 · `jeffrey-noren-00a879231`

**M1**

Hi Jeffrey,

Got me thinking about Securian's WriteFit guide: an accelerated applicant cannot switch back to the traditional path. That makes the eApp step the moment evidence enters.

Two photos at that step would give a Smart Scales weight estimate, a flag against the carrier's threshold and one timestamped record.

Where in the WriteFit journey would you put a two-photo step, if anywhere?

Nick

**M2**

Hi Jeffrey,

The scan itself runs under 45 seconds from the photos to structured results. Completion would be measured during the evaluation.

A page showing how the step sits inside an application is at https://3dlook.ai/for-insurance-underwriting/

FitXpress is not a medical device and does not make underwriting decisions. If a different product owner runs the eApp journey, an introduction would also work. You can reserve a call on placement at https://meetings.hubspot.com/nick-omelchak

Nick

### John Helberg · Chief Underwriter, Individual Markets · lane underwriting · P1 · `john-helberg-b4544612`

**M1**

Hi John,

Noticed that Securian's Preferred Stretch Program gives better-than-published decisions in areas including build. WriteFit has no medical exam or blood test.

Two photos at the eApp step would give a Smart Scales weight estimate, a flag where the gap crosses Securian's own threshold, and a timestamped record.

Which of your build lines would a gap between declared and estimated weight be read against on WriteFit cases?

Nick

**M2**

Hi John,

A shadow run would count flags at a few thresholds and compare them with build from paramedical exam cases, and the lines you hold stay yours.

A page walking through that run for a carrier is at https://3dlook.ai/for-insurance-underwriting/

FitXpress is not a medical device and does not make underwriting decisions. A call that walks that run through against Preferred Stretch is open at https://meetings.hubspot.com/nick-omelchak

Nick

### Lara Shemtob · Medical Director · lane medical · P2 · `lara-shemtob-md-b41456236`

**M1**

Hi Lara,

This stood out: your background includes occupational health research at Imperial College. Securian's WriteFit approves after a tele-interview, with no exam behind it.

FitXpress returns a Smart Scales weight estimate from two photos in the eApp, flags a gap only above a carrier-set threshold, and returns the result as a timestamped record.

Which research questions would you want answered about a photo-based weight estimate before using it on WriteFit cases?

Nick

**M2**

Hi Lara,

An evaluation answers that kind of question in order: flags are counted, outputs stay outside decisions, and Securian reviews the evidence before choosing any threshold.

An outline of the evaluation steps is at https://3dlook.ai/for-insurance-underwriting/

FitXpress is not a medical device and does not make underwriting decisions. A call to go through your questions can be reserved at https://meetings.hubspot.com/nick-omelchak

Nick

### Shona Murray · Chief Medical Director · lane medical · P1 · `shona-murray-283910134`

**M1**

Hi Shona,

Curious about Securian's WriteFit, which decides with no medical exam or blood test. On those cases the weight on file is the one the applicant enters.

From two photos in the eApp, FitXpress returns a Smart Scales weight estimate and, when the gap against the declared figures is large, a flag at a threshold Securian chooses. BMI and a timestamped record come with it.

What would you ask a vendor first if a weight estimate were offered for WriteFit?

Nick

**M2**

Hi Shona,

Stated plainly: Smart Scales shows approximately 3.5% mean absolute error under evaluated conditions and is not a scale reading. Securian's underwriters would set any referral line above that error.

FitXpress is not a medical device and does not make underwriting decisions. Booking a call on what to ask of the estimate for WriteFit is easy at https://meetings.hubspot.com/nick-omelchak

Nick

### Brian Rock · Director & Actuary, Life Product Development · lane proposition · P2 · `brian-rock-fsa-cera-maaa-25203b142`

**M1**

Hi Brian,

Quick thought on WriteFit: clients who do not qualify move to traditional underwriting with labs, which makes the evidence collected at the start matter for routing.

FitXpress adds, at the eApp, two photos that return a Smart Scales weight estimate and a flag against the carrier's threshold on a timestamped record.

How does Securian usually test a new application step with the advisors who place the business?

Nick

**M2**

Hi Brian,

For that kind of test, the step can be offered on a share of eApp cases with its outputs kept out of decisions, and completion and drop-off are measured throughout.

FitXpress is not a medical device and does not make underwriting decisions. An introduction to whoever leads advisor distribution would be welcome. You can pick a time to talk through the test design at https://meetings.hubspot.com/nick-omelchak

Nick

## Symetra (7)

### Mary Bates · SVP Underwriting Risk Management and Strategic Direction · lane underwriting · P1 · `mary-bates-491652139`

**M1**

Hi Mary,

Curious how Symetra's Swift guidelines treat build: they use limited random holdouts and post-issue reviews as program monitoring, and instant and accelerated cases carry the height and weight entered by the applicant.

FitXpress adds two photos to the application, returning a Smart Scales weight estimate, BMI from the declared height and a flag against the threshold Symetra sets, as a timestamped record.

How do the random holdouts and post-issue reviews treat build today?

Nick

**M2**

Hi Mary,

In an evaluation, flags are counted at a range of thresholds and read against build from the holdouts the program already runs.

A page outlining how that comparison is set up is at https://3dlook.ai/for-insurance-underwriting/

FitXpress is not a medical device and does not make underwriting decisions. A call on reading flags against your holdouts can be booked at https://meetings.hubspot.com/nick-omelchak

Nick

### Mindi Work · EVP Individual Life Division and Emerging Solutions · lane proposition · P2 · `mindi-work-046a345`

**M1**

Hi Mindi,

Wanted to reach out given Emerging Solutions in your title. SwiftTerm sorts each application into one of three paths, from instant coverage to full underwriting.

FitXpress would add a step of two photos: a Smart Scales weight estimate, and a flag above a threshold Symetra sets, all on a timestamped record.

Where in the direct online journey would a two-photo step belong, if at all?

Nick

**M2**

Hi Mindi,

The scan itself runs under 45 seconds from the photos to structured results. Everything it returns goes to Symetra's systems only.

A page describing the evaluation that measures completion is at https://3dlook.ai/for-insurance-underwriting/

FitXpress is not a medical device and does not make underwriting decisions. You can find a time to talk through the online journey at https://meetings.hubspot.com/nick-omelchak

Nick

### Jamal Bodey-Burks · Chief Information Security Officer · lane technical-integration · P3 · `jamal-b-70b7b32a`

**M1**

Hi Jamal,

Couldn't help but ask about Symetra's new-business journey: a photo step means a new vendor handling images.

FitXpress returns one timestamped record through an API or SDK, built from two photos in the application: a Smart Scales weight estimate and a flag against the carrier's threshold.

How does Symetra review a new data vendor before it joins the new-business journey?

Nick

**M2**

Hi Jamal,

Photos are deleted after processing or within 30 days per the carrier's policy. Retained photos are blurred, and scan records use random identifiers, with TLS in transit and S3-managed encryption at rest.

The privacy FAQ for a vendor review is at https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/

FitXpress is not a medical device and does not make underwriting decisions. A conversation on Symetra's vendor review is open for scheduling at https://meetings.hubspot.com/nick-omelchak

Nick

### Silke Lavallee · VP, Life Product & Economics · lane proposition · P2 · `silke-lavallee`

**M1**

Hi Silke,

This stood out in your headline: product strategy and data-driven growth. Symetra's SwiftTerm page describes three application paths, and the evidence behind each one carries a cost.

On any of them, FitXpress returns a Smart Scales weight estimate from two photos, a flag when the gap crosses a carrier-set threshold, and a timestamped record carrying BMI from the declared height.

How does Symetra weigh what a new evidence input costs against what it adds to a path?

Nick

**M2**

Hi Silke,

An evaluation puts figures on that trade-off: flags are counted and compared with build in exam-based cases, before any product change is considered.

FitXpress is not a medical device and does not make underwriting decisions. You can book a call on that cost-and-value question at https://meetings.hubspot.com/nick-omelchak

Nick

### Mike Derrig · Chief Underwriter · lane underwriting · P1 · `mike-derrig-65213323`

**M1**

Hi Mike,

Noticed your background as chief underwriter at more than one carrier. Symetra gates instant coverage on a height and weight chart.

Next to that chart, FitXpress returns a weight estimate from Smart Scales built on two photos, with a flag only when the gap crosses the carrier's threshold.

Which edges of the chart would matter most if a gap between declared and estimated weight could trigger a referral?

Nick

**M2**

Hi Mike,

The flag is a referral for gaps large enough to cross a chart line or a class boundary, with the threshold set above the estimate's error. Small differences are left alone.

FitXpress is not a medical device and does not make underwriting decisions. A call about the chart edges that matter most can be set at https://meetings.hubspot.com/nick-omelchak

Nick

### Dimitri Robert · Chief Technology Officer · lane technical-integration · P3 · `dimitrirobert`

**M1**

Hi Dimitri,

Had a thought about Symetra's Swift flow: it runs a digital interview inside the application, and a photo step would sit beside it.

FitXpress is a REST API with SDKs. Two photos go in, and a timestamped record comes out with a Smart Scales weight estimate and a flag against the carrier's threshold.

How would an SDK step enter a digital interview flow like that one?

Nick

**M2**

Hi Dimitri,

On the technical points: REST API and SDKs, one record per applicant, and the decision boundary stays with the carrier.

FitXpress is not a medical device and does not make underwriting decisions. A technical call on SDK placement is easy to arrange at https://meetings.hubspot.com/nick-omelchak

Nick

### Harry Stanger · Medical Director · lane medical · P2 · `harry-stanger-6423021b3`

**M1**

Hi Harry,

Quick note on Symetra's Swift guidelines: on full underwriting, height and weight come from the paramed exam, and on instant and accelerated cases the applicant enters them.

Two photos, taken in the application, give FitXpress what it needs for a Smart Scales weight estimate and a flag against the carrier's threshold, returned as one timestamped record.

Could a weight estimate ever inform the decision to order a paramed, in your view?

Nick

**M2**

Hi Harry,

The carrier sets the threshold, the flag refers only a gap above it, and no paramedical exam or lab is replaced where the guidelines call for one.

FitXpress is not a medical device and does not make underwriting decisions. Time for a call on where a flag could sit before a paramed order? Book it at https://meetings.hubspot.com/nick-omelchak

Nick

## Nationwide (6)

### Cathy Allocco · Vice President, Underwriting, Product, and Pricing · lane underwriting · P3 · `cathy-allocco-58672618`

**M1**

Hi Cathy,

Caught my eye in Nationwide's Intelligent Underwriting guide: an abbreviated exam has the examiner collect height and weight, while accelerated decisions rest on the figures entered.

Two photos in the e-application allow FitXpress to add a Smart Scales weight estimate, a flag against the carrier's threshold and a timestamped record, with BMI worked from the declared height.

On accelerated cases, where would a gap between declared and estimated weight start to change the class?

Nick

**M2**

Hi Cathy,

The evaluation runs in shadow: flags are counted at a range of thresholds and set against build from paramedical exam cases. Nothing reaches a case until your team decides.

An outline of that shadow run is at https://3dlook.ai/for-insurance-underwriting/

FitXpress is not a medical device and does not make underwriting decisions. If a conversation on thresholds for Nationwide's accelerated cases would help, a time can be picked at https://meetings.hubspot.com/nick-omelchak

Nick

### Matt Mylroie · AVP, Life Product Management · lane proposition · P2 · `matt-mylroie-48780994`

**M1**

Hi Matt,

Got me thinking after Nationwide's indexed UL launch this year: a new permanent product brings its own application journey.

FitXpress would add a step of two photos to that journey: a Smart Scales weight estimate, BMI from the declared height, and a flag when the gap crosses the carrier's threshold, on one timestamped record.

Where in a new product's application journey would a two-photo step feel natural to you?

Nick

**M2**

Hi Matt,

The scan itself runs under 45 seconds from the photos to structured results. Completion and placement would be measured in the evaluation, on the journey you pick.

A page showing where the step sits for a carrier is at https://3dlook.ai/for-insurance-underwriting/

FitXpress is not a medical device and does not make underwriting decisions. You can reserve a call to map that journey at https://meetings.hubspot.com/nick-omelchak

Nick

### Tim Lyons · Vice President & Chief Information Security Officer · lane technical-integration · P3 · `tim-lyons-7098023`

**M1**

Hi Tim,

This stood out: a photo step inside Nationwide's new-business journey brings a new vendor handling images into it.

FitXpress sits behind an API or SDK: two photos in the e-application come back as one timestamped record with a Smart Scales weight estimate, BMI from the declared height and a flag against the carrier's threshold.

What does Nationwide's review of a new data vendor look like for a step inside the application?

Nick

**M2**

Hi Tim,

Photos are deleted after processing or within 30 days per the carrier's policy, retained photos are blurred, faces are obscured at capture, and scan records sit on random identifiers.

The privacy FAQ sets the points out for a security review, at https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/

FitXpress is not a medical device and does not make underwriting decisions. A call on Nationwide's vendor review can be booked at https://meetings.hubspot.com/nick-omelchak

Nick

### Todd Lukens · SVP, Chief Technology and Information Security Officer · lane technical-integration · P3 · `todd-lukens-7a0aa4`

**M1**

Hi Todd,

Wanted to reach out about a technical point in Nationwide's new-business journey: where a structured record from an external step lands.

FitXpress is a REST API and SDKs: from two photos in the e-application it returns one timestamped record, with a Smart Scales weight estimate and a flag against the carrier's threshold.

Which system would take such a record first, the underwriting workbench or case management?

Nick

**M2**

Hi Todd,

For an integration review the facts are short: REST API, web and mobile SDKs, and the decision boundary staying with the carrier's underwriters. The record returns to the carrier's systems only.

FitXpress is not a medical device and does not make underwriting decisions. A technical call on the record's route into Nationwide's case systems is easy to arrange at https://meetings.hubspot.com/nick-omelchak

Nick

### Paulo Pinho · Senior Medical Director · lane medical · P2 · `paulobpinho`

**M1**

Hi Paulo,

Noticed your headline spans insurance medicine and clinical informatics, a good lens for a new kind of input on Nationwide's accelerated cases.

FitXpress turns two photos in the e-application into a Smart Scales weight estimate, with a flag raised only when the gap against the declared figures crosses a threshold the carrier sets. BMI comes from the declared height.

What margin between a software estimate's error and a referral threshold would you want?

Nick

**M2**

Hi Paulo,

On the error to weigh: Smart Scales has approximately 3.5% mean absolute error under evaluated conditions and is not a scale reading. The decision boundary stays with Nationwide's underwriters.

FitXpress is not a medical device and does not make underwriting decisions. A call to go through the evaluated conditions can be set at https://meetings.hubspot.com/nick-omelchak

Nick

### Michael Moore · Chief Medical Director · lane medical · P2 · `michael-moore-a2568a26`

**M1**

Hi Michael,

Quick thought on Nationwide's Intelligent Underwriting guide: it runs an e-application and a client interview, and may accelerate eligible clients to a decision without an exam.

FitXpress puts two photos into the e-application, returns a weight estimate from Smart Scales, and flags a gap against the declared figures only above the carrier's threshold. One timestamped record goes back.

How does Nationwide's build guidance treat a declared weight next to an examiner's measured one?

Nick

**M2**

Hi Michael,

In an evaluation the flags are only counted, outputs stay outside decisions, and the carrier keeps the threshold and the guidance.

FitXpress is not a medical device and does not make underwriting decisions. A short call on how the flag would sit beside Nationwide's build guidance can be arranged at https://meetings.hubspot.com/nick-omelchak

Nick

## Gen Re US (6)

### Sarah Fusco · VP, Underwriting Executive · lane reinsurance · P2 · `sarahfusco2`

**M1**

Hi Sarah,

Quick thought on SOURCE: its manuals cover individual life and individual disability, and on accelerated cases of either kind build comes from the height and weight entered on the application.

On either line, FitXpress adds two photos to the application and returns a weight estimate from Smart Scales, with a flag only when it differs from the declared figures by more than the carrier's threshold, on one timestamped record.

Does Gen Re's guidance treat build differently on DI than on life?

Nick

**M2**

Hi Sarah,

In a client evaluation the flag counts can be split by product, with DI and life side by side before anything reaches a case. The carrier's rules and underwriters keep the decision.

FitXpress is not a medical device and does not make underwriting decisions. If comparing DI and life in one evaluation would help, a call is easy to set up at https://meetings.hubspot.com/nick-omelchak

Nick

### Frank Chechel · SVP, Head of Individual Life · lane reinsurance · P1 · `frankchechel`

**M1**

Hi Frank,

Noticed the line on Gen Re's US underwriting page about helping insurers sort new data and technology for accelerated programs. Build on those programs is the height and weight an applicant enters.

FitXpress takes two photos inside the e-application and returns a Smart Scales weight estimate, BMI from the declared height and one timestamped record, with a flag when the gap crosses the carrier's own threshold.

When a carrier brings Gen Re a remote build input to size up, what does the first conversation cover?

Nick

**M2**

Hi Frank,

One way to size it up with a client is a shadow evaluation: outputs stay outside decisions, flags are counted per candidate threshold, and they are compared with build from the client's paramedical exam cases.

A page that lays out that path for a carrier is at https://3dlook.ai/for-insurance-underwriting/

FitXpress is not a medical device and does not make underwriting decisions. A call on how Gen Re would run that evaluation is easy to arrange at https://meetings.hubspot.com/nick-omelchak

Nick

### Michael Clift · Vice President, Underwriting Executive - Individual Products Division · lane reinsurance · P2 · `michaelcliftlifeunderwriting`

**M1**

Hi Michael,

Got me thinking about Custom-SOURCE: when a carrier's own guidelines carry the build section, the figures behind it on accelerated cases are the declared height and weight.

Two photos in the e-application would add a Smart Scales weight estimate and a flag above the carrier's threshold, returned as one structured record.

Could a gap between declared and estimated weight ever belong in a SOURCE build section?

Nick

**M2**

Hi Michael,

The use I would test first is a referral line written into a client's custom build text, set well above the estimate's error, with flags counted in shadow before anything touches a case.

A page describing that sequence from the carrier's side is at https://3dlook.ai/for-insurance-underwriting/

FitXpress is not a medical device and does not make underwriting decisions. You can book a call on where such a line could sit in Custom-SOURCE at https://meetings.hubspot.com/nick-omelchak

Nick

### David Chien · Vice President, Chief Underwriter, Individual Life · lane reinsurance · P2 · `davidmchien`

**M1**

Hi David,

Curious about one line in Gen Re's individual life brochure: an approach to underwriter audits. On accelerated cases, the build in front of an auditor is the height and weight entered on the application.

A timestamped record is what FitXpress adds: two photos at application, a Smart Scales weight estimate, BMI from the declared height and a flag where the gap crosses the carrier's threshold.

What build evidence do audited accelerated cases give a reviewer to work from?

Nick

**M2**

Hi David,

An evaluation would set the record beside accelerated files in an audit sample and compare its flags with build from paramedical exam cases. That gives a reviewer a second reference point.

FitXpress is not a medical device and does not make underwriting decisions. Pick a time to talk through what an audit reviewer would want from the record at https://meetings.hubspot.com/nick-omelchak

Nick

### Joe Curtin · VP Chief Underwriter - IL Production · lane reinsurance · P2 · `joe-curtin-94261623a`

**M1**

Hi Joe,

Spotted something in Gen Re's individual life brochure: simplified application and requirement design. On a simplified application, build rests on the height and weight entered.

FitXpress was built for that gap. Two photos in the application give a Smart Scales weight estimate, and a flag when it differs from the declared figures by more than the carrier's threshold, with one timestamped record back.

Which requirement in a simplified application would a photo step sit beside?

Nick

**M2**

Hi Joe,

For a carrier's application, the step arrives through an API or web and mobile SDKs, and the carrier keeps every requirement it has today. Results return to the carrier's systems only.

A page showing how the step is offered beside existing requirements is at https://3dlook.ai/for-insurance-underwriting/

FitXpress is not a medical device and does not make underwriting decisions. A walkthrough call for Gen Re's requirement design can be booked at https://meetings.hubspot.com/nick-omelchak

Nick

### Georgette Chekiri · Vice President and Medical Director · lane medical · P2 · `georgette-chekiri`

**M1**

Hi Georgette,

This stood out in your background: family medicine, then carrier medical director, now Gen Re.

FitXpress produces a Smart Scales weight estimate from two photos taken in the e-application, with a flag raised only on a difference large enough to cross a threshold the carrier sets.

How would you judge whether a weight estimate from photos has a place in SOURCE-based rules?

Nick

**M2**

Hi Georgette,

The stated error is this: Smart Scales has approximately 3.5% mean absolute error under evaluated conditions and is not a scale reading. A carrier would set any threshold above that, on gaps large enough to change a class.

FitXpress is not a medical device and does not make underwriting decisions. A call to go through that error and the decision boundary is open at https://meetings.hubspot.com/nick-omelchak

Nick

## Zinnia (6)

### Timothy Nash · Chief Information Security Officer · lane technical-integration · P3 · `timothy-nash-1815973`

**M1**

Hi Timothy,

Wanted to reach out about security review in Zinnia's platform: an SDK that captures photos in a carrier's application raises a data-handling question first.

FitXpress takes two photos in the application and returns a Smart Scales weight estimate and a flag against the carrier's threshold through an API, as one timestamped record.

How does Zinnia review a new evidence vendor that carriers would connect through its platform?

Nick

**M2**

Hi Timothy,

Photos are deleted after processing or within 30 days per the carrier's policy, and faces are obscured at capture. TLS covers data in transit.

The privacy FAQ at https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/ goes through the rest, and documents go through legal@3dlook.me.

FitXpress is not a medical device and does not make underwriting decisions. A review call on Zinnia's vendor checks is open at https://meetings.hubspot.com/nick-omelchak

Nick

### Michael Hogan · Head of Underwriting & Fulfillment · lane partnership · P1 · `michael-hogan-1849132a`

**M1**

Hi Michael,

Noticed your background across life fulfillment and disability insurance. Zinnia runs underwriting and fulfillment work for carriers, and on accelerated cases the build in that work is the height and weight entered.

FitXpress adds two photos at application: a Smart Scales weight estimate and a flag against the carrier's threshold, in one timestamped record that could reach that workflow.

Where does build get checked on accelerated cases in the underwriting and fulfillment work Zinnia runs?

Nick

**M2**

Hi Michael,

A shadow evaluation shows it on real flow: outputs stay outside decisions, and flags are counted and compared with build from paramedical exam cases.

A page laying out that evaluation for a carrier program is at https://3dlook.ai/for-insurance-underwriting/

FitXpress is not a medical device and does not make underwriting decisions. A call on running it inside Zinnia's fulfillment work is easy to arrange at https://meetings.hubspot.com/nick-omelchak

Nick

### Michael Celi · Chief Product Officer · lane partnership · P1 · `michael-celi`

**M1**

Hi Michael,

Got me thinking about The Policy Processor's low-code rules and forms: a new evidence step is something a carrier could switch on by configuration.

FitXpress offers one API and SDK route: two photos in the carrier's application, a Smart Scales weight estimate, BMI from the declared height, and a flag against the carrier's threshold on a timestamped record.

How would a step like that be added to The Policy Processor for several carriers at once?

Nick

**M2**

Hi Michael,

For a platform, one integration is the point: API and web and mobile SDKs, with one record per applicant returned to Zinnia and each carrier setting its own threshold.

A page describing the product's use for carriers is at https://3dlook.ai/for-insurance-underwriting/

FitXpress is not a medical device and does not make underwriting decisions. You can set a call on configuring the step in The Policy Processor at https://meetings.hubspot.com/nick-omelchak

Nick

### Brad Medd · Chief Technology Officer · lane technical-integration · P3 · `brad-medd-3172b710`

**M1**

Hi Brad,

This stood out: The Policy Processor 8.0 is built API-first, which is how an outside evidence step would connect.

Through a REST API, FitXpress takes two photos from the carrier's application and returns one timestamped record: a Smart Scales weight estimate, BMI from the declared height and a flag against the carrier's threshold.

What does Zinnia's team want to see in a new evidence vendor's REST API before connecting it?

Nick

**M2**

Hi Brad,

On the build: REST API and web and mobile SDKs, results to the platform, and the decision boundary stays with the carrier's underwriters.

FitXpress is not a medical device and does not make underwriting decisions. A technical call on connecting through the API can be booked at https://meetings.hubspot.com/nick-omelchak

Nick

### Jennifer Abboud · Head of Product Operations · lane partnership · P3 · `jenniferabboud`

**M1**

Hi Jennifer,

Caught my eye: Zinnia's product page covers simplified issue and accelerated models alongside fully underwritten ones, across life and disability.

On accelerated cases, FitXpress adds two photos, a Smart Scales weight estimate and a flag above the carrier's threshold, recorded with a timestamp.

What are carrier clients asking Zinnia for on accelerated cases?

Nick

**M2**

Hi Jennifer,

If build evidence is on that list, it can reach the platform as an API call or through web and mobile SDKs, one record per applicant, with each carrier setting its own rules.

FitXpress is not a medical device and does not make underwriting decisions. If client solutions is the better route, an introduction would be welcome. You can book a call on what clients ask for at https://meetings.hubspot.com/nick-omelchak

Nick

### Vikash Rai · VP, Head of Product, System of Record. · lane partnership · P2 · `vrai-productmanager`

**M1**

Hi Vikash,

Quick thought on Zinnia's product page: case data, evidence and decisions sit in one workspace, which means a new evidence type needs a defined place to land.

FitXpress returns one structured, timestamped record per applicant from two photos, with a Smart Scales weight estimate and a flag where the gap crosses the carrier's threshold.

How would a record like that be written back to the system of record?

Nick

**M2**

Hi Vikash,

The record carries a timestamp and a random identifier, and each carrier decides where it appears on a case.

FitXpress is not a medical device and does not make underwriting decisions. Booking a conversation on the write-back path to the system of record is easy at https://meetings.hubspot.com/nick-omelchak

Nick

## Bestow (5)

### Laura Boylan · VP, Underwriting Solutions · lane partnership · P1 · `laura-mckiernan`

**M1**

Hi Laura,

Quick thought on Bestow's underwriting platform, where carriers set their own risk thresholds and decide which cases go to instant issue.

FitXpress adds two photos to the e-application and returns a Smart Scales weight estimate, BMI from the declared height, and a flag when the gap crosses the carrier's threshold, as one timestamped record.

Where would a build referral sit among those decision options?

Nick

**M2**

Hi Laura,

One integration could serve several carriers on your platform: API and web and mobile SDKs, with one timestamped record per applicant returned to Bestow. https://3dlook.ai/for-insurance-underwriting/ shows how that record sits beside a carrier's own thresholds.

FitXpress is not a medical device and does not make underwriting decisions.

If you want to see how a build flag would slot into the engine's routing, here is my calendar: https://meetings.hubspot.com/nick-omelchak

Nick

### David Peters · Director of Underwriting · lane partnership · P3 · `david-peters-9b1b6898`

**M1**

Hi David,

Got me thinking about the cases Bestow sends to instant issue.

What we built is a step of two photos: the declared height anchors the BMI, Smart Scales estimates weight, and the carrier's threshold decides whether a flag is raised. One timestamped record lands on the case.

On cases that go to instant issue, how is build looked at today?

Nick

**M2**

Hi David,

For an underwriter the value sits in the record: timestamped, on the case file, with a flag raised only above the threshold the carrier sets. A comparison with build from paramedical exam cases would show how the flag lines up.

FitXpress is not a medical device and does not make underwriting decisions.

If it helps to walk through that comparison for instant-issue cases, grab a time here: https://meetings.hubspot.com/nick-omelchak

Nick

### David Malenoir-Evans · Chief Product Officer · lane partnership · P1 · `malenoir`

**M1**

Hi David,

Noticed your product work at MetaMap and Procore.

A step of two photos is what FitXpress adds to the e-application. It returns a Smart Scales weight estimate, a flag at the carrier's threshold, and the BMI that follows from the height entered.

In Bestow's journeys for agents and for applicants, where would you try a step like that first?

Nick

**M2**

Hi David,

A scan runs under 45 seconds from the photos to structured results. Completion would be measured in an evaluation that keeps outputs out of live cases.

FitXpress is not a medical device and does not make underwriting decisions.

If a test of the step across those journeys sounds useful, I would be glad to plan it on a call: https://meetings.hubspot.com/nick-omelchak

Nick

### Dave Belanger · Chief Security & Privacy Officer · lane technical-integration · P3 · `dbelanger1`

**M1**

Hi Dave,

Wanted to reach out about how Bestow reviews a new data vendor.

FitXpress is a capture of two photos inside the e-application. It sends the carrier's systems one timestamped record: a Smart Scales weight estimate, a BMI based on the height entered and a flag at the carrier's threshold.

When a vendor like that comes up for review, what does your team ask for first, the data flow or the retention terms?

Nick

**M2**

Hi Dave,

Data handling: TLS in transit and S3-managed encryption at rest. Photos are deleted after processing or within 30 days per the carrier's policy, retained photos are blurred, faces are obscured at capture, and scan records sit on random identifiers. Documents for your review go through legal@3dlook.me.

FitXpress is not a medical device and does not make underwriting decisions.

If a walk through the data flow and retention terms would help your review, this is my calendar: https://meetings.hubspot.com/nick-omelchak

Nick

### Eric Lee · Vice President of Product Management · lane partnership · P2 · `ericwonsuklee`

**M1**

Hi Eric,

Saw the news on Bestow Labs, the team building AI-native products fully apart from production systems.

Our scan, FitXpress, takes two photos in the e-application and sends back one timestamped record: a Smart Scales weight estimate, a BMI calculated from the applicant's height and a flag above the carrier's threshold.

For a new data input like that, what would it take to move from Labs into the production engine?

Nick

**M2**

Hi Eric,

FitXpress comes as an API with web and mobile SDKs, returning one timestamped record per applicant. A first try could sit in Labs, with outputs kept out of live decisions.

FitXpress is not a medical device and does not make underwriting decisions.

If integrations belong to a platform team, I would gladly speak with them first. Otherwise a call about trying it in Labs fits here: https://meetings.hubspot.com/nick-omelchak

Nick

## Ethos (4)

### Sean Flanagan · Senior Director, Underwriting Automation · lane underwriting · P2 · `spflan`

**M1**

Hi Sean,

Caught my eye that Ethos takes applications with no medical exams and just a few health questions.

Our FitXpress step takes two photos at application. A Smart Scales weight estimate comes back with a BMI worked out from the height entered, and a gap beyond the threshold you set raises a flag.

Where in the instant-decision rules would a build referral rule sit?

Nick

**M2**

Hi Sean,

Smart Scales gives a weight estimate with approximately 3.5% mean absolute error under evaluated conditions, not a scale reading. A referral threshold would sit well above that, on gaps that change the class.

FitXpress is not a medical device and does not make underwriting decisions.

I would be glad to go through where such a rule fits in your flow on a call: https://meetings.hubspot.com/nick-omelchak

Nick

### Nichole Myers · Chief Underwriter · lane underwriting · P1 · `nicholelmyers`

**M1**

Hi Nichole,

Noticed that Ethos audits its automated decisions.

FitXpress is a step of two photos for the application: it returns a Smart Scales weight estimate, BMI from the declared height, and a flag when the gap crosses a threshold your team sets, as one timestamped record.

In those audits, how does build get treated?

Nick

**M2**

Hi Nichole,

A shadow evaluation could count how many flags each candidate threshold raises, then compare them with build from paramedical exam cases, with no output reaching a case. https://3dlook.ai/for-insurance-underwriting/ describes that path.

FitXpress is not a medical device and does not make underwriting decisions.

If the audit angle is where to start, a call could shape the design around your audit sample: https://meetings.hubspot.com/nick-omelchak

Nick

### Vipul Sharma · Chief Technology Officer (Product, Engineering, Data/AI) · lane technical-integration · P2 · `vipulethos`

**M1**

Hi Vipul,

Curious about your take, given engineering at Indeed before Ethos.

FitXpress ships as an SDK step in the application. Two photos in, one timestamped structured record out, with a Smart Scales weight estimate and a flag at the threshold set in your rules.

How would a record like that reach your decisioning service, through a request at submission or as an event afterwards?

Nick

**M2**

Hi Vipul,

FitXpress comes as a REST API with SDKs. The record returns to your systems only, scan records sit on random identifiers, and photos are deleted after processing or within 30 days per your policy.

FitXpress is not a medical device and does not make underwriting decisions.

I can take you through the integration on a call: https://meetings.hubspot.com/nick-omelchak

Nick

### Ashwath Muralidharan · Vice President of Product Management · lane proposition · P2 · `ashwath-muralidharan-945a415`

**M1**

Hi Ashwath,

Saw the news on Ethos's ChatGPT app for instant term estimates.

With FitXpress, two photos taken in the application return a Smart Scales weight estimate, the resulting BMI and a flag at the threshold set in your rules, in one timestamped record.

Would a step like that fit better right after the estimate or inside the application itself?

Nick

**M2**

Hi Ashwath,

In a flow that is already instant, completion matters most. The scan finishes under 45 seconds from the photos to structured results.

FitXpress is not a medical device and does not make underwriting decisions.

If tests of new steps in the agent channel run through another group, I am happy to speak with them first. Otherwise a call about where the step fits between estimate and application works well: https://meetings.hubspot.com/nick-omelchak

Nick

## Ladder Life (3)

### Ryan Mackillop · Director of Underwriting · lane underwriting · P1 · `rmackillop`

**M1**

Hi Ryan,

Quick one on Ladder's fully digital path, with a few health questions and no medical exam.

FitXpress adds two photos and returns a Smart Scales weight estimate, BMI from the declared height and a flag when the gap crosses a threshold your team sets, as one timestamped record.

Where would a large gap route on that path, to an underwriter or to the at-home health check?

Nick

**M2**

Hi Ryan,

A shadow evaluation would run beside live decisions with outputs kept out of cases, and compare flags with build gathered separately in exam-based cases. https://3dlook.ai/for-insurance-underwriting/ shows that path for a flow like yours.

FitXpress is not a medical device and does not make underwriting decisions.

I would welcome a call on how such an evaluation fits the fully digital path: https://meetings.hubspot.com/nick-omelchak

Nick

### Laura Hale · Chief Product Officer · lane proposition · P2 · `hale-laura`

**M1**

Hi Laura,

Noticed your path from Ebates employee number one to co-founding Ladder.

Two photos become one timestamped record with FitXpress: a Smart Scales weight estimate, a BMI calculated from the entered height and a flag above a threshold set in your rules.

In an application that takes minutes, would those photos go before or after the health questions?

Nick

**M2**

Hi Laura,

Speed decides whether a step stays in a flow like Ladder's. Each scan completes under 45 seconds from the photos to structured results.

FitXpress is not a medical device and does not make underwriting decisions.

If you would like to look at where the step fits in the application, my calendar is here: https://meetings.hubspot.com/nick-omelchak

Nick

### Keerthi Mandala · Vice President of Product Management · lane proposition · P2 · `keerthi-mandala`

**M1**

Hi Keerthi,

Made me think about your split of consumer risk and growth at Ladder.

On our side, FitXpress turns two photos into a Smart Scales weight estimate, the matching BMI and a flag above a threshold set in your rules, kept as one timestamped record.

How would you read drop-off from a new step in Ladder's instant flow?

Nick

**M2**

Hi Keerthi,

The evaluation we would propose measures completion and keeps the data in Ladder's systems only. Nothing reaches a decision during the test.

FitXpress is not a medical device and does not make underwriting decisions.

A short call to plan that test across the instant flow and the advisor channel would suit me: https://meetings.hubspot.com/nick-omelchak

Nick

## iPipeline US (3)

### Katie Kahl · Chief Product Officer · lane partnership · P1 · `katie-kahl-15049526`

**M1**

Hi Katie,

Saw the news on iGO Evolve and its API-enabled architecture.

FitXpress is a step of two photos for the e-application. It returns a Smart Scales weight estimate, BMI from the declared height, and a flag when the gap crosses the carrier's threshold, as one timestamped record.

Where in iGO Evolve would a carrier switch on a step like that?

Nick

**M2**

Hi Katie,

Carriers on your e-application could switch the step on through one integration: API and web and mobile SDKs, with one timestamped record per applicant returned to the platform. https://3dlook.ai/for-insurance-underwriting/ shows the build record a carrier would see.

FitXpress is not a medical device and does not make underwriting decisions.

If mapping the step onto iGO Evolve is worth a conversation, my calendar is here: https://meetings.hubspot.com/nick-omelchak

Nick

### Chris Cella · Vice President of Product Management · lane partnership · P2 · `chriscella`

**M1**

Hi Chris,

Caught the Resonant and XRAE pages on iPipeline's site.

Two photos in the e-application return a Smart Scales weight estimate, the BMI it implies and a flag above the carrier's threshold, as one timestamped structured record from FitXpress.

Would that build record land best in Resonant's case management or in XRAE's field underwriting?

Nick

**M2**

Hi Chris,

The record is made to be read by a workbench: structured, timestamped, one per applicant, with the flag present only above a threshold the carrier sets.

FitXpress is not a medical device and does not make underwriting decisions.

If you would like to talk through the data mapping into Resonant or XRAE, here is my calendar: https://meetings.hubspot.com/nick-omelchak

Nick

### Alex Tompkins · Vice President of Product Management · lane partnership · P2 · `alexctompkins`

**M1**

Hi Alex,

Spotted the Novera API Hub, where API workflows get built and tested at iPipeline.

FitXpress takes two photos in the e-application and returns a timestamped record with a Smart Scales weight estimate, a calculated BMI and a flag above the carrier's threshold.

Would an outside evidence step like that connect through Novera, or through iGO's own configuration?

Nick

**M2**

Hi Alex,

On the technical side, FitXpress is a REST API with web and mobile SDKs, returning one timestamped record per applicant.

FitXpress is not a medical device and does not make underwriting decisions.

If another group curates what the Hub lists, I am glad to speak with them first. Otherwise a call on connecting it through Novera would suit me: https://meetings.hubspot.com/nick-omelchak

Nick

## Foresters Financial US (1)

### Paul Greene · Chief Underwriting Officer · lane underwriting · P1 · `paul-greene-40b337a4`

**M1**

Hi Paul,

Saw the news on the April expansion of accelerated underwriting at Foresters, with more applicants going fluidless.

FitXpress adds two photos to the e-App and returns a Smart Scales weight estimate, BMI from the declared height, and a flag when the gap crosses the threshold Foresters sets, as one timestamped record.

Where does build enter a fluidless case once tele-med, exam and labs are out?

Nick

**M2**

Hi Paul,

Smart Scales gives a weight estimate with approximately 3.5% mean absolute error under evaluated conditions, not a scale reading. A flag would refer only gaps well above that, at a threshold you set. https://3dlook.ai/for-insurance-underwriting/ shows the evaluation steps.

FitXpress is not a medical device and does not make underwriting decisions.

I can take you through a shadow evaluation for the fluidless program on a call: https://meetings.hubspot.com/nick-omelchak

Nick
