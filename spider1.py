# encoding: utf-8

import requests
import urllib
import json
import time
import os
from bs4 import BeautifulSoup
import ctypes

def get_file_content(file):
    txt = open(file, 'r')
    str = txt.read()
    contentArr = str.split()
    return contentArr

urlArr = get_file_content('check.txt')
for url in urlArr:
    r = requests.get(url='http://' + url)
    if(r.status_code!=200):
        boxMessage = url
        contentMessage = '404'
        ctypes.windll.user32.MessageBoxA(0, contentMessage.encode('ascii'), boxMessage.encode('ascii'), 0)
print('ok!')