"""Build the bariatric landing v2 on Nika's fx-bar template.

Takes CSS, logos, the two illustrative mocks and the form/tracking script from
the source HTML (Asselya's edited copy of Nika's draft), writes new copy and
structure per the page kit, regenerates JSON-LD from the visible FAQ.
usage: build_v2.py <source.html> <out.html>
"""
import html
import json
import re
import sys

src = open(sys.argv[1], encoding="utf-8").read()
URL = "https://3dlook.ai/fitxpress/for-bariatric-programs/"
TITLE = "Bariatric Patient Tracking Between Visits | FitXpress"
DESC = ("Bariatric patient tracking between clinic visits: patients scan at home, and FitXpress "
        "returns waist and body composition data to the care team.")
HUB = "https://3dlook.ai/content-hub/bariatric-pre-qualification-mobile-3d-body-scanning/"
assert len(TITLE) <= 60 and len(DESC) <= 155, (len(TITLE), len(DESC))

css = re.search(r"<style>.*?</style>", src, re.S).group(0)
css = css.replace("</style>", """
/* v2 additions */
.fx-bar-page .fx-bar-stats-3{grid-template-columns:repeat(3,minmax(0,1fr))}
.fx-bar-page .fx-bar-record-table tbody th{width:42%;font-size:15px;font-weight:700}
.fx-bar-page .fx-bar-record-table tbody td:nth-child(2){background:none}
.fx-bar-page .fx-bar-record-table thead th:nth-child(2){color:inherit}
.fx-bar-page .fx-bar-related{margin-top:14px;font-size:15px}
#record .fx-bar-progress-layout{align-items:start}
.fx-bar-page .fx-bar-faq summary h3{display:inline;font:inherit;margin:0;letter-spacing:inherit}
@media(max-width:1050px){.fx-bar-page .fx-bar-stats-3{grid-template-columns:1fr}}
</style>""")

trusted = re.search(r'<section class="fx-bar-trusted".*?</section>', src, re.S).group(0)
logos = "\n".join(re.findall(r"<img [^>]+>", trusted))
figures = re.findall(r'<figure class="fx-bar-progress-visual">.*?</figure>', src, re.S)
chart_fig, queue_fig = figures[0], figures[1]
chart_fig = (chart_fig.replace("Your program sets the follow-up schedule", "The program sets the follow-up schedule")
             .replace("Illustrative interface and values, not patient results or a clinical outcome claim.", "Illustrative interface with example values and no clinical outcome claim."))
queue_fig = (queue_fig.replace(" · capture checks passed", "")
             .replace("6–7 October", "6-7 October")
             .replace("Illustrative interface in the program’s patient system; values are examples, not patient results.", "Illustrative interface in the program’s patient system, with example values.")
             .replace("BMI from Smart Scales estimated weight", "BMI from Smart Scales estimate (beta)")
             .replace("<b>44.6</b>", "<b>44.8</b>").replace("<b>44.9</b>", "<b>45.1</b>"))
script = re.search(r"<script>\s*\(function.*?</script>", src, re.S).group(0).replace("fx_vertical: 'bariatric-programs'", "fx_vertical: 'bariatric'")
assert "for-bariatric-programs" in script

E = html.escape

def stat(num, text, label, href):
    return (f'<div class="fx-bar-stat"><b>{num}</b><p>{text}</p><small><a href="{href}" target="_blank" '
            f'rel="noopener">{label}</a></small></div>')

