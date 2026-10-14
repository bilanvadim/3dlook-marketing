> Evidence for `../2026-10-14-p0-1-ticket-v2.md`. Raw downloads, screenshots and helper scripts stayed in the session scratchpad and are not in the repo.

# Static audit: /pricing/ and /contact-us/ (curl-only), 2026-10-14

Scope: read-only static analysis; no browser. 13 sequential requests to 3dlook.ai (≥2 s apart, all 200 except one 301);
third-party files fetched from their own hosts.

Files (all under `scratchpad/clarity-p0/static/`):
- `pricing-desktop.html`, `pricing-mobile.html`, `contact-desktop.html`, `contact-mobile.html`, `home-desktop.html` (+ `.headers`)
- `scripts-*.txt`: every `<script>` tag with line number and attributes (from `tools/scripts.py`)
- `lazy-*/`: base64 `data:` scripts decoded from the delayed tags (from `tools/lazy.py`)
- `js/`: first-party JS (`wcc-script.min.js`, `wcc-gcm.min.js`, `theme-main.js`, `remodal.min.js`, `hs-6014382.js`, `jquery-cached.min.js`)
- `ext/`: `gtm-PW77M7K.js`, `hsforms-v2.js`, `hs-conversations-embed.js`, `clearout_js_widget.js`, `omappapi-api.min.js`, `hs-banner.js`, `hs-collectedforms.js`, `apollo-tracker.iife.js`, `ahrefs-analytics.js`, `hsform-f227f5ce.json`
- `gtm-parsed/resource.json`, `gtm-parsed/html-tag-*.html`, `gtm-summary.txt`: the GTM container decoded (from `tools/gtm.py`, `tools/gtm_rules.py`)

Legend: **[V]** = verified in the downloaded files. **[I]** = inference.

---

## 0. Corrections to the ticket's guesses

| Ticket guess | Finding |
|---|---|
| WP Rocket "Delay JavaScript execution" | **[V] Off.** 0 hits for `rocketlazyloadscript`, `data-rocket-src`, `data-rocket-type`, `rocket-delay-js` or `RocketLazyLoadScripts` in all 5 HTML files. Scripts are delayed by a separate plugin, **Flying Scripts** (`<script id="flying-scripts">`, pricing-desktop L1845). It uses the pattern `data-type="lazy" data-src=…`. |
| Elementor popups | **[V] Not on these pages.** There is no Elementor JS or CSS. "elementor" appears only as a cookie name in the consent banner template (L1840). The popups are **Remodal v1.1.1** (theme `remodal.min.js?ver=1.1`). Some GTM triggers still use Elementor CSS selectors from old pages (tags 343–347). |
| HubSpot embeds | **[V] Partly right.** The forms load correctly. The JSON.parse error comes from a **GTM Custom HTML tag about the HubSpot chat**, not from the form embeds (§3). |
| Multiple jQuery versions | **[V] The HTML has one copy (3.6.0).** A second copy (3.7.0) is injected at runtime by the **Clearout** widget loaded from GTM (§4). It is not linked to any of the top errors. |

---

## 1. Desktop vs mobile HTML

- **[V]** WP Rocket serves a **separate mobile cache**: desktop `cached@1791971340` vs mobile `cached@1791978679` (pricing), and `1791971002` vs `1791974728` (contact). The Last-Modified headers also differ.
- **[V]** The `<script>` lists are **identical** (same tags, same order, same `data-type="lazy"` set). `diff` of `scripts-*-desktop.txt` vs `-mobile.txt` is empty apart from inline lengths.
- **[V]** The only differences are image and render optimisations: on mobile, below-the-fold icons get `data-lazy-src`, `.content-for_mt` gets `data-wpr-lazyrender="1"` and there is a `rocket-lazyrender-inline-css` style. There is also a different `wpr_t` cache-busting value on the CSS links.
- **[V]** The delay settings are the same on both (Flying Scripts: timeout of 10 s or first interaction).

---

## 2. Cookie consent: `_wccConfig`, `_lawSelected`, `_regions`

