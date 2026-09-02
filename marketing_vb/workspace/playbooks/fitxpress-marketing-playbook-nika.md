---
title: FitXpress Marketing Playbook
subtitle: Presentations and landing pages, end to end
owner: Nika (Product Marketing Manager)
start_date: 2026-08-25
product: fitxpress
scope: B2B health verticals only. Mobile Tailor is out of scope.
language: English (all FitXpress B2B copy)
version: 1.0
created: 2026-08-24
prepared_by: Marketing automation (Vadim's repo) from the FitXpress Sales Playbook (June 2026), the Drive sales folder, and the local brand source-of-truth files
status: draft for Vadim's review
---

# FitXpress Marketing Playbook

**Who this is for.** Nika, joining 2026-08-25 as Product Marketing Manager. She owns presentations
and landing pages end to end, for every FitXpress health use case.

**What this is.** An operating manual, structured after the FitXpress Sales Playbook (June 2026) so
that marketing and sales describe the same product the same way. Section 4 is the working reference
Nika will open most often. Sections 5 and 6 are the two production lines she runs.

**One rule above all the others.** Every figure in a deck or on a page comes from
`brand-assets/product-info/proof-points.md`. A number that is not there does not ship. It goes into
an Open items block and the slot stays visibly empty until Vadim confirms it. This is the fastest way
this function either earns or loses credibility with a buyer doing diligence.

---

## Table of contents

1. [Role and scope](#1-role-and-scope)
2. [Brand and voice guardrails](#2-brand-and-voice-guardrails)
3. [Design system quick reference](#3-design-system-quick-reference)
4. [Use-case library (11 health segments)](#4-use-case-library)
5. [Deck build playbook](#5-deck-build-playbook)
6. [Landing-page build playbook](#6-landing-page-build-playbook)
7. [Messaging and proof library](#7-messaging-and-proof-library)
8. [QA checklist](#8-qa-checklist)
9. [Open items and conflicts to resolve](#9-open-items-and-conflicts-to-resolve)
10. [Source index](#10-source-index)

---

## 1. Role and scope

### 1.1 What Nika owns

| Artifact | Owned by Nika | Notes |
|---|---|---|
| Vertical demo decks (FitXpress for X) | Yes, end to end | Copy, structure, slide-level design brief, versioning |
| First-call and leave-behind decks | Yes | Short cuts of the demo deck, same spine |
| Vertical landing pages on 3dlook.ai | Yes, as the driver | Runs through the `/page` pipeline (see 6.1). Nika owns the brief, the copy decisions and the final quality call |
| Campaign landing pages | Yes | Same section map, shorter, single message per campaign |
| Two-pagers and one-pagers | Yes | Print variant of the design system, see 3.6 |
| Messaging per segment | Yes | Hero line, proof set, objection answers, disclaimer, kept in section 7 and pushed back into `brand-assets/product-info/messaging.md` |
| Blog and SEO articles | No | Route to `/new-article`. A PMM page brief and an article brief resolve against different plans and will contradict each other if both run |
| Social posts from a published article | No | Route to `/post-from-article` |
| Outbound sequences | No | Route to `/outbound` |
| Pricing decisions and exceptions | No | Katerina Galich or Kate Kondakova |
| Final editorial sign-off on published health copy | No | Asselya Sekerova reviews before anything goes live |
| Claims that touch medical, compliance, underwriting or employment | No, escalates | Whitney Cathcart and Katerina, before publishing |

### 1.2 How Nika plugs into the team

| Person | Role | What Nika needs from them |
|---|---|---|
| Katerina Galich | CEO | Positioning calls, competitive framing sign-off, pricing exceptions, customer logo and quote permission |
| Whitney Cathcart | Co-founder and CCO | Deck guidance, claims framing on regulated verticals |
| Vadim Bilan | Marketing | Number confirmation, `proof-points.md` updates, brand asset access, the repo and the automation pipelines |
| Asselya Sekerova | Editorial | Final review of health copy before publish. Non-optional |
| Max Kucherenko | VP Product | Capability questions, roadmap status, what may be promised |
| Kate Kondakova | COO | Contracts, operations |
| Nick Omelchak (USA), Olena Kudryavtseva (Europe), Kateryna Boichuk (Israel and Gulf) | BD | The real objections and the vertical specifics a page or deck needs. They are the source for "what a buyer in this market actually asks" |
| Yurii Tymko | Demo accounts | Demo links and screenshots for collateral |

**Cadence to adopt.** Weekly: what shipped, what is blocked, which numbers need confirmation.
Bi-weekly with Katerina: positioning and priorities. Monthly: asset audit, which decks and pages
have drifted from `proof-points.md`.

**Escalate immediately** when a deck or page needs a figure that does not exist, when a customer name
or quote is requested without written permission, or when a claim starts drifting toward diagnosis,
eligibility decisioning or guaranteed compliance.

### 1.3 Where the assets live

**Local repo (source of truth for voice, claims and design).**
`/home/vadim_prod/3dlook-marketing/marketing_vb/`

| Path | What it governs |
|---|---|
| `CLAUDE.md` | Company facts, two-product split, banned words (section 6), compliance posture (section 12) |
| `about-me.md` | Brand voice, claims discipline, accuracy framing, CTA discipline |
| `audience.md` | The seven health segments: hook and "what NOT to say" |
| `DESIGN.md` | Every design token. The only design source of truth |
| `brand-assets/product-info/proof-points.md` | **Every number.** Nothing else is a citable figure |
| `brand-assets/product-info/icp-detail.md` | Buyer titles, revenue thresholds, pains, triggers, named target companies |
| `brand-assets/product-info/messaging.md` | Approved hero lines per use case, anti-positioning table |
| `brand-assets/product-info/compliance.md` | Security and privacy answers, what is never claimed |
| `brand-assets/product-info/tech-spec.md` | Integration options, SDK behaviour, output detail, the two integration patterns |
| `brand-assets/product-info/pricing.md` | Internal tier table. Internal per-request rates never ship |
| `brand-assets/product-info/case-studies/` | The only place a customer name and a customer number may come from |
| `brand-assets/product-info/use-cases/fx-*.md` | Per-vertical use-case files, eight of eleven exist |
| `brand-assets/style-guides/editorial-guardrails.md` | The 11 principles and rules M1, M2 |
| `brand-assets/style-guides/ai-tells-sweep.md` | The hard-fail list, and the detector script |
| `brand-assets/content-strategy/terminology-guardrails.md` | Word-level rules from Asselya |
| `.claude/skills/page-builder/` | The page pipeline: gates, the 17-slot Vertical Page Kit, site inventory |
| `docs/quality-rubric.md` | The 20-point QC rubric artifacts are scored against |

**Drive sales folder** (Katerina's, shared, the same folder the AE playbook points at):
`https://drive.google.com/drive/folders/1UdeWy90iiTVzHrLPsmOyYqM0wl3l_BlO`

| Subfolder | Useful to Nika |
|---|---|
| `Marketing docs & Decks` | FitXpress for Insurance Underwriting demo deck (May 2026), FitXpress for Telehealth demo deck (May 2026), FX Guidance for Decks (Whitney, Feb 2026), FitXpress 2-pager PDF, Integration Guidelines, ICP all-in-one |
| `Technology & Accuracy` | Accuracy and Repeatability Analysis (Apr 2026), Technology Presentation (May 2025), Fat estimation approach, earlier accuracy study (Feb 2025) |
| `Useful info` | BMI verification use case deck, Prism Labs introduction and Whitney's Prism analysis, Brainstorm deck (the market-sizing source), GLP-1 weight-validation deck, Katerina's AI keynote |
| `Email and skrips templates` | Post-demo, reconnect and break-up templates. Useful for the tone sales uses after a deck lands |
| `Integration docs`, `Legal docs` | Reference for the integration and compliance slots |
| `Nick Omelchak — Deal Call Transcripts` | Real buyer objections in the buyer's own words. The best raw material for section 5 slide 2 and the vertical FAQ |

Two notes on the Drive folder. `FX Guidance for Decks Whitney Feb 2026` is a shortcut whose target
did not resolve on read, so ask Vadim or Whitney to re-share the underlying file. The published
2-pager PDF contains "seamlessly embeds" and quotes "under 60 seconds", both of which are now wrong
(see section 9), so treat it as a layout reference and not as copy.

**Design references (Figma).** Blog banners:
`https://www.figma.com/design/zWV1W9fs7cbp7Jc0pVDTDX/Blog-banners`. Website pages:
`https://www.figma.com/design/yQlvzqLeCJAAQjaHSKIduC/3DLOOK-website`.

**Live pages worth reading before building anything**

| URL | Why |
|---|---|
| `/structured-body-data-for-telehealth-digital-health-programs/` | The in-house benchmark. About 1,613 words, a 13-question FAQ with FAQPage schema, Service schema with `audienceType` and `areaServed`. Match this |
| `/for-bmi-verification/` | About 659 words, no FAQ, no cases. The first rewrite candidate |
| `/fitxpress/for-connected-and-digital-fitness/` | Sits on a `/fitxpress/` path level that does not exist (`/fitxpress/` redirects to the homepage). Do not copy its URL pattern |
| `/pricing/` | The public price signal every commercial page links to |

### 1.4 First two weeks

**Days 1 to 3, read and calibrate.** `CLAUDE.md`, `about-me.md`, `audience.md`, `DESIGN.md`,
`proof-points.md`, `editorial-guardrails.md`. Then the insurance underwriting deck copy end to end
(`/home/vadim_prod/3dlook-marketing/fitxpress-insurance-underwriting-deck-copy.md`) as the structural
exemplar, and the telehealth page structure doc (Drive) as the landing-page exemplar. Then the sales
playbook, to hear how sales speaks.

**Days 4 to 7, audit.** Score the existing decks and the six live vertical pages against section 8.
Produce one list: every figure in circulation that is not in `proof-points.md`, every banned word on
a live page, every claim that needs Whitney. Section 9 is the starting point for that list, not the
end of it.

**Week 2, ship one thing.** Rewrite `/for-bmi-verification/` (the weakest live page, and the vertical
with a real customer reference in UK Meds), taking it through the full pipeline in section 6. It is
the shortest path to seeing every gate work.

---

## 2. Brand and voice guardrails

### 2.1 The positioning, in one line

**Outcomes and workflow, not accuracy.** FitXpress is a trusted workflow layer for verified body
data, for industries where measurement consistency, fraud reduction and audit-ready records drive a
business result. It is not a measurement API.

Why this matters commercially: body scanning commoditizes on a 12 to 36 month horizon as vision
foundation models become common and Apple or Google may ship native primitives. A deck that wins on
"most accurate" loses the day that happens. A deck that wins on workflow integration, governance,
auditability and longitudinal reliability does not.

Practical consequence for every artifact Nika builds: the hero line names the buyer's business
outcome. Accuracy appears later, scoped, as support for that outcome.

### 2.2 The voice

Calm, specific, evidence-led B2B. It sells by clarifying the buyer's decision, and it names its own
limits before anyone else can.

- **The reframe move (the signature).** Open by turning the obvious question into the better one.
  "How accurate is it?" becomes "accurate enough for which decision?". "DEXA or mobile?" becomes
  "how do the two fit together inside one program?".
- **Declarative and unhurried.** Mostly 15 to 30 word sentences, 2 to 4 sentence paragraphs. An
  occasional short verdict line for emphasis: "In short." "Production conditions are not lab
  conditions."
- **Concrete over abstract.** Every claim carries a number, a named source, a condition or a
  disclosed limitation. A vague adjective is missing information.
- **Honest about limits.** State what the product does not do in the same breath as what it does.
- **Buyer framing.** "Enterprise teams", "insurers", "care teams", "programs". Use "you" sparingly,
  and mainly on landing pages and conversion sections where a decision-maker is being addressed
  directly.
- **Neutral authority.** Cite external bodies (CDC, Munich Re, Swiss Re, NAIC, LIMRA, ISO,
  RadiologyInfo) with links, rather than asserting authority.
- **Compare by role, not by hype.** A comparison answers "which method fits which workflow?". A
  clean sweep across every row reads as marketing and buyers discount it.
- **No jokes in published copy.** Internal strategy docs may be witty. Customer-facing copy is sober.

### 2.3 Claims discipline: what FitXpress is and is not

**Position FitXpress as:** a mobile body-scanning solution, a structured body-data capture layer, a
remote intake and documentation layer, a workflow-standardization tool, a progress-tracking and
scan-to-scan comparison layer, support for review, monitoring, documentation and operational
efficiency.

**FitXpress never claims to:**

| Never claim | Say instead |
|---|---|
| Diagnose a condition | Provides structured body data that supports clinician review |
| Make treatment, underwriting, hiring or fitness-for-duty decisions | Supporting evidence, not standalone decisioning |
| Replace clinicians, DEXA, BIA, calibrated scales or a protocol-defined reference method | Complements the reference method by collecting remote measurements between clinical assessment points |
| Guarantee regulatory compliance | Supports compliant workflows and audit-ready documentation |
| Detect fraud automatically | Supports fraud-prevention workflows by flagging discrepancies for review |
| Act as a standalone medical authority | An intake and documentation layer, alongside clinical oversight |

**The medical framing, exactly.** "FitXpress is not positioned as a medical device." Never "medical
device regulation does not apply". Compliance is framed on data-privacy frameworks (HIPAA, GDPR,
SOC 2 where applicable), not on medical-device frameworks (FDA Class II, CE-MDR).

**What is never claimed at all** (from `compliance.md`): FDA clearance, medical advice or diagnosis,
SOC 2 certification (in progress, confirm with Vadim before any mention), direct PHI processing.

### 2.4 Repeatability is not accuracy

This is the single framing most often broken, and it is the one that sells.

- **Accuracy** is measured against a reference method. It is only meaningful with four conditions
  named: reference method, measurement protocol, population tested, intended workflow.
- **Repeatability** is scan-to-scan consistency. It is what matters for longitudinal use: GLP-1
  progress over 30, 60, 90 days, year-over-year underwriting refreshes, survivorship monitoring.
- **Never reduce accuracy to one universal number.** Always qualify: accurate for which decision,
  against which reference, under which capture protocol, for which population, at what tolerance.
- **Two benchmarks, never combined.** The references differ, so mixing them produces a figure that
  describes nothing.
  1. Internal validation against expert manual measurement: 96 to 97% accuracy, typical absolute
     error 1.5 to 2.0 cm, scan-to-scan repeatability `< 1 cm`. This set is in `proof-points.md`.
  2. The ISO multi-company benchmark, reported as 0.40 cm session-to-session repeatability. **This
     set is not in `proof-points.md`.** It is in `about-me.md` and in both shipped decks. Until
     Vadim adds it, treat it as pending, see section 9, item 2.
- **Write repeatability as `< 1 cm`.** Locked convention.
- **Never the words "independent", "validated" or "third-party"** without a named external party and
  a citable output (guardrail 3). The compliant forms are internal validation, benchmark
  participation, dataset enrichment. State the negatives plainly: not peer-reviewed, not third-party
  validated, not clinically certified.
- **No bare headline percentage** (guardrail 4). ">95%" invites "of what, measured how, over how many
  sessions?". Pair a qualitative claim with one concrete sub-figure and "detailed methodology
  available under NDA".

The reusable paragraph, adapt the vertical and the decision:

> The better diligence question is: accurate enough for which decision? For [decision in this
> vertical], what matters is whether a change between scans is real rather than measurement noise.
> Against expert manual measurement, FitXpress reaches 96 to 97% accuracy with a typical absolute
> error of 1.5 to 2.0 cm, and scan-to-scan variance stays `< 1 cm`. Detailed methodology is
> available under NDA. FitXpress is not positioned as a medical device, and it supports clinician
> review rather than replacing it.

### 2.5 Words to use

Operational verbs: *supports, helps standardize, provides structured records, reduces manual intake,
standardizes capture, supports review, creates structured records, improves documentation
consistency, reduces rework, supports scan-to-scan comparison, improves data availability before
review.*

Precise hedges: *designed to, can support, where the workflow or protocol allows, supporting
evidence rather than standalone decisioning, not a replacement for clinician review, an intake and
documentation layer, the operational layer between clinical assessment points, a supporting data
layer.*

Framing phrases: *accurate enough for which decision?*, *compare by role, not by hype.*

"Supports clinician review" is the workhorse phrase. Use it often and honestly.

### 2.6 Words never to use

**Banned words.** leverage, utilize, harness, robust, seamless, comprehensive, revolutionize,
revolutionary, cutting-edge, state-of-the-art, game-changer, disrupt, delve, tapestry, realm,
groundbreaking, best-in-class, industry-leading, world-class, unparalleled, and *navigate* in its
figurative sense.

**Banned phrasings.** "In today's fast-paced world", "Unlock the power of", "Are you struggling
with?", "It's no secret that", "Have you ever wondered", "Let's dive in", "Here's everything you
need to know", and "AI-powered" standing alone as a value claim.

**Banned constructions.**

| Construction | Why | Fix |
|---|---|---|
| "It's not just X, it's Y", "not only X but also Y" | The most reliable AI signature in English marketing copy. It also survives casual editing because it is what people reach for when they want emphasis | State Y directly |
| Adjectival punch triads: "fast, reliable, scalable" | Reads generated | Two adjectives, or one with a condition. A list of real things ("positioning, posture, equipment") is a list and is fine |
| Em dash and en dash (— and –) | Banned in all contexts, no exceptions | Comma, full stop, or brackets |
| Corrective negation "X, not Y" | Sounds corrective and dismissive. **Exception:** a necessary product, clinical, legal or regulatory boundary. "FitXpress supports clinician review; it is not a diagnostic tool" is correct | Lead with the recommended approach and explain its purpose |
| "Furthermore / Moreover / Additionally" opening a sentence | Minimize |  |

**Word-level rules from Asselya** (`terminology-guardrails.md`): never *objective* about our own
output (use standardized, timestamped, structured, repeatable), never *the reader / the audience /
the following sections / see below*, never *this article / this guide*, never *by hand* (use
manually), never *plus* as a capability connector (use including, along with, as well as), never
*let* (use allow), never *so* introducing a benefit (use reducing, helping to reduce, which can
reduce). Careful with *we / our*: heavy use makes copy read as a company-centered sales deck.

**Anti-positioning, what never to lead with** (`messaging.md`): "most accurate body scanning",
"AI-powered body scanning" alone, "replace your in-person fitting", "disrupt body measurement",
"just plug in our API".

**Rules M1 and M2.**
- **M1.** Expand every abbreviation at first use, then use the short form. This is universal and it
  includes the ones that feel obvious: Body Mass Index (BMI), glucagon-like peptide-1 (GLP-1),
  dual-energy X-ray absorptiometry (DEXA), Application Programming Interface (API), Software
  Development Kit (SDK), Contract Research Organization (CRO), and cited regulators or standards
  (FDA, ICH, GCP, MHRA, CQC). Regulators cited as authority are the ones most often left bare.
- **M2.** One clear negative statement of scope, stated once. Avoid chaining a second negation onto
  it in the same sentence, avoid interrupted negation ("the scope FitXpress is, and is not, designed
  for"), avoid double negatives ("necessary but not sufficient"). Repeating the scope disclaimer
  across sections is fine; this rule governs negation density inside a sentence.

**The AI-tells sweep is a separate pass, after writing.** Draft, then sweep. Policing your own tells
while drafting does neither job well.

```bash
python3 brand-assets/style-guides/scripts/detect-ai-tells.py <file> --channel page --summary
```

`--channel` is `article`, `post`, `dm`, `page` or `any`. Fix every `hard_fails` and
`house_rule_violations` entry. Then read the copy yourself and answer the question the detector
cannot: what here still reads as machine-written? That second pass is the point.

### 2.7 Disclaimer boilerplate for sensitive verticals

Every sensitive vertical (telehealth, GLP-1, online pharmacy, insurance, health plans, bariatrics,
occupational health, clinical trials, plastic surgery, BCRL) gets a scope note early, not a
disclaimer bolted on at the end, and an italic line near any accuracy or eligibility claim.

Approved patterns. Adapt the second clause per vertical, keep the first sentence intact.

- **Universal base.** *FitXpress is not positioned as a medical device. It provides structured body
  data that supports clinical and operational workflows.*
- **Telehealth, GLP-1 and weight loss.** *...It supports remote progress tracking and clinician
  review; treatment decisions remain with the care team.*
- **Online pharmacy and remote prescribing.** *...It supports eligibility verification workflows and
  audit-ready documentation; prescribing and eligibility determinations remain with the prescriber.*
- **Insurance underwriting.** *...Outputs are supporting evidence for underwriter review; risk
  classification and pricing decisions remain with the carrier.*
- **Health plans and employer wellness.** *...It supports remote verification and documentation for
  incentive programs; reward and eligibility determinations remain with the program administrator.*
- **Bariatric and metabolic clinics.** *...It supports remote pre-qualification workflows; surgical
  candidacy remains the clinical team's determination.*
- **Occupational health.** *...It supports screening intake and documentation; fitness-for-duty and
  clearance determinations remain with the occupational health provider.*
- **Clinical trials.** *...It standardizes and documents anthropometric capture; endpoint validation
  and protocol compliance remain with the sponsor and the investigator.*
- **Plastic surgery.** *...It supports remote pre-screening and planning input; surgical and
  anaesthetic risk assessment remains with the surgeon.*
- **BCRL and oncology survivorship.** *...It supports remote monitoring workflows and reproducible
  body records; it does not detect or diagnose lymphedema, and clinical assessment remains with the
  care team.* This is the most compliance-sensitive vertical. Lead with the scope note, and route
  every draft to Whitney before it leaves the building.

**Compliance framing that is always safe:** "supports compliant workflows", "audit-ready
documentation", "HIPAA-aware and GDPR-aligned". Never "makes you compliant", never "guarantees
compliance", never an absolute compliance claim.

**Every control is stated with its limit** (guardrail 5). Pose validation, clothing detection and
live capture reduce error and reduce fraud exposure; they do not remove the need for capture
instructions, retake logic or deployment-specific thresholds.

---

## 3. Design system quick reference

`DESIGN.md` is the only design source of truth. Use tokens exactly as written. Never introduce a
font, colour or radius that is not in it.

### 3.1 Brand essence

Clinical precision with consumer-app polish. Confident, spacious, technical but human. Every layout
should read as precision, trust, modern AI.

Four principles: **restraint over density** (one or two big moments per page, generous negative
space), **product over icons** (a real 3D body-scan render, the guided-capture phone UI, the Admin
Panel in a browser frame, in preference to a generic icon), **precision as a visual language** (fine
measurement lines, grids, keypoint dots, large exact numerals), **depth rather than flat fills**
(navy zones carry a radial glow and subtle texture, never a dead flat block). Proof zones are
evidence-forward: the number is the hero.

### 3.2 Colour

| Token | Hex | Role |
|---|---|---|
| `--blue` | `#143DFF` | Electric blue. The single sharp accent: calls to action, key numbers, links, highlights |
| `--navy` | `#050F40` | Navy surfaces: hero, proof bands, CTA band, footer |
| `--black` | `#000000` | Dark buttons, high-contrast type |
| `--white` | `#FFFFFF` | Dominant background on content zones, text on dark |

Blue scale, ten steps: `#ECEFFF` · `#D8DEFF` · `#B1BDFF` · `#8A9CFF` · `#4F6DFF` · **`#143DFF`** ·
`#0F2ECD` · `#0B2299` · `#08186B` · `#050F40`. Tints for soft cards, chips and the focus ring
(`#B1BDFF`). `#0F2ECD` is the primary hover, `#0B2299` the gradient end.

Gray scale, ten steps: `#F9F9F9` · `#F2F2F2` · `#E5E5E5` · `#D1D1D1` · `#A8A8A8` · `#808080` ·
`#666666` · `#4C4C4C` · `#333333` · `#1A1A1A` (`--ink`).

**Weighting.** White dominates content zones. Navy `#050F40` carries 60 to 70% of the weight on
hero, proof, CTA and footer. Electric blue stays a single sharp accent and never becomes a large fill.

**Navy glow gradient** for hero, CTA and footer: radial glow, brighter blue upper-centre falling to
deep navy at the edges. Stops `#4F6DFF` or `#0B2299` glow core, then `#08186B`, then `#050F40` edge.
Add subtle grain or a faint measurement-grid texture. Rounded top corners on the footer band, about
30 to 40px.

**A note on `#2962FF`.** The task brief for this playbook named `#2962FF` as the accent. That value
is superseded. It was a placeholder in `brand-assets/color-palette/colors.md` before the Figma export
arrived, both `CLAUDE.md` section 7 and `DESIGN.md` section 15 mark it and Inter as retired, and both
old files are now redirect stubs. The canonical accent is `#143DFF` and the canonical typeface is
Satoshi. Do not resurrect `#2962FF` or Inter. Flagged in section 9, item 1.

**Status colours** (success, pending, error) are not defined in the palette. If a status UI is needed,
choose an accessible green or amber and flag it for confirmation. Do not treat it as a brand token.

### 3.3 Typography

**Satoshi**, headings and body. Weights 400 Regular, 500 Medium, 600 Semi Bold, 700 Bold, 900 Black
for display accents. Import:
`https://api.fontshare.com/v2/css?f[]=satoshi@400,500,600,700,900&display=swap`. Fallback stack
`'Satoshi','Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif`. Embed or outline Satoshi
in print PDFs.

| Heading | Size | Weight |  | Body | Size | Weight |
|---|---|---|---|---|---|---|
| Display | 80px | 700 |  | Body lg | 20px | 400 |
| H1 | 65px | 700 |  | Body | 17px | 400 |
| H2 | 50px | 700 |  | Body sm | 12px | 400 |
| H3 | 40px | 600 |  | Body medium | 16px | 500 |
| H4 | 35px | 600 |  | Body lg medium | 20px | 500 |
| H5 | 27px | 500 |  | Body menu | 16px | 500 |

Headings: line-height about 1.08, letter-spacing -0.02em, scaled responsively down from these desktop
sizes on web. Body line-height 1.5.

**The eyebrow technique, a signature.** A small uppercase label above a section heading: 13px, weight
700, letter-spacing 0.14em, colour `--blue` (muted variant `--g500`), margin-bottom 18px. Use it on
every major section.

**Hero and proof numerals** are oversized: 72 to 120pt in print, a large `clamp()` on web.

Bricolage Grotesque and IBM Plex Sans appeared in the earliest telehealth prototype and are not
brand fonts.

### 3.4 Spacing, radius, buttons

**Spacing scale, these steps only:** 2 · 4 · 8 · 12 · 16 · 20 · 24 · 32 · 40 · 48 · 60 · 80 · 96 ·
120 px. Component rhythm favours 8, 12, 16, 24. Section padding favours 60, 80, 96, 120. Container
max-width 1200px, horizontal padding `clamp(24px, 5vw, 80px)`, section vertical rhythm
`clamp(56px, 8vw, 110px)`. Breakpoints: Desktop 1920, Desktop 1440, mobile.

**Border radius:** 0 · 4 · 5 · 15 · 20 · 30 · 40 · 9999 px. Buttons and inputs 4 to 5. Chips and
small cards 15. Cards and panels 20. Large surfaces, footer band, feature blocks 30 to 40. Pills and
avatars 9999.

**Buttons.** Two shapes, four fills each. Base Satoshi 700 at 16px, padding about `14px 26px`, hover
lift `translateY(-1px)`, focus-visible `outline: 3px solid #B1BDFF; outline-offset: 2px`.
Rectangular (radius 4 to 5) for primary page actions, labelled like "Get in touch". Pill (radius
9999) for content and navigation actions, labelled like "Read Articles" with a trailing arrow. Fills:
Black, Blue primary (`#143DFF`, hover `#0F2ECD`), Outline or ghost, Text-only. **On navy, the primary
call to action is a white button with dark text.**

### 3.5 Header, footer, motion, accessibility

**Header.** Left, the triangle logo mark with wordmark. Nav at Body-menu 16px Medium with dropdowns:
Use Cases (Telehealth and Weight Loss, Connected and Digital Fitness, Weight and BMI Verification),
Technology, Pricing, Resources (Case Studies, Content Hub, Terms and Policies), Made-to-Measure,
About 3DLOOK. Right, a "Let's talk" call to action.

**Footer, the link section.** A full-width navy radial-glow band with rounded top corners at about 30
to 40px. Centred CTA band: heading in Display or H1 Satoshi Bold white, one of "Let's talk",
"Request a Demo", "Unlock Body Data"; muted subcopy; a white rectangular "Get in touch" button. The
"Unlock Body Data" variant uses two buttons, "Book a Consultation" white and "Explore Technology"
outline. Two centred outlined navy trust pills: HIPAA Compliant, GDPR. Then the link columns: the
triangle logo on the left, **What We Do** (FitXpress, Mobile Tailor, Technology, Case Studies),
**About 3DLOOK** (About Us, Content Hub, Careers), **Ready to get started?** with social icons
(Facebook, Instagram, X, LinkedIn, YouTube). Column headers in muted blue-gray, links in white.
Legal row, muted and small: the GDPR EU-representative notice on the left, Legal and Privacy Policy
on the right.

**Motion.** Scroll-reveal with stagger on section entry, smooth scroll behaviour, button hover lift,
transitions about 0.15s ease. No bounce or overshoot. Always honour
`@media (prefers-reduced-motion: reduce)`.

**Accessibility.** Body text meets AA contrast minimum. Never place light text on light imagery
without a scrim. Visible focus ring `#B1BDFF` at 3px with 2px offset.

### 3.6 Print and collateral variant

For a two-pager or a printed leave-behind, the print art direction uses a marginally warmer navy
`#0A1338`, ink `#0B0B0C`, muted `#5D6070`, with the same blue tints. On web, use the canonical values.
Electric blue `#143DFF` is identical everywhere.

### 3.7 Do and don't

**Do.** Keep electric blue as one sharp accent. Lead proof zones with oversized numerals. Use the
navy radial glow with texture. Prefer product imagery. Use the type scale and spacing steps exactly.
Use the eyebrow technique. White CTA button on navy. Honour reduced-motion.

**Don't.** Spread `#143DFF` across large fills. Use flat navy blocks. Use an icon where a product
asset fits. Invent a size or radius off-scale. Put light text on imagery without a scrim. Introduce
a font other than Satoshi. Resurrect `#2962FF` or Inter.

**Logo caveat.** Logo files, the exact triangle geometry, clearspace and minimum sizes are not in the
Figma export. Request the brand-mark asset kit from Vadim before reproducing the mark at small sizes,
and never rebuild it by eye.

### 3.8 Copy-paste tokens

```css
:root{
  --black:#000; --white:#fff; --blue:#143DFF;
  --blue-50:#ECEFFF; --blue-100:#D8DEFF; --blue-200:#B1BDFF; --blue-300:#8A9CFF;
  --blue-400:#4F6DFF; --blue-500:#143DFF; --blue-600:#0F2ECD; --blue-700:#0B2299;
  --blue-800:#08186B; --navy:#050F40;
  --g50:#F9F9F9; --g100:#F2F2F2; --g200:#E5E5E5; --g300:#D1D1D1; --g400:#A8A8A8;
  --g500:#808080; --g600:#666666; --g700:#4C4C4C; --g800:#333333; --g900:#1A1A1A;
  --ink:#1A1A1A;
  --r-4:4px; --r-5:5px; --r-15:15px; --r-20:20px; --r-30:30px; --r-40:40px; --r-pill:9999px;
  --s-8:8px; --s-12:12px; --s-16:16px; --s-24:24px; --s-32:32px; --s-40:40px;
  --s-60:60px; --s-80:80px; --s-96:96px; --s-120:120px;
  --maxw:1200px; --pad:clamp(24px,5vw,80px);
  --font:'Satoshi','Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
}
```

---

## 4. Use-case library

### 4.0 How to read this section, and the boundary rule

Eleven segments, each with the same eight fields. Sources: `audience.md` (hook and what not to say),
`icp-detail.md` (buyer titles, revenue thresholds, pains, triggers), `proof-points.md` (every
number), `case-studies/` (every customer name and customer number).

**Respect the vertical boundaries.** Telehealth copy does not bleed into online-pharmacy compliance.
Fitness copy does not bleed into GLP-1 clinical workflows. Wellness copy does not bleed into clinical
decisioning. Each vertical page and each deck holds its own lane, otherwise two assets compete for
the same query and the same buyer, and neither reads as written by someone who knows the market.

Note that `audience.md` treats telehealth and GLP-1 weight loss as one segment with two lenses. This
playbook splits them into 4.1 and 4.2 because they need different decks, but they share proof and
they must not contradict each other.

**Proof-availability reality, read this before promising a deck.** Three tiers:

| Tier | Segments | What that means for collateral |
|---|---|---|
| Has a named customer with a number | Telehealth and GLP-1 (Yazen), online pharmacy (UK Meds) | A case card and a vertical proof point are possible, subject to naming permission |
| Has a use-case file and market sizing, no customer | Insurance, health plans and wellness, bariatric, occupational health, clinical trials, digital fitness | The vertical case slot stays empty and is recorded. Build on workflow, governance and the product proof set |
| No use-case file, no proof | Plastic surgery, BCRL | Needs proof and needs a use-case file. Flag to Vadim before any commitment |

**Market sizing figures are internal.** The TAM and SAM ranges in `proof-points.md` come from the
Brainstorm deck and are marked illustrative. Use them for prioritization and internal business cases.
Do not put them in customer-facing collateral.

---

### 4.1 Telehealth and virtual care

- **ICP.** Virtual-first clinics, telehealth platforms, longitudinal care and remote patient
  monitoring programs, cardiometabolic health platforms. Series A through public, 50 to 5,000
  employees, **$2M+ annual revenue**. Typically 500+ active members with repeat check-ins. Geo: USA,
  Canada, UK, Germany, UAE, Australia.
- **Buyer titles.** Founder or CEO, Chief Medical Officer or Medical Director, Head of Clinical
  Operations, Head of Member Engagement or Retention, Head of Product, CTO, Head of Outcomes and
  Program Insights.
- **Core pain.** Remote programs run on repeat check-ins, and the data underneath is shaky. Self
  report and occasional progress photos are inconsistent, easy to skip and hard to compare across
  scans. Clinical teams cannot separate real change from measurement noise. Manual intake slows
  scaling and loads the clinical team.
- **FitXpress fit.** A structured intake and documentation layer inside the existing app flow. Two
  photos return 80+ measurements and body composition, and because variance stays `< 1 cm`, the
  trend a care team reads is change rather than noise.
- **Hero outcome.** *Verify body progress remotely to boost retention, reduce drop-off, and prove
  program ROI.* Shorter variant: *Make body progress visible before members drop off.*
- **Proof to use.** Yazen, 34,000 scans in 2025, weight-loss management support (naming subject to
  permission, see section 9 item 5). 80+ measurements. Under 45 seconds from two photos. 96 to 97%
  accuracy against expert manual measurement, typical absolute error 1.5 to 2.0 cm. Repeatability
  `< 1 cm`, 95%+ consistency. Weight estimation ±3.5% average error. HIPAA maintained, GDPR
  principles, AWS S3 SSE-S3 at rest, TLS in transit, photos deleted immediately or within 30 days
  per client policy, no personal identifiers processed.
- **What NOT to say.** No diagnostic claims. Do not position as a DEXA or calibrated-scale
  replacement. Do not imply eligibility decisioning. Keep separate from UK online-pharmacy BMI
  compliance unless the piece is explicitly the bridge.
- **Deck localization.** Problem slide on trust in the trend rather than one-time accuracy. Journey
  slide on the 30, 60, 90 day check-in cadence. Outputs slide member-facing. Accuracy slide leads
  with repeatability.
- **Landing page.** The live benchmark page
  `/structured-body-data-for-telehealth-digital-health-programs/` already covers this vertical well.
  Extend rather than duplicate. CTA by stage: TOFU "Explore how mobile body scanning works", MOFU
  "See how FitXpress supports remote progress tracking", BOFU "Book a demo" with "See sample outputs"
  as the secondary.

---

### 4.2 Weight loss and GLP-1 programs

- **ICP.** GLP-1 prescription platforms, metabolic and obesity platforms, coaching apps treating
  weight management, employer-sponsored metabolic health programs. **$2M+ annual revenue.** Geo: USA,
  UK, Germany, Australia, Canada, UAE.
- **Buyer titles.** Founder or CEO, Chief Medical Officer, Head of Clinical Operations, Head of
  Member Engagement, Head of Outcomes, Growth and Revenue Operations.
- **Core pain.** Members drop off when progress is not visible, and weight alone hides what matters
  because it does not separate fat from lean mass. GLP-1 prescribing needs reliable baseline and
  follow-up body metrics. Rising customer acquisition cost with weak engagement and early churn.
  Payers and enterprise partners increasingly expect measurable, defensible outcomes.
- **FitXpress fit.** Repeat scans that make composition change visible between clinical assessment
  points, feeding both member engagement and outcomes reporting.
- **Hero outcome.** *Make body progress visible between check-ins, so programs keep members past day
  90.* Rewrite the connector to avoid "so": *Make body progress visible between check-ins, helping
  programs keep members past day 90.*
- **Proof to use.** Same set as 4.1. Yazen is the anchor. Lean-mass preservation tracking is a
  buyer KPI worth naming, framed as what the data supports rather than what the product proves.
- **What NOT to say.** No claim about clinical outcomes of GLP-1 therapy. No eligibility or dosing
  implication. No lean-mass-preservation efficacy claim: FitXpress documents the measurement, the
  clinical interpretation belongs to the care team.
- **Deck localization.** Problem slide on day-90 drop-off. A dedicated slide on the progress and
  target-weight 3D visualization as an engagement mechanic. Outcomes slide on retention, adherence
  and outcomes reporting to payers.
- **Landing page.** Its own page, linked from and to the telehealth page. CTA: MOFU "Review the
  buyer checklist", BOFU "Book a demo".

---

### 4.3 Online pharmacy and remote prescribing (BMI verification)

- **ICP.** Online pharmacies and remote-prescribing platforms dispensing GLP-1 and weight-loss
  medication, needing to verify eligibility (a Body Mass Index threshold, typically 27 or above with
  a comorbidity, or 30 or above) without a visit. 50 to 1,000 employees, **$2M+ annual revenue.**
  **The UK is the priority market**, plus international telehealth providers operating in the UK.
- **Buyer titles.** Head of Compliance and Risk, Chief Medical Officer, Clinical Operations Director,
  Head of Clinical Governance, Founder or CEO, Product Manager, CTO.
- **Core pain.** Patients misreport weight and BMI to qualify. Manual photo review is subjective and
  inconsistent. UK regulators are tightening scrutiny of remote GLP-1 eligibility. High intake
  volumes overload the clinical team, and incorrect verification carries prescribing, legal and
  reputational exposure.
- **FitXpress fit.** Verification inside the order flow, with a structured record behind it. Smart
  Scales compares self-reported weight against the estimate and flags a mismatch for clinician
  review. Integration Pattern B fits this vertical: the user submits photos, eligibility is validated
  server-side, body metrics are never shown to the user, and the compliance team keeps an audit trail.
- **Hero outcome.** *Verify BMI inside the order flow to cut fraud, speed approvals, and stay
  audit-ready.*
- **Proof to use.** UK Meds, 7,500 scans in 2025, BMI verification for online pharmacy ordering
  (naming subject to permission). Weight estimation ±3.5% average error. Under 45 seconds, two
  photos. Repeatability `< 1 cm`. Audit and compliance posture from `compliance.md`. Pattern B from
  `tech-spec.md`.
- **What NOT to say.** Never imply automated eligibility or prescribing decisions. Never guarantee
  compliance: "supports compliant workflows", never "makes you compliant". Never "detects fraud",
  always "flags discrepancies for review". Name UK regulators only when the piece is genuinely about
  the UK market, and expand them at first use (Medicines and Healthcare products Regulatory Agency,
  MHRA; Care Quality Commission, CQC).
- **Deck localization.** Problem slide on manual photo review and the regulatory tightening. A
  workflow slide showing Pattern B explicitly, including who reviews a flagged scan. Compliance and
  audit trail elevated to a deciding slide rather than a footnote.
- **Landing page.** `/for-bmi-verification/` exists at about 659 words with no FAQ and no cases. It
  is the priority rewrite. CTA: MOFU "See how BMI verification fits your order flow", BOFU "Book a
  demo".

---

### 4.4 Insurance underwriting (life and disability)

- **ICP.** Life and disability insurers, group benefits carriers, reinsurers, insurtech and digital
  distribution platforms, accelerated and digital underwriting teams. Large enterprise, typically
  5,000+ employees, **$5M+ annual revenue.** Geo: US core, UK and EU, Canada, UAE, Australia.
- **Buyer titles.** Chief Underwriting Officer or VP Underwriting, Chief Medical Officer, Chief Risk
  Officer or Head of Risk and Analytics, Head of Digital Innovation, Population Health Director, CTO,
  Compliance and Fraud Prevention.
- **Core pain.** Accelerated underwriting removed friction and created an evidentiary gap. Self
  reported height, weight, build and BMI can be incomplete, inconsistent or intentionally
  misrepresented, which affects risk classification, pricing accuracy and fraud exposure. The
  alternatives (paramedical exams, attending physician statements, manual cross-checks) reintroduce
  the delay accelerated programs were designed to remove.
- **FitXpress fit.** A structured digital evidence layer: remote guided capture producing repeatable,
  auditable body data that supports underwriter review, applicant triage and fraud-prevention
  workflows, without becoming a decisioning engine.
- **Hero outcome.** *Verify body metrics remotely to issue faster, cut rework, and strengthen
  auditability.* The shipped deck headline is *Stronger evidence, faster underwriting.*
- **Proof to use.** No FitXpress insurance customer exists. **Needs proof, flag to Vadim** for a
  case card, a quote or a reference. Build on: 96 to 97% accuracy against expert manual measurement,
  error margin 1.5 to 2.0 cm, repeatability `< 1 cm` and 95%+ consistency, weight estimation ±3.5%,
  80+ measurements, under 45 seconds, and the full governance set (encryption, configurable
  retention, no personal identifiers, logging of scan status, timestamps, quality flags and failure
  reasons, HIPAA business associate agreements where applicable). External context may be cited with
  a named source and a link: CDC research on self-reported obesity prevalence, Munich Re on BMI
  misrepresentation as a driver of misclassification in accelerated programs. **Verify both at source
  and get external-use approval before either appears in a deck**, per the shipped deck's own open
  items.
- **What NOT to say.** Never automated underwriting. Never automatic fraud detection. Never
  standalone decisioning. Never employment screening. Never "best-in-class repeatability", which the
  shipped deck currently contains and which is a banned word. HIPAA applicability to life insurers
  varies, so do not assert it as given; confirm per prospect.
- **Deck localization.** This is the exemplar deck, already written. Reuse its shape: alternatives
  and their limitations on the problem slide, five outcome cards with "driven by" and "track with"
  on the outcomes slide, a five-stage underwriting journey, and the integration boundary slide that
  keeps the carrier in control of decisioning.
- **Landing page.** Does not exist. Build after the case-evidence gap is resolved. CTA: MOFU
  "Review the evidence-workflow checklist", BOFU "Talk to 3DLOOK about your underwriting workflow".

---

### 4.5 Health plans and employer wellness (rewards verification)

- **ICP.** Health insurers running wellness incentive programs, Medicare Advantage providers,
  self-insured employers, employer benefit and wellness platforms, population-health vendors. Large
  enterprise, **$5M+ annual revenue.** Geo: USA, Canada, UK, Germany, UAE, Australia.
- **Buyer titles.** CHRO, Head of Wellness or Director of Wellbeing, VP Population Health, Chief
  Medical Officer, Health Plan Operations Director, Compliance and Risk, Wellness Program
  Administrator.
- **Core pain.** Manual wellness verification is an administrative load and self report is
  unreliable. Hybrid and remote workforces complicate onsite screening. Complex verification cuts
  participation, delayed verification weakens the reward's motivational effect, and disputes and
  inconsistent submissions undermine fairness and trust.
- **FitXpress fit.** Remote, standardized, audit-ready verification of a biometric milestone, with
  fraud-prevention support and consistent treatment across a distributed population.
- **Hero outcome.** *Verify wellness progress remotely to reduce disputes, boost participation, and
  improve program reporting.*
- **Proof to use.** No customer. **Needs proof, flag to Vadim.** Bupa Rewards is noted internally as
  a public reference for what a good program looks like; it is not a 3DLOOK customer and must never
  be presented as one. Build on the product proof set and the governance set. Participation-rate and
  dispute-rate figures do not exist: use them as "track with" metric categories on the outcomes
  slide, never as claimed results.
- **What NOT to say.** No medical or diagnostic claims. Never imply the reward or eligibility
  decision is automated. Keep every benefit claim soft: supports, may reduce, can help.
- **Deck localization.** Outcomes slide on participation, dispute volume and cost per validated
  check-in. A fairness and consistency slide, which is what this buyer actually worries about.
  Compliance and data-governance slide elevated.
- **Landing page.** Does not exist. CTA: MOFU "See how remote verification fits an incentive
  program", BOFU "Book a demo".

---

### 4.6 Bariatric and metabolic clinics (pre-qualification)

- **ICP.** Bariatric surgery centres, hospital programs, multi-site surgical networks, metabolic and
  obesity clinics. Mid to large hospital systems and surgical-centre chains. Geo: US, EU.
- **Buyer titles.** Director of Operations, Medical Director, VP Patient Access, COO for multi-site.
- **Core pain.** Long consult waitlists, a high rate of late-stage disqualification that wastes
  consult slots, pre-authorization backlogs, and staff time consumed per pre-authorization.
- **FitXpress fit.** Remote pre-qualification before the consult, producing a structured record that
  supports pre-authorization documentation.
- **Hero outcome.** *Pre-qualify patients remotely to reduce wasted consults, speed pre-auth, and
  improve conversion to procedures.*
- **Proof to use.** No customer. **Needs proof, flag to Vadim.** Product proof set only. KPI
  categories to offer as "track with": consult-to-procedure conversion, pre-authorization cycle time,
  wasted consult rate, staff time per pre-authorization.
- **What NOT to say.** Never surgical candidacy determination. Never a claim about anaesthetic or
  surgical risk. Never guaranteed payer approval.
- **Deck localization.** Journey slide from enquiry through remote pre-screen to consult booking.
  Operational slide on throughput and staff time.
- **Landing page.** Later. This vertical is better served first by a use-case one-pager for BD.
  `brand-assets/product-info/use-cases/fx-bariatric-pre-auth.md` exists as the starting point.

---

### 4.7 Occupational health and pre-employment screening

- **ICP.** Occupational health providers, workforce screening vendors, workers' compensation and
  absence administrators, large multi-site employers. Mid to large. Geo: US, EU.
- **Buyer titles.** VP Operations or COO, Chief Medical Officer, Director of Clinical Services, Head
  of Occupational Health.
- **Core pain.** Throughput per clinic per day, rescreen and rework rates, time to clearance, and
  audit readiness across sites that each do it slightly differently.
- **FitXpress fit.** Standardized remote intake that reduces variability between sites and reviewers,
  with a documented record.
- **Hero outcome.** *Standardize screening intake remotely to increase throughput, reduce rescreens,
  and speed clearance decisions.*
- **Proof to use.** No customer. **Needs proof, flag to Vadim.** Product proof set only.
- **What NOT to say.** This is the vertical where a claims slip is most expensive. Never
  fitness-for-duty determination, never clearance decisioning, never a hiring decision, never a
  medical assessment. The framing is intake standardization and documentation; the determination is
  the provider's. Employment screening is explicitly excluded from what FitXpress claims.
- **Deck localization.** Multi-site standardization slide. Audit-readiness slide. Journey slide from
  candidate invitation to clearance review.
- **Landing page.** Later. Get a legal read on the framing before any public page in this vertical.

---

### 4.8 Clinical trials (CROs and pharma sponsors)

- **ICP.** Contract Research Organizations (CROs), pharma sponsors running metabolic and obesity
  trials, academic research networks, decentralized clinical trial (DCT) platforms. Global.
- **Buyer titles.** Director of Clinical Operations, VP Decentralized or Hybrid Trials, Head of Site
  Management, Director of Data Management.
- **Core pain.** Site-to-site variability in anthropometric measurement, coordinator time per visit,
  retention and dropout, screen-failure rate, and audit findings on measurement variability across
  sites.
- **FitXpress fit.** Standardized anthropometric capture with a timestamped, structured record that
  reduces visit burden and inter-site variability.
- **Hero outcome.** *Standardize anthropometrics across sites and reduce visit burden to improve data
  quality and retention.*
- **Proof to use.** No customer. **Needs proof, flag to Vadim.** Product proof set, and the
  repeatability figures specifically, which are the argument here. The published clinical-trials
  article (`brand-assets/past-articles/blog/clinical-trials-anthropometric-measurement.md`) is the
  best existing model for compliance scoping and the operational-not-clinical framing. Read its
  `known_issues` frontmatter to avoid repeating its M1 and M2 slips.
- **What NOT to say.** Never endpoint validation. Never a claim of protocol or regulatory compliance.
  Never a Good Clinical Practice (GCP) or Food and Drug Administration (FDA) qualification claim.
  Endpoint validation stays with the sponsor; FitXpress standardizes and documents capture. Expand
  every regulator and standard at first use, which is exactly where this vertical's drafts slip.
- **Deck localization.** Variability-across-sites problem slide. Data-management and export slide
  (Electronic Data Capture, EDC, and electronic Clinical Outcome Assessment, eCOA, integration
  questions will come up). Audit-trail slide.
- **Landing page.** Later. The article already covers the top of the funnel for this vertical.

---

### 4.9 Connected and digital fitness

- **ICP.** Connected fitness platforms, digital fitness and coaching apps, virtual personal training,
  fitness subscription platforms, corporate wellness and fitness platforms. Series B to public,
  **$1M+ annual revenue**, strong recurring-subscription focus. Geo: US, UK, Canada, Germany, UAE,
  Australia, Nordics.
- **Buyer titles.** Founder or CEO, Chief Product Officer, Head of Growth, VP User Engagement or
  Retention, CTO, Product Manager.
- **Core pain.** Users lose motivation without visible progress, churn after onboarding is high,
  personalization is limited to surveys and stated goals, and the market is crowded and competing on
  user experience. Rising acquisition cost demands stronger engagement.
- **FitXpress fit.** Visible transformation and body-data personalization as an engagement and
  premium-tier mechanic. The tone here is lighter and less clinical than every other segment in this
  library.
- **Hero outcome.** *Give members visible body progress, and give the product a reason to be
  renewed.*
- **Proof to use.** `proof-points.md` holds no named fitness customer. Names circulating elsewhere
  (in the sales deck and in the telehealth page draft) are **not** in `proof-points.md` or
  `case-studies/`, so they are unusable until Vadim adds them with permission. **Needs proof, flag
  to Vadim.** Build on 80+ measurements, body composition outputs, the target-weight 3D
  visualization, side-by-side longitudinal comparison, under 45 seconds, and repeatability `< 1 cm`.
- **What NOT to say.** No medical, diagnostic or clearance language at all. Do not blur into GLP-1
  clinical workflows or wellness-rewards verification. This is the one vertical where the clinical
  register actively hurts the pitch.
- **Deck localization.** Engagement and retention outcomes slide. A visual-progress slide carrying
  more weight than the accuracy slide. Shorter deck overall, 12 to 15 slides.
- **Landing page.** `/fitxpress/for-connected-and-digital-fitness/` exists at about 1,352 words with
  no FAQ and no schema. Two jobs: add the FAQ block with FAQPage schema, and resolve the URL, which
  currently sits on a `/fitxpress/` path level that redirects. Coordinate the redirect with Vadim.
  CTA: TOFU "Explore how mobile body scanning works", BOFU "Book a demo".

---

### 4.10 Plastic surgery clinics (Turkey first)

- **ICP.** Plastic surgery clinics and aesthetic medicine centres. Large (10+ surgeons, 50+
  procedures a month) or mid-sized (3 to 10 surgeons, 20 to 50 procedures a month). **$1M+ annual
  revenue**, premium pricing. **Turkey is the priority geography** for medical tourism, then USA,
  Canada, UK, Germany, UAE, Australia.
- **Buyer titles.** Clinic Owner or Director, Plastic Surgeon, Project Manager or Technical Lead.
- **Core pain.** High drop-off between consultation and surgery because patients are disqualified at
  the last moment on BMI. Wasted in-person consult slots on unqualified patients. No reliable remote
  pre-screen, and ordinary scales are not enough. Patients misstate or do not know their BMI. Fat
  distribution and composition affect surgical outcome but are poorly measured before the visit.
- **FitXpress fit.** Remote pre-qualification on BMI and body composition before travel or a consult,
  and better structured input for surgical planning.
- **Hero outcome.** *Pre-qualify international patients before they book a flight.*
- **Proof to use.** No customer, no use-case file, and no vertical proof. **Needs proof and needs a
  use-case file (`use-cases/fx-plastic-surgery.md` does not exist), flag to Vadim.** Do not build a
  deck for this vertical until at least the use-case file exists, because the vertical-context slot
  (who signs off, how the medical-tourism funnel actually runs, what the coordinator does with a
  flagged scan) cannot be filled from any current source.
- **What NOT to say.** Never a diagnostic claim. Never an anaesthesia-risk or surgical-risk claim.
  Never a replacement for surgeon assessment. The framing is support for pre-screening and planning.
- **Deck localization.** Not yet. When it is unblocked: a medical-tourism funnel journey slide, and a
  coordinator-workflow slide, since the coordinator is the daily user.
- **Landing page.** Not yet.

---

### 4.11 BCRL detection and monitoring (oncology survivorship)

- **ICP.** Oncology survivorship platforms, breast-cancer aftercare clinics, remote patient
  monitoring providers, cancer care networks, lymphedema and rehabilitation teams, cancer treatment
  centres and hospital systems. **$2M+ annual revenue.** Geo: USA, Canada, Germany, UAE, Australia.
  (BCRL is breast cancer-related lymphedema.)
- **Buyer titles.** Chief Medical Officer, Oncology Program Director, Survivorship Care Leader, RPM
  Director, Rehabilitation and Lymphedema Specialist, Digital Health Product Manager, CTO.
- **Core pain.** BCRL is underdiagnosed early. Tape measurement is inconsistent and hard to reproduce
  at home. In-clinic monitoring does not scale and long-term self-monitoring adherence is weak.
  Subtle volumetric and asymmetry changes are hard to capture, and documentation is slow and manual.
- **FitXpress fit.** Remote longitudinal monitoring support and reproducible digital body records,
  with engagement through visual 3D comparison.
- **Hero outcome.** Not yet writable. Any outcome line here would rest on a volumetric-asymmetry
  tracking claim that no current proof point supports.
- **Proof to use.** **None. This segment has no proof point, no use-case file, and `icp-detail.md`
  records explicitly that the clinically relevant metric (volumetric asymmetry tracking accuracy) is
  absent from `proof-points.md`.** Flag to Vadim. No deck, no page, no one-pager until a validated
  metric exists and Whitney has reviewed the framing.
- **What NOT to say.** Never detect or diagnose lymphedema or BCRL. Never replace clinical
  assessment. "Supports monitoring workflows" is the only safe frame. This is the most
  compliance-sensitive vertical in the whole portfolio.
- **Deck and landing page.** Blocked pending proof and a Whitney review. Recommendation: treat this
  as a research request to product before it is treated as a marketing request.

---

## 5. Deck build playbook

### 5.1 The principle

A vertical deck is not written from scratch. About 60% of it is a fixed spine of product truth that
is identical in every vertical, and about 40% is localization. Building it any other way is how two
decks end up quoting two different numbers for the same thing.

The exemplar is
`/home/vadim_prod/3dlook-marketing/fitxpress-insurance-underwriting-deck-copy.md`. It is 29 slides
built by localizing the telehealth deck, and it documents its own text-fit review and its own open
items at the end. Copy that discipline, and copy its structure. Do not copy its two banned-word
slips (see section 9).

### 5.2 Deck lengths

| Deck | Slides | Use |
|---|---|---|
| Demo deck | 19 core + appendix, 25 to 29 total | The main vertical asset, sent after a demo |
| First-call deck | 10 to 12 | Slides 1 to 8 plus compliance and the close |
| Leave-behind / two-pager | 2 pages | Hero, outcomes, how it works, proof, compliance, contact |
| Conference or keynote | 8 to 10 | Problem, why now, workflow, proof, close |

### 5.3 The 19-slide core

**F** = fixed, product truth, changes only when `proof-points.md` changes.
**L** = localize per vertical.

| # | Slide | F/L | What goes on it |
|---|---|---|---|
| 1 | Cover | L | Outcome headline in the vertical's language, three proof points (2 smartphone photos, results in under a minute, no specialized hardware), the "Built for [vertical]" label. Highly visual, minimal text |
| 2 | The industry problem | L | Why existing approaches fail **in this vertical**. Four alternative-method blocks, each with what it is good at and its limitation. Close with a "The result" statement that names the business consequence |
| 3 | Business outcomes | L | Five outcome cards. Each: name, one sentence, two "Driven by" bullets, two or three "Track with" metrics. **"Track with" names metric categories, never claimed results.** Testimonial slot stays empty unless an approved quote exists |
| 4 | How it works | F | Four stages: user inputs, guided photo capture with pose and clothing validation, processing with photo deletion, structured return to your platform |
| 5 | What each scan returns | F | 80+ measurements, body composition (BMI, BMR, body fat %, lean mass, fat mass), 3D model, progress comparison, validation outputs (pose quality, clothing classification, Smart Scales mismatch flag) |
| 6 | Accuracy and repeatability, scoped | F | Reframe to "accurate enough for which decision?", the four conditions, then the figures from `proof-points.md`. Lead with repeatability for any longitudinal vertical. Never "independent", "validated", "third-party" or "best-in-class" |
| 7 | Comparison | L | Compare by role. FitXpress against the alternative **this buyer actually uses** (self report, in-clinic DEXA or BIA, consumer photo apps, manual review). Never a clean sweep across every row |
| 8 | Where it fits in the workflow | L | The vertical's own five-stage journey, with the FitXpress step marked and the human decision point marked |
| 9 | The core workflow feature | L | The one capability this vertical buys: progress comparison, disclosure verification, eligibility pre-check, inter-site standardization |
| 10 | The end-user experience | L | Adoption and completion in this vertical's flow. Or, where outputs are internal only (pharmacy Pattern B, underwriting), say so plainly and keep the slide short |
| 11 | Built for [vertical] operations | L | The operational requirements this buyer will ask about: volumes, review queues, exception handling, reporting |
| 12 | Reliability in production | F | Uptime posture, consistency across body types, lighting and capture environments, error handling |
| 13 | Built-in quality checks | F | Real-time pose validation, clothing detection (sport, regular, oversized), live capture, Smart Scales mismatch flag. **State the limit of each control** |
| 14 | Integration architecture | F | The "we provide / you build" boundary, the two integration patterns, API and the three SDKs. The boundary slide is what makes the buyer feel in control |
| 15 | Admin Panel | F | Centralized view and management of scan results, for teams that do not want to build a dashboard |
| 16 | What the team sees | L | Member-facing, internal-only, or both. Real white-label screenshots where permission allows |
| 17 | Security, privacy, compliance | F, with an L intro | The data-flow diagram, the controls list, HIPAA and GDPR posture. Localize only the opening sentence to the vertical's regulatory context |
| 18 | Pricing | F | The public price signal and "no integration fee". Never the internal per-request table. Check `/pricing/` on the day the deck ships |
| 19 | How teams evaluate this | F | Three stages: demo evaluation, decision discussion, contracting. Ends on a concrete next step |

**Appendix** (slides 20 onward): integration examples (onboarding and scan entry, the
customer-controlled wrapper, SDK capture, post-scan processing, output UI, internal-only
consumption), About 3DLOOK, contacts.

### 5.4 How to localize, in order

1. **Fix the segment.** Open section 4. Read the segment's hook and its "what NOT to say" before
   writing a line.
2. **Check the proof tier.** Is there a named customer with a number? If not, the case card and the
   testimonial slot stay empty and get recorded. Do not fill them with an adjacent vertical.
3. **Write slide 2 from the buyer's alternatives**, not from our features. What does this team do
   today, and what specifically breaks?
4. **Write slide 3 from the buyer's KPI list** in `icp-detail.md`. Outcomes are hedged (supports,
   may reduce, can help). "Track with" is a measurement category.
5. **Rewrite only the L slides.** Copy the F slides verbatim from the most recent approved deck.
   Every F-slide edit is a change to product truth and needs Vadim.
6. **Run the guardrails pass as its own step.** The 11 principles plus M1 and M2. Not while drafting.
7. **Run the AI-tells sweep** with `--channel page`, fix every hard fail, then read it yourself.
8. **Write the text-fit review.** Slide by slide, is the new copy longer than what it replaces? The
   exemplar deck's review is the model, and roughly 15% is the tolerance before a layout change is
   needed.
9. **Write the open items block.** Every unresolved number, every unapproved quote, every claim
   needing Whitney. Per guardrail 11, flag rather than decide.
10. **Route it.** Vadim for numbers, Whitney for regulated claims, Asselya for editorial, Katerina
    for competitive framing.

### 5.5 Deck design rules

Land the design system, do not reinvent it. Navy `#050F40` with the radial glow on the cover, section
dividers, proof bands and the close. White on content slides. Electric blue `#143DFF` on one thing
per slide, usually the number. Satoshi throughout, with the eyebrow label on every content slide
(13px, 700, letter-spacing 0.14em, in blue). Proof slides lead with an oversized numeral, because the
number is the hero. Prefer the three carrier assets (3D body-scan render, guided-capture phone UI,
Admin Panel in a browser frame) over icon grids. Cards at 20px radius, chips at 15px. Confidentiality
footer on every slide with the current month and year.

One text rule that saves a rebuild: write to the layout you have. If the replacement headline is much
longer than what it replaces, shorten the headline rather than shrinking the type.

### 5.6 Roadmap discipline

Only mention what is shipped or in progress. Currently safe to mention: clothing detector (available
in the API), anti-fraud live capture (in progress, not released), audit IDs and logs (in release,
further development in progress). Do not promise dates for height detection, Smart Scale accuracy
improvements, the accuracy or landmark-detector model upgrade, or full SDK branding customization.
Confirm current status with Max Kucherenko before any roadmap slide ships, since this list moves.

---

## 6. Landing-page build playbook

### 6.1 Route it through the pipeline

Pages that live on 3dlook.ai go through the `page-builder` skill (`/page [vertical] [gate|build|judge|handoff|full]`),
which enforces four gates and keeps every page at the same standard. Nika owns the brief, the copy
decisions and the final quality call. The pipeline enforces the parts that are easy to skip under
deadline.

| Gate | Blocks | The test |
|---|---|---|
| **G-I** | The page existing at all | A use-case file, **two or more publishable cases from that vertical**, real demand, five facts absent from the parent page, and the 60% uniqueness rule |
| **G-A** | Writing | Placement, URL, cannibalization against existing pages, and the Search Console baseline all settled |
| **G-T** | Publishing | Technical: schema, canonical, Yoast title and description, breadcrumbs, single H1 |
| **G-J** | Publishing again, on quality | A **blind** judge in a fresh subagent, 100-point page scorecard, threshold 85, maximum three rounds. Publishing below 85 without flagging it is not allowed. `quality-controller` is not a substitute: it is neither blind nor page-shaped |

**Read this before promising a vertical page.** G-I currently blocks almost every FitXpress vertical,
because it wants two publishable cases and every FX vertical has at most one. The options are a
second case, an approved reference, or a recorded G-I waiver from Vadim. Do not quietly proceed.

**URL structure, two hierarchies of different depth.** The homepage is the FitXpress parent
(`/fitxpress/` redirects to `/`), so FX vertical pages sit at `/for-{vertical}/` with two-level
breadcrumbs. Mobile Tailor has its own parent, with `/mobile-tailor/for-{vertical}/` beneath it and
three-level breadcrumbs. Never invent a `/fitxpress/` path level.

Artifacts go to `workspace/pages/{slug}/`.

### 6.2 The section map, 17 slots

The same 17 slots the pipeline enforces. Use this map when writing a brief, reviewing a draft, or
building a campaign landing by hand.

| # | Slot | The rule |
|---|---|---|
| 1 | **Breadcrumbs** | Two levels for FitXpress (`Home → [Vertical]`), three for Mobile Tailor. Match what live pages declare. Never a middle level that resolves to a redirect |
| 2 | **H1** | `[Outcome in the vertical's terms] for [vertical]`. One H1. Primary query in it and in the first 100 words. No "best", no "most accurate", no banned words |
| 3 | **Hero and a vertical proof point** | One sentence on what the product does here, and a number from **this** vertical. The company-wide 112,100 scans figure does not work in a vertical hero |
| 4 | **Vertical context** | The slot the page exists for. Three to five specifics only someone who has worked in this market knows: which regulators actually come up, who signs off and who blocks, the procurement cycle, the units, the export formats, the seasonality. Source: the use-case file and the BD owner |
| 5 | **Pains of this vertical** | From the use-case file and the `audience.md` hook, in the buyer's phrasing. Then honour that segment's "what NOT to say" |
| 6 | **What it is here, and the boundary** | Scope in the vertical's own words: what is captured, what is returned, what is documented. Then one boundary sentence: *FitXpress is not positioned as a medical device.* One negative, once |
| 7 | **Where the workflow differs** | Not the whole flow. The two or three steps that run differently here: consent capture, retake logic, who reviews a flagged scan, how the record is filed |
| 8 | **Compliance and data governance** | For a regulated vertical this is the deciding block. HIPAA and GDPR posture, encryption at rest (AWS S3 SSE-S3), retention (immediate or within 30 days per customer policy), no personal identifiers, consent handling, audit trails, `privacy@3dlook.me`. Every control stated with its limit |
| 9 | **Accuracy, scoped** | The reframe, then the four conditions, then figures from `proof-points.md` only. No bare percentage. Never the three reserved words |
| 10 | **Cases from this vertical only** | Two cards minimum, each with a number from `case-studies/`, linked to `/case-studies/`. A case from an adjacent vertical breaks the page's promise. Mobile Tailor customer ARRs never appear anywhere |
| 11 | **Customer quote from this vertical** | Name, role, company, only where the use is approved. No approved quote means the slot is dropped and recorded. Never an invented name or testimonial |
| 12 | **Integration, formats, support** | API, web and mobile SDKs, web widget, CSV export, 3D model export, what it plugs into here (EHR or patient portal, benefits platform, order management), white-label options, implementation support. The signal is "we are already inside your environment" |
| 13 | **Vertical FAQ** | The questions asked here and nowhere else. Ships with FAQPage schema. See 6.3 |
| 14 | **Price signal** | Name the entry tier and link to `/pricing/`. Mention the trial where it applies. Never the internal per-request rates |
| 15 | **Primary action and form** | One action in the site's own language, visible without scrolling and repeated at the end. Minimal fields, visible consent, a confirmation state |
| 16 | **Soft alternative and sibling verticals** | For buyers not ready to talk: the accuracy framework article, the vertical's hub article, a checklist. Then cards for two sibling verticals and a link up to the parent |
| 17 | **Hidden technical layer** | Service or Product schema with `audience` and `areaServed`, FAQPage on the FAQ block, BreadcrumbList on the crumbs, canonical to self, Yoast title 60 characters or fewer, description 155 or fewer, clean URL |

**Campaign landing variant.** Same spine, shorter: slots 2, 3, 5, 6, 9, 13 trimmed to four or five
questions, 15. One message, one action, no sibling-vertical cards competing with the campaign.

### 6.3 FAQ guidance for search and answer engines

The FAQ is where a landing page earns citations in answer engines, and it is the slot most often
skipped. Only one page on the whole site currently ships FAQPage schema.

- **Ten to thirteen questions.** The benchmark telehealth page runs 13. Below about eight, the block
  stops carrying weight.
- **Answer-first.** Each answer opens with a 40 to 60 word capsule that answers the question
  completely on its own, then adds detail. An answer engine quotes the first sentences.
- **Number first where a number exists.** "Structured body data returns in about 45 seconds from two
  guided smartphone photos" beats "Results are fast."
- **Vertical questions only.** Regulatory posture, licensing, data residency, retention, who owns the
  data, what happens on a failed scan, what a pilot looks like, what the integration costs the dev
  team. General product questions belong on the product page.
- **Source them from real objections**, from `faq.md` and from the BD owner for that market, not from
  imagination. Nick's call transcripts in Drive are the best raw material.
- **The boundary questions are mandatory** on every health vertical: "Is it a medical device?" (no,
  it provides structured body data that supports workflow, and it is not a diagnostic device or a
  replacement for clinical judgment) and "Where do the photos go?" (the flow, the deletion policy,
  who controls retention).
- **FAQPage schema on the block**, modelled on the telehealth page. Mark it up, or the block is doing
  half its job.
- Two more page-level rules that help both humans and answer engines: open **every** major section
  with a 40 to 60 word answer-first capsule, and keep a visible "Last updated" line.

### 6.4 CTA discipline by funnel stage

Match the call to action to where the page sits. Do not force one CTA onto every page.

| Stage | Page intent | CTA language |
|---|---|---|
| **TOFU** | Educational, definitional, "what is this" | Soft: "Explore how mobile body scanning works", "Read the accuracy framework" |
| **MOFU** | Comparison, workflow, evaluation | Evaluation: "See how FitXpress supports remote progress tracking", "Review the buyer checklist", "See sample outputs" |
| **BOFU** | Operational, commercial, vertical page bottom | Direct: "Book a demo", "Talk to 3DLOOK about your workflow", "Explore FitXpress for telehealth and weight loss" |

On a vertical page, pair a direct primary with an evaluation secondary, which is what the benchmark
page does: "Book a demo" plus "See sample outputs". The secondary catches the buyer who is not ready
to talk to a human but is ready to look at a JSON payload, and that buyer is a large share of the
technical audience.

Site-wide CTA language already in use, worth matching: "Let's talk", "Request a Demo", "Unlock Body
Data", "Get in touch", "Book a Consultation", "Explore Technology".

### 6.5 Design compliance on a page

Every token from `DESIGN.md`. Navy `#050F40` with the radial glow on hero, proof band, CTA band and
footer, carrying 60 to 70% of the visual weight. White on content zones. Electric blue `#143DFF` as
a single sharp accent, never a large fill. Satoshi only. The eyebrow label above each section
heading. Cards 20px radius, chips 15px, the footer band 30 to 40px on its top corners. Section
rhythm `clamp(56px, 8vw, 110px)`, container 1200px. Oversized numerals in the proof zone. AA
contrast, a visible focus ring, reduced-motion honoured. The comparison table reflows on mobile, or
it is not shippable.

### 6.6 Page pre-launch checklist

One H1, and H2 and H3 hierarchy intact. Every number byte-identical across hero, body, FAQ and
disclaimer. Data-flow wording accurate everywhere. Logo-usage permission confirmed per customer, and
no scan-volume figures published from the activity dashboard. No pricing table on the page, only the
signal and a link to `/pricing/`. Internal links in all four directions per the site inventory: up
to the parent, down or across to siblings, out to the supporting article, in from the parent.
JSON-LD present: Organization, Service or SoftwareApplication, BreadcrumbList, FAQPage. Alt text
written for this vertical's context. WebP or AVIF, lazy-loaded, largest contentful paint under 2.5
seconds. A visible "Last updated". Asselya's editorial review before publish.

---

## 7. Messaging and proof library

### 7.1 Master positioning

**3DLOOK is the trusted infrastructure for verified body data, built for industries where measurement
consistency, fraud reduction and audit-ready workflows drive business outcomes.** Not a measurement
API. A workflow layer, with enterprise compliance posture and nine or more years of training data
behind it.

### 7.2 Approved hero lines (FitXpress health)

From `messaging.md`, which is the approved set. Adapt wording per artifact; do not invent a new claim
inside a hero line.

| Segment | Hero line |
|---|---|
| Telehealth and weight loss | Verify body progress remotely to boost retention, reduce drop-off, and prove program ROI |
| Online pharmacy / BMI verification | Verify BMI inside the order flow to cut fraud, speed approvals, and stay audit-ready |
| Insurance underwriting | Verify body metrics remotely to issue faster, cut rework, and strengthen auditability |
| Wellness rewards | Verify wellness progress remotely to reduce disputes, boost participation, and improve program reporting |
| Bariatric pre-authorization | Pre-qualify patients remotely to reduce wasted consults, speed pre-auth, and improve conversion to procedures |
| Occupational health | Standardize screening intake remotely to increase throughput, reduce rescreens, and speed clearance decisions |
| Clinical trials | Standardize anthropometrics across sites and reduce visit burden to improve data quality and retention |

Three of these are three-part parallel constructions, which sits close to the punch-triad rule. They
are approved as hero lines because the three items are outcomes rather than adjectives. Do not extend
the pattern into body copy.

Taglines, used sparingly when a short hook is needed: "Verified body data, built for trust." /
"Two photos. 80+ measurements. 45 seconds." / "From scan to outcome, in one workflow."

Phrases to prefer: "verified body data" over "accurate measurements"; "trusted workflow layer" over
"scanning API"; "audit-ready records" for regulated industries; "real-world accuracy" over "lab
accuracy".

### 7.3 The approved proof set

**This table is the whole permitted universe of figures.** It is copied from `proof-points.md`. If a
number is not here, it does not ship.

**Accuracy** (against expert manual measurement, 2025 Accuracy and Repeatability Study)

| Claim | Figure |
|---|---|
| Overall accuracy against manual measurement | 96 to 97% |
| Typical error margin | 1.5 to 2.0 cm |
| Wrist girth | 0.54 cm absolute error |
| Calf | 1.27 cm |
| Neck | 1.48 cm |
| Thigh | 1.64 cm |
| Knee | 1.73 cm |
| Chest | 1.74 cm |
| Waist | 2.14 cm |
| Hip | 2.25 cm |
| Weight estimation | ±3.5% average error margin |

**Repeatability** (same study)

| Claim | Figure |
|---|---|
| Overall repeatability | 95%+ consistency |
| Variance across repeated scans | `< 1 cm` |
| Chest | 0.60 cm |
| Waist | 0.89 cm |
| Low hips | 0.86 cm |
| Knee | 0.12 cm |
| Calf | 0.12 cm |
| Ankle | 0.07 cm |

**Speed and coverage.** Photo to results: under 45 seconds. Photos required: 2, front and side.
Body measurements: 80+. Body composition outputs: BMI, BMR, body fat %, lean mass, fat mass,
essential fat, beneficial fat. Points in the source 3D model: 5M+ per model.

**Training data.** 9+ years. 150,000+ photographs. 30,000+ 3D scans. 430,000+ individual
measurements. Ages 16 to 78. Weight 38 to 210 kg. Height 150 to 220 cm. 48% male, 52% female.
Locations: US and Europe. 86 parameters measured per person, 34 photo configurations per user.

**FitXpress customer outcomes.** Yazen: 34,000 scans in 2025, weight-loss management support.
UK Meds: 7,500 scans in 2025, BMI verification for online pharmacy, 7 months customer lifetime to
date. Healthyr: patient profile complement.

**Aggregate.** 100+ customers all-time. 67 active customers in 2025. 112,100 total scans in 2025.
Internal only, never customer-facing: ARR figures ($1.084M total 2025, $822K enterprise, $262K SMB)
and Mobile Tailor customer ARRs.

**Company.** Founded 2016. 28 employees. $16.2M raised. Sifted 2020 Pioneers of the New World. IEEE
Retail Digital Transformation Grand Challenge winner. Member of Mobile Body Scanning Standards.

**Compliance and security.** HIPAA maintained (FitXpress in US healthcare contexts). Follows GDPR
principles. TLS in transit. AWS S3 SSE-S3 at rest, always on, cannot be disabled. Photos removed
immediately after processing or within 30 days per client policy. Photos auto-blurred when stored.
Face obfuscation at capture. No personal identifiers processed. End-user images never shared with
third parties. Privacy contact `privacy@3dlook.me`. Business associate agreements signed for
HIPAA-covered customers. **Not** FDA-cleared, **not** SOC 2 certified (in progress, confirm with
Vadim before any mention), **not** peer-reviewed or third-party clinically validated.

**Pricing signal.** Free trial: one month, 200 requests, full SDK access. Entry tier $1,000 a month.
No integration fee, no setup fee. Public detail lives on `/pricing/`, and the internal per-request
table never appears in an external artifact. Confirm the live page before any deck or landing page
ships, because `pricing.md` and the live page disagree (section 9, item 4).

**Market sizing, internal only.** Insurance underwriting TAM $25 to 75M a year. Wellness rewards $50
to 200M. Bariatric pre-qualification $10 to 30M. Occupational health screening $20 to 60M. Clinical
trials $10 to 40M. Marked illustrative in the source. Planning use only.

### 7.4 Citation rules

- **Prefer the customer outcome over the internal metric** where one exists. "UK Meds uses FitXpress
  for BMI verification" carries more weight with a buyer than "we have 96% accuracy".
- **Never invent a comparison.** No "ten times more accurate than X" unless that exact figure exists
  in `proof-points.md` with a source.
- **Use the range form when a figure may drift.** "Around 95 to 97% accuracy" survives a small
  correction; a single precise number does not.
- **Do not link to internal documents in public collateral.**
- **One number, everywhere the same** (guardrail 2). Byte-identical in the hero, the body, the FAQ
  and the disclaimer. If two sources conflict, never average them: keep the defensible one, or
  replace both with a qualitative statement. Conflicting numbers are the first thing a diligence
  reader catches.
- **Every customer name and every customer number comes from `case-studies/`**, and only with
  current written permission. Mobile Tailor customer ARRs are never published in any context.
- **External statistics need a named body and a link** (CDC, Munich Re, Swiss Re, NAIC, LIMRA, ISO).
  Verify at the source, and get approval before an external stat appears in a customer-facing deck.

### 7.5 Objection handling

The six objections that always come up, answered in brand voice. These are marketing-side answers
built for collateral. Sales has its own phrasing in the AE playbook, and the two should not
contradict each other.

| Objection | Answer |
|---|---|
| "Patients already self-report their weight." | Self report is inconsistent and easy to misrepresent. FitXpress adds structured, repeatable body data before review, from two photos in under 45 seconds, inside the flow the member already completes |
| "We already use connected scales." | A scale returns one number. FitXpress returns body composition, 80+ measurements, a 3D model and scan-to-scan comparison, captured remotely from a phone |
| "We don't want onboarding friction." | Two photos with guided capture, under a minute. The scan is triggered from a flow the program already runs, and the capture layer validates pose and framing in real time to reduce retakes |
| "How accurate is it?" | Accurate enough for which decision? Against expert manual measurement, 96 to 97% with a typical absolute error of 1.5 to 2.0 cm. For repeat-scan programs the figure that matters is repeatability: variance stays `< 1 cm`, so a change between scans reads as real rather than as noise. Detailed methodology is available under NDA |
| "Our clinicians and underwriters assess manually." | The human still decides. FitXpress standardizes intake and reduces review burden, and it supports clinician or underwriter review rather than replacing it |
| "How does this help the business?" | Better qualification and engagement feed conversion, retention and cleaner outcomes reporting to the payers, employers and regulators the program answers to |
| "We're evaluating other options." | Compare by role. The useful question is which method fits which workflow: a remote structured-data layer, an in-clinic reference method, and a consumer app answer different questions. Route named-competitor framing to Katerina before it goes in writing |
| "Is this a medical device?" | No. FitXpress is not positioned as a medical device. It provides structured body data that supports clinical and operational workflows, and compliance is evaluated on data-privacy frameworks rather than medical-device frameworks |
| "Do you train your AI on our photos?" | No. Photos sent through a customer's tenant are deleted per the retention policy and are not used to train the model |
| "Where is the data stored, and for how long?" | AWS S3 with mandatory server-side encryption, TLS in transit. Photos are removed immediately after processing or within 30 days, depending on the client policy chosen, and are auto-blurred when stored. No personal identifiers are processed |

### 7.6 Competitive framing

Prism Labs is the primary competitor in the FitXpress space, strong in insurance, population health
and GLP-1. Bodygram is secondary, aimed at trainers and dieticians. Size Stream is strong in hybrid
on-premise and at-home clinical research. The long-term risk is native platform primitives from
Apple or Google.

Three rules. **Compare by method or by role, never by competitor name in published copy.** **Never a
clean sweep**, because a table where we win every row reads as marketing and both buyers and answer
engines discount it. **Route any competitive positioning to Katerina before it goes in writing**,
because competitive data moves and the internal analysis is dated March and April 2026. The
competitive analysis deck in Drive is internal only and never leaves the building.

---

## 8. QA checklist

Run this before anything is sent, published or handed to a designer. It maps to the 20-point rubric
in `docs/quality-rubric.md` (Adherence 5, Factual accuracy 5, Brand and tone 3, Format and structure
3, Output quality 4).

### 8.1 Claims and facts (rubric category B, and the hard-fail category)

- [ ] Every figure traced to a line in `proof-points.md`. No exceptions, no "approximately".
- [ ] Every figure byte-identical across hero, body, FAQ, disclaimer and any chart label.
- [ ] Every customer name and customer number from `case-studies/`, with current written permission.
- [ ] No Mobile Tailor content or Mobile Tailor customer ARR anywhere.
- [ ] No claim of diagnosis, treatment, eligibility, underwriting, hiring or clearance decisioning.
- [ ] No claim of replacing a clinician, DEXA, BIA, a calibrated scale or a protocol reference method.
- [ ] No guaranteed compliance, no automatic fraud detection, no "most accurate", no "just an API".
- [ ] Accuracy scoped: the reframe, the four conditions, no bare headline percentage.
- [ ] Repeatability written as `< 1 cm` and never presented as accuracy.
- [ ] The two benchmarks are not mixed.
- [ ] "Independent", "validated", "third-party" absent unless a named external party and a citable
      output are present.
- [ ] SOC 2 not claimed. FDA clearance not claimed. Peer review not claimed.
- [ ] Roadmap items limited to shipped or in-progress, with no promised dates.
- [ ] External statistics carry a named body and a link, and have external-use approval.

### 8.2 Voice and brand (rubric category C)

- [ ] Banned-word grep clean: leverage, utilize, harness, robust, seamless, comprehensive,
      revolutionize, revolutionary, cutting-edge, state-of-the-art, game-changer, disrupt, delve,
      tapestry, realm, groundbreaking, best-in-class, industry-leading, world-class, unparalleled,
      figurative "navigate".
- [ ] No em dash or en dash anywhere.
- [ ] No "it's not just X, it's Y", no "not only X but also Y".
- [ ] No adjectival punch triad.
- [ ] Terminology guardrails clean: no "objective" about our output, no "the reader", no "this
      guide", no "by hand", no "plus" as a connector, no "let", no "so" introducing a benefit, no
      corrective "X, not Y" outside a stated boundary.
- [ ] M1: every abbreviation expanded at first use, including BMI, GLP-1, API, SDK and every cited
      regulator.
- [ ] M2: one clear negative scope statement, no second negation chained onto it.
- [ ] The hero sells an outcome, not accuracy.
- [ ] Buyer framing rather than "you"-spam, except on conversion sections.
- [ ] The detector has been run and every hard fail and house-rule violation is fixed:
      `python3 brand-assets/style-guides/scripts/detect-ai-tells.py <file> --channel page --summary`
- [ ] The second pass has been done: what here still reads as machine-written, and it was fixed.

### 8.3 Disclaimers and sensitive verticals

- [ ] The vertical's scope note appears early, not only at the end.
- [ ] The italic disclaimer sits near any accuracy or eligibility claim.
- [ ] "FitXpress is not positioned as a medical device" is present, in that wording.
- [ ] The segment's "what NOT to say" list from section 4 has been checked line by line.
- [ ] Every control is stated with its limit.
- [ ] BCRL, occupational health, clinical trials and insurance drafts have gone to Whitney.

### 8.4 Design compliance

- [ ] `#143DFF` as a single sharp accent, never a large fill. `#2962FF` absent.
- [ ] Navy `#050F40` with the radial glow and texture on hero, proof, CTA and footer. No flat navy.
- [ ] Satoshi only. No Inter, Bricolage Grotesque or IBM Plex Sans.
- [ ] Type scale, spacing steps and radii taken from `DESIGN.md`, with nothing off-scale.
- [ ] Eyebrow label on each section or content slide.
- [ ] Proof zone leads with an oversized numeral.
- [ ] Product imagery in preference to icon grids.
- [ ] AA contrast, a scrim under light text on imagery, a visible focus ring, reduced-motion honoured.
- [ ] White CTA button on navy.

### 8.5 Calls to action and conversion

- [ ] The CTA matches the funnel stage, and one CTA has not been forced onto everything.
- [ ] One primary action, visible without scrolling and repeated at the end.
- [ ] An evaluation-stage secondary action exists for the buyer who is not ready to talk.
- [ ] The price signal names the entry tier and links to `/pricing/`. No internal per-request rates.
- [ ] Form fields minimal, consent visible, a confirmation state exists.

### 8.6 Structure and technical (pages)

- [ ] One H1, hierarchy intact.
- [ ] Ten or more FAQ questions, answer-first, with FAQPage schema.
- [ ] Service or Product schema with `audience` and `areaServed`, BreadcrumbList, canonical to self.
- [ ] Yoast title 60 characters or fewer, description 155 or fewer, clean URL.
- [ ] Breadcrumb depth matches the product's real hierarchy, with no invented path level.
- [ ] Internal links in all four directions.
- [ ] Comparison table reflows on mobile.
- [ ] A visible "Last updated" line.
- [ ] Word count in the range of the benchmark page, roughly 1,200 to 1,600.

### 8.7 Structure (decks)

- [ ] The 19-slide core is present, and any dropped slide is a recorded decision.
- [ ] Fixed slides copied verbatim from the last approved deck, not rewritten.
- [ ] The text-fit review is written, slide by slide.
- [ ] The confidentiality footer carries the current month and year.
- [ ] Empty slots (case card, testimonial) are recorded rather than filled with adjacent-vertical
      material.

### 8.8 Sign-off

- [ ] Open items block written. Per guardrail 11, unresolved trade-offs are flagged rather than
      silently decided.
- [ ] Numbers confirmed by Vadim.
- [ ] Regulated claims reviewed by Whitney.
- [ ] Competitive framing reviewed by Katerina.
- [ ] Editorial review by Asselya complete.
- [ ] For a site page: G-T passed and G-J scored 85 or above, or the shortfall is explicitly flagged.

---

## 9. Open items and conflicts to resolve

Found while building this playbook, from the sources listed in section 10. Per guardrail 11, these
are flagged rather than silently decided. Nika's first audit should start here and extend the list.

1. **`#2962FF` in the task brief for this playbook.** The brief named it as the accent. It is a
   superseded placeholder from before the Figma export, and both `CLAUDE.md` section 7 and
   `DESIGN.md` section 15 retire it along with Inter. This playbook uses `#143DFF` and Satoshi. If
   `#2962FF` is genuinely in use somewhere, that artifact needs correcting rather than the design
   system.

2. **The ISO benchmark set is in circulation and is not in `proof-points.md`.** 0.40 cm
   session-to-session repeatability, ISO 8559-1:2017, 14 companies, 8 countries, 27 subjects, 1,152
   data points, 11 ISO-compatible measurements, BMI 19 to 41, ages 18 to 55, and the comparison
   figures 0.57 cm for 3D scanners and 0.94 cm for expert manual measurement. All of it appears in
   `about-me.md`, in the sales playbook and in the shipped insurance deck. None of it is in
   `proof-points.md`. Under the sourcing rule it is currently unusable, which conflicts with two
   shipped assets. **Ask:** add the set to `proof-points.md` with its source, or withdraw it from
   collateral. This is the highest-value item on the list, because 0.40 cm is the strongest number
   we have for longitudinal verticals.

3. **ISO 8559-1:2017 versus ISO 20685-1.** `about-me.md`, the sales playbook and the insurance deck
   cite ISO 8559-1:2017. The June 2026 telehealth page structure document cites ISO 20685-1, with a
   different benchmark shape (17 subjects, 8 stations). One of these is wrong and both are in
   circulation. **Ask Vadim and product which standard the benchmark actually ran against.**

4. **Pricing figures disagree across three sources.** `pricing.md`: $1,000 a month for 500 requests,
   $1,500 for 1,000. The sales playbook: $1,000 a month for 1,000 requests, and a $0.50 per-request
   floor above 5,000 a month, where `pricing.md` puts $0.50 at 20,000. `CLAUDE.md` section 2 matches
   `pricing.md`. There is also a live `/pricing/` page that a previous audit found to contradict
   `pricing.md` on Mobile Tailor tiers. Separately, `about-me.md` says never state or imply prices,
   while the page pipeline requires a price signal and a link to `/pricing/` on every commercial
   page. **Ask:** which table is current, and what the standing rule is for a price signal in
   marketing collateral.

5. **Customer naming permission is contradictory.** The insurance deck's open items record that an
   NDA prohibits naming Yazen, UK Meds and Healthyr. The telehealth page structure document plans a
   logo wall including Yazen, UK Meds, Pharmacy Online, Healthyr, Tera Science, CoreDirection,
   SIMETRIA, HEXFIT, Body Science, MAGIC and IB, with a note to confirm permission per customer. The
   sales playbook lists Yazen, Erakulis and Magic AI as named clients on a competitive slide.
   `case-studies/` tells agents to cite UK Meds and Yazen by name in outbound. **Ask Katerina and
   Olena Chorna for a single per-customer permission list.** Until it exists, treat naming as
   blocked and use the numbers without the name.

6. **Speed claim varies: 45 seconds, under a minute, under 60 seconds, 40 to 50 seconds.**
   `proof-points.md` and `tech-spec.md` say under 45 seconds. The published 2-pager PDF says under 60
   seconds twice. The insurance deck cover says under a minute. The telehealth page structure
   document says about 40 to 50 seconds. Guardrail 2 makes this a defect. **Recommendation:** hold
   "under 45 seconds" as the single claim, and correct the 2-pager.

7. **Training-data height range — RESOLVED 2026-09-02, Vadim: 150 to 220 cm.** Was: `proof-points.md` said 150 to 205 cm, `about-me.md` said
   150 to 220 cm. **Ask Vadim which is right**, and correct the other.

8. **Company headcount disagrees.** `CLAUDE.md` and `proof-points.md` say 28 employees. The June 2026
   sales playbook says 22. The About slide in every deck carries this number.

9. **Banned words are live in shipped assets.** "Best-in-class Repeatability" is a section title on
   slide 6 of the insurance deck, and "best-in-class repeatability" is also listed as a hero-message
   alternative in `icp-detail.md` section 1. The sales playbook uses "Best-in-class repeatability".
   The published 2-pager uses "seamlessly embeds". Previous audits also found "leverage",
   "best-in-class" and "revolutionize" on live site pages. All are hard fails under `CLAUDE.md`
   section 6. **Action:** Nika's week-one audit produces the full list and a correction plan.

10. **"Independently benchmarked" on insurance slide 6** breaks guardrail 3, since independence is
    not provable with a named external party and a citable output. Compliant rewrite: "benchmarked
    against 3D scanners and expert manual measurements in a multi-company benchmark", with the
    naming resolved through item 2.

11. **Two verticals have no proof and no use-case file.** Plastic surgery
    (`use-cases/fx-plastic-surgery.md` missing) and BCRL (missing, and `icp-detail.md` records that
    the clinically relevant metric is absent from `proof-points.md`). Neither can carry a deck or a
    page yet. **Ask:** should product produce a volumetric-asymmetry validation figure, and is
    plastic surgery a 2026 priority?

12. **G-I blocks nearly every FitXpress vertical page.** The gate requires two or more publishable
    cases from the vertical, and every FX vertical has at most one. **Ask Vadim** for either a second
    case per priority vertical, an approved external reference, or a recorded waiver. Without this,
    "vertical landing pages for all use cases" is not deliverable as stated.

13. **`FX Guidance for Decks Whitney Feb 2026` did not resolve.** It is a shortcut in the Drive
    Marketing docs folder whose target could not be read. This is likely the single most relevant
    existing document for Nika's deck work. **Ask Whitney or Vadim to re-share it.**

14. **Digital fitness has no citable customer.** The names in circulation (Erakulis, Magic AI,
    HEXFIT, Body Science, MAGIC, IB) appear in the sales deck and the telehealth page draft but not
    in `proof-points.md` or `case-studies/`. Either add them with permission, or the fitness deck
    ships without a case card.

15. **HIPAA applicability to life insurers** is flagged in the insurance deck's own open items, since
    HIPAA covers health plans and healthcare providers and a life insurer's status varies. The
    compliance slide currently carries the claim forward from the telehealth deck. **Ask Whitney.**

16. **The Munich Re and CDC statistics on insurance slides 2 and 7** are carried from an article and
    the deck flags them as needing external-use approval. **Verify at source and get approval before
    the deck goes out again.**

---

## 10. Source index

**Read (local repo, `/home/vadim_prod/3dlook-marketing/marketing_vb/`)**

- `CLAUDE.md`
- `about-me.md`
- `audience.md`
- `DESIGN.md`
- `docs/quality-rubric.md`
- `brand-assets/product-info/proof-points.md`
- `brand-assets/product-info/icp-detail.md`
- `brand-assets/product-info/messaging.md`
- `brand-assets/product-info/pricing.md`
- `brand-assets/product-info/compliance.md`
- `brand-assets/product-info/tech-spec.md`
- `brand-assets/product-info/case-studies/uk-meds.md`
- `brand-assets/product-info/case-studies/yazen.md`
- `brand-assets/style-guides/editorial-guardrails.md`
- `brand-assets/style-guides/ai-tells-sweep.md`
- `brand-assets/content-strategy/terminology-guardrails.md`
- `.claude/skills/page-builder/SKILL.md`
- `.claude/skills/page-builder/references/kit-vertical-page.md`
- `.claude/skills/page-builder/references/site-inventory.md`
- Directory listings: `brand-assets/`, `brand-assets/product-info/use-cases/`,
  `brand-assets/product-info/case-studies/`, `brand-assets/style-guides/`, `brand-assets/team/`

**Read (repo parent)**

- `/home/vadim_prod/3dlook-marketing/fitxpress-insurance-underwriting-deck-copy.md`

**Read (Google Drive, via Drive MCP)**

- `FitXpress_Sales_Playbook_June 2006` (Google Slides, 30 slides, the structural template)
- `FitXpress by 3DLOOK_2-pager.pdf`
- `BMI verification use case.pdf`
- `FitXpress for Telehealth — Page Structure & Content (v4)` (Google Doc, the landing-page exemplar)
- Folder listings: sales root folder `1UdeWy90iiTVzHrLPsmOyYqM0wl3l_BlO`, `Marketing docs & Decks`,
  `Technology & Accuracy`, `Useful info`

**Attempted, did not resolve**

- `FX Guidance for Decks Whitney Feb 2026` (shortcut, target unreadable, see section 9 item 13)

**Not opened, worth reading next**

- `3DLOOK Accuracy_and_Repeatability_Analysis (1).pdf` (Apr 2026) and
  `3DLOOK_Accuracy and Repeatabilty 2_26_2025.pdf`, which are the likely source for open item 2
- `FitXpress for Insurance Underwriting (Demo Deck) May 2026` and
  `FitXpress for Telehealth (Demo Deck) May 2026`, the built decks behind the copy documents
- `Prism vs 3DLOOK_ Whitney Analysis_3_25_2026.pdf` and `Prism Labs Introduction (March 2026)`
- `Nick Omelchak — Deal Call Transcripts`, the best raw material for vertical FAQs
- `FitXpress Integration Guidelines April 2026`
- `FitXpress _ Fat estimation approach .pdf`
