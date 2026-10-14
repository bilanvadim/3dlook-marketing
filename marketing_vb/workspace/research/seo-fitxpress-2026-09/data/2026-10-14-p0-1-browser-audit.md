> Evidence for `../2026-10-14-p0-1-ticket-v2.md`. Raw downloads, screenshots and helper scripts stayed in the session scratchpad and are not in the repo.

# Browser audit: 3dlook.ai /pricing/ and /contact-us/ (2026-10-14)

Tooling: Playwright MCP, Chromium 154 (headless). Every scenario ran in its own fresh browser context (clean cookies, storage and cache). Listeners captured `console` (error and warning), `pageerror` with stack, `requestfailed` and HTTP >= 400.
- Desktop: 1366x900, Windows Chrome 141 UA.
- Mobile: 390x844, DPR 3, isMobile + hasTouch, iPhone iOS 18.6 Safari UA. **The engine is still Chromium.** Safari-specific behaviour (WebKit error wording, ITP) could NOT be reproduced, because no WebKit build is installed.
- Geo/IP: the VPS. WebToffee config showed `_lawSelected: ["GDPR","CCPA"]` (pricing, P1). The banner showed up with GDPR-style default denial.
- Nothing was submitted. No meeting was booked. I typed into form fields only. I opened the chat widget once without sending anything. I clicked "Accept All" on the cookie banner in one context, which the task allowed.
- Request volume was normal sequential browsing: about 60 page loads over about 40 minutes, no parallel bursts.

Labels: **[VERIFIED]** means I reproduced or observed it in the browser. **[INFERRED]** means reasoning from code or data that I did not reproduce.

---

## 0. Key mechanism: the delayed JS is "Flying Scripts", not WP Rocket "Delay JS"

[VERIFIED] No script uses `type="rocketlazyloadscript"` or `data-rocket-src`, so WP Rocket's delay-JS is not active. Delaying is done by an inline script `<script id="flying-scripts">` (the Flying Scripts plugin):

```js
const loadScriptsTimer=setTimeout(loadScripts,10*1000);
const userInteractionEvents=['click','mousemove','keydown','touchstart','touchmove','wheel'];
...
function loadScripts(){document.querySelectorAll("script[data-type='lazy']").forEach(function(elem){elem.setAttribute("src",elem.getAttribute("data-src"))})}
```

Delayed scripts carry `data-type="lazy" data-src=…` and are released on first interaction or after 10 s.

/pricing/:
1. `#webtoffee-cookie-consent-js-extra`: `data:text/javascript;base64,…` (≈60 KB decoded). It contains `var _wccConfig = {…}`, `_wccStyles` and `_wccGCMConfig`, all three configs in this one script.
2. `#webtoffee-cookie-consent-js`: `/wp-content/plugins/webtoffee-cookie-consent/lite/frontend/js/script.min.js?ver=3.5.5`, the consumer of `_wccConfig`.
3. `#webtoffee-cookie-consent-gcm-js`: `/…/lite/frontend/js/gcm.min.js?ver=3.5.5`, the consumer of `_wccGCMConfig`.
4. `#hs-script-loader`: `/wp-content/cache/min/1/6014382.js` (HubSpot tracking loader, WP Rocket-minified copy).
5. 4 × `data:` scripts with `hbspt.forms.create({region:"na1",portalId:"6014382",formId:…})` for forms 0a22d79d…, 38880e8c…, aa061d33…, a48a1930….

/contact-us/ has the same three WebToffee scripts, `hs-script-loader` and 1 × `hbspt.forms.create` for form `f227f5ce-8ce1-473d-a4f8-597c832979cc`.

Not delayed: jQuery 3.6.0 (`/wp-content/cache/min/1/ajax/libs/jquery/3.6.0/jquery.min.js`, sync in head), remodal.min.js, slick, swiper, main.js, `//js.hsforms.net/forms/embed/v2.js` (parser-inserted, 4 tags on /pricing/ that the browser dedupes to 1 request), GTM, Clarity, Hotjar, OptinMonster, FB pixel, Apollo, Ahrefs, HubSpot banner/analytics/chat loaders.

Plugin and version: **WebToffee Cookie Consent (lite) 3.5.5** (`webtoffee-cookie-consent`), not CookieYes.

