# Review digest — glp-1-market

**Article:** [GLP-1 Market Growth and the Need for Better Patient Progress Tracking](https://3dlook.ai/content-hub/glp-1-market/) — published 2026-08-28 (hub refresh, republished in place)
**Source of record:** `workspace/seo/articles/glp-1-market-hub/published-live-2026-08-28.md`
**Date:** 2026-08-28 (checks and fixes completed 2026-08-31)
**Profiles:** 9 of 9 active (`linkedin-whitney` skipped, `posts_per_week: 0`)

> **Why the source is not `publish-package.md`.** That file carries no article body, and the live
> page received a further editorial pass after `draft-v6-revision2.md` left the pipeline: ~500 words
> shorter, a new market-structure section, a market-indicator table, and materially harder hedging.
> Every post below was written against the live published text, and every claim traced back to it.
> Full draft-vs-live delta in `workspace/seo/articles/glp-1-market-hub/FINAL-PUBLISHED.md`.

## Checks

| Check | Result |
|---|---|
| `post-brand-checker` | **9/9 PASS** — run independently per post |
| `detect-ai-tells.py` | **0 markers, 0 hard bans on all 9** — only a soft rhythm marker on three |
| `quality-controller` | **6/9 complete**, all "good": 15-17/20. Three outstanding. |

`post-drafter` cannot call `post-brand-checker` itself — its definition grants no Task tool, so its
hard rule #6 is unexecutable and all nine runs reported the failure. The coordinator ran the checker
instead, which is how the findings below surfaced.

**QC still outstanding:** `linkedin-katya`, `linkedin-olena`, `linkedin-vadim`. Those three
`quality-controller` runs died on the org monthly spend limit (HTTP 429). Copy is not gated by this —
the brand checks are the binding gate and all three passed — but their rubric scores are missing.
Re-runnable with `/qc` per artifact.

**Findings raised and fixed before this digest (13):** two unexpanded `GLP-1`s and an unexpanded
`KFF` (rule M1) · a false "assets avoid photography" design tip · `article_slug` carrying the folder
name · flattened pharmacy/employer hedges on Facebook · a dropped "pricing" · a compressed retention
claim · a truncated regulatory boundary sentence · a "can provide" hardened to "give" · two posts
opening with the same "My view:" · and on Facebook, seven claims driftings including a factually
wrong "no hardware" and a guarantee where the article states a conditional. Several of the Facebook
items were caused by the coordinator's own character-count trims; that post was rewritten.

## Angle map — one entry point each, no overlap

| Profile | Angle | QC |
|---|---|---|
| twitter-company | Market scale outpacing documentation | 16/20 |
| instagram-company | The individual check-in record: weight can't say *what* changed | 16/20 |
| facebook-company | Four delivery routes, three shared needs | 15/20 |
| linkedin-company | Market structure segmenting by treatment format | 16/20 |
| linkedin-katerina | Progress tracking as a procurement and governance question (UK) | 17/20 |
| linkedin-katya | How the capability is bought: white-label, no hardware, stated limits (Israel & Gulf) | pending |
| linkedin-nick | Employer coverage data and program-level reporting (US) | 17/20 |
| linkedin-olena | Capture variance across multi-market programs (Continental Europe) | pending |
| linkedin-vadim | The caseload-level view at scale (Australia) | pending |

---

## twitter-company

**Angle:** Market scale outpacing documentation
**Length:** 257 / 240-260 chars
**QC:** 16/20

Glucagon-like peptide-1 (GLP-1) use is scaling faster than how programs document progress. J.P. Morgan projects ~25M US users by 2030. Check-ins run on a scale number and a photo in any lighting. Same capture method every time, or records aren't comparable.

**CTA:** Soft. Article link in the reply to the tweet, with link in bio as the fallback.

> **Design tip**
> Article visual: The live page ships three 2026 assets; the closest fit here is `banner_1-3.webp`, the market-projection infographic (approximately $200B global incretin market by 2030, 25M US users, 43% large-employer coverage, 59% higher-than-expected use, 66% higher spending, credited to J.P. Morgan and KFF).
> Format: text + photo
> Adaptation: Crop to the 25M US users panel alone as a single-stat card sized for the Twitter timeline, keeping the J.P. Morgan credit, and drop the $200B panel along with the two KFF employer figures (the $200B figure covers the broader incretin category and would read as the GLP-1 market next to this tweet, and the KFF numbers apply only to surveyed firms with 5,000 or more workers).
> Keep: Navy `#050F40` ground with electric blue `#143DFF` on the figure, Satoshi numerals, the visible source credit, and the abstract data-card treatment of the two `banner_*` infographics. Match the banners here, not the cover: `cover-3.webp` does use photography (a woman at a desk), so it is the wrong reference for a single-stat card.

---

## instagram-company

**Angle:** The individual check-in record: weight can't say *what* changed
**Length:** 982 / 600-1000 chars
**QC:** 16/20

Month one, month three, month six. Those three dates only tell a story if all three were captured the same way.

On a glucagon-like peptide-1 (GLP-1) program, a check-in is often a single number on a scale. That number is real, it just doesn't say what changed. Scale weight doesn't separate fat mass, lean mass and fluid balance, and a 2024 review of lean-mass change during GLP-1 treatment found substantial variation across studies.

Capturing more than weight, the same way every time, is what makes those dates comparable. Two photos, front and side, about 30 to 45 seconds, no special equipment: 80+ measurements with estimates of body fat percentage, lean mass and fat mass. For most evaluated measurements, repeat scans typically differ by less than 1 cm.

FitXpress is not a medical device. It doesn't diagnose or decide anything. It keeps the record consistent between appointments. The care team reads it. 📈

Full piece on GLP-1 growth and progress tracking: link in bio.

**CTA:** Soft — "link in bio" on the caption's closing line.

> **Design tip**
> Article visual: The live cover `cover-3.webp` — a woman at a desk with a laptop, her body stats displayed across three dates, highlighting changes in body fat and mass, under headline text on GLP-1 market growth and patient progress tracking.
> Format: carousel (3 slides)
> Adaptation: Slide 1 crops the cover tight to a single date column with only a weight figure on it and the hook line over the top; slide 2 restores the full three-date stat panel from the cover with the body-fat and mass deltas called out; slide 3 reduces to the two-photo capture glyph, front and side, captioned "same method, every date."
> Keep: The cover's three-date stat-overlay layout as the hero of the sequence, the everyday desk setting rather than a clinic, navy `#050F40` with electric blue `#143DFF` on the changing figures, Satoshi numerals, and no body-exposure imagery in any slide.

---

## facebook-company

**Angle:** Four delivery routes, three shared needs
**Length:** 1200 / 800-1200 chars
**QC:** 15/20

Glucagon-like peptide-1 (GLP-1) weight-management care reaches patients four ways: telehealth, in-person and hybrid clinics, pharmacy-led programs, and some employer-supported ones. How progress gets tracked depends partly on the route.

In a fully remote program, nobody comes in to be measured. Capture has to work in a kitchen and produce records authorized care teams can access. A hybrid clinic may measure at visits, with remote intervals between. Pharmacy-led programs may keep eligibility paperwork separate from tracking, with rules varying by jurisdiction and pharmacy model. Employer-supported programs add a data-access question that depends on the contract and applicable privacy rules.

Four routes, three shared needs: consistent capture, comparable records, appropriate access for review teams.

FitXpress handles that: two photos, about 30 to 45 seconds, no specialized scanning hardware. Consistent capture helps programs compare results more reliably over time. It is not a medical device, makes no clinical decisions and does not determine treatment eligibility.

Which model is yours, and what does a check-in look like?

Full article: https://3dlook.ai/content-hub/glp-1-market/

**CTA:** Soft. "Full article" with the link, after the discussion question.

> **Design tip**
> Article visual: The live page's second infographic `banner_2-2.webp` — the five requirements for scalable progress tracking (baseline, remote capture, records, context, professional review), 3DLOOK logo upper right.
> Format: infographic (single landscape card for the Facebook feed)
> Adaptation: Re-lay the same five requirement blocks as a horizontal Facebook-ratio card and add a top row of four route labels (telehealth, in-person and hybrid clinic, pharmacy-led, employer-supported) with connectors running down into the shared blocks, showing that all four models feed one requirement set.
> Keep: The article's five requirement blocks and their wording unchanged, navy `#050F40` ground with electric blue `#143DFF` as the single accent on the blocks, Satoshi type, the 3DLOOK logo upper right, and the abstract diagram treatment with no patient imagery.

---

## linkedin-company

**Angle:** Market structure segmenting by treatment format
**Length:** 267 / 180-280 words
**QC:** 16/20

The obesity-drug market is segmenting by treatment format. For the programs delivering care, that is a design problem.

Reuters reported in August 2026 that competition between Novo Nordisk and Eli Lilly is becoming more segmented as pills and future medications widen the range of available treatment formats. An IQVIA outlook for 2026 to 2030 names oral glucagon-like peptide-1 (GLP-1) medications and combination therapies as important parts of the developing market.

For enterprise health operators, each format has its own cadence and duration, and one provider may end up running several at once across different delivery routes. Changes in delivery format, pricing, coverage and patient adoption may affect program volume and workflow design.

Our view: as the formats multiply, the capture method is the one variable that should stay fixed. A check-in record supports comparison only when every check-in used the same defined process. Programs that settle that early keep a usable baseline while their treatment mix changes. Programs that improvise per format end up with records nobody can compare.

FitXpress adds structured body-data capture at intake and recurring check-ins. Two photos, front and side, return results in roughly 30 to 45 seconds, with no specialized hardware. For most evaluated measurements, repeat scans showed typical scan-to-scan differences of less than 1 cm. FitXpress is not a medical device and does not make clinical decisions or determine treatment eligibility. What each program documents still depends on its own protocol and intended use.

The full article covers the market indicators behind this shift and the five requirements for progress tracking that scales across delivery models.

🔗 Read it here: https://3dlook.ai/content-hub/glp-1-market/

**CTA:** Explicit but soft — "Read it here" with the live article link, per the profile's closing move.

> **Design tip**
> Article visual: The live page's second infographic `banner_2-2.webp` — the five requirements for scalable progress tracking (baseline, remote capture, records, context, professional review) as abstract blocks with the 3DLOOK logo upper right.
> Format: infographic (single square card for the LinkedIn feed)
> Adaptation: Keep the five requirement blocks as the base and add a top band of three treatment-format chips (injectable, oral, combination) fanning into the single "consistent baseline" block, with "one capture method across every format" as the caption. Deliberately different from the `facebook-company` treatment of the same asset, which is a landscape card with four delivery-route labels: this one segments by treatment format, not by delivery model, and stays square.
> Keep: The article's five requirement blocks and their wording unchanged, navy `#050F40` ground with electric blue `#143DFF` as the single accent, Satoshi type, the 3DLOOK logo upper right, and the abstract diagram treatment with no patient imagery (the cover `cover-3.webp` is photographic and is the wrong reference here).

---

## linkedin-katerina

**Angle:** Progress tracking as a procurement and governance question (UK)
**Length:** 248 / 180-250 words
**QC:** 17/20

Growth in glucagon-like peptide-1 (GLP-1) treatment has moved progress tracking from a clinical conversation into a procurement one.

When a program is small, how a check-in gets recorded is a clinical preference. As caseloads and treatment duration grow, it becomes a governance question too, and a different person answers for it.

In the UK, I see the shift in the order of the questions. Capture consistency comes first, then the roles: who is the controller, who is the processor, who may see which record, how long outputs are kept, and what may be reported to an employer or a health plan.

Those answers vary by deployment and contract, which is why they belong in the evaluation. Finding them at amendment stage is expensive.

Employer-supported programs show it most clearly. A provider, a health plan and a benefits platform can sit inside one program, with access and reporting rights set by structure and contract.

My position is simple: a vendor should be able to state its role in writing before a pilot starts. In most enterprise deployments the customer is the controller and 3DLOOK is the processor. Photos are deleted after processing in production workflows, and the structured output is retained per the agreement.

FitXpress is not a medical device. It does not diagnose or determine treatment eligibility. It documents, and the documentation has an accountable owner.

I have linked the market piece we published today. Worth a read if you are scaling a program this year 👇
https://3dlook.ai/content-hub/glp-1-market/

**CTA:** Soft invitation to explore the article, per the profile's closing move. One emoji, no hashtags.

> **Design tip**
> Article visual: The live page's cover `cover-3.webp` — a woman at a desk with a laptop, her body stats shown across three dates, under headline text on GLP-1 market growth and progress tracking.
> Format: text (native LinkedIn post, no card — a founder speaking about contracts and accountability reads more credibly unpolished, and the three article assets are already claimed by the Twitter, Instagram and Facebook posts in this pack)
> Adaptation: no visual needed — native platform format.
> Keep: n/a.

---

## linkedin-katya

**Angle:** How the capability is bought: white-label, no hardware, stated limits (Israel & Gulf)
**Length:** 235 / 180-250 words
**QC:** pending — blocked on spend limit

When a digital health operator in Israel or the Gulf adds progress tracking to a glucagon-like peptide-1 (GLP-1) program, the early questions are commercial ones.

The first is whose brand the patient sees. A weight-management program spends real money building its own app and its own check-in flow. Sending a patient out to a third-party experience halfway through undoes part of what the program paid for. FitXpress is delivered white-label, which means guided capture sits inside the program's own patient experience and carries the program's name.

The second is what has to be bought before launch. The scan runs on two photos, front and side, in roughly 30 to 45 seconds, with no specialized scanning hardware. For a regional operator scaling across markets, that removes a procurement cycle from the plan.

The third is trust, and in this region it matters more than either.

The piece we published today is explicit about what the product does not do. FitXpress is not a medical device. It does not diagnose conditions, make clinical decisions, prescribe treatment, or determine treatment eligibility. It sits alongside the measurement methods a clinic already uses.

My view: a vendor that states its limits plainly is easier to bring in front of a clinical committee than one that leaves them for the buyer to find later.

Where does a body-data vendor lose your trust first: an overclaim, or a vague answer?

🔗 https://3dlook.ai/content-hub/glp-1-market/

**CTA:** Discussion question first, then the link to the live article, per the profile's closing move. One emoji, no hashtags.

> **Design tip**
> Article visual: The live page's second infographic `banner_2-2.webp` — the five requirements for scalable progress tracking (baseline, remote capture, records, context, professional review) as abstract blocks with the 3DLOOK logo upper right.
> Format: screenshot (one quote card carrying the article's own limitations sentence, which is the trust proof the post is built on and lands harder as a card than as a fifth paragraph)
> Adaptation: Drop the five requirement blocks and set a single line from the article's Role and Limitations section as the whole card, quoted verbatim — "FitXpress is not a medical device and does not diagnose conditions, make clinical decisions, prescribe treatment, or determine treatment eligibility" — with a small `3dlook.ai/content-hub/glp-1-market` source line beneath it. This is a clearly different treatment of the asset from the two already claimed on it: the square five-block format chips on `linkedin-company` and the two-column capture-variance card on `linkedin-olena`.
> Keep: Navy `#050F40` ground with electric blue `#143DFF` as the single accent, Satoshi type, the 3DLOOK logo upper right, the article's exact wording, and the abstract non-photographic treatment of the `banner_*` assets with no patient imagery (the cover `cover-3.webp` is a photograph of a woman at a desk and is not the reference here).

---

## linkedin-nick

**Angle:** Employer coverage data and program-level reporting (US)
**Length:** 249 / 180-250 words
**QC:** 17/20

Coverage for glucagon-like peptide-1 (GLP-1) treatment moved quickly inside the largest US employers, and the reporting question came with it.

The 2025 Kaiser Family Foundation (KFF) Employer Health Benefits Survey: among surveyed firms with 5,000 or more workers, 43% provided coverage in 2025, up from 28% in 2024. Among those that provided coverage, 59% reported higher-than-expected use and 66% reported a significant effect on prescription-drug spending.

One survey, very large employers only, and I would not read it wider than that. For a telehealth provider, pharmacy-led program or benefits platform serving firms that size, it still says something about the buyer across the table.

Higher-than-expected use and the spending effect create additional considerations for those firms, which may contribute to greater interest in consistent program-level reporting.

What can be reported depends on the structure. An employer-supported program may run through a provider, a health plan, a benefits platform, or a combination, with reporting rights determined by contract and applicable privacy requirements.

The operational work starts at capture. Program-level reporting is assembled from individual check-in records, which aggregate only when every check-in used the same defined process.

FitXpress covers that part: two photos, front and side, roughly 30 to 45 seconds, no specialized hardware. For most evaluated measurements, repeat scans showed typical scan-to-scan differences of less than 1 cm. It is not a medical device and does not determine treatment eligibility.

For US teams in employer-sponsored channels: does reporting come up at contracting, or at renewal?

Full article 🔗 https://3dlook.ai/content-hub/glp-1-market/

**CTA:** Discussion question first, then a soft invitation to the live article, per the profile's closing move. One emoji, no hashtags.

> **Design tip**
> Article visual: The live page's first infographic `banner_1-3.webp`, a data card carrying the market projections ($200B by 2030, 25M US users, 43% large-employer coverage, 59% higher-than-expected use, 66% higher spending), credited to J.P. Morgan and KFF.
> Format: text + photo (one stat card in the feed under the post)
> Adaptation: Crop away the $200B and 25M panels that the Twitter post already used and keep only the three employer figures (43% / 59% / 66%) as a square card, with the qualifier "surveyed firms with 5,000 or more workers, 2025 KFF Employer Health Benefits Survey" set as a readable footnote line under the numbers instead of fine print, since the scoping is the point of the post.
> Keep: The asset's navy `#050F40` ground with electric blue `#143DFF` as the single accent on the figures, Satoshi type, the existing J.P. Morgan and KFF source credit, and the abstract data-card treatment of `banner_1-3.webp` with no patient imagery (the photographic cover `cover-3.webp` is not the reference here).

---

## linkedin-olena

**Angle:** Capture variance across multi-market programs (Continental Europe)
**Length:** 248 / 180-250 words
**QC:** pending — blocked on spend limit

A European glucagon-like peptide-1 (GLP-1) program rarely runs in one place.

Several markets, several sites, different teams on the same protocol, sometimes different languages in one check-in form. Every one of those is a place where capture can drift.

What can vary at a check-in:

• Self-reported measurements, because technique, equipment, timing and data entry differ
• Progress photos, because lighting, pose, distance, clothing and camera angle differ
• Free-text notes, because the recorded fields and level of detail differ across patients and staff

Each is minor on its own. Together they set how comparable a March record and a September record are. As caseloads and treatment duration increase, inconsistently collected information becomes harder to organize and review.

I treat capture consistency as an operations decision before a clinical one. Across several markets it decides whether you end up with one comparable dataset or a separate one per site.

The remedy is unglamorous. One defined capture process, used for the baseline and every check-in after it, with explicit guidance for pose, image collection and timing. Without it, each site defines its own.

FitXpress is one way to standardize that step: a guided scan, two photos front and side, roughly 30 to 45 seconds, no specialized hardware. For most evaluated measurements, repeat scans showed typical scan-to-scan differences of less than 1 cm. It is not a medical device and does not determine treatment eligibility.

Is your capture process defined centrally, or does each site decide?

Full article 🔗 https://3dlook.ai/content-hub/glp-1-market/

**CTA:** Discussion question first, then the invitation to the live article, per the profile's closing move. One emoji, no hashtags.

> **Design tip**
> Article visual: The live page's second infographic `banner_2-2.webp` — the five requirements for scalable progress tracking (baseline, remote capture, records, context, professional review) as abstract blocks with the 3DLOOK logo upper right.
> Format: screenshot (one text card carrying the article's variance finding, which reads harder as a card than as a third bullet list in the feed)
> Adaptation: Rebuild it as a two-column card in the same visual system: the left column stacks the three capture inputs with what varies in each (technique / equipment / timing / data entry · lighting / pose / distance / clothing / angle · recorded fields and detail), and the right column collapses them into a single "one defined capture process" block, keeping only requirements 1 and 2 of the five highlighted. This stays clear of the two treatments of the same asset already claimed, the square format-chip card on `linkedin-company` and the landscape delivery-route card on `facebook-company`.
> Keep: Navy `#050F40` ground with electric blue `#143DFF` as the single accent, Satoshi type, the 3DLOOK logo upper right, the article's own wording for the variance sources, and the abstract diagram treatment of the `banner_*` assets with no patient imagery (the cover `cover-3.webp` is a photograph of a woman at a desk and is not the reference here).

---

## linkedin-vadim

**Angle:** The caseload-level view at scale (Australia)
**Length:** 246 / 180-250 words
**QC:** pending — blocked on spend limit

Scale changes what an Australian health team is actually reviewing.

A glucagon-like peptide-1 (GLP-1) program with a few hundred patients reviews people one at a time. Past a certain volume, the team also reviews the caseload: how a cohort is tracking, and who needs a closer look this month.

The piece we published today puts it plainly. As caseloads and treatment duration increase, inconsistently collected information becomes more difficult to organize and review. Structured records can give clinical and program teams a more consistent basis for comparison across individual patients and the wider caseload.

Here is the operational catch. A caseload view is only as good as the capture underneath it. Records built five different ways do not roll up. On a report they still look comparable.

In Australia this arrives early, because many programs are remote-first by geography. In a fully remote workflow the check-in is the record, with no in-person appointment behind it.

I would settle the capture method before the caseload grows. Retrofitting consistency onto two years of mixed records is the expensive version.

That is the part FitXpress handles. Two photos, front and side, return results in roughly 30 to 45 seconds, with no specialized scanning hardware. For most evaluated measurements, repeat scans showed typical scan-to-scan differences of less than 1 cm. It is not a medical device and does not determine treatment eligibility.

Australian operators: where does your caseload view break first, at capture or at reporting?

Full article 🔗 https://3dlook.ai/content-hub/glp-1-market/

**CTA:** A question to the Australian operators first, carried into the native poll, then a soft invitation to the live article. One emoji, no hashtags.

> **Design tip**
> Article visual: The live page's second infographic `banner_2-2.webp`, the five requirements for scalable progress tracking (baseline, remote capture, records, context, professional review) as abstract blocks with the 3DLOOK logo upper right.
> Format: poll (LinkedIn native, two options: "At capture" and "At reporting", question: "Where does a scaling GLP-1 caseload break first?")
> Adaptation: No visual needed. This is a native platform format, and the poll carries the closing question instead of a card, which also keeps the post clear of the four treatments already claimed on the three article assets in this pack.
> Keep: n/a.

---
