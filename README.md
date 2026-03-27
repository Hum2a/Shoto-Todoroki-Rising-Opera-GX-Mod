# Shouto Todoroki Rising — Opera GX Mod (schema 1)

Ice/fire theme, wallpaper, background music, and **web modding** via `page_styles` using the **bucket layout** (global sheet + `sites-01` … `sites-06`), aligned with **Great Glacial Aegir**, Ochaco, and Hagakure mods.

## Web modding (bucket layout)

| File | Role |
|------|------|
| `webmodding/shoto-rising.css` | All pages: links, selection, scrollbars, ice + ember mist |
| `webmodding/sites-01-google-youtube.css` | Google suite + YouTube |
| `webmodding/sites-02-social.css` | Reddit, X, Facebook, Instagram, TikTok, Discord, Pinterest, Tumblr, LinkedIn, Threads |
| `webmodding/sites-03-dev.css` | GitHub, GitLab, Stack Overflow / Exchange, Hacker News |
| `webmodding/sites-04-shopping.css` | Amazon regions, eBay, PayPal, Apple |
| `webmodding/sites-05-media.css` | Netflix, Spotify, Twitch, BBC, CNN, IMDb, Medium |
| `webmodding/sites-06-productivity.css` | Wikipedia, Notion, Dropbox, Microsoft / Outlook / Yahoo, Steam, Craigslist, Indeed |

Reload the mod in **opera://extensions** after edits. Enable **web modding** for this mod under **Mods**.

**Optional cursor:** `python scripts/generate_cursor.py` writes `webmodding/cursor-optional.css`. Add it to `page_styles` in `manifest.json` only if you want the data-URL ice/fire arrow everywhere.

### Webmodding works in Izuku but not Shouto?

Opera applies **page styles per mod**. Select **Shouto Todoroki Rising** and turn on website / web modding. Disable other mods while testing if your build only injects one mod’s styles.

Background music: `music/Todorokis_Counterattack.mp3` (no spaces in filename).

**Settings vs Mods:** After `manifest.json` changes, remove and **Load unpacked** again, then open a **new** tab.

## Project layout

```
Shouto Todoroki Rising/
├── manifest.json
├── license.txt
├── icon_512.png
├── webmodding/
├── wallpaper/
├── music/
└── scripts/
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
