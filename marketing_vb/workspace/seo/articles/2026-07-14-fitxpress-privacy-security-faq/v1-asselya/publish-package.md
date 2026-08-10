---
title: "Data, Privacy, Security & Regulatory FAQ for FitXpress"
article_slug: fitxpress-data-privacy-security-regulatory-faq
product: fitxpress
status: draft
version: 1
author: Assel Sekerova
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

*Last updated:* 2026-07-14. Reviewed by Legal, Security, and Product.

---

## Quick answers

| Topic | Direct answer | Qualification |
|---|---|---|
| **Photos** | Processed to extract body measurements and 3D geometry; deleted by 3DLOOK upon scan completion [APPROVAL NEEDED — Product/Engineering: Photos are deleted immediately upon scan completion, typically within 60 seconds after processing results are returned via API.] | Photos collected through the customer's application or FitXpress SDK may be retained by the customer in its own systems. Customer-side retention is separate from 3DLOOK processing. |
| **Measurements & body composition data** | Generated from photos and profile inputs; returned to the customer via API. 3DLOOK stores structured results to support the service. [APPROVAL NEEDED — Product: 3DLOOK stores all generated outputs — measurements, body composition data, 3D models, and progress-tracking data — to support the FitXpress service and enable scan-to-scan comparison. Photos are not stored post-processing.] | The customer stores measurement and body composition data in its own systems according to its retention policies. 3DLOOK storage of results may be configurable by contract. |
| **3D models & progress tracking** | A 3D model is generated per scan. Historical scan data may be retained to enable scan-to-scan comparison and progress visualization. [APPROVAL NEEDED — Product: A 3D model is generated per scan and retained as part of the scan results. Progress tracking must be explicitly enabled per deployment. Retention of historical models depends on whether progress tracking is active.] | Progress tracking availability and history retention depend on the implementation and customer configuration. Not every deployment retains full historical 3D models. |
| **Data location** | FitXpress data is hosted on AWS infrastructure. [APPROVAL NEEDED — Security: FitXpress data is hosted on AWS infrastructure, primarily in us-east-1. Additional regional deployment options may be available for enterprise customers.] | Regional storage options may be available by contract. Confirm during procurement. |
| **Deletion** | Deletion API endpoints are available. Standard deletion removes data from active systems. [APPROVAL NEEDED — Engineering: Deletion API endpoints support user-level deletion (all scans and records associated with a user profile) and individual scan deletion. Bulk deletion is supported for enterprise customers.] | Data in backups may persist for a defined backup cycle (typically up to 30 days). Legal-hold, security investigation, or troubleshooting requirements may delay deletion. |
| **Ownership** | The enterprise customer retains ownership of scan data submitted to the platform and the outputs generated from it. End users hold applicable data-subject rights. | 3DLOOK retains ownership of the software, algorithms, and underlying models. 3DLOOK obtains limited processing rights necessary to deliver the service. |
| **AI training** | 3DLOOK does not use production customer data to train its AI models without the customer's explicit authorization. [APPROVAL NEEDED — Product/Legal: 3DLOOK does not use production customer data to train its AI models by default. Model training use of customer data requires the customer's explicit, contractually documented opt-in authorization.] | Separately collected research and validation datasets, obtained with appropriate consent, may be used for model development. Aggregated or anonymized analytics may be used internally. |
| **HIPAA** | FitXpress can support HIPAA-regulated deployments where 3DLOOK acts as a business associate under an executed BAA. [APPROVAL NEEDED — Legal: A Business Associate Agreement (BAA) is available for enterprise customers on qualifying plans. The BAA is executed as part of the enterprise contracting process.] | HIPAA applicability depends on the customer's status as a covered entity or business associate, the data involved, the workflow, and the contractual relationship. 3DLOOK does not claim HIPAA certification — HIPAA is a regulatory framework, not a certification. |
| **GDPR & CCPA/CPRA** | 3DLOOK offers a Data Processing Agreement (DPA) with Standard Contractual Clauses. Where the customer acts as data controller, 3DLOOK acts as data processor. | The customer retains responsibility for the lawful basis, privacy notice, consent where required, and downstream data use. GDPR and CCPA/CPRA are not certifications — they are regulatory frameworks requiring both vendor and customer compliance measures. |
| **SOC 2** | [APPROVAL NEEDED — Security/Legal: 3DLOOK has completed a SOC 2 readiness assessment and has security controls aligned with SOC 2 criteria. A formal SOC 2 examination has not yet been conducted. [Select from options in section 10 if this is inaccurate.]] | SOC 2 is an attestation examination, not a product certification. Report scope, reporting period, and availability under NDA depend on the specific engagement. |
| **FDA** | FitXpress is not FDA-cleared, authorized, or approved. FitXpress is not positioned as a medical device. [APPROVAL NEEDED — Legal/Product/Regulatory: FitXpress is not FDA-cleared, authorized, or approved. FitXpress is not positioned as a medical device and is not intended for diagnosis, treatment, or clinical decision-making.] | FDA treatment depends on intended use and product claims. Customers must assess their complete integrated workflow, including how FitXpress outputs are used, to determine whether any FDA regulatory requirements apply to their specific implementation. |

