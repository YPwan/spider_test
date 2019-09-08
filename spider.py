
# #coding:utf-8
# from urllib.request import urlopen
# import os
# import re
#
# def get_html(url):
#
#     page = urllib.request.urlopen(url)
#     print(page)
#     exit()
#     htmlcode = page.read()
#     return htmlcode
#
#
# def write2txt(content):
#     pageFile = open('pageBaidu.txt', 'wb')  # 以写的方式打开pageCode.txt
#     pageFile.write(htmlcode)  # 写入
#     pageFile.close()  # 开了记得关
#     return True
#
#
# with urlopen('https://www.baidu.com/s?ie=utf-8&f=8&wd=site:bbs.e23.cn%C2%A0%C2%A0%C2%A0%E4%B8%AD%E5%85%B1') as x:
#     data = x.read()
#
# print(data)
#
# exit()
#
# write2txt(get_html('https://www.baidu.com/s?ie=utf-8&f=8&wd=site:bbs.e23.cn%C2%A0%C2%A0%C2%A0%E4%B8%AD%E5%85%B1'))
#
#


# coding=utf-8
import urllib.request as url
import string
import urllib
import re

def baidu_search(keyword):
    p= {'wd': keyword}
    res=url.urlopen("http://www.baidu.com/s?"+urllib.parse.urlencode(p))
    html=res.read()
    return html
def getList(regex,text):
    arr = []
    res = re.findall(regex, text)
    if res:
        for r in res:
            arr.append(r)
    return arr
def getMatch(regex,text):
    res = re.findall(regex, text)
    if res:
        return res[0]
    return ""
def clearTag(text):
    p = re.compile(u'<[^>]+>')
    retval = p.sub("",text)
    return retval

html = baidu_search('site:car.e23.cn%C2%A0%C2%A0%C2%A0中共')
content = str(html, 'utf-8','ignore')

pageFile = open('pageBaidu.txt','w',encoding='utf-8')  # 以写的方式打开pageCode.txt
pageFile.write(content)  # 写入
pageFile.close()  # 开了记得关

exit()

arrList = getList(u"<table.*?class=\"result\".*?>.*?<\/a>", content)
for item in arrList:
    regex = u"<h3.*?class=\"t\".*?><a.*?href=\"(.*?)\".*?>(.*?)<\/a>"
    link = getMatch(regex,item)
    url = link[0]
    title = clearTag(link[1]).encode('utf8')
    print (url)
    print (title)