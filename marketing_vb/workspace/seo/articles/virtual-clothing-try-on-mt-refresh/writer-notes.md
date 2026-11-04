---
slug: virtual-clothing-try-on
workspace: virtual-clothing-try-on-mt-refresh
product: mobile_tailor
stage: draft-v1
draft: draft-v1-writer.md
author: Assel Sekerova
created: 2026-11-04
---

# Writer notes, draft v1

Lint: `python3 scripts/article_lint.py workspace/seo/articles/virtual-clothing-try-on-mt-refresh/draft-v1-writer.md --pack workspace/seo/_context-packs/virtual-clothing-try-on-mt-refresh.yaml`
returned VERDICT PASS on run 1, and again on run 2 after the judgment edits listed below. Run 2 numbers:

- Prose words: 2,274 against a target of 2,250 (allowed band 1,912-2,587).
- Sentences: 147, mean 13.5 words, p90 20. One sentence runs over 25 words, and it is also the only one over 35: the verbatim `accuracy-formulations.md` §1.1 sentence (42 words), which the plan allows.
- Detector: CLEAN, density 0.0. No near-duplicate pairs.
- Links in all three required directions: up 1, sideways 6, trust 1. Down is optional and not used.

Run 1 also passed. Run 2 fixed things the gates do not check:

- In the S5 lead paragraph, an ext-claim marker sat on a sentence the source does not support. I removed "in 2026" and the marker.
- S1's Google sentence now uses different wording from the S5 Google entry.
- "on the Zara.com website" became "on Zara.com", which is Inditex's own wording.
- The Tesco sentence in S7 is reworded to match what Tesco actually said.
- The reframe sentence now uses canon wording ("performance").
- Source markers added to S6 list items 1, 2, and 4.

## Sources used (each fetched and read on 2026-11-04)

| Marker | What the draft uses | Source | Notes |
|---|---|---|---|
| GOOG-TRYON-US-2025 | Try-on launched for US shoppers in July 2025, across Search, Google Shopping, and product results in Google Images (S1, S5) | https://blog.google/products-and-platforms/products/shopping/back-to-school-ai-updates-try-on-price-alerts/ (Google, Jul 24, 2025) | Says verbatim: "Today, try on is launching in the U.S. … across Search, Google Shopping and even product results on Google Images." |
| GOOG-UK-IN-2025 | Apparel try-on reached the UK and India in December 2025 (S5) | https://blog.google/products-and-platforms/products/shopping/virtual-apparel-try-on-uk-india/ (Google, Dec 3, 2025) | Google's own post, which replaces the plan's FashionUnited link as the plan preferred |
| GOOG-SELFIE-2025 | Selfie option in the US; "select their usual clothing size" (S5, S6, S8) | https://blog.google/products/shopping/studio-quality-digital-try-on/ (Google, Dec 11, 2025, Lilian Rincon) | Says verbatim: "select your usual clothing size". US only |
| GOOG-DOPPL-2025 | Doppl, an experimental Google Labs app on iOS and Android in the US, launched June 2025. Animated digital version of the shopper, built from photos or screenshots. Save and share. The fit caveat is quoted verbatim (S5, S7, S8) | https://blog.google/technology/google-labs/doppl/ (Google, Jun 26, 2025) | Quote checked character for character: "Fit, appearance and clothing details may not always be accurate." |
| GOOG-HOWTO | The "try it on" icon and a full-length photo. Google recommends "a full-body shot, good lighting, and fitted clothing". Save or share the look (S6, S7) | https://blog.google/products/shopping/how-to-use-google-shopping-try-it-on (Google, May 20, 2025, updated Nov 20, 2025) | The plan said "verify the URL". It resolves with no trailing slash, so the draft uses it that way |
| TC-CHATGPT-2026 | Try On button in ChatGPT shopping results, global launch on October 1, 2026, with Favorites/Library. Works from a selfie or a full-body photo, or from an uploaded screenshot of an item. Runs on the ChatGPT Images 2.5 model "according to OpenAI". Saved items are kept alongside try-on images (S1, S3, S5, S6, S7) | https://techcrunch.com/2026/10/01/chatgpt-can-now-virtually-try-on-clothes-for-you/ (Sarah Perez, Oct 1, 2026) | **This rests on TechCrunch, not an OpenAI page.** The plan names TechCrunch as the source. OpenAI's help center and release notes (help.openai.com/en/articles/11128490 and /6825453) returned HTTP 403 to WebFetch. Other coverage (emarketer, TechRepublic, mixed-news.com) gives the same date and features. The draft attributes the fact to TechCrunch in the text |
| INDITEX-FY2025 | Zara Try-On has run on Zara.com since mid-December 2025. Shoppers create a synthetic avatar from their own photos. Live in 43 markets with more than 7 million sessions, as reported in March 2026 (S5, FAQ 1) | https://www.inditex.com/itxcomweb/es/en/press/news-detail/b870d5ec-6b7e-491d-b38e-340cd69036df/fy2025-results (Inditex FY2025 results, Mar 11, 2026) | Primary source, as the plan required. It says "Since mid-December" with no year; 2025 follows from the FY2025 period (Feb 2025 to Jan 2026). It also says the tool "operates exclusively on Zara.com". Some secondary sources call it app-only, so the draft uses Inditex's wording and does not say "in-app" |
| RG-TESCO-2026 | Tesco F&F trial at Sandhurst Extra, September 2026. About 1,500 menswear and womenswear items. Shoppers take a photo on the spot or upload one. Tesco's quoted aim (S4, S6, S7) | https://retailgazette.co.uk/blog/2026/09/tesco-trials-virtual-try-on (Retail Gazette, Sep 24, 2026). Matches https://retailtimes.co.uk/tesco-trials-virtual-try-on-technology-as-part-of-new-ff-in-store-shopping-experience/ (Retail Times, Sep 25, 2026) | **This is trade press. No Tesco plc release was found:** tescoplc.com/news returned HTTP 500, and a search restricted to Tesco domains found nothing. Two outlets agree on the store, the date, the item count, and the photo flow. The editor can drop the Tesco paragraph if trade press does not count as primary; S4 still works if it answers by category only |
| NRF-RETURNS-2025 | Retailers estimated that 15.8% of annual sales and 19.3% of online sales would be returned in 2025 (S7) | https://nrf.com/media-center/press-releases/consumers-expected-to-return-nearly-850-billion-in-merchandise-in-2025 (NRF with Happy Returns, Oct 15, 2025) | Primary. Covers all retail; there is no apparel or fit-specific figure on the page. The draft says it covers every category |