FAQ = [
    ("Does FitXpress measure muscle loss after bariatric surgery?",
     "FitXpress does not measure muscle directly. Its lean mass estimates include organs, bone and water along with muscle, and the "
     "accuracy figures on this page do not cover body composition after surgery. Where the protocol needs a "
     "muscle measure, DXA or BIA stays the method."),
    ("What happens when a patient cannot complete the scan?",
     "The capture needs a smartphone and standing front and side photos; mobility, space and phone access affect "
     "completion. The program sets the retake logic and an in-clinic alternative, and the pilot measures "
     "completion before rollout."),
    ("How does FitXpress perform at higher body weights?",
     "Internal validation covered participants up to 210 kg, aged 16-78, in the US and Europe; performance "
     "outside that range has not been characterized. The pilot checks capture completion and measurement "
     "performance in the program’s own patients, including its heaviest."),
    ("Can a FitXpress record support bariatric prior-authorization documentation?",
     "A FitXpress record can supply part of it. Each insurer or health plan sets its documentation requirements and accepted sources, and some "
     "require a BMI measured at a clinical visit. The program can add dated scan outputs and the BMI inputs to "
     "its supporting records. FitXpress does not guarantee payer acceptance or approval."),
]
DOCS = '<a href="https://docs.fitxpress.3dlook.me/" target="_blank" rel="noopener">FitXpress API documentation</a>'

faq_html = "\n".join(
    f'<details><summary><h3>{q}</h3></summary><p class="fx-bar-answer">{a.format(docs=DOCS)}</p></details>' for q, a in FAQ)

