import requests
def save(url, filename):
    resp = requests.get(url)
    if resp.status_code:
        print(resp.status_code)
        with open(f'/workspace/files/view/0/{filename}.txt', 'wb') as file:
            file.truncate(0)
            file.write(resp.content)
    else:
        print(f'error {resp.status_code}')

save('https://www.deviantart.com/ospkt/art/club-jess-81665124', '157')