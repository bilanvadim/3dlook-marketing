---
slug: 2026-08-31-ai-body-data-wellness-platforms-hub
review: 2
decided: 2026-09-02
purpose: >
  How each Review 2 item is applied. Read alongside review-2.md. Where this file and
  review-2.md disagree, THIS FILE WINS. Revision 3 is a wording pass: no restructure, no
  re-plan, no keyword change. plan.md revision 2 stands.
supersedes_partially: review-1-decisions.md §A1 (the meta description's keyword home)
---

# Review 2 — application decisions

## A. What kind of revision this is

Review 2 is **sentence-level**. It changes no section, no heading, no word target and no
keyword decision. So revision 3 runs `edit` and `publish` only: `plan.md` revision 2 stands
untouched, and there is no reason to re-run the planner or the writer.

That is worth stating because Review 1 was the opposite, and treating this like Review 1 would
cost another $53 for nothing. The reviewer's own summary is that the article is "substantially
stronger and close to publishable" and that after these corrections it is ready for
proofreading and illustration planning.

## B. The reviewer accepted both of our deviations

Recorded because closing them changes our open-items list, not the text:

| Review 1 item | What we did | Reviewer's response |
|---|---|---|
| 13, `predicted weight` | Omitted. FX-009 does not contain it and it is absent from `product-info/` | "correct if it is absent from the approved product sources. **The approved repository should take precedence over my earlier recommendation.**" |
| 9, third-party engagement source | None added, none invented, left as an open item | "does not need to remain a publication blocker... can be closed through slightly narrower wording instead of introducing an unapproved source" |

**Open item 1 from revision 2 is therefore CLOSED**, not by finding a source but by removing
the outcome claim that needed one. See item 2 below. Nothing is left on Vadim for this.

## C. The two facts the reviewer asked us to verify. Both check out in his favour.

### C1. Item 9, "similar time of day". **Not in approved product guidance. Remove it.**

The reviewer suspected this was general measurement advice rather than a FitXpress condition.
Checked on 2026-09-02: `time of day` returns **zero hits** across
`brand-assets/product-info/`, `about-me.md` and the article's context pack. The documented
capture conditions are the pose-validation engine and the real-time clothing detector
(`how-it-works.md` lines 7-8).

So the writer generalised. Applied: "same guided pose and similar capture conditions"
everywhere the phrase appears.

### C2. Item 11, "No personal identifiers are processed". **Approved, but not as article prose. Use the reviewer's wording.**

The phrase is approved, and that is why it survived: `compliance.md` carries
"process zero personal identifiers" as an **outbound sequence line** and
"no personal identifiers stored" as a **one-line social reassurance**. Neither is an
article-grade privacy statement, and the reviewer's objection is correct: body photos and
derived measurements can be personal data even with no direct identifier attached.

The reviewer's replacement is *supported by the same source*, which records
"Personal identifier processing | None, photos cannot be linked to individuals via 3DLOOK".
So this is a precision gain, not a new claim. Applied:

> FitXpress does not receive names, contact details, or other direct identifiers that connect
> the scan with a specific individual.

**Flag for `compliance.md`:** the short forms stay fine for outbound and social, where they
are labelled as such. Worth adding the long form there as the article/page variant, so the
next writer does not reach for the DM line again. Owner: Vadim. Not done in this revision.

## D. Every item, and how it lands

| # | Item | Disposition |
|---|---|---|
| 1 | Opening logic: scale weight IS comparable over time | **Apply. This is a factual correction and the most important one.** The current sentence treats self-reported entries and scale weight as having the same limitation. They do not: a scale reading compares fine, it just compresses different kinds of change into one number. Rebuild as three beats: self-reported entries may be estimated, rounded or inconsistently collected; scale weight compares but compresses; repeatable body data adds measurements and visual context. |
| 2 | Engagement outcome claim | **Apply, remove the sentence.** "Across a program cycle, that can contribute to continued engagement" is an outcome claim, and it is the one sentence in the article that would need the source we do not have. Replace with mechanism only: another structured check-in, specific progress information to present, context for coaching or content selection. **This is what closes open item 1.** |
| 3 | Unsupported comparative in personalization | **Apply.** "each of those influences outcomes more than a waist measurement" asserts a ranking nobody established. Reviewer's wording: "A scan carries no information about motivation, food environment, or the time a member can commit, and each of those also influences outcomes." The limitation survives, the ranking goes. |
| 4 | Grouping members by measured starting point | **Apply, and go further than revision 2 did.** Review 1 item 8 said reconsider it and add safeguards if retained; we retained it with safeguards. Review 2 says the article still *actively recommends* it. Turn it into: aggregated body-data trends for program reporting, participation and change across appropriately defined cohorts, and do not make measured body characteristics the default basis for segmentation. The reviewer's reason is the right one: this hub covers employee wellness. |
| 5 | Repeated program-access boundary | **Apply.** The boundary appears three times: "Where FitXpress fits", the last sentence of "Boundaries and related hubs", and FAQ Q4. Keep the full statement in the FitXpress section and the short FAQ answer for search intent. Delete it from "Boundaries and related hubs", where it also makes the section end on decisioning rather than routing. |
| 6 | Compliance formulation | **Apply.** "Adding capture to a program leaves compliance where it was" is too broad: image capture and body-data processing can add consent, retention and governance requirements. Replace with "The platform remains responsible for its program rules and applicable compliance requirements." Keeps the division of responsibility, drops the claim that nothing changes. |
| 7 | Automated-program contradiction | **Apply.** Saying judgement "stays with a person" in a *fully automated* program contradicts itself. Reviewer's boundary: the record can support content selection and progress display, while the platform stays responsible for the rules and recommendations applied, and human review can be specified for consequential decisions. |
| 8 | Cadence guidance | **Apply, soften.** Four to twelve weeks becomes a practical starting point that depends on program goal, expected magnitude of change and capture conditions. Drop the FAQ's assertion that longer intervals stop members "feeling progress". We have no source for any of the three current conclusions. |
| 9 | "similar time of day" | **Apply, remove.** See C1. Verified absent from every approved source. |
| 10 | Server-side retention | **Apply.** "which stay server-side for reporting" implies the full output set should be kept. Reviewer's version is conditional and matches data minimisation: "which outputs are retained or made available to authorized program teams." |
| 11 | Privacy wording | **Apply the reviewer's precise version.** See C2. |
| 12 | Meta description | **Apply. This narrows `review-1-decisions.md` §A1.** §A1 recorded the meta description as the second and last home of `corporate wellness platform`. The reviewer is right that this contradicts the broadening: metadata frames the whole hub. So the phrase now has **one** home, the dedicated subsection, and the description uses "wellness platform". **This follows the direction Vadim chose at §A1 rather than reversing it**, so it is applied without escalating. Flagged because it changes a recorded decision detail. |
| 13 | Keyword stacking in the corporate subsection | **Apply.** "A corporate wellness platform working on that specific problem, including an employee wellness app tied to an employee wellness program" stacks three near-identical phrases and reads as insertion. Keep `corporate wellness platform`, cut the other two. |
| — | Six smaller softenings | **Apply all six.** "the comparison invents movement" → "may show apparent change"; "a chart that moves for reasons the member did not cause" → "a chart with reduced comparability"; "on its own it has no answer" → "a headline accuracy figure is incomplete on its own"; "onsite-only programs never will" → "without requiring participants to attend an onsite assessment"; "a better basis than asking a member" → "additional context alongside the member's own account"; body fat percentage "works well as a trend line and poorly as a headline number" → "can be more useful as a trend than as an isolated headline number". |

## E. What must NOT change in revision 3

- **Structure.** Eleven H2s, the same order. `plan.md` revision 2 stands.
- **Keyword decision.** Primary stays `wellness platform`. Only the meta description changes,
  per item 12.
- **Word target.** 2,650 +/-150. These edits are roughly length-neutral: item 2 and item 5
  remove sentences, item 1 adds a beat.
- **The medical-device wording.** "It is not positioned as a medical device." The reviewer
  lists it under what is now working well.
- **DXA, 150 to 220 cm, `96-97%`, `1.5-2.0 cm`, body composition estimates.** All confirmed
  correct by the reviewer.
- **All four internal-link directions**, 14 links across 8 targets.
- **The two `<!-- TODO(publish) -->` markers** for the unpublished privacy FAQ. Item 11's
  fallback ("ensure the privacy FAQ explains the distinction between direct identifiers and
  personal data") is a note for that FAQ when it ships, not a change here. Added to the
  publish tasks.

## F. Open items after revision 3

Revision 2 carried five. Three survive, one closes, and one gains a note.

1. ~~No third-party source on self-monitoring~~ **CLOSED by Review 2 item 2.** The outcome
   claim that needed a source is gone. No source required.
2. **DEXA/DXA divergence in brand-assets.** Still open. `DEXA` remains the house spelling in
   `terminology-guardrails.md` §1, `editorial-guardrails.md` #7 and the Part 3 grep row, so
   the next article regenerates it. `scripts/article_lint.py` now catches it in the article,
   which contains the damage but does not fix the source. Owner: Vadim.
3. **essential/beneficial fat vs `predicted weight` in `proof-points.md` and FX-009.** Still
   open, and Review 2 sharpened it: the reviewer now defers to the repository, which means
   the repository has to be right. Owner: Vadim.
4. **"positioned as" is in its third policy state.** Still worth settling in the source Doc.
   Owner: editorial owner + Vadim.
5. **Images still not produced.** The reviewer explicitly names illustration planning as the
   next step after this pass. Owner: design.
6. **New, small: `compliance.md` has no article-grade privacy line.** See C2. Owner: Vadim.

## G. Applied. What the editor actually changed, in its own words

Moved here out of `final.md`'s frontmatter on 2026-09-02. It had grown to 72 lines, and
audit content does not belong in the artifact the CMS reads: the pipeline audit's own
finding F2 is that a file serving three audiences gets read by everyone who needs one of
them. It also created a live grep trap. Checking whether item 9 had been applied,
`grep -c "time of day" final.md` returned 1, and the hit was the frontmatter line saying
the phrase had been removed. Body-only measurement is the correct measurement, which is
why `article_lint.py` strips frontmatter before every gate.

### `open_items_closed`

engagement_source: >
Open item 1 (no approved third-party source for self-monitoring and engagement) is CLOSED by
Review 2 item 2. The one sentence that needed that source, "Across a program cycle, that can
contribute to continued engagement", is gone and its slot carries mechanism only. Nothing is
left on Vadim for this.

### `conflicts_resolved`

corporate_wellness_platform_home: >
Narrowed by Review 2 item 12, which supersedes review-1-decisions.md §A1 on this detail.
`corporate wellness platform` now has exactly ONE home, the corporate subsection in section 10.
The meta description (owned by the publisher) uses "wellness platform".
privacy_wording: >
"No personal identifiers are processed" replaced by the longer approved meaning from
compliance.md ("photos cannot be linked to individuals via 3DLOOK"), in both section 8 and
FAQ Q5. The short forms stay valid for outbound and social, where they are labelled as such.

### `changes_summary`

Revision 3 is a wording pass on revision 2: no section moved, no heading changed, no keyword
re-decided. 11 H2s and all 14 links in 4 directions intact. 13 numbered Review 2 corrections plus
6 softenings, and 5 editor fixes that fell out of them.
- 1 Opening logic corrected (the factual one): self-reported entries, scale weight and repeatable
body data now carry three different limitations instead of one shared one
- 2 Engagement outcome claim removed, replaced with mechanism only; closes open item 1
- 3 Unsupported comparative in personalization dropped ("more than a waist measurement")
- 4 Grouping by measured starting point turned into aggregated reporting plus a segmentation caveat
- 5 Third statement of the program-access boundary deleted from "Boundaries and related hubs"
- 6 "Leaves compliance where it was" replaced with the platform's continuing responsibility
- 7 Automated-program contradiction resolved (rules and recommendations, plus specified review)
- 8 Cadence softened to a starting point that depends on goal, magnitude and capture conditions,
in both the body and the FAQ; the FAQ's "feel progress" assertion dropped
- 9 "Similar time of day" removed in both places; verified absent from every approved source
- 10 Server-side retention made conditional, in the workflow step and in section 4
- 11 Privacy wording replaced with the reviewer's precise version, both instances
- 12/13 Keyword stacking cut in the corporate subsection; `corporate wellness platform` down to
one home in the body
- 6 softenings applied verbatim in intent (apparent change, reduced comparability, incomplete
headline figure, onsite assessment, member's own account, trend over headline number)
- Editor's own: split two stacked negations (M2) into single-boundary sentences, de-duplicated the
onboarding-to-result-display list that ran twice, merged two same-length sentences in the
engagement opener, and trimmed to land inside 2,650 +/-150

### `self_check`

- The engagement opener was the worst rhythm in the file after the outcome claim came out: four
consecutive sentences of near-identical length all doing the same job. Merged two of them, so
the paragraph now runs long, medium, medium, short. That is the paragraph a reader will decide
the section on.
- My own item 11 fix created a stacked negation ("does not receive... and photos are not used"),
which is the shape M2 exists to catch. Split into one boundary per sentence, in both places.
- "Onboarding, consent wording, the scan entry point, result display" ran verbatim in section 7
and again in section 9. Two identical lists fifteen lines apart is the signature of a text
assembled section by section. Section 7 now compresses it.
- Still reads machine-shaped, and left deliberately: "Boundaries and related hubs" now ends on
four consecutive topic-to-link sentences, because item 5 removed the line that used to break
them. The reviewer wants that section to end on routing, and inventing a closing beat there
would mean inventing a claim, so a routing block is allowed to read like a routing block.
- Still true from revision 2: no first person, no proof point, no named customer, because none
exists for a wellness deployment (context pack claim_gaps). The article argues from mechanism
end to end. Honest, and it costs the text the specificity a named deployment would give.

