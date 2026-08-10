# Log — 2026-07-08-uk-telehealth

## Step 2: Company research (2026-07-09)

**Agent:** company-researcher (sub-agent run)
**Input:** `hypothesis.md` (status: approved), `workspace/outbound/exclusions/global-company-registry.json`, `brand-assets/product-info/icp-detail.md` (segment 1: Telehealth & GLP-1/Weight Loss).

**Tooling:** WebSearch worked without any blocking throughout this run (contrary to the flag left in hypothesis.md open questions — that flag applied to the earlier hypothesis-generation step, not this one). Ran ~30 search queries plus 3 WebFetch calls (glp1guide.co comparison article, wearefounders.uk GLP-1 founders piece, gettrim.co.uk "welcome to Trim" page) to verify each named company and discover new candidates.

**What was done:**
1. Read hypothesis.md, confirmed sub-segment: England-HQ, private/cash-pay, subscription GLP-1 telehealth with repeat check-ins, ~$2M+ revenue, 50-500 employees.
2. Verified all 12 named starting-set companies individually (HQ, business model, prescribing, size signal) via WebSearch.
3. Found and evaluated ~25 additional candidate companies via search (GLP-1 provider comparison articles, funding news, Companies House lookups) to try to reach the requested 20.
4. Applied exclusions.json (UK Meds, Yazen, Healthyr already excluded — confirmed not re-added) and hypothesis anti-cases.
5. Applied one additional exclusion rule pulled from `icp-detail.md`'s "Universal exclusion criteria" not explicit in the hypothesis itself: dropped Juniper UK for being a recently-acquired company (Eucalyptus Health acquired by Hims & Hers, Feb 2026, ~$1.15B) on top of its non-England (Australian) parent HQ.
6. Wrote `companies.md` with 17 companies (short of the requested 20 — documented why in the "Coverage gaps / risks" section rather than padding with disqualified small clinics).

**Key decisions / judgment calls:**
- Merged "Voy" and "Manual" into a single entry (Voy is Manual's weight-loss brand post-2025 rebrand) rather than double-counting.
- Kept Oviva UK despite its NHS-Tier-3-dominant model because the hypothesis explicitly named it and its own site claims a private channel exists — flagged as the highest-risk inclusion in the list, recommend Vadim confirm before outreach.
- Dropped Roczen/Reset Health as B2B/B2G (sells to insurers/employers/NHS/health systems, not D2C) — distinct from Oviva UK, which does have a direct-to-consumer product.
- Dropped ~10 boutique private-GP/aesthetic clinics found in search (One5 Health, 222 Healthcare, Knightsbridge Doctors, Clinic51, Medical Express Clinic, The Wellness London) as sub-scale (most confirmed 11-50 employees or smaller, single/few-site) — weight loss is a side offering among general private GP services for all of these, which is structurally the same problem as the named multiline-pharmacy anti-case even though they aren't literally on the anti-case list.
- Flagged "Simple.Life" (named in hypothesis) as likely a naming mix-up — closest real match is Simple Online Pharmacy / Simple Online Healthcare Ltd, which is Glasgow (Scotland) HQ, not England.
- Included ZAVA with a low-medium flag despite it appearing in our own `icp-detail.md` as a segment-2 (BMI-verification/pharmacy) example rather than a segment-1 (GLP-1 telehealth) example — a real structural-fit tension, not just a data gap.

**Output:** `workspace/outbound/campaigns/2026-07-08-uk-telehealth/companies.md` — 17 companies, tiered High/Medium/Low-Medium/Low confidence, full summary table + named-set disposition table + excluded-candidates list + coverage-gaps section.

**Next step:** people-extractor (mechanical step per CLAUDE.md workflow — no manager checkpoint required per task instructions before this step, though Vadim should review the Oviva UK and Simple.Life/geo flags before message-sequencer runs).
