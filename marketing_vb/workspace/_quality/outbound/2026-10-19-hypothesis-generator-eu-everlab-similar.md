---
qc_date: 2026-10-19
agent: hypothesis-generator
artifact: workspace/outbound/campaigns/2026-10-19-eu-everlab-similar/hypothesis.md
track: outbound
artifact_type: hypothesis
total_score: 16/20
status: good
coordinator_review: done
---

# QC Report — hypothesis-generator — 2026-10-19

**Artifact:** `workspace/outbound/campaigns/2026-10-19-eu-everlab-similar/hypothesis.md`
**Total: 16/20** — good (approve after the three fixes below, before message-sequencer)

**What I scored against:**
- `icp-detail.md` §1, §4, §8, the universal exclusions (l.558-565) and the IT roles section
- `proof-points.md`, `accuracy-formulations.md` §1.2 and §1.4, `compliance.md` §9 (l.102)
- the agent prompt
- `outbound_pack.py` CARD_SECTIONS (l.745-753), build_card (l.818-937) and the rule-gram check (l.1660-1692)
- the registry (`global-company-registry.json`, every `exclusions/*.json`)
- the AU 08-14 and EU 10-07 notes and responses
- the 10-16 hypothesis QC
- Vadim's brief, quoted on l.23

**Taken as fact:** limits, signature, bans, the detector and completeness.

**Limits of this QC:**
- No web tool, so the external figures (Lucis, Axo, Aeon, Neko) were not re-fetched.
- No shell, so notify.py was not run.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 4 | 5 |
| B | Factual accuracy | 4 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence — 4/5
- **What holds:**
  - One hypothesis and every template section.
  - The `titles` block and the Message 1 gate (l.178).
  - Sourced evidence and eight open questions, each with a default.
  - Lessons from the Everlab and Clinique La Prairie declines drive the design (l.32-37).
  - The registry claim (l.19) checks out: none of the 20 named leads appears in any registry. CLP, Lifesum, Thriva, Superpower, Everlab and Vively are where l.19 puts them.
- **Agent defaults filed as Vadim's decisions.** The "Vadim's decisions" section goes verbatim into both cards. Two items in it are not in the verbatim brief (l.23):
  - l.27, the ≥20 gate.
  - l.28, `status: approved` "folded into" the list review. The prompt says `draft` and STOP.
  - The 10-11 and 10-16 QCs flagged the same pattern.
- **The vertical is never mapped to an ICP segment.** `icp-detail.md` has no preventive-health or longevity segment. The validate card's regex (outbound_pack.py l.880) picks up the first `icp-detail.md §N` (l.230). It hands the validator §1 verbatim: weight loss and GLP-1, 50-5000 employees, and a geo with no Continental country except Germany. Open questions do not flag this.

### B. Factual accuracy — 4/5
- **Copy-facing facts are clean.** Each of these is in `proof-points.md` wording:
  - two photos
  - "under 45 seconds from the photos to structured results"
  - 80+ body measurements
  - estimates, BMI and BMR calculated
  - 34,000 anonymised, 112,100 3DLOOK-wide, "3DLOOK has worked with 100+ clients"
- Other sources check out too:
  - Validation ranges (l.76) match `accuracy-formulations.md` §1.4.
  - The GDPR line (l.184) exists verbatim at `compliance.md` l.102.
  - The CLP decline paraphrase (l.34) matches `responses-summary.md` l.22.
- **l.75 misreads the AU notes.** It says Everlab "buys clinical body composition at facility cost"; `companies.md` l.82 says Everlab *sells* it.
- **l.33 is unsupported.** It says Everlab declined at "Message 2", but `responses-summary.md` l.38 does not record which message.
- **Reason 2 (l.75) is off-audience.** It rests the "body size matters" case on the Lancet obesity-diagnosis commission. That is evidence for obesity care, applied to "healthy adults" (l.43), with "obesity" banned in copy. The pain itself is inferred from an absence in a desk pass. No source from this vertical shows that anyone wants it.
- **Sourcing:** about 20 external links, mostly trade press and company pages. Not re-fetched.

### C. Brand & tone — 2/3
- No em or en dashes (grep). No banned words outside the ban lists.
- **The Use case (l.70) is a 64-word sentence that goes verbatim to writers.** It uses "so the member records…", the benefit-"so" that the artifact's own l.189 bans.
- **"plus" is used as a connector at l.58.** That section is carded to the validator.

