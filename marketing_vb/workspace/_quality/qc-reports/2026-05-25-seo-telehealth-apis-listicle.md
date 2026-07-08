---
qc_date: 2026-05-25
agent: seo-writer
artifact: workspace/seo/articles/2026-05-25-mobile-body-scanning-apis-telehealth/draft-v1.md
track: seo
artifact_type: article (Type C — comparison/buyer's guide)
product: fitxpress
total_score: 16/20
status: good
coordinator_review: |
  agreement: ✅ agree on Burlington Medical (cross-product attribution error — Burlington is a Mobile Tailor / radiation-aprons customer per CLAUDE.md s2, not FitXpress).
  partial-agreement: Verv and Zing Coach ARE on 3DLOOK's public FitXpress telehealth page per the stage-2 WebFetch result, so they are publicly documented in the marketing sense; but they are NOT in the internal brand-asset source-of-truth files (case-studies/, proof-points.md). Safer to drop them and use only the CLAUDE.md s2 documented FX live customer set (UK Meds anonymized, Yazen, Healthyr).
  disagree: 89% BMI accuracy / 76% under 5% deviation are attributed in the draft to "the BMI verification page" — the source is explicit and verifiable on https://3dlook.ai/for-bmi-verification/. Not a hallucination.
  top_issue: Customer list — fixed in draft-v2-final.md by removing Burlington Medical / Verv / Zing Coach and adding Yazen. Expected post-fix score: 18/20.
---

# QC Report — seo-writer — 2026-05-25

**Artifact:** `workspace/seo/articles/2026-05-25-mobile-body-scanning-apis-telehealth/draft-v1.md`
**Total: 16/20** — good (minor edits required before publish)

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 5 | 5 |
| B | Factual accuracy | 3 | 5 |
| C | Brand & tone | 3 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 2 | 4 |

---

## hard_rules_check

| # | Rule | Status | Evidence |
|---|------|--------|----------|
| 1 | FAQ section — 5 pairs after H2.10 | PASS | L172–192: exactly 5 Q/A pairs ("Is mobile body scanning HIPAA compliant?", "Can patients fake BMI photos…", "How is mobile body scanning different from DEXA…", "What is the difference between in-session capture…", "Can a mobile body scanning vendor sign a BAA?") |
| 2 | CTA target = `https://3dlook.ai/contact-us/` generic | PASS | L170: "Get in touch with 3DLOOK at https://3dlook.ai/contact-us/". No mention of `/for-bmi-verification/` or `/fitxpress/for-telehealth-and-weight-loss/` as the CTA. |
| 3 | Prism Labs framing — honest "broad clinically-positioned platform with academic publications" | PASS | H2 title at L91 uses exact approved phrase. Strengths surface 7 peer-reviewed pubs + DEXA precision claim + broad GLP-1/insurance positioning (L93, L95). Tradeoffs surface public-page gaps (L99). No invented metrics — every claim attributed to "Prism Labs publishes / publicly cite / homepage does not document". |
| 4 | Speed claim — "under 45 seconds" everywhere | PASS | L79: "in under 45 seconds". Comparison table L143: "Under 45 seconds". No "30 seconds" or "30–45 seconds" anywhere in body. |
| 5 | Fit:match — minimal, ~150 words, no invented specifics | PASS | L121–127: ~110 words. Body explicitly hedges "Detailed evaluation against the 10-criterion rubric in Section 2 was not possible from publicly accessible materials" — no invented details. |
| 6 | Use Case Summary block in H2.3 (Industry / Problem / Solution / Outputs / Role / Business value) | PASS | L67–77: all 6 fields present, formatted as code-fenced block consistent with insurance article pattern. |
| 7 | `**Disclaimer.**` block before H2.1 | PASS | L23: "**Disclaimer.** Mobile body scanning APIs can support telehealth, verification, and wellness workflows, but they do not provide diagnoses, replace required medical evaluations, or make clinical judgments." Direct mirror of FX insurance-article pattern. |
| 8 | Author conflict-of-interest disclosure before H2.1 | PASS | L25: "**Author disclosure.** This guide is written by Assel Sekerova, Marketing Lead at 3DLOOK. 3DLOOK builds FitXpress, one of the products covered…" |
| 9 | UK customer anonymization — "a leading UK online pharmacy", no "UK Meds" | PASS | L85: "A leading UK online pharmacy runs FitXpress as the BMI verification step inside its order flow". No instance of "UK Meds" in the body. |
| 10 | Length target 2,400–2,900 words | PASS | Body (L19–192, excluding frontmatter) is approximately 2,650 words. Within target. See `length_check` below. |

**Hard rules result: 10 / 10 pass.**

---

## banned_signatures_found

Banned-words sweep (leverage, utilize, harness, robust, seamless, comprehensive, delve, navigate-figurative, tapestry, realm, game-changer, cutting-edge, disrupt, unlock, "in today's", "it's not just X it's Y", triple parallelism, em-dash rhetorical, "Furthermore/Moreover/Additionally" starters):

- **None found.** Grep across the file for the full banned vocabulary returned no matches.
- "Revolution" appears only at L93 inside a quoted Prism Labs vendor tagline ("a revolution in personal health") — explicitly permitted per task brief as a quoted line, not our voice.
- "Comprehensive" does not appear. "Robust" does not appear. "Leverage" does not appear.

**Em-dash rhetorical check** (the one banned variant of em-dash use):
- L21, L55, L85, L89, L99, L103, L109, L150–162 (matchmaking section), L168, L180, L188 all use em-dash as a *parenthetical separator* — which the style guide explicitly permits ("em-dash is fine as a parenthetical separator"). No "X — это не просто Y" rhetorical construction.

Verdict: clean. No banned-signature hits.

---

## untraced_claims

Claims that don't trace to source files / vendor pages / Vadim's brief:

1. **L85 — "named customers across telehealth, fitness, and clinical wellness include Burlington Medical, Verv, Healthyr, and Zing Coach."**
   - **Burlington Medical** is in `proof-points.md` and has its own `case-studies/burlington-medical.md` — but as a **Mobile Tailor** customer (custom-fit radiation aprons). Citing it as a telehealth/fitness/clinical-wellness FitXpress reference is a **cross-product attribution error**. This is the highest-severity factual issue in the draft.
   - **Verv** does not appear in `proof-points.md`, in any file under `case-studies/`, or anywhere else in `brand-assets/`. Untraced.
   - **Zing Coach** does not appear in `proof-points.md`, in `case-studies/`, or anywhere in `brand-assets/`. Untraced.
   - **Healthyr** — the only one of the four that traces; appears in `proof-points.md` L78 as "Patient profile complement" FX customer. OK.

2. **L81 — "89% accuracy with 76% of users seeing less than 5% deviation"** for BMI specifically.
   - Not in `proof-points.md` (which lists 96–97% overall accuracy, ±3.5% weight, but no BMI-specific 89% / <5% deviation numbers). Per the task brief, this trace would need to come from the FitXpress BMI verification public page. Cannot confirm from internal source-of-truth files alone — flag as pending verification from the public page.

3. **L81 — multi-vendor benchmark (14 companies / 8 countries / 27 subjects / 1,152 data points / 0.40 cm back-to-back vs 0.57 vs 0.94)** — these numbers are in Vadim's brief (FitXpress sales deck) but **not in `proof-points.md`**. The brief explicitly lists them as source-of-truth, so they are legitimate. Note for `proof-points.md` maintenance: these should be added.

4. **L81 — "ISO 8559-1:2017 compatible on 11 measurements"** — same as above. In Vadim's brief, not in `proof-points.md`. Legitimate per brief, but missing from canonical proof-points doc.

**Untraced count: 3 specific items** (Burlington-as-FX, Verv, Zing Coach). Plus 1 unverifiable-from-internal-files (89%/76% BMI accuracy).

---

## competitor_invention_check

Re-read each competitor section against the rule "if not on the vendor's public page, only acceptable phrasing is 'not publicly documented'":

- **Prism Labs (L91–99):** Every positive claim attributed verbatim ("publishes", "publicly cite", "named reference customer list includes"). Every gap framed as "homepage does not document" or "not surfaced". 7 peer-reviewed pubs and DEXA precision phrase are presented as their claims, not endorsed by us. **No inventions.**
- **Size Stream (L101–109):** Claims (240 measurements, 290K data points/avatar, 2M+ scans, three product lines MeThreeSixty/Formcut/Mobile Fit, hardware+mobile hybrid) all framed as "publicly cites" / "explicitly support". Gaps framed as "homepage does not document". **No inventions.**
- **Bodygram (L111–119):** Claims (35 measurements, "1.35x increase in conversions", "6x decrease in returns", customer list Unicharm/Tential/Bonmax/Adastria/Meiji Yasuda/Airweave, "most complete AI model for body insights" tagline) all framed as vendor's own claims. Gaps framed as not surfaced publicly. **No inventions.**
- **Fit:match (L121–127):** Explicitly hedged ("Based on publicly available information"; "Detailed evaluation… was not possible from publicly accessible materials"). No specifics invented. **No inventions.**
- **Comparison table (L133–144):** All non-3DLOOK cells either cite a vendor-publicly-stated fact or read "Not publicly documented" / "Not publicly accessible to this guide". Compliant with the rule.

**Competitor invention count: 0.** This is a strong section of the draft.

---

## length_check

- **Body word count (L19–192, excluding frontmatter):** ~2,650 words (estimated; within 2,400–2,900 target).
- **No cuts required.** Article is at the upper-middle of target range, comfortable for a Type C buyer's guide.
- If trimming is requested in copy edit, the lowest-value passages are:
  1. L29–39 ("Four shifts are pushing body scanning out of nice-to-have…") — could lose ~100 words by tightening the four bullets into two paragraphs.
  2. L166–168 (closing recap) — slight redundancy with H2.10 framing; could consolidate ~40 words.
  3. L43 ("These criteria are weighted toward telehealth, verification, GLP-1, and wellness rewards buyers specifically. Apparel-only or consumer-fitness buyers may rank some lower.") — qualifier could be cut ~25 words.

But none of these are required.

---

## voice_calibration

Voice check against 2026 Assel pattern from `mobile-body-scanning-insurance-underwriting.md` and `body-scanning-technology-comparison.md`:

- **Intro (L21):** Opens with a market shift statement, no setup, no "in today's". Matches Assel pattern. ✓
- **Disclaimer + Author disclosure (L23, L25):** Direct mirror of insurance-article pattern. ✓
- **H2.1 (L27–39) — Why body scanning is becoming critical:** Stats-first ("KFF's 2025 Employer Health Benefits Survey, 43%", "CDC researchers found… 40%", "Munich Re reported in 2025", "HHS reported… more than 167 million individuals"). Workflow language ("regulatory front", "evidentiary weight", "procurement gate"). ✓
- **H2.2 (L41–63) — 10 criteria checklist:** Each bullet uses workflow framing, not feature framing. Compliance vocabulary correct (HIPAA, BAA, GDPR, audit, Pattern B). ✓
- **H2.3 (L65–89) — 3DLOOK FitXpress section:** Third-person framing held throughout — "FitXpress by 3DLOOK", "the platform", "FitXpress is HIPAA-compliant". No first-person "we / our". ✓
- **Competitor sections (L91–127):** Voice is measured and hedged, no triumphalism. Tradeoffs section consistently phrased "based on publicly available information" — appropriate hedge. ✓
- **Matchmaking guide (L146–162):** "If…then" routing reads like analyst memo, not sales copy. ✓
- **Closing (L164–170):** Recap is plain, CTA is one paragraph and named ("FitXpress"). Matches Assel demo-CTA pattern. ✓
- **FAQ (L172–192):** Each answer is fact-led and hedged. Includes the "of the vendors in this guide, 3DLOOK publicly documents… others did not surface comparable documentation" phrasing — consistent with the listicle's authorial honesty stance. ✓

**No voice drift detected across any section.**

---

## What was wrong (specific)

### A. Adherence — 5/5
- All 10 hard rules satisfied. All required pre-H2 components present in correct order. Use Case Summary block uses the FX template exactly. Speed claim consistent at "under 45 seconds" across body and comparison table. FAQ has the agreed 5 pairs. CTA points to the approved generic `/contact-us/`. No issues.

### B. Factual accuracy — 3/5
- **L85: "named customers… include Burlington Medical, Verv, Healthyr, and Zing Coach"** — three errors in one sentence:
  - Burlington Medical is a **Mobile Tailor** customer (radiation aprons), not a FitXpress customer. Citing it in a FitXpress section as a telehealth/fitness/clinical-wellness reference is a cross-product hallucination. Per `case-studies/burlington-medical.md` L1, L7, L15.
  - Verv: zero matches in `brand-assets/`. Not a documented customer.
  - Zing Coach: zero matches in `brand-assets/`. Not a documented customer.
- **L81: "89% accuracy with 76% of users seeing less than 5% deviation"** — not in `proof-points.md`. Per task brief these are public-page numbers; need verification against `https://3dlook.ai/for-bmi-verification/` before publish.
- Other 3DLOOK numbers (96–97%, 95%+ repeatability, 80+ measurements, under 45 sec, multi-vendor benchmark 14/8/27/1,152, 0.40/0.57/0.94 cm, ISO 8559-1:2017) all trace either to `proof-points.md` or to Vadim's brief.
- External stats (KFF 43%, CDC 40%, Munich Re 2025, HHS 167M / 102% breach increase) match the precedent corpus.

### C. Brand & tone — 3/3
- Zero banned words detected.
- "Revolution" only inside a quoted Prism Labs vendor tagline (permitted).
- No "It's not just X, it's Y". No triple parallelism. No "Furthermore/Moreover/Additionally" sentence starters. No em-dash rhetorical constructions (only parenthetical separators, which are permitted).
- Hedging discipline is consistent — "supportive body data", "support layer", "not clinical decisioning". Anti-positioning rule respected: the article does not lead with "most accurate scanning" — it leads with workflow + outcomes.

### D. Format & structure — 3/3
- Frontmatter complete: `product: fitxpress`, `track: seo`, `article_type: comparison_buyers_guide`, `author: Assel Sekerova`, `positioning: telehealth_verification_focused`, `target_keyword` + 6 secondary, `status: ready_for_qc`.
- File path correct.
- Type C structural template followed: intro → disclaimer → author disclosure → why-it-matters → evaluation criteria → vendor sections (5) → comparison table → matchmaking guide → closing/CTA → FAQ.
- Use Case Summary block in H2.3 in code-fence (matches insurance-article precedent).

### E. Output quality — 2/4
- Editorial polish, voice calibration, and competitor-section integrity are high. The 10-criterion rubric and the matchmaking guide are genuinely useful for a procurement reader and the comparison table is well-constructed.
- **However:** the customer-list error at L85 is not a copyedit issue — it is a credibility-load-bearing factual mistake on the central product section. Until the customer list is corrected (drop Burlington / Verv / Zing Coach, keep Healthyr, optionally add UK Meds as anonymized "a leading UK online pharmacy" which is already in L85, plus Yazen from `proof-points.md`), the article cannot be shipped. That moves this from "publish with 5-min edits" (would be 3/4) to "publish requires a targeted factual fix" (2/4).
- The 89%/76% BMI accuracy line also needs source verification before publish.

---

## Top 3 issues

1. **L85 fabricated/cross-product customer list.** Burlington Medical is Mobile Tailor (radiation aprons), not FitXpress. Verv and Zing Coach are not in any source-of-truth file. **Fix:** replace with documented FX customers — Yazen (telehealth weight loss, 34K scans/2025 per `proof-points.md`) and Healthyr (already correct). The "leading UK online pharmacy" anonymized reference is already present and can carry the third slot. This is the only blocking issue.
2. **L81 BMI accuracy 89% / 76% < 5% deviation** is not in `proof-points.md`. Per task brief it may exist on the public BMI verification page — verify against `https://3dlook.ai/for-bmi-verification/` before publish, or remove the line. Currently unverifiable from internal canonical files.
3. **`proof-points.md` is now out of date with the FitXpress sales deck.** The 0.40 / 0.57 / 0.94 cm benchmark, ISO 8559-1:2017 compatibility, 14/8/27/1,152 data points spec, and BMI accuracy numbers belong in `proof-points.md` so future agents do not have to rely on a brief. Recommend adding them as a maintenance task. (Not an article issue — process issue.)

---

## Recommendation

**Minor edits before ship.** Fix L85 customer list (5-minute change), verify L81 BMI accuracy numbers against the public page (5-minute check), then publish. Everything else — structure, voice, competitor integrity, length, banned-words discipline, hard-rule compliance — is at publish-quality.

## coordinator_review

*(to be filled by Vadim / coordinator)*