body = f"""<main id="main">
<section class="fx-bar-navy fx-bar-hero" aria-labelledby="hero-heading">
 <div class="fx-bar-wrap">
  <nav class="fx-bar-crumbs" aria-label="Breadcrumb"><a href="https://3dlook.ai/">Home</a><span aria-hidden="true">/</span><span aria-current="page">FitXpress for bariatric programs</span></nav>
  <div class="fx-bar-hero-grid">
   <div>
    <p class="fx-bar-eyebrow">Bariatric and metabolic surgery programs</p>
    <h1 id="hero-heading">Bariatric patient tracking with FitXpress: help keep body data on file at every follow-up time frame</h1>
    <p class="fx-bar-lead">Patients scan at home when a visit is hard to make, and the care team gets waist and body composition data for that time frame, which can mean fewer calls chasing measurements. FitXpress returns the record from two phone photos and can also check BMI before the first consultation.</p>
    <div class="fx-bar-actions"><a class="fx-bar-btn fx-bar-btn-white" href="#demo" data-cta="hero">Book a demo</a><a class="fx-bar-action-link" href="#record">See the follow-up record <span aria-hidden="true">↓</span></a></div>
   </div>
   <aside class="fx-bar-record" aria-label="Illustrative follow-up record">
    <div class="fx-bar-record-head"><strong>Follow-up from home.</strong><span class="fx-bar-example">Illustrative data</span></div>
    <div class="fx-bar-dates"><div><strong>7 October 2026</strong>Pre-surgery baseline</div><div><strong>20 January 2027</strong>Month 3, scanned at home</div></div>
    <dl class="fx-bar-record-list">
     <div><dt>Entered weight <span>−17.6 kg</span></dt><dd><span>119.0 kg</span><span aria-hidden="true">→</span><strong>101.4 kg</strong></dd></div>
     <div><dt>Waist measurement <span>−13.5 cm</span></dt><dd><span>131.5 cm</span><span aria-hidden="true">→</span><strong>118.0 cm</strong></dd></div>
     <div><dt>Body-fat estimate <span>−3.9 percentage points</span></dt><dd><span>46.8%</span><span aria-hidden="true">→</span><strong>42.9%</strong></dd></div>
    </dl>
    <p class="fx-bar-flag">Completed at home between clinic visits. The program files it in the patient’s record for care-team review.</p>
    <p class="fx-bar-disclosure">Illustrative values, not patient results. Weight is entered; body composition values are estimates. The program sets the follow-up schedule and which results patients and care teams see.</p>
   </aside>
  </div>
  <div class="fx-bar-strip">
   <div><b>2 photos</b><span>front and side, on the patient’s own phone</span></div>
   <div><b>Under 45 sec</b><span>from the photos to structured results</span></div>
   <div><b>From home</b><span>follow-up scans between clinic visits</span></div>
   <div><b>No integration fee</b><span>plans from $1,000 a month</span></div>
  </div>
 </div>
</section>
<section class="fx-bar-trusted" aria-label="3DLOOK clients">
  <div class="fx-bar-wrap fx-bar-trusted-inner">
    <p>100+ clients have used 3DLOOK body scanning since 2016.</p>
    {logos}
    <!-- [PLACEHOLDER] remaining client logos from design (kit: logos of all clients); alt text = client name -->
  </div>
</section>
<section class="fx-bar-section" aria-labelledby="benefits-heading">
 <div class="fx-bar-wrap">
  <p class="fx-bar-eyebrow">For patients</p>
  <h2 id="benefits-heading">Follow-up checks the patient can complete at home</h2>
  <p class="fx-bar-intro">One phone scan gives the program body data at each check.</p>
  <ul class="fx-bar-cards">
   <li><h3>Fewer trips for a measurement</h3><p>A scheduled check runs at home when the protocol does not require a visit.</p></li>
   <li><h3>Waist and body composition beside weight</h3><p>A patient app or portal can show waist change and body composition estimates next to the scale weight.</p></li>
   <li><h3>A scan without help from staff</h3><p>Real-Time Pose Validation (RTPV) gives pose and framing guidance, with voice prompts for a patient scanning alone.</p></li>
   <li><h3>Progress from their own starting point</h3><p>A patient app or portal can show change since the pre-surgery scan, when the program chooses to display it.</p></li>
  </ul>
  <p class="fx-bar-more"><a href="{HUB}">Bariatric pre-qualification and patient progress tracking, in depth <span aria-hidden="true">→</span></a></p>
 </div>
</section>
<section class="fx-bar-section fx-bar-light" id="problem" aria-labelledby="problem-heading">
 <div class="fx-bar-wrap">
  <p class="fx-bar-eyebrow">The problem</p>
  <h2 id="problem-heading">What does a bariatric program lose when follow-up depends on clinic visits?</h2>
  <p class="fx-bar-intro">Programs accredited under the US <a href="https://www.facs.org/quality-programs/accreditation-and-verification/metabolic-and-bariatric-surgery-accreditation-and-quality-improvement-program/standards/" target="_blank" rel="noopener">Metabolic and Bariatric Surgery Accreditation and Quality Improvement Program (MBSAQIP)</a> follow every patient through 30 days, 6 months and 1 year, and <a href="https://www.nice.org.uk/guidance/ng246" target="_blank" rel="noopener">UK guidance from the National Institute for Health and Care Excellence (NICE)</a> asks for two years. Each missed time frame means documented contact attempts, and a phone check-in returns a scale weight at best.</p>
  <div class="fx-bar-stats fx-bar-stats-3">
   {stat("44.6%", "of patients attended follow-up five years after surgery at one German center; long distance was the most cited reason for dropping out.", "Nutrients, patients lost to follow-up after bariatric surgery", "https://pmc.ncbi.nlm.nih.gov/articles/PMC11357598/")}
   {stat("2 attempts", "at minimum, to reach each patient who misses a time frame, each documented in the MBSAQIP registry.", "American College of Surgeons, MBSAQIP Standards", "https://www.facs.org/quality-programs/accreditation-and-verification/metabolic-and-bariatric-surgery-accreditation-and-quality-improvement-program/standards/")}
   {stat("8.1 kg", "of lean body mass is lost on average in the first 12 months after surgery, about 55% of it within 3 months.", "Obesity Reviews, lean body mass loss after bariatric surgery", "https://pmc.ncbi.nlm.nih.gov/articles/PMC9285034/")}
  </div>
  <p class="fx-bar-closing">Each patient lost to follow-up leaves a gap in the program’s outcome data, and a weight-only check cannot show lean mass loss.</p>
 </div>
</section>
<section class="fx-bar-section" id="record" aria-labelledby="record-heading">
 <div class="fx-bar-wrap">
  <p class="fx-bar-eyebrow">What the care team gets</p>
  <h2 id="record-heading">Each home scan returns a record the care team can compare with the baseline</h2>
  <div class="fx-bar-scroll"><table class="fx-bar-table fx-bar-record-table"><caption class="fx-bar-sr">Outputs FitXpress returns and what each changes for a bariatric care team</caption><thead><tr><th scope="col">Returned output</th><th scope="col">What it changes for the care team</th></tr></thead><tbody>
   <tr><th scope="row">80+ body measurements, including waist, hip and thigh</th><td>Waist change is on file at every follow-up, including those done at home.</td></tr>
   <tr><th scope="row">Body composition estimates: body-fat percentage, fat mass and lean mass</th><td>The team sees fat and lean mass estimates beside weight and decides when a dual-energy X-ray absorptiometry (DXA) or bioelectrical impedance analysis (BIA) check is needed.</td></tr>
   <tr><th scope="row">BMI and basal metabolic rate (BMR), calculated metrics; entered weight beside a Smart Scales estimate (beta)</th><td>The program keeps one BMI series from intake through follow-up and sees when entered and estimated weight disagree.</td></tr>
   <tr><th scope="row">On the FitXpress Pro plan: 3D Body Progress, comparing two scans the program selects</th><td>Patients and care teams see change in a 3D view during follow-up conversations.</td></tr>
   <tr><th scope="row">Processing status and timestamps</th><td>The program files each scan by date and orders scans for comparison.</td></tr>
  </tbody></table></div>
 </div>
 <div class="fx-bar-wrap fx-bar-progress-layout" style="margin-top:40px">
  <div class="fx-bar-progress-text">
   <p>FitXpress returns the record through its application programming interface (API), and the program links each scan identifier to the patient record.</p>
   <p class="fx-bar-feature-note"><strong>FitXpress is not a medical device.</strong> Surgical candidacy and treatment decisions remain with the clinical team.</p>
   <div class="fx-bar-actions"><a class="fx-bar-btn fx-bar-btn-blue" href="#demo" data-cta="record">See a sample record in the demo</a></div>
  </div>
  {chart_fig}
 </div>
</section>
<section class="fx-bar-section fx-bar-light" id="review" aria-labelledby="review-heading">
 <div class="fx-bar-wrap fx-bar-progress-layout">
  <div class="fx-bar-progress-text">
   <p class="fx-bar-eyebrow">Before the first consultation</p>
   <h2 id="review-heading">Check BMI before surgeon time is booked</h2>
   <p>At the first inquiry, the program compares BMI from the patient’s entered weight with BMI from the Smart Scales weight estimate (beta), both using entered height.</p>
   <p>A difference above the program’s threshold goes to a coordinator for another scan, a call or an in-clinic measurement. A completed scan becomes the pre-surgery baseline.</p>
   <div class="fx-bar-actions"><a class="fx-bar-btn fx-bar-btn-blue" href="#demo" data-cta="review">See pre-qualification in the demo</a></div>
  </div>
  {queue_fig}
 </div>
</section>
<section class="fx-bar-section" id="how-it-works" aria-labelledby="workflow-heading">
 <div class="fx-bar-wrap">
  <p class="fx-bar-eyebrow">How it works</p>
  <h2 id="workflow-heading">The scan runs inside the follow-up schedule the program already has</h2>
  <ol class="fx-bar-steps">
   <li><h3>Baseline before surgery</h3><p>At intake, the patient completes the program’s consent flow and a guided front and side capture on their phone, with no appointment.</p></li>
   <li><h3>Scans at home on the program’s schedule</h3><p>At the program’s time frames, such as 3, 6 and 12 months, the patient scans at home and the record reaches the care team.</p></li>
   <li><h3>Review in the program’s own system</h3><p>The care team reviews change against the baseline in its electronic health record (EHR) or bariatric tracking software, or in the optional FitXpress Admin Panel with comma-separated values (CSV) export.</p></li>
  </ol>
  <p class="fx-bar-intro">The recommended setup pairs the web and mobile software development kits (SDKs) for capture with the API for results (<a href="https://docs.fitxpress.3dlook.me/" target="_blank" rel="noopener">FitXpress API documentation</a>). The program designs consent and results screens; the capture layer stays fixed to protect measurement quality.</p>
 </div>
</section>
<section class="fx-bar-section fx-bar-light" aria-labelledby="compare-heading">
 <div class="fx-bar-wrap">
  <p class="fx-bar-eyebrow">Compare approaches</p>
  <h2 id="compare-heading">FitXpress compared with a home scale, clinic measurement and BIA or DXA</h2>
  {{COMPARE}}
  <p class="fx-bar-closing">For patients who live far from the center, a home scan can keep waist and body composition on file at time frames they would otherwise miss. In-clinic measurement, calibrated scales, BIA and DXA stay wherever the protocol requires them.</p>
  <div class="fx-bar-actions"><a class="fx-bar-btn fx-bar-btn-blue" href="#demo" data-cta="compare">See a follow-up comparison in the demo</a></div>
 </div>
</section>
<section class="fx-bar-section fx-bar-navy" aria-labelledby="proof-heading">
 <div class="fx-bar-wrap">
  <p class="fx-bar-eyebrow">Accuracy and data handling</p>
  <h2 id="proof-heading">How accurate is FitXpress for follow-up, and how is patient data handled?</h2>
  <p class="fx-bar-intro">For follow-up, repeatability matters most, because the care team compares each patient with their own baseline.</p>
  <div class="fx-bar-figs">
   <div><b>&lt; 1 cm</b><span>typical scan-to-scan difference for most evaluated body measurements</span></div>
   <div><b>96-97%</b><span>accuracy against expert manual measurement, typical absolute error 1.5-2.0 cm</span></div>
  </div>
  <p class="fx-bar-proof-note">Both figures come from internal validation of body measurements (38-210 kg, 150-220 cm), have not been peer-reviewed, and do not cover body composition estimates or performance after bariatric surgery. The methodology is available under a non-disclosure agreement (NDA).</p>
  <p class="fx-bar-more"><a href="https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/">Body scanning accuracy: an enterprise framework <span aria-hidden="true">→</span></a></p>
  <ul class="fx-bar-data">
   <li><strong>Photos</strong><span>FitXpress deletes photos immediately after processing or retains them for up to 30 days under a customer-specific policy. Retained photos are blurred, and face obfuscation is applied during capture.</span></li>
   <li><strong>Identifiers</strong><span>Scan records use randomly generated identifiers, and the program links them to its patient records.</span></li>
   <li><strong>HIPAA</strong><span>FitXpress can support HIPAA-governed deployments where 3DLOOK acts as a business associate under an executed Business Associate Agreement (BAA).</span></li>
   <li><strong>GDPR</strong><span>In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR.</span></li>
   <li><strong>Encryption</strong><span>Data is encrypted in transit and at rest.</span></li>
   <li><strong>Model training</strong><span>3DLOOK does not use production customer data to train its models without the customer’s explicit, documented authorization.</span></li>
  </ul>
  <p class="fx-bar-more">The <a href="https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/">FitXpress data, privacy, security and regulatory FAQ</a> covers hosting, deletion, System and Organization Controls 2 (SOC 2) and U.S. Food and Drug Administration (FDA) information. Privacy contact: <a href="mailto:privacy@3dlook.me">privacy@3dlook.me</a>.</p>
 </div>
</section>
<section class="fx-bar-section" id="pricing" aria-labelledby="pilot-heading">
 <div class="fx-bar-wrap fx-bar-pilot">
  <div>
   <p class="fx-bar-eyebrow">Pilot and pricing</p>
   <h2 id="pilot-heading">Start with one follow-up cohort, then scale on a monthly plan</h2>
   <p class="fx-bar-intro">The pilot starts with one clinic and one post-surgery cohort; pre-qualification can join later. FitXpress uses production infrastructure already deployed in remote BMI-verification and weight-management workflows.</p>
   <div class="fx-bar-price">
    <p><b>Starter.</b> $1,000 a month for up to 500 API requests.</p>
    <p><b>Pro.</b> $1,500 a month for up to 1,000 API requests, adding 3D Body Progress tracking and 3D Goal Visualization.</p>
    <p>Both include guided implementation support, with no integration fee. Custom plans cover higher volumes.</p>
    <p class="fx-bar-more"><a href="https://3dlook.ai/pricing/">FitXpress plans and pricing <span aria-hidden="true">→</span></a></p>
   </div>
  </div>
  <div>
   <ol class="fx-bar-steps-v">
    <li><h3>Walk through the pathway</h3><p>The demo shows guided capture, a follow-up comparison and integration options.</p></li>
    <li><h3>Pilot against a comparison cohort</h3><p>One cohort scans at home. A comparable cohort keeps the usual follow-up schedule; where practical, patients are assigned randomly.</p></li>
    <li><h3>Evaluate and roll out</h3><p>Results are measured against criteria agreed before the pilot, and the scan goes live only if they are met.</p></li>
   </ol>
   <h3>What the program and 3DLOOK track</h3>
   <ul class="fx-bar-out"><li>Scan completion and retake rates</li><li>Follow-up time frames completed with body data, against the comparison cohort</li><li>Contact attempts per patient who misses a time frame</li></ul>
   <div class="fx-bar-actions"><a class="fx-bar-btn fx-bar-btn-blue" href="#demo" data-cta="pilot">Discuss a pilot</a></div>
  </div>
 </div>
</section>
<section class="fx-bar-section fx-bar-light" id="faq" aria-labelledby="faq-heading">
 <div class="fx-bar-wrap"><p class="fx-bar-eyebrow">Frequently asked questions</p><h2 id="faq-heading">Questions bariatric teams ask</h2><div class="fx-bar-faq">{faq_html}
 </div></div>
</section>
<section class="fx-bar-section fx-bar-navy" id="demo" aria-labelledby="demo-heading">
 <div class="fx-bar-wrap fx-bar-cta">
  <div>
   <p class="fx-bar-eyebrow">Book a demo</p>
   <h2 id="demo-heading">See bariatric patient tracking in the program’s own pathway</h2>
   <ul class="fx-bar-demo-list"><li>Guided front and side capture on a phone</li><li>A follow-up comparison against the pre-surgery baseline</li><li>A sample record and pilot options</li></ul>
   <p class="fx-bar-more"><a href="{HUB}">Bariatric pre-qualification and patient progress tracking <span aria-hidden="true">→</span></a></p>
   <p class="fx-bar-related">Other FitXpress uses: <a href="https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/">remote patient monitoring for weight loss</a> · <a href="https://3dlook.ai/for-bmi-verification/">BMI verification</a></p>
  </div>
  {{FORM}}
 </div>
</section>
</main>"""

