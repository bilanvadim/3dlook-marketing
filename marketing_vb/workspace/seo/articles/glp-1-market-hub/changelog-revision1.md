# Changelog — GLP-1 Market Hub, Revision 1

**Source:** `draft-v4-publisher-final.md` (approved final, 2026-08-01)
**Review input:** `review1-comments.md` (Review 1 tab, 12 numbered priority revisions, overall assessment 6.5/10)
**Output:** `draft-v5-revision1.md`
**Date:** 2026-08-05

This is a revision on top of the approved final draft, not a rewrite from scratch. Structure, phrasing, and section boundaries changed; the underlying approved claims (FX-001, FX-003 through FX-007, FX-009, FX-010, FX-012) are unchanged in substance — only their wording and placement changed per the review.

## Center of gravity (overarching requirement)

Moved from "why FitXpress is useful" to "how GLP-1 market growth is changing program infrastructure." FitXpress now appears by name only in three places: a one-line bridge at the end of "What Better GLP-1 Progress Tracking Looks Like," the dedicated "Where FitXpress Fits" section, and the closing CTA/disclaimer. All earlier educational sections (market size, market drivers, ecosystem/delivery models, infrastructure challenge, scale-weight-alone) describe the problem and requirements generically, with no product name.

## Item-by-item

**1. Strengthen the actual market analysis** — Added a new section, "What Is Driving Market Expansion," covering all seven required points: diabetes-to-obesity expansion, employer/payer participation, virtual/hybrid care growth, demand exceeding utilization expectations, cost/coverage pressure, the shift from medication access to ongoing program support, and why infrastructure matters more as volume grows. It sits between the market-size section and the ecosystem section, so the move into progress tracking is now evidence-led. No new statistics were invented; the section synthesizes the already-approved KFF and J.P. Morgan figures into a drivers narrative.

**2. Reduce the product-page weighting** — Removed the FitXpress compliance paragraph from the opening scope section. Removed all FitXpress mentions from the market-size, market-drivers, ecosystem/delivery-models, infrastructure-challenge, and scale-weight sections. FitXpress by name is now confined to: (a) one bridging sentence in "What Better GLP-1 Progress Tracking Looks Like," (b) the full "Where FitXpress Fits" section, and (c) the CTA/disclaimer, matching the reviewer's three-place allowance exactly.

**3. Consolidate repetitive sections** — Merged "The Progress-Tracking Gap" and "Why Progress Tracking Is Becoming Table Stakes" into one section, "The Infrastructure Challenge Created by Market Growth" (three limitations: consistency, clinical review, program economics/engagement — down from six overlapping arguments across two sections). Merged "Body Composition Beyond the Scale" into "Why Scale Weight Alone Provides an Incomplete Progress Record" (shortened to two paragraphs). Folded "Telehealth and Remote Check-ins" into the generic ecosystem description (no separate section) and folded "Clinic Workflow at Scale" into "How Progress Tracking Fits Into Program Workflows." Net effect: 5 overlapping sections became 4 non-overlapping ones, and the article is shorter overall (previous draft ~3,650 body words; this revision ~2,850 body words, excluding frontmatter).

**4. Correct the repeatability claim** — Every instance of "FitXpress reports scan-to-scan repeatability of < 1 cm" (there were two, in "Clinic Workflow at Scale" and "Where FitXpress Fits") is now a single instance of the approved wording: "For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm," located once in "Where FitXpress Fits." Consolidating the two mentions into one also serves item 3.

**5. Distinguish estimates from direct measurements** — "A program that can see composition can tell a healthy trajectory from a concerning one" is replaced with the specified sentence, "Longitudinal body-composition estimates can give care teams additional context alongside weight, patient history, and other information used in the program," placed once in "Why Scale Weight Alone Provides an Incomplete Progress Record." "FitXpress produces body-composition outputs" is now "FitXpress provides software-derived body-composition estimates" in "Where FitXpress Fits." The distinction appears once and is not restated elsewhere.

