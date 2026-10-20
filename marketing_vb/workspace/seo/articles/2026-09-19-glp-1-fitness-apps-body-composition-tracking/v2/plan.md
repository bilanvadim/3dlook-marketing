---
slug: 2026-09-19-glp-1-fitness-apps-body-composition-tracking
product: fitxpress
primary_keyword: glp-1 muscle loss
primary_use_case: brand-assets/product-info/use-cases/fx-digital-fitness.md (primary reader), fx-telehealth-weight-loss.md (GLP-1 program side); audience.md segments 3 and 1
hub: AI in Fitness (Hub 1), linked into GLP-1 Market (Hub 3)
cluster: GLP-1 bridge
intent: MOFU
action_type: create-net-new
priority: P1
status: approved
approved: 2026-09-19 (Vadim, checkpoint 1)
created: 2026-09-19
target_words: 2000
author: Assel Sekerova
audit: plan-audit.md
context_pack: workspace/seo/_context-packs/2026-09-19-glp-1-fitness-apps-body-composition-tracking.yaml
keywords_files: workspace/seo/_keywords/2026-09-19-glp-1-fitness-apps-body-composition-tracking*.yaml (4 pulls, 2026-09-19)
---

# SEO Plan: GLP-1 muscle loss and fitness apps (body composition tracking)

This is the writing document. Reasons, the full priced keyword table, the source log and the
Open items are in `plan-audit.md` (section numbers are given as audit §N).

## Checkpoint 1: approved by Vadim, 2026-09-19

These answers override anything below that says "Open item", "only if cleared" or "if Vadim
prefers". Vadim's words are in quotes.

1. **Primary keyword `glp-1 muscle loss`:** "беремо з плану" (take it from the plan).
2. **H1 "GLP-1 Muscle Loss and Fitness Apps: Tracking Body Composition Beyond Scale Weight":**
   "беремо з плану". The row's "Not Just Weight" option is dropped.
3. **Format:** "окрема стаття" (a standalone article). The section-in-GLP-1-Market fallback is
   dropped.
4. **Yazen:** "язен не згадуємо" (do not mention Yazen). Section 6 uses "a weight-loss management
   platform" and never names the customer. The same applies to meta, alt text, FAQ and the
   publish package.
5. **M1 gate on "GLP-1" in the H1:** "прийняти як відомий збій" (accept it as a known failure).
   The writer expands GLP-1 at its first body use, as Section 1 already specifies. When
   `article_lint.py` flags M1 on the H1, record it as the known, accepted failure. Do not reshape
   the H1 to satisfy it.

### Checkpoint 1 decisions as the planner framed them

1. **Primary keyword `glp-1 muscle loss` (600/mo, KD 45, traffic potential 100), chosen with a
   known intent mismatch.**
   - The topic as phrased has no measured demand (`seed_has_data: false`). This keyword is the
     only measured, on-topic term, and no other 3dlook.ai page targets it.
   - Its SERP is consumer and clinical. Most searchers are patients, not app teams.
   - Alternatives and their price are in audit §1. The limits on what the article can say about
     muscle are under "Keyword Analysis" below.
2. **One CTA: the fitness product page.** The telehealth page appears once in the body, for
   readers from GLP-1 programs. Audit §3 gives the reasons.
3. **A standalone page, narrowed, rather than a section in GLP-1 Market.** The row's note ("Net-new
   bridge or section in GLP-1 Market") is a note, not a condition, so the gate is GO. The narrow
   angle and the section fallback are Open item 2, for Vadim to confirm or overrule.

The package for the external reviewer is the last section of this file.

## Content Strategy Fit (Phase 0)

- **Hub / cluster:** AI in Fitness (Hub 1), row `content-plan.md:122`, "GLP-1 bridge". It links
  into GLP-1 Market (Hub 3).
- **Action type:** `Create net-new` (verbatim). The family is create-net-new with no condition,
  so the gate is GO. Priority P1, pencilled for October 2026.
- **Published inventory:** `already_live: false`. This is not a refresh.
- **Intent:** the row says "Cross-cluster bridge". The frontmatter uses `MOFU`, with an
  evaluation CTA.
- **The one job this page owns.** A fitness or coaching app has members taking GLP-1
  medications. The page answers three questions:
  - What should the app record and show besides scale weight?
  - What does research say about lean mass?
  - Which questions belong to the prescribing program?
