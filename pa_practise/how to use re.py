import re 

# # findall 是匹配字符串中所有符合要求的内容(返回的是列表)
# lst = re.findall(r"\d+", "my phone is : 133429, his is : 10086")
# print(lst)

# # finditer 返回的是迭代器,从迭代器拿到内容需要用.group()
# it = re.finditer(r"\d+", "my phone is : 133429, his is : 10086")
# print(it)
# for i in it:
#     print(i.group())

# # search 匹配第一个符合的结果，找到一个结果就返回，返回的结果是match对象用.group()获取内容
# s = re.search(r"\d+", "my phone is : 133429, his is : 10086")
# print(s.group())

# # match 是从头匹配，如果头不符合就匹配不了
# s = re.match(r"\d+", "my phone is : 133429, his is : 10086")
# print(s.group())

# 预加载正则表达式
# obj = re.compile(r"\d+", re.S) # re.S可以让.匹配换行符
# s = obj.finditer("my phone is : 133429, his is : 10086")
# print(s)
# for i in s:
#     print(i.group())

# (?P<分组名字>正则内容) 用.group("分组名字")可以提取分组名字所在的正则内容