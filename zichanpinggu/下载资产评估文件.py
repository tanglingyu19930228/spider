#!/usr/bin/env python3
# coding=utf-8
import requests,os,re

def down(name,url,n):
    try_num=1
    while True:
        try:
            response=requests.get(url)
        except:
            if try_num > 3:
                print("No response!")
                response = None
                break
            else:
                try_num += 1
            continue
        break
    name_pdf=name+'.pdf'
    with open(name_pdf, 'wb') as f:
        f.write(response.content)
    print('down:',n,'>>>',name)


with open('资产评估列表.csv', 'r') as f:
    result=f.read()
infos=result.split('\n')


path = os.path.join(os.path.abspath('.'), '资产评估说明')
if not os.path.exists(path):
    os.mkdir(path)
os.chdir(path)


for n in range(1,len(infos)-1):
    info_list=infos[n].split(',')
    name=info_list[1]
    url=info_list[2]
    type=info_list[6]
    if type=='PDF':
        down(name, url,n)
    else:
        print(n)