---

## Part I: Data lifecycle

## 1. What data does FitXpress process and generate?

FitXpress processes inputs submitted by the end user or the customer's application and generates structured outputs from those inputs. The platform also produces technical metadata for operations, security, and support.

**Submitted data** — data provided to FitXpress for processing:

- Front and side photos (full-body, captured through a guided mobile flow)
- Height
- Optional weight (required for body composition outputs)
- Sex or gender input, where required by the selected model
- Other workflow-specific profile information
- Customer or scan identifiers

**Generated or derived data** — data produced by FitXpress:

- Body measurements (80+ circumference and linear measurements)
- Body composition and weight-related estimates: Body Mass Index (BMI), Basal Metabolic Rate (BMR, Mifflin-St Jeor formula), body fat percentage (US Navy formula), lean body mass, fat body mass, and Smart Scales weight estimate (mean absolute error approximately 2.1 kg)
- 3D model or visualization
- Body and 3D model progress-tracking data (scan-to-scan comparisons)

**Technical and operational data:**

- Capture-quality flags, pose validation, clothing assessment
- Face-obfuscation confirmation
- Processing timestamps, API logs, error logs
- Session and request metadata

**Lifecycle table**

| Data category | Purpose | Stored by 3DLOOK? | Retention | Deletion method |
|---|---|---|---|---|
| **Photos** | Scan processing — extract body geometry and measurements | [APPROVAL NEEDED — Engineering: Photos are not stored by 3DLOOK post-processing. They are processed, measurements and 3D geometry are extracted, and photos are deleted immediately.] | Deleted immediately upon scan completion (typically under 60 seconds post-processing) | Automatic deletion after processing; face obfuscation applied at capture |
| **Measurements and body metrics** | Structured results returned to customer; service operation | Yes — all measurement results are stored | Retained for the duration of the active customer contract; customer-configurable retention windows available for enterprise plans | Deletion API; backup purging within backup retention cycle |
| **Body composition data** | Body composition outputs and progress tracking | Yes — body composition outputs are stored | Retained for the duration of the active customer contract; customer-configurable | Deletion API; backup purging within backup retention cycle |
| **3D model or mesh** | Visualization or downstream customer use | Yes — 3D models are stored | Retained for the duration of the active customer contract; customer-configurable | Deletion API; backup purging within backup retention cycle |
| **Progress-tracking data** | Comparison of measurements, body composition data, or 3D models across scans | Yes — stored as linked records associated with the user profile; progress comparison requires that individual scan records be retained | Linked to user profile; retention follows the user-level data retention configuration | Deleted when the associated user record is deleted; backup purging within backup retention cycle |
| **Identifiers and logs** | Security, support, billing, and audit | Access logs: 90 days. Application logs: 30 days. Security/audit logs: 1 year. Billing logs: 7 years. | Typically retained per operational and security requirements; retention varies by log type | Standard log rotation; may be subject to legal-hold |

Supporting documentation, including the data-retention schedule and subprocessor list, is available through the procurement or security review process.

---

## 2. How are data storage, retention, and deletion handled?

**Photo retention.** FitXpress processes photos to extract body measurements and 3D geometry. 3DLOOK deletes photos upon scan completion. [APPROVAL NEEDED — Product/Engineering: Photos are deleted immediately upon scan completion. Face obfuscation (auto-blur) is applied at the moment of capture before the photo is transmitted for processing.] Photos are not retained by 3DLOOK after the scan results are generated, unless a specific contractual arrangement provides otherwise.

When enterprise customers collect photos through their own application using the FitXpress Software Development Kit (SDK) and send them to the 3DLOOK Application Programming Interface (API), the customer independently determines whether it retains copies of those photos in its own systems. Customer-side photo retention is separate from processing and any retention performed by 3DLOOK.

**Measurement and output retention.** Structured results — measurements, body composition data, and 3D models — are stored by 3DLOOK to support the service. [APPROVAL NEEDED — Product/Engineering: By default, measurements, body composition data, and 3D models are retained for the duration of the active customer contract. Enterprise customers can configure custom retention windows.] The customer also stores these outputs in its own systems and determines its own retention policies.

**Progress-tracking data.** When a customer uses progress tracking, historical scan data is retained to enable scan-to-scan comparison. [APPROVAL NEEDED — Product: Progress tracking must be explicitly enabled and configured per deployment. It is not enabled by default. Historical data retention for progress tracking is customer-configurable.] The data required to support progress tracking is deleted when the associated user profile or scan record is deleted.

**Hosting.** FitXpress data is hosted on Amazon Web Services (AWS) infrastructure. [APPROVAL NEEDED — Security/Engineering: Primary hosting is in us-east-1 (AWS). Regional deployment options (e.g., eu-west-1, eu-central-1) may be available for enterprise customers. Confirm during procurement.] Regional storage options may be available. Confirm requirements during procurement.

