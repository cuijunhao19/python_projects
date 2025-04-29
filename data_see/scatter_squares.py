import matplotlib.pyplot as plt 

plt.style.use('seaborn-v0_8')

x_values = range(1, 5001) 
y_values = [x**3 for x in x_values]

fig, ax = plt.subplots() 
# ax.scatter(x_values, y_values, color=(1,0,0), s=10)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10) 

ax.set_title("title", fontsize=14)
ax.set_xlabel("x", fontsize=7)
ax.set_ylabel("y", fontsize=7)
ax.tick_params(labelsize=7)

# 设置每个坐标轴的取值范围 
ax.axis([0, 5000, 0, 1e11])
ax.ticklabel_format(style='plain')

plt.show()