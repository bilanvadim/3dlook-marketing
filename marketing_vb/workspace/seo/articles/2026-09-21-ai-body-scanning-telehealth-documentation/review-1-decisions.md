---
review: review-1.md (Doc 1mvt73JNvyKWW-ALzokJKWnf0kOG5kUWaeUnfvUjOzrE, tab "Review 1", fetched 2026-11-23)
reviewer: Asselya Sekerova
base_text: v1/final.md (= the Doc tab "Version 1", identical; the page is NOT published: /content-hub/telehealth-documentation-ai-body-scanning/ returns 404 on 2026-11-23)
decided_by: coordinator (new-article.md review procedure), checked against brand-assets/ and the live pages listed in §V
rule: THIS FILE WINS over review-1.md wherever they differ, and over plan.md for the H1, headings, CTA count and section content.
type: EDIT round. Section order stays. One H1 change, one H2 rename, the product section rewritten into two H3s, additions in S2, S4, S7, S8, the pilot section and the FAQ. plan.md is not regenerated.
word_target: about 2,150-2,300 prose words (v1 1,867; plan target 2,100). The additions are required by the review; pay for them by cutting repetition, not by cutting required content. Do not touch S3 ("Why record consistency is under pressure now") beyond what the gates need.
next: seo-editor -> seo-publisher (meta.md + article_package.py assemble) -> quality-controller -> editor fix pass on QC findings
---

# Review 1: decisions

Status words: **ACCEPT** = do what the review says. **ACCEPT, CHANGED** = do it with the change
written here. **REJECT** = do not do it, with the reason. **KEEP** = no change. **VERBATIM** = use
these exact words. Where this file gives text in a quote block, that text is the instruction. Do not
paraphrase it.

New claims for this round are in the context pack as FX-013 to FX-016 (added 2026-11-23 by the
coordinator from the sources in §V). Every new product sentence carries a `<!-- claim: FX-0NN -->`
marker, as in v1.

Actor naming (terminology-guardrails §2.12 and §2.14): "the program" stays the default actor, as in
v1. "Customer" only where it names a contractual relationship, a deployment responsibility or a legal
role (agreements, retention instructions, GDPR roles, who controls integration and patient
association). Never "organization" as a default. The reviewer asks for no vague pronouns: every
sentence about responsibility names FitXpress, 3DLOOK, the program or the clinical team.

## A. Title: ACCEPT, VERBATIM.

- H1 becomes: "How AI Body Scanning Supports More Consistent Telehealth Documentation".
  Also the frontmatter title, if final.md has one.
- Byline stays: "By Assel Sekerova".
- Checked: landing-map rule 3 forbids the Hub 2 landing's primary keyword ("remote patient
  monitoring for weight loss") in the title, H1 and meta title. The new H1 does not contain it.
  The primary keyword "telehealth documentation" stays in the H1.
- Slug KEEP: `telehealth-documentation-ai-body-scanning` (approved 2026-09-21; the page is not
  live, but the reviewer did not ask to change it).

## B. Early landing link: ACCEPT, VERBATIM.

- Directly after the scope note, as its own paragraph (keep the scope note exactly as it is, it is
  the clinical boundary the review asks to retain):

  > For telehealth teams standardizing remote intake, [FitXpress supports structured body-data collection and repeat measurement](https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/) through a guided smartphone capture flow, API/SDK integration, and optional scan-management tools.

- This paragraph is the article's **early CTA** (`blog-style-guide.md` §5, two CTAs per article,
  Vadim 2026-11-23) and its landing-map rule 1 down link, at about 15% of the body.
- Format note: §5 describes the early CTA as a short block followed by a link with an action
  label. The reviewer wrote this sentence with the link inside it, and we keep her words. Do not add
  a separate action-label line under it: it would repeat the same link two lines apart.
- "API/SDK" stays as written: API and SDK are expanded later, in the product section, where v1
  expands them. If gate M1 fails because "API/SDK" now comes before the expansion, expand the
  terms at this first use and record that in editor-report.md. Change nothing else in the sentence.
- The landing-map rule 2 keyword anchor goes on the contextual link in E1, not here.

## C. Short answer (S2), structured body data: ACCEPT, CHANGED to canon wording.

