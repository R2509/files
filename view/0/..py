from pathlib import Path
from bs4 import BeautifulSoup

dirpath = Path(__file__).resolve().parent

files = [file for file in dirpath.iterdir()]
links = []

for file_path in files:
    with open(file_path) as data:
        d = data.read()
        if (d.split('\n')[0].lower() != '<!doctype html>'):
            continue # ignore non-html files
        html = BeautifulSoup(d, 'lxml')
    el = html.find('a', {'data-hook': 'deviation_link'})
    if el is None:
        continue
    print(file_path, el.attrs['href'])
    links.append(el.attrs['href'])
    with open(dirpath / 'urls.txt', 'w') as file_path:
        file_path.truncate(0)
        file_path.write('\n'.join(links))