# comparison table + mobile cards
cols = ["FitXpress", "Weight from a home scale", "Measurement at a clinic visit", "Clinic BIA or DXA"]
rows = [
    ("Trip to the clinic", ["None", "None", "Required", "Required"]),
    ("What it records", ["80+ body measurements, body composition estimates, BMI and timestamps",
                         "Weight as reported", "Staff-entered measurements set by the program’s protocol",
                         "Body composition values; DXA also measures bone"]),
    ("Waist and body composition between visits", ["At each home check", "Not recorded", "Only at a visit",
                                                   "Only at a visit"]),
    ("Who enters the data", ["Returned from the scan", "The patient", "Clinic staff", "The clinic device"]),
]
table = ('<div class="fx-bar-scroll fx-bar-comparison-table"><table class="fx-bar-table"><caption class="fx-bar-sr">'
         'FitXpress compared with other ways a bariatric program collects body data</caption><thead><tr><th scope="col">Dimension</th>'
         + "".join(f'<th scope="col">{c}</th>' for c in cols) + "</tr></thead><tbody>"
         + "".join(f'<tr><th scope="row">{r}</th>' + "".join(f"<td>{v}</td>" for v in vals) + "</tr>" for r, vals in rows)
         + "</tbody></table></div>")
cards = '<div class="fx-bar-comparison-cards">' + "".join(
    f'<article class="fx-bar-comparison-card{" fx-bar-featured" if i == 0 else ""}"><h3>{c}</h3><dl>'
    + "".join(f"<dt>{r}</dt><dd>{vals[i]}</dd>" for r, vals in rows) + "</dl></article>"
    for i, c in enumerate(cols)) + "</div>"
