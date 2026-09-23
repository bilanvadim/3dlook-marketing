---
source: Google Doc 1-55t2X23q4zE1fMn6uBDrMt98QyQzkljVmmDWn9Dao0, tab t.iqf0ijyp2fa6 "Review 1"
fetched: 2026-09-23
applies_to: v1/final.md (the Doc tab "Version 1" = v1/final.md; ChatGPT line numbers refer to the Doc, not the file)
---

# Review 1  <!-- h.t0tcwsqh6mca -->
## Personal feedback:  <!-- h.41r3g1dsfosz -->
- The text reads and feels like a presentation speech, not an article - fact after fact and after another fact, in short sentences without a meaningful connection between. 
- "Still" - overemphasizes diminishing factors: 
| Usable results still depend on suitable capture conditions. |
| RTPV is a capture-quality control, not a clinical posture assessment. |
| Loose, layered, or oversized clothing can still affect the visible body outline. |
| Accessibility, available space, and device placement still matter. |
- So - Contradicts the following established guardrail -https://docs.google.com/document/d/1dPNXQL62t_y82MFJblBidEvRgwXjJxzADdapB7Pa214/edit?tab=t.0#bookmark=id.sol2z8ndrfx9  
“See” - Contradicts the following established guardrail - https://docs.google.com/document/d/1dPNXQL62t_y82MFJblBidEvRgwXjJxzADdapB7Pa214/edit?tab=t.0#bookmark=id.pkx1ckbo9k87   
Revisit General Approach & Language Guardrails for Corporate Content - 3DLOOK - https://docs.google.com/document/d/1dPNXQL62t_y82MFJblBidEvRgwXjJxzADdapB7Pa214/edit?tab=t.0#bookmark=id.sol2z8ndrfx9 
- (Image 1) - Guided capture and quality-control flow: guided instructions, positioning and framing checks (RTPV), clothing check, front and side capture, processing in under 45 seconds, structured results. A retake loop runs back from the checks. Clinical review sits outside the product, in the customer’s workflow.
(Image 2) - Evidence panel with three columns: accuracy against a reference method, repeatability across comparable scans, and capture-quality controls before processing. Definitions only, no figures.
- The placements for the illustration need different formatting to distinguish them from the article’s text

## ChatGPT’s feedback:  <!-- h.9amr6d8535fc -->
The first version is structurally strong and follows the agreed content strategy. I would keep the title, question order, quick-answer table, clinical boundary, internal-link architecture, and the single progress bridge question.
It is not ready to publish yet: several product statements are either too absolute, unsupported, or inconsistent with current public documentation.
## Required corrections  <!-- h.swvjychakoxl -->
| Draft location | Issue | Recommended change |
| Lines 29–31 | “Capture runs only through the SDK” and custom flows produce “meaningfully worse accuracy” are too absolute. Current customer terms describe SDKs as optional, while the privacy policy allows several photo-submission routes. | Say that the standard end-user flow uses the supported SDK to provide guided capture controls. Remove the unsubstantiated accuracy comparison. |
| Lines 39–41 | RTPV is presented as performing pose, framing, and phone-tilt validation as one function. Public copy distinguishes RTPV from gyroscope-based angle guidance. | Separate them: RTPV checks positioning/framing; SDK guidance also supports device-angle requirements. |
| Line 43 | “Skeletal tracking runs on-device or live in the browser” is vague and unsupported. Face obfuscation is also unrelated to explaining RTPV. | Delete this sentence. Face obfuscation belongs in the privacy FAQ. |
| Line 47 | “The photo capture layer…is not customizable” is broader than existing wording. The tutorial may be disabled and replaced with customer instructions before SDK capture. | Say that the core capture flow is standardized, while customers control and brand the surrounding onboarding and results experience. |
| Lines 51–63 | The answer blends real-time correction with retakes after a photo has been submitted. | Distinguish capture-time guidance from a failed or unusable scan requiring another attempt. |
| Lines 67–71 | The exact sport / regular / oversized classification, user prompts, and availability in the response payload need product confirmation. Public pages use different terms, including “baggy or tight,” while the privacy FAQ confirms only that clothing classification exists. | Until confirmed, use broader wording: “The Clothing Detector identifies clothing conditions that may interfere with capture and can prompt corrective action.” |
| Line 81 | “The single biggest factor in measurement accuracy” is unsupported and conflicts with the accuracy framework’s multi-factor treatment. | Delete it. State that no single public percentage or ranking describes the effect of individual capture conditions. |
| Lines 91–93 | The full accuracy and repeatability block is accurate in principle but partially duplicates the canonical Accuracy Framework. | Keep the definitions and one concise proof point. Link to the framework for validation figures, tested population, and methodology. |
| Line 115 | The disability-training statement is a sensitive product and legal claim not supported by the public source set. | Remove it unless Product and Legal explicitly approve the wording and evidence. Retain the practical accessibility and alternative-path guidance. |
| Line 121 | “Standard indoor lighting is fine, and any background works” is too broad and potentially incorrect. | Replace with: “Users should follow the on-screen guidance for lighting, distance, framing, and phone placement.” |
| Line 147 | “Camera SDK (React) for web and hybrid apps” may confuse React with React Native. The Admin Panel also does not replace integration. | Use “web and mobile SDKs, including supported iOS and Android integrations.” Describe the Admin Panel as a complementary monitoring and export interface. |
| Line 149 | “Results can stay server-side only…user sees a submission confirmation” is implementation-specific and unsupported. | Replace with: “The customer controls which outputs appear in its interface and how they are routed for review.” |
| Lines 157–165 | The draft defines “under 45 seconds” as processing only. Live pages currently use several formulations: full flow under a minute, processing under 40 seconds, processing under 45 seconds, and full pipeline under 45 seconds. | Choose one centrally approved definition before publication. The safest current construction is: “The guided capture flow typically takes under a minute, while processing time varies by implementation and capture outcome.” |
| Line 171 | “Access to the device’s camera roll is disabled” is an unnecessary implementation claim. | Keep only: “Users cannot upload existing photos in the standard guided FitXpress capture flow.” Current product copy supports that answer. |
## Cannibalization check  <!-- h.2xm2ffg929c9 -->
The page remains sufficiently differentiated after those corrections.
- Two Photos → Structured Body Data continues to own the technology and output pipeline.
- Accuracy Framework owns evidence, validation methodology, accuracy, repeatability, and robustness.
- Telehealth product page owns deployment and conversion intent.
- Privacy FAQ owns data handling and regulatory matters.
- Patient Engagement owns detailed progress presentation.
- This FAQ owns capture reliability, user guidance, exceptions, self-scanning, and operational implementation.
I would shorten the accuracy subsection by approximately one paragraph. It currently risks becoming a second accuracy explainer rather than an operational FAQ.
## What should remain unchanged  <!-- h.cepyzgrl4w8p -->
- The H1 is correct.
- The quick-answer table works well.
- “RTPV is not a clinical posture assessment” is an important distinction.
- The exception-handling answer is valuable once the unsupported disability statement is removed.
- “FitXpress is not a medical device” is the approved formulation.
- The progress section correctly uses fat mass and lean mass, not “muscle mass.”
- Body Progress is accurately limited to customer-selected scans matched by scan ID.
- Two visuals are enough; neither duplicates the article’s existing tables.
- The pilot-oriented next step is stronger than a generic sales conclusion.
Overall, this is a good first version. The necessary work is primarily claim control and technical precision, not restructuring.
