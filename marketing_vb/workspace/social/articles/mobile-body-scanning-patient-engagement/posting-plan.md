# Posting Plan — How Mobile Body Scanning Improves Patient Engagement

**Article:** How Mobile Body Scanning Improves Patient Engagement
**Slug:** mobile-body-scanning-patient-engagement
**Source draft:** `workspace/seo/articles/mobile-body-scanning-patient-engagement/draft-v5-revision1.md` (Revision 1, Review 1 applied)
**Live URL:** https://3dlook.ai/content-hub/mobile-body-scanning-patient-engagement/
**Product:** FitXpress (100%)
**Vertical:** Telehealth (hub: AI in Telehealth → cluster: Patient experience)
**Date:** 2026-08-17
**Total profiles:** 9 (all active — `linkedin-whitney` remains disabled, `posts_per_week: 0`, not included)
**Max carousels:** 3 (per visual coherence rule)

**Note on gate:** the article gate is already cleared for this pack — the article is `status: published`, published 2026-08-14, and live at the URL above. Every post therefore carries the live link rather than a placeholder. What is still open is the *social* gate: these 9 drafts need Vadim's Telegram approval before scheduling or any designer hand-off, per CLAUDE.md §9 (approver = Vadim) and §10 rule 2 (no direct publishing).

**Note on claim currency:** all posts draw on the **Revision 1** claim set, not v4. Three formulations changed in Review 1 and the posts follow the new ones: capture time is "approximately 30 to 45 seconds" (never "under 45 seconds"), repeatability uses the approved sentence verbatim, and the privacy paragraph uses the new deletion/retention/hosting language. The GLP-1 discontinuation statistic (64.8%, JAMA Network Open) was **removed** in Review 1 and must not reappear in any post, caption, or design brief.

---

## Claims Table — Core Extract from Article