### 2.1 Plugin
- **[V] WebToffee GDPR Cookie Consent** (lite). Slug `webtoffee-cookie-consent`, **ver 3.5.5**. The `_restApiUrl` points to `directory.cookieyes.com`, which is the CookieYes codebase.
- The three tags in `<head>` (pricing-desktop L75–77; contact identical; homepage L74–76):
  ```
  L75 <script id="webtoffee-cookie-consent-js-extra" data-type="lazy" data-src="data:text/javascript;base64,…">   ← inline config (wp_localize_script), 60,627 chars decoded
  L76 <script id="webtoffee-cookie-consent-js"     data-type="lazy" data-src=".../lite/frontend/js/script.min.js?ver=3.5.5">
  L77 <script id="webtoffee-cookie-consent-gcm-js" data-type="lazy" data-src=".../lite/frontend/js/gcm.min.js?ver=3.5.5">
  L78 <script src=".../cache/min/1/ajax/libs/jquery/3.6.0/jquery.min.js" id="jquery-js">   ← not delayed
  L81 GTM snippet GTM-PW77M7K                                                           ← not delayed
  ```
- The decoded config (`lazy-pricing-desktop/lazy-L75-webtoffee-cookie-consent-js-extra.js`) defines **`var _wccConfig`, `var _wccStyles`, `var _wccApi`, `var _wccGCMConfig`**. It contains `"_lawSelected":["GDPR"` and `_wccGCMConfig = {"_mode":"advanced",…,"_regions":[],…,"_isGTMTemplate":"1"}`. `node --check` confirms it is valid JS. The config is byte-identical across pricing and contact, and across desktop and mobile.

### 2.2 Consumers (exact code)
- **`script.min.js` (first statement of the IIFE)** → the `_lawSelected` error:
  ```js
  !function(){const _wccStore=window._wccConfig,_wccStyle=window._wccStyles;let currentLaw=window._wccConfig._lawSelected[0],…
  ```
  This matches the Safari text literally: `evaluating 'window._wccConfig._lawSelected'`.
- **`gcm.min.js` (first statements)** → the `_regions` error:
  ```js
  !function(){const data=window._wccGCMConfig;let setDefaultSetting=!0;const regionSettings=data._regions||[], …
  ```
  This matches the Safari text literally: `evaluating 'data._regions'`.
- Both throw **only when the inline config script (L75) has not run yet**. One script defines both globals, so one missing config gives both errors on the same page view. That fits the paired counts exactly (177/177 Chrome, 46/46 Safari).
- **[V] It is not a geo/AJAX config.** The config is inline. The geo lookup (`fetch(_wccStore._restApiUrl)`) runs only if some law has `selectedRegion !== "ALL"`, and here GDPR is `"selectedRegion":"ALL"`. That fetch also happens after `_wccConfig` has already been read.

### 2.3 Load mode and order
- **[V]** All three WebToffee tags are delayed by Flying Scripts. That includes the config, which Flying Scripts turned into a base64 `data:` URI. They run after a 10 s timer or on the first `click/mousemove/keydown/touchstart/touchmove/wheel`:
  ```js
  function loadScripts(){document.querySelectorAll("script[data-type='lazy']").forEach(function(elem){elem.setAttribute("src",elem.getAttribute("data-src"))})}
  ```
- **[I, from the HTML spec]** When the parser hits these empty scripts, it sets the element's *force-async* flag ("prepare the script element", step 3). When `src` is set later, each script runs **as an async script, as soon as it loads, with no ordering guarantee**. So the data-URI config and the two external files race. If `script.min.js` and `gcm.min.js` are ready first (for example from cache on a repeat page view), both run before `_wccConfig` and `_wccGCMConfig` exist, and both errors fire together.
- **[I]** Other ways the data-URI config could fail to run (environments that block `data:` scripts, proxies or review bots) would give the same pair. Segmenting the Clarity errors by browser, new vs returning visitor and bot flag would tell them apart.
- **Fix [I]:** exclude WebToffee from Flying Scripts (keywords `webtoffee-cookie-consent` / `_wccConfig`). At minimum exclude the inline `-js-extra` config, which is inert data and costs nothing to run early. A consent tool should not be delayed anyway: today GTM (L81) starts tags up to 10 s before the consent tool exists.

