# Xpath是在XML文档搜索内容的一门语言
# HTML是的XML的一种子集

from lxml import etree

xml = """
<book_catalog>
    <book>
        <title>斗破苍穹</title>
        <author>天蚕土豆</author>
        <price>299</price>
        <category>玄幻</category>
    </book>
    <book>
        <title>斗罗大陆</title>
        <author>唐家三少</author>
            <book>
                <title>龙王传说</title>
            </book>
        <price>34</price>
        <category>玄幻</category>
    </book>
    <book>
        <title>盗墓笔记</title>
        <author>南派三叔</author>
        <price>24.99</price>
        <category>恐怖</category>
    </book>
    <news>
        <title>新闻周刊</title>
        <author>茂名一中</author>
        <price>99</price>
        <category>无</category>
    </news>
</book_catalog>
"""
tree = etree.XML(xml)
result1 = tree.xpath("/book_catalog") # /表示层级关系，第一个/表示根节点
result2 = tree.xpath("/book_catalog/title/text()") # text()用于获取节点内的文本
result3 = tree.xpath("/book_catalog//book/title/text()") #  //表示后代所有符合的
result4 = tree.xpath("/book_catalog/*/author/text()") # *是通配符, 可以代表任意名字的节点
print(result3)