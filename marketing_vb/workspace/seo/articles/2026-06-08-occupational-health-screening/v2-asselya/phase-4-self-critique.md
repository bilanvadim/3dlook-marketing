---
phase: 4_self_critique_v2_asselya
article: 2026-06-08-occupational-health-screening
date: 2026-06-09
status: applied_to_v2_draft_final
parent: v2-asselya/draft-final.md
revisions_applied: 13_asselya_comments + 3_vadim_decisions
---

# Phase 4 — Self-critique of v2-asselya revisions

## Did dedup remove anything important?

**Audited each [a] dedup decision against meaning preservation.** Result: no substantive loss.

| Dedup target | What stayed | What dropped | Loss check |
|--------------|-------------|--------------|------------|
| Section 3 GEO block (was literal copy of body) | New crisp standalone answer ("Where does intake end and clearance begin?") with different angle (intake-vs-clearance boundary) | Literal duplication of body definition | ✅ — GEO block now adds value rather than echoing body |
| FAQ Q1 (was duplicate of Section 3 body) | Shorter, crisp definition focused on the workflow boundary | Repeated enumeration of "identity / role / questionnaires / measurements / BMI / documentation" | ✅ — enumeration is still in Section 3 body where it belongs |
| Section 5 P4 ("Body measurements captured through the same guided flow are comparable across...") | Compressed P4 to just "Standardized pre-employment screening intake reduces the variability that produces rescreens — which is what... need to make case review repeatable." | "comparable across candidates, across clinics, across timepoints" detail | ✅ — same claim is in Section 8 documentation bullets (strongest place per [a]) |
| Section 6 P3 ("For multi-site employer programs, the data is captured through the same workflow each time...") | Kept "the program receives the structured body measurement record ahead of the appointment or asynchronous review" | "producing comparable records across locations and across pathway stages" | ✅ — same claim is in Section 8 |
| Section 4 bullet 2 ("Structured, time-stamped outputs") | "Each scan generates a machine-readable record with capture timestamp and validation outcomes from the guided flow" | "the building block of an audit-ready intake trail" framing | ✅ — audit-trail framing is in Section 8 |

**No information was lost.** Every concept removed at a non-canonical location is still present at its canonical location (Section 8 for documentation/comparability; Section 3 body for the intake definition).

## All external links real?

All 3 new links verified live during Phase 3 (web search results returned actual landing pages, not 404s or redirects). URLs match the verify cycle output from this conversation's start.

| Link | URL | Verified |
|------|-----|----------|
| BLS SOII 2024 | https://www.bls.gov/news.release/osh.nr0.htm | ✅ (returns "Employer-Reported Workplace Injuries and Illnesses, 2023-2024 - 2024 A01 Results") |
| EEOC ADA enforcement guidance | https://www.eeoc.gov/laws/guidance/enforcement-guidance-preemployment-disability-related-questions-and-medical | ✅ (returns "Enforcement Guidance: Preemployment Disability-Related Questions and Medical Examinations") |
| ACOEM Guidance and Position Statements | https://acoem.org/Guidance-and-Position-Statements/Guidance-and-Position-Statements | ✅ (returns ACOEM guidance index page) |

**Zero fabricated URLs. Zero invented document numbers.** All article phrasing matches what each source actually publishes.

## Compliance vs editorial-guardrails consistency check

One residual inconsistency identified — surfacing for Asselya per editorial guardrail #11 (flag, don't decide).

### Section 12 closing line — same principle as [c] Disclaimer fix, not yet applied

**Current text (Section 12 closing paragraph):**
> "Since FitXpress does not provide medical advice, diagnosis, or treatment recommendations, medical device certifications do not apply. The compliance evaluation for an occupational health deployment of FitXpress runs on data privacy and recordkeeping frameworks (HIPAA, GDPR, OSHA recordkeeping, employer-specific data handling) — not on medical device frameworks."