### 2.4 Side finding: Consent Mode is not wired [V]
`_wccGCMConfig._isGTMTemplate = "1"` tells `gcm.min.js` **not** to send `gtag('consent','default',…)`: `if(!is_gtm_template) … setDefaultConsents()`. It also skips the refresh-time update. The plugin expects the WebToffee CMP template in GTM. But the GTM container (v226) has **0** references to `webtoffee`, `_wcc` or `wt_consent`. No tag has consent settings, and the only custom templates are Facebook Pixel (`__cvt_6392678_244`) and Clarity (`__cvt_MQDKZ`). Hotjar, Clarity, FB Pixel, Apollo, Clearout and Ahrefs all fire on `gtm.js` (All Pages). Nothing sets a consent default.

---

## 3. `JSON Parse error: Unexpected identifier "object"`

- **[V] Culprit: GTM Custom HTML tag `tag_id 179`** (`gtm-parsed/html-tag-125.html`). It fires on `gtm.js`, i.e. All Pages:
  ```js
  window.addEventListener("message",function(a){if("https://app.hubspot.com"!==a.origin)return!1;a=JSON.parse(a.data);switch(a.type){case "closed-welcome-message":… case "open-change":… case "external-api-event":…}
    b&&dataLayer.push({event:"Hubspot Widget",event_category:"Live Chat",…})});
  ```
  It only checks the origin. There is no `typeof a.data==="string"` check and no try/catch. Any object-typed message from `https://app.hubspot.com` becomes `JSON.parse("[object Object]")`, which Safari reports as `JSON Parse error: Unexpected identifier "object"`. In Chrome the same error reads `Unexpected token 'o', "[object Obj"... is not valid JSON` and is probably further down the export.
- **[V] Supporting evidence:**
  - The HubSpot chat iframe domain is `app` for hublet na1 (`getIFrameDomain()` → `fn("app",{hubletOverride:na1})`) = `https://app.hubspot.com`.
  - HubSpot's own chat embed listener wraps the same parse in `try{const t=JSON.parse(e);…}` (`hs-conversations-embed.js`).
  - HubSpot forms `v2.js` also listens for **object** messages from `https://(app|local).hubspot.com` (`e.data.action===SET_IFRAME_HEIGHT`, embedded viral-link iframe). So app.hubspot.com frames do send object-typed data. That particular viral-link iframe is off here: the form JSON has `"noBranding":true`.
- **[I]** Which app.hubspot.com frame sends the object message on 3dlook (most likely the chat widget iframe) cannot be confirmed statically. The chat loader is delayed by Flying Scripts, so the error appears only after the first interaction or 10 s.
- **[V] Ruled out:**
  - The other GTM listeners are guarded: tags 300 and 306 check `a.data&&a.data.type==="hsFormCallback"`, and GTM's own runtime TCF/GPP/gcl listeners use try/catch.
  - First-party JS (theme `main.js`, `remodal`, WebToffee, all inline and decoded delayed scripts) has no message listeners. WebToffee's only JSON.parse is in a try block.
  - OptinMonster `api.min.js`, Clearout, Apollo, HubSpot banner/collectedforms and Ahrefs have no `message` listeners.
  - HubSpot's `hsFormCallback` messages are posted by the page itself (origin 3dlook.ai), so tag 179 skips them.
- **Fix:** `if(a.origin!=="https://app.hubspot.com"||typeof a.data!=="string")return; try{a=JSON.parse(a.data)}catch(e){return}`. Better: replace it with `window.HubSpotConversations.on('conversationStarted', …)` and the related widget events.

---

## 4. jQuery

- **[V]** One jQuery in the HTML: `https://3dlook.ai/wp-content/cache/min/1/ajax/libs/jquery/3.6.0/jquery.min.js?ver=1791970234` (pricing L78, contact L78, home L77). The banner reads `/*! jQuery v3.6.0`. It is WP Rocket's minified local copy of the Google CDN build, loaded synchronously in `<head>` and not delayed. There is **no jquery-migrate** and no WP-core `jquery-core`.
- **[V] Second copy at runtime:** the Clearout widget (GTM Custom HTML `tag_id 288`, All Pages) runs:
  ```js
  "undefined"!=typeof jQuery&&jQuery.fn.jquery===o.a.SUPPOERTED_JQUERY_VERSION||(a.push(n("https://ajax.googleapis.com/ajax/libs/jquery/3.7.0/jquery.min.js")),s=!0) … clearout.$=e?jQuery.noConflict(!0):jQuery
  ```
  `SUPPOERTED_JQUERY_VERSION:"3.7.0"` does not match the page's 3.6.0, so **jQuery 3.7.0 is always injected** and then released with `noConflict(true)`.
