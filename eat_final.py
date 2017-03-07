#coding:utf-8
import re
import requests
from bs4 import BeautifulSoup
from mafengwo import city
while True:
    Cityname=raw_input('去哪吃（回车退出）：')
    Citycode=city.get(Cityname)
    if not Cityname:
        print '不吃，谢谢'
        break
    if Citycode:
        url='http://www.mafengwo.cn/cy/%s/gonglve.html'%Citycode
        data=requests.get(url)
        page=data.text
        foodlist=[]
        soup=BeautifulSoup(page)
        soup_div=soup.find_all('div',class_='title')
        for i in soup_div:
            soup_data=i.find_all('a')[0]
            foodlist.append(soup_data.get_text())
        for bistro in foodlist:
            print bistro
    else:
        print '别吃了，好好减肥'