- **Existing pages. Link to them; do not repeat them:**
  - `glp-1-market` owns the market, the care ecosystem, program-side tracking requirements and
    the "scale weight alone is incomplete" argument.
  - `ai-in-fitness-industry` owns the broad fitness overview and its own "What FitXpress does
    not do" list.
  - `visual-progress-tracking-glp1-adherence-retention` owns the engagement and retention
    argument.
  - `remote-body-measurement-online-fitness-coaching` owns the coach workflow, the
    method-by-method table and the pilot metrics.
  - `top-7-remote-body-composition-tools-glp-1-clinics` owns tool and vendor evaluation.
- **Cannibalization guardrail (row, verbatim):** "Keep fitness app strategy separate from
  wellness and GLP-1 content." Also `content-plan.md:157`: "Every GLP-1 supporting asset must
  own a distinct intent and not repeat GLP-1 Market, Online Pharmacy BMI Verification, Visual
  Progress Tracking or the GLP-1 tools list."
  - The text stays on the app side.
  - The GLP-1 program appears only in the role split (Section 7) and as a reader sent to its own
    pages (Section 9).
  - Do not take over rows 123, 125, 126, 166 or 167 (map: audit §2).
- **Vertical boundary.** Fitness owns app features, progress visibility, training, engagement
  and retention. It does not blur into GLP-1 clinical workflows or wellness rewards.
  - Nothing here is diagnosis, dosing, prescribing, side-effect management, eligibility, or an
    assessment of muscle health.
  - FitXpress says nothing about the medication.

## Keyword Analysis

### Primary cluster

- **Primary keyword:** `glp-1 muscle loss`.
- **Monthly volume (US):** 600. **Difficulty:** 45. **Traffic potential:** 100. Parent topic
  `glp1 muscle loss`. Intent: informational.
- **The same H1 also covers** `glp 1 muscle loss` (400/mo, KD 11).
- **Seed had data: false.** "GLP-1 and fitness apps tracking body composition not just weight"
  has no measured demand. `glp-1 body composition` has no data, meaning Ahrefs has no figure,
  not a measured 0. The row title survives as the H1's angle.
- **Placement:** the H1 and the Section 3 H2 only. Prose uses plain words such as "lean mass"
  and "members on GLP-1 treatment".
- **Thin demand, stated plainly.** The whole on-topic pocket is a few hundred US searches a
  month, and much of it is one question spelled several ways. The page earns its keep through
  answer-engine coverage and the link path between the Fitness and GLP-1 hubs, not through
  organic volume.

### Secondary keywords (weave them in, do not stuff)

| Keyword | Volume / KD | Where |
|---|---|---|
| `glp-1 and muscle loss` | 150 / KD 28 | Section 3 prose |
| `muscle loss glp-1` | 200 / no data | Section 3 or the FAQ 1 phrasing |
| `does glp-1 cause muscle loss` | 250 / no data | Section 3 answers it. **Not an FAQ** |
| `glp 1 lean muscle loss` | 30 / no data | Section 3, where lean mass is distinguished from muscle |
| `glp-1 muscle loss prevention` | 250 / KD 37 | Only as the joint advisory's topic, never as advice |
| `glp-1 app` | 100 / no data | Once, in prose |
| `glp 1 tracking app` | 100 / no data | Optional, once |
| `body composition tracking` | not pulled | H1, Section 5 H2, prose |

### What the article cannot claim about muscle loss

FitXpress says nothing about the medication. Every statement about lean mass or muscle during
GLP-1 treatment comes from a named peer-reviewed or society source, linked on that sentence. If
the writer cannot verify a source at fetch time, the sentence is cut.

- **One research figure only:** the range in Neeland, Linge & Birkenfeld (2024). Some trials
  report lean mass at 40% to 60% of total weight lost; others report about 15% or less. Keep
  both ends and the word "some". Never write a single number such as "GLP-1 users lose X%
  muscle".
- **Lean mass is not muscle.** Every mention of lean mass carries the point that it includes
  organs, bone, fluids and water in fat tissue.
- **No verdict in our own voice** on whether the loss is clinically harmful. Attribute any
  balance to the review ("appear to be adaptive") or to the JAMA Viewpoint, and use the JAMA
  piece only if verified.
