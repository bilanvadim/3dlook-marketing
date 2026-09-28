# Messaging — 2026-09-14-eu-erakulis-similar — batch "other" (Freeletics · Gymondo · Kilo · Lifesum · Fastic · Fitify · Activerse)

> This batch covers the groups that are **not** Welltech / BetterMe / Yazio (those are written by three
> parallel agents into their own `_summary-*.md` files). Profile: `olena`. Product: `fitxpress`.

- **Total people in this batch:** 38
- **Total messages generated:** 38 x 2 = 76
- **Avg char count Message 1:** 466.3 / 600 (min 415, max 593)
- **Avg char count Message 2:** 350.7 / 550 (min 261, max 423)
- **Wave split:** wave 1 = 24, wave 2 = 14 (wave 2 sends only after the wave-1 contact(s) at the same
  company have been invited; Kilo wave 2 additionally waits a full week after Kilo wave 1 / Renata Roze,
  per `release_note` in `people-approved.csv`, Vadim 2026-09-28)

## Distribution by group

| Group | People |
|---|---:|
| Freeletics | 11 |
| Gymondo | 8 |
| Kilo | 8 |
| Lifesum | 6 |
| Fastic | 2 |
| Fitify | 2 |
| Activerse | 1 |
| **Total** | **38** |

## Distribution by angle

| Angle | People |
|---|---:|
| referral | 14 |
| technical-integration | 8 |
| product | 8 |
| retention | 6 |
| insurer-prevention | 2 |

`insurer-prevention` is a new angle (2026-09-28 addendum, pool M) used only for Gymondo's two
Business Development - Prevention contacts (Patricia Malovana, Stefanie Schultheis). Both messages are
framed as questions about how Gymondo documents member progress for insurer-funded prevention courses,
never as a statement about how insurers work, reimbursement rules, §20 SGB V or ZPP certification, per
the task brief.

## Proof points used (verbatim from proof-points.md, fully anonymized)

- **"One platform ... ran 34,000 scans in 2025"** (`case-studies/yazen.md`, no client name, no
  geography, no vertical claim beyond "platform") — used in most product/retention/technical messages
  as the scale proof.
- **80+ body measurements, body composition (fat %, lean mass, BMI), under 45 seconds, 2 photos, API/SDK**
  — product spec, `proof-points.md`.
- **2-4 weeks typical basic integration** — `icp-detail.md`, licensed by the hypothesis as a generic
  claim, used only in `technical-integration` messages (no customer-specific timeline stated).
- No mention of the 112,100-scans-across-all-customers figure was needed in this batch (34,000 covered
  every scale point required); it stays available if Vadim wants it swapped in.
- **FitXpress** (our own product name) is named once, in Mina Baghal's Message 2, describing our own
  product running on an anonymized platform. Not a client name.

## No client names, no pricing, no competitors, no em/en dashes

Mechanically checked on message bodies only (extracted to a `mktemp -d` temp dir, headers/Context
blocks excluded, since those carry em dashes in labels like "Message 1 — Opener" that would give false
positives):

- `erakulis / yazen / uk meds / healthyr / cr7 / ronaldo` — 0 hits
- `$ € £ / free trial / /mo` — 0 hits
- em dash (—) / en dash (–) — 0 hits in bodies
- `zing coach / prism labs / bodygram / size stream` — 0 hits
- banned words (leverage, utilize, harness, robust, seamless, comprehensive, delve, navigate, tapestry,
  realm) — 0 hits
- `rather than` (corrective contrast, terminology guardrails Part 1 §9) — 0 hits after one round of
  rewrites (Christian Weber, Alejandro, Kieran, Matias, Henry msg2 originally used it, rewritten with
  "instead of" / "without")
- `so` as a result/benefit connector and `plus` as a benefits connector — removed everywhere found
  during drafting (rewritten as relative clauses, "and", or "giving X")
- `80+ measurements` bare — none; every mention is `80+ body measurements` (§2.13)
- generic `organization` / bare `customer` for the prospect's company — 0 hits (used `platform`,
  `app`, `team`, or the company name; "customer" appears only inside Nisha Nair's own job title and a
  CRM-industry phrase describing her focus, not our label for the prospect)