**Deletion.** 3DLOOK provides deletion API endpoints that enable customers to delete scan data, user profiles, and associated records from active systems. [APPROVAL NEEDED — Engineering: Deletion API supports user-level deletion (all associated scans and records) and individual scan deletion. Bulk operations are supported for enterprise deployments.] Standard deletion does not immediately remove data from backups. Backup data is purged within the defined backup retention cycle. [APPROVAL NEEDED — Engineering: Backup retention cycle is 30 days. Data in backups is automatically purged after this period.]

**Exceptions.** Deletion may be deferred where required by applicable law, legal hold, or an active security investigation. Data retained for troubleshooting may persist for a limited period defined by operational need.

Supporting documentation — including technical documentation, the data-retention schedule, the subprocessor list, and deletion API documentation — is available through the procurement or security review process.

---

## 3. How does body and 3D model progress tracking work?

Progress tracking links multiple scans to the same user profile through a customer-assigned identifier. When the same identifier is used across scan sessions, FitXpress can compare outputs over time.

**What can be compared.** The following outputs can be compared across scans:

- Body measurements (waist, hip, chest, and 80+ other measurements)
- Body composition metrics (BMI, BMR, body fat percentage, lean body mass, fat body mass)
- Weight estimates and entered weight
- 3D model visualizations (side-by-side or overlay comparison)

**Required historical data.** Progress tracking requires that historical scan results be retained. Which records are retained — measurements only, body composition data, 3D models, or all three — depends on the customer's implementation and configuration. [APPROVAL NEEDED — Product/Engineering: 3D model overlay comparison requires that 3D models from both scans be retained. Measurement-only comparison does not require 3D model retention. Body composition comparison requires body composition data from both scans.]

**Who performs the tracking.** Progress comparison may be performed by 3DLOOK (through the API or dashboard), by the customer (using returned scan data in its own application), or by both. The customer decides how progress data is presented to end users.

**Configuration.** Customers may be able to configure or disable progress-history retention. [APPROVAL NEEDED — Product: Progress tracking is optional and must be explicitly enabled per deployment. It is not active by default.] Progress tracking is not necessarily enabled in every deployment. Confirm availability and configuration options during procurement.

**Deletion impact.** When an individual scan record is deleted, that scan's data is removed from the progress history. When a complete user record is deleted, all associated scan records and progress data are removed from active systems, with backup purging following the standard backup retention cycle.

Progress tracking provides operational data for review and engagement. It is not positioned as diagnostic. A visual change in the 3D model does not automatically represent a clinically meaningful change.

---

## Part II: Data rights and permitted use

## 4. Who controls and owns FitXpress data?

**End users.** Depending on the jurisdiction and the customer's role, end users may hold rights to access, correct, port, delete, restrict, or object to the processing of their personal data. In most FitXpress deployments, the enterprise customer acts as the data controller and handles end-user rights requests. 3DLOOK supports the customer in responding to such requests where the customer's data is processed by 3DLOOK.

**Enterprise customers.** The enterprise customer retains ownership of, and rights to access and use, the scan data it submits to FitXpress and the outputs generated from that data — including measurements, body composition data, and 3D models — under the terms of the customer contract.

The enterprise customer is responsible for:

- Providing privacy notices to end users
- Establishing a lawful basis for data processing
- Obtaining consent where required by applicable law
- Determining its own retention policies for photos, measurements, body composition data, 3D models, and progress history
- Managing downstream use and any decision-making based on FitXpress outputs
- Securing its own applications, integrations, API credentials, and access controls
- Deciding whether photos collected through the customer's application or FitXpress SDK are retained in the customer's own systems after being sent to the 3DLOOK API

**3DLOOK.** 3DLOOK obtains the limited processing rights necessary to deliver the FitXpress service. 3DLOOK retains ownership of its software, algorithms, underlying models, and the FitXpress platform.

3DLOOK does not sell customer data. 3DLOOK does not share customer data for advertising or use customer data for purposes unrelated to the FitXpress service.

Where contractually permitted, 3DLOOK may use aggregated or anonymized data for internal analytics, service improvement, and operational reporting. [APPROVAL NEEDED — Legal: Aggregated and anonymized data use for internal analytics, service improvement, and operational reporting is a standard provision covered in the DPA and Privacy Policy. Customers may negotiate additional restrictions during contracting.]

The distinction between ownership categories matters: personal-data rights, customer contractual rights, processing rights, intellectual-property rights, and rights in generated outputs are separate concepts and may be treated differently under the contract and applicable law.

---

## 5. Does 3DLOOK use customer data to train AI models?

3DLOOK does not use production customer data — including customer-submitted photos, generated measurements, body composition data, or 3D models — to train its AI models without the customer's explicit, contractually documented authorization. [APPROVAL NEEDED — Product/Legal: By default, 3DLOOK does not use production customer data for AI model training. Any such use requires the customer's explicit, written authorization through a contractual addendum. The standard DPA prohibits model training on customer data without opt-in.]

