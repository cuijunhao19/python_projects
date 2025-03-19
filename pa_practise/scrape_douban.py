import requests
from bs4 import BeautifulSoup

url = "https://www.zongheng.com/rank?nav=default"
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
}
respond = requests.get(url, headers=headers)
print(respond.status_code)

html = respond.text
soup = BeautifulSoup(html, "html.parser")
all_titles = soup.find_all("a", attrs = {"class" : "global-hover"})

for title in all_titles:
    print(title)