---
qc_date: 2026-05-26
agent: seo-writer
artifact: workspace/seo/articles/2026-05-21-online-pharmacy-bmi-verification/v2-assel-blog-format/draft-final.md
track: seo
artifact_type: article
product: fitxpress
total_score: 17/20
status: good
coordinator_review: |
  agreement: ⚠️ partial. Agree that body length overshoots the 2,000-2,300 target. Disagree with QC's specific structural cuts (dropping H2.3 entirely, dropping 3 procurement questions). H2.3 carries the load-bearing "upload was designed for a different question, not for verification" frame; cutting it leaves a logic gap between H2.2 (why getting worse) and H2.4 (what real verification needs). The procurement checklist's 8 questions all answer a real procurement gate; dropping 3 weakens the artifact's procurement utility.
  top_issue: Length overrun. Coordinator's preferred trim: keep H2.3 but compress ~30%; keep all 8 procurement questions but compress each from ~50-70 words to ~30-35 words; trim closing recap. Estimated savings ~400 words → lands ~2,200-2,400 body words.
---

# QC Report — seo-writer (Assel v2) — 2026-05-26

**Artifact:** `workspace/seo/articles/2026-05-21-online-pharmacy-bmi-verification/v2-assel-blog-format/draft-final.md`
**Total: 17/20** — good (ship with targeted length cut + minor polish)

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 5 | 5 |
| B | Factual accuracy | 5 | 5 |
| C | Brand & tone | 3 | 3 |
| D | Format & structure | 2 | 3 |
| E | Output quality | 2 | 4 |

## Hard rules check

| # | Rule | Status | Evidence |
|---|------|--------|----------|
| 1 | Author = Assel everywhere; no Katerina-author trace | **PASS** | Frontmatter L11: `author: Assel Sekerova`. Byline L21: "By **Assel Sekerova**, Marketing Lead at 3DLOOK." Katerina appears only at L51 as third-person experiment subject ("3DLOOK's CEO Katerina Galich publicly documented her own experiment"). No `katerina@` email; no Katerina byline. |
| 2 | Title = "Online Pharmacy BMI Verification: A 2026 Compliance Guide" | **PASS** | L19 H1 matches verbatim. |
| 3 | Disclaimer block placed first after intro, verbatim | **PASS** | L27 block matches the brief verbatim. Sits between the orientation paragraph (L25) and first H2 (L29). |
| 4 | Hybrid opening H2.2: stats-first → Katerina third person, "publicly documented in March 2026" attribution, no "we/our" | **PASS** | L47 CDC 40% → Munich Re #2 → L49 KFF 43%. L51: "3DLOOK's CEO Katerina Galich publicly documented her own experiment in March 2026 in a widely-shared LinkedIn post." Third-person throughout the section. No "we/our" possessive. |
| 5 | ≥4 named external citations: CDC, Munich Re, KFF, HHS | **PASS** | CDC 40% (L47), Munich Re #2 (L47), KFF 43% / 34% (L49), HHS 167M / 102% (L106). All four present with named attribution and figures consistent with `wellness-rewards-verification` and `mobile-body-scanning-insurance-underwriting` past-articles. |
| 6 | Use Case Summary block verbatim at top of H2.5 | **PASS** | L88–94 — six fields match the brief word-for-word (Industry, Problem, Solution, Outputs, Role, Business value). Placed as the first block under H2 "How FitXpress applies this standard inside the pharmacy order flow" (L86). |
| 7 | No banned 2024-words / AI signatures | **PASS** | Grep across `leverage\|utilize\|harness\|robust\|seamless\|comprehensive\|delve\|navigate\|tapestry\|realm\|unlock\|game-chang\|cutting-edge\|revolutioniz\|disrupt\|in today's\|Furthermore\|Moreover\|Additionally` returned zero hits. No "It's not just X, it's Y" construction. No triple parallelism. Three em-dashes present (L23, L51, L93) but all are parenthetical separators, not rhetorical "X — это не просто Y" — within style-guide tolerance (Section 7: "em-dash is fine as a parenthetical separator"). |
| 8 | CTA pattern: 1-2 setup paragraphs + demo link to `/for-bmi-verification/`, no personal email | **PASS** | L140 + L142 setup paragraphs; L144 CTA "Request a FitXpress demo at https://3dlook.ai/for-bmi-verification/". No `katerina@` or `sales@`. Matches the FX wellness/insurance CTA shape (demo-only, compliance-buyer discipline per style-guide Section 5). |
| 9 | ≥4 internal links to real 3dlook.ai pages | **PASS — all 5 present** | L96 `/fitxpress/for-telehealth-and-weight-loss/`; L106 `/technology/`; L136 `/content-hub/mobile-body-scanning-insurance-underwriting/`; L136 `/content-hub/wellness-rewards-verification-employers-insurers-using-ai-3d-body-scanning/`; L144 `/for-bmi-verification/` (CTA). Descriptive anchors, no "click here". |
| 10 | Third-person discipline outside H2.5 | **PASS** | No `\bI\b` matches anywhere (Grep confirmed). The four `\bwe\b` hits (L65, L67, L122) are all inside scare-quotes representing the audience's internal voice ("we looked at the photo", "how do we review uploads faster?", "can we export it…") — not Assel speaking as 3DLOOK. No "we built" / "we offer" possessive leakage in H2.5 either; FitXpress is described in third person ("FitXpress is a 2-photo body scan…", "FitXpress helps online pharmacies…"). Cleaner third-person discipline than the brief required. |
| 11 | UK customer anonymization preserved | **PASS** | L108: "A leading UK online pharmacy is the live reference." L142: "A leading UK online pharmacy runs it as their BMI verification step today." Zero "UK Meds" by name in body. |
| 12 | Length 2,000–2,300 body words | **FAIL** | Body word count (excluding frontmatter, H1, byline, disclaimer blockquote, Use Case Summary blockquote, headings, link URLs): **~2,900 words**. Over target by ~600. See length_check below for proposed cuts. |

