# QC Report — FitXpress Capture Quality & User Experience FAQ

slug: `2026-09-22-fitxpress-capture-quality-user-experience-faq`
type: off-plan FAQ, external 3DLOOK brief · reviewer: seo-quality-controller

## A. Adherence to plan/intent — 5/5

All 14 outline sections present, in brief order, nothing added or dropped. Brief-specific constraints (a long list) are honored one by one, not just generally gestured at:

- RTPV defined at first use and explicitly carved out from health assessment: *"RTPV is a capture-quality and positioning control. It does not assess posture as a medical, musculoskeletal, or health condition."* (Section 4)
- Clothing Detector correctly bounded — no "through any clothing," no "prevents manipulation," no auto-rejection language; it only "flags the condition and prompts the user" (Section 6).
- Accuracy / repeatability / capture quality kept as three distinct, explicitly defined terms, figures qualified ("describe performance under the tested conditions. They do not guarantee the result of any single scan"), with a link out to the accuracy framework instead of re-litigating it (Section 7).
- Self-scan promise correctly hedged: *"Some users and some homes are not suited to self-scanning. Those users need the assisted or alternative path..."* (Section 9) — no blanket "everyone can self-scan" claim.
- Workflow section: exactly 6 numbered steps, ends with the verbatim required sentence *"FitXpress is not a medical device."* and keeps clinical decisions with the customer (Section 10).
- Timing section: only "under 45 seconds" appears as a figure, three stages cleanly separated, no other numeric timing claims leak in (Section 11).
- Exactly 5 internal links, each used once, none repeated — matches the brief's link budget precisely.
- Word count 2,039 sits inside the 1,800–2,400 brief window.
- No scope creep into a general telehealth article, accuracy article, progress-tracking article, or privacy FAQ — Q10 (telehealth) and Q13 (progress outputs) both stay at FAQ-answer depth and route deeper coverage to internal links rather than re-writing those articles inline.

Nothing to dock here — this is the standard the rest of the category should be judged against.

## B. Factual accuracy — 5/5 (per code)

Per instructions, accepted as-is from the mechanical layer: detector 0.44/1000, hard_fails `[]`, claims traceability 18/18, no banned claims. No manual override warranted — spot-checked a few numeric claims (96-97%, 1.5-2.0 cm, under-45-seconds, 80+ measurements) against the approved-claims list and all trace cleanly to FX-CQ-009/010, FXS-SPEED, FXS-OUTPUTS.

## C. Brand & tone — 3/3

Reads like a product-literate FAQ, not a compiled one. No banned words found on manual scan (leverage/utilize/harness/robust/seamless/comprehensive/delve/navigate/tapestry/realm/unlock/unleash/game-changing/cutting-edge — none present), consistent with the 0.44/1000 detector score.

Examples of held voice:
- *"Replacing the SDK capture with a custom camera flow removes those checks. Implementations that do so see meaningfully worse accuracy."* (Section 3) — a flat, confident statement about what actually happens in deployments, not a hedge-everything disclaimer.
- *"The classification covers fit categories and will not catch every garment issue that could affect a scan. Clothing instructions during onboarding therefore remain part of the program design."* (Section 6) — hedges land where they should (limitation of an automated check) without turning into blanket caution.
- Minor tic, not a lapse worth losing a point over: "the program needs..." is used as a framing crutch three times across the piece (intro: *"The program still needs clear instructions..."*; Section 8: *"The program needs defined exception handling for this case"*; Section 8 again: *"the program needs a documented alternative measurement path"*). Noted for the improver, not penalized here.

## D. Format & structure — 3/3 (per code, false-positive noted)

Mechanical checklist 16/17; the one failure (`faq_present`) is a detector false positive per coordinator note — the whole page IS an 11-question FAQ under H3s grouped by 3 H2s, the check just looks for a literal `## FAQ` heading. Not counted against the score.

Meta: title 47 chars is short of the standard 50-60 window, but this is a brief-fixed SEO title per the external brief (documented exception, not a miss) — primary keyword "capture quality" sits in the first half of the title as required. Description 155 chars is inside the 140-160 window. Frontmatter/path per pack conventions.

## E. Output quality / unique value — 3/4

This is close to publish-ready but not flawless — a real copyeditor would spend 5-10 minutes, not zero, on two small things:

- Section 5's correction list breaks its own parallel structure: "Repositioning," "Framing," and "Phone angle and placement" are input variables, but the fourth bullet — *"Another attempt. The user takes the photo again where needed."* — is the outcome that wraps the other three, not a peer category. Minor, but a careful editor would collapse it into a closing sentence rather than a 4th bullet.
- The "program needs X" phrasing (see C above) recurs often enough to read as a light rhetorical crutch across a ~2000-word FAQ.

Where it clearly earns its score — genuine product-specific value a generic FAQ template would not produce:
- *"Implementations that do so see meaningfully worse accuracy"* (Section 3) — an operational admission about what breaks when customers bypass the SDK capture layer; only someone who has seen real integrations write this.
- The three-way accuracy/repeatability/capture-quality distinction (Section 7) is a genuinely useful conceptual framework, not FAQ boilerplate, and it's disciplined about qualifying every figure instead of leading with the number.
- The clothing classification detail — *"sport, regular, or oversized"* plus payload propagation to the customer's team (Section 6) — is specific enough that it reads as implementation knowledge, not a generic "wear form-fitting clothes" tip.

## Total: 19/20 — Excellent

**Verdict: ship**

## for_agent_improver

1. **Mechanical checklist / seo-linter**: `faq_present` only matches a literal `## FAQ` heading and produces a false positive on any all-FAQ page (H3 questions grouped under topical H2s, no literal "FAQ" heading). Worth adding a pattern that recognizes "≥N H3s phrased as questions" as satisfying the FAQ requirement, or letting off-plan briefs declare `faq_present: n/a` so QC doesn't have to re-litigate this per article.
2. **seo-editor (voice pass)**: watch for the "the program needs X" framing repeating as a crutch phrase across an article — flag repeated sentence openers/structural crutches, not just repeated words, during the tone pass.
3. **seo-editor (list structure)**: when an FAQ answer turns into a bulleted breakdown, check that all bullets are peers of the same kind (all inputs, or all steps) — Section 5 here mixes three input variables with one outcome bullet ("another attempt"), which a quick structural check would catch.
