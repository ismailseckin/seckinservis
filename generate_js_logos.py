import base64
import os

source_dir = r"C:\Users\USER\.gemini\antigravity\brain\9f060131-156e-4007-9060-e98e63977942"
dest_file = r"c:\Users\USER\.gemini\antigravity\scratch\seckin-servis\assets\logos\logo_data.js"

mapping = {
    "habas": "media__1773757158092.png",
    "gage": "media__1773757158134.png",
    "bisan": "media__1773757158037.jpg",
    "ustunkarli": "media__1773757646874.jpg",
    "inancelik": "media__1773757993065.jpg",
    "cemer": "media__1773757158108.png",
    "endosa": "media__1773757158155.png",
    "kavurlar": "media__1773758199275.jpg",
    "merka": "media__1773758210302.jpg"
}

logo_data = "const LOGO_DATA = {\n"

for key, filename in mapping.items():
    path = os.path.join(source_dir, filename)
    if os.path.exists(path):
        ext = filename.split('.')[-1]
        mime = f"image/{ext}"
        if ext == "jpg": mime = "image/jpeg"
        with open(path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode('utf-8')
            logo_data += f"  '{key}': 'data:{mime};base64,{encoded}',\n"
    else:
        print(f"Missing: {path}")

logo_data += "};"

with open(dest_file, "w", encoding="utf-8") as f:
    f.write(logo_data)

print(f"Successfully generated {dest_file}")
