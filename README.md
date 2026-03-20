# Shouto Todoroki Rising — Opera GX Mod (schema 1)

Ice/fire theme, wallpaper, background music, and **web modding** via `page_styles` only.

## Web modding

| Path | Role |
|------|------|
| `webmodding/theme.css` | Shared CSS variables |
| `webmodding/opera.css` | Opera sites (`*.opera.com`) — quick injection check |
| `webmodding/cursor.css` | Custom cursor on modded sites |
| `webmodding/<site>.css` | Per-site styling |

After editing CSS, reload the mod (unpacked folder or new zip) in **opera://extensions**.

### Webmodding works in Izuku but not Shouto?

Opera GX applies **page styles per mod**. Open **Mods** (or Easy Setup → Mods), select **Shouto Todoroki Rising**, and ensure **website / web modding / web design** (wording varies by version) is **turned on** for that mod. If only wallpaper or theme is enabled, YouTube and GitHub stay default.

Also **disable or remove Izuku** while testing Shouto—some builds only inject one mod’s page styles at a time.

Background music file has no spaces: `music/Todorokis_Counterattack.mp3` (spaces in paths can break loaders).

**Settings vs Mods:** There are two places that mention web modding (Settings search and **Mods → Effects → Web modding**). Both need to allow it. After changing `manifest.json`, remove the mod in **opera://extensions** and **Load unpacked** again, then open a **new** tab (not an old pinned YouTube tab).

## Project layout

```
Shouto Todoroki Rising/
├── manifest.json       # schema_version 1, payload.page_styles only for the web
├── license.txt
├── icon_512.png
├── webmodding/
├── wallpaper/
├── music/
└── scripts/            # generate_wallpaper.py, generate_icon.py, generate_cursor.py, …
```

## Scripts

```bash
pip install Pillow
python scripts/generate_wallpaper.py
python scripts/generate_icon.py
python scripts/generate_cursor.py
```

## License

Fan-made tribute. My Hero Academia © Kohei Horikoshi / Shueisha.
