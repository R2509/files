import requests, json
import xml.etree.ElementTree as et

r = requests.get('https://backend.deviantart.com/rss.xml?q=gallery:ruff-sketches')

dom = et.fromstring(r.content)
l = []

for i in dom[0][11:]:
    l.append({
        'title': i[0].text,
        'description': i[-1].text,
        'url': i[-2].attrib['url']
    })
l = json.dumps(l, indent=4)
with open('151.txt', 'w') as file:
    file.truncate()
    file.write(l)