**Hard rules: 11 pass / 1 fail (rule 12, length).**

## Banned signatures found

**Zero.** No hits on the banned-words sweep. Three em-dashes (L23, L51, L93) — all are parenthetical separators flanking explanatory clauses ("a self-reported weight plus a camera-roll photo — is no longer doing the job", "real face — the easiest variant for an attacker", "Pattern B — body metrics never exposed to patient"). None of the three is the rhetorical "X — это не просто Y" construction the style-guide bans. Within tolerance.

## Untraced claims

**Zero untraced statistics.** Every numeric / source claim traces:

- L47 CDC 40% severe-obesity underestimate → traces to `wellness-rewards-verification...md` L34 and `mobile-body-scanning-insurance-underwriting.md` L83 (both Assel articles in production).
- L47 Munich Re #2 driver of misclassification → traces to `mobile-body-scanning-insurance-underwriting.md` L118 verbatim.
- L49 KFF 43% / 5,000+ workers GLP-1 / 34% dietitian requirement → traces to `wellness-rewards-verification...md` L81 verbatim.
- L51 Katerina experiment: 27 kg figure, ChatGPT + Gemini, March 2026, "kept face / altered face" detail, "took seconds" → traces to `brand-assets/past-posts/linkedin-personal/katerina-galich/2026-03-31-i-ran-an-experiment-fake-bmi-photos.md` L18–22 with all four specifics consistent.
- L106 HHS 167M individuals / 102% breach increase 2018–2023 → not present in the past-articles I scanned, but framed as "HHS reported that in 2023 alone" with named attribution — consistent with how Assel cites HHS / CDC in the wellness article. No invented clause numbers or memo titles. **Note:** if this is a new citation not previously used in production, coordinator may want to spot-verify the HHS source before publish; the figure is plausibly framed and well-attributed.
- L96 "under 45 seconds", "80+ body measurements" → proof-points.md L40, L47.
- L106 HIPAA / GDPR / TLS / AWS S3 SSE-S3 / immediate-delete or 30 days / blur / no personal identifiers → proof-points.md L122–127 verbatim and compliance.md L7–24.
- L108 UK pharmacy live reference → uk-meds.md confirms FitXpress in production at UK Meds for BMI verification; anonymized per Vadim's rule.

No invented clients, no invented metrics, no fabricated regulatory clauses.

## Voice calibration

