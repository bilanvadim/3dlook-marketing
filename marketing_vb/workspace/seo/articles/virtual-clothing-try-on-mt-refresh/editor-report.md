---
slug: virtual-clothing-try-on
workspace: virtual-clothing-try-on-mt-refresh
product: mobile_tailor
stage: final
input: draft-v1-writer.md + writer-notes.md + plan.md + plan-audit.md + refresh-gap-analysis.md + context pack
output: final.md
editor: seo-editor
date: 2026-11-04
---

# Editor report, draft v1 → final

## Gates

These are the numbers before the QC fix pass. The current numbers are in "QC fix pass" at the end of this report.

- `python3 scripts/article_lint.py final.md --pack …/virtual-clothing-try-on-mt-refresh.yaml`: **PASS**, all 10 gates `ok`. Attempt 1 passed on the edit before Vadim's CTA addition. Attempt 2 passed after it.
- Detector (`--channel article`): **CLEAN**. Density is 0.0/1000 and rhythm variation 0.51. There are no hard fails and no house-rule violations.
- Prose words: **2,297**, against a target of 2,250. The lint band is 1,912-2,587 and the plan's ±10% is 2,025-2,475. The writer's draft had 2,274.
- Sentence length: 142 sentences, mean **14.1**, p90 21.
  - One sentence runs over 25 words (0.7%), and it is also the only one over 35: the verbatim `accuracy-formulations.md` §1.1 sentence (42 words).
  - The draft had three over 25. I made two of them during the edit and split both before finishing.
- Near-duplicate pairs: none. The repeated phrases are topic terms ("virtual try-on", "Zara Try-On", "virtual fitting room").
- Links:
  - Internal: up 1 distinct (three anchors), sideways 6, trust 1. All 8 targets returned HTTP 200 in the coordinator's check on 2026-11-04.
  - External: 5 links, each to a different publisher.
- Mobile Tailor link depth by prose words: early **12.6%** (S2), mid 79.1% (S9), final 99.8% (S11).

## The three judgment calls

### 1. External hyperlinks: kept, one link per source publisher (9 → 5)

**What canon says.** The canon disagrees with itself, and the newer, higher-ranked sources point one way.

- Against links: `blog-style-guide.md` §4 (2026-05-22) says "No external hyperlinks to source sites. The source name is the citation." That line describes the corpus of nine articles it was built from.
- For links:
  - `terminology-guardrails.md` Part 1 §2 is Asselya's Doc, synced 2026-09-28. CLAUDE.md §6 makes it the winning source on sentence construction. It says: "Internal and third-party linking: Integrate links directly into the anchor text … Applies wherever a source citation is needed." Part 3 adds: "bare URL → link on the meaningful anchor phrase". §3 sets source quality for third-party citations.
  - Asselya's editorial final of 2026-09-11 (`manual-vs-digital-intake-occupational-health-screening`, the basis of `editorial-rewrites.md`, which "wins because it records what the editor actually shipped") has three inline external links: NHANES, OSHA and EEOC.
  - The live `online-pharmacy-bmi-verification` and `clinical-trials-anthropometric-measurement` pages also link out.
  - The `accuracy-roi-telehealth-refresh` final, after Asel's Review 1 (2026-11-02), keeps its inline CDC link.
  - Type G pages are *required* to link external authorities.

**Decision.** Inline links stay, on descriptive anchors.

- Pass 1 dedup applies per publisher. Google is one publisher, so only one Google link stays: the Doppl post, because the plan wants its quote "with the link".
- The other four Google posts are attributed to Google by name in the sentence. Those sentences state Google's own facts about its own product.
- Trade press is named in the sentence and linked once.

To switch to the §4 rule instead, unlink the five anchors in the table below. The text reads correctly without them, because each attribution is already named in the sentence.

**Style-guide drift (flag for Vadim/Asel):** `blog-style-guide.md` §4 should be updated to match the terminology Doc and the 2026-09 finals. I did not edit it; it is outside this run's scope.

