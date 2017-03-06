#coding:utf-8
import re
import requests
from mafengwo import city
Cityname=raw_input('去哪吃：')
Citycode=city.get(Cityname)
url='http://www.mafengwo.cn/cy/%s/gonglve.html'%Citycode
data=requests.get(url)
page=data.text
pattern=r'poi/\d+.html".+</a>' #匹配包含店名的字段
req=re.findall(pattern,page)
for i in req[1::2]:
    print i











