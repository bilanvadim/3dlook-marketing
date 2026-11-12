---
qc_date: 2026-11-12
agent: message-sequencer
artifact: workspace/outbound/campaigns/2026-10-29-eu-insurance-underwriting/messages/ (second widening 2026-11-12, «додай усіх», item 7: 20 new pairs, read verbatim from the coordinator's dump eu-insurance-add-all-2026-11-12-messages.md)
track: outbound
artifact_type: message
total_score: 10/20
status: failed
coordinator_review: done
---

# QC Report: message-sequencer, 2026-11-12 (EU insurance underwriting, second widening, 20 new pairs)

**Artifact:** I read all 20 new pairs verbatim and judged them against the 85 pairs already written at the same five companies (`existing-add-2026-11-12-mixed-1.md` and `-mixed-2.md`, read in full). The split is Irish Life 12, Munich Re 16, SCOR 18, Swiss Re 27 and a.s.r. 4. Rules come from `card-messages.md`, read in full: Rules, lanes, Account facts, Vadim's decisions 2026-11-12 items 1-7, the hard-bans card and both templates. I checked every claim about a person against the title, headline, bio and experience in `pool-*.md`. Mechanics (limits, signature, link placement, bans, detector) come from the gate at 0 hard, and I took them as given.

**Total: 10/20, failed.** These parts are clean:
- the compliance line, correct by lane in 20 of 20, one per pair, in Message 2 only;
- numbers: "2 photos" appears in every pair, and 3.5% appears only in Message 2 of Till Böhmer (`reinsurance`) and Marlot Linstra (`medical`), each time with "not a scale reading";
- **claims about people: all 20 hooks are supported by the profile**, against 5 unsupported claims in the first widening;
- the round-1 A1 fix held in 17 of 20 M1s;
- no Never term, no other prospect, and no former employer that is an account (Canada Life, Swiss Re, AXA and ING are not named);
- no P1 in the batch gets an easy out.

Three things fail:
- **Item 6 and item 7 sameness, against colleagues already contacted.** All seven repeat elements come back: hook, product sentence, central question, M2 opener, easy-out target, closer and CTA. The worst cases are near-clones of sent messages:
  - Samantha's and SarahJane's M2 value lines are Alan Q.'s;
  - Sofia's M2 is Martijn Reijerse's;
  - Till's M2 is Christoph Henschel's;
  - Fabian's and Julia's questions are Keyvan Izadi's.
- **The defects of the first widening are back:**
  - 14 of 20 M1s open on the person's bio, headline or career;
  - stock closers repeat sent colleagues word for word;
  - 3 M1s lost the declared-weight gap (A1);
  - Irish Life easy outs point to the same owner, which item 7 forbids;
  - 8 of the 12 data and AI chiefs, none of them the buyer, have no easy out.
- **Data-handling claims beyond the card.**
  - 5 data-chief M2s state as fact that the client insurer exports per-applicant records to the reinsurer.
  - Mark W.'s whole pair rests on how long Swiss Re keeps client-supplied data.
  - Julia's M2 says "Nothing connects to production systems."
  - Sofia's M2 paraphrases the photo-retention form.

**Recommendation:** do not regenerate all 20.
- **Irish Life (7):** rewrite as one block from a grid. The grid assigns each person a hook type, product-sentence shape, question topic, M2 value, easy-out owner and CTA, and checks each against the 12 written there.
- **Munich Re (6):** new hooks with no bio or headline recital, new M2 value sentences, and one "what must it pass" question at most.
- **Data-chief M2s (all 12):** give each a different value, remove "The client exports…", and add easy outs where missing.
- **Line edits:** SCOR (4), Swiss Re (2) and Marlot.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 2 | 5 |
| B | Factual accuracy | 3 | 5 |
| C | Brand & tone | 1 | 3 |
| D | Format & structure | 2 | 3 |
| E | Output quality | 2 | 4 |

## What was wrong (specific)

### A. Adherence, 2/5

**A1. Repeats against colleagues already contacted (item 6: opener, central question, easy-out target, M2 opener, closer).**

**Irish Life (7 new against 12 written):**
- **M2 value line.** Alan Q. (sent): "an evaluation can run in the background first, with flags counted and no case changed. The insurer chooses where the step is offered."
  - Samantha: "an evaluation could run alongside it, with flags counted and no case changed. Irish Life would choose where the step appears." Both sentences are Alan Q.'s, reworded.
  - SarahJane: "an evaluation first, with flags counted and no case changed, and the insurer decides where the step goes live." These are the same two parts.
  - "flags counted" or "no case changed" appears in 6 of the 7 new M2s: Sean, Samantha, Nicola, SarahJane, Denis and Eimear. Only Alan Brady avoids it.
- **Product sentence:**
  - Sean's "The step is 2 photos from the applicant…" opens like Alan Q.'s "The step is 2 photos in the application."
  - Nicola's "FitXpress asks for 2 photos in the application" is Laura Mongan's "The step asks for 2 photos in the application". Her tail "each case gets one timestamped record" is Alan Q.'s "the case gets one timestamped record".
  - Denis: "The record flags a case only when…" repeats Mark Rodgers' "the record flags a case if…".
  - Sean and SarahJane share the record label "side by side". The card says: "No stock label for the scan or the record repeats across people at one company."
  - Sean's "far enough apart to matter" is close to Laura's "far enough from the declared weight".
- **M2 opener:**
  - Sean's "A shadow phase would show how many cases…" is close to Christopher Curran's "A shadow evaluation … would show how often a flag is raised".
  - Alan Brady's "An evaluation shows what the step would change on the cases Irish Life picks" and Denis's "An evaluation would show what the step adds to those cases" are twins.
  - Alan Brady's "cases Irish Life picks" also echoes Siobhan Buckley's "the cases the insurer chooses".
- **Closer:**
  - Denis: "If sales and distribution for protection should hear this, please point me there." This is Shay Browne's "If protection underwriting should hear this first, please point me there."
  - Sean: "If the rules for build sit with someone else, please point me to them." This has the frame of Kelvin Gillen's "If protection new business sits in another team, please point me there."
  - Samantha: "…may be the better first contact." This is close to Patricia Smith's "…may be a better contact for this."
  - Alan Brady's "please name whoever leads them" and Nicola's "please name who runs it" put two "please name" closers in one batch.
- **CTA:**
  - Sean's "A call would cover the rest:" and SarahJane's "A short call would cover it:" repeat Mark Rodgers' "A call can cover the fields:".
  - Samantha's "If a call helps, my calendar is here:" and Nicola's "If a call makes sense, my diary is open here:" share one frame.
- **Central question:**
  - Sean's "Which parts of your strategy depend on how protection applications are assessed?" is close to Samantha's "Which of your strategic programmes reach into the protection application?"
  - Nicola's "How do your programmes govern a small change inside a live journey?" is close to SarahJane's "How does a change to a live application travel from first request to release in your team?"
  - Eimear's "How does a new idea for the application earn a place in your portfolio?" is close to Kelvin's "How does ExO take an outside idea from first look…" and Christopher's "How do you decide which team sees a new external idea first?"
  - **Topic quota:** one topic now covers about 10 of the 19 Irish Life people: how a change or idea for the application gets prioritised, governed or released. Sent: Alan Q., Shay, Christopher, Kelvin. New: Sean, Samantha, Alan Brady, Nicola, SarahJane, Eimear. The card allows "at most about a fifth".

**Munich Re (6 new against 16 written):**
- **Hook:** 5 of 6 open on the bio or headline:
  - Dirk: "Your bio sets out a mission"
  - Till: "…is in your headline"
  - Jürgen: "Your headline makes you responsible"
  - Fabian: "Your bio gives you global responsibility"
  - Julia: "Your headline speaks of a passion"

  Three sent openers have the same frame: Roland Schneider's "your bio talks about", Mirjam Jonker-Heidolph's "Your headline combines" and Fabian Schmitt's "Your own description mentions a love of…". That makes 8 of 22 Munich Re M1s. Julia's "passion" also repeats Fabian Schmitt's "love of".
- **Product sentence:**
  - Fabian's "FitXpress collects 2 photos and returns one structured record" is Christian Helmes' "FitXpress takes 2 photos in an insurer's application and returns one structured record by API".
  - Dirk's "One structured record comes back" is a third version.
- **Central question:**
  - Fabian ("How does Munich Re admit a new external data source before teams build on it?") and Julia ("Which review would a field like that pass at Munich Re before it could feed a model?") ask one question.
  - Keyvan Izadi was already sent it: "What would a build flag have to pass inside your digital services before a client insurer sees it?"
  - Till and Andreas both close on the same binary shape, "would … want A or B".
- **M2:**
  - Till: "A first read for analysts comes from flag counts at each candidate margin, set against build data the client already holds." This is Christoph Henschel's sent M2: "flag counts at several thresholds, set against build data from other sources. That gives analysis a clean first read".
  - Dirk's "Shadow mode would keep the platform side simple for a first client" is close to Cosima Escher's and Roland's "one client / one insurer, shadow mode" openers.
  - Fabian and Julia share "how often the flag fires" (Keyvan, sent: "The flag fires on…").
  - Dirk and Till share "at each candidate margin".
- **Closer:** Dirk's "…may be the better contact." is word for word Alban Senn's "…may be the better contact."
- **CTA:**
  - Fabian's "I can go through the record fields on a call:" is close to Declan O'Neill's "I can take you through the design on a call:".
  - Andreas's "to go over the fields" twins Fabian's.

**SCOR (4 new against 18 written):**
- Sofia's M2, "the SDK carries the photo step and a REST API returns one record per applicant, on a random identifier", repeats Martijn Reijerse's "FitXpress returns one record per applicant through its REST API, on a random identifier, and the SDKs carry the photo step." Her CTA "I can cover the interfaces … on a call" is close to Martijn's "A call can go through the interfaces".
- Madhu's question "…what would the product side need to see first?" is close to Martijn's "What would a client insurer's IT ask you first about a tool like this?"
- **Closers:**
  - Madhu: "If … sit with another lead, please say whose." It has the frame of Roberto Castellini's "If … led by someone else, please say who." and Lucie Aubry's "If … sit elsewhere, say where."
  - Thibault: "The owner of model risk review is welcome instead." It repeats Manuel Plisson's "The owner of automated build rules is welcome in your place."
- **M2:**
  - Madhu's "…is straightforward in shadow mode" and Thibault's "…are easy to measure in shadow mode" share one opener frame.
  - Kristoph's "flag rates at each margin under test" is close to Roberto's "Flag rates per candidate threshold" and Gianfranco's and Yosra's "each limit under test".
- Sofia's hook "You write about leading…" is the fourth "You lead / You head / You write" opener at SCOR.

**Swiss Re (2 new against 27 written):**
- Mark W.'s closer "If records retention is set by records management or legal, a name is welcome." has the skeleton of Pia Burghartz's "If consulting work on applications is led by another colleague, a name is welcome."
- Mark W.'s M2 "the client's live route stays as it is" repeats Ariane Ehlers' "its current journey stays as it is". Ermir's "the client's live route stays unchanged" is close to Pia's "with the live journey unchanged", and the two new pairs share "the client's live route".
- Ermir's CTA "I would welcome a call to…" repeats Claudia Szwillus's "I would welcome a call to go through the options:".
- Ermir's hook "Your bio puts…" is the sixth bio or headline hook at Swiss Re, after Claude Schwarz, Ian Long, Ginger Turner, Pia and Ariane.
- Ermir's question "How does a data science team judge whether a new field adds anything beyond what it already holds?" adds one more to the "judge or test a new build source" topic. Round 1 already counted about 7 of 28 there, Ueli Konrad and Daniel Meier the closest.

**a.s.r. (1 new against 4 written):**
- Marlot's "FitXpress returns a Smart Scales weight estimate" appears in Gert Lokhorst's M1 and nearly in Angelique R's.
- Her "the margin a.s.r. has set" means 5 of 5 a.s.r. M1s end the flag sentence on "[threshold / margin] a.s.r. sets". That is the stock company tail flagged at New Ireland in round 1.
- Her M2 "a.s.r. would set the margin, and a flag leaves the decision with its own people." has Angelique's skeleton: "a.s.r. sets the threshold, and a flag only refers a case to an underwriter."

**A2. Item 7 says each Irish Life referral person "points to a different owner".**
- Three new easy outs point at one owner: whoever writes build guidance for underwriters.
  - Sean: "the rules for build"
  - SarahJane: "Whoever keeps the guidance for underwriters"
  - Eimear: "a medical director sets the guidance for build"
- Add Shay ("protection underwriting") and Christopher ("risk assessment for protection new business"), and 5 of the 11 referral easy outs target underwriting or build guidance.
- Alan Brady's "operations for new business" sits next to Kelvin's "protection new business".

**A3. The A1 defect is back in 3 M1s: the flag is not tied to the gap from the declared weight.**
- Madhu: "a flag, raised when the insurer's threshold on the weight difference is met". The declared weight is nowhere in the M1, and neither is the no-examination context.
- Sofia: "a flag if the weight difference exceeds the insurer's threshold". She mentions only the declared height.
- Samantha: "When the two weights are further apart than Irish Life allows". The estimate is never named, so "the two weights" has no antecedent.

**A4. Easy outs missing for people who are not the buyer.** The Sender rule says: "for people who are not the buyer, with an easy out: or a pointer to whoever owns it".
- All 12 data and AI chiefs are P3 with no L&H line, and 8 have no easy out: Till, Jürgen, Fabian, Julia, Andreas, Sofia, Kristoph and Ermir.
- For these readers, a pointer to whoever owns L&H data is the most useful line in the pair.
- New easy outs must avoid the closer frames already used at each company (A1).

**A5. Irish Life M2 order.** The card's order for referral is value, then call offer, then easy out. All 7 new M2s put the easy out first and the CTA after it, in one paragraph, as 9 of the 12 sent ones did. That makes 16 of 19 Irish Life M2s share one shape. The effects on the CTA are under C.

### B. Factual accuracy, 3/5

**Clean:**
- Every number comes from the card.
- The 3.5% placement is correct.
- The compliance line is correct by lane in 20 of 20.
- No client, price, pilot or trial term appears.
- No other prospect is named.
- **Every claim about a person matches the profile:**
  - Alan Brady: "over 20 years in banking and life assurance … strategic plans"
  - Denis: Head of Strategy at Liberty Insurance Ireland
  - SarahJane: Digital Product Lead (Vodafone Business)
  - Nicola: "new product introductions"
  - Samantha: "Operating Model Design"
  - Eimear: "Strategic Portfolio Execution"
  - Dirk: "shape the digital future of the insurance industry"
  - Till: "Building Enterprise AI, Data & Analytics Capability"
  - Jürgen: "responsible for Munich Re's Data Assets"
  - Fabian: "Global responsibility for all Data, Analytics and AI activities"
  - Julia: "Passion for Data & AI"
  - Madhu: "integrating innovative technologies to optimize sales processes"
  - Sofia: "data products development"
  - Ermir: "forward-deployed engineers"
  - Marlot: "Medisch Adviseur Inkomen"

**Data handling beyond the card.** The card returns the record "to the insurer's systems". It allows only the `compliance.md` data forms, and it keeps data transfers and special-category data out of cold copy. Nothing in it says what a client insurer passes to its reinsurer. That is the client's decision as controller, and weight is health-related data.
- **Stated as the evaluation design in 5 M2s:**
  - Julia: "A client runs it in shadow and exports the records with their timestamps"
  - Andreas: "The client exports one row per applicant with both weights and the flag"
  - Thibault: "exports one record per scanned applicant"
  - Kristoph: "The client exports the record for each scanned applicant"
  - Ermir: "The client exports the estimate and the declared weight for each scanned applicant, and the team can test the pair offline"
- **Built into the M1 premise:**
  - Dirk: "If a client shared such records"
  - Till: "the raw records or only the client's summary"
  - Jürgen: "if the client shared it", and in his M2 "before any data moves on"
  - Kristoph: "If a client insurer shared records"
  - Mark W.: the whole pair

  A conditional M1 ("If a client shared…") is acceptable. The declarative M2 statements are not.
- **Mark W. is the riskiest pair.**
  - His M1 is about how long Swiss Re keeps client-supplied data and what it may use it for.
  - His M2 opens "Terms for anything a client shares with Swiss Re are simplest to agree before an evaluation starts."
  - His easy out sends him to records management or legal.

  3DLOOK is not a party to those terms, and the pair routes a cold message into Swiss Re's data-retention policy.
- **Julia's M2:** "Nothing connects to production systems." In shadow mode the photo step runs inside the client's live application. The card's boundary is that outputs stay out of decisions. The sentence is absolute, and it contradicts Ginger Turner's sent "beside a live journey".
- **Sofia's M2:** "The insurer's policy sets photo retention, which ends after processing or within 30 days." This paraphrases the compliance form, the defect the first widening QC found in Martijn's M2. "Retention … ends after processing" also misreads the form.

**Implied use.** Alan Brady's M1: "Irish Life sets a limit for how far the estimate may sit from the declared weight." It stands alone, in the present tense, before the step is introduced. It reads as if Irish Life already runs the estimate, and the card says "Never imply an insurer or reinsurer uses FitXpress". Marlot's "the margin a.s.r. has set" is a weaker case.

**Invented company detail.** Dirk's easy out names "The team that operates the data landing zone". No source says Munich Re has such a team.

**Sourcing:** not applicable (outbound).

### C. Brand & tone, 1/3

- **Three-item lists** (a hard ban in both templates):
  - Eimear's M2: "flags counted, no case changed, the insurer's rules unchanged."
  - Nicola's M2: "The step runs, flags are counted, and no case decision changes." This is almost the sentence the first widening QC flagged in Ariane's M2.
  - Lower severity: Thibault's M2, "The client runs …, exports …, and the evaluation counts …".
- **M2s that answer the M1 question for the reader, or read as a reply:**
  - Samantha: "Where a programme does reach the application". The emphatic "does" answers a reply that never came.
  - Eimear: "Such an idea earns its place with evidence."
  - Nicola: "Governance is easier when a change starts as an evaluation only." This lectures a governance head.
  - SarahJane: "Release would come in stages".
  - Fabian: "For an admission review, the most useful evidence is a small shadow run with one client."
  - Thibault: "Missing values are easy to measure in shadow mode." It also misses the point of his own M1: counting missing values is trivial, and the question is the bias.
  - Dangling references across the five-day gap: Denis's "those cases" and Alan Brady's "the plan can use that evidence".
- **Presumed view or presumed reaction:**
  - Marlot's M1: "A medical adviser on income cover meets a software weight estimate with one question first: what may it be used for?"
  - Marlot's M2: "A medical view on the estimate starts from the size of its error".
  - Sean's M1: "Planning for a protection range starts with how people apply for it."
  - Till's M1: "would give central analytics a real data set to read".
  - Ermir's M1: "the kind of input such a team gets asked to judge".
- **Ease claims:**
  - Dirk: "keep the platform side simple" and, in his CTA, "easy to set up"
  - Madhu: "straightforward"
  - Thibault: "easy"
  - Mark W.: "simplest"
- **Idioms** (the card says "no idioms"):
  - Samantha: "otherwise it stays quiet"
  - Dirk: "out of line by more than"
  - Andreas: "the line the insurer draws"
  - Mark W.: "drift apart"
  - Till: "A first read"
  - Eimear: "earn a place" and "earns its place"
  - Madhu: "talk it over"
- **Contorted English:**
  - Jürgen's "Your headline makes you responsible for…" and Fabian's "Your bio gives you global responsibility for…" are a twin contortion: a headline does not make anyone responsible.
  - Andreas: "A model team at Munich Re could meet two weights for one applicant of a client insurer".
  - Madhu: "A photo step … is one such step". The antecedent is "technologies". His closer "please say whose" is incomplete.
  - Sofia: "one more data product for SCOR to receive". One record is not a data product.
  - Jürgen: "would be a new asset to describe" and "such a client field".
  - Alan Brady: "How does the strategic plan weigh a small change…"
  - Denis: "What would protection need from its application journey to grow under Irish Life's strategy?"
  - Eimear: "declared build is one place a small project could start"
  - Thibault: "would raise it for SCOR". His M1 asks one question twice, in the opener and again as the closing question.
  - Nicola: "a small change inside a live journey" appears in both her hook and her question.
  - "small" as a minimiser appears in 5 Irish Life M1s (Samantha, Alan Brady, Nicola twice, Eimear) and in Dirk's.
- **The Irish Life M2 layout, with the easy out and the CTA in one paragraph:**
  - The CTA loses its referent in 4 of 7:
    - Sean: "please point me to them. A call would cover the rest:"
    - SarahJane: "may need to see it first. A short call would cover it:"
    - Alan Brady: "please name whoever leads them. I can explain on a call:"
    - Eimear: "please introduce me there. Happy to discuss on a call:"
  - Nicola stacks two conditionals: "If broker applications follow another process, … If a call makes sense, …".
  - SarahJane, Alan Brady and Eimear call Irish Life "the insurer" to Irish Life staff (minor).

### D. Format & structure, 2/3

- The gate passes limits, signature, link placement and bans (0 hard).
- Paragraph order in every M1 follows the template: hook, product, question.
- In all 7 Irish Life M2s the order is inverted against the card: easy out before the call offer, in one paragraph (A5 and C).
- I did not check `product:` frontmatter. The per-person files were not in my input, as in round 1.

### E. Output quality, 2/4

**Strong:**
- **Questions:**
  - Thibault: how an AI team treats a field that is missing for applicants who do not scan. This is the best data question in the batch, and it fits a former life actuary.
  - Kristoph: who defines the field, SCOR or the client insurer.
  - Till: raw records or only the client's summary.
  - Marlot: should a flag prompt a doctor's weighing or only be noted on the file.
  - SarahJane and Nicola ask answerable process questions.
- **M2s:**
  - Ermir: "A feature test needs paired values, and a shadow run gives them."
  - Jürgen: "In the record, some fields come from the applicant's declaration and others from the scan."

**Mail merge across the batch:**
- **14 of 20 M1s open on the person's bio, headline or career.** That is Irish Life 6 of 7, Munich Re 5 of 6, SCOR 2 of 4 and Swiss Re 1 of 2. Six begin "Your bio" plus a verb: Dirk, Fabian, Nicola, Eimear, Madhu, Ermir. The 2026-11-02 QC top issue and round 1's career-hook finding are the same frame.
- **The data chiefs' M2 value is "the evaluation counts records returned and flags at each margin" in 8 of 12:** Dirk, Fabian, Julia, Andreas, Madhu, Thibault, Kristoph and Mark W. Madhu's "records returned per applicant offered and flag rates at each setting" and Kristoph's "records returned and flag rates at each margin under test" are near twins. "The client exports … per scanned applicant" appears in 5 of 12. Four of 12 open on "simple / easy / straightforward".
- **The Irish Life M2 value is "flags counted / no case changed" in 6 of 7.**
- **Synonym rotation.** "threshold" became margin, limit, range, tolerance, line, trigger, amount, rule and setting. The rotation does not make the copy distinct, and it produces the idioms listed under C.

**Cross-company twins** (the rubric's 60%-unique override):
- Openers:
  - Kristoph: "If a client insurer shared records from a new application step, SCOR would…"
  - Mark W.: "If a client insurer shared the records from an evaluation of a build step, group rules would…"
- Andreas's question repeats Enzo Vitale's (Swiss Re, sent): "…as separate fields, or as one difference?"
- Julia's question ("Which review would a field like that pass at Munich Re before…") and Sofia's ("Which review would an external API at SCOR have to pass before…") share a frame.
- "for each scanned applicant" appears in both Kristoph and Ermir.
- CTAs:
  - "to hear your view": Ermir and Marlot.
  - "a call on this?": Julia, Kristoph and Mark W.
- "clients may test" or "may want to try": Dirk, Fabian and Madhu.
- "Your bio talks about": Madhu (SCOR) and Roland Schneider (Munich Re, sent).
- Sean's "Anyone who does not scan keeps the current route." is close to Yosra Jemai's (SCOR, sent) "Applicants who do not scan keep the current path."

**Question plausibility, data and AI chiefs.**
- **On their role and answerable:** Thibault, Kristoph, Till, Ermir, and Andreas (whose question is copied).
- **Weak:**
  - Mark W. asks about Swiss Re's internal retention rules. The answer is "our data policy", and the easy out routes to legal.
  - Jürgen asks what a data contract would record about the lineage of one vendor field.
  - Fabian, Julia and Sofia ask the same generic admission-gate question.
  - Dirk's question depends on the shared-records premise.
  - Madhu's "When a client asks SCOR for…" presumes the request.

**Irish Life strategy heads.** Sean, Alan Brady and Denis ask a stranger to describe Irish Life's strategy or how its plan weighs one step. Those are unlikely to be answered. Samantha, Nicola, SarahJane and Eimear ask answerable questions.

**Account facts unused:**
- the MIRA Digital Suite for Munich Re's digital and data people;
- AI Assistant for Thibault;
- Magnum for Ermir, whose bio says his team works "across underwriting";
- income protection and term life in Irish Life's range.

Sent colleagues already use these facts, which partly explains the gap. Still, the hooks fell back to bio recitals, as in round 1.

## Top 3 issues (priority for improver)

1. **Same-company repeats, all seven elements, against sent colleagues (item 6).**
   - Near-clones:
     - Samantha's and SarahJane's M2 are Alan Q.'s;
     - Sofia's M2 is Martijn Reijerse's;
     - Till's M2 is Christoph Henschel's;
     - Fabian's and Julia's questions are Keyvan Izadi's.
   - Closers copied:
     - Denis from Shay Browne;
     - Dirk from Alban Senn;
     - Mark W. from Pia Burghartz;
     - Thibault from Manuel Plisson;
     - Madhu from Roberto Castellini.
   - Inside the batch:
     - "flags counted / no case changed" in 6 of 7 Irish Life M2s;
     - "counts records returned and flags at each margin" in 8 of 12 data-chief M2s.
   - The writer checked central questions but not M2 value lines, closers or CTAs, the same gap as round 1.
2. **Round-1 defects back.**
   - 14 of 20 bio, headline or career openers;
   - stock closers;
   - A1 in Madhu, Sofia and Samantha;
   - three Irish Life easy outs pointing at one owner (item 7);
   - 8 non-buyer data chiefs with no easy out.
3. **Data-handling claims beyond the card.**
   - "The client exports …" in 5 data-chief M2s;
   - Mark W.'s retention and terms pair;
   - Julia's "Nothing connects to production systems.";
   - Sofia's paraphrase of the retention form.

## System notes (not scored against the agent)

- **The gate still counts word runs, not frames.** A frame check against `existing-add-*.md` would catch most of A1. It would compare:
  - the first four words of the hook;
  - the closer skeleton: "[role] … may be the better contact", "… is welcome instead", "If … , please point me there", "a name is welcome";
  - the CTA label;
  - the M2 value phrases "flags counted", "no case changed", "records returned", "at each margin".
- **The proposed A1 soft check must look for "declared weight", not "declared".** Sofia's M1 passes a "declared" check on "declared height".
- **A soft check for `export` / `shares with` / `shared` in `reinsurance` copy** would catch the data-handling premise.
- **A soft check for `P3` without an easy out.**
- **`notify.py` was not run,** because this QC session has no Bash. The coordinator should send:
  `❌ QC: message-sequencer → 10/20 (failed). Top issue: 20 add-all pairs repeat sent colleagues at all 5 companies (Samantha/SarahJane M2 = Alan Q., Sofia M2 = Martijn, Till M2 = Christoph Henschel, 5 copied closers); 14/20 bio/career openers; 5 data-chief M2s state the client exports per-applicant records to the reinsurer. Recommend: rewrite Irish Life 7 as a block, new hooks + M2 values for Munich Re 6, line-edit the rest. File: workspace/_quality/outbound/2026-11-12-message-sequencer-eu-insurance-underwriting-widening-2.md`

## Coordinator review

agreement: ✅ agree. My full read caught the retention and field-naming claims (Mark W., Kristoph) and three Irish Life twins, but not the client-export premise in 5 M2s or the frame repeats against sent colleagues.
top_issue: Writers given existing pairs still converge on the sent colleagues' frames, and the data/AI-chief angle as I briefed it ("records a client may share") produced a data-sharing premise the card does not support. Fix round 1 changes the angle to the reinsurer's own underwriting tools reading a third-party field (hypothetical), rewrites the Irish Life 7 as one block from a new grid, and gives every non-buyer an easy out.
