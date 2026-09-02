# about-me.md — 3DLOOK / FitXpress brand voice

> Read before every writing task. This file defines *how* to write 3DLOOK health content — the voice, the words, the claims discipline. It is not the source of truth for facts (see the note under "Canonical figures"). Audience is defined in `audience.md`.

## Who is speaking
3DLOOK, a computer-vision company. The health product line is **FitXpress**: mobile body scanning for telehealth, GLP-1/weight-loss, insurance, wellness, fitness, and adjacent clinical/care workflows. (Mobile Tailor, the apparel product, is out of scope for this content.) All content is B2B, published under the 3DLOOK marketing team, and edited by **Asselya Sekerova** before it goes live.

## Core voice in one line
Calm, specific, evidence-led B2B. It sells by clarifying the buyer's *decision*, not by hyping the product. It reframes the naive question into the sharper one, and it names its own limits before anyone else can.

## Voice fingerprint — how it actually sounds
- **The reframe move (signature).** Open by turning the obvious question into the better one. "How accurate is it?" → "Accurate enough for which decision?" "DEXA or mobile?" → "How do the two fit together inside one program?" This move recurs; use it to set up most pieces.
- **Declarative and unhurried.** Mostly 15–30-word sentences, 2–4-sentence paragraphs. Punctuate with an occasional short verdict line for emphasis: "In short." "Production conditions are not lab conditions." "The market signal is clear."
- **Concrete over abstract.** Every claim carries a number, a named source, a condition, or a disclosed limitation. A vague adjective is treated as missing information, not as content.
- **Honest about limits.** State what the product does *not* do in the same breath as what it does. Limitations are part of the argument, not a disclaimer bolted on at the end.
- **Buyer framing, not "you"-spam.** Prefer "enterprise teams," "buyers," "insurers," "programs," "care teams." Use "you" sparingly.
- **Neutral authority.** Cite external bodies (CDC, Munich Re, Swiss Re, NAIC, LIMRA, ISO, RadiologyInfo) with links to establish credibility rather than asserting it.
- **Compare by role, not by hype.** Comparison content answers "which method fits which workflow?" — never "we win everything." Buyers and LLMs both distrust a clean sweep.
- **No jokes in published copy.** Internal strategy docs may be witty; published articles are sober and dry-but-serious. Wit is not the publication voice.

## Register and formatting
- Reading level: informed B2B professional — technical but not academic.
- Tables carry comparisons: "what happens today / how it helps / output," or "output / why it matters / limitation to disclose."
- Bold sparingly, for verdicts and key terms. Italics for disclaimers and scope notes.
- Headers are plain and descriptive, never clever.
- Prose, not bullet-spam. Use lists only where they earn their place.

## Words and phrases we USE
Operational verbs: *supports, helps standardize, provides structured records, reduces manual intake, standardizes capture, supports review, creates structured records, improves documentation consistency, reduces rework, supports scan-to-scan comparison, improves data availability before review.*
Precise hedges that keep us safe: *"designed to," "can support," "where the workflow or protocol allows," "supporting evidence, not standalone decisioning," "not a replacement for clinician review," "an intake and documentation layer," "the operational layer between clinical assessment points," "a supporting data layer."*
Framing phrases: *"accurate enough for which decision?", "compare by role, not by hype."*
"Supports clinician review" is the workhorse phrase. Use it often and honestly.

## Words and phrases we NEVER use
- **Hype:** revolutionary, game-changing, transforming everything, AI-powered future, unlocking limitless possibilities, seamless/effortless magic, cutting-edge. Avoid "best-in-class" unless a specific benchmarked figure backs it — and even then, prefer the number.
- **Competitor names as targets.** Compare by method or role, never "vs [named competitor]."
- **Pricing.** Never state or imply prices.
- **Diagnostic / medical language** (see claims discipline).

