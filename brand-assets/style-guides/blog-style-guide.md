# 3DLOOK Blog Style Guide

> Based on analysis of 9 production articles from `3dlook.ai/content-hub/`: 4 FitXpress + 5 Mobile Tailor.
> Created: 2026-05-22. Source files: `brand-assets/past-articles/blog/`.

> **Critical note on style evolution.** The corpus contains two distinct eras. The **2026 Assel Sekerova articles** (4 of 9) represent the current target style: measured, hedged, fact-dense, B2B compliance-conscious, audit-trail-aware. The **2024 articles** (5 of 9, multiple authors) use looser industry-trend prose with heavy buzzword density ("leverage", "revolutionize", "game-changer", "harness the power") — patterns that CLAUDE.md section 6 now bans. **New articles must follow the 2026 style, not the 2024 style.** Where this guide describes "the voice", it means the 2026 voice unless explicitly stated.

---

## 1. Voice & Tone

**Default voice (FitXpress and Mobile Tailor alike, 2026 era):** Authoritative, educational, B2B trade-publication. Reads like a serious analyst memo more than a marketing post. The reader is an operator, compliance lead, VP of underwriting, head of e-commerce, or director of procurement — not a consumer.

Three constants across the 2026 corpus:

- **Hedged claims, not effusive ones.** Outputs are "supportive body data", a "fraud-prevention support layer", a "non-clinical underwriting-support input". Never "the solution that fixes X" or "a game-changer."
- **Stats-first, opinion-second.** Numbers from named external sources (NAIC, CDC, Swiss Re, McKinsey, LIMRA, Munich Re, Gen Re) carry the argument. Editorial line follows.
- **Workflow language, not feature language.** The article describes where the technology sits in the buyer's existing process ("pre-screening, evidence collection, applicant verification, workflow acceleration"), not what the technology does in isolation.

**FitXpress vs Mobile Tailor — tonal differences:**

| Dimension | FitXpress | Mobile Tailor |
|-----------|-----------|---------------|
| Hedging intensity | Very high — includes explicit `**Disclaimer.**` blocks, "not a replacement for medical exams", "not standalone decisioning" | Moderate — sustainability and fit framing, less regulatory hedging |
| Compliance vocabulary | Heavy — HIPAA, GDPR, audit trail, BAA, retention, encrypted in transit and at rest | Lighter — mostly privacy mentions, not regulatory deep-dives |
| Use of disclaimers | Standard pattern (see insurance article L24) | Not present |
| Stats sourcing | Primary mode of argument | Stats present but mixed with brand name-drops as social proof |

---

## 2. Article Structure

**Length:**
- Typical range: **2,200–4,200 words**
- FX use-case deep-dive sweet spot: **3,500–4,200 words** (e.g., insurance underwriting, wellness rewards)
- MT industry-trend sweet spot: **2,500–3,500 words**
- Product deep-dive: **2,500–3,000 words** (e.g., 3dlook-turns-two-photos)
- **Avoid going below 2,000 or above 4,500** unless format requires it

**H2 count:** 4–15 main H2s. Use-case articles tend toward 11–15 H2s with multiple H3 subsections. MT trend articles tend toward 4–8 H2s with many H3s under each.

**Standard intro pattern (newer style):**
1. **No setup, no "in today's fast-paced world".** First sentence is the problem statement or a market data point.
2. **One-paragraph context.** What's broken or shifting.
3. **One-paragraph orientation.** What this article will cover.

Example (insurance article opening): "Accelerated underwriting has helped life insurers reduce friction, shorten application timelines, and move more applicants through digital journeys. But faster underwriting also creates a practical evidentiary challenge..."

**Use Case Summary block (FX pattern):** Newer FX use-case articles open with a structured block before the intro:

```
**Industry** — [target verticals]
**Problem** — [one line]
**Solution** — [one line, hedged: "guided mobile body scan"]
**Outputs** — [structured outputs, hedged: "Structured body-related measurements and verification signals"]
**Role** — [what it is NOT: "Supporting evidence for underwriting review — not standalone decisioning"]
**Business value** — [3-4 phrases]
```

Apply this block to any new FX use-case article. MT articles do not use it.

**Standard conclusion pattern:**
1. **One-paragraph recap.** Reframe the main argument in plain terms.
2. **Business value summary.** What changes operationally.
3. **`### Next Steps` subsection (FX) or `## Final Thoughts` (MT older).** Single demo or contact CTA.
4. **FAQ section (FX standard, optional MT).** 5–8 Q&A pairs in bold-question + plain-paragraph format. Repeat target keywords naturally in questions.

---

## 3. Fingerprint Phrases — Top 30 (use 3–6 naturally in any new article)

These are the recurring formulations across the corpus that constitute "our voice." Mix and match — do not stuff.

**Product / capability phrasings:**

1. `two photos` / `two smartphone photos` / `front and side smartphone photos`
2. `80+ body measurements` (always with the plus, always exact phrasing)
3. `in under 45 seconds` / `approximately 45 seconds` / `roughly 45 seconds`
4. `guided mobile scan` / `guided smartphone scan` / `guided two-photo flow`
5. `structured body data` (2026 signature — use this, not "body measurement data")
6. `AI-powered computer vision` / `AI-driven 3D body scanning`
7. `Smart Scales` (always proper noun, never "smart scale")
8. `Future Body` (always proper noun)
9. `mobile-first workflow` / `scalable, mobile-first workflow`
10. `without specialized hardware`

**Positioning hedges (FX — use these to stay on the right side of compliance):**

11. `supportive body data outputs rather than standalone diagnostic conclusions`
12. `non-clinical underwriting-support input`
13. `fraud-prevention support layer` (NOT "fraud detection")
14. `not a replacement for required medical evaluations`
15. `support tool for underwriters — not a replacement`

**Compliance vocabulary (FX):**

16. `HIPAA compliance and adheres to GDPR principles`
17. `Images are blurred, used only to generate scan results, and deleted immediately after processing`
18. `encrypted in transit and at rest, with role-based access controls`
19. `auditable digital trail per case` / `audit-ready evidence`
20. `applicant verification`

**Workflow vocabulary:**

21. `evidence collection` (insurance) / `verification workflow` (wellness)
22. `disclosed vs. captured measurements`
23. `accelerated underwriting`
24. `BMI/build verification`

**Mobile Tailor industry vocabulary:**

25. `made-to-measure (MTM)` / `made-to-order (MTO)`
26. `on-demand manufacturing` / `on-demand production`
27. `scan-to-pattern automation`
28. `factory-ready files`
29. `size inclusivity`
30. `mass customization`

---

## 4. How We Present Facts

**Numbers:** Yes, heavily. Every concrete claim should trace to a named external source (NAIC, CDC, Swiss Re, Munich Re, LIMRA, Gen Re, McKinsey, KFF, BoF, ThredUp, Statista). When citing 3DLOOK's own numbers, use the documented set: `96–97% accuracy`, `error margin 1.5–2.0 cm`, `95%+ repeatability`, `<1 cm variance across repeated scans`, `80+ measurements`, `~45 seconds`.

**Citations:** Always inline ("According to Swiss Re...", "Munich Re reported in 2025 that...", "CDC researchers found that..."). **No footnotes. No external hyperlinks to source sites.** The source name is the citation.

**Bold for key terms:** Yes, used for:
- Section-opening claims that summarize an argument (`**The strongest use case for AI is as a support tool for underwriters — not a replacement for or elimination of human judgment.**`)
- Disclaimer markers (`**Disclaimer.**`)
- Bullet labels in structured lists (`**Faster underwriting cycle time.** [explanation]`)
- Stat call-outs in mid-paragraph (`**$308.6 billion a year**`, `**$74.7 billion in life insurance fraud**`)