### 2. Trade-press facts: both kept, attributed in text

editorial-guardrails #1 asks for a citable source. terminology-guardrails §1.3 names "established trade press" among the safe source classes.

- **ChatGPT Try On (TechCrunch): kept.**
  - I fetched TechCrunch on 2026-11-04 (HTTP 200; Sarah Perez, Oct 1, 2026, 12:21 PM PDT). It confirms every fact used: OpenAI "announced the global launch"; a Try On button in shopping results; a selfie or full-body photo; an uploaded screenshot of an item; Favorites saved "alongside your try-on images".
  - OpenAI's own help center and release notes still return 403, to curl as well as WebFetch.
  - This is the defining 2026 event for the query family. TechCrunch is now named and linked once, in the S5 entry; the draft named it three times. S1, S6 and S7 carry only the source marker.
  - The S3 sentence naming the "ChatGPT Images 2.5" model is cut. It was a third TechCrunch attribution and added nothing to the explanation.
- **Tesco F&F trial (Retail Gazette): kept, narrowed.**
  - Retail Gazette returned 429 to me. The writer read it on 2026-11-04.
  - Retail Times (Fiona Briggs, Sep 25, 2026) loaded and carries the same facts: Sandhurst Extra; about 1,500 F&F womenswear and menswear items; take or upload a photo onto a try-on screen in the clothing department. Two trade outlets agree.
  - It is the page's only concrete in-store example and a UK one (UK traffic is 51 clicks a year). S4 reads abstract without it.
  - **Cut: the Tesco quote.** It was second-hand, and the draft closed the quotation mid-sentence: the Retail Times text continues "…discover new styles and feel more confident before they buy". The facts stay, attributed to Retail Gazette.
  - The S7 callback is one clause with no detail and no link.
- Open item 4 in the context pack ("the writer verifies from a primary source or drops") is therefore met for ChatGPT through established trade press, not an OpenAI page. If Vadim reads open item 4 as primary-only, take out the ChatGPT clause in S1, the S5 entry, S6 route 2 and the S7 sentence. The S3 generative-AI paragraph and FAQ 1 also name ChatGPT and need a small edit.

### 3. Section 9 length: 371 → 352 words, the rest accepted

- Cut: the §5 reframe sentence, which mixed §5 with the verbatim §1 sentences in one paragraph, against `accuracy-formulations.md` §5 "do not mix the two inside one paragraph".
- Cut: the positive restatement before the boundary. The paragraph above already says what Mobile Tailor supplies, so the licensed boundary now stands as one sentence.
- Rewritten: the "In practice, the measurements go straight into…" lead-in.
- Shortened: the accuracy tail.
- The remaining 32 words over the 320 budget are the 62-word verbatim §1.1 + §1.8 block. Section budgets were set before that block was pasted, and the total is inside the target band.

## Coordinator addition (Vadim, 2026-11-04): early CTA

- **Added.** One sentence after the S2 bullets, at 12.6% of prose words:
  > "A try-on image can settle the look, while size for custom and made-to-measure orders comes from body measurements, which [Mobile Tailor](https://3dlook.ai/mobile-tailor/) captures from smartphone photos."
  - It is a text link with no button wording and no trial wording. It leads with try-on and gives Mobile Tailor body measurements only.
  - 25 words, at the gate limit. It carries an MT-HERO marker for traceability and no figure.
- **Three touchpoints.** Early in S2 (anchor "Mobile Tailor"), mid in S9 ("capture body measurements with Mobile Tailor"), and final in S11 ("see how Mobile Tailor works"). All three go to `https://3dlook.ai/mobile-tailor/`.
- **What this overrides, for this article only:**
  - The one-CTA rule in `blog-style-guide.md` §5 ("One CTA per article").
  - Plan D7 and pack guidance ("Mobile Tailor named only in S9 and the closing CTA").
  - It resolves plan-audit open item 6 at the place that item named: S2, on the fit bullet.
  - Reason: Clarity shows articles are read to about 5-35% depth, so a CTA placed only at the end goes unseen. Precedent: `accuracy-roi-telehealth-refresh`, where Asel's Review 1 P1 (item 5, decision A5) asked for early, mid and final CTAs.
