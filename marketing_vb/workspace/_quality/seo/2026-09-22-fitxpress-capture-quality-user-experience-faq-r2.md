# QC Report — FitXpress Capture Quality & User Experience FAQ (Review Round 2)

**Slug:** 2026-09-22-fitxpress-capture-quality-user-experience-faq
**Scope:** off-plan FAQ, review round 2 (progress-tracking questions + W1–W7 wording fixes)
**Date:** 2026-09-23

## Scores

| Category | Score | Max |
|---|---|---|
| A — Adherence to plan & Review 2 decisions | 4 | 5 |
| B — Factual (code-verified, accepted) | 5 | 5 |
| C — Brand & tone | 3 | 3 |
| D — Format (code-verified, accepted) | 3 | 3 |
| E — Output quality / positioning | 4 | 4 |
| **Total** | **19** | **20** |

**Verdict: ship**

---

## A — Adherence to plan and Review 2 decisions (4/5)

Nearly every P0–P5/W1–W7 item from the Review 2 decisions was implemented precisely, several verbatim.

- The three progress H3s were added under the exact new H2, with the exact titles the decisions specified, and exactly one link to patient-engagement: `## Tracking and displaying progress` → `### How do you track fat loss and lean-mass change?`, `### How can programs visually display fat-mass and lean-mass changes?`, `### How should programs show meaningful progress at 5, 10, or 20 pounds of weight loss?`, closing with "...is covered in [mobile body scanning and patient engagement]".
- The rejected reviewer sentence stayed rejected, and the instruction to mention goal visualization "in neither direction" was honored: no "generic 5/10/20-pound transformation" phrase appears anywhere; instead the piece lands on "Milestone thresholds and the logic behind them belong to the program, because FitXpress returns scan outputs and does not detect milestones by itself." — correct, neutral, no target-weight-visualization claim either way.
- All W1–W7 exact-wording asks landed as specified, e.g. W5 "The phone stands vertically on a stable surface around desk height." and W6 "The captured data is submitted through the integration for FitXpress processing." are verbatim matches.

The one drift: Review 1's "one timing definition ('under 45 seconds from the photos to structured results')" was supposed to recur as a single fixed phrase, but this round carries three different wordings of it — Quick answers: "Structured results return in under 45 seconds from the front and side photos."; Illustration 1 brief: "structured results in under 45 seconds from the photos"; Timing H3: "FitXpress returns structured results in under 45 seconds from the two photos." None matches the canonical string literally, though the meaning is consistent across all three. This is the only place a specific carryover instruction wasn't followed to the letter, so A lands at 4/5 rather than 5/5.

## B — Factual (5/5, code-verified, accepted as-is)

Per instructions this category is not independently re-checked. Code facts: detector CLEAN at 0.37/1000, and "all claim markers trace to the pack (FX-R1-*, FX-R2-* legalized from the reviews)" — including the new P2/P3/P4 corrections (lean mass ≠ muscle mass, Body Progress by scan ID, 3D differences not a tissue map, milestone logic owned by the program) all being present as legalized claims rather than bare assertions. Accepted at full marks per the code verdict.

## C — Brand & tone (3/3)

- No banned-word hits anywhere in the piece (leverage/utilize/harness/robust/seamless/comprehensive/delve/navigate/tapestry/realm/unlock/unleash/game-changing/cutting-edge) — clean scan.
- Review 1's style bans held: no "still", no "so" used as a result-connector, no "see" used as a cross-reference verb — all three were flagged risks in round 1 and none recurred here.
- Prose reads as connected argument rather than a stitched compilation, e.g.: "Guided capture reduces avoidable variation in the photos, while the program prepares its users for the conditions that guidance cannot control." — a real causal sentence, not a list dressed as a sentence.

Minor note (shared with A): the three non-identical "under 45 seconds" phrasings are the one spot where the seams between edit passes show through in tone as well as literal wording — not enough to cost a point, but worth flagging.

## D — Format (3/3, code-verified, accepted as-is)

- Lint PASS, 144 sentences at mean 14.2 / p90 22 / none over 25 — comfortably inside target, no run-on drift from the added progress section.
- Checklist 16/17 with the sole fail being the known `faq_present` false positive — treated as a full pass per instructions.
- Structural ask fulfilled exactly: new H2 "Tracking and displaying progress" holding the three specified H3s, article settling at 13 FAQ H3s / 2,431 words against a 2,300-word target (well inside the ≤2,450 ceiling) — the progress-question expansion didn't bloat the piece into "a progress article," per the P0/P1 guardrail.

## E — Output quality / positioning (4/4)

The FAQ repeatedly earns the "could only be written by someone who saw the product" bar:

- "Phone angle is a separate requirement. The SDK's guidance also covers phone tilt, which concerns the device, while RTPV concerns the person in front of it." — a precise device-vs-person distinction that a generic compiler wouldn't invent.
- "FitXpress estimates lean mass and does not provide a direct measurement of muscle mass. Lean mass includes muscle along with water, bone, organs, and other non-fat tissue." — the P2 correction isn't bolted on; it's folded into the prose as genuine, correcting teaching, exactly the kind of sentence a templated FAQ on this topic would get wrong.
- The three-term glossary — "**Accuracy** is how close a result is to the selected reference method. **Repeatability** is how consistent repeated scans are under comparable conditions. **Capture quality** is whether the submitted photos meet the requirements for processing." — a tight, non-obvious conceptual framework that adds real value beyond what the prompt strictly required.

---

## for_agent_improver

1. **seo-editor (review-round executor):** when a decisions file specifies a single canonical phrase to be reused verbatim across the article (Review 1's "one timing definition"), grep the draft for every existing instance of that concept before closing the round and force literal string match, not just paraphrase match. This round left three near-but-not-identical wordings of the 45-second claim (Quick answers table, Illustration 1 brief, Timing H3) — harmless here, but it's exactly the kind of drift that compounds over multiple review rounds.
2. **seo-reviewer (decisions author):** the "~150-170 words each" sizing guidance for the new H3s was hit almost exactly on the first new question but undershot by ~20-30 words on the second and third (progress-display, milestone). Not a defect worth a return, but if per-answer length parity matters for how these render in a FAQ accordion, worth a quick word-count gate before decisions are marked satisfied.
3. **Positive pattern worth reinforcing pipeline-wide:** the P2 lean-mass/muscle-mass correction is a good model of "legalize the correction into connected prose," not "append a disclaimer sentence" — future correction rounds (any topic) should be pointed at this section as the reference example.

---

## Summary for coordinator

19/20, verdict: **ship**. Main note: the "one timing definition" carryover from Review 1 drifted into three slightly different 45-second phrasings across the piece — harmless to substance, worth a tighter grep-before-close habit in future review rounds.