Avoid bolding for decoration. Each bold should change the reader's parsing.

**Competitors:** Never named directly. Discuss the category ("vendors", "any verification vendor"). The competitors that DO appear by name in articles are non-overlapping industry players used as examples (Nike, Zara, Patagonia, Unspun, Bolt Threads) — never Prism Labs, Bodygram, or Size Stream.

**Tables:** Used in comparison / use-case articles to contrast traditional vs new workflow. Standard column patterns:
- Method | Remote | Standardization | Repeatable | Audit trail | Scaling
- Criterion | 2-Photo Scan | Video Flow | Hardware 3D Scanner
- Parameter | Traditional Underwriting | AI-Assisted + Mobile 3D Body Scanning

Use them when the argument is structurally a comparison. Don't force a table where prose works.

**Quotes / pull quotes:** Rare. One example (sustainable-fashion-manufacturing) uses a Stella McCartney pull quote for atmospheric purposes. Default to no pull quotes in serious B2B articles.

---

## 5. CTA Standards

**Default CTA pattern (2026):**

- **FX use-case articles:** "See how **FitXpress** can support [specific workflow] in your [audience program]. Get in touch with 3DLOOK or book a demo to explore the technology in practice with our team." — under a `### Next Steps` subheading.
- **FX product deep-dive:** "Book a demo to explore how FitXpress, Mobile Tailor, and 3DLOOK's AI-powered body scanning solutions can work for your business."
- **FX wellness/insurance articles:** "Request a demo to check how 3DLOOK can help modernize [workflow] and find the right workflow for your program."
- **MT (older pattern, still in production):** "Discover the full benefits of YourFit" or "Speak to a 3DLOOK expert to find a solution that supports your brand goals and objectives."

**CTA targets:**

- Primary: `https://3dlook.ai/pricing/` (with `#bd-modal-personalized` for the demo modal)
- Secondary: `https://3dlook.ai/contact-us/`
- Trial (rare, for self-serve product CTAs): `https://mtm.3dlook.me/accounts/signup`
- Homepage as fallback: `https://3dlook.ai/`

**Demo vs trial discipline:**
- Compliance-buyer audience (insurance, pharmacy, telehealth, employer wellness, Medicare Advantage) → **demo only**, never self-serve trial
- MT/apparel audience → demo or trial both acceptable, depending on the buyer profile

**One CTA per article. No banner-style "subscribe to our newsletter" mid-body.**

---

## 6. Internal Linking

**Most-linked targets across the corpus:**

| Target URL | Anchor patterns we use |
|------------|------------------------|
| `https://3dlook.ai/` (homepage) | "3DLOOK", "AI-driven 3D body-scanning solutions", "FitXpress by 3DLOOK", "YourFit" |
| `https://3dlook.ai/mobile-tailor/` | "Mobile Tailor" |
| `https://3dlook.ai/mobile-tailor/for-on-demand-manufacturing/` | "Mobile Tailor" |
| `https://3dlook.ai/for-bmi-verification/` | "BMI/build verification", "verification process", "live photo capture" |
| `https://3dlook.ai/fitxpress/for-telehealth-and-weight-loss/` | "weight-loss and telehealth" |
| `https://3dlook.ai/case-studies/` | "organizations that need structured body data" |
| `https://3dlook.ai/content-hub/[other-article]/` | Article-title-as-anchor (full or partial title) |
| `https://3dlook.ai/pricing/` | "Book a FitXpress demo", "Let's talk" |
| `https://3dlook.ai/contact-us/` | "Book a demo", "Talk to 3DLOOK" |

**Rules:**
- 4–8 internal links per article. Newer FX articles tend toward 3–5; older MT articles toward 6–10.
- **Always descriptive anchors, never "click here" or "this article".** The anchor should preview what the linked page covers.
- Cross-link to other content-hub articles 2–4 times per article — this is the SEO topic-cluster pattern visible across the corpus.
- Product-page links (`/for-bmi-verification/`, `/technology/`, `/mobile-tailor/`) should appear in the most relevant body section, not in the intro.
- CTA links in the conclusion are separate from in-body internal links — count them additionally.

