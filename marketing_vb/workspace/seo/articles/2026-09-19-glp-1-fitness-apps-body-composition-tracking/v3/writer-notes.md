---
slug: 2026-09-19-glp-1-fitness-apps-body-composition-tracking
stage: write (Review 1 rewrite, revision 2)
written: 2026-10-20
for: seo-editor, then seo-publisher
---

# Writer notes for draft.md

These notes cover the judgment calls in the draft and anything left open. None of this goes into
the article.

## Gate state at hand-off

- `article_lint.py`: every gate passes except M1 on "GLP-1" in the H1, which is the accepted known
  failure.
- Sentence gate: 92 sentences, mean 15.1, p90 22, 1 sentence over 25 (the first sentence of
  T-PRIVACY-ROLES, 26 words, kept whole), 0 over 35.
- `detect-ai-tells.py --channel article`: CLEAN. Density 0.0, no hard fails, no soft markers.
- Word count: 1,574 prose words, which excludes the three image concept lines. The lint's own count
  includes those lines and gives 1,753, inside the 1,360-1,839 band.
- Lint repetition hints, for the editor:
  - "the prescribing provider" x3: two of the three sit in locked text (T-RECORDS-ACTORS,
    T-PRIVACY-ROLES).
  - "body composition tracking" x3: the Section 1 anchor, the v2 first sentence of FAQ 2, and the
    CTA.
  - "the progress view", "scan to scan" and "glp 1 treatment" x3 each.

## Placements that are mine, not the plan's wording

1. **Privacy FAQ link.** The link sits on "applicable lawful basis" inside the first
   T-PRIVACY-ROLES sentence, so it is mid-paragraph and the locked words are unchanged. If the editor
   reads a link inside a locked sentence as an edit, the alternative is a separate short sentence
   carrying the link. That would add words without adding facts.
2. **KFF sentence (25 words).** "about one in eight" was dropped to keep the sentence at 25 words or
   fewer. "12% of US adults" and "currently taking" stay, and the scope clause "a figure for adults
   generally, not fitness app members" is the one decisions §6 requires. The "X, not Y" shape is
   deliberate there. Restoring "about one in eight US adults (12%)" makes the sentence 28 words,
   which the gate still allows.
3. **Joint advisory.** The draft says "strength training" because that is the advisory's own term.
   "Resistance training" does not appear on the obesity.org release (checked 2026-10-20).
   - "As part of broader nutritional and medical management" is the wording decisions §6 asks for.
     The release itself speaks of lifestyle intervention integrated into the treatment plan.
   - Its own phrase "comprehensive care" is not quoted because "comprehensive" is a banned word.
   - The v2 sentence "names muscle and bone loss among the challenges of GLP-1 therapy" is kept. It is
     attributed and verified.
4. **Neeland.** v2's clause on magnetic resonance imaging studies and its sentence on population,
   drug and comorbidity reasons are dropped as part of the condensing. "Appear to be adaptive" stays,
   quoted and attributed. The abstract was re-checked through NCBI E-utilities, because the PubMed
   page requires cookies and the journal page returns 403.
5. **Section 2 boundary sentence.** "A body scan cannot settle what this research leaves open about
   muscle." The wording is mine, written to the plan's description. It makes no physiological
   statement in our voice, and it avoids a second "question" next to T-MUSCLE-FUNCTION.
6. **Section 1 reframe and down link.** The reframe is "For the app team, the question is what to
   show next to the scale number." The down link follows on the anchor "Body composition tracking for
   fitness apps", which is capitalized at the start of its sentence. It sits at about 16% of the
   body.
7. **Section 5, P3a.** Two sentences there are not locked text:
   - the framework-link sentence from v2;
   - "Repeatability is especially important for a progress view, because each check-in is compared
     with an earlier scan." This is the conditional form in `accuracy-formulations.md` §3.4.

   P3a, P3b and P3c are three separate paragraphs (decisions §A3).
8. **Section 5, P4.** In the optional second-record sentences, "one of those methods" became "with
   DXA or BIA". After the coaching sentence lists six methods, "those methods" would be ambiguous.
9. **Section 4 lead sentence.** "On the app's side, comparable check-ins involve five parts: …". The
   plan asks for one sentence naming the five steps.
10. **Optional items used:**
    - FXS-POPULATION sentence 2;
    - the GLP-1 programs sentence and the top-7 link in Section 5, P1, for AEO prompt 565495617300;
    - the second-record sentences in Section 5, P4.

    `glp-1 app` and `glp-1 and muscle loss` are not placed, because neither fit naturally.
11. **"customer".** The word appears once, in "real-world customer dataset". That is the canonical
    repeatability sentence the coordinator mandated in §A3.
12. **Image concept lines.** Each is one line under its placeholder, in the wording from the plan's
    Illustrations table. None shows muscle definition, muscle labels or medication.

## Section lengths against the plan

Lint shape, including the concept lines:

| Section | Lint count | Without concept lines | Plan |
|---|---|---|---|
| Section 1 | 322 | about 270 | 300 |
| Section 2 | 206 | 206 | 240 |
| Section 3 | 268 | about 195 | 190 |
| Section 4 | 239 | 239 | 270 |
| Section 5 | 562 | about 510 | 430 |
| FAQ | 113 | 113 | 130 |
| Next steps | 31 | 31 | 40 |

Most of the Section 5 overrun is locked text. If the editor needs words back, the first candidates
are the optional top-7 sentence and the second-record pair.

## Still open for Vadim (publish package and digest, not the draft)

These are unchanged from decisions §1, §5 and §H:

- the reviewer's verbatim H1, which drops the primary keyword;
- the customer's sign-off on the description of the 34,000 scans;
- incoming links from the AI in Fitness hub and from `glp-1-market`.
