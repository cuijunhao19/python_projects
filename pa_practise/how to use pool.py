# 线程池：一次性开辟一些线程去执行任务

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def fn(name):
    for i in range(1, 100):
        print(name, i)


if __name__ == '__main__':
    # 创建线程池
    with ThreadPoolExecutor(50) as t:
        for i in range(1, 10):
            t.submit(fn, name=f"thread{i}")

    print("over!")