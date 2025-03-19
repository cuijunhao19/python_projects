import requests

# 获取用户输入的单词
s = input("Please input a word: ")

# 构造请求数据
data = {
    "from": "en",
    "to": "zh-Hans",
    "text": s,  # 使用用户输入的单词
    "token": "i4qpnaUhiCMSnLc4AbFEuH4aMLI9HHzF",
    "key": "1741702565649"
}

# 请求URL
url = "https://cn.bing.com/tlookupv3?&IG=EDB7FAAF18C4447D88FD4702768E43F2&IID=SERP.5696.3"

# 请求头
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
}

# 发送POST请求
response = requests.post(url, data=data, headers=headers)

# 打印响应状态码和内容
print("Status Code:", response.status_code)
print("Response Text:", response.text)

# 解析JSON响应（假设返回的是JSON格式）
try:
    translated_text = response.json().get("translatedtext", "No translation found")
    print("Translated Text:", translated_text)
except ValueError:
    print("Failed to parse JSON response.")