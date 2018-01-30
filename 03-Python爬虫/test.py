import requests
import scrapy

content = requests.get("http://pm25.in/").content.decode("utf8")
start = content.find('<div class="bottom">')
end = content.find('<!-- end of all -->')

# print(content)


bottom = content.xpath('//div[@class="bottom"]')
print(bottom)



# print(start)
# print(end)
# print(content[start:end])

