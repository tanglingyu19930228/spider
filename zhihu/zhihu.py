import login_zhihu
import re
get=login_zhihu.zhihu()
params = {'type': 'content', 'q': '孤独'}
response = get.session.get('https://www.zhihu.com/search', params=params, timeout=10)
# print(response.request.headers)
rep=r'href="/question/([\S]*)" class'
pattern1=re.compile(rep)
htmls=re.findall(pattern1,response.text)

for id in htmls:
    url='https://www.zhihu.com/question/'+id
    print(url)
    question=get.session.get(url)
    title_re='class="QuestionHeader-title".*-->(.*)<!--.*</h1>'
    title=re.findall(re.compile(title_re),question.text)
    print(title)
    #print(question.text)

#print(type(htmls[1]))
#知乎的每条搜索只能找到十个问题，其余的需要点击
#知乎的每个问题只显示前两个回答，其余的全是动态生成



