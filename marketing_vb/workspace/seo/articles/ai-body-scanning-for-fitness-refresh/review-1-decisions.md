---
review: review-1.md (Doc 1WH8C53jidzvTDKKUPlevQqSQ4aHQE5emXMemJ-4ZpgE, tab "Review 1", fetched 2026-11-23)
reviewer: Asselya Sekerova
base_text: v1/final.md (= the Doc tab "Version 1"; the page is NOT yet published, live is still the 2024 article)
decided_by: coordinator (new-article.md review procedure), checked against brand-assets/
rule: THIS FILE WINS over review-1.md wherever they differ, and over plan.md for headings, CTA count and section content.
type: EDIT round. Section order stays. Two sections are shortened (S4 retention, S6 hardware), three additions (early CTA, one example, pilot secondary metrics), one timing line, meta description. plan.md is not regenerated.
word_target: about 2,000-2,150 prose words (band 1657-2242 holds). The reviewer: "The body of the article should not be expanded significantly."
next: seo-editor -> seo-publisher (meta.md + article_package.py assemble) -> QC -> editor fix pass on QC findings
---

# Review 1: decisions

Status words: **ACCEPT** = do what the review says. **ACCEPT, CHANGED** = do it with the change written
here. **REJECT** = do not do it, with the reason. **KEEP** = no change. **VERBATIM** = use these exact
words, no rewording. Where this file gives text in a quote block, that text is the instruction.
Do not paraphrase it.

## A. P1, required

### A1. Early CTA: ACCEPT, VERBATIM.

- Keep the existing last paragraph of the short-answer section unchanged, including its link
  "[body scanning for fitness apps](https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/)".
  It is the landing-map down link.
- Immediately after it, add a standalone CTA block: one paragraph with the two sentences, then the
  link on its own line as the button label. All of it VERBATIM (the reviewer's button label
  "Explore FitXpress for Fitness Apps" in sentence case):

  > See how FitXpress works for fitness apps. Explore the guided scan experience, member progress features, and integration options for connected and digital fitness platforms.
  >
  > [Explore FitXpress for fitness apps](https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/)

- The CTA goes to the landing, not to `#form`. The review: "The early CTA should lead to the landing page rather than introducing another competing conversion destination."
- Format: its own short paragraph, text only. No banner or box in the markdown. The web team may render the link as a button; note that in the package.
- This follows the new `blog-style-guide.md` §5 rule (Vadim, 2026-11-23): two CTAs per article, an early one in the first 30% of the body to the landing, and the closing one in Next steps. The contextual landing link at the end of the hardware section (A2) is an internal link, not a third CTA.

### A2. Hardware section: ACCEPT, CHANGED. Shorten and reposition from "product alternative" to "choosing a measurement workflow".

