# Proof Points (3DLOOK)

> **Правило:** каждое число цитируемое в outbound / SEO / posts должно браться отсюда. Если хочешь использовать число, которого тут нет — STOP, спроси Вадима. Не выдумывай.

> Every number here has a source / context column. Source links to internal deck or public material.

## Accuracy

> **Published wording lives in `brand-assets/product-info/accuracy-formulations.md`, transcribed verbatim from the
> live framework article on 2026-09-02.** That article is canonical for accuracy language;
> this table is the number store behind it. Copy the sentence from there, not a number from
> here, into anything that ships.
>
> Format is `96-97%` and `1.5-2.0 cm`, **hyphens**, matching the live page. En dashes were in
> this table until 2026-09-02 and are a hard ban.

| Claim | Number | Source / Context |
|-------|--------|------------------|
| Overall accuracy vs manual measurements | 96-97% | 2025 Accuracy & Repeatability Study (real-world customer scan events benchmarked against expert manual measurements). Published sentence: accuracy-formulations.md §1.1 |
| Typical error margin | 1.5-2.0 cm | Same study |
| Wrist girth accuracy | 0.54 cm absolute error | Same study (highest precision metric). **INTERNAL / technical material only — the live framework article publishes no per-measurement figures, only "varying by body part" plus methodology under NDA. Review 1 item 16 cut these from a hub article. Do not publish in a hub, use accuracy-formulations.md §1.1 instead** |
| Calf accuracy | 1.27 cm absolute error | Same study |
| Neck accuracy | 1.48 cm absolute error | Same study |
| Thigh accuracy | 1.64 cm absolute error | Same study |
| Knee accuracy | 1.73 cm absolute error | Same study |
| Chest accuracy | 1.74 cm absolute error | Same study |
| Waist accuracy | 2.14 cm absolute error | Same study |
| Hip accuracy | 2.25 cm absolute error | Same study |
| Weight estimation accuracy | ±3.5% average error margin | FitXpress deck, real-world conditions |

## Repeatability

> **Published wording: `brand-assets/product-info/accuracy-formulations.md` §1.2.** The locked convention is `< 1 cm`.

| Claim | Number | Source / Context |
|-------|--------|------------------|
| Overall repeatability | 95%+ consistency | **INTERNAL ONLY, DO NOT PUBLISH, and query it with Vadim.** Checked against the live framework article 2026-09-02: it describes this same 2025 study and gives **no** such percentage, only "typical scan-to-scan differences of less than 1 cm". So this figure has no published home and may not be a real derived statistic at all. It was in `CLAUDE.md`, `overview.md` and claim FX-004 until 2026-09-02 |
| Variance across repeated scans | < 1 cm | Same study. **This is the publishable repeatability figure.** Published sentence: accuracy-formulations.md §1.2 |
| Variance: chest | 0.60 cm | Same study (girth measurements) |
| Variance: waist | 0.89 cm | Same study |
| Variance: low hips | 0.86 cm | Same study |
| Variance: knee | 0.12 cm | Same study |
| Variance: calf | 0.12 cm | Same study |
| Variance: ankle | 0.07 cm | Same study (lowest variance) |

## Speed

| Claim | Number | Source / Context |
|-------|--------|------------------|
| Time from photo to results | Under 45 seconds | FitXpress product spec |
| Photos required | 2 (front + side) | Product spec |

## Output coverage

| Claim | Number | Source / Context |
|-------|--------|------------------|
| Body measurements | 80+ | Product spec |
| Body composition outputs | BMI, BMR, fat %, lean mass, fat mass, essential fat, beneficial fat | Product spec |
| Points in source 3D model | 5M+ per model | Dataset Generation Protocol |

## Training data

| Claim | Number | Source / Context |
|-------|--------|------------------|
| Years of training data | 9+ | FitXpress deck, Apr 2025 |
| Photographs in training set | 150,000+ | Same |
| 3D scans in training set | 30,000+ | Same |
| Individual measurements | 430,000+ | Same |
| Demographic coverage (age) | 16-78 years | Same |
| Demographic coverage (weight) | 38-210 kg | Same |
| Demographic coverage (height) | 150-220 cm | **Vadim confirmed 2026-09-02.** One figure for both training-data coverage and the internal validation population, and the only one to publish. The Apr 2025 deck row read 150-205 cm and is superseded. Matches the live accuracy article |
| Gender distribution | 48% male / 52% female | Same |
| Locations | US, Europe | Same |
| Population not established | People with physical disabilities: the model was not specifically trained on data representing them, and measurement performance for this population has not been established | Editor's final of the occupational-health intake article, 2026-09-11; approved for publication by Vadim the same day. Published wording: accuracy-formulations.md §5, "Population limitation" |
| Hardware scanner cameras | 4 dynamic | Dataset Protocol |
| Parameters per person measured | 86 | Dataset Protocol |
| Photo configurations per user | 34 (distance, angle, slope, lighting) | Dataset Protocol |

## Customer outcomes (real)

### FitXpress
| Customer | Metric | Number | Source |
|----------|--------|--------|--------|
| Yazen | 2025 scans | 34,000 | Internal customer breakdown |
| Yazen | Use case | Weight loss management support | Internal |
| UK Meds | 2025 scans | 7,500 | Internal |
| UK Meds | Use case | BMI verification for online pharmacy | Internal |
| UK Meds | Customer lifetime so far | 7 months | Internal |
| Healthyr | Use case | Patient profile complement | Internal |

