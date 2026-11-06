# mtm.3dlook.me: sign-up page returns HTTP 404, and Google Ads / Meta tags crash on it

**For:** whoever has access to AWS (CloudFront + S3) for `mtm.3dlook.me` (Problem 1) and the Mobile Tailor front-end developer (Problem 2).
**Priority:** P2. Users can still sign up. Crawlers, link checkers and ad platforms see a broken page, and ad tracking on the app is partly broken.
**First seen:** 2026-10-14 (browser audit of /pricing/). **Re-checked:** 2026-11-06, both problems still there.

---

## Problem 1. Every app URL except `/` returns HTTP 404

The Basic and Premium "Start a 7-day trial" buttons on https://3dlook.ai/pricing/?mt link to https://mtm.3dlook.me/accounts/signup. The browser shows the sign-up form, but the server answers **404 Not Found**.

```
$ curl -sI https://mtm.3dlook.me/accounts/signup
HTTP/2 404
server: AmazonS3
x-amz-error-code: NoSuchKey
x-amz-error-message: The specified key does not exist.
x-amz-error-detail-key: accounts/signup
x-cache: Error from cloudfront
```

| URL | Status |
|---|---|
| `/` and `/index.html` | 200 |
| `/accounts/signup`, `/accounts/signup/` | **404** |
| `/accounts/login`, `/accounts/login/` | **404** |
| any other path | **404** |

The 404 body is byte-identical to `index.html` (Angular 8.2.14 app, `<saia-root>`).

**Cause.** The app is a single-page Angular app served from S3 through CloudFront. S3 has no object called `accounts/signup`, so it answers 404 `NoSuchKey`. A fallback then serves `index.html` so the page renders, but it **keeps the 404 status**. The fallback is set either as the S3 static-website "Error document = index.html" or as a CloudFront custom error response that returns code 404. Both behave like this.

**Why it matters.**
- Google Ads checks destination URLs. A final URL that returns 404 can get ads disapproved ("Destination not working").
- Link checkers, uptime monitors, Ahrefs and Google Search Console report https://3dlook.ai/pricing/ as linking to a broken page.
- The same applies to any deep link into the app (login and any other route).

### Fix: pick one

**Option A: CloudFront custom error response (about 5 minutes in the console).**
1. CloudFront → the distribution for `mtm.3dlook.me` → **Error pages** → **Create custom error response**.
2. HTTP error code: **404**. Customize error response: **Yes**. Response page path: **`/index.html`**. HTTP response code: **200**. Error caching minimum TTL: **10**.
3. If a rule like this already exists with response code 404, change only the response code to **200**.
4. If the origin is a private bucket (REST endpoint + OAC/OAI), S3 answers **403** for missing keys. Add the same rule for 403.
5. Create an invalidation for `/accounts/*` to flush the cached 404s.

Side effect: a missing static file (an old JS chunk, for example) will also come back as 200 with HTML instead of 404. That is normal for SPAs.

**Option B: CloudFront Function (cleaner, real 404 stays for missing files).**
Create a CloudFront Function and attach it to the **default (S3) behaviour** as *Viewer request*. Do not attach it to any `/api/*` or other non-S3 behaviour, if there is one.

```js
function handler(event) {
  var request = event.request;
  // Static files keep their real path (and a real 404 if missing).
  // Everything else is an Angular route: serve index.html with 200.
  if (!/\.(js|css|map|json|txt|xml|ico|png|jpe?g|gif|svg|webp|woff2?|ttf|eot)$/i.test(request.uri)) {
    request.uri = '/index.html';
  }
  return request;
}
```

### How to check
```
curl -sI https://mtm.3dlook.me/accounts/signup | head -1    # expect HTTP/2 200
curl -sI https://mtm.3dlook.me/accounts/login  | head -1    # expect HTTP/2 200
curl -sI https://mtm.3dlook.me/                | head -1    # expect HTTP/2 200
```
Then click "Start a 7-day trial" on https://3dlook.ai/pricing/?mt: the form must open, and the URL must still carry the `_gl` parameter. Cross-domain GA4 works today, so make sure the fix keeps it working.

---

## Problem 2. `Promise.allSettled is not a function` crashes the Google Ads tag and Meta Pixel

On https://mtm.3dlook.me/accounts/signup (Chromium, 2026-11-06):

```
Uncaught TypeError: Promise.allSettled is not a function
    at https://www.googletagmanager.com/gtag/js?id=AW-842555409:588
Uncaught TypeError: Promise.allSettled is not a function
    at https://connect.facebook.net/en_US/fbevents.js:58
```

In the page console: `Promise.name === "S"` and `typeof Promise.allSettled === "undefined"`.

**Cause.** Angular 8 ships with zone.js 0.9.x. It replaces `window.Promise` with its own `ZoneAwarePromise`, which has no `allSettled`. Current Google `gtag.js` and Meta `fbevents.js` call `Promise.allSettled` and throw.

**Impact (what we saw).** The Google Ads `page_view` hit still went out (`google.com/ccm/collect` → 200), but the tag throws during its run, so conversion events after sign-up are at risk. Meta Pixel `642279129301626` sent **no** PageView in our test (no request to `facebook.com/tr`). We could not test a real sign-up conversion.

### Fix
In `src/polyfills.ts`, add a small shim **right after** the zone.js import:

```ts
import 'zone.js/dist/zone';  // existing line

// gtag.js and fbevents.js call Promise.allSettled; zone.js 0.9 does not provide it.
if (typeof (Promise as any).allSettled !== 'function') {
  (Promise as any).allSettled = (items: Iterable<unknown>) =>
    Promise.all(
      Array.from(items, (p) =>
        Promise.resolve(p).then(
          (value) => ({ status: 'fulfilled', value }),
          (reason) => ({ status: 'rejected', reason }),
        ),
      ),
    );
}
```

Upgrading Angular, and zone.js with it, also fixes this. The shim is the one-deploy fix.

### How to check
On https://mtm.3dlook.me/accounts/signup, in DevTools console:
- `typeof Promise.allSettled` returns `"function"`;
- no `allSettled` errors after reload;
- Meta Pixel Helper shows a PageView for `642279129301626`;
- Google Tag Assistant shows `AW-842555409` with no errors.
