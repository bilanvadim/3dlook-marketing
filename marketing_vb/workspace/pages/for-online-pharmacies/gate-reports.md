---
product: fitxpress
type: vertical-page
vertical: online-pharmacies
status: gates
---

# Online pharmacies landing: intake, G-I, G-A (2026-11-09)

Decision (Vadim, 2026-11-09): the BMI verification page is a feature page that explains and routes, so online
pharmacies get their own selling landing, UK-led. Reverses the 2026-10-22 note that the BMI page supersedes a
pharmacy page (`landing-map.md`, `site-inventory.md` updated in 6988db2).

## Phase 0 · Intake

| Field | Answer |
|---|---|
| Page type | Use-case (vertical) page, vertical Kit |
| Product | fitxpress |
| Vertical | Online pharmacies and digital prescribers dispensing weight-loss medication; UK first (GPhC), written to work for EU later |
| Use-case file | `brand-assets/product-info/use-cases/fx-online-pharmacy-bmi.md` (exists) |
| Buyer | Head of Compliance & Risk, Head of Clinical Governance, Chief Pharmacist / Superintendent Pharmacist, Clinical Operations Director; product and CTO for integration (`icp-detail.md` §2) |
| Intent | BOFU. Traffic comes from outbound to UK pharmacies (profile `katerina`), sales follow-ups, the compliance-guide article and the BMI feature page, not from search (see G-I demand) |
| Place in the site | `/for-online-pharmacies/` at the root until `/fitxpress/` ships, then `/fitxpress/for-online-pharmacies/` (301), as with insurance |
| Conversion | "Book a demo", shared HubSpot form `FX \| LP \| Demo` at `#demo`, `fx_vertical` via GTM |
| Proof | UK Meds logo first in the shared logo row (logos approved 2026-10-21; no case study, no name in the copy); `proof-points.md`: under 45 seconds, weight ≈3.5% MAE under evaluated conditions; accuracy framework; trust FAQ |
| Language | English; UK regulatory context |

## G-I · Should this page exist

- [x] **Use-case file** exists.
- [x] **Cases:** standing FX waiver 2026-09-27 (logos only). UK Meds is the one production BMI-verification client; its
      logo goes first. `G-I: standing FX waiver 2026-09-27`.
- [x] **Five facts not on the parent (the BMI feature page):**
  1. GPhC distance-selling guidance (February 2025) requires independent verification of weight, height and/or BMI
     before weight-loss medication is supplied remotely (verified 2026-10-07, `for-glp-1-programs/sources-problem-block.md`).
  2. GPhC review (April 2026): 1,307 concerns from January 2024 to December 2025; inadequate BMI verification was the
     third most reported (11%), and the public raised easily manipulated photographs (same file).
  3. The order-flow pattern: the scan runs at checkout when weight-loss treatment is ordered; the patient sees "Your
     photos are submitted" and no body metrics; the prescriber reviews the result (`case-studies/uk-meds.md`, pattern B;
     described without naming the client).
  4. Re-order and refill checks: the same capture at each re-order, compared with the previous one (to confirm with
     product before it goes on the page).
  5. UK GDPR roles: the pharmacy is the controller, 3DLOOK the processor, with a DPA including SCCs and the UK Addendum
     (`compliance.md` §2).
- [~] **Demand.** Search demand from pharmacy buyers is effectively zero (Ahrefs 2026-11-09: GB "bmi verification" 0,
      "gphc weight loss" 0, "online pharmacy bmi" no data; US "bmi verification software" no data). The page is a
      conversion destination for outbound and sales, measured by demo requests, not organic traffic. Passes on that
      basis; recorded so the Phase 7 review measures the right thing.
- [x] **60% uniqueness against the BMI feature page:** achievable. The BMI page stays generic (how the feature works,
      methods, routing); this page carries GPhC, the order flow, prescriber review, re-orders and UK GDPR. Rule for both
      pages: the BMI page's pharmacy card does not retell GPhC.

**G-I: pass** (waiver + demand note).

