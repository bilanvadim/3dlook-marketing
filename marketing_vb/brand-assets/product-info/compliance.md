# Compliance, Privacy & Security (FitXpress)

> **Source of truth: the live [Data, Privacy, Security & Regulatory FAQ for FitXpress](https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/)** (published 2026-09-16, modified 2026-09-17). Captured verbatim in `workspace/seo/articles/2026-07-14-fitxpress-privacy-security-faq/published-live-2026-09-18.md`.
> **Rebuilt from that page on 2026-09-18 on Vadim's instruction** ("our latest article, the most accurate data-privacy and security information — update it everywhere"). Every statement below is the FAQ's, shortened where marked. If this file and the live FAQ ever disagree, the FAQ wins and this file gets fixed. If any other repo file disagrees with this one, this one wins.
> **In content, link to the FAQ instead of restating it.** A vertical page, article or post carries a short, context-specific note and links to the FAQ for storage, retention, deletion, ownership, HIPAA, GDPR, CCPA/CPRA, SOC 2 and FDA answers (content-plan guardrail, v2.0).
> Critical for FitXpress outbound and content aimed at insurance, telehealth, healthcare, occupational health and clinical trials.

## 1. Status at a glance — say this, never that

| Topic | Say (FAQ wording) | Never say |
|---|---|---|
| **HIPAA** | "FitXpress can support HIPAA-governed deployments where 3DLOOK acts as a business associate under an executed BAA, where applicable." A BAA is available for qualifying enterprise deployments. | "HIPAA compliant", "HIPAA-compliant", "HIPAA certified", "HIPAA compliance: maintained". **HIPAA is a regulatory framework, not a certification.** |
| **GDPR / UK GDPR** | Canonical role sentence (§2), verbatim. Where applicable, 3DLOOK provides a DPA that incorporates Standard Contractual Clauses (SCCs) for international transfers, with a UK Addendum where UK GDPR applies. | "GDPR certified". "Follows GDPR principles" / "GDPR-aligned" as the whole answer — the FAQ states roles and contracts, use those. |
| **CCPA / CPRA** | "Where the CCPA and CPRA apply, 3DLOOK generally acts as a service provider or contractor." 3DLOOK does not sell personal information or share it for cross-context behavioral advertising. | "CCPA compliant" as a status. |
| **SOC 2** | "3DLOOK is working toward obtaining a SOC 2 Attestation Report and has completed an initial readiness assessment aligned with SOC 2 Trust Services Criteria." Alternative security documentation is available to qualified enterprise customers under NDA. | "SOC 2 certified", "SOC 2 compliant", "SOC 2 Type II". SOC 2 is an attestation, not a product certification, and 3DLOOK does not have the report yet. |
| **UK / EU medical-device status** | "An independent regulatory assessment concluded that FitXpress does not meet the definition of a medical device under the UK Medical Devices Regulations 2002 (UK MDR) or the EU Medical Devices Regulation (EU MDR)." The conclusion applies to the current intended purpose and claims. Short form, per editorial guardrail #6: **"FitXpress is not a medical device."** | "Medical-device certifications don't apply", "MDR does not apply" (categorical), anything with "positioned as". |
| **FDA** | "FitXpress is not cleared, authorized, or approved by the U.S. Food and Drug Administration (FDA). 3DLOOK makes no representation as to whether FDA clearance, authorization, or approval is required for any particular customer's use case." | "FDA-cleared", "FDA-approved", "FDA does not apply", "no FDA clearance is needed". |
| **AI training** | "3DLOOK does not use production customer data to train its models." (unless the customer gives explicit, documented authorization) | "We never use any data" — aggregated or anonymized data may be used for analytics and service improvement where the agreement permits. |
| **Data location** | "FitXpress data is hosted on Amazon Web Services (AWS), primarily in the US-West-2 and partially in the US-East-1 region." Hosting configuration depends on the deployment environment and the customer agreement. | "Region per client", "EU data residency" — not offered by the FAQ. |

