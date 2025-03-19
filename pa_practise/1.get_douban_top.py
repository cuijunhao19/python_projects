import requests
import re
import csv

# 伪装游览器
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
}

# 发送请求，获取页面源代码
for num in range(0, 10): # 豆瓣Top250分为10页,每页25条数据

    start = num*25      # 计算当前页的起始位置
    url = f"https://movie.douban.com/top250?start={start}"  # 构建url


    respond = requests.get(url = url, headers = headers)    # 发送GET请求
    page_content = respond.text                         # 获取页面源代码（HTML）
    respond.close()                     #关闭请求

    # 解析我想要的数据，如：电影名字，年份，评分，多少人评价等
    obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                    r'</span>.*?<br>(?P<year>.*?)&nbsp.*?<span class="rating_num" property="v:average">'
                    r'(?P<score>.*?)</span>.*?<span>(?P<count>.*?)评价', re.S)


    # 开始匹配并将爬取的数据存入csv文件，mode为添加写入模式
    result = obj.finditer(page_content)  # 使用正则表达式匹配页面内容
    f = open("douban_top250_date.csv", mode = "a", encoding = 'utf-8') # 打开 CSV 文件（追加模式）
    csvwriter = csv.writer(f)   # 创建 CSV 写入对象
    for i in result:
        # print(i.group("name"))
        # print(i.group("year").strip()) # .strip() 的作用：去除字符串开头和结尾的空白字符，确保数据干净
        # print(i.group("score"))
        # print(i.group("count"))
        # print("\n")
        dic = i.groupdict()                 # 将匹配结果转换为字典
        dic["year"] = dic["year"].strip()   # 去除年份字段的空白字符
        csvwriter.writerow(dic.values())    # 将字典的值写入 CSV 文件

    f.close()                               # 关闭文件
print("over!") 
  
