import json
import os
from functools import cmp_to_key
#href name data-id level price address
path="C:\美团有价格\美团有价格"
files=os.listdir(path)
s = []
fd=[]
for file in files: #遍历文件夹
     if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
          f = open(path+"/"+file,encoding='gbk'); #打开文件
          fd+=json.load(f)
pllist=[]
avg=0
for i in fd:
    if len(i['price'])==0 or len(i['level'])<3 or len(i['level'][2])==0:
        continue
    pl=int(i['level'][2][:-3])
    pllist.append(pl)
    avg+=pl
    #print(pl)
pllist.sort(reverse=True)
avg=avg/len(pllist)
print('pl max:',pllist[0])
print('pl mid:',pllist[int(len(pllist)/2)] )
print('pl avg:',avg )
pllist50=[]
pllist100=[]
pllist200=[]
pllist200plus=[]

for i in fd:
    if len(i['price'])==0 or len(i['level'])<3 or len(i['level'][2])==0:
        continue
    pl=int(i['level'][2][:-3])
    #print(pl,avg)
    if  pl>avg:
        name = i['name']
        rawdata = i['level']
        rawprice = i['price']
        rawlist = [name, rawdata, rawprice]
        #print(pl)
        if(int(i['price'][2:])<=50):
            pllist50.append(rawlist)
        elif (int(i['price'][2:])<=100):
            pllist100.append(rawlist)
        elif (int(i['price'][2:])<=200):
            pllist200.append(rawlist)
        else:
            pllist200plus.append(rawlist)
print(pllist50[0])
def cmp(elem1,elem2):
    if(elem1[1][1][:-1]!=elem2[1][1][:-1]):
        return float(elem1[1][1][:-1])-float(elem2[1][1][:-1])
    else:
        return float(elem1[1][2][:-3])-float(elem2[1][2][:-3])
def key2(elem):
    return elem[1][:-1]
key=cmp_to_key(cmp)
pllist50.sort(key=key,reverse=True)
news_ids = []
for id in pllist50:
    if id not in news_ids:
        news_ids.append(id)
pllist50=news_ids
pllist100.sort(key=key,reverse=True)

news_ids = []
for id in pllist100:
    if id not in news_ids:
        news_ids.append(id)
pllist100=news_ids
pllist200.sort(key=key,reverse=True)

news_ids = []
for id in pllist200:
    if id not in news_ids:
        news_ids.append(id)
pllist200=news_ids
pllist200plus.sort(key=key,reverse=True)
news_ids = []
for id in pllist200plus:
    if id not in news_ids:
        news_ids.append(id)
pllist200plus=news_ids
print('50')
cnt=0
for i in pllist50:
    print(i)
    cnt+=1
    if cnt >5 :
        break
print('100')
cnt=1
for i in pllist100:
    print(i)
    cnt+=1
    if cnt >5:
        break
print('200')
cnt=1
for i in pllist200:
    print(i)
    cnt+=1
    if cnt >5:
        break
print('200+')
cnt=1
for i in pllist200plus:
    print(i)
    cnt+=1
    if cnt>5:
        break
"""
for i in fd:
    if len(i['price'])==0:
        continue
    name=i['name']
    rawdata=i['level']
    rawprice=i['price'][2:]
    rawlist=[name,rawdata,rawprice]
    print(rawlist)
"""