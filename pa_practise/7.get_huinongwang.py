# 目的：利用多线程去快速获取多个网页的数据，注：该代码仅为思路示例，并不能完全成功爬取所有数据，
# 因为该网页部分访问需要登陆，该代码仅为使用线程池的思路

import requests
from lxml import etree
import csv
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

f = open("huinogwang_datas.csv", mode='a', encoding='utf-8')
csvwriter = csv.writer(f)

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
}

def one_page_data_download(url):

    resp = requests.get(url, headers=headers) 
    page = resp.text
    resp.close()

    html = etree.HTML(page)

    lis = html.xpath('//*[@id="__layout"]/div/div/div[2]/div[1]/div[3]/div/div[1]/div/div[1]/div[2]/ul/li')

    for li in lis:
        # time = li.xpath('./a/span[1]/text()')[0]
        # name = li.xpath('./a/span[2]/text()')[0]
        # place = li.xpath('./a/span[3]/text()')[0]
        # price = li.xpath('./a/span[4]/text()')[0]
        # print("time:", time, "name:", name, "place:", place, "price:", price)
        text = li.xpath('./a/span/text()')
        text = (item.replace("\n", "").replace(" ", "").replace("-", "")for item in text)
        csvwriter.writerow(text)
    print(url, "Over!")


if __name__ == '__main__':

    # for i in range(1, 200): # 单线程效率低下
    #     url = f"https://www.cnhnb.com/hangqing/cdlist-0-0-0-0-0-{i}/"
    #     one_page_data_download(url)
    
    # 将下载任务交给线程池
    with ThreadPoolExecutor(50) as t:
        for i in range(1, 200):
            url = f"https://www.cnhnb.com/hangqing/cdlist-0-0-0-0-0-{i}/"
            t.submit(one_page_data_download, url)
