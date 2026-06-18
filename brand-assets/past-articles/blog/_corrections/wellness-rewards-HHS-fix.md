---
correction_id: wellness-rewards-HHS-fix
source_article: brand-assets/past-articles/blog/wellness-rewards-verification-employers-insurers-using-ai-3d-body-scanning.md
production_url: https://3dlook.ai/content-hub/wellness-rewards-verification-employers-insurers-using-ai-3d-body-scanning/
discovered_by: fact-check pass during BMI verification v3 rewrite, 2026-05-26
discovered_during: workspace/seo/articles/2026-05-21-online-pharmacy-bmi-verification/v3-fact-checked/fact-check-report.md
correction_date: 2026-05-26
severity: factual_error_in_production_content
auto_pushed_to_wordpress: no — Vadim updates manually
local_archive_fixed: yes — `brand-assets/past-articles/blog/wellness-rewards-verification...md` already corrected
---

# Correction — Wellness Rewards Article: HHS Breach Statistics

## What was wrong

The published article cited HHS health-data-breach statistics that do not match the HHS Office for Civil Rights' Report to Congress for 2023. Both the headline figure and the trend claim were inaccurate.

## Original wrong claim (verbatim, as currently in WordPress)

> "U.S. Department of Health and Human Services (HHS) reported that in 2023 alone, more than **167 million individuals** were affected by large health data breaches, and the number of breaches rose **102% from 2018 to 2023**."

## Corrected claim (with verified source)

> "The U.S. Department of Health and Human Services (HHS) Office for Civil Rights [reported 732 large health data breaches affecting more than **113 million individuals** in 2023](https://www.hipaajournal.com/ocr-reports-congress-hipaa-compliance-data-breaches-2023/), with hacking and IT incidents responsible for **96% of compromised records**."

## Why the change

The "167 million / 102% increase" figures were not supported by HHS OCR's 2023 Report to Congress when re-checked. The verified 2023 figures from OCR are:

- **732** breach reports for breaches affecting 500 or more individuals
- **113,173,613** individuals had PHI exposed, stolen, or impermissibly disclosed
- Hacking and IT incidents accounted for **81% of breaches** and **96% of breached records**
- 22 breaches each affected more than 1 million individuals; the largest was HCA Healthcare at 11.27 million

The "102% increase 2018-2023" claim could not be sourced to any primary HHS publication during re-verification and has been dropped from the corrected version rather than retained without evidence.

## Source URLs

- HIPAA Journal summary of OCR's 2023 Report to Congress (cited in correction): `https://www.hipaajournal.com/ocr-reports-congress-hipaa-compliance-data-breaches-2023/`
- HHS OCR Breach Portal (primary public record): `https://ocrportal.hhs.gov/ocr/breach/breach_report.jsf`

## Location in the article

- **Section:** "Key Considerations for AI-Powered 3D Body Scanning Integrated Wellness Rewards Program Design" → subsection "Privacy and data governance"
- **Approximate position:** First sentence of the second paragraph in that subsection (after the paragraph that mentions HIPAA Security Rule safeguards). Look for "**U.S. Department of Health and Human Services (HHS)**" or "**167 million**" — the latter is the most reliable find string.

## Instructions to update on live WordPress

1. Log into WordPress admin.
2. Open the post titled "Wellness Rewards Verification for Employers & Insurers Using AI 3D Body Scanning" (URL: `/content-hub/wellness-rewards-verification-employers-insurers-using-ai-3d-body-scanning/`).
3. Use the editor's Find function and search for **`167 million`**.
4. Replace the entire sentence — from "U.S. Department of Health and Human Services" through "2018 to 2023." — with the corrected sentence above (including the inline link to HIPAA Journal).
5. Verify the link target opens to `https://www.hipaajournal.com/ocr-reports-congress-hipaa-compliance-data-breaches-2023/`.
6. Re-save / re-publish the post.
7. (Optional but recommended) Add an editorial note in the WordPress post revision log: "Corrected 2026-05-26: replaced inaccurate HHS breach statistic per OCR 2023 Report to Congress."

## Cross-impact check

This was the only article in `brand-assets/past-articles/blog/` that used the 167M / 102% figures. The BMI verification v1 (Katerina-author) draft did not include HHS statistics. The BMI verification v2 (Assel-author) draft DID carry the wrong figures forward — they have been corrected at source in v3 and the v2 draft has been superseded.

## Local archive status

- `brand-assets/past-articles/blog/wellness-rewards-verification...md` — **already updated** to the corrected version at the time this patch was created (2026-05-26).
- Production WordPress site — **not updated**. Vadim updates manually per the instructions above.

## Confirmation checklist (for Vadim after WordPress update)

- [ ] Found and replaced the "167 million" sentence in WordPress
- [ ] Inline link added and verified to open HIPAA Journal
- [ ] Post re-published
- [ ] Editorial note added to revision log
- [ ] Vadim confirms back: "wellness article HHS fix live"
