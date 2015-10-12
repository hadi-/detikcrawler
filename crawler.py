__author__ = 'xhadix'
__author__ = 'xhadix'
import requests, urllib
from bs4 import BeautifulSoup
from urlparse import urlparse

print "usage insert URL with quotes \"google.com\" "
url = input("insert url to crawl = ")
r = requests.get('http://' + url)

html = r.content
parse = BeautifulSoup(html, 'html.parser')
if r.status_code == 200:
    totalImg = parse.findAll('img')
    print 'total image in site = ', len(totalImg)
    for imgSrc in totalImg:
        cekUrl = urlparse(imgSrc['src'])

        if cekUrl.scheme == '' and cekUrl.netloc != '':
            imageSize = 'http://'+imgSrc['src']
        elif cekUrl.scheme == '' and cekUrl.netloc == '':
            imageSize = 'http://'+url+imgSrc['src']
        else:
            imageSize = imgSrc['src']

        try:
            print(imageSize)
            fileSize = urllib.urlopen(imageSize)
            print(fileSize.headers.get("content-length"))
        except Exception as e:
            print('cannot open link '+str(e))

else:
    print('access blocked')
