---
program: Fast Company Most Innovative Companies (2027 cycle)
deadline: early rate 2026-09-04, final 2026-10-02
category_recommended: Health
entrant: 3DLOOK Inc
product: mixed
status: DRAFT — not submitted
fee: unconfirmed exact amount, tiered — confirm before submitting (open-questions.md #3)
---

## Application narrative

**What 3DLOOK does:** 3DLOOK turns two smartphone photos into a 3D body model, 80+ body measurements
and body composition data in under 45 seconds, delivered through an API and SDK that health and
apparel companies build directly into their own products. We are not a consumer app. We're the
verification and measurement layer other companies' patients, members and customers touch without
ever seeing our name.

**Why now:** Body scanning is heading toward commodity status as vision foundation models improve, and
we expect that within 12 to 36 months, large platform vendors will ship native body-measurement
primitives. Our answer has been to stop competing on "most accurate scan" and instead build the parts
of the stack that don't commoditize: workflow integration, audit-ready records, longitudinal tracking,
and governance that HIPAA- and GDPR-aligned health customers require before they'll put a scan result
into a clinical or compliance decision. That's the innovation we'd want judged here: a company-level
bet on what stays defensible once the underlying computer vision is everywhere.

**Evidence it's working:** In 2025, 67 active customers ran 112,100 scans through the platform.
Enterprise contracts, deeper integrations rather than one-off usage, now account for $822K of our
$1.084M in annual recurring revenue, a sign that customers are building us into permanent workflows
rather than testing us. On the health side, UK Meds uses scan-based BMI verification inside an
online-pharmacy prescribing flow, and Yazen built it into a weight-loss program that ran 34,000 scans
in 2025. On the apparel side, Safariland has run custom-fit PPE production on our platform for more
than five years, the kind of retention number a "just an API" vendor doesn't get.

**The technology, briefly:** a patented statistical generative human body model trained on 9+ years of
data, 150,000+ photos, 30,000+ 3D scans and 430,000+ individual measurements. It reaches 96-97%
accuracy against manual measurement under standard two-photo capture conditions, with a published
error margin of 1.5-2.0 cm, and repeatability with variance under 1 cm across repeated scans of the
same person.

**What we'd want Fast Company to recognize:** a small team (28 people, $16.2M raised) building the
governance and workflow layer for a category that's about to get crowded by bigger players, proven out
in two very different verticals, health compliance and apparel manufacturing, that most vision-AI
companies never bother to serve at once.

---

## Notes for Vadim

- Ran this through `brand-checker`; revised to remove em dashes and the "not a single feature, but…"
  corrective construction it flagged, and tightened the accuracy/repeatability sentence to the
  `< 1 cm` repeatability convention from `about-me.md` with a capture-condition qualifier, instead of
  bundling accuracy + error margin + repeatability into one unqualified claim.
- Frontmatter uses `product: mixed`, which isn't one of the two defined values in CLAUDE.md §4
  (`fitxpress | mobile_tailor`). This piece genuinely covers both products, so `mixed` may need to be
  approved as a new value for this artifact type rather than forced into one product silo. Confirm.
- Fast Company's application typically wants a specific "what's new in the last 12 months" hook: a
  shipped feature, a new customer segment entered, a milestone crossed. I've used the
  accuracy/repeatability study and the enterprise-ARR mix shift as the closest verifiable "what's new"
  I have in proof-points.md, but if there's a more recent, more submittable news hook (a launch, a
  partnership, a specific 2026 milestone) that isn't in this workspace, give me that and I'll rework
  the middle section around it, rather than implying something happened when I can't verify the date.
- Same category-selection and fee-approval flags as the Stevie draft apply here (open-questions.md
  #3, #4).
