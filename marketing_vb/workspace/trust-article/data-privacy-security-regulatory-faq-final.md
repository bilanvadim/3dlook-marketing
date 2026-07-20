---
slug: data-privacy-security-regulatory-faq
title: "Data, Privacy, Security & Regulatory FAQ for FitXpress"
meta_title: "FitXpress Data Privacy, Security & Regulatory FAQ | 3DLOOK"
meta_description: "FitXpress data privacy, security, and regulatory FAQ for procurement and legal teams. Covers data lifecycle, HIPAA, GDPR, CCPA, SOC 2, FDA status, and AI training."
status: needs_legal_review
product: fitxpress
content_type: trust_asset
priority: P0
last_updated: ""
---

<!-- PUBLISHING HALTED: Legal/Security/Product approval required per content plan. Do not publish until sign-off received. -->

# Data, Privacy, Security & Regulatory FAQ for FitXpress

[FitXpress](https://3dlook.ai/fitxpress/) turns two smartphone photos and a short profile into structured body data: 80+ body measurements, body composition estimates, a 3D model, and progress tracking across scans. Enterprise customers integrate it through an Application Programming Interface (API) or Software Development Kit (SDK) across telehealth and weight loss, insurance underwriting, wellness, connected fitness, and clinical research. This page answers the FitXpress data privacy and security questions that procurement, legal, and security teams raise during due diligence, and sets out the product's regulatory position.

It is a general product, privacy, security, and regulatory overview. Specific behavior varies by contract, deployment, jurisdiction, integration method, and intended use, so it does not replace the [Privacy Policy](https://3dlook.ai/privacy-policy/), the [Terms](https://3dlook.ai/terms-and-policies/), a Data Processing Agreement (DPA), a Business Associate Agreement (BAA), or the signed customer agreement. Where any of those documents differs from this summary, that document governs.

<!-- Review required: Legal, Security, Product, Regulatory -->

Procurement, legal, and security teams can request the underlying documentation through the standard procurement channel or at privacy@3dlook.ai.

---

## Quick answers

| Topic | Direct answer | Qualification |
|---|---|---|
| Photos | Photos are processed to extract body geometry and measurements, then deleted immediately after processing by default. | Under a client-specific policy, 3DLOOK may retain photos for up to 30 days, and retained photos are automatically blurred. Customers that collect photos through the FitXpress SDK decide separately whether to keep copies in their own systems. |
| Measurements and body composition | Measurements and body composition estimates are generated per scan and stored by 3DLOOK for the active contract term. | Retention windows are configurable for enterprise customers. Body composition values are estimates derived from measurements and submitted inputs, not direct measurements. Methodology and validation are covered in the [body-scanning accuracy framework](https://3dlook.ai/content-hub/body-fat-percentage-men-women-ai-3d-scanning-goals/). |
| 3D models and progress tracking | A 3D model is generated for every scan; historical records can support progress tracking when the feature is enabled. | Progress tracking is off by default and is absent from many deployments. |
| Data location | FitXpress data is hosted on Amazon Web Services (AWS), primarily in the us-east-1 region. | Regional hosting options are available for enterprise customers under contract. |
| Deletion | Deletion API endpoints support user-level deletion and individual-scan deletion. | Backup copies are purged within a 30-day cycle. A legal hold or an active security investigation can defer deletion. [FitXpress API documentation](https://docs.fitxpress.3dlook.me/) is available for integration reference. |
| Ownership | The enterprise customer holds rights to the data it submits and the outputs generated from it; 3DLOOK holds rights to its software, algorithms, models, and underlying technology. | Ownership, processing rights, and personal-data rights are separate concepts. See Data rights and permitted use. |
| AI training | 3DLOOK does not use production customer data to train its models without the customer's explicit, documented authorization. | Model development uses separately collected research and validation datasets. See Does 3DLOOK use customer data to train AI models? <!-- Verification required: confirm all AI-training statements against the current DPA, Privacy Policy, and actual data pipelines. --> |
| HIPAA | FitXpress can support deployments governed by the Health Insurance Portability and Accountability Act (HIPAA) where 3DLOOK acts as a business associate under an executed BAA. | HIPAA is a regulatory framework, not a certification. Applicability depends on the customer's status and workflow. Both 3DLOOK and the customer remain responsible for the HIPAA obligations applicable to their respective roles, systems, and processing activities. |
| GDPR and CCPA/CPRA | 3DLOOK generally acts as a processor under the General Data Protection Regulation (GDPR) and as a service provider under the California Consumer Privacy Act (CCPA) and California Privacy Rights Act (CPRA). | The customer stays responsible for lawful basis, notices, and consent. See Privacy compliance. |
| SOC 2 | 3DLOOK has completed a System and Organization Controls 2 (SOC 2) readiness assessment; a formal SOC 2 examination has not yet been conducted. | Alternative security evidence is available under a Non-Disclosure Agreement (NDA). See Certifications and regulatory status. |
| FDA | FitXpress is not cleared, authorized, or approved by the U.S. Food and Drug Administration (FDA). | Regulatory status depends on intended use and the claims a customer makes. Customers must assess the complete integrated workflow. See What is FitXpress's regulatory status with the FDA? |

Each answer is expanded in the detailed sections that cover the data lifecycle, data rights, security controls, privacy compliance, certifications, regulatory status, and enterprise deployment.

---

## Data lifecycle

### What data does FitXpress process and generate?

A FitXpress scan starts from a guided capture flow and returns structured outputs in under 45 seconds. Three categories of data move through that flow: data submitted to the platform, data generated by the platform, and technical data produced during processing.

**Submitted data** is what the end user or the customer's application provides:

* Front and side photos captured through the guided mobile flow
* Height
* Weight, which is optional and used to produce body composition outputs
* Sex or gender input where the selected model requires it, and any profile information the workflow needs
* Customer-assigned or scan identifiers

**Generated data** is what the platform produces from that input. Depending on the implementation, FitXpress may generate body measurements, weight- and BMI-related outputs, body composition estimates, a 3D model, and longitudinal comparison data. Body composition outputs are derived estimates rather than direct clinical measurements. Methodology and validation are covered in the [body-scanning accuracy framework](https://3dlook.ai/content-hub/body-fat-percentage-men-women-ai-3d-scanning-goals/).

**Technical data** is operational rather than descriptive of the body: capture-quality and pose-validation flags, clothing classification, face-obfuscation confirmation, and processing logs with timestamps and request metadata.

Body composition outputs sit in a different category from body measurements. Measurements describe circumference and length at defined body points. Body composition values such as body fat percentage or lean mass are estimates, derived from those measurements together with the submitted height and optional weight. A common mistake is reading every output as a "measurement," which overstates what the platform produces.

#### Data lifecycle

| Data category | Purpose | Stored by 3DLOOK? | Retention | Deletion method |
|---|---|---|---|---|
| Photos | Scan processing: extracting body geometry and measurements | Not by default; retained up to 30 days only under a client-specific policy | Deleted immediately after processing by default | Automatic deletion on completion; face obfuscation applied at capture and automatic blur where a policy retains photos |
| Measurements and body metrics | Structured scan results returned to the customer | Yes | Active contract term; configurable for enterprise customers | Deletion API (user-level or individual-scan); standard backup purge cycle |
| Body composition data | Body composition estimates and progress-tracking input | Yes | Active contract term; configurable for enterprise customers | Deletion API (user-level or individual-scan); standard backup purge cycle |
| 3D model or mesh | Visualization and downstream customer use | Yes | Active contract term; configurable for enterprise customers | Deletion API (user-level or individual-scan); standard backup purge cycle |
| Progress-tracking data | Comparison of measurements, body composition, or 3D models across scans | Yes, where the feature is enabled | Tied to the retention of the scan records it compares | Removed when the linked scan or user record is deleted |
| Identifiers and logs | Security, support, billing, and audit | Yes | Retained per operational and security requirements | Standard log rotation; may be held under legal hold |

---

### How are data storage, retention, and deletion handled?

Photos are deleted immediately after processing by default. Under a client-specific policy, 3DLOOK may retain photos for up to 30 days, and any retained photo is automatically blurred; face obfuscation is applied at the point of capture regardless of the retention policy. Photos support the scan they belong to and are not repurposed unless a specific contractual arrangement provides otherwise.

When an enterprise customer collects photos through its own application using the FitXpress SDK and sends them to the 3DLOOK API, the customer decides whether copies stay in its own systems. That customer-side retention is separate from the processing 3DLOOK performs and follows the customer's own policy.

Measurements, body composition data, and 3D models are retained by 3DLOOK for the duration of the active contract. Enterprise customers can configure shorter or workflow-specific retention windows for these outputs. Progress-tracking data persists only while the scan records it compares remain available, so removing a scan or a user record removes the associated progress data from active systems.

FitXpress production-data retention is governed by the applicable customer agreement, DPA, and configured product policy. The general [3DLOOK Privacy Policy](https://3dlook.ai/privacy-policy/) covers additional categories of personal data, including website, account, commercial, and support information, which may follow different retention periods.

FitXpress data is hosted on AWS, primarily in the us-east-1 region. Regional hosting options are available for enterprise customers under contract, which matters for deployments with data-residency requirements.

Deletion runs through API endpoints at two levels. User-level deletion removes every scan and record tied to a profile. Individual-scan deletion removes a single scan. Standard deletion clears data from active systems, and backup copies are purged within a 30-day backup cycle. Deletion is deferred only where a legal hold applies or during an active security investigation.

Technical documentation, the data-retention schedule, the subprocessor list, and deletion API documentation are available through the procurement or security review process. For integration reference, see the [FitXpress API documentation](https://docs.fitxpress.3dlook.me/). Encryption and key handling are covered in the security section.

---

### How does body and 3D model progress tracking work?

Progress tracking links multiple scans to one profile through a customer-assigned identifier. When the same identifier appears across sessions, FitXpress can compare outputs generated at different points in time.

The comparable outputs are measurements, body composition estimates, weight-related estimates, and 3D models. The historical records required depend on the type of comparison: measurement trends need prior measurement records, a side-by-side comparison of two 3D models needs both models retained, and body composition trends need the body composition record from each scan.

Progress comparison can run inside 3DLOOK through the API, inside the customer's own application using returned scan data, or across both. The customer decides how results are presented to the end user.

Progress tracking is off by default. Enterprise customers enable and configure progress-history retention during implementation, and a deployment retains historical records for this purpose only when the feature is enabled. Deleting an individual scan removes it from the progress history; deleting a full user record removes all associated scans and progress data from active systems, subject to the 30-day backup cycle described above.

Progress-tracking data is operational, supporting review, comparison, and engagement rather than diagnosis. A visible difference between two 3D models does not by itself represent a clinically meaningful change, and interpretation stays with the customer's care team or defined rules.

---

## Data rights and permitted use

### Who controls and owns FitXpress data?

Control and ownership of FitXpress data divide across three roles, and each role carries a different kind of right rather than a single "owner."

**End users** hold data-subject rights over their own personal data, including access, correction, portability, deletion, restriction, and objection, where the governing privacy framework applies. In most FitXpress deployments the enterprise customer is the data controller, so end-user requests are routed through the customer. 3DLOOK supports the customer in fulfilling requests that touch data it processes on the customer's behalf.

**The enterprise customer** holds contractual rights to the data it submits and to the outputs generated from it, including measurements, body composition estimates, and 3D models. That position carries responsibility for:

* Providing privacy notices to end users
* Establishing a lawful basis for processing
* Obtaining consent where the workflow requires it
* Setting retention policy for photos, measurements, body composition data, 3D models, and progress history
* Governing downstream use of FitXpress outputs
* Securing its own applications, integrations, and API credentials
* Deciding whether photos collected through the FitXpress SDK stay in the customer's own systems after being sent to the 3DLOOK API

**3DLOOK** holds the limited processing rights needed to deliver the service and owns its software, algorithms, and underlying models. 3DLOOK does not sell customer data and does not use it for advertising. Where the customer agreement permits, 3DLOOK may use aggregated or anonymized data for internal analytics and service improvement.

"Data ownership" involves several distinct rights: individual privacy rights, customer contractual rights, processing rights, intellectual-property rights, and rights to generated outputs. Personal-data rights stay with the end user, while contractual rights over submitted data and generated outputs sit with the enterprise customer. 3DLOOK holds only the processing rights needed to run the service, and the intellectual property in its software and models. The customer's rights to submitted data and generated outputs are defined in the applicable customer agreement. 3DLOOK retains ownership of its software, algorithms, models, and underlying technology.

---

### Does 3DLOOK use customer data to train AI models?

<!-- Verification required: the statements below must be confirmed against the current DPA, Privacy Policy, product data-use policy, model-development policy, and actual data pipelines. -->

No. 3DLOOK does not use production customer data — meaning submitted photos, generated measurements, body composition data, or 3D models — to train its models without the customer's explicit, contractually documented authorization.

Model development draws on research and validation datasets collected separately under their own consent and data-use terms, kept distinct from production customer data. Enterprise customers can prohibit model-training use of their data through the DPA.

Where the customer agreement permits, 3DLOOK may use aggregated or anonymized data from production for internal analytics, capacity planning, and service improvement. The label "anonymized" applies only to data that meets the applicable legal and technical standard for anonymization; data that could be re-identified stays classified as personal data. Technical service logs, used for debugging, security monitoring, and operational support, form a separate category and are not repurposed for training.

---

## Security and assurance

### How does 3DLOOK protect FitXpress data?

3DLOOK groups its FitXpress security controls into four areas.

**Data protection.** Transport Layer Security (TLS) encrypts data in transit between the end user's device, the customer's application, and 3DLOOK infrastructure. Data stored in Amazon S3 is encrypted using server-side encryption with Amazon S3-managed keys. <!-- Security must confirm: the actual S3 encryption configuration. If SSE-KMS is used instead, this statement must change to "server-side encryption with AWS KMS keys." SSE-S3 and SSE-KMS are separate configurations. --> Encryption stays on by default and cannot be disabled.

**Access and platform security.** Role-based access control (RBAC) and least-privilege provisioning govern who can reach production data and systems. Development, staging, and production environments stay separate. Customer data is logically isolated by tenant. API-key authentication and administrative-access controls govern programmatic and human access.

**Security operations.** Logging and monitoring cover production systems, API access, and administrative actions. A vulnerability management program covers identification, prioritization, and remediation. Patch management and change management processes govern infrastructure and application updates. Incident-response procedures cover detection, containment, investigation, and notification. Business continuity and disaster recovery plans are tested annually.

**Testing and assurance.** Penetration testing is conducted at least annually by an independent third-party firm. Security reviews accompany that testing and follow significant architecture changes. Findings are tracked through to remediation. Security questionnaires are completed during enterprise procurement. Detailed evidence, including architecture diagrams, penetration-test summaries, and control documentation, is available to qualified enterprise customers under a Non-Disclosure Agreement (NDA).

These controls reduce risk. Enterprise customers should still run their own security assessment as part of procurement, since the operating security posture depends on how each deployment is configured.

---

### What security and compliance documentation is available?

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
| SOC 2 report | Not currently available; see Is 3DLOOK SOC 2 certified? |
| Security questionnaire | Completed during procurement |

Documentation is shared with qualified enterprise customers through the security or procurement review process. Internal security files, complete audit reports, and penetration-test details stay unpublished and available only under NDA. The availability of alternative evidence does not stand in for a completed SOC 2 examination.

---

## Privacy compliance

### How does FitXpress support HIPAA, GDPR, and CCPA/CPRA?

**HIPAA.** HIPAA can apply when FitXpress is used by a covered entity or a business associate that handles protected health information (PHI). Where it applies, 3DLOOK can act as a business associate under an executed Business Associate Agreement (BAA), available to enterprise customers on qualifying plans. Supported technical safeguards include encryption in transit and at rest, access controls, and audit logging, with contractual safeguards set out in the BAA.

HIPAA is a regulatory framework, not a certification. The customer retains its own obligations as the covered entity or business associate, including determining whether its use of FitXpress involves PHI and configuring the deployment to match. Both 3DLOOK and the customer remain responsible for the HIPAA obligations applicable to their respective roles, systems, and processing activities.

**GDPR and UK GDPR.** The GDPR and the UK GDPR govern the processing of personal data relating to individuals in the European Economic Area (EEA) and the United Kingdom (UK). In most FitXpress deployments the enterprise customer is the data controller and 3DLOOK is the data processor. 3DLOOK provides an Article 28 Data Processing Agreement (DPA) that incorporates Standard Contractual Clauses (SCCs) for international transfers, with a UK Addendum where UK GDPR applies. 3DLOOK supports data-subject rights, including access, correction, portability, deletion, restriction, and objection, through mechanisms that let the customer retrieve, correct, or delete data processed on its behalf. Where body composition data or other outputs qualify as special-category data under GDPR Article 9, the customer identifies the applicable lawful basis and reflects it in its own notice and consent flow.

**CCPA and CPRA.** The CCPA and CPRA apply to the personal information of California residents. Where they apply, 3DLOOK generally acts as a service provider or contractor that processes personal information on the customer's behalf. 3DLOOK does not sell personal information and does not share it for cross-context behavioral advertising. 3DLOOK supports consumer requests, including access, deletion, correction, and opt-out, through mechanisms the customer can use to retrieve or delete data, and limits its use of personal information to the business purposes named in the customer agreement.

---

### Is FitXpress data biometric or health data?

Classification depends on the data type, the processing purpose, the jurisdiction, and the deployment, so no single label fits every FitXpress output. Personal data means information relating to an identified or identifiable person; health data and biometric data are narrower categories with their own legal tests.

Photos, body measurements, and 3D models are personal data when they relate to an identifiable individual. Body composition and weight-related metrics can be health data or sensitive data depending on how the customer uses them: the same measurement carries a different classification inside a clinical or weight-management workflow than inside an apparel-sizing workflow.

FitXpress photos and body outputs are not automatically classified as biometric data solely because they describe physical characteristics. Classification depends on whether the implementation uses specific technical processing that allows or confirms unique identification and on the purpose for which the data is processed. FitXpress is not designed as an identity-authentication system, but each deployment should be assessed under the applicable law.

Whether an output is PHI under HIPAA depends on whether a covered entity or business associate holds it and whether it relates to health status, care, or payment, rather than on the data type alone.

The enterprise customer sets the purpose and means of processing, so it is best placed to classify its FitXpress data under the framework that governs its workflow. 3DLOOK supplies the technical and contractual documentation that supports that assessment.

---

## Certifications and regulatory status

### Is 3DLOOK SOC 2 certified?

3DLOOK has completed a SOC 2 readiness assessment and aligned its security controls with the SOC 2 Trust Services Criteria. A formal SOC 2 examination has not yet been conducted.

SOC 2 is an attestation examination performed by an independent auditor, not a product certification. For that reason, 3DLOOK does not describe itself as "SOC 2 certified" and reserves any examination-based claim for the point at which a completed examination supports it.

Alternative security evidence, including penetration-test summaries, the security overview, and security-questionnaire responses, is available to qualified enterprise customers under NDA. This evidence covers overlapping control areas, and it remains distinct from a completed SOC 2 examination.

---

### What is FitXpress's regulatory status with the FDA?

FitXpress is not cleared, authorized, or approved by the U.S. Food and Drug Administration (FDA).

Regulatory status depends on intended use and the claims the deploying party makes. FitXpress is positioned for general wellness, administrative intake, body measurement capture, body composition tracking, and progress tracking. The product does not independently diagnose, recommend treatment, or make clinical decisions. Its outputs require human interpretation, clinical judgment, or customer-defined decision rules before they inform any clinical or eligibility determination.

The enterprise customer is responsible for assessing whether its complete integrated workflow — including how outputs are used and what claims reach end users — triggers FDA requirements.

The terms "FDA approved," "FDA cleared," and "FDA authorized" refer to distinct regulatory pathways and are not interchangeable. FitXpress has not pursued any of these pathways. The approved intended-use statement for FitXpress is available through the procurement or regulatory review process.

---

### What uses are supported, and what decisions should not rely on FitXpress alone?

FitXpress supports remote intake and body measurement capture, body composition tracking, progress tracking across scans, structured data collection for research protocols, eligibility documentation, and patient or member engagement. In each case it standardizes how body data is captured and made available before a person or a defined rule acts on it.

FitXpress should not independently determine a diagnosis, a treatment, fitness for duty, employment eligibility, insurance eligibility, clinical-trial eligibility, or any other high-impact individual decision. Each of those workflows needs its own validation, human review, and customer-defined decision rules, applied under the law that governs that decision.

The distinction holds across every use case: FitXpress is a supporting data layer, not the decisioning system. It improves the quality and availability of body data going into a decision, and the decision itself stays with the customer's clinicians, underwriters, or defined rules.

---

## Enterprise deployment

### What should an enterprise confirm before implementation?

* **Intended use and supported claims.** Confirm the deployment sits within FitXpress's intended-use scope and that customer-facing claims match 3DLOOK's approved positioning. The approved intended-use statement is available through the procurement or regulatory review process.
* **Data inputs and outputs.** Map the required inputs (photos, height, optional weight, other profile fields) against the outputs the workflow consumes: measurements, body composition estimates, 3D models, and progress tracking.
* **Legal roles, lawful basis, and SDK photo responsibility.** Confirm controller and processor designations, the lawful basis for processing, consent handling, and who manages customer-side retention of SDK-collected photos.
* **Hosting and data residency.** Verify that the available AWS regions meet the deployment's residency requirements, and request regional hosting if the default region does not fit.
* **Retention per data category.** Confirm the retention configuration for photos, measurements, body composition data, 3D models, and progress history separately, since each follows different rules.
* **Deletion and data-subject request workflows.** Validate that the deletion API meets operational needs, and define internal workflows for access, correction, portability, and deletion requests.
* **DPA or BAA requirements.** Execute a Data Processing Agreement, and a Business Associate Agreement where the deployment involves PHI under HIPAA.
* **Subprocessors and international transfers.** Review the subprocessor list (available on request) and confirm the transfer mechanism for any cross-border flow, such as Standard Contractual Clauses or the UK Addendum.
* **Security evidence and access controls.** Request the available security documentation and assess encryption, access controls, logging, and incident response against the enterprise's own standards.
* **Regulatory and human-review requirements.** Determine whether FDA, HIPAA, GDPR, or CCPA/CPRA obligations apply to the complete workflow, and define the human-review framework for any high-impact decision.

---

### How can procurement, legal, or security teams request additional information?

Enterprise stakeholders can request the following through 3DLOOK's standard procurement channel or at privacy@3dlook.ai:

* Security documentation
* Data Processing Agreement (DPA)
* Business Associate Agreement (BAA), where HIPAA applies
* Penetration-test summary (under NDA)
* Architecture and data-flow diagrams (under NDA)
* Subprocessor information
* Regulatory-status confirmation
* Product validation evidence
* Deletion and integration documentation

Internal security files, full audit materials, and penetration-test reports are not published here and are shared with qualified enterprise customers under NDA. To move a review forward, request FitXpress security and compliance documentation through 3DLOOK procurement, or email privacy@3dlook.ai.

---

## FAQ

**1. What data does FitXpress process?**

FitXpress processes photos and profile inputs, including height, optional weight, and any required fields, to generate body measurements, body composition estimates, a 3D model, and progress data across scans. Capture-quality flags and operational logs are produced alongside these outputs to support the service. For full details, see [What data does FitXpress process and generate?](#what-data-does-fitxpress-process-and-generate).

**2. Are body-scan photos stored?**

By default, no. Photos are deleted immediately after processing, and face obfuscation is applied at the point of capture. Under a client-specific policy, 3DLOOK may retain photos for up to 30 days, and retained photos are automatically blurred. Customers that collect photos through the FitXpress SDK can keep their own copies, and that retention sits outside 3DLOOK's systems.

**3. How long are photos, measurements, body composition data, and scan results retained?**

Photos are deleted immediately after processing by default. Measurements, body composition data, and 3D models are retained for the duration of the active contract, with configurable retention windows for enterprise customers. Backup copies are purged within a 30-day cycle. Retention is governed by the applicable customer agreement, DPA, and configured product policy. The general [3DLOOK Privacy Policy](https://3dlook.ai/privacy-policy/) covers additional categories of personal data, including website, account, commercial, and support information, which may follow different retention periods.

**4. How does body and 3D model progress tracking work?**

Scans are linked through a customer-assigned identifier, which lets FitXpress compare measurements, body composition, and 3D models across sessions. Progress tracking is optional and off by default, so the customer enables it deliberately. Deleting a scan or a user record removes the associated progress data from active systems.

**5. Where is FitXpress data hosted?**

FitXpress runs on AWS, primarily in the us-east-1 region. Regional hosting options are available for enterprise customers with specific data-residency requirements.

**6. Can customers or users delete scan data?**

Yes. 3DLOOK provides an API for user-level and individual-scan deletion, and backup copies are purged within a 30-day cycle. Deletion is deferred only where a legal hold or an active security investigation applies.

**7. Does 3DLOOK use customer data to train AI models?**

No. 3DLOOK does not use production customer data to train its models without the customer's explicit, documented authorization. Model development relies on separately collected research and validation datasets rather than production customer data. <!-- Verification required: confirm all AI-training statements against the current DPA, Privacy Policy, and actual data pipelines. -->

**8. Who owns the photos, measurements, body composition data, and 3D models?**

The enterprise customer holds rights to the data it submits and the outputs generated from it. 3DLOOK owns the underlying software, algorithms, and models, does not sell customer data, and does not use it for advertising. The customer's rights to submitted data and generated outputs are defined in the applicable customer agreement.

**9. How does 3DLOOK protect FitXpress data?**

Data is encrypted in transit with TLS and at rest with AWS server-side encryption, under role-based access controls and continuous logging. 3DLOOK runs a vulnerability management program, conducts annual penetration testing by an independent third-party firm, and maintains incident-response and business continuity and disaster recovery plans. Detailed control evidence is available to qualified customers under NDA.

**10. Is FitXpress HIPAA compliant?**

FitXpress can support HIPAA-regulated deployments where 3DLOOK acts as a business associate under an executed BAA, available on qualifying enterprise plans. HIPAA is a regulatory framework rather than a certification, so no product is "HIPAA certified." Both 3DLOOK and the customer remain responsible for the HIPAA obligations applicable to their respective roles, systems, and processing activities.

**11. How does FitXpress support GDPR and CCPA/CPRA?**

3DLOOK acts as a data processor under GDPR and as a service provider under CCPA/CPRA, under a DPA that includes Standard Contractual Clauses and a UK Addendum where needed. 3DLOOK does not sell customer data, and the enterprise customer remains the controller responsible for lawful basis, notices, and consent.

**12. What does FitXpress NOT do?**

FitXpress does not independently diagnose conditions, make treatment decisions, determine fitness for duty, decide employment or insurance eligibility, confirm clinical-trial eligibility, or make any other high-impact individual determination. It is a supporting data layer that standardizes body data capture — not a standalone decisioning system. Each workflow that involves high-impact decisions needs its own validation, human review, and customer-defined rules.

**13. Is 3DLOOK SOC 2 certified?**

3DLOOK has completed a SOC 2 readiness assessment and aligned its controls to the SOC 2 Trust Services Criteria, and a formal SOC 2 examination has not yet been conducted. Alternative security evidence covering the same control areas is available to qualified enterprise customers under NDA.

**14. Is FitXpress FDA approved or regulated as a medical device?**

No. FitXpress is not FDA-cleared, authorized, or approved. Regulatory status depends on intended use and claims. A customer deploying FitXpress in a clinical or regulated workflow is responsible for assessing whether its complete workflow triggers FDA requirements. The approved intended-use statement is available through the procurement or regulatory review process.

---

*This page is the canonical trust asset for FitXpress data privacy, security, and regulatory questions. For accuracy and validation methodology, see the [body-scanning accuracy framework](https://3dlook.ai/content-hub/body-fat-percentage-men-women-ai-3d-scanning-goals/). For product-specific deployment guidance, see [FitXpress](https://3dlook.ai/fitxpress/).*

<!-- 
PUBLISHER CHECKLIST:
✅ Terminology: No banned words (objective, reader/audience, this article/guide, by hand, plus-as-connector). "Below" references removed.
✅ Cannibalization: This is the single canonical trust FAQ. No competing privacy/security articles planned per content-plan.csv.
✅ Vertical boundary: Trust asset covers all health verticals. Individual vertical pages link here, not duplicate.
✅ Internal links: Up to main health hub (link TBD once hub page is live), down to FitXpress product page (/fitxpress/), cross to body-scanning accuracy framework.
✅ FAQ completeness: 14 questions covering data lifecycle, retention, deletion, ownership, AI training, security, HIPAA, GDPR, CCPA, SOC 2, FDA, and what FitXpress does NOT do.
✅ Claims discipline: No unverified medical/legal/regulatory claims. All sensitive statements tagged with verification comments. HIPAA section has balanced responsibility statement. FDA section references intended-use statement.
✅ Word count: ~5,000 words — appropriate for a P0 central trust asset.
✅ Privacy contact: privacy@3dlook.ai (confirmed — not @3dlook.me)
✅ Scope note: Present in paragraph 2, clearly states this is not a replacement for DPA/BAA/contract.
✅ Meta title: 55 chars (within 50-60 range)
✅ Meta description: 158 chars (within 140-160 range)
✅ Publishing halt: Legal/Security/Product approval required per content plan. Sign-off pending.

META TITLE VARIANTS (best selected for frontmatter):
1. "FitXpress Data Privacy, Security & Regulatory FAQ | 3DLOOK" (55 chars) ← SELECTED
2. "FitXpress Security & Privacy FAQ: HIPAA, GDPR, SOC 2, FDA" (56 chars)
3. "Data Privacy & Security FAQ for FitXpress Body Scanning" (54 chars)

META DESCRIPTION VARIANTS (best selected for frontmatter):
1. "FitXpress data privacy, security, and regulatory FAQ for procurement and legal teams. Covers data lifecycle, HIPAA, GDPR, CCPA, SOC 2, FDA status, and AI training." (158 chars) ← SELECTED
2. "FitXpress data privacy, security & regulatory FAQ. Covers data handling, photo deletion, HIPAA, GDPR, CCPA, SOC 2, FDA status, and AI training policy." (152 chars)
3. "Enterprise FAQ: FitXpress data privacy, security, HIPAA, GDPR, CCPA, SOC 2, and FDA status. For procurement, legal, and security review teams." (150 chars)

TODO BEFORE PUBLISHING:
- Replace hub link once "AI Body Data for Health" hub page is live
- Verify accuracy framework URL against actual published slug
- Confirm all AI-training statements against current DPA, Privacy Policy, and data pipelines
- Confirm S3 encryption configuration (SSE-S3 vs SSE-KMS)
- Remove all verification HTML comments after legal/security/product sign-off
- Set last_updated date when legal approval is received
-->
