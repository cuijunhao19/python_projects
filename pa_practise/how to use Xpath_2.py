from lxml import etree
from lxml import html

tree = html.parse("a.html")
# result = tree.xpath('/html/body/ul/li[1]/a/text()') # xpath 的顺序从一开始数
# print(result)
ol_list = tree.xpath('/html/body/ol/li')
for li in ol_list:
    result1 = li.xpath('./a/text()')
    result2 = li.xpath('./a/@href')
    print(result1)
    print(result2)