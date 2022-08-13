#get urls from extensionless 'dat' file and output to 'out.txt'
import requests, json, sys
with open(sys.path[0]+'/dat', 'r') as data:
    entries = json.loads(data.read())

out = {}
for entry in entries:
    out[entry['title']] = entry['url']

with open(sys.path[0]+'/out.txt', 'w') as output:
    output.truncate()
    output.seek(0)
    output.write(json.dumps(out, indent=4))