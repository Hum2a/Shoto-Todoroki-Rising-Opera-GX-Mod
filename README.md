# Shouto Todoroki Rising — Opera GX Mod

A true homage to Shouto Todoroki from My Hero Academia. Half ice, half fire — Plus Ultra.

Transform your Opera GX browser with a complete ice-and-fire aesthetic inspired by Todoroki's dual Quirk. Theme colors, wallpapers, web styling, and custom cursors bring the duality of ice and flame to every corner of your browsing experience.

---

## What This Mod Does

### Included (Ready to Use)

| Feature | Description |
|---------|-------------|
| **Theme** | Ice blue accent (`gx_accent`) with fire red secondary (`gx_secondary_base`) for tabs, sidebars, and UI highlights. Supports both dark and light mode. |
| **Wallpaper** | Static ice-to-fire gradient background (`wallpaper/dark.png`) with matching text colors for the speed dial. |
| **Webmods** | Site-specific styling on 12 popular sites. List items, cards, and nav elements alternate ice (odd) and fire (even) — a 50/50 split that mirrors Todoroki's duality. |
| **Custom Cursor** | Ice/fire gradient arrow cursor on all webmod sites (YouTube, GitHub, Google, Reddit, X, Wikipedia, Stack Overflow, Twitch, Discord, Amazon, Spotify, LinkedIn). |

### Webmod Sites

Each site gets the Todoroki treatment: icy blue and fiery red accents, left borders, gradient backgrounds, and alternating colors on lists and cards.

- **YouTube** — Video grid, sidebar, chips, comments
- **GitHub** — Repo rows, file lists, issues, pinned repos
- **Google** — Search results, nav links, footer
- **Reddit** — Posts, comments, subreddit links
- **X (Twitter)** — Tweets, timeline, sidebar
- **Wikipedia** — Search results, TOC, sidebar nav
- **Stack Overflow** — Questions, answers, tags
- **Twitch** — Stream cards, sidebar, "Live" badges
- **Discord** — Channels, messages, server list
- **Amazon** — Product cards, nav, search
- **Spotify** — Playlists, tracks, sidebar
- **LinkedIn** — Feed, connections, buttons

### Optional (Add Your Own Assets)

| Feature | Status | How to Add |
|---------|--------|------------|
| **Background Music** | Scaffold | Add `music/track_1.mp3`–`track_4.mp3`, merge payload from `manifest.with-sounds.json` |
| **Browser Sounds** | Scaffold | Add `sound/*.mp3` (clicks, hovers, tabs), run `generate_placeholder_sounds.py` for WAV placeholders |
| **Keyboard Sounds** | Scaffold | Add `keyboard/*.wav` (typing, backspace, enter, space) |
| **Fonts** | Scaffold | `python scripts/download_font.py` for Bebas Neue, merge `fonts` from `manifest.interface-extras.json` |
| **Splash Screen** | Scaffold | Add `splash/todoroki.mp4` (1080×1080, ~5s), merge `splash_screen` |
| **Native Cursor** | Scaffold | `python scripts/generate_cursor.py` creates `.cur`; requires schema 2 (see note below) |
| **App Icon** | Scaffold | `app_icon_290.png` for Mods 2.0; requires schema 2 |
| **Stickers / Game Strips / Icons** | Scaffold | Structure TBD; see `INTERFACE.md` |

### Schema 2 Note

Native cursor, fonts, app icon, and splash screen require `schema_version: 2`. Opera's schema 2 validation is undocumented and inconsistent (errors like "body or header required," "items field," etc.). This mod uses **schema 1** for reliable loading. The web cursor still works on all webmod sites; only the browser-wide cursor (tabs, address bar) is affected.

---

## Project Structure

```
Shouto Todoroki Rising/
├── manifest.json              # Mod configuration (schema 1)
├── manifest.interface-extras.json  # Optional: fonts, splash, cursors, app_icon (schema 2)
├── INTERFACE.md                # Guide for all Interface mod categories
├── icon_512.png                # Mod icon (512×512)
├── app_icon_290.png            # App icon for Mods 2.0 (290×290)
├── license.txt
├── fonts/                      # Custom fonts (add .ttf)
├── splash/                     # Splash screen video (add .mp4)
├── cursor/                     # Native cursor (.cur) + web cursor (in webmods)
├── stickers/                   # Decorative stickers
├── game_strips/                # Game strip assets
├── browser_icons/              # Browser UI icons
├── webmods/                    # Site-specific CSS + cursor.css
├── wallpaper/
│   ├── dark.png                # Static wallpaper
│   ├── video.webm              # Animated (optional)
│   ├── first_frame.jpeg        # Video thumbnail
│   └── wallpaper_generator.html # Open in browser to record
├── music/                      # track_1.mp3, track_2.mp3, etc.
├── sound/                      # Browser sound effects
├── keyboard/                   # Typing sounds (.wav)
└── scripts/
    ├── generate_wallpaper.py   # Creates wallpaper/dark.png
    ├── generate_icon.py        # Creates icon_512.png, app_icon_290.png
    ├── generate_cursor.py      # Creates cursor/default.png + .cur, updates cursor.css
    ├── generate_placeholder_sounds.py  # WAV placeholders for sound/
    └── download_font.py        # Downloads Bebas Neue to fonts/
```

---

## Setup

### 1. Generate Required Assets

```bash
pip install Pillow
python scripts/generate_wallpaper.py   # Creates wallpaper/dark.png
python scripts/generate_icon.py        # Creates icon_512.png, app_icon_290.png
python scripts/generate_cursor.py     # Creates cursor assets + webmods/cursor.css
```

### 2. Create Animated Wallpaper (Optional)

1. Open `wallpaper/wallpaper_generator.html` in Chrome
2. Resize to 1920×1080 (or use DevTools device mode)
3. Record with OBS or similar as WebM
4. Save as `wallpaper/video.webm`
5. Update `manifest.json` light wallpaper to use `"image": "wallpaper/video.webm"` and add `"first_frame": "wallpaper/first_frame.jpeg"`

### 3. Add Sounds & Music (Optional)

1. **Generate placeholders**: `python scripts/generate_placeholder_sounds.py`
2. **Convert to MP3** (requires [ffmpeg](https://ffmpeg.org)):
   ```bash
   for f in sound/*.wav; do ffmpeg -i "$f" -y "${f%.wav}.mp3"; done
   for f in music/*.wav; do ffmpeg -i "$f" -y "${f%.wav}.mp3"; done
   ```
3. Merge the `manifest.with-sounds.json` payload into `manifest.json`

**Sound ideas**: Ice crackle for clicks, flame whoosh for hovers, orchestral stabs for important actions.

### 4. Install the Mod

1. Zip the entire folder (**manifest.json must be at root**)
2. In Opera GX: **Easy Setup** → **Mods** → **Load mod** → select your zip

Or load unpacked: `opera://extensions` → Developer mode → **Load unpacked** → select the mod folder.

---

## Color Palette

| Element | Color | HSL |
|---------|-------|-----|
| Accent (gx_accent) | Icy blue | `h: 199, s: 89, l: 62` |
| Secondary (gx_secondary_base) | Fire red | `h: 14, s: 91, l: 16` |

**Webmods** use `:nth-child(odd)` for icy blue and `:nth-child(even)` for fiery red — an even 50/50 split across list items, cards, and navigation elements.

---

## License

Fan-made tribute. My Hero Academia © Kohei Horikoshi / Shueisha.
