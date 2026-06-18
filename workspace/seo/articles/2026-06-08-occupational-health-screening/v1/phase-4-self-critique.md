---
phase: 4_self_critique
article: 2026-06-08-occupational-health-screening
date: 2026-06-08
status: post_critique_fix_applied
parent: draft-final.md
---

# Phase 4 — Self-critique

5 weakest passages, 3 compliance-edge risks, 2 verb-strength leaks, plus the external citation verification list with URLs.

---

## 5 weakest passages

### W1 — Section 2 paragraph 1 ("Several pressures are pushing the operational gap wider...")

The opening sentence ("Several pressures are pushing the operational gap wider") is a generic transition that adds no information. The paragraph would land harder if it opened with the BLS-citation paragraph directly, or with the specific employer-side pressure (hiring volume against fixed clinic capacity).

**Fix recommendation:** drop the first sentence and start with "Employer hiring volume in workforce-intensive sectors..." — the BLS citation becomes the second paragraph as is. Saves ~10 words and gives the section a sharper opener.

### W2 — Section 8 closing paragraph ("The compliance posture matters at procurement...")

The compliance posture sentence repeats fingerprint phrases that already appeared in Section 4 ("HIPAA-maintained, BAA-ready, encrypted-in-transit, encrypted-at-rest, role-based access controls"). The repetition is intentional for SEO and reinforcement, but at length the second mention dilutes rather than reinforces.

**Fix recommendation:** keep the second mention shorter — e.g., "FitXpress is HIPAA-maintained and BAA-ready, with encryption and role-based access controls at the level an occupational health program should expect from any partner handling employee body data." Saves ~15 words and reduces fingerprint-phrase density.

### W3 — Section 9 bullet "Faster pre-appointment data turnaround"

The bullet explanation reads slightly meta ("Better intake data, available earlier, reduces back-and-forth between intake teams, clinicians, and reviewers. The clearance decision itself remains with the clinician, but the path to the decision shortens"). The closing sentence is the clearest claim; the lead-in could compress.

**Fix recommendation:** Combine into "Better intake data available earlier shortens the path from request to clearance review — without changing the clinician's decision rights." Crisper.

### W4 — Section 11 ("More than body scanning") second paragraph

The second paragraph ("Generic body scanning tools may capture measurements. Occupational health programs need more than that — consistent intake workflows, multi-site standardization, audit-ready documentation...") functions as a list-in-prose. The same content would read more cleanly as a true bulleted list per the FX list-with-bold-leads pattern Asselya prefers.

**Fix recommendation:** convert the second paragraph to 4–5 bullets with bold leads. Style-consistency win. Not applied in this version to keep Section 11 short, but worth a pass if the section needs visual differentiation.

### W5 — FAQ Q1 and the Section 3 GEO block are essentially duplicates

The Section 3 GEO answer block question ("What is occupational health screening intake?") and FAQ Q1 ("What is occupational health screening intake?") are the same question with very similar answers (one slightly longer than the other). This is intentional for GEO/LLM citation — search engines may surface either — but a human reader of the full article hits the same content twice within a few minutes.

**Fix recommendation:** accept as is; the duplication serves GEO citation coverage. Note for future articles: keep both, vary the answer phrasing slightly to differentiate.

---

## 3 compliance-edge places (clearance / EEOC / BMI-employment)

### CE1 — Section 9 closing paragraph (the "speeds up clearance" line) — FIXED

**Issue at draft time:** the sentence "The outcome a buyer should evaluate is not whether FitXpress **speeds up clearance** — clearance is a clinician decision" used the literal forbidden Guardrail-4 phrase even in a negation context. A keyword-scanning compliance reviewer would flag the literal string regardless of negation framing.

**Fix applied inline:** rewritten to "The outcome a buyer should evaluate is not the clearance decision itself — that remains a clinician determination. The right question is whether the workflow leading to clearance has fewer manual steps and produces more consistent records." Avoids the literal forbidden phrase, keeps the rhetorical structure.

**Post-fix scan:** zero hits for "speeds up clearance / speeds clearance / FitXpress clears / FitXpress determines / FitXpress makes clearance / FitXpress decides".

### CE2 — Section 5 EEOC anchor sentence — held tight per legal-sensitive sign-off

Sentence reads exactly as approved in Phase 2 §4: "In U.S. employment contexts, pre-employment medical examinations apply only after a conditional offer of employment and where the same examination is required of all entering employees in the same job category, consistent with EEOC enforcement guidance under the Americans with Disabilities Act (ADA). FitXpress intake operates inside that framework — it does not enable a pre-offer medical examination and should not be deployed in a way that would."