### Mobile Tailor
| Customer | Metric | Number | Source |
|----------|--------|--------|--------|
| Safariland | 2025 scans | 15,500 | Internal |
| Safariland | Customer lifetime | 62 months | Internal |
| Safariland | Use case | Custom-fit PPE — measurement consistency to avoid remakes | Internal |
| Burlington Medical | 2025 scans | 11,500 | Internal |
| Burlington Medical | Customer lifetime | 64 months | Internal |
| Burlington Medical | Use case | Custom-fit radiation aprons | Internal |
| Jim's Formal Wear | 2025 scans | 3,200 | Internal |
| Jim's Formal Wear | Customer lifetime | 58 months | Internal |
| Jim's Formal Wear | Use case | Remote measuring for wedding parties | Internal |
| Generation Tux | Use case | DTC online formal wear rental | Internal |

### Aggregate
| Claim | Number | Source |
|-------|--------|--------|
| Total customers (all-time) | 100+ | Company deck |
| Active customers in 2025 | 67 | Internal customer breakdown |
| Total ARR 2025 | $1.084M | Internal |
| Enterprise ARR | $822K | Internal |
| SMB ARR | $262K | Internal |
| Total scans 2025 | 112,100 | Internal |
| Enterprise scans 2025 | 72,300 | Internal |
| SMB scans 2025 | 39,800 | Internal |
| 4 legacy MT customers retention | 5+ years | Internal (lifetime durability evidence) |

## Market sizing (illustrative, FitXpress new use cases)

| Use case | TAM | SAM (US + EU/UK) | Source |
|----------|-----|------------------|--------|
| Insurance underwriting | $25-75M / year | $5-15M | Brainstorm deck (50-150M events × ~$0.50) |
| Wellness rewards verification | $50-200M / year | $10-40M | Brainstorm deck |
| Bariatric pre-qualification | $10-30M / year | $2-8M | Brainstorm deck |
| Occupational health screening | $20-60M / year | $5-15M | Brainstorm deck |
| Clinical trials (metabolic / obesity) | $10-40M / year | $3-12M | Brainstorm deck |

## Compliance & security

| Claim | Detail | Source |
|-------|--------|--------|
| HIPAA | Supports HIPAA-governed deployments where 3DLOOK acts as a business associate under an executed BAA. Framework, not a certification: never "HIPAA compliant" | Live trust FAQ (2026-09-16), via `compliance.md` §1 |
| GDPR | **Verbatim: "In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR."** DPA with SCCs; UK Addendum where UK GDPR applies | Same, `compliance.md` §2 |
| CCPA / CPRA | Service provider or contractor; no sale of personal information | Same |
| SOC 2 | Working toward a SOC 2 Attestation Report; initial readiness assessment completed. **Not certified** | Same |
| UK / EU MDR | Independent regulatory assessment: not a medical device under UK MDR / EU MDR (current intended purpose) | Same |
| FDA | Not cleared, authorized or approved; no representation on whether it is required | Same |
| Encryption in transit | TLS | Same |
| Encryption at rest | Amazon S3 SSE-S3 (S3-managed keys), on by default, cannot be disabled | Same |
| Hosting | AWS, primarily US-West-2, partially US-East-1 | Same |
| Photo retention | Deleted immediately after processing OR within 30 days, per customer policy | Same |
| Photo blur / face obfuscation | Retained photos auto-blurred; face obfuscation at capture | Same |
| Output retention | Measurements, body composition, 3D models stored on an ongoing basis unless the agreement says otherwise; deletion by scan identifier | Same |
| Identifiers | Scan records carry random, anonymized IDs; 3DLOOK cannot identify an individual from stored scan records. (Replaces "personal identifier processing: none", retired 2026-09-18) | Same |
| AI training | Production customer data not used to train models | Same |
| Scan speed | Structured outputs in under 45 seconds | Same |

## Pricing (FitXpress)

See `pricing.md` for full table. Key anchors:
- Free trial: 1 month, 200 free requests
- $1,000 / mo at 500 requests ($2.00/request)
- $10,000 / mo at 20,000 requests ($0.50/request)

## Funding & company milestones

| Claim | Number | Source |
|-------|--------|--------|
| Founded | 2016 | About deck |
| Employees | 28 | Same |
| Total raised | $16.2M | Same |
| Sifted recognition | 2020 Pioneers of the New World | Same |
| IEEE | Winner, 2019 Retail Digital Transformation Grand Challenge, run by the 3D Retail Coalition with Kalypso and IEEE. | Terminology Doc §2.11, approved wording (2026-09-14) |
| Standards | Participant in the IEEE 3D Body Processing working group, which is developing standards for mobile body scanning. | Same |

> **IEEE wording is fixed (2026-09-14).** Use the two sentences above verbatim, and only those
> (`brand-assets/content-strategy/terminology-guardrails.md` §2.11). IEEE has raised an issue with
> incorrect claims 3DLOOK was making. The banned forms are listed in §2.11 and failed by
> `detect-ai-tells.py` (`ieee_claims`); the earlier wording of these two rows is recorded in the
> guardrails' Overrides table, not here, because agents copy from this file. No standalone IEEE
> logo in an award, certification, validation or recognition strip either.

---

## How agents should cite

When using a number above:
- For posts / outbound: **mention the number with light context** ("96-97% accuracy against expert manual measurement") — do not link to internal docs publicly
- For SEO articles: **prefer customer outcome over internal metric** when possible ("Safariland uses our scanning to reduce remakes" > "we have 96% accuracy")
- **Never invent comparisons** — e.g., do not say "10× more accurate than X" unless that number exists in this file with a source

When uncertain, use the **range form** ("around 95-97% accuracy") rather than precise number — preserves credibility if number drifts.
