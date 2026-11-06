---
qc_date: 2026-11-05
agent: hypothesis-generator
artifact: workspace/outbound/campaigns/2026-11-05-latam-insurance-underwriting/hypothesis.md
track: outbound
artifact_type: hypothesis
total_score: 17/20
status: good
coordinator_review: done
---

# QC Report — hypothesis-generator — 2026-11-05

**Artifact:** `workspace/outbound/campaigns/2026-11-05-latam-insurance-underwriting/hypothesis.md`
**Total: 17/20** — good

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 4 | 5 |
| B | Factual accuracy | 4 | 5 |
| C | Brand & tone | 3 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence — 4/5
- Present: every template section, Learnings applied (IDs and figures match learnings.md 2026-10-30), registry dry run, web research, Account facts stub, the whole evaluation design (l.207).
- The default people source for step 3 cannot run as written (l.108, OQ6 l.326): `apollo-pull.py search` sends only an org domain and titles; `--seniorities` switches titles off; no location or exclusion parameter; the 15-per-company cut happens in Apollo's own order before location is known (only at `enrich`, 1 credit per person). For group C (global reinsurer domains) and global-domain groups the slots fill with people outside BR/MX or P&C staff. OQ6's 300-465 credits and the 150-300 to send ignore this.

### B. Factual accuracy — 4/5
- Product numbers all from proof-points.md; internal figures check out (katya baselines, HYP-5, UK twin 90/15/0, 11+10+2+8 = 31, geo_profile "america" trap).
- l.68 "Most individual life in both markets is accepted on a declaration": no share figure backs "most".
- Mexican forms seen only via search (AXA, Banorte); 7 of 10 A-MX rows have no evidence of a declaration path or a height/weight question (GNP, MetLife MX, Monterrey NYL, BBVA, Allianz MX, Zurich Santander, MAPFRE annex only). "About 23 IN" leans on them.
- l.40/54/352 call the Allianz Brasil form "its individual life declaration"; the file is "DeclaracaoComplementar-e-ficha-financeira" (complementary declaration + financial questionnaire, likely a higher-sum route). Step 2 to confirm.

### C. Brand & tone — 3/3
- No dashes, no banned words; English-only rules for second-language readers explicit (l.164, l.197).

### D. Format & structure — 3/3
- Frontmatter complete, titles block present, banned_terms adapted to LatAm.

### E. Output quality — 3/4
- **Tele-interview scope contradicts itself:** l.23/l.173 say Icatu sends cases above the DPS limit to a tele-interview (height/weight still stated), but l.199 ("adds evidence to cases that get none of these"), the anti-case l.226 (copied from the US twin) and the evaluation design l.207 (reference group = applicants sent to a medical exam above the declaration limit) assume an exam right above the limit.
- **"The insurer's own reviews of declaration cases … as its monitoring"** (l.173, l.200): US holdouts/post-issue audits renamed; no evidence BR/MX insurers run them; the usual after-issue check there is at claim, which the Rules ban.
- **"risk class"** (l.173, l.197, l.199): US term; LatAm evidence points to acceptance, loading and routing to an exam.
- **"results to the insurer's systems only"** (l.175): outputs stored on AWS in the US (compliance.md §3); a paraphrase would be wrong for BR/MX readers (Risk 5).
- **Open questions:** 14, sensible defaults; missing: Itaú OUT on individual-life grounds only though mortgage/credit life with DPS is in the Vertical (Bradesco IN on that basis; Itaú #2 by 2025 life premium, l.349); OQ5 doesn't say the "not a medical device" line rests on UK/EU MDR (compliance.md l.16), no ANVISA/COFEPRIS basis, nor that katya's 2026-10-05 LatAm default was no compliance line.
- **Acceptance target** 37% (l.294) = katya's health-list baseline; Risk 7 and UK twin (15/90) point lower.

## Top 3 issues (priority for improver)

1. **Tele-interview scope contradicts itself** (l.199, l.207, l.226 vs l.23, l.173): treat tele-interview cases as declared-height-and-weight cases, fix the anti-case, reference group = whichever cases the insurer actually measures.
2. **Default people source cannot run with apollo-pull.py as is** (l.108, OQ6 l.326): no location filter, no exclusions, cap before location. State the method that works or the wasted-credit risk.
3. **US carry-overs and missing routing:** "own reviews of declaration cases", "risk class", "results to the insurer's systems only"; route Itaú's credit/mortgage-life path and the jurisdiction behind the medical-device line to Vadim.

## Coordinator review

- **agreement:** agree with all three top issues; verified l.23/173/199/207/226 by sed (the contradiction is real, the anti-case is the US twin's line). On issue 2 the script gap is real, but the twins already ran it with a coordinator scratch wrapper adding `person_locations[]` plus a free title pre-filter before `enrich` (UK 10-23, EU 11-02, US 11-05); the fix is to state that method and the credit estimate after pre-filter, not to switch source.
- **top_issue:** tele-interview scope / evaluation reference group (would make writers drop a real use case or propose the wrong comparison, the same class of defect that cost the US twin a 12/20 messages round).
- **action:** fix round by a FRESH hypothesis-generator (playbook: never resume the ~400K author), then Vadim's open questions.
