# Interface Mods — Implementation Guide

Scaffolding for all Opera GX Interface categories. Add assets and merge into `manifest.json` when ready.

## Status

| Category | Status | Notes |
|----------|--------|------|
| **Wallpaper** | ✅ Done | `wallpaper/dark.png` |
| **Theme** | ✅ Done | Ice/fire HSL in manifest |
| **App Icon** | ✅ Done | `icon_512.png` (512×512) |
| **Fonts** | 📁 Scaffold | Add `fonts/todoroki.ttf`, merge from manifest.interface-extras.json |
| **Game Strips** | 📁 Scaffold | Structure TBD — check GX Store mods |
| **Stickers** | 📁 Scaffold | Structure TBD — check GX Store mods |
| **Icons** | 📁 Scaffold | Browser UI icons — `browser_icons/` |
| **Splash Screen** | 📁 Scaffold | Add `splash/todoroki.mp4` (1080×1080, ~5s, H.264) |
| **Cursors** | ✅ Web / 📁 Native | Web: `webmods/cursor.css`. Native: convert PNG→CUR, add to manifest |

## Enabling Extras

1. Set `"schema_version": 2` in the `mod` section (already in manifest).
2. Copy payload entries from `manifest.interface-extras.json` into `manifest.json` → `payload`.
3. Add the corresponding asset files.

## Asset Specs

- **Fonts:** TTF or WOFF. Download from [Google Fonts](https://fonts.google.com).
- **Splash:** MP4, 1080×1080, ~5 seconds, H.264 + AAC.
- **Cursors (native):** .CUR or .ANI. Convert PNG with [Convertio](https://convertio.co/png-cur/).
- **App icon (Mods 2.0):** 290×290 PNG for `app_icon` payload.
