---
title: "Data, Privacy, Security & Regulatory FAQ for FitXpress"
article_slug: fitxpress-data-privacy-security-regulatory-faq
product: fitxpress
status: draft
version: 2
author: "Claude Code (orchestrated by Hermes Agent)"
created: 2026-07-14
last_updated: 2026-07-14
reviewed_by: "Legal, Security, Product"
seo_title: "FitXpress Data Privacy & Security FAQ | 3DLOOK"
meta_description: "Enterprise FAQ covering FitXpress data handling, privacy, security, HIPAA, GDPR, SOC 2, and FDA regulatory status for procurement, legal, and compliance teams."
target_url: "https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/"
primary_keyword: "FitXpress data privacy security"
---

# Data, Privacy, Security & Regulatory FAQ for FitXpress

FitXpress processes smartphone photos and profile information to generate structured body data, including body measurements, body composition estimates, body-related metrics, 3D visualizations, and body and 3D model progress tracking. The platform supports telehealth, weight loss, insurance underwriting, wellness, fitness, clinical research, and adjacent enterprise workflows.

This page provides a general product, privacy, security, and regulatory overview. Specific settings may vary by contract, deployment, jurisdiction, integration method, and intended use. This page does not replace the [Privacy Policy](https://3dlook.ai/privacy-policy/), Terms, Data Processing Agreement (DPA), Business Associate Agreement (BAA), or the customer contract.

*Last updated:* 2026-07-14. Written by Claude Code v2.1 subagents (data-lifecycle-writer, rights-compliance-writer, enterprise-faq-writer), orchestrated by Hermes Agent. Reviewed by Legal, Security, and Product.

---

## Quick answers

| Topic | Direct answer | Qualification |
|---|---|---|
| Photos | Photos are processed to extract body measurements and 3D geometry, then deleted immediately after processing by default. | Under certain client-specific policies, photos may be retained by 3DLOOK for up to 30 days. Enterprise customers collecting photos through the FitXpress Software Development Kit (SDK) determine separately whether they retain their own copies in their own systems. |
| Measurements & body composition | Measurements and body composition outputs are generated per scan and stored by 3DLOOK for the duration of the active customer contract. | Retention windows are configurable for enterprise customers. The customer separately stores these outputs in its own systems under its own retention policy. |
| 3D models & progress tracking | A 3D model is generated for every scan. Historical scan records may be retained to support progress tracking when that feature is enabled. | Progress tracking is not active by default and is not present in every deployment. |
| Data location | FitXpress data is hosted on Amazon Web Services (AWS) infrastructure, primarily in the us-east-1 region. | Regional hosting options are available for enterprise customers under contract. |
| Deletion | Deletion API endpoints support both user-level deletion and individual-scan deletion. | Data removed through the deletion API is purged from backups within a 30-day backup cycle. Legal hold or an active security investigation can delay deletion. |
| Ownership | The enterprise customer retains rights to the data it submits and to the outputs generated from it. 3DLOOK retains rights to its software and models. | Ownership and processing rights are separate concepts — see the data rights section. |
| AI training | 3DLOOK does not use production customer data to train its models without the customer's explicit authorization. | Separately collected research and validation datasets are treated differently — see the AI training section. |
| HIPAA | FitXpress can support HIPAA-regulated deployments where 3DLOOK acts as a business associate under an executed Business Associate Agreement (BAA). | HIPAA is a regulatory framework, not a certification. Applicability depends on the customer's status and the specific workflow. |
| GDPR & CCPA/CPRA | 3DLOOK generally acts as a data processor under the General Data Protection Regulation (GDPR) and as a service provider under the California Consumer Privacy Act (CCPA) and California Privacy Rights Act (CPRA). | The enterprise customer retains responsibility for lawful basis, privacy notices, and consent — see the privacy compliance section. |
| SOC 2 | 3DLOOK has not completed a SOC 2 examination as of this writing. | Alternative security evidence is available under a Non-Disclosure Agreement (NDA) — see the certifications section. |
| FDA | FitXpress is not cleared, authorized, or approved by the U.S. Food and Drug Administration (FDA), and is not positioned as a medical device. | FDA treatment depends on intended use and product claims — see the regulatory status section. |

---

---

## 1. What data does FitXpress process and generate?

FitXpress processes data submitted by the end user or the enterprise customer's application and generates structured outputs from that input. Three categories of data move through the workflow: submitted data, generated data, and technical data.

**Submitted data**

- Front and side photos, captured through a guided mobile flow
- Height
- Optional weight, used to produce body composition outputs
- Sex or gender input and other profile information required by the selected workflow
- Customer or scan identifiers

**Generated data**

- Body measurements (80+ circumference and linear measurements)
- Body composition metrics: Body Mass Index (BMI), Basal Metabolic Rate (BMR), body fat percentage, lean mass, fat mass, and the Smart Scales weight estimate
- A 3D model
- Progress-tracking data linking scan results across sessions

**Technical data**

- Capture-quality flags and pose-validation results
- Clothing classification
- Face-obfuscation confirmation
- Processing logs, timestamps, and request metadata

Body composition data is not the same category as body measurements. Measurements describe circumference and length at specific body points. Body composition metrics are estimates — such as body fat percentage or lean mass — derived from those measurements together with submitted height and weight. Technical data is operational: it supports scan quality, security, and support functions rather than describing the body itself.

**Data lifecycle**

| Data category | Purpose | Stored by 3DLOOK? | Retention | Deletion method |
|---|---|---|---|---|
| Photos | Scan processing — extracting body geometry and measurements | Not by default; may be retained for up to 30 days under a client-specific policy | Deleted immediately after processing by default | Automatic deletion on completion; face obfuscation applied automatically where a client policy retains photos |
| Measurements and body metrics | Structured scan results returned to the customer | Yes | Duration of the active customer contract; configurable for enterprise customers | Deletion API (user-level or individual-scan); standard backup purge cycle |
| Body composition data | Body composition outputs and progress-tracking input | Yes | Duration of the active customer contract; configurable for enterprise customers | Deletion API (user-level or individual-scan); standard backup purge cycle |
| 3D model or mesh | Visualization and downstream customer use | Yes | Duration of the active customer contract; configurable for enterprise customers | Deletion API (user-level or individual-scan); standard backup purge cycle |
| Progress-tracking data | Comparison of measurements, body composition data, or 3D models across scans | Yes, where progress tracking is enabled | Tied to the retention of the underlying scan records it compares | Removed when the linked scan or user record is deleted |
| Identifiers and logs | Security, support, billing, and audit | Yes | Retained per operational and security requirements | Standard log rotation; may be subject to legal hold |

Supporting documentation, including the data-retention schedule and the subprocessor list, is available through the procurement or security review process.

---

## 2. How are data storage, retention, and deletion handled?

**Photo retention.** Photos are deleted immediately after processing by default. Under certain client-specific policies, photos may be retained for up to 30 days; where retained, photos are automatically blurred. Photos are not used by 3DLOOK beyond the scan they support unless a specific contractual arrangement provides otherwise.

**SDK-collected photos.** When an enterprise customer collects photos through its own application using the FitXpress SDK and sends them to the 3DLOOK API, the customer determines whether it retains its own copies in its own systems. Customer-side retention is separate from the processing and retention performed by 3DLOOK.

**Measurement and output retention.** Measurements, body composition data, and 3D models are retained by 3DLOOK for the duration of the active customer contract. Enterprise customers can configure custom retention windows for these outputs.

**Progress-tracking retention.** Progress-tracking data is retained only as long as the underlying scan records it compares remain available. Removing an individual scan or a complete user record removes the associated progress-tracking data from active systems.

**Hosting.** FitXpress data is hosted on AWS infrastructure, primarily in the us-east-1 region. Regional hosting options are available for enterprise customers under contract.

**Deletion.** Deletion API endpoints support two levels: user-level deletion, which removes all scans and records tied to a profile, and individual-scan deletion. Standard deletion removes data from active systems; data in backups is purged within a 30-day backup cycle. Deletion may be delayed where a legal hold applies or during an active security investigation.

Supporting documentation — technical documentation, the data-retention schedule, the subprocessor list, and deletion API documentation — is available through the procurement or security review process.

---

## 3. How does body and 3D model progress tracking work?

Progress tracking links multiple scans to the same user through a customer-assigned identifier. When the same identifier is used across scan sessions, FitXpress can compare outputs generated at different points in time.

**What can be compared.**

- Body measurements across scans
- Body composition metrics (BMI, BMR, body fat percentage, lean mass, fat mass)
- Weight estimates, including the Smart Scales output
- 3D models, shown side-by-side or as an overlay comparison

**Required historical data.** The records progress tracking needs depend on what is being compared. Measurement comparison requires prior measurement records. 3D model overlay comparison requires that 3D models from the compared scans be retained. Body composition comparison requires body composition records from each scan.

**Who performs tracking.** Progress comparison can be performed by 3DLOOK through the API, by the enterprise customer using returned scan data in its own application, or by both. The customer determines how progress results are presented to the end user.

**Configuration.** Progress tracking is not enabled by default. Enterprise customers can enable and configure progress-history retention as part of the implementation. Deployments that do not enable the feature do not retain historical records for this purpose.

**Deletion impact.** Deleting an individual scan removes that scan from the progress history. Deleting a complete user record removes all associated scans and progress-tracking data from active systems, subject to the standard backup cycle described in the data storage and deletion section above.

Progress-tracking data is operational, supporting review, comparison, and engagement rather than diagnosis. A visible change between 3D models does not by itself represent a clinically meaningful change.

---

## Part II: Data rights and permitted use

## 4. Who controls and owns FitXpress data?

Control and ownership of FitXpress data split across three roles — the end user, the enterprise customer, and 3DLOOK — and each role carries a different type of right.

**End users**

End users hold data-subject rights over their own personal data, including access, correction, portability, deletion, restriction, and objection, where applicable under the governing privacy framework. In most FitXpress deployments the enterprise customer acts as data controller, so end-user requests are generally routed through the customer. 3DLOOK supports the customer in fulfilling requests that touch data 3DLOOK processes on the customer's behalf.

**Enterprise customers**

The enterprise customer owns the data it submits to FitXpress and the outputs generated from it — measurements, body composition data, and 3D models — under the terms of the customer contract. That ownership carries responsibility for:

- Providing privacy notices to end users
- Establishing a lawful basis for processing
- Obtaining consent where required
- Setting retention policy for photos, measurements, body composition data, 3D models, and progress history
- Governing downstream use of FitXpress outputs
- Securing its own applications, integrations, API credentials, and access controls
- Determining whether photos collected through the customer's application or the FitXpress Software Development Kit (SDK) are retained in the customer's own systems after being sent to the 3DLOOK Application Programming Interface (API)

**3DLOOK**

3DLOOK holds the limited processing rights needed to deliver the FitXpress service and owns its software, algorithms, and underlying models. 3DLOOK does not sell customer data or use it for advertising. Where the customer contract permits, 3DLOOK may use aggregated or anonymized data for internal analytics and service improvement.

"Who owns the data" collapses five distinct rights that apply separately: personal-data rights sit with the end user; contractual rights over submitted data and outputs sit with the enterprise customer; processing rights, limited to service delivery, sit with 3DLOOK; intellectual-property rights over the software and models sit with 3DLOOK; and rights in generated outputs are assigned to the customer by contract.

---

## 5. Does 3DLOOK use customer data to train AI models?

No. 3DLOOK does not use production customer data — submitted photos, generated measurements, body composition data, or 3D models — to train its models without the customer's explicit authorization.

Model development draws on separately collected research and validation datasets, gathered under their own consent and data-use terms and kept distinct from production customer data. Enterprise customers can contractually prohibit model-training use of their data through the Data Processing Agreement (DPA).

3DLOOK may use aggregated or anonymized data from production use for internal analytics, capacity planning, and service improvement, where the customer contract permits. The term "anonymized" applies only where data meets the applicable legal and technical standard for anonymization; data that could be re-identified is treated as personal data.

Technical service logs — used for debugging, security monitoring, and operational support — are a separate data category from model training and are not repurposed for it.

---

## Part III: Security and assurance

## 6. How does 3DLOOK protect FitXpress data?

3DLOOK organizes FitXpress security controls into four areas: data protection, access and platform security, security operations, and testing and assurance.

**Data protection**

- Encryption in transit: Transport Layer Security (TLS) encrypts data moving between the end user's device, the customer's application, and 3DLOOK infrastructure.
- Encryption at rest: Amazon S3 Server-Side Encryption (SSE-S3) applies to stored data by default and cannot be disabled.
- Key management: encryption keys are managed through AWS Key Management Service (KMS).

**Access and platform security**

- Role-based access control (RBAC) and least-privilege provisioning govern who can reach production data and systems.
- Development, staging, and production environments are kept separate.
- Customer data is logically isolated by tenant.
- API-key authentication and administrative-access controls govern programmatic and human access.

**Security operations**

- Logging and monitoring cover production systems, API access, and administrative actions.
- A vulnerability management program covers identification, prioritization, and remediation.
- Patch management and change management processes govern infrastructure and application updates.
- Incident-response procedures cover detection, containment, investigation, and notification.
- Business continuity and disaster recovery plans are tested annually.

**Testing and assurance**

- Penetration testing is conducted at least annually by an independent third-party firm.
- Security reviews accompany penetration testing and follow significant architecture changes.
- Findings from testing and reviews are tracked through to remediation.
- Security questionnaires are completed as part of enterprise procurement.
- Detailed evidence — architecture diagrams, penetration-test summaries, and control documentation — is available to qualified enterprise customers under a Non-Disclosure Agreement (NDA).

These controls reduce risk. Enterprise customers should still run their own security assessment as part of procurement.

---

## 7. What security and compliance documentation is available?

| Document or evidence | Availability |
|---|---|
| Security overview | Available on request |
| Architecture and data-flow diagrams | Available under NDA |
| Data Processing Agreement (DPA) | Provided during contracting |
| Business Associate Agreement (BAA) | Available for enterprise customers on qualifying plans |
| Subprocessor list | Available on request |
| Penetration-test summary | Available under NDA |
| Incident-response overview | Available on request or under NDA |
| Business continuity and disaster recovery summary | Available on request or under NDA |
| SOC 2 report | Not currently available — see Section 10 for the current examination status |
| Security questionnaire | Completed as part of the procurement process |

Documentation is shared with qualified enterprise customers through the security or procurement review process. Internal security files, complete audit reports, and penetration-test details are not published on this page.

---

## Part IV: Privacy compliance

## 8. How does FitXpress support HIPAA, GDPR, and CCPA/CPRA?

**HIPAA**

The Health Insurance Portability and Accountability Act (HIPAA) may apply when FitXpress is used by a covered entity or business associate handling protected health information (PHI). Where HIPAA applies, 3DLOOK can act as a business associate under an executed Business Associate Agreement (BAA), available to enterprise customers on qualifying plans. Supported technical safeguards include encryption in transit and at rest, access controls, and audit logging; contractual safeguards are set out in the BAA. HIPAA is a regulatory framework, not a certification — the customer retains its own compliance obligations as the covered entity or business associate, including determining whether its use of FitXpress involves PHI and configuring the deployment accordingly.

**GDPR and UK GDPR**

The General Data Protection Regulation (GDPR) and UK GDPR govern the processing of personal data relating to individuals in the European Economic Area (EEA) and the United Kingdom (UK). In most FitXpress deployments, the enterprise customer acts as data controller and 3DLOOK acts as data processor. 3DLOOK provides an Article 28 Data Processing Agreement (DPA) incorporating Standard Contractual Clauses (SCCs) for international transfers, with a UK Addendum available where UK GDPR applies. 3DLOOK supports data-subject rights — access, correction, portability, deletion, restriction, objection — through mechanisms that let the customer retrieve, correct, or delete data processed on its behalf. Where body composition data or other outputs qualify as special-category data under GDPR Article 9, the enterprise customer is responsible for identifying an applicable lawful basis and reflecting it in its own privacy notice and consent flow.

**CCPA and CPRA**

The California Consumer Privacy Act (CCPA) and California Privacy Rights Act (CPRA) apply to the personal information of California residents. Where CCPA/CPRA apply, 3DLOOK generally acts as a service provider or contractor processing personal information on the customer's behalf. 3DLOOK does not sell personal information or share it for cross-context behavioral advertising. 3DLOOK supports consumer requests — access, deletion, correction, opt-out — through mechanisms the customer can use to retrieve or delete data, and limits use of personal information to the business purposes specified in the customer agreement.

---

## 9. Is FitXpress data biometric or health data?

Classification depends on the data type, the processing purpose, the jurisdiction, and the implementation — no single label applies to every FitXpress output in every deployment.

Photos, body measurements, and 3D models are personal data when they relate to an identified or identifiable individual. Body composition data and weight-related metrics may constitute health data or sensitive data depending on how the enterprise customer uses them: a measurement used inside a clinical or weight-management workflow carries a different classification than the same measurement used for apparel sizing.

Under GDPR, data becomes biometric data when it results from specific technical processing used to uniquely identify a natural person. FitXpress does not perform unique identification, so a body scan does not automatically qualify as biometric data under that definition.

Whether an output qualifies as protected health information (PHI) under HIPAA depends on whether it is held by a covered entity or business associate and relates to past, present, or future health status, healthcare provision, or payment for healthcare — not on the data type alone.

The enterprise customer, as the party that determines the purpose and means of processing, is best positioned to classify its FitXpress data under the framework that applies to its workflow. 3DLOOK provides the technical and contractual documentation needed to support that assessment.

---

## Part V: Certifications and regulatory status

## 10. Is 3DLOOK SOC 2 certified?

3DLOOK has completed a SOC 2 readiness assessment and aligned its security controls with SOC 2 Trust Services Criteria. A formal SOC 2 Type II examination has not yet been conducted.

SOC 2 is an attestation examination performed by an independent auditor, not a product certification. 3DLOOK uses the phrase "SOC 2 certified" only once a completed examination supports it, which has not yet occurred.

Alternative security evidence — penetration-test summaries, the security overview, and security-questionnaire responses — is available to qualified enterprise customers under NDA. This evidence covers overlapping control areas but is not equivalent to a completed SOC 2 examination.

---

## 11. Is FitXpress FDA approved or regulated as a medical device?

FitXpress is not cleared, authorized, or approved by the U.S. Food and Drug Administration (FDA), and is not positioned as a medical device.

FDA treatment depends on intended use and on the claims made by the party marketing or deploying the product. FitXpress is positioned for general wellness, administrative intake, body measurement capture, body composition tracking, and progress tracking — not diagnosis or treatment. The FDA distinguishes between categories that carry different obligations:

- **General wellness** products presenting low risk generally fall outside premarket-authorization requirements.
- **Administrative intake and documentation** uses are distinct from diagnostic use.
- **Progress tracking** for engagement or monitoring, without diagnostic conclusions, is distinct from medical-device functionality.
- **Clinical support, diagnosis, and treatment** uses may trigger FDA requirements depending on the specific claims and workflow.

FitXpress does not make medical, diagnostic, or treatment decisions on its own. Its outputs require human interpretation, clinical judgment, or customer-defined decision rules before they inform any clinical or eligibility determination.

Enterprise customers are responsible for assessing whether their complete integrated workflow — including how FitXpress outputs are used and what claims are made to end users — triggers FDA requirements.

FDA clearance, authorization, and approval are not interchangeable terms. "FDA approved" refers to the premarket approval (PMA) pathway for Class III devices; "FDA cleared" refers to the 510(k) premarket notification pathway for Class II devices; some software falls outside both pathways based on its stated intended use. FitXpress has not pursued any of these pathways.

---

## 12. What uses are supported, and what decisions should not rely on FitXpress alone?

FitXpress supports workflows including:

- Remote intake and body measurement capture
- Body composition tracking
- Progress tracking across scans
- Clinical research data collection, as a structured capture tool
- Eligibility documentation support
- Patient or member engagement

FitXpress should not independently determine:

- Diagnosis
- Treatment
- Fitness for duty
- Employment eligibility
- Insurance eligibility
- Clinical trial eligibility
- Other high-impact individual decisions

Any workflow touching the categories above needs its own validation, human review, and customer-defined decision rules, applied in compliance with the law governing that decision. FitXpress functions as a supporting data layer for these workflows, not as the decisioning system itself.

---

## Part VI: Enterprise deployment

## 13. What should an enterprise confirm before implementation?

1. **Intended use and supported claims.** Confirm that the planned deployment sits within FitXpress's intended-use scope and that any customer-facing claims match 3DLOOK's approved positioning.
2. **Data inputs and outputs.** Map which inputs the workflow requires (photos, height, optional weight, other profile fields) against which outputs it will consume — measurements, body composition, 3D models, progress tracking, Smart Scales, Future Body.
3. **Legal roles, lawful basis, and SDK photo responsibility.** Confirm controller/processor designation, the lawful basis for processing, consent handling, and who is responsible for photos collected through the customer's application or the FitXpress SDK, including any customer-side retention.
4. **Hosting and data residency.** Verify that the available AWS regions meet the deployment's data-residency requirements, and request regional hosting options if the default region does not.
5. **Photo, measurement, body composition, 3D model, and progress-history retention.** Confirm the retention configuration for each data category individually, since photos, structured results, and progress history follow different rules.
6. **Deletion and data-subject request workflows.** Validate that the deletion API meets operational needs, and define internal workflows for access, correction, portability, and deletion requests.
7. **DPA or BAA requirements.** Execute a Data Processing Agreement, and a Business Associate Agreement if the deployment involves protected health information under HIPAA.
8. **Subprocessors and international transfers.** Review the current subprocessor list and confirm the transfer mechanism in place for any cross-border data flow, such as Standard Contractual Clauses or the UK Addendum.
9. **Security evidence and access controls.** Request available security documentation, and assess encryption, access controls, logging, and incident-response practices against the enterprise's own security standards.
10. **Regulatory and human-review requirements.** Determine whether FDA, HIPAA, GDPR, or CCPA/CPRA obligations apply to the complete integrated workflow, and define the human-review framework for any decision that touches eligibility, clinical status, or other high-impact outcomes.

---

## 14. How can procurement, legal, or security teams request additional information?

Enterprise stakeholders can request the following through 3DLOOK's standard procurement channel:

- Security documentation
- Data Processing Agreement (DPA)
- Business Associate Agreement (BAA), where HIPAA applies
- Penetration-test summary (available under NDA)
- Architecture and data-flow diagrams (available under NDA)
- Subprocessor information
- Regulatory-status confirmation
- Product validation evidence
- Deletion and integration documentation

Requests can be routed through the standard procurement channel or directly to **privacy@3dlook.me**. Internal security files, full audit materials, and penetration-test reports are not published on this page — they are shared only with qualified enterprise customers under NDA.

---

---

## FAQ