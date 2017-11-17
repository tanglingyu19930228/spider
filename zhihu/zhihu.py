#!/usr/bin/env python3
#coding=utf-8
import login_zhihu
import re
import threading
from concurrent import futures
get=login_zhihu.zhihu()
lock = threading.Lock()
result = []


def return_pageid(q):
    params = {'type': 'content', 'q': q}
    page_response = get.session.get('https://www.zhihu.com/search', params=params, timeout=10)
    page_reg=r'href="/question/([\S]*)" class'
    #返回的结果里有专栏有问题，这里只提取问题
    page_pattern=re.compile(page_reg)
    search_ids=re.findall(page_pattern,page_response.text)
    return search_ids


def return_answer(search_ids):
    id=[i for i in search_ids]
    with futures.ThreadPoolExecutor(10) as t:
        t.map(get_result,id)
    return result


def get_result(id):
    #print(threading.currentThread())
    global lock
    url='https://www.zhihu.com/question/'+id
    #构造url
    question=get.session.get(url)
    title_re='class="QuestionHeader-title".*-->(.*)<!--.*</h1>'
    #获取问题名称
    title=re.findall(re.compile(title_re),question.text)
    #print('\n\n','Title: ',title[0])
    text_re = 'itemprop="text" data-reactid=[\S]*?>([\S\s]*?)(</span>)'
    #获取问题内容
    text = re.findall(re.compile(text_re), question.text)
    with lock:
        result.append(''.join(['\n\n', 'Title: ', title[0]]))
        if len(text) == 2:
            reference= '*' * (len(title[0]) * 2-4)
            reference_list=[reference,'','']
            text.insert(0,reference_list)
        for answer_list in text:
            answer_n = answer_list[0]
            answer_reg = '<.+?>'
            answer = re.sub(re.compile(answer_reg), '', answer_n)
            if answer_list==text[0]:
                #print('\n','Question: ',answer)
                result.append(''.join(['\n','Question: ',answer]))
            else:
                #print('\n', 'Answer: ',answer)
                result.append(''.join(['\n','Answer: ',answer]))


def zhihu_search(q):
    search_ids=return_pageid(q)
    result=return_answer(search_ids)
    return result


if  __name__=='__main__':
    b=zhihu_search('职场')
    for i in b:
        print(i)




#知乎的每条搜索只能找到十个问题，其余的需要点击
#知乎的每个问题只显示前两个回答，其余的全是动态生成



