# Vertical (use-case) Page Kit — FitXpress and Mobile Tailor

The page a buyer from one market lands on to answer one question: **have you done this for people
like me, and can I defend the decision internally?** A product page cannot prove that. A vertical
page can — if it is written with that vertical's regulators, workflows, buyer titles and KPIs.

The trap everyone falls into: the vertical page is the product page with the vertical's name swapped
into the headline. That produces a duplicate that cannibalises its own parent and adds nothing. Which
is why this Kit opens with a gate about whether the page should exist, not with a structure.

3DLOOK-specific version of the trap: a vertical page that is really an accuracy pitch. Buyers in
telehealth, insurance and occupational health are not buying millimetres, they are buying a
defensible workflow. `overview.md` says it plainly — sell outcomes, workflow integration and
governance, not "best model".

---

## G-I · Should this page exist at all

Run this **before** the intake questionnaire. Fail it and there is no page — there is a section on the
product page plus the vertical's hub article in the content hub.

- [ ] **A use-case file exists** — `brand-assets/product-info/use-cases/{fx|mt}-{vertical}.md`. It
      supplies the pain, hero message, ICP, buyer titles, KPIs and critical messaging. No file → write
      it first (the same rule `hypothesis-generator` follows) or stop.
- [ ] **2+ publishable case studies from this vertical** in `brand-assets/product-info/case-studies/`.
      One case does not hold a page; zero is fiction. Check the coverage table in `page-types.md` —
      most FitXpress verticals do not clear this today.
- [ ] **Demand exists** — a row in `brand-assets/content-strategy/content-plan.md`, Search Console
      volume on vertical-named queries, or ≥15% of outbound pipeline from
      `workspace/outbound/campaigns/` for this segment.
- [ ] **Five facts that are not on the parent page.** A named regulator or standard, a buyer title
      who signs off, a workflow step, a KPI in the vertical's own units, an integration or export
      format, a procurement or seasonal cycle. Fewer than five → write nothing yet.
- [ ] **The market's BD owner confirms the objections differ** from the general ones — Nick Omelchak
      (USA), Olena Kudryavtseva (Europe), Kateryna Boichuk (Israel), Katerina Galich (UK).
- [ ] **The parent and the URL are settled.** FitXpress verticals are children of the homepage and
      live at `/for-{vertical}/`; Mobile Tailor verticals sit under `/mobile-tailor/`. Never invent a
      `/fitxpress/` level — see `site-inventory.md`.

> **The 60% rule.** At least 60% of a vertical page must be unique against the parent product page.
> Only the workflow overview and the integration basics are shared. Below 60% it is a duplicate, and
> a duplicate is better unpublished.

**If G-I fails:** add a "For [vertical]" section to the product page, link it to the vertical's hub
article, and record the decision with a date. Revisit when the second case lands. A G-I waiver is
possible — Vadim's call, recorded in `gate-reports.md` with the reason and what stands in for the
missing case (an approved reference call, a named pilot, an anonymised deployment).

---

## Structure — 17 slots

**1. Breadcrumbs** — two levels for FitXpress (`Home → [Vertical]`, since the homepage is the parent),
three for Mobile Tailor (`Home → Mobile Tailor → [Vertical]`). Match what the live pages already
declare; do not invent a middle level that resolves to a redirect.

**2. H1** — `[Outcome in the vertical's terms] for [vertical]`. Not "AI-powered precision" but
"Verified weight and BMI capture for GLP-1 programs". One H1. Primary query in it and in the first
100 words. No "best", no "most accurate", no banned words from CLAUDE.md §6.

**3. Hero + a vertical proof point** — one sentence on what the product does here, plus a number from
**this** vertical: scans delivered for a named customer in this market, or the KPI the use-case file
names. The company-wide 112,100 scans figure does not work here; a vertical figure does.

