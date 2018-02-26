#!/usr/bin/env python3
# coding=utf-8
import time
import re
import sys
import os
import urllib.request
from concurrent import futures

'发起请求'


def request_get(url):
    num = 1
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}
    request = urllib.request.Request(url, headers=headers)
    while True:
        try:
            response = urllib.request.urlopen(request, timeout=5)
        except Exception:
            if num > 3:
                print("No response!")
                response = None
                break
            else:
                time.sleep(3)
                num += 1
            continue
        break
    return response


'判断域名'


def ischange(home_url):
    reg_home_url_now = re.compile('(http.*com)')
    home_url_now1 = request_get(home_url).geturl()
    if not home_url_now1:
        print('主页请求失败，请重试或检查是否存在该页面！')
        sys.exit()
    home_url_now2 = re.findall(reg_home_url_now, home_url_now1)
    # ['url']
    home_url_now = home_url_now2[0]
    if home_url_now != home_url and home_url_now.find('htm') == -1:
        print('网址有变，请修改homeurl为：%s' % home_url_now)
        sys.exit()
    else:
        pass


'获取网页'


def get_html(url, home_url=None):
    if home_url:
        ischange(home_url)
    response = request_get(url)
    return response


'下载图片'


def get_jpg(item):
    jpg_num = item[0]
    url = item[1]
    page_num = item[2]
    time_now = time.strftime('%Y%m%d', time.localtime(time.time()))
    try:
        img_html = get_html(url).read()
        with open('%s_%d_%d.%s' % (time_now, page_num, jpg_num, 'jpg'), 'wb') as fp:
            fp.write(img_html)
            print_text = 'Picture>>>' + str(jpg_num) + '\r'
            print(print_text)
    except Exception:
        pass


'下载页面'


def downpage(html_page_text, page_num):
    reg_list = ['<img src="([\S]*.jpg)', '<img src="([\S]*.jpeg)', '<li><a href="([\S]*)"']
    img_list = []
    for reg_img in reg_list:
        pattern = re.compile(reg_img)
        imgs = re.findall(pattern, html_page_text)
        for img in imgs:
            img_list.append(img)
    num_url = []
    for i in range(len(img_list)):
        num_url.append((i + 1, img_list[i], page_num))
    with futures.ThreadPoolExecutor(15) as t:
        t.map(get_jpg, num_url)


'下载板块'


def home_page_downlod(home_html, page_num, home_url):
    reg_page = '<li><a href="([\S]*\.htm)'
    pattern = re.compile(reg_page)
    reg_urls = re.findall(pattern, home_html)
    for reg in reg_urls:
        page_num += 1
        url = home_url + reg
        print('Page ', page_num, ':', url)
        try:
            html_page_text = get_html(url, home_url=home_url).read().decode('utf-8')
        except Exception:
            html_page_text = ''
        downpage(html_page_text, page_num)
    return page_num


'启动'


def run(homeurl, piclist=2, start=1, end=740):
    path = os.path.join(os.path.abspath('.'), 'Piclist%d' % piclist)
    if not os.path.exists(path):
        os.mkdir(path)
    os.chdir(path)
    # 创建并更改默认工作目录
    page_num = (start - 1) * 20
    home_url = homeurl
    for i in range(start, end + 1):
        if i == 1:
            url = home_url + '/htm/piclist%d/' % piclist
        else:
            url = home_url + '/htm/piclist%d/' % piclist + str(i) + '.htm'
        try:
            home_html = get_html(url, home_url=home_url).read().decode('utf-8')
        except Exception:
            home_html = ''
        page_num = home_page_downlod(home_html, page_num, home_url)

    print('you download %d page.' % page_num)


if __name__ == '__main__':
    homeurl = 'https://www.uuu447.com'
    arr = [1, 3, 4, 5, 6, 7, 8]
    for n in arr:
        run(homeurl, piclist=n, start=1)
        # run函数有四个参数，第一为主页，第二为板块，第三和第四为起始页面，默认从1到740

