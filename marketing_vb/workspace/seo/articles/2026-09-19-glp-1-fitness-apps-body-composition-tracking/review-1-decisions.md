---
article: 2026-09-19-glp-1-fitness-apps-body-composition-tracking
published_slug: glp-1-muscle-loss-fitness-apps
review: 1
review_source: review-1.md (verbatim extract of the Google Doc tab "Review 1", 2026-10-20)
written: 2026-10-20
written_by: coordinator
reviewed_text: "v1/final.md (the Doc tab «Version 1»), NOT the current text. The QC fix pass of 19.09 already changed some lines the reviewer quotes. The current text is snapshotted in v2/ (draft, final, plan, plan-audit, publish-package)."
round_type: "STRUCTURAL. The review replaces the section skeleton, so it is applied to plan.md first and the stages run again: plan -> write -> edit -> publish -> qc -> git."
authority: "THIS FILE WINS over review-1.md wherever the two differ. Agents read both."
next_stages: plan (seo-planner) -> write (seo-writer) -> edit (seo-editor) -> publish (seo-publisher) -> qc (seo-qc)
---

# Review 1 — decisions

**How to read this file.** Every review item has a disposition and the source that grounds it.
**verbatim** = place the quoted sentence exactly, do not paraphrase or improve it. **amended** = the
reviewer's intent is accepted, but the wording or scope in this file is what ships. **declined** =
not applied, with the reason. Text in a "Text to place" line is literal copy, not a description of
copy. Where two blocks are alternatives, the row says so; otherwise apply every row.

**What does NOT change.** Primary keyword `glp-1 muscle loss` (Vadim, checkpoint 1, 19.09). Slug
`glp-1-muscle-loss-fitness-apps` (Vadim, 19.09; the page is not live, 404 on 2026-10-20). Author
Assel Sekerova. Hub 1 (AI in Fitness) with the bridge into Hub 3 (GLP-1 Market), action type
create-net-new, P1. One CTA to the fitness product page. The customer behind the 34,000 scans is
never named. The three external sources (Neeland 2024 PMID 38937282, the 2025 joint advisory on
obesity.org, the KFF poll) stay, with their verified wording. M1 on "GLP-1" in the H1 stays an
accepted known failure.

---

## 1. Headline — amended

**Reviewer:** the H1 "GLP-1 Muscle Loss and Fitness Apps" may suggest the article can identify
muscle loss; suggested H1 "GLP-1 and Fitness Apps: Tracking Body Change Beyond Scale Weight"; keep
"Can a body scan measure muscle loss?" as a prominent H2 or FAQ.

**Ruling.** The concern is accepted: the H1 must not read as if the app or the scan identifies,
tracks or measures muscle loss. The reviewer's exact H1 is not adopted by default, because it drops
the primary keyword that Vadim chose on 19.09, and `article_lint.py` gate 7 requires the primary
keyword in the H1 and in 1-2 H2s.

- **H1:** contains the exact string "GLP-1 muscle loss" (any case), framed as the question or
  concern the app team faces, not as something the app or scan measures. Keep "Tracking Body Change
  Beyond Scale Weight" (the reviewer's wording) or close to it as the second half. The planner
  proposes 2-3 candidates in `plan-audit.md`, picks one, and gives the reason.
- **H2:** the evidence section's H2 carries the keyword and the "what a scan cannot determine"
  boundary (see §6, Section 2).
- **FAQ:** keep the muscle-loss question as the first FAQ: "Can a mobile body scan measure muscle
  loss during GLP-1 treatment?" (current wording, keep).
- **Open item for Vadim (publish package + digest):** the reviewer's verbatim H1 "GLP-1 and Fitness
  Apps: Tracking Body Change Beyond Scale Weight" is a one-line swap if he prefers it. The price:
  the primary keyword leaves the H1 (gate 7 fails), so it means changing the primary keyword too.

## 2. What composition estimates depend on — accepted, amended wording

**Reviewer:** "split" sounds more definitive than the method warrants; outputs derive from
model-generated measurements and user inputs including optional weight; body-fat percentage uses an
anthropometric formula; state that the figures are model-derived estimates.

