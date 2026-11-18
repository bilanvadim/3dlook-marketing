# Murdo Macmillan — CTO — PillTime

## Context used
- Angle: technical-integration
- Hook: CTO, PillTime data flow
- Proof point: SDK and API; camera-roll picker disabled; controller line

---

## Connection request (Day 0)
_Без note — отправляем запрос в друзья без сопроводительного текста._

## Message 1 — Opener (сразу после принятия запроса)
Hi Murdo,

I would like to go through the data flow for PillTime's weight-loss service. A typed weight arrives as a bare value with no source attached, and the data around it differs from method to method.

I run 3DLOOK, and FitXpress is an SDK with an API. The SDK runs the capture in the session, 2 photos on the phone with the camera-roll picker disabled. The API returns structured data: a Smart Scales weight estimate, BMI and one timestamped record per check, which your system can compare with the declared figure against a threshold PillTime sets. Liveness controls may require a prompted action during capture, helping indicate whether the session involved a live person.

I'll be in London 23 to 25 November. Could we do 30 minutes there, or over a call?
https://meetings.hubspot.com/katerina-galich

Katerina

**Char count:** 819 / 900

## Message 2 — Value + demo call (+5 дней, если нет ответа)
Hi Murdo,

Beyond weight, the API returns 80+ body measurements. In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR.

For the engineering detail, you can book a call here:
https://meetings.hubspot.com/katerina-galich

Katerina

**Char count:** 297 / 900
