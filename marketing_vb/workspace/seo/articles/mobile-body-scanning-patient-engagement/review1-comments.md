# Review 1 — Editorial Comments

> Source: Google Doc https://docs.google.com/document/d/1rGBWUVHTiesfbelC0VnWwopokxLPrQixgqtpF2xn1zE/edit (tab "Review 1")

Review 1
Overall writing style
General Approach & Language Guardrails for Corporate Content - 3DLOOK - https://docs.google.com/document/d/1dPNXQL62t_y82MFJblBidEvRgwXjJxzADdapB7Pa214/edit?tab=t.0#heading=h.3cw1vsfedk37 is not taken into consideration.
Highest-priority corrections
1. Replace the inaccurate repeatability claim
Current:
Scan-to-scan repeatability of < 1 cm means a small real change registers as signal rather than measurement noise, so a two-week gain shows up instead of washing out.
Problems:
* It changes the approved claim.
* It suggests changes below 1 cm can be reliably detected.
* It promises meaningful results after two weeks without evidence.
* “Repeatability of <1 cm” is technically incomplete.
Use the approved formulation:
For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm. Consistent capture conditions help programs compare results more reliably over time.
Avoid claiming that a specific two-week change will be detectable.
2. Correct the privacy section
This passage appears inconsistent with the currently approved product information:
Photos are deleted immediately or within 30 days under the client’s retention policy, photos are automatically blurred when stored, and no names or personal identifiers are processed.
The approved position is closer to:
* Production photos are deleted after processing.
* Structured outputs can be retained.
* AWS US hosting is standard.
* EU or UK hosting may be available on request.
* HIPAA support should be described carefully, including the BAA where applicable.
Suggested replacement:
Production photos are deleted after processing, while structured outputs may be retained according to the customer’s configuration and agreement. Data is encrypted in transit and at rest. Standard hosting is provided through AWS in the United States, with EU or UK hosting available on request. FitXpress supports HIPAA-compliant workflows, with a Business Associate Agreement available where required, and GDPR-aligned data handling.
3. Remove the GLP-1 discontinuation statistic from “Why this matters now”
The statistic is credible context for a GLP-1 adherence article, but it is poorly matched to a telehealth-wide patient-engagement page. It also weakens the cannibalization guardrail.
Replace it with broader evidence concerning one of these topics:
* Patient engagement in virtual care
* Remote monitoring adherence
* Patient portal or digital-health engagement
* The relationship between digital feedback and continued participation
If no strong broader source is available, the section can work without a second statistic.
4. Soften unsupported cause-and-effect claims
Several statements present plausible engagement mechanisms as established outcomes:
Visible change sustains effort...
Recurrence scans create a rhythm...
The engagement loop produces operational effects...
...gives members a reason to stay and upgrade.
The article currently lacks direct evidence showing that FitXpress or mobile body scanning causes higher engagement, retention, or adherence.
Use language such as:
* “can help patients recognize change”
* “may support continued participation”
* “gives programs an additional engagement signal”
* “creates opportunities for more meaningful check-ins”
* “can support motivation when weight alone does not reflect the full pattern of change”
Positioning issues
The article is too defensive
“What FitXpress does NOT do” occupies a large section and repeats the same limitations again in the FAQ and conclusion. This makes the article feel like a compliance document rather than a patient-engagement article.
Rename it:
Where mobile body scanning fits—and where other methods remain necessary
Then retain only four boundaries:
* Supports review rather than diagnosis
* Does not make clinical or eligibility decisions
* Does not replace required clinical assessments
* Does not guarantee engagement or health outcomes
Fraud and underwriting are unrelated to this article and should be removed.
The opening overstates the weakness of self-reported data
Current:
People misremember, round down, or estimate.
This sounds accusatory toward patients. It also shifts the article toward verification, which belongs more naturally in the BMI-verification cluster.
Suggested version:
Self-reported weight and BMI offer a limited view of change. Readings may come from different scales, capture conditions vary, and a single number cannot show how measurements or body composition are changing.
Avoid “clinical-facing documentation”
Current:
One capture produces both the patient-facing signal and the clinical-facing documentation.
FitXpress provides data that can support documentation; it does not itself create clinical documentation.
Use:
One capture can support both a patient-facing progress experience and a structured record for care-team review.
Remote patient monitoring needs qualification
“Remote patient monitoring” can refer to regulated clinical programs and connected medical devices. The draft risks suggesting that FitXpress supplies clinical monitoring data.
Safer wording:
In remote monitoring and longitudinal care programs, recurring scans can provide an additional body-data record between formal assessment points.
Structural improvements
The article is longer and more repetitive than necessary. I recommend merging:
* “The engagement mechanics of structured body data”
* “The scan-to-scan engagement loop in practice”
* “What improves operationally”
A clearer structure would be:
1. The engagement challenge in remote care
2. What mobile body scanning adds
3. Five ways it can support patient engagement
4. How the scan-to-scan experience works
5. Applications beyond GLP-1
6. Implementation considerations
7. Where FitXpress fits
8. FAQs
9. CTA
This would keep the article focused while preserving its TOFU/MOFU value.
Missing or required internal links
Actual hyperlinks should be added directly to the relevant anchors:
* AI in telehealth → main telehealth hub
* Visual progress tracking for GLP-1 adherence and retention → GLP-1 supporting article
* Beyond BMI → relevant Beyond BMI article
* Mobile body scanning accuracy framework → accuracy article
* FitXpress for telehealth and weight loss → product/use-case page
* How two photos become structured body data → technology or body-data article
* Privacy and data handling → security/privacy resource when available
The GLP-1 links should appear only in the “broader than GLP-1” section, rather than being used to establish the article’s central argument.
Minor editorial problems
* “Section 4” and “Section 10” should be replaced with descriptive anchor text because the headings are unnumbered.
* Expand “BMI” only once; the draft unnecessarily capitalizes the full term again in the FAQ.
* “In under 45 seconds” should preferably be “in approximately 30–45 seconds.”
* “Composition change explains what the scale hides” is too absolute. Use “can provide context that weight alone does not show.”
* “Clinical team” should become “care team” where the audience may include coaches or wellness professionals.
* The conclusion repeats the medical-device disclaimer already stated several times.
* “What FitXpress does NOT do” should use sentence case: “What FitXpress does not do.”