body = body.replace("{COMPARE}", table + "\n  " + cards)

form = re.search(r'<div class="fx-bar-form">.*?</div>\s*</div>\s*</section>', src, re.S).group(0)
form = form[: form.rfind("</div>")].rstrip()
form = form.replace("program requirements", "follow-up requirements")
body = body.replace("{FORM}", form)

def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s)

ld = {"@context": "https://schema.org", "@graph": [
    {"@type": "WebPage", "@id": URL + "#webpage", "url": URL, "name": TITLE, "description": DESC, "inLanguage": "en",
     "isPartOf": {"@id": "https://3dlook.ai/#website"}, "about": {"@id": URL + "#service"},
     "mainEntity": {"@id": URL + "#service"}, "hasPart": {"@id": URL + "#faq"}, "breadcrumb": {"@id": URL + "#breadcrumb"}},
    {"@type": "Service", "@id": URL + "#service", "name": "FitXpress for bariatric patient tracking", "url": URL,
     "provider": {"@id": "https://3dlook.ai/#organization"}, "brand": {"@type": "Brand", "name": "FitXpress"},
     "serviceType": "Remote body scanning for bariatric follow-up and pre-qualification",
     "description": "FitXpress turns two guided smartphone photos into 80+ body measurements, body composition estimates, BMI and timestamps, returned through an API for bariatric follow-up between clinic visits and BMI review before the first consultation.",
     "audience": {"@type": "BusinessAudience", "audienceType": "Bariatric surgery centers, hospital bariatric programs, surgical networks, and metabolic and obesity clinics"},
     "areaServed": [{"@type": "Country", "name": "United States"}, {"@type": "Country", "name": "United Kingdom"}],
     "serviceOutput": [{"@type": "Thing", "name": n} for n in ["80+ body measurements", "Body composition estimates", "BMI and BMR (calculated metrics)", "3D Body Progress (Pro plan)", "Processing status and timestamps"]]},
    {"@type": "Organization", "@id": "https://3dlook.ai/#organization", "name": "3DLOOK", "url": "https://3dlook.ai/"},
    {"@type": "FAQPage", "@id": URL + "#faq", "url": URL, "name": "Questions bariatric teams ask",
     "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a.format(docs="FitXpress API documentation"))}} for q, a in FAQ]},
    {"@type": "BreadcrumbList", "@id": URL + "#breadcrumb", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://3dlook.ai/"},
        {"@type": "ListItem", "position": 2, "name": "FitXpress for bariatric programs", "item": URL}]}]}

