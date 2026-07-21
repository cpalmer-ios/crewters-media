# crewters-media

Shared static media for **Crewters website** and **iOS** (and any other client).

Hosted via GitHub + [jsDelivr](https://www.jsdelivr.com/) CDN. No Places API in this repo.

## Why public?

jsDelivr’s free `gh/` CDN only serves **public** GitHub repos. Venue exterior / facility photos used for discovery are fine to ship publicly.

## Layout

```text
london/venues/{handle}.webp   # WebP q≈80 (preferred)
manifest.json                 # handle → CDN URL map
```

Future cities: `manchester/venues/…`, etc. Borough subfolders are optional later when we have a stable borough→venue map.

## CDN URLs

```text
https://cdn.jsdelivr.net/gh/cpalmer-ios/crewters-media@main/london/venues/{handle}.webp
```

Pin a commit SHA instead of `@main` in production if you need immutable cache:

```text
https://cdn.jsdelivr.net/gh/cpalmer-ios/crewters-media@{sha}/london/venues/{handle}.webp
```

After pushing new photos, purge once if needed:

```text
https://purge.jsdelivr.net/gh/cpalmer-ios/crewters-media@main/london/venues/{handle}.webp
```

## Website

`crewters-web` reads `lib/venues/photo-manifest.json` (synced from this repo’s `manifest.json`) and prefers CDN URLs over API `pp` hotlinks.

## iOS

Use the same CDN URL as `UIImage` / Nuke / Kingfisher source. Example:

```swift
let url = URL(string:
  "https://cdn.jsdelivr.net/gh/cpalmer-ios/crewters-media@main/london/venues/\(handle).webp"
)
```

Or ship / fetch `manifest.json` from the same CDN:

```text
https://cdn.jsdelivr.net/gh/cpalmer-ios/crewters-media@main/manifest.json
```

Do **not** call Google Places Photo Media for bulk venue imagery.

## Adding photos

1. Drop source images under `london/venues/` (JPG or WebP; handle = Crewters venue handle).
2. If JPG: `bash scripts/jpg-to-webp.sh` (cwebp q=80) — or run `python3 scripts/rebuild-manifest.py` if already WebP.
3. Commit + push to `main`.
4. Sync website `lib/venues/photo-manifest.json` from this repo’s `manifest.json`.

## Linear

CRWTRS-213
