import matplotlib.pyplot as plt
from pathlib import Path 
import csv
from datetime import datetime

path = Path('weather_data/death_valley_2021_simple.csv')

# 读取文件并拆分为行列表
lines = path.read_text().splitlines()

# 创建 CSV 解析器并提取标题行
reader = csv.reader(lines) 
head_row = next(reader)

# for index, columnheader in enumerate(head_row):
#     # 对列表调⽤enumerate()来获取每个元素的索引及其值
#     print(index, columnheader)

# 提取日期、最高温度、最低温度
highs, lows, dates = [], [], []

for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# print(highs)

# 根据日期、最⾼温度和最低温度绘图
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='Red', alpha=0.5)
ax.plot(dates, lows, color='Blue', alpha=0.5)
# fill_between()方法，它接受一组x坐标值和两组y坐标值，并填充两组y坐标值之间的空间
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置绘图的格式
title = "Daily High and Low Temperatures, 2021\nDeath Valley, CA" 
ax.set_title(title, fontsize=20) 
ax.set_xlabel('', fontsize=16)
# 调⽤fig.autofmt_xdate() 来绘制倾斜的⽇期标签，以免它们彼此重叠
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16) 
ax.tick_params(labelsize=10)

plt.show()