- **No prevention or protection claim** for apps, training, protein or FitXpress. The only
  wording allowed is the joint advisory's attributed recommendation: adequate protein intake and
  strength training to preserve lean mass.
- **Excluded entirely:**
  - drug names;
  - doses;
  - side effects;
  - trial-by-trial numbers;
  - figures from clinic, vendor or news blogs.
- **FitXpress does not measure, detect or monitor muscle loss or sarcopenia.** Its lean mass is
  an estimate calculated from model-generated measurements and profile values (height, optional
  weight). It is not equivalent to DXA or professional BIA when a protocol requires those
  methods.
- **No outcome claims.** Do not write that composition tracking improves adherence, retention
  or treatment results. The engagement argument is a link to the Visual Progress page.
- **Never present "lean mass preservation tracking" as a capability.**

## CTA decision

- **The only CTA:** `https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/`.
  - Anchor (evaluation, MOFU): "see how FitXpress supports body composition tracking in
    connected and digital fitness apps".
  - It appears in Section 12, and once in the body in Section 6.
- **Secondary link, in the body only (Section 9):**
  `https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/` for GLP-1
  programs. This is the URL the live GLP-1 hub links. The telehealth URL in the pack appears to
  redirect (Open item 4).

## Recommended Title

**H1:** GLP-1 Muscle Loss and Fitness Apps: Tracking Body Composition Beyond Scale Weight

The keyword is in the first three words and both halves of the row stay. "Beyond Scale Weight"
avoids the corrective "Not Just Weight" shape.

### Other options

1. GLP-1 Muscle Loss and Fitness Apps: Tracking Body Composition, Not Just Weight. This is the
   row's wording. It is the live alternative if Vadim prefers it.
2. GLP-1 Muscle Loss: What Fitness Apps Should Track Beyond the Scale. It reuses the subtitle of
   row 123.
3. GLP-1 Muscle Loss and Body Composition Tracking in Fitness Apps. It loses the reframe and
   drifts toward row 167.
4. GLP-1 and Fitness Apps: Tracking Body Composition, Not Just Weight. The row title verbatim.
   Gate 7 fails unless the primary keyword changes; this is the fallback for Open item 1.

## Article Outline (12 sections)

Follow the order in `content-strategy-guidelines.md` §12. Follow the sentence shape and format
in `editorial-rewrites.md` §7:

- a mean of 14-15 words per sentence;
- bold-label bullets;
- one table;
- "fits when" H3s;
- headings that describe rather than assert.

### Section 1. Where scale weight can fall short for members on GLP-1 treatment

- **Goal:** the app team recognises the problem within two sentences and knows the scope.
- **Words:** 180
- **Must-cover:**
  - `(Cover) - Concept` directly under the H2.
  - **Scene, in two sentences.** A member taking a glucagon-like peptide-1 (GLP-1) medication
    logs a falling scale weight in a fitness app. The number does not separate fat mass, lean
    mass and fluid.
  - **One sentence** on what changes when the app records body composition estimates and
    circumferences next to weight.
  - **"The choice turns on two questions":** what the app records beyond scale weight, and which
    decisions stay with the prescribing program. Link up to the AI in Fitness hub, with an
    anchor about structured body data for progress tracking in fitness apps.
  - **`**Scope note.**`** in 4-5 short sentences:
    - The page covers fitness and coaching apps, and GLP-1 programs that run training features.
    - FitXpress supplies body measurements and body composition estimates.
    - It does not evaluate GLP-1 medications, doses or side effects.
    - An estimated lean mass is not a measurement of muscle.
    - "FitXpress is not a medical device."
    - Clinical questions stay with the prescribing clinician.
- **Keywords:** GLP-1 treatment, fitness apps, scale weight. Keep the primary keyword out of the
  prose.
- **Approved claims:** none.
- **Boundary:** no drug names. Do not claim that the app or FitXpress detects muscle loss.

### Section 2. Short answer: what fitness apps can track beyond scale weight

