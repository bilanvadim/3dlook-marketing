# QC Report — FitXpress User Experience and Capture Quality FAQ (Review Round 1)

slug: `2026-09-22-fitxpress-capture-quality-user-experience-faq`
Round: R1 (post-Review 1 edit)
Reviewer: seo-qc (sonnet)

## Scores

| Category | Score | Max |
|---|---|---|
| A — Adherence to plan & Review 1 decisions | 4 | 5 |
| B — Factual (accepted from code) | 5 | 5 |
| C — Brand & tone | 3 | 3 |
| D — Format (accepted from code) | 3 | 3 |
| E — Output quality | 4 | 4 |
| **Total** | **19** | **20** |

**Verdict: ship**

## A — Adherence to plan & Review 1 (4/5)

R1 had ~19 discrete asks (5 personal-feedback items + 14 ChatGPT corrections) plus a "must remain unchanged" list. Compliance is near-total, checked item by item:

- A1 (fix presentation-speech prose) — fixed. E.g. "Because every scan in that flow follows the same instructions and checks, repeated scans of the same person start from comparable conditions. That comparability supports consistency between a baseline scan and the scans that follow it." — causal connective tissue, not a fact-list. Sentence mean moved 12.2→14.3, matching the fix.
- A2–A4 ("still"/"so"/"see" guardrails) — 0 occurrences per code facts, confirmed by spot read.
- A5 (illustration formatting) — both illustrations use a distinct blockquote pattern (`> **[Illustration N: ...]**` + "Designer brief: ..."), clearly separated from body prose.
- C4 — "The organization controls and brands the surrounding experience, including onboarding, user instructions, and the results display. The core capture flow where RTPV runs is standardized, a design decision intended to protect measurement accuracy." — exact match to the requested reframing away from "not customizable."
- C7 — "No single public percentage or ranking describes the effect of individual capture conditions." — replaces the "single biggest factor" claim precisely as instructed.
- C13 — "under 45 seconds" used consistently in the Quick-answers table, Illustration 1 brief, and the Timing section (three separate mentions, one definition) — correctly follows the coordinator's canon decision over the reviewer's unsupported "under a minute."
- C14 — "Users cannot upload existing photos in the standard guided FitXpress capture flow." — verbatim as specified.
- Structural anchors (H1, 11 H3 strings in original order, Quick-answers table, RTPV-not-clinical-posture line, exception-handling answer, "FitXpress is not a medical device.", lean mass, Body Progress by scan ID, two visuals, pilot next step, CTA) — all present and untouched.

One partial miss: **C6** asked for "broader Clothing Detector wording, no sport/regular/oversized." The article dropped "sport" but still leans on the flagged category words: *"Form-fitting or regular-fit clothing keeps that outline visible, while oversized, loose, layered, or body-obscuring garments can hide parts of it."* It's broadened (added "loose," "layered," "body-obscuring"), but "regular-fit" and "oversized" survive verbatim, which is likely to draw the same flag again in a round-2 pass if a reviewer greps literally for those words.

## B — Factual (5/5, accepted from code)

Lint PASS, all claim markers trace to the pack including the FX-R1-* claims legalized from this review round. No override.

## C — Brand & tone (3/3)

- No banned words found (leverage/utilize/harness/robust/seamless/comprehensive/delve/navigate/tapestry/realm/unlock/unleash/game-changing/cutting-edge) — clean.
- Guardrail-word count (still/so/see) = 0, detector 0.43/1000 clean, rhythm 0.37 — consistent with a genuine voice fix rather than a superficial find-replace.
- Confident, non-hedgy expert register: *"Pose validation is designed to reduce retakes. Some users need more than one attempt, and the program's support plan should allow for that."* — states a design intent and a practical consequence without padding or AI-typical throat-clearing ("it's worth noting," "in today's landscape," etc. — none found).
- Lists are used only where list format is the right editorial choice (progress outputs, six-step integration sequence, exception-route options) while explanatory sections stay in connected prose — this is exactly the discipline Review 1's A1 complaint was asking for.

## D — Format (3/3, accepted from code)

Checklist 16/17; the one fail (`faq_present`) is the known false positive for an all-FAQ page without a literal "## FAQ" heading — not penalized per instructions. Word count 2,135 vs target 2,100 (within tolerance), no sentences >25 words, p90 22.

## E — Output quality (4/4)

Reads as ready to publish, not a shell needing another pass:

- *"In 3DLOOK's internal repeatability testing, typical scan-to-scan differences remained below 1 cm for most of the evaluated measurements."* — a concrete proprietary proof point with an honest scope caveat right after it ("does not guarantee the result of any single scan"), not a vague compiled claim.
- *"Scan records carry randomly generated IDs, and 3DLOOK cannot identify a specific individual from them."* — a specific architectural/privacy detail that reads like someone who has seen the product, not boilerplate.
- The six-step integration sequence under "Can FitXpress be integrated into a telehealth or clinical workflow?" gives an engineering/product reader an actual mental model of the data flow (capture → API → processing → structured outputs → customer routing → clinician review) — a genuine differentiator versus a generic "how it works" FAQ.

## for_agent_improver

1. **seo-editor (round-1 rewrite step):** when a review lists explicit banned/flagged terms (e.g. "no sport/regular/oversized"), do a literal string check on the rewritten passage before marking the item resolved — this pass dropped "sport" but left "regular-fit" and "oversized" in the Clothing Detector answer, which risks the same flag recurring in round 2.
2. **coordinator/QC:** the "regular-fit"/"oversized" wording above is defensible as genuinely broadened phrasing (more adjectives, not a literal payload enum) — worth a quick human call with Vadim on whether that satisfies C6's intent, since an automated grep alone can't distinguish "broadened description" from "still using the flagged words."
3. **Pattern worth keeping / templating:** the illustration-brief format (`> **[Illustration N: title]**` + "Designer brief: ...") cleanly and reusably satisfies "visuals must be visually distinct from article text" — worth adopting as the default house style for future FAQ/plan-heavy articles so this isn't re-solved from scratch each round.
