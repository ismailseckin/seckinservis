import urllib.request
import os
import ssl

# Bypass SSL certificates
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

logos = {
    "ref-habas.png": "https://www.habas.com.tr/Content/images/uploads/F300/e0dfec77-af46-499d-a064-6f2783d1f4be_habas--logo.png",
    "ref-bisan.png": "https://www.bisan.com.tr/cdn/shop/files/bisan-400x100-white.png?v=1718739293&width=400",
    "ref-ustunkarli.png": "https://ustunkarli.com/wp-content/uploads/logo_1_LOGO.png",
    "ref-gage.png": "https://static.wixstatic.com/media/285971_60e3d97ca36f4956ac28a2b14fa8868e~mv2.png/v1/fill/w_268,h_268,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/285971_60e3d97ca36f4956ac28a2b14fa8868e~mv2.png",
    "ref-inan.png": "https://www.inancelik.com.tr/site/o/107555/2026/02/logo-band-colored-2x.png",
    "ref-cemer.png": "https://www.cemer.com.tr/assets/img/logo.png",
    "ref-endosa.png": "https://endosa.com.tr/wp-content/uploads/2019/04/endosa-logo.png",
    "ref-kavurlar.png": "https://www.kavurlar.com.tr/assets/front/style/assets/logo.png",
    "ref-merka.png": "https://merkamakina.com/wp-content/uploads/2021/05/merka-logo.png"
}

# Use absolute path to avoid any confusion
base_dir = r"c:\Users\USER\.gemini\antigravity\scratch\seckin-servis"
dest_dir = os.path.join(base_dir, "assets", "logos")

print(f"Ensuring directory exists: {dest_dir}")
os.makedirs(dest_dir, exist_ok=True)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

for filename, url in logos.items():
    file_path = os.path.join(dest_dir, filename)
    print(f"Downloading {filename} from {url}...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=20) as response:
            with open(file_path, 'wb') as f:
                f.write(response.read())
        print(f"Success: {filename}")
    except Exception as e:
        print(f"Error downloading {filename}: {e}")

# Verify
print("\nResults in assets/logos:")
if os.path.exists(dest_dir):
    for f in os.listdir(dest_dir):
        print(f"- {f}")
else:
    print("Error: Directory still does not exist!")