Every line that states an external fact carries `<!-- ext-claim: ID -->`, the format the `accuracy-roi-telehealth-refresh` precedent used. Product facts carry `<!-- claim: ID -->`.

## Dropped (could not verify, or off-plan)

| Item | Why |
|---|---|
| Walmart "Be Your Own Model" | All coverage found dates from the September 2022 launch, with nothing on its 2025 or 2026 status. Cut, as the plan's default requires. Zeekit and Memomi are cut as well |
| Walmart eyewear try-on (PYMNTS 2024) | Not confirmed as current. The eyewear point stays only as an unbranded category sentence in the S5 lead |
| ChatGPT reference-photo handling (saved for later try-ons; change or delete under Settings, Personalization, Reference photos) | OpenAI's help center and release notes returned HTTP 403. The only confirmation is secondary: mixed-news.com quotes the release note, and search snippets show it. FAQ 3 now gives tool-neutral guidance instead. **If the editor can open help.openai.com in a browser, this is a one-sentence add-back to FAQ 3** |
| OpenAI's fit caveat ("may not represent the product or your appearance exactly and do not guarantee fit or size") | Seen only in search snippets of the 403 help page. It would strengthen S8 next to the Doppl quote if someone can verify it |
| ChatGPT Try On plan availability (Free, Plus, Pro) | TechCrunch does not say which plans include it, and OpenAI's pages were unreachable. FAQ 2 says "Availability varies by country, product, and service" and makes no claim about plans |
| Tesco aim "more confidence when choosing" (plan paraphrase) | The quote Retail Gazette attributes to Tesco is about helping shoppers "discover new styles". Retail Times paraphrases it as feeling "more confident". The draft uses the verbatim quote |
| Tesco's technology vendor | Named in the trade press. Left unnamed, as the plan requires |
| Zara US launch in early 2026; Google expansion to Australia, Canada, and Japan in October 2025 | Each has only a single secondary source. Not used |
| VR headset clothing try-on | No current example confirmed. The draft uses the plan's fallback sentence: the tools run on phones, laptops, and in-store screens, and none needs a virtual reality (VR) headset |
| Shopify 65%, Barclaycard, Deloitte, Forbes, Byondxr, Metropol, "71%", Statista, UBS, First Insight | The plan's default is to cut them, so they were not searched. None appears in the draft |
| MT-RETENTION, MT-CLIENTS, MT-IEEE | Optional. I left out MT-RETENTION because "5+ years" next to the rental company's "nearly 5 years" would look inconsistent. The other two are not needed for the argument |

## Deviations from the plan