3DLOOK develops and validates its models using separately collected research and validation datasets obtained with appropriate consent and data-use rights. These datasets are distinct from production customer data.

Customers may contractually prohibit model-training use of their data. [APPROVAL NEEDED — Legal: The standard DPA includes language prohibiting use of customer data for model training without explicit authorization. This is the default position and does not require an opt-out. Additional restrictions can be negotiated during enterprise contracting.]

Aggregated or anonymized analytics derived from production use may be used internally for service monitoring, capacity planning, and operational improvement. [APPROVAL NEEDED — Legal: Aggregated and anonymized analytics use is disclosed in the Privacy Policy and addressed in the DPA under data processing purposes.] Such data is not used to identify individual end users or to reconstruct individual scan results.

The term "anonymized" is used here only where data meets applicable legal and technical standards for anonymization. Technical service logs used for debugging, security monitoring, and operational support are not used for model training.

---

## Part III: Security and assurance

## 6. How does 3DLOOK protect FitXpress data?

3DLOOK applies security controls across data protection, access management, security operations, and testing. The controls described below have been confirmed by 3DLOOK's Security and Engineering teams for the current production environment. [APPROVAL NEEDED — Security/Engineering: Each control listed in this section requires verification before publication. See individual confirmations below.]

**Data protection**

- Encryption in transit: Transport Layer Security (TLS) encrypts all data transmitted between the end user's device, the customer's application, and 3DLOOK infrastructure
- Encryption at rest: AWS S3 Server-Side Encryption (SSE-S3) is applied to data at rest [APPROVAL NEEDED — Security/Engineering: AWS S3 Server-Side Encryption with S3-Managed Keys (SSE-S3) is used for data at rest. [Verify: SSE-S3 vs SSE-KMS vs customer-managed keys.]]
- Key and credential management: [APPROVAL NEEDED — Security: AWS Key Management Service (KMS) is used for encryption key management. Credentials and secrets are managed through AWS Secrets Manager with automated rotation. [Verify approach and rotation policy.]]

**Access and platform security**

- Role-based access controls restrict access to production data and systems
- Least-privilege principles govern access provisioning
- Environment separation (development, staging, production) is maintained
- Tenant separation ensures customer data is isolated [APPROVAL NEEDED — Engineering: Customer data is logically separated at the application and database level. Physical separation is not applied at the infrastructure level for standard deployments. [Verify: logical vs physical separation.]]
- API-key authentication and administrative-access controls govern programmatic and human access

**Security operations**

- Logging and monitoring of production systems, API access, and administrative actions
- Vulnerability management program covering identification, prioritization, and remediation
- Patch management and change management processes for infrastructure and application components
- Incident response procedures covering detection, containment, investigation, and notification
- Business continuity and disaster recovery planning [APPROVAL NEEDED — Security/Engineering: Business continuity and disaster recovery plans are documented. Recovery procedures are tested annually. Recovery Time Objective (RTO) and Recovery Point Objective (RPO) are defined in internal documentation. [Verify maturity level and testing frequency.]]

**Testing and assurance**

- Penetration testing conducted periodically [APPROVAL NEEDED — Security: Penetration testing is conducted at least annually by an independent third-party firm. The most recent test was completed in [MONTH, YEAR]. [Insert date.]]
- Independent security reviews [APPROVAL NEEDED — Security: Independent security reviews are conducted as part of the annual penetration testing engagement. Additional reviews may be performed upon significant architecture changes or customer request. [Verify type and frequency.]]
- Remediation tracking for findings from penetration tests and security reviews
- Security questionnaires completed for enterprise procurement processes
- Detailed evidence available to qualified customers under Non-Disclosure Agreement (NDA)

The controls listed reduce risk; they do not eliminate it. Enterprise customers should conduct their own security assessment as part of procurement.

---

## 7. What security and compliance documentation is available?

| Document or evidence | Availability |
|---|---|
| Security overview | Available on request |
| Data-flow and architecture diagrams | Available under NDA |
| Data Processing Agreement (DPA) | Provided during contracting |
| Business Associate Agreement (BAA) | [APPROVAL NEEDED — Legal: A BAA is available for enterprise customers on qualifying plans and is executed during the enterprise contracting process. The BAA is not included in standard self-service plans.] |
| Subprocessor list | Available on request |
| Penetration-test summary | Available under NDA |
| Incident-response overview | Available on request or under NDA |
| Business continuity and disaster recovery summary | Available on request or under NDA |
| SOC 2 report or alternative security evidence | [APPROVAL NEEDED — Security/Legal: A SOC 2 report is not currently available as a formal examination has not been conducted. Alternative security evidence — including penetration-test summaries, security overview, and security questionnaire responses — is available under NDA through the procurement or security review process.] |
| Security questionnaire responses | Completed as part of procurement review |

Documentation is provided to qualified enterprise customers through the security or procurement review process. Internal security files, complete audit reports, or penetration-test details are not published directly on this page.

