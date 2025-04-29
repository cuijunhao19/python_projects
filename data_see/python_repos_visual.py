import requests
import plotly.express as px 

# 执行API调用并查看响应，"https://api.github.com/search/repositories?q=language:python+sort:stars+stars:>10000"
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"} 
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# 处理结果
response_dict = r.json()
print(f"Complete results: {not response_dict['incomplete_results']}")

# 处理有关仓库的信息
repo_dicts = response_dict['items']
repo_links, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    # 将仓库名转换为链接
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    star = repo_dict['stargazers_count']
    stars.append(star)
    # 创建悬停⽂本
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}" 
    hover_texts.append(hover_text)


# 可视化
title = "Most-Starred Python Projects on GitHub"
labels = {'x':'Repository', 'y':'Stars'}

fig = px.bar(
    x=repo_links, 
    y=stars, 
    title=title, 
    labels=labels,
    hover_name=hover_texts
)

# fig.update_layout()⽅法修改⼀些图形元素
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)

#  update_traces()则可⽤来定制图形呈现的数据
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)

fig.show()
