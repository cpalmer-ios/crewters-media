#!/usr/bin/env python3
"""Rebuild root manifest.json from london/venues/*.jpg — no Places API."""

from __future__ import annotations

import datetime
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENUES = ROOT / "london" / "venues"
CDN_BASE = (
    "https://cdn.jsdelivr.net/gh/cpalmer-ios/crewters-media@main/london/venues"
)


def main() -> None:
    handles = sorted(
        path.stem for path in VENUES.glob("*.jpg") if path.is_file()
    )
    photos = {handle: f"{CDN_BASE}/{handle}.jpg" for handle in handles}
    manifest = {
        "generatedAt": datetime.datetime.now(datetime.timezone.utc).strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        ),
        "cdnBase": CDN_BASE,
        "city": "london",
        "count": len(photos),
        "photos": photos,
    }
    out = ROOT / "manifest.json"
    out.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out} ({len(photos)} photos)")


if __name__ == "__main__":
    main()
