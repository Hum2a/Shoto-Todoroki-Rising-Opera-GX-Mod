#!/usr/bin/env python3
"""
Generates the mod icon (512x512) with Todoroki's ice/fire split.
Run: python scripts/generate_icon.py
"""
import os

try:
    from PIL import Image, ImageDraw
except ImportError:
    print("Install Pillow: pip install Pillow")
    exit(1)

SIZE = 512
OUTPUT = os.path.join(os.path.dirname(__file__), "..", "icon_512.png")
# For app_icon (Mods 2.0): 290×290 recommended
APP_ICON_SIZE = 290
APP_ICON_OUTPUT = os.path.join(os.path.dirname(__file__), "..", "app_icon_290.png")

img = Image.new("RGB", (SIZE, SIZE))
draw = ImageDraw.Draw(img)

# Left half: icy blue | Right half: fire red
for x in range(SIZE):
    if x < SIZE // 2:
        color = (79, 195, 247)   # Ice blue
    else:
        color = (255, 87, 34)     # Fire red
    draw.line([(x, 0), (x, SIZE)], fill=color)

# Add a subtle center line (Todoroki's split)
draw.line([(SIZE//2 - 1, 0), (SIZE//2 - 1, SIZE)], fill=(255, 255, 255, 128))
draw.line([(SIZE//2, 0), (SIZE//2, SIZE)], fill=(255, 255, 255, 128))
draw.line([(SIZE//2 + 1, 0), (SIZE//2 + 1, SIZE)], fill=(255, 255, 255, 128))

img.save(OUTPUT)
print(f"Created: {OUTPUT}")

# Also create 290×290 for app_icon (Mods 2.0)
img_small = img.resize((APP_ICON_SIZE, APP_ICON_SIZE), Image.Resampling.LANCZOS)
img_small.save(APP_ICON_OUTPUT)
print(f"Created: {APP_ICON_OUTPUT} (for app_icon payload)")
