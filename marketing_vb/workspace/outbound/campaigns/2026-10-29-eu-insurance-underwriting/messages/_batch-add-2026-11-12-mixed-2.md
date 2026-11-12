@@@ fabian-winter-13bb1688
hook: concrete scenario, a remote build record as a new field for a reinsurer's underwriting tools
proof: 2 photos, Smart Scales weight estimate beside declared weight (Rules, What the scan is)
--- M1
Hi Fabian,

Underwriting tools at a reinsurer run on the fields of an insurer's application, and a remote build record would be a new kind of field for them.

FitXpress produces it from 2 photos taken in the application. The Smart Scales estimate is placed beside the declared weight, with a flag where the insurer's tolerance for the gap between them is exceeded.

What would such an external field need in its description before Munich Re's tools could read it?

Olena
--- M2
Hi Fabian,

The record keeps the declared weight and the estimate in separate fields under one timestamp. A field description can name the source of each, and an insurer running a shadow evaluation would hold the records itself.

FitXpress is not a medical device and does not make underwriting decisions.

If the L&H underwriting engines have a separate owner, I will write to that person next.

I can lay out the record on a call: https://meetings.hubspot.com/olena-kudriavtseva

Olena
@@@ juergen-wendlandt
hook: remit stated plainly, data assets at Munich Re; a field has an origin someone must state
proof: 2 photos, timestamp, declared weight and estimate (Rules, What the scan is)
--- M1
Hi Jürgen,

Munich Re's data assets are in your charge, and every field in them has an origin that someone must be able to state.

A remote build record has two origins in one row. The declared weight comes from the applicant's form. The estimate comes from FitXpress, which takes 2 photos in the application and returns a Smart Scales value with a timestamp, and the insurer's threshold on the gap between the two sets a flag.

What origin details would a field like that need in Munich Re's data descriptions?

Olena
--- M2
Hi Jürgen,

In an insurer's evaluation, origin stays visible in every row: the declared weight comes from the form and the estimate from the scan.

FitXpress is not a medical device and does not make underwriting decisions.

Stewardship of L&H underwriting data may sit with someone else, and I would raise it there.

Field origins could be the topic of a call: https://meetings.hubspot.com/olena-kudriavtseva

Olena
@@@ julia-krezdorn
hook: concrete scenario, a second weight reaching a model in Munich Re's L&H underwriting tools
proof: 2 photos, Smart Scales (Rules, What the scan is)
--- M1
Hi Julia,

Applications that reach an insurer without a doctor's examination hold one weight, the one the applicant declares. A model in Munich Re's L&H underwriting tools that reads them would meet a second weight if the insurer used a software estimate.

The estimate is returned from 2 photos in the application, as a Smart Scales value beside the declared weight, with a flag where the insurer's tolerance for the difference is exceeded.

What would your team want to know about how an estimate is produced before a model reads it as an input?

Olena
--- M2
Hi Julia,

A model team would find the estimate and the declared weight as separate fields in each record, never merged into one value. An insurer's evaluation produces those pairs on its own applications and keeps the results.

FitXpress is not a medical device and does not make underwriting decisions.

I can take this to L&H model validation if that fits.

Provenance of the estimate can be covered on a call: https://meetings.hubspot.com/olena-kudriavtseva

Olena
@@@ andreas-bayerstadler-20b9b6111
hook: concrete scenario, a new column beside the declared weight needing history (title only)
proof: 2 photos, Smart Scales weight estimate, timestamp (Rules, What the scan is)
--- M1
Hi Andreas,

A weight estimate adds a column next to the declared weight, and a model team decides what history that column needs before it is used.

FitXpress produces it: the applicant takes 2 photos in the insurer's application, and a Smart Scales weight estimate comes back with a timestamp. The record flags cases where the insurer's rule finds the declared weight and the estimate too far apart.

How much history would a model team at Munich Re want on such a column before testing it?

Olena
--- M2
Hi Andreas,

The timestamp on each record is what starts the history. An evaluation at an insurer builds a dated series from the first application it includes, and that series stays with the insurer that ran it.

FitXpress is not a medical device and does not make underwriting decisions.

I am ready to put the history question to whoever owns the L&H models.

I would like to discuss the timestamp history on a call: https://meetings.hubspot.com/olena-kudriavtseva

Olena
@@@ dr-till-boehmer
hook: concrete scenario, an insurer's evaluation of a build field and the choice of comparison
proof: 2 photos, Smart Scales estimate beside declared weight (Rules, What the scan is)
--- M1
Hi Till,