- **Goal:** a summary an answer engine can extract.
- **Words:** 150
- **Must-cover:** 4-5 bullets. Each has a bold label and one or two sentences.
  - **Scale weight** records total change. It does not separate fat mass, lean mass and fluid.
  - **Body composition estimates** (body fat percentage, fat mass, lean mass) show what the
    change consists of. They are estimates, and what they mean depends on the method.
  - **Circumferences** (waist, hip, thigh, upper arm) show where change happens. A guided
    smartphone scan can capture them remotely.
  - **Training history** the app already holds, such as strength progression and completed
    sessions, gives the composition trend context.
  - **Who decides what?** The app supports training and progress views. Medication and clinical
    questions stay with the prescribing program.
- **Keywords:** body composition tracking. Optionally `glp 1 tracking app`, once.
- **Approved claims:** FX-005 (output names only). No figures.
- **Boundary:** this is the only list of signals. Section 5 describes steps and does not repeat
  it.

### Section 3. What research shows about GLP-1 muscle loss and lean mass

- **Goal:** present the evidence through its sources. This H2 carries the primary keyword.
- **Words:** 230
- **Must-cover:**
  - **Neeland, Linge & Birkenfeld** (*Diabetes, Obesity and Metabolism*, 2024).
    - Lean mass accounts for 40% to 60% of total weight lost in some trials, and about 15% or
      less in others.
    - The review gives population, drug-specific and comorbidity effects as the reasons.
  - **The same review on lean mass and muscle.**
    - Lean mass includes organs, bone, fluids and water in fat tissue, not only muscle.
    - Magnetic resonance imaging (MRI) studies suggest muscle changes "appear to be adaptive".
  - **Optional balance: the JAMA Viewpoint by Conte, Hall and Klein (2024).** It argued that
    current data do not support concern about frailty or sarcopenia from GLP-1-induced weight
    loss. Include it **only if verified on the JAMA page** (Open item 7). Otherwise cut it.
  - **The 2025 joint advisory.** It comes from the American College of Lifestyle Medicine, the
    American Society for Nutrition, the Obesity Medicine Association and The Obesity Society.
    - It recommends adequate protein intake and strength training to preserve lean mass.
    - Add one sentence connecting this to the app: strength training is the app's territory.
    - Give no training or protein prescription.
  - **Link up to the GLP-1 Market hub,** with an anchor on scale weight and progress records in
    GLP-1 programs. Do not restate its argument.
- **Keywords:** `glp-1 muscle loss` (H2), `glp-1 and muscle loss`, `glp 1 lean muscle loss`.
  Use each at most once.
- **Sources (fetch them and quote precisely):**
  - https://pubmed.ncbi.nlm.nih.gov/38937282/ (the journal page
    https://dom-pubs.onlinelibrary.wiley.com/doi/full/10.1111/dom.15728 returns 403 to fetchers).
    The verbatim abstract sentences are in audit §7.
  - https://jamanetwork.com/journals/jama/article-abstract/2819410
  - https://onlinelibrary.wiley.com/doi/full/10.1002/oby.24336 and
    https://www.obesity.org/nutritional-priorities-to-support-glp-1-therapy-for-obesity/
  - https://3dlook.ai/content-hub/glp-1-market/
- **Approved claims:** none. FitXpress does not appear in this section.
- **Boundary:** every rule under "What the article cannot claim about muscle loss" applies.

### Section 4. Why GLP-1 treatment is relevant to fitness and coaching apps

- **Goal:** explain why this matters now, from the app's side.
- **Words:** 150
- **Must-cover:**
  - **KFF Health Tracking Poll** (fieldwork October 27 to November 2, 2025): about one in eight
    US adults (12%) said they were currently taking a GLP-1 drug, either to lose weight or to
    treat a chronic condition. Keep the poll's framing, and do not extrapolate to app members.
  - **Hedge the link to apps.** Fitness and coaching apps are likely to serve some of these
    members, whether or not a member tells the app.
  - **Why scale weight is weak here.** For members treated for weight management, a falling
    scale weight is the expected direction.
    - A scale-based progress view then says little about what the training program adds.
    - Composition estimates and circumferences can make that contribution visible.
  - **One sentence** with a sideways link to Visual Progress Tracking for GLP-1, for engagement
    and retention.
- **Keywords:** `glp-1 app` (optional, once), fitness apps.
- **Source:** https://www.kff.org/public-opinion/poll-1-in-8-adults-say-they-are-currently-taking-a-glp-1-drug-for-weight-loss-diabetes-or-another-condition-even-as-half-say-the-drugs-are-difficult-to-afford/
- **Boundary:**
  - no outcome claims;
  - no invented adoption statistics;
  - no app or platform names.