| # | Claim | Source | Strength |
|---|-------|--------|----------|
| C1 | The engagement gap: remote care removed the in-clinic ritual that anchored motivation; motivation can fade when progress stays invisible, and on 30, 60, and 90-day cycles that drift separates a member who renews from one who quietly disappears | §The engagement challenge in remote care | High — the article's spine and its most reusable problem framing |
| C2 | Self-reported weight and BMI are a limited signal: readings may come from different scales, capture conditions vary, and a single number cannot show how measurements or body composition are changing | §The engagement challenge in remote care | High — problem framing, pairs with C1 |
| C3 (EXT-TELEHEALTH) | A 2026 analysis of the Medical Expenditure Panel Survey (MEPS), published in the journal *Healthcare*, found the share of US adults with at least one telehealth visit rose from about 7% in 2020 to roughly 12% in 2021 and held near that level through 2023 | §The engagement challenge in remote care | High — the only external statistic surviving Review 1; must carry its source attribution wherever used |
| C4 (FX capture) | Two guided smartphone photos, front and side, become more than 80 body measurements, body composition outputs, and a 3D body model in approximately 30 to 45 seconds | §What mobile body scanning adds | High — core product stat. Revision-1 wording; "under 45 seconds" is retired |
| C5 (FX-REPEATABILITY) | "For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm. Consistent capture conditions help programs compare results more reliably over time" | §Five ways it can support patient engagement → Reliable scan-to-scan comparison | High — must be used in this approved formulation only; no "repeatability of < 1 cm", no two-week-detectability implication |
| C6 | Body-composition mechanic: a patient losing fat while gaining lean mass may see little movement on a scale, while a body-composition record can help them recognize that change | §Five ways it can support patient engagement | High — the most quotable engagement mechanic in the piece |
| C7 | The scan-to-scan loop, six steps: enrollment capture (from home, in about a minute) → baseline → scheduled re-scans → progress visualization → care-team review → next-cycle goals | §How the scan-to-scan experience works | Medium-High — workflow spine, good for walkthrough formats |
| C8 | Cadence: more frequent is not automatically better. Scanning too often surfaces noise, scanning too rarely misses the moments that keep a patient engaged; match cadence to program length and expected rate of change | §Implementation considerations → Scan frequency | Medium — operator-facing, strong discussion starter |
| C9 (FX-PRIVACY) | Privacy posture: production photos deleted after processing; structured outputs may be retained per the customer's configuration and agreement; data encrypted in transit (TLS) and at rest; standard hosting AWS US, with EU or UK hosting available on request; HIPAA-compliant workflows with a BAA available where required; GDPR-aligned data handling | §Where FitXpress fits, and where other methods remain necessary | High — procurement gate. Used per-region: (HIPAA/BAA) for US, (GDPR / EU hosting) for EU, (UK hosting) for UK |
| C10 | White-label delivery: the two-photo capture runs through an API or SDK inside the program's own patient app under its own branding, with no specialized hardware for the patient to buy; results can connect into an EMR | §Where FitXpress fits + §Implementation considerations → Integration | Medium-High — answers the "how does it ship" question |
| C11 (FX-NOTDEVICE) | The four boundaries: supports review rather than diagnosis; does not make clinical or eligibility decisions; does not replace required clinical assessments such as DEXA or BIA where a protocol calls for them; does not guarantee engagement or health outcomes. Not positioned as a medical device; compliance is evaluated on data-privacy frameworks | §Where FitXpress fits, and where other methods remain necessary | High — mandatory guardrail, trimmed from 7 items to 4 in Review 1 |
| C12 | Capture quality: production conditions are not lab conditions. A patient may stand in poor light, wear a loose sweater, or hold the phone at the wrong angle. Guided capture and retake logic can reduce that error; they do not remove the need for clear instructions | §Implementation considerations → Capture guidance | Medium — operator credibility, the honest-implementation angle |
| C13 | Engagement measurement: scan completion rate, repeat check-in rate, and progress-visualization views are engagement signals, not clinical outcome measures | §Implementation considerations → Measuring engagement outcomes | Medium — protects a rollout's internal credibility |
| C14 | The engagement pattern repeats across program types, not one medication pathway: general telehealth, weight-loss programs, wellness and coaching, remote monitoring and longitudinal care | §Applications beyond GLP-1 | Medium — carries the cannibalization guardrail: GLP-1 links must not anchor the central argument |

**Claim not available (do not reintroduce):** the GLP-1 discontinuation statistic (64.8%, JAMA Network Open / EXT-GLP1DROP) was removed per Review 1 comment 3 and was deliberately not replaced. No post or design brief may imply a retention/discontinuation curve sourced from it.

---

## Profile Assignments — Unique Angles

### Company Accounts

| Profile | Platform | Claim Used | Angle | Format | Length |
|---------|----------|------------|-------|--------|--------|
| twitter-company | Twitter/X | C2 + C4 | The between-visit signal problem in one sharp line: a program's whole progress record is one self-reported number, taken on whatever scale is in the house | Text | 240-260 chars (253 delivered) |
| instagram-company | Instagram | C1 + C4 + C6 + C11 | Human/visual: the scale can stay flat while the body changes. Remote care removed the moment that made change visible; a scan-to-scan record puts it back | Carousel | 600-1000 chars (919 delivered) |
| facebook-company | Facebook | C7 + C8 + C11 | Accessible walkthrough of the scan-to-scan loop, opened on the cadence question programs actually argue about: how often should a patient scan? | Text+photo | 800-1200 chars (1,196 delivered) |
| linkedin-company | LinkedIn | C1 + C2 + C4 + C5 + C11 | Market trend, not a summary: virtual care matured into a standing channel, and the unsolved part moved to the space between visits. Business value plus an explicit scope boundary | Text+photo | 180-280 words (253 delivered) |

### Personal Accounts — Leadership

