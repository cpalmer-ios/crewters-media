#!/usr/bin/env python3
"""Rebuild root manifest.json from london/venues/*.{webp,jpg} — no Places API."""

from __future__ import annotations

import datetime
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENUES = ROOT / "london" / "venues"
CDN_BASE = (
    "https://cdn.jsdelivr.net/gh/cpalmer-ios/crewters-media@main/london/venues"
)
EXTENSIONS = (".webp", ".jpg", ".jpeg", ".png")


def main() -> None:
    files = sorted(
        path
        for path in VENUES.iterdir()
        if path.is_file() and path.suffix.lower() in EXTENSIONS
    )
    # Prefer webp when both exist for the same handle
    by_handle: dict[str, Path] = {}
    for path in files:
        handle = path.stem
        prev = by_handle.get(handle)
        if prev is None or path.suffix.lower() == ".webp":
            by_handle[handle] = path

    photos = {
        handle: f"{CDN_BASE}/{path.name}"
        for handle, path in sorted(by_handle.items())
    }
    manifest = {
        "generatedAt": datetime.datetime.now(datetime.timezone.utc).strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        ),
        "cdnBase": CDN_BASE,
        "city": "london",
        "format": "webp",
        "count": len(photos),
        "photos": photos,
    }
    out = ROOT / "manifest.json"
    out.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out} ({len(photos)} photos)")


if __name__ == "__main__":
    main()
