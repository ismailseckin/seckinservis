import base64
import os

brain_dir = r"C:\Users\USER\.gemini\antigravity\brain\9f060131-156e-4007-9060-e98e63977942"
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

css_content = "/* Embedded Logos */\n"

for key, brain_file in mapping.items():
    full_path = os.path.join(brain_dir, brain_file)
    if os.path.exists(full_path):
        ext = brain_file.split('.')[-1]
        mime = f"image/{ext}"
        if ext == "jpg": mime = "image/jpeg"
        with open(full_path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode('utf-8')
            css_content += f".ref-logo[data-brand='{key}'] img {{\n"
            css_content += f"  content: url('data:{mime};base64,{b64}');\n"
            css_content += "}\n"
    else:
        print(f"Missing: {full_path}")

with open("logos_embedded.css", "w", encoding="utf-8") as f:
    f.write(css_content)

print("DONE: logos_embedded.css created.")
