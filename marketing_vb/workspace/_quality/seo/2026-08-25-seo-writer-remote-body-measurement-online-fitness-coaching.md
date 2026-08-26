---
qc_date: 2026-08-25
agent: seo-writer
artifact: workspace/seo/articles/remote-body-measurement-online-fitness-coaching/draft.md
track: seo
artifact_type: seo-final
total_score: 20/20
status: excellent
coordinator_review: |
  agreement: ✅ agree
  top_issue: GLP-1 not expanded at first use (M1 miss) and BOFU URL path-debt need to be closed in edit/publish passes, not carried silently to Vadim.
---

# QC Report — seo-writer — 2026-08-25

**Artifact:** `workspace/seo/articles/remote-body-measurement-online-fitness-coaching/draft.md`
**Total: 20/20** — excellent

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 5 | 5 |
| B | Factual accuracy | 5 | 5 |
| C | Brand & tone | 3 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 4 | 4 |

## What was wrong (specific)

### A. Adherence — 5/5
- All 12 plan sections written in order, each holding its assigned boundary. Scope note placed in the intro (line 13), the "accurate enough for which decision?" reframe carried through (lines 25, 104), repeatability framed as the coaching-relevant property (line 29).
- Every approved-claim ID assigned in the plan appears inline as an HTML comment on the correct sentence (FX-001…FX-008 all used; `claims_used` frontmatter matches).
- 4-direction internal links all present: up → AI in Fitness hub (line 135); side → Main Health hub (line 135) + Patient Engagement (line 67); down → `/fitxpress/for-connected-and-digital-fitness/` (line 137); trust → accuracy framework (line 92).
- Privacy trust link handled per plan open-item #4: no dead link, short inline note that the central privacy reference is planned (line 128).
- FAQ = 7 questions, matching the plan's list one-for-one (lines 112-131).

### B. Factual accuracy — 5/5
- Every numeric/factual claim traces to an approved claim ID: 80+ measurements + 3D model (FX-003), under 45s (FX-004), composition outputs BMI/BMR/fat%/lean/fat (FX-005), weight ±3.5% labeled as software output not a scale (FX-006, line 43), 96-97% vs expert manual (FX-001), variance under 1 cm at 95%+ (FX-002), HIPAA/GDPR + face obfuscation + no identifiers + 30-day delete (FX-007), 9+ yrs / 150K+ / 30K+ / 430K+ training data (FX-008). All match `proof-points.md`.
- No fabricated fitness-coaching customer — the article uses capability + segment framing only, exactly as plan open-item #2 required. Yazen/UK Meds correctly not borrowed.
- Accuracy scoped, never reduced to one universal number (line 55 qualifies it explicitly); the two benchmarks are never combined; no anti-positioning ("most accurate") language.

### C. Brand & tone — 3/3
- Zero em dashes (grep-confirmed), zero banned words, no "positioned as", no "not just X, it's Y", no adjectival triple parallelisms. Medical framing stated directly ("FitXpress is not a medical device", lines 13/73/131).
- BMI / US / EU left unexpanded per the commonly-known rule; DEXA, BIA, BMR expanded at first use (lines 27, 75).
- Minor terminology items for the editor pass (not category-dropping): (1) **GLP-1 is never expanded** (lines 73, 100) — it is not on the commonly-known exception list, so M1 asks for glucagon-like peptide-1 at first use; (2) repeatability is written as "variance under 1 cm" throughout (lines 55, 63, 90, 106, 122) rather than the `< 1 cm` glyph form the context pack's `accuracy_framing` specifies — semantically identical, acceptable prose, flagged only for consistency; (3) DEXA is re-expanded in the FAQ (line 119) after its line-75 first use — redundant, trim on edit.

### D. Format & structure — 3/3
- Frontmatter complete (`slug`, `section`, `status`, `word_count`, `claims_used`, `author`, `product`); `word_count: 1985` sits inside the 1,800-2,200 target; author Assel Sekerova; product fitxpress.
- Correct path under `workspace/seo/articles/{slug}/`. Full 12-part strategic structure with comparison-by-role table and FAQ block, matching the plan template.

### E. Output quality — 4/4
- Publication-ready pending a light editor pass on the three C-items above. Owned intent is narrow and on-strategy (coaching-program workflow, not generic apps), cannibalization guardrail respected — stays clear of the two sibling Hub 1 rows and does not re-do the AI-in-Fitness overview.
- Comparison table does not oversell: it concedes weight to the calibrated scale and composition to DEXA both in the table (line 89) and in prose ("Where a program needs a single trusted body weight, the scale is the tool. Where it needs a clinical composition reference, DEXA is the tool", line 92).
- "What FitXpress does not do" section is present and honest (lines 69-77): not a medical device, not a DEXA/BIA/scale replacement, not GLP-1 eligibility, not a decisioning system.
- Reads as expert human copy — declarative, hedged, workflow-framed; retention consistently framed as a lever, not a promise (lines 37, 63).

## Top 3 issues (priority for improver)

1. GLP-1 not expanded at first use (lines 73, 100) — the one concrete M1 terminology miss; editor to expand or confirm GLP-1 as commonly-known for this segment.
2. BOFU link `/fitxpress/for-connected-and-digital-fitness/` (line 137) carries the CLAUDE.md §16 path-level debt (plan open-item #3) — confirm the canonical URL with Vadim before publish, not a writer defect.
3. Repeatability rendered as "under 1 cm" rather than the specified `< 1 cm` form, and DEXA re-expanded in the FAQ — trivial consistency cleanups on the editor pass.

## Coordinator review

(заполняется Claude в чате после автозапуска QC)
