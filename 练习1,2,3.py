# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Exercise 1
temper=[18,20,13,31,28,25,24]
print(str(temper[0])+' '
      +str(temper[1])+' '
      +'周三'+str(temper[2])+'°'+' '
      +str(temper[3])+' '
      +str(temper[4])+' '
      +str(temper[5])+' '
      +str(temper[6]))

'''定义一个字典，
存储5天的天气信息，温度，天气情况，打印星期三的信息
'''
#Exercise 2
temper={'Monday':['18°','小雨'],
        'Tuesday':['19°','多云'],
        'Wednesday':['20°','小雨'],
        'Thursday':['25°','晴'],
        'Friday':['26°','晴'],
        'Saturday':['26°','大雨'],
        'Sunday':['29°','晴']}
print('星期三天气信息：'
      +temper['Wednesday'][0]
      +temper['Wednesday'][1])
#Exercise 3
''' 
1.通过复制联网天气代码，获取老家的天气字典
2.打印温度temp，天气情况description，天气气压pressure
'''
import urllib.request as req
data=req.urlopen('http://api.openweathermap.org/data/2.5/weather?q=xinxian&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996').read().decode('utf-8','ignore')
import json
data = json.loads(data)
print('温度：'+str(data['main']['temp']))
print('天气情况：'+data['weather'][0]['description'])
print('天气气压：'+str(data['main']['pressure']))
#Exercise 4
'''
1.打印每天18点的天气信息：温度，城市，情况，亲呀，最高温度，最低温度
2.写出英文版的天气-天气情况，用户输入英文
3.打印温度折线图
4.获取所有温度，并且排序sorted()
5.友情提示：根据温度提示穿衣，打伞，出门
'''