- **Effect on Asel's intent objection.** Mobile Tailor now appears in the top 13% of the page, in one sentence that sits outside the bullet list an assistant would lift. Try-on still owns the H1, title, nine H2s and the answer blocks. The check on "3dlook" sitelinks and rankings 2-3 weeks after re-indexing (gap analysis §5) is the place to see whether this costs anything.

## Change log by pass

| Pass | What changed |
|---|---|
| 1 Citations | 9 external links became 5 (table below). TechCrunch named 3 times → 1. The ChatGPT Images 2.5 sentence is cut. The second-hand Tesco quote is cut. The NRF link sits on the report's name, and the attribution sentence is split to keep both sentences under 25 words |
| 2 Structure | The intro roadmap triad became a content sentence: "differ in cost, catalog coverage, and how much they reveal about fit". The S5 closer, which restated the look/size refrain, now carries an observation: all four platforms use generative AI and work from ordinary photos, so that is the approach shoppers most likely meet first. S11 ends on orders where size decides the outcome, then the CTA |
| 3 Voice | The five link-pointer sentences were all "The guide to X covers Y"; one is left (the fitting-room depth link). The AR, 3D-scanning and measuring-at-home links now sit inside sentences that carry content. The body-measurement-app link is the category sentence before Mobile Tailor. Added two "depends on" conditions: the 3D preview depends on the body data and the garment twin, and whether the error matters depends on garment cut. Added two judgments: generative try-on is what shoppers meet first; for jeans and tailored jackets, use the size chart and treat the image as a look check. S8's evidence now opens with a claim: "Google's own tools leave the size decision with the shopper." "Try-on addresses" became "can help with". The vague "Returns carry a large cost" is cut |
| 3b Strategy | No YourFit. Customers are anonymized. "3DLOOK's Mobile Tailor" states ownership once, before the 3DLOOK accuracy sentence. The boundary is a single licensed negation. Three Mobile Tailor touchpoints (above). The sideways links to both cannibalization siblings stay, as the guardrail requires |
| 3c Sweep | Detector CLEAN before and after. Judgment rows checked by grep: no "rather than", no corrective "X, not Y", no we/our, no buyer/organization. "Customer" appears once, in the PPE manufacturer's "customer ordering flow", which is its own customers ordering. `you`/`your` appear only in S6 and the FAQ; the other hits are inside URLs. No hub, cluster or bridge labels |
| 3d Length | S6 tip (30 words) and FAQ 1 last sentence (26 words) split. "full-length photo" ×4 → ×3, "live camera" ×4 → ×3, "the brand's size chart" ×3 → ×2 |
| 4 Polish | AR, VR and PPE are expanded at first use. AI, US, UK and iOS are bare. NDA is bare inside the verbatim §1.8 sentence (flag 1). Serial commas throughout. Every external figure and quote was rechecked (table below). Primary keyword in the H1 and the S3 H2 |

## Sources (all rechecked 2026-11-04 unless noted)

