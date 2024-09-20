# 如何发送请求
# pip install requests
import requests
# pip install lxml
from lxml import etree

# 发送给谁
url = 'https://dldl1.nsbuket.cc/xiaoshuo/douluodalu/1.html'   #起始网址，比如我这里用的斗罗大陆引子目录为起始地址

while True:
    # 将代码访问伪装成游览器访问
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
    }     # 用户代理可以通过游览器查找

    # 发送请求
    respond = requests.get(url,headers=headers)

    # 设置编码
    respond.encoding = 'utf-8'    #支持中文显示

    # 响应信息，注：复制想要寻找的Xpath路径，还要注意你想要Xpath的元素以及属性
    e = etree.HTML(respond.text)
    info = '\n'.join(e.xpath('//div[@class="m-post"]/p/text()'))   #join的用法：''内的符号表示列表的元素间的间隔的样式，将列表元素组合成字符串
    title = e.xpath('//h1/text()')[0]
    url = f'https://dldl1.nsbuket.cc{e.xpath("//tr/td[2]/a/@href")[0]}'   #下一章节地址

    print(title)  #将目录打印在终端方便查看下载进度
    # 保存
    with open('斗罗大陆.txt','a',encoding='utf-8') as a:  # 'a'表示追加数据，不能用'w'，会覆盖掉原来的数据
        a.write(title+'\n\n'+info+'\n\n')

    # 下载到最后一章停止，退出循环，防止重头再下载一遍
    if(url == 'https://dldl1.nsbuket.cc/xiaoshuo/douluodalu/'):
        break 
   
