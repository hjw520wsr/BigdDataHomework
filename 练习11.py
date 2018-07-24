# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 10:09:10 2018

@author: Nothing
"""




ls=open('学校和编号.txt',encoding='gbk').readlines()
schoolls=[]
numls=[]
f=open('学校名称2.txt','a',encoding='utf-8')
f1=open('学校招生人数1.txt','a',encoding='utf-8')
for line in ls:
    schoolls.append(line.split(',')[0][1:])
    numls.append(int(line.split(',')[1][0:-2]))

f.write(str(schoolls))
f1.write(str(numls))
f.close()
f1.close()

















