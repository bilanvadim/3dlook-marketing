# Michael Sasaki — IT Director IWR — Aviva

## Context used
- Angle: technical-integration
- Hook: IT Director for Insurance, Wealth and Retirement
- Proof point: 2 photos, flag on insurer threshold (card)

---

## Connection request (Day 0)
_Без note — отправляем запрос в друзья без сопроводительного текста._

## Message 1 — Opener (сразу после принятия запроса)
Hi Michael,

A capture step in a protection application is one more outside dependency for the IT estate you direct in IWR.

FitXpress returns one timestamped record from 2 photos: a Smart Scales weight estimate, BMI from the declared height, and a flag when the gap from declared weight passes a threshold Aviva sets.

What fallback does IWR expect when an external step in an application is unavailable?

Katerina

**Char count:** 415 / 600

## Message 2 — Value + demo call (+5 дней, если нет ответа)
Hi Michael,

The scan is a REST API call with SDKs for web and mobile, and the application can time the step out and carry on by its existing route if the call fails.

In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes SCCs.

I would be glad to go through the integration pattern in a call: https://meetings.hubspot.com/katerina-galich

Katerina

**Char count:** 442 / 550
