# Vertical (use-case) Page Kit — FitXpress and Mobile Tailor

The page a buyer from one market lands on to answer one question: **have you done this for people
like me, and can I defend the decision internally?** A product page cannot prove that. A vertical
page can — if it is written with that vertical's regulators, workflows, buyer titles and KPIs.

The trap everyone falls into: the vertical page is the product page with the vertical's name swapped
into the headline. That produces a duplicate that cannibalises its own parent and adds nothing. Which
is why this Kit opens with a gate about whether the page should exist, not with a structure.

3DLOOK-specific version of the trap: a vertical page that is really an accuracy pitch. Buyers in
telehealth, insurance and occupational health are not buying millimetres, they are buying a
defensible workflow. `overview.md` says it plainly — sell outcomes, workflow integration and
governance, not "best model".

---

## G-I · Should this page exist at all

Run this **before** the intake questionnaire. Fail it and there is no page — there is a section on the
product page plus the vertical's hub article in the content hub.

- [ ] **A use-case file exists** — `brand-assets/product-info/use-cases/{fx|mt}-{vertical}.md`. It
      supplies the pain, hero message, ICP, buyer titles, KPIs and critical messaging. No file → write
      it first (the same rule `hypothesis-generator` follows) or stop.
- [ ] **2+ publishable case studies from this vertical** in `brand-assets/product-info/case-studies/`.
      One case does not hold a page; zero is fiction. Check the coverage table in `page-types.md` —
      most FitXpress verticals do not clear this today.
- [ ] **Demand exists** — a row in `brand-assets/content-strategy/content-plan.md`, Search Console
      volume on vertical-named queries, or ≥15% of outbound pipeline from
      `workspace/outbound/campaigns/` for this segment.
- [ ] **Five facts that are not on the parent page.** A named regulator or standard, a buyer title
      who signs off, a workflow step, a KPI in the vertical's own units, an integration or export
      format, a procurement or seasonal cycle. Fewer than five → write nothing yet.
- [ ] **The market's BD owner confirms the objections differ** from the general ones — Nick Omelchak
      (USA), Olena Kudryavtseva (Europe), Kateryna Boichuk (Israel), Katerina Galich (UK).
- [ ] **The parent and the URL are settled.** FitXpress verticals are children of `/fitxpress/` and
      live at `/fitxpress/for-{vertical}/`; Mobile Tailor verticals sit under `/mobile-tailor/`
      (Vadim, 2026-09-27) — see `site-inventory.md`.

> **The 60% rule.** At least 60% of a vertical page must be unique against the parent product page.
> Only the workflow overview and the integration basics are shared. Below 60% it is a duplicate, and
> a duplicate is better unpublished.

**If G-I fails:** add a "For [vertical]" section to the product page, link it to the vertical's hub
article, and record the decision with a date. Revisit when the second case lands. A G-I waiver is
possible — Vadim's call, recorded in `gate-reports.md` with the reason and what stands in for the
missing case (an approved reference call, a named pilot, an anonymised deployment).

**Standing G-I waiver for every FitXpress vertical (Vadim, 2026-09-27).** Clients do not agree to public case studies (logos only), so FX vertical pages are built without the 2-case bar. What stands in for cases: customer logos; anonymised figures only from `proof-points.md` (a figure that could identify a client is cleared with Vadim first); the accuracy framework; the trust FAQ; the workflow itself. Never an invented or implied case. The logo row under the hero carries the logos of all 3DLOOK clients, captioned without implying they belong to the vertical (Vadim, 2026-10-06). The vertical's own clients go first, and only then may the caption name the vertical: "100+ clients have used 3DLOOK body scanning since 2016, including fitness teams." (fitness final, 2026-10-07; the fitness row opens with Zing Coach and verv, clients per Vadim 2026-10-07). With no client from the vertical in the row, the caption stops at "since 2016." Alt text is the client's name. The waiver for a vertical ends when its first approved case lands. The other G-I checks (use-case file, demand, 5 facts, 60% rule) still apply. Record `G-I: standing FX waiver 2026-09-27` in `gate-reports.md`.

---

## Length and order: short and commercial (Vadim, 2026-09-30)

A use-case landing converts, and the articles teach. Vadim, 2026-09-30: use-case landings are shorter
and more commercial than the pages built before, and the depth lives in the hub article, the accuracy
framework and the trust FAQ, which the page links to.

- **Budget: 1,100 to 1,600 words of visible copy**, tables and FAQ included, navigation, the hero mock,
  the form and schema excluded (a comparison shown twice, as a desktop table and as mobile cards,
  counts once). Above 1,700 the page is doing an article's job. The ceiling rose from 1,300 on
  2026-10-07: the fitness final runs about 1,560 words, the insurance final about 1,250.
- **One paragraph, then a link.** Anything that needs more than one paragraph of explanation belongs in
  an article. The page keeps one line and links to it.
- **A call to action on every second screen:** the hero, after the "what you get" block, after the pilot
  block, and the form.
- **Structure benchmark (since 2026-10-07):**
  `workspace/pages/for-connected-and-digital-fitness/page-final-2026-10-07.{md,html}`, the fitness
  copy Vadim approved as final ("the latest and the most correct"). Take the block order, the value
  cards, the record table, the comparison, the data lines, the price lines, the pilot and the FAQ from
  it; what it settled is in "Fitness final" below.
