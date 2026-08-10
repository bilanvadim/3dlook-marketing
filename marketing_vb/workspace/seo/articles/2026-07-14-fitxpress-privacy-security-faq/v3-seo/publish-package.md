---
slug: fitxpress-data-privacy-security-regulatory-faq
product: fitxpress
status: ready_for_review
created: 2026-07-14
---

# Publish Package — fitxpress-data-privacy-security-regulatory-faq

## Meta

**Title:** FitXpress Data Privacy & Security FAQ | 3DLOOK (46 chars)
**Description:** How FitXpress handles data privacy and security: photo retention, HIPAA, GDPR, SOC 2, and FDA status for procurement, legal, and security teams. (144 chars)
**Slug:** fitxpress-data-privacy-security-regulatory-faq
**Target URL:** https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/
**Category:** Data Privacy & Security

---

## ⚠️ Pre-publish blocker: unresolved Open Items

`final.md` ships an **"Open items for editorial review (Asselya)"** block that this package does not resolve — it is a publisher/checklist step, not a fact-verification step. Flagging up front because one item is a live conflict, not a routine double-check:

- **SOC 2 status conflict.** The article states *"SOC 2 readiness assessment completed, no formal examination conducted."* `compliance.md` reportedly still reads **"in progress — confirm with Vadim before claiming."** This is a regulatory/trust claim on a page whose entire purpose is procurement due diligence — do not publish until Vadim or Security confirms the current wording.
- Smart Scales MAE (2.1 kg / ~3.5%), retention/hosting specifics (immediate/30-day, us-east-1, 30-day backup purge), and assurance cadence (annual pen-test, annual BC/DR test) are marked "confirm against current docs" — unverified by this step.
- Hub URL `/content-hub/ai-body-data-for-health/` is marked "forthcoming" — confirm it resolves before the internal link goes live, and confirm the three down/side product-page slugs are live.

**Recommendation:** hold at `status: ready_for_review` (not `approved`) until these are cleared. Everything below assumes the copy as currently drafted; re-run this checklist if any figure changes.

---

## Checklists

### SEO checklist

| Check | Status | Notes |
|---|---|---|
| Primary keyword in H1, first paragraph, 1–2 H2 | ✅ | H1 "Data, Privacy, Security & Regulatory FAQ for FitXpress" carries all four pillar terms (order reversed vs. the raw keyword — intentional, this is the canonical title fixed by the brief and the live URL slug). First paragraph contains the phrase verbatim: *"the FitXpress data privacy and security questions."* Individual H2s intentionally target secondary-cluster terms (HIPAA, GDPR, SOC 2, FDA) rather than repeating the primary phrase — matches the plan's GEO/AEO-over-density approach for a trust asset. |
| Meta title ≤ 60 chars | ✅ | Recommended variant is 46 chars. |
| Meta description 140–160 chars | ✅ | Recommended variant is 144 chars. |
| All numbers from approved claims | ⚠️ | Numbers trace to `about-me.md`/`compliance.md` per the draft's own Open Items block, but several are explicitly flagged there as unconfirmed against current docs (see blocker above). Not a fresh finding — carrying it forward since it blocks publish. |
| No banned words | ✅ | Grepped for leverage/utilize/harness/robust/seamless/comprehensive/delve/navigate/tapestry/realm/game-changer/revolutionary/cutting-edge/disrupt/unlock and sentence-initial furthermore/moreover/additionally — zero hits. |
| Word count ±10% of target | ✅ | Plan target ~3,200 (band 2,500–3,500). Frontmatter declares 3,290 words, which reconciles almost exactly with a direct recount of the numbered prose sections alone (Parts I–VI intro + body, excluding Quick-answers table, the 3 data tables, and the FAQ section): 3,329 words. Total *published* length including tables and the 13-item FAQ is ~4,830 words — expected for a reference/scan page per the plan's "13–15 min, not a linear read" framing, but flagging so the word-count target is understood to cover prose, not the full rendered page. |
| Intro hook in first 2 sentences | ✅ | Direct value statement (what FitXpress produces from two photos) in sentence 1, no generic opener — matches the brief's explicit ban on a generic digital-health/AI-ethics opener for this page type. |
| CTA placement matches plan | ✅ | Soft procurement-channel CTA lands in §14 exactly as scoped ("Request FitXpress security and compliance documentation through 3DLOOK procurement, or email privacy@3dlook.me"); no hard demo push, no pricing — correct for a trust/objection-handling asset. |
| No generic AI patterns | ✅ | No "not just X, it's Y," no sentence-initial furthermore/moreover/additionally. 2 em dashes in the whole file, both inside non-rendering artifacts (an HTML schema comment and the Open Items internal note) — none in reader-facing prose. Comma-separated lists (e.g., "access, correction, portability, deletion, restriction, and objection") are substantive rights/category enumerations, not the banned rhythmic adjective-triplet filler. |
| Images/alt text suggestions if needed | ⚠️ | No images specified. This is a text/table reference page (schema-first, not visual-first), so it isn't a hard requirement, but consider one lightweight diagram for the data-lifecycle table in §1 (suggested alt text: "FitXpress data lifecycle: photos, measurements, body composition, 3D models, and progress data, with retention and deletion method per category") — optional, route through visual-brief if Vadim wants it. |

