import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.set_page_load_timeout(30)

# 页数

browser.get("http://www.17huo.com/newsearch/?k=%E5%A4%A7%E8%A1%A3")

page_info = browser.find_element_by_css_selector("body > div.wrap > div.search_container > div.pagem.product_list_pager > div")
#共 40 页，每页 60 条

print(page_info.text)