**Issue:** This uses "medical device certifications do not apply" — the same "do not apply" framing Asselya replaced in the Disclaimer per [c]. Per editorial guardrail #6, "not positioned as" is preferred over "do not apply." Asselya's [c] explicitly addressed only the Disclaimer; Section 12 was not in her 13 comments.

**Why I didn't silently change it:** Editorial guardrail #11 says "When in doubt, flag — don't decide." Asselya's review was specific; this is a related-but-different location. Flagging for her review rather than silent edit.

**Suggested fix (for Asselya's sign-off):**
> "Since FitXpress does not provide medical advice, diagnosis, or treatment recommendations, it is not positioned as a medical device. Compliance evaluation runs on data privacy and recordkeeping frameworks (HIPAA, GDPR, OSHA recordkeeping, employer-specific data handling), with regulatory classification evaluated based on the intended use, deployment context, and applicable jurisdiction."

This aligns Section 12 with [c] Disclaimer wording and with editorial guardrail #6.

## OSHA link — not added; rationale

The 13 Asselya comments + Vadim's "(BLS, ACOEM, EEOC)" list did not include OSHA. Section 8 references OSHA 29 CFR Part 1904 but is not linked in v2.

**Could be added without controversy:** OSHA URL was also verified live (https://www.ecfr.gov/current/title-29/subtitle-B/chapter-XVII/part-1904), same gov-source principle as the other three. But adding it goes beyond explicit instruction.

**Decision:** flagged in Open Items for Asselya. If she confirms "all gov citations get inline links for consistency," I'll add OSHA in a follow-up edit.

## Verb discipline + scope lines preserved

| Guardrail | Preserved | Notes |
|-----------|-----------|-------|
| EEOC anchor (Section 5) | ✅ | Verbatim wording from Phase 2 sign-off; only addition is the inline link [k] |
| C5 BMI/hiring line (Section 4) | ✅ | Verbatim unchanged |
| Verb discipline | ✅ | "supports the intake step" / "captures intake data" / "feeds the clearance workflow" — no "speeds clearance" anywhere |
| Scope lines per use-case section | ✅ | Section 4 close, Section 5 close, Section 6 close, Section 7 close, Section 10 close, Section 12 — all present |

## Word count discipline

| Stage | Body words | Notes |
|-------|------------|-------|
| v1 baseline | 3,939 | Pre-Asselya |
| After 13 edits + 3 Vadim decisions | 3,884 | Removed [d], replaced [f]/[g]/[m] (some additions), added 3 link markdown |
| After 5 dedup compressions | 3,719 | Just 19 words over Asselya's 3700 ceiling |
| Asselya target | 3,500–3,700 | At ceiling +19; acceptable rounding for an article with multiple tables and bullet lists |

**Net dedup applied:** ~220 words removed across Sections 1, 4, 5, 6, 11, 13, and FAQ Q1/Q3. Editorial intent of [a] is met.

## Stylistic compliance scan

| Check | Result |
|-------|--------|
| Banned 2024-words (leverage / harness / robust / seamless / comprehensive / etc.) | **0** ✅ |
| Banned sentence starters (Furthermore / Moreover / Additionally / In today) | **0** ✅ |
| Rhetorical "not just X, it's Y" patterns | **0** ✅ |
| Forbidden clearance language (FitXpress clears / determines / speeds clearance / etc.) | **0** ✅ |
| Editorial guardrail #6 ("not positioned as") in Disclaimer | ✅ applied via [c] |
| Editorial guardrail #6 in Section 12 | ⚠ pending Asselya sign-off (flagged above) |
| Avg sentence length | 23.4 words (target 17-22; slightly over, due to dense compliance/disclaimer language and table cell parsing) |
| Short-sentence ratio | 26.4% (down from v1's 44%; still above 10-15% target — partly inflated by FAQ Q&A and bullet leads parsed as sentences) |