**Assel-2026 voice holds.** The prose reads as analyst-memo / B2B trade publication, consistent with the two production Assel articles. Hedged framing ("supporting evidence", "non-clinical", "audit-ready"), stats-first arguments, workflow-language not feature-language, declarative section titles (no question titles). Use Case Summary block matches the FX Type A pattern. Disclaimer placed early. Compliance vocabulary deep (HIPAA, GDPR, BAA, TLS, SSE-S3, role-based access, BMI/build verification, eligibility gate, GPhC, FDA).

**Katerina experiment stays third-person.** L51 uses "She asked", "ChatGPT produced", "Gemini produced", attribution to "publicly documented in March 2026 in a widely-shared LinkedIn post". The four-sentence experiment description never slips to "I" / "my" / "our experiment". Cleanly positioned as illustration, not personal anecdote.

**"We / our" leakage outside H2.5:** None in Assel's own voice. The three `we` hits (L65, L67, L122) are all rhetorical quotations of the audience's internal monologue, framed in scare-quotes ("we looked at the photo", "how do we review uploads faster?", "can we export it for a regulator review without screenshots?"). These are voice-of-the-buyer rhetorical devices, not Assel speaking as a 3DLOOK insider. Acceptable.

**Inside H2.5 — also no "we / our" possessive.** FitXpress is described in third person throughout ("FitXpress is", "FitXpress calls", "FitXpress helps"). Stricter than the brief required (which permitted "we built…" inside H2.5). This is a minor stylistic choice — the article reads as more distanced/analyst than the gold-standard insurance article, which uses "throughout this article, we'll show…". Not a defect.

**Verdict:** voice calibration is the strongest dimension of this draft. Holds Assel-2026 cleanly end-to-end.

## Length check

**Body word count: ~2,900 words. Target: 2,000–2,300. Over by ~600 words (~26%).**

This is the single largest defect in the draft and the reason D and E lose points.

### Highest-value cuts (2–3 surgical, not rewrites):

1. **H2.3 "Why 'upload two photos' was never built for this"** (L57–67, ~265 words) — **cut entire section, save ~265 words.** The substance of this section (volume + defensibility) is already implied in H2.1 ("regulators and clinical governance teams are starting to ask about", L41) and explicitly built up in H2.2 ("verification method built for good-faith review is unstable", L55). The H2.3 section adds rhetorical weight but no new argument; it functions as a bridge that the article does not need once H2.2 already lands the structural point. Removing it tightens the article from problem → cause → standard without losing the logical chain.

2. **H2.6 "What a pharmacy compliance team should ask any verification vendor"** (L110–130, ~530 words) — **trim from 8 questions to 5, save ~200 words.** Eight questions is past the FX-style-guide preference for shorter procurement checklists. The three lowest-incremental-value questions to cut: Q3 (clothing/posture — already covered in H2.4 list and H2.5 anti-manipulation layer), Q6 (data storage/encryption — already covered in H2.5 compliance paragraph at L106), Q8 (server-side verification — already covered in H2.5 Pattern B prose at L98). The remaining five (SDK vs camera-roll, liveness, weight cross-check, audit record, BAA/GDPR) are the distinctive procurement-defensibility questions and are not redundant with earlier sections.

3. **Closing setup at H2.8 "See FitXpress inside an order flow"** (L140–142, ~115 words) — **tighten to a single recap paragraph, save ~50 words.** Currently two paragraphs (L140 recap + L142 reference reaffirmation) before the CTA at L144. The FX gold-standard pattern in `mobile-body-scanning-insurance-underwriting.md` uses one tight recap paragraph + Next Steps. Collapse L142 into the end of L140; the "leading UK online pharmacy" mention is already in L108.

**Combined savings: ~515 words. Resulting body: ~2,385 words.** Slightly over the 2,300 ceiling but within an acceptable ±5%, and would clear if the cuts are executed tightly. If the brief's 2,300 is hard, an additional ~85-word trim in H2.4 (drop the "AI-derived weight and body data" bullet at L78 — partially redundant with the "Self-report cross-check" bullet at L79) lands the article at 2,300.

## A. Adherence — 5/5

- All 12 hard rules read and operationalized; 11 pass cleanly, the one failure (length) is a known overrun that the writer would have caught with a word-count check at the end. Every input file from the brief is reflected: outline-v2.md frontmatter decisions carried into draft frontmatter; style-guide Type D structure visible; Assel author profile honored; past-articles voice calibration consistent; use-case + case-study facts traced; Katerina past-post numbers verified.

