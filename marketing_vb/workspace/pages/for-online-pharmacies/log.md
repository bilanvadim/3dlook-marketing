# Log: online pharmacies landing

## 2026-11-09: decision and gates

- Origin: BMI verification review (`workspace/pages/bmi-verification/log.md`). Vadim: the BMI page "describes product
  features and routes to the use-case landings"; asked whether to rework it for pharmacies or build a separate UK
  pharmacy landing. Recommendation: keep the BMI page as the feature description, build a separate landing. Vadim: «ок».
- Map and inventory updated, commit 6988db2.
- Ahrefs (~1,000 units): no measured buyer demand for pharmacy phrases in GB or US (see `gate-reports.md`).
- Phase 0 intake, G-I (pass: standing FX waiver, demand note) and G-A written in `gate-reports.md`. Stopped at the G-A
  checkpoint: URL, angle, H1 and who drafts are Vadim's call.
- 2026-11-09, Vadim's reply to the checkpoint: «ок, коміт та пуш» (typed in the Latin layout). Read as OK on the URL
  (`/for-online-pharmacies/` → 301 `/fitxpress/for-online-pharmacies/`) and the angle. Still open: H1 (A or B) and
  who drafts (Nika or page-builder).

## 2026-11-23: Phase 3 build and builder's G-T (page-builder subagent)

- Brief from the coordinator: Vadim 2026-11-23 «build the whole page», with two hard requirements: no competition
  with the articles, the BMI feature page or the GLP-1 landing; structure as close as possible to the live fitness
  landing. H1 = option B (Vadim confirms at the final checkpoint).
- Read: CLAUDE.md, page-builder skill and references, gate-reports/log here, fitness final (md + html) and the live
  fitness HTML captured 2026-11-23 (block order, `#form` anchor, shared form embed, logo strip), insurance final
  (register), BMI v7 + its log, GLP-1 v4, the compliance guide (FINAL-PUBLISHED + live text), use-case file,
  uk-meds.md, proof-points, accuracy-formulations, tech-spec, compliance, roadmap, landing-map, schema-entities,
  live /pricing/ (2026-11-23).
- GPhC review PDF (April 2026) downloaded and read: 1,307 concerns, 11% third most reported, "photographs that could
  be easily manipulated", questionnaire-only verification not enough. The GPhC website itself returns 403 to curl.
- Built `page.md` (copy, Yoast fields, markers, JSON-LD) and `page.html` (fitness final CSS namespaced `.fx-op-*`,
  live section order). JSON-LD FAQ answers and the meta description are generated from / checked against page.md by
  script.
- Sales pass and blog test, cuts: duplicate GPhC source label (one shared line), the step-3 routing sentence (repeated
  the mismatch tile), the response-fields sentence in the API FAQ (repeated the tiles), the SDK list in the price
  block, the trust-FAQ sentence's retention clause (FAQ 5 carries it), "through the pharmacy's alternative route" in
  the comparison close (the accuracy block carries it). The accuracy intro's second sentence was replaced with a
  conclusion ("The pharmacy sets its mismatch threshold with that error in mind"). 1,672 → 1,595 visible words.
- Humanisation pass: detector CLEAN on the first run (no hard bans). "What still reads as machine-written?" answers
  and fixes: (1) value intro and card 1 said the same thing, rewritten; (2) two blocks opened "For an online pharmacy",
  one changed; (3) tile sentences all had the "X does Y, giving the prescriber Z" shape, varied; (4) the Admin Panel
  tile was a fragment with no verb, rewritten with a subject; (5) "Smart Scales" appeared without FitXpress at first
  mention, fixed. Meta description was 160 characters in the first draft, now 152.
- Render check in Chromium (Playwright, local server): first pass failed the hero (six-line H1 pushed the button below
  the fold at 1280×800; a hero grid override beat the mobile media query and squeezed the 375 layout). Fixed with a
  smaller H1 size scoped to this page and a desktop-only grid rule. Final: no horizontal scroll at 375 / 768 / 1280;
  hero complete at 1280×800; H1 and button above the fold at 375×667. Template caption contrast 3.95:1 raised to
  5.74:1. Screenshots saved: `screenshot-1280.png`, `screenshot-375.png`.