## 2. GDPR roles — canonical sentence, use it verbatim

> In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR.

The FAQ's Quick answers sentence. It replaces the 2026-09-07 ruling's wording ("…acts as controller … acts as processor…"), which is identical in substance and missing "the data". Keep the hedge "In most enterprise deployments": the allocation is contractual and varies. "Customer" is correct here because it names a legal role (terminology guardrails §2.12).

**Now approved because the FAQ publishes them:** DPA incorporating SCCs for international transfers, UK Addendum where UK GDPR applies, UK GDPR alongside GDPR, data-subject rights (access, correction, portability, deletion, restriction, objection) supported through mechanisms available to the customer. **Still not stated anywhere approved:** "Article 28" / "Article 9" by number — the FAQ discusses health-data classification without citing articles.

## 3. Data lifecycle

A scan starts with a guided capture flow and returns structured outputs **in under 45 seconds**.

- **Submitted data:** front and side photos from the guided mobile flow · gender · height · weight (optional; used to produce body composition outputs).
- **Generated data:** body measurements, weight- and BMI-related outputs, body composition estimates, a 3D model, comparison outputs between scans (depending on the implementation).
- **Technical data:** capture-quality and pose-validation flags, clothing classification, face-obfuscation confirmation, processing logs with timestamps and request metadata.

| Data category | Stored by 3DLOOK? | Retention | Deletion |
|---|---|---|---|
| Photos | Depends on the customer's contract | Deleted **immediately after processing, or within 30 days** following processing, per the customer's instructions | Automatic, after processing or at the end of the retention period |
| Measurements and body metrics | Yes | **Ongoing** (indefinitely), unless the customer agreement says otherwise or a deletion request applies | Customer provides the relevant scan identifiers to 3DLOOK |
| Body composition data | Yes | Ongoing, same conditions | Same |
| 3D model / mesh | Yes | Ongoing, same conditions | Same |
| Progress-tracking data | Not stored as a separate person-level record | Follows the scan records selected for comparison | Follows the underlying scan records |
| Identifiers and logs | Yes | Per operational and security requirements | Standard log rotation; may be held under legal hold |

- **Photos:** any retained photo is **automatically blurred**; **face obfuscation is applied at capture**, whatever the retention policy. When a customer collects photos through its own app with the FitXpress SDK, the customer decides whether copies stay in its own systems, and that retention is entirely the customer's.
- **Outputs are stored.** Never write that FitXpress "processes but does not store" data: measurements, body composition and 3D models are retained on an ongoing basis.
- **Deletion:** by scan identifier, on the customer's request. 3DLOOK cannot identify a specific individual from stored scan records. Do not promise self-serve deletion endpoints or a backup cycle — the FAQ names neither.
- **Body measurements vs estimates:** measurements are circumferences and lengths at defined body points; body composition values are estimates derived from them plus height and optional weight (same rule as terminology guardrails §2.13).

## 4. Identifiers, personal data and progress tracking

- Scan records are associated with **anonymized, randomly generated IDs**, not user-identifying information. 3DLOOK cannot identify a specific individual from the stored data.
- Photos, body measurements and 3D models **may be personal data** when they can be linked to an identifiable individual; body composition and weight-related metrics can be health or sensitive data depending on the customer's use. So do **not** write "no personal data", "process zero personal identifiers" or "no personal identifiers stored". Write the ID sentence above instead.
- **Not biometric by default.** Outputs are not produced or used for identification or authentication, and FitXpress does not process facial features or geometry for identification or authentication. Classification varies by jurisdiction (GDPR functional test vs BIPA categorical list).
- **PHI** depends on who holds the data and the context (covered entity or business associate, relation to health status, care or payment), not on the data type. Do not write "we don't process PHI".
- **Body Progress compares two scans by their scan IDs**, chosen by the customer. **3DLOOK does not track individuals or determine whether two scans belong to the same person.** Write "the program compares scans it selects" or "scan-to-scan comparison", never "FitXpress tracks each patient over time". Progress data is informational, not diagnostic; a visible difference between two 3D models is not by itself a clinically meaningful change.

