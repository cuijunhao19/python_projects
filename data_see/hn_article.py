import requests
import plotly.express as px
import json
from operator import itemgetter

#  执⾏API调⽤并存储响应
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status_code:{r.status_code}")

# 处理有关每篇⽂章的信息
submission_ids = r.json()
# print(submission_ids)
submission_dicts = []
for submission_id in submission_ids[:25]:
    # 对于每篇⽂章，都执⾏⼀个API调⽤
    try:
        son_url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
        son_r = requests.get(son_url)
        print(f"id: {submission_id}\tstatus: {son_r.status_code}")
        resp_dict = son_r.json()

        # 对于每篇⽂章，都创建⼀个字典
        submission_dict = {
            'title':resp_dict['title'],
            'hn_link': f"<a href='https://news.ycombinator.com/item?id={submission_id}'>{resp_dict['title']}</a>",
            'comments':resp_dict['descendants']
        }
        submission_dicts.append(submission_dict)
    except KeyError:
        print("不可访问！跳过")
        continue
    
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# for submission_dict in submission_dicts:
#     print(f"Title: {submission_dict['title']}")
#     print(f"Comments: {submission_dict['comments']}")
#     print(f"Discussion link: {submission_dict['hn_link']}\n")

# 生成柱状图
title = '评论最多的文章'
labels = {'x':'文章名', 'y':'评论数'}
x_values = []
y_values = []
for submission_dict in submission_dicts:
    x_values.append(submission_dict['hn_link'])
    y_values.append(submission_dict['comments'])


fig = px.bar(
    x = x_values,
    y = y_values,
    labels = labels
)
fig.update_xaxes(tickangle=45)  # 标签旋转 45 度
fig.update_xaxes(tickfont=dict(size=5))
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)

fig.show()