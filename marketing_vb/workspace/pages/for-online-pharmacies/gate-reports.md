---
product: fitxpress
type: vertical-page
vertical: online-pharmacies
status: gates
---

# Online pharmacies landing: intake, G-I, G-A (2026-11-09)

Decision (Vadim, 2026-11-09): the BMI verification page is a feature page that explains and routes, so online
pharmacies get their own selling landing, UK-led. Reverses the 2026-10-22 note that the BMI page supersedes a
pharmacy page (`landing-map.md`, `site-inventory.md` updated in 6988db2).

## Phase 0 · Intake

| Field | Answer |
|---|---|
| Page type | Use-case (vertical) page, vertical Kit |
| Product | fitxpress |
| Vertical | Online pharmacies and digital prescribers dispensing weight-loss medication; UK first (GPhC), written to work for EU later |
| Use-case file | `brand-assets/product-info/use-cases/fx-online-pharmacy-bmi.md` (exists) |
| Buyer | Head of Compliance & Risk, Head of Clinical Governance, Chief Pharmacist / Superintendent Pharmacist, Clinical Operations Director; product and CTO for integration (`icp-detail.md` §2) |
| Intent | BOFU. Traffic comes from outbound to UK pharmacies (profile `katerina`), sales follow-ups, the compliance-guide article and the BMI feature page, not from search (see G-I demand) |
| Place in the site | `/for-online-pharmacies/` at the root until `/fitxpress/` ships, then `/fitxpress/for-online-pharmacies/` (301), as with insurance |
| Conversion | "Book a demo", shared HubSpot form `FX \| LP \| Demo` at `#demo`, `fx_vertical` via GTM |
| Proof | UK Meds logo first in the shared logo row (logos approved 2026-10-21; no case study, no name in the copy); `proof-points.md`: under 45 seconds, weight ≈3.5% MAE under evaluated conditions; accuracy framework; trust FAQ |
| Language | English; UK regulatory context |

## G-I · Should this page exist

- [x] **Use-case file** exists.
- [x] **Cases:** standing FX waiver 2026-09-27 (logos only). UK Meds is the one production BMI-verification client; its
      logo goes first. `G-I: standing FX waiver 2026-09-27`.
- [x] **Five facts not on the parent (the BMI feature page):**
  1. GPhC distance-selling guidance (February 2025) requires independent verification of weight, height and/or BMI
     before weight-loss medication is supplied remotely (verified 2026-10-07, `for-glp-1-programs/sources-problem-block.md`).
  2. GPhC review (April 2026): 1,307 concerns from January 2024 to December 2025; inadequate BMI verification was the
     third most reported (11%), and the public raised easily manipulated photographs (same file).
  3. The order-flow pattern: the scan runs at checkout when weight-loss treatment is ordered; the patient sees "Your
     photos are submitted" and no body metrics; the prescriber reviews the result (`case-studies/uk-meds.md`, pattern B;
     described without naming the client).
  4. Re-order and refill checks: the same capture at each re-order, compared with the previous one (to confirm with
     product before it goes on the page).
  5. UK GDPR roles: the pharmacy is the controller, 3DLOOK the processor, with a DPA including SCCs and the UK Addendum
     (`compliance.md` §2).
- [~] **Demand.** Search demand from pharmacy buyers is effectively zero (Ahrefs 2026-11-09: GB "bmi verification" 0,
      "gphc weight loss" 0, "online pharmacy bmi" no data; US "bmi verification software" no data). The page is a
      conversion destination for outbound and sales, measured by demo requests, not organic traffic. Passes on that
      basis; recorded so the Phase 7 review measures the right thing.
- [x] **60% uniqueness against the BMI feature page:** achievable. The BMI page stays generic (how the feature works,
      methods, routing); this page carries GPhC, the order flow, prescriber review, re-orders and UK GDPR. Rule for both
      pages: the BMI page's pharmacy card does not retell GPhC.

**G-I: pass** (waiver + demand note).

## G-A · Architecture

- [x] **Parent, URL, siblings.** Parent `/fitxpress/` (not live) → root URL for now. Siblings: `/for-bmi-verification/`
      (feature page, links down here), telehealth, GLP-1 (planned), insurance. **Needs Vadim's OK.**
- [x] **Cannibalisation.** The compliance guide (`/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/`)
      already carries "Online Pharmacy BMI Verification" in its title and owns the informational intent. The landing
      does not use that phrase as its H1 or title head. With zero measured demand on every phrase, the risk is low in
      practice; the split is still kept clean.
- [x] **Inbound links named:** the BMI page's pharmacy card; the compliance guide (relink from `/for-bmi-verification/`
      when this ships); the landing-map row for pharmacy articles in any hub; UK outbound sequences.
- [x] **Search Console baseline:** new URL, none. The BMI page's baseline is in
      `workspace/pages/bmi-verification/keywords-2026-11-09.md`.

**Proposed angle:** a second, live-captured weight source inside the order flow, so the pharmacy can check
self-reported weight before a prescriber approves weight-loss medication, with a record for inspection. Lead with
compliance and defensibility, not accuracy (use-case file). Boundaries: the prescriber decides; "FitXpress is not a
medical device"; never "meets GPhC requirements" or "GPhC compliant".

**Proposed H1 (formula: product + audience + outcome):**
- A. "FitXpress for online pharmacies: check self-reported weight inside the order flow"
- B. "FitXpress for online pharmacies: a second weight source before weight-loss prescribing"

**Title draft:** "Weight & BMI Verification for Online Pharmacies | FitXpress" (59).

**Checkpoint (Vadim): URL, angle, H1, and who drafts (Nika as on other use cases, or page-builder here).**