- **[I]** For a moment `window.jQuery` is 3.7.0, until the Promise callback runs. A theme call to a plugin such as `.remodal()` or `.slick()` in that window would fail. This is a low-probability risk and none of the top errors match it.
- HubSpot `v2.js` does not bundle jQuery (it only uses `window.jQuery` if present). Remodal is a jQuery plugin and loads after jQuery (L1881).

---

## 5. Delayed vs not delayed (pricing; contact and home follow the same pattern)

**Delayed by Flying Scripts (`data-type="lazy"`; run after first interaction or 10 s, async/unordered):**
- WebToffee config (L75, data URI), `script.min.js` (L76), `gcm.min.js` (L77)
- All `hbspt.forms.create(...)` calls (pricing L1567/1587/1607/1627; contact L545), as base64 data URIs
- HubSpot tracking loader `hs-script-loader` → `/wp-content/cache/min/1/6014382.js` (L2006, `async defer` + lazy). It loads the ads pixel, `hs-analytics`, chat (`conversations-embed.js`), the HubSpot cookie banner and collected forms.

**Not delayed:**
- jQuery 3.6.0 (L78)
- GTM snippet (L81), and everything GTM loads: Hotjar 1082457, Clarity `ptrtdxgprb`, FB Pixel, Clearout, Apollo, Ahrefs, the HubSpot chat listener (tag 179), the UTM helpers and GA4
- **HubSpot forms `//js.hsforms.net/forms/embed/v2.js`.** It is synchronous and parser-blocking, and is included **4×** on pricing (L1566/1586/1606/1626) and 1× on contact (L544).
- `remodal.min.js?ver=1.1` (L1881), `slick.min.js`, `swiper-bundle.min.js`, theme `main.js`, `resize-fz.js`
- OptinMonster: `api.min.js` is injected **twice** (L1842 with campaign `cvrmwb352ycz06yxtvpa`, and L1885 with `id="omapi-script"`) plus `helper.min.js?ver=2.16.24`
- WP Rocket helpers: lazyload 17.8.3, preload-links, lazyload-css

**Elementor:** not present.

**WP Rocket features actually on [V]:** minify JS and CSS (`data-minify="1"`, `/cache/min/1/`), image/iframe LazyLoad 17.8.3, lazy CSS backgrounds, preload links, critical image preloads (`data-rocket-preload`), separate mobile cache, and lazy render on mobile. **Delay JS: off. Load JS deferred: off.**

**Order of `hbspt.forms.create` vs the loader [V/I]:** `v2.js` is not delayed and comes first in the document, so `hbspt` exists when the delayed calls run. There is no ordering error unless `v2.js` itself is blocked (ad blocker → `hbspt is not defined`). The calls have no `target`. `v2.js` renders at `document.currentScript` (`j_=()=>{if(document.currentScript)return document.currentScript;…}`), and that is set for the re-armed script, so each form renders in place. Effect: forms build only after the first interaction or 10 s. On pricing they sit in popups, so the click that opens the popup also starts the forms loading, and the form appears a moment after the popup [I].

---

## 6. HubSpot forms inventory (all `region:"na1"`, `portalId:"6014382"`, no `target`)

| Page | formId (GUID) | Location | In Remodal? | Opened by | GTM `form_name` map |
|---|---|---|---|---|---|
| /pricing/ | `0a22d79d-8ad2-4672-bfa0-df212dedf624` | L1567, `.pricing-contact__form` | **Yes**: `data-remodal-id="modal-pricing-contact"` (L1553), "Maximize Mobile Tailor Benefits…" | MT Enterprise "Start a Trial" `href="#modal-pricing-contact"` (L660, L971) | `pricing_enterprise` |
| /pricing/ | `38880e8c-a0b0-4f2e-ba03-bf226e949612` | L1587 | **Yes**: `bd-modal-starter` (L1573) | FX Starter "Book a demo" `#bd-modal-starter` (L706, L1017) | `fx_pricing_starter` |
| /pricing/ | `aa061d33-717c-4fbf-b5ef-3285a14b10b3` | L1607 | **Yes**: `bd-modal-pro` (L1593) | FX Pro "Book a demo" `#bd-modal-pro` (L738, L1049) | **missing → `"other"`** |
| /pricing/ | `a48a1930-6b6f-432e-9ab9-040122b42d90` | L1627 | **Yes**: `bd-modal-personalized` (L1613) | FX Personalized "Talk to sales" `#bd-modal-personalized` (L773, L1084) | `fx_pricing_talk_to_sales` |
| /contact-us/ | `f227f5ce-8ce1-473d-a4f8-597c832979cc` | L545, `section.contact-form .c-hero__form.dark-form` "Request a Demo" | No (inline) | none | `contact_us` |

