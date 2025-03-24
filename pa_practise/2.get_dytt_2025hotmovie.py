# 目的：获取电影天堂2025必看热片的下载地址
# 1. 在主页面源代码找到2025必看热片的部分
# 2. 获取2025必看热片的各电影的子页面源代码，再从中获取到电影下载地址

import requests
import re
import csv

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
}

#主干url
domain_url = "https://www.dytt8899.com"
respond = requests.get(domain_url, headers=headers)
print(respond.status_code)
respond.encoding = "gb2312"
web_content = respond.text
respond.close()
# print(Web_content)

# 爬取主网页以及子网页的相关信息的正则表达式，如：在主网页先获取2025必看热片部分，
# 再获取该部分子网页的url，再分别在子网页获取各电影片名2和下载地址
obj1 = re.compile(r"2025必看热片.*?<ul>(?P<ul>.*?)</ul>", re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'", re.S)
obj3 = re.compile(r'◎片　　名　(?P<movie>.*?)<br />.*?<td style="WORD-WRAP: '
                r'break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">', re.S)

# 创建一个用于储存子网页url的列表
child_url_list = []

# 锁定2025必看热片部分并提取出里面子网页的url
result1 = obj1.search(web_content)
ul = result1.group("ul")

# 依次将获取的子网页url存入列表，注：该提取的子url需要与主url连接才是一个完整的url，
# 这个连接视情况而定
result2 = obj2.finditer(ul)
for it2 in result2:
    all_url = domain_url + it2.group("href")
    child_url_list.append(all_url)

# 分别对获取到的每个子url进行访问并获取子网页源代码，同第一步一样
for it3 in child_url_list:
    child_respond = requests.get(it3, headers=headers)
    child_respond.encoding = "gb2312"
    chiil_web_content = child_respond.text
    child_respond.close()
    
    f = open("dytt_2025_hotmovie_download_url.csv", mode = "a", encoding = 'utf-8')
    csvwriter = csv.writer(f)
    # 获取子页面源代码里的相关信息，如电影名字以及下载地址并写入csv文件
    result3 = obj3.search(chiil_web_content)
    dic = result3.groupdict()
    csvwriter.writerow(dic.values())

print("Over!")