## G-A · Architecture

- [x] **Parent, URL, siblings.** Parent `/fitxpress/` (not live) → root URL for now. Siblings: `/for-bmi-verification/`
      (feature page, links down here), telehealth, GLP-1 (planned), insurance. **Needs Vadim's OK.**
- [x] **Cannibalisation.** The compliance guide (`/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/`)
      already carries "Online Pharmacy BMI Verification" in its title and owns the informational intent. The landing
      does not use that phrase as its H1 or title head. With zero measured demand on every phrase, the risk is low in
      practice; the split is still kept clean.
- [x] **Inbound links named:** the BMI page's pharmacy card; the compliance guide (relink from `/for-bmi-verification/`
      when this ships); the landing-map row for pharmacy articles in any hub; UK outbound sequences.
- [x] **Search Console baseline:** new URL, none. The BMI page's baseline is in
      `workspace/pages/bmi-verification/keywords-2026-11-09.md`.

**Proposed angle:** a second, live-captured weight source inside the order flow, so the pharmacy can check
self-reported weight before a prescriber approves weight-loss medication, with a record for inspection. Lead with
compliance and defensibility, not accuracy (use-case file). Boundaries: the prescriber decides; "FitXpress is not a
medical device"; never "meets GPhC requirements" or "GPhC compliant".

**Proposed H1 (formula: product + audience + outcome):**
- A. "FitXpress for online pharmacies: check self-reported weight inside the order flow"
- B. "FitXpress for online pharmacies: a second weight source before weight-loss prescribing"

**Title draft:** "Weight & BMI Verification for Online Pharmacies | FitXpress" (59).

**Checkpoint (Vadim): URL, angle, H1, and who drafts (Nika as on other use cases, or page-builder here).** 2026-11-09: «ок» → URL and angle approved; H1 and drafter still open.

---

# Phase 3 · Build (2026-11-23, page-builder)

Inputs fixed before the build (coordinator brief, Vadim 2026-11-09 and 2026-11-23): URL and angle approved; H1 =
option B (Vadim confirms at the final checkpoint); build the whole page; (1) no competition with the articles, the BMI
feature page or the GLP-1 landing; (2) structure as close as possible to the live fitness landing.

## Non-competition matrix (requirement 1)

