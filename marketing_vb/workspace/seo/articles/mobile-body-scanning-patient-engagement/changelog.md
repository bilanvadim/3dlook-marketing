# Changelog — mobile-body-scanning-patient-engagement (Phase 2 edit)

From `draft-v1-writer.md` → `draft-v3-edited.md`. Concrete before/after changes:

## Pass 1 — Citation dedup
- Trimmed internal-link anchors from 12 instances to 10 (10 distinct plan-mandated targets kept).
- Deduped accuracy framework link: kept in H2.4, removed the duplicate in H2.10. Before: H2.10 "The [mobile body scanning accuracy](…) framework sets out how capture protocol affects the numbers." → After: "Capture protocol shapes the resulting numbers, so protocol discipline belongs in the rollout plan." (no duplicate link).
- Deduped legal/privacy link: kept in H2.7, removed the duplicate in H2.10. Before: H2.10 "The [privacy and data-handling terms](…) cover retention and deletion options." → After: "Retention and deletion options follow the client's policy, as set out in the privacy note above." (no duplicate link).
- Both external H2.3 PMC citations left untouched (telehealth-utilization + GLP-1 discontinuation).

## Pass 2 — Structure & flow
- Broke monotone rhythm in H2.9: two of four paragraphs no longer open "In [vertical]…".
  - Before: "In wellness and coaching programs, visible progress supports engagement…" → After: "Wellness and coaching programs use the same visible progress to support engagement…"
  - Before: "In remote patient monitoring, a reproducible body record supports longitudinal check-ins…" → After: "Remote patient monitoring depends on a reproducible body record for longitudinal check-ins…"

## Pass 3 — Expert voice
- Removed near-banned "it is worth stating plainly." Before (H2.7): "Privacy posture matters for a compliance buyer, so it is worth stating plainly." → After: "Privacy posture is a procurement gate for a compliance buyer, so the specifics matter."
- Keyword placement: Before (H2.1) "…the repeat check-in that should drive engagement becomes a churn risk…" → After: "…the repeat check-in that should drive patient engagement becomes a churn risk…"
- Flagged (not inserted): Yazen 34,000 scans (2025) proof-point recommended for H2.7, pending Asselya approval (not in plan's H2.7 approved-claims list).

## Pass 4 — Final polish
- Fixed 1 "plus" quantifier: "80-plus measurements" → "more than 80 measurements" (H2.2); also aligns one-number consistency with body/FAQ.
- Verified 0 em dashes, 0 en dashes, 0 banned words in the article body.
- Verified all 15 abbreviations expanded at first use (AI, BMI, API, SDK, BMR, MEPS, GLP-1, GDPR, HIPAA, SOC 2, TLS, AWS, DEXA, BIA, EMR).
- Verified no stacked negation (M2) and no "<30s" sub-timing (only "under 45 seconds").
- Removed the non-published "Writer notes" meta-block from the article body (its verification content is carried into `phase2-editor-report.md`).
- Frontmatter rebuilt from the plan: added title, keywords, meta_description, hub, cluster, intent, action_type, priority: P0, existing_urls, cannibalization_guardrail, vertical_boundary; set status: edited.

## Post-editor coordinator fix (compliance accuracy — flagged by quality-controller QC on draft-v1)
- **Removed unsupported "SOC 2 where applicable" claim (3 instances: H2.7 body, H2.8 scope note, FAQ "Is this a medical device?").** `brand-assets/product-info/compliance.md` line 48 states verbatim: "We are NOT SOC 2 certified yet (in progress — confirm with Vadim before claiming)." SOC 2 is absent from `proof-points.md` and CLAUDE.md §12. This was inherited from the plan's H2.7 approved-claims list (plan.md line 185), which incorrectly listed it — flagging for the plan to be corrected so it is not re-inherited on regeneration. Replaced with the two claims that ARE substantiated: HIPAA compliance (maintained) and GDPR principles (followed).
- **Fixed "faces are obfuscated at capture" → "photos are automatically blurred when stored" (H2.7).** `compliance.md` line 21/57 and `proof-points.md` line 126 both specify blur is applied automatically at storage time, not obfuscation at capture time. Wrong mechanism and wrong timing in the writer draft.
- Both fixes applied directly to `draft-v3-edited.md` after the editor pass; `claims_verified` frontmatter list unchanged (no SOC 2 claim ID was ever registered).
