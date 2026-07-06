---
qc_date: 2026-05-21
agent: seo-editor
artifact: workspace/seo/2026-05-21-online-pharmacy-bmi-verification/draft-v2-final.md
track: seo
artifact_type: article
product: fitxpress
total_score: 18/20
status: excellent
coordinator_review: |
  agreement: ✅ agree
  top_issue: L92 "Most online pharmacies deploy FitXpress in Pattern B" — implies a sample size we cannot defend publicly (UK Meds is the only documented online-pharmacy reference). Trivial 1-line fix, does not require editor round-trip.
---

# QC Report — seo-editor — 2026-05-21

**Artifact:** `workspace/seo/2026-05-21-online-pharmacy-bmi-verification/draft-v2-final.md`
**Total: 18/20** — excellent (ship with minor polish)

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 5 | 5 |
| B | Factual accuracy | 4 | 5 |
| C | Brand & tone | 3 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 3 | 4 |

## Hard rules check

| Rule | Status | Evidence |
|------|--------|----------|
| 1. UK Meds — live customer reference only, no metrics | **PASS** | L102: "UK Meds is the live reference. They use FitXpress as the BMI verification step inside their online pharmacy order flow." L123: "UK Meds runs it as their BMI verification step today." Zero scan counts, zero customer-lifetime numbers, zero outcome metrics anywhere in body. |
| 2. Regulators — general formulations only, no invented clauses | **PASS** | L57: "UK GPhC scrutiny of online weight-loss prescribing is rising. US FDA monitoring of telehealth weight-loss pathways is rising too." Matches the use-case file phrasing exactly. No fake guidance numbers, memo titles, or clause references. |
| 3. CTA — demo only, no 200-request free trial | **PASS** | L123: "request a demo and we will walk through..." L125: "Request a FitXpress demo: contact our team at katerina@3dlook.me." No mention of trial, 200 requests, free tier, or self-serve testing anywhere in body, meta, or OG description in the publish package. |

All three hard rules pass.

## Banned signatures found

