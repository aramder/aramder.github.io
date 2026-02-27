"""Quick helper to extract crop candidates and create an HTML preview."""
import os
import io
import base64
from PIL import Image

temp = os.environ["TEMP"]
img = Image.open(os.path.join(temp, "tripod_frame.png"))

# Try several crop regions (x1, y1, x2, y2) on the 1080x1920 portrait frame
regions = {
    "center": (280, 372, 1080, 1072),
    "center_lower": (140, 860, 940, 1460),
    "lower_third": (100, 1000, 980, 1600),
    "tight_label": (150, 750, 900, 1300),
}

html = '<html><body style="background:#222; color:white; font-family:monospace">'
html += "<h2>Full Frame (1080x1920)</h2>"

# Full frame thumbnail
thumb = img.copy()
thumb.thumbnail((300, 533))
buf = io.BytesIO()
thumb.save(buf, "PNG")
b64 = base64.b64encode(buf.getvalue()).decode()
html += f'<img src="data:image/png;base64,{b64}" style="border:1px solid white"><br><br>'

html += '<h2>Crop Candidates (click to zoom)</h2><div style="display:flex;gap:20px;flex-wrap:wrap">'

for name, box in regions.items():
    crop = img.crop(box)
    w, h = crop.size
    buf2 = io.BytesIO()
    crop.save(buf2, "PNG")
    b2 = base64.b64encode(buf2.getvalue()).decode()
    html += (
        f'<div><h3>{name}<br><small>{box} → {w}x{h}</small></h3>'
        f'<img src="data:image/png;base64,{b2}" style="border:1px solid yellow;max-height:400px"></div>'
    )

html += "</div></body></html>"

out = os.path.join(temp, "crop_preview.html")
with open(out, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Preview saved to: {out}")