**6. Remove unsupported causal retention claims** — All five flagged absolute statements are removed: "Programs that cannot show progress lose the members whose retention pays for the program," "The ones that keep members are the ones that can show a member what is changing," "A repeat check-in only sustains retention when it shows the member something worth returning for," "A number on a scale rarely carries that engagement," and "That is the moment programs lose people." Replaced with a single instance of "Limited progress visibility can make it harder for programs to maintain engagement between check-ins," in "The Infrastructure Challenge Created by Market Growth," with an explicit link to Visual Progress Tracking for the supporting evidence. (Deliberately used once, not repeated, to avoid re-introducing the overlap the reviewer flagged with the Visual Progress Tracking page.)

**7. Fix medical and product-positioning language** — All six specified replacements applied, each appearing once in "Where FitXpress Fits":
- "verified BMI and body-composition data" → "structured BMI-related and body-composition outputs"
- "tell a healthy trajectory from a concerning one" → covered by item 5's full-sentence replacement (the phrase does not recur elsewhere, so no separate short-form replacement was needed)
- "trust the difference" → "compare changes using a consistent capture method"
- "makes a virtual review carry weight" → removed along with the "Telehealth and Remote Check-ins" section it lived in; the underlying idea (consistent capture supports virtual review) is folded into "How Progress Tracking Fits Into Program Workflows" without this phrasing
- "live or die on" → removed along with the sentence it was in ("Telehealth GLP-1 programs live or die on..."); not needed elsewhere
- "clinical review and program monitoring work from consistent records" → "gives clinical and program teams more consistent longitudinal records"
- DEXA → DXA, throughout (previously appeared in "What FitXpress Does NOT Do" and in the frontmatter `vertical_boundary` field; both updated)

**8. Reconsider the pharmacy-led program description** — "The touchpoint is verification at the point of eligibility review before a prescription" replaced verbatim with the specified language: "Pharmacy-led programs may combine intake and eligibility-related documentation with recurring remote reviews. The regulated BMI-verification workflow [...] is covered separately in the Online Pharmacy BMI Verification guide," now in "How the GLP-1 Care Ecosystem Is Evolving."

**9. Tighten privacy and compliance wording** — Removed the three restated compliance lines ("maintains HIPAA compliance," "follows GDPR principles," "processes no personal identifiers") everywhere they appeared (opening scope section, "Where FitXpress Fits," "What FitXpress Does NOT Do," and two FAQ answers). "Where FitXpress Fits" now carries one short, accurate summary sourced from the approved `fitxpress-data-privacy-security-regulatory-faq` article (photos deleted immediately after processing by default; 3DLOOK typically acts as processor or, under an executed BAA, business associate, not controller) plus a link to that FAQ for full detail. The closing disclaimer also links to that FAQ instead of only to `/legal/`.

