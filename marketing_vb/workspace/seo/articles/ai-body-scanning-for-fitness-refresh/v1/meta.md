---
meta_title: "AI Body Scanning for Fitness: Where a Phone Scan Fits"
meta_description: "AI body scanning for fitness: where a phone scan fits a fitness app, what it returns, how it compares with gym scanners, and how to test it with members."
url_slug: ai-body-scanning-for-fitness
category: Fitness and Connected Health
---

## Judgment checklist

- [x] intro_hook: opens on a concrete scene (first check-in, weight chart flat, waist and hip may have moved, nothing in the app shows it), then names the product decision in the third paragraph.
- [x] cta_type: soft-to-evaluation CTA for MOFU intent: landing link in the short answer (15.4% of the prose), the "mobile alternative" link in the hardware-alternative section (60.0%), and a closing link plus "book a demo" to the landing #form (end).
- [x] landing_link: down link is `/fitxpress/for-connected-and-digital-fitness/` ("Link now" for Hub 1 Fitness in landing-map.md), anchor "body scanning for fitness apps" (a map anchor) in the short answer, at 15.4% of the prose; demo CTA goes to `{landing}#form`, which was live on 2026-11-18 (the landing's demo anchor is `#form`; re-check at publish).
- [x] anchors_sources: anchors are descriptive and sit inside sentences; external sources are Adjust, JMIR and ACSM via Newswise, with no competitor blogs (Adjust is a vendor blog, see Open items).
- [x] cannibalization: the page owns the member-journey and cohort-test question; the landing, `ai-in-fitness-industry`, `body-scanning-technology-for-weight-loss`, `ai-body-scanners-vs-dexa-scans` and the accuracy framework are linked for depth, not copied.
- [x] distinct_intent: one intent, the commercial case for adding a phone body scan to a fitness app (MOFU); the landing keeps the product pitch and the pilot steps.
- [x] vertical_boundary: fitness only; "FitXpress is not a medical device" is stated, no diagnosis or health-risk framing, no clients or competitors named, hardware described as a separate category.
- [x] terminology_actors: the product team, member, coach and app are named by role; "customer" appears only inside the verbatim compliance sentence context, "platform" is the app's own product, 3DLOOK and FitXpress are named where they act.

## Meta variants

### Title
1. AI Body Scanning for Fitness: Where a Phone Scan Fits (53 chars)  [chosen]
2. AI Body Scanning for Fitness: Phone Scans and Check-Ins (56 chars)

Live title today: "Fitness Tracking with AI-Powered Body Scanning - 3DLOOK". The new one puts the primary keyword first. Chosen H1: "AI Body Scanning for Fitness: Where a Phone Scan Fits in the Member Journey".

### Description
1. AI body scanning for fitness: where a phone scan fits a fitness app, what it returns, how it compares with gym scanners, and how to test it with members. (153 chars)  [chosen; replaces the 2026-11-18 publisher draft, which carried the landing's primary keyword string]

## Open items

Decisions and checks (plain English, for a colleague to act on):

1. Byline. The live page is signed Dana Vioreanu (2024). The refresh names Assel Sekerova, who asked for it and is the default author. Her call before publish.
2. Adjust source. The retention figures (24% on day 1, 7% on day 30) come from a blog on adjust.com. Our terminology rules say to avoid vendor blogs. Adjust is not a competitor and the figures are its own benchmark data, and the fitness landing uses the same source, so it stays. Confirm, or swap for a neutral source with the same figures.
3. ACSM link. It points to the ACSM release on Newswise. If https://www.acsm.org/2027-fitness-trends/ loads at publish (it returned 403 from the server), swap the link to it. The text does not change.
4. Two accuracy-framework links sit in adjacent paragraphs of the section "What a phone body scan produces" (one after the repeatability figure, one after the accuracy figure). This is deliberate. If it reads as repetitive, drop the link from the accuracy paragraph.
5. DXA expansion. DXA is first spelled out in the "Evidence with its reference" bullet as an example reference method, so the first FAQ heading can stay short ("Is a phone body scan the same as a DXA scan?"). Confirm the example reads right.
6. Length of the member-cohort test section. It is shorter than the 210 words planned, in prose without bold labels, and no longer restates the landing's pilot steps. Total article length (2,068 prose words after the QC fix pass) is inside the target band (1,657-2,242).
7. Pilot wording vs the landing. The article says each test fixes one baseline placement (onboarding or first check-in). The landing's pilot step 2 scans "at onboarding and the first check-in". They are compatible but can read as different advice. Align one of them if you see a conflict.
8. At publish, re-check that https://3dlook.ai/content-hub/ai-body-scanning-for-fitness/ links to /fitxpress/for-connected-and-digital-fitness/ return 200 and that `#form` exists on the landing (both verified on 2026-11-18).
9. Section heading "How visible progress may affect fitness app retention" differs from the plan. It is hedged on purpose, because no source tested body scans. It does not affect the meta.

9a. Traffic expectation. The refresh does not target `ai body scanner` (owned by the homepage and the planned /fitxpress/ page), so the page may lose the little consumer traffic it still gets for that family (Aug–Nov 2026: about 170 impressions a month at position ~36). The goal is clicks to the fitness landing, HubSpot contacts whose first page is this URL, and visibility on the two AEO prompts.

Republish steps for the web side (the URL and slug do not change):
10. Replace the body at the same URL, https://3dlook.ai/content-hub/ai-body-scanning-for-fitness/. Keep "Published: June 12, 2024" and set "Updated" to the republish date.
11. In Yoast, set the SEO title and meta description to the chosen variants above, and update the OG and Twitter title and description to match.
12. New og:image (current one is 2024/04/fitness-tracking-with-ai-powered-body-scanning.jpg, which matches the old title). Use the cover concept below.
13. Set the author (see item 1).
14. Add the FAQPage JSON-LD below in a Custom HTML block (not a Yoast FAQ block). Do not expect FAQ rich results: Google stopped them for most sites in May 2026. The live page has no FAQPage schema today.
15. Purge the cache, view the page source to check the title, description and schema, then use Request indexing in Google Search Console.

Inbound links on other pages (refresh-gap-analysis.md §6; nine pages link here today):
16. Hub `ai-in-fitness-industry`: it already links here, but from a sentence that no longer fits: "For how the capture and measurement pipeline works end-to-end, see [AI-powered body scanning for fitness](…/ai-body-scanning-for-fitness/)." Replace that sentence with: "For where a scan can sit in a fitness app's member journey, see [AI body scanning for fitness](https://3dlook.ai/content-hub/ai-body-scanning-for-fitness/)."
17. `glp-1-muscle-loss-fitness-apps`, section "How to run comparable body scan check-ins", paragraph "**Baseline.** The first scan occurs during onboarding or at the start of a strength program, …": link the words "during onboarding or at the start of a strength program" to https://3dlook.ai/content-hub/ai-body-scanning-for-fitness/. The page does not link here today.
18. `remote-body-measurement-online-fitness-coaching`: change the anchor "Revolutionizing Fitness Tracking with AI-powered Body Scanning" (the old title) to the new H1 or a short form of it.
19. Optional: five more pages link here with generic anchors and can stay as they are: `connected-fitness-industry`, `top-fitness-tech-companies`, `top-fitness-industry-trends`, `top-health-tech-companies`, `weight-loss-industry-overview`. `body-scanning-technology-for-weight-loss` links here from the mismatched anchor "adjust fitness routines"; fix it during that article's own refresh (row 1.x2). Full list in refresh-gap-analysis.md §6.

Follow-up:
20. Check AEO prompts 565780358696 and 565540613659 in the HubSpot AEO pull about 8 weeks after re-indexing. There was no baseline of our citations on 2026-11-18.

## FAQPage JSON-LD (3 questions, for the Custom HTML block)

Question and answer text is exactly as worded in final.md (links and claim comments removed).

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is a phone body scan the same as a DXA scan?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "They are different methods. FitXpress is not equivalent to DXA, BIA, or a calibrated scale when the workflow, protocol, or regulatory standard requires those methods. For progress tracking, the comparison that matters is between scans taken with the same method. AI body scanners and DXA (also written DEXA) compares the two in detail."
      }
    },
    {
      "@type": "Question",
      "name": "Can members with a physical disability use the scan?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "FitXpress was not specifically trained on data representing people with physical disabilities, and its measurement performance has not been established for this population. This matters when a disability affects the standard standing pose or capture sequence. In those cases, the app needs a documented alternative measurement path."
      }
    },
    {
      "@type": "Question",
      "name": "Does 3DLOOK know which member a scan belongs to?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Scan records are associated with anonymized, randomly generated IDs; 3DLOOK cannot identify a specific individual from stored scan records. The platform connects each scan ID to its own member profile and chooses which scans to compare. The FitXpress data, privacy, and security answers cover retention, hosting, and regulatory questions."
      }
    }
  ]
}
</script>
```

## Image and alt-text suggestions

1. Cover, below the H1 and the new og:image. Concept: a phone showing a fitness app's own progress screen, with two flat body silhouettes side by side (baseline and check-in) and a waist callout. No numbers, no 3DLOOK interface, no device-maker hardware. Alt: "Phone screen with two body outlines side by side and a marker at the waist" (75 chars)
2. S3, member journey. Concept: a line of four steps: onboarding with a baseline scan, a scheduled check-in with a second scan, coach review, and a premium-tier 3D progress view labeled as a FitXpress Pro plan feature. Markers show where each scan record is created. No figures. Alt: "Four-step timeline from first scan to check-in, coach review and a premium progress view" (88 chars)