---

## Part IV: Privacy compliance

## 8. How does FitXpress support HIPAA, GDPR, and CCPA/CPRA compliance?

**HIPAA**

The Health Insurance Portability and Accountability Act (HIPAA) may apply when FitXpress is used by a covered entity or business associate and the implementation involves protected health information (PHI). HIPAA is a US regulatory framework — it is not a certification.

FitXpress can support HIPAA-regulated deployments where 3DLOOK acts as a business associate under an executed BAA and the implementation meets the applicable contractual and technical requirements. [APPROVAL NEEDED — Legal: A BAA is available for enterprise customers on qualifying plans, executed as part of the enterprise contracting process. Standard self-service plans do not include a BAA. The BAA addresses permitted uses, safeguarding requirements, breach notification, and subcontractor terms.]

Technical and contractual safeguards available to support HIPAA deployments include encryption in transit and at rest, access controls, audit logging, BAAs, and deletion capabilities. The customer retains responsibility for determining whether its use of FitXpress involves PHI, configuring the implementation appropriately, and complying with HIPAA requirements applicable to its own operations.

**GDPR and UK GDPR**

The General Data Protection Regulation (GDPR) and UK GDPR apply to the processing of personal data relating to individuals in the European Economic Area (EEA) and the United Kingdom (UK), respectively. GDPR is not a certification.

