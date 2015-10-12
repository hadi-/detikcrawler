__author__ = 'xhadix'
import requests, urllib2
from bs4 import BeautifulSoup
from urlparse import urlparse
from progressbar import ProgressBar

url = raw_input("insert url to crawl = ")
r = requests.get('http://' + url)
pbar = ProgressBar()
html = r.text
parse = BeautifulSoup(html, 'html.parser')
if r.status_code == 200:
    totalImg = parse.findAll('img')
    print 'total image in site = ', len(totalImg)
    for imgSrc in pbar(totalImg):
        totalSize = 0
        cekUrl = urlparse(imgSrc['src'])

        if cekUrl.scheme == '' and cekUrl.netloc != '' and  not imgSrc['src'].startswith('//'):
            imageSize = 'http://'+imgSrc['src']
        elif cekUrl.scheme == '' and cekUrl.netloc == '' and not imgSrc["src"].startswith("images/"):
            imageSize = 'http://'+url+imgSrc['src']
        elif cekUrl.netloc == '' and cekUrl.scheme == '' and imgSrc["src"].startswith("images/"):
            imageSize = 'http://'+url+'/'+imgSrc['src']
        elif imgSrc['src'].startswith('//'):
            imageSize = 'http:'+imgSrc['src']
        else:
            imageSize = imgSrc['src']

        try:
            fileSize = urllib2.urlopen(imageSize)
            totalSize += int(fileSize.headers.get("content-length"))
        except Exception as e:
            print('cannot open link '+str(e))

    print(totalSize)

else:
    print('access blocked')
