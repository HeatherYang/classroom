#coding:utf-8
import jieba
from collections import Counter
cheer=[]
with open('cheerLyrics') as f:
    source=f.read()
    data=jieba.cut(source)
    cheer.extend(set(data))
count=Counter(cheer)
results=sorted(count.items(),key=lambda x:x[1],reverse=True)
print results[1:6]



