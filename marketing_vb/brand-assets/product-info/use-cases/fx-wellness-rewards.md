# Use Case: FitXpress — Wellness Rewards Verification

## The pain we remove
Wellness programs rely on self-reported progress and inconsistent check-ins, driving low trust, disputes, and weak ROI reporting.

## Why now
Wellness budgets under pressure to prove outcomes. Programs need simple remote verification without clinic visits or admin burden.

## What FitXpress is here
2-photo scans for baseline + check-ins. Captures objective body measurements + BMI/body composition (structured, time-stamped).

## Biometric screening angle (Vadim, 2026-09-29)
The FX wellness landing (`/fitxpress/for-wellness-programs/`) is built around **remote biometric screening**. Demand: "biometric screening" gets 8,600 US searches a month at KD 3 (Ahrefs, 2026-09-29); the keyword map is in `workspace/research/seo-fitxpress-2026-09/2026-09-29-landing-keywords.md`.
- **What FitXpress covers:** the body-measurement part of a screening. Waist circumference (and 80+ other body measurements) from two photos; BMI calculated from height and weight, with Smart Scales (beta) cross-checking a self-reported weight; body composition as estimates (body fat %, lean mass). Timestamped, structured records for the program.
- **What it does not cover, and the copy must say so:** blood pressure, cholesterol, glucose, A1c or any blood test. Programs that need those keep a lab or onsite component; FitXpress replaces the in-person measurement step, not the screening.
- **Boundaries:** no ADA, GINA, EEOC or HIPAA wellness-program compliance claims (incentive design is the employer's decision, made with counsel); no result interpretation or health-risk assignment; "FitXpress is not a medical device."; no per-measurement accuracy figures (use `accuracy-formulations.md`). Rules: `brand-assets/content-strategy/landing-map.md` rule 7.

## Hero message
Verify wellness progress remotely to reduce disputes, boost participation, and improve program reporting.

## ICP
Health plans, employer wellness platforms, benefit administrators, group insurers.
**Buyers:** VP Member Engagement, Head of Wellness, CCO, VP Population Health.

## Examples to target
**US:** UnitedHealthcare, Aetna (CVS Health), Cigna, Elevance Health, Kaiser Permanente.
**EU:** Bupa (UK — strong reference), Vitality (UK), AXA Health, Allianz Partners, Generali (health units).

## Reference: Bupa Rewards
Bupa Rewards page is a public example of what these programs look like — health assessments, GP consults, gym memberships discounted via wellness milestones.

## KPIs we improve
- Check-in completion rate
- Program retention
- Disputes and fraud signals
- Admin time per validation cycle
- Outcomes reporting quality

## Market sizing
**TAM:** $50-200M / year (100-400M check-ins × ~$0.50/scan)
**SAM (US + EU/UK):** $10-40M / year

## Commercial value
Lower admin cost + higher program participation. Scales across large member/employee populations.

## AI resilience
We sell trust + fairness (rules + proof + reporting), not raw measurements. Apple/Google primitives don't replace program logic and audit trail.

## Critical messaging
- Reduce member disputes
- Audit trail for HR / benefits team
- Simple remote check-in (vs. clinic visit) drives participation
