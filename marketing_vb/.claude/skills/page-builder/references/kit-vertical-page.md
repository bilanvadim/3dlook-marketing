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
- [ ] **The parent and the URL are settled.** FitXpress verticals are children of `/fitxpress/` and
      live at `/fitxpress/for-{vertical}/`; Mobile Tailor verticals sit under `/mobile-tailor/`
      (Vadim, 2026-09-27) — see `site-inventory.md`.

> **The 60% rule.** At least 60% of a vertical page must be unique against the parent product page.
> Only the workflow overview and the integration basics are shared. Below 60% it is a duplicate, and
> a duplicate is better unpublished.

**If G-I fails:** add a "For [vertical]" section to the product page, link it to the vertical's hub
article, and record the decision with a date. Revisit when the second case lands. A G-I waiver is
possible — Vadim's call, recorded in `gate-reports.md` with the reason and what stands in for the
missing case (an approved reference call, a named pilot, an anonymised deployment).

**Standing G-I waiver for every FitXpress vertical (Vadim, 2026-09-27).** Clients do not agree to public case studies (logos only), so FX vertical pages are built without the 2-case bar. What stands in for cases: customer logos; anonymised figures only from `proof-points.md` (a figure that could identify a client is cleared with Vadim first); the accuracy framework; the trust FAQ; the workflow itself. Never an invented or implied case. The waiver for a vertical ends when its first approved case lands. The other G-I checks (use-case file, demand, 5 facts, 60% rule) still apply. Record `G-I: standing FX waiver 2026-09-27` in `gate-reports.md`.

---

## Length and order: short and commercial (Vadim, 2026-09-30)

A use-case landing converts, and the articles teach. Vadim, 2026-09-30: use-case landings are shorter
and more commercial than the pages built before, and the depth lives in the hub article, the accuracy
framework and the trust FAQ, which the page links to.

- **Budget: 1,100 to 1,300 words of visible copy**, tables and FAQ included, navigation and schema
  excluded. Above 1,400 the page is doing an article's job.
- **One paragraph, then a link.** Anything that needs more than one paragraph of explanation belongs in
  an article. The page keeps one line and links to it.
- **A call to action on every second screen:** the hero, after the "what you get" block, after the pilot
  block, and the form.
- **Shape benchmark:** `workspace/pages/for-insurance-underwriting/page-v2-short.md`. The telehealth page
  stays the benchmark for schema and claims discipline, not for length.

| # | Block, in page order | Words | Slots |
|---|---|---|---|
| 1 | Hero: H1 with the primary keyword, 2-3 sentences (outcome and time), "Book a demo" to `#demo` and an anchor to block 4, a four-fact strip | ~90 | 1, 2, 3, 15 |
| 2 | The problem in three numbers from named industry sources, one line, a link to the hub article | ~90 | 4, 5 |
| 3 | How it works in three steps, in the vertical's own systems; the recommended setup in one line; a link to the feature page | ~130 | 7, 12 |
| 4 | What you get: a five-row table, then "Get a sample" to `#demo` | ~150 | 6 |
| 5 | Compared with how it is done today: a five-row table, and one line on where the old method still fits | ~120 | 5 |
| 6 | Accuracy and data handling on one screen: three figures, one method sentence, five data lines, links to the accuracy framework and the trust FAQ | ~180 | 8, 9 |
| 7 | Pilot and price: three steps, what the team walks away with, the entry price and `/pricing/`, a demo button | ~150 | 10, 14 |
| 8 | FAQ: 5-6 questions, GEO phrases from the keyword map verbatim as H3, the answer in the first sentence | ~280 | 13 |
| 9 | The shared form at `#demo`, a soft exit to the hub article, then keep reading | ~50 | 15, 16 |

The order and the budget decide the page. The slots below say what each ingredient must contain.

## Slots: the 17 ingredients

