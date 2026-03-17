import base64
import os
import json

source_dir = r"C:\Users\USER\.gemini\antigravity\brain\9f060131-156e-4007-9060-e98e63977942"
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

data_uris = {}

for key, filename in mapping.items():
    path = os.path.join(source_dir, filename)
    if os.path.exists(path):
        ext = filename.split('.')[-1]
        mime = f"image/{ext}"
        if ext == "jpg": mime = "image/jpeg"
        with open(path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode('utf-8')
            data_uris[key] = f"data:{mime};base64,{encoded}"
    else:
        print(f"Missing: {path}")

with open("logos_data.json", "w") as f:
    json.dump(data_uris, f)

print("SUCCESS: Logolar JSON formatına dönüştürüldü.")