| Profile | Platform | Claim Used | Angle | Format | Length |
|---------|----------|------------|-------|--------|--------|
| linkedin-katerina | LinkedIn | C1 + C9 (UK hosting) + C11 | CEO, UK lens: the enterprise buying question moved from model performance to scope and data residency. A layer with narrow, stated boundaries is easier to place in a regulated care pathway | Text | 180-250 words (229 delivered) |
| linkedin-vadim | LinkedIn | C8 + C10 + C12 + C13 | AU lens: an engagement feature is easy to demo and hard to keep honest at scale. Capture protocol, cadence, and what you agree to measure decide whether the signal holds up | Text+photo | 180-250 words (235 delivered) |

### Personal Accounts — Business Development

| Profile | Platform | Claim Used | Angle | Format | Length |
|---------|----------|------------|-------|--------|--------|
| linkedin-nick | LinkedIn | C3 + C4 + C5 + C6 + C9 (HIPAA/BAA) + C11 | US lens: telehealth settled in as a standing channel (MEPS), so the operating question moved to between-visit engagement, with HIPAA/BAA posture as the second thing every buyer checks | Text+photo | 180-250 words (239 delivered) |
| linkedin-olena | LinkedIn | C9 (GDPR / EU hosting) + C10 + C11 + C14 | Continental Europe lens: operators run several program types on one platform and all hit the same between-visit gap. The pattern transfers; evaluation then turns to data handling and white-label delivery | Text+photo | 180-250 words (230 delivered) |
| linkedin-katya | LinkedIn | C1 + C4 + C6 + C11 | Israel + Gulf lens: teams quote acquisition numbers to the decimal and go vague on week six. Retention is where the money is, and retention runs on whether a patient can see change | Text | 180-250 words (224 delivered) |

---

## Format Distribution Check

- **Carousels:** 1 of 9 (instagram-company)
- **Text+photo:** 5 (facebook-company, linkedin-company, linkedin-vadim, linkedin-nick, linkedin-olena)
- **Text only:** 3 (twitter-company, linkedin-katerina, linkedin-katya)
- **Within max 3 carousel limit:** ✅ (1 of 3 used)
- **No restricted formats used** (no poll, no lead magnet), so no platform-restriction conflicts: ✅

---

## Regional Lens Enforcement

| Profile | Region | Rule | Status |
|---------|--------|------|--------|
| linkedin-katerina | UK | UK-only: MHRA/CQC/NHS context where the article supports it. NEVER US/EU regulatory framing. NEVER Mobile Tailor | Enforced. UK remote-care buyers and UK data residency. The article raises no UK regulator, so none is named. One "US" mention appears, and it is the **data-residency fact** from C9 ("standard hosting runs in the US, with UK hosting available on request") — a hosting location, not US regulatory framing; HIPAA is not mentioned |
| linkedin-vadim | Australia | AU health-operator lens: ops, privacy, implementation, procurement. NEVER US/EU/UK regulatory framing unless the article raises it. NEVER CEO-level strategy | Enforced. Capture protocol, cadence, and measurement definition — practitioner register throughout. Zero regulators named, zero strategy-level content |
| linkedin-nick | USA | US health-tech pain points, HIPAA/BAA. NEVER European regulatory context | Enforced. MEPS/US adoption plus HIPAA, BAA, deletion, encryption. Zero GDPR, EU, or UK references |
| linkedin-olena | Continental Europe (UK excluded) | GDPR/EU-wide framing only, no country-specific regulation, no UK references | Enforced. GDPR-aligned handling and EU hosting only — the article's "EU or UK hosting" is correctly narrowed to EU. Zero country names, zero UK references, zero HIPAA |
| linkedin-katya | Israel + Gulf | Commercial/buying-behavior framing, no technical deep dive, no EU/US regulatory specifics | Enforced. Acquisition-versus-retention economics and buyer behavior. Zero HIPAA/GDPR, no technical deep dive |

---

## Hook-Uniqueness Check

Each profile opens on a distinct hook. No duplicate primary insight:

1. **twitter-company** → "Between virtual visits, a remote care program often runs on one number a patient types into an app, taken on whatever scale is in the house" (the signal problem, compressed to one line)
2. **instagram-company** → "The scale barely moved. But the body changed a lot." (the visible-change paradox, human register)
3. **facebook-company** → "How often should a patient scan? More often is not automatically better." (cadence question straight to the audience)
4. **linkedin-company** → "Virtual care is past the question of whether it works. The harder problem now sits between visits." (market-maturity reframe)
5. **linkedin-katerina** → "The question I hear from UK remote care teams has changed over the past two years. It used to be about accuracy." (CEO observation on how the buying question moved)
6. **linkedin-vadim** → "A progress feature is easy to demo and hard to keep honest at scale." (AU implementation warning)
7. **linkedin-nick** → "Telehealth stopped being a temporary channel a while ago." + the MEPS figures (US adoption data as the entry point)
8. **linkedin-olena** → "European health and wellness operators I speak with are rarely running one program at a time." (multi-program platform reality)
9. **linkedin-katya** → "Most digital health teams I meet across Israel and the Gulf can quote their acquisition numbers to the decimal." (commercial asymmetry: acquisition precise, retention vague)

**No duplicate hooks:** ✅ — nine distinct entry points across four different framings (signal problem, visible-change paradox, operator question, buyer/commercial behavior). The C1 engagement-gap theme recurs because it is the article's spine, but each profile pairs it with a different second move: capture stat (twitter), body-composition story (instagram), loop walkthrough (facebook), procurement reframe (linkedin-company), scope and residency (katerina), protocol discipline (vadim), adoption data and privacy (nick), cross-program transfer (olena), retention economics (katya).

**Phrase-level watch item:** hooks and primary insights are distinct, but three LinkedIn posts reuse article phrasing verbatim. See `review-digest.md` → Open items #2 for the specific lines and the recommended fix.

---

## Brand Rules Reference (all posts must follow)

- **Hard bans:** NEVER "diagnoses," "makes decisions," "replaces clinician," "autonomously triages," "determines eligibility," "guarantees compliance"
- **Banned words:** leverage, utilize, harness, robust, seamless, comprehensive, delve, navigate, tapestry, realm, groundbreaking, cutting-edge, game-changer, revolutionary, disrupt; "objective" → standardized/structured; "by hand" → manually
- **Banned phrases:** "reader," "audience," "below," "this article/this guide" (use "the full piece" or "the full article" as a CTA label only), "In today's fast-paced world," "Have you ever wondered," "It's no secret that," bare "AI-powered"
- **AI signatures banned:** em-dash rhetoric, "It's not just X, it's Y," triple adjective parallelisms ("fast, reliable, scalable")
- **No hashtags anywhere. 1–2 emoji max per post**, and only where an emoji actually earns its place (CLAUDE.md §6)
- **POV:** company accounts (twitter, instagram, facebook, linkedin-company) — 3rd person / "we." Personal accounts — 1st person
- **Positioning:** FitXpress is a structured body-data capture layer that supports clinician review. It does not diagnose, does not make clinical or eligibility decisions, does not replace required clinical assessments (DEXA/BIA) where a protocol calls for them, and does not guarantee engagement or health outcomes. It is not positioned as a medical device; compliance is evaluated on data-privacy frameworks
- **Scope discipline:** this article owns patient engagement **broader than GLP-1**. Per the cannibalization guardrail, no post may center on GLP-1 adherence or retention — that belongs to the dedicated GLP-1 visual-progress page. No drift into underwriting, eligibility screening, or fraud detection (both were removed from the article as out of scope in Review 1)
- **No named customers.** No client names, no scan-volume figures attributable to a named program
- **Claim currency:** Revision-1 formulations only. "Approximately 30 to 45 seconds," the approved repeatability sentence, and the new privacy paragraph. No "under 45 seconds," no reinstated GLP-1 discontinuation statistic
- **Abbreviations (M1):** expand on first use where a post uses one (BAA → Business Associate Agreement, API/SDK spelled where the post's register allows)