**1. Breadcrumbs** — three levels for both products: `Home → FitXpress → [Vertical]` and
`Home → Mobile Tailor → [Vertical]` (hierarchy of 2026-09-27). `/fitxpress/` ships with the use-case
release (`docs/page-pipeline.md`); until it is live, do not link a middle level that resolves to a
redirect.

**2. H1** — `[Outcome in the vertical's terms] for [vertical]`. Not "AI-powered precision" but
"Verified weight and BMI capture for GLP-1 programs". One H1. Primary query in it and in the first
100 words. No "best", no "most accurate", no banned words from CLAUDE.md §6.

**3. Hero + a vertical proof point** — one sentence on what the product does here, plus a number from
**this** vertical: scans delivered for a named customer in this market, or the KPI the use-case file
names. A company-wide scale figure appears only as "100+ clients", the one public number everywhere
(Vadim, 2026-09-30). "112,100 scans" and "67 clients" never appear on a page. An approved vertical
figure beats both.

**4. Vertical context — the slot the page exists for** — 3–5 specifics only someone who has worked in
this market knows: the regulators and frameworks that actually come up (HIPAA in US health, GDPR in
the EU, MHRA / CQC / NHS in the UK, FDA / ICH / GCP in trials), who signs off and who blocks,
the procurement cycle, the units results are measured in, the export formats, the seasonality.
Source: the use-case file plus the BD owner's answers. On the short page these facts are not an essay
of their own: they surface in the problem numbers, the systems named in the three steps (PAS, EHR,
benefits platform) and the FAQ.

**5. Pains of this vertical** — from the use-case file's "The pain we remove" and `audience.md`'s
segment hook, in the buyer's phrasing. Then honour that segment's **"what NOT to say"** list.

**6. What the product is here + the boundary** — scope in the vertical's own words: what is captured,
what is returned, what is documented. Then one clear boundary sentence: *"FitXpress is not a medical
device."* One negative, stated once — guardrail #6 for the framing, M2 for not chaining a second
negation onto it. "Positioned as" is banned (terminology guardrail §2.10, since 2026-09-11).

**7. How it works, three steps** — do not restate the whole product flow. Three steps as they run in
this vertical, in its own systems: what the person does, what FitXpress returns, where the result goes
and who acts on it (consent capture, retake logic, who reviews a flagged scan, how the record is filed).