- Keep the three groups and the order.
- "What the person submits": KEEP.
- "What the scan generates" lists: 80+ body measurements, a 3D model, applicable BMI- and
  weight-related metrics, body composition estimates, and Body Progress comparisons between two
  scans the program selects. <!-- FX-002, FX-005, FX-016 --> The next paragraph keeps v1's
  distinction (measurements are circumferences, lengths and widths; BMI and BMR are calculated;
  body composition figures are estimates). Do not call every generated value a measurement.
- "What the system records technically": KEEP v1's list (it is `compliance.md` §3 verbatim), then
  add one sentence that not every technical field appears in every API response, in the Admin
  Panel, or in the program's own record. Do not say which fields appear where: product has not
  confirmed it (§V, open question 2).
- Processing time: KEEP v1 "in under 45 seconds". It matches the reviewer's "under 45 seconds"
  and `tech-spec.md` (the only public timing definition). Do not add "typically", "processing only"
  or any other variant.

## D. Telehealth workflow (S4): ACCEPT.

- The three H3s stay: At intake · Between visits · Before clinician review.
- Add, once in this section (the section lead or the end of "Between visits"), that the program
  controls scan scheduling, the integration, which patient a scan belongs to, its documentation
  requirements, and clinical review. <!-- FX-016 -->
- In "Between visits", state: Body Progress compares two scans the program selects, by their scan
  IDs. FitXpress does not keep a patient timeline, and 3DLOOK does not determine that two scans
  belong to the same person (`compliance.md` §4: "the program compares scans it selects"; never
  "FitXpress tracks each patient over time"). One negation per sentence.

## E. Product section (S5): ACCEPT, rewrite into two H3s.

H2 KEEP: "Where FitXpress fits: capture, records, and the Admin Panel". Under it, a two-sentence
lead (the two capabilities complement each other; API/SDK integration is the primary route), then:

### E1. H3 "API/SDK integration"

- Guided remote body-data capture inside the program's own application. <!-- FX-001 -->
- Structured outputs come back through supported interfaces (API, SDK). Keep v1's first-use
  expansions "application programming interface (API)" and "software development kit (SDK)" unless
  B forced them earlier.
- The customer decides how scan results map into its own record systems. Say plainly that
  connecting results to an electronic health record (EHR) or updating a medical record is the
  program's integration work. Do not promise automatic EHR integration or record updates.
