---
qc_date: 2026-11-24
agent: seo-editor (Review 1 edit round); seo-publisher for publish-package.md / meta.md
artifact: workspace/seo/articles/2026-09-21-glp-1-patient-progress-record-body-data/final.md
round: Review 1 (review-1.md, review-1-decisions.md wins)
track: seo
artifact_type: seo-final
total_score: 16/20
status: good
verdict: ship after a short editor fix pass; findings 1 and 2 touch decision quote-block text and need coordinator sign-off first
coordinator_review: done 2026-11-24
---

# QC Report: seo-editor, 2026-11-24, Review 1

**Artifact:** `workspace/seo/articles/2026-09-21-glp-1-patient-progress-record-body-data/final.md` (line numbers = final.md file lines)
**Total: 16/20**, good
**Verdict:** every R1 item and the coordinator addition is in the text as decided. None of the payload claims the canon forbids remain. CTAs and canon wording hold, and Open items carry everything the decisions file asks for. What's left is one overclaim and one near-copy, both in the new muscle-loss H2 and both from decision-supplied text, plus three small fixes.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 4 | 5 |
| B | Factual accuracy | 4 | 5 |
| C | Brand & tone | 3 | 3 |
| D | Format & structure | 2 | 3 |
| E | Output quality | 3 | 4 |

## Verification against review-1-decisions.md (checked in final.md, not in the reports)

| Item | Where | Result |
|---|---|---|
| R1-1, 5 replacements | L108, L112, L200, L174, L232 | verbatim |
| R1-1, capture log H3 | L138-L144 | Order is as fixed: status + known gap, then timestamps + scan identifier, then the program's log, then RTPV (verbatim, FXS-RTPV marker), then the first-entry sentence, unchanged. The program-log sentence was reworded to "What the program logs about...". That falls under "the editor writes the prose" |
| R1-1, L174 marker | L174 | FXS-DELIVERY + FXS-RECORD-STATUS. v1 carried FXS-LIFECYCLE, not FXS-DELIVERY. The deviation is documented and matches the decision's intent |
| Coordinator addition | L180 | verbatim |
| Forbidden payload grep (`flag, clothing, obfuscation, pose, metadata, usable, request, payload, classif, conditions of`) | whole file | 2 hits: L142 (RTPV, allowed) and L220 "standing pose" (FXS-POPULATION canon). No flags, clothing info, face-obfuscation, request metadata or "usable pose" |
| R1-2 early CTA | L114 | Verbatim, in its own paragraph after L112 and before the H2 at L116. It sits at 19.8% of body words (≤30%) |
| R1-2 contextual link | L170 | Anchor verbatim. It is an in-sentence link, so it is not a CTA (blog-style-guide.md L177) |
| R1-2 closing CTA | L234 | verbatim, last H2 |
| Exactly two CTAs → Hub 3 "Link now" | L114, L234 | Both go to `/structured-body-data-for-telehealth-digital-health-programs/` (landing-map.md L19). No `/pricing/` or `/contact-us/` |
| R1-3 | L106, L124 | Bullet verbatim. FXS-PHOTOS added and FXS-LIFECYCLE kept. The H3 sentence is kept. No retention periods in the body |
| R1-4 new H2 | L146-L150 | Heading verbatim. It sits between the capture log and Cadence, at about 153 words. No trial figures, no composition accuracy figures, no "why muscle loss happens". The Neeland claim is attributed ("A 2024 review by... notes"). One sideways link. Body sites match tech-spec "Circumferences" |
| R1-4 M1 follow-on | L226, L228; frontmatter L52-L53 | Short forms used. The frontmatter no longer says DXA/BIA are expanded in the FAQ |
| R1-5 timing | L110 | Same as tech-spec.md L71 |
| R1-6 NDA | L160 | §5 wording, directly after the FXS-REPEAT sentence. "Internal" and the framework link are in the same paragraph, with no percentage |
| R1-7 | L224 | verbatim, pharmacy guide kept |
| R1-8 | L188 | only the deletion sentence was cut |
| Canon | L192, L220, L100/L182 | HIPAA matches the decision's KEEP string (decisions L218-L219). GDPR is verbatim. The disability limitation matches accuracy-formulations.md L292-L295. "FitXpress is not a medical device." appears twice |
| Open items | publish-package L132-L141 | All present: the three relink lines (verbatim), body sites, the third-party source decision and the Telehealth consistency item. plan.md L38 gives volume as "no data", not TBD, and the zero-demand line is carried |

