import requests

session = requests.session()

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
}

url = "https://passport.17k.com/ck/user/login"

# data = {
#     "loginName": "shjdvhh",
#     "password": "15976576602Cjh.@"
# }

# session.post(url, data=data, headers=headers)
# resp = session.get("xxx")
# resp.close()

resp = session.get("https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919", headers={
    "Cookie":"GUID=83e0d40b-3459-4d6e-ba4e-85fe745e9214; sajssdk_2015_cross_new_user=1; Hm_lvt_9793f42b498361373512340937deb2a0=1742996018; HMACCOUNT=68C213D3BA5AA50E; c_channel=0; c_csc=web; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F01%252F41%252F83%252F104058341.jpg-88x88%253Fv%253D1742996141000%26id%3D104058341%26nickname%3Dshjdvhh%26e%3D1758549830%26s%3Dc041a6d39055ddf5; tfstk=g4MZa3ZLfdpN2kHwok2VTuLhR-wTnRYW7xabmmm0fP4ghCU0om3Lcti0swY48qU_1R0juZusRP0qDhE0oq04lfOBFcnTH-Y53L9SX78Uj_uai5XHmorRoHNMfmdu1-YWPps-9UsznVMS_AQExyE4mlqioMxU0u2cISXGtw4Lm-20iP2nxorbotX0oHo3Jo20oqViBQygdEr0sn81RlL1QnFgrc4FnTS8f5jrbs6AHvra_xmg8lrZLlParWBNhBMiRmDsBWddO-nIaqlmre1_Sbrr87GwzOurWo0UCYxv6WFm3xrK9E54zjmswjVejdmUQPPmd2j59RlmWxPt_iK-xR0KwzFM9eEECYN4yW7HSDiUS7lq5eB05bon87MCRTwow2k4Z8jPQZE3d6Hx_Zf0skEUPH-FUDSKyF8hbj5AM5n8YztZasCYskEUPH-FMsFTykzWbb5..; acw_sc__v2=67e40947b8f645187952de6d7ef2239f27a199dd; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22104058341%22%2C%22%24device_id%22%3A%22195d2a89307995-0b646df2789943-4c657b58-1058400-195d2a8930826aa%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%2283e0d40b-3459-4d6e-ba4e-85fe745e9214%22%7D; ssxmod_itna=eqRxcCD=KYqCT4BPqB4DK3dtGQ42xD5GO7jK1+459DBk0Y4iNDnD8x7YDv+jT46Q24qqFQ7Aa2rk7D0Kd64pD8ueq8g7i+Fiqfx0aDbqGkpeKxiiSDCeDIDWeDiDG4GmKqGtDpxG=Djey1M2yCDYPDEeYDRPKDuO7+DGpz26I+DeKD0rT7DQFwnOxDBOrEFmiTAcW+DiW73fHvB=4LqQiCD7HwDlpxM8rCORLXFDYLn8Mh6jKDX2QDv25pycoPno7s5t2FQYhHhexbqQRDhi0WwWcK5ieewQbQTg0iwDnWket/FDDW+Q2K4D; ssxmod_itna2=eqRxcCD=KYqCT4BPqB4DK3dtGQ42xD5GO7jK1+45D8wp2YO04GNDkbjDFOCYW5Ij8D8hhUhqnp7e=moycLErAh8bG5Nkn9pe56e75pG9NwwfpQOQ8KTI7C8GqKqzmR8CXuKYNdQAZmt9BDGSDPrQW0re75q9iDqpne55gisTzpTHtnYO9qNetnb5ZgO=Zqb59m1q1pEY1nQGbqLUFwpqZwm/eLO82MiF8SD9CW2I8yteQDGA8F=vo7+3OwohImrQebc19QE8dBk=x9DIr7Hl0jAZcYoF7DOQD9iNbzvQXqjKGAxS0MYQhzVB=lYGqBG32QwxoGwGwDzYoeZuDSSNCf=ihoow5eBKKEY9rCKA7PrHwOetdwnfsrm5woTZqGnSYIhooOY2nI2ftwosYWIC3F9rQv3F5u+qGapw5im7d+5Y=scoGGdAepzKbihf7orb+Rtt1e8hh431T+NNmK4qfj2YS+ohDwUldVB7Qox5LGP4F+7bgT71eoBRaKeH5khd6Yu=A04ATEGjDDwOqk7xke4BjwiiG+gDwiOdwODpm=ygNMDDjKDeu44D; Hm_lpvt_9793f42b498361373512340937deb2a0=1742998514"
})
print(resp.status_code)
print(resp.json())