**None.** Confirmed by automated sweep and manual read:
- No em-dash characters anywhere in the article body (publish-package OG description has one, but that's outside the article scope).
- No `leverage / utilize / harness / robust / seamless / comprehensive / delve / tapestry / realm`.
- No `Furthermore / Moreover / Additionally` sentence starters.
- No `It's not just X, it's Y` construction.
- No triple parallelism (`fast, reliable, scalable` pattern).
- No `game-changer / revolutionary / cutting-edge / disrupt / unlock the power of / In today's fast-paced world / It's no secret that`.
- `navigate` appears nowhere in figurative sense.

Note: the word "comprehensive" is absent. The closest near-miss is L92 "Pattern B" which is the canonical name from `tech-spec.md` — not a banned term.

## Untraced claims

**None material.** Every factual claim traces to a source:

| Claim (line) | Source |
|---|---|
| L47 — ChatGPT/Gemini experiment, 27 kg heavier, face/body details | `past-posts/.../2026-03-31-i-ran-an-experiment-fake-bmi-photos.md` lines 18-22 |
| L57 — UK GPhC + US FDA scrutiny (general) | `use-cases/fx-online-pharmacy-bmi.md` L7 |
| L77 — Live, in-session SDK capture | `how-it-works.md` L40, `tech-spec.md` L34-38 |
| L78 — Liveness/pose checks | `tech-spec.md` L41-45 |
| L79 — Clothing classification (sport/regular/oversized) | `tech-spec.md` L47-51 |
| L81 — Smart Scales mismatch flag | `how-it-works.md` L19, `tech-spec.md` L100 |
| L90 — 2-photo scan, <45 sec, 80+ measurements | `proof-points.md` L40-41, L47 |
| L92 — Pattern B server-side | `tech-spec.md` L69-72, `case-studies/uk-meds.md` L18-23 |
| L100 — HIPAA, GDPR, TLS, SSE-S3, retention, blur, no PII | `compliance.md` L7-23 |
| L102 — UK Meds is live customer in pharmacy BMI | `case-studies/uk-meds.md` L1-13 |

One soft observation (not an untraced claim, but a slight over-reach): L92 says "Most online pharmacies deploy FitXpress in what we call Pattern B." UK Meds is currently the only documented live online-pharmacy customer in the proof-points + case-studies files. The phrasing implies a sample size we cannot publicly defend. See category B issue below.

## What was wrong (specific)

### A. Adherence — 5/5
- No issues. Every outline section is present in order (H2.1–H2.7). The checklist in H2.4 contains all 5 required items plus the explicit "Self-report cross-check" the outline calls out (L81). All four secondary keywords appear naturally (verified by publish-package L89). Word count 1672 is inside the 1500–2000 target. The Katerina-voice anchors (problem-first opener at L27, single-sentence stand-alone "The trouble is not the patient. The trouble is the method." at L39) match the style brief.

### B. Factual accuracy — 4/5
- L92: "Most online pharmacies deploy FitXpress in what we call Pattern B." UK Meds is the single documented online-pharmacy reference customer in `case-studies/` and `proof-points.md`. "Most" implies a plurality of online-pharmacy customers we cannot defend in print. Suggest tightening to "The most common deployment pattern for this use case is Pattern B…" — same workflow point, no implicit sample size. This is the only factual softness; nothing else is over-stated.

### C. Brand & tone — 3/3
- No issues. Tone matches Katerina-voice anchors: flat declarative opener, short paragraphs, single-sentence stand-alones at transitions ("The trouble is not the patient. The trouble is the method." L39; "If a vendor cannot answer the first two cleanly, the rest does not matter." L117). Compliance language is conservative ("HIPAA-maintained" not "HIPAA-certified") which matches `compliance.md` constraints. Zero banned-word hits.

### D. Format & structure — 3/3
- No issues. Frontmatter contains `track`, `product: fitxpress`, `stage`, `target_keyword`, `secondary_keywords`, `status`, `word_count`, `edits_summary`, `hard_rules_check`, `created`. File path matches `workspace/seo/{YYYY-MM-DD}-{slug}/draft-v2-final.md` convention. H1 + 7 H2s match outline structure 1:1. Two embedded bullet checklists (H2.4 standard, H2.6 vendor questions) match the outline's "Katerina bullet style" call-out.

### E. Output quality — 3/4
- Ready with minor polish (5–10 minutes of Vadim's editorial pass). Three observations holding this off a 4:
  1. **L92 "Most online pharmacies" over-reach** (see B). Same fix removes both issues.
  2. **L98 anglicism inconsistency:** "second line of defence" (British spelling) but the rest of the article uses US conventions elsewhere ("defensible" L41, L67, L86, L121; "defensibility" L67). Pick one. Given UK-first SEO targeting (per outline L30), `defence` is defensible — but it should be consistent.
  3. **CTA L125 is slightly weak as a closer:** "Request a FitXpress demo: contact our team at katerina@3dlook.me." A bare mailto burns the CTA for compliance buyers who expect a form or calendar link. Not the editor's fault (the publish-package flags the URL as TBD), but it's the part that will need a Vadim swap before publish.

The unique value is real — the article articulates a "verification standard" framework (H2.4) that competitor pages don't, anchored in a published CEO experiment and a real customer. That's the kind of asset that earns mid-funnel backlinks from compliance/telehealth analyst pieces.

## Top 3 strengths

1. **H2.4 "verification standard" framing is genuinely differentiated.** The six-item checklist (live capture + liveness + clothing + AI-derived weight + self-report cross-check + audit-ready evidence) is the core defensible angle and it lands cleanly. This is the section that will get quoted.
2. **Compliance block (L100) is exemplary.** TLS, SSE-S3, retention policy, auto-blur, no PII — all sourced, all in one paragraph, no hedging. This is the answer a Head of Compliance can forward to procurement as-is.
3. **Katerina voice is preserved without copying her LinkedIn posts.** Re-tells the ChatGPT/Gemini experiment without lifting her sentences. The "trouble is not the patient. The trouble is the method." cadence (L39) is faithful to the anchor posts without being a copy-paste.

## Top 3 issues (minor polish items, score ≥ 18)

1. **L92 "Most online pharmacies deploy FitXpress in what we call Pattern B"** — over-reaches the sample size. Rephrase to "The most common deployment pattern for this use case is Pattern B…" Same point, no implicit customer-count claim.
2. **Spelling consistency:** "defence" L98 vs. "defensible/defensibility" elsewhere. Pick UK or US and apply uniformly.
3. **CTA mailto at L125** — confirm with Vadim whether a demo-request form or Calendly is preferred before CMS paste. The publish-package already flags the demo URL as TBD; this is the natural moment to resolve it.

## Coordinator review

(заполняется Claude в чате после автозапуска QC)