- H2 VERBATIM: "When should fitness programs use phone scanning instead of in-club hardware?"
- Target length: about 180-220 words for the whole section (v1: about 320).
- Opening paragraph, answer-first, at most 3 sentences. It must still answer the AEO prompt "What's the best alternative to hardware 3D body scanners for fitness studios?" (22% visibility, refresh-gap-analysis.md line 103), so sentence 1 says plainly that a guided scan on the member's own phone, in the studio's app or on its website, is the alternative to a hardware 3D body scanner, and when it fits (members train at home or between club visits). No product pitch here: **remove** "FitXpress by 3DLOOK provides this kind of scan as a mobile alternative to a gym body scanner." and "Two smartphone photos produce 80+ body measurements, such as waist and hip circumferences, along with body composition estimates." from this section. Those are the landing's job.
- One sentence on the hardware category stays (3D camera booths, rotating-platform scanners, BIA platforms; every repeat scan means a visit). Keep "bioelectrical impedance analysis (BIA)" expanded, it is the first use.
- Keep the three contexts as three H3 lists ("In-club hardware fits when", "Progress photos fit when", "A phone scan fits when"), at most 3 bullets each. For the phone-scan list keep: train at home or between visits; each check-in needs a structured record; a coach reviews results remotely. Drop "The scan should appear under the platform's own brand" (white-label is said in S2 and S3).
- Closing paragraph: keep "The options can work together." and the sentence "Each method should keep its own trend line, because numbers from different methods are not interchangeable." Keep the link to the [comparison of two-photo, video, and hardware body scanning](https://3dlook.ai/content-hub/body-scanning-technology-comparison/) in one sentence.
- End the section with a contextual landing link for technical and commercial details. Use the landing-map anchor "mobile alternative to a gym body scanner", for example: "Capabilities, integration, and plans are on the FitXpress [mobile alternative to a gym body scanner](https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/) page." You may phrase the sentence, keep the anchor.
- Do not reuse the landing's H1 wording ("A mobile gym body scanner alternative for fitness apps") in any heading.
- Claim comments: the section loses FXS-SPEED and FXS-OUTPUTS (their sentences are removed). Keep FIT-CAPTURE and FIT-SDK on the sentences that carry them (own phone, app or website).

### A3. One concrete example: ACCEPT, VERBATIM.

- Place it in S3 directly after the "Scheduled check-ins." paragraph and before "Coach review.".
- It is a separate paragraph with its own bold label, so it does not read as a fifth placement:

  > **An example: a six-week program.** A member completes a baseline scan at enrollment and another scan at the end of the program. The app displays the change in waist and hip measurements alongside the member's weight log. If a coach reviews the program, the two scan records provide additional context for the next training block. The app determines which results to show and how to use them.

- Do not add outcomes, percentages, member reactions or retention effects to it. The review: "without inventing customer results or implying a demonstrated retention improvement." One example only.
- If a gate fails on a word inside it, change only that word and record it in editor-report.md.

## B. P2

### B1. Retention section (S4): ACCEPT. Keep the statistics, shorten the discussion, pivot to the hypothesis.

- H2 stays: "How visible progress may affect fitness app retention".
- Target: about 200 words (v1: about 330).
- Keep Adjust (24% day 1, 7% day 30) with its qualifiers (global, 2022 data, all app users). Keep Kidman (median 70% within the first 100 days) with its qualifier: lifestyle behavior and mental health apps, not body-scanning interventions. Keep both links and both claim comments.
- Keep the link to [AI in the fitness industry](https://3dlook.ai/content-hub/ai-in-fitness-industry/) (hub bridge) and to [body scanning for weight-loss progress](https://3dlook.ai/content-hub/body-scanning-technology-for-weight-loss/). Each in one sentence.
- ACSM: keep, cut to 2 sentences (release date October 20, 2026; wearables first, mobile exercise apps second; it ranks how widely professionals observe trends, not usage). The reviewer verified it and counts it as the fresh 2026 research.
- The section turns on the question, VERBATIM:

  > Does showing structured body progress increase the likelihood that a member returns for another check-in?

  Put it after the statistics, as the question this article helps a team test. Keep "None of these sources tested body scans." and the sentence that the effect is measured with the app's own members.
- S8 already states the testable hypothesis. S4 asks the question, S8 turns it into a test. Do not state the hypothesis twice in the same words.

### B2. Processing time: ACCEPT the concern, REJECT the reviewer's wording.

- REJECT "Processing typically completes in under 45 seconds after capture." `tech-spec.md` line 71 and `proof-points.md` line 50: one public timing definition (Vadim, 2026-09-23), "under 45 seconds from the photos to structured results". No processing-only or capture-only splits, and "typically" would be a second variant. (Corrected 2026-11-23: the live landing hero says "with results in under 45 seconds after capture". That starts the clock at the same point as the canon line, so the article and the landing agree in meaning; the article keeps the canon wording.) Same rejection as accuracy-roi-telehealth-refresh Review 1 (A3).
- ACCEPT "guided" and the reviewer's goal (the 45 seconds must not read as the whole member interaction). The canon wording already starts the clock at the photos.
- Short-answer bullet becomes, VERBATIM:

  > - **What it is.** The member takes two guided smartphone photos, front and side. It takes under 45 seconds from the photos to structured results. <!-- claim: FXS-SPEED -->

### B3. Pilot evaluation (S8): ACCEPT.

- Keep the share of members who return for the next check-in as the **primary** outcome. "The outcome is then a single measure" becomes primary-outcome wording.
- Add one or two sentences naming the secondary metrics, VERBATIM list in this order: scan completion rate, retake rate, onboarding completion, and premium conversion if the feature is offered in a paid tier. Say why: they show the friction a new step adds, not only engagement.
- Write it in the article's own words. Do not copy the landing FAQ line "The pilot compares onboarding completion with the usual flow and measures scan completion separately." (the v1 QC cut an onboarding-completion sentence as a landing echo).
- Keep the rest of S8 (comparison group, random assignment where practical, threshold fixed before launch, documented fallback reported separately).

## C. Accuracy

### C1. "Not peer-reviewed or externally validated" sentence: KEEP, no change.

- The sentence is canon VERBATIM: `accuracy-formulations.md` §1.9 "What is NOT claimed. Quote these when scope comes up." It already is the approved wording. Nothing to change in this round.
- Goes to the package as an answer to the reviewer (open item, not a defect): if newer validation documentation exists, the canon changes first (Vadim), then the article.

## D. SEO elements

### D1. H1: KEEP. "AI Body Scanning for Fitness: Where a Phone Scan Fits in the Member Journey" (the reviewer agrees).

### D2. Meta title: REJECT "AI Body Scanning for Fitness Apps | 3DLOOK".

- `landing-map.md` rule 3: "The article's title, H1 and meta title never use the landing's primary keyword". For Hub 1 Fitness the primary keyword is "body scanning for fitness apps" (first anchor in the row, landing-map.md line 17). The proposed title contains it word for word. It would be the same cannibalization the review itself flags in P1 "Reduce overlap with the fitness landing page".
- Keep v1: "AI Body Scanning for Fitness: Where a Phone Scan Fits" (53 chars).
- seo-publisher: if the reviewer wants the brand suffix, give one variant at most 60 characters, with " | 3DLOOK", without the landing keyword. Example: "AI Body Scanning for Fitness: Member Journey | 3DLOOK".

### D3. Meta description: ACCEPT, VERBATIM.

> Explore how AI body scanning fits fitness apps, from member onboarding and progress tracking to coach reviews, SDK integration, and pilot testing.

Rule 3 does not cover the description, and it does not contain the exact landing keyword. Update it in final.md frontmatter, meta.md and the package.

### D4. Canonical and URL: KEEP. `https://3dlook.ai/content-hub/ai-body-scanning-for-fitness/`, no redirect.

## E. Keep unchanged (review §5)

Short answer (except B2 and the A1 CTA after it), the member journey (except the A3 example), accuracy and repeatability (S5), SDK and API considerations (S7), the disability FAQ, the privacy FAQ, the DXA FAQ, the scope note, Next steps. Do not polish them in this round.

## F. Not in the article

- The GA4 figures (410 → 29 sessions) and "57 contacts / 4 deals" are planning inputs. They do not go into the article or the meta.
- v1 open items stay open in the package: byline (Assel vs Dana), Adjust vendor-blog source, ACSM link swap, illustrations for Kristina, 3 inbound-link edits.
- FAQPage JSON-LD: the FAQ questions do not change, so the schema does not change.
