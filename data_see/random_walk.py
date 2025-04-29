from random import choice

class RandomWalk:
    """⼀个⽣成随机游⾛数据的类"""
    def __init__(self, num_points=5000):
        """初始化随机游⾛的属性"""
        self.num_points = num_points
        # 所有随机游⾛都始于(0, 0)
        self.x_values = [0]
        self.y_values = [0]

    # 决定前进的⽅向以及沿这个⽅向前进的距离
    def get_x_step(self):
        x_direction = choice([-1, 1])
        x_distance = choice([0, 1, 2, 3, 4])
        x_step = x_distance * x_direction 
        return  x_step

    def get_y_step(self):
        y_direction = choice([-1, 1])
        y_distance = choice([0, 1, 2, 3, 4])
        y_step = y_distance * y_direction
        return y_step


    def fill_walk(self):
        '''计算随机游⾛包含的所有点'''

        # 不断游⾛，直到列表达到指定的⻓度
        while len(self.x_values) < self.num_points:
            
            x_step = self.get_x_step()
            y_step = self.get_y_step()
            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下⼀个点的x坐标值和y坐标值
            nx = self.x_values[-1] + x_step
            ny = self.y_values[-1] + y_step

            self.x_values.append(nx)
            self.y_values.append(ny)




