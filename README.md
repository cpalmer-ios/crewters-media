# crewters-media

Shared static media for **Crewters website** and **iOS** (and any other client).

Hosted via GitHub + [jsDelivr](https://www.jsdelivr.com/) CDN. No Places API in this repo.

## Why public?

jsDelivr’s free `gh/` CDN only serves **public** GitHub repos. Venue exterior / facility photos used for discovery are fine to ship publicly.

## Layout

```text
london/venues/{handle}.jpg   # one city, flat by venue handle
manifest.json                # handle → CDN URL map
```

Future cities: `manchester/venues/…`, etc. Borough subfolders are optional later when we have a stable borough→venue map.

## CDN URLs

```text
https://cdn.jsdelivr.net/gh/cpalmer-ios/crewters-media@main/london/venues/{handle}.jpg
```

Pin a commit SHA instead of `@main` in production if you need immutable cache:

```text
https://cdn.jsdelivr.net/gh/cpalmer-ios/crewters-media@{sha}/london/venues/{handle}.jpg
```

After pushing new photos, purge once if needed:

```text
https://purge.jsdelivr.net/gh/cpalmer-ios/crewters-media@main/london/venues/{handle}.jpg
```

## Website

`crewters-web` reads `lib/venues/photo-manifest.json` (synced from this repo’s `manifest.json`) and prefers CDN URLs over API `pp` hotlinks.

## iOS

Use the same CDN URL as `UIImage` / Nuke / Kingfisher source. Example:

```swift
let url = URL(string:
  "https://cdn.jsdelivr.net/gh/cpalmer-ios/crewters-media@main/london/venues/\(handle).jpg"
)
```

Or ship / fetch `manifest.json` from the same CDN:

```text
https://cdn.jsdelivr.net/gh/cpalmer-ios/crewters-media@main/manifest.json
```

Do **not** call Google Places Photo Media for bulk venue imagery.

## Adding photos

1. Drop JPEGs under `london/venues/{handle}.jpg` (handle = Crewters venue handle).
2. Regenerate `manifest.json` (see script note below or run the website sync helper).
3. Commit + push to `main`.
4. Update website manifest copy if it vendors the JSON.

## Linear

CRWTRS-213