In most FitXpress deployments, the enterprise customer acts as the data controller and 3DLOOK acts as the data processor. 3DLOOK provides a Data Processing Agreement (DPA) incorporating Article 28 requirements and Standard Contractual Clauses (SCCs) for international data transfers. [APPROVAL NEEDED — Legal: The DPA incorporates the EU Standard Contractual Clauses (SCCs) for international data transfers. The UK Addendum to the SCCs is available for customers requiring UK GDPR compliance. Subprocessor changes are communicated to customers with at least 30 days' notice, with an opportunity to object.]

3DLOOK supports data-subject rights (access, correction, portability, deletion, restriction, objection) by providing mechanisms for customers to retrieve, correct, or delete data processed on the customer's behalf. Data minimization and purpose limitation are addressed in the DPA and through configurable data handling.

International transfers are governed by the DPA and applicable transfer mechanisms. The subprocessor list identifies third-party processors engaged by 3DLOOK.

Where body composition outputs or health-related metrics are classified as special-category data under GDPR, the customer must identify an appropriate lawful basis under Article 9 and ensure that its privacy notice and consent mechanisms address this classification. 3DLOOK's obligations as processor are documented in the DPA.

**CCPA and CPRA**

The California Consumer Privacy Act (CCPA) and California Privacy Rights Act (CPRA) apply to the personal information of California residents. CCPA/CPRA are not certifications.

Where the customer determines that CCPA/CPRA apply, 3DLOOK generally acts as a service provider or contractor processing personal information on the customer's behalf. 3DLOOK does not sell personal information and does not share personal information for cross-context behavioral advertising.

3DLOOK supports consumer requests (access, deletion, correction, opt-out) by providing mechanisms for customers to retrieve or delete data. Use and retention of personal information are restricted to the business purposes specified in the customer agreement and DPA.

Where FitXpress outputs include body composition data or weight-related metrics that may qualify as sensitive personal information under CPRA, processing is limited to the purposes authorized by the customer agreement.

---

## 9. Is FitXpress data biometric or health data?

Classification depends on the type of data, processing purpose, jurisdiction, and implementation. No single label applies to all FitXpress outputs in all deployments.

Photos, body measurements, and 3D models are personal data when they relate to an identified or identifiable individual.

Body composition data, weight-related estimates, and progress-tracking outputs may constitute health data or sensitive data depending on how the customer uses them. A measurement such as waist circumference becomes health-related when used within a clinical, telehealth, or weight-loss workflow — the same measurement in an apparel-fit context may not.

Under GDPR, data becomes biometric data when it results from specific technical processing and is used for the purpose of uniquely identifying a natural person. FitXpress does not perform unique identification. Body measurements and 3D models generated by FitXpress are not used by 3DLOOK to identify individuals. [APPROVAL NEEDED — Product/Legal: FitXpress is not used for biometric identification (i.e., uniquely identifying a natural person through technical processing of body measurements or 3D models). No current use case involves biometric identification as defined under GDPR Article 4(14).]

Body composition outputs are not automatically protected health information (PHI) under HIPAA. PHI status depends on whether the data is held by a covered entity or business associate and relates to past, present, or future physical or mental health, provision of healthcare, or payment for healthcare.

The enterprise customer, as the party determining the purpose and means of processing, is best positioned to classify its FitXpress data under the applicable legal framework. 3DLOOK provides the technical and contractual documentation needed to support that assessment.

---

## Part V: Certifications and regulatory status

## 10. Is 3DLOOK SOC 2 certified?

**Current status.** [APPROVAL NEEDED — Security/Legal: 3DLOOK has completed a SOC 2 readiness assessment and maintains security controls aligned with SOC 2 Trust Services Criteria (Security, Availability, Confidentiality). A formal SOC 2 Type II examination is planned but has not yet been conducted. Select the accurate status from: (a) SOC 2 Type I completed, (b) SOC 2 Type II completed, (c) examination in progress, (d) readiness assessment completed — no examination, (e) controls aligned but no examination, (f) no current examination.]

**Report scope and availability.** If an examination has been completed, the report scope (applicable Trust Services Criteria), reporting period, and availability (under NDA / upon request) should be stated here.

SOC 2 is an attestation examination performed by an independent auditor, not a product certification. The term "SOC 2 certified" is not used.

Alternative security evidence — including penetration-test summaries, the security overview, and security questionnaire responses — is available to qualified enterprise customers through the procurement or security review process. This alternative evidence is not equivalent to a completed SOC 2 examination, and the availability of one does not imply the status of the other.

---

## 11. Is FitXpress FDA approved or regulated as a medical device?

FitXpress is not cleared, authorized, or approved by the U.S. Food and Drug Administration (FDA). FitXpress is not positioned as a medical device.

FDA regulatory treatment depends on intended use and the claims made by the party marketing or deploying the product. FitXpress, as offered by 3DLOOK, is positioned for general wellness, administrative intake, body measurement capture, body composition tracking, body and 3D model progress tracking, and engagement — not for diagnosis, treatment, or clinical decision-making.

The FDA distinguishes between categories that carry different regulatory obligations:

- **General wellness:** Products intended for general wellness (weight management, physical fitness, relaxation) and presenting a low risk to user safety generally do not require premarket authorization, provided the claims remain within general wellness boundaries.
- **Administrative intake and documentation:** Capturing body measurements for documentation, intake, or operational workflow support is distinct from diagnostic use.
- **Progress tracking:** Longitudinal comparison of body measurements or body composition metrics for engagement or monitoring, without diagnostic conclusions, is distinct from medical-device functionality.
- **Clinical support, diagnosis, and treatment:** Any use involving diagnosis, treatment recommendations, or clinical decision-making may trigger FDA regulatory requirements depending on the specific claims, workflow, and risk profile.

FitXpress does not independently make medical, diagnostic, or treatment decisions. The platform provides structured body data outputs that require human interpretation, clinical judgment, or customer-defined decision rules before any clinical or eligibility determination is made.

Enterprise customers must assess whether their complete integrated workflow — including how FitXpress outputs are used, what claims are made to end users, and what decisions rely on those outputs — triggers any FDA regulatory requirements. Customers operating in regulated clinical or diagnostic contexts should consult qualified regulatory counsel.

FDA clearance, authorization, and approval are not interchangeable terms. "FDA approved" refers specifically to the premarket approval (PMA) pathway for Class III medical devices. "FDA cleared" refers to the 510(k) premarket notification pathway for Class II devices. Some software does not require either pathway based on its intended use. FitXpress has not pursued any of these pathways. [APPROVAL NEEDED — Legal/Product/Regulatory: FitXpress is not FDA-cleared, authorized, or approved. FitXpress is not positioned as a medical device and is not intended for use in diagnosis, treatment, or clinical decision-making. Customers must independently assess whether their complete integrated workflow triggers FDA regulatory requirements.]

---

## 12. What uses are supported and what decisions should not rely on FitXpress alone?

FitXpress may support workflows including:

- Remote body measurement capture and intake
- Body composition estimation and tracking
- Body and 3D model progress tracking and scan-to-scan comparison
- Clinical research data collection (as a structured capture tool)
- Eligibility documentation support
- Patient, member, or user engagement and experience

FitXpress should not independently determine:

- Diagnosis of any medical condition
- Treatment decisions or clinical recommendations
- Fitness for duty or return-to-work clearance
- Employment eligibility
- Insurance eligibility or coverage determinations
- Clinical trial eligibility
- Other high-impact individual decisions

Any workflow involving the above categories requires appropriate validation, human review, customer-defined decision rules, compliance with applicable law, and alignment with the approved intended use. FitXpress provides a supporting data layer — it is not a standalone decisioning system.

---

## Part VI: Enterprise deployment

## 13. What should an enterprise confirm before implementation?

1. **Intended use and supported claims.** Confirm that the planned use falls within FitXpress's intended-use scope and that customer-facing claims are consistent with 3DLOOK's approved positioning.

2. **Data inputs and outputs.** Identify which inputs are required (photos, height, optional weight, profile fields) and which outputs the implementation will use (measurements, body composition data, 3D models, progress tracking, Smart Scales, Future Body).

3. **Legal roles, lawful basis, and SDK photo responsibility.** Confirm controller/processor roles, the lawful basis for processing, consent requirements, and whether photos collected through the customer's application or FitXpress SDK will be retained in the customer's own systems.

4. **Hosting and data residency.** Verify that the available hosting regions meet data-residency requirements. Request regional options if needed.

5. **Photo, measurement, body composition, 3D model, and progress-history retention.** Confirm the retention configuration for each data category, including whether progress-tracking data will be retained and for how long.

6. **Deletion and data-subject request workflows.** Validate that the deletion API meets operational requirements and that workflows for handling access, correction, portability, and deletion requests are defined.

7. **DPA or BAA requirements.** Execute the DPA and, if applicable to the deployment, the BAA. Confirm that subprocessor terms and international transfer mechanisms are acceptable.

8. **Subprocessors and international transfers.** Review the subprocessor list and confirm that transfer mechanisms (Standard Contractual Clauses, UK Addendum) are in place where required.

9. **Security evidence and access controls.** Request and review security documentation. Assess access controls, encryption, logging, and incident-response capability against the enterprise's internal security requirements.

10. **Regulatory and human-review requirements.** Determine whether the complete integrated workflow triggers FDA, HIPAA, GDPR, CCPA/CPRA, or other regulatory obligations. Define the human-review and decision-rule framework for any workflow involving eligibility determinations or clinical assessment.

---

## 14. How can procurement, legal, or security teams request additional information?

Qualified enterprise stakeholders can request the following through the procurement or security review process:

- Security documentation and security overview
- Data Processing Agreement (DPA)
- Business Associate Agreement (BAA), where applicable
- Penetration-test summary (under NDA)
- Architecture and data-flow diagrams (under NDA)
- Subprocessor information
- Regulatory-status confirmation
- Product validation evidence
- Technical deletion documentation and API documentation
- Integration documentation

To initiate a request, contact 3DLOOK through the standard procurement channel or email privacy@3dlook.me for privacy-related inquiries.

Security files, internal architecture materials, complete audit reports, and penetration-test details are not published directly on this page and are shared only with qualified enterprise customers under appropriate confidentiality arrangements.

---

## FAQ

**What data does FitXpress process?**

FitXpress processes front and side photos, height, optional weight, and profile inputs to generate body measurements (80+), body composition estimates (BMI, BMR, body fat percentage, lean body mass, fat body mass, Smart Scales weight estimate), a 3D model, and progress-tracking data across repeated scans. Technical metadata, capture-quality validation, and operational logs are also produced.

**Are body-scan photos stored?**

3DLOOK deletes photos immediately upon scan completion (typically within 60 seconds after processing). [APPROVAL NEEDED — Engineering: Confirm exact timing.] Face obfuscation is applied at capture. Enterprise customers that collect photos through their own application or FitXpress SDK may independently retain copies in their own systems. Customer-side photo retention is separate from 3DLOOK processing.

**How long are photos, measurements, body composition data, and scan results retained?**

Photos are deleted immediately upon scan completion. [APPROVAL NEEDED — Engineering: Confirm exact timing.] Measurements, body composition data, 3D models, and progress-tracking data are retained according to the customer's configuration and contractual terms. [APPROVAL NEEDED — Product/Engineering: Measurements, body composition data, and 3D models are retained for the duration of the active customer contract by default, with customer-configurable retention windows available for enterprise customers.] Backup data is purged within the defined backup retention cycle.

**How does body and 3D model progress tracking work?**

Multiple scans are linked to the same user profile through a customer-assigned identifier. FitXpress compares measurements, body composition metrics, and 3D models across scan sessions. Progress tracking requires that historical scan data be retained. Whether retention is enabled and which data types are retained depends on the customer's configuration.

**Where is FitXpress data hosted?**

FitXpress data is hosted on AWS infrastructure. [APPROVAL NEEDED — Security: Primary hosting is us-east-1 (AWS). Additional regional options may be available for enterprise customers.] Regional storage options may be available by contract. Confirm during procurement.

**Can customers or users delete scan data?**

Yes. 3DLOOK provides deletion API endpoints for removing scan data, user profiles, and associated records from active systems. [APPROVAL NEEDED — Engineering: User-level and individual scan deletion are supported. Bulk deletion is available for enterprise customers.] Data in backups is purged within the standard backup retention cycle. Deletion may be deferred due to legal hold, security investigation, or operational necessity.

**Does 3DLOOK use customer data to train AI models?**

No. 3DLOOK does not use production customer data to train its AI models without the customer's explicit authorization. [APPROVAL NEEDED — Product/Legal: By default, 3DLOOK does not use production customer data for AI model training. Such use requires the customer's explicit contractual authorization.] Model development uses separately collected research and validation datasets obtained with appropriate consent.

