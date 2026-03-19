#!/usr/bin/env python3
"""
Generates a Todoroki-style cursor (ice/fire gradient arrow).
Run: pip install Pillow && python scripts/generate_cursor.py

Output: cursor/default.png
Also updates webmods/cursor.css with embedded base64 data URL.
"""
import os
import base64

try:
    from PIL import Image, ImageDraw
except ImportError:
    print("Install Pillow: pip install Pillow")
    exit(1)

SIZE = 32
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "cursor")
WEBMODS_DIR = os.path.join(os.path.dirname(__file__), "..", "webmods")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Todoroki colors
ICE = (79, 195, 247)
FIRE = (255, 87, 34)

img = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
pixels = img.load()

# Draw arrow: diagonal ice-to-fire gradient
# Arrow shape: thick line from (2,2) to (28,28) with arrowhead at (28,28)
for y in range(SIZE):
    for x in range(SIZE):
        # Arrow shaft (diagonal band)
        dist = abs((x - y) - 0)
        if dist <= 3 and 4 <= x <= 26 and 4 <= y <= 26:
            t = (x + y) / 52  # 0 to 1 along diagonal
            t = max(0, min(1, t))
            r = int(ICE[0] + (FIRE[0] - ICE[0]) * t)
            g = int(ICE[1] + (FIRE[1] - ICE[1]) * t)
            b = int(ICE[2] + (FIRE[2] - ICE[2]) * t)
            pixels[x, y] = (r, g, b, 255)
        # Arrowhead (triangle at bottom-right)
        elif x >= 20 and y >= 20 and (x - 20) + (y - 20) <= 14:
            t = ((x - 20) + (y - 20)) / 14
            r = int(ICE[0] + (FIRE[0] - ICE[0]) * t)
            g = int(ICE[1] + (FIRE[1] - ICE[1]) * t)
            b = int(ICE[2] + (FIRE[2] - ICE[2]) * t)
            pixels[x, y] = (r, g, b, 255)

path = os.path.join(OUTPUT_DIR, "default.png")
img.save(path)
print(f"Created: {path}")

# Generate base64 and update cursor.css
with open(path, "rb") as f:
    data_url = "data:image/png;base64," + base64.b64encode(f.read()).decode()

cursor_css = f'''/* Shouto Todoroki Rising — Custom cursor (ice/fire gradient arrow) */

html,
body {{
  cursor: url("{data_url}") 0 0, auto !important;
}}

a,
button,
[role="button"],
input[type="submit"],
input[type="button"],
[onclick] {{
  cursor: url("{data_url}") 0 0, pointer !important;
}}
'''

css_path = os.path.join(WEBMODS_DIR, "cursor.css")
with open(css_path, "w") as f:
    f.write(cursor_css)
print(f"Updated: {css_path}")