comment = """<!--
  FitXpress bariatric landing page · v2 · 2026-10-16 · /fitxpress/for-bariatric-programs/
  Remove data-prototype-chrome header/footer when the WordPress theme supplies them.
  Swap formConfig.formId for the shared "FX | LP | Demo" form during integration.
-->"""

head_start = src[: src.index("<style>")]
head_start = re.sub(r"<title>.*?</title>", f"<title>{TITLE}</title>", head_start, flags=re.S)
head_start = re.sub(r'(<meta name="description" content=")[^"]*', r"\g<1>" + DESC, head_start)
head_start = re.sub(r'(<meta property="og:description" content=")[^"]*', r"\g<1>" + DESC, head_start)
head_start = re.sub(r'(<meta property="og:title" content=")[^"]*', r"\g<1>" + TITLE, head_start)
head_start = re.sub(r"<!--.*?-->", comment, head_start, count=1, flags=re.S)

chrome_head = re.search(r'<body.*?</header>', src, re.S).group(0)
chrome_foot = re.search(r'<footer.*?</footer>\s*</div>', src, re.S).group(0)
out = (head_start + css + "\n</head>\n" + chrome_head + "\n" + body + "\n" + chrome_foot + "\n"
       + '<script type="application/ld+json">\n' + json.dumps(ld, ensure_ascii=False, indent=1) + "\n</script>\n"
       + script + "\n</body>\n</html>\n")
assert "{" not in re.sub(r"<(script|style)[^>]*>.*?</\1>", "", out, flags=re.S).replace("{{", ""), "unfilled template"
open(sys.argv[2], "w", encoding="utf-8").write(out)
print("written", sys.argv[2], len(out))
