import urllib.request
with urllib.request.urlopen('https://raw.githubusercontent.com/ismailseckin/seckin-servis-app/main/index.html') as response:
   html = response.read().decode('utf-8')
with open('claude_index.html', 'w', encoding='utf-8') as f:
   f.write(html)
print("done")