An insurer that tests a new build field produces numbers for analysts to read, and the choice of comparison shapes what they show.

In FitXpress the applicant adds 2 photos in the application, and a Smart Scales weight estimate comes back beside the declared weight. The insurer sets a tolerance for the difference, and a flag marks cases outside it.

For such an evaluation, which comparison would central analytics at Munich Re expect: the estimate against the declared weight, or against a measured weight?

Olena
--- M2
Hi Till,

A comparison against measured weights covers only the cases where a weighing exists, which is a smaller group than all applications in an evaluation. The insurer can count both comparisons side by side and keeps the results.

FitXpress is not a medical device and does not make underwriting decisions.

The actuarial team that studies build experience may prefer to take this up, and I would write to them next.

Your reading of the comparison could be covered on a call: https://meetings.hubspot.com/olena-kudriavtseva

Olena
@@@ dirk-heiss-80a72b4
hook: remit stated plainly, digital underwriting tools on Munich Re's platforms; the application is where the record starts
proof: 2 photos, REST API and SDKs, structured record (Rules, What the scan is)
--- M1
Hi Dirk,

Munich Re's digital underwriting tools sit on its platforms, and a client insurer's application is where a remote build record would start.

The step is an API integration. The applicant's 2 photos go to FitXpress, and one structured record comes back with a Smart Scales weight estimate, the declared weight beside it, and a flag when their difference passes the insurer's own limit.

Which side would own the interface for a step like this: the insurer's application or Munich Re's platform?

Olena
--- M2
Hi Dirk,

The step reaches an application through SDKs for web and mobile, or by a direct call to the REST API. The insurer chooses the route, and a shadow evaluation runs entirely inside its own application.

FitXpress is not a medical device and does not make underwriting decisions.

My next message would go to whoever runs client integrations, if you would rather.

The two integration routes can be explained on a call: https://meetings.hubspot.com/olena-kudriavtseva

Olena
@@@ madhu-d-24842112
hook: remit stated plainly, product and digital at SCOR; a build record as a possible new input to tools SCOR offers
proof: 2 photos, SDK, Smart Scales weight estimate beside declared weight (Rules)
--- M1
Hi Madhu,

Product and digital at SCOR are both yours, and a remote build record could be a new input for the underwriting tools SCOR offers its clients.

FitXpress adds an SDK step to an insurer's application. The applicant takes 2 photos, and a Smart Scales weight estimate returns beside the declared weight, with a flag where the insurer's threshold on the difference is met.

How would SCOR's product side describe a build field like that to a client insurer?

Olena
--- M2
Hi Madhu,

One evaluation at a client would give SCOR's product side a complete example of the record, from the SDK step to the flag. The insurer runs it on its own applications and keeps the results.

FitXpress is not a medical device and does not make underwriting decisions.

The L&H product owner would be my next message, if that suits you.

I can show the record on a call: https://meetings.hubspot.com/olena-kudriavtseva

Olena
@@@ sofiakyriakopoulou
hook: bio, delivering analytics and AI solutions that read an insurer's application
proof: 2 photos, API and SDK, timestamped record (Rules, technical-integration)
--- M1
Hi Sofia,

Your bio speaks of delivering analytics and AI solutions. A solution that reads an insurer's application needs an interface behind each new field.

FitXpress is an API and SDK step. The applicant sends 2 photos, and a Smart Scales weight estimate returns with a timestamp, held beside the declared weight. A flag marks cases where the insurer's threshold on their difference is exceeded.

How is a new external API reviewed at SCOR before a tool reads from it?

Olena
--- M2
Hi Sofia,

The insurer can request deletion of specific scans by scan identifier. Photos are deleted after processing or within 30 days, per the insurer's policy.

In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes SCCs.

Review documents go through legal@3dlook.me.

If vendor onboarding is a separate function at SCOR, I would contact that team instead.

The interfaces can be covered on a call: https://meetings.hubspot.com/olena-kudriavtseva

Olena
@@@ thibault-antoine-697b1425
hook: concrete scenario, a field present only for applicants who scan (title only)
proof: 2 photos, Smart Scales weight estimate, timestamp (Rules)
--- M1
Hi Thibault,

Only applicants who scan would have an estimated weight. A model that reads an insurer's application would see that field for part of the cases at SCOR's clients.

FitXpress returns it from 2 photos in the application: a Smart Scales weight estimate beside the declared weight, with a timestamp and a flag where the insurer's rule finds the two too far apart.