**10. Reduce the limitations section** — "What FitXpress Does NOT Do" (three paragraphs, repeated "not" four times) renamed to "Role and Limitations of Mobile Body Scanning" and compressed to one paragraph covering exactly the four required points (supports capture/comparison/documentation; does not diagnose/prescribe/determine eligibility; does not replace DXA/BIA/calibrated scales where required; outputs must be read within the program's workflow). The paragraph uses "not" once in total ("rather than substitute for them" carries the same meaning without the word), consistent with the "avoid repeatedly using 'not'" instruction.

**11. Cut the FAQ from eight questions to four** — Kept exactly: "How big is the GLP-1 market?", "What is driving GLP-1 market growth?", "Why do GLP-1 programs need progress tracking?", "What should GLP-1 programs track beyond scale weight?" (reordered to match the reviewer's list, market-size question first). Removed: "Is this a medical device?", "How do remote check-ins work?", "What does FitXpress not do?", "Can body scanning replace the scale or DEXA?" — these are product-specific and belong on the FitXpress use-case page per the reviewer's note; they were not ported anywhere in this deliverable since moving them onto a different page is out of scope for this hub revision.

**12. Remove or replace the Hims & Hers example** — Kept the example (Option A from the review) and added the explicit caveat: "These figures cover the whole company rather than the weight-management line alone, and the company named weight management as one contributing driver of that growth rather than the only one." No fabricated new statistic was substituted, since the task requires working only from approved facts already in the corpus; a genuinely new market-hub statistic (prescription growth, persistence/discontinuation, virtual obesity-care program count) would require new research and Vadim's approval of a new claim before it could be added as FX-0XX.

## Bonus fold-in from "what already works"

The reviewer noted that KFF also reports 59% higher-than-expected utilization and 66% significant effect on drug spending, and that these would strengthen the operator perspective. Both figures are now included in "GLP-1 Market Size and Growth Trajectory," "What Is Driving Market Expansion," and the "What is driving GLP-1 market growth?" FAQ answer, with the KFF source link preserved.

## Structural mapping (old → new)

| Old section | New section |
|---|---|
| The GLP-1 Market Moment (+ intro paras) | GLP-1 Growth Is Changing How Weight-Management Programs Operate |
| Short Answer: What This Hub Covers | Folded into the intro section (short answer + scope note + adjacent links retained; FitXpress compliance paragraph removed) |
| GLP-1 Market Growth: Size and Trajectory | GLP-1 Market Size and Growth Trajectory (KFF utilization/spend stats added; Hims & Hers caveated) |
| — (new) | What Is Driving Market Expansion |
| Program Models and Where Tracking Fits | How the GLP-1 Care Ecosystem Is Evolving (pharmacy description rewritten; FitXpress-specific asides removed) |
| The Progress-Tracking Gap + Why Progress Tracking Is Becoming Table Stakes | The Infrastructure Challenge Created by Market Growth (consolidated, retention claims rewritten) |
| Body Composition Beyond the Scale | Why Scale Weight Alone Provides an Incomplete Progress Record (estimates-vs-measurement language applied) |
| — (new, matches reviewer's requested section) | What Better GLP-1 Progress Tracking Looks Like |
| Telehealth and Remote Check-ins + Clinic Workflow at Scale | How Progress Tracking Fits Into Program Workflows (consolidated, generic, no FitXpress by name) |
| Where FitXpress Fits | Where FitXpress Fits (retained as the one full product section; language fixes applied; privacy section shortened + linked) |
| What FitXpress Does NOT Do | Role and Limitations of Mobile Body Scanning (renamed, compressed to one paragraph) |
| FAQs (8 questions) | FAQs (4 questions, reordered) |
| Next Steps / CTA | Next Steps / CTA (disclaimer now links to the Data/Privacy/Security/Regulatory FAQ) |

## Frontmatter changes

- Added `revised: 2026-08-05` and `revision_note` fields documenting this pass.
- Updated `vertical_boundary`: DEXA → DXA.
- `claims_used` list unchanged (FX-001, FX-003, FX-004, FX-005, FX-006, FX-007, FX-009, FX-010, FX-012) — all claims are still substantively used, only reworded/repositioned per the review.
- All inline `<!-- claim: FX-XXX -->` markers stripped from the body per delivery instructions; the claims list in frontmatter remains the source of truth for what is cited.

## Not done / flagged for Vadim

- Item 11 says the four removed FAQ questions belong on the FitXpress use-case page. This deliverable does not add them there — that would touch a different article and was out of scope for "revise this hub." Flagging so Vadim can route that as a follow-up task against `fitxpress/for-telehealth-and-weight-loss` if wanted.
- Item 12's stronger alternative statistics (GLP-1 prescription/patient growth, employer utilization, coverage expansion, persistence/discontinuation, virtual obesity-care program growth, beyond what KFF and J.P. Morgan already supply) were not sourced or added as new claims. Doing so would need new research and a new approved FX claim; this revision used the safer, explicitly-sanctioned option (Option A: retain Hims & Hers with a caveat) instead.