- Overlap check (6-gram shingles): BMI v7 6.4% (logo caption and data lines only; 94% of words unique), compliance
  guide 0.2%, GLP-1 v4 5.9% (data lines), fitness final 16.4% (template lines).
- Written: `fact-sheet.md`, `open-items.md` (27 items; #1 blocking: weight-accuracy figure vs roadmap), Phase 3 section
  in `gate-reports.md`. Not done here: blind judge (coordinator spawns it), handoff package, git, Slack.
- Inspo MCP not used.

## 2026-11-23: G-J round 1 (73/100) and round-2 fix pass

- Coordinator relayed blind judge round 1: 73/100, no hard fails, lowest Sales argument (9/15). Saved verbatim as
  `judge-round-1.json`.
- Coordinator rulings applied to page.md and page.html (kept in sync, checked word for word):
  1. one_fix declined (Vadim's live block order); fixed in place with a "See the patient flow in the demo" button after
     the patient cards, a "See a sample record in the demo" button after How it works, the record CTA as a "Book a
     demo" button, and a benefit on every record tile and on the RTPV step (no "fewer retakes": capture claims stay at
     the confirmed level).
  2. H1 → "FitXpress for online pharmacies: a live weight check before weight-loss prescribing".
  3. Lede and H2s with a named subject; no imperative openings.
  4. Patient cards rewritten as four patient benefits, hedged.
  5. Live capture made explicit: comparison row "Where the photos come from" plus one problem-block sentence.
  6. Manual forms named in one line under the comparison.
  7. Logo caption singular; GPhC February 2025 guidance PDF found through the review's own links, downloaded, read and
     linked; UK GDPR expanded and the data line made UK-specific; photos "within 30 days"; "internal study".
  8. Consultation questionnaire, GLP-1 (expanded), clinical team, compliance team, superintendent pharmacist; "pharmacy"
     29 → 20 in the visible copy; two-item lists in place of the three-item cadences.
  9. FAQ Q4 replaced (video consultations); Q1 rephrased around the pharmacy's own process.
  10. "Related pages" line after the FAQ (BMI feature page, telehealth); insurance and fitness not added.
  11. US spelling kept; question for Asel.
- Cuts to stay in budget: 1,719 → 1,593 visible words (comparison cells shortened, duplicated transfer sentence in FAQ
  5, the disability sentence's follow-on line, `/technology/` link, shorter hero micro-copy, FAQ answers tightened).
- Detector CLEAN on page.md and the visible copy; direct address 0; sentence mean 17.6.
- Re-rendered in Chromium: no horizontal scroll at 375 and 1280; hero button above the fold at both. Screenshots
  replaced.
- Updated: fact-sheet.md (guidance source, changed wording, CTA gaps), gate-reports.md (round-1 response),
  open-items.md (H1, spelling, method wording, roles, the guidance's own verification examples).

## 2026-11-23: G-J round 2 (71/100) and round-3 fix pass

- Coordinator relayed blind judge round 2 (a new judge): 71/100, no hard fails, lowest Conversion (6/10). Saved
  verbatim as `judge-round-2.json`. Last fix pass before the final round.
- Applied: the judge's one_fix (button "See the order flow in the demo" after the comparison); one anchor, `#demo` on
  the form section with a `#form` alias, every button pointing to it; comparison manual column rewritten so each form
  is described correctly; "body metrics" replaced; Smart Scales inputs stated (two live photos and the entered height)
  and the "route other than the patient's own answers" wording dropped; lede now leads with the pharmacy's outcome;
  pricing conclusion added; PMR, prescriber dashboard and order management named in step 3; "declared weight" used
  throughout; "BMI verification" once in FAQ 1 body copy; tile and step endings varied; FAQ: integration question with
  the API documentation link and an ownership question replaced the video-consultation and completion questions.
- Kept as conscious decisions: block order, no MHRA or CQC, USD prices, US spelling (open items).
- Cuts: the physical-disabilities limitation sentence (open item 16-r3), the line under the comparison, shorter tiles
  and steps. 1,689 → 1,594 visible words.
- Detector CLEAN on page.md and the visible copy; direct address 0. page.md and page.html in sync (scripted word diff).
  Re-rendered at 375 and 1280: no horizontal scroll, hero button above the fold at both; screenshots replaced.
- Updated fact-sheet.md, gate-reports.md, open-items.md (7a height dependence, 16-r3, 18b MHRA/CQC, 24a USD).

## 2026-11-23: correction before round 3

- Coordinator: restore the approved physical-disabilities limitation (a boundary sentence; Claims discipline deducts
  when a page drops one, length is deducted only past 1,700). Restored in page.md and page.html: the first sentence of
  `accuracy-formulations.md` §5 verbatim (checked by script against the canon file) plus "Those patients follow the
  pharmacy's alternative route." Nothing else cut.
- Visible copy 1,624 words. Detector CLEAN on page.md and the visible copy (no hard bans, no house-rule hits, no
  unexpanded acronyms, direct address 0). md/html sync check: no content differences (1,624 / 1,623, list numbering).
- fact-sheet.md source row added; open-items 16-r3 closed.

## 2026-11-23: G-J round 3 (75/100), gate not taken; post-round-3 correctness pass; Phase 6 handoff

- Coordinator relayed blind judge round 3 (a new judge): 75/100, no hard fails, lowest Sales argument. Saved verbatim
  as `judge-round-3.json`. Three rounds done (73 → 71 → 75): **gate not taken**, judging stops; publishing needs
  Vadim's explicit decision. page.md status `gate-not-taken-75`.
- Correctness pass (unscored), per the coordinator:
  - GPhC sentence now quotes the February 2025 guidance verbatim in two places ("the person's weight, height and/or body
    mass index"; "a different way to verify the information provided to them by the person"), cost right after,
    repeated closing sentence removed. The word "independently" itself hard-fails the detector's reserved-word check
    even in a quotation, so the guidance's own definition carries the qualifier (open item 17a).
  - Scope stated honestly: FitXpress adds one input (a weight estimate from live photos, calculated with the entered
    height); the pharmacy decides whether it meets its process; FAQ 2 keeps "height is not verified".
  - "Speaks to that last concern more directly" removed; "Results kept private" reworded as the pharmacy's choice of
    patient view; "weight management medicines" where the GPhC is cited; lede no longer keyword-stuffed.
  - Repetition cut (four "with no …" tails, value intro, pilot intro, the redundant comparison row, a clause in FAQ 1):
    1,624 → 1,589 visible words. No boundary sentence cut.
  - Schema: the five `mentions` @ids are not defined on their own URLs (checked live); the page now defines them as
    DefinedTerm nodes in the 3DLOOK Entity Inventory set, as the live insurance and fitness landings do.
- Detector CLEAN on page.md and the visible copy; md/html sync clean (1,589 / 1,588). Re-rendered at 375 and 1280, no
  horizontal scroll; screenshots replaced.
- Phase 6: `README.md`, `TODO.md`, `wordpress-notes.md` written (gate status first; blockers a-f; inbound links;
  template issues; nice-to-haves). fact-sheet.md, gate-reports.md and open-items.md updated.

## 2026-11-23: two post-round-3 changes at Vadim's request (unscored)

- Reorder: the scan-record block now sits right after the problem block, before How it works (value before mechanics;
  matches round 1's one_fix). Seams: weight tile shortened (the problem block already states photos plus entered height);
  band colours swapped; record block button "See a sample record in the demo", How it works button "Book a demo".
  Gaps at 1280×800: about 1,110 / 1,910 / 950 / 1,000 / 2,500 / 1,410 px; no two buttons within one screen.
- Online consultation option: step 1 now names checkout, a re-order, or during or straight after an online
  consultation; comparison closing says the scan and a video consultation can run together; new FAQ "Can the scan run
  during an online consultation?" replaced "How does FitXpress fit into the pharmacy's own verification process?"
  (answered by the problem block); FAQPage JSON-LD synced (four questions). Open item 6a for product (camera in use by
  the call app on the same phone).
- Pricing conclusion shortened to "Each scan is one API request, which means the plan follows the number of checks
  run."; comparison line tightened. Visible copy 1,596 words; detector CLEAN; md/html in sync; screenshots replaced.
- Updated README.md, TODO.md, wordpress-notes.md, fact-sheet.md, open-items.md, gate-reports.md.
