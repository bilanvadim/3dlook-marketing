---
product: fitxpress
type: vertical-page
vertical: clinical-trials
status: review
source: Nika's two drafts + Asselya's chat-edited version (Slack #marketing, thread 1793092031.104189, 2026-10-27)
---

# Gate reports: clinical trials landing, review of three drafts (2026-10-28)

Inputs, all from the #marketing thread of 2026-10-27:

| Draft | File | Angle |
|---|---|---|
| A, Nika | `nika-v3-2026-10-27.html` | the hub's angle: standardize the measurement workflow across sites, move measurement-only visits to remote check-ins, audit-ready records, remote BMI pre-check |
| B, Nika | `nika-v2-2026-10-27.html` | her own repositioning: an additional body measurement between site and imaging visits, white-label inside the participant app or DCT platform; drops "more consistent than manual" |
| C, Asselya | `asselya-v4-2026-10-27.html` | B run through ChatGPT against the keyword map and guardrails: shorter, hedged, BELIEVE and FDA cost removed, pricing and pilot block removed |

## Decisions by Vadim (2026-10-28)

1. **The hero and value cards are written for DCT platforms** (DCT, eCOA and participant-app vendors as
   integration partners). Sponsors and CROs are served by the problem block, the methods comparison and the FAQ.
   Base = draft B plus Asselya's edits; draft A's standardization angle is dropped.
2. **`use-cases/fx-clinical-trials.md` is not rewritten.** The page holds the between-visits module angle, and
   the use-case file's promises (standardization, retention, screen failures) do not move onto it.
3. Review and sources file go to Nika's thread; the folder is committed.

Nika's own doubt in the thread: no clinical trial clients in the CRM, research only, "not sure how well we fit
this heavily regulated field; for me this is one of the weakest pages".

## G-I · should the page exist: PASS on the standing FX waiver, weakest vertical so far

- Use-case file: `use-cases/fx-clinical-trials.md` exists. Its hero ("standardize anthropometrics across sites
  and reduce visit burden to improve data quality and retention") and KPIs (site variability, coordinator
  time, retention, screen-failure rate, audit readiness) are outcomes nothing in `proof-points.md` supports.
  Draft B already walks away from them. The file needs to follow whichever angle is approved.
- Cases: `G-I: standing FX waiver 2026-09-27`. No clinical trial client, no CRM contact, no sales conversation.
  The logos (Yazen, UK Meds, Healthyr) are weight-management and pharmacy clients.
- Demand: content-plan Hub 7, landing-map row 7. Keyword map §8: primary phrase has no measured demand; the
  DCT-platform cluster has ~410 US searches a month (CPC $12); the hub got 1 impression in 3 months.
- Facts not on the parent: DCT / eCOA / EDC boundary, protocol-defined schedules, results hidden from
  participants, sponsor-decided use of the data, DXA / MRI in a subset, FDA DHT guidance on fit-for-purpose
  verification. Enough for the 60% rule.
- BD owner: not asked. `competitors.md`: Size Stream Health (since July 2026) names clinical trials as a target.
- `audience.md` has no clinical-trials segment layer, so there is no "what NOT to say" list for this buyer.

## G-A · architecture: PASS with one note for publishing

- URL `/fitxpress/for-clinical-trials/` = landing map = all three canonicals. `/fitxpress/` is not live, so the
  insurance precedent applies (root URL until `/fitxpress/` ships, then a 301). Decide on the day.
- Cannibalisation: the hub's live SEO title on 2026-10-28 is "Standardizing Anthropometric Measurements in
  Obesity Trials", so the keyword-map title conflict is already gone. The content plan gives the hub "site-to-site
  variability, hybrid and remote check-ins, operational standardization, structured records, audit-readiness".
  Draft A is that premise retold: high cannibalisation and the blog test fails block by block. B and C sit on
  the DCT-integration and between-visit angle, which the hub does not own (the DCT integration article is an
  unwritten P1): low risk.
- Primary keyword `remote anthropometric measurement for clinical trials`: only C's title carries it
  ("Remote Anthropometric Measurements for Clinical Trials | FitXpress", 66 characters, over 60). A's title
  "Anthropometric Capture…" and B's "White-Label Body Scanning…" miss it. None has "DCT platform" in H1/H2
  except C's H2 "…to a DCT platform or participant app".
- Inbound links: the hub's landing-map "Link now" is `/`; relink to this page when it is live.
- GSC baseline: new URL, none.

## Mechanical checks

| Check | A (Nika v3) | B (Nika v2) | C (Asselya v4) | Rule |
|---|---|---|---|---|
| Visible words, hero to form, table once | ~3,150 | ~2,910 | ~2,070 | 1,100-1,600 |
| FAQ | 10 | 10 | 5 | 4-6 |
| H2 count | 12 | 11 | 11 | kit: 10 blocks |
| you/your per 1,000 | 0 | 0 | 1.0 | ≤ 12.5 |
| H1 = product + audience + outcome | yes (16 words) | yes (16 words) | no product in H1 | kit sales rule 1 |
| Yoast title / description | 54 / 145 | 57 / 144 | **66 / 160** | ≤ 60 / ≤ 155 |
| Service `areaServed` | yes | yes | yes | |
| Detector `--channel page` (visible copy) | "platform decides" (anthropomorphism) | "platform decides" | 6 en dashes (96–97%, 1.5–2.0 cm), "replace DXA" (FAQ H3) | 0 hard fails |
| Bare percentage | mock 41.3% → 39.8% (labelled illustrative) | same + 92.8% | mock only | |
| `[PLACEHOLDER]` comments | 2 | 1 | 1 | 0 |
| Author notes in HTML comments | yes (long) | yes (long) | no | strip before publishing |
| Form | `/contact-us/` form `f227f5ce` | same | same | shared `FX \| LP \| Demo` |
| Price signal | Starter / Pro tiers, "scans" | same | none, no `/pricing/` link | name the entry tier, link `/pricing/` |
| Hero at 1280×800, layout at 375 | not measured | OK / OK | OK / OK | |

## Fact check against the product files (detail in `fact-sheet.md`)

Unsourced in all three: **"React Native"** (`tech-spec.md`: do not write it). Unsourced in A and B, already cut
from the fitness page on 2026-10-06 for the same reason: offline capture in native kits, webhooks without retries
or signature verification, iOS 15+, older Android with lower frame rate, standing-only, two gender options,
"height difference above 2 cm affects results". B also: "version requirements agreed before the study starts".

Claims above the product: A's "Audit-ready records" and "records support ICH E6(R3) documentation
expectations" (no audit trail, no Part 11 documentation); A's remote BMI pre-check (BMI comes from entered
height and weight, so the scan adds nothing to it); A and B "supports blinded study designs" (the platform hides
results, the product does nothing); A and B "capture source" in the record (unconfirmed field).

C's regulatory lines drop the canonical sentences: no "FitXpress is not a medical device", and "The current
regulatory assessment applies to the product's assessed intended purpose" replaces the UK MDR / EU MDR line.
C also drops the validation population and "under NDA" from the accuracy block.

Third-party statistics: `sources-problem-block.md`.
