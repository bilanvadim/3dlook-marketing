# Pricing — FitXpress

## Recommended pricing (per request, tier-based)

| Requests / month | Subscription / month | Per-request rate | Per-request over limit |
|------------------|----------------------|------------------|------------------------|
| 500 | $1,000 | $2.00 | $2.00 |
| 1,000 | $1,500 | $1.50 | $1.50 |
| 2,500 | $3,125 | $1.25 | $1.25 |
| 5,000 | $5,000 | $1.00 | $1.00 |
| 10,000 | $7,500 | $0.75 | $0.75 |
| 20,000 | $10,000 | $0.50 | $0.50 |

Custom pricing available above 20K/mo.

**No integration fee** (Vadim, 2026-09-30). Public: say it on pages, in outbound and in posts. It is an
advantage over competitors. Page wording: "Plans start at $1,000 a month for up to 500 scans, with no
integration fee."

## How a customer starts (no self-serve trial)

Vadim, 2026-10-14. There is no trial before the contract.

1. **Demo call.**
2. **Demo page access.** After the call, the prospect gets a demo page to walk through the flow and run
   scans themselves. Typically 2 weeks and 100 scans.
3. **First month free, after the contract is signed.** Up to 200 scans for integration and testing, with
   full SDK access (Android, iOS, React, API). There is no sandbox, so this month is where the customer
   tests against the production API.
4. **Paid plan.** Billing follows the plan and the monthly request volume (table above).

Open question: does the 200 in month one count only scans, or every billable request? Goal models and
progress comparisons draw from the same API limit as scans.

Never call any of this a "free trial". On site pages the action is "Book a demo" (Vadim, 2026-09-27).

**Public copy has no figures (Vadim, 2026-10-14).** Pages, posts and client-facing text may describe the
path (demo call → hands-on demo access → free first month after signing → plan) but never name the
2 weeks, the 100 scans or the 200 scans. Sales keeps these flexible per deal.

## How agents should use pricing in messaging

- **Don't lead with price** in cold outbound. Lead with outcome / business case.
- **Use range hint** if budget is the conversation: "Pricing scales from ~$1K to ~$10K/month depending on volume."
- **Never offer a "free trial" in outbound** (message-sequencer rule 5; `outbound_pack.py` blocks the phrase).
  The ask is a demo call. Demo access and the free first month come after it, from sales.
- **If buyer asks specific tier price** — give the exact number from the table above.

## Mobile Tailor pricing

Mobile Tailor pricing is custom (enterprise contract). Reference internal customer ARRs for anchoring:
- Safariland: $256K ARR
- Burlington Medical: $309K ARR
- Generation Tux: $77K ARR
- Jim's Formal Wear: $51K ARR

In outbound, do NOT cite specific MT customer ARRs publicly. Use these only for sales conversations and pricing benchmarks.
