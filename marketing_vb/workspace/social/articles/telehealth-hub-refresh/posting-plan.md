# Posting Plan — AI in Telehealth Hub

**Article:** AI in Telehealth: Workflows, Privacy, Patient Experience, and Remote Body Data Use Cases
**Slug:** telehealth-hub-refresh
**Product:** FitXpress (100%)
**Vertical:** Telehealth
**Date:** 2026-08-07
**Total profiles:** 9 (all active — `linkedin-whitney` remains disabled, `posts_per_week: 0`, not included)
**Max carousels:** 3 (per visual coherence rule)
**Note on gate:** article status is `ready_for_review`, not yet `approved_for_publish`. Vadim explicitly instructed drafting to proceed ahead of that checkpoint; final publish still requires his Telegram approval per CLAUDE.md §9.

---

## Claims Table — Core Extract from Article

| # | Claim | Source | Strength |
|---|-------|--------|----------|
| C1 (FX-003) | For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm | Article §How mobile body scanning fits into telehealth | High — differentiation, longitudinal use |
| C2 (FX-005) | Full pipeline returns results in under 45 seconds | Article §How mobile body scanning fits into telehealth | High — core product stat |
| C3 (FX-006) | 80+ body measurements from two smartphone photos plus onboarding inputs | Article §How mobile body scanning fits into telehealth | High — core product stat |
| C4 (FX-007) | Predicted weight, BMI, BMR, estimated body-fat %, lean mass, fat mass as outputs | Article §How mobile body scanning fits into telehealth | Medium — capability breadth |
| C5 (FX-010) | One weight-loss management program recorded ~34,000 scans in 2025 (kept generic, no customer name — NDA) | Article §How mobile body scanning fits into telehealth | Medium — adoption signal, must stay unnamed |
| C6 (FX-012) | Supports HIPAA-compliant implementations, including a BAA on request | Article §Privacy, security, and data governance | High — US procurement gate |
| C7 (FX-013) | Supports GDPR-aligned workflows | Article §Privacy, security, and data governance | High — EU procurement gate |
| C8 (FX-014) | Data encrypted in transit and at rest | Article §Privacy, security, and data governance | Medium — security posture |
| C9 (FX-015) | Photos deleted after processing by default | Article §Privacy, security, and data governance | Medium — data minimization |
| C10 (FX-016) | No names or direct personal identifiers required; customer controls session-identifier association | Article §Privacy, security, and data governance | Medium — data minimization |
| C11 | The remote body-data gap: self-reported measurements vary with equipment, technique, recall, and format — "looks like data but does not compare cleanly across time" | Article §The remote body-data gap | High — problem framing, most quotable line |
| C12 | Evaluation reframe: not "how accurate is it?" but "accurate enough for which decision?" | Article §How to evaluate an AI tool for telehealth | High — signature reframe move |
| C13 | Patient-experience checklist: consent in plain language, why front+side photos, comfort with capture, accessibility, retakes, alternative path, outputs are estimates, who sees results | Article §Patient-experience considerations | High — human/experience angle |

---

## Profile Assignments — Unique Angles

### Company Accounts

| Profile | Platform | Claim Used | Angle | Format | Length |
|---------|----------|------------|-------|--------|--------|
| twitter-company | Twitter/X | C11 + C12 | Punchy reframe: self-reported data "looks like data but doesn't compare" → the sharper evaluation question is "accurate enough for which decision?" | Text | 240-260 chars (250 delivered) |
| instagram-company | Instagram | C13 | Human/visual patient-experience walkthrough: why two photos, consent in plain language, the alternative path for patients who can't/won't scan | Carousel | 600-1000 chars (847 delivered) |
| facebook-company | Facebook | C11 + C3 | Accessible framing: a scale gives one number, a remote program needs a comparable record; question to audience | Text+photo | 800-1200 chars (1105 delivered) |
| linkedin-company | LinkedIn | C12 + C6 + C7 | Expert/procurement: the data-capture layer behind telehealth workflows, "accurate enough for which decision," HIPAA/GDPR as the privacy half of that question | Text+photo | 180-280 words (229 delivered) |

### Personal Accounts — Leadership

| Profile | Platform | Claim Used | Angle | Format | Length |
|---------|----------|------------|-------|--------|--------|
| linkedin-katerina | LinkedIn | C11 + C1 | CEO, UK lens: as NHS-adjacent/private remote programs scale, body-data consistency and CQC-relevant governance become procurement gates | Text | 180-250 words (214 delivered) |
| linkedin-vadim | LinkedIn | C1 + C2 | AU lens: what structured capture means operationally for AU telehealth/RPM at scale — deployment, privacy posture, procurement, not strategy-level | Text+photo | 180-250 words (216 delivered) |

### Personal Accounts — Business Development

