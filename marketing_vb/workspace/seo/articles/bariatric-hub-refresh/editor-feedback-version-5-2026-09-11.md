# Bariatric hub, Version 5 (style): what still needs fixing

**For:** Assel Sekerova
**From:** Vadim Bilan, marketing
**Date:** 2026-09-11
**Document:** [Rewrite - Bariatric Pre-Qualification and Patient Progress Tracking](https://docs.google.com/document/d/15bydjzHTEHhHt5LAapc4iqTsIAdcWUMtn4ryu9E4SHo/edit?tab=t.axdvdo5fl68b), tab "Version 5 (style)"

Version 5 reads much better, and most of Review 4 landed well. A few things still stand between it
and publication. Section 1 lists what breaks a content rule or an approved fact. Section 2 needs a
decision. Section 3 is minor.

**How it was checked:** our article linter and AI-tells detector; every number against the
approved claims and sources for this article; every compliance statement against our approved
compliance wording; and every link opened.

---

## 1. Must fix

### 1.1 Two links point to ChatGPT, not to the source

- **GLP-1 section, the JAMA Surgery citation.** The link is `https://chatgpt.com/g/...`. Please link
  the paper: `https://doi.org/10.1001/jamasurg.2026.1343`.
- **Patient progress section, "AI in telehealth".** The link is `https://chatgpt.com/g/...`. Please
  use `https://3dlook.ai/content-hub/the-potential-of-ai-in-telehealth/`.
- Stray bold markers sit around both links: `** (**`, `**). **` and `**.**`. Please remove them.

### 1.2 Smart Scales accuracy sentence (Where FitXpress fits)

> In internal validation under evaluated capture conditions, including tight-fitting clothing,
> predicted weight from Smart Scales showed a mean absolute error of approximately 3.5% relative to
> scale weight.

Three parts of this sentence have no source on file:

- **"including tight-fitting clothing":** no document states a clothing condition for the weight
  estimate.
- **"mean absolute error":** the approved figure is an "average error margin". Nothing on file
  shows it is specifically a mean absolute error.
- **"internal validation":** that name belongs to the measurement-accuracy study against expert
  manual measurements. The weight figure comes from a different source.

These points came up in Review 1, and we did not apply them then for the same reason. Suggested
replacement:

> Against scale weight, predicted weight from Smart Scales carries a ±3.5% average error margin
> under real-world conditions.

Your next sentence ("That figure is an average across evaluated captures…") can stay as it is.

### 1.3 Scan time

> Results typically return in approximately 30–45 seconds

The approved figure is **under 45 seconds**. Suggested: "Results return in under 45 seconds and may
include:"

### 1.4 "Ratio validation"

> When enabled, liveness prompts and ratio validation add further capture-integrity signals.

"Liveness prompts" is fine: it already appears in a published article. "Ratio validation" does not
appear in any product documentation or published article. Please remove it, unless product confirms
the feature.

### 1.5 Privacy and security paragraph

Three statements differ from our approved compliance wording:

| Version 5 | Approved wording |
|---|---|
| A Business Associate Agreement is available on request for applicable US healthcare deployments. | 3DLOOK signs Business Associate Agreements with customers covered by the Health Insurance Portability and Accountability Act (HIPAA). |
| Photos are deleted after processing. | Photos are deleted immediately after processing or within 30 days, depending on the customer's policy. |
| Derived outputs are retained in accordance with the applicable customer agreement. | There is no approved statement on output retention yet. Please remove this sentence for now. |

The GDPR sentence is correct. It only needs the abbreviation spelled out (see 1.7).

### 1.6 Dashes in number ranges

Our house style does not use en or em dashes. Number ranges take a hyphen, as the live accuracy
article does:

- 96–97% → 96-97%
- 1.5–2.0 cm → 1.5-2.0 cm
- 150–220 cm → 150-220 cm
- 38–210 kg → 38-210 kg

The fifth one, 30–45, goes away with 1.3.

### 1.7 Abbreviations to spell out at first use

- **GLP-1** → glucagon-like peptide-1 (GLP-1). Its first appearance is the H2 of the GLP-1 section,
  and our checker reads headings too. Either spell it out there or introduce the term earlier in
  the body.
- **GDPR** → General Data Protection Regulation (GDPR), in the privacy paragraph.
- **CMS** → Centers for Medicare & Medicaid Services (CMS), in the CMS-0057-F paragraph.

### 1.8 Three sentences are too long

Our standard allows at most one sentence over 35 words. Version 5 has three. Suggested splits:

1. **CDC prevalence, 48 words (first section):**
   > The most recent clinical measurement cycle from the Centers for Disease Control and Prevention
   > (CDC) ran from August 2021 to August 2023. It found that 40.3% of US adults had obesity (BMI of
   > 30 or higher) and 9.4% had severe obesity (BMI of 40 or higher).
2. **CMS-0057-F, 40 words (prior-authorization section):**
   > Under CMS-0057-F from the Centers for Medicare & Medicaid Services (CMS), new prior-authorization
   > timeframes apply from January 1, 2026. They cover Medicare Advantage organizations and specified
   > Medicaid and Children's Health Insurance Program (CHIP) payers. These payers must issue standard
   > non-drug decisions within 7 calendar days and expedited decisions within 72 hours, subject to
   > applicable extension provisions.
3. **DXA and bioelectrical impedance analysis, 36 words (patient progress section):** see 3.1.
   Deleting that sentence solves both issues.

With these three fixed, the article meets our sentence-length standard. The average sentence is
already fine at 15.5 words.

### 1.9 The "diagnosis" sentence (Where FitXpress fits)

> Medical or surgical eligibility, diagnosis, clinical evaluation, and prior-authorization decisions
> remain with authorized healthcare professionals and payers.

The meaning is right, but our checker rejects "diagnosis" in a positive statement about the
product's scope. Please use the approved intended-use sentence:

> FitXpress does not diagnose conditions, make clinical decisions, or determine treatment
> eligibility. Prior-authorization decisions remain with payers.

---

## 2. Needs a decision

### 2.1 The FAQ section was removed

Our content rules ask for an FAQ in every major article, and the live page has 20 questions. Review
4 suggested removing the section or keeping four questions. We would like to keep those four:

- How does Smart Scales support BMI comparison during remote intake?
- How long do specified payers have to decide a prior authorization?
- Does FitXpress determine eligibility or payer approval?
- Can FitXpress replace in-clinic measurement?

### 2.2 Length

Version 5 has about 2,480 words of body text. The plan for this refresh set 4,400, and the live page
it replaces has about 4,100. Review 4 suggested cutting 500 to 700 words; Version 5 cut about 1,400.
The refreshed hub is now shorter than the page it replaces. Please confirm the shorter length is
intended.

### 2.3 Demo link

"Request a FitXpress demo" links to the BMI verification page. Our demo link is
`https://3dlook.ai/pricing/#bd-modal-personalized`.

---

## 3. Minor

### 3.1 The DXA boundary appears twice

Patient progress tracking says:

> Body composition estimates are not equivalent to dual-energy X-ray absorptiometry (DXA) or
> bioelectrical impedance analysis, and predicted weight from Smart Scales is not a substitute for a
> calibrated scale when the protocol or payer requires one.

Where FitXpress fits already says it, with the condition: "It does not replace DXA, bioelectrical
impedance analysis, or a calibrated scale where those methods are required." Review 4 also asked to
keep boundaries in that one section. Suggest deleting the first sentence. If it goes, spell out DXA
in the second one: dual-energy X-ray absorptiometry (DXA).

### 3.2 "Do not apply"

> …and do not apply to Medicare fee-for-service.

The fact is right. We avoid saying a regulation "does not apply", so suggested: "Medicare
fee-for-service is outside these provisions."

### 3.3 Link text

"AI body data for the health programs" still reads awkwardly. Suggest the page title used in
Related reading: "AI body data across health programs".

---

## What already works

- "FitXpress is not a medical device." is our current approved wording.
- The GDPR controller and processor sentence matches the approved wording.
- The accuracy paragraph names the reference method, uses the approved repeatability wording, and
  links the accuracy framework in the same paragraph.
- The validation-population limits are correct, and the pilot table asks how many patients fall
  outside the evaluated weight range.
- Every external figure matches its approved source: CDC, CDC Preventing Chronic Disease, ASMBS,
  JAMA Surgery (scoped as a claims cohort), CMS-0057-F with the correct payer scope, Johns Hopkins,
  and the 2026 narrative review with its caveat.
- The record-level example from Review 4 makes the workflow concrete.
- The four-stage workflow, the manual-versus-guided table and the pilot table are in good shape.

Once these points are addressed, we will save the article as final and move it to publication.
