#!/usr/bin/env python3
"""
Generates wallpaper images for the Shouto Todoroki mod.
Run: pip install Pillow && python scripts/generate_wallpaper.py
"""
import os

try:
    from PIL import Image
except ImportError:
    print("Install Pillow: pip install Pillow")
    exit(1)

WIDTH, HEIGHT = 1920, 1080
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "wallpaper")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Ice blue (left) to fire red (right) - Todoroki's signature gradient
img = Image.new("RGB", (WIDTH, HEIGHT))
pixels = img.load()

for x in range(WIDTH):
    t = x / WIDTH
    # Smooth gradient
    r = int(13 + (191 - 13) * t)   # 0D -> BF
    g = int(71 + (54 - 71) * t)    # 47 -> 36
    b = int(161 + (12 - 161) * t)  # A1 -> 0C
    for y in range(HEIGHT):
        pixels[x, y] = (r, g, b)

dark_path = os.path.join(OUTPUT_DIR, "dark.png")
img.save(dark_path)
print(f"Created: {dark_path}")

# First frame for video (same as dark for now)
first_frame = os.path.join(OUTPUT_DIR, "first_frame.jpeg")
img.save(first_frame, "JPEG", quality=90)
print(f"Created: {first_frame}")
