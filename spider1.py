# encoding: utf-8

import requests
import ctypes

def get_file_content(file):
    txt = open(file, 'r')
    str = txt.read()
    contentArr = str.split()
    return contentArr

# urlArr = get_file_content('check.txt')
urlArr = [
    'www.e23.cn',
    'bbs.e23.cn',
    'news.e23.cn',
    'www.jnio.gov.cn',
    'www.jnxc.gov.cn',
    'ftz.e23.cn',
    'www.jntyzx.gov.cn',
    'www.jnlgbj.gov.cn',
    'www.jngdjt.cn',
    'jw.lixia.gov.cn',
    'jnrb.e23.cn',
    'jnsb.e23.cn',
    'car.e23.cn',
    'mall.e23.cn',
    'hea.e23.cn',
    'health.e23.cn',
    'jinannews.cn',
    'money.e23.cn',
    'shzyhxjzg.com',
    'm.e23.cn',
    'zhibo.e23.cn',
    'video.e23.cn',
    'zhuanti.e23.cn',
    'www.frjie.com',
    'wx.bbs.e23.cn',
    'jnec.jnbusiness.jinan.gov.cn',
    'russian.e23.cn',
    'korea.e23.cn',
    'jp.e23.cn',
    'german.e23.cn',
    'france.e23.cn',
    'english.e23.cn',
    'www.jinanxsd.cn',
    'opinion.e23.cn',
    'www.jncsjs.com',
    'jn.wenming.cn',
    'www.jnzqhg.cn',
    'www.jihuagas.com',
    'www.jinan-energy.com',
    'www.bishuiqingyuan.com.cn'
]

for url in urlArr:
    r = requests.get(url='http://' + url)
    if(r.status_code!=200):
        boxMessage = url
        contentMessage = '404'
        ctypes.windll.user32.MessageBoxA(0, contentMessage.encode('ascii'), boxMessage.encode('ascii'), 0)

boxMessage = 'ok!'
contentMessage = '200'
ctypes.windll.user32.MessageBoxA(0, contentMessage.encode('ascii'), boxMessage.encode('ascii'), 0)