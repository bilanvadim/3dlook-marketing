# Koos van der Veen — Chief Information Officer Life&Pension Nationale Nederlanden — Nationale-Nederlanden

## Context used
- Angle: technical-integration
- Hook: CIO Life and Pension; where ORV acceptance meets IT
- Proof point: 2 photos, Smart Scales weight estimate, threshold flag, retention, GDPR line (card); NN ORV page (Account facts)

---

## Connection request (Day 0)
_Без note — отправляем запрос в друзья без сопроводительного текста._

## Message 1 — Opener (сразу после принятия запроса)
Hi Koos,

Quick one for the CIO of Life & Pension at NN. ORV applications within its limits are accepted on an online questionnaire alone.

The step returns one timestamped record: a Smart Scales weight estimate from 2 photos, and a flag when the gap to the declared weight crosses NN's threshold.

How would such a record be stored in the acceptance system today, as a document or as fields?

Olena

**Char count:** 399 / 600

## Message 2 — Value + demo call (+5 дней, если нет ответа)
Hi Koos,

An SDK step in the web journey sends the 2 photos, and a REST API request can pass the structured record to the acceptance system. Photos are deleted after processing or within 30 days, per the insurer's policy.

In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes SCCs.

A technical session can be booked here: https://meetings.hubspot.com/olena-kudriavtseva

Olena

**Char count:** 472 / 550
