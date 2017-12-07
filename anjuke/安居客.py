# -*-coding:utf-8-*-
import requests,csv
from functools import namedtuple
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}
row=['a_title','em_title','house_type','size','layers','bilud_year','brokername','address','tags','price']
info=namedtuple('info',row)
results=[]

def get_info(response):
    soup=BeautifulSoup(response,"lxml")
    list_items=soup.find_all("li",{'class':'list-item'})
    for list_item in list_items:
        house_title=list_item.find('div',{'class':'house-title'})
        a_title=house_title.a.get('title')
        try:
            em_title=house_title.em.get('title')
        except AttributeError as e:
            em_title='have no'
        details_item= list_item.find('div', {'class': 'details-item'})
        spans=details_item.find_all('span')
        house_type=spans[0].string
        size=spans[1].string.replace('²','2')
        layers=spans[2].string
        bilud_year=spans[3].string
        try:
            brokername=spans[4].text.replace('','')
        except IndexError as e:
            brokername='have no'
        address=list_item.find('span', {'class': 'comm-address'}).get('title').replace(u'\xa0','')
        tags=list_item.find('div', {'class': 'tags-bottom'}).text.replace('\n','')
        price=list_item.find('div', {'class': 'pro-price'}).text.replace('\n','').replace('²','2')
        result=info(a_title,em_title,house_type,size,layers,bilud_year,brokername,address,tags,price)
        #print((a_title,em_title,house_type,size,layers,bilud_year,brokername,address,tags,price))
        results.append(result)

for i in range(1,51):
    url='https://wuhan.anjuke.com/sale/p{}/#filtersort'.format(i)
    response = requests.get(url, headers=headers)
    response_text=response.text
    get_info(response_text)
    print(i)

with open('安居客.csv', 'w', newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(row)
    f_csv.writerows(results)