**Verification:** EEOC framework (three stages: pre-offer / post-offer / during employment) confirmed live via direct lookup at eeoc.gov enforcement guidance pages (see Citation Verification §C1 below). Framework description in the article matches the actual EEOC guidance. No invented document number, no fabricated citation.

**Compliance reviewer note:** the article does not claim the sentence is a verbatim quote from EEOC. It describes the framework attribution-style ("consistent with EEOC enforcement guidance under the ADA") which is the safer construction.

### CE3 — Section 4 close + Section 12 table row: BMI/body composition not for hiring

The C5 explicit line in Section 4 close reads: "BMI and body composition outputs captured by FitXpress are intake data points within the documentation workflow. They are not designed for, and should not be used as, the basis of hiring, clearance, or employment decisions."

The Section 12 table reinforces with the row: "Inform hiring or employment decisions based on body measurements or BMI" in the "FitXpress does not do" column.

**Compliance assessment:** the dual placement (use-case overview + scope table) provides defense-in-depth. The article never describes FitXpress BMI/body composition outputs as anything other than "intake data points." No language suggests employer discretion to use this data for hiring discrimination.

**Residual risk:** the Use Case Summary block top of article uses the phrase "BMI/body composition estimates as intake documentation" — the "as intake documentation" qualifier is the scope guard. Reader could miss it if they skim only the Summary block. Mitigation: the explicit Disclaimer immediately after the intro re-states the same constraint.

---

## 2 places "FitXpress does X" may read stronger than "supports X"

### V1 — Use Case Summary block: "Solution — Guided mobile body scan from two smartphone photos completed remotely before the appointment"

This is the verbatim approved §2 block from Phase 2. The "Solution" line describes WHAT FitXpress does (the scan capture) without explicit "supports" framing. In the Summary block format, that is the standard pattern (active verb describes the offering); the scope is reinforced two lines down in the "Role" line: "Intake and documentation layer that supports clinician review — not a fitness-for-duty assessment, clearance decision tool, or basis for hiring decisions."

**Assessment:** acceptable as is. The Summary block is structured so the Solution line carries the offering description and the Role line carries the scope. Both lines are visible together.

### V2 — Section 4 paragraph 1: "FitXpress returns structured body data — 80+ body measurements, BMI inputs, and body composition estimates — to the program before the appointment"

"FitXpress returns" reads more active than "FitXpress provides" or "FitXpress supports the capture of". The verb choice is intentional — at the technical-capability level, FitXpress does literally return the data file. The compliance hedge sits in the next paragraph ("BMI and body composition outputs... are intake data points... not designed for... employment decisions").

**Assessment:** acceptable. Verb strength matters at the capability description; scope guards do the compliance work in adjacent sentences. Reader does not encounter "FitXpress returns" in isolation.

**Could be softened to:** "FitXpress generates structured body data — 80+ body measurements, BMI inputs, and body composition estimates — and delivers the record to the program before the appointment." Marginal change. Not applied; original verb chain reads cleaner.

---

## External citation verification list

All four citations were verified live during Phase 3 writing via direct web search and source-page review. Each is anchored to a real authoritative source with a live URL.

### C1 — EEOC enforcement guidance under the ADA

**Cited in:** Section 5 (EEOC anchor sentence) + FAQ Q4
**Source:** U.S. Equal Employment Opportunity Commission, *Enforcement Guidance: Preemployment Disability-Related Questions and Medical Examinations*
**URL verified:** https://www.eeoc.gov/laws/guidance/enforcement-guidance-preemployment-disability-related-questions-and-medical
**What the article cites:** the three-stage ADA framework — pre-offer (no medical questions or examinations), post-offer (examinations allowed if applied consistently to all entering employees in the same job category), during employment (job-related and consistent with business necessity).
**Verification status:** ✅ framework matches the EEOC guidance page. No invented quote or document number. The article does not claim verbatim citation — it describes the framework attribution-style ("consistent with EEOC enforcement guidance under the ADA").
**Related EEOC pages also confirmed:** https://www.eeoc.gov/laws/guidance/enforcement-guidance-disability-related-inquiries-and-medical-examinations-employees + https://www.eeoc.gov/eeoc-disability-related-resources/disability-related-questions-medical-exams-and-confidentiality

### C2 — BLS Survey of Occupational Injuries and Illnesses 2024

