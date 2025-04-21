# aiohttp模块的应用
# pip install aiohttp 
import asyncio
import aiohttp
import aiofiles

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
}

urls = [
    "https://www.umei.cc/d/file/20230914/c556c6fc88490700fbdc2a983890fb77.jpg",
    "https://www.umei.cc/d/file/20230914/51ebf12784a697444e9df9a59f3aaaf2.jpg",
    "https://www.umei.cc/d/file/20230914/f16eacf43b6476fa4eb24d8f22e0c22f.jpg"
]
    
async def aiodownload(url):
    # s = aiohttp.ClientSession() <--> requests
    name = url.rsplit("/", 1)[1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as resp:
            content = await resp.content.read()
            with open("img/"+name, mode="wb") as f:
                f.write(content)
    print(name, "OK")

async def aiomain():
    tasks = []
    for url in urls:
        tasks.append(aiodownload(url))
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(aiomain())


