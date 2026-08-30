# Log — remote-body-measurement-online-fitness-coaching

## 2026-08-26 — Write stage completed (seo-writer)

- **Artifact:** `draft-v1.md` (full article, 12-section outline per plan.md, H2.1–H2.12 + short intro + scope note).
- **Word count:** ~2,680 (approximate).
- **Author byline:** Assel Sekerova (default).
- **Claims used:** FX-001, FX-002, FX-003, FX-005, FX-006, FX-007, FX-008. FX-004 (ISO 8559-1:2017 benchmark) deliberately NOT used — plan did not call for it and it must never be combined with FX-001/003 (different reference method).
- **Internal links placed:**
  - up → AI in Fitness hub (`/content-hub/ai-in-fitness-industry/`) in H2.3.
  - trust → accuracy framework (`/content-hub/mobile-body-scanning-accuracy/`) in H2.2 and H2.10.
  - down → BOFU product page (`/fitxpress/for-connected-and-digital-fitness/`) as soft MOFU evaluation link after H2.6 and as direct BOFU CTA in the conclusion.
  - sideways → **omitted** (see open items #3 below).
- **Self-check (grep):** no em dash, no banned words (leverage/utilize/harness/robust/seamless/comprehensive/delve/tapestry/realm/unlock/etc.), no "positioned as", no "by hand", no "objective" about our tech, no named competitors, no banned claims. The only matches for diagnose/eligibility/underwriting terms are inside the boundary section (H2.7), the scope note, and the reframe contrast in H2.2 — all correct usages, no asserted claims.

### Deviations / open items flagged for review

1. **Word count vs plan estimate (deviation).** plan.md article-meta estimates ~2,000 (range 1,900–2,300) and asks for the shorter end, but the sum of the per-section word-count targets in the outline is ~2,970 (mins) to ~4,130 (maxes). The two figures are arithmetically incompatible. I prioritized the per-section must-cover depth and wrote toward the lower end of each section, landing ~2,680. This is above the stated ~2,300 ceiling but below the section-target sum, and still within the corpus norm (blog-style-guide §2 floor is 2,000). Editor/Vadim to confirm whether to trim toward 2,300 (would require dropping must-cover content) or accept ~2,680.
2. **Difficulty is TBD** for the head term (Ahrefs returned null) — carried from plan Open items #2, unchanged at write stage.
3. **Sideways internal link omitted.** Per plan Open items #6 and the vertical-boundary guardrail, the only live sideways candidate is the GLP-1 tools list (different vertical). I did not link it to avoid blurring the Fitness/GLP-1 boundary. Article ships with up/down/trust links only. Confirm whether to hold a slot for the planned "Smart Scale vs AI Body Scan" / "GLP-1 and Fitness Apps" siblings once written.
4. **No named fitness-coaching customer** exists in proof-points (plan Open items #3). Draft uses capability + segment framing with no named customer, as planned.
5. **BOFU URL path debt** (plan Open items #4): `/fitxpress/for-connected-and-digital-fitness/` is flagged in CLAUDE.md §16 as using a non-existent path level with a redirect breadcrumb. URL kept as written in content-plan.md/plan.md; confirm canonical URL before publish.
6. **Central Privacy/Regulatory FAQ not live** (plan Open items #5): privacy handled as a short practical note (H2.5, H2.10, FAQ #6); no dead link inserted.

### Next step
Draft ready for `seo-editor` (Pass 3b strategy compliance, Pass 3c detector, Pass 4 terminology-guardrails full pass).

## 2026-08-26 — Edit stage completed (seo-editor)

- **Artifact:** `draft-v2-final.md` (edited, status: edited). Feeds directly to publish (no checkpoint between edit and publish).
- **Body word count:** ~2,525 prose words (2,599 from H1 to end minus 72 claim-comment tokens; frontmatter `word_count: 2525`). Down from v1's ~2,640 prose.
- **detect-ai-tells.py (channel article), actual final output:**
  `SEO / blog article · en · 2646 words / AI density: 0.0/1000 (budget 6.0) -> low / VERDICT: CLEAN`
  (baseline on draft-v1 was `1.08/1000`, VERDICT `HARD FAILS (1)` — anthropomorphism "platform decides").

### Pass-by-pass

- **Pass 1 — citation dedup.** The accuracy-framework trust link (`/content-hub/mobile-body-scanning-accuracy/`) was linked twice in v1 (H2.2 and H2.10). Kept one anchor in H2.2; H2.10 now says "as the accuracy framework sets out" without re-linking (also avoids the positional "linked above"). BOFU down-link kept in two spots (H2.6 soft MOFU eval + conclusion BOFU demo) — plan-sanctioned CTA placement, not a dup. Verified link inventory: up ×1, trust ×1, down ×2.
- **Pass 2 — structure & flow.** Intro already lands the pain in two sentences; wove the primary keyword into the second intro sentence and into the H2.1 heading so it appears in H1 + first paragraph + one H2 + body (4 occurrences total). No Furthermore/Moreover/Additionally transitions. Conclusion is actionable (next step + two CTAs).
- **Pass 3 — expert voice.** Fixed the anthropomorphism hard fail ("the platform decides" -> "the platform team decides how to use it"). Converted H2.6 from a bold-headed checklist to prose so it no longer clones H2.10's checklist (two identical lists back-to-back was the main "template" tell). Removed ungrammatical keyword-stuffed phrases ("client retention online coaching", "visible progress coaching", "body composition tracking for coaching") and rewrote naturally. Kept/sharpened the stated positions (the "accurate enough for which decision?" reframe; the "not the right tool for every practice" call).
- **Pass 3b — strategy compliance.** No banned positioning claim; boundary section H2.7 present and direct. Vertical boundary held (GLP-1 appears only inside the boundary statement; no wellness-rewards bleed). Narrow coaching-workflow angle held (no hub-overview duplication). Internal links up/down/trust present; sideways deliberately omitted (plan Open item #6, avoids Fitness/GLP-1 boundary blur). FAQ (7 items) intact; CTA-by-intent (MOFU eval + BOFU demo) intact.
- **Pass 3c — detector + self-check.** Ran the detector twice mid-edit (caught a fresh anthropomorphism "body data feels current" introduced by a trim, rewrote it), final run CLEAN 0.0/1000. Self-check written into the artifact `self_check` field.
- **Pass 4 — terminology & polish.** Expanded BMR, CTO, HIPAA, GDPR, and SSE-S3 at first use (matching the house convention in `online-pharmacy-bmi-verification.md`); BMI kept bare per the 2026-08-25 override. Removed two "so"-as-result connectors in H2.6. Removed corrective negations: the "with real clients, not staff" line (-> "under real conditions"), the "is noise, not progress" line (-> positive "only a larger move should read as progress"), the "repeatability, not one-off variation" line (-> "base thresholds on measurement repeatability"), and the FX-006 "software estimate, not a reading from a physical scale" clause (-> "a software output read from the images"). Split the one stacked negation in H2.7 (GLP-1 + qualification) into a positive frame for the qualification half. Removed em dashes from the frontmatter notes as well (body had none).

### Verification (all pass)
- No claim outside the approved list: only FX-001, FX-002, FX-003, FX-005, FX-006, FX-007, FX-008 used.
- **FX-004 absent** (grep for ISO 8559 / 0.40 cm / multi-company / 14 companies / 1,152 all negative) — not combined with FX-001/003.
- **Repeatability written as "< 1 cm"** in all 4 occurrences.
- **No named competitors** (Prism / Bodygram / Size Stream all absent).
- **Vertical boundary held** — no GLP-1-clinical or wellness-rewards claims outside the boundary statement.
- **"FitXpress is not a medical device"** stated directly (scope note + H2.7), never "positioned as".
- Internal links correct per context-pack: up (`/content-hub/ai-in-fitness-industry/`), trust (`/content-hub/mobile-body-scanning-accuracy/`), down (`/fitxpress/for-connected-and-digital-fitness/` ×2).
- Zero em dashes; zero banned words; no "positioned as" / "by hand" / "plus"-stacking / "objective"-about-our-tech / "so"-as-result-connector in the body.

### Open items carried to publish
1. **Word count vs plan ceiling (editorial call, resolved toward quality).** Final body ~2,525 prose words. This sits inside the context-pack's stated "1,800-2,800 typical for a P1 supporting article in this hub" band, and modestly above the plan's soft 2,300 ceiling. Trimmed ~115 prose words from v1 (duplicated retention/recomposition + a redundant privacy line) without cutting any FAQ item, the boundary section, or any approved claim. Held here deliberately rather than stripping must-cover content, per the writer's flagged plan/section arithmetic conflict (open item #1 above). Publisher/Vadim can request a further trim to <=2,300 if the plan ceiling is hard, but it would mean cutting must-cover depth.
2. **BOFU URL path debt** (plan Open item #4): `/fitxpress/for-connected-and-digital-fitness/` flagged in CLAUDE.md §16 as a non-existent path level with a redirect breadcrumb. URL kept as written in content-plan.md; **confirm the canonical down-link URL before publish.**
3. **Central Privacy/Regulatory FAQ not live** (plan Open item #5): privacy kept as a short practical note (H2.5 + H2.10 + FAQ), no dead link inserted.
4. **Sideways internal link still omitted** (plan Open item #6): ships with up/down/trust only; hold a slot for the planned "Smart Scale vs AI Body Scan" / "GLP-1 and Fitness Apps" siblings once written.
5. **Head-term difficulty still TBD** (plan Open item #2): Ahrefs returned null; unchanged at edit stage.

### Next step
`draft-v2-final.md` ready for `seo-publisher` (meta generation + final checklist, incl. its own detector re-run and the BOFU-URL confirmation).

## 2026-08-26 — Publish stage completed (seo-publisher)

- **Artifact:** `publish-package.md` — meta title/description (3 variants each), full 15-point SEO checklist,
  9-point strategy checklist, all open items carried forward explicitly, alt-image suggestions, full CMS-ready
  article body.
- **detect-ai-tells.py re-run by me, not cited from the editor.** Ran
  `python3 brand-assets/style-guides/scripts/detect-ai-tells.py workspace/seo/articles/2026-08-26-remote-body-measurement-online-fitness-coaching/draft-v2-final.md --channel article --summary`
  directly via Bash (no permission issue — the `settings.json` fix from earlier on 2026-08-26 held).
  Result: `2646 words · AI density 0.0/1000 (budget 6.0) -> low · VERDICT: CLEAN`. Also ran the non-summary
  JSON form: `hard_fails: [], house_rule_violations: [], em_dashes: 0, punch_triad_count: 0`. This confirms
  the editor's Pass 3c number rather than assuming it carries over.
- **Recommended meta title (57 chars):** "Online Fitness Coaching Programs: Remote Body Measurement" —
  front-loads the actual SEO head term (100/mo, US); 2 alt variants provided, including the exact
  content-plan.md/H1 phrasing as an option if title/H1 consistency is preferred over front-loading.
- **Recommended meta description (154 chars):** "Coaches can't tape-measure remote clients. See how a
  guided smartphone scan gives online fitness coaching programs structured progress data clients trust."
  2 alt variants provided.
- **SEO checklist: 14/15 pass.** One flagged deviation: word count (2,525 prose words vs plan's stated
  ~2,000/1,900-2,300 estimate) — already an editorial call documented by writer and editor, not newly
  discovered, carried forward explicitly rather than silently accepted.
- **Strategy checklist: 8/9 pass.** One flagged deviation: sideways internal link omitted (deliberate,
  to avoid a Fitness/GLP-1 vertical-boundary blur — the only live sideways candidate is off-vertical and
  the two planned siblings are not yet written).
- **No STOP triggered.** Two single-item deviations across two separate checklists, both below the ≥2-❌
  threshold per checklist, neither in the positioning/compliance/cannibalization auto-stop category.
- **Zero third-party/external sources confirmed** — all 4 links are internal `3dlook.ai` URLs (up, trust,
  down ×2). Flagged explicitly per the 2026-08-26 CLAUDE.md finding that this caps quality-controller's
  category B score, so it reads as a declared fact rather than an oversight if `quality-controller` runs
  on this package next.
- **All open items from the write/edit stages carried forward verbatim** into publish-package.md §4: word
  count vs ceiling, BOFU URL path debt (`/fitxpress/for-connected-and-digital-fitness/`, CLAUDE.md §16),
  sideways link omission, central Privacy/Regulatory FAQ not live, head-term difficulty TBD, thin-demand
  checkpoint-1 decision, zero external sources. The TBD dependency is declared in the package itself, per
  the 2026-08-26 CLAUDE.md note that an undeclared TBD caps quality-controller's category A score.
- **Minor judgment-call note, not a fail:** one residual "so" in the Implementation section (capture-
  protocol bullet) reads as an imperative recommendation following a claim, not the detector's narrowly-
  scoped benefit shape. Flagged for editorial awareness in publish-package.md §2, not treated as a hard
  fail since the mechanical detector correctly did not flag it.

### Status
Article is now at **checkpoint 2** — text + meta together, awaiting Vadim's approval in Telegram. No
further pipeline action until that approval; publishing to the CMS is manual (Vadim or via API), per
CLAUDE.md §10.
