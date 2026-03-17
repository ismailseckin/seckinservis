import shutil
import os

source_dir = r"C:\Users\USER\.gemini\antigravity\brain\9f060131-156e-4007-9060-e98e63977942"
dest_dir = r"c:\Users\USER\.gemini\antigravity\scratch\seckin-servis\assets\logos"

mapping = {
    "media__1773757158092.png": "habas.png",
    "media__1773757158134.png": "gage.png",
    "media__1773757158037.jpg": "bisan.jpg",
    "media__1773757646874.jpg": "ustunkarli.jpg",
    "media__1773757993065.jpg": "inancelik.jpg",
    "media__1773757158108.png": "cemer.png",
    "media__1773757158155.png": "endosa.png",
    "media__1773758199275.jpg": "kavurlar.jpg",
    "media__1773758210302.jpg": "merka.jpg"
}

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

for src_name, dest_name in mapping.items():
    src_path = os.path.join(source_dir, src_name)
    dest_path = os.path.join(dest_dir, dest_name)
    try:
        shutil.copy2(src_path, dest_path)
        print(f"Copied {src_name} to {dest_name}")
    except Exception as e:
        print(f"Failed to copy {src_name}: {e}")

print("\nFiles in dest:")
print(os.listdir(dest_dir))
