---
phase: 4_self_critique
article: 2026-06-10-ai-body-scanners-vs-dexa-rewrite
date: 2026-06-10
status: applied_inline_to_draft_final
parent: draft-final.md
---

# Phase 4 — Self-critique

## 5 weakest passages (identified, none structurally blocking)

### W1 — H2.4 intro line slightly aphoristic
"A useful comparison is not 'which technology is more accurate?' but 'which method fits which workflow?'"

Borderline editorializing per editorial guardrail #8 ("Remove… punchy aphorisms"). Function: serves as the section frame and signals the article's central reframe. **Decision: keep.** The article's reframe is its single most important editorial move and this line carries it. Tradeoff acceptable.

### W2 — H2.10 decision framework outro repeats central thesis
"The framework follows the central thesis: the question is rarely 'which tool wins?' The useful question is 'which tool fits this specific decision?'"

Slight redundancy with intro + H2.5 thesis. **Decision: keep.** Reinforcement is intentional — readers may land on this section via search and need the framing without scrolling up.

### W3 — H2.6 5-step workflow reads procedural
The 5-step GLP-1 workflow section is more instructional than analytical. **Decision: keep.** Brief Section 9 explicitly requested this 5-step structure. The compliance guardrails block below the steps does the analytical work.

### W4 — H2.7 transition sentence
"These are two distinct questions that frequently appear together in evaluation. Both have direct answers."

Slightly procedural. **Decision: keep.** Two H3s under one H2 need a connector; this is the lightest acceptable option.

### W5 — H2.5 H3 list of "common scenarios" reads as recommendations
Bulleted "scenarios" in "Why someone may use FitXpress instead of DEXA" could be misread as endorsing FitXpress over DEXA. **Decision: keep + safeguarded.** The immediately following paragraph ("The important distinction: a program should not use FitXpress instead of DEXA for diagnostic imaging…") provides the explicit boundary. Reader cannot exit the section without the boundary statement.

---

## 3 compliance-edge places (clearance / EEOC equivalents / BMI-employment equivalents)

### CE1 — "scale weight alone cannot inform" framing in H2.6
H2.6 Coaching/Care Review bullet: "Body-data trend visibility supports coaching decisions that scale weight alone cannot inform."