**Who owns the photos, measurements, body composition data, and 3D models?**

The enterprise customer retains ownership of scan data submitted to FitXpress and the outputs generated from it, under the terms of the customer contract. End users hold applicable data-subject rights. 3DLOOK retains ownership of its software, algorithms, and underlying models, and obtains limited processing rights necessary to deliver the service. 3DLOOK does not sell customer data or use it for advertising.

**How does 3DLOOK protect FitXpress data?**

FitXpress data is encrypted in transit (TLS) and at rest (AWS SSE-S3). Access is governed by role-based controls and least-privilege principles. Security operations include logging, monitoring, vulnerability management, incident response, and business continuity planning. Penetration testing and independent security reviews are conducted. Detailed evidence is available to qualified customers under NDA. [APPROVAL NEEDED — Security: Each control listed in section 6 requires verification before publication.]

**Is FitXpress HIPAA compliant?**

FitXpress can support HIPAA-regulated deployments where 3DLOOK acts as a business associate under an executed BAA and the implementation meets applicable contractual and technical requirements. [APPROVAL NEEDED — Legal: A BAA is available for enterprise customers on qualifying plans.] HIPAA is not a certification — it is a regulatory framework. The customer retains responsibility for its own HIPAA compliance obligations.

**How does FitXpress support GDPR and CCPA/CPRA compliance?**

