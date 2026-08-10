# 3D GLB Model Integration Pattern

Session: smiro.dev — replacing procedural Three.js PC with DRACO-compressed GLB.

## Google Drive → project pipeline

```bash
# 1. Download folder from Google Drive
pip install gdown
gdown --folder "https://drive.google.com/drive/folders/<FOLDER_ID>" -O /tmp/3d-assets/

# 2. Unzip
unzip -o "/tmp/3d-assets/path/to/3d-pc.zip" -d /tmp/3d-assets/extracted/

# 3. Copy to project public/
cp /tmp/3d-assets/extracted/*.glb /path/to/project/public/models/
```

## GLB optimization (if source is 50MB+)

Claude Code can handle this automatically. Key tools:
- `npx @gltf-transform/cli draco input.glb output.glb` — DRACO compression
- `npx @gltf-transform/cli meshopt input.glb output.glb` — meshopt alternative
- Target: under 5MB for web delivery

In this session Claude produced `pc.glb` (1.3MB) from 62MB source.

## CRITICAL: Remove old geometry, don't async-hide

**Anti-pattern (causes visible old model for 2-5 seconds):**
```javascript
// BAD: procedural PC visible until GLB loads
gltfLoader.load('/model.glb', (gltf) => {
  hideProcedural();        // hides old model in CALLBACK
  scene.add(gltf.scene);   // ~3 seconds after page load
});
```

**Correct: GLB-only (no old geometry at all):**
```javascript
// GOOD: only GLB in scene. If load fails, show fallback or message.
gltfLoader.load('/model.glb', (gltf) => {
  const model = gltf.scene;
  fitModel(model);
  scene.add(model);
  // screen overlay + enter ring are added separately (not part of GLB)
}, undefined, (err) => {
  console.warn('GLB failed', err);
  // show simple fallback, NOT procedural PC
});
```

Why: `hideProcedural()` in GLB callback = old model visible 2-5 seconds. User sees both models, or old model flashes. Remove procedural geometry completely — don't hide it.

## Dual-mode pattern: GLB primary, procedural fallback

If you DO need fallback, HIDE old model BEFORE loading:
```javascript
// Hide procedural IMMEDIATELY, before GLB load starts
proceduralGroup.visible = false;

gltfLoader.load('/model.glb', (gltf) => {
  scene.add(gltf.scene);
}, undefined, (err) => {
  proceduralGroup.visible = true;  // show fallback only on error
  console.warn('GLB failed, using procedural fallback', err);
});
```

## Interaction mapping for merged GLBs

When the GLB is one merged mesh with no named sub-parts:
- Keep invisible interaction meshes (enterKey, kbBody) positioned over the GLB keyboard
- Keep the screen overlay plane with CanvasTexture over the GLB monitor
- Raycasting hits the invisible meshes (Three.js raycaster ignores `.visible`)

```javascript
// Invisible enter key for raycasting
const enterKey = new THREE.Mesh(
  new THREE.BoxGeometry(KEY_W, KEY_H, KEY_D),
  new THREE.MeshStandardMaterial({ visible: false })
);
enterKey.name = 'enter';

// Visible glowing ring as affordance
const enterRing = new THREE.Mesh(
  new THREE.TorusGeometry(0.34, 0.018, 10, 40),
  new THREE.MeshBasicMaterial({ color: 0xe86830, transparent: true, opacity: 0 })
);
// Opacity animated in render loop based on cursor proximity
```

## Screen overlay on GLB monitor

```javascript
// CanvasTexture plane over GLB monitor
const screen = new THREE.Mesh(
  new THREE.PlaneGeometry(SCREEN_W, SCREEN_H),
  new THREE.MeshBasicMaterial({ map: canvasTexture, toneMapped: false })
);
screen.name = 'screen';
screen.position.copy(TUNE.screen);

// If GLB has a named screen mesh — steal its material
model.traverse((o) => {
  if (/screen|display|monitor/i.test(o.name)) {
    o.material = screen.material;
    o.name = 'screen';
    screen.visible = false; // hide overlay, use GLB mesh
  }
});
```

## Live tuning via window.__pc3d

```javascript
window.__pc3d = {
  model: pcModel, mon, kb, screen, enterKey, enterRing, camera,
  TUNE: {
    fitHeight: 3.4,           // world height to scale model to
    pos: { x: 0, y: 0, z: 0 },
    rotY: 0,
    cam: { x: 2.8, y: 1.95, z: 8.0 },
    look: { x: 0, y: 1.15, z: 0.1 },
    screen: { x: 0, y: 1.75, z: 0.55, w: 3.3, h: 2.2 },
    enter: { x: 0.55, y: 0.5, z: 1.5 },
  },
  apply: () => {
    fitModel(pcModel);
    placeScreen(screen, TUNE.screen);
    enterKey.position.set(TUNE.enter.x, TUNE.enter.y, TUNE.enter.z);
    enterRing.position.copy(enterKey.position);
    camera.position.set(TUNE.cam.x, TUNE.cam.y, TUNE.cam.z);
    camera.lookAt(TUNE.look.x, TUNE.look.y, TUNE.look.z);
  },
};
// In browser console: __pc3d.TUNE.cam.z = 9.0; __pc3d.apply();
```

## Git: exclude large source GLBs

```bash
# After optimization, remove originals before commit
git reset HEAD public/models/base_basic_pbr.glb public/models/base_basic_shaded.glb
rm public/models/base_basic_*.glb
# Only optimized version stays
git add public/models/pc.glb
```

## Merge conflict when remote advanced

Pattern: remote has NEW improvements while you worked locally.
```bash
git pull --no-rebase origin main    # let git create merge conflict
git checkout --theirs <file>        # accept remote (better base)
# Then re-apply local changes via Claude Code on top
```

## Key Three.js CDN imports for GLB + DRACO

```javascript
import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.183.2/build/three.module.js';
import { GLTFLoader } from 'https://cdn.jsdelivr.net/npm/three@0.183.2/examples/jsm/loaders/GLTFLoader.js';
import { DRACOLoader } from 'https://cdn.jsdelivr.net/npm/three@0.183.2/examples/jsm/loaders/DRACOLoader.js';

const draco = new DRACOLoader();
draco.setDecoderPath('https://cdn.jsdelivr.net/npm/three@0.183.2/examples/jsm/libs/draco/');
const gltfLoader = new GLTFLoader();
gltfLoader.setDRACOLoader(draco);
```

Note: DRACO path MUST end with `/`. Without trailing slash, WASM files won't resolve.