| Marker | Used for | URL | Linked in final.md | Check |
|---|---|---|---|---|
| GOOG-TRYON-US-2025 | US launch, July 2025; Search, Shopping, Google Images (S1, S5) | https://blog.google/products-and-platforms/products/shopping/back-to-school-ai-updates-try-on-price-alerts/ | no, attributed to Google | Jul 24, 2025; "launching in the U.S. … Search, Google Shopping and even product results on Google Images" |
| GOOG-UK-IN-2025 | UK and India, December 2025 (S5) | https://blog.google/products-and-platforms/products/shopping/virtual-apparel-try-on-uk-india/ | no | Dec 03, 2025 |
| GOOG-SELFIE-2025 | US selfie option; "select your usual clothing size"; default try-on photo (S5, S6, S8, FAQ 3) | https://blog.google/products/shopping/studio-quality-digital-try-on/ | no | Dec 11, 2025; "select your usual clothing size"; "Select one to make it your default try on photo"; U.S. shoppers |
| GOOG-DOPPL-2025 | Doppl, US, iOS and Android, June 2025; animated digital version; photos or screenshots; save and share; fit caveat (S5, S7, S8) | https://blog.google/technology/google-labs/doppl/ | **yes**, S8 "Doppl announcement" | Jun 26, 2025; caveat verbatim: "Fit, appearance and clothing details may not always be accurate." |
| GOOG-HOWTO | "try it on" icon; full-length photo; "full-body shot with good lighting and fitted clothing"; save or share (S6, S7) | https://blog.google/products/shopping/how-to-use-google-shopping-try-it-on | no, "Google recommends" | wording confirmed |
| TC-CHATGPT-2026 | ChatGPT Try On, global launch Oct 1, 2026; selfie or full-body photo; screenshot; Favorites (S1, S5, S6, S7) | https://techcrunch.com/2026/10/01/chatgpt-can-now-virtually-try-on-clothes-for-you/ | **yes**, S5 "TechCrunch reported" | trade press, HTTP 200, facts confirmed (call 2) |
| INDITEX-FY2025 | Zara Try-On since mid-December (2025); synthetic avatar from own photos; 43 markets; over 7 million sessions; Zara.com only (S5, FAQ 1) | https://www.inditex.com/itxcomweb/es/en/press/news-detail/b870d5ec-6b7e-491d-b38e-340cd69036df/fy2025-results | **yes**, S5 "full-year 2025 results" | wording confirmed |
| RG-TESCO-2026 | Tesco F&F trial, Sandhurst Extra, September 2026; about 1,500 items; photo on the spot or upload (S4, S6, S7) | https://retailgazette.co.uk/blog/2026/09/tesco-trials-virtual-try-on | **yes**, S4 "Retail Gazette reported" | 429 to me; writer read it 11-04. Corroborated by https://retailtimes.co.uk/tesco-trials-virtual-try-on-technology-as-part-of-new-ff-in-store-shopping-experience/ (Sep 25, 2026) |
| NRF-RETURNS-2025 | 15.8% of annual sales and 19.3% of online sales returned in 2025, all retail (S7) | https://nrf.com/media-center/press-releases/consumers-expected-to-return-nearly-850-billion-in-merchandise-in-2025 | **yes**, S7 report name | both figures confirmed; the report is NRF with Happy Returns |

## Plan deviations

1. **S5 closing clause.** The plan's "each of these shows how an item looks, and size is still chosen separately" became the generative-AI observation. The look/size line was a refrain in five sections (`editorial-rewrites.md` §2). S6 carries the size point for shoppers, S7 sets up S8, and S8 makes the argument.
2. **S3 ChatGPT Images 2.5 parenthetical.** Cut (call 2).
3. **S9 boundary.** One sentence instead of two (call 3).
4. **S4 Tesco aim.** Cut: no quote, no paraphrase (call 2).
5. **Mobile Tailor in S2.** Added per Vadim's addition (above).

## Flags and open items

