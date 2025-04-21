# 在python中如何编写协程
import asyncio
import time

async def fun1():
    print("11")
    await asyncio.sleep(3)
    print("111")

async def fun2():
    print("22")
    await asyncio.sleep(5)
    print("222")

async def fun3():
    print("33")
    await asyncio.sleep(4)
    print("333")

async def main():
    tasks = {
        asyncio.create_task(fun1()),
        asyncio.create_task(fun2()),
        asyncio.create_task(fun3())
    }
    await asyncio.wait(tasks)


if __name__ == '__main__':
    
    t1 = time.time()
    asyncio.run(main())
    t2 = time.time()
    print(t2 - t1)   