**8. Data handling: five lines and a link** — for regulated verticals this still decides deals, so it
sits on the proof screen next to the accuracy figures, but short: photos (deleted after processing or
within 30 days per customer policy, retained photos blurred, faces obfuscated at capture), scan records
on anonymized, randomly generated IDs, HIPAA support under an executed BAA and the canonical GDPR role
sentence, no training on production data without documented authorization, and the boundary. Hosting,
encryption detail, deletion by scan ID, SOC 2, FDA and consent go to one link to the
[trust FAQ](https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/). Source:
`compliance.md` (rebuilt 2026-09-18 from that FAQ) and `CLAUDE.md` §12. Never "HIPAA compliant",
"SOC 2 certified" or "no personal identifiers" (detector category `compliance_status`), and never a
control presented as removing risk (guardrail #5).

**9. Accuracy, scoped in three figures and a link** — three oversized figures, each with its
reference: 96-97% vs expert manual measurement with typical absolute error 1.5-2.0 cm, repeatability
written as `< 1 cm`, and weight estimation ±3.5% where weight matters to the vertical. Then one sentence
on the method and its limit (internal validation; peer review and third-party clinical certification
are not part of that record; methodology under NDA) and a link to the
[accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/), which carries the
"accurate enough for which decision?" reframe and the four conditions (reference method, protocol,
population, workflow). Wording from `accuracy-formulations.md`, numbers from `proof-points.md`. No bare
">95%" (guardrail #4). "Independent", "validated" and "third-party" never appear as claims
(guardrail #3).

**10. Cases from this vertical only** — 2 cards minimum, each with a number from
`case-studies/`, linked to `/case-studies/`. A case from an adjacent vertical breaks the page's whole
promise. Mobile Tailor customer ARRs never appear.

**11. Customer quote from this vertical** — name, role, company, only where that use is approved. No
approved quote → the slot is dropped and recorded. Never an invented name, role or testimonial.

**12. Integration, formats and support** — API plus web and mobile SDKs, web widget, CSV export, 3D
model export, what it plugs into in this vertical (EHR / patient portal, PAS, OMS, pattern-making,
benefits platform), white-label options, implementation support. Source: `tech-spec.md` and the
published tier features. The signal is "we are already inside your environment". On the short page
this folds into the three steps and the record table: API plus web and mobile SDKs, and the system the
result lands in. Formats and white-label detail go to the FAQ only when the vertical asks for them.

**13. Vertical FAQ** — the questions asked here and nowhere else: regulatory, licensing, data
residency, retention, who owns the data, what happens on a failed scan, what a pilot looks like.
Source: `faq.md` plus the BD owner's real objections. General product questions stay on the product
page. **5-6 questions.** The GEO phrases from the landing's keyword map go in verbatim as H3, and each
answer opens with the answer. Ships with FAQPage schema, modelled on the markup of
`/structured-body-data-for-telehealth-digital-health-programs/` (its schema, not its 13-question length).

**14. Price signal** — name the entry tier and link to `/pricing/` (FitXpress from $1,000/mo,
Mobile Tailor from $499/mo as published on 2026-08-23 — re-check before shipping). FitXpress pages
also say **"no integration fee"** (Vadim, 2026-09-30: true, and an advantage over competitors). No
public trial: the action is always "Book a demo" (Vadim, 2026-09-27). Never the internal per-request
rates from `pricing.md`.

**15. Primary action + form** — one action, in the site's own language ("Book a demo" / "Talk to
sales" / "Start a trial"), visible without scrolling and repeated at the end. Minimal fields, visible
consent, confirmation state.

**FitXpress pages: one shared form, never a page-specific one (Vadim, 2026-09-29).** Every FX page
(`/fitxpress/`, each `/fitxpress/for-{vertical}/`, the BMI verification page) embeds the same HubSpot
form `FX | LP | Demo`; submission opens HubSpot Meetings. The page does not configure anything per
vertical: GTM writes the hidden field `fx_vertical` from the page path. The form section carries the
anchor `id="demo"`, because hub articles link to `/fitxpress/for-{vertical}/#demo` from their
"Book a demo" button. Do not spec new fields or a new form for a vertical; a field every vertical
needs goes into the shared form. Source: `workspace/research/seo-fitxpress-2026-09/2026-09-27-tz-tracking-hubspot-ga4.md`
(A1, B1, B2.5).

**Shared-form field added 2026-09-30 (Vadim):** optional "Expected monthly scan volume" (under 500 ·
500-1,000 · 1,000-5,000 · over 5,000 · not sure yet). It started as a page-specific field in Nika's
insurance draft; it qualifies the lead in every vertical, so it lives in the shared form (tracking TZ B1).

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
   headings. Take its schema and its claims discipline, not its length: the budget is 1,100 to 1,300
   words ("Length and order" above), and the shape benchmark is
   `workspace/pages/for-insurance-underwriting/page-v2-short.md`.
2. **Read the use-case file, `audience.md` and the segment's "what NOT to say"** before the first
   sentence. A vertical page written without them is a product page with a new headline.
3. **Check the 60% rule before handover** — count the paragraphs with no equivalent on the parent.
   Under 60%, go back for material.
4. **Every number from `proof-points.md`; every client name and client metric from `case-studies/`.**
   Anything else goes to Open items. One number, byte-identical everywhere on the page (guardrail #2).
5. **Name regulators and standards precisely** — the framework, the jurisdiction, and what it governs.
   A vague gesture at a standard is worse than omitting it. Expand every acronym at first use, FDA,
   ICH, GCP and DXA included (M1). BMI, CEO, UK, US and EU are commonly known and stay bare.
   IEEE appears only in the two approved sentences from `proof-points.md`, and never as a standalone
   logo in a recognition strip (terminology guardrail §2.11). Outputs are "80+ body measurements";
   BMI and BMR are calculated metrics and body composition is an estimate (§2.13).
   Name the vertical's actor: "the pharmacy", "the clinic", "the employer", "the insurer". A vertical
   page always knows who acts, so a generic "organization" is a miss here (§2.14, synced 2026-09-28).
6. **Scope accuracy, never brag about it.** Every figure carries its reference and its limit, and the
   page links to the accuracy framework for the reframe (slot 9). Leading with "most accurate" or
   "best-in-class" is an anti-positioning violation and a hard fail at the judge.
7. **State the boundary once**, directly: "FitXpress is not a medical device." Do not chain a
   second negation onto it (M2), and do not write "positioned as" (terminology guardrail §2.10).
8. **Only your own cases from this vertical.** Fewer than two means G-I should have stopped the page.
9. **Do not restate the whole workflow.** Differences only.
10. **FAQ stays narrow: 5-6 questions.** General questions belong on the product page, long answers
    in the articles.
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

**URL and anti-cannibalisation** — `/fitxpress/for-{vertical}/` for FitXpress, `/mobile-tailor/for-{vertical}/`
for Mobile Tailor · canonical to self, never to the parent · request the in-body link down from the
parent, which no parent page currently has ·
run a cannibalisation check against both inventories before writing and against Search Console after
indexing · Yoast title and description differ from the parent's and from the vertical's hub article.

**Schema** — Service or Product with `audience` and `areaServed` · FAQPage on the FAQ block ·
BreadcrumbList with the full chain · Organization comes from the Yoast site template.

**Template and analytics** — sticky CTA on mobile · form with minimal fields, visible consent and a
confirmation state · analytics events on form view, first input, submit, and demo-link clicks (FX
names: `generate_lead` with `form_name = fx_lp_demo` and `fx_vertical`, `demo_click`,
`meeting_booked`) ·
sibling-vertical block · WebP, lazy-load, images under 200KB · indexable, in the sitemap, inbound
internal links in place.

---

## Designer brief — tokens from `DESIGN.md`, no exceptions

| Marker | What to produce |
|---|---|
| `[HERO]` | First screen: H1, one sentence, the vertical's number as an oversized numeral, one action. Navy `#050F40` with the radial glow, or white |
| `[CONTEXT]` | Vertical realities: stakeholder-and-cycle diagram or a regulator chip row, 15px radius chips |
| `[COMPLIANCE]` | Five short data-handling lines beside the accuracy figures, one screen. No padlock icons |
| `[WORKFLOW]` | The diverging steps highlighted against the base flow, readable on mobile |
| `[ACCURACY]` | Three oversized numerals, each with its reference underneath. The number is the hero |
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
- [ ] Visible copy 1,100 to 1,300 words; FAQ 5-6 questions; a call to action on every second screen
- [ ] Accuracy figures carry their reference and limit, plus a link to the accuracy framework; no bare percentages; no reserved words
- [ ] Boundary sentence present, stated once, in the approved wording
- [ ] 2+ cases from this vertical with numbers from `case-studies/`
- [ ] Every figure traced to `proof-points.md` and identical everywhere it appears
- [ ] Data-handling lines worded from `compliance.md`, plus the trust-FAQ link
- [ ] Price signal ("no integration fee" on FitXpress) plus a link to `/pricing/`; no public trial, no internal rates, no MT ARRs
- [ ] Vertical FAQ narrow, plus FAQPage schema that validates
- [ ] Links up, sideways to two siblings, to the hub article, to conversion
- [ ] One primary action; analytics events verified manually
- [ ] All `[markers]` replaced; alt text everywhere; mobile checked at 375 and 768
- [ ] Open items block listing every bent guardrail, for Asselya