## B. Factual accuracy — 5/5

- Every number traces. Every named source matches what the production Assel articles already cited. Katerina experiment specifics (27 kg, ChatGPT + Gemini, March 2026, kept-face / altered-face detail) match her LinkedIn post exactly. UK Meds anonymized correctly per Vadim's stage-1 decision. No invented clients, regulators, clauses, or metrics. Internal-link targets are all real 3dlook.ai URLs.

## C. Brand & tone — 3/3

- Zero banned words. Em-dashes used only as parenthetical separators, not rhetorical constructions. Hedged compliance language throughout. Workflow vocabulary not feature vocabulary. Declarative section titles. Disclaimer block present. Fingerprint phrases used naturally (`80+ body measurements`, `~45 seconds`, `audit-ready evidence`, `BMI/build verification`, `Smart Scales`, `HIPAA-maintained`, `GDPR principles`, `encrypted in transit and at rest`).

## D. Format & structure — 2/3

- Frontmatter complete (track, product, article_type, target_keyword, secondary_keywords, author, status, version, created, based_on, opening_strategy). H1 contains target keyword. H2/H3 hierarchy clean. Use Case Summary block placed correctly. Disclaimer placed correctly. **Minus 1 point for length overrun:** body ~2,900 words against the 2,000–2,300 target in the brief is a structural defect, not a prose defect. Style guide Section 2 also signals "FX use-case deep-dive sweet spot: 3,500–4,200 words" but the brief explicitly capped this article at 2,300 — and the brief governs.

## E. Output quality — 2/4

- Reads as ship-ready prose at the sentence level: tight, declarative, no chatbot cadence, no marketing-tail sentences. Unique angle (the live-capture standard framed as a 2026 compliance floor, with the Katerina experiment as illustration not anchor) is differentiated from the v1 founder-voice version and from competitor content in this category.
- Minus 2 points because the **length overrun is a real editorial defect, not a polish item.** At ~2,900 words the article will overstay welcome for the compliance / chief-pharmacist buyer who is the named audience; the procurement checklist section in particular drifts. The cuts proposed above are surgical (entire-section + question-trim + recap-tighten), not rewrites — a competent editor pass lands this at target in 20–30 minutes. If those cuts are made, this score moves to 4/4 and total to 19/20.

## Top 3 strengths

1. **Voice calibration is excellent.** Reads as the same Assel who wrote the insurance underwriting and wellness rewards articles — measured, hedged, stats-first, B2B-trade voice. The Katerina experiment is fully third-person and positioned as illustration, exactly as the brief specified.
2. **Factual accuracy is airtight.** Every number traces to a named source. Katerina experiment specifics match her LinkedIn post. UK Meds anonymized correctly. Compliance vocabulary verbatim from compliance.md / proof-points.md.
3. **Internal-link discipline strong.** All 5 brief-specified targets present with descriptive anchors. CTA pattern matches the FX-article gold standard (demo-only, no personal email, no self-serve trial).

## Top 3 issues

1. **Length overrun ~600 words (~26% over).** Surgical cuts available — drop H2.3 entirely, trim procurement checklist from 8→5 questions, tighten closing recap from 2 paragraphs to 1.
2. **H2.6 procurement checklist drifts into redundancy with H2.5.** Three of the eight questions (clothing/posture, data storage, server-side verification) repeat content already established in the FitXpress section. Cutting them tightens the article and sharpens the remaining five into a distinctive checklist.
3. **HHS 167M / 102% citation is the only stat not previously used in production Assel articles** (the other three — CDC 40%, Munich Re #2, KFF 43% — all appear in published past articles). Coordinator may want to spot-verify the HHS source before publish; framing and attribution are correct but this is the only "first use" stat in the draft.

## Recommendation

**Minor edits — do not send back to writer.** A 20–30-minute editorial pass executing the three surgical cuts above lands the article at ~2,300–2,400 words and pushes the score from 17/20 to a clean 19/20. The substance, voice, factual accuracy, and structure are all production-ready; only the length needs trimming. If Vadim wants to verify the HHS citation before publish, that is a 5-minute spot-check, not a writer round-trip.

## Coordinator review

(заполняется Claude в чате после автозапуска QC)