**Cited in:** Section 2 (urgency)
**Source:** U.S. Bureau of Labor Statistics, *Employer-Reported Workplace Injuries and Illnesses (Annual)*, 2024 release
**URL verified:** https://www.bls.gov/news.release/osh.nr0.htm (annual news release) + https://www.bls.gov/iif/ (IIF home) + https://www.bls.gov/web/osh/table-1-industry-rates-national.htm (industry rate table)
**Exact claim cited:** "private industry employers reported 2.5 million nonfatal workplace injuries and illnesses, with an incidence rate of 2.3 cases per 100 full-time-equivalent workers" — for 2024.
**Verification status:** ✅ exact numbers confirmed from BLS news release (released January 22, 2026). The 2.5M total represents the lowest count in the SOII data series going back to 2003; the 2.3 incidence rate is also the lowest in series.
**Article phrasing:** "According to the U.S. Bureau of Labor Statistics' Survey of Occupational Injuries and Illnesses for 2024, private industry employers reported 2.5 million nonfatal workplace injuries and illnesses, with an incidence rate of 2.3 cases per 100 full-time-equivalent workers." Matches source exactly.

### C3 — ACOEM fitness-for-duty guidance

**Cited in:** Section 3 (definition)
**Source:** American College of Occupational and Environmental Medicine — guidance and position statements on fitness-for-duty assessments
**URL verified:** https://acoem.org/Guidance-and-Position-Statements/Guidance-and-Position-Statements/Fitness-for-Duty-Assessments-of-Industrial-Firefighters-Guidance-for-Occupational-Medicine-Physicia (industry-specific guidance for firefighters, illustrative of ACOEM's general approach) + https://acoem.org/XOnline-Learning/Fitness-for-Duty-Challenges-(Essentials) (educational module)
**What the article cites:** general framing — that ACOEM guidance describes fitness-for-duty evaluation as "a process of medical review, examination, and documentation conducted within the physician's professional judgment."
**Verification status:** ✅ ACOEM does publish fitness-for-duty guidance for occupational medicine physicians. The framing in the article is general and conservative — it does not claim a specific publication number or invented quote. ACOEM's actual published guidance does describe the assessment as review + examination + documentation conducted by occupational medicine physicians, which is what the article states.
**Note:** the most cited specific ACOEM document is the 2014 Task Force guidance for industrial firefighters (PubMed: https://pubmed.ncbi.nlm.nih.gov/29280776/). The article uses the general framing rather than citing the firefighter-specific document, because the article's audience is broader than firefighter screening.

### C4 — OSHA 29 CFR Part 1904 recordkeeping

**Cited in:** Section 8 (documentation)
**Source:** U.S. Occupational Safety and Health Administration, *Recording and Reporting Occupational Injuries and Illnesses*, 29 CFR Part 1904
**URL verified:** https://www.ecfr.gov/current/title-29/subtitle-B/chapter-XVII/part-1904 (full eCFR text) + https://www.osha.gov/recordkeeping (OSHA recordkeeping landing page)
**Exact claim cited:** "Under OSHA's 29 CFR Part 1904 recordkeeping standards, employers with 10 or more employees in covered industries are required to maintain records of work-related injuries and illnesses on OSHA Forms 300, 300A, and 301, with annual electronic submission required from establishments meeting size and industry criteria."
**Verification status:** ✅ all facts confirmed. The "10 or more employees" threshold, the Forms 300/300A/301 requirement, and the electronic submission requirement (annual window January 2 – March 2, for establishments meeting size and industry criteria per § 1904.41) all match the regulation.
**Article phrasing:** matches source. No invented language, no exaggerated claims.

---

## Summary

**Compliance posture:** clean post-fix. All 5 guardrails enforced. Zero forbidden clearance language. EEOC framework verified. BMI/employment line stated twice (Section 4 close + Section 12 table). Medical-device disclaimer present.

**Citation integrity:** 4 of 4 citations verified live with URLs. Zero fabricated statistics. Article phrasing matches source content in each case. Where the article describes a framework rather than quoting a specific document (EEOC + ACOEM), the attribution language is conservative and does not invent specifics.

**Style discipline:** zero banned 2024-words. Zero banned sentence starters. Zero "not just X, it's Y" rhetorical patterns. Avg sentence length 18.3 words (target 17-22 ✅).

**Open structural improvements (W1–W4):** five passages where prose could tighten further. None block publish. Vadim's call on whether to apply before final.

**Short-sentence ratio note:** see Phase 5 metrics for full discussion. The 44% global short-sentence count is inflated by structural elements (table cells, bullet leads, GEO blocks, FAQ answers, Use Case Summary lines). Body-prose-only ratio is closer to 30%, still higher than the 10-15% target — partly a stylistic feature of B2B punchy-declarative rhythm, partly an artifact of the FX list-with-bold-leads format.
