# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 17:37:14 2018
练习7
1.使用多选其一，完成天气的提醒，淘宝客户端
2.一定要多次使用for循环，偶尔使用while 在淘宝客户端中
3.使用到break或者continue  在淘宝客户端中

练习8
保存淘宝数据（小组项目）
1.每个组员爬取某个URL的100页数据   每个组员爬取不同的城市
2.保存淘宝商品信息（同练习6），并且保存为csv格式
3.每组组长合并各组员的数据
@author: Nothing
"""
import urllib.request as r
import json
page = 0
for i in range(1,101):
    url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&ie=utf8&loc=%E6%B1%9F%E8%A5%BF&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s={}&ajax=true'   
    try:
        data=r.urlopen(url.format(page)).read().decode('utf-8')
    except Exception as err:
        print('发生了错误')
    print('正在爬取第{}页'.format(int(page/44)+1))
    data=json.loads(data)
    f=open('tmp.txt','a',encoding='utf-8')
    f.write(str(data))
    f.write('\n')
    f.close()
    page = page+44

#1.商品名称(title)  价格(price) 销量(month_sales) 
#modes 字典->grid 字典->data 字典->spus 列表->索引 一共48个->
















