import urllib.request
url = 'https://raw.githubusercontent.com/ismailseckin/seckin-servis-app/main/index.html'
try:
    with urllib.request.urlopen(url) as response:
        html_content = response.read().decode('utf-8')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("DOWNLOAD_SUCCESS: index.html downloaded")
except Exception as e:
    print(f"DOWNLOAD_ERROR: {e}")
