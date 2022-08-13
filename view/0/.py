#get urls from extensionless 'dat' file and output to 'out.txt'
import requests, json, sys
with open(sys.path[0]+'/dat', 'r') as data:
    entries = json.loads(data.read())

out = {}
i=0
for entry in entries:
    out[i] = [entry['title'], entry['url']]
    i+=1
o=''
for i in range(len(out)):
    o += f'[{out[i][0]}]({out[i][1]})\n'


with open(sys.path[0]+'/out.md', 'w') as output:
    output.truncate()
    output.seek(0)
    output.write(o)