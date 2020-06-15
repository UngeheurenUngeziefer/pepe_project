from bs4 import BeautifulSoup
import requests
import urllib3
import re
import os.path

http = urllib3.PoolManager()
url = requests.get('https://rare-pepe.com/')
soup = BeautifulSoup(url.text, 'html.parser')

links = []
links2 = []
links3 = []
links4 = []

# search for all <img>'s
for img in soup.find_all('img'):
    links.append(img)
strlinks = str(links)

# search for all 'data-orig-file' in <img>'s
urls = re.findall(r'(data-orig-file="https?://\S+)', strlinks)
links2.append(urls)
links2 = str(links2)
urls2 = re.findall(r'(https?://\S+)', links2)

for line in urls2:
    links3.append(line.replace(r"'", ''))

for line in links3:
    links4.append(line.replace(r'",', ''))
links4[-1] = links4[-1][0:-3]
# print(links4)

counter = 0

for url in links4:
    r = http.request('GET', url)
    counter += 1
    num = str(counter+1)
    frmt = url[-4:]
    with open(os.path.join('.\downloads', 'pepe_' + num + frmt), 'wb') as final_image:
        final_image.write(r.data)
    print('downloading pic ' + str(counter))
