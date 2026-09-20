---
profile: linkedin-olena
platform: linkedin
article_slug: bariatric-pre-qualification-mobile-3d-body-scanning
product: fitxpress
format: text
status: draft
created: 2026-09-20
---

## Post: linkedin-olena / bariatric-pre-qualification-mobile-3d-body-scanning

**Angle:** Data governance belongs in the pilot plan, not after it. Photos and the record built from them have different lifespans, and the roles have to be explicit before the first capture.
**Claims used:** Photos are deleted immediately after processing or within 30 days, depending on the customer's policy. "In most enterprise deployments, the customer acts as controller and 3DLOOK acts as processor under the General Data Protection Regulation (GDPR)." Encrypted at rest in Amazon S3 and in transit using TLS. Pilot checklist item on data governance: retention, access control, BAA scope, output storage, identifier handling, photo deletion.
**Length:** 158 words / 100-170 words

---

Most remote-capture pilots settle data governance last. That is the wrong order.

A scan produces two things with different lifespans. Photos can be deleted immediately after processing or within 30 days, depending on the customer's policy. The record built from them, the measurements, the timestamp, the quality flags, is what your workflows keep using after the pilot ends.

Roles have to be explicit before the first capture. In most enterprise deployments, the customer acts as controller and 3DLOOK acts as processor under the General Data Protection Regulation (GDPR).

Encryption at rest and in transit is the straightforward part. Who may open a record, and for how long, is what programs settle too late.

I put retention, access control and photo deletion in the pilot plan itself, next to capture completion.

When your last pilot ended, who owned the records it produced, and for how long?

The full article on bariatric intake records is in the comments.

**CTA:** Soft, full article in the comments.

---

### Design tip

**Article visual:** The bariatric pilot checklist table, and its data governance row on retention, access control, Business Associate Agreement scope, output storage, identifier handling and photo deletion.
**Format:** text
**Adaptation:** no visual needed, native platform format.
**Keep:** n/a
