# Google Drive batch download

## Install gdown
```bash
pip install gdown
```

## Download a folder
```bash
gdown --folder "https://drive.google.com/drive/folders/<FOLDER_ID>" -O /tmp/output-dir/
```

Files arrive in a nested structure: `/tmp/output-dir/<Folder Name>/<files>`. Navigate with `find /tmp/output-dir -type f`.

## Download a single file
```bash
gdown "https://drive.google.com/uc?id=<FILE_ID>" -O /tmp/output.ext
```

## Common pitfalls
- Large folders (100MB+) take time — use `timeout=120` or higher
- Files may be in subdirectories matching the Drive folder name (e.g., `Modified/`, `DEV-AI Projects/`)
- After download, copy needed files to project and DELETE originals that are too large for git (>10MB)
- GLB files >50MB: optimize BEFORE committing (DRACO, meshopt via gltf-transform)

## Optimizing GLB for web
```bash
npm install -g @gltf-transform/cli
gltf-transform draco input.glb output.glb    # DRACO compression
gltf-transform resize input.glb output.glb --width 1024 --height 1024  # texture resize
```

Target: <5MB for production, <15MB acceptable. Original 60MB GLB → 1.3MB after DRACO.
