# Review digest — mobile-body-scanning-patient-engagement

Article: `workspace/seo/articles/mobile-body-scanning-patient-engagement/draft-v5-revision1.md`
(no `publish-package.md` exists for this slug; frontmatter `status: published`, live at https://3dlook.ai/content-hub/mobile-body-scanning-patient-engagement/ since 2026-08-14. This draft is the canonical pre-CMS snapshot per its own frontmatter note.)
Date: 2026-08-17
Profiles: 9 (linkedin-whitney skipped — disabled, `posts_per_week: 0`)

**Note on gate:** this run proceeded on Vadim's `/post-from-article` invocation per CLAUDE.md §9 — the approval gate is this request plus his Telegram approval of the digest below, not a `status:` field on the source file. All 9 drafts still need that Telegram approval before any visual work or scheduling (CLAUDE.md §9, §10 rule 2). `visual-brief` was not run.

**Open items for Vadim (not silently fixed — see below):**
1. **linkedin-katya Design tip — needs a fix before any designer hand-off.** It currently specifies "a simple retention curve dropping after week four ... one label: 'week six.'" The only figure that could justify that shape (the GLP-1 discontinuation stat, 64.8%, JAMA Network Open) was removed from the article in Review 1 with an explicit note not to reintroduce it in any post or design brief. The post's own body copy is clean — this is a design-tip-only defect. QC scored this post 16/20 (good) specifically for this. Recommend: replace with a neutral, unlabeled "week six" marker on a flat timeline (no curve shape implied), as suggested in `all-posts-compiled.md`.
2. **Verbatim phrase reuse across 3 LinkedIn posts.** "Motivation fades when progress stays invisible" appears identically in linkedin-company and linkedin-katerina; "30, 60, and 90-day cycles" appears in linkedin-company, linkedin-katerina, and linkedin-katya. Company-page and CEO audiences overlap heavily, so this is a real dedup risk if someone follows more than one profile. Not fixed automatically — flag for your call on whether to vary phrasing.
3. **Claim-ID cosmetic issue.** Several personal-LinkedIn post frontmatters cite `C1/C8/C9/...` claim IDs (from a planning-stage claims table) rather than the article's own `FX-*` claim registry. Every underlying fact still checks out against the source article — this is a traceability-label mismatch only, no content risk.
4. `instagram-company` uses one emoji (📈) — within the 1-2 max ceiling, noted only for visibility.

Order below: company accounts first (twitter → instagram → facebook → linkedin-company), then personal LinkedIn alphabetically (Katerina, Katya, Nick, Olena, Vadim).

---

## twitter-company

Between virtual visits, a remote care program often runs on one number a patient types into an app, taken on whatever scale is in the house. Two guided smartphone photos give the patient and the care team the same structured record to compare over time.

**CTA:** Article link in the reply to the tweet.

> **Design tip**
> Article visual: No OG block exists in `draft-v5-revision1.md`. Derived direction: the article's core contrast between a lone self-reported figure and a structured, comparable body record.
> Format: text (optional single card)
> Adaptation: If a card is used, split it in two: left side a single bare number in a thin outline box, right side a scan-to-scan measurement strip with a 3D silhouette. One idea only, no captions beyond the two labels.
> Keep: Navy `#050F40` ground, electric blue `#143DFF` accent, Satoshi labels, abstract silhouette only, no patient photography, no medical imagery.

QC: 20/20 (excellent)

---

## instagram-company

The scale barely moved. But the body changed a lot.

In a clinic, progress had a ritual. A patient steps on a scale, a nurse records the number, and change becomes something visible. Remote care quietly removed that moment. What is left is a figure typed into an app between visits, and a single number can hide the change that matters most.

Mobile body scanning puts that moment back. Two guided smartphone photos, front and side, turn into more than 80 measurements, body composition, and a 3D model in approximately 30 to 45 seconds. No hardware. No trip to a clinic.

A patient losing fat while gaining lean mass may see a scale that looks stuck, while the 3D model and the waist measurement tell a different story. Seeing that change is a reason to keep showing up. 📈

The care team still reviews the data and decides what it means. FitXpress keeps the record consistent and progress visible between appointments.

**CTA:** Link in bio for the full piece.

> **Design tip**
> Article visual: No OG block exists in `draft-v5-revision1.md`. Derived direction: a scan-to-scan 3D body comparison where visible change shows up even when the weight figure barely moves.
> Format: carousel (3 slides)
> Adaptation: Slide 1, the hook line over a flat weight figure with a nearly horizontal trend line. Slide 2, the same patient silhouette at two timepoints side by side, waist and lean-mass deltas called out on the second. Slide 3, the two-photo capture glyph with the caption "front and side, about 30 to 45 seconds."
> Keep: Navy `#050F40` and electric blue `#143DFF`, Satoshi type, abstract 3D silhouette as the hero, no patient photography, no body-exposure imagery, no clinical props.

QC: 20/20 (excellent)

---

## facebook-company

How often should a patient scan? More often is not automatically better.

Programs run into this question early, and the answer shapes whether progress data helps anyone. Scanning too often surfaces noise. Scanning too rarely misses the moments that keep a patient engaged. Cadence should track program length and the expected rate of change.

Here is the loop it fits into. A patient takes a first guided two-photo scan at intake, from home, in about a minute. That scan becomes the baseline: measurements, body composition, and a 3D model that later scans compare against. The program sets the re-scan cadence from there. Between appointments the patient sees a scan-to-scan comparison and watches the 3D model change. The care team reviews consistent records and decides what they mean.

Because capture is guided and repeatable, each pass produces data that lines up with the last, instead of figures that drift session to session.

FitXpress supports that review. It does not diagnose, and it does not make clinical or eligibility decisions.

What cadence works for your program? The full article walks through the rest: https://3dlook.ai/content-hub/mobile-body-scanning-patient-engagement/

**CTA:** "Read the full article" with the live link in the post body.

> **Design tip**
> Article visual: No OG block exists in `draft-v5-revision1.md`. Derived direction: the six-step scan-to-scan loop described in the "How the scan-to-scan experience works" section.
> Format: text + photo
> Adaptation: One horizontal strip of the loop (Enrollment capture → Baseline → Scheduled re-scans → Progress visualization → Care-team review → Next-cycle goals), with a curved arrow returning from the last stage to the third so the loop reads as a cycle. Enlarge the labels for a broader, less technical audience.
> Keep: Navy `#050F40` ground, electric blue `#143DFF` on the capture stages, Satoshi labels, abstract icons only, no patient photography, no medical imagery.

QC: 18/20 (excellent)

---

## linkedin-company

Virtual care is past the question of whether it works. The harder problem now sits between visits, where a program has no in-room ritual left to carry a patient's motivation.

What usually fills that space is a self-reported weight. Readings come from different scales, capture conditions vary, and a single number cannot show how measurements or body composition are changing. Motivation fades when progress stays invisible, and the repeat check-in that supports patient engagement becomes a churn risk instead. For programs built on 30, 60, and 90-day cycles, that drift separates a member who renews from one who quietly disappears.

Structured body data changes what both sides can see. FitXpress turns two guided smartphone photos into more than 80 measurements, body composition outputs, and a 3D model in approximately 30 to 45 seconds, delivered through an API or SDK inside a program's own patient app. For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm, and consistent capture conditions help programs compare results more reliably over time.

One capture supports two things at once: a patient-facing progress experience and a structured record for care-team review.

The boundary matters as much as the capability. FitXpress supports review rather than diagnosis. It does not make clinical or eligibility decisions, and it does not replace required clinical assessments where a protocol calls for them. It is not positioned as a medical device, and compliance is evaluated on data-privacy frameworks.

Read the full article on how mobile body scanning improves patient engagement: https://3dlook.ai/content-hub/mobile-body-scanning-patient-engagement/

**CTA:** "Read the full article" with the live link.

> **Design tip**
> Article visual: No OG block exists in `draft-v5-revision1.md`. Derived direction: the between-visit gap, shown as a timeline with two clinic touchpoints and a long empty stretch in the middle.
> Format: text + photo
> Adaptation: A horizontal timeline in navy with two blue visit markers at either end. The middle stretch carries a single grey self-reported figure, then the same stretch repeats underneath filled with evenly spaced scan markers. Caption the second row "structured capture between visits."
> Keep: Navy `#050F40` ground, electric blue `#143DFF` markers, Satoshi labels, no patient photography, no medical imagery, no logos other than 3DLOOK.

QC: 19/20 (excellent)

---

## linkedin-katerina

The question I hear from UK remote care teams has changed over the past two years. It used to be about accuracy. Now it is about what happens between appointments.

Virtual-first programs solved the visit. They did not solve the weeks in between, when the only progress signal is a number a patient types into an app, often taken on a different scale each time. Motivation fades when progress stays invisible, and a program built on 30, 60, and 90-day cycles feels that quickly.

What interests me more is how the buying conversation has changed alongside it. Enterprise buyers here rarely open with model performance any more. They open with scope. What does this layer decide, what does it not decide, and where does the data sit.

Our answers are deliberately narrow. Structured body data supports clinician review; the care team interprets it and makes the decision. It is not positioned as a medical device, and it is evaluated on data-privacy frameworks rather than medical-device ones. Standard hosting runs in the US, with UK hosting available on request.

That narrowness is turning into an advantage rather than a limitation. A layer with clearly stated boundaries is far easier to place inside a regulated care pathway than a system claiming more ground than it can defend.

The full piece works through the patient-engagement side of this. Curious what you think.

https://3dlook.ai/content-hub/mobile-body-scanning-patient-engagement/

**CTA:** Soft invitation to the article, "Curious what you think," with the live link.

> **Design tip**
> Article visual: No OG block exists in `draft-v5-revision1.md`. Derived direction: scope, shown as a bounded box rather than a workflow.
> Format: text (no visual required; a founder observation reads better native)
> Adaptation: If a card is later requested, use a single navy panel with one line of white Satoshi text: "Supports review. Does not decide." Nothing else on the card.
> Keep: Navy `#050F40` ground, electric blue `#143DFF` used only as a thin rule, Satoshi type, no stock photography, no UK flags or landmark imagery, no regulator logos.

QC: 19/20 (excellent)

---

## linkedin-katya

Most digital health teams I meet across Israel and the Gulf can quote their acquisition numbers to the decimal. Ask what happens to a patient in week six and the answer gets noticeably vaguer.

That gap is usually where the commercial problem sits. A program built on 30, 60, and 90-day cycles depends on people coming back, and people come back when they can see something change. Remote care removed the moment that made change visible. A number typed into an app between visits has not replaced it.

The interesting part commercially is that the fix is not another notification stream. It is giving the patient and the care team the same thing to look at. Two guided smartphone photos produce more than 80 measurements, body composition, and a 3D model, and every new scan compares against the last one. Someone losing fat while gaining lean mass can finally see why the scale is not moving.

The buyers who move fastest here tend to be the ones already treating engagement as a revenue metric rather than a product feature. They ask what the layer decides. The honest answer is that it decides nothing: the care team reviews the data and makes the call.

Where does your program lose people, and do you know why?

Full piece here if that number is not obvious yet: https://3dlook.ai/content-hub/mobile-body-scanning-patient-engagement/

**CTA:** Discussion question first, article link after.

> **Design tip**
> Article visual: No OG block exists in `draft-v5-revision1.md`. Derived direction: the retention curve, not the product.
> Format: text (no visual required; a buyer-conversation post reads better native)
> Adaptation: ⚠️ **Flagged, see Open items #1 above — do not hand this to a designer as written.** As drafted: "If a card is later requested, use a simple retention curve dropping after week four, with a single blue marker where a progress view would land, and one label: 'week six.'" This implies a discontinuation shape the article does not support (the supporting stat was removed in Review 1). Recommended fix: a flat, unlabeled timeline with a single "week six" marker — no curve, no implied drop-off.
> Keep: Navy `#050F40` ground, electric blue `#143DFF` marker, Satoshi labels, no patient photography, no regional flags or landmark imagery, no clinical stock imagery.

QC: 16/20 (good) — scored down for the design-tip issue above; post copy itself is clean.

---

## linkedin-nick

Telehealth stopped being a temporary channel a while ago. A 2026 analysis of the Medical Expenditure Panel Survey, published in the journal Healthcare, found that the share of US adults with at least one telehealth visit rose from about 7% in 2020 to roughly 12% in 2021, and held near that level through 2023.

Virtual care scaled, then settled in. The conversations I have with US healthcare organizations have moved to a narrower question: what keeps a patient engaged between visits, when there is no in-room ritual left to carry it?

Today the answer is usually a self-reported weight. It arrives from a different scale each time, and it cannot show how body composition is changing. A patient losing fat while gaining lean mass sees a flat number while the change that matters stays invisible.

Structured capture changes what both sides see. Two guided smartphone photos produce more than 80 measurements, body composition, and a 3D model in approximately 30 to 45 seconds. For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm.

Privacy is the second question every US buyer asks, and rightly. FitXpress supports HIPAA-compliant workflows with a Business Associate Agreement where required, production photos are deleted after processing, and data is encrypted in transit and at rest.

It supports review rather than diagnosis. The care team keeps the decision.

How is your program measuring engagement between visits today? Full piece here: https://3dlook.ai/content-hub/mobile-body-scanning-patient-engagement/

**CTA:** Discussion question plus invitation to the article, with the live link.

> **Design tip**
> Article visual: No OG block exists in `draft-v5-revision1.md`. Derived direction: the telehealth adoption curve from the MEPS analysis, used as the entry point rather than a product diagram.
> Format: text + photo
> Adaptation: A minimal line chart, 2020 to 2023, rising from about 7% to roughly 12% and flattening, with the flat stretch labelled "the channel settled. the engagement problem did not." Source line in small type: MEPS analysis, journal Healthcare, 2026.
> Keep: Navy `#050F40` ground, electric blue `#143DFF` line, Satoshi labels, no patient photography, no stethoscope or clinical stock imagery, no US flag motifs.

QC: 19/20 (excellent)

---

## linkedin-olena

European health and wellness operators I speak with are rarely running one program at a time. The same platform carries a weight-loss cohort, a coaching product, and a remote monitoring pathway. All of them hit the same wall between appointments: progress stops being visible, and participation drops with it.

What makes structured body data worth a look is that the pattern transfers across those program types:

• Telehealth: a shared body record for patient and clinician between virtual visits
• Weight-loss programs: context around a stalled number on the scale
• Wellness and coaching: repeat participation supported with lighter, non-clinical framing
• Remote monitoring: a consistent record between formal assessment points

Two questions come up in every European evaluation I join.

Data handling. Production photos are deleted after processing, structured outputs are retained according to the customer's configuration and agreement, data is encrypted in transit and at rest, and EU hosting is available on request alongside GDPR-aligned data handling.

Delivery. The two-photo capture runs through an API or SDK inside the program's own patient app, under its own branding, with no specialized hardware for a patient to buy.

FitXpress is the capture layer underneath, nothing more. It supports clinician review instead of replacing it, and it makes no clinical or eligibility decisions.

Which of your programs would feel that engagement gap first? The full piece goes into the workflow detail: https://3dlook.ai/content-hub/mobile-body-scanning-patient-engagement/

**CTA:** Engaging question plus invitation to read the article, with the live link.

> **Design tip**
> Article visual: No OG block exists in `draft-v5-revision1.md`. Derived direction: one capture layer feeding four different program types.
> Format: text + photo
> Adaptation: A single capture glyph on the left, four thin blue lines fanning out to four labelled cards on the right (telehealth, weight loss, wellness and coaching, remote monitoring). Add a small lock mark beside the capture glyph for the data-handling point.
> Keep: Navy `#050F40` ground, electric blue `#143DFF` connectors, Satoshi labels, abstract icons only, no patient photography, no country flags or country-specific imagery.

QC: 20/20 (excellent)

---

## linkedin-vadim

Something I keep coming back to with Australian telehealth and digital health operators: a progress feature is easy to demo and hard to keep honest at scale.

Visible progress only works if the data behind it holds up. The part that decides whether it holds up is not the model. It is the capture protocol.

Production conditions are not lab conditions. A patient stands in poor light, wears a loose sweater, or holds the phone at the wrong angle. Guided capture and retake logic reduce that error. They do not remove the need for clear instructions, which is why capture guidance belongs in the rollout plan rather than in a help-centre article written after launch.

Two other things worth settling before go-live.

Cadence. Scanning too often surfaces noise, scanning too rarely misses the moments that keep a patient engaged. Match it to program length and the expected rate of change.

Measurement. Decide upfront what you will track, whether that is scan completion rate, repeat check-in rate, or progress-visualization views. Those are engagement signals rather than clinical outcome measures, and treating them as the latter is how a rollout loses internal credibility fast.

FitXpress provides the capture and structuring layer through an API or SDK. The program builds the experience around it, and the care team keeps the decision.

For anyone running a remote program here at scale: where does your capture quality break down first?

https://3dlook.ai/content-hub/mobile-body-scanning-patient-engagement/

**CTA:** Discussion question plus the live article link.

> **Design tip**
> Article visual: No OG block exists in `draft-v5-revision1.md`. Derived direction: the operational half of the article, capture guidance and cadence, rather than the patient-facing progress view.
> Format: text + photo
> Adaptation: A simple two-column card. Left column "what reduces capture error": guided flow, retake logic, clear instructions. Right column "what it does not fix": light, clothing, phone angle. Keep it plain and unstyled, closer to a whiteboard than a brochure.
> Keep: Navy `#050F40` ground, electric blue `#143DFF` for the left column only, Satoshi labels, no patient photography, no Australian flags or landmark imagery.

QC: 19/20 (excellent)

---
