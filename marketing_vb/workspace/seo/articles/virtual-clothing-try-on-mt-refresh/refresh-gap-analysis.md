---
slug: virtual-clothing-try-on
workspace: virtual-clothing-try-on-mt-refresh
product: mobile_tailor
hub: "Apparel (Mobile Tailor), no content-plan row"
intent: Informational/MOFU (try-on research) with a Mobile Tailor bridge
action_type: refresh-reposition-in-place
live_url: https://3dlook.ai/content-hub/virtual-clothing-try-on/
live_published: 2023-05-10
live_modified: 2026-09-24
live_robots: "noindex, follow (set deliberately 2026-09-24, see §1)"
baseline_file: published-live-2026-11-04.md
baseline_words: ~2,350
live_byline: Luke Christou
prepared: 2026-11-04
status: input-to-plan
---

# Refresh gap analysis: Virtual Try-on for Clothing → Mobile Tailor

Prepared before Phase 0, so the plan starts from the live page and its Search Console record.

## 0. Why this refresh runs (the Phase 0 override)

There is no content-plan row for this URL. The content plan covers FitXpress health topics, and this is an
apparel post. Phase 0 would STOP here.

**Gate overridden. Vadim gave the instruction on 2026-11-04:** «переписать статью на MT с минимальной
потерей траффика». He accepts that some traffic will be lost. **Republish at the same URL. The slug does
not change. No redirect. No net-new page.** Precedents for refresh in place: `accuracy-roi-telehealth-refresh`
(09-23), `bariatric-hub-refresh` (09-03), `glp-1-market-hub-refresh` (08-01).

## 1. What happened to the page

- **2026-09-24.** Whitney asked why Google showed YourFit / «Virtual try on» as a sitelink under brand searches
  for 3DLOOK. YourFit is the discontinued try-on product, and its `/yourfit/` page already 301s to `/`. The
  post mentions YourFit 11 times, with YourFit-only results (48% fewer returns, TA3 Swim 47%, +31% engagement,
  +16% conversions, +23% AOV).
- **Same day, Asel** removed the internal links to the post and set `noindex` in Yoast. On 10-01 the sitelink
  was gone. Google now reports «Excluded by ‘noindex’ tag» (crawled 2026-11-02).
- **2026-11-04, Vadim:** noindex was an interim fix. Rewrite the post for Mobile Tailor and keep as much
  traffic as possible.
- **Asel's objection (11-04), which the plan must answer:** the topics are different (try-on visualization
  vs body measurement). If the page turns into an MT page, Google will see the intent change and demote it.
  Her fallback: rewrite it so the two topics are linked. **This analysis follows her fallback.** Try-on stays
  the primary intent, and MT is the answer to one sub-question inside it: fit and size.

## 2. Search record (Google Search Console, page filter)

**Monthly clicks / impressions:**
2025-07 308/36.3K · 2025-09 229/34.0K · 2025-12 174/36.6K · 2026-01 229/54.4K · 2026-03 211/34.7K ·
2026-05 202/33.1K · 2026-06 129/23.7K · 2026-07 113/14.9K · 2026-08 101/15.3K · 2026-09 106/14.1K ·
2026-10 0 (noindex).
The page halved after the May 2026 core update and held at ~100 clicks/month until the noindex.
**~100 clicks/month is the baseline to protect.**

**12 months before the noindex (2025-09-24 → 2026-09-23), queries with data (467 clicks of ~2,500; the rest are
anonymized long-tail queries):**

| Cluster | Clicks | Impressions |
|---|---|---|
| Brand («3dlook», «3d look», «3dlook yourfit», «3dlook api») | 134 | 5.9K |
| Try-on core («virtual try on clothes», «virtual try-on», «3d try on clothes») | 265 | 74.7K |
| Virtual clothing / fitting room / dressing room | 56 | 20.5K |
| 3D / AR / VR try-on | 78 | 9.6K |
| App questions | 13 | 14.1K |

Last quarter before the noindex (06-24 → 09-23): brand 28 clicks, non-brand 34 clicks.

**Top non-brand queries (12 months):**

