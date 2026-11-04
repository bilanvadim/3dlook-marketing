---
plan: plan.md
slug: virtual-clothing-try-on
workspace: virtual-clothing-try-on-mt-refresh
product: mobile_tailor
created: 2026-11-04
---

# Plan audit: virtual-clothing-try-on, refresh and reposition in place

This file explains why `plan.md` looks the way it does. It is read by `seo-publisher` and by Vadim.
The writer does not need it.

## 1. Decisions made

| # | Decision | Why |
|---|---|---|
| D1 | Phase 0 gate overridden; refresh and reposition in place; slug unchanged; no redirect | Vadim's instruction of 2026-11-04, verbatim: «переписать статью на MT с минимальной потерей траффика». No content-plan row (the plan covers FitXpress health only) and `already_live: true`: both expected for a refresh target. Same pattern as `accuracy-roi-telehealth-refresh`, `bariatric-hub-refresh`, `glp-1-market-hub-refresh` |
| D2 | Try-on stays the primary intent; Mobile Tailor answers the fit and size sub-question only | Asel's objection of 11-04 (an intent change invites demotion), and the gap analysis follows her fallback. Mobile Tailor is named in S9 and the S11 CTA only (~15%); fit and measurement together ~26%, inside the 20-30% the brief allows |
| D3 | Target query `virtual try on clothes` (350 / KD 11 / TP 800); frontmatter and headings carry `virtual try-on clothes` | It is the page's top non-brand query (42 clicks, position 18.9) and the pack's first candidate. `article_lint.py` gate 7 matches the exact string in the H1 and an H2, and house style hyphenates "try-on". Ahrefs lists the hyphenated spelling separately (90 / KD 15) |
| D4 | Head term `virtual try on` (1,300 / KD 0) carried by the H1 and several H2s, not set as primary | Pack: "do not make it the sole target". The SERP mixes makeup, eyewear and AI image tools, and the page sat at position 38.8 for it |
| D5 | H1 `Virtual Try-On Clothes in 2026: How It Works and Where Fit Comes From`; SEO title without the year | Keeps "Virtual Try-On" (brief §3.2), puts the primary in the first three words, signals the 2026 rewrite. The SEO title drops the year so the SERP snippet does not go stale |
| D6 | Fit content in two sections placed where the live "Replicating real garments" sat: S8 (shopper answer, no product) and S9 (Mobile Tailor) | Brief §3.4 placement. S8 earns the turn honestly from the fit-shaped question queries before any product appears |
| D7 | First Mobile Tailor link at ~75% depth, with no product link in the first 30% | Clarity read-through on health articles is 5-35%, so few readers reach S9. Accepted: a product link near the top would make the page read as a Mobile Tailor page (D2), and the blog style guide keeps product links out of the intro. Open item 6 offers the alternative |
| D8 | S9 accuracy paragraph = `accuracy-formulations.md` §1.1 verbatim (contains MT-ACC-SECONDARY byte-for-byte with its reference) followed by §1.8 verbatim, framework link in the paragraph | The pack requires the verbatim MT-ACC-SECONDARY with its reference and the trust link in one paragraph. §1 and §5 forms are not mixed. The §5 short form names FitXpress and cannot be used on a Mobile Tailor page. The 42-word §1.1 sentence uses the article's one allowed sentence over 35 words |
| D9 | No repeatability or ISO figure | Not needed for the argument; fewer figures, fewer rule collisions |
| D10 | All customers anonymized | Coordinator decision 2026-11-04 (pack open item 1 stays open); blog style guide: anonymize when no published case-study agreement exists |
| D11 | Author Assel Sekerova | Coordinator decision 2026-11-04; CLAUDE.md §15 default; the text is a substantive rewrite. Keeping Luke Christou stays open (item 3) |
| D12 | Every live external figure defaults to CUT; 2025-2026 sources found in planning are listed per section for the writer to verify | Brief §3.6. The live figures date from 2017-2024, several come from vendor blogs, and one (TA3 SWIM) is a YourFit case |
| D13 | Platforms and retailers named; try-on technology vendors not named | The query family asks "which website / which platform". Google, OpenAI, Zara, Tesco and Walmart are public facts and not 3DLOOK competitors. Naming vendors (Tesco's screen supplier, FASHN and others) reads as endorsement and adds no answer |
| D14 | The `free` query gets FAQ 2, not an H2 | 150/month with no KD; consumer pull that clashes with the operator CTA (pack note). One FAQ answer captures it at no cost to the structure |
| D15 | No separate "What Mobile Tailor does not do" H2; the boundary is two sentences in S9 | One product section on an informational page; a second would push the product share past the brief's ceiling |
| D16 | One CTA, S11, wording "see how Mobile Tailor works" (or "start a 7-day trial") | Coordinator decision 2026-11-04 (resolves pack open item 2). Informational/MOFU intent → soft CTA |
| D17 | Target 2,250 words | Brief range 1,900-2,400; live ~2,350. Cutting further loses the long-tail question queries the page ranked for |
| D18 | Question-shaped Search Console queries mapped one by one to answer blocks (plan.md table) | They are the page's most defensible traffic (positions 1.0-11.2) and stand in for AEO prompts, of which none is tracked for this topic |

## 2. Alternatives rejected

- **Rewrite as a Mobile Tailor explainer under the same URL.** Exactly the intent change Asel warned
  about; it would likely lose the try-on rankings and the brand sitelink would point at a product page.
- **301 to `/mobile-tailor/` or a new URL.** Loses or dilutes 94 live referring domains; against the
  instruction.
- **`virtual try on` (1,300 / KD 0) as primary.** Broad, mixed SERP, page at position 38.8.
- **`virtual fitting room` (300 / KD 10) as primary.** `virtual-fitting-room-for-ecommerce` owns it.
- **`body measurement app for clothing` (70 / KD 3) anywhere in a heading.** Owned by the sibling post
  of that name; anchor only.
- **A "best free virtual try-on apps" listicle section.** Vendor naming, consumer pull, a ranking we
  cannot substantiate.
- **Keeping the 2020-2022 brand list "as history".** Unverified as current, and it dates the page.
- **Using the §5 accuracy short form.** It names FitXpress.

## 3. Cannibalization check (§5 of the guidelines)

1. **Does an existing article already answer this?** Partly. `virtual-fitting-room-for-ecommerce`
   answers "what is a virtual fitting room, its types and benefits". `ar-clothing-try-on-tools`
   answers "who benefits from AR try-on" with its history. Neither covers 2026 generative try-on, how
   to use Google or ChatGPT try-on, or what try-on shows about fit. This URL has ranked for the broad
   "virtual try on clothes" query.
2. **Does the title overlap a sibling?** No. "Virtual Try-On Clothes" versus "Virtual Fitting Room
   Technology for eCommerce" and "AR clothing try-on". The head terms differ.
3. **Broad enough for its own page?** Yes: an existing URL with 94 referring domains and a
   2,250-word scope.
4. **Does the recommendation say refresh or do-not-duplicate?** Refresh in place (Vadim). The pack
   guardrail forbids copying the siblings' sections; S3, S4 and S7 stay short and link out.
5. **Exact intent owned:** virtual try-on for clothes in 2026: what it is, how the three approaches
   work, where to use it, what it does for brands, and what it shows about fit.

## 4. Deletions ledger (live → refreshed)

| Live section | Fate |
|---|---|
| Intro (2024-2027 market figures, UBS, "store of the future") | Rewritten as S1 with a 2026 scene, no market size |
| AR market paragraph (Statista 2017 forecast, Snapchat × Farfetch caption) | Cut; "how AR works" moves into the S3 AR H3 |
| "3D virtual fitting technology: Unlocking the virtual fitting room" | Split: mechanics → S3 (3D avatar H3), magic mirrors → S4 |
| H3 "What exactly does 'try on clothes virtually' entail for customers?" | Argument → S3; the question becomes the S6 how-to H2 |
| "Improving the ecommerce experience" (Body Labs, YourFit ×2, 48%, Request a Demo) | Online fitting-room point → S4; everything else cut |
| "The benefits of a virtual dressing room" (5 H3s) | Three hedged points in S7; Covid H3 and personalization cut; all figures default cut |
| "Leading brands pioneering virtual try-on technology" | Rebuilt as S5 with 2025-2026 examples |
| "Replicating real garments in the digital world" (YourFit ×3, API, voice-guided scan) | Argument → S8; YourFit paragraphs replaced by S9 |
| "AR virtual try-on technology: … conversion hacks" (YourFit +31/+16/+23%, 71%) | Rewritten as the S11 close with one CTA |
| No FAQ, no short answer | Added: S2 and S10 |

## 5. AEO and HubSpot

- `aeo_signals`: no tracked prompt covers apparel try-on (all 8 matched prompts in
  `workspace/seo/_aeo/2026-11-04-virtual-clothing-try-on-mt-refresh.yaml` are FitXpress health
  prompts). Plan unchanged. **Signal to Vadim:** the question this page answers is not tracked in
  HubSpot AEO.
- `open_recommendations`: none in scope.

## 6. Found during planning (2026-11-04)

- **Both cannibalization siblings still promote YourFit** (WebFetch 2026-11-04).
  `virtual-fitting-room-for-ecommerce` promotes YourFit throughout, carries the TA3 SWIM case and
  "Request a Demo". `ar-clothing-try-on-tools` has a YourFit H3 and names a brand "using YourFit".
  This refresh links to both (the guardrail requires depth links).
- **`/mobile-tailor/` disagrees with canon:** "In under 60 seconds, our AI generates a precise 3D
  model and over 85 measurements" against canon "under 45 seconds" and "80+ body measurements". The
  article follows canon.
- **2026 try-on facts checked in planning** (the writer re-verifies before use):
  - ChatGPT try-on, global launch 2026-10-01, Images 2.5 model:
    https://techcrunch.com/2026/10/01/chatgpt-can-now-virtually-try-on-clothes-for-you/
  - Google selfie try-on, "select your usual clothing size", US, 2025-12-11:
    https://blog.google/products/shopping/studio-quality-digital-try-on/
  - Google Doppl, US Labs experiment, 2025-06-26, "Fit, appearance and clothing details may not
    always be accurate.": https://blog.google/technology/google-labs/doppl/
  - Google apparel try-on in the UK and India (December 2025, secondary source):
    https://fashionunited.uk/news/fashion/google-launches-virtual-apparel-try-on-tool-in-the-uk-and-india/2025120385179
  - Tesco F&F in-store try-on trial, Sandhurst, September 2026 (trade press):
    https://retailgazette.co.uk/blog/2026/09/tesco-trials-virtual-try-on
  - Zara in-app try-on: secondary sources conflict on dates and markets; primary (Inditex) not found.
  - Walmart "Be Your Own Model": only 2022 coverage found; 2026 status unknown.

## 7. Open items for Vadim

1. **Client naming** (pack open item 1). S9 anonymizes the PPE manufacturer, the formalwear rental
   company and the 3D configurator. If Vadim clears Safariland, Jim's Formal Wear and Tailoor for a
   blog article, the three S9 bullets take the names with no other change.
2. **Byline** (pack open item 3). Planned as Assel Sekerova. Alternative: keep Luke Christou (2023
   guest author). A guest author on a text that now describes a 3DLOOK product is the weaker option.
3. **External 2026 figures** (pack open item 4). Every date and figure in S1, S4, S5, S6 and S7 is
   verify-or-drop. If Zara and Walmart cannot be confirmed from primary sources, S5 runs with three
   entries (Google, ChatGPT, eyewear line) and stays inside its budget.
4. **Sibling pages still carry YourFit.** Recommend cleaning `virtual-fitting-room-for-ecommerce`
   and `ar-clothing-try-on-tools` of YourFit soon after this republish. Otherwise the sitelink
   problem of 2026-09-24 can move to them, and readers who follow the depth links reach the
   discontinued product. Alternative: drop those two links now (lint still passes on the other
   sideways targets), at the cost of the guardrail's "link to them for depth".
5. **`/mobile-tailor/` numbers** ("under 60 seconds", "over 85 measurements") disagree with canon
   ("under 45 seconds", "80+"). Not this run's scope; flag for a product-page fix.
6. **Mobile Tailor link depth (D7).** If Vadim wants product visibility earlier, the one acceptable
   place is S2 bullet 5 (a link on "body measurements"). That moves a product link into the first
   30% and weakens the answer to Asel's objection. The plan does not do it.
7. **Year in the H1.** "in 2026" needs an update or removal in 2027. The SEO title has no year.
8. **Republish checklist additions** (on top of gap analysis §6): check the live eBook CTA and
   author bio (dropped by the capture) and remove anything YourFit-related; when restoring 2-3
   inbound links from apparel posts, pick posts that do not mention YourFit; check whether
   `case-study-ta3-swim` (a YourFit case) is still live and indexed; check the "3dlook" SERP for the
   sitelink 2-3 weeks after re-indexing (gap analysis §5).
9. **Expectation.** Recovery target is most of the ~70 non-brand clicks per month within 4-8 weeks of
   re-indexing. Not guaranteed: the page halved in the May 2026 core update before the noindex, and
   the content now carries a product section it did not have.
10. **AEO tracking.** Consider adding one apparel try-on prompt to HubSpot AEO (for example "how can
    I see which size will fit before buying clothes online?") so the page's AI-answer visibility
    becomes measurable.
