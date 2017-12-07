#!/usr/bin/env python3
# coding=utf-8
import requests
import re
import time
import csv
from functools import namedtuple


row=['announcementTitle', 'adjunctUrl', 'secCode', 'announcementTime', 'adjunctSize', 'adjunctType']
info=namedtuple('info',row)
result=[]

def get_info(qidi):
    em = '<.+?>'
    announcementTitle=qidi['announcementTitle']
    announcementTitle_a=re.sub(re.compile(em),'',announcementTitle)

    adjunctUrl=qidi['adjunctUrl']
    adjunctUrl_a='http://www.cninfo.com.cn/'+adjunctUrl

    announcementTime=qidi['announcementTime']
    announcementTime_a=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(str(announcementTime)[:10])))

    secCode = 'code:'+str(qidi['secCode'])
    adjunctSize=qidi['adjunctSize']
    adjunctType=qidi['adjunctType']
    print(announcementTitle_a,
          adjunctUrl_a,
          secCode,
          announcementTime_a,
          adjunctSize,
          adjunctType)
    result.append(info(announcementTitle_a,adjunctUrl_a,secCode,announcementTime_a,adjunctSize,adjunctType))


n=1
while True:
    url='http://www.cninfo.com.cn/cninfo-new/fulltextSearch/full?searchkey=%E8%B5%84%E4%BA%A7%E8%AF%84%' \
        'E4%BC%B0%E8%AF%B4%E6%98%8E&sdate=&edate=&isfulltext=false&sortName=nothing&sortType=desc&pageN' \
        'um={}'.format(n)
    response=requests.get(url).json()
    announcements=response['announcements']
    len_announcements=len(announcements)
    if len_announcements!=0:
        for announcement in announcements:
            get_info(announcement)
    else:
        break
    time.sleep(0.2)
    n+=1


with open('data.csv', 'w', newline='',) as f:
    # newline默认会在行之间插入空行
    f_csv = csv.writer(f)
    f_csv.writerow(row)
    f_csv.writerows(result)

