---
phase: 4_self_critique
article: 2026-05-29-3dlook-accuracy-enterprise-evaluation
version: v2-asselya-rewrite
date: 2026-05-29
status: applied_inline_to_draft_final
target: draft-final.md
---

# Phase 4 — Self-critique of v2-asselya draft-final.md

Five findings. Three were structural design choices made during the rewrite (recorded here for traceability). One produced an inline edit. One stays as a flag.

## Findings that produced edits

### 1. Meta-talk + "problematic/problematic" repetition in Dimension 3

**Location:** Dimension 3 final paragraph.
**Original (draft as first written):** "...3DLOOK addresses all three in its production stack, **with the specific features described further in this article.**"
Plus the phrase "what catches a problematic scan before it becomes a problematic measurement" used "problematic" twice in 12 words.

**Issue:** The "described further in this article" clause is meta-talk per Asselya [h]. The double "problematic" is just awkward.

**Fix applied inline to draft-final.md:**
- Cut the meta-clause.
- Replaced "problematic scan / problematic measurement" with "bad scan / bad measurement" for cleaner cadence.

Final reads: "The substantive question is what catches a bad scan before it becomes a bad measurement. For any body scanning system, the answer is some combination of capture-time validation, clothing-aware correction, and training across varied real-world conditions. 3DLOOK addresses all three in its production stack."

## Findings on structural design choices made during rewrite

### 2. H2.4 (dataset deep-dive) and H2.5 (per-body-part repeatability stability) — cut from v2 entirely

**v1/v2 had** two separate H2 sections for dataset methodology (ground-truth capture rig, 4 cameras, 34 configs, 86 anatomical params, NCSU expansion in full) and per-body-part repeatability stability (variance categories).

**v2-asselya cut both.** Per Asselya [o], no dataset methodology deep-dive; per Asselya [o] + Vadim follow-Asselya, no per-body-part numbers.

**What replaced them:**
- Dataset demographic scope (the defensive disclosure piece) moved into Dimension 1.
- NCSU mention condensed into a single paragraph in Dimension 5 + a one-line reference in the pipeline section.
- Per-body-part repeatability claim collapsed into the Dimension 2 single sentence: "variance of less than 1 cm for most measurements across repeated scans".

**Net effect:** ~9 H2 sections instead of 10, ~950 fewer words.

### 3. Order of post-dimensions sections changed

**v1/v2 order:** Pipeline → Dataset methodology → Repeatability deep-dive → Body composition → Methods landscape → Compliance → Production reliability → Checklist.

**v2-asselya order:** Pipeline → Production reliability → Body composition → Methods landscape → Compliance → Checklist.

**Rationale:** Dataset methodology and repeatability deep-dive sections were removed (see Finding 2). Production reliability now sits adjacent to the pipeline section because both describe "how the system works at run time"; compliance now closes the body content (procurement-oriented), with the checklist as the final reader takeaway.

### 4. Pipeline section keeps the "trained on a proprietary dataset of thousands of participants across US and Europe" line

**Decision:** the verbatim phrasing from Asselya's instruction [o] is preserved exactly at the end of the pipeline section. This is the article's only mention of dataset scale, and it follows Asselya's preferred wording rather than the precise 5,000+/150,000+/30,000+/430,000+ breakdown that was in v1/v2.

### 5. DEXA/InBody/manual mentions: stripped of academic definitions, kept as method labels with operational context

**Decision per Asselya [q]:** the methods section names DEXA, bioimpedance, smart scales, manual anthropometry, hardware 3D scanners — but never defines them ("dual-energy X-ray attenuation imaging" wording removed). Each is described only by operational context (in-clinic / consumer / remote / etc.) so the reader knows where 3DLOOK fits without an academic primer they didn't ask for.

## Flagged for Asselya verification (item [l])

The user's revision brief noted that comment [l] flagged "a specific fact for verification, probably near Smart Scales or ISO benchmark detail." My best-guess removal — applied to v2-asselya — is the **ISO 8559-1:2017 multi-company benchmark internal study scope** (14 companies, 8 countries, 27 participants, 72 subjects, 1,152 data points).

**What stayed:** the simplified ISO mention — "an independent multi-company benchmark using the ISO 8559-1:2017 standard placed session-to-session repeatability at 0.40 cm."

**What was removed (pending Asselya confirmation):** the breakdown of 14 companies / 8 countries / 1,152 data points. This material was already being trimmed under [o], so [l] removal piggybacks cleanly.

If Asselya intended a different fact to flag (Smart Scales MAE / SD / relative-error breakdown is the second most likely candidate; or the U.S. Navy formula selection rationale a more distant third), surface that and the rewrite can adjust.

## Hedge discipline audit (sampling 9 numeric claims)

| Claim | Hedge | Status |
|-------|-------|--------|
| 96–97% accuracy | "Internal validation against expert pattern-maker manual measurements..." | ✅ |
| 1.5–2.0 cm typical error | Same sentence as above | ✅ |
| >95% repeatability, <1 cm variance | "Internal repeatability testing across five repeated scans per person..." | ✅ |
| BMI 89% / 76% within 5% | "Internal testing of BMI calculated from estimated weight..." | ✅ |
| Smart Scales 2.1 kg / 3.11% / 3.5% | "Internal testing shows..." | ✅ |
| 0.40 cm ISO benchmark | Reference disclosed inline (3D scanner average), and explicit warning not to combine with internal study | ✅ |
| "thousands of participants" | "trained on a proprietary dataset of thousands of participants across US and Europe" — scope claim, not performance claim, no hedge needed | ✅ |
| Demographics 16–78 / 150–205 cm / 38–210 kg | "The internal validation population covers..." — scope disclosure | ✅ |
| 1.5–2.2 cm waist-circumference industry range | "Mobile body scanning systems in this category typically operate in..." | ✅ |

**All sampled performance claims sit in explicit hedges. None are naked numbers.**

## Insider-tone re-scan

| Pattern | v1 result | v2-asselya result |
|---------|------------|----------------------|
| Word "vendor" | Present in 6 places | **0** ✅ |
| "framework 3DLOOK uses internally" | Present | **0** ✅ |
| "opens every sales call" or "the question that opens" | Present | **0** ✅ |
| "Two vendors quoting same %" comparative framing | Present | **0** ✅ |
| Speaking-for-others comparisons | Several | **0** (one industry observation about 1.5–2.2 cm range remains, but is phrased neutrally) ✅ |

## Banned-content re-scan

| Category | Result |
|----------|--------|
| Banned 2024-words (leverage / harness / robust / seamless / comprehensive / delve / tapestry / realm / navigate / game-changer / revolutionary / cutting-edge / disrupt) | **0** ✅ |
| Banned sentence starters (Furthermore / Moreover / Additionally) | **0** ✅ |
| Rhetorical em-dash patterns ("not just X — Y") | **0** ✅ |
| Triple parallelisms | **0** ✅ |
| AI-powered as standalone value | **0** ✅ |
| Per-body-part error table | **0** ✅ (was cut entirely) |
| Smart Scales formula / volume-density methodology | **0** ✅ (was cut entirely) |
| Dataset methodology deep-dive (4 cameras / 34 configs / 86 params / 1M polygons) | **0** ✅ (was cut entirely) |
| Academic DEXA/InBody/manual definitions | **0** ✅ (was cut entirely) |
| Em-dash density | 18 instances in 3,143 words — all parenthetical or range; none rhetorical |

## Frontmatter status update applied

`status: ready_for_vadim_full_read` set in draft-final.md frontmatter.