---

## 7. Banned Patterns (specific to our blog)

**Phrases that do NOT appear in the 2026 articles and should NOT appear in new ones** (these align with CLAUDE.md section 6):

- "In today's fast-paced world / digital era / fashion landscape"
- "Game-changer", "revolutionary", "cutting-edge", "disrupt"
- "Leverage" / "leveraging" (the 2024 articles use this dozens of times — 2026 articles avoid it almost completely)
- "Harness" / "harness the power of"
- "Utilize" / "utilization" (use "use" / "uses")
- "Robust", "seamless", "comprehensive" (as standalone adjectives for the product)
- "Delve into", "navigate" (figurative), "tapestry", "realm"
- "Furthermore / Moreover / Additionally" as sentence starters (the 2024 articles sin here repeatedly)
- "It's not just X, it's Y" rhetorical construction
- Triple parallelism ("fast, reliable, scalable")
- "Unlock the power of"
- "Pioneer / pioneering" (used in 2024 article titles — feels dated now)
- Em-dash in rhetorical "X — это не просто Y" constructions (em-dash is fine as a parenthetical separator)

**Stylistic patterns to avoid:**

- **Effusive product praise.** Replace "Mobile Tailor is a groundbreaking solution that transforms..." with "Mobile Tailor turns two photos into 80+ body measurements used directly in sizing workflows." Cut all "transforms / redefines / reshapes" verbs unless tied to a specific operational change.
- **First-person "I" / "we believe / we think".** The 2026 articles use "we" only when stating what 3DLOOK does ("we built FitXpress to..."). They never say "we believe" or share opinion in first person.
- **Questions as section titles.** Older MT articles use this ("Why Are Virtual Body Measurements a Big Deal?"). Newer FX articles use declarative titles. Prefer declarative.
- **Smiley emojis, decorative emojis.** No 🚀 ✨ 💡 in body. Bullet points can use `*` or `-`, not ✅ or → unless the article is a short list-style piece.
- **All-caps section headers.** Never. The "TECHNOLOGY OVERVIEW" header in `on-demand-fashion-industry-tech-landscape` is a formatting artifact and should not be repeated.
- **Trailing exclamation points.** No.
- **Marketing-tail sentences** ("This is what we mean by innovation."). Cut.

---

## 8. Vertical-Specific Notes

### FitXpress

**Audience profile:** Senior compliance leads, VPs of underwriting, chief medical officers, directors of clinical operations, heads of compliance at online pharmacies, Medicare Advantage plan operations leads, employer benefits leaders, CROs / clinical trial sponsors. They read this article looking for evidence they can take into a procurement conversation or an audit defense.