| Query | Clicks | Impr. | Avg pos. |
|---|---|---|---|
| virtual try on clothes | 42 | 4,918 | 18.9 |
| virtual try on | 25 | 7,229 | 38.8 |
| 3d try on clothes | 19 | 646 | 15.9 |
| 3d virtual try on | 16 | 834 | 11.6 |
| virtual clothes try on | 14 | 1,508 | 30.5 |
| virtual clothing | 14 | 1,635 | 9.3 |
| 3d virtual try on clothes | 11 | 124 | 4.9 |
| virtual try-on clothes | 10 | 1,138 | 15.8 |
| virtual clothing try on | 8 | 510 | 19.7 |
| virtual try-on | 7 | 4,468 | 22.2 |
| virtual clothing store | 6 | 660 | 13.7 |
| virtual try on apps | 0 | 791 | 6.8 |

**Question-shaped queries where the page already ranked in the top 10.** These are AI-mode and long-tail
queries, and they are the most defensible part of the traffic:

| Query | Impr. | Avg pos. |
|---|---|---|
| best vr platforms for trying on clothes virtually | 235 | 1.8 |
| best virtual fitting platforms for fashion apparel, eyewear, and accessories with high visual quality | 214 | 6.4 |
| which website lets me try on real clothes using my 3d model? | 141 | 5.2 |
| what are the leading virtual try-on solutions for online apparel? | 133 | 5.4 |
| best ar virtual try-on apps for clothes | 123 | 1.0 |
| which retailers provide live video try-ons for clothing? | 119 | 5.5 |
| what options do i have for trying on clothes virtually before making a purchase? | 113 | 9.4 |
| how to tell if clothes will look good in person as online | 112 | 7.1 |
| how to try on clothes virtually | 109 | 3.8 |
| which virtual fitting room software gives the most realistic sizing for jeans? | 107 | 2.3 |
| can you recommend a platform that helps me visualize how clothes will fit me before i buy them? | 102 | 11.2 |

Several of these ask about **fit and sizing**, not only looks: «most realistic sizing», «how clothes will
fit me», «how to tell if clothes will look good». That is the honest bridge to Mobile Tailor.

**Countries (12 months, clicks):** India 142, US 76, UK 51, Pakistan 20, Canada 19, Australia 15.
Desktop 253, mobile 207.

**Ahrefs:** 94 live referring domains (206 all-time), 133 live backlinks. **This is why the URL must stay.**
Ahrefs US keywords on 2026-09-01: «virtual clothing» (100/mo, KD 41, pos 11), «virtual clothing store»
(30, KD 75, pos 9).

**HubSpot (24 months to 2026-09):** 80 contacts had this post as their first page, 68 of them organic, 6 in the
last 12 months, **0 with a deal**. The traffic is mostly consumers and students. The refresh is about keeping
search visibility and link equity working for MT, not about the leads the page produced so far.

## 3. Constraints that protect the traffic (the core of this brief)

1. **Same URL, same slug, no redirect.** The page keeps its 94 referring domains.
2. **The primary intent stays «virtual try-on for clothing».** Keep «Virtual Try-On» in the H1 and title,
   and keep the core phrases where they read naturally: virtual try-on clothes, try on clothes virtually,
   3D virtual try-on, virtual fitting room, virtual try-on app. **Do not turn the article into an MT
   product page.** This is the direct answer to Asel's objection.