## 1. Console errors: exact texts, sources, triggers

### 1a. `_wccConfig._lawSelected` / `_regions`: REPRODUCED [VERIFIED]

Exact Chromium texts, as `pageerror`, uncaught:

```
TypeError: Cannot read properties of undefined (reading '_lawSelected')
    at https://3dlook.ai/wp-content/plugins/webtoffee-cookie-consent/lite/frontend/js/script.min.js?ver=3.5.5:1:108
TypeError: Cannot read properties of undefined (reading '_regions')
    at https://3dlook.ai/wp-content/plugins/webtoffee-cookie-consent/lite/frontend/js/gcm.min.js?ver=3.5.5:1:96
```

Source code at those positions (downloaded copies are in `browser-dl/`):
- script.min.js: `!function(){const _wccStore=window._wccConfig,_wccStyle=window._wccStyles;let currentLaw=window._wccConfig._lawSelected[0],…`
- gcm.min.js: `!function(){const data=window._wccGCMConfig;…const regionSettings=data._regions||[],…`

These match Clarity's `(reading '_lawselected')` / `(reading '_regions')` and Safari's `evaluating 'window._wccConfig._lawSelected'` / `evaluating 'data._regions'` word for word. Both always fire together, which fits 177/177 and 46/46.

**Root cause [VERIFIED by reproduction; mechanism per HTML spec]:**
- Flying Scripts sets `src` on all lazy `<script>` elements in one loop.
- A parser-created script that gets its `src` later executes as an *async* script ("force-async"), so execution order is whatever finishes loading first, not DOM order.
- The config arrives as a `data:` URI and the consumers as network URLs. When the consumers come from the HTTP cache, they can run before the config. `_wccConfig` and `_wccGCMConfig` are then undefined and both IIFEs throw on their first line.
- `_wccConfig` exists a moment later, which I checked after each error.

**Trigger matrix (desktop and mobile, Chromium):**

| Scenario | Result |
|---|---|
| Cold cache, no interaction, 10 s timer fires (desktop pricing) | 0 errors (1 run) |
| Cold cache, first interaction ~1.5 s after DOMContentLoaded (desktop pricing) | 0/2 |
| Warm cache, 10 s timer only (desktop pricing) | 0/4 |
| Warm cache, interaction 0.4–1.5 s after load (desktop pricing, reload) | **10/10 runs errored** (mousemove) |
| Warm cache, interaction at 2.5 s / 3.5 s / ~6 s after load | 0/4 |
| **Realistic flow:** home (cold, no error) → click to /pricing/ → mouse move at 0.7 s | **errored** |
| Same flow → /contact-us/ | **errored** |
| Mobile emulation, warm, first tap at 0.8 s after DOMContentLoaded (pricing) | **3/3 errored** |
| Mobile emulation, warm, timer only | 0/1 |
| After "Accept All" (wt_consent consent:yes) + warm + early interaction | **errored**, so consent state does not matter |

So the condition is: **cached WebToffee JS (any 2nd+ pageview) plus a first interaction within about 2 s of page load.** /pricing/ and /contact-us/ are typically reached from another page, which explains their high error share. That last point is [INFERRED] from the trigger condition.

**Impact [VERIFIED]:** on an errored pageview the consent banner never renders. In the home → pricing flow without prior consent, the banner showed on home but `.wcc-consent-container` did not exist on /pricing/ and /contact-us/. The "revisit consent" button also never renders. HubSpot forms are NOT affected: all 4 /pricing/ forms rendered in errored runs. GCM defaults: `_isGTMTemplate: "1"`, so the GTM template handles consent mode anyway [INFERRED].

**Fix direction [INFERRED]:** exclude the three WebToffee scripts from Flying Scripts, or at least keep the config inline and non-delayed so it always exists before the consumers. Script screenshot: `shot-desktop-pricing-after-wcc-error.png`.

### 1b. `JSON Parse error: Unexpected identifier "object"`: source identified, not reproduced in Chromium

[VERIFIED] I hooked `EventTarget.prototype.addEventListener` on /pricing/. Exactly **one** top-window `message` listener calls `JSON.parse(event.data)`. It is a **GTM Custom HTML tag** in GTM-PW77M7K (stack: `gtm.js?id=GTM-PW77M7K:969`), the HubSpot chat → dataLayer "Hubspot Widget" tracker:

```js
window.addEventListener("message",function(a){if("https://app.hubspot.com"!==a.origin)return!1;a=JSON.parse(a.data);switch(a.type){case "closed-welcome-message":…case "open-change":…case "external-api-event":…}b&&dataLayer.push({event:"Hubspot Widget",…})});
```

It has no `typeof a.data === "string"` guard and no try/catch.

The other `message` listeners do not parse: 2 more GTM tags (`hsFormCallback` UTM filler and form-submit tracker), fbevents, hsadspixel, conversations-embed (bound native function) and hsforms v2.

[VERIFIED] In Chromium, every message from `https://app.hubspot.com` (chat iframe `#hubspot-conversations-iframe`, `app.hubspot.com/conversations-visitor/6014382/…`) was a JSON **string**, both on load and when opening the chat. A `JSON.parse` wrapper recorded 0 failures on /pricing/ and /contact-us/, desktop and mobile.

[INFERRED] In Safari, some app.hubspot.com message must arrive as an **object**, so `JSON.parse(obj)` turns into `"[object Object]"`. That is exactly the Safari text `JSON Parse error: Unexpected identifier "object"`, and it is Safari-only in her export. Likely candidates are the chat iframe's storage-access or ITP handshake, or another app.hubspot.com frame. Untested, since there is no WebKit here.

**Fix:** guard the tag, for example `if(typeof a.data!=="string")return; try{a=JSON.parse(a.data)}catch(e){return}`.

### 1c. Other errors and warnings seen