**Special vocabulary** (use these — they signal we understand the buyer's world):
- Clinical: BMI, BMR, body composition, body fat %, lean mass, fat mass, GLP-1, accelerated underwriting, paramedical exam, APS (Attending Physician Statement), MIB
- Compliance: HIPAA, GDPR, BAA (Business Associate Agreement), audit trail, encrypted in transit and at rest, role-based access controls, role-based permissions, retention policy, role-based, data minimization
- Workflow: pre-screening, evidence collection, applicant verification, workflow acceleration, triage, case routing, fraud-prevention support layer, eligibility gate
- Regulatory bodies: GPhC (UK), FDA (US), NAIC, CDC, HHS, NHCAA

**Stance on regulation:** Cautious, opt-in to compliance language. Always position FitXpress as "non-clinical", "supporting evidence", "not standalone decisioning". Reference regulatory bodies in general terms (no invented clauses, memo titles, or guidance numbers). Acknowledge that "depending on jurisdiction, processing purpose, and implementation design, photos and body-derived outputs may be treated as personal, sensitive, health-related, or biometric data" — this exact framing from the insurance article is the safe phrasing for any new compliance-adjacent article.

**Disclaimers:** When the use case touches medical decisions, include a `**Disclaimer.**` block early in the article. Pattern: "Mobile 3D body scanning can support [workflow], but it does not [forbidden claim], replace required [medical evaluations], or make [clinical judgments]."

### Mobile Tailor

**Audience profile:** Founders and heads of e-commerce at MTM brands, VPs of operations at uniform companies, heads of product development at on-demand manufacturers, directors of procurement at PPE/medical/public-safety apparel companies, bridal/formalwear ops leads.

**Special vocabulary:**
- Manufacturing: on-demand manufacturing, made-to-measure (MTM), made-to-order (MTO), micro-factory, on-demand factory, scan-to-pattern automation, factory-ready files, small-batch production, pattern-making, 3D weaving, 3D printing
- Fit: body measurements (always with "body" — never just "measurements"), 80+ measurements, custom-fit, perfect fit, size inclusivity, return rates, remakes
- Sustainability: circular textiles, circularity, supply chain transparency, fair labor, ethical sourcing, biofabrication, biodegradable materials, GOTS (Global Organic Textile Standard)
- Industry stakeholders: brands, retailers, fashion executives, supply chain, e-commerce, brick-and-mortar

**Stance on industry change:** Optimistic but measured. The 2024 articles overdo "transforming / reshaping / revolutionizing". The 2026 standard for MT is to describe operational changes concretely: "reduces return rates", "supports on-demand factory output", "integrates into B2B ordering pipelines". Sustainability is a value lever to mention but should not dominate the argument.

**Stats sources for MT:** McKinsey State of Fashion, BoF, ThredUp, Statista, Business Research Company, Coresight Research, Qualtrics. Use these — they're the existing precedent.

---

## 9. Article Types Taxonomy

The corpus contains 6 distinct article types. Each has its own structural template.

### Type A — Use-Case Deep-Dive (FX preferred format)
**Examples:** `mobile-body-scanning-insurance-underwriting`, `wellness-rewards-verification`
**Target length:** 3,500–4,200 words
**Structure:**
1. Use Case Summary block (Industry / Problem / Solution / Outputs / Role / Business value)
2. Introduction (2–3 paragraphs, includes a `**Disclaimer.**` line)
3. "Where [Product] Fits" — positions the product against the workflow
4. "What Is [Workflow]?" — defines the buyer's existing process
5. Workflow breakdown — H3 subsections per stage
6. Problem deep-dive — the specific gap (e.g., "Build & BMI Misrepresentation Problem")
7. Comparison table — Traditional vs AI-Assisted
8. Fraud / Risk support layer — how technology addresses the gap (hedged framing)
9. Key Business Benefits — bulleted, each with one-line explanation
10. Important Compliance Considerations — explicit
11. Conclusion + `### Next Steps`
12. FAQ — 5–7 pairs

### Type B — Product Deep-Dive
**Examples:** `3dlook-turns-two-photos-structured-body-data`
**Target length:** 2,500–3,000 words
**Structure:**
1. One-paragraph intro
2. "How [product] technology works" — numbered step-by-step (4 steps usually)
3. "What [product] generates from [input]" — output catalog
4. Per-output sections (80+ measurements, body composition, body progress, Smart Scales, Future Body)
5. "What inputs [product] uses"
6. "Why [product] uses [method] instead of [alternative]"
7. "How [product] outputs support different use cases"
8. "How accurate are [product] results?" — proof points
9. Conclusion with demo CTA
10. FAQ — 10–15 pairs (longer than Type A)

### Type C — Comparison / Buyer's Guide
**Examples:** `body-scanning-technology-comparison`
**Target length:** 3,000–4,000 words
**Structure:**
1. Intro framing the choice
2. Quick Answer Block — bulleted summary up top
3. Definition section ("What Is [Category]?")
4. Comparison table — side-by-side
5. Trade-offs section — accuracy / privacy / scalability / cost
6. Business-fit section — per audience segment
7. "Where 3DLOOK Fits Best" — product positioning at the end
8. FAQ — 5–7 pairs

### Type D — Industry Analysis / Trend Piece (MT preferred format)
**Examples:** `on-demand-clothing-manufacturing`, `sustainable-fashion-manufacturing`
**Target length:** 2,500–3,500 words
**Structure:**
1. Atmospheric intro — market context, optional pull quote
2. "What Is [Topic]?" — definition
3. "Multiple Benefits / Key Players" — H3 numbered subsections
4. Industry examples — brand name-drops (Nike, Zara, Patagonia, Unspun, etc.)
5. Technology section — how 3DLOOK fits
6. Case study mentions — 1822 Denim, Slø Jeans, MADE Outdoor (anonymize if no published case study agreement exists)
7. "Final Thoughts" — slow conclusion + CTA

### Type E — Tech Landscape Mapping
**Examples:** `on-demand-fashion-industry-tech-landscape`
**Target length:** 3,000–3,500 words
**Structure:**
1. Intro
2. Numbered tech categories (typically 8–9)
3. Each section: definition + how it works + KEY COMPANIES list (vendor map)
4. Final thoughts

This format is heavy and reads like a buyer's directory. Use it for annual landscape pieces.

### Type F — Trend Roundup (annual)
**Examples:** `the-future-of-fashion-retail`
**Target length:** 3,500–4,000 words
**Structure:**
1. Year-framing intro (cite McKinsey State of Fashion)
2. Numbered trend list — 12–15 trends as H3s
3. Each trend: 3–4 paragraphs with stats + brand examples
4. "Why technology is crucial" — bridge section
5. "Embracing digital transformation" — closing argument with product mention
6. Product-fit section at end

---

## 10. Quick Pre-Publish Checklist

Before any new blog article ships, verify:

- [ ] Word count within the type's expected range (Section 9)
- [ ] H1 contains target keyword or close variant
- [ ] H2/H3 hierarchy correct — no all-caps headers, no question-style titles unless Type B/C/D
- [ ] 3–6 fingerprint phrases from Section 3 appear naturally
- [ ] All numbers cite a named external source (or the 3DLOOK documented number set)
- [ ] FitXpress articles include a `**Disclaimer.**` block when touching medical decisions
- [ ] No banned phrases from Section 7 (run a Find for "leverage", "harness", "revolutioniz", "game-chang", "in today's", "Furthermore", "Moreover")
- [ ] No competitors named directly (no "Prism Labs", "Bodygram", "Size Stream")
- [ ] Customer references — if no published case-study agreement exists, anonymize ("a leading UK online pharmacy"); otherwise name only as agreed
- [ ] CTA matches audience (demo-only for compliance buyers; demo+trial OK for MT apparel)
- [ ] 4–8 internal links, descriptive anchors, none pointing to placeholder URLs
- [ ] Frontmatter includes `author: Assel Sekerova` (default) unless founder-voice piece signed by Katerina Galich
- [ ] Reads aloud without any sentence sounding like a chatbot

---

## Sources for this guide

All claims and patterns in this document trace to one or more files in `brand-assets/past-articles/blog/`. To verify any specific pattern, re-read the source article cited in the example.

Most-instructive references for new writers (read these first):
1. `mobile-body-scanning-insurance-underwriting.md` — gold standard for Type A (FX use-case)
2. `body-scanning-technology-comparison.md` — gold standard for Type C (comparison)
3. `3dlook-turns-two-photos-structured-body-data.md` — gold standard for Type B (product deep-dive)
4. `on-demand-clothing-manufacturing.md` — example of Type D done in older voice (good for structure, dated for vocabulary — do NOT mimic phrasing)
