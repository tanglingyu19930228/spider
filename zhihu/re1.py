import re
import login_zhihu
get=login_zhihu.zhihu()
#test='<h1 class="QuestionHeader-title" data-reactid="84"><!-- react-text: 85 -->你最孤独的时刻是什么？<!-- /react-text --></h1>'

test=get.session.get('https://www.zhihu.com/question/20406962')
#title_re='class="QuestionHeader-title"(.*)</h1>'

# title_re='class="QuestionHeader-title".*-->(.*)<!--.*</h1>'
# title=re.findall(re.compile(title_re),test.text)
# print(title)

