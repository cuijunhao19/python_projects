# 目的：获取优美图库的唯美图片
# 1. 获取主页面的源代码
# 2. 再从主页面获取子页面源代码，再从中获取图片的下载路径，并写入文件

import requests
from bs4 import BeautifulSoup
import time

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
}

domian_url = "https://www.umei.cc/weimeitupian/"
resp = requests.get(domian_url, headers=headers)
resp.encoding = 'utf-8'

# 获取主页面下的子页面的url
main_webpage = BeautifulSoup(resp.text, "html.parser")
resp.close()
url_list = main_webpage.find("div", class_ = "taotu-main").find_all("a")
 # 根据你想要的数据定位标签以及属性

for it in url_list:
    href = "https://www.umei.cc" + it.get("href") # 直接通过get获取属性, 注：url要完整, 所以前面加上了HTTP

    # 获取子网页源代码
    child_resp = requests.get(href, headers=headers)
    
    child_resp.encoding = 'utf-8'
    child_webpage = BeautifulSoup(child_resp.text, "html.parser")
    child_resp.close()

    # 从子页面源代码中获取图片下载路径
    p = child_webpage.find("div", class_ = "big-pic")
    img = p.find("img")
    img_src = img.get("src")
    img_name = child_webpage.find("div", class_ = "photo").find("h1").text
    
    # 下载图片
    img_resp = requests.get(img_src, headers=headers)
    img_resp_content = img_resp.content # 这里拿到的是字节
    img_resp.close()
    with open("img/"+img_name+".jpg", mode='wb') as f:
        f.write(img_resp_content)
        print("over!", img_name)
    time.sleep(1)

print("All over!")
