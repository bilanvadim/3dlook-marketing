# Matthew Clark — Chief Information Security Officer — Penn Mutual

## Context used
- Angle: technical-integration
- Hook: security review of a photo step added to Penn Mutual's e-application
- Proof point: API/SDK, two photos (card Rules)

---

## Connection request (Day 0)
_Без note — отправляем запрос в друзья без сопроводительного текста._

## Message 1 — Opener (сразу после принятия запроса)
Hi Matthew,

Wondering how a photo step in Penn Mutual's e-application would pass through security review.

FitXpress takes two photos through an API or SDK and returns a Smart Scales weight estimate with a flag above a threshold the carrier sets, as one structured record.

What does a new data vendor have to clear before it joins the new-business journey?

Nick

**Char count:** 364 / 600

## Message 2 — Value + demo call (+5 дней, если нет ответа)
Hi Matthew,

For the review: TLS in transit and S3-managed encryption at rest. Photos are deleted after processing or within 30 days per the carrier's policy, retained photos are blurred, and faces are obscured at capture.

FitXpress is not a medical device and does not make underwriting decisions.

Documents go through legal@3dlook.me, and the FAQ covers data handling: https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/

A call with security would cover the rest: https://meetings.hubspot.com/nick-omelchak

Nick

**Char count:** 543 / 550
