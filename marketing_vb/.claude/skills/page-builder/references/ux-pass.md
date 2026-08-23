# UI/UX pass

Phase 3, pass 5. The page already has structure and copy; this pass decides whether a buyer can
actually use it on the device they are holding.

---

## The rule that decides every conflict

**`DESIGN.md` wins.** Colours, type, spacing, radius, button shapes and imagery direction come from
the 3DLOOK design system, confirmed from the Figma export. A generic recommendation never overrides
it, however good it looks in isolation. A page that is beautiful and off-brand has failed, because the
buyer's first judgement is "is this the same company I was just talking to".

| Decided by `DESIGN.md` | Decided by this pass |
|---|---|
| Palette, Satoshi type scale | Layout and section rhythm |
| Spacing steps, radius scale, shadows | Which component carries which slot |
| Button shapes and fills, focus ring | Hierarchy and scan path |
| Imagery direction, the triangle motif | Accessibility and touch behaviour |
| Motion character | Loading and empty states |

`ui-ux-pro-max` is not installed in this project, and it is not needed: the tokens question is already
answered. If it is ever installed, never run it with `--design-system` for a 3DLOOK page — that flag
generates a fresh palette and type pairing, which is exactly what `DESIGN.md` already decides.

### The tokens, in short

Satoshi only — **Bricolage Grotesque and IBM Plex Sans are superseded and must never reappear**.
Electric blue `#143DFF` stays a single sharp accent, never a large fill; `#0F2ECD` on hover. Navy
`#050F40` carries hero, proof and CTA bands with a radial glow plus grain or a measurement-grid
texture — never a flat navy block. Radius: 4–5px buttons and inputs, 15px chips, 20px cards, 30–40px
large surfaces, pill for circular. Spacing only from the 2 · 4 · 8 · 12 · 16 · 20 · 24 · 32 · 40 · 48
· 60 · 80 · 96 · 120 scale; container `1200px`, padding `clamp(24px, 5vw, 80px)`. Focus ring
`#B1BDFF`, 3px, 2px offset. On navy, the primary CTA is a white button with dark text. Copy-paste
`:root` block is in `DESIGN.md` §13.

Proof moments lead with oversized numerals — the number is the hero. Prefer the three carrier assets
(3D body-scan render, guided-capture phone UI, admin panel in a browser frame) over icon grids.

---

## Review order — highest cost of failure first

### 1. Accessibility — blocking

- [ ] Contrast at least 4.5:1 for body text, 3:1 for large text and meaningful icons
- [ ] No light text over imagery without a scrim
- [ ] Visible focus ring on every interactive element; focus order matches visual order
- [ ] Alt text on every meaningful image; empty alt on decorative ones
- [ ] `aria-label` on icon-only buttons
- [ ] Every form field has a real `<label>` tied by `for` — the demo form especially
- [ ] Operable by keyboard alone, including the primary action and the FAQ accordion

A page that fails contrast or keyboard operation fails the pass outright. It is also a hard fail at
the blind judge, and for a company selling into US healthcare and EU enterprises it is a procurement
question, not a polish item.

### 2. Touch and interaction — blocking

- [ ] Touch targets at least 44×44 px, with spacing between adjacent ones
- [ ] Nothing important revealed only on hover — there is no hover on a phone
- [ ] Submit button disables and shows state during async work
- [ ] Errors appear next to the field that caused them, in plain language
- [ ] FAQ accordion opens on tap, and its state is announced
- [ ] `cursor: pointer` on anything clickable

### 3. Performance

- [ ] Images WebP with `srcset`, lazy-loaded below the fold, under 200KB where possible
- [ ] Space reserved for async content so nothing jumps as it loads
- [ ] `prefers-reduced-motion` respected — required by `DESIGN.md` §9
- [ ] Satoshi subset and preloaded; no layout shift when it swaps in

### 4. Layout and responsive

- [ ] Viewport meta present
- [ ] Body text at least 16px on mobile
- [ ] No horizontal scroll at 320px
- [ ] Comparison tables, accuracy tables and diagrams scroll inside their own container, not the page
- [ ] Section rhythm from the spacing scale; no invented gaps
- [ ] A defined z-index scale rather than ad-hoc numbers

### 5. Typography and colour — inside the design system

- [ ] Line height 1.5–1.75 for body copy
- [ ] Line length 65–75 characters at desktop width
- [ ] Heading levels used for hierarchy, not for size
- [ ] Sentence case in headings, per the humanisation pass
- [ ] Colour never the only carrier of meaning

### 6. Motion

- [ ] Scroll-reveal with stagger on section entry, subtle and precise — no bounce or overshoot
- [ ] Transitions ~150ms; hover lift `translateY(-1px)` on buttons
- [ ] Animate `transform` and `opacity`, not `width` and `height`
- [ ] Loading states are skeletons, never a blank region

---

## The 60-second scan test

Look at the page for one minute the way a stranger from the target vertical would, and answer:

1. What does this do, and for whom in my market?
2. What is the one action this page wants?
3. Why should I believe them — which number or customer did I actually notice?

If any answer takes longer than the minute, the problem is hierarchy, not copy. Fix it here rather
than sending it back to the writer.

---

## What this pass hands to the blind judge

The judge scores **Design and technical layer** without opening a browser, so `fact-sheet.md` states
plainly: measured performance, viewport widths checked, contrast results, whether keyboard operation
was verified manually, and which tokens came from `DESIGN.md` versus anything improvised. Unverified
items are reported as unverified, never as passed.

`⚠` Logo geometry, clearspace and minimum sizes are not in the current export. Request the brand-mark
asset kit before reproducing the triangle mark at small sizes — do not redraw it.