**Grounding:** `compliance.md` §3 ("body composition values are estimates derived from them plus
height and optional weight"), `terminology-guardrails.md` §2.13, `how-it-works.md` backend step 5,
context pack FX-005 (body fat % by the US Navy formula, which is a circumference-based
anthropometric formula).

- **Remove** every "split(s) that change into fat and lean components" and any wording that has the
  scan or the estimates determine which tissue changed.
- **Text to place (verbatim, all three, in this order, where the article first explains the
  estimates):**
  "Body composition estimates are derived from the body measurements along with height and optional weight."
  "Body fat percentage comes from an anthropometric formula applied to those measurements."
  "These are model-derived estimates to review alongside weight and measurements. They do not determine which tissue changed."
- Do not name the US Navy formula in the article.

## 3. The app-specific table — accepted, the article's centerpiece

**Reviewer:** add a compact table of what the app receives / can show or do / should avoid
concluding; add an illustrative progress view.

- **Place the reviewer's table verbatim** (three columns, three rows) in the progress-view section
  (§6, Section 3). Header row: `What the app receives | What it can show or do | What it should
  avoid concluding`. Rows exactly as in `review-1.md`. Only terminology fixes are allowed, and none
  are needed as written.
- One or two sentences before the table say why it matters to an app team (the app team's
  decisions are the thread of the article). No sentence after the table restates it.
- **Image 1** sits in this section. See §8.

## 4. Measurement evidence vs composition evidence — accepted, verbatim

**Reviewer:** repeatability and the 96-97% figures concern evaluated body measurements, not lean
mass, muscle-loss detection, or the smallest meaningful change during GLP-1 treatment; use the
approved repeatability sentence exactly; the accuracy claims are not externally validated.

**Grounding:** `accuracy-formulations.md` §1.2 (preferred repeatability sentence), §1.1 (96-97%,
1.5-2.0 cm, hyphens), §1.8 (methodology under NDA), §1.9 (what is not claimed).

- **Repeatability, text to place (verbatim):** "For most evaluated measurements, repeated scans
  showed typical scan-to-scan differences of less than 1 cm." It REPLACES the current "For most of
  the evaluated measurements, typical scan-to-scan differences remained below 1 cm."
- **Scope, text to place (verbatim, directly after the accuracy and repeatability sentences):**
  "These figures describe body measurements. They are not validated accuracy for lean mass, for detecting muscle loss, or for the smallest meaningful change during GLP-1 treatment."
- **Validation status, text to place (verbatim, same paragraph):** "3DLOOK's accuracy claims have
  not been peer-reviewed or externally validated through a third-party clinical study."
- The 96-97% / 1.5-2.0 cm sentence and the NDA sentence may stay (current wording is canon). Keep
  the link to the accuracy framework once in this paragraph.
- Never place 0.40 cm (ISO benchmark) in this article.

## 5. The 34,000-scan proof point — kept, with conditions

**Reviewer:** keep only with an approved internal source, a confirmed count and period, and
permission to describe the use case publicly; the linked fitness page does not substantiate it.

**Grounding:** `proof-points.md` "Customer outcomes" (2025 scans 34,000, Internal customer
breakdown), `case-studies/yazen.md` ("What they use": periodic check-in scans, 3D body
visualization, body composition), context pack FX-007 with Vadim's decision of 19.09: keep it
anonymized as "a weight-loss management platform", never name the customer.

- **Kept.** Source, count (34,000) and period (2025) are confirmed in `brand-assets/`.
- **Text to place (verbatim, current sentence unchanged):** "A weight-loss management platform ran
  34,000 FitXpress scans in 2025. It used them for periodic check-in progress tracking, 3D
  visualization, and body composition context."
- **Placement rule:** no link on this sentence, and not in the same paragraph as the product-page
  link, so no reader takes the linked page as its source. No geography, no customer name.
- **Open item for Vadim (publish package + digest):** the reviewer asks for explicit permission to
  describe the customer's use publicly. Vadim's 19.09 decision covers the anonymized mention; if he
  wants the customer's sign-off on the use description, the two sentences are cut cleanly.

## 6. Structure — accepted as the new section skeleton

The reviewer's "Suggested structure" replaces the 12-section outline. The app team's decisions are
the organizing thread throughout. Section headings below are working titles; the planner writes the
final H2s (in `### Section N.` form for the plan lint).

**Opening (no H2 of its own beyond the first section's).** Keep the current first two paragraphs'
job: the member on GLP-1 treatment, what the scale number does and does not show, and one hub link
to the AI in Fitness hub. Keep the scope note (current text, it already carries the clinical
boundary and "FitXpress is not a medical device."). The separate "Short answer" H2 is **dropped**:
its scale and circumference points move into the opening or into the table, and its "split" bullet
is replaced per §2.

**Section 1. Why this is a fitness app question.** Members may be using GLP-1 treatment while
following a strength program; a weight chart alone leaves the training record disconnected from
body-change data. **KFF: amended, one sentence**, and it must say the figure describes US adults
generally, not fitness app members (the reviewer allows "shortened to one sentence or omitted"; one
sentence keeps the only demand figure). Keep the market and adherence discussion brief: one link to
the GLP-1 market article and one to the visual-progress adherence article, which owns the retention
angle. No retention claims here.

**Section 2. What the evidence says, and what a scan cannot determine.** H2 carries "GLP-1 muscle
loss". Condense the research section. Keep: the Neeland range with its attribution, the
lean-mass-versus-muscle distinction ("lean mass includes more than muscle"), "appear to be
adaptive". Joint advisory, **amended**: say it supports resistance training as part of broader
nutritional and medical management, and that an app offering workouts does not, by itself, fulfil
all of that guidance. This REPLACES "Strength training is already part of the programs many fitness
apps offer." Add (from §G1 below) that a clinician's assessment of muscle function is a separate
question from a composition reading.

**Section 3. What to show in a GLP-1-aware fitness progress view.** The §3 table, Image 1, the §2
estimate sentences, and the weight-source sentence from §G2.

**Section 4. How to run comparable check-ins.** Baseline, cadence, capture conditions, review of
differences, and an alternative path when standard capture is unsuitable.
- **Baseline, text to place (verbatim):** "A later scan can establish a new baseline, but it cannot
  recreate the earlier measurement." Keep the current point that a member may already be partway
  through treatment when the app's record begins.
- **Review of differences:** the current "Change thresholds" point moves here (smallest difference
  worth showing depends on observed scan-to-scan variation and the interval), with its link to the
  online coaching article.
- **Alternative path:** the approved limitation sentence stays verbatim ("FitXpress was not
  specifically trained on data representing people with physical disabilities, and its measurement
  performance has not been established for this population."), and one sentence says the app can
  offer manual measurements or a weight-only progress view for members who cannot use standard
  capture.
- The current FAQ "How often should a fitness app scan members" answer belongs here as cadence
  content, not as a FAQ.

**Section 5. Where FitXpress fits and what to test in a pilot.** Concise outputs (FX-005, FX-006),
Body Progress per §G3, integration responsibilities per §G4 and §G5 (this REPLACES the 4-row roles
table section), measurement limits per §4, the 34,000-scan point per §5, and pilot metrics (current
pilot paragraph). **Add one contextual product link** to the fitness product page where the
integration workflow is discussed (assessment table, row 4); keep the final CTA too. The "not
equivalent to DXA, BIA, or a calibrated scale" guardrail sentence stays verbatim, once.

**FAQ, short.** Keep the muscle-loss question first. Keep a question only if its answer is not
already in the body. "How often" moves into Section 4. "Does a fitness app need to know whether a
member takes a GLP-1 medication?" may stay (the body does not answer it), its last sentence aligned
with §G4.

**Next steps / CTA.** Keep.

**Condensed or removed sections:**
- "What the app, the prescribing program, and FitXpress each handle" → condensed into Section 5
  (integration responsibilities). The 4-row table goes.
- "Scale weight, body composition estimates, and DXA or professional BIA: which fits when" →
  **removed**. One sentence with a link sends method comparison to the online coaching article,
  which already covers scales, tape, BIA, DXA and scans.
- "Fitness apps and GLP-1 programs this workflow fits" → cut. The point about a second record made
  by a different method may survive as one sentence in Section 4 or 5. The link to the GLP-1 tools
  article may survive once if it fits Section 1 or 5.
- "Implementation and evaluation considerations" → privacy into Section 5, change thresholds and the
  alternative path into Section 4, pilot measures into Section 5.

**Length.** Condensing is the point. Target 1,400-1,800 words of article prose; under 1,400 is fine
if nothing required is missing.

## G. Precise copy and product checks

**G1. "Reference methods include DXA and professional BIA" — accepted (already half-fixed).**
The current text no longer calls them "reference methods". Keep it that way everywhere, including
headings. Where a protocol is mentioned, say the protocol names its own method; do not present DXA
and BIA as equivalent references (`accuracy-formulations.md` treats bioimpedance as an estimation
method). Text to place (verbatim, Section 2 or 5): "A clinician's assessment of muscle function is
a separate question from a composition reading."

**G2. Weight in the progress view — amended.** Grounding: `how-it-works.md` (Smart Scales is a beta
output that cross-validates self-reported weight). Text to place (verbatim, Section 3): "Weight in
the progress view is the value the member enters or the app syncs from a connected scale." Do not
imply that FitXpress capture supplies a measured scale weight. **Do not introduce Smart Scales or
predicted weight** in this article: it is a beta feature and outside the article's scope, and the
one sentence above answers the reviewer's concern.

**G3. Body Progress — accepted, verbatim.** Grounding: `compliance.md` §4 and CLAUDE.md §12. Text to
place (verbatim, Section 5): "The app company links each scan ID to its own member record and
chooses which two scans to compare. 3DLOOK does not track individuals or determine whether two
scans belong to the same person." Never write that FitXpress tracks a member over time.

**G4. Privacy paragraph — accepted, amended wording.** Grounding: `compliance.md` §6 (the customer
provides privacy notices, establishes the lawful basis, obtains consent where needed). REPLACES
"record sharing depends on the member's consent and on agreements between the two". Text to place
(verbatim): "Sharing records between the fitness app company and the prescribing provider depends on
the applicable lawful basis, privacy notices, member permissions, and the agreements between them.
Consent is required in some workflows." Keep the link to the privacy FAQ, once, mid-paragraph. The
FAQ answer on asking about medication keeps "purpose, notice" and replaces a bare "consent" with
"lawful basis, notice, and consent where required".

**G5. Terminology — accepted, verbatim.** Grounding: `terminology-guardrails.md` §2.14
("organization" only as an umbrella; "company" for a FitXpress buyer). REPLACES "two organizations
hold parts of the progress record". Text to place (verbatim): "the fitness app company and the
prescribing provider may each hold different records." Apply the same rule across the article:
no "organization(s)" where the actor is known.

**G6. Image placeholders — accepted.** Image 1: an annotated, explicitly illustrative app progress
view (label it "Illustrative example" in the concept; dated weight, circumference and composition
trends, method labels, training blocks). Image 2: a capture-to-results visual (two photos, guided
capture, results). Neither may show a scan measuring muscle tissue: no muscle overlays, no
anatomical muscle imagery, no "muscle" labels on the body. The cover concept follows the same rule.

## A. Coordinator amendments after the re-plan (2026-10-20)

The planner flagged three conflicts between this file and the canon. Resolved here; these rows win.

**A1. "Let" in the reviewer's table.** `let` is a hard ban (CLAUDE.md §6, `let` -> `allow`). §3
originally said no fix was needed; that was wrong. Row 2, column 2, text to place (verbatim):
"Allow a member or coach to review both at a scheduled check-in".

**A2. Down-link depth.** `landing-map.md` rule 1 puts the down link within the first 30% of the body
(Clarity: health articles are read to 5-35% depth). Section 5 starts at about 62%. So the fitness
landing is linked three times: Section 1 (plain contextual link, anchor "body composition tracking
for fitness apps"), Section 5 (the reviewer's contextual link, anchor "body scanning for fitness
apps"), and the Next steps CTA. Neither anchor is used in the H1 or meta title (rule 3).

**A3. Accuracy paragraphs.** `accuracy-formulations.md` §5: "Either §1 or §5 is fine; do not mix the
two inside one paragraph." §4 above puts the §1.2 repeatability sentence next to the §5 short-form
accuracy sentences. Split into three paragraphs: (a) repeatability: "Internal repeatability testing
used a real-world customer dataset with five repeated scans per participant." + the §1.2 sentence +
framework link; (b) accuracy, own paragraph: the §5 short form verbatim incl. the NDA sentence +
framework link; (c) the scope sentences and the validation sentence from §4. The "same paragraph"
rule in §4 now means: the scope and validation sentences share paragraph (c).

## H. Not article copy — open items for the publish package

- **Incoming links.** After publication, add contextual links INTO this article from the AI in
  Fitness hub and the GLP-1 market article. That is CMS work on two other live pages (Assel / the
  site editors), recorded as an open item, not done by this pipeline.
- **The reviewer's suggested H1** (§1) and **the customer-permission question** (§5): both for
  Vadim, in the digest.