1. **NDA unexpanded.** "available under NDA" is verbatim `accuracy-formulations.md` §1.8. M1 would expand it at first use, but §1 forbids edits. I kept it verbatim, as the precedent refresh kept RTPV and BAA. If M1 should win, write "under a non-disclosure agreement" and say so in the canon file.
2. **"across body metrics".** This is the verbatim §1.1 wording. `terminology-guardrails.md` §2.13 already lists it as an open item for Vadim and Asselya: an error in centimetres describes body measurements. Not changed here.
3. **Sibling pages still promote YourFit** (plan-audit open item 4). The S3 and S4 depth links go to `ar-clothing-try-on-tools` and `virtual-fitting-room-for-ecommerce`. Both should be cleaned soon after this republish, or the two links dropped. Lint still passes on the other four sideways targets.
4. **Client naming** (pack open item 1) and **byline** (open item 3). Both are still open. The text anonymizes all three customers and carries Assel Sekerova's byline.
5. **FAQ 3 add-back.** ChatGPT's reference-photo handling (Settings → Personalization → Reference photos) is still unverified: help.openai.com returns 403. If someone confirms it in a browser, one sentence can go into FAQ 3 next to the Google example. The same applies to OpenAI's fit caveat for S8.
6. **FAQ 2, "free to use".** This rests on Search and Shopping being free services; Google's posts state no price. ChatGPT plan availability is not claimed.
7. **Unsourced category statements kept, as the plan wrote them.**
   - "AR works best for shoes, eyewear, accessories, and tops"
   - "Live video try-on … runs mainly on AR"
   - "Eyewear and accessory try-on has run on live AR for longer"
   - "3D avatar try-on appears on individual brand sites"
   - Editor additions are relational or opinion sentences with no new fact: the 3D preview "depends on both inputs"; whether the error matters "depends on the garment and how closely it is cut"; generative try-on is the approach shoppers "are likely to meet first".
8. **"Zara Try-On" casing.** Inditex writes "Zara Try-on". The draft's Title Case is kept for consistency with "Try On" and the H1. Change it if strict primary casing is wanted.
9. **H1 year.** "in 2026" needs updating in 2027 (plan-audit open item 7). The SEO title has no year.
10. **Publisher items, unchanged.** The eBook CTA and author bio (dropped by the capture) need a YourFit check. Run the link-200 check again before publish, lift `noindex`, request indexing, and restore 2-3 inbound try-on anchors from apparel posts that do not mention YourFit.

## Self-check (Pass 3c step 4)

- **The look-versus-size thesis was a refrain.** It came back as the closing line of S1, S5, S6, S7 and S11, the same tidy landing each time. Fixed: each section now closes on its own information.
- **Every link sentence had one shape** ("The guide to X covers Y"). Fixed: one pointer sentence remains, and the other links sit inside sentences that carry content.
- **There was no position anywhere.** Fixed with two short judgments (S5, S6) and two "depends on" conditions (S3, S9).
- **Kept on purpose:** the list-heavy middle (S2, S5 and S7 bold labels, the S6 numbered list). These are planned answer blocks for the Search Console question queries the page ranked for.

## QC fix pass (2026-11-04, after QC 18/20)

QC report: `workspace/_quality/seo/2026-11-04-virtual-clothing-try-on-mt-refresh.md`. The coordinator asked for issues 1 and 2. Issue 3 (operator-level customer detail) is **not** acted on: canon has no such facts, and none were invented.

### Gates after the fix

- `article_lint.py final.md --pack …`: **PASS** on the first fix attempt, all 10 gates `ok`.
- Detector **CLEAN**, density 0.0, rhythm variation 0.49.
- Prose words: **2,292** (band 1,912-2,587; plan ±10% 2,025-2,475).
- 136 sentences, mean **14.7**, p90 22. One sentence is over 25 words and over 35: the verbatim §1.1 accuracy sentence. The new S9 lead-in is exactly 25 words.
- No near-duplicate pairs.
- Mobile Tailor link depth: early **12.5%** (S2), mid 78.0% (S9), final 99.8% (S11).

### Issue 1: the look-versus-size refrain, six sections → three

My own self-check claimed this was fixed. It was not: I had varied the wording and left the move in place. The thesis now stays in three places:

- S2: the early CTA sentence.
- S8: where it is argued.
- S9: the opener, "Some clothing businesses need measurements more than images."

