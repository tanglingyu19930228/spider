#!/usr/bin/env python3
# coding=utf-8
import requests
import csv
from functools import namedtuple
from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}

row=['行政区','电子监督号','项目名称','项目位置','面积','土地来源','土地用途','供应方式','土地使用年限',
     '行业分类','土地级别','成交价格万元','支付期号','约定支付日期','约定支付金额万元','备注',
     '土地使用权人','约定容积率下限','约定容积率上限','约定交地时间','约定开工时间','约定竣工时间',
     '实际开工时间','实际竣工时间','批准单位','合同签订日期']
info=namedtuple('info',row)
results=[]
NUM=1

with open('中国土地.csv','r') as f:
    url_item=f.read()
url_list=url_item.split('\n')

# with open('中国土地data.csv', 'w', newline='') as f:
#     f_csv = csv.writer(f)
#     f_csv.writerow(row)


def save_result():
    with open('中国土地data.csv', 'a', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(results)
    results.clear()

def get_info(html):
    global NUM
    soup=BeautifulSoup(html,"lxml")
    item=soup.find('div',{'id':'mainModuleContainer_1855_1856_ctl00_ctl00_vdFromIII'})
    if item is not None:
        a=item.find('span',{'id':'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r1_c2_ctrl'}).string
        b=item.find('span',{'id':'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r1_c4_ctrl'}).string.replace(u'\xa0','')
        c=None #item.find('span',{'id':'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r17_c2_ctrl'}).string.replace('�~','硚')
        d=item.find('span',{'id':'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r16_c2_ctrl'}).string.replace('�~','硚').replace('�事芬远�','澥路以东')
        e=item.find('span',{'id':'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r2_c2_ctrl'}).string
        f=item.find('span',{'id':'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r2_c4_ctrl'}).string
        g=item.find('span',{'id':'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r3_c2_ctrl'}).string
        h=item.find('span',{'id':'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r3_c4_ctrl'}).string
        i=item.find('span',{'id':'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r19_c2_ctrl'}).string
        j=item.find('span',{'id':'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r19_c4_ctrl'}).string.replace(u'\xa0','')
        k=item.find('span',{'id':'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r20_c2_ctrl'}).string
        l=item.find('span',{'id':'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r20_c4_ctrl'}).string
        m=None#item.find('span',{'id':'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f3_r2_c1_0_ctrl'}).string
        n=None#item.find('span',{'id':'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f3_r2_c2_0_ctrl'}).string
        o=None#item.find('span',{'id':'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f3_r2_c3_0_ctrl'}).string
        p=None#item.find('span',{'id':'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f3_r2_c4_0_ctrl'}).string
        q=item.find('span',{'id':'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r9_c2_ctrl'}).string
        r=item.find('span',{'id':'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f2_r1_c2_ctrl'}).string
        s=item.find('span',{'id':'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f2_r1_c4_ctrl'}).string
        t=item.find('span',{'id':'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r21_c4_ctrl'}).string
        u=item.find('span',{'id':'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r22_c2_ctrl'}).string
        v=item.find('span',{'id':'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r22_c4_ctrl'}).string
        w=item.find('span',{'id':'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r10_c2_ctrl'}).string
        x1=item.find('span',{'id':'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r10_c4_ctrl'}).string
        x=x1.replace(u'\xa0','')
        y=item.find('span',{'id':'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r14_c2_ctrl'}).string
        z=item.find('span',{'id':'mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r14_c4_ctrl'}).string
        result=info(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z)
        print((a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z))
        results.append(result)
    print(NUM)
    if NUM%10==0:
        save_result()
    NUM+=1


def get_html(url):
    try_num=1
    while True:
        try:
            response=requests.get(url, headers=headers)
        except:
            if try_num > 3:
                print("No response!")
                response = None
                break
            else:
                try_num += 1
            continue
        break
    return response

for i in range(1,124):
    url=url_list[i]
    #print(url)
    response = get_html(url)
    get_info(response.text)

with open('中国土地data.csv', 'a', newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerows(results)

print('Done')