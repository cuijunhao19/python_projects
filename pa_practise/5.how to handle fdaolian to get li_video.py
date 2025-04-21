# 目的： 获取梨视频的视频下载地址并下载到video文件夹
# 注：该篇要处理防盗链

import requests

url = "https://www.pearvideo.com/video_1798742"
contId = url.split("_")[1]

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0",
    "referer":url
}

video_statusurl = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.7330864095790433"

resp = requests.get(video_statusurl, headers=headers)
dic = resp.json()
resp.close()

srcUrl= dic["videoInfo"]["videos"]["srcUrl"]
systemTime = dic["systemTime"]
srcUrl = srcUrl.replace(systemTime, f"cont-{contId}")
print(srcUrl)

with open("video/"+"a.mp4", mode="wb") as f:
    f.write(requests.get(srcUrl).content)