| Profile | Platform | Claim Used | Angle | Format | Length |
|---------|----------|------------|-------|--------|--------|
| linkedin-nick | LinkedIn | C11 + C6 + C8 + C9 | US lens: the comparability question at scale + the privacy reality US buyers check (HIPAA BAA, encryption, deletion by default) | Text+photo | 180-250 words (211 delivered) |
| linkedin-olena | LinkedIn | C7 + C10 + C11 | Continental Europe lens: cross-border consistency and GDPR-aligned capture as one combined problem, data minimization | Text+photo | 180-250 words (199 delivered) |
| linkedin-katya | LinkedIn | C11 + C1 | Israel + Gulf lens: commercial buying behavior — sharp buyer questions about the data layer as programs scale past pilot | Text | 180-250 words (193 delivered) |

---

## Format Distribution Check

- **Carousels:** 1 of 9 (instagram-company)
- **Text+photo:** 5 (facebook-company, linkedin-company, linkedin-vadim, linkedin-nick, linkedin-olena)
- **Text only:** 3 (twitter-company, linkedin-katerina, linkedin-katya)
- **Within max 3 carousel limit:** ✅ (1 of 3 used)

---

## Regional Lens Enforcement

| Profile | Region | Rule | Status |
|---------|--------|------|--------|
| linkedin-katerina | UK | UK-only: MHRA/CQC/NHS context where the article supports it. NEVER US/EU regulatory framing. NEVER Mobile Tailor | Enforced in draft — no US/EU references |
| linkedin-vadim | Australia | AU health-operator lens: ops, privacy, implementation, procurement. NEVER US/EU/UK regulatory framing unless article raises it (it doesn't). NEVER CEO-level strategy | Enforced in draft — no regulatory-body references, practitioner tone |
| linkedin-nick | USA | US health-tech pain points, HIPAA/BAA. NEVER European regulatory context | Enforced in draft — GDPR not mentioned |
| linkedin-olena | Continental Europe (UK excluded) | GDPR/EU-wide framing only, no country-specific regulation, no UK references | Enforced in draft — EU-wide GDPR only, no country names |
| linkedin-katya | Israel + Gulf | Commercial/buying-behavior framing, no technical deep dive, no EU/US regulatory specifics | Enforced in draft — no HIPAA/GDPR mention, buyer-behavior framing only |

---

## Hook-Uniqueness Check

Each profile opens on a distinct hook. No duplicate primary insight:

1. **twitter-company** → "Self-reported weight and measurements shift with the scale, the tape, and the person using them" (comparability problem, stat-forward)
2. **instagram-company** → "Two photos. One clear explanation. That's the whole ask." (patient-consent human moment)
3. **facebook-company** → "A scale gives one number. A remote-care program often needs to see more than that." (scale vs. structured record, question to audience)
4. **linkedin-company** → "Telehealth programs are scaling remote check-ins faster than most teams are standardizing what gets captured during them." (expert market-trend framing)
5. **linkedin-katerina** → "The same pattern as remote care programs scale across the UK: the technology to check in with patients remotely is mature, but what gets captured...is often the weakest link." (UK founder observation)
6. **linkedin-vadim** → "The check-in workflow is solid, but the body-data step underneath it is still built on whatever the patient reports." (AU operator/implementation angle)
7. **linkedin-nick** → "Once you scale past a pilot, how do you know the body data you are capturing between visits is actually comparable over time?" (US evaluation question)
8. **linkedin-olena** → "How do you keep body-data capture consistent and still meet a GDPR-aligned standard everywhere you operate?" (EU cross-border framing)
9. **linkedin-katya** → "The product is ready to scale, but the data feeding it is still whatever the patient typed into a form." (Israel/Gulf buyer-behavior angle)

**No duplicate hooks:** ✅ — no two profiles lead on the same claim-as-primary-insight; the comparability/gap theme (C11) recurs across several profiles per the article's own emphasis, but each is paired with a distinct secondary angle (consent, privacy regime, procurement, buyer behavior) so no two posts read the same.

---

## Brand Rules Reference (all posts must follow)

- **Hard bans:** NEVER "diagnoses," "makes decisions," "replaces clinician," "autonomously triages," "determines eligibility," "guarantees compliance"
- **Banned words:** leverage, utilize, harness, robust, seamless, comprehensive, delve, navigate, tapestry, realm, groundbreaking, cutting-edge, game-changer; "objective" → standardized/structured; "by hand" → manually
- **Banned phrases:** "reader," "audience," "below," "this article/this guide" (use "the full piece"), "In today's fast-paced world," "Have you ever wondered"
- **AI signatures banned:** em-dash rhetoric, "It's not just X, it's Y," triple adjective parallelisms ("fast, reliable, scalable")
- **No hashtags anywhere. 1–2 emoji max per post, only LinkedIn posts use them.**
- **POV:** company accounts (twitter, instagram, facebook, linkedin-company) — 3rd person / "we." Personal accounts — 1st person.
- **Positioning:** FitXpress is a structured-data-capture and remote-intake support layer. It does not diagnose, does not autonomously triage or determine eligibility, does not replace protocol-required reference methods, and does not make the customer's workflow compliant on its own — compliance is a programmatic outcome the organization owns.
- **Scope discipline:** telehealth vertical stays on remote-care workflows, privacy, documentation, and patient experience. No drift into GLP-1 eligibility screening or online-pharmacy BMI verification — those are separate clusters.
- **No named customers.** The "~34,000 scans" figure (C5) stays generic ("one weight-loss management program") per NDA.
