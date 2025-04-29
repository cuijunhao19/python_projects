import plotly.express as px 
from die import Die

# 创建2个骰子 1个6面、1个10面
die_1 = Die(6)
die_2 = Die(10)

# 记录50000次的结果
results = []

# 同时投2个骰子1000次
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
# print(results)

# 分析结果
frequencies = []
result_kinds = range(1, die_1.num_sides + die_2.num_sides + 1)
for value in result_kinds:
    frequency = results.count(value)
    frequencies.append(frequency)
# print(frequencies)

# 对结果进⾏可视化
title = "两个骰子投50000次的结果"
labels = {'x':'num', 'y':'count'}
fig = px.bar(x=result_kinds, y=frequencies, title=title, labels=labels) # bar直方图、line折线图、scatter点图
# fig.show()  # !!!生成HTML文件，并且会在游览器打开
# 保存图片
path = 'D:\Programming\python_work\data_see\die.html'
fig.write_html(path)