### Content strategy checklist

| Check | Status | Notes |
|---|---|---|
| Article attached to correct hub | ✅ | Up-link to "AI Body Data for Health" hub is present in the intro; hub URL is marked "forthcoming" in Open Items — confirm it resolves before publish. |
| No duplicate of existing_urls | ✅ | Scope note explicitly defers to Privacy Policy, Terms, DPA, BAA, and the customer contract rather than restating them; positioned as the hub's trust asset, not a competing page. |
| Vertical boundary respected; scope note present | ✅ | Second intro paragraph is the scope note verbatim: general overview, does not replace the governing legal documents, "that document governs" on conflict. |
| Internal links in 4 directions (up/side/down/trust) | ✅ | Up: AI Body Data for Health hub (intro). Down: telehealth/weight-loss, BMI-verification, connected-fitness product pages (intro, §12). Side: insurance underwriting (intro). Trust: accuracy framework (§1), two-photo explainer (intro). |
| FAQ section present (GEO/AEO-friendly) | ✅ | 13 visible Q&As plus FAQPage schema (11 items, Q4/Q5 held out of markup per the plan's 10–12-item cap). |
| "What FitXpress does NOT do" section present | ✅ | Covered by §12 ("What uses are supported, and what decisions should not rely on FitXpress alone?") rather than a literally-titled section — this is the canonical structure's equivalent per the brief's own H2.12 spec, not a gap. |
| No prohibited positioning claims | ✅ | Checked every instance of "HIPAA certified," "SOC 2 certified," "FDA approved," "100% secure," "military-grade," "completely anonymous," "guaranteed/fully compliant" — every hit is either an interrogative section heading ("Is 3DLOOK SOC 2 certified?") or an explicit negation ("no product is 'HIPAA certified,'" "not cleared, authorized, or approved by the FDA"). None asserts the claim positively. |
| Article owns one distinct search intent | ✅ | Branded objection-handling/trust-verification intent per the plan; vertical pages are scoped to carry only a short privacy note pointing back here, not their own privacy/HIPAA/SOC 2 FAQs. |

---

## Alt meta options

**Title variants:**
1. **FitXpress Data Privacy & Security FAQ \| 3DLOOK** (46 chars) — *recommended.* Leads with the primary keyword, fits the brand suffix comfortably under 60 chars.
2. FitXpress Data Privacy, Security & Regulatory FAQ (49 chars) — all four topic pillars, no brand suffix.
3. FitXpress Data Privacy & Security FAQ for Enterprise (52 chars) — adds audience signal, no brand suffix.

**Description variants:**
1. **How FitXpress handles data privacy and security: photo retention, HIPAA, GDPR, SOC 2, and FDA status for procurement, legal, and security teams.** (144 chars) — *recommended.* Leads with the keyword phrase, names every framework covered, closes on the audience (soft CTA by implication — "for procurement, legal, and security teams" signals self-selection).
2. FitXpress data privacy, security, and regulatory answers for enterprise procurement: retention periods, HIPAA/BAA, GDPR, SOC 2 status, and FDA position. (152 chars) — leads with "enterprise procurement," slightly more formal register.
3. Enterprise FAQ on FitXpress data handling: what's stored, HIPAA, GDPR, CCPA support, SOC 2 status, FDA classification, and how to request full documentation. (157 chars) — explicit soft CTA ("how to request full documentation").

---

## Article

---
slug: fitxpress-data-privacy-security-regulatory-faq
product: fitxpress
status: edited
word_count: 3290
editing_passes: 4
changes_summary: |
  - Deduped 1 repeated procurement-reference sentence (§1 ending); no external citations required dedup
  - Replaced 4 generic AI patterns: condensed a five-sentence parallel "rights stay with…" run in §4, fixed 2 stacked negations (§3 progress-default, §9 biometric), tightened the body-composition close in §1
  - Added 2 expert-judgment reframes ("what trips up most procurement reviews," "the common mistake is") in place of flat statements; no new figures introduced (all approved numbers already present)
  - Removed 6 redundant phrasings: re-expansions of HIPAA, GDPR, CCPA/CPRA, PHI, and FDA already defined in Quick answers, plus a duplicated procurement line
  - Added internal links in 4 directions (up: health hub; down: telehealth/weight-loss, connected-fitness, BMI-verification product pages; side: insurance underwriting; trust: accuracy framework, two-photo explainer)
  - Fixed 0 banned words (none present in draft)
---

# Data, Privacy, Security & Regulatory FAQ for FitXpress

FitXpress turns two smartphone photos and a short profile into [structured body data](https://3dlook.ai/content-hub/3dlook-turns-two-photos-structured-body-data/): 80+ body measurements, body composition estimates, a 3D model, and progress tracking across scans. Enterprise customers integrate it through an Application Programming Interface (API) or Software Development Kit (SDK) across [telehealth and weight loss](https://3dlook.ai/fitxpress/for-telehealth-and-weight-loss/), [insurance underwriting](https://3dlook.ai/content-hub/mobile-body-scanning-insurance-underwriting/), wellness, [connected fitness](https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/), and clinical research. This page answers the FitXpress data privacy and security questions that procurement, legal, and security teams raise during due diligence, and sets out the product's regulatory position; it is the reference that 3DLOOK's [AI body data for health hub](https://3dlook.ai/content-hub/ai-body-data-for-health/) and product pages point to for that detail.

It is a general product, privacy, security, and regulatory overview. Specific behavior varies by contract, deployment, jurisdiction, integration method, and intended use, so it does not replace the [Privacy Policy](https://3dlook.ai/privacy-policy/), the Terms, a Data Processing Agreement (DPA), a Business Associate Agreement (BAA), or the signed customer contract. Where any of those documents differs from this summary, that document governs.

*Written by Assel Sekerova. Reviewed by Legal, Security, and Product. Last updated: 2026-07-14. Procurement, legal, and security teams can request the underlying documentation through the standard procurement channel or at privacy@3dlook.me.*

---

## Quick answers

| Topic | Direct answer | Qualification |
|---|---|---|
| Photos | Photos are processed to extract body geometry and measurements, then deleted immediately after processing by default. | Under a client-specific policy, 3DLOOK may retain photos for up to 30 days, and retained photos are automatically blurred. Customers that collect photos through the FitXpress SDK decide separately whether to keep copies in their own systems. |
| Measurements and body composition | Measurements and body composition estimates are generated per scan and stored by 3DLOOK for the active contract term. | Retention windows are configurable for enterprise customers. Body composition values are estimates derived from measurements and submitted inputs, not direct measurements. |
| 3D models and progress tracking | A 3D model is generated for every scan; historical records can support progress tracking when the feature is enabled. | Progress tracking is off by default and is absent from many deployments. |
| Data location | FitXpress data is hosted on Amazon Web Services (AWS), primarily in the us-east-1 region. | Regional hosting options are available for enterprise customers under contract. |
| Deletion | Deletion API endpoints support user-level deletion and individual-scan deletion. | Backup copies are purged within a 30-day cycle. A legal hold or an active security investigation can defer deletion. |
| Ownership | The enterprise customer holds rights to the data it submits and the outputs generated from it; 3DLOOK holds rights to its software and models. | Ownership, processing rights, and personal-data rights are separate concepts. See the data rights section. |
| AI training | 3DLOOK does not use production customer data to train its models without the customer's explicit, documented authorization. | Model development uses separately collected research and validation datasets. See the AI training section. |
| HIPAA | FitXpress can support deployments governed by the Health Insurance Portability and Accountability Act (HIPAA) where 3DLOOK acts as a business associate under an executed BAA. | HIPAA is a regulatory framework, not a certification. Applicability depends on the customer's status and workflow. |
| GDPR and CCPA/CPRA | 3DLOOK generally acts as a processor under the General Data Protection Regulation (GDPR) and as a service provider under the California Consumer Privacy Act (CCPA) and California Privacy Rights Act (CPRA). | The customer stays responsible for lawful basis, notices, and consent. See the privacy compliance section. |
| SOC 2 | 3DLOOK has completed a System and Organization Controls 2 (SOC 2) readiness assessment; a formal SOC 2 examination has not yet been conducted. | Alternative security evidence is available under a Non-Disclosure Agreement (NDA). See the certifications section. |
| FDA | FitXpress is not cleared, authorized, or approved by the U.S. Food and Drug Administration (FDA), and is not positioned as a medical device. | FDA treatment depends on intended use and the claims a customer makes. See the regulatory status section. |

---

## Part I: Data lifecycle

## 1. What data does FitXpress process and generate?

A FitXpress scan starts from a guided capture flow and returns structured outputs in under 45 seconds. Three categories of data move through that flow: data submitted to the platform, data generated by the platform, and technical data produced during processing.

**Submitted data** is what the end user or the customer's application provides:

- Front and side photos captured through the guided mobile flow
- Height
- Weight, which is optional and used to produce body composition outputs
- Sex or gender input where the selected model requires it, plus any profile information the workflow needs
- Customer-assigned or scan identifiers

**Generated data** is what the platform produces from that input:

- 80+ circumference and linear body measurements
- Body composition estimates: Body Mass Index (BMI), Basal Metabolic Rate (BMR) using the Mifflin-St Jeor equation, body fat percentage using the U.S. Navy formula, lean mass, and fat mass
- A Smart Scales weight estimate, a software output with a mean absolute error of 2.1 kg (about 3.5% average error), not a reading from a physical scale
- A 3D model
- Progress-tracking data that links scan results across sessions

**Technical data** is operational rather than descriptive of the body: capture-quality and pose-validation flags, clothing classification, face-obfuscation confirmation, and processing logs with timestamps and request metadata.

Body composition outputs sit in a different category from body measurements. Measurements describe circumference and length at defined body points. Body composition values such as body fat percentage or lean mass are estimates, derived from those measurements together with the submitted height and optional weight. The common mistake is reading every output as a "measurement," which overstates what the platform produces. How that measurement and estimate accuracy is validated and reported sits outside this page, in the [body-scanning accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/).

**Data lifecycle**

| Data category | Purpose | Stored by 3DLOOK? | Retention | Deletion method |
|---|---|---|---|---|
| Photos | Scan processing: extracting body geometry and measurements | Not by default; retained up to 30 days only under a client-specific policy | Deleted immediately after processing by default | Automatic deletion on completion; face obfuscation applied at capture and automatic blur where a policy retains photos |
| Measurements and body metrics | Structured scan results returned to the customer | Yes | Active contract term; configurable for enterprise customers | Deletion API (user-level or individual-scan); standard backup purge cycle |
| Body composition data | Body composition estimates and progress-tracking input | Yes | Active contract term; configurable for enterprise customers | Deletion API (user-level or individual-scan); standard backup purge cycle |
| 3D model or mesh | Visualization and downstream customer use | Yes | Active contract term; configurable for enterprise customers | Deletion API (user-level or individual-scan); standard backup purge cycle |
| Progress-tracking data | Comparison of measurements, body composition, or 3D models across scans | Yes, where the feature is enabled | Tied to the retention of the scan records it compares | Removed when the linked scan or user record is deleted |
| Identifiers and logs | Security, support, billing, and audit | Yes | Retained per operational and security requirements | Standard log rotation; may be held under legal hold |

---

## 2. How are data storage, retention, and deletion handled?

Photos are deleted immediately after processing by default. Under a client-specific policy, 3DLOOK may retain photos for up to 30 days, and any retained photo is automatically blurred; face obfuscation is applied at the point of capture regardless of the retention policy. Photos support the scan they belong to and are not repurposed unless a specific contractual arrangement provides otherwise.

When an enterprise customer collects photos through its own application using the FitXpress SDK and sends them to the 3DLOOK API, the customer decides whether copies stay in its own systems. That customer-side retention is separate from the processing 3DLOOK performs and follows the customer's own policy.

Measurements, body composition data, and 3D models are retained by 3DLOOK for the duration of the active contract. Enterprise customers can configure shorter or workflow-specific retention windows for these outputs. Progress-tracking data persists only while the scan records it compares remain available, so removing a scan or a user record removes the associated progress data from active systems.

FitXpress data is hosted on AWS, primarily in the us-east-1 region. Regional hosting options are available for enterprise customers under contract, which matters for deployments with data-residency requirements.

Deletion runs through API endpoints at two levels. User-level deletion removes every scan and record tied to a profile. Individual-scan deletion removes a single scan. Standard deletion clears data from active systems, and backup copies are purged within a 30-day backup cycle. Deletion is deferred only where a legal hold applies or during an active security investigation.

Technical documentation, the data-retention schedule, the subprocessor list, and deletion API documentation are available through the procurement or security review process. Encryption and key handling are covered in the security section below.

---

## 3. How does body and 3D model progress tracking work?

Progress tracking links multiple scans to one profile through a customer-assigned identifier. When the same identifier appears across sessions, FitXpress can compare outputs generated at different points in time.

The comparable outputs are measurements, body composition estimates (BMI, BMR, body fat percentage, lean mass, and fat mass), weight estimates including the Smart Scales output, and 3D models shown side by side or as an overlay. The historical records the feature needs scale to what is being compared: measurement trends need prior measurement records, an overlay of two 3D models needs both models retained, and body composition trends need the body composition record from each scan.

Progress comparison can run inside 3DLOOK through the API, inside the customer's own application using returned scan data, or across both. The customer decides how results are presented to the end user.

Progress tracking is off by default. Enterprise customers enable and configure progress-history retention during implementation, and a deployment retains historical records for this purpose only when the feature is enabled. Deleting an individual scan removes it from the progress history; deleting a full user record removes all associated scans and progress data from active systems, subject to the 30-day backup cycle described above.

Progress-tracking data is operational, supporting review, comparison, and engagement rather than diagnosis. A visible difference between two 3D models does not by itself represent a clinically meaningful change, and interpretation stays with the customer's care team or defined rules.

---

## Part II: Data rights and permitted use

## 4. Who controls and owns FitXpress data?

Control and ownership of FitXpress data divide across three roles, and each role carries a different kind of right rather than a single "owner."

End users hold data-subject rights over their own personal data, including access, correction, portability, deletion, restriction, and objection, where the governing privacy framework applies. In most FitXpress deployments the enterprise customer is the data controller, so end-user requests are routed through the customer. 3DLOOK supports the customer in fulfilling requests that touch data it processes on the customer's behalf.

The enterprise customer holds contractual rights to the data it submits and to the outputs generated from it, including measurements, body composition estimates, and 3D models. That position carries responsibility for:

- Providing privacy notices to end users
- Establishing a lawful basis for processing
- Obtaining consent where the workflow requires it
- Setting retention policy for photos, measurements, body composition data, 3D models, and progress history
- Governing downstream use of FitXpress outputs
- Securing its own applications, integrations, and API credentials
- Deciding whether photos collected through the FitXpress SDK stay in the customer's own systems after being sent to the 3DLOOK API

3DLOOK holds the limited processing rights needed to deliver the service and owns its software, algorithms, and underlying models. 3DLOOK does not sell customer data and does not use it for advertising. Where the customer contract permits, 3DLOOK may use aggregated or anonymized data for internal analytics and service improvement.

What trips up most procurement reviews is treating "who owns the data" as one question, when it is really five. Personal-data rights stay with the end user, while contractual rights over submitted data and generated outputs sit with the enterprise customer. 3DLOOK holds only the processing rights needed to run the service, plus the intellectual property in its software and models. The generated outputs themselves are assigned to the customer by contract.

---

## 5. Does 3DLOOK use customer data to train AI models?

No. 3DLOOK does not use production customer data, meaning submitted photos, generated measurements, body composition data, or 3D models, to train its models without the customer's explicit, contractually documented authorization.

Model development draws on research and validation datasets collected separately under their own consent and data-use terms, kept distinct from production customer data. Enterprise customers can prohibit any model-training use of their data through the Data Processing Agreement (DPA).

Where the customer contract permits, 3DLOOK may use aggregated or anonymized data from production for internal analytics, capacity planning, and service improvement. The label "anonymized" applies only to data that meets the applicable legal and technical standard for anonymization; data that could be re-identified stays classified as personal data. Technical service logs, used for debugging, security monitoring, and operational support, form a separate category and are not repurposed for training.

---

## Part III: Security and assurance

## 6. How does 3DLOOK protect FitXpress data?

3DLOOK groups its FitXpress security controls into four areas.

**Data protection.** Transport Layer Security (TLS) encrypts data in transit between the end user's device, the customer's application, and 3DLOOK infrastructure. Amazon S3 Server-Side Encryption with managed keys (SSE-S3) encrypts stored data by default and stays on; it cannot be disabled. Encryption keys are managed through AWS Key Management Service (KMS).

**Access and platform security.** Role-based access control (RBAC) and least-privilege provisioning govern who can reach production data and systems. Development, staging, and production environments stay separate. Customer data is logically isolated by tenant. API-key authentication and administrative-access controls govern programmatic and human access.

**Security operations.** Logging and monitoring cover production systems, API access, and administrative actions. A vulnerability management program covers identification, prioritization, and remediation. Patch management and change management processes govern infrastructure and application updates. Incident-response procedures cover detection, containment, investigation, and notification. Business continuity and disaster recovery plans are tested annually.

**Testing and assurance.** Penetration testing is conducted at least annually by an independent third-party firm. Security reviews accompany that testing and follow significant architecture changes. Findings are tracked through to remediation. Security questionnaires are completed during enterprise procurement. Detailed evidence, including architecture diagrams, penetration-test summaries, and control documentation, is available to qualified enterprise customers under a Non-Disclosure Agreement (NDA).

These controls reduce risk. Enterprise customers should still run their own security assessment as part of procurement, since the operating security posture depends on how each deployment is configured.

---

## 7. What security and compliance documentation is available?

| Document or evidence | Availability |
|---|---|
| Security overview | On request |
| Architecture and data-flow diagrams | Under NDA |
| Data Processing Agreement (DPA) | Provided during contracting |
| Business Associate Agreement (BAA) | For enterprise customers on qualifying plans |
| Subprocessor list | On request |
| Penetration-test summary | Under NDA |
| Incident-response overview | On request or under NDA |
| Business continuity and disaster recovery summary | On request or under NDA |
| SOC 2 report | Not currently available; see the SOC 2 section below |
| Security questionnaire | Completed during procurement |

Documentation is shared with qualified enterprise customers through the security or procurement review process. Internal security files, complete audit reports, and penetration-test details stay unpublished and available only under NDA. The availability of alternative evidence does not stand in for a completed SOC 2 examination.

---

## Part IV: Privacy compliance

## 8. How does FitXpress support HIPAA, GDPR, and CCPA/CPRA?

**HIPAA.** HIPAA can apply when FitXpress is used by a covered entity or a business associate that handles protected health information (PHI). Where it applies, 3DLOOK can act as a business associate under an executed Business Associate Agreement (BAA), available to enterprise customers on qualifying plans. Supported technical safeguards include encryption in transit and at rest, access controls, and audit logging, with contractual safeguards set out in the BAA. HIPAA is a regulatory framework, not a certification. The customer keeps its own obligations as the covered entity or business associate, including determining whether its use of FitXpress involves PHI and configuring the deployment to match.

**GDPR and UK GDPR.** GDPR and the UK GDPR govern the processing of personal data relating to individuals in the European Economic Area (EEA) and the United Kingdom (UK). In most FitXpress deployments the enterprise customer is the data controller and 3DLOOK is the data processor. 3DLOOK provides an Article 28 Data Processing Agreement (DPA) that incorporates Standard Contractual Clauses (SCCs) for international transfers, with a UK Addendum where UK GDPR applies. 3DLOOK supports data-subject rights, including access, correction, portability, deletion, restriction, and objection, through mechanisms that let the customer retrieve, correct, or delete data processed on its behalf. Where body composition data or other outputs qualify as special-category data under GDPR Article 9, the customer identifies the applicable lawful basis and reflects it in its own notice and consent flow.

**CCPA and CPRA.** The CCPA and CPRA apply to the personal information of California residents. Where they apply, 3DLOOK generally acts as a service provider or contractor that processes personal information on the customer's behalf. 3DLOOK does not sell personal information and does not share it for cross-context behavioral advertising. 3DLOOK supports consumer requests, including access, deletion, correction, and opt-out, through mechanisms the customer can use to retrieve or delete data, and limits its use of personal information to the business purposes named in the customer agreement.

---

## 9. Is FitXpress data biometric or health data?

Classification depends on the data type, the processing purpose, the jurisdiction, and the deployment, so no single label fits every FitXpress output. Personal data means information relating to an identified or identifiable person; health data and biometric data are narrower categories with their own legal tests.

Photos, body measurements, and 3D models are personal data when they relate to an identifiable individual. Body composition and weight-related metrics can be health data or sensitive data depending on how the customer uses them: the same measurement carries a different classification inside a clinical or weight-management workflow than inside an apparel-sizing workflow.

Under GDPR, data becomes biometric data when it results from specific technical processing used to uniquely identify a person. Because FitXpress does not perform that unique identification, a body scan falls outside the biometric-data definition by default.

Whether an output is PHI under HIPAA depends on whether a covered entity or business associate holds it and whether it relates to health status, care, or payment, rather than on the data type alone.

The enterprise customer sets the purpose and means of processing, so it is best placed to classify its FitXpress data under the framework that governs its workflow. 3DLOOK supplies the technical and contractual documentation that supports that assessment.

---

## Part V: Certifications and regulatory status

## 10. Is 3DLOOK SOC 2 certified?

3DLOOK has completed a SOC 2 readiness assessment and aligned its security controls with the SOC 2 Trust Services Criteria. A formal SOC 2 examination has not yet been conducted.

SOC 2 is an attestation examination performed by an independent auditor, not a product certification. For that reason, 3DLOOK does not describe itself as "SOC 2 certified" and reserves any examination-based claim for the point at which a completed examination supports it.

Alternative security evidence, including penetration-test summaries, the security overview, and security-questionnaire responses, is available to qualified enterprise customers under NDA. This evidence covers overlapping control areas, and it remains distinct from a completed SOC 2 examination.

---

## 11. Is FitXpress FDA approved or regulated as a medical device?

FitXpress is not cleared, authorized, or approved by the FDA, and is not positioned as a medical device.

FDA treatment depends on the intended use of a product and the claims the deploying party makes. FitXpress is positioned for general wellness, administrative intake, body measurement capture, body composition tracking, and progress tracking, rather than diagnosis or treatment. The FDA separates categories that carry different obligations:

- **General wellness** products that present low risk generally fall outside premarket-authorization requirements.
- **Administrative intake and documentation** uses are distinct from diagnostic use.
- **Progress tracking** for engagement or monitoring, without diagnostic conclusions, is distinct from medical-device functionality.
- **Clinical support, diagnosis, and treatment** uses can trigger FDA requirements depending on the claims and the workflow.

FitXpress does not make medical, diagnostic, or treatment decisions on its own. Its outputs need human interpretation, clinical judgment, or customer-defined decision rules before they inform any clinical or eligibility determination. The enterprise customer assesses whether its complete integrated workflow, including how outputs are used and what claims reach end users, triggers FDA requirements.

The relevant terms are not interchangeable. "FDA approved" refers to the premarket approval (PMA) pathway for Class III devices. "FDA cleared" refers to the 510(k) premarket notification pathway for Class II devices. "FDA authorized" refers to other authorization pathways. Some software stays outside all of them based on its stated intended use. FitXpress has pursued none of these pathways.

---

## 12. What uses are supported, and what decisions should not rely on FitXpress alone?

FitXpress supports remote intake and body measurement capture, body composition tracking, progress tracking across scans, clinical research data collection as a structured capture tool, [eligibility documentation](https://3dlook.ai/for-bmi-verification/), and patient or member engagement. In each case it standardizes how body data is captured and made available before a person or a defined rule acts on it.

FitXpress should not independently determine a diagnosis, a treatment, fitness for duty, employment eligibility, insurance eligibility, clinical-trial eligibility, or any other high-impact individual decision. Each of those workflows needs its own validation, human review, and customer-defined decision rules, applied under the law that governs that decision.

The distinction holds across every use case: FitXpress is a supporting data layer, not the decisioning system. It improves the quality and availability of body data going into a decision, and the decision itself stays with the customer's clinicians, underwriters, or defined rules.

---

## Part VI: Enterprise deployment

## 13. What should an enterprise confirm before implementation?

1. **Intended use and supported claims.** Confirm the deployment sits within FitXpress's intended-use scope and that customer-facing claims match 3DLOOK's approved positioning.
2. **Data inputs and outputs.** Map the required inputs (photos, height, optional weight, other profile fields) against the outputs the workflow consumes: measurements, body composition, 3D models, progress tracking, and Smart Scales estimates.
3. **Legal roles, lawful basis, and SDK photo responsibility.** Confirm controller and processor designations, the lawful basis for processing, consent handling, and who owns any customer-side retention of SDK-collected photos.
4. **Hosting and data residency.** Verify that the available AWS regions meet the deployment's residency requirements, and request regional hosting if the default region does not fit.
5. **Retention per data category.** Confirm the retention configuration for photos, measurements, body composition data, 3D models, and progress history separately, since each follows different rules.
6. **Deletion and data-subject request workflows.** Validate that the deletion API meets operational needs, and define internal workflows for access, correction, portability, and deletion requests.
7. **DPA or BAA requirements.** Execute a Data Processing Agreement, and a Business Associate Agreement where the deployment involves PHI under HIPAA.
8. **Subprocessors and international transfers.** Review the subprocessor list and confirm the transfer mechanism for any cross-border flow, such as Standard Contractual Clauses or the UK Addendum.
9. **Security evidence and access controls.** Request the available security documentation and assess encryption, access controls, logging, and incident response against the enterprise's own standards.
10. **Regulatory and human-review requirements.** Determine whether FDA, HIPAA, GDPR, or CCPA/CPRA obligations apply to the complete workflow, and define the human-review framework for any high-impact decision.

---

## 14. How can procurement, legal, or security teams request additional information?

Enterprise stakeholders can request the following through 3DLOOK's standard procurement channel or at **privacy@3dlook.me**:

- Security documentation
- Data Processing Agreement (DPA)
- Business Associate Agreement (BAA), where HIPAA applies
- Penetration-test summary (under NDA)
- Architecture and data-flow diagrams (under NDA)
- Subprocessor information
- Regulatory-status confirmation
- Product validation evidence
- Deletion and integration documentation

Internal security files, full audit materials, and penetration-test reports stay unpublished on this page and are shared with qualified enterprise customers under NDA. To move a review forward, request FitXpress security and compliance documentation through 3DLOOK procurement, or email privacy@3dlook.me.

---

## FAQ

**1. What data does FitXpress process?**

FitXpress processes photos and profile inputs, including height, optional weight, and any required fields, to generate 80+ body measurements, body composition estimates (BMI, BMR, body fat percentage, lean mass, fat mass, and a Smart Scales weight estimate), a 3D model, and progress data across scans. Capture-quality flags and operational logs are produced alongside these outputs to support the service.

**2. Are body-scan photos stored?**

By default, no. Photos are deleted immediately after processing, and face obfuscation is applied at the point of capture. Under a client-specific policy, 3DLOOK may retain photos for up to 30 days, and retained photos are automatically blurred. Customers that collect photos through the FitXpress SDK can keep their own copies, and that retention sits outside 3DLOOK's systems.

**3. How long are photos, measurements, body composition data, and scan results retained?**

Photos are deleted immediately after processing by default. Measurements, body composition data, and 3D models are retained for the duration of the active contract, with configurable retention windows for enterprise customers. Backup copies are purged within a 30-day cycle.

**4. How does body and 3D model progress tracking work?**

Scans are linked through a customer-assigned identifier, which lets FitXpress compare measurements, body composition, and 3D models across sessions. Progress tracking is optional and off by default, so the customer enables it deliberately. Deleting a scan or a user record removes the associated progress data from active systems.

**5. Where is FitXpress data hosted?**

FitXpress runs on AWS, primarily in the us-east-1 region. Regional hosting options are available for enterprise customers with specific data-residency requirements.

**6. Can customers or users delete scan data?**

Yes. 3DLOOK provides an API for user-level and individual-scan deletion, and backup copies are purged within a 30-day cycle. Deletion is deferred only where a legal hold or an active security investigation applies.

**7. Does 3DLOOK use customer data to train AI models?**

No. 3DLOOK does not use production customer data to train its models without the customer's explicit, documented authorization. Model development relies on separately collected research and validation datasets rather than production customer data.

**8. Who owns the photos, measurements, body composition data, and 3D models?**

The enterprise customer holds rights to the data it submits and the outputs generated from it. 3DLOOK owns the underlying software, algorithms, and models, does not sell customer data, and does not use it for advertising.

**9. How does 3DLOOK protect FitXpress data?**

Data is encrypted in transit with TLS and at rest with AWS SSE-S3, under role-based access controls and continuous logging. 3DLOOK runs a vulnerability management program, conducts annual penetration testing by an independent third-party firm, and maintains incident-response and business continuity and disaster recovery plans. Detailed control evidence is available to qualified customers under NDA.

**10. Is FitXpress HIPAA compliant?**

FitXpress can support HIPAA-regulated deployments where 3DLOOK acts as a business associate under an executed BAA, available on qualifying enterprise plans. HIPAA is a regulatory framework rather than a certification, so no product is "HIPAA certified." Compliance depends on how the customer configures and operates its own workflow.

**11. How does FitXpress support GDPR and CCPA/CPRA?**

3DLOOK acts as a data processor under GDPR and as a service provider under CCPA/CPRA, under a DPA that includes Standard Contractual Clauses and a UK Addendum where needed. 3DLOOK does not sell customer data, and the enterprise customer remains the controller responsible for lawful basis, notices, and consent.

**12. Is 3DLOOK SOC 2 certified?**

3DLOOK has completed a SOC 2 readiness assessment and aligned its controls to the SOC 2 Trust Services Criteria, and a formal SOC 2 examination has not yet been conducted. Alternative security evidence covering the same control areas is available to qualified enterprise customers under NDA.

**13. Is FitXpress FDA approved or regulated as a medical device?**

No. FitXpress is not FDA-cleared, authorized, or approved, and is not positioned as a medical device. A customer deploying FitXpress in a clinical or regulated workflow is responsible for assessing whether its complete workflow triggers FDA requirements.

---

<!-- FAQPage schema — 11 items, excluded from word count. Q4 (progress tracking) and Q5 (hosting) stay visible above but sit outside the markup per plan (schema cap). Answers mirror the visible FAQ verbatim. -->

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What data does FitXpress process?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "FitXpress processes photos and profile inputs, including height, optional weight, and any required fields, to generate 80+ body measurements, body composition estimates (BMI, BMR, body fat percentage, lean mass, fat mass, and a Smart Scales weight estimate), a 3D model, and progress data across scans. Capture-quality flags and operational logs are produced alongside these outputs to support the service."
      }
    },
    {
      "@type": "Question",
      "name": "Are body-scan photos stored?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "By default, no. Photos are deleted immediately after processing, and face obfuscation is applied at the point of capture. Under a client-specific policy, 3DLOOK may retain photos for up to 30 days, and retained photos are automatically blurred. Customers that collect photos through the FitXpress SDK can keep their own copies, and that retention sits outside 3DLOOK's systems."
      }
    },
    {
      "@type": "Question",
      "name": "How long are photos, measurements, body composition data, and scan results retained?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Photos are deleted immediately after processing by default. Measurements, body composition data, and 3D models are retained for the duration of the active contract, with configurable retention windows for enterprise customers. Backup copies are purged within a 30-day cycle."
      }
    },
    {
      "@type": "Question",
      "name": "Can customers or users delete scan data?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. 3DLOOK provides an API for user-level and individual-scan deletion, and backup copies are purged within a 30-day cycle. Deletion is deferred only where a legal hold or an active security investigation applies."
      }
    },
    {
      "@type": "Question",
      "name": "Does 3DLOOK use customer data to train AI models?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. 3DLOOK does not use production customer data to train its models without the customer's explicit, documented authorization. Model development relies on separately collected research and validation datasets rather than production customer data."
      }
    },
    {
      "@type": "Question",
      "name": "Who owns the photos, measurements, body composition data, and 3D models?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The enterprise customer holds rights to the data it submits and the outputs generated from it. 3DLOOK owns the underlying software, algorithms, and models, does not sell customer data, and does not use it for advertising."
      }
    },
    {
      "@type": "Question",
      "name": "How does 3DLOOK protect FitXpress data?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Data is encrypted in transit with TLS and at rest with AWS SSE-S3, under role-based access controls and continuous logging. 3DLOOK runs a vulnerability management program, conducts annual penetration testing by an independent third-party firm, and maintains incident-response and business continuity and disaster recovery plans. Detailed control evidence is available to qualified customers under NDA."
      }
    },
    {
      "@type": "Question",
      "name": "Is FitXpress HIPAA compliant?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "FitXpress can support HIPAA-regulated deployments where 3DLOOK acts as a business associate under an executed BAA, available on qualifying enterprise plans. HIPAA is a regulatory framework rather than a certification, so no product is HIPAA certified. Compliance depends on how the customer configures and operates its own workflow."
      }
    },
    {
      "@type": "Question",
      "name": "How does FitXpress support GDPR and CCPA/CPRA?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "3DLOOK acts as a data processor under GDPR and as a service provider under CCPA/CPRA, under a DPA that includes Standard Contractual Clauses and a UK Addendum where needed. 3DLOOK does not sell customer data, and the enterprise customer remains the controller responsible for lawful basis, notices, and consent."
      }
    },
    {
      "@type": "Question",
      "name": "Is 3DLOOK SOC 2 certified?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "3DLOOK has completed a SOC 2 readiness assessment and aligned its controls to the SOC 2 Trust Services Criteria, and a formal SOC 2 examination has not yet been conducted. Alternative security evidence covering the same control areas is available to qualified enterprise customers under NDA."
      }
    },
    {
      "@type": "Question",
      "name": "Is FitXpress FDA approved or regulated as a medical device?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. FitXpress is not FDA-cleared, authorized, or approved, and is not positioned as a medical device. A customer deploying FitXpress in a clinical or regulated workflow is responsible for assessing whether its complete workflow triggers FDA requirements."
      }
    }
  ]
}
```

---

## Open items for editorial review (Asselya)

Per editorial guardrail #11, figures are surfaced rather than silently edited. Verify before publish:

- **Smart Scales weight estimate:** written as mean absolute error of 2.1 kg (about 3.5% average error), per `about-me.md`. Confirm this is the current published figure.
- **Retention and hosting specifics:** "immediately after processing / up to 30 days," "us-east-1 primary region," "30-day backup purge cycle" reflect `compliance.md` and the v2 approved language. Confirm each against the current retention schedule and infrastructure docs.
- **SOC 2 status:** "readiness assessment completed, no formal examination conducted." `compliance.md` still reads "in progress — confirm with Vadim before claiming." Confirm the readiness-assessment framing is approved for public use.
- **Assurance cadence:** "penetration testing at least annually by an independent third-party firm" and "business continuity and disaster recovery tested annually" come from the v2 approved list. Confirm both with Security before publish.
- **Internal links:** hub URL (`/content-hub/ai-body-data-for-health/`) is forthcoming per plan; confirm it resolves before publish, and confirm the product-page and content-hub slugs used in the intro and §1/§12 match live URLs.
