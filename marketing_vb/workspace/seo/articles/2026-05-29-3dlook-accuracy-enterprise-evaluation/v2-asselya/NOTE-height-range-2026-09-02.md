# Height range: local copies were stale, the live page was right

**2026-09-02.** Vadim confirmed the height range is **150 to 220 cm**, for both the training-data
demographic coverage and the internal validation population. There is no second dataset and no
second figure.

## What was actually wrong here

The live page carries the correct figure. Fetched 2026-09-02 from
<https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/>, which states 150-220 cm in three
places:

> The internal validation population included participants aged 16-78, heights of 150-220 cm,
> weights of 38-210 kg, and participants from the US and Europe.

So this was **not** a case of a published page needing a CMS edit. It was the opposite: our local
copies in this directory had drifted to 150-205 cm and no longer matched what shipped. Corrected
on 2026-09-02 in `final.md`, `draft-final.md` and `phase-4-self-critique.md`.

## What was deliberately NOT changed

`(With Comments from Whitney) FAQ Article - Accuracy, Validation & Comparative Proof.txt` and
`(Pre-Final version) FAQ Article - Accuracy, Validation & Comparative Proof.txt` still read
150-205 cm. Those are **inbound documents** and they are the record of what was received and
reviewed. Editing them would falsify that record, so they keep the old figure. They are inputs,
not sources of truth, and no agent cites them.

## Where the figure now lives

`brand-assets/product-info/proof-points.md` is the source of truth and reads 150-220 cm, alongside
`how-it-works.md`, `faq.md`, `about-me.md` and claim FX-011 in the wellness-hub context pack.