- No compliance line (HIPAA/GDPR/"not a medical device") in this batch: none of the seven groups is
  insurance / healthcare / clinical / online pharmacy ICP, so the mandatory-compliance-line rule does
  not apply. Gymondo's insurer-prevention angle stays a question about Gymondo's own program design,
  not a 3DLOOK compliance claim.

## Detector run

`detect-ai-tells.py --channel dm --summary` on all 38 message bodies (Message 1 + Message 2,
extracted separately from headers): **38 / 38 CLEAN.**

Two soft (non-blocking, L3/L5) markers surfaced and were left as-is because they are sourced,
specific personalization rather than filler: 'holistic' (Anaïs Pitou — quotes Gymondo's own "#1
holistic fitness and wellbeing platform" self-description) and 'the missing pillar' (Tomasz
Gałczyński). One soft marker ('the pillar', Matias Olocco) was rewritten anyway to cut a repeated
word choice with Kenichi Takahira's message at the same company (Gymondo, both product/technical
angle, same "pillar" framing would have read templated if compared).

## Special handling flagged for Vadim

- **Mohammad A. (Lifesum, `mohammadalrawi`)** — his listed title is "Director of Data & Analytics"
  (matches `people-approved.csv`), but his LinkedIn headline reads "Strategic Advisor / Angel
  Investor". Both messages are written neutral and title-based (data/analytics framing only); the
  headline is not referenced anywhere in copy.
- **Cristina G. (Kilo, `cristina-g-528824263`)** — empty LinkedIn bio/experience, UK-based (routed to
  `olena` under the one-company-one-profile exception for in-scope groups, Vadim 2026-09-28). Written
  neutral and title-based (Country Manager), referral angle, no personalization beyond title and
  company.
- **Kilo wave 2 (7 people: Cristina G., Domantas Patinskas, Lina Jasaite, Mohamed Youssef, Tautvydas
  Žalynas, Ugnius Zykas, Žygimantas Surintas)** — all release **one week after Kilo wave 1 (Renata
  Roze) is sent**, not on her connection acceptance, per `release_note` in `people-approved.csv`
  (Vadim 2026-09-28). Noted in each file's Context block.
- **Freeletics wave 2 referral trio (Christian Weber, Estefania Ullrich Gavilanes, Philipp Hagspiel)**
  and **Lifesum wave 2 referral trio (Marcus Gners, Matthias Lenz, Åsa Odell Nordström)** — standard
  wave-2 rule: send after the wave-1 product/retention/technical contacts at the same company.
  Noted in each file's Context block.
- **DoFasting / Keto Cycle** (Kilo's own consumer apps) are named in Domantas Patinskas's Message 1 as
  specific personalization. These are the prospect's own products, not a 3DLOOK client or a
  competitor, and the hypothesis explicitly discusses them by name — not a banned mention. Kilo's
  Bioma supplement brand is not mentioned anywhere (out of scope, anti-case).
- **No compliance / GDPR / "not a medical device" line anywhere in this batch** — judged not required
  (ICP is consumer digital fitness/nutrition, not insurance/healthcare/clinical/online pharmacy).
  Flagging in case Vadim wants the German-market Gymondo insurer-prevention pair to carry a GDPR line
  after all.

## Random sample for Vadim review (5 people)

1. `messages/tomasz-galczynski.md` — Activerse, Co-Founder & CTO, technical-integration (build-vs-buy
   line, single-person group)
2. `messages/danielsobhani.md` — Freeletics, CEO, retention (founder-level primary buyer)
3. `messages/stefanie-schultheis-a8752441.md` — Gymondo, Head of Business Development, insurer-prevention
   (new angle, question-framed)
4. `messages/cristina-g-528824263.md` — Kilo Health, Country Manager, referral, wave 2 (empty profile,
   neutral copy, flagged above)
5. `messages/mohammadalrawi.md` — Lifesum, Director of Data & Analytics, product (headline mismatch,
   flagged above)

## Not done / open items

- Did not run `closelyhq-importer` or any import step, per instructions.
- Did not touch any file belonging to Welltech / BetterMe / Yazio or their `_summary-*.md` files.
- Did not write the campaign-wide `_summary.md` (that aggregation, if wanted across all four agents'
  batches, is for the coordinator to assemble from the four `_summary-*.md` files).
