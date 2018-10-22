#this script only downloads the images with name tags given the specific url of the category.

import urllib.request, urllib.error, urllib.parse
import ssl
from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

title = {}

url = "" #enter the url from where you want to download the images
reurl = urllib.request.urlopen(url,context = ctx).read()
soup =BeautifulSoup(reurl,'html.parser')

tags = soup('img')
for tag in tags:
    getsrc1 = tag.get('src')
    gettitle = tag.get('title')
    title[gettitle] = title.get(gettitle, 0 ) + 1
    #above line creates a dict to keep the count of the names if repeated
    if(title[gettitle] > 1):
        gettitle = str(gettitle) + str(title[gettitle])
    gettitle = str(gettitle)
    getsrc1 = str(getsrc1)
    pos = getsrc1.find(".jpg")
    getsrc = getsrc1[:pos-2]+getsrc1[pos:]
    #this line is to get the original file not the thumbnail one
    orurl = 'http://www.platonphoto.com'
    try:
        urllib.request.urlretrieve(orurl+getsrc,gettitle)
        print(gettitle + "done downloading")
    except:
        print("cannot download" + gettitle)
print("done")
