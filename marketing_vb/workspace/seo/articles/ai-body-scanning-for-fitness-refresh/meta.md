---
meta_title: "AI Body Scanning for Fitness: Where a Phone Scan Fits"
meta_description: "Explore how AI body scanning fits fitness apps, from member onboarding and progress tracking to coach reviews, SDK integration, and pilot testing."
url_slug: ai-body-scanning-for-fitness
category: Fitness and Connected Health
---

## Judgment checklist

- [x] intro_hook: opens on a concrete scene (first check-in, weight chart flat, waist and hip may have moved, nothing in the app shows it), then names the product decision in the third paragraph.
- [x] cta_type: two CTAs under the 2026-11-23 rule: early CTA block right after the short answer (landing, 15.8% of the body, MOFU soft/evaluation) and the closing CTA in Next steps (landing plus `#form` demo); the S6 "mobile alternative to a gym body scanner" link (68.9%) is a contextual internal link, not a CTA.
- [x] landing_link: down link is `/fitxpress/for-connected-and-digital-fitness/` ("Link now" for Hub 1 Fitness in landing-map.md), map anchor "body scanning for fitness apps" in the short answer at 13.2% of the body, repeated by the early CTA at 15.8%; demo CTA goes to `{landing}#form` (live anchor; the map implies `#demo`, re-check at publish, see Open items).
- [x] anchors_sources: anchors are descriptive and sit inside sentences; external sources are Adjust, JMIR and ACSM via Newswise, no competitor blogs (Adjust is a vendor blog, see Open items).
- [x] cannibalization: the page owns the member-journey and cohort-test question; the landing, `ai-in-fitness-industry`, `body-scanning-technology-for-weight-loss`, `ai-body-scanners-vs-dexa-scans` and the accuracy framework are linked for depth, not copied; the S6 section no longer carries the product pitch, and no title, H1 or meta title uses the landing keyword.
- [x] distinct_intent: one intent, the commercial case for adding a phone body scan to a fitness app (MOFU); the landing keeps the product pitch and the pilot steps.
- [x] vertical_boundary: fitness only; "FitXpress is not a medical device" is stated in the scope note, no diagnosis or health-risk framing, no clients or competitors named, hardware described as a separate category.
- [x] terminology_actors: the product team, member, coach and app are named by role; "customer" appears only inside verbatim compliance context, "platform" is the app's own product, 3DLOOK and FitXpress are named where they act.

## Meta variants

### Title
1. AI Body Scanning for Fitness: Where a Phone Scan Fits (53 chars)  [chosen]
2. AI Body Scanning for Fitness: Member Journey | 3DLOOK (53 chars)  [brand-suffix variant, no landing keyword]

Rejected (decision D2): the reviewer's "AI Body Scanning for Fitness Apps | 3DLOOK". It contains "body scanning for fitness apps", the landing's primary keyword, and landing-map.md rule 3 forbids that keyword in the article's title, H1 and meta title (same cannibalization the review itself flags). Chosen H1: "AI Body Scanning for Fitness: Where a Phone Scan Fits in the Member Journey".

### Description
1. Explore how AI body scanning fits fitness apps, from member onboarding and progress tracking to coach reviews, SDK integration, and pilot testing. (146 chars)  [chosen, verbatim from decision D3 / reviewer]

## Open items

Answers to the reviewer (Review 1):

1. C1, peer review sentence. "3DLOOK's accuracy claims have not been peer-reviewed or externally validated through a third-party clinical study." is canon verbatim (accuracy-formulations.md section 1.9) and is unchanged. If newer validation documentation exists, the canon changes first (Vadim), then the article.
2. D2, meta title. The reviewer's "AI Body Scanning for Fitness Apps | 3DLOOK" is rejected: it contains the landing's primary keyword (landing-map rule 3). Kept "AI Body Scanning for Fitness: Where a Phone Scan Fits". If a brand suffix is wanted: "AI Body Scanning for Fitness: Member Journey | 3DLOOK" (53 chars).
3. B2, timing. The article keeps the canon line "under 45 seconds from the photos to structured results". The landing hero says "under 45 seconds after capture"; same meaning, nothing to change in the article. Optional for the landing owner: align the hero to the canon wording.
4. Early CTA. The web team may render "Explore FitXpress for fitness apps" (own line after the short answer) as a button. The markdown is a plain link to the landing.