1. **S5 has four entries:** Google, Doppl (Google Labs) as its own entry, ChatGPT, and Zara. Walmart and the eyewear entry were dropped (see above). The plan-audit fallback was three entries, so this is still within budget.
2. **S1 "what the page covers"** is written about the subject ("The three approaches differ in how they work, where shoppers find them, and what they do for brands. They also differ in how much they reveal about fit."). It does not describe the page, per `editorial-rewrites.md` §3.
3. **S6 tips are one short paragraph**, not a list. The photo tip is attributed to Google's how-to page. The AR-apps query is answered by category, without the word "best", so there is no implied ranking.
4. **FAQ questions are reworded.** FAQ 1 reads "Which website can I use to try on clothes with my own 3D model?" because the plan's "lets me" uses `let`, which is a hard ban. FAQ 2 reads "Can I try on clothes online for free?" to carry the `virtual try on clothes online free` query.
5. **S9 reframe sentence.** I added "What counts as adequate performance depends on how the measurements will be used." between the verbatim §1.1 + §1.8 sentences and the trust-link sentence. It is verbatim from `accuracy-formulations.md` §5 ("The reframe, as a statement"). The coordinator said `about-me.md` does not apply here, but this sentence is accuracy canon, not health voice. The editor can cut it if it reads as health-article voice.
6. **NDA is not expanded.** The §1.8 sentence is pasted verbatim, as the plan instructs. M1 is not gated for NDA. Expanding it would break the verbatim wording, so I left it for the editor.
7. **Section lengths differ from budget; the total does not.**

   | Section | Draft | Budget | Why |
   |---|---|---|---|
   | S9 | ~370 | 320 | The verbatim accuracy paragraph and the three-example list |
   | S3 | ~360 | 310 | Includes the Image 1 concept line |
   | S7 | ~170 | 220 | |
   | S11 | ~50 | 70 | |

   Total is 2,274 against 2,250.
8. **MT-OUTPUTS marker** sits next to MT-HERO, because the hero sentence contains "80+ body measurements".
9. **The S9 H2 gains the serial comma:** "made-to-measure, rental, and uniform orders".
10. **External sources are linked inline:** blog.google, TechCrunch, Retail Gazette, Inditex, and NRF. `blog-style-guide.md` §4 says "no external hyperlinks". The plan asks for the Doppl quote "with the link", and the precedent refresh linked CDC inline. I flag the conflict and leave the call to the editor.
11. **Dates are in US format** ("October 1, 2026"), and spelling is American ("color", "behavior").

## Live defects checklist

Every row of the plan's checklist is gone from the draft. I checked by grep:

- Zero hits for YourFit, `/contact-us/`, "Request a Demo", 48%, TA3, 31/16/23%, and "store of the future".
- Zero hits for "Future of Fashion", "conversion hack", empower, seamless, "not only", and em or en dashes.
- Zero hits for Body Labs, Zeekit, Memomi, Gucci, Kohl's, Nike, Temperley, MySizeID, Farfetch, Louis Vuitton, Statista, UBS, Forbes, Deloitte, Barclaycard, Byondxr, Metropol, 71%, 65%, Covid, and First Insight.
- Zero hits for "Source:" captions, "free trial", Luke Christou, "under 60 seconds", "85 measurements", "replace", "most accurate", Walmart, and Shopify.
- No client names in visible text: Safariland, Jim's, Tailoor, and AIUTA appear nowhere. The only match is the claim-marker ID inside an HTML comment.

Other checks:

- The byline is Assel Sekerova.
- All H2s and H3s are in sentence case.
- `you` appears only in S6 and the FAQ.
- Mobile Tailor is named only in S9 and the S11 CTA.
- There is one CTA, in S11, to https://3dlook.ai/mobile-tailor/, worded "see how Mobile Tailor works".

The eBook CTA and author bio were dropped by the capture, so they stay the publisher's item.

## For the editor

- **Unsourced category statements carried from the plan.** None of them contains a figure, date, or brand, but check them for tone:
  - S3: "AR works best for shoes, eyewear, accessories, and tops".
  - S4: "Live video try-on … runs mainly on AR".
  - S5: "Eyewear and accessory try-on has run on live AR for longer".
  - FAQ 1: "3D avatar try-on appears on individual brand sites".
- **FAQ 2:** "Google's try-on sits on apparel listings in Search and Shopping, which are free to use." Google's posts state no price. The sentence rests on Search and Shopping being free services.
- **The product boundary is the article's one licensed corrective:** "Mobile Tailor does not render garments on a person or offer virtual try-on." It is written as a single negation, per M2. The 3D configurator example (MT-CFG) says only that it takes Mobile Tailor measurements as input. It says nothing about rendering.
- **Both required sideways siblings still promote YourFit** (plan-audit open item 4): `ar-clothing-try-on-tools` and `virtual-fitting-room-for-ecommerce`. The draft links them, as the guardrail requires.
- **Repeated phrases** reported by the gate are topic phrases, not refrains: "full length photo" ×4, "a live camera" ×4, "Zara Try-On" ×3, and "virtual fitting room" ×3.
- `plan-audit.md` was read, because the coordinator's brief listed it. The writer agent definition excludes it.
