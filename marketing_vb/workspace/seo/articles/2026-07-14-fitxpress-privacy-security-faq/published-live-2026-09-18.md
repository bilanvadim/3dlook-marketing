---
slug: fitxpress-data-privacy-security-regulatory-faq
product: fitxpress
title: "Data, Privacy, Security & Regulatory FAQ for FitXpress"
status: published
published_url: https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/
author: Asselya Sekerova
article_published_time: 2026-09-16T09:41:48+00:00
article_modified_time: 2026-09-17T13:57:45+00:00
captured_from_live: 2026-09-18
capture_method: "curl of the live page, body converted to markdown; eBook CTA, author bio and empty anchor rows dropped"
source_of_truth: live page
role: "Canonical source for FitXpress data, privacy, security and regulatory facts (Vadim, 2026-09-18). brand-assets/product-info/compliance.md is derived from this file."
---

# Data, Privacy, Security & Regulatory FAQ for FitXpress

[FitXpress](https://3dlook.ai/) turns two smartphone photos and a short profile into structured body data: 80+ body measurements, body composition estimates, a 3D model, and Body Progress comparisons between scans. Enterprise customers integrate FitXpress via an Application Programming Interface (API) or Software Development Kit (SDK) to support telehealth, weight management, wellness, connected fitness, insurance, and research workflows. This FAQ provides a general overview of the data, privacy, security, and regulatory aspects.

Specific terms and operational details vary by contract, deployment, jurisdiction, integration method, and intended use. Accordingly, this summary does not replace or supersede the [Privacy Policy](https://3dlook.ai/privacy-policy/), the [Terms](https://3dlook.ai/terms-and-policies/), or any other applicable agreement governing your use, including, where applicable, a Data Processing Agreement (DPA), Standard Contractual Clauses (SCCs), a Business Associate Agreement (BAA), or the signed customer agreement. This FAQ is provided for informational purposes only. It does not constitute part of any agreement and does not modify, limit, expand, or supersede any rights or obligations outlined in the applicable customer agreement. Your use remains governed by those documents, as applicable.

Procurement, legal, and security teams can request the underlying documentation via the standard procurement channel or by emailing legal@3dlook.me.

## Quick answers

| Topic | Direct answer | Qualification |
|---|---|---|
| Photos | Photos are processed to extract body geometry and measurements, then deleted immediately after processing or within 30 days. | Under a customer-specific policy, 3DLOOK may retain photos for up to 30 days, and retained photos are automatically blurred. Customers who collect photos via the FitXpress SDK determine whether to retain copies in their own systems. |
| Measurements and body composition | Measurements and body composition estimates are generated for each scan and stored by 3DLOOK. | Scan outputs are retained indefinitely unless otherwise specified in the applicable customer agreement, or a deletion request applies. Methodology and validation are covered in the body-scanning accuracy framework. |
| 3D models and progress tracking | A 3D model is generated for each scan. The Body Progress feature compares two scans by their scan IDs to show changes between them. | 3DLOOK does not track individuals or determine whether two scans belong to the same person. The comparison is performed between the customer-selected scans. |
| Data location | FitXpress data is hosted on Amazon Web Services (AWS), primarily in the US-West-2 and partially in the US-East-1 region. | Hosting configuration depends on the deployment environment and applicable customer agreement. |
| Deletion | Customers can request deletion of specific scan outputs by providing the relevant scan identifiers to 3DLOOK. | 3DLOOK cannot identify a specific individual from stored scan records. Deletion handling follows the applicable customer agreement and available technical processes. |
| Ownership | The enterprise customer holds rights to the data it submits and the outputs generated from it; 3DLOOK holds rights to its software, algorithms, models, and underlying technology. 3DLOOK may retain and use anonymized data. | Data ownership involves distinct personal data, contractual, processing, and intellectual property rights, as explained under Data rights and permitted use. |
| AI training | 3DLOOK does not use production customer data to train its models. | Any permitted use of customer data is defined in the applicable DPA and customer agreement. Model development practices are explained in Does 3DLOOK use customer data to train AI models? |
| HIPAA | FitXpress can support HIPAA-governed deployments where 3DLOOK acts as a business associate under an executed BAA, where applicable. | HIPAA (Health Insurance Portability and Accountability Act) is a regulatory framework, not a certification. Applicability depends on the customer’s status and workflow, whether the customer is subject to HIPAA, and whether protected health information is involved. Both 3DLOOK and the customer remain responsible for the HIPAA obligations applicable to their respective roles, systems, and processing activities, where applicable. |
| GDPR and CCPA/CPRA | In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR. Where the California Consumer Privacy Act (CCPA) and California Privacy Rights Act (CPRA) apply, 3DLOOK generally acts as a service provider or contractor. | The customer remains responsible for establishing a lawful basis, providing required notices, and obtaining consent where applicable. The applicable legal roles are explained under Privacy compliance section. |
| SOC 2 | 3DLOOK is working toward obtaining a SOC 2 Attestation Report and has completed an initial readiness assessment aligned with SOC 2 Trust Services Criteria. | Alternative security documentation is available to qualified enterprise customers upon execution of a Non-Disclosure Agreement (NDA). The current examination status is detailed under the Certifications and regulatory status section. |
| UK and EU medical-device classification | An independent regulatory assessment concluded that FitXpress does not meet the definition of a medical device under the UK Medical Devices Regulations 2002 (UK MDR) or the EU Medical Devices Regulation (EU MDR). | The conclusion applies to FitXpress’s current intended purpose and claims. A material change in intended use, including functionality intended to support diagnosis or treatment decisions, would require reassessment. |
| FDA | FitXpress is not cleared, authorized, or approved by the U.S. Food and Drug Administration (FDA). 3DLOOK makes no representation as to whether FDA clearance, authorization, or approval is required for any particular customer’s use case. | Regulatory status depends on intended use and the claims a customer makes. Customers must assess the complete integrated workflow. The applicable regulatory position is explained in What is FitXpress’s regulatory status with the FDA? |

## Data lifecycle

### What data does FitXpress process and generate?

A FitXpress scan begins with a guided capture flow and returns structured outputs in under 45 seconds. The flow includes three categories of data: submitted data, generated data, and technical data produced during processing.

**Submitted data** includes information provided by the end user or the customer’s application:

- Front and side photos captured through the guided mobile flow

- Gender

- Height

- Weight, which is optional and used to produce body composition outputs

**Generated data** includes outputs produced from the submitted information. Depending on the implementation, FitXpress may generate body measurements, weight- and BMI-related outputs, body composition estimates, a 3D model, and comparison outputs between scans. Methodology and validation are covered in the [body-scanning accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/).

**Technical data** is operational rather than descriptive of the body: capture-quality and pose-validation flags, clothing classification, face-obfuscation confirmation, and processing logs with timestamps and request metadata.

Not all FitXpress outputs should be classified as measurements. Body measurements describe circumference and length at defined body points, while body composition values are estimates derived from those measurements and submitted inputs, including height and optional weight.

| Data category | Purpose | Stored by 3DLOOK? | Retention | Deletion method |
|---|---|---|---|---|
| Photos | Scan processing: extracting body geometry and measurements | Depends on the customer’s contract. | Deleted either: (i) within 30 days following the processing or (ii) immediately after the completion of the processing (depending on the customer’s instructions). | Automatic deletion after processing or at the end of the applicable retention period |
| Measurements and body metrics | Structured scan results returned to the customer | Yes | On an ongoing basis, unless otherwise specified in the applicable customer agreement or required in connection with a deletion request | To request deletion, the customer provides the relevant scan identifiers to 3DLOOK. |
| Body composition data | Body composition estimates and related scan outputs | Yes | On an ongoing basis, unless otherwise specified in the applicable customer agreement or required in connection with a deletion request | To request deletion, the customer provides the relevant scan identifiers to 3DLOOK. |
| 3D model or mesh | Visualization and downstream customer use | Yes | On an ongoing basis, unless otherwise specified in the applicable customer agreement or required in connection with a deletion request | To request deletion, the customer provides the relevant scan identifiers to 3DLOOK. |
| Progress-tracking data | Comparison of measurements, body composition, or 3D models across scans | Not stored as a separate person-level record | Based on the scan records selected for comparison | Deletion follows the handling of the underlying scan records |
| Identifiers and logs | Security, support, billing, and audit | Yes | Retained per operational and security requirements | Standard log rotation; may be held under legal hold |

### How are data storage, retention, and deletion handled?

Photos are deleted immediately after processing, or 3DLOOK may retain photos for up to 30 days under a customer-specific policy. Any retained photo is automatically blurred; face obfuscation is applied at capture, regardless of the retention policy. Photos are processed for the purposes defined in the applicable customer agreement. Any additional use, where applicable, requires a separate legal basis and contractual authorization.

When an enterprise customer collects photos through its own application using the FitXpress SDK and sends them to the 3DLOOK API, the customer determines whether copies are retained in its own systems. That customer-side retention occurs entirely outside 3DLOOK’s systems, and the customer is solely responsible for that retention and processing, which are governed by the customer’s own policies.

3DLOOK retains measurements, body composition data, and 3D models on an ongoing basis, unless otherwise specified in the applicable customer agreement or required in connection with a deletion request. The comparison uses the scan records selected by the customer, and deletion of those underlying scan records affects their availability for future comparisons.

FitXpress production data retention is governed by the applicable customer agreement and DPA.

FitXpress data is hosted on Amazon Web Services (AWS), primarily in the US-West-2 region and partially in the US-East-1 region. The deployment environment and applicable customer agreement define the hosting configuration.

Scan records are associated with anonymized identifiers, and 3DLOOK cannot identify a specific individual from the stored data. To request deletion of specific scan outputs, the customer provides the relevant scan identifiers to 3DLOOK. Deletion handling follows the applicable customer agreement and available technical processes.

Technical documentation and the subprocessor list are available through the procurement or security review process. The [**FitXpress API documentation**](https://docs.fitxpress.3dlook.me/) provides integration details. Encryption and key-management controls are described under [**Security and assurance**](#security-assurance).

### How does body and 3D model progress tracking work?

Body Progress compares two scans by their scan IDs and shows how the body has changed between them. The comparison can include measurements, body composition estimates, weight-related estimates, and 3D models, depending on the selected outputs.

3DLOOK does not track individuals or determine whether two scans belong to the same person. The customer selects the scans to be compared, and the comparison is performed between those specific scan records.

The required records depend on the type of comparison: comparing measurements requires the relevant measurement records from each scan; comparing two 3D models requires both models; and comparing body composition requires the relevant body composition records from each scan.

Progress-tracking data is operational and provided for informational purposes only, supporting review, comparison, and engagement rather than diagnosis. It should not be relied upon or construed as medical advice, a diagnosis, or a substitute for professional clinical judgment. A visible difference between two 3D models does not, by itself, represent a clinically meaningful change. Interpretation of results is the sole responsibility of the customer, whether by designated personnel or customer-defined rules. 3DLOOK does not validate, endorse, or assume responsibility for how customers interpret, rely on, or act upon this data.

## Data rights and permitted use

### Who controls and owns FitXpress data?

Rights and responsibilities relating to FitXpress data are divided among end users, enterprise customers, and 3DLOOK.

**End users** hold data subject rights over their personal data, including access, correction, portability, deletion, restriction, and objection, where applicable under the governing privacy framework. In most FitXpress deployments, the enterprise customer is the data controller, so end-user requests are generally routed through the customer. 3DLOOK supports the customer in fulfilling requests that touch data it processes on the customer’s behalf.

**The enterprise customer** holds contractual rights to the data it submits and to the outputs generated from it, including measurements, body composition estimates, and 3D models. The enterprise customer is responsible for:

- Providing privacy notices to end users

- Establishing a lawful basis for processing

- Obtaining consent where the workflow requires it

- Defining applicable retention requirements for photos, measurements, body composition data, and 3D models

- Governing downstream use of FitXpress outputs

- Securing its own applications, integrations, and API credentials

- Determining whether photos collected through the FitXpress SDK are retained in the customer’s own systems after being sent to the 3DLOOK API

3DLOOK holds the limited use rights needed to provide and improve the service, as set out in the applicable customer agreement, and retains ownership of its software, algorithms, and underlying models. 3DLOOK does not sell customer data or use it for advertising. Where permitted by the customer agreement, 3DLOOK may use aggregated or anonymized data for analytics, service improvement, and other purposes described in the applicable agreement.

“Data ownership” therefore involves several distinct rights: individual privacy rights, customer contractual rights, processing rights, intellectual-property rights, and rights to generated outputs. The applicable customer agreement defines the customer’s rights to submitted data and generated outputs.

### Does 3DLOOK use customer data to train AI models?

No. Production customer data is not used for model training unless the customer provides explicit, documented authorization. The applicable DPA and customer agreement define the permitted uses of customer data.

Where permitted by the customer agreement, 3DLOOK may use aggregated or anonymized production data for internal analytics, capacity planning, and service improvement. Data is considered anonymized only when it meets applicable legal and technical standards. Technical service logs, used for debugging, security monitoring, and operational support, form a separate category and are not repurposed for training.

## Security and assurance

### How does 3DLOOK protect FitXpress data?

3DLOOK groups its FitXpress security controls into four areas.

**Data protection.** Transport Layer Security (TLS) encrypts data in transit between the end user’s device, the customer’s application, and 3DLOOK infrastructure. Data stored in Amazon S3 is encrypted using server-side encryption with Amazon S3-managed keys. Encryption is enabled by default and cannot be disabled.

**Access and platform security.** Role-based access control (RBAC) and least-privilege provisioning govern who can access production data and systems. Development and production environments are separated. Tenant isolation logically separates each customer’s data. API key authentication and administrative access controls govern programmatic and human access.

**Security operations.** Logging and monitoring cover production systems, API access, and administrative actions. A vulnerability management program covers identification, prioritization, and remediation. Patch management and change management processes govern infrastructure and application updates, while incident-response procedures cover detection, containment, investigation, and notification. Business continuity and disaster recovery plans are tested regularly.

**Testing and assurance.** Penetration testing is conducted regularly by an independent third-party firm. Security reviews are conducted alongside penetration testing and after significant architecture changes. Findings are tracked until remediation is complete. Security questionnaires are completed as needed during the procurement process, upon the customer’s request. Detailed evidence, including architecture diagrams, penetration-test summaries, and control documentation, is available to qualified enterprise customers under an NDA.

Enterprise customers should conduct their own independent security assessment based on the final deployment configuration.

### What security and compliance documentation is available?

| Document or evidence | Availability |
|---|---|
| Security overview | On request |
| Architecture and data-flow diagrams | Under NDA |
| Data Processing Agreement (DPA) | Available as part of the contracting process upon customer request |
| Business Associate Agreement (BAA) | Available as part of the contracting process for qualifying enterprise deployments |
| Subprocessor list | In the Privacy Policy |
| Penetration-test summary | Under NDA |
| Incident-response overview | Under NDA |
| Business continuity and disaster recovery summary | Under NDA |
| SOC 2 report | 3DLOOK is working toward obtaining the SOC 2 Attestation Report; the current status is described in Is 3DLOOK SOC 2 certified? |
| Security questionnaire | Completed as needed during procurement upon the customer’s request |

Documentation is shared with qualified enterprise customers through the security or procurement review process. Internal security files, audit materials, policies, and penetration test reports are not publicly available and are shared with qualified enterprise customers under an NDA.

## Privacy compliance

### How does FitXpress support HIPAA, GDPR, and CCPA/CPRA?

**HIPAA.** HIPAA may apply when FitXpress is used by a covered entity or a business associate that processes protected health information (PHI). Where it applies, 3DLOOK may act as a business associate under an executed BAA for qualifying enterprise deployments. Supported technical safeguards include encryption in transit and at rest, access controls, and audit logging, with contractual safeguards set out in the BAA and applicable policies.

HIPAA is a regulatory framework, not a certification. The customer is responsible for determining whether its use of FitXpress involves PHI, implementing its own administrative safeguards, and configuring the deployment to meet the applicable requirements. Both 3DLOOK and the customer remain responsible for the HIPAA obligations applicable to their respective roles, systems, and processing activities.

**GDPR and UK GDPR.** The GDPR and the UK GDPR govern the processing of personal data relating to individuals in the European Economic Area (EEA) and the United Kingdom (UK). In most FitXpress deployments, the enterprise customer is the data controller, and 3DLOOK is the data processor. Where applicable, 3DLOOK provides a DPA that incorporates Standard Contractual Clauses (SCCs) for international transfers, with a UK Addendum where UK GDPR applies. 3DLOOK supports data subject rights, including access, correction, portability, deletion, restriction, and objection, through mechanisms available to the customer for data processed on its behalf.

**CCPA and CPRA.** Where the CCPA/CPRA applies to the processing, 3DLOOK generally acts as a service provider or contractor that processes personal information on the customer’s behalf. 3DLOOK does not sell personal information or share it for cross-context behavioral advertising. Sharing with customers to enable the contracted service and with service vendors for technical operations may be considered “sharing” under the CCPA/CPRA, for which end users have opt-out rights. 3DLOOK supports consumer requests, including access, deletion, correction, and opt-out, through mechanisms the customer can use to retrieve or delete data, and limits its use of personal information to the business purposes named in the customer agreement.

### Is FitXpress data biometric or health data?

Classification depends on the data type, the processing purpose, the jurisdiction, and the deployment. No single legal classification applies to every FitXpress output.

Photos, body measurements, and 3D models may constitute personal data when they can be linked to an identifiable individual. Body composition and weight-related metrics can be health data or sensitive data depending on how the customer uses them: the classification of the same measurement may differ between clinical, weight-management, and apparel-sizing workflows. FitXpress provides the same service across sectors, and any health-data qualifiers arise from the healthcare context in which the outputs are used by the customer.

FitXpress photos and body outputs are not automatically classified as biometric data solely because they describe physical characteristics. Biometric data definitions vary across jurisdictions. Some frameworks (such as GDPR) use a functional approach, requiring specific processing designed for identification or authentication; others (such as BIPA) use a categorical approach, listing specific data types. Classification depends on the applicable framework. FitXpress processes photographs and inputs to generate body measurements, models, metrics, and indexes. These outputs are not produced or used for identification or authentication. FitXpress does not process facial features or geometry for identification or authentication and links data only to randomly generated IDs, not user-identifying information.

Health data and PHI classification, however, operate differently. Whether an output is PHI under HIPAA depends on whether a covered entity or business associate holds it and whether it relates to health status, care, or payment, rather than on the data type alone. The classification depends on the applicable legal frameworks and should also be determined considering the customer’s use context and purpose.

The enterprise customer generally determines the purpose of the deployment and must assess how the data is classified within its workflow. 3DLOOK provides the technical and contractual information needed to support that assessment.

## Certifications and regulatory status

### Is 3DLOOK SOC 2 certified?

SOC 2 is an attestation examination performed by an independent auditor, not a product certification. 3DLOOK is working toward obtaining a SOC 2 Attestation Report and has completed an initial readiness assessment aligned with SOC 2 Trust Services Criteria.

Alternative security evidence, including penetration-test summaries, the security overview, and security-questionnaire responses, is available to qualified enterprise customers under NDA. This documentation remains distinct from a completed SOC 2 examination.

### Does FitXpress qualify as a medical device under the UK MDR or EU MDR?

FitXpress does not meet the definition of a medical device under the **UK Medical Devices Regulations 2002 (UK MDR)** or the **EU Medical Devices Regulation (EU MDR)**, based on its current intended purpose and functionality. This conclusion is documented in a Product Classification Assessment prepared by 3DLOOK’s independent regulatory advisors, with a formal confirmation available to qualified enterprise customers.

FitXpress does not diagnose, recommend treatment, provide clinical guidance, or make clinical decisions. Outputs are informational only and require independent interpretation and decision-making. 3DLOOK makes no claims about clinical validity or suitability for medical purposes and is not responsible for health outcomes resulting from use of the outputs. FitXpress does not make, inform, or automate any clinical decisions.

The enterprise customer is responsible for assessing whether its use of FitXpress complies with applicable regulations and for any regulatory obligations arising from the integration of the outputs into its workflow.

### What is FitXpress’s regulatory status with the FDA?

FitXpress has not been cleared, authorized, or approved by the U.S. Food and Drug Administration (FDA). 3DLOOK makes no representation as to whether FDA clearance, authorization, or approval is required for any particular customer’s use case.

FitXpress provides structured body data for use within customer-defined workflows and does not independently determine a diagnosis, treatment recommendation, fitness for duty, employment eligibility, insurance eligibility, clinical-trial eligibility, or other high-impact individual decision.

The enterprise customer is responsible for assessing whether its complete integrated workflow, including how outputs are used and what claims are communicated to end users, triggers FDA requirements. 3DLOOK has no responsibility for the customer’s FDA compliance assessment or obligations.

### What uses are supported, and what decisions should not rely on FitXpress alone?

FitXpress supports remote intake and body-measurement capture, body-composition outputs and Body Progress comparisons between scans, structured data collection for research protocols, structured intake and supporting documentation for customer-managed eligibility workflows, and patient or member engagement.

FitXpress does not independently determine a diagnosis, treatment, medication recommendation, fitness for duty, employment eligibility, insurance eligibility, clinical-trial eligibility, or any other high-impact individual decision. It does not provide dose calculations, symptom tracking, prescribing recommendations, or automated clinical decision support.

These workflows require appropriate validation, human review, and customer-defined decision rules that align with applicable law. Final decisions remain the responsibility of the customer’s clinicians, underwriters, or other designated decision-makers operating under an approved governance process.

## Enterprise deployment

### How can procurement, legal, or security teams request additional information?

Enterprise stakeholders can request the following through 3DLOOK’s standard procurement channel or at legal@3dlook.me:

- Security documentation

- Data Processing Agreement (DPA)

- Business Associate Agreement (BAA), where HIPAA applies

- Penetration-test summary (under NDA)

- Architecture and data-flow diagrams (under NDA)

- Subprocessor information

- Regulatory-status confirmation

- Product documentation and performance information

- Deletion and integration documentation

Internal security files, audit materials, policies, and penetration test reports are not publicly available and are shared with qualified enterprise customers under an NDA.

Related resources: [ Body-scanning accuracy framework  ](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) [ FitXpress product overview ](https://3dlook.ai/)
