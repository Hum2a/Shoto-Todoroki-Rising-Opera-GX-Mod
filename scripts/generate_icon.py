#!/usr/bin/env python3
"""
Generates the mod icon (512x512) from todoroki.jpg.
Run: python scripts/generate_icon.py
"""
import os

try:
    from PIL import Image
except ImportError:
    print("Install Pillow: pip install Pillow")
    exit(1)

SIZE = 512
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.join(SCRIPT_DIR, "..")
SRC = os.path.join(PROJECT_ROOT, "todoroki.jpg")
OUTPUT = os.path.join(PROJECT_ROOT, "icon_512.png")

if not os.path.exists(SRC):
    print(f"Source image not found: {SRC}")
    exit(1)

src = Image.open(SRC).convert("RGBA")
W, H = src.size

# Crop 512x512 from bottom-center to capture Todoroki (character in lower third)
if W >= SIZE and H >= SIZE:
    left = max(0, (W - SIZE) // 2)
    top = max(0, H - SIZE)
    icon = src.crop((left, top, left + SIZE, top + SIZE))
else:
    scale = max(SIZE / W, SIZE / H)
    new_w, new_h = int(W * scale), int(H * scale)
    src = src.resize((new_w, new_h), Image.Resampling.LANCZOS)
    left = (new_w - SIZE) // 2
    top = max(0, new_h - SIZE)
    icon = src.crop((left, top, left + SIZE, min(top + SIZE, new_h)))
    if icon.size != (SIZE, SIZE):
        icon = icon.resize((SIZE, SIZE), Image.Resampling.LANCZOS)

icon.save(OUTPUT)
print(f"Created: {OUTPUT}")