3. **Keep H2s mapped to the query clusters** (exact wording is the planner's job):
   what virtual try-on is and how it works (AR overlay, 3D avatar, generative AI); the virtual fitting room
   in store and online; what it does for brands (conversion, returns); brands and retailers using it, updated
   to 2026; how to try on clothes virtually and which apps or tools exist (the question queries above).
4. **The Mobile Tailor bridge, one or two sections plus the CTA, about 20–30% of the text:**
   try-on shows how a garment looks; it does not tell which size or cut fits. Fit comes from body
   measurements. For made-to-measure, custom apparel, formalwear rental and uniforms, the measurement is
   the product. That is where Mobile Tailor sits: 80+ body measurements from two smartphone photos. The live
   section «Replicating real garments in the digital world» already argues that shoppers want fit as well as
   looks. It is the natural place for the bridge.
5. **Honest scope.** 3DLOOK does not sell a try-on visualization product today. Do not say or imply that
   Mobile Tailor renders garments on a person or does virtual try-on. Do not mention YourFit at all (no
   «formerly», no history), and remove every YourFit number. A 3D configurator customer (Tailoor, per
   `use-cases/mt-made-to-measure.md`) shows how measurements feed custom-garment visualization. Whether the
   name can be used publicly follows canon in the pack.
6. **Freshness.** The live text is 2023 with 2017–2024 statistics and Covid framing. Bring it to 2026: generative
   AI try-on is mainstream (Google Shopping try-on; ChatGPT virtual try-on, launched 2026-10-01 per TechCrunch).
   The writer verifies every external figure from a primary source and drops anything it cannot confirm.
   Remove the Body Labs, Zeekit/Memomi and MySizeID examples if they cannot be confirmed as current.
7. **Length.** Keep it close to the live length: 1,900–2,400 words. Cutting it to a short MT note would lose
   the long-tail queries.
8. **Internal links out:** `/mobile-tailor/` (primary CTA), plus 2–3 relevant apparel posts from the pack:
   `body-measurement-app-for-clothing`, `how-to-take-your-body-measurements-at-home`,
   `body-scanning-technology-for-apparel`, `on-demand-clothing-manufacturing`, `ar-clothing-try-on-tools`,
   `virtual-fitting-room-for-ecommerce`. **Cannibalization guardrail:** `virtual-fitting-room-for-ecommerce`
   and `ar-clothing-try-on-tools` cover close topics. This post owns the broad «virtual try-on clothes»
   query and links to them for depth; it does not copy their sections.
9. **CTA:** Mobile Tailor, to `/mobile-tailor/`. The MT page offers a 7-day trial; the «free trial» ban is
   FitXpress-only. Do not promise free API access.

## 4. Section verdicts on the live page

| Live section | Verdict |
|---|---|
| Intro (fashion e-commerce market, 2024 figures, UBS, «store of the future») | Rewrite. Fresh 2026 figures or none. Shorter. |
| AR market $198bn by 2025 (Statista 2017 forecast), Snapchat × Farfetch | Remove the stale forecast. Keep a short «how AR try-on works». |
| 3D virtual fitting technology: unlocking the virtual fitting room | Keep the topic, rewrite. Magic mirrors in stores are fine as one paragraph. |
| What does «try on clothes virtually» entail for customers? | Keep. It maps to «how to try on clothes virtually». Add the three approaches: 2D overlay, 3D avatar, generative AI. |
| Improving the e-commerce experience (Body Labs, YourFit ×2, 48% returns, Request a Demo) | Remove YourFit and its numbers. Keep the online-try-on point. |
| Benefits: conversions (Shopify 65%), personalization (Deloitte 20%), returns ($800m, Barclaycard 19%, TA3 Swim 47%), safe fitting (Covid), relationships (Byondxr 70%) | Keep the structure. Re-verify or drop each figure. Remove TA3 Swim (a YourFit case) and the Covid section. The returns point leads into the bridge: fit-related returns need measurements, not only visuals. |
| Leading brands (Gucci, Kohl's, Walmart/Zeekit/Memomi, Nike, Temperley/MySizeID, Farfetch) | Keep as the «who uses it» section, updated to 2026 and verified. |
| Replicating real garments: digital twins of garment and body; YourFit ×3, API integration, voice-guided scan | Turn into the MT bridge (§3.4). No YourFit. |
| AR as an e-commerce conversion hack; YourFit +31% / +16% / +23%; «71% of consumers» | Remove YourFit numbers. Fold into the conclusion. |
| Byline «Luke Christou» (2023 guest author) | Open item for Vadim/Asel: keep the byline or move it to the default author, Assel Sekerova. |

## 5. Risks and expectations

- **Some traffic will be lost** (Vadim accepts this). The brand sitelink clicks (~28 per quarter before the
  noindex) will mostly go to other 3DLOOK pages, which is fine. The aim is to recover most of the
  non-brand ~70 clicks/month over 4–8 weeks after re-indexing. This is not guaranteed: the page lost half its
  traffic in the May core update, and the intent shift adds risk.
- **Sitelink risk (Asel's question):** after the rewrite the page may come back as a brand sitelink. Without
  YourFit, and with an MT bridge, that is acceptable. Check the «3dlook» SERP 2–3 weeks after re-indexing.

## 6. Republish steps (for Asel, after the final pack)

1. Replace the body at the same URL, set the new title and meta, update the modified date.
2. Yoast → Advanced → «Allow search engines to show this Post in search results?» → Yes. Purge the cache.
3. Check: `index, follow` in the source, and the URL is back in `post-sitemap.xml`.
4. GSC → URL Inspection → Test live URL → Request indexing.
5. Restore 2–3 internal links from apparel posts with try-on anchors (removed on 09-24).
