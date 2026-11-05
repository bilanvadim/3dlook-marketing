# Paul Mocarski — Chief Information Security Officer (CISO) and Vice President IT Infrastructure — Sammons Financial

## Context used
- Angle: technical-integration
- Hook: security review of a photo step at Sammons
- Proof point: API/SDK, two photos (card Rules)

---

## Connection request (Day 0)
_Без note — отправляем запрос в друзья без сопроводительного текста._

## Message 1 — Opener (сразу после принятия запроса)
Hi Paul,

Wondering how Sammons reviews a new data vendor: a photo step in the e-application would bring one into the new-business journey.

Through an SDK or API, two photos give FitXpress a Smart Scales weight estimate and a flag above a threshold the carrier sets, returned as one structured record.

Which checks does a new data vendor go through before launch at Sammons?

Nick

**Char count:** 382 / 600

## Message 2 — Value + demo call (+5 дней, если нет ответа)
Hi Paul,

TLS in transit and S3-managed encryption at rest. Photos are deleted after processing or within 30 days per the carrier's policy, with retained photos blurred and faces obscured at capture.

FitXpress is not a medical device and does not make underwriting decisions.

Security documents go through legal@3dlook.me, and the FAQ covers data handling: https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/

A call would cover the rest: https://meetings.hubspot.com/nick-omelchak

Nick

**Char count:** 515 / 550
