# Interactive SVG Zoom/Pan — ZoneMap pattern

## Context
Converting a static SVG map (radar-style, 500×500 viewBox) into an interactive component with:
- Mouse wheel zoom (slow, centered on cursor)
- +/- buttons (corner, appear on hover)
- Drag to pan
- All existing SVG elements preserved inside a transformed `<g>`

## Component structure

```tsx
"use client";
import { useState, useCallback, useRef, useEffect } from "react";

interface Transform {
  scale: number;
  x: number;
  y: number;
}

export default function InteractiveMap() {
  const [transform, setTransform] = useState<Transform>({ scale: 1, x: 0, y: 0 });
  const svgRef = useRef<SVGSVGElement>(null);

  // Wheel zoom — native listener because React onWheel is passive
  useEffect(() => {
    const svg = svgRef.current;
    if (!svg) return;
    const handler = (e: WheelEvent) => {
      e.preventDefault();
      const rect = svg.getBoundingClientRect();
      // Convert screen coordinates to viewBox coordinates
      const mouseX = ((e.clientX - rect.left) / rect.width) * 500;
      const mouseY = ((e.clientY - rect.top) / rect.height) * 500;
      const direction = e.deltaY > 0 ? -1 : 1;
      const factor = 1 + direction * 0.08;
      
      setTransform(prev => {
        const newScale = Math.min(3, Math.max(1, prev.scale * factor));
        const newX = mouseX - (mouseX - prev.x) * (newScale / prev.scale);
        const newY = mouseY - (mouseY - prev.y) * (newScale / prev.scale);
        return { scale: newScale, x: newX, y: newY };
      });
    };
    svg.addEventListener("wheel", handler, { passive: false });
    return () => svg.removeEventListener("wheel", handler);
  }, []);

  return (
    <div className="group relative w-full">
      <svg ref={svgRef} viewBox="0 0 500 500" className="w-full cursor-grab active:cursor-grabbing">
        <g transform={`translate(${transform.x} ${transform.y}) scale(${transform.scale})`}>
          {/* All existing SVG content goes here */}
        </g>
        {/* +/- buttons — show on group hover */}
        <foreignObject x="440" y="440" width="50" height="80">
          <div className="flex flex-col gap-1 opacity-0 group-hover:opacity-100 transition-opacity">
            <button onClick={() => zoomStep(0.15)} className="w-8 h-8 rounded-lg bg-black/40 hover:bg-black/60 flex items-center justify-center text-white/60 hover:text-white">+</button>
            <button onClick={() => zoomStep(-0.15)} className="w-8 h-8 rounded-lg bg-black/40 hover:bg-black/60 flex items-center justify-center text-white/60 hover:text-white">−</button>
          </div>
        </foreignObject>
      </svg>
    </div>
  );
}
```

## Key decisions

| Decision | Why |
|----------|-----|
| `addEventListener("wheel", { passive: false })` | React's `onWheel` is passive → `preventDefault()` has no effect |
| Zoom factor `1 ± 0.08` per tick | Slow, precise. 0.15 would be too fast for this map |
| Scale clamped to `[1, 3]` | Prevents zoom-out below native size; 3× is enough for cities |
| `foreignObject` for +/- buttons | Avoids SVG button complexity; uses Tailwind classes directly |
| `group-hover:opacity-100` on buttons | Buttons appear only when user interacts with the map area |
| Zoom to cursor | `mouseX/mouseY` mapped from screen coords to viewBox coords; transform adjusted so cursor point stays put |

## Drag implementation (add to component)

```tsx
const dragRef = useRef<{ active: boolean; startX: number; startY: number; offsetX: number; offsetY: number }>({
  active: false, startX: 0, startY: 0, offsetX: 0, offsetY: 0,
});

const onMouseDown = (e: React.MouseEvent) => {
  dragRef.current = { active: true, startX: e.clientX, startY: e.clientY, offsetX: transform.x, offsetY: transform.y };
};
// Listeners on window so drag continues outside SVG bounds
useEffect(() => {
  const move = (e: MouseEvent) => {
    if (!dragRef.current.active) return;
    const dx = (e.clientX - dragRef.current.startX) * (500 / svgRef.current!.getBoundingClientRect().width);
    const dy = (e.clientY - dragRef.current.startY) * (500 / svgRef.current!.getBoundingClientRect().height);
    setTransform(prev => ({ ...prev, x: dragRef.current.offsetX + dx, y: dragRef.current.offsetY + dy }));
  };
  const up = () => { dragRef.current.active = false; };
  window.addEventListener("mousemove", move);
  window.addEventListener("mouseup", up);
  return () => { window.removeEventListener("mousemove", move); window.removeEventListener("mouseup", up); };
}, []);
```

## Snap-back to center on minimum zoom

When the user drags at minimum zoom (scale ≈ 1), the map should automatically return to center on release. At higher zoom levels, drag should be free.

**Why `useRef` + `scaleRef` is needed:** the `onUp` handler inside `useCallback` may capture a stale `scale` from the closure. A ref always holds the latest value.

```tsx
// Track scale in a ref so onUp always reads the latest value
const scaleRef = useRef(1);
// Update on every render
scaleRef.current = t.scale;

// In the onUp handler (inside handleMouseDown's useCallback):
const onUp = () => {
  dragRef.current = null;
  setDragging(false);
  window.removeEventListener("mousemove", onMove);
  window.removeEventListener("mouseup", onUp);
  // Snap back to center when zoomed out
  if (scaleRef.current <= 1.05) {
    setT((prev) => ({ ...prev, x: 0, y: 0 }));
  }
  // If scale > 1.05, leave map where user dragged it
};
```

**What NOT to do:**
- Don't use `setT((prev) => { if (prev.scale <= 1.05) ... })` — `prev.scale` inside `setT` may be stale due to batching
- Don't use CSS `transition` on the transform group during snap-back — it conflicts with active dragging
- Don't use a `snapBack` state flag with `setTimeout` to control transitions — it's unreliable and adds complexity

**Threshold:** `1.05` (not exactly `1.0`) — accounts for floating-point drift from wheel zoom.

## Real usage: ASCoFaçade ZoneMap
- File: `components/ui/ZoneMap.tsx` (410 insertions, 256 deletions from static version)
- Commit: `369651b` (initial interactive), `b362f85` (snap-back fix)
- Map data: SECTEUR (red intervention towns) + LIMITROPHES (taupe neighboring towns)
- Center: Saint-Gervais (44.1855, 4.5713)
- Rings at 10/25/50 km, département labels, legend
