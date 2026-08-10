# Prompt Template: 3D visual rewrite (Three.js scene)

Use this structure when delegating a 3D scene replacement to Claude Code —
changing the visual style of a Three.js scene while preserving interactive logic.

## Template

```
Replace the current [OLD_STYLE] 3D [OBJECT] in the hero section
with a [NEW_STYLE] 3D [OBJECT].

REFERENCE STYLE (from [reference_url]):
- [visual property 1]
- [visual property 2]
- [visual property 3]

WHAT TO DO:

1. REMOVE [old approach] completely — no more [old imports/loaders/files].

2. BUILD [new approach] using ONLY [tech stack]:

   The [OBJECT] should consist of:
   - [COMPONENT 1]: [geometry description]
   - [COMPONENT 2]: [geometry description]
   - [COMPONENT 3]: [geometry description]

   Style:
   - [color, opacity, material specs]
   - [NO solid faces — everything is wireframe/edges only]
   - [any exceptions — e.g. "screen plane is the ONLY solid surface"]

3. LIGHTING: [how to light the new scene]

4. BACKGROUND: [CSS/canvas background treatment]

5. INTERACTION — KEEP ALL EXISTING LOGIC:
   - [list specific functions/variables to preserve]
   - [state machine to preserve]

6. ANIMATION:
   - [new animations to add]
   - [existing animations to preserve]

7. CAMERA: [adjustments for new object]

CRITICAL RULES:
- Do NOT touch [list of things to preserve]
- Do NOT change [content/data structures]
- Do NOT break [specific mechanism]
- Remove ALL [old approach]-related code
- [build command] must pass

OPTIONAL ENHANCEMENTS:
- [bonus feature 1]
- [bonus feature 2]
```

## Real example: smiro.dev GLB → wireframe PC

Prompt: `/tmp/prompts/smiro-wireframe-pc.txt` (3596 bytes)

Result:
- Claude Code, 30 turns, $2.98, timed out at 600s (exit 124)
- Rewrote `public/pc3d.js`: 694 → 893 lines (+382/-183)
- Updated `src/pages/index.html`: +44/-6 lines (CSS background, floating glyphs)
- `npm run build` passed (3 pages, 2.2s)
- Vercel deploy: Ready (22s)
- All interactive logic preserved: CanvasTexture screen, proximity typing, Enter→build→CV

## Why this structure works

1. **REFERENCE STYLE first** — gives Claude a concrete visual target before any instructions
2. **REMOVE then BUILD** — clear teardown/rebuild sequence prevents hybrid artifacts
3. **Component breakdown** — monitor/stand/keyboard listed separately so Claude builds them as units
4. **CRITICAL RULES** — negative constraints prevent Claude from touching working code
5. **OPTIONAL at the end** — bonus features that Claude can skip if running out of turns

## Pitfalls avoided

- The old `claude-code-hermes` pitfall about "Claude уходит в сторону с широкими промптами"
  was NOT triggered here because:
  - Reference style focused Claude on the visual target
  - CRITICAL RULES section explicitly listed what NOT to touch
  - The prompt had clear component breakdown (not vague "make it beautiful")
  - No unrelated tasks mixed in (just the 3D scene)