### Section 5. How a fitness app can track body composition during GLP-1 treatment

- **Goal:** the workflow on the app's side. The GLP-1 hub owns the program-side requirements.
- **Words:** 190
- **Must-cover:** one sentence naming the steps, then bold-label bullets (not a numbered list).
  - **Baseline.** The first scan at onboarding or at the start of a strength program, using the
    same guided capture as later scans.
  - **Check-ins at defined points,** such as the end of a training block. Leave the reasoning on
    how often to FAQ 2.
  - **Repeatable capture conditions.** Similar clothing, time of day and setting. The guided
    flow checks pose and framing.
  - **One progress view.** Weight, circumferences and composition estimates together, next to
    training history, with labels that mark estimates.
  - **A route for clinical questions.** Questions about medication, side effects or muscle
    health go to the prescribing clinician. The app's content does not answer them.
  - `(Image 1) - Concept` after the bullets.
- **Keywords:** body composition tracking.
- **Approved claims:** none.
- **Boundary:**
  - The workflow does not require the app to know a member's medication (this sets up FAQ 3).
  - No numeric change thresholds.

### Section 6. Where FitXpress fits

- **Goal:** describe the product once, briefly, with evidence in the approved short forms.
- **Words:** 260
- **Must-cover:**
  - `(Image 2) - Concept` under the H2.
  - **What it provides, in three short sentences:**
    - The software development kit (SDK) embeds guided two-photo capture (front and side) in the
      app.
    - Results arrive in under 45 seconds.
    - The outputs are 80+ body measurements, body composition estimates (body fat percentage,
      fat mass, lean mass), BMI, basal metabolic rate (BMR) and a 3D model.
  - **Comparison wording.** Scan-to-scan comparison uses two scans that the app selects. Never
    write "FitXpress tracks each member".
  - **Method, in the live coaching article's phrasing.** Composition estimates apply established
    formulas to model-generated measurements and profile values such as height and optional
    weight. Then add: the lean mass figure is an estimate, not a measurement of muscle.
  - **Reframe as a statement.** "What counts as adequate performance depends on how the
    measurements will be used." For a trend view, repeatability is especially important; say
    so conditionally.
  - **Repeatability paragraph.** Use the `accuracy-formulations.md` §5 short form verbatim (two
    sentences), with the framework link in the same paragraph.
  - **Accuracy paragraph,** its own paragraph after that. Use the §5 short form (three
    sentences, including the NDA line).
  - **Case, in one or two sentences:** "a weight-loss management platform" ran 34,000 FitXpress
    scans in 2025. It used them for periodic check-in progress tracking, 3D visualization and
    body composition context.
    - **Do not name Yazen** (Vadim, 2026-09-19: "язен не згадуємо").
    - No GLP-1 attribution, no geography, no outcome, no superlative.
  - **Link down** to the fitness product page, with an anchor on FitXpress for connected and
    digital fitness apps.
- **Keywords:** body composition tracking, fitness apps.
- **Sources:** https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/ ,
  https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/
- **Approved claims:**
  - FX-006;
  - FX-005, without the two fat sub-categories retired in Review 1 item 13;
  - FX-002 (primary);
  - FX-001 (own paragraph);
  - FX-007.
- **Boundary:**
  - no ISO benchmark;
  - no per-measurement figures;
  - never FX-003;
  - no FX-004.
  - For equivalence, use `accuracy-formulations.md` §2.1 option 2: not equivalent to DXA, BIA
    or a calibrated scale when the workflow, protocol or regulatory standard requires those
    methods.

### Section 7. What the app, the prescribing program, and FitXpress each handle

- **Goal:** the division of responsibility, which belongs to neither hub. This fills the "what
  FitXpress does not do" slot for this context.