- [VERIFIED] `Uncaught (in promise) TypeError: Cannot read properties of null (reading 'sequence')` at `https://scripts.clarity.ms/0.8.72-beta/clarity.js:1:49742`. Clarity's own beta build threw it once on desktop /pricing/ while I was opening and closing the remodals. It did not recur in other runs. Low priority. I don't know whether Clarity reports its own rejections.
- [VERIFIED] Warnings, not errors: `The resource …/main-hero-desktop.webp (mobile: main-hero-mobile.webp) was preloaded using link preload but not used within a few seconds…` repeats on both pages. `[quick-fetch] quickFetchScript was not included…` comes from HubSpot `visitor.js`. Neither is a JS error.
- [VERIFIED] Failed requests (benign): `https://www.google.com/ccm/collect?...tid=AW-842555409…` net::ERR_ABORTED on every load. `https://api.omappapi.com/v2/embed/386537/cvrmwb352ycz06yxtvpa?device=desktop` net::ERR_ABORTED: the OptinMonster embed is requested twice per load because `api.min.js` is included by 2–4 script tags (#22 `data-campaign`, #27 `omapi-script`, plus 2 inline injectors). `region1.analytics.google.com/measurement/conversion…` ERR_ABORTED on CTA clicks.
- [VERIFIED] Off-site: the Mobile Tailor "Sign up for a trial" / "Start a Trial" buttons go to `https://mtm.3dlook.me/accounts/signup`. That page renders a sign-up form but returns **HTTP 404** for the document. It also throws `TypeError: Promise.allSettled is not a function` at `gtag/js?id=AW-842555409:587` because something on mtm overrides `Promise`, plus a RudderStack-deprecated console.error. This is outside the two pages, but it means the Google Ads conversion tag on the signup page is broken. Screenshot: `shot-desktop-mtm-signup.png`.
- No errors from Hotjar, OptinMonster, Clearout, the HubSpot forms embed or jQuery in any state.

## 2. Inventory

- **jQuery [VERIFIED]:** two copies.
  - Global `jQuery`/`$` = **3.6.0** (WP Rocket local copy, sync, head).
  - **3.7.0** from `ajax.googleapis.com` is injected by the **Clearout widget** (`clearout_js_widget.js:0:33797`, per CDP initiator). Clearout itself is injected by a GTM Custom HTML tag. Clearout keeps it private as `window.clearout.$` (3.7.0), and the global stays 3.6.0.
  - No conflicts and no jQuery errors were observed.
- **Cookie consent:** WebToffee Cookie Consent lite 3.5.5. Config (`_wccConfig`, `_wccStyles`, `_wccGCMConfig`) is in a single delayed `data:` script placed *before* its two delayed consumers in the DOM. DOM order is irrelevant because they execute async (see 1a). `_wccGCMConfig`: `{"_mode":"advanced","_regions":[],"wait_for_update":"500","_isGTMTemplate":"1",…}`. GDPR and CCPA banner templates are both inlined (`#wccBannerTemplate_GDPR`, `#wccBannerTemplate_CCPA`).
- **HubSpot forms:** v2 embed `//js.hsforms.net/forms/embed/v2.js`, not delayed. Forms are created by inline `hbspt.forms.create` calls that are **delayed by Flying Scripts**, not created on popup open. On /pricing/, all 4 forms are pre-rendered inside the hidden remodals as soon as Flying Scripts fires. Forms render in-page (`form.hs-form-private`), not in an iframe.
- Portal 6014382:
  - /pricing/: `#modal-pricing-contact` → form `0a22d79d-8ad2-4672-bfa0-df212dedf624` (title "Maximize Mobile Tailor Benefits with Premium Features"; fields firstname, lastname, email, company, type_of_business, message, consent).
  - /pricing/: `#bd-modal-starter` → `38880e8c-a0b0-4f2e-ba03-bf226e949612`, `#bd-modal-pro` → `aa061d33-717c-4fbf-b5ef-3285a14b10b3`, `#bd-modal-personalized` → `a48a1930-6b6f-432e-9ab9-040122b42d90`. All three titled "Shape the Future of Health and Fitness Tech", with fields firstname, lastname, company, email, jobtitle, website, consent and submit "Let's talk".
  - /contact-us/: `f227f5ce-8ce1-473d-a4f8-597c832979cc` in `.c-hero__form.dark-form`. Fields: firstname, lastname, jobtitle, email, website, `0-2/type_of_business` (select), message, consent checkbox, submit "Let's talk".
  - **No HubSpot Meetings iframe** on either page before submission. I did not submit, so I can't tell whether a meetings step follows.
- Other: HubSpot chat (conversations-embed), HubSpot cookie-banner script `js.hs-banner.com/v2/6014382/banner.js` (loaded alongside WebToffee, so two consent systems are present [VERIFIED presence]), collected-forms, Clarity (`clarity.ms/tag/ptrtdxgprb?ref=gtm` → `0.8.72-beta/clarity.js`), Hotjar 1082457, GA4 G-NXNB16WGX6, Google Ads AW-842555409 (gtag loaded twice), FB pixel, Apollo tracker, Ahrefs analytics, OptinMonster campaign `cvrmwb352ycz06yxtvpa`.

## 3. /pricing/ CTAs [VERIFIED]

Before any interaction, `elementFromPoint` returned the CTA itself for every CTA below, with one exception: on desktop with the consent banner open, the Pro/Personalized buttons in the first viewport (y≈740–790) sit under the banner (see dead clicks).

| Tab | Text | Selector | href / data-event-name | Result | Timing |
|---|---|---|---|---|---|
| FitXpress | Book a demo (Starter) | `.request-hero-yourfit .pricing__item.favourite a.button` | `#bd-modal-starter` / "Starter plan click" | remodal opens, HubSpot form 38880e8c visible | modal + form 165 ms |
| FitXpress | Book a demo (Pro) | `.request-hero-yourfit .pricing__item a.button[href="#bd-modal-pro"]` | `#bd-modal-pro` / "Pro plan click" | remodal + form aa061d33 | 117 ms |
| FitXpress | Talk to sales (Personalized) | `…[href="#bd-modal-personalized"]` | / "Personalized plan click" | remodal + form a48a1930 | 191 ms (Clarity `sequence` rejection appeared here once) |
| Mobile Tailor | Sign up for a trial (Basic) | `.request-hero-tailor … a.button[data-event-name="Basic plan click"]` | `https://mtm.3dlook.me/accounts/signup` | same-tab navigation, page loads in ~3.0 s, **HTTP 404 status** on the signup document | — |
| Mobile Tailor | Start a Trial (Premium) | `…[data-event-name="Premium plan click"]` | same signup URL | same as above | ~2.7 s |
| Mobile Tailor | Start a Trial (Enterprise) | `…[data-event-name="Enterprise plan click"]` | `#modal-pricing-contact` | remodal + form 0a22d79d. **The label says "Start a Trial" but it opens a contact form.** | 138 ms |

- Mobile first-interaction case: the first tap of the session lands on "Book a demo" before Flying Scripts has fired. The modal opens at ~330 ms and the HubSpot form appears at **~630–655 ms**, because the form is created by that tap. Same result cold and warm. On desktop, prior mouse movement normally pre-creates the forms.
- Esc closes remodals. Opening a modal sets the URL to `/pricing/#` (remodal hash handling).
- Product switch: `button.switch-btn` "FitXpress" / "Mobile Tailor" works. It swaps the two full hero sections: `.request-hero-yourfit` (opacity 1, z 1, relative) ↔ `.request-hero-tailor` (opacity 0, **z-index -1**, absolute). Both sections duplicate the whole pricing block (duplicate `id="pricing_plan"`).
- **The hidden (opacity 0) hero does NOT intercept clicks**, on desktop or mobile, because z-index -1 puts it underneath. I checked with an `elementFromPoint` grid over the hero and on every CTA, switch and label.
- Monthly/Annual (`label.l-monthly`, `label.l-annual`, `span.switch`, delegated handler `.pricing-switcher .fieldset`) works: prices change between monthly and yearly.

### Dead-click candidates on /pricing/ [VERIFIED: 0 DOM mutations, no navigation, no scroll after click]

1. Plan name pills `h3.title` "Starter" / "Pro" / "Personalized" (`.pricing__item h3.title`). They are pill-shaped with a background, look like buttons and do nothing.
2. "Recommended" band `div.favourite-label` above Starter: blue full-width bar, no action.
3. "save up to 20%" pill `p.pricing-switcher__text.box.box-1`: glowing-border pill next to the toggle, no action.
4. Price block `.pricing__part.part-top` ("$1 000 / month") and feature rows `.pricing__item li.item.checked`: no action.
5. Client-logo marquee `.swiper-slide img`: no links.
6. Active "FitXpress" `button.switch-btn.active`: clicking the already-active tab causes no visible change. It does produce ~100 DOM mutations, so Clarity may or may not count it as dead [INFERRED]. It is blue and button-like, which matches the UX note.
7. Header `a.main-item-link[href="#"]` "Use Cases", "Made-to-Measure", "Resources", "About 3DLOOK".
   - Desktop: the dropdown opens on hover. Clicking the parent does nothing: URL and scroll unchanged, default prevented.
   - Mobile menu: submenus are already expanded, and tapping the parent only appends `#` to the URL.
8. Cookie banner covering CTAs on desktop. At 1366×900, the WebToffee banner (fixed bottom, 117 px, z 9999999) covers the y≈783–900 band where the first-viewport "Book a demo" (Pro) and "Talk to sales" sit. At the button centres, `elementFromPoint` returned the banner's `<p>` text and `button.wcc-btn-customize`. My first automated click hit "Customize" instead of the CTA.
9. **HubSpot chat iframe covers "Accept All" on desktop.** `#hubspot-messages-iframe-container` (z 2147483647) expands to 268×245 at bottom-right to show the welcome bubble ("Hey 🙌 We're here to help"). That box covers the whole Accept All button (1219,837,122×44): `elementFromPoint` at 4 points across the button returned `IFRAME#hubspot-conversations-iframe`. A real mouse click on Accept All did **not** record consent (wt_consent unchanged) and the banner stayed. Reproduced on /contact-us/ and visible on /pricing/. Screenshots: `shot-desktop-contact-banner-vs-chat.png`, `shot-desktop-pricing-chat-area.png`.
   - Clarity cannot see clicks inside the cross-origin iframe, so this may show up as rage or dead clicks around the banner rather than in iframe stats [INFERRED].

Mobile [VERIFIED]:
- The consent banner is 273 px (32% of an 844 px viewport) with z 9999999. That is **above the remodal** (z 10000), so it covers the lower fields and submit button of the "Book a demo" modal form until the user acts on the banner (`shot-mobile-modal-starter-cold.png`).
- Monthly/Annual labels are 58×16 and 50×16 px, small tap targets.

## 4. /contact-us/

- Desktop, cold:
  - Before the first interaction, **no form exists** (`.c-hero__form` is an empty placeholder) for up to 10 s, because the Flying Scripts timer delays the form.
  - First mousemove → form f227f5ce rendered in **27 ms**, since v2.js is already loaded.
  - The form starts at y≈1291 px, below the first screen. The first screen shows two benefit cards with check-list items that look like cards but are not links (dead-click candidates [INFERRED from the screenshot; I did not click-test those cards]).
- Mobile, cold:
  - No form before interaction (placeholder at y=1958, 150 px).
  - First tap → form visible in **417 ms**. The form starts at y≈2068 px of a 4942 px page.
  - With the banner open, the submit button (top≈576 px when the form is scrolled into view) sits under the 273 px consent banner (`elementFromPoint` → `P.wcc-title`).
  - All other fields received taps.
- Typing (no submit), desktop and mobile:
  - I typed into firstname, lastname, jobtitle, email ("abc") and message, and website got "example.org".
  - HubSpot showed inline "Email must be formatted correctly." There were **0 console errors**, and the JSON.parse wrapper recorded 0 failures.
- **Clearout:**
  - The widget is initialized via GTM Custom HTML (`mode:"ajax"`, `safe_to_send_only:true`, `timeout:3`, public `app_token` in page source). `window.clearout` exposes `name, version, emailValidator, push, $`.
  - It made **no network calls and threw no errors** while typing or blurring an invalid email. It probably validates on submit, which I did not test.
- The wcc errors reproduce on /contact-us/ under the same warm + early-interaction condition (section 1a).
- Desktop vs mobile:
  - The same errors appear on both, with the same trigger.
  - Mobile differences are layout only: banner height 273 vs 117 px, and the banner covers the submit button and modal fields.
  - The chat-over-Accept-All overlap was observed on desktop. On mobile, the banner itself is the main obstruction.
  - I found nothing desktop-only that would explain "42% on desktop" beyond the trigger condition: desktop users fire `mousemove` almost immediately, so they hit the <2 s window more often than mobile users, whose first touch comes later [INFERRED].

## 5. The ticket's guessed causes

| Guess | Verdict |
|---|---|
| WP Rocket "Delay JavaScript execution" delays HubSpot / popup scripts | **Partly supported, wrong plugin.** Delaying is done by **Flying Scripts**, not WP Rocket delay-JS (no rocketlazyloadscript on the page). The delay does cause the top JS errors, via the WebToffee config race. It also delays HubSpot form creation: no form on /contact-us/ until interaction or 10 s, and +~0.6 s on a first-tap modal on mobile. It does **not** break HubSpot. [VERIFIED] |
| Elementor popups | **Not supported.** The CTAs open **remodal** popups (`[data-remodal-id]`, `remodal.min.js`). [VERIFIED] |
| HubSpot embed failing inside popups | **Not supported.** All 4 forms render inside the modals in 117–191 ms (desktop) and ≤655 ms (mobile first tap), with no errors. [VERIFIED] |
| Multiple jQuery versions | **Present but harmless as far as observed.** Global 3.6.0 plus Clearout's private 3.7.0 (`clearout.$`), with no jQuery errors. [VERIFIED] |
| Mobile-only issue on /pricing/ | **Not supported as mobile-only.** The same errors reproduce on desktop and in mobile emulation. The mobile-specific problems are the banner covering 32% of the screen and sitting above the modal form. [VERIFIED in Chromium; real iOS Safari untested] |
| Desktop-only issue on /contact-us/ | **Not supported as desktop-only.** The mechanism is the same on both. The desktop-specific problem is the chat iframe blocking "Accept All". [VERIFIED] |
| Third-party scripts | **Supported for the JSON.parse error** (GTM Custom HTML HubSpot-chat tracker; Safari trigger untested) and Clarity's own `sequence` rejection. The top 4 messages come from the WebToffee plugin plus Flying Scripts, which is first-party WP config. [VERIFIED source; Safari trigger INFERRED] |

## Files
- Screenshots in this folder: `shot-desktop-*.png`, `shot-mobile-*.png`.
- Downloaded scripts: `browser-dl/script.min.js`, `browser-dl/gcm.min.js` (WebToffee 3.5.5), `browser-dl/gtm-PW77M7K.js` (GTM container v226).
