---
product: fitxpress
type: open-items
vertical: insurance-underwriting
for: Asselya Sekerova (editorial), Vadim (product and commercial), Whitney Cathcart (regulatory)
date: 2026-08-31
---

# Open items — /for-insurance-underwriting/

Editorial guardrail #11: every bent guardrail is surfaced, never silently decided.

## 1 · G-I waiver — Vadim

The vertical has **zero case studies**, which fails G-I outright. The page was drafted under a requested
waiver. Detail and the fallback are in `gate-reports.md`. Nothing is published until this is answered.

## 2 · Two sources conflict on customer naming — Vadim, Whitney

| Source | Says |
|---|---|
| `case-studies/uk-meds.md` | "In compliance-focused outbound (insurance, regulated healthcare): example of audit-ready workflow", and cite as "UK Meds uses FitXpress for BMI verification" |
| `messaging.md` | Key proof phrase: "Trusted by Safariland, Burlington Medical, UK Meds, Yazen" |
| `fitxpress-insurance-underwriting-deck-copy.md`, slide 26 | "Do NOT mention client names (Yazen, UK Meds, Healthyr, etc.) — NDA" |

Guardrail #2 forbids resolving this silently. The page takes the conservative path and **names nobody**.
A yes on naming would materially strengthen the deployment block.

## 3 · The ISO benchmark figures are missing from `proof-points.md` — Vadim

`about-me.md` and the live telehealth page both carry the ISO 8559-1:2017 multi-company benchmark:
session-to-session repeatability 0.40 cm, 14 companies, 8 countries, 27 subjects, 1,152 data points over
4 days. **`proof-points.md` does not list any of it**, and the Kit allows only `proof-points.md` figures,
so the block was dropped.

This is the highest-value item on the list. One row added to `proof-points.md` restores a proof block the
benchmark page already runs, and it is exactly the block an underwriting diligence reviewer looks for.

Note the discipline `about-me.md` sets: the two benchmarks have different references and are **never
combined**. Internal validation gives `< 1 cm`; the ISO benchmark gives 0.40 cm. The page currently uses
only the first.

## 4 · Validation population height range conflicts — Vadim

`proof-points.md` records demographic coverage of 150 to 205 cm. `about-me.md` records the internal
validation population as 150 to 220 cm. Not averaged, not silently picked: the page uses the
`proof-points.md` figure and labels it demographic coverage. One of the two files needs correcting.

## 5 · Publication rights on the 2025 aggregate — Vadim

"112,100 scans across 67 active customers in 2025" is sourced from `proof-points.md`, marked Internal.
The live site publishes "100+ clients" and "$16.2m raised" but no scan volume. Confirm before publish, or
the sentence is cut.

## 6 · `about-me.md` bans price on a page that the Kit requires to carry one — Asselya, Vadim

`about-me.md` → Words and phrases we NEVER use: "**Pricing.** Never state or imply prices."
`kit-vertical-page.md` slot 14 and `CLAUDE.md` §16: "a price signal and a link to `/pricing/` on every
commercial page", because silence about money reads as evasive.

The page includes the price signal, on the grounds that the page rule is newer (2026-08-23), is
page-specific, and that `/pricing/` is already public with the same figures. Recorded rather than decided
quietly.

## 7 · Internal `pricing.md` contradicts the live `/pricing/` page — Vadim

Already recorded in `site-inventory.md` and still unresolved. The page takes the live figures. `pricing.md`
needs re-syncing.

## 8 · Regulatory wording needs Whitney's sign-off

Three sentences carry regulatory weight and were written cautiously:

- "Whether HIPAA obligations reach a given carrier depends on the lines it writes and how it handles
  health information; 3DLOOK signs a Business Associate Agreement where the customer is a covered
  entity." Written this way because guardrail #6 forbids asserting that a framework does not apply, and
  the deck itself flags that a life carrier's HIPAA status varies.
- "Depending on jurisdiction, processing purpose and how the flow is designed, photos and body-derived
  outputs may be treated as personal data, and in some jurisdictions as health data or as biometric
  data."
- The NAIC paragraph.

## 9 · SOC 2 is absent from the page by choice — Vadim

`compliance.md`: "We are NOT SOC 2 certified yet (in progress — confirm with Vadim before claiming)."
`audience.md` lists SOC 2 among the procurement gates for this buyer. The page says nothing about it.
Silence is the safe call today, and it will be the first question a carrier's security review asks.

## 10 · The BD owner was not consulted

G-I asks the market's BD owner to confirm that the objections in this vertical differ from the general
ones. Nick Omelchak owns the US market and was not consulted. The vertical objections on the page come
from `audience.md` §5, `faq.md` and the hub article. Worth 20 minutes with Nick before publish.

## 11 · Deck claims that were deliberately left off the page

`fitxpress-insurance-underwriting-deck-copy.md` carries several claims that break guardrails and were
excluded. Flagged because the deck is in active sales use.

| Deck wording | Why it is not on the page |
|---|---|
| "Best-in-class Repeatability" (slide 6, slide 7 row 3) | Anti-positioning violation, and an automatic hard fail at the page judge |
| "Independently benchmarked against 3D scanners and expert manual measurements" (slide 6) | Guardrail #3 reserved word with no named external party |
| "Validated Methodology" (slide 6) | Same |
| "Outperforms 3D scanners (0.57 cm) and expert manual measurements (0.94 cm)" (slide 6) | Figures absent from `proof-points.md` |
| "Accuracy You Can Trust in Underwriting Workflows" (slide 6 title) | Unscoped accuracy claim, and the Kit requires the "accurate enough for which decision" reframe |

**The deck should be corrected too.** These are the same guardrails that apply to every channel.