| Owner | What it owns | What this landing does | Check |
|---|---|---|---|
| Article "Online Pharmacy BMI Verification: A 2026 Compliance Guide" (`/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/`) | Informational intent; the phrase "online pharmacy BMI verification"; GPhC rules in depth; camera-roll and generative-AI risk; capabilities list (live capture, liveness, clothing, cross-check, session records); the vendor procurement checklist; telehealth remote BMI verification; UK BMI thresholds for Mounjaro/Wegovy (content-plan row, Section-first there) | One regulatory paragraph (problem block: the February 2025 guidance in one sentence, two GPhC review figures, one cost sentence) and a link to the guide right under it, plus the guide as the form's soft exit. The phrase appears only as the guide's link label, never in the H1, title or meta. No BMI thresholds, no drug names, no capability list, no procurement checklist, no telehealth | 6-gram overlap of the copy with the live guide: 0.2% |
| BMI verification feature page (live `/for-bmi-verification/`; Asel's v7 `workspace/pages/bmi-verification/asselya-v7-2026-11-12.txt`) | "BMI verification · remote BMI verification · weight and BMI verification"; what BMI verification is; how the feature works (capture → compare → route); the outputs explained (predicted weight, BMI formula, comparison and routing); the illustrative BMI cross-check mock; "Live capture. No photo uploads." with liveness "coming soon"; "BMI verification methods compared" (self-report, Smart Scales, video consultation, calibrated scale; criteria data source and user requirements / output and appropriate use); vertical routing cards; FAQ (physical scale?, mismatch = fraud?, approves eligibility?, cannot complete capture, progress tracking) | No "BMI verification" head in H1 or title; the feature is not re-explained: the value block sends "the feature behind the check" to the BMI page with its anchor "remote BMI verification", and the pilot block links it as "BMI-verification". The record block names outputs in order-record terms (no BMI formula, no comparison-and-routing card). The hero mock is an order timeline with no body values, not a cross-check. No live-capture/no-upload section and no liveness. The comparison has different rows (FitXpress in the order flow vs manually reviewed evidence) and different criteria (where the check sits, what the patient does, what the prescriber gets, what the order record keeps, at a re-order). None of the five FAQ questions repeats a v7 question | 6-gram overlap with v7: 6.4%, all of it in the shared logo caption and the five data lines (template lines, identical on every FX landing). Paragraph-level: 94% of words unique against v7 |
| GLP-1 landing `/fitxpress/for-glp-1-programs/` (approved, not live; `nika-v4-2026-10-13.txt`) | Body-composition tracking between clinic visits; progress and muscle-loss monitoring; retention | Verification at the order and re-order step only. Re-order wording is "a current estimate for each supply", with no comparison to earlier scans and no progress language. No body measurements, body composition, 3D model or Pro-plan progress features on the page (Pro is listed by volume only) | 6-gram overlap with v4: 5.9% (data lines) |
| GLP-1 / weight-loss articles (glp-1-market hub, top-7 remote body composition tools, visual-progress-tracking, glp-1-compliance-challenge) | Their topics | Not linked and not covered | — |
| Telehealth landing `/structured-body-data-for-telehealth-digital-health-programs/` | Telehealth workflows | One sideways link from the pilot block ("weight-management"), as on the fitness landing. No telehealth content | — |

**Primary phrase:** `weight checks for online pharmacies` (commercial, pharmacy-specific; not in any owner's anchor list
above; zero measured search demand, like every phrase in G-I, so it exists to keep the split clean and to give
articles a distinct down-link anchor). Proposed anchors for `landing-map.md` when the page ships: weight checks for
online pharmacies · FitXpress for online pharmacies · weight check before weight-loss prescribing.

**Title:** `Order-Flow Weight Checks for Online Pharmacies | FitXpress` (58). The G-A title draft "Weight & BMI
Verification for Online Pharmacies | FitXpress" was dropped: it puts "BMI Verification" at the head of the title,
which requirement 1 forbids. **Meta description:** 152 characters, carries the primary phrase.

**H1 kept** as option B. It names product, audience and outcome; it carries "online pharmacies" and "weight" but not
the exact primary phrase, which sits in the lede's second sentence, the title and the meta description. No gate forced
a change.

## Template mapping (requirement 2): live fitness landing → this page

| Live fitness block (2026-11-23) | This page | Status and reason |
|---|---|---|
| H1 + lede, proof strip, logo row | H1 option B + two-sentence lede (outcome first, FitXpress in sentence 2), four-fact strip (2 photos · Under 45 sec · Order and re-order · No integration fee), logo row with UK Meds first and caption "…including online pharmacies." | Kept. Hero mock adapted: an order timeline (no body values) in place of the fitness progress record, to stay clear of the BMI page's cross-check mock. H1 type size reduced so the hero stays complete at 1280×800 |
| H2 "Body data for member check-ins" + 4 value cards (H3) + in-depth link | "For patients": H2 "A weight check patients finish while they order" + 4 cards + "The feature behind the check: remote BMI verification →" | Kept. The in-depth link goes to the BMI feature page (it owns the feature explanation); the compliance-guide link moved down to sit under the regulatory paragraph, as requirement 1 asks |
| H2 problem as a question + 2 stats + cost sentence | "Why does self-reported weight put online pharmacies at risk?" + GPhC sentence + 1,307 / 11% + cost sentence + guide link | Kept. One shared source line for both figures (same GPhC review) |
| H2 "The scan runs inside check-ins the program already has" (3 steps + recommended setup) | "The check runs inside the order flow the pharmacy already has" (3 steps + recommended setup + /technology/ link) | Kept. Voice prompts dropped (native iOS/Android voice guidance is "in testing" per roadmap.md) |
| H2 "Each scan reveals changes beyond weight" + 5 output tiles (H3) | "Each scan adds a second weight source to the order record" + 5 tiles (Weight estimate · Mismatch flag · Calculated BMI · Status and timestamps · Admin Panel) + boundary sentence + "See a sample record in the demo" | Adapted: pharmacy outputs instead of measurements, body composition, BMR and 3D tools (GLP-1 / fitness territory). Admin Panel tile added (roadmap: Live). Follows the live order (workflow before outputs), which differs from the Kit's "What you get before How it works"; the value cards still come before the mechanics |
| H2 "FitXpress compared with …" (table, cards on mobile) | "FitXpress compared with manually reviewed weight evidence" (2 options × 5 operational rows; cards under 960 px) + closing | Adapted, not dropped: the BMI page owns the methods comparison, so the rows and criteria are the pharmacy's operational decision (where the check sits, patient effort, what the prescriber gets, what the order record keeps, re-order) |
| H2 "How accurate is FitXpress, and how is member data handled?" + figures + method + 5 data tiles + trust-FAQ sentence | "How accurate is the weight estimate, and how is patient data handled?" + one figure (3.5% weight estimate) + method + population limitation + 5 data lines + trust-FAQ sentence | Adapted: body-measurement figures (96-97%, < 1 cm) dropped because the page's job is weight; FDA dropped from the trust-FAQ sentence (UK page), medical-device status kept. Weight figure carries an open item (roadmap conflict, `open-items.md` #1) |
| H2 pilot + pricing (Walkthrough, Pilot cohort, Evaluate and roll out, "3DLOOK and the platform track:") | "Start with a share of weight-loss orders, then scale on a fixed monthly plan": Starter and Pro lines from live /pricing/, the three steps, "3DLOOK and the pharmacy track:" | Kept. Pilot keeps the pharmacy's existing verification on every order; Pro listed by volume only (its added features are progress tools) |
| H2 FAQ (6 questions as H3) | "Questions online pharmacy teams ask" (5 questions as H3) | Kept, 5 within 4-6; none repeats the body or the BMI page FAQ; one links the API documentation |
| Demo form | "See FitXpress in the order flow" + soft exit to the compliance guide + shared form | Kept; `#form` (live template anchor) with a `#demo` alias |

**Kit slots dropped:** 10 (cases from this vertical) and 11 (customer quote): standing FX waiver, logos only, UK Meds
unnamed in the copy. 16 (sibling-vertical cards): the fitness template has none; sideways links sit in the body
(BMI feature page, telehealth). 12 (integration formats): folded into the steps, as on the fitness page.

## Detector and register (Phase 3 pass 3)

`detect-ai-tells.py --channel page --summary` on `page.md` and on the extracted visible copy: **CLEAN**, no hard bans,
AI density 0.0 per 1,000, no house-rule violations, no punch triads, no "vs" headings, no unexpanded acronyms (GPhC is
not caught by the regex; expanded by hand at first use), H1 names the product. Direct address: 0 per 1,000. Visible
copy: 1,595 words (fitness final by the same count: 1,570). Sentence mean 18.5 words (fitness final 19.1).

## G-T, builder's part (Phase 4)

- [x] Canonical to self in the prototype; title 58 ≤ 60; description 152 ≤ 155; one H1
- [x] Schema written: WebPage (Yoast `@id`), Service with `audience` + `areaServed` (UK), FAQPage (5, answers checked
      byte-identical by script), BreadcrumbList (two levels). JSON parses; validator.schema.org not run
- [x] Viewports 375 / 768 / 1280 checked in Chromium: no horizontal scroll; hero complete at 1280×800; H1 and
      primary button above the fold at 375×667; comparison turns into cards under 960 px. 1440 not checked
- [x] Contrast computed for every token pair used; template captions raised from 3.95:1 to 5.74:1
- [x] Alt text on all logos (client name); the hero mock is HTML, captioned "Illustrative example"
- [x] `fact-sheet.md` written
- [ ] Indexable / sitemap / inbound links: on publish
- [ ] Analytics events verified firing: on publish (GTM `fx_vertical` lookup row needed)
- [ ] Performance: not measured (prototype)

---

# G-J round 1 and the round-2 fix pass (2026-11-23)

**Round 1 (blind judge, spawned by the coordinator): 73 / 100, no hard fails, lowest axis Sales argument (9/15).**
Saved verbatim as `judge-round-1.json`. Points lost: proof of belonging 11/15, claims 12/15, sales 9/15,
uniqueness 8/10, conversion 8/10, buyer language 8/10, human copy 7/10, search 7/10, place and technical 3/5.

**one_fix not applied as written (coordinator ruling 1).** The judge asked to move the scan-record block above "How it
works" and to turn its tiles into a two-column table. Vadim's requirement 2 is the live fitness block order, where the
workflow comes before the outputs and the outputs are tiles. The same weakness was fixed in place:
- **CTA gap:** a button ("See the patient flow in the demo") at the end of the patient block, a button ("See a sample
  record in the demo") at the end of How it works, and the record block's CTA turned into a "Book a demo" button. At
  1280×800 the gaps between buttons after the hero are now about 1,160 / 1,800 / 960 px (was one gap of about
  2,870 px). The comparison and accuracy blocks still run about 3,460 px to the pilot button, as on the fitness
  template.
- **Value before mechanics:** each record tile and the RTPV step now carry what they spare or settle (second figure
  without asking the patient for more evidence; flag points prescribers to orders where weights disagree; BMI without a
  manual calculation; a dated entry for inspection; failed-scan messages and photo-deletion dates without manual
  chasing; staff spared from coaching each capture). "Fewer retakes" was not used: the confirmed capture level
  (Kit, fitness final) excludes retake claims.

**Other rulings applied (2-11):**
- **H1 changed** to "FitXpress for online pharmacies: a live weight check before weight-loss prescribing" (ruling 2):
  carries "weight check" and "online pharmacies"; the focus keyphrase stays in the title, meta and the lede's first
  sentence. Vadim confirms at the final checkpoint.
- Lede and H2s carry a named subject (ruling 3): lede opens "FitXpress runs weight checks…"; "A pilot starts on a
  share of weight-loss orders, then scales on a fixed monthly plan"; "The demo shows FitXpress in the order flow"; the
  trust-FAQ sentence no longer opens with "See".
- Patient cards are patient benefits only, hedged (ruling 4): No appointment to book · On their own phone · Body
  numbers kept private · Simpler re-orders ("where the pharmacy's rules allow … can replace a separate request for
  evidence").
- The live-capture argument is explicit (ruling 5): comparison row "Where the photos come from" and one sentence in
  the problem block ("A photo taken live during the order speaks to that last concern more directly than one sent in
  later"). No "no gallery upload" or "cannot be edited" claim.
- Comparison names the usual manual forms in one line under the table ("a scale photo, a video consultation or
  clinical records"), not as rows (ruling 6).
- Claims (ruling 7): logo caption "including an online pharmacy"; the GPhC February 2025 guidance is now linked
  directly (PDF verified 2026-11-23, found through the review's own links) and paraphrased from its own text; UK GDPR
  expanded and the data line made UK-specific (DPA with SCCs and the UK Addendum, then the canonical role sentence);
  photos "within 30 days"; "internal study" replaces "internal validation".
- Buyer vocabulary (ruling 8): "consultation questionnaire", "glucagon-like peptide-1 (GLP-1) treatments", clinical
  team, compliance team, superintendent pharmacist and compliance lead used where accurate; three-item cadences in the
  walkthrough and form text cut to two. "Pharmacy" in the visible copy: 29 → 20.
- FAQ (ruling 9): Q4 "How do scan results reach the prescriber?" replaced by "Can the scan sit alongside video
  consultations?"; Q1 rephrased to "How does FitXpress fit into the pharmacy's own verification process?". The API
  documentation link moved to the recommended-setup line; the `/technology/` link there was dropped for length.
- Place in the site (ruling 10): a "Related pages" line after the FAQ (remote BMI verification · remote body measurement
  for telehealth). Insurance and fitness not added: neither reads naturally for a pharmacy buyer. No up-link while
  `/fitxpress/` is not live (fact sheet).
- US spelling kept (ruling 11), question for Asel in `open-items.md`.

**Non-competition re-check for the new copy.** The new FAQ on video consultations is operational (where the pharmacy
routes flagged orders and patients who cannot scan) and does not compare methods; the one-line list of manual forms
names three forms without rows or criteria, so the BMI page's methods comparison stays unrepeated. FAQ Q1 no longer
explains GPhC; the compliance guide keeps that. No BMI thresholds, drug names beyond the GLP-1 class, or progress
language were added.

**Detector and length after round 2:** `detect-ai-tells.py --channel page` CLEAN on page.md and on the visible copy (no
hard bans, no house-rule hits, no unexpanded acronyms, no punch triads). Direct address 0 per 1,000. Visible copy 1,593
words. Sentence mean 17.6 (was 18.5). page.md and page.html copy checked word for word (1,593 / 1,592, the difference is
list numbering).

---

# G-J round 2 and the round-3 fix pass (2026-11-23)

**Round 2 (a new blind judge): 71 / 100, no hard fails, lowest axis Conversion (6/10).** Saved verbatim as
`judge-round-2.json`. Proof 11/15, claims 12/15, sales 11/15, uniqueness 7/10, conversion 6/10, buyer language 7/10,
human copy 7/10, search 7/10, place and technical 3/5. This is the last fix pass before the final round.

**Applied (coordinator rulings):**
1. **one_fix applied:** button "See the order flow in the demo" after the comparison's closing line. One anchor
   everywhere: the form section is `id="demo"` (Kit and landing-map); `#form` stays as an alias for the live
   template. All seven buttons, including the prototype header, point to `#demo`. Gaps between buttons at 1280×800
   are now at most about 2,420 px (accuracy block to the pilot button).
2. **Claims:** (a) the comparison's manual column now names each form correctly ("a scale photo the patient sends, a
   video consultation or clinical records"; "Sends a photo, joins a call or agrees to a records check"), and the line
   under the table was folded into the row; (b) "body metrics" replaced ("weight and BMI"); (c) Smart Scales inputs
   stated: the estimate comes from the two live photos and the height the patient enters (weight tile, FAQ 2); "a
   route other than the patient's own answers" removed from the GPhC sentence; product open item added; (d) BMI stays
   unexpanded (house list), noted in the fact sheet.
3. **Sales:** the lede now leads with the pharmacy's outcome, hedged ("Each weight-loss order can reach the prescriber
   with a dated weight estimate from photos taken live during the order, and the pharmacy can keep that record for
   inspections and concerns"), then FitXpress and the how. A pricing conclusion: "Each scan is one API request, which
   means the plan follows the number of orders and re-orders that run the check." H1 unchanged.
4. **Buyer language:** step 3 names the pharmacy's systems (patient medication record (PMR), prescriber dashboard,
   order management); "declared weight" is the one term for the patient's figure (problem H2 now "Why does declared
   weight put online pharmacies at risk?"; schema outputs aligned); the subjectless FAQ opening is gone; "BMI
   verification" appears once in body copy (FAQ 1, "the weight part of the pharmacy's BMI verification process"),
   never in H1, H2s, title or meta.
5. **Human copy:** the five tiles and step 2 no longer share the "giving / pointing / sparing" tail; openings vary
   (subject-first, "The clinical team sets…", "Failed-scan messages … sit in…", "Every record carries…").
6. **FAQ:** the video-consultation fallback replaced by "How does FitXpress connect to the pharmacy's checkout?" (links
   the API documentation, as the Kit requires); the completion FAQ that restated the pilot replaced by "Who owns the
   scan results?" (`compliance.md` §6). The API link left the recommended-setup line.
7. **Place in the site:** "Related pages" keeps the BMI page and telehealth; fitness and insurance not added (no
   natural reason for a pharmacy buyer), reason recorded in the fact sheet.

**Not changed, as conscious decisions (ruling 8):** block order (Vadim's template requirement); no MHRA or CQC context
(neither is in the canon sources for this page; open item for Whitney and Asel); USD prices (the live `/pricing/` is
USD only; open item); US spelling (open item for Asel).

**Cuts to hold the budget:** the physical-disabilities limitation sentence (canon, optional; the comparison keeps the
manual route for patients who cannot scan), the line under the comparison, the API link in the recommended setup,
shorter tiles, step 3, walkthrough, evaluate step and form text. 1,689 → 1,594 visible words.

**Non-competition re-check:** the comparison names three manual forms inside one cell and one patient-action cell, with
operational criteria only; nothing repeats the BMI page's methods rows or criteria. "BMI verification" appears once in
body copy, as the buyer's term, outside every heading and Yoast field. No GLP-1 progress language; no GPhC explainer in
the FAQ.

**Detector and length after round 3:** `detect-ai-tells.py --channel page` CLEAN on page.md and the visible copy (no
hard bans, no house-rule hits, no unexpanded acronyms, no punch triads). Direct address 0. Visible copy 1,594 words;
sentence mean 18.7. page.md and page.html checked word for word (1,594 / 1,593, list numbering).

---

# G-J round 3 and the end of judging (2026-11-23)

**Round 3 (a new blind judge): 75 / 100, no hard fails, lowest axis Sales argument (11/15).** Saved verbatim as
`judge-round-3.json`. Proof 12/15, claims 12/15, sales 11/15, uniqueness 7/10, conversion 8/10, buyer language 8/10,
human copy 7/10, search 7/10, place and technical 3/5.

**Gate status: NOT TAKEN — 75/85 after three blind rounds (73 → 71 → 75), weakest axis Sales argument.** Per the
skill, judging stops after three rounds; publishing requires Vadim's explicit decision.

## Post-round-3 fixes, unscored (coordinator's correctness pass)

1. **GPhC sentence now follows the February 2025 guidance as read in the PDF**, qualifier included: "Since February
   2025, General Pharmaceutical Council (GPhC) guidance has said that, when supplying weight management medicines such
   as glucagon-like peptide-1 (GLP-1) treatments, the prescriber verifies "the person's weight, height and/or body
   mass index" using "a different way to verify the information provided to them by the person". An order supplied on
   declared weight alone is therefore a prescribing decision the pharmacy may have to defend at inspection or in
   answer to a concern." The judge's one_fix shape was applied (cost right after the rule; the repeated closing
   sentence removed). The regulator's word "independently" is rendered through its own definition, because
   `detect-ai-tells.py` hard-fails "independently verif" as a reserved word even inside a quotation (open item for Asel:
   a regulator-quotation exception).
2. **Scope made honest** after the GPhC figures: "FitXpress adds one input to that check: a weight estimate from photos
   taken live in the order flow, calculated with the height the patient enters. Whether that estimate, alone or with
   other checks, meets the pharmacy's process is the pharmacy's decision." FAQ 2 keeps "Does FitXpress verify the
   patient's height? No." "Speaks to that last concern more directly" was removed; the plain fact that photos are taken
   live stays.
3. **"Results kept private" reworded** as the pharmacy's choice: "A short confirmation screen. The pharmacy decides what
   patients see after the scan, for example only a confirmation that the photos are submitted."
4. **"Weight management medicines"** (the GPhC's term) where the regulator is cited; "weight-loss" kept elsewhere.
   Lede no longer reads keyword-stuffed: "FitXpress adds this weight check to the online pharmacy's order flow, on the
   patient's own phone." The exact focus keyphrase now sits in the title and meta description only.
5. **Repetition cut, no boundary sentences cut:** the four "with no …" tails (patient card, RTPV step, weight tile, BMI
   tile), the value-block intro line, the pilot intro sentence that repeated the tracking list, the comparison row
   "What the patient does" (repeated "Where the evidence comes from"), and the clinical-team clause in FAQ 1. 1,632 (the
   judge's count) / 1,624 (ours) → 1,589 visible words.
6. **Schema `mentions`:** the five @ids (Smart Scales, BMI, BMI verification, RTPV, accuracy) are not defined on their
   own URLs (checked live 2026-11-23); the live insurance and fitness landings define them inline. This page now does
   the same: `DefinedTermSet` "3DLOOK Entity Inventory" plus five `DefinedTerm` nodes, definitions from
   `docs/schema-entities.csv`. Every `mentions` @id resolves inside the graph.

Detector after the pass: CLEAN on page.md and the visible copy (no hard bans, no house-rule hits, no unexpanded
acronyms, direct address 0). page.md and page.html checked word for word (1,589 / 1,588, list numbering). Re-rendered
at 375 and 1280: no horizontal scroll, hero button above the fold at both.

**Round-3 judge points not addressed (no ruling, listed in `TODO.md` as nice-to-have):** H1 states the product, not
the paid-for outcome; FAQ H3s are brand-phrased; siblings are a text line, not cards; the demo block does not say what
happens after submission (HubSpot Meetings opens); button gap of about 2,500 px across the accuracy block; no
vertical figure in the hero.

## Post-round-3 changes at Vadim's request, unscored (2026-11-23)

**1. Block order now value-first (Vadim: «постав результати вище а потім хау іт воркс якщо це краще для сейл»).** The
scan-record block (`#record`: H2, intro, five tiles, boundary sentence, button) moved from after How it works to
directly after the problem block. This matches round 1's one_fix and the Kit's "Sell, not educate" rule 2 (value before
mechanics). It departs from the live fitness landing, which keeps How it works before the outputs; the same change
could be proposed there. Seams fixed: the weight tile no longer repeats the problem block's scope sentence ("estimates
weight from the photos and the entered height"); the record block uses no term that How it works introduces later
(no SDK, API, PMR or scan identifier); the boundary sentence stays under the record tiles. Band colours re-alternated
(record white, How it works light). Buttons: the record block carries "See a sample record in the demo", How it works
carries "Book a demo"; gaps at 1280×800 are about 1,110 / 1,910 / 950 / 1,000 / 2,500 / 1,410 px. Without either
swapped-block button a gap of about 1,900 or 2,860 px would open, so both stay, and no two buttons sit within one
800 px screen.

**2. Scan during an online consultation, as an option (Vadim: «наша фото оцінка може проходити під час онлайн
консультації як варік»).** Canon basis: `tech-spec.md`, scan entry point "trigger from any flow". Changes:
- Step 1: "The patient scans where the pharmacy places the check. That can be checkout, a re-order, or during or
  straight after an online consultation, with consent and instruction screens in the pharmacy's own wording."
- Comparison closing: "Manual review still suits patients who cannot complete the scan, and the two can run together:
  the scan can sit during or straight after a video consultation." (the table no longer reads as replacing video
  consultations only)
- New FAQ "Can the scan run during an online consultation?": "Yes, as one placement the pharmacy can choose. The patient
  takes the two photos on their own phone during or straight after the consultation, and the prescriber can see the
  result in the same session. The prescriber still decides, and the pharmacy judges whether the combined check meets
  its process."
- Removed FAQ "How does FitXpress fit into the pharmacy's own verification process?" (the problem block's scope
  sentence answers it; four FAQs remain, within 4-6). The FAQPage JSON-LD was updated to match.
- Not claimed: that a scan during a consultation meets GPhC requirements or counts as video verification; any call
  integration, live video analysis or video-platform connection. "During or straight after" is used until product
  confirms the camera question (open item 6a).

Visible copy 1,596 words. Detector CLEAN on page.md and the visible copy. page.md and page.html in sync (scripted word
diff). Re-rendered at 375 and 1280: no horizontal scroll; hero button above the fold at both; screenshots replaced.