## What was wrong (specific)

### A. Adherence: 4/5
- Everything in the table above was applied as decided. The edits beyond the item text (paragraph boundary in the new H2, serial commas, the cut v1 sentence in "The generated fields", "itself" dropped) are all logged in changes_summary and in Open items L139.
- -1: the R1-1 acceptance check fails literally and nobody owns the conflict. Decisions L76-L78 and L240 say "the only hit allowed is the RTPV sentence", but L220 "standing pose" also hits. Keeping it was right: it is canon on the do-not-change list (decisions L228). But final.md L63-L65 says "Kept; listed for Open items", and publish-package L81 files it as "Note, information only" in the change log, outside Open items (L130-L142).

### B. Factual accuracy: 4/5
- Every figure is approved: 80+ (L107), the timing in tech-spec form (L110), and "five scans per participant ... below 1 cm" (L160, the accuracy-formulations §5 short form; "below 1 cm" is accepted per §5 L282-L283). There is no 96-97% and no composition accuracy figure. No client names, and FXS-CLIENTS is unused.
- Sourcing: one external link, the PubMed review at L150 (EXT-NEELAND, verbatim abstract in pack L108). It is a neutral source, not a vendor blog. Every other link is internal and returns live (links_live 10/0).
- -1, positioning (L148): "A program answers it from fields the record already carries." Here "it" is muscle loss during GLP-1 treatment. L150 then says lean mass "may not always reflect changes in muscle" and that FitXpress "does not assess muscle strength, muscle function, or sarcopenia". The live sibling states the limit outright: "A mobile body scan cannot determine whether a member has lost muscle" (published-live-2026-11-06.md L25). audience.md L40, segment #1 Don't: diagnostic claims. The sentence comes from the decision's quote block (decisions L160). It is not part of the FXS-MUSCLE-FIELDS text (pack L93).
- Nit (L150): "Its definition of lean mass also covers organs, bone, and fluids." The abstract (pack L108) says what the lean-mass *measure* includes. It does not give its own definition.

### C. Brand & tone: 3/3
- No issues. The body has 0 banned words and 0 em/en dashes. There is no let / so / plus / you / our / organization / buyer (grep hits only in frontmatter). Detector 0.0/1000, mean sentence 13.1, 0 sentences over 25. "customer" appears only at L160 (canon dataset phrase), L188, L192 and L224 (contract, legal or canon). The actor is "the program" throughout.

### D. Format & structure: 2/3
- The frontmatter is complete (`product: fitxpress`, `status: edited`, claims_verified, external_sources_used). There are 11 H2s in decision order. The meta title is 56 characters and the description 154. Checklist 19/19.
- -1: article_lint VERDICT FAIL at gate 8 (GLP-1 in the H1, the documented `gate_m1_note` case). This is the same deduction as the 2026-09-21 QC, which the coordinator confirmed there ("-1 за lint FAIL корректен").

### E. Output quality: 3/4
- The value holds. The capture log now separates what FitXpress returns (status, timestamp, scan identifier) from what the program logs. The five-count audit (L198-L202) survives with a usable item 3. The new H2 gives the program-side muscle-loss answer that the plan row (content-plan.md L197) asked for.
- -1: about 10 minutes of edits. The RTPV sentence at L142 has no bridge. "Photos are the input to the capture." repeats verbatim at L106 and L124. "what the change is made of" (L130) echoes "what the weight change is made of" (L148). The Neeland lines near-copy the live sibling (finding 2).

## Findings by severity, each with a fix

1. **Medium (B). L148 overclaims on muscle loss.** "A program answers it from fields the record already carries" says more than L150 and the live sibling allow.
   Fix: the coordinator approves changing this connective sentence. It is outside the FXS-MUSCLE-FIELDS claim text, so no claim moves. It should say the record holds the fields a program reviews for that question, in line with "These figures support clinician review." Deleting it also works, since the paragraph still runs question → fields. The editor applies the change.
