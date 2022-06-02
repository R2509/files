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

save('https://www.google.co.uk/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwjIlNzp2o34AhXS34UKHfSgBPwQFnoECA4QAQ&url=https%3A%2F%2Fwww.deviantart.com%2Fdevelopers%2Fhttp%2Fv1%2F20210526&usg=AOvVaw3KIOI7BL2SdsSwUhnmPlgf', '160')