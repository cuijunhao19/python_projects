# 目的：获取猪八戒网的saas服务商的相关信息

import requests
from lxml import etree

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
}

url = "https://www.zbj.com/fw/?k=saas"

resp = requests.get(url, headers=headers)
page_content = resp.text
resp.close()

# 解析HTML
html = etree.HTML(page_content)

# 通过检查，找到每一个服务所在的div，获取所有，然后遍历打印相关信息
divs = html.xpath('//*[@id="__layout"]/div/div[3]/div/div[4]/div/div[2]/div/div[2]/div')
for div in divs:
    title = "saas".join(div.xpath('./div/div[3]/div[2]/a/span/text()'))
    price = div.xpath('./div/div[3]/div[1]/span/text()')[0]
    com_name = div.xpath('./div/div[5]/div/div/div/text()')[0]
    print("介绍："+title)
    print("公司："+com_name)
    print("价格："+price)
    print("\n")
    
