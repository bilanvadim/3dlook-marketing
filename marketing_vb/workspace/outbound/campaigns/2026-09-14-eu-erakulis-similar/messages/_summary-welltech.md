# Messaging — 2026-09-14-eu-erakulis-similar — Welltech batch

- Total people (group = Welltech): 35
- Total messages generated: 35 × 2 = 70
- Avg char count message 1: 506 / 600 (min 362, max 594)
- Avg char count message 2: 324 / 550 (min 217, max 443)
- Distribution by angle: product (19), retention (10), technical-integration (4), referral (2)
- Distribution by wave: wave 1 (33), wave 2 / referral (2: Mirka Pejanovic, Nikolay Zdvyzhkov — sent only after wave-1 product/retention contacts at Welltech have gone out)

## What's in the messages

- All 35 contacts are at one company (Welltech), per the campaign's accepted concentration risk (2026-09-28 addendum, caps raised to ≤35/company). Each hook is built off that person's own LinkedIn headline/bio/experience (previous employer, a phrase from their bio, their specific function) so forwarded screenshots inside the same company don't read as a blast. No two messages share a hook or an identical sentence (hash-checked across all 70 bodies, 0 duplicates).
- No Welltech app brand is named anywhere (FitCoach and Omo are explicitly excluded per instructions as unverified Welltech products; Muscle Booster / Yoga-Go / WalkFit were not clearly tied to any individual contact's bio, so none were named either). References to "the app you lead" / "Welltech's apps" / "your portfolio" stay generic.
- No client names (Erakulis, Yazen, UK Meds, Healthyr) and no competitor names (Zing / Zing Coach) anywhere. Only the two anonymous proofs from the campaign rules are used: "one platform ran 34,000 scans in 2025" and "112,100 scans in 2025 across all 3DLOOK customers", one proof per message, never stacked in the same message (one contact, Stan Gladkov, gets 34,000 in Message 1 and 112,100 in Message 2, which is the intended pattern, not a stack).
- No pricing, no $/£/€, no tiers, no "free trial" anywhere.
- No self-reported Welltech revenue figure from any profile bio (one bio claimed "€500M ARR" — not used, per instructions).
- Compliance line ("FitXpress is not a medical device." / GDPR sentence) not used: this ICP is consumer digital fitness/wellness, not insurance / healthcare / clinical / online pharmacy, so it isn't mandatory per the contract, and none of the 35 hooks needed it.
- 4 `technical-integration` contacts (Anas Lamarfa CTO, Isa Vilacides, Mehdi Dogguy, Peter Turek — all Directors of Engineering/Infrastructure) are written to implementers: SDK/API, integration effort (2-4 weeks, no computer-vision hire), data flow. No retention-economics pitch, which they don't own.
- 2 `referral` contacts (wave 2, Mirka Pejanovic — Director of Portfolio & Operations, and Nikolay Zdvyzhkov — Head of FP&A) get a short ask for the roadmap owner, no product pitch dump, per the campaign's referral-angle rule.
- 1 caveated contact: Anastasiia Stovpova (New Channels Lead, headline reads "User Acquisition Lead") is written softly, offering a pointer to the real feature owner rather than assuming she owns the roadmap, since her fit is Vadim's by-name exception, not a title match.
- 1 stretch-fit contact: Dmitry Zenevich (AI Product Builder, generative video/marketing assets) is angled toward the visual-asset parallel (his AI ad-creative pipeline vs. our member-facing progress visuals) rather than assumed app-roadmap ownership, per the CSV's own caveat.
- 1 builder-PM contact (added after coordinator flagged a missing row): Stan Gladkov, Senior AI Product Manager, Builder — his bio ("I do the PM work and then ship it... run by single person," AI-powered tooling, ex-Atlassian, ex-Wayfair) is used directly as the hook, angled toward build-vs-buy since he would personally do the integration.

## Checks run

| Check | Result |
|---|---|
| `detect-ai-tells.py --channel dm` on all 70 message bodies (extracted to temp files, headers/context stripped) | **70/70 CLEAN** |
| Char limits (Message 1 ≤600, Message 2 ≤550) | All 35×2 within limits (see averages above) |
| Client names (Erakulis, CR7/Ronaldo, Yazen, UK Meds, Healthyr) | 0 |
| Competitor names (Zing / Zing Coach) | 0 |
| Welltech app brand names (FitCoach, Omo, Muscle Booster, Yoga-Go, WalkFit) | 0 |
| Pricing symbols ($ £ €), "free trial", tiers | 0 |
| Em dash / en dash (— –) | 0 |
| Corrective "rather than" / "X, not Y" | 0 (7 instances found and rewritten during drafting, incl. 1 in the added Stan Gladkov message) |
| `"let"` used as "allow" | 0 (1 instance found — "lets you" — and rewritten) |
| `"so"` as a result/benefit connector | 0 (1 instance found — "so you've seen both sides" — and rewritten) |
| "80+ body metrics" (banned form) | 0 — always "80+ body measurements" |
| "your organization" | 0 — always "Welltech" or a specific descriptor |
| Banned words (leverage, utilize, harness, robust, seamless, comprehensive, delve, tapestry, realm) | 0 |
| Duplicate message bodies (md5 hash across all 70) | 0 |

## Note on the missing row

The first pass wrote 34 files, missing `stasgladkov` (Stan Gladkov). Root cause: the initial
company filter used `awk -F','` on the raw CSV, and his title field `"Senior AI Product Manager,
Builder"` contains a comma inside quotes, which broke the column count and dropped the row from
that intermediate file before any per-person work started. Rebuilt the Welltech subset with
Python's `csv` module (which handles quoting correctly) and got 35 rows; wrote the missing message
file, ran the full check suite above on the corrected 70-body set, and updated this summary.

## Random sample for Vadim review (5 people)

- `dmitryzenevich.md` — Dmitry Zenevich, AI Product Builder | Generative Video & Marketing Assets, angle: product (stretch-fit case, visual-asset framing)
- `bezrukartem.md` — Artem Bezruk, General Manager (H&F), angle: retention
- `yuliana-rondyak-ba7b3b156.md` — Yuliana Rondyak, Growth Product Manager, angle: retention
- `valentyna-rudenko-575b0b121.md` — Valentyna Rudenko, Content Product Manager, angle: product
- `sofia-ortins-3847a761.md` — Sofia Ortins, Senior Product Manager, angle: product
- `stasgladkov.md` — Stan Gladkov, Senior AI Product Manager, Builder, angle: product (added after the initial pass)

Full path: `workspace/outbound/campaigns/2026-09-14-eu-erakulis-similar/messages/{person_id}.md`