- **Words:** 170
- **Must-cover:**
  - **Lead-in, one sentence, about the subject:** when a member on GLP-1 treatment also uses a
    separate fitness app, two organizations hold parts of the progress record.
  - **The table:** a bold header row and 4 rows.

    | **Role** | **Responsible for** | **Uses body data to** |
    |---|---|---|
    | Prescribing clinician or GLP-1 program | Medication, dosing, side effects and any clinical assessment of muscle or nutritional status | Review progress alongside clinical information, where its protocol includes body data |
    | Fitness or coaching app | Training programs, progress views and member communication | Show measurement and composition trends next to training history |
    | Member | Completing scans and choosing what to share with each service | See change beyond the scale reading |
    | FitXpress | Body measurements, body composition estimates, a 3D model and scan-to-scan comparison | Supply structured records to the app or program that integrates it |

  - **Then 2-3 sentences in `compliance.md` §7 wording:**
    - "FitXpress is not a medical device."
    - It does not provide dose calculations, symptom tracking, prescribing recommendations or
      clinical decision support.
    - It does not evaluate GLP-1 medications.
    - Treatment decisions stay with the prescribing clinician.
- **Boundary:** 3DLOOK does not track individuals or decide whether two scans belong to the
  same person.

### Section 8. Scale weight, body composition estimates, and reference methods: which fits when

- **Goal:** a decision framework. It does not rebuild the coaching article's method table or
  the smart-scale comparison planned in row 123.
- **Words:** 190
- **Must-cover:** a one-sentence lead-in, then three H3s. Each H3 holds 3-4 complete-sentence
  bullets of about ten words.
  - `### Scale weight alone fits when`
    - the app tracks general weight trends;
    - members check in rarely or decline scans;
    - no training program depends on composition context.
  - `### Body composition estimates fit when`
    - members follow a strength program in the app;
    - coaches review check-ins;
    - capture conditions are repeatable;
    - the app labels estimates and their limits.
  - `### A reference method fits when`
    - a clinical protocol or study requires dual-energy X-ray absorptiometry (DXA) or
      professional bioelectrical impedance analysis (BIA);
    - the prescribing clinician needs an assessment of muscle health or function;
    - the result feeds a clinical decision.
  - **One sentence on consumer smart scales.** They estimate composition through bioelectrical
    impedance, and readings depend on the device and conditions. Then add a sideways link to the
    coaching article for the method-by-method comparison.
- **Keywords:** body composition tracking.
- **Source:** https://3dlook.ai/content-hub/remote-body-measurement-online-fitness-coaching/
- **Boundary:**
  - no table;
  - no accuracy ranking against DXA.
  - Mobile scanning complements reference methods; frame this as fit, not rank.

### Section 9. Fitness apps and GLP-1 programs this workflow fits

- **Goal:** who this fits, on both sides, in a few lines.
- **Words:** 100
- **Must-cover:**
  - **Subscription fitness apps and coaching platforms** with strength programs, recurring
    check-ins and members who may be on GLP-1 treatment.
  - **Coaching platforms** where human coaches review check-ins.
  - **GLP-1 programs** that add training features to their own app. Send them to the telehealth
    page (down link). Optionally, send them to the GLP-1 tools list (sideways link).
  - **One limitation sentence:** fit is lower with no check-in cadence, no training program, or
    no defined use for composition data.
- **Sources:** https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/ ;
  optional https://3dlook.ai/content-hub/top-7-remote-body-composition-tools-glp-1-clinics/
- **Boundary:** no named companies.

### Section 10. Implementation and evaluation considerations

- **Goal:** what an app team settles before launch, in four bold-label paragraphs.
- **Words:** 170
- **Must-cover:**
  - **Consent and data sharing.**
    - Scan outputs can be personal or health data, depending on use.
    - When the app and a GLP-1 program are separate organizations, sharing records between them
      depends on the member's consent and the agreements between the organizations.
    - Link the trust FAQ for storage, retention, deletion, HIPAA and GDPR. Do not restate it.
    - Optional: the FX-008 GDPR sentence, verbatim.
  - **Change thresholds.** Set the difference worth showing from observed scan-to-scan variation
    and the check-in interval. No figure.
  - **An alternative path.** Use the first two sentences of the `accuracy-formulations.md` §5
    disability limitation. Then say what the workflow does instead: manual measurements or a
    view with weight only.
  - **Pilot measures,** in at most three sentences: scan completion, completion of repeat
    check-ins, use of the progress view, and member questions routed to the program. Measure
    them against a baseline taken before the pilot.
