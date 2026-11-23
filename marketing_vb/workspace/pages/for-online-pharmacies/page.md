---
product: fitxpress
type: use-case
vertical: online-pharmacies
status: gate-not-taken-75
url: https://3dlook.ai/for-online-pharmacies/
canonical: self
moves_to: https://3dlook.ai/fitxpress/for-online-pharmacies/ (301 when /fitxpress/ ships)
language: en (US house spelling, as on the fitness page)
title: "Order-Flow Weight Checks for Online Pharmacies | FitXpress"
meta_description: "Weight checks for online pharmacies: FitXpress adds a weight estimate from photos taken live at checkout, for the prescriber to review before supplying."
h1: "FitXpress for online pharmacies: a live weight check before weight-loss prescribing"
focus_keyphrase: weight checks for online pharmacies
structure_benchmark: live /fitxpress/for-connected-and-digital-fitness/ (block order captured 2026-11-23) + page-final-2026-10-07.html (components)
register_benchmark: workspace/pages/for-insurance-underwriting/page-final-2026-10-02.md
facts: fact-sheet.md
date: 2026-11-23
---

<!-- Builder notes are in HTML comments; the copy is everything else. page.html is the prototype of the
     same copy in the fitness template. If the two differ, this file wins until design takes over.
     Round 2 (2026-11-23): judge round 1 = 73, fixes per the coordinator's rulings; block order unchanged.
     Round 3 (2026-11-23): judge round 2 = 71, fixes per the coordinator's rulings; one anchor #demo. -->

## Yoast

| Field | Value | Length |
|---|---|---|
| SEO title | `Order-Flow Weight Checks for Online Pharmacies \| FitXpress` | 58 / 60 |
| Meta description | `Weight checks for online pharmacies: FitXpress adds a weight estimate from photos taken live at checkout, for the prescriber to review before supplying.` | 152 / 155 |
| Focus keyphrase | `weight checks for online pharmacies` (title, meta description, lede) | |
| Canonical | `https://3dlook.ai/for-online-pharmacies/` (self) | |
| Breadcrumb | Home → FitXpress for Online Pharmacies (no middle level while `/fitxpress/` 301s to `/`) | |

---

<!-- 1 · HERO -->
**Eyebrow:** FitXpress for online pharmacies

# FitXpress for online pharmacies: a live weight check before weight-loss prescribing

Each weight-loss order can reach the prescriber with a dated weight estimate from photos taken live during
the order, and the pharmacy can keep that record for inspections and concerns. FitXpress adds this weight
check to the online pharmacy's order flow, on the patient's own phone.