- **Register benchmark:** `workspace/pages/for-insurance-underwriting/page-final-2026-10-02.md`,
  the copy passed to design on 2026-10-02 after Asselya's deduplication and guardrails pass
  (`comments-asselya-2026-10-02.md`). It predates the sales rules of 2026-10-06, so it is not the model
  for the H1, the block order or the record table: see "Sell, not educate" below for the five places it
  falls short. The telehealth page stays the benchmark for schema and claims discipline, not for length.

| # | Block, in page order | Words | Slots |
|---|---|---|---|
| 1 | Hero: the H1 (slot 2, two approved forms), with the primary or secondary keyword; 2-3 sentences, what the vertical's actor gets first, then time and effort, the product named by the second sentence at the latest; "Book a demo" to `#demo` and an anchor to the record block; a four-fact strip; then the client logo row. An illustrative product mock is allowed when captioned "Illustrative example", and it shows no field the record table does not list | ~90 | 1, 2, 3, 15 |
| 2 | Value for the end user: an eyebrow naming that user ("For members", "For patients"), a statement H2, one intro line, four cards (a benefit H3 and one sentence each, saying what the platform can show or offer), then the hub-article link with its topic in the label ("Body data in fitness apps, in depth: AI in fitness →") | ~80 | 5, 6 |
| 3 | The problem: a question H2, one sentence on what the gap costs this buyer (money, risk, time or retention) without repeating the hero, two or three numbers from named industry sources backing that sentence, each source label linked to the primary source, and one closing sentence on what the loss costs | ~90 | 4, 5 |
| 4 | What you get (`id="record"`): a five-row table, each returned output beside what it changes for the actor (neutral column headings, e.g. "Returned output" and "What it changes for the app"), the boundary sentence, then "See a sample record in the demo" to `#demo` | ~170 | 6 |
| 5 | How it works in three steps, in the vertical's own systems, each step saying what it spares or gives the actor; the recommended setup in one line; a link to the feature page | ~110 | 7, 12 |
| 6 | "FitXpress compared with…": a four- or five-row table on desktop and one card per option on mobile, one sentence on what the comparison means for this buyer, and one line on where the old method still fits | ~130 | 5 |
| 7 | Accuracy and data handling on one screen, under a question H2 ("How accurate is FitXpress, and how is … data handled?"): the answer in the first sentence, then two or three figures, one method sentence, five data lines (slot 8), the trust-FAQ sentence ending with the privacy contact, the accuracy framework link | ~200 | 8, 9 |
| 8 | Pilot and price: a formal H2, the low-risk start first, one production-infrastructure sentence (one, not a paragraph), one line per tier, the "no integration fee" and custom-plans line, `/pricing/`, three steps (walkthrough, pilot cohort against a comparison cohort, evaluate and roll out), what the platform and 3DLOOK track as a short list, a demo button | ~190 | 10, 14 |
| 9 | FAQ: 4-6 questions, GEO phrases from the keyword map verbatim as H3, the answer in the first sentence; one integration question links to the FitXpress API documentation | ~280 | 13 |
| 10 | The shared form at `#demo` with a soft exit to the hub article; `legal@3dlook.me` for procurement documents in the footer. No separate "keep reading" block | ~50 | 15, 16 |

The order and the budget decide the page. "What you get" sits before "How it works" since 2026-10-06
(sales rule 2: value before explanation), and since 2026-10-07 the value cards for the end user open the
page, before the problem (the fitness final). The slots below say what each ingredient must contain.

## Sell, not educate (Vadim, 2026-10-06)

Use-case landings need a stronger sales angle, because their job is to close leads. Vadim passed on the
team's writing rules on 2026-10-06. Verbatim:

> 1. **H1 = product + audience + primary outcome.** Keep it clear, specific, and outcome-focused.
> 2. **Lead with value, not explanation.** Tell the customer what they get before explaining how it works.
> 3. **Write to sell, not educate.** A landing page is not an article or product guide.
> 4. **State conclusions directly.** Never make the reader connect the dots.
> 5. **Turn features into benefits.** Always answer: "Why should the customer care?"
> 6. **Give each section one job.** One section = one message, benefit, or objection.
> 7. **Cut unnecessary explanation.** Remove technical details, background, and process unless they help the buying decision.
> 8. **Keep it concise.** Remove filler, repetition, qualifiers, and long-winded phrasing.
> 9. **Use proof to support the claim.** Stats, studies, and technical details should strengthen the argument—not become the argument.
> 10. **Apply the "blog test."** If a paragraph could be moved to a blog post without weakening the sales argument, cut it.

What each rule means on a use-case landing:

