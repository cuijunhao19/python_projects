import requests
from bs4 import BeautifulSoup

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
}

url = 'http://www.xinfadi.com.cn/index.html'

respond = requests.get(url, headers=headers)

# 1.把页面源代码交给BeautifulSoup进行处理，生成bs4对象
web_content = BeautifulSoup(respond.text, "html.parser") # 指定html解析器

# 从bs4对象查找数据
# find(标签, 属性=值) 找第一个
# find_all() 找全部
table = web_content.find_all("table", class_ = "xxx") 
table = web_content.find_all("table", attrs={"class" : "xxx"})
# .text表示获取被标签标记的内容 