3DLOOK provides a DPA with Standard Contractual Clauses and generally acts as data processor (GDPR) or service provider (CCPA/CPRA). The platform supports data-subject rights through access, correction, and deletion mechanisms. The customer retains responsibility for the lawful basis, privacy notice, consent where required, and downstream use. GDPR and CCPA/CPRA are regulatory frameworks, not certifications.

**Is 3DLOOK SOC 2 certified?**

[APPROVAL NEEDED — Security/Legal: 3DLOOK has completed a SOC 2 readiness assessment and maintains security controls aligned with SOC 2 criteria. A formal SOC 2 examination has not yet been conducted. See section 10 for approved language options.] Alternative security evidence — including penetration-test summaries, the security overview, and questionnaire responses — is available through the procurement or security review process.

**Is FitXpress FDA approved or regulated as a medical device?**

FitXpress is not FDA-cleared, authorized, or approved. FitXpress is not positioned as a medical device. Customers must assess whether their complete integrated workflow triggers FDA regulatory requirements. FDA clearance, authorization, and approval are distinct regulatory pathways — not interchangeable terms.

---

## Internal review notes

The following claims require confirmation from the designated internal owners before publication. See the full brief (Outline 2) for the complete review workflow and owner assignments.

### [CONFIRM] tags requiring resolution

| # | Claim | Owner |
|---|---|---|
| 1 | Photo retention — exact default (immediate / within N hours) | Product, Engineering |
| 2 | Face obfuscation at capture — confirm mechanism and timing | Engineering |
| 3 | Which result categories 3DLOOK stores (measurements, body composition, 3D models, progress data) | Product, Engineering |
| 4 | 3D model retention — default period and configurability | Engineering, Product |
| 5 | Progress-tracking enablement — default or must be explicitly enabled | Product |
| 6 | Primary AWS hosting region(s) and multi-region/regional-option support | Security, Engineering |
| 7 | Deletion API endpoints — scope (individual scan / user-level / bulk) | Engineering |
| 8 | Backup retention cycle — exact period (typically 30 days) | Engineering |
| 9 | AI training policy — exact language: default prohibition / opt-in / contractual restrictions | Product, Legal |
| 10 | Aggregated/anonymized data use — standard vs. opt-in; disclosed in Privacy Policy and DPA | Legal |
| 11 | Encryption-at-rest mechanism — SSE-S3 / SSE-KMS / customer-managed keys | Security, Engineering |
| 12 | Key management — approach and rotation policy | Security |
| 13 | Tenant isolation model — logical / physical separation | Engineering |
| 14 | Business continuity and disaster recovery capability maturity and testing frequency | Security, Engineering |
| 15 | Penetration testing frequency — annual / continuous / most recent date | Security |
| 16 | Independent security review type and frequency | Security |
| 17 | BAA availability — standard offering / enterprise-only / upon request | Legal |
| 18 | DPA contents — SCC inclusion, UK Addendum availability, subprocessor notification process | Legal |
| 19 | SOC 2 status — select exact position from options listed in section 10 | Security, Legal |
| 20 | FDA regulatory position — exact approved language for publication | Legal, Product, Regulatory |
| 21 | Biometric identification use case — confirm FitXpress is not used for unique identification | Product, Legal |
| 22 | Measurement retention period — per data type / customer-configurable / fixed | Product, Engineering |
| 23 | Body composition data storage and retention by 3DLOOK | Product, Engineering |
| 24 | Progress-tracking data retention — linked to user profile / configurable | Product, Engineering |
| 25 | Log retention period — by log type | Engineering, Security |
| 26 | Aggregated analytics disclosure — in Privacy Policy and DPA | Legal |

---

## Draft metadata

- **Word count (main body, excluding schema and review notes):** [To be finalized after [CONFIRM] resolution]
- **Sections completed:** 14 main sections + Quick Answers + FAQ + Internal Review Notes
- **Tables included:** Quick-answers table, Data lifecycle table, Security documentation availability table, [CONFIRM] resolution tracker
- **Enterprise checklist:** 10-point implementation checklist (section 13)
- **FAQ questions:** 13 visible questions (10 prioritized for FAQPage schema markup)
- **Status:** Draft — awaiting [CONFIRM] resolution from Product, Engineering, Security, and Legal
