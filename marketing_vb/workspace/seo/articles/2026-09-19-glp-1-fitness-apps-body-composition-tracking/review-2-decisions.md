---
article: 2026-09-19-glp-1-fitness-apps-body-composition-tracking
published_slug: glp-1-muscle-loss-fitness-apps
review: 2
review_source: review-2.md (verbatim extract of the Google Doc tab "Review 2", 2026-10-20)
written: 2026-10-21
written_by: coordinator
reviewed_text: "v2/final.md (the Doc tab «Version 2», the 19.09 text), NOT the current text. The Review 1 rewrite (commit 93c4d79, snapshotted in v3/) already fixed about half of the items. The input for this round is the current final.md (= v3/final.md)."
round_type: "EDIT round, not structural. The Review 1 section skeleton stays. Changes are applied to final.md by seo-editor, then seo-publisher -> article_package.py assemble -> seo-qc -> git. No re-plan."
vadim_decisions: "2026-10-21: (1) keep the 34,000-scan point; (2) remove the KFF poll paragraph."
authority: "THIS FILE WINS over review-2.md wherever the two differ. Agents read both. review-1-decisions.md still holds, except where a row below says it is replaced."
next_stages: edit (seo-editor, input final.md) -> publish (seo-publisher) -> assemble -> qc (seo-qc) -> git
---

# Review 2 — decisions

**How to read this file.** Same conventions as `review-1-decisions.md`. **verbatim** = place the
quoted sentence exactly. **amended** = the reviewer's intent is accepted, but the wording in this
file is what ships. **already done** = the current final.md already does this; change nothing.
**declined** = not applied, with the reason. Text in a "Text to place" line is literal copy. Apply
every row unless a row says it is an alternative.

**What does NOT change.** Primary keyword `glp-1 muscle loss`. Slug `glp-1-muscle-loss-fitness-apps`.
Author Assel Sekerova. The Review 1 section skeleton (Sections 1-5, FAQ, Next steps) and every
locked string from the Review 1 round, EXCEPT the three listed under "Locks lifted" below. The
customer behind the 34,000 scans is never named. M1 on "GLP-1" in the H1 stays an accepted known
failure (`gate_m1_note` stays in the frontmatter). The FAQ H2 stays literally `## FAQ`.

