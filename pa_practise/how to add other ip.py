import requests

ip = "xxx.xxx.xxx:xxxx"
proxies = {
    "https" : f"https://{ip}"
}

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
}

url = "https://www.baidu.com"

resp = requests.get(url, headers=headers, proxies=proxies)
print(resp.status_code)