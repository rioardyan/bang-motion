"""Lembar kontak: python3 -I tools/contact.py <keluaran.png> <kolom> <png> [<png> ...]
Judul tiap kotak = detik dari nama berkas (t7_40.png -> 7.40s)."""
import sys, re
from PIL import Image, ImageDraw, ImageFont
out, cols, *files = sys.argv[1:]
cols = int(cols)
TW = 360
th = None
tiles = []
for f in files:
    im = Image.open(f).convert('RGB')
    th = int(im.height * TW / im.width)
    tiles.append((f, im.resize((TW, th), Image.LANCZOS)))
rows = (len(tiles) + cols - 1) // cols
G = 8
sheet = Image.new('RGB', (cols * (TW + G) + G, rows * (th + G + 26) + G), (24, 24, 28))
d = ImageDraw.Draw(sheet)
try: font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 18)
except Exception: font = ImageFont.load_default()
for i, (f, im) in enumerate(tiles):
    x = G + (i % cols) * (TW + G); y = G + (i // cols) * (th + G + 26)
    m = re.search(r't(\d+)_(\d+)', f)
    d.text((x, y + 2), f"{m.group(1)}.{m.group(2)} dtk" if m else f, fill=(235, 235, 235), font=font)
    sheet.paste(im, (x, y + 26))
sheet.save(out)
print(out, sheet.size)
