# 目的：获取网易云音乐的热评
# 1.找到未加密的参数，想办法加密（要参照网易云的逻辑）params,encSecKey
# 2.请求到网易云，拿到评论


import requests
import re

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
}

url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token=e5200019e59d032f881e27258e161f1d"

# 请求方式是post
