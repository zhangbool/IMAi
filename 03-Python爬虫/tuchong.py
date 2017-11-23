
# 原来图虫的图片是可以下载的

import requests
from bs4 import BeautifulSoup

response = requests.get("https://tuchong.com/2604463/", allow_redirects = True)
content = BeautifulSoup(response.text, "html.parser")

# widget-gallery
gallery = content.find_all(name="a", class_="")


# print(str(result.content, "utf-8"))
