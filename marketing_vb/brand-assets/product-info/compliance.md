# Compliance & Security (3DLOOK)

> Critical for FitXpress outbound to insurance, telehealth, healthcare, occupational health, clinical trials. Always cite when targeting these audiences.

## Certifications & frameworks

| Standard | Status | Scope |
|----------|--------|-------|
| HIPAA | Maintained | FitXpress in US healthcare contexts |
| GDPR | Follows GDPR principles; the customer is controller and 3DLOOK is processor | EU customers and processing. Canonical role sentence below |
| Medical device certifications | N/A | FitXpress does not provide medical advice / diagnosis / treatment recommendations, so device certs do not apply |


### GDPR roles — canonical sentence, use it verbatim

> In most enterprise deployments, the customer acts as controller and 3DLOOK acts as processor
> under GDPR.

**Vadim's ruling, 2026-09-07.** Use this sentence wherever a piece of content states the GDPR
allocation. It does not replace "follows GDPR principles", which stays available as the shorter
form; it is the sentence to reach for when the buyer is asking *who is responsible for what*,
which is what procurement, legal and security teams actually ask.

Why it needed a ruling: the sentence had been shipping since 2026-08-26 (`online fitness
coaching`) and was recorded as "the approved role formulation" by the wellness-platforms hub on
2026-08-31, while the occupational-health article declined it on 2026-09-07 on the correct ground
that no brand-asset carried it. This file is now that asset, and the decline is reversed.

**Scope discipline.** "In most enterprise deployments" is part of the sentence. The allocation is
contractual and varies, so the hedge is not padding and does not get trimmed for length. Anything
beyond the roles themselves — Article 28 DPA, Standard Contractual Clauses, the UK Addendum,
Article 9 special-category data — is **not** approved by this ruling. That material currently
exists only in `workspace/seo/faq-data-privacy-security-clean.md`, which is marked "Draft — not yet
reviewed".

## Data security

| Layer | Implementation |
|-------|----------------|
| Encryption in transit | TLS |
| Encryption at rest | AWS S3 server-side (SSE-S3 managed keys), always on, cannot be disabled |
| Storage | Amazon S3 |
| Access monitoring | Continuous monitoring for unauthorized access attempts |
| Photo blur | Automatic when photos are stored |
| Photo retention | Permanently removed immediately after processing OR within 30 days, per client policy |
| Personal identifier processing | None — photos cannot be linked to individuals via 3DLOOK |
| Third-party sharing | End users' images are never shared with third parties |

## Privacy contact

End users may exercise privacy rights via privacy@3dlook.me

## How agents should use compliance points

### In outbound (insurance, telehealth, healthcare, clinical trials)
- **Always include in step 2 or step 3 of sequence**: "We're HIPAA compliant, encrypt at rest with SSE-S3, and process zero personal identifiers."
- **For insurance underwriting specifically**: highlight audit-ready records + photo retention policy alignment with their data governance.
- **For clinical trials**: highlight per-client retention policy, drift monitoring, traceable records.

### In SEO content
- Articles targeting healthcare buyers should have a dedicated section on compliance posture.
- Link to privacy contact for trust signal.

### In social posts
- For posts on healthcare / insurance use cases, include 1-line compliance reassurance: "HIPAA-compliant, GDPR-aligned, no personal identifiers stored."

## What we do NOT claim

- We are NOT FDA-cleared (we're not a medical device).
- We do NOT provide medical advice or diagnosis.
- We are NOT SOC 2 certified yet (in progress — confirm with Vadim before claiming).
- We do NOT process PHI directly — we process body data only, no patient identifiers.

## Common buyer questions (ready answers)

**Q: Where is data stored?**
A: AWS S3 in [region per client], with mandatory server-side encryption (SSE-S3).

**Q: How long do you keep photos?**
A: We delete photos immediately after processing OR within 30 days, depending on the client policy you choose. When stored, photos are automatically blurred.

**Q: Can we audit your security?**
A: Yes — we provide a security questionnaire, encryption documentation, and walk-throughs. Contact privacy@3dlook.me for a full security review packet.

**Q: Who is the controller and who is the processor under GDPR?**
A: In most enterprise deployments, the customer acts as controller and 3DLOOK acts as processor under GDPR.

**Q: HIPAA Business Associate Agreement?**
A: We sign BAAs for HIPAA-covered customers.

**Q: Do you train your AI on our customer photos?**
A: No. Photos sent through your tenant are deleted per the retention policy and are not used to train the model.

**Q: Can we use this for diagnosis?**
A: No. FitXpress provides body measurements and composition estimates as an information layer. We are not a medical device and do not diagnose.
