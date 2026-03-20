# Web modding (schema 1)

This mod uses **`mod.payload.page_styles`** only — no Mods 2.0 / schema 2 interface fields.

- **CSS:** `webmodding/*.css` (see `manifest.json` → `page_styles`).
- **Shared variables:** `webmodding/theme.css` (optional include per site).
- **Opera pages:** `webmodding/opera.css` matches `https://*.opera.com/*` — useful to confirm injection is working before debugging YouTube/GitHub.

Regenerate the in-page cursor after changing the PNG: `python scripts/generate_cursor.py`.
