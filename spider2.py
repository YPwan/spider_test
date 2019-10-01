# encoding: utf-8

import requests
import urllib
import json
import time
import os
from bs4 import BeautifulSoup


def get_html(keywords):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'
    }
    url = "https://www.baidu.com/s?wd="+ keywords
    r = requests.get(url=url,timeout=30 ,headers=headers)
    r.encoding = "utf-8"
    if(r.status_code == 404):
        returnInfo = False
    else:
        returnInfo = r.text
    return returnInfo

def get_info(html_code):
    soup = BeautifulSoup(html_code,'html.parser')
    content_list = soup.find_all('div', attrs={'class': 'result c-container '})
    result_list = []

    for content in content_list:
        findInfo = {}
        findInfo["title"] = content.h3.a.text
        content_url = content.h3.a.get('href')
        real_content = requests.get(url=content_url)
        findInfo["url"] = real_content.url
        findInfo["describe"] = content.find('div',{'class':'c-abstract'}).text
        result_list.append(findInfo)

    return result_list

def get_file_content(file):
    txt = open(file, 'r')
    str = txt.read()
    contentArr = str.split()
    return contentArr


def mkdir(path):

    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)


def save_txt(content,filename):
    res = open(filename + '.txt','a+',encoding='utf-8')
    save_content = ''
    for text in content :
        save_content += '标题：'+ text["title"]
        save_content += '\n\r'
        save_content += '链接：'+ text["url"]
        save_content += '\n\r'
        save_content += '简介：'+ text["describe"]
        save_content += '\n\r'
        save_content += '\n\r'
    res.write(save_content)
    res.close

def base():
    keywordsArr = get_file_content('keywords.txt')

    urlArr = get_file_content('check.txt')

    # url = 'http://zhongs.e23.cn/'   # Response 404
    for url in urlArr:
        for keywords in keywordsArr:
            check_url = f'site%3A{url}%20{keywords}'
            html = get_html(check_url)
            nowtime = time.strftime('%Y%m%d', time.localtime(time.time()))
            path = 'result/'+ nowtime + '/' + keywords + '/'
            mkdir(path)
            if(html):
                info = get_info(html)
                newInfo = []
                if info:
                    for text in info:
                        target = 'http://www.e23.cn/404/404.html'
                        if (target not in text):
                            newInfo.append(text)
                    if len(newInfo):
                        save_txt(newInfo, path + url)
                else:
                    continue
            else:
                continue
    print('ok!')





if __name__ == '__main__':
    base()