The plan grid appears twice on pricing (L568–780 and L880–1090), so every button exists twice. The MT Basic and Premium buttons go to `https://mtm.3dlook.me/accounts/signup`. There is no HubSpot meetings embed on either page (`meetings.hubspot` has 0 hits).

---

## 7. GTM container GTM-PW77M7K (version 226)

- **GA4:** `G-NXNB16WGX6`. A Google tag (`tag_id 298`) fires on `gtm.init`; it is blocked when the host ≠ `3dlook.ai` or the path starts with `/wp-admin`. The constant `G-35H60LHD2Y` (macro 36) is unused. The legacy UA `UA-92309701-1` (`__gas`) still drives 24 dead UA tags, including a "JS Errors" UA tag on `gtm.pageError`.
- **Events that exist today [V]:**
  - `demo_click` (tag 316). Fires on `gtm.linkClick` with URL containing `#bd-modal` (FX Starter/Pro/Personalized). It also fires on links to `/contact-us` whose text matches `book a demo|let's talk|request a demo|talk to sales|sign up`. **It does not cover** `#modal-pricing-contact` (MT Enterprise "Start a Trial").
  - `generate_lead` (tag 310). Fires on custom event `hs_form_submit`, unless form_name = careers. Params: `form_id` and `form_name` (lookup map). `hs_form_submit` is pushed by Custom HTML tag 306 on `hsFormCallback/onFormSubmitted` or `hs-form-event:on-submission:success`.
  - `meeting_booked` (tag 314). Fires on custom event `meeting_booked`, which tag 306 pushes on `message` with `data.meetingBookSucceeded`. Neither page has a meetings embed.
  - `pricing_plan_click` (tag 320). Exists, but its trigger is `gtm.click` AND click text matches the regex above AND **`Page Path` equals `/pricing`** (predicate 103, `_eq`). The live path is **`/pricing/`** (canonical), so **[I, high confidence] this tag never fires**. It would also skip "Start a Trial".
  - Also present: `demo_button_click` (`.u-hero__link`), `docs_click`, `careers_submit`, and older events (`send_form`, `contact_us`, `get_in_touch`, `request_a_quote`, `try_for_free`, `404_error`, `ap_*`).
- **Side finding [V]:** `https://3dlook.ai/pricing` (no slash) returns **301 → `https://3dlook.me/`** (`X-Redirect-By: redirection`). A Redirection-plugin rule sends any slashless `/pricing` link to the 3dlook.me homepage.

---

## 8. Recommended changes, in order
1. **Flying Scripts:** exclude WebToffee (at least `webtoffee-cookie-consent-js-extra`; ideally all three). This fixes the `_lawSelected` and `_regions` pairs (~446 of 519 errors).
2. **GTM tag 179:** add a string check and try/catch around `JSON.parse` (or switch to the `HubSpotConversations` API). This fixes the `[object Object]` JSON errors.
3. **GTM tracking fixes:**
   - `pricing_plan_click`: change the path condition to `/pricing/` or "starts with `/pricing`".
   - Add `aa061d33-…` to the form_name map (e.g. `fx_pricing_pro`).
   - Decide whether `#modal-pricing-contact` counts as `demo_click` or `pricing_plan_click`.
4. **Consent:** add the WebToffee CMP template on Consent Initialization, or set `_isGTMTemplate` off. Add consent checks to the Hotjar, Clarity, FB, Apollo and Clearout tags.
5. **Hygiene:** load `v2.js` once per page instead of 4×. Remove the duplicate OptinMonster `api.min.js` injection. Remove the Clearout jQuery duplication (Clearout setting or page jQuery 3.7.0). Fix the `/pricing` → 3dlook.me redirect rule.