### D. Format & structure — 3/3
- The frontmatter is complete: `product`, `profile`, `market`, `use_case`, `cap_per_group`, `referral_call`, `banned_terms`.
- The path is correct. The `titles` block has one title per line.
- Section names match the card keys (`company types in scope`, `message angle`, `decisions`).

### E. Output quality — 3/4
- **Strong:**
  - The persona is built on the two real objections (l.82-83).
  - Every lane has a defined target (l.153-158).
  - There is a feature screen per row (l.66).
  - Honest limits (l.76) and an honest count: ~15-20 known names against 25-30 asked (l.58).
- **The success metrics cannot produce a verdict (l.218-224):**
  - 60 contacts at 25% acceptance is about 15 accepts, and at 10% replies that is about 1.5 replies.
  - "Inconclusive if fewer than 30 people accept" (l.224) is therefore the planned outcome, and the artifact does not say so.
  - The falsification test needs three objection replies, and the positive-reply target is 3 (l.221). Neither is reachable.
  - Precedents (08-14 l.386, 09-29 obesity l.256) size this to volume. This hypothesis copied 10-07's "30" instead.
- **The clinical lane asks for a sentence the writer will not have.** l.154 and l.186 require "the §1.2 repeatability sentence". The messages card does not carry `accuracy-formulations.md` (outbound_pack.py l.893-895), only "< 1 cm". The writer will rebuild the sentence from the number. The 10-06 hypothesis l.346 pasted it verbatim instead.
- **One coined phrase is planted four times in carded text:** "compare(s) across the scans [it / the programme] selects" at l.70, l.146, l.154 and l.181. At l.181 it is a quoted copy line.
  - The code licenses quoted text and skips any 5-gram containing "scans" (l.1666-1671), so repeats will not fail the gate.
  - Same mechanism as the 10-07, 10-11 and 10-16 QCs.
  - "nothing to ship, stock or install" also repeats (l.86, l.149, l.155).
- **Segment B contradicts the design response.**
  - l.37 targets members who are away from the clinic, with re-tests and an app.
  - Segment B (l.54) is imaging check-ups that measure the body on site, which is the CLP objection. Two of its four leads are expected to be fit 3 with no app.
  - Fit-3 rows count toward the gate (l.49, l.234), which is soft padding.
- **Hello Inside (l.53, "CGM programme") is listed as "likely" in segment A.** It is a metabolic nutrition programme, which the anti-cases exclude as a thesis already run on `olena` (l.199). It is also not a lab re-test membership.
- **l.37 prescribes one Message 1 question for every account ("what members do between assessments").** The lane notes (l.153, l.158) ask for a question about the person's own work instead. One question across 25-30 companies pushes the openers toward sameness.

## Top 3 issues (priority for improver)

1. **The success metrics are unreachable at the planned volume (l.221, l.224).**
   - Size "inconclusive" to about 15 accepts, and state that it is the likely outcome.
   - Bring the positive-reply target and the falsification count down to what about 1.5 expected replies can show.
2. **The clinical handoff and copy traps (l.154, l.181, l.186).**
   - Paste the §1.2 sentence verbatim into Rules: "For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm."
   - Drop the quoted copy line at l.181.
   - Keep "scans it selects" to one carded mention, out of l.70, l.146 and l.154.
3. **The segment logic contradicts the artifact's own lesson.**
   - Segment B and fit-3 counting toward the gate (l.49, l.54, l.234) conflict with l.37 and the CLP decline. Rank B below A and C, or stop counting fit 3 toward the gate.
   - Move Hello Inside (l.53) to "to check" against anti-case l.199.
   - Move l.27-28 out of "Vadim's decisions" into Open questions.

## Coordinator review

agreement: ✅ agree
top_issue: the success metrics cannot produce a verdict (60 contacts × 25% acceptance ≈ 15 accepts, but "Inconclusive if fewer than 30 accept" and 3 positive replies as target); checked l.218-224. Also confirmed: items 3 (≥20 gate) and 4 (status approved) in "Vadim's decisions" are my own coordinator reading of his brief («знайти 25-30 компаній»), not his words: they move to a separate coordinator block. All three top issues and the smaller items (l.70 use-case sentence, l.75 "buys") went to a fresh hypothesis-generator fix round before step 2.