- **Source:** https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/
- **Approved claims:** FX-008 (optional, the GDPR sentence only).
- **Boundary:**
  - Do not model the live coaching article's privacy paragraph; it uses retired wording.
  - Take all wording from `compliance.md`.
  - Do not copy that article's nine-row pilot list.

### Section 11. Frequently asked questions

- **Goal:** three questions the body does not settle. Answer each in 2-3 sentences, more briefly
  than the body, and link.
- **Words:** 170
- **The three:**
  1. **Can a mobile body scan measure muscle loss during GLP-1 treatment?**
     - It does not measure muscle directly.
     - It estimates lean mass from measurements and profile values, and lean mass includes more
       than muscle.
     - A reference method such as DXA applies where a protocol requires it.
     - Link the accuracy framework.
  2. **How often should a fitness app scan members on GLP-1 treatment?**
     - It depends on the expected change compared with typical scan-to-scan variation, and on
       the training block.
     - The prescribing program sets its own clinical schedule.
     - Give no number of weeks.
  3. **Does a fitness app need to know whether a member takes a GLP-1 medication?**
     - Not for body composition tracking itself.
     - Asking is a health-data decision that involves purpose, notice and consent.
     - Link the trust FAQ.
- **Boundary:** do not add "Does GLP-1 cause muscle loss?" as an FAQ. Section 3 already answers
  it.

### Section 12. Next steps

- **Goal:** one evaluation CTA.
- **Words:** 40
- **Must-cover:** two sentences.
  - First: compare the app's current progress view with what members on GLP-1 treatment need to
    see.
  - Second: start with "Then" and carry the CTA link, "see how FitXpress supports body
    composition tracking in connected and digital fitness apps", pointing to
    `https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/`.

## Illustrations

| Name | Placement | Concept |
|---|---|---|
| Cover | Under the Section 1 H2 | A fitness app progress screen on a phone. A scale-weight trend line sits above one stacked bar per check-in that splits estimated fat mass and lean mass, labelled "estimate". No medication or injection imagery. |
| Image 1 | Section 5, after the bullets | A timeline for one member: a baseline scan, then check-ins at the end of each training block. Each point shows three tiles (weight, circumferences, composition estimates) above a training-volume sparkline. |
| Image 2 | Section 6, under the H2 | Two 3D body models from scans the app selected, side by side, with the waist, hip and thigh circumference differences labelled. |

## Article meta

- **Estimated words:** 2,000 prose words. **Estimated read time:** about 9 minutes.
- **Tables and visuals:** one table (Section 7), a cover and two images.
- **CTA placement:** Section 12 only. The fitness page is also linked once in Section 6.

| Section | Words |
|---|---|
| 1. Where scale weight can fall short | 180 |
| 2. Short answer | 150 |
| 3. Research on GLP-1 muscle loss | 230 |
| 4. Why it is relevant to apps | 150 |
| 5. App-side workflow | 190 |
| 6. Where FitXpress fits | 260 |
| 7. Who handles what | 170 |
| 8. Which fits when | 190 |
| 9. Fit | 100 |
| 10. Implementation | 170 |
| 11. FAQ | 170 |
| 12. Next steps | 40 |
| **Total** | **2,000** |

**Internal links.** There are 9 distinct links, covering all four directions.

| Direction | Target | Placement |
|---|---|---|
| up | https://3dlook.ai/content-hub/ai-in-fitness-industry/ | Section 1 |
| up | https://3dlook.ai/content-hub/glp-1-market/ | Section 3 |
| sideways | https://3dlook.ai/content-hub/visual-progress-tracking-glp1-adherence-retention/ | Section 4 |
| sideways | https://3dlook.ai/content-hub/remote-body-measurement-online-fitness-coaching/ | Section 8 |
| sideways (optional) | https://3dlook.ai/content-hub/top-7-remote-body-composition-tools-glp-1-clinics/ | Section 9 |
| down / CTA | https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/ | Sections 6 and 12 |
| down | https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/ | Section 9 |
| trust | https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/ | Section 6 (the paragraphs with figures), FAQ 1 |
| trust | https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/ | Section 10, FAQ 3 |

**External links:** Neeland et al., the JAMA Viewpoint (if verified), the joint advisory and the
KFF poll. Put each link on an anchor phrase in the sentence it supports.

## Writing constraints carried into the draft