## 5. Security controls (four areas)

| Area | Controls |
|---|---|
| Data protection | **TLS** in transit (device → customer app → 3DLOOK). Data in Amazon S3 encrypted with **server-side encryption using Amazon S3-managed keys (SSE-S3)**, on by default, cannot be disabled. |
| Access and platform | Role-based access control (RBAC) and least-privilege provisioning · separated development and production · tenant isolation (logical separation per customer) · API key authentication and administrative access controls |
| Security operations | Logging and monitoring of production systems, API access and admin actions · vulnerability management · patch and change management · incident response (detection, containment, investigation, notification) · business continuity and disaster recovery plans, tested regularly |
| Testing and assurance | **Penetration testing conducted regularly by an independent third-party firm** · security reviews alongside pen tests and after significant architecture changes · findings tracked to remediation · security questionnaires completed during procurement on request |

Not in the FAQ, so not ours to claim (Vadim 2026-09-18: "the truth is in the article, delete the rest"): KMS / customer-managed keys, "at least annual" pen testing, ISO 27001, specific monitoring vendors, on-device privacy options or modes, consent management by 3DLOOK (the customer obtains consent). The only capture-side privacy control the FAQ names is face obfuscation at capture.

## 6. Ownership and permitted use

- The **enterprise customer** holds contractual rights to the data it submits and to the outputs (measurements, body composition estimates, 3D models). It provides privacy notices, establishes the lawful basis, obtains consent where needed, defines retention, governs downstream use, secures its own apps and API credentials, and decides on SDK-side photo copies.
- **3DLOOK** holds limited use rights to provide and improve the service, owns its software, algorithms and models, **does not sell customer data or use it for advertising**, and may use aggregated or anonymized data where the customer agreement permits.
- **End users** hold data-subject rights; in most deployments requests go through the customer, and 3DLOOK supports the customer.

## 7. Scope of use — what FitXpress supports and does not decide

**Supports:** remote intake and body-measurement capture · body composition outputs and Body Progress comparisons · structured data collection for research protocols · structured intake and supporting documentation for customer-managed eligibility workflows · patient or member engagement.

**Does not independently determine:** a diagnosis, treatment, medication recommendation, fitness for duty, employment eligibility, insurance eligibility, clinical-trial eligibility, or any other high-impact individual decision. It does not provide dose calculations, symptom tracking, prescribing recommendations or automated clinical decision support. Final decisions stay with the customer's clinicians, underwriters or other designated decision-makers.

## 8. Documentation and contacts

| Document | Availability |
|---|---|
| Security overview | On request |
| Architecture and data-flow diagrams · pen-test summary · incident-response overview · BC/DR summary | Under NDA |
| DPA | Part of contracting, on request |
| BAA | Part of contracting, for qualifying enterprise deployments |
| Subprocessor list | In the Privacy Policy |
| SOC 2 report | Not available yet — working toward it (§1) |
| Security questionnaire | Completed during procurement on request |

- **Procurement, legal and security documentation requests:** `legal@3dlook.me` or the standard procurement channel (FAQ).
- **End-user privacy rights and privacy questions:** `privacy@3dlook.me` (the address the Privacy Policy uses, checked 2026-09-18).

## 9. How agents use this file

### Outbound (insurance, telehealth, healthcare, clinical trials, occupational health)
- `message-sequencer` puts one compliance line in message 1 or 2. Pick the variant for the market; do not stack both:
  - **US / health:** "We support HIPAA-governed deployments under a BAA, encrypt data in transit and at rest, and delete photos after processing or within 30 days."
  - **UK / EU:** "In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes SCCs."
