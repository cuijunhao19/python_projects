import matplotlib.pyplot as plt
from random_walk import RandomWalk

# 只要程序处于活动状态，就不断地模拟随机游⾛
while True:
    # 创建⼀个RandomWalk实例
    rw = RandomWalk(5000)
    rw.fill_walk()

    # 将所有的点绘制出来
    plt.style.use('classic') 
    fig, ax = plt.subplots()

    point_numbers = range(rw.num_points)

    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=7)
    # ax.plot(rw.x_values, rw.y_values, color='Green', linewidth=1)

    # 这⾥使⽤set_aspect()指定两条轴上刻度的间距必须相等
    ax.set_aspect('equal')          

    # 标出起点和终点
    ax.scatter(0, 0, color='Green', edgecolors='none', s=25)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], color='Red', edgecolors='none',s=25)

    # 隐藏坐标轴
    ax.get_xaxis().set_visible(False) 
    ax.get_yaxis().set_visible(False) 

    plt.show()

    keep_running = input("Make another walk? (y/n): ") 
    if keep_running == 'n':
        break