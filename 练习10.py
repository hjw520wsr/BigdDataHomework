# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 14:21:34 2018

1.获取2300所学校的编号
2.获取31所城市的编号
3.获取142600条数据,
4.使用spark统计
@author: Nothing
"""

ls=open('school_id.txt',encoding='utf-8').readlines()
schoolls=[]

for line in ls:
    schoolls.append(line) #.split('-jianjie-')[1].split('.')[0]
import urllib.request as r
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'}

f=open('陕西招生人数5.txt','a',encoding='utf-8')
for schoolid in schoolls[0:]:
    req=r.Request(url,data='id={}&type=1&city=61&state=1'.format(schoolid).encode(),headers=headers)
    f.write(r.urlopen(req).read().decode('utf-8','ignore')+'\n')
f.close()





f1=open('异常的学校.txt','a',encoding='utf-8')

for schoolid in [2828,2240,600,526,337]:
    req=r.Request(url,data='id={}&type=1&city=61&state=1'.format(schoolid).encode(),headers=headers)
    f1.write(r.urlopen(req).read().decode('utf-8','ignore')+'\n')
f1.close()