2. **Low-Medium (cross-page duplicate, not an intent cannibalization).** L150 "A 2024 review by [Neeland, Linge, and Birkenfeld](…) notes that changes in lean mass may not always reflect changes in muscle. Its definition of lean mass also covers organs, bone, and fluids." almost repeats the live sibling at L37 and L39 ("A 2024 review by [Neeland, Linge, and Birkenfeld](…)" / "The same review notes that changes in lean mass may not always reflect changes in muscle. Its definition of lean mass also covers organs, bone, fluids, and water in fat tissue."). It is the same source and the same point, in almost the same words, on the page that owns the muscle-loss intent. Everything else in the H2 is within the constraints: no figures, no "why", program-side framing, one sideways link.
   Fix: extend the EXT-NEELAND Open item (publish-package L136) to name this overlap so Asselya chooses. Option A is to strike it (the fallback is already written there). Option B is to keep it, reworded away from the sibling's phrasing and attributing what the *measure* includes rather than "Its definition". The coordinator signs off because this is decision quote-block text.
3. **Low (A, process). The grep acceptance conflict is not in Open items.**
   Fix: the publisher moves the publish-package L81 note into Open items as one line. The line names the conflict (decisions L240 vs do-not-change L228) and who decides. The coordinator amends the acceptance check to exempt the FXS-POPULATION canon sentence, and final.md L63-L65 then matches the package.
4. **Low (E). The RTPV sentence at L142 sits under "The capture log" with no bridge.** It can read as if RTPV output were a logged field, which pack note L87 rules out ("RTPV output is never described as part of the record").
   Fix: keep the RTPV sentence verbatim. Tie it to "the same protocol" in the preceding sentence as capture-side guidance, which is the decision's own reason for placing it there (decisions L64-L65).
5. **Low (E). Repetitions.** (a) "Photos are the input to the capture." appears at L106 and L124, and Open item L140 exists. (b) The "made of" echo between L130 and L148.
   Fix: (a) the coordinator waives the "only if the gate flags the pair" condition (decisions L131-L133), and the editor varies L124 while the bullet keeps its wording. (b) The editor rewords L130, a v1 sentence that is not decision text, so the "made of" framing stays only in the new H2.
6. **Low (meta). meta.md L3: "including for muscle loss questions".** The compound modifier is unhyphenated, and the clause puts the sibling's head term into this page's snippet.
   Fix: hyphenate to "muscle-loss questions". The publisher confirms with the coordinator whether the clause stays (the plan row assigns the program-side angle here) or goes.

## Checked, not issues
- L170 is an in-sentence landing link, which blog-style-guide.md L177 counts as an internal link, not a third CTA.
- "below 1 cm" rather than "< 1 cm": this is the verbatim §5 short form and the gate accepts it.
- BAA is expanded inside the HIPAA sentence, unlike the compliance.md short form. Decisions L218-L219 keep that string verbatim.
- The serial-comma split between the verbatim bullets and the new H2 is already Open item L138.
- The early CTA has no action-label line, which blog-style-guide §5 asks for. Decisions L97-L98 override this explicitly.

## Top 3 issues (for improver)

1. Decision quote blocks can carry overclaims and sibling copies (findings 1 and 2). The editor applies them verbatim, so a "constraints" list in a decision needs a coordinator self-check against the sibling's live text and the section's own limits before it ships to the editor.
2. Acceptance checks that collide with do-not-change canon (finding 3) should land in Open items automatically, not in a change-log note.
3. Placement-mandated feature sentences (RTPV) need a bridge requirement in the decision, or they read as dropped-in.

## Coordinator review

coordinator_review:
  agreement: ✅ agree
  top_issue: Q2 — the Neeland pair copied the live sibling's wording; the copy came from the coordinator's own R1-4 quote block, not from the editor. Lesson: when a decisions file quotes an approved external source already cited on a sibling page, write the sentence fresh from the abstract, never from the sibling's text.
  actions: all six findings confirmed in final.md and applied (decisions file, section "QC fix pass"): Q1/Q2/Q6 verbatim, Q3 check amended + Open item 9, Q4 bridge, Q5 two rewordings. After the fix pass: 2,230 words, lint 10/11 (only the documented GLP-1 H1 M1 case), detector CLEAN, package 19/19 + 8/8, links_live 10/0, CTAs at 19.6% / 97.6% (+ contextual 57.6%), grep = RTPV sentence + canon disability line only.
