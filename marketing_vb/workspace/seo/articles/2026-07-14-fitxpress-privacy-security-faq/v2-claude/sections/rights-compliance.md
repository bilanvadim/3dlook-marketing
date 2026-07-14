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
