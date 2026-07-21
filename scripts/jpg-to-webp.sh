#!/usr/bin/env bash
# Convert london/venues/*.jpg → *.webp (q=80), drop JPG, rebuild manifest.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
VENUES="$ROOT/london/venues"
cd "$VENUES"
shopt -s nullglob
jpgs=(*.jpg)
if ((${#jpgs[@]} == 0)); then
  echo "No JPGs to convert in $VENUES"
else
  for f in "${jpgs[@]}"; do
    cwebp -quiet -q 80 "$f" -o "${f%.jpg}.webp"
    rm -f "$f"
  done
  echo "Converted ${#jpgs[@]} JPG → WebP"
fi
python3 "$ROOT/scripts/rebuild-manifest.py"
