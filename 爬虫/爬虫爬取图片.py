#coding=utf-8
from urllib import request # python3 专用
# import urllib  # python2 专用
import re

def getHtml(url):
    page = request.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    html = html.decode('utf-8')  # python3 专用
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        request.urlretrieve(imgurl,'爬取的图片/%s.jpg' %x)
        x+=1

if __name__=='__main__':
    html = getHtml("http://tieba.baidu.com/p/2460150866")

    print(getImg(html))
