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

## FAQ

*Note on structured data: if FAQPage schema is capped below 13 items, prioritize in this order — photos, retention, deletion, AI training, ownership, HIPAA, GDPR, SOC 2, FDA. The remaining questions stay visible on the page outside the schema markup.*

**1. What data does FitXpress process?**

FitXpress processes photos and profile inputs — height, optional weight, and other required fields — to generate 80+ body measurements, body composition data (BMI, BMR, body fat percentage, lean mass, fat mass, Smart Scales estimates), a 3D model, and progress data across scans. Capture-quality flags and operational logs are produced alongside these outputs to support service delivery.

**2. Are body-scan photos stored?**

No. Photos are deleted immediately after processing, typically within 60 seconds, and face obfuscation is applied at the point of capture. Customers who collect photos through their own application or the FitXpress SDK may retain their own copies; that retention sits entirely outside 3DLOOK's systems.

**3. How long are photos, measurements, body composition data, and scan results retained?**

Photos are deleted immediately after processing. Measurements, body composition data, and 3D models are retained for the duration of the active contract, with configurable retention windows available to enterprise customers. Any backup copies are purged within a 30-day cycle.

**4. How does body and 3D model progress tracking work?**

Scans are linked through a customer-assigned identifier, allowing FitXpress to compare measurements, body composition, and 3D models across sessions. Progress tracking is optional — it must be explicitly enabled by the customer rather than running by default.

**5. Where is FitXpress data hosted?**

FitXpress runs on AWS, primarily in the us-east-1 region. Regional hosting options are available for enterprise customers with specific data-residency requirements.

**6. Can customers or users delete scan data?**

Yes. 3DLOOK provides an API for user-level and individual scan deletion, and any corresponding backup copies are purged within 30 days. Deletion can be delayed where a legal hold or active security investigation applies.

**7. Does 3DLOOK use customer data to train AI models?**

No. 3DLOOK does not use customer data to train its models without the customer's explicit authorization. Model development relies on separately collected research datasets, not production customer data.

**8. Who owns the photos, measurements, body composition data, and 3D models?**

The customer owns the data it submits and the outputs generated from it. 3DLOOK owns the underlying software, algorithms, and models, and does not sell customer data or use it for advertising.

**9. How does 3DLOOK protect FitXpress data?**

Data is encrypted in transit and at rest (AWS SSE-S3), with role-based access controls and continuous logging. 3DLOOK maintains a vulnerability management program, conducts annual penetration testing, and maintains incident-response and business continuity/disaster recovery plans. Detailed control evidence is available to qualified customers under NDA.

**10. Is FitXpress HIPAA compliant?**

FitXpress can support HIPAA-regulated deployments where 3DLOOK acts as a business associate under an executed BAA, available to qualifying enterprise plans. HIPAA is a regulatory framework, not a certification, so no product is "HIPAA certified" — compliance depends on how the customer configures and operates its own workflow.

**11. How does FitXpress support GDPR and CCPA/CPRA?**

3DLOOK acts as a data processor (GDPR) or service provider (CCPA/CPRA) under a DPA that includes Standard Contractual Clauses and the UK Addendum where needed. 3DLOOK does not sell customer data, and the enterprise customer remains the controller responsible for lawful basis, notices, and consent.

**12. Is 3DLOOK SOC 2 certified?**

3DLOOK has completed a SOC 2 readiness assessment and aligned its controls to SOC 2 criteria, but has not yet undergone a formal SOC 2 examination. Alternative security evidence covering the same control areas is available to qualified enterprise customers under NDA.

**13. Is FitXpress FDA approved or regulated as a medical device?**

No. FitXpress is not FDA-cleared, authorized, or approved, and is not positioned as a medical device. Customers deploying FitXpress in clinical or regulated workflows are responsible for assessing whether their own complete workflow triggers FDA requirements.
