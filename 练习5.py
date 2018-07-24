# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 09:58:04 2018

@author: Nothing
"""
#Exercise 5
'''
1.优化代码，用函数的方式修改练习4，输出每一天的天气（函数）
2.打印温度折线图，使用函数来优化（要有返回值）
'''
city = input('please input city you want to search：')
url='http://api.openweathermap.org/data/2.5/forecast?q='+city+',cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r
data=r.urlopen(url).read().decode('utf-8','ignore')
import json
data=json.loads(data)
i=2
def weather(day):
    print('day'+str(day)+':')
    print('temper:'+str(data['list'][i]['main']['temp']))
    print('city:'+city)
    print('description:'+data['list'][i]['weather'][0]['description'])
    print('pressure:'+str(data['list'][i]['main']['pressure']))
    print('temp_max:'+str(data['list'][i]['main']['temp_max']))
    print('temp_min:'+str(data['list'][i]['main']['temp_min']))
    print('***************')
for j in range(1,6):
    weather(j)
    i += 8
#打印折线图
def lineChart():
    i = 2
    for j in range(1,6):
        print('-' * int(data['list'][i]['main']['temp']))
        i += 8
    return
lineChart()