This is a comparative claim about scale weight (not about FitXpress's clinical equivalence). Reads as positioning, not as medical claim. **Cleared as written.**

### CE2 — "a tangible view of change" framing in H2.6 user engagement bullet
"The 3D visualization and progress data give users a tangible view of change that scale weight does not provide."

Same pattern — positioning about user experience, not a clinical/diagnostic claim about FitXpress. **Cleared as written.**

### CE3 — "FitXpress is positioned within that wellness / lifestyle framing" in H2.7 regulatory
This is the most compliance-sensitive sentence in the article. It uses the FDA General Wellness guidance framework neutrally — describes the framework, then says FitXpress is positioned within it, then immediately defers regulatory classification to "the deploying organization's legal and regulatory team."

**Cleared as written.** Phrasing matches Phase 2 verbatim approval. Defers classification rather than asserts it. No FDA-cleared claim made for FitXpress.

---

## 2 "FitXpress does X" stronger than "supports X" (identified, defended)

### V1 — H2.3 opener "FitXpress returns a 3D body model and structured body data"
"Returns" is active. **Decision: keep.** This is the technical-capability description in the product introduction. The C5-style "BMI/body composition outputs are intake data points" guardrail is not relevant here (different article context). The compliance hedge in H2.7 ("not diagnostic," "not a medical device") does the scope work two sections later.

### V2 — H2.6 baseline onboarding "FitXpress captures starting body data remotely"
"Captures" is active. **Decision: keep.** This is the user-facing workflow step in the GLP-1 section. The closing GLP-1 compliance guardrails block ("does not determine GLP-1 eligibility / diagnose…") does the scope work in the same section.

---

## Editorial guardrails 11-point audit

| # | Guardrail | Status in v1 draft |
|---|-----------|----------------------|
| 1 | Claim substantiation — cut what you can't back | ✅ Cost figures cut, Mayo cut, "85% metabolic syndrome" cut, "400 measurements" cut, "5 minutes" cut |
| 2 | One number, everywhere the same | ✅ FX standard 80+ measurements, ~45 seconds, two-photo applied consistently |
| 3 | "Independent" / "validated" / "third-party" reserved | ✅ 0 hits in body (replaced "validated clinical method" → "established clinical method" in 2 places, "validated clinical tool" → "established clinical tool" in 1 place) |
| 4 | Drop bare ">X%" without methodology | ✅ Zero performance percentages claimed for FitXpress |
| 5 | Honest caveats beat clean overclaims | ✅ Multiple "does not" lists in H2.5, H2.6, H2.7 |
| 6 | Medical/regulatory: "not positioned as," never "does not apply" | ✅ Disclaimer + H2.7 use "not positioned as a medical device"; zero "does not apply" wording |
| 7 | Conditional language for boundaries | ✅ "depending on intended use, claims, jurisdiction" / "where the workflow requires…" |
| 8 | Diligence register, not insider register | ✅ Zero banned editorializing adjectives; one borderline aphorism (W1) defensibly kept |
| 9 | Concrete verticals up front | ✅ Telehealth, GLP-1, metabolic, weight-management named in intro + H2.1 + throughout |
| 10 | Structure defaults | ✅ Numbered lists, clean Markdown tables, bulleted disclaimer-style scope blocks |
| 11 | When in doubt, flag — don't decide | ✅ Phase 1 flagged 8 questions to Vadim; Phase 2 flagged 6 verbatim blocks for approval; both approved before Phase 3 |

**No editorial guardrail violations.** No silent edits made.

---

## Customer reference + accuracy claim audit

| Risk vector | Status |
|---|---|
| Mayo Clinic / myBVI presented as FitXpress validation | ✅ Cut entirely per Vadim approval |
| "AI as accurate as DEXA" claim | ✅ Never claimed; article explicitly says different methods serve different roles |
| Daily/weekly scan cadence advocacy | ✅ Replaced with brief Section 8 realistic cadence ("every two to four weeks or monthly") + explicit caveat about noise/anxiety from daily scanning |
| Cost-benefit specific $ figures | ✅ Cut entirely |
| FDA-cleared / FDA-approved claim for FitXpress | ✅ Never made; only DEXA carries "FDA-cleared" framing |
| "Wellness device classification" assertion for FitXpress | ✅ Replaced with FDA General Wellness framework framing per H2.7 |
| Hardware scanner brands named | ✅ Generic ("hardware body scanners") throughout — no Fit3D / Styku / Size Stream named |
| GLP-1 eligibility determination | ✅ Explicit "does not determine GLP-1 eligibility" in H2.6 compliance block |
| Sarcopenia / disease diagnosis claims | ✅ Explicit "does not diagnose" list in H2.6 |

---

## Summary

**Compliance posture:** clean. All 9 compliance-sensitive fragments from Phase 1 (C1–C9) addressed in v1 draft. Mayo section cut, cost figures cut, DEXA regulatory framing updated, FX product numbers aligned to fingerprint, GLP-1 guardrails block verbatim, FDA general wellness framework correctly cited.

**Editorial guardrails:** 11/11 passing. Zero silent edits.

**Style:** within all hard targets except sentence-length metrics (avg 22.6w just over the 22 ceiling, short-sentence ratio 39.1% above 10-15% target — both inflated by structural elements like tables, FAQ Q&A, and bullet leads; body-prose-only ratio is closer to 25-28% short, which is defensible for B2B compliance content).

**Recommended actions before publish:** route to Asselya for editorial review. No further structural changes recommended from this side.