- Contextual landing link (the reviewer's "mid-article" touchpoint, J): one in-sentence link with
  the landing-map rule 2 anchor **"body scanning API for telehealth platforms"** →
  https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/ . It replaces v1's
  link "structured body data for telehealth and digital health programs" in this section. It is an
  internal link, not a CTA block (no button label, no "book a demo" here).

### E2. H3 "FitXpress Admin Panel"

- Canon line first (`tech-spec.md`, Vadim 2026-09-23): an optional, complementary interface for
  monitoring and exporting results. It does not replace API/SDK integration. Add: it does not
  replace an EHR either.
- Publicly documented features (FX-013, from the live launch post). A short list is fine here, at
  most 7 bullets:
  - centralized access to scans made with the customer's API keys
  - scans separated by API-key environment (for example, primary and sandbox keys)
  - scan statuses: Success, Failed, Pending
  - sorting and filtering of scan records
  - individual scan details with measurement information
  - CSV export of selected records
  - API key, scan allowance and subscription details
- Do NOT name the other environment tabs from the launch post: they carry client or integration
  names (rule: no client names in content).
- Do NOT mention the Clothes Detector results the launch post shows in the scan view:
  `roadmap.md` keeps clothing information at the 2026-10-07 safer level until release.
- Availability (FX-014), qualified: the first version is available to selected FitXpress clients,
  with credentials provided by the 3DLOOK team, and there is no public sign-up.
- Link: [the FitXpress Admin Panel launch post](https://3dlook.ai/content-hub/fitxpress-admin-panel-launch/)
  (v1 anchor "FitXpress Admin Panel launch post" may stay or be reworded; not exact-match with
  any other anchor).

Keep v1's point that both routes leave a retrievable record with a timestamp, but say it once.

## F. Comparison table (S6): ACCEPT. Rename the H2.

- H2: v1 "What changes in the record" is too close to the banned "What changed" heading
  (review §3). New H2: **"Fragmented inputs and structured records, side by side"**. Avoid
  "change/changes/changed" in this heading.
- Keep the table, both columns, all six rows. Rewrite the structured-record column:
  - Fields on each entry → "Consistent fields when scans use the same successful capture configuration"
  - Timestamp → "A timestamp associated with each scan record"
  - Format → keep "Structured outputs in one shape"
  - Availability before review → "Available once the scan completes and the program's integration or retrieval brings it into the record"
  - Manual re-entry → "Can be reduced where the integration transfers the required fields"
  - Comparison across time points → "Possible between records the program selects, under a consistent capture protocol"
- The paragraphs under the table: no efficiency claim. v1's "quicker to read" goes; keep the hedge
  that any gain depends on how much was missing before. Keep the recalculation sentence (each
  entry shows the figures from that day).

## G. Limitations (S7): ACCEPT.

- KEEP v1's three paragraphs. Make sure the section says FitXpress is not a medical device, not a
  clinical diagnostic tool, and not a substitute for clinician assessment; not equivalent to DXA,
  BIA or calibrated scales where those methods are required; and does not independently make
  high-impact decisions (diagnosis, treatment, insurance eligibility, trial participation,
  employment). Most of this is in v1 already (FX-006); add only what is missing.
- Add one sentence: using FitXpress does not by itself make a program's workflow compliant with
  HIPAA, GDPR or telehealth documentation rules; compliance stays with the program and its
  advisors. ("HIPAA compliant" as a status is banned by `compliance.md` §1; this sentence denies
  it, which is allowed.)

## H. Privacy and data handling (S8): ACCEPT, CHANGED to canon wording.

- Open the section with the photo vs output split (FX-015): photos are deleted immediately after
  processing or within 30 days, according to the customer agreement and the customer's
  instructions. Use "within 30 days" (`compliance.md` §3), not "up to 30 days".
- KEEP v1: outputs retained on an ongoing basis unless the agreement or a deletion request says
  otherwise; deletion of specific scan outputs by scan identifier; anonymized, randomly generated
  IDs, 3DLOOK cannot identify a specific individual from stored scan records; HIPAA/BAA sentence;
  the GDPR sentence VERBATIM ("In most enterprise deployments, the customer acts as the data
  controller and 3DLOOK acts as the data processor under GDPR.").
- KEEP the link to the privacy FAQ. No certification claims (no SOC 2, ISO, "HIPAA compliant").
- `compliance.md` says articles link to the FAQ instead of restating it, so add only the photo
  sentence. Keep the section near its v1 length.

## I. Pilot evaluation: ACCEPT.

- KEEP the five measures, in v1's order.
- Add a short implementation framework, as a numbered list of five steps, VERBATIM order:
  establish baseline performance; define the pilot cohort and capture protocol; configure result
  retrieval and documentation handling; measure outcomes within the program's own systems; compare
  against the baseline and evaluate operational fit. One short line each.
- No numbers, no expected savings, no outcome claims.
- KEEP the FX-012 population limitation (people with physical disabilities) where v1 has it.

## J. Conversion: ACCEPT two touchpoints plus one contextual link. Closing-CTA target: canon, flagged to Vadim.

- The reviewer allows "two or three". `blog-style-guide.md` §5 (Vadim, 2026-11-23) allows two CTAs
  and no mid-body CTA. So: early CTA = B; mid-article = the E1 in-sentence link (an internal link,
  not a CTA); closing CTA = Next steps.
- Closing CTA target. The reviewer asks for `https://3dlook.ai/pricing/#bd-modal-personalized`
  (v1 already links there). Checked 2026-11-23: the pricing page script opens the
  `bd-modal-personalized` popup from the URL hash on load, so the deep link works. But §5 says the
  closing CTA links "as landing-map rule 4 says", and the Hub 2 row's "Demo button now" column is
  "same page" = the telehealth landing (its "Book a demo" buttons open the page's own modal).
  **Use the landing URL for now:** https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/
  The anchor text names the demo ("book a demo of FitXpress for telehealth intake" or similar,
  BOFU direct). This is a canon question for Vadim (open question 1). If he picks the pricing deep
  link, only the URL changes.
- Do not add any other promotional paragraph.

## K. FAQ: ACCEPT.

- KEEP the four questions word for word. Update answers only where this round changed a claim:
  FAQ 4 (comparability) should say the program compares scans it selects (Body Progress, by scan
  ID) under a consistent capture protocol, and keep the below-1-cm sentence with its dataset
  condition and the framework link exactly as v1 has it.
- Add a fifth question and answer, VERBATIM:

  > ### Does FitXpress replace a telehealth platform's existing medical record system?
  >
  > No. FitXpress provides remote body-data capture and structured scan outputs through supported integration interfaces. The customer determines how these results are stored, displayed, associated with patients, and incorporated into its existing documentation workflows. The optional Admin Panel supports scan-data management but is not a replacement for an electronic health record system.

- FAQPage JSON-LD in the package: five questions, text = final.md answers.

## L. Terminology rules (review §3): ACCEPT, all already canon.

- FitXpress / 3DLOOK / Body Progress / Admin Panel as named. Body composition = estimates.
- No patient-history or identity-matching feature. No "objective" about our output
  (terminology-guardrails §2.1). No "What changed" heading (F). Do not front-load "AI" in product
  descriptions: "AI" stays in the H1 and where v1 discusses AI note-taking tools, nowhere else new.
- "100+ clients": do not add a client count; the review only says how to phrase it if used.
- No roadmap features as available; no new statistics, savings, regulatory promises or clinical
  results.

## M. SEO (review §4) and internal links (review §5): ACCEPT.

- Primary keyword stays "telehealth documentation" (plan.md). Secondary concepts are used where
  they read naturally. No keyword stuffing.
- Boundaries KEEP: BMI verification → link to the pharmacy guide only (S4 "At intake"); no GLP-1
  monitoring, no engagement discussion beyond the Related reading link; the hub stays the hub.
- All seven URLs return 200 (checked sequentially 2026-11-23). Each appears at least once:
  landing (B early CTA + E1 contextual; the closing CTA too while J stands), Admin Panel (E2),
  privacy FAQ (S8), accuracy framework (FAQ 4), hub (S4 lead + Related reading), engagement
  (Related reading), pharmacy guide (S4 "At intake"). Descriptive anchors; no exact-match anchor
  repeated.

## N. Deliverables (review §7): seo-publisher.

The package must contain, besides meta and the checklist:
1. change log: every substantive change v1 → v2 with its reason (from this file and editor-report.md);
2. claim verification table: claim · source · status (verified / qualified / removed) · open question;
3. SEO metadata: meta title (≤ 60 chars, contains "telehealth documentation", without the landing
   primary keyword), description, slug (KEEP), primary search intent;
4. internal-link map: URL · anchor · section;
5. remaining approval questions (§V below plus anything new).
A final verdict line: whether the review's acceptance condition holds (all mandatory fixes in,
claims verified, landing link within the first 30%).

## V. Verification record (review §6) and open questions

Sources read 2026-11-23: `compliance.md` §3, §4, §6, §7; `tech-spec.md` (Admin Panel canon, timing,
Clothing Detector status); `roadmap.md` (status as of 2026-10-21, read 2026-11-11); `proof-points.md`
(100+ clients wording); `terminology-guardrails.md` (synced 2026-09-28: §2.14 "organization" is the
only change; applied); `landing-map.md`; `blog-style-guide.md` §5; live pages: Admin Panel launch
post (published 2026-06-02, updated 2026-07-08), telehealth landing, pricing page, privacy FAQ,
accuracy framework, hub, engagement article, pharmacy guide (all 200).

Review §6 checks:
- Technical fields in the API response: `tech-spec.md` lists validation messages; clothing
  detection in the API is planned for Q4 2026 (`roadmap.md`), not released. → The article does not
  say which fields appear in the API response (C).
- Technical fields in the Admin Panel: the launch post shows measurement status, photo-deletion
  timing and Clothes Detector results; `roadmap.md` lists photo-deletion date and failed-scan
  messages as Live. → The article lists only the features in E2; no clothing information.
- Admin Panel availability and export: launch post (updated 2026-07-08): selected clients, no
  public sign-up, credentials from 3DLOOK; CSV export of selected records. → Used as stated.
- Roadmap features: none described as available.
- 09-28 terminology: §2.14 only. 11-11 roadmap checkpoint: no feature used here changed status.

Open questions (go to the package):
1. **Vadim:** closing CTA target, landing (canon §5 + landing-map rule 4) or the pricing demo deep
   link the reviewer asked for (works, checked).
2. **Product:** which technical processing fields appear in the API response and which in the Admin
   Panel (the article does not specify them; confirm nothing needs adding).
3. **Product:** is the Admin Panel still "selected clients, no public sign-up"? The launch post was
   last updated 2026-07-08.
4. Carried from v1 hand-off (Doc 10nLoZ…): three inbound-link spots on `glp-1-market` and
   `the-potential-of-ai-in-telehealth`; illustrations (the Doc's Illustrations tab is empty).
