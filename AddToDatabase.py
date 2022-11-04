import urllib.request, json
github_link = "https://BOBINYOURFLOP.github.io/Database.json"
with urllib.request.urlopen(github_link) as url: 
   json_data = json.loads(url.read().decode())
print(json_data)