**4. Vertical context — the slot the page exists for** — 3–5 specifics only someone who has worked in
this market knows: the regulators and frameworks that actually come up (HIPAA in US health, GDPR in
the EU, MHRA / CQC / NHS in the UK, FDA / ICH / GCP in trials), who signs off and who blocks,
the procurement cycle, the units results are measured in, the export formats, the seasonality.
Source: the use-case file plus the BD owner's answers.

**5. Pains of this vertical** — from the use-case file's "The pain we remove" and `audience.md`'s
segment hook, in the buyer's phrasing. Then honour that segment's **"what NOT to say"** list.

**6. What the product is here + the boundary** — scope in the vertical's own words: what is captured,
what is returned, what is documented. Then one clear boundary sentence: *"FitXpress is not positioned
as a medical device."* One negative, stated once — guardrail #6 for the framing, M2 for not chaining a
second negation onto it.

**7. Where the workflow differs** — do not restate the whole flow. The 2–3 steps that run differently
here and why: consent capture, retake logic, who reviews a flagged scan, how the record is filed.

**8. Compliance and data governance** — for regulated verticals this is the deciding block, not a
footnote: HIPAA and GDPR posture, encryption at rest (AWS S3 SSE-S3), photo retention (immediate or
within 30 days per customer policy), no personal identifiers processed, consent handling, audit
trails, `privacy@3dlook.me`. Source: `compliance.md` and `CLAUDE.md` §12. Every control is stated
with its limit — controls reduce risk, they do not remove the need for capture instructions and
deployment thresholds (guardrail #5).

**9. Accuracy and reliability, scoped** — open by reframing "how accurate is it?" into **"accurate
enough for which decision?"**, then name the four conditions that make an accuracy claim mean
anything: reference method, measurement protocol, population tested, intended workflow. Figures from
`proof-points.md` only — 96–97% vs manual, error margin 1.5–2.0 cm, repeatability written as
`< 1 cm`, weight estimation ±3.5%. No bare ">95%" (guardrail #4): pair a qualitative claim with one
concrete sub-figure and "detailed methodology available under NDA". Never the words "independent",
"validated" or "third-party" (guardrail #3).

**10. Cases from this vertical only** — 2 cards minimum, each with a number from
`case-studies/`, linked to `/case-studies/`. A case from an adjacent vertical breaks the page's whole
promise. Mobile Tailor customer ARRs never appear.

**11. Customer quote from this vertical** — name, role, company, only where that use is approved. No
approved quote → the slot is dropped and recorded. Never an invented name, role or testimonial.

**12. Integration, formats and support** — API plus web and mobile SDKs, web widget, CSV export, 3D
model export, what it plugs into in this vertical (EHR / patient portal, PAS, OMS, pattern-making,
benefits platform), white-label options, implementation support. Source: `tech-spec.md` and the
published tier features. The signal is "we are already inside your environment".

**13. Vertical FAQ** — the questions asked here and nowhere else: regulatory, licensing, data
residency, retention, who owns the data, what happens on a failed scan, what a pilot looks like.
Source: `faq.md` plus the BD owner's real objections. General product questions stay on the product
page. Ships with FAQPage schema, modelled on the 13-question block on
`/structured-body-data-for-telehealth-digital-health-programs/` — the only page on the site that has it.

**14. Price signal** — name the entry tier and link to `/pricing/` (FitXpress from $1,000/mo,
Mobile Tailor from $499/mo as published on 2026-08-23 — re-check before shipping). Mention the trial
where it applies. Never the internal per-request rates from `pricing.md`.

**15. Primary action + form** — one action, in the site's own language ("Book a demo" / "Talk to
sales" / "Start a trial"), visible without scrolling and repeated at the end. Minimal fields, visible
consent, confirmation state.

**16. Soft alternative + sibling verticals** — for buyers not ready to talk: the accuracy framework
article, the vertical's hub article, the ebook, a vertical checklist. Then cards for two sibling
verticals and a link up to the product page. Per the four linking directions in `site-inventory.md`.

**17. Hidden technical layer** — Service (or Product) schema with `audience` and `areaServed`,
FAQPage on the FAQ block, BreadcrumbList on the crumbs, canonical to self, Yoast title ≤ 60 and
description ≤ 155 characters, clean URL.

## Slots by category

| Category | Slots |
|---|---|
| **Proof of belonging** | vertical context · compliance · integration and formats · vertical cases · quote |
| **Offer clarity** | H1 formula · vertical pains · scope and the boundary · where the workflow differs · price signal |
| **Claims discipline** | scoped accuracy block · every figure traced to `proof-points.md` · guardrails #1–#6 |
| **Conversion** | hero action · inline actions · final form · soft alternative · sibling verticals |
| **Search & AI visibility** | breadcrumbs · single H1 · vertical FAQ + FAQPage schema · canonical · link up to the parent |

---

## Intake — who answers what

The point is to extract what is **not** on the product page. Questions are deliberately narrow.

**A. Vertical context** — Which frameworks and regulators actually come up on calls in this market?
Who approves, who blocks, and how is that different from other verticals? Typical cycle from first
contact to signature? What units does this buyer measure results in? What deadlines or seasonality
drive their timelines? *(BD owner for the market + the use-case file.)*

**B. Language** — What does this buyer call what we deliver, verbatim? Which words from the product
page are meaningless to them? Three verbatim pain phrases from recent calls. *(BD owner + `audience.md`.)*

**C. Differences in the workflow** — What runs differently here, and why? What consent, retention or
residency requirements apply? What does it integrate with in this vertical? *(Vadim + `tech-spec.md`.)*

**D. Proof** — How many scans, in which markets, for which named customers in this vertical? Which
2–3 cases can be shown with numbers? Which customer will give a quote with name and company, and is
that use approved? *(`case-studies/` + Vadim.)*

**E. Objections** — Which questions get asked here and nowhere else? What killed deals in this
vertical specifically? *(BD owner + `faq.md`.)*

**F. Positioning and claims** — Anything in the draft that bends a guardrail goes to Asselya, per
principle #11. Medical, clinical or regulatory framing goes to Whitney before it ships.

---

## Writer SOP

1. **Read two pages first:** the parent — the homepage for FitXpress, `/mobile-tailor/` for Mobile
   Tailor — so nothing gets copied from it, and
   `/structured-body-data-for-telehealth-digital-health-programs/`, which is the in-house benchmark —
   scoped accuracy, a real comparison block, a 13-question FAQ with schema, no banned words in the
   headings. Match its depth (~1,600 words), not `/for-bmi-verification/`'s ~659.
2. **Read the use-case file, `audience.md` and the segment's "what NOT to say"** before the first
   sentence. A vertical page written without them is a product page with a new headline.
3. **Check the 60% rule before handover** — count the paragraphs with no equivalent on the parent.
   Under 60%, go back for material.
4. **Every number from `proof-points.md`; every client name and client metric from `case-studies/`.**
   Anything else goes to Open items. One number, byte-identical everywhere on the page (guardrail #2).
5. **Name regulators and standards precisely** — the framework, the jurisdiction, and what it governs.
   A vague gesture at a standard is worse than omitting it. Expand every acronym at first use, FDA,
   ICH, GCP, BMI and DEXA included (M1).
6. **Scope accuracy, never brag about it.** The reframe in slot 9 is mandatory. Leading with "most
   accurate" or "best-in-class" is an anti-positioning violation and a hard fail at the judge.
7. **State the boundary once** — "not positioned as a medical device" — and do not chain a second
   negation onto it (M2).
8. **Only your own cases from this vertical.** Fewer than two means G-I should have stopped the page.
9. **Do not restate the whole workflow.** Differences only.
10. **FAQ stays narrow.** General questions belong on the product page.
11. **Links up, sideways, to the hub article and to conversion** — all four directions, every page.
12. **Mark visuals:** `[HERO]`, `[CONTEXT]`, `[COMPLIANCE]`, `[WORKFLOW]`, `[ACCURACY]`,
    `[CASE CARD]`, `[QUOTE]`, `[INTEGRATION]`.
13. **Run `copy-humanisation.md` as its own pass** after the draft is finished. Negative parallelism
    ("not just X — it's Y"), rule-of-three triads and the CLAUDE.md §6 banned words are hard fails at
    the judge, not style preferences.
14. **Fact-check** every figure, customer name, framework and price against the sources before
    handover, and write `fact-sheet.md` for the blind judge as you go.

---

## Technical checklist

**URL and anti-cannibalisation** — `/for-{vertical}/` for FitXpress, `/mobile-tailor/for-{vertical}/`
for Mobile Tailor · canonical to self, never to the parent · request the in-body link down from the
parent, which no parent page currently has ·
run a cannibalisation check against both inventories before writing and against Search Console after
indexing · Yoast title and description differ from the parent's and from the vertical's hub article.

**Schema** — Service or Product with `audience` and `areaServed` · FAQPage on the FAQ block ·
BreadcrumbList with the full chain · Organization comes from the Yoast site template.

**Template and analytics** — sticky CTA on mobile · form with minimal fields, visible consent and a
confirmation state · analytics events on form view, first input, submit, and demo-link clicks ·
sibling-vertical block · WebP, lazy-load, images under 200KB · indexable, in the sitemap, inbound
internal links in place.

---

## Designer brief — tokens from `DESIGN.md`, no exceptions

| Marker | What to produce |
|---|---|
| `[HERO]` | First screen: H1, one sentence, the vertical's number as an oversized numeral, one action. Navy `#050F40` with the radial glow, or white |
| `[CONTEXT]` | Vertical realities: stakeholder-and-cycle diagram or a regulator chip row, 15px radius chips |
| `[COMPLIANCE]` | Governance block — encryption, retention, consent, audit trail. Cards at 20px radius |
| `[WORKFLOW]` | The diverging steps highlighted against the base flow, readable on mobile |
| `[ACCURACY]` | The four conditions plus the figures, as a table or numeral row. The number is the hero |
| `[CASE CARD]` | Vertical case card: customer, number, link. 20px radius |
| `[QUOTE]` | Pull quote with photo or logo, only where the use is approved |
| `[INTEGRATION]` | API / SDK / widget / export as a diagram, not an icon grid |

Satoshi throughout. `#143DFF` stays a single sharp accent — never a large fill. Real product imagery
(guided-capture UI, 3D body render, admin panel in a frame) over stock or generic icons. Precision as
the visual language: measurement lines, keypoint dots, exact numerals. Alt text on every visual,
mobile checked.

---

## Campaign landing variant

Same Kit with four changes: no site navigation, no sibling-vertical block, exactly one action on the
page, and the soft alternative replaced by the gated asset itself. The vertical context, compliance
and accuracy slots stay — they are what makes a cold visitor believe the page. Landing pages live at
their own URL and are never a copy of the vertical page.

---

## Pre-launch checklist

- [ ] G-I passed, or the waiver recorded with its reason
- [ ] 60% uniqueness against the parent held and counted
- [ ] Parent exists, breadcrumbs resolve, canonical to self
- [ ] Vertical context carries ≥3 facts absent from the parent page
- [ ] Regulators and frameworks named precisely; every acronym expanded at first use
- [ ] Accuracy block scoped with the four conditions; no bare percentages; no reserved words
- [ ] Boundary sentence present, stated once, in the approved wording
- [ ] 2+ cases from this vertical with numbers from `case-studies/`
- [ ] Every figure traced to `proof-points.md` and identical everywhere it appears
- [ ] Compliance block with limits stated, not just capabilities
- [ ] Price signal plus a link to `/pricing/`; no internal rates, no MT ARRs
- [ ] Vertical FAQ narrow, plus FAQPage schema that validates
- [ ] Links up, sideways to two siblings, to the hub article, to conversion
- [ ] One primary action; analytics events verified manually
- [ ] All `[markers]` replaced; alt text everywhere; mobile checked at 375 and 768
- [ ] Open items block listing every bent guardrail, for Asselya