**Locks lifted in this round (only these):**
1. The Review 1 table (three columns "What the app receives / What it can show or do / What it
   should avoid concluding", including the A1 row) is replaced by the §4 table below.
2. The KFF sentence and its claim marker are removed (§8).
3. The two "second record made by a different method" sentences move from Section 5 to Section 3,
   wording unchanged (§5).

---

## 0. Items the current text already resolves (already done, change nothing)

The reviewer quotes the 19.09 text. These lines are already fixed in final.md:

- "split that change into fat and lean components": gone since Review 1 §2. The three estimate
  sentences stay as they are.
- Body-measurement vs composition validation: the T-REPEAT-SCOPE and T-VALIDATION sentences stay.
- Approved repeatability sentence: already verbatim ("For most evaluated measurements, repeated
  scans showed typical scan-to-scan differences of less than 1 cm.").
- Scan IDs: already "The app company links each scan ID to its own member record and chooses which
  two scans to compare. 3DLOOK does not track individuals or determine whether two scans belong to
  the same person."
- Records: already the reviewer's words "the fitness app company and the prescribing provider may
  each hold different records."
- Sharing: the current G4 sentences ("Sharing records ... depends on the applicable lawful basis,
  privacy notices, member permissions, and the agreements between them. Consent is required in some
  workflows.") carry the same content as the reviewer's suggestion and match `compliance.md` §6.
  Keep them.
- Repeated middle sections (roles table, method selection, best fit): already cut in Review 1.

## 1. Headline — accepted, verbatim

**Reviewer:** keep the search topic, make the promise exact: "GLP-1 Muscle Loss: What Fitness Apps
Can Track Beyond Scale Weight".

**Grounding:** it contains the primary keyword, which settles the Review 1 open item (the
Review 1 H1 swap would have dropped the keyword and failed gate 7).

- **H1, text to place (verbatim):** "GLP-1 Muscle Loss: What Fitness Apps Can Track Beyond Scale Weight"
- Update the frontmatter `title` to the same string. The evidence H2 keeps "GLP-1 muscle loss".
- The publisher re-checks the meta title against the new H1 (no landing-page anchor in either).

## 2. Short answer at the top — accepted, verbatim

**Reviewer:** readers arriving for "GLP-1 muscle loss" should see the direct answer before the
workflow and product sections.

- **Text to place (verbatim, both sentences, as its own paragraph directly after the first
  paragraph of Section 1, the one ending "...whether fat mass, lean mass, or fluid made up the
  change."):**
  "A fitness app can show weight, body measurements, body composition estimates, and strength-training history together. A mobile body scan cannot determine whether a member has lost muscle or establish the cause of a change in lean mass."
- No H2 for it (Review 1 dropped the separate "Short answer" H2).
- Once this paragraph exists, the Section 2 sentence "A body scan cannot settle what this research
  leaves open about muscle." repeats it. The editor may cut that one sentence. The T-MUSCLE-FUNCTION
  sentence after it stays verbatim. The scope note stays verbatim.

## 3. Which weight the workflow uses — accepted, amended wording

**Reviewer:** specify which weight input the proposed app workflow uses, rather than leaving
"optional weight" unexplained.

**Grounding:** `compliance.md` §3 (estimates derived from measurements plus height and optional
weight), `tech-spec.md` (weight input is self-reported when provided), Review 1 G2 (no Smart Scales,
no predicted weight in this article).

- **Text to place (verbatim, directly after "Body composition estimates are derived from the body
  measurements along with height and optional weight."):**
  "In this workflow, the app sends the same weight value with each scan as that optional input."
- Do not mention Smart Scales, weight estimation or predicted weight.

## 4. A concrete progress view — accepted, the reviewer's new table replaces the Review 1 table

**Reviewer:** build the article around a concrete progress view: a labeled table (App displays /
Source / Interpretation shown to the member), then one paragraph on what happens when signals
disagree; Image 1 becomes an annotated mockup of this exact view.

**Ruling.** The same reviewer asked for both tables; Review 2 is her later and more concrete ask.
One table only, to avoid two tables back to back. The Review 1 table goes; its unique points move
into the disagreement paragraph below.

- **Table, text to place (verbatim except one amended cell):**

| **App displays** | **Source** | **Interpretation shown to the member** |
|---|---|---|
| Weight trend | Member-entered or synced scale reading | Total weight change |
| Waist and other circumferences | Guided scans | Measurement changes, subject to capture variation |
| Fat and lean mass estimates | FitXpress estimate from scan measurements | Estimated trends; lean mass is not muscle mass |
| Completed strength sessions and performance | Fitness app | Training context alongside the body-data trends |

  Amended cell: the reviewer's "FitXpress calculation" became "FitXpress estimate from scan
  measurements" (`terminology-guardrails.md` §2.13: body composition = estimates; "calculated" is
  reserved for BMI and BMR).
- Keep the `<!-- claim: T-TABLE -->` marker above the table.
- The two lead-in sentences before the table stay ("The app team decides what its progress view
  displays..." and "Those choices matter more...").
- **Disagreement paragraph (amended, editor writes the prose, 3-4 sentences), placed after the
  weight/estimates paragraph and before Image 1.** It must say, in this order: when the signals
  disagree, the app or coach reviews capture conditions and earlier readings first; the app avoids
  assigning a cause from one scan, including a claim that the training program caused a measured
  change; clinical concerns go to the prescribing provider, and the app generates no medication or
  clinical advice. Use "prescribing provider" (the article's term), not "prescribing team". No new
  numbers, no new claims.
- **Image 1 concept (amended).** An annotated mockup of exactly this view, labeled "Illustrative
  example" on the image, any numbers labeled illustrative. Four dated rows on one time axis: weight
  (label "entered by member" or "synced from scale"), waist and hip circumferences ("body scan"),
  fat and lean mass ("estimate"), completed strength sessions (training markers). One callout points
  at the source labels. No attribution of change to fat or muscle, no "muscle" label anywhere, no
  medication fields.

## 5. Condense the middle — already done, one move

**Reviewer:** keep the point that scans and DXA/BIA records are each compared with earlier results
from the same method; move it into the progress-view section; link to the existing method
comparison.

- The repeated sections were cut in Review 1 (§0).
- **Move (wording unchanged)** from Section 5 to Section 3, after the disagreement paragraph:
  "Where the prescribing provider already records body composition with DXA or BIA, the app's scans
  form a second record made by a different method. Each record is best read against its own earlier
  values." The method-comparison link sentence ("Remote body measurement for online fitness coaching
  programs compares scales, tape measurements, photos, BIA, DXA, and mobile scans method by method.")
  moves with them. DXA and BIA must be expanded at their first body use, wherever that now falls.
- The T-GUARDRAIL-DXA sentences stay in Section 5, verbatim.

## 6. Cadence and the pilot interval — accepted, verbatim

**Reviewer:** "Scans spaced closer than the change they are meant to show add records without adding
information" is too absolute; the published repeatability figure is for evaluated body measurements
and is not a universal change threshold for composition estimates.

- **Delete** "Scans spaced closer than the change they are meant to show add records without adding
  information." and "The interval depends on the expected change compared with typical scan-to-scan
  differences, and on the length of the block."
- **Text to place (verbatim, Cadence block, after "Check-ins sit at defined points, such as the end
  of a training block."):**
  "Set the check-in interval according to the program schedule, expected changes, member burden, and variation in the specific measurements being compared."
- **Pilot paragraph, replace** "That interval is set before launch, long enough for the expected
  change to exceed observed scan-to-scan variation." **with (verbatim):**
  "That interval is set before launch, on the same factors as the check-in cadence."
- The "Review of differences" block stays as is (it refers to the app's own observed variation).

## 7. Alternative path — accepted, amended wording

**Reviewer:** complete the thought: offer an appropriate alternative, identify the method used, and
avoid treating results from different methods as one continuous trend.

- Keep the FXS-POPULATION sentences and "The app can offer manual measurements or a weight-only
  progress view to members who cannot use standard capture." verbatim.
- **Text to place (verbatim, directly after it):**
  "The progress view labels the method behind each value and keeps results from different methods as separate trends."

## 8. KFF poll — removed (Vadim, 2026-10-21)

**Reviewer:** the poll does not establish the share of fitness app members on GLP-1 medication;
consider removing it, since the opening member scenario establishes relevance.

- **Delete** the KFF paragraph and its claim marker. This replaces Review 1 decisions §6 (KFF in one
  sentence). Remove the KFF entry from `claims_external` in the frontmatter.
- No replacement demand figure. Do not bring in another statistic.

## 9. The 34,000-scan point — kept (Vadim, 2026-10-21)

**Grounding:** `proof-points.md` line "Yazen | 2025 scans | 34,000 | Internal customer breakdown",
`case-studies/yazen.md`, context pack FX-007, Vadim's 19.09 decision (anonymized) and his
2026-10-21 decision (keep).

- No text change. The T-34K sentences, the bridge sentence after them and the placement rule from
  Review 1 §5 (no link, no customer name, no geography) stay.
- The publish package closes the Review 1 open item "34,000 scans (decisions 5, for Vadim)" as
  "kept, Vadim 2026-10-21".

## 10. Image 2 — accepted, amended concept

**Reviewer:** guided two-photo capture, then scan-derived outputs, then the app-controlled progress
view; no visual that labels lean mass as muscle.

- **Image 2 concept (amended), three panels left to right:** guided front and side capture (pose
  outline, framing guide); scan-derived outputs (a short list of circumferences, a smooth neutral 3D
  model with no muscle definition, composition values tagged "estimate"); the app's own progress
  view inside the app's interface, showing the same dated trends as Image 1. No "muscle" label
  anywhere, no muscle overlays.

## 11. Incoming links — open item, unchanged

After publication, contextual links INTO this article from `ai-in-fitness-industry` and
`glp-1-market` (CMS work for Assel). Stays in the publish package open items.

## 12. Length and gates

- Expected net change: about +60 to +110 words (short answer, table, disagreement paragraph,
  method sentence) and about -60 words (KFF, two cadence sentences, the Section 2 repeat). Target
  stays 1,400-1,800 words.
- `article_lint.py` gates as in Review 1: all PASS except the accepted M1 on "GLP-1" in the H1.
  Detector CLEAN. Mean sentence length ≤ 16 words; the new verbatim cadence sentence is 21 words.

## A. Coordinator amendments after the edit pass (2026-10-21)

The editor flagged two points. Resolved here; these rows win over §3 and §5.

**A1. Weight-input sentence (replaces the §3 text).** The §3 wording can be read as "a constant
weight on every scan". Text to place (verbatim, same position, replacing the §3 sentence):
"In this workflow, the app sends the member's current progress-view weight as that optional input with each scan."

**A2. DXA and BIA expanded twice (lifts part of the T-GUARDRAIL-DXA lock).** After the §5 move, the
first body use of DXA and BIA is in Section 3, where they are expanded. In Section 5, the first
T-GUARDRAIL-DXA sentence becomes (verbatim): "Some clinical protocols and research studies require DXA or professional BIA."
The second T-GUARDRAIL-DXA sentence ("FitXpress is not equivalent to DXA, BIA, or a calibrated scale
when the workflow, protocol, or regulatory standard requires those methods.") stays verbatim.
