# 在python中如何使用多进程

from multiprocessing import Process

def func():
    for i in range(1000):
        print("son_process", i)


if __name__ == '__main__':
    p = Process(target=func)
    p.start()

    for i in range(1000):
        print("main_process", i)

    print("Over!")
