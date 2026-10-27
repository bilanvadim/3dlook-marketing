---
qc_date: 2026-10-27
agent: hypothesis-generator
artifact: workspace/outbound/campaigns/2026-10-27-uk-dhwc-glp1-verification/hypothesis.md
track: outbound
artifact_type: hypothesis
total_score: 19/20
status: excellent
coordinator_review: agree
---

# QC Report — hypothesis-generator — 2026-10-27

**Artifact:** `workspace/outbound/campaigns/2026-10-27-uk-dhwc-glp1-verification/hypothesis.md`
**Total: 19/20** — excellent

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 5 | 5 |
| B | Factual accuracy | 4 | 5 |
| C | Brand & tone | 3 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 4 | 4 |

## What was wrong (specific)

### A. Adherence — 5/5
- All template sections present; `icp-detail.md` §2 and `proof-points.md` both used correctly. WebSearch grounding (ITV 2026-01-02, GPhC, DHWC) with sources. Registry checked and saturation surfaced. Deviation from the default "≥30 companies" validation gate (line 149) is deliberate and justified by registry coverage, not an omission.

### B. Factual accuracy — 4/5
- Every number traces to `proof-points.md`: "112,100 scans in 2025 across all 3DLOOK customers", "under 45 seconds from the photos to structured results", "2 photos", "80+ body measurements", "approximately 3.5% mean absolute error under evaluated conditions", "100+ clients". No 96-97% / repeatability in cold copy. No invented clients; UK Meds correctly excluded.
- Line 120: the "Compliance line (UK)" presented as **verbatim** fuses the canonical GDPR sentence with ", with a DPA that includes SCCs." The canonical sentence (`compliance.md` §2 / CLAUDE.md §12) ends at "...under GDPR." DPA/SCC content is separately allowed, but the fused clause is labeled verbatim and the sequencer copies verbatim into M2. Should be two sentences, not one.

### C. Brand & tone — 3/3
- Rule-setting is strong and on-brand: liveness locked to one approved verbatim phrase (line 111), "patients are never suspects" framing (line 115), no "fraud-proof", lead-with-record-and-defensibility. Em-dashes appear in the doc body but are confined to writer-instructions explicitly marked "never copy" (line 105), so they do not reach messages; mechanical bans are code-gated per task scope.

### D. Format & structure — 3/3
- Frontmatter complete (`product`, `profile`, `market`, `use_case`, `cap_per_group`, `banned_terms`). Correct path. `titles` block well-formed. All sections plus Vadim's-decisions and Sources.

### E. Output quality — 4/4
- Hand-off ready for step 2. Sharp, event-anchored angle. Persona work identifies the superintendent/responsible pharmacist as the title generic lists miss (line 68). Honest limits stated (line 56). Objection table with honest answers. Open questions are the right ones.

## Flagged sanity-checks (requested)

1. **HIPAA / customer-name echo — handled correctly.** The live article does carry banned language: line 112 "FitXpress complies with the Health Insurance Portability and Accountability Act (HIPAA)" (equivalent to banned "HIPAA compliant") and line 207 "a leading UK online pharmacy runs it as the BMI verification step in its checkout today." The hypothesis does NOT echo either: line 120 bans all HIPAA wording and marks the "complies with HIPAA" sentence superseded by `compliance.md`; line 119 + Open question 3 quarantine the "leading UK online pharmacy" line out of cold copy pending Vadim. Correct.
2. **DHWC date discrepancy — surfaced, not silently resolved.** Hypothesis WebSearch/Sources state DHWC 23-24 Nov (line 16, 186); Vadim's brief window is 23-25 Nov. The hypothesis flags the conflict explicitly inline at M2 (line 109, "Vadim's window: 23-25 November; confirm, Open question 1") and as Open question 1 (line 173), rather than picking one. Correct.

## Top 3 issues (приоритет для improver)

1. Line 120 GDPR "verbatim" line fuses two permitted statements into one labeled-verbatim sentence; split before it is copied into M2.
2. Strategic risk: net-new universe expected <10 after exclusions (line 20, 149); full pipeline is specified before the go/no-go is answered (Open question 2). This is the dominant campaign risk and is correctly flagged, not a defect.
3. Minor: em-dashes throughout the doc body under an "always, no exceptions" ban context; acceptable only because confined to writer-instructions, not sample copy.

## Coordinator review

agreement: ✅ agree
top_issue: Line-120 GDPR/DPA fusion fixed directly in hypothesis.md (split into two sentences, canonical GDPR sentence now stands alone per CLAUDE.md §12). Two real structural risks remain open for Vadim, not QC defects: (1) net-new company universe likely <10 after registry + HubSpot-deal exclusions, flagged as Open question 2; (2) the HubSpot exclusion CSV at /home/vadim_prod/workspaces/dhwc-2026/ sits outside this repo's sandbox, so whoever runs `company-researcher`/`icp-validator` at step 2 needs read access to it or the exclusion cannot be enforced.
