# Rob Waldron — Chief Technology & Security Officer — Fitness and Lifestyle Group

## Context used
- Angle: technical-integration
- Hook: CIO and CISO seat, earlier head of architecture and engineering; SDK step in the member apps
- Proof point: SDK/API, Real-Time Pose Validation, 2-4 weeks for basic integration, 80+ body measurements, data-handling sentence

---

## Connection request (Day 0)
_Без note — отправляем запрос в друзья без сопроводительного текста._

## Message 1 — Opener (сразу после принятия запроса)
Hi Rob,

For the CIO and CISO seat at Fitness & Lifestyle Group, a body scan in the member apps would be one SDK step in onboarding.

A weight entry or a progress photo leaves out waist and lean mass change. FitXpress ships as web and mobile SDKs with supported iOS and Android integrations. Real-Time Pose Validation guides framing during capture, and the API returns one timestamped record per scan with a processing status, including 80+ body measurements.

How does your team review a new SDK vendor before it reaches the member apps?

Vadim

**Char count:** 545 / 900

## Message 2 — Value + demo call (+5 дней, если нет ответа)
Hi Rob,

The recommended setup is the SDK along with the API: pose and framing validation runs in the SDK capture layer, and processing status and timestamps come back in the API response. Typical time for a basic integration is 2 to 4 weeks.

On data handling, photos are deleted after processing or kept up to 30 days under the client's policy, with blurring and face obfuscation.

Might be worth a quick chat?

Vadim

**Char count:** 419 / 700
