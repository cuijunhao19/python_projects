# 在python如何调用多线程类来进行多线程运行

# 单线程
def func1():
    for i in range(1,100):
        print("func1", i)

if __name__ == '__main__':
    func1()
    for i in range(1, 10):
        print("main", i)
    print("Over!")


# 多线程1
from threading import Thread # 线程的类

def func2():
    for i in range(1,100):
        print("func2", i)

if __name__ == '__main__':
    t = Thread(target = func2) # 创建线程并给线程安排任务
    t.start()          # 多线程状态为开始工作状态，但具体的执行时间由CPU决定
    for i in range(1, 100):
        print("main", i)
    print("Over!")


# 多线程2
class MyThread(Thread):
    def run(self):   # 固定的，当线程被执行的时候就是执行run
        for i in range(1, 100):
            print("son_thread", i)

if __name__ == '__main__':
    t2 = MyThread()
    t2.start()    # 开启线程，Thread类的start()方法内部会自动调用run()
    for i in range(1, 100):
        print("main_thread", i)
    print("Over!")