How would an AI team at SCOR treat a field that is present for only some applicants?

Olena
--- M2
Hi Thibault,

A missing record can have more than one cause: the insurer did not offer the step, or the applicant did not scan. The insurer decides where the step is offered and keeps its usual route for applicants who cannot or do not scan.

FitXpress is not a medical device and does not make underwriting decisions.

Model risk may own this question, and if so I would take it to that team.

We could go through missing records on a call: https://meetings.hubspot.com/olena-kudriavtseva

Olena
@@@ steikert
hook: concrete scenario, a field called estimated weight needs a definition of how it was produced (headline only)
proof: 2 photos, Smart Scales weight estimate, timestamp (Rules)
--- M1
Hi Kristoph,

A field called estimated weight means little until its definition says how it was produced.

FitXpress produces it from 2 photos in an insurer's application, as a Smart Scales weight estimate held beside the declared weight with a timestamp. The insurer sets the threshold on their difference, and the record carries a flag for cases above it.

How would a data catalogue at SCOR describe an estimated weight that comes from an external API?

Olena
--- M2
Hi Kristoph,

A definition for the field would name its method and keep the declared weight as a separate field. An evaluation at an insurer shows the full set of fields before anyone writes that definition.

FitXpress is not a medical device and does not make underwriting decisions.

If cataloguing belongs to a data governance lead, I would write to that person.

Do you want to set up a conversation on field definitions? https://meetings.hubspot.com/olena-kudriavtseva

Olena
@@@ mark-w-28796b
hook: remit stated plainly, group data and analytics at Swiss Re; weight declared on cases with no examination
proof: 2 photos, Smart Scales weight estimate beside declared weight (Rules)
--- M1
Hi Mark,

Group data and analytics at Swiss Re are yours. On applications with no doctor's examination, weight is a declared value, and a remote build record would add an estimate beside it.

FitXpress returns that estimate from 2 photos in an insurer's application, as a Smart Scales value with a timestamp, and flags cases where the difference exceeds the insurer's threshold.

Does a group data model have a place for an estimate that sits beside a declared value?

Olena
--- M2
Hi Mark,

In the record the two values stay in separate fields, and each keeps its own source. An insurer evaluating the step holds the records itself.

FitXpress is not a medical device and does not make underwriting decisions.

If the owner of Magnum is the better first reader, I will write to them.

The two fields can be shown on a call: https://meetings.hubspot.com/olena-kudriavtseva

Olena
@@@ ermirqeli
hook: remit stated plainly, data science and AI at Swiss Re reach underwriting
proof: 2 photos, Smart Scales weight estimate beside declared weight (Rules)
--- M1
Hi Ermir,

Data science and AI at Swiss Re reach underwriting, and underwriting teams ask for features that someone has to test. A remote build record is one candidate.

FitXpress turns 2 photos in an insurer's application into a Smart Scales weight estimate placed beside the declared weight. A flag marks cases where the insurer's tolerance for their difference is exceeded.

Would your team test such a field first as a model feature or as an input to Magnum?

Olena
--- M2
Hi Ermir,

Testing as a feature needs both weights for the same applicant, and each record carries them together. The insurer's evaluation produces them on its own applications and keeps them.

FitXpress is not a medical device and does not make underwriting decisions.

If L&H analytics owns that first test, I will take it there.

I could present the record structure on a call: https://meetings.hubspot.com/olena-kudriavtseva

Olena
@@@ marlot-linstra-520056b6
hook: hypothetical, a software weight estimate appearing on an AOV file beside the declared weight
proof: 2 photos, Smart Scales; 3.5% sentence in M2 (Facts, medical lane)
--- M1
Hi Marlot,

If a software weight estimate reached an AOV file, it would appear as one more line beside the declared weight.

FitXpress would produce it from 2 photos in the application, with a flag where the insurer's own threshold on the difference is exceeded.

At a.s.r., would a medical adviser on income cover want such a flag to prompt a doctor's weighing or to stay a note on the file?

Olena
--- M2
Hi Marlot,

The estimate has a stated error. Smart Scales is a weight estimate with approximately 3.5% mean absolute error under evaluated conditions, and it is not a scale reading. A flag would only point a case to an underwriter.

FitXpress is not a medical device and does not make underwriting decisions.

The medical director for income cover could be the right person for this, and I would write to them.

Could we speak about the evidence a medical reader would want? https://meetings.hubspot.com/olena-kudriavtseva

Olena
