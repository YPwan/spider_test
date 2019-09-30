# encoding: utf-8

import requests
import urllib
import json
from bs4 import BeautifulSoup


def get_html(keywords):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'
    }
    url = "https://www.baidu.com/s?wd="+ keywords
    r = requests.get(url=url,headers=headers)
    r.encoding = "utf-8"
    return r.text

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

def save_txt(content):
    res = open('result.txt','a+',encoding='utf-8')
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
            # print(html)
            # exit()
            info = get_info(html)
            # print(info)
            # print(info)
            # exit()
            if info:
                save_txt(info)
            else :
                continue
            # print(info)




if __name__ == '__main__':
    base()
