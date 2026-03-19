# Shouto Todoroki Rising — Opera GX Mod

A true homage to Shouto Todoroki from My Hero Academia. Half ice, half fire — Plus Ultra.

## Features

- **Ice-Fire Theme**: Accent colors use icy blue (#4FC3F7) with fiery red secondary backgrounds
- **Custom cursor**: Ice/fire themed cursor on all webmod sites
- **Webmods**: Site-specific styling for 12 sites — YouTube, GitHub, Google, Reddit, X, Wikipedia, Stack Overflow, Twitch, Discord, Amazon, Spotify, LinkedIn — alternating ice/fire (odd = icy blue, even = fiery red)
- **Animated Wallpaper**: Ice/fire gradient animation (video + static fallback)
- **Background Music**: 4 slots for epic MHA-style tracks
- **Browser Sounds**: Full set of custom sounds (clicks, hovers, tabs, switches)
- **Keyboard Sounds**: Typing sounds for that satisfying feel

## Project Structure

```
Shouto Todoroki Rising/
├── manifest.json          # Mod configuration
├── manifest.interface-extras.json  # Optional: fonts, splash, cursors, app_icon
├── INTERFACE.md           # Guide for all Interface mod categories
├── icon_512.png           # Mod icon (512×512)
├── app_icon_290.png       # App icon for Mods 2.0 (290×290)
├── license.txt
├── fonts/                 # Custom fonts (add .ttf, merge from manifest.interface-extras)
├── splash/                # Splash screen video (add .mp4)
├── cursor/                # Native cursor (.cur) + web cursor (in webmods)
├── stickers/              # Decorative stickers
├── game_strips/           # Game strip assets
├── browser_icons/         # Browser UI icons
├── webmods/               # Site-specific CSS (YouTube, GitHub, etc.)
├── wallpaper/
│   ├── dark.png         # Static wallpaper (dark mode)
│   ├── video.webm       # Animated wallpaper (light mode)
│   ├── first_frame.jpeg # Video thumbnail
│   └── wallpaper_generator.html  # Open in browser to record
├── music/               # track_1.mp3, track_2.mp3, etc.
├── sound/               # Browser sound effects
├── keyboard/            # Typing sounds (.wav)
└── scripts/
    └── generate_wallpaper.py
```

## Setup

### 1. Generate Wallpaper Images

```bash
pip install Pillow
python scripts/generate_wallpaper.py
```

This creates `wallpaper/dark.png` and `wallpaper/first_frame.jpeg`.

### 2. Create Animated Wallpaper (Optional)

For an animated ice/fire wallpaper in light mode:
1. Open `wallpaper/wallpaper_generator.html` in Chrome
2. Resize window to 1920×1080 (or use DevTools device mode)
3. Record with OBS or similar as WebM
4. Save as `wallpaper/video.webm`
5. Update `manifest.json` light wallpaper to use `"image": "wallpaper/video.webm"` and add `"first_frame": "wallpaper/first_frame.jpeg"`

### 3. Add Sounds & Music (Optional)

The mod works out of the box with theme, wallpaper, and webmods. To add sounds:

1. **Generate placeholders** (WAV): `python scripts/generate_placeholder_sounds.py`
2. **Convert to MP3** (requires [ffmpeg](https://ffmpeg.org)):
   ```bash
   for f in sound/*.wav; do ffmpeg -i "$f" -y "${f%.wav}.mp3"; done
   for f in music/*.wav; do ffmpeg -i "$f" -y "${f%.wav}.mp3"; done
   ```
3. **Merge** the `manifest.with-sounds.json` payload into `manifest.json`

| Asset | Format | Notes |
|-------|--------|-------|
| `icon_512.png` | PNG | 512×512 (run `python scripts/generate_icon.py`) |
| `music/track_*.mp3` | MP3 | Background music — MHA OST style |
| `sound/*.mp3` | MP3 | Clicks, hovers, tabs, switches |
| `keyboard/*.wav` | WAV | Typing sounds |

**Sound ideas**: Ice crackle for clicks, flame whoosh for hovers, orchestral stabs for important actions.

### 4. Optional Interface Extras

| Asset | Command / Action |
|-------|------------------|
| **Font** | `python scripts/download_font.py` then merge `fonts` from manifest.interface-extras.json |
| **Splash** | Add `splash/todoroki.mp4` (1080×1080, ~5s), merge `splash_screen` |
| **Native cursor** | Convert `cursor/default.png` to .cur, merge `cursors` |

See `INTERFACE.md` for full guide.

### 5. Install the Mod

1. Zip the entire folder (manifest.json must be at root)
2. In Opera GX: **Easy Setup** → **Mods** → **Load mod** → select your zip

## Color Palette

| Element | Color | HSL |
|---------|-------|-----|
| Accent (gx_accent) | Icy blue | `h: 199, s: 89, l: 62` |
| Secondary (gx_secondary_base) | Fire red | `h: 14, s: 91, l: 16` |

**Webmods** use `:nth-child(odd)` for icy blue and `:nth-child(even)` for fiery red — an even 50/50 split across list items, cards, and navigation elements.

## License

Fan-made tribute. My Hero Academia © Kohei Horikoshi / Shueisha.
