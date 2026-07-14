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