| Section | Before | After |
|---|---|---|
| S1 | "Try-on shows how a garment looks. Size and fit come from body measurements." | Cut. The intro ends on "…and how much they reveal about fit", which sets up the H1 promise without stating the answer |
| S2 bullet 5 | "**What it leaves open.** Size and fit. Both depend on body measurements…" | "**How close it gets to fit.** It varies by approach: 3D avatars come nearest but need a 3D model of every product, and generated images can get fit details wrong." This is a condition. The Doppl caveat backs "get fit details wrong" (GOOG-DOPPL-2025 marker added). The early CTA sentence below it now carries the thesis alone |
| S6 | "…pick the size from the size chart. Treat the image as a check on the look." | "For jeans, a tailored jacket, or anything else cut close to the body, compare your own measurements with the brand's size chart before ordering." This is a garment condition and an action, and it sets up the S9 lead-in |
| S7 | "The second is a sizing problem, and sizing depends on body measurements." | "The published summary does not break those figures down by cause." This is a new fact: I checked the NRF release on 2026-11-04 and found no size, fit, apparel or clothing breakdown. The S8 question H2 picks up the second cause |
| S8 | "Fit is a separate question. The answer comes from…" and the closing "For clothing cut to the body or allocated by size, the order therefore starts from measurements." | "For fit, the shopper compares body measurements taken at home with the size chart." The closing transition is cut. The paragraph now ends on information ("3D avatar tools come closest, for the products a brand has digitized."), and S9's opener makes the turn |
| S11 | "Orders where size decides the outcome will still start from body measurements." | "Inditex said in March 2026 that Zara's tool is being rolled out to the group's other brands." This is a new, verified fact supporting the "spreading" forecast; Inditex's FY2025 results say "is being rolled out to the other concepts". The CTA sentence now names the operator's need ("and need the body measurements behind each order") in place of the thesis |

Kept: the S7 two-cause sentence ("A garment can come back because it looks different than expected, or because the size or cut is wrong."). It explains the causes of returns rather than restating the thesis, and the QC quote covered only the sentence after it.

### Issue 2: lead-in before the verbatim accuracy block

Added at the start of the S9 accuracy paragraph:

> "A loose t-shirt can absorb centimeter-level measurement error, but a tailored jacket or made-to-measure trousers sit close enough to the body for it to show."

- Plain reasoning, no new numbers, US spelling.
- The verbatim §1.1 + §1.8 sentences are unchanged, and so are the trust-link anchor and URL.
- The old tail sentence, "Whether that error matters depends on the garment and how closely it is cut.", said the same thing as the new lead-in and is cut (two sentences making one point, `editorial-rewrites.md` §2).
- With that sentence gone, the trust-link sentence's "it" had no antecedent. It now reads "…explains how to judge that error for apparel sizing." This is the only wording change around the block.

### Length and plan deviations

- S9 is now 364 words, against 352 before and a budget of 320. The new lead-in adds 25 words and the cut tail sentence removes 14.
- The total fell from 2,297 to 2,292.
- Plan items now departed from:
  - S1 must-cover 4 (thesis as two sentences)
  - S2 bullet 5 wording
  - S8 item 5 (transition sentence)
  - S11 sentence 2 (size and fit still depend on measurements)
- All four departures follow the QC and coordinator instruction to keep the thesis in at most three places.

### Self-check after the fix

- **The refrain is gone outside the three slots.** Each replaced spot now carries a condition (S2, S6), a sourced fact (S7, S11), or nothing (S1, S8 close).
- **Still neutral connective tissue (QC issue 2b).** For example, "Each approach needs different input from the shopper and the brand…" (S3). It was not in the fix scope and was left as is.
- **S9 still reads as product copy after the explainer (QC issue 3).** The new lead-in eases the step into the accuracy block. The operator-level detail QC asks for needs facts canon does not hold, so it stays with Vadim.