- **H1 (rule 1).** The product name, the audience and the one outcome that audience pays for, in the H1
  itself, not only in the eyebrow. The primary keyword stays in it (slot 2). An output is not an
  outcome: "build and BMI evidence" is what FitXpress returns; checking disclosed build without slowing
  the accelerated path is why a carrier buys it. **Second approved form (fitness final, 2026-10-07):**
  the H1 names the method the buyer already knows and offers the mobile alternative to it, for the
  audience ("A mobile gym body scanner alternative for fitness apps"). The H1 then carries the
  category keyword the buyer searches, the outcome opens the lede ("Give members a clearer view of body
  progress at each check-in."), and FitXpress is named in the lede's second sentence at the latest.
  Use it when the buyer compares against a known method or device; otherwise use the formula.
- **Value before mechanics (rule 2).** The hero opens with what the actor gets. Time and effort ("under
  45 seconds", "on the applicant's own phone") count as value; how the capture works does not belong in
  the hero. On the page, "What you get" comes before "How it works".
- **Conclusions stated (rule 4).** Every number, table and comparison is followed or preceded by one
  sentence saying what it means for this buyer: money, risk, time or retention. "Build is the leading
  misclassification reason" is evidence; the sentence that follows says what that misclassification
  costs the carrier. The question H2s stay (problem and accuracy, Asselya's register), and the first
  sentence under each one is the answer, not a lead-in.
- **Benefits (rule 5).** Every feature answers "why should the actor care?" in the same sentence or the
  next. The "What you get" table carries the answer in its own column. A feature with no answer is cut.
- **One job per block (rule 6).** The blocks in the table above are the jobs: the outcome (hero), the
  cost of the gap (problem), what the actor gets, the effort to adopt (how it works), why not the old
  method (comparison), whether it can be trusted (accuracy and data), a low-risk start and the price
  (pilot), the remaining objections (FAQ), the action (form). A sentence doing another block's job moves
  there or goes. A statement H2 names the block's message, not its topic: "The underwriting case-file
  output" is a topic.
- **Explanation only where it moves the decision (rules 7 and 3).** Technical detail stays when it
  removes a buying objection: integration effort (the SDK or API and the system the result lands in),
  data handling for a regulated buyer, accuracy with its method. Model internals, capture mechanics,
  market background and definitions go to the linked article, or to the FAQ when buyers really ask.
- **Concise (rule 8).** Filler, repeats, stacked hedges and long-winded phrasing go. **Not filler:**
  the qualifiers the guardrails require, meaning the hedge on an outcome without an internal figure
  (guardrail #1: "may reduce", "can help"), the method sentence beside the accuracy figures (#4), the
  boundary sentence (#6) and "available when enabled for the deployment" (register). When a sales rule
  and a guardrail pull apart, the guardrail wins and the sentence is rewritten so it sells inside it.
- **Proof behind the claim (rule 9).** Claim first, proof after. The three problem numbers back one
  sentence about the cost of the gap; the accuracy figures back the answer to the accuracy H2. A strip
  of numbers with no claim above it, or a block that is mostly method, has made the proof the argument.
- **The blog test (rule 10).** Before the judge, read every paragraph and ask whether it could move to
  the hub article without weakening the case for a demo. If it could, cut it and leave a one-line link
  when the depth matters. Record the cuts in `log.md`.

The sales rules decide what each sentence does; the register rules below decide how it sounds. Both
apply. "Sell" never licenses direct address above 12.5 per 1,000 words, figurative headings or an
unsubstantiated outcome.

**Where the insurance benchmark falls short of these rules.** `page-final-2026-10-02.md` was approved
before them, so do not copy these five: (1) the H1 "Second-source build and BMI evidence for accelerated
underwriting" names neither the product nor the audience and states an output; (2) "How it works" comes
before the record; (3) the record table lists outputs with no "what it changes" column; (4) the problem
block leaves the cost of misclassification for the reader to infer ("The remaining gap is independent
build evidence"); (5) the pilot block spends a second sentence on infrastructure, which fails the blog
test.

Illustrative H1s (not approved copy; the final H1 is Vadim's call):
"FitXpress for life insurers: check disclosed build without slowing accelerated underwriting" ·
"FitXpress for fitness apps: help retain members with a mobile alternative to the gym body scanner".
Approved H1 in the second form: "A mobile gym body scanner alternative for fitness apps" (fitness final,
2026-10-07).
An outcome verb without an internal figure keeps its guardrail #1 hedge in the H1 too ("help retain", not
"retain"): the blind judge flagged the unhedged form on the fitness page, 2026-10-06.

## Register for an enterprise reader (Asselya, 2026-10-02)

Asselya's pass on the insurance v2 ran 21 edits. Nearly all of them apply rules the terminology
guardrails already had, which v2 broke anyway, so they are now checks rather than advice. Layer 0 of
`copy-humanisation.md` reports the first three mechanically (`detect-ai-tells.py --channel page`).

- **Direct address within budget: at most 12.5 "you / your" per 1,000 words.** v2 ran 23.7 and the final
  runs 12.1. Explanatory sentences name the actor: "the carrier's rules determine case routing", "the
  platform". "Your" stays for ownership and control ("your threshold", "your systems") and for the
  calls to action. Table and section headings carry no direct address ("Returned output", not "What
  your underwriter gets").
- **Every acronym expanded at first use**, the product's own included: software development kit (SDK),
  application programming interface (API), non-disclosure agreement (NDA), Business Associate Agreement
  (BAA), System and Organization Controls 2 (SOC 2), U.S. Food and Drug Administration (FDA),
  Real-Time Pose Validation (RTPV). Bare: AI, WWW, iOS, BMI, CEO, UK, US, EU per the Doc, and HIPAA and
  GDPR as on the final insurance page (not yet in Asselya's Doc list: open item). "IDs" becomes
  "identifiers".
- **No "vs" in headings.** "FitXpress compared with self-report and a paramedical examination". Inside a
  table cell "vs" stays.
- **A named subject in every sentence.** "FitXpress returns one record per applicant", not "One record
  per applicant. It returns over the API…". No fragments in data lines, and no action attributed to a
  thing that cannot act ("failure reasons return with the record" becomes "FitXpress returns the
  failure reasons with the record").
- **Relationships stated, not compressed.** "The carrier-defined threshold determines whether the
  response includes a disclosure flag", not "a gap above your threshold comes back flagged". What
  depends on configuration says so: "available when enabled for the deployment", not "available if you
  need them".
- **No figurative or conversational phrasing** in headings and claims: "kept its weight", "where it
  leaks", "Prove it", "touches a live decision", "before day one", "You finish with numbers" were all
  replaced. The pilot H2 names the evaluation boundary in the vertical's own terms.
- **No corrective negation as an opener.** "No new app for the applicant and no new queue for your team"
  became a positive statement of how FitXpress is embedded and where results go.
- **Deduplication.** The problem sentence does not restate the hero. An FAQ question that a block above
  already answers is cut: the shadow-evaluation and internal-only questions went, leaving four. Count
  repeats across blocks before the judge sees the page.
- **Source links on the label.** Each problem statistic carries its source as "Publisher, study name",
  linked to the primary source (terminology guardrails §1, rule 2).

**Product wording that changed on the final page (Vadim-approved 2026-10-02):** Weight reads
"approximately 3.5% mean absolute error under evaluated conditions". The pilot block proves readiness
with one sentence ("FitXpress uses production infrastructure already deployed in remote
BMI-verification and weight-management workflows"), without naming a client's market or a client count.
The capture wording of that page ("pauses capture until pose and framing requirements are met";
clothing-related information "surfaced for review") is superseded on new pages by the safer wording in
"Fitness final" below until product confirms it.

## Fitness final (Vadim, 2026-10-07)

Vadim approved `workspace/pages/for-connected-and-digital-fitness/page-final-2026-10-07.html` as the
final fitness page: v3 merged with the team's fixes and the fitness logos. What it settled, now rules
for every FX use-case landing:

- **The value cards come first.** Right after the hero and the logo row: four cards for the end user
  (members, patients, employees), each a benefit H3 and one sentence on what the platform can show or
  offer, then the hub-article link. The problem block follows them.
- **The H1 has a second approved form**, the mobile alternative to the method the buyer already knows
  ("Sell, not educate", rule 1). The product is then named in the lede by its second sentence.
- **Capture claims stay at the confirmed level until product confirms more.** Real-Time Pose Validation
  "gives pose and framing guidance during capture, with voice prompts for a member scanning alone". Not
  "pauses capture until…", not "helps avoid retakes". The record table lists "Processing status and
  timestamps", not pose and framing validation results or clothing-related information, and the hero
  mock carries no "Pose passed / Framing passed" chips. Open item P1-P2 in the fitness folder; when
  product answers, one wording goes to every page, the insurance final included.
- **The platform owns the identity link.** "FitXpress returns the record through its API, and the
  platform links each scan ID to the member profile." FitXpress never returns a record "to the member
  profile" or to a named person (CLAUDE.md §12: 3DLOOK does not track people).
- **White-label carries its boundary.** "The platform designs the onboarding, consent and results
  screens; the photo-capture layer, where pose validation runs, stays fixed to protect measurement
  quality." (`tech-spec.md`, "What's NOT customizable").
- **Five data lines:** Photos · Identifiers · GDPR (or the HIPAA/BAA line on a US health page) ·
  Encryption ("Data is encrypted in transit and at rest.") · Model training. The trust-FAQ sentence
  then ends with "Privacy contact: privacy@3dlook.me". The procurement address `legal@3dlook.me` stays
  in the footer.
- **One line per price tier.** "Starter. $1,000 a month for up to 500 scans." · "Pro. $1,500 a month
  for up to 1,000 scans, adding 3D Body Progress tracking and 3D Goal Visualization." · "Both include
  guided implementation support, with no integration fee. Custom plans cover higher volumes." Re-read
  the live `/pricing/` before shipping.
- **The pilot is a controlled comparison.** "A comparable cohort keeps the usual check-in flow. Where
  practical, members are assigned randomly before the pilot." Write "comparison cohort", not
  "holdout". The third step is "Evaluate and roll out": outcomes are measured against criteria agreed
  before the pilot, and the scan goes live only if they are met. What the platform and 3DLOOK track is a
  short list, opening with scan completion and retake rates.
- **The secondary call to action says what happens in the demo.** "See a sample record in the demo",
  not "Request a sample record" or "Get a sample": the form books a demo and sends nothing.
- **FAQ answers carry their dependency.** An objection is answered with how the pilot measures it ("The
  pilot compares onboarding completion with the usual flow and measures scan completion separately").
  A third-party integration answer ends on what it depends on ("The integration depends on the fields
  and permissions supported by the destination platform."). One integration question links to the
  [FitXpress API documentation](https://docs.fitxpress.3dlook.me/). A capture-conditions answer uses the
  recommended capture environment in `tech-spec.md` (form-fitting clothing, the phone on a stable
  surface); open item P3 until product confirms the list.
- **Source labels are "Publisher, study name".** No year or data-scope qualifier on the label
  ("Adjust, mobile app retention benchmarks"); `fact-sheet.md` keeps the year and the scope.
- **The comparison turns into cards on mobile.** Under 960 px the table hides and each option becomes a
  card, the FitXpress card first and highlighted (`ux-pass.md`).

## Slots: the 17 ingredients

**1. Breadcrumbs** — three levels for both products: `Home → FitXpress → [Vertical]` and
`Home → Mobile Tailor → [Vertical]` (hierarchy of 2026-09-27). `/fitxpress/` ships with the use-case
release (`docs/page-pipeline.md`); until it is live, do not link a middle level that resolves to a
redirect.

**2. H1** — product + audience + primary outcome (sales rule 1, 2026-10-06), e.g.
`[Product] for [audience]: [primary outcome]`. The product name sits in the H1 itself, not only in the
eyebrow. Second approved form (fitness final, 2026-10-07): `A mobile [known method] alternative for
[audience]`, with the outcome opening the lede and the product named by its second sentence. The
audience is named the way it names itself (life insurers, fitness apps, online pharmacies). The outcome
is what that audience pays for, not what FitXpress returns. Not "AI-powered precision", and not an
output list. One H1. Primary query in it and in the first 100 words; in the second form the H1 carries
the category query the buyer searches ("gym body scanner"), and the focus keyphrase sits in the SEO
title and the meta description. No "best",
no "most accurate", no banned words from CLAUDE.md §6. `detect-ai-tells.py --channel page` reports an H1
without the product name in the H1 or the first two sentences of the lede.

**3. Hero + a vertical proof point** — one sentence on what the vertical's actor gets (the outcome), then
how fast and with how little effort, plus a number from **this** vertical: scans delivered for a named
customer in this market, or the KPI the use-case file names. No description of the process in the hero. A company-wide scale figure appears only as "100+ clients", the one public number everywhere
(Vadim, 2026-09-30). "112,100 scans" and "67 clients" never appear on a page. An approved vertical
figure beats both.

**4. Vertical context — the slot the page exists for** — 3–5 specifics only someone who has worked in
this market knows: the regulators and frameworks that actually come up (HIPAA in US health, GDPR in
the EU, MHRA / CQC / NHS in the UK, FDA / ICH / GCP in trials), who signs off and who blocks,
the procurement cycle, the units results are measured in, the export formats, the seasonality.
Source: the use-case file plus the BD owner's answers. On the short page these facts are not an essay
of their own: they surface in the problem numbers, the systems named in the three steps (PAS, EHR,
benefits platform) and the FAQ.

**5. Pains of this vertical** — from the use-case file's "The pain we remove" and `audience.md`'s
segment hook, in the buyer's phrasing. Then honour that segment's **"what NOT to say"** list.

**6. What the product is here + the boundary** — scope in the vertical's own words: what is captured,
what is returned, what is documented. Then one clear boundary sentence: *"FitXpress is not a medical
device."* One negative, stated once — guardrail #6 for the framing, M2 for not chaining a second
negation onto it. "Positioned as" is banned (terminology guardrail §2.10, since 2026-09-11).

**7. How it works, three steps** — do not restate the whole product flow. Three steps as they run in
this vertical, in its own systems: what the person does, what FitXpress returns, where the result goes
and who acts on it (consent capture, retake logic, who reviews a flagged scan, how the record is filed).
Each step says what it spares or gives the actor (no appointment, no new queue, the result in the
system the team already uses). Process detail that does not change the buying decision goes to the
feature page.

**8. Data handling: five lines and a link** — for regulated verticals this still decides deals, so it
sits on the proof screen next to the accuracy figures, but short. Wording as on the final insurance
page: "Deleted immediately after processing or retained for up to 30 days under a customer-specific
policy. Retained photos are blurred, and face obfuscation is applied during capture." · "Scan records
use anonymized, randomly generated identifiers." · HIPAA support under an executed Business Associate
Agreement (BAA) on a US health page, or the canonical GDPR role sentence · "Data is encrypted in transit
and at rest." · no training on production data without explicit, documented authorization (fitness
final, 2026-10-07). The boundary sentence sits under the record table. Hosting, the encryption detail
(TLS, SSE-S3), deletion by scan ID, SOC 2, FDA and consent go to one link to the
[trust FAQ](https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/), written as a
sentence that says what the FAQ covers and expands SOC 2 and FDA, ending with "Privacy contact:
privacy@3dlook.me". Source:
`compliance.md` (rebuilt 2026-09-18 from that FAQ) and `CLAUDE.md` §12. Never "HIPAA compliant",
"SOC 2 certified" or "no personal identifiers" (detector category `compliance_status`), and never a
control presented as removing risk (guardrail #5).

**9. Accuracy, scoped in three figures and a link** — three oversized figures, each with its
reference: 96-97% vs expert manual measurement with typical absolute error 1.5-2.0 cm, repeatability
written as `< 1 cm`, and, where weight matters to the vertical, "approximately 3.5% mean absolute error
under evaluated conditions" (the final insurance page's wording, 2026-10-02; `proof-points.md` still
says "±3.5% average error, real-world conditions", open item for Vadim). Then one sentence
on the method and its limit (internal validation; peer review and third-party clinical certification
are not part of that record; methodology under a non-disclosure agreement (NDA)) and a link to the
[accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/), which carries the
"accurate enough for which decision?" reframe and the four conditions (reference method, protocol,
population, workflow). Wording from `accuracy-formulations.md`, numbers from `proof-points.md`. No bare
">95%" (guardrail #4). "Independent", "validated" and "third-party" never appear as claims
(guardrail #3).

**10. Cases from this vertical only** — 2 cards minimum, each with a number from
`case-studies/`, linked to `/case-studies/`. A case from an adjacent vertical breaks the page's whole
promise. Mobile Tailor customer ARRs never appear.

**11. Customer quote from this vertical** — name, role, company, only where that use is approved. No
approved quote → the slot is dropped and recorded. Never an invented name, role or testimonial.

**12. Integration, formats and support** — API plus web and mobile SDKs, web widget, CSV export, 3D
model export, what it plugs into in this vertical (EHR / patient portal, PAS, OMS, pattern-making,
benefits platform), white-label options, implementation support. Source: `tech-spec.md` and the
published tier features. The signal is "we are already inside your environment". On the short page
this folds into the three steps and the record table: API plus web and mobile SDKs, and the system the
result lands in. Formats and white-label detail go to the FAQ only when the vertical asks for them.

**13. Vertical FAQ** — the questions asked here and nowhere else: regulatory, licensing, data
residency, retention, who owns the data, what happens on a failed scan, what a pilot looks like.
Source: `faq.md` plus the BD owner's real objections. General product questions stay on the product
page. **4-6 questions** (the final insurance page ships four), none that a block above already
answers. The GEO phrases from the landing's keyword map go in verbatim as H3, and each
answer opens with the answer. One integration question links to the FitXpress API documentation, and a
third-party integration answer ends on what it depends on ("Fitness final" above). Ships with FAQPage schema, modelled on the markup of
`/structured-body-data-for-telehealth-digital-health-programs/` (its schema, not its 13-question length).

**14. Price signal** — name the entry tier and link to `/pricing/` (FitXpress from $1,000/mo,
Mobile Tailor from $499/mo as published on 2026-08-23 — re-check before shipping). On FitXpress pages
the pilot block lists each tier on its own line and closes with "Custom plans cover higher volumes."
("Fitness final" above). FitXpress pages also say **"no integration fee"** (Vadim, 2026-09-30: true, and an advantage over competitors). No
public trial: the action is always "Book a demo" (Vadim, 2026-09-27). Never the internal per-request
rates from `pricing.md`.

**15. Primary action + form** — one action, in the site's own language ("Book a demo" / "Talk to
sales" / "Start a trial"), visible without scrolling and repeated at the end. Minimal fields, visible
consent, confirmation state.

**FitXpress pages: one shared form, never a page-specific one (Vadim, 2026-09-29).** Every FX page
(`/fitxpress/`, each `/fitxpress/for-{vertical}/`, the BMI verification page) embeds the same HubSpot
form `FX | LP | Demo`; submission opens HubSpot Meetings. The page does not configure anything per
vertical: GTM writes the hidden field `fx_vertical` from the page path. The form section carries the
anchor `id="demo"`, because hub articles link to `/fitxpress/for-{vertical}/#demo` from their
"Book a demo" button. Do not spec new fields or a new form for a vertical; a field every vertical
needs goes into the shared form. Source: `workspace/research/seo-fitxpress-2026-09/2026-09-27-tz-tracking-hubspot-ga4.md`
(A1, B1, B2.5).

**Shared-form field added 2026-09-30 (Vadim):** optional "Expected monthly scan volume" (under 500 ·
500-1,000 · 1,000-5,000 · over 5,000 · not sure yet). It started as a page-specific field in Nika's
insurance draft; it qualifies the lead in every vertical, so it lives in the shared form (tracking TZ B1).

**16. Soft alternative + sibling verticals** — for buyers not ready to talk: the accuracy framework
article, the vertical's hub article, the ebook, a vertical checklist. Then cards for two sibling
verticals and a link up to the product page. Per the four linking directions in `site-inventory.md`.

**17. Hidden technical layer** — Service (or Product) schema with `audience` and `areaServed`,
FAQPage on the FAQ block, BreadcrumbList on the crumbs, canonical to self, Yoast title ≤ 60 and
description ≤ 155 characters, clean URL.

## Slots by category

| Category | Slots |
|---|---|
| **Proof of belonging** | vertical context · compliance · integration and formats · vertical cases · quote |
| **Offer clarity** | H1 formula · vertical pains · scope and the boundary · where the workflow differs · price signal |
| **Claims discipline** | scoped accuracy block · every figure traced to `proof-points.md` · guardrails #1–#6 |
| **Conversion** | hero action · inline actions · final form · soft alternative · sibling verticals |
| **Search & AI visibility** | breadcrumbs · single H1 · vertical FAQ + FAQPage schema · canonical · link up to the parent |

---

## Intake — who answers what

The point is to extract what is **not** on the product page. Questions are deliberately narrow.

**A. Vertical context** — Which frameworks and regulators actually come up on calls in this market?
Who approves, who blocks, and how is that different from other verticals? Typical cycle from first
contact to signature? What units does this buyer measure results in? What deadlines or seasonality
drive their timelines? *(BD owner for the market + the use-case file.)*

**B. Language** — What does this buyer call what we deliver, verbatim? Which words from the product
page are meaningless to them? Three verbatim pain phrases from recent calls. *(BD owner + `audience.md`.)*

**C. Differences in the workflow** — What runs differently here, and why? What consent, retention or
residency requirements apply? What does it integrate with in this vertical? *(Vadim + `tech-spec.md`.)*

**D. Proof** — How many scans, in which markets, for which named customers in this vertical? Which
2–3 cases can be shown with numbers? Which customer will give a quote with name and company, and is
that use approved? *(`case-studies/` + Vadim.)*

**E. Objections** — Which questions get asked here and nowhere else? What killed deals in this
vertical specifically? *(BD owner + `faq.md`.)*

**F. Positioning and claims** — Anything in the draft that bends a guardrail goes to Asselya, per
principle #11. Medical, clinical or regulatory framing goes to Whitney before it ships.

---

## Writer SOP

1. **Read two pages first:** the parent — the homepage for FitXpress, `/mobile-tailor/` for Mobile
   Tailor — so nothing gets copied from it, and
   `/structured-body-data-for-telehealth-digital-health-programs/`, which is the in-house benchmark —
   scoped accuracy, a real comparison block, a 13-question FAQ with schema, no banned words in the
   headings. Take its schema and its claims discipline, not its length: the budget is 1,100 to 1,600
   words ("Length and order" above). The structure benchmark is
   `workspace/pages/for-connected-and-digital-fitness/page-final-2026-10-07.md` (block order, value
   cards, record table, data lines, price lines, pilot, FAQ), and the register benchmark is
   `workspace/pages/for-insurance-underwriting/page-final-2026-10-02.md`, which predates the sales
   rules, so take the H1, the block order and the record table from the fitness final, not from it.
2. **Read the use-case file, `audience.md` and the segment's "what NOT to say"** before the first
   sentence. A vertical page written without them is a product page with a new headline.
3. **Check the 60% rule before handover** — count the paragraphs with no equivalent on the parent.
   Under 60%, go back for material.
4. **Every number from `proof-points.md`; every client name and client metric from `case-studies/`.**
   Anything else goes to Open items. One number, byte-identical everywhere on the page (guardrail #2).
5. **Name regulators and standards precisely** — the framework, the jurisdiction, and what it governs.
   A vague gesture at a standard is worse than omitting it. Expand every acronym at first use, FDA,
   ICH, GCP and DXA included (M1). BMI, CEO, UK, US and EU are commonly known and stay bare.
   IEEE appears only in the two approved sentences from `proof-points.md`, and never as a standalone
   logo in a recognition strip (terminology guardrail §2.11). Outputs are "80+ body measurements";
   BMI and BMR are calculated metrics and body composition is an estimate (§2.13).
   Name the vertical's actor: "the pharmacy", "the clinic", "the employer", "the insurer". A vertical
   page always knows who acts, so a generic "organization" is a miss here (§2.14, synced 2026-09-28).
6. **Scope accuracy, never brag about it.** Every figure carries its reference and its limit, and the
   page links to the accuracy framework for the reframe (slot 9). Leading with "most accurate" or
   "best-in-class" is an anti-positioning violation and a hard fail at the judge.
7. **State the boundary once**, directly: "FitXpress is not a medical device." Do not chain a
   second negation onto it (M2), and do not write "positioned as" (terminology guardrail §2.10).
8. **Only your own cases from this vertical.** Fewer than two means G-I should have stopped the page.
9. **Do not restate the whole workflow.** Differences only.
10. **FAQ stays narrow: 4-6 questions.** General questions belong on the product page, long answers
    in the articles, and a question the page body already answers is cut.
11. **Links up, sideways, to the hub article and to conversion** — all four directions, every page.
12. **Mark visuals:** `[HERO]`, `[CONTEXT]`, `[COMPLIANCE]`, `[WORKFLOW]`, `[ACCURACY]`,
    `[CASE CARD]`, `[QUOTE]`, `[INTEGRATION]`.
13. **Run the sales pass** after the draft is finished and before humanisation, because it cuts and
    moves content and humanisation polishes what is left. Take the ten rules in "Sell, not educate" as a
    checklist, block by block: the H1 formula, value before mechanics, a conclusion after every number
    and table, a benefit beside every feature, one job per block, and the blog test on every paragraph.
    Record the cuts in `log.md`.
14. **Run `copy-humanisation.md` as its own pass** after the sales pass. Negative parallelism
    ("not just X — it's Y"), rule-of-three triads and the CLAUDE.md §6 banned words are hard fails at
    the judge, not style preferences. Then the register checks above: direct address within 12.5 per
    1,000 words, every acronym expanded, no "vs" in headings, a named subject in every sentence, and a
    deduplication read across blocks.
15. **Fact-check** every figure, customer name, framework and price against the sources before
    handover, and write `fact-sheet.md` for the blind judge as you go.

---

## Technical checklist

**URL and anti-cannibalisation** — `/fitxpress/for-{vertical}/` for FitXpress, `/mobile-tailor/for-{vertical}/`
for Mobile Tailor · canonical to self, never to the parent · request the in-body link down from the
parent, which no parent page currently has ·
run a cannibalisation check against both inventories before writing and against Search Console after
indexing · Yoast title and description differ from the parent's and from the vertical's hub article.

**Schema** — Service or Product with `audience` and `areaServed` · FAQPage on the FAQ block ·
BreadcrumbList with the full chain · Organization comes from the Yoast site template.

**Template and analytics** — sticky CTA on mobile · form with minimal fields, visible consent and a
confirmation state · analytics events on form view, first input, submit, and demo-link clicks (FX
names: `generate_lead` with `form_name = fx_lp_demo` and `fx_vertical`, `demo_click`,
`meeting_booked`) ·
sibling-vertical block · WebP, lazy-load, images under 200KB · indexable, in the sitemap, inbound
internal links in place.

---

## Designer brief — tokens from `DESIGN.md`, no exceptions

| Marker | What to produce |
|---|---|
| `[HERO]` | First screen: H1, one sentence, the vertical's number as an oversized numeral, one action. Navy `#050F40` with the radial glow, or white |
| `[CONTEXT]` | Vertical realities: stakeholder-and-cycle diagram or a regulator chip row, 15px radius chips |
| `[COMPLIANCE]` | Five short data-handling lines beside the accuracy figures, one screen. No padlock icons |
| `[WORKFLOW]` | The diverging steps highlighted against the base flow, readable on mobile |
| `[ACCURACY]` | Three oversized numerals, each with its reference underneath. The number is the hero |
| `[CASE CARD]` | Vertical case card: customer, number, link. 20px radius |
| `[QUOTE]` | Pull quote with photo or logo, only where the use is approved |
| `[INTEGRATION]` | API / SDK / widget / export as a diagram, not an icon grid |

Satoshi throughout. `#143DFF` stays a single sharp accent — never a large fill. Real product imagery
(guided-capture UI, 3D body render, admin panel in a frame) over stock or generic icons. Precision as
the visual language: measurement lines, keypoint dots, exact numerals. Alt text on every visual,
mobile checked.

---

## Campaign landing variant

Same Kit with four changes: no site navigation, no sibling-vertical block, exactly one action on the
page, and the soft alternative replaced by the gated asset itself. The vertical context, compliance
and accuracy slots stay — they are what makes a cold visitor believe the page. Landing pages live at
their own URL and are never a copy of the vertical page.

---

## Pre-launch checklist

- [ ] G-I passed, or the waiver recorded with its reason
- [ ] 60% uniqueness against the parent held and counted
- [ ] Parent exists, breadcrumbs resolve, canonical to self
- [ ] Vertical context carries ≥3 facts absent from the parent page
- [ ] Regulators and frameworks named precisely; every acronym expanded at first use
- [ ] Visible copy 1,100 to 1,600 words; FAQ 4-6 questions, none repeating the body; a call to action on every second screen
- [ ] H1 = product + audience + primary outcome, or the approved "mobile [method] alternative for [audience]" form with the product named in the lede by its second sentence (detector `--channel page` reports a hero without the product)
- [ ] "Fitness final" rules held: value cards before the problem; capture claims at the confirmed level; the platform links scan IDs; white-label with its boundary; five data lines and the privacy contact; one line per tier; comparison cohort and an evaluate step; "See a sample record in the demo"
- [ ] Sales pass done: "What you get" before "How it works"; a benefit beside every feature; a conclusion with every number, table and comparison; one job per block; no paragraph that passes the blog test
- [ ] Register: "you / your" at most 12.5 per 1,000 words, actor named in explanatory sentences; every acronym expanded at first use; no "vs" in headings (detector `--channel page` reports all three)
- [ ] Accuracy figures carry their reference and limit, plus a link to the accuracy framework; no bare percentages; no reserved words
- [ ] Boundary sentence present, stated once, in the approved wording
- [ ] 2+ cases from this vertical with numbers from `case-studies/`
- [ ] Every figure traced to `proof-points.md` and identical everywhere it appears
- [ ] Data-handling lines worded from `compliance.md`, plus the trust-FAQ link
- [ ] Price signal ("no integration fee" on FitXpress) plus a link to `/pricing/`; no public trial, no internal rates, no MT ARRs
- [ ] Vertical FAQ narrow, plus FAQPage schema that validates
- [ ] Links up, sideways to two siblings, to the hub article, to conversion
- [ ] One primary action; analytics events verified manually
- [ ] All `[markers]` replaced; alt text everywhere; mobile checked at 375 and 768
- [ ] Open items block listing every bent guardrail, for Asselya