- **Hard bans.** The editor runs the full pass.
  - No em dashes or en dashes.
  - None of these words: leverage, utilize, harness, robust, seamless, comprehensive, delve,
    navigate (as a metaphor), unlock, unleash, revolutionary, game-changing, cutting-edge.
  - None of these: `by hand`, `let`, `plus` as a connector, `so` introducing a benefit,
    `objective` about our own outputs, "positioned as", "not just X, it's Y".
  - No `this article` outside the scope note.
- **Terms.** Write "80+ body measurements". BMI and BMR are calculated metrics. Body
  composition figures are estimates.
- **Abbreviations.** Expand GLP-1, DXA, BIA, SDK, BMR, MRI, HIPAA and GDPR at their first use in
  the body. Leave BMI and US bare. Open item 6 covers the H1.
- **Accuracy.**
  - Use the `accuracy-formulations.md` §5 short forms or the §1 wording verbatim, and never mix
    the two in one paragraph.
  - Put the framework link on the paragraph that carries the figure.
  - No ISO figure.
  - In Section 3, keep "variation" and "variance" away from "40% to 60%". Gate 9 reads a
    percentage within 40 characters after them as an unapproved accuracy figure.
- **Compliance.**
  - Use only the wording in `compliance.md`.
  - Never write "HIPAA compliant", "SOC 2 certified", "processed, not stored" or "no personal
    identifiers".
- **Actors.**
  - Name them: fitness app, coaching platform, GLP-1 program, prescribing clinician, member.
  - Use "buyer" only for procurement, and "customer" only in the GDPR role sentence.
- **Tone and names.**
  - Lighter on the fitness half, hedged on the GLP-1 half.
  - No names of competitors, apps or platforms. Yazen is not named (Vadim, 2026-09-19).
  - No pricing.
  - Author: Assel Sekerova.

## Package for the external reviewer

Send this file together with `plan-audit.md`. At this stage the reviewer can cheaply overturn:

- the framing and audience;
- the choice and order of sections;
- keyword placement;
- the boundaries with neighbouring pages;
- what to cut.

**Contents:**

- **12-section outline**, with a goal and must-cover list per section: see "Article Outline".
- **Primary keyword and metrics:** `glp-1 muscle loss`, 600/mo, KD 45, TP 100. The SERP is
  informational and leans toward consumers. The alternatives are priced in audit §1:
  - the tracker-app cluster: consumer app-store intent;
  - `body composition tracking`: not pulled;
  - `body composition`: definition intent owned elsewhere;
  - the row phrase: no data.
- **Hub, cluster, action type and guardrail:** see "Content Strategy Fit".
- **Questions we most want challenged:**
  - (a) Should a B2B vendor page carry `glp-1 muscle loss` in its H1?
  - (b) Is the role split in Section 7 the right way to fill the "does not do" slot?
  - (c) Is the page distinct enough from `glp-1-market`, or should it be a section there?

**Deliberately not covered:**

1. The smart scale vs mobile body scan comparison (`content-plan.md:123`, P2, one shared page if
   demand supports it). It gets one sentence and a link.
2. Dosing, drug names, side effects, symptom tracking, medication effectiveness, clinical
   monitoring schedules, and any assessment of muscle health or sarcopenia.
3. BMI verification, eligibility and prescribing gates. The online pharmacy BMI verification
   article owns these. UK Meds is not cited.
4. Wellness rewards and employer incentive programs (Hub 5).
5. GLP-1 market size, the care ecosystem, and program-side tracking requirements
   (`glp-1-market`).
6. The argument that visual progress drives adherence and retention (the Visual Progress page;
   `mobile-body-scanning-patient-engagement` is the canonical engagement asset).
7. A comparison of tools or vendors for GLP-1 clinics (`top-7-...`).
8. The coaching workflow, the method-by-method table and the pilot metrics list (the coaching
   article).
9. Body composition basics and a methods tutorial (`how-to-measure-body-composition`; row 167).
10. Protein targets and exercise prescriptions. Only the advisory's attributed recommendation
    appears.
11. Privacy and regulatory answers. A short note links to the trust FAQ.
12. Accuracy methodology. Short forms appear, linked to the framework.
13. Named fitness apps, GLP-1 platforms and competitors. Yazen is not named either.
