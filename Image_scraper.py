from bs4 import BeautifulSoup
import requests
import urllib3
import re
import os.path

class ImageScraper:
    def __init__(self, web_url, tag_name, regex_request, regex_request2, folder, img_name):
        self.web_url = web_url
        self.tag_name = tag_name
        self.regex_request = regex_request
        self.regex_request2 = regex_request2
        self.folder = folder
        self.img_name = img_name
        self.http = urllib3.PoolManager()
        self.url = requests.get(self.web_url)

    def TagSearcher(self, ):
        soup = BeautifulSoup(self.url.text, 'html.parser')
        links = []
        # search for all <img>'s
        for img in soup.find_all(self.tag_name):
            links.append(img)
        self.strlinks = str(links)

    def Regex(self):
        # search for all 'data-orig-file' in <img>'s
        urls = re.findall(self.regex_request, self.strlinks)
        links2 = []
        links2.append(urls)
        links2 = str(links2)
        self.urls2 = re.findall(self.regex_request2, links2)

    def ClearingArtifacts(self):
        # clearing artifacts
        links3 = []
        for line in self.urls2:
            links3.append(line.replace(r"'", ''))
        self.links4 = []
        for line in links3:
            self.links4.append(line.replace(r'",', ''))
        self.links4[-1] = self.links4[-1][0:-3]
        # print(links4)

    def Downloader(self):
        counter = 0

        for url in self.links4:
            r = self.http.request('GET', url)
            counter += 1
            num = str(counter + 1)
            frmt = url[-4:]
            if not os.path.exists(self.folder):
                os.makedirs(self.folder)
            with open(os.path.join(self.folder, self.img_name + num + frmt), 'wb') as final_image:
                final_image.write(r.data)
            print('downloading pic ' + str(counter))

# Obj = class           url adress             tag            regex requests
Obj = ImageScraper('https://rare-pepe.com/', 'img', r'(data-orig-file="https?://\S+)',
                    r'(https?://\S+)', '.\downloads', 'pepe_')
#                                   folder to dwnld     name of files

if __name__ == '__main__':
    Obj.TagSearcher()
    Obj.Regex()
    Obj.ClearingArtifacts()
    Obj.Downloader()
