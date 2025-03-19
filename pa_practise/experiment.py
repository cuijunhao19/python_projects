import requests

url = "https://movie.douban.com/j/chart/top_list"

#伪装游览器请求头
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
}


#封装参数
params = {
    "type": "24",
    "interval_id": "100:90",
    "action":"" ,
    "start": "0",
    "limit": "20"
}


respond = requests.get(url=url, headers=headers, params=params)

print(respond.url)
print(respond.status_code)
#print(respond.json())
respond.close()