**Primary:** [Book a demo](#demo) · **Secondary:** [See what the prescriber receives →](#record)

**Under the button:** A phone walkthrough with a sample record.

**[HERO] mock, order timeline (no body values, no patient data):** header "Order record · weight-loss
treatment". Rows: 10:24:05 Order placed, declared weight entered (pharmacy) · 10:25:12 Scan uploaded
(FitXpress) · 10:25:31 Results ready, weight estimate returned (FitXpress) · 10:25:31 Smart Scales
mismatch flag raised (FitXpress) · 10:25:32 Sent to prescriber review (pharmacy rule). Highlight line:
"Prescriber decision: pending". Caption: *Illustrative example. Order, routing and decision steps belong
to the pharmacy's system; FitXpress returns the scan status, timestamps and the Smart Scales result.*

**Proof strip:**

| 2 photos | Under 45 sec | Order and re-order | No integration fee |
|---|---|---|---|
| taken live on the patient's own phone | from the photos to structured results | the same check at both steps | plans from $1,000 a month |

**[LOGOS] row:** caption "100+ clients have used 3DLOOK body scanning since 2016, including an online
pharmacy." UK Meds first (logo approved 2026-10-21; no name or metric in the copy), then the shared
client strip of the live use-case pages. Alt text = client name.

---

<!-- 2 · VALUE · for patients -->
**Eyebrow:** For patients

## A weight check patients finish while they order

- **No appointment to book.** The check happens at checkout, during the order itself.
- **On their own phone.** Patients scan inside the pharmacy's website or app, guided on screen.
- **A short confirmation screen.** The pharmacy decides what patients see after the scan, for example only
  a confirmation that the photos are submitted.
- **Simpler re-orders.** Where the pharmacy's rules allow, a fresh two-photo check at a re-order can
  replace a separate request for evidence.

The feature behind the check: [remote BMI verification →](https://3dlook.ai/for-bmi-verification/)

**Button:** [See the patient flow in the demo](#demo)

---

<!-- 3 · PROBLEM · [CONTEXT] -->
**Eyebrow:** The problem

## Why does declared weight put online pharmacies at risk?

Since February 2025, [General Pharmaceutical Council (GPhC) guidance](https://assets.pharmacyregulation.org/files/2025-02/gphc-guidance-registered-pharmacies-providing-pharmacy-services-distance-february-2025.pdf)
has said that, when supplying weight management medicines such as glucagon-like peptide-1 (GLP-1)
treatments, the prescriber verifies "the person's weight, height and/or body mass index" using "a different
way to verify the information provided to them by the person". An order supplied on
declared weight alone is therefore a prescribing decision the pharmacy may have to defend at inspection or
in answer to a concern.

| 1,307 | 11% |
|---|---|
| concerns about weight management medicines and services reached the GPhC between January 2024 and December 2025 | of concerns were about inadequate BMI verification, the third most reported area; public examples included photographs that could be easily manipulated |

Source for both: [General Pharmaceutical Council, "Weight management medicines and services: a review of GPhC inspections and concerns"](https://assets.pharmacyregulation.org/files/2026-04/Weight-management-medicines-and-services-a-review-of-GPhC-inspections-and-concerns-April-2026.pdf)

FitXpress adds one input to that check: a weight estimate from photos taken live in the order flow,
calculated with the height the patient enters. Whether that estimate, alone or with other checks, meets the
pharmacy's process is the pharmacy's decision.

GPhC guidance in depth:
[Online pharmacy BMI verification: a 2026 compliance guide →](https://3dlook.ai/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/)

---

<!-- 4 · WHAT THE PRESCRIBER RECEIVES · id="record" · five tiles, H3 each · moved before How it works by Vadim's decision 2026-11-23 (value before mechanics) -->
**Eyebrow:** The scan record

## Each scan adds a second weight source to the order record

FitXpress returns one timestamped record per scan; the pharmacy chooses which fields the prescriber sees.

- **Weight estimate.** FitXpress Smart Scales estimates weight from the photos and the entered height. The
  prescriber reads it beside the declared weight.
- **Mismatch flag.** The clinical team sets a threshold. A difference beyond it flags the record, and
  prescribers start there; the cause is theirs to judge.
- **Calculated BMI.** FitXpress returns BMI already calculated from the estimate and the entered height.
- **Status and timestamps.** Every record carries processing status and timestamps, which show when the
  check ran if an inspector asks.
- **Admin Panel.** Failed-scan messages and photo-deletion dates sit in the optional FitXpress Admin
  Panel, ready for compliance staff to look up.

FitXpress is not a medical device. It adds evidence to the order; the prescriber decides whether to
supply.

**Button:** [See a sample record in the demo](#demo)

---

<!-- 5 · HOW IT WORKS · [WORKFLOW] -->
**Eyebrow:** How it works

## The check runs inside the order flow the pharmacy already has

Pharmacies embed FitXpress through web and mobile software development kits (SDKs), including supported
iOS and Android integrations.

1. **The patient scans where the pharmacy places the check.** That can be checkout, a re-order, or during or
   straight after an online consultation, with consent and instruction screens in the pharmacy's own wording.
2. **Real-Time Pose Validation (RTPV) guides the capture.** Patients follow on-screen pose and framing
   guidance while they take both photos live.
3. **The result reaches the prescriber with the order.** The pharmacy's system pulls the record through the
   FitXpress application programming interface (API) into its patient medication record (PMR), prescriber
   dashboard or order management, linked by scan identifier to the patient and the order.

**Recommended setup:** the SDK together with the API, because pose and framing validation runs in the
SDK's capture layer.

**Button:** [Book a demo](#demo)

---

<!-- 6 · COMPARE · table on desktop, one card per option on mobile -->
**Eyebrow:** Compare

## FitXpress compared with manually reviewed weight evidence

| Dimension | FitXpress in the order flow | Manually reviewed evidence |
|---|---|---|
| Where the evidence comes from | Two photos taken live in the capture flow during the order | A scale photo the patient sends, a video consultation or clinical records |
| Where the check sits | At checkout, before the order reaches the prescriber | After the order, in a separate review step |
| What the prescriber gets | A weight estimate, a mismatch flag and calculated BMI | The evidence itself, assessed by the reviewer |
| What the order record keeps | Processing status and timestamps for each scan | What the reviewer writes down |
| At a re-order | The same scan, started from the re-order | The review step repeats |

For an online pharmacy, the evidence belongs with the order, captured live and in the same format every
time. Manual review still suits patients who cannot complete the scan, and the two can run together: the
scan can sit during or straight after a video consultation.

**Button:** [See the order flow in the demo](#demo)

---

<!-- 7 · PROOF + TRUST · [ACCURACY] [COMPLIANCE] -->
**Eyebrow:** Proof and data handling

## How accurate is the weight estimate, and how is patient data handled?

Smart Scales estimates weight with approximately 3.5% mean absolute error under evaluated conditions.
The clinical team sets the mismatch threshold with that error in mind. FitXpress is not equivalent to a
calibrated scale when the prescribing protocol requires one.

| 3.5% |
|---|
| approximate mean absolute error of the Smart Scales weight estimate, under evaluated conditions |

The figure comes from an internal study. Peer review and third-party clinical certification are not part
of that record, and the full methodology is available under a non-disclosure agreement (NDA). FitXpress
was not specifically trained on data representing people with physical disabilities, and its measurement
performance has not been established for this population. Those patients follow the pharmacy's
alternative route.
[Body scanning accuracy: an enterprise framework →](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/)

- **Photos.** FitXpress deletes photos immediately after processing or within 30 days under a
  customer-specific policy. Retained photos are blurred, and face obfuscation is applied during capture.
- **Identifiers.** Scan records use anonymized, randomly generated identifiers.
- **Data protection.** Where the UK General Data Protection Regulation (UK GDPR) applies, 3DLOOK provides
  a data processing agreement (DPA) that includes Standard Contractual Clauses (SCCs) and the UK
  Addendum. In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as
  the data processor under GDPR.
- **Encryption.** Data is encrypted in transit and at rest.
- **Model training.** 3DLOOK does not use production customer data to train its models without the
  customer's explicit, documented authorization.

The [Data, Privacy, Security & Regulatory FAQ](https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/)
covers medical-device status and System and Organization Controls 2 (SOC 2). Privacy contact:
[privacy@3dlook.me](mailto:privacy@3dlook.me)

---

<!-- 8 · PILOT + PRICE · prices re-read on the live /pricing/ 2026-11-23 -->
**Eyebrow:** Pilot and pricing

## A pilot starts on a share of weight-loss orders, then scales on a fixed monthly plan

FitXpress runs on
production infrastructure already deployed in remote
[BMI-verification](https://3dlook.ai/for-bmi-verification/) and
[weight-management](https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/)
workflows.

**Starter.** $1,000 a month for 500 API requests, including the Smart Scales weight estimate.

**Pro.** $1,500 a month for 1,000 API requests.

Each scan is one API request, which means the plan follows the number of checks run. Both include guided implementation support, with no integration fee. Custom plans cover higher volumes.
[See pricing →](https://3dlook.ai/pricing/)

1. **Walkthrough.** 3DLOOK shows the order flow and a sample record, then maps the integration to the
   existing checkout.
2. **Pilot on a share of orders.** Some weight-loss orders add the scan while a comparable share keeps
   the current flow. Every order keeps its existing verification. Where practical, orders are
   assigned randomly.
3. **Evaluate and roll out.** Outcomes are measured against criteria agreed with the superintendent
   pharmacist and compliance lead. If they are met, the scan goes live for orders and re-orders.

3DLOOK and the pharmacy track:

- scan completion and retake rates
- checkout completion against the comparison group
- orders flagged for prescriber review
- time from order to prescriber decision

**Button:** [Book a demo](#demo)

---

<!-- 9 · FAQ · FAQPage schema, answers text-identical in JSON-LD -->
**Eyebrow:** FAQ

## Questions online pharmacy teams ask

### Does FitXpress verify the patient's height?
No. The patient enters height, which FitXpress uses with the two photos to estimate weight and calculate
BMI. Where the prescribing protocol needs more than the patient's own figure, that check sits outside
FitXpress.

### Can the scan run during an online consultation?
Yes, as one placement the pharmacy can choose. The patient takes the two photos on their own phone during
or straight after the consultation, and the prescriber can see the result in the same session. The
prescriber still decides, and the pharmacy judges whether the combined check meets its process.

### How does FitXpress connect to the pharmacy's checkout?
The pharmacy's developers add the SDK capture step to the checkout and call the FitXpress API from their
own back end. Integration details are covered in the [FitXpress API
documentation](https://docs.fitxpress.3dlook.me/).

### Where is patient data hosted, and how long are results kept?
FitXpress data is hosted on Amazon Web Services (AWS), primarily in the US-West-2 region and partially in
US-East-1. Scan outputs are retained on an ongoing basis unless the agreement says otherwise, and the
compliance team can request deletion by scan identifier.

Related pages: [remote BMI verification](https://3dlook.ai/for-bmi-verification/) ·
[remote body measurement for telehealth](https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/)

---

<!-- 10 · FORM · id="demo" (Kit and landing-map anchor; every button points here) with a #form alias for the live template · shared HubSpot form FX | LP | Demo
     (portalId 6014382, formId 11acb23a-e81c-46ee-bb23-4d47a0ef0125), GTM fx_vertical = online-pharmacies -->
**Eyebrow:** Book a demo

## The demo shows FitXpress in the order flow

We walk the order flow with a sample record and scope a pilot.

Not ready for a call? [Start with the online pharmacy compliance guide](https://3dlook.ai/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/).

**Form:** shared `FX | LP | Demo` (work email, company, job title, optional "Expected monthly scan
volume", consent). No page-specific fields.

**Footer:** FitXpress for online pharmacies · Procurement and security documentation:
[legal@3dlook.me](mailto:legal@3dlook.me)

---

## Schema markup

<!-- Yoast supplies WebPage, WebSite, Organization and BreadcrumbList; add Service and FAQPage on top and
     check the Yoast breadcrumb matches the two-level list below. The WebPage node here only wires
     about / mainEntity / hasPart / mentions to Yoast's WebPage @id. FAQ answers are text-identical to the
     page. Entity @ids reused from docs/schema-entities.csv; every @id in "mentions" is defined in this graph as a
     DefinedTerm in the 3DLOOK Entity Inventory set, as on the live insurance and fitness landings (2026-11-23 check:
     those @ids are not defined on their own URLs, so they must be defined here). -->

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://3dlook.ai/for-online-pharmacies/",
      "url": "https://3dlook.ai/for-online-pharmacies/",
      "name": "Order-Flow Weight Checks for Online Pharmacies | FitXpress",
      "description": "Weight checks for online pharmacies: FitXpress adds a weight estimate from photos taken live at checkout, for the prescriber to review before supplying.",
      "isPartOf": {
        "@id": "https://3dlook.ai/#website"
      },
      "publisher": {
        "@id": "https://3dlook.ai/#organization"
      },
      "inLanguage": "en",
      "about": {
        "@id": "https://3dlook.ai/for-online-pharmacies/#fitxpress-online-pharmacy-service"
      },
      "mainEntity": {
        "@id": "https://3dlook.ai/for-online-pharmacies/#fitxpress-online-pharmacy-service"
      },
      "hasPart": {
        "@id": "https://3dlook.ai/for-online-pharmacies/#faq"
      },
      "breadcrumb": {
        "@id": "https://3dlook.ai/for-online-pharmacies/#breadcrumb"
      },
      "mentions": [
        {
          "@id": "https://3dlook.ai/#smart-scales"
        },
        {
          "@id": "https://3dlook.ai/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/#bmi"
        },
        {
          "@id": "https://3dlook.ai/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/#bmi-verification"
        },
        {
          "@id": "https://3dlook.ai/#rtpv"
        },
        {
          "@id": "https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/#accuracy"
        }
      ]
    },
    {
      "@type": "Service",
      "@id": "https://3dlook.ai/for-online-pharmacies/#fitxpress-online-pharmacy-service",
      "name": "FitXpress for online pharmacies",
      "url": "https://3dlook.ai/for-online-pharmacies/",
      "provider": {
        "@id": "https://3dlook.ai/#organization"
      },
      "brand": {
        "@type": "Brand",
        "name": "FitXpress"
      },
      "serviceType": "Smartphone weight estimate for online pharmacy order flows",
      "category": [
        "Online pharmacy",
        "Weight-loss medication supply",
        "Weight check before prescribing",
        "Mobile body scanning"
      ],
      "description": "FitXpress adds a weight estimate from two guided smartphone photos, taken live at checkout together with the height the patient enters, to an online pharmacy's order flow, with a mismatch flag against the declared weight, BMI calculated from the entered height, and processing status and timestamps, as evidence for the prescriber's review.",
      "audience": {
        "@type": "BusinessAudience",
        "audienceType": "Online pharmacies and digital prescribing services supplying weight-loss medication"
      },
      "areaServed": {
        "@type": "Country",
        "name": "United Kingdom"
      },
      "serviceOutput": [
        "Smart Scales weight estimate",
        "Mismatch flag against the declared weight",
        "BMI calculated from the entered height",
        "Processing status and timestamps"
      ]
    },
    {
      "@type": "FAQPage",
      "@id": "https://3dlook.ai/for-online-pharmacies/#faq",
      "url": "https://3dlook.ai/for-online-pharmacies/#faq",
      "name": "Questions online pharmacy teams ask",
      "isPartOf": {
        "@id": "https://3dlook.ai/for-online-pharmacies/"
      },
      "about": {
        "@id": "https://3dlook.ai/for-online-pharmacies/#fitxpress-online-pharmacy-service"
      },
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Does FitXpress verify the patient's height?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No. The patient enters height, which FitXpress uses with the two photos to estimate weight and calculate BMI. Where the prescribing protocol needs more than the patient's own figure, that check sits outside FitXpress."
          }
        },
        {
          "@type": "Question",
          "name": "Can the scan run during an online consultation?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes, as one placement the pharmacy can choose. The patient takes the two photos on their own phone during or straight after the consultation, and the prescriber can see the result in the same session. The prescriber still decides, and the pharmacy judges whether the combined check meets its process."
          }
        },
        {
          "@type": "Question",
          "name": "How does FitXpress connect to the pharmacy's checkout?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The pharmacy's developers add the SDK capture step to the checkout and call the FitXpress API from their own back end. Integration details are covered in the FitXpress API documentation."
          }
        },
        {
          "@type": "Question",
          "name": "Where is patient data hosted, and how long are results kept?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "FitXpress data is hosted on Amazon Web Services (AWS), primarily in the US-West-2 region and partially in US-East-1. Scan outputs are retained on an ongoing basis unless the agreement says otherwise, and the compliance team can request deletion by scan identifier."
          }
        }
      ]
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://3dlook.ai/for-online-pharmacies/#breadcrumb",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://3dlook.ai/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "FitXpress for Online Pharmacies",
          "item": "https://3dlook.ai/for-online-pharmacies/"
        }
      ]
    },
    {
      "@type": "DefinedTermSet",
      "@id": "https://3dlook.ai/#entity-inventory",
      "name": "3DLOOK Entity Inventory",
      "publisher": {
        "@id": "https://3dlook.ai/#organization"
      }
    },
    {
      "@type": "DefinedTerm",
      "@id": "https://3dlook.ai/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/#bmi-verification",
      "name": "BMI verification",
      "description": "BMI verification is a workflow that uses body data inputs to support verification of BMI-related information in digital programs.",
      "url": "https://3dlook.ai/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/",
      "inDefinedTermSet": {
        "@id": "https://3dlook.ai/#entity-inventory"
      }
    },
    {
      "@type": "DefinedTerm",
      "@id": "https://3dlook.ai/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/#bmi",
      "name": "BMI",
      "description": "BMI (Body Mass Index) is a calculated ratio based on height and weight used as a general body-size indicator.",
      "url": "https://3dlook.ai/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/",
      "inDefinedTermSet": {
        "@id": "https://3dlook.ai/#entity-inventory"
      }
    },
    {
      "@type": "DefinedTerm",
      "@id": "https://3dlook.ai/#smart-scales",
      "name": "Smart Scales",
      "description": "Smart Scales is a FitXpress feature that provides estimated weight data within the FitXpress body-data workflow.",
      "url": "https://3dlook.ai/",
      "inDefinedTermSet": {
        "@id": "https://3dlook.ai/#entity-inventory"
      }
    },
    {
      "@type": "DefinedTerm",
      "@id": "https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/#accuracy",
      "name": "accuracy",
      "description": "Measurement accuracy is the difference between the system's output and the chosen reference's estimate of the true value, which is never directly observable.",
      "url": "https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/",
      "inDefinedTermSet": {
        "@id": "https://3dlook.ai/#entity-inventory"
      }
    },
    {
      "@type": "DefinedTerm",
      "@id": "https://3dlook.ai/#rtpv",
      "name": "Real-Time Pose Validation",
      "description": "Real-Time Pose Validation is a capture-quality feature that checks user positioning and framing during image capture to support successful scanning.",
      "url": "https://3dlook.ai/",
      "inDefinedTermSet": {
        "@id": "https://3dlook.ai/#entity-inventory"
      }
    }
  ]
}
```
