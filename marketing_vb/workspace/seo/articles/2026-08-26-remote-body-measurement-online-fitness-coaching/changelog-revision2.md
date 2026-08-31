# Changelog — Remote Body Measurement for Online Fitness Coaching, Revision 2

**Source:** `draft-v3-revision1.md` (== the doc's Version 2 tab, frozen as `review2-version2.md`)
**Review input:** `review2-comments.md` (Review 2 tab, 20 numbered corrections + evidence + length)
**Output:** `draft-v4-revision2.md`
**Date:** 2026-08-31

**Governing ruling.** Vadim, 2026-08-31: «всі формулювання тут точні і бери як головний істочнік». Review 2's
wordings are the primary source for this article and outrank the internal guardrail files on wording. That
reverses revision 1's medical-device decision (item 1 below).

**Note on how this round finished.** The revision agent wrote `draft-v4-revision2.md` and was then cut off by
an API spend limit before it could produce this changelog or run the detector. The draft was verified,
the detector run, the frontmatter word count filled in, and this changelog written in the main session
afterwards. No content in the draft was re-generated; every claim below was checked against the file.

## Required corrections

**1. Approved medical-device wording — applied.** "FitXpress is not positioned as a medical device." now
appears in both places the review names: the scope note (L19) and `What FitXpress does not do` (L146).
Revision 1 had declined this on the strength of `terminology-guardrails.md`; the corporate instruction
takes precedence, and this is the recorded exception. Consequence, accepted knowingly: the phrase is an
auto-grep hard fail in `detect-ai-tells.py`, so the article no longer runs CLEAN. See the detector block.

**2. GLP-1 reference removed.** The clause "It has no role in glucagon-like peptide-1 (GLP-1) eligibility"
is gone. The boundary now reads as the general form only: does not diagnose conditions, make clinical
decisions, or determine treatment eligibility. Verified: zero occurrences of `GLP-1` or `glucagon` in the
article.

**3. Smart Scales workflow corrected.** "the software flags a difference" is gone. Now: "where a
self-reported weight is also supplied, the platform can compare the two values and configure discrepancy
logic" — a capability the platform configures, not a universal automatic flag.

**4. No implication of direct measurement.** The paragraph opening "The line between a measured value and
an estimate…" is deleted. The four-way distinction the review restates is carried by the output list
itself: model-generated body measurements, software-derived body-composition estimates, calculated
metrics, predicted weight (plus the 3D model as the fifth artefact).

**5. Smart Scales defined as software.** "read from the images" is gone: "a software-based predicted-weight
output and not a physical scale, with approximately 3.5% average prediction error under evaluated
conditions."

**6. Scale comparison corrected.** "A connected scale gives a precise weight" is gone from both the body
and the FAQ. Now: "A connected scale gives a direct weight reading, and a calibrated scale remains the
right instrument where a precise weight matters." The consumer-smart-scale table row also names device
quality and calibration as the disclosed limitation.

**7. Remote-method statement corrected.** "None of the three runs remotely across a whole roster" is gone.
Now: "Access separates them. DXA and professional BIA require facility access; home scales do not. What
none of the three delivers is standardized, comparable capture of circumferences and composition across a
whole roster at every check-in." The paragraph's logic now rests on comparability, not on remoteness.

**8. Sub-variance changes no longer called noise.** "A movement smaller than the variation is best read as
capture noise" is gone. Now: "A smaller difference cannot be confidently distinguished from expected
scan-to-scan variation, which leaves open whether a real change occurred."

**9. Micro-change limitation added,** in the same place, once: "Mobile scanning is intended for
longitudinal trends across weeks and months; very small short-term changes sit below what the method can
resolve."

**10. Legal basis fixed.** "A coaching program still owns its own consent language" is gone. The approved
role statement is used verbatim: "In most enterprise deployments, the customer acts as controller and
3DLOOK acts as processor under GDPR." followed by the customer's duties — establish an appropriate legal
basis, provide the required notice, and obtain consent where consent is required or relied upon. The FAQ
answer no longer says programs should always obtain explicit consent; it now names the controller role and
consent as the basis "where consent is the basis relied upon."

## Content and style refinements

**11.** "a coach carrying two hundred remote clients" → "Managing a large remote roster means nobody is in
the room to put a tape measure around a client's waist." The invented number is gone.
**12.** "in place of an in-person intake or check-in appointment" → "covers the measurement component of an
intake or a check-in without an in-person appointment."
**13.** "Self-reported weight moves with hydration" → "Body weight varies with hydration, food timing, and
which scale was used; a self-reported figure records the reading and none of those conditions."
**14.** "reads as a loss that never happened" → "can produce an apparent difference caused by placement
rather than body change."
**15.** "which removes the parallel spreadsheet" → "which, depending on how results are stored and
displayed, can remove the parallel spreadsheet and the manual entry of tape figures."
**16.** "The fourth column carries the weight." deleted. The paragraph now opens on the limitation itself:
"Interpretation is where the limits bite."
**17.** "A scan can show that a waist circumference moved" → "A scan records a measurement difference
between two check-ins; confirming a physical change means weighing that difference against scan-to-scan
variation and the conditions of each capture."
**18.** Progress-photos table cell: "not measurable" → "not inherently standardized or quantitative."
**19.** "coach hours are what caps how many clients a program can serve well" → "coach hours can become the
constraint on how many clients a program serves well."
**20.** "and less to protect" deleted; the sentence ends at "has fewer check-ins to standardize."

## Evidence and sourcing

Both sources the review names are added to the method-comparison section, in one paragraph, two sentences.
Neither was fetched from PubMed (it blocks automated fetches); both were verified through the NCBI
E-utilities API on 2026-08-31, citation and abstract:

- **BIA hydration sensitivity** — Ugras S., *Libyan Journal of Medicine* 2020;15(1):1741904
  (doi:10.1080/19932820.2020.1741904, PMID 32182203). Used for: 140 subjects, foot-to-foot BIA after four
  successive 500 mL water intakes, body fat mass overestimated relative to baseline by 2.08% to 7.92% in
  males and 3.4% to 9.4% in females. Anchor text is descriptive and the journal is named in the sentence.
- **DXA protocol standardization** — Nana A, Slater GJ, Stewart AD, Burke LM, *International Journal of
  Sport Nutrition and Exercise Metabolism* 2015;25(2):198-215 (doi:10.1123/ijsnem.2013-0228, PMID
  25029265). Used for: few studies detail their scanning protocol; the review proposes a standardized one
  (rested, overnight-fasted, minimal clothing, consistent positioning) as the condition for detecting
  small changes with confidence.

Neither source is used to attack the method it describes, and neither is presented as validating FitXpress.
**This closes the "zero external sources" open item** carried since 2026-08-26, which was capping
`quality-controller` category B.

No named coaching customer was invented, per the review's explicit instruction.

## Length and repetition

| Measure | v3 | v4 |
|---|---|---|
| Body words, tables included | 2,916 | **2,644** |
| Body words, table rows excluded | 2,584 | 2,348 |
| Detector tokenisation | 3,015 | 2,750 |

The frontmatter now carries one number with its method stated on the same line, so the three-way
disagreement the review flagged (frontmatter 2,582 vs reviewer ~2,980 vs detector 3,015) cannot recur:
v3's 2,582 was a table-excluded count compared against table-included ones.

**Reduction as shipped: 9.3%**, against the review's "approximately 10–15%". The two evidence sentences the
same review commissioned are 118 words; excluding them the editorial reduction is **13.3%**, inside the
band. Consolidations made, all named by the review: the output list now appears once as the canonical
five-item list (was three places), the FAQ went from 7 questions to 5 by dropping the two that only
restated the body ("How do clients take the measurements?", "What body data does it capture?"), the privacy
material is one subsection plus one short FAQ answer, "the coach decides" survives once in the body and
once in the FAQ, and engagement/retention is no longer repeated across pilot, best-fit and conclusion.

Verified repetition counts, body vs FAQ: `80+` 1/1, `45 seconds` 1/1, `less than 1 cm` 1/1, `1.5 to 2.0`
1/1, `96 to 97` 1/0, photo deletion 1/1, HIPAA 1/1, who-decides 1/1. This is the 1-body-plus-1-FAQ pattern
Review 1 item 7 asked for and Review 2 did not overturn.

**Production notes removed from the article frontmatter** per the review: `changes_summary`, `self_check`
and `revision_note` are gone, along with all detector commentary and any discussion of reviewer conflicts.
The frontmatter is now slug, product, title, author, date, status, word_count, claims_verified,
review_source. Everything removed lives here and in `log.md`.

## Detector

Run on the output, `--channel article`:

```
SEO / blog article · en · 2750 words
AI density: 1.09/1000 (budget 6.0) -> low
VERDICT: HARD FAILS (2) — fix every hard_fails entry and the house-rule violations
HARD FAILS:
  [positioned_as] x2: 'not positioned as' (L19)
```

JSON form: `hard_fails` contains only the `positioned_as` category (2 hits, scope note and limitations),
`house_rule_violations: []`, `markers_by_category: {positioned_as: 2, corrective_contrast: 1}`.

**Both hard fails are the approved exception from item 1.** Nothing else fails: no em dashes, no banned
words, no `DEXA`, no `±`, no `so`-as-result, no `we/our/you`, no presumed reader reactions, no attributed
behaviour, FX-004 absent, no named competitors, GLP-1 absent. The one soft marker, `corrective_contrast`
at L25 ("caused by placement rather than body change"), is the review's own mandated wording for item 14
and was left as written.

## Open items for Vadim

1. **`terminology-guardrails.md` still bans "positioned as".** This article ships the corporate wording by
   ruling, but the guardrail file and the detector are unchanged, so the next article and the next detector
   run will hit the same conflict. Either record the corporate exception in the guardrail file and add an
   allowlist entry to `detect-ai-tells.py`, or treat this article as a one-off. Not touched without a
   decision, since both are sources of truth.
2. **`context-pack.md` claim records still carry the older wording** — FX-006 as `±3.5%`, FX-007 naming
   SSE-S3. The article now says "approximately 3.5% average prediction error under evaluated conditions"
   and "encrypted in transit and at rest on AWS". CLAUDE.md §1 and §12 carry the old forms too.
3. **`about-me.md` locks repeatability as `< 1 cm`;** the reviewer's mandated sentence spells "less than
   1 cm". Reconcile at source rather than per article.
4. **The controller/processor statement is new to this article's claim set.** It came from the review as
   approved wording; it is not in `context-pack.md` approved_claims and has no proof-point entry. Worth
   adding to `product-info/compliance.md` so the next article can use it without a fresh ruling.
5. **Older `ai-body-scanning-for-fitness` page** (Review 1 item 1): still a separate content-ops decision.
   Verified 2026-08-31 as live, published 2024-06-12, updated 2026-07-08, H1 "Revolutionizing Fitness
   Tracking…" — which uses a CLAUDE.md §6 banned word. It sits on its own `content-plan.md` row (line 81,
   Review / decide, P2), so no cannibalization with this article's row (line 75).

## Post-pack correction, 2026-08-31 (main session)

Caught while reading the CMS body: the output list has five items, and the sentence under it said "Those
**four** data types are not interchangeable", with the FAQ echoing "Those are **four** different kinds of
output". Four is defensible as the review's four data classes, with the 3D model as the fifth artefact, but
directly beneath a five-item list it reads as an arithmetic error, and review 2 was entirely about
precision. Both sentences now drop the count: "Those data types are not interchangeable." and "Those are
different kinds of output". The four-way distinction the review requires is still carried by the list
itself.

Applied to `draft-v4-revision2.md` and to §7 of `publish-package.md` together, then verified: the CMS body
diffs clean against the draft (comments stripped) with no other difference. Counts updated everywhere
they appear: body 2,644 words including tables (2,348 excluding table rows), detector 2,750. Detector re-run
after the edit: `AI density 1.09/1000 -> low · VERDICT: HARD FAILS (2)`, both `positioned_as`, unchanged.