Decisions and checks (plain English, for a colleague to act on):

5. Byline. The live page is signed Dana Vioreanu (2024). The refresh names Assel Sekerova. Her call before publish.
6. Adjust source. The retention figures (24% on day 1, 7% on day 30) come from a blog on adjust.com. Our terminology rules say to avoid vendor blogs. Adjust is not a competitor, the figures are its own benchmark data, and the fitness landing uses the same source. Confirm, or swap for a neutral source with the same figures.
7. ACSM link. It points to the ACSM release on Newswise. If https://www.acsm.org/2027-fitness-trends/ loads at publish (it returned 403 from the server), swap the link. The text does not change.
8. Demo anchor. The Hub 1 row in landing-map.md says "Demo button now: same page", which by rule 4 implies `#demo`. The live landing anchor is `#form` and Next steps uses it. Re-check `#form` at publish; the map owner may state `#form` in the row.
9. Repeat across a frozen section: resolved in the QC fix pass of 2026-11-23 (QC 18/20, coordinator override of section E). The S3 closing sentence "The product team also decides what members and coaches see." is cut. The Coach review lead "Before planning the next training block," is cut too, so the A3 example alone carries the next-block point. The A3 example is unchanged and verbatim. Nothing to do.
10. Section lengths. S4 is 224 words with the H2, against about 200 targeted. The next cut, if wanted, is "Early in a program, weight can change slowly while body measurements shift." S6 is 225 words with headings after QC fix 1 ("…train away from the club, at home or between visits."), against A2's 180-220. Accepted as the coordinator's wording.

Republish steps for the web side (the URL and slug do not change):
11. Replace the body at the same URL, https://3dlook.ai/content-hub/ai-body-scanning-for-fitness/. Keep "Published: June 12, 2024" and set "Updated" to the republish date.
12. In Yoast, set the SEO title and meta description to the chosen variants above, and update the OG and Twitter title and description to match.
13. New og:image (current one is 2024/04/fitness-tracking-with-ai-powered-body-scanning.jpg, which matches the old title). Use the cover concept below.
14. Set the author (see item 5).
15. Add the FAQPage JSON-LD below in a Custom HTML block (not a Yoast FAQ block). Do not expect FAQ rich results: Google stopped them for most sites in May 2026. The live page has no FAQPage schema today.
16. Purge the cache, view the page source to check the title, description and schema, then use Request indexing in Google Search Console.
17. Illustrations for Kristina: cover and Image 1 below (concepts unchanged; none refers to the hardware section).

Inbound links on other pages (refresh-gap-analysis.md section 6), three edits:
18. Hub `ai-in-fitness-industry`: it links here from a sentence that no longer fits: "For how the capture and measurement pipeline works end-to-end, see [AI-powered body scanning for fitness](.../ai-body-scanning-for-fitness/)." Replace that sentence with: "For where a scan can sit in a fitness app's member journey, see [AI body scanning for fitness](https://3dlook.ai/content-hub/ai-body-scanning-for-fitness/)." Also compare the hub's "seven in ten users... stop using a fitness app" framing with this page's Kidman wording.
19. `glp-1-muscle-loss-fitness-apps`, section "How to run comparable body scan check-ins", paragraph "**Baseline.** The first scan occurs during onboarding or at the start of a strength program, ...": link "during onboarding or at the start of a strength program" to https://3dlook.ai/content-hub/ai-body-scanning-for-fitness/.
20. `remote-body-measurement-online-fitness-coaching`: change the anchor "Revolutionizing Fitness Tracking with AI-powered Body Scanning" (the old title) to the new H1 or a short form.

Minor, from the editor: two accuracy-framework links in S5 sit in adjacent paragraphs on purpose (drop one if it reads as repetitive); DXA is first spelled out in S7; the pilot wording (one baseline placement, now with secondary metrics) is compatible with the landing's pilot step 2 but can read as different advice.

Follow-up:
21. Check AEO prompts 565780358696 and 565540613659 in the HubSpot AEO pull about 8 weeks after re-indexing (no baseline on 2026-11-18). The page may lose the little consumer traffic it gets for `ai body scanner` (about 170 impressions a month at position ~36); the goal is landing clicks, HubSpot contacts and AEO visibility.

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
