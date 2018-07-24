# -*- coding: utf-8 -*-
'''
1.打印5天18点的天气信息：温度，城市，情况，气压，最高温度，最低温度
2.写出英文版的天气-天气情况，用户输入英文
3.打印温度折线图
4.获取所有温度，并且排序sorted()
5.友情提示：根据温度提示穿衣，打伞，出门
'''
city = input('please input city you want to search：')
url='http://api.openweathermap.org/data/2.5/forecast?q='+city+',cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r
data=r.urlopen(url).read().decode('utf-8','ignore')
import json
data=json.loads(data)
temper = [data['list'][2]['main']['temp'],
          data['list'][10]['main']['temp'],
          data['list'][18]['main']['temp'],
          data['list'][26]['main']['temp'],
          data['list'][34]['main']['temp']]
print('There is the specific description of '+city+'in 5 days:')
#第一天
print('First day:')
print('temper:'+str(temper[0]))
print('city:'+city)
print('description:'+data['list'][2]['weather'][0]['description'])
print('pressure:'+str(data['list'][2]['main']['pressure']))
print('temp_max:'+str(data['list'][2]['main']['temp_max']))
print('temp_min:'+str(data['list'][2]['main']['temp_min']))
print('***************')
#第二天
print('Second day:')
print('temper:'+str(temper[1]))
print('city:'+city)
print('description:'+data['list'][10]['weather'][0]['description'])
print('pressure:'+str(data['list'][10]['main']['pressure']))
print('temp_max:'+str(data['list'][10]['main']['temp_max']))
print('temp_min:'+str(data['list'][10]['main']['temp_min']))
print('***************')
#第三天
print('Third day:')
print('temper:'+str(temper[2]))
print('city:'+city)
print('description:'+data['list'][18]['weather'][0]['description'])
print('pressure:'+str(data['list'][18]['main']['pressure']))
print('temp_max:'+str(data['list'][18]['main']['temp_max']))
print('temp_min:'+str(data['list'][18]['main']['temp_min']))
print('***************')
#第四天
print('Forth day:')
print('temper:'+str(temper[3]))
print('city:'+city)
print('description:'+data['list'][26]['weather'][0]['description'])
print('pressure:'+str(data['list'][26]['main']['pressure']))
print('temp_max:'+str(data['list'][26]['main']['temp_max']))
print('temp_min:'+str(data['list'][26]['main']['temp_min']))
print('***************')
#第五天
print('Fifth day:')
print('temper:'+str(temper[4]))
print('city:'+city)
print('description:'+data['list'][34]['weather'][0]['description'])
print('pressure:'+str(data['list'][34]['main']['pressure']))
print('temp_max:'+str(data['list'][34]['main']['temp_max']))
print('temp_min:'+str(data['list'][34]['main']['temp_min']))
print('***************')
#打印温度折线图
print('The line chart is ：')
print('-' * int(temper[0]))
print('-' * int(temper[1]))
print('-' * int(temper[2]))
print('-' * int(temper[3]))
print('-' * int(temper[4]))
print('***************')
#五天天气排序
print('The temper in 5 days is :')
print(temper)
print('The Sorted temper is :')
print(sorted(temper))
#友情提示
j=1
for i in range(0,5):
    if temper[i] >25 and temper[i] < 30:
        print('第{}天:'.format(j)+'气温{}'.format(temper[i]))
        j=j+1
        print('天气凉爽，适宜外出活动')
    elif temper[i] <= 25:
        print('第{}天:'.format(j)+'气温{}'.format(temper[i]))
        j=j+1
        print('天气转凉，多穿点衣服哟')
    else:
        print('第{}天:'.format(j)+'气温{}'.format(temper[i]))
        j=j+1
        print('天气炎热，请待在室内')





