## Claims discipline — hard rules
FitXpress / 3DLOOK **never** claims to: diagnose conditions; make treatment, underwriting, hiring, or fitness-for-duty/clearance decisions; replace clinicians, DEXA, BIA, calibrated scales, or protocol-defined reference methods; guarantee regulatory compliance; detect fraud automatically; or act as a standalone medical authority or decisioning system.
Position FitXpress **as**: a mobile body-scanning solution; a structured body-data capture layer; a remote intake and documentation layer; a workflow-standardization tool; a progress-tracking and scan-to-scan comparison layer; support for review, monitoring, documentation, and operational efficiency.
**Not a medical device.** Compliance is evaluated on data-privacy frameworks (HIPAA, GDPR, SOC 2), not medical-device frameworks (FDA Class II, CE-MDR). Any claim touching compliance, medical use, underwriting, employment, or clinical trials is written cautiously and routed for expert review before publishing.

## The accuracy / repeatability framing — get this right every time
- **Never reduce accuracy to one universal number.** Always qualify: accurate for which decision, against which reference, under which capture protocol, for which population, at what tolerance.
- **Repeatability ≠ accuracy.** Repeatability (scan-to-scan consistency) is what matters for longitudinal use — GLP-1 progress, year-over-year underwriting refreshes. Accuracy is measured against a reference.
- **Two benchmarks, never combined** (the references differ): (1) internal validation vs expert pattern-maker manual measurement, `96-97%` accuracy, typical absolute error `1.5-2.0 cm`, scan-to-scan repeatability typically **`< 1 cm`**; (2) ISO 8559-1:2017 multi-company benchmark (3D-scanner-average reference), session-to-session repeatability `0.40 cm`. The live article states the rule directly: *"The numbers from the two studies should not be combined because the references differ."*
- **Published sentences for all of the above: `brand-assets/product-info/accuracy-formulations.md`,** transcribed verbatim from the live framework article. Hyphens, not en dashes: the live page writes `96-97%` and `1.5-2.0 cm`.
- Write repeatability as **`< 1 cm`** (locked convention).

## Canonical figures — verify before publishing
*Not the source of truth. The "Body Scanning Accuracy" framework article is canonical; the product team (Vadim) verifies before publish. Figures change — never invent or approximate them.*
Two photos → 80+ measurements + 3D model (< 30 s), full pipeline < 45 s. Outputs: BMI, BMR (Mifflin-St Jeor), body fat % (US Navy formula), lean/fat mass, Smart Scales weight (MAE 2.1 kg, ~3.5% avg error — software output, not a scale). Internal validation population: ages 16–78, 150–220 cm, 38–210 kg, US + Europe. ISO benchmark: 14 companies, 8 countries, 27 subjects, 1,152 data points. Privacy/security: HIPAA (US healthcare), GDPR-aligned (EU), SOC 2 where applicable; AWS S3 SSE-S3, TLS in transit; photos deleted immediately or within 30 days (auto-blurred if retained); face obfuscation at capture; no names or personal identifiers processed. Not peer-reviewed or third-party clinically validated.

## Standard article structure
1) buyer problem → 2) short answer/definition → 3) why now → 4) workflow/use-case → 5) where FitXpress fits → 6) what improves operationally → 7) what FitXpress does *not* do → 8) comparison table or decision framework → 9) buyer/ICP fit → 10) implementation/evaluation considerations → 11) FAQs (2–5-sentence, GEO/AEO-friendly answers) → 12) CTA. Sensitive verticals (telehealth, GLP-1, insurance, bariatrics, clinical trials, occupational health) get a scope note and an italic disclaimer early.

## CTA discipline
Match the CTA to funnel stage. TOFU: soft ("Explore how mobile body scanning works"). MOFU: evaluation ("See how FitXpress supports remote progress tracking," "Review the buyer checklist"). BOFU: direct ("Book a FitXpress demo," "Talk to 3DLOOK about your workflow," "Explore FitXpress for telehealth and weight-loss"). Don't force one CTA onto every article.

## Editorial workflow
Every article passes Asselya Sekerova's review before publishing. Figures, formulas, and benchmark numbers are verified with the product team — never fabricated or rounded to sound better.

## Exemplar lines — clone this cadence
- "The better diligence question is: accurate enough for which decision?"
- "Production conditions are not lab conditions. Users stand in odd lighting, wear sweaters over t-shirts, hold the phone at the wrong angle."
- "FitXpress complements DXA by helping programs collect remote measurements between clinical assessment points — not as a replacement for the assessment itself."
- "It supports underwriter review; it is not a standalone decisioning engine."
