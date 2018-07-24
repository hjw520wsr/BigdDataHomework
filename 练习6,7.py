# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 11:56:28 2018
1.每一行显示4个商品然后打印分割线，只要第一页36个商品信息
2.列出36个商品
3.获取所有的商品的价格，并且排序（高->低）
4.按照销量排序
5.商品过滤，只要15天退款或者包邮的信息，显示
@author: Nothing
"""
page = 0
url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.2&ie=utf8&initiative_id=tbindexz_20170306&ajax=true'
import urllib.request as r
data=r.urlopen(url).read().decode('utf-8','ignore')
import json
data=json.loads(data)
title=[0]*36
view_price=[0]*36
view_sales=[0]*36
view_fee=[]
b=[]
def showMessage():
    index = 0
    j=1
    while j < 10:
        for i in range(1,5):
            title[index]=data['mods']['itemlist']['data']['auctions'][index]['title']
            view_price[index]=float(data['mods']['itemlist']['data']['auctions'][index]['view_price'])
            view_sales[index]=data['mods']['itemlist']['data']['auctions'][index]['view_sales']
            view_fee.append(float(data['mods']['itemlist']['data']['auctions'][index]['view_fee']))
            b.append(float(view_sales[index][0:-3]))
            print('名称：'+title[index])
            print('价格：'+str(view_price[index]))
            print('销量：'+view_sales[index])
            print(' ')
            index=index+1
        print('*'*30)
        j=j+1
    return
showMessage()
print('商品价格排序：')
a=[0]*36
a=sorted(view_price)
a.reverse()
print(a)
print('*'*30)
print('按销量排序:')
b=sorted(b)
print(b)
print(view_fee)

for i in range(0,36):
    j=i
    if view_fee[i]==0.0:
        print('第{}件商品包邮'.format(j+1),end=' ')
    else:
        continue