- **Insurance underwriting:** structured, timestamped records and the photo-retention choice (immediate or up to 30 days) mapped to their data governance. Underwriting-support only.
- **Clinical trials:** per-customer retention terms, scan records tied to random IDs, documentation available under NDA.
- The line the sequencer used before 2026-09-18 ("We're HIPAA compliant, encrypt at rest with SSE-S3, and process zero personal identifiers.") is **retired**: two of its three claims contradict the FAQ.

### SEO and pages
- Healthcare-facing articles carry a short, context-specific privacy note and **link to the FAQ**; they do not restate its answers (content plan v2.0: privacy rows are "section-first / link to central FAQ").
- Statements taken verbatim from this file are pre-approved. Anything beyond it (new certifications, regions, key management, retention numbers) is invented until the FAQ says it.

### Social posts
- One line at most, only where the post is about a healthcare or insurance use case: "BAA available for HIPAA-governed deployments, photos deleted after processing." Link the FAQ if the post is about privacy itself.

## 10. Ready answers (buyer questions)

**Q: Where is data stored?**
A: On AWS, primarily in US-West-2 and partially in US-East-1. Data in Amazon S3 is encrypted with S3-managed keys (SSE-S3), on by default; TLS protects data in transit.

**Q: How long do you keep photos?**
A: Photos are deleted immediately after processing, or within 30 days under a customer-specific policy. Any retained photo is automatically blurred, and faces are obfuscated at capture.

**Q: And the measurements and 3D models?**
A: Measurements, body composition estimates and 3D models are retained on an ongoing basis unless the customer agreement says otherwise. The customer can request deletion of specific scans by scan identifier.

**Q: Are you HIPAA compliant?**
A: HIPAA is a regulatory framework, not a certification. FitXpress can support HIPAA-governed deployments where 3DLOOK acts as a business associate under an executed BAA; the BAA is available for qualifying enterprise deployments.

**Q: Who is the controller and who is the processor under GDPR?**
A: In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR. 3DLOOK provides a DPA with SCCs, and a UK Addendum where UK GDPR applies.

**Q: Are you SOC 2 certified?**
A: Not yet. 3DLOOK is working toward a SOC 2 Attestation Report and has completed an initial readiness assessment aligned with the SOC 2 Trust Services Criteria. Pen-test summaries, the security overview and questionnaire responses are available under NDA.

**Q: Can we audit your security?**
A: Security documentation is shared with qualified enterprise customers through the procurement or security review process; detailed evidence is under NDA. Requests go to legal@3dlook.me.

**Q: Do you train your AI on our data?**
A: No. 3DLOOK does not use production customer data to train its models unless the customer gives explicit, documented authorization.

**Q: Is FitXpress a medical device? FDA?**
A: An independent regulatory assessment concluded that FitXpress does not meet the definition of a medical device under the UK MDR or EU MDR for its current intended purpose. FitXpress is not cleared, authorized or approved by the FDA, and 3DLOOK makes no representation as to whether clearance is required for a particular use case; the customer assesses its complete integrated workflow.

**Q: Can we use it for diagnosis or eligibility decisions?**
A: No. FitXpress provides structured body data; it does not independently determine a diagnosis, treatment, or any eligibility decision. Those decisions stay with the customer's clinicians, underwriters or other designated decision-makers.

## History

- **2026-09-18** — rebuilt from the live FAQ (Vadim). Retired: "HIPAA: Maintained" / "HIPAA compliant", "Personal identifier processing: None", "We do NOT process PHI", "Medical device certifications: N/A … do not apply", "region per client", "Third-party sharing: never", the outbound line with "process zero personal identifiers". GDPR sentence gained "the data" (FAQ wording). DPA/SCCs/UK Addendum approved. This supersedes the 2026-09-11 decision to leave this file unchanged (`editorial-rewrites.md`).
- **2026-09-07** — GDPR role sentence ruled canonical (Vadim), then without "the data".
