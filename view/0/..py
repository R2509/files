from pathlib import Path
from bs4 import BeautifulSoup
from json import loads

dirpath = Path(__file__).resolve().parent

files = [file for file in dirpath.iterdir()]


with open(dirpath / 'urls.txt', 'r') as output_file:
    existing_str = output_file.read()
existing = existing_str.strip('\r').split('\n')
for file_path in files:
    with open(file_path, 'rb') as data:
        d = data.read()
        if (d.split(b'\n')[0].lower() != b'<!doctype html>\r'):
            print(f"\x1b[33mFILE SKIP\x1b[m {file_path}")
            continue # ignore non-html files
        html = BeautifulSoup(d, 'lxml')
    el = html.find('a', {'data-hook': 'deviation_link'})
    if el is None:
        print(f"\x1b[31mFILE EXCL\x1b[m {file_path}")
        continue
    print(f"\x1b[32mFILE OK  \x1b[m {file_path}")
    # print(file_path, el.attrs['href'])
    url = el.attrs['href']
    if url not in existing:
        existing.append(url)
        print(f"\x1b[34mDATA ADD \x1b[m {file_path}")
    else:
        print(f"\x1b[35mDATA SKIP\x1b[m {file_path}")

with open(dirpath / 'urls.txt', 'w') as output_file:
    output_file.truncate(0)
    output_file.write('\n'.join(existing))