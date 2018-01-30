# -*- coding: utf-8 -*-
import scrapy
import codecs
import requests
from bs4 import BeautifulSoup


# 城市对象模型
class City:
    def __init__(self, name, url):
        self.name = name
        self.url =url

# 爬虫程序
class GetcitySpider(scrapy.Spider):

    name = 'getCity'
    allowed_domains = ['http://pm25.in']
    start_urls = ['http://pm25.in']

    # 解析结果
    def parse(self, response):

        print("----------------------------spider-start----------------------------")

        #1，xpath获取所有的城市名
        cityNameList = response.xpath('/html/body/div[2]/div[2]/div[2]/div[2]/ul[@class="unstyled"]/div[2]/li/a/text()').extract()

        #2，xpath获取所有的城市对应数据的url
        # 在a前面用//居然ok了， 嗷嗷嗷！！！
        urlList = response.xpath('/html/body/div[2]/div[2]/div[2]/div[2]/ul[@class="unstyled"]/div[2]/li//a/@href').extract()

        #3，保存城市和url数据
        cities = []
        for i in range(len(cityNameList)):
            city = City(cityNameList[i], "http://pm25.in"+urlList[i])
            cities.append(city)

        #4, 写入保存的数据到文件中(其实这里存不存都无所谓)
        # for city in cities:
        #     print("城市名："+city.name+",url："+city.url)
        #     lineTxt = city.name+" "+city.url+"\n"
        #     f = codecs.open("cityInfo.txt", "a", "utf-8")
        #     f.write(lineTxt)
        #     f.close()

        # #5，开始遍历获取每个城市的空气质量数据
        for city in cities:
            print(city.url)
            content = requests.get(city.url).content.decode("utf8")
            soup = BeautifulSoup(content, "html.parser")

            # print("soup:\n"+soup.text)
            # thead那些标题都是死的，所以这里就不再抓取，直接定义就好了
            # tableHead = soup.thead
            # print("tableHead:\n"+tableHead)

            #5.1, 首先获取发布时间
            dataReleaseTimeSoup = soup.find(attrs={"class": "live_data_time"})
            releaseTimeStr = dataReleaseTimeSoup.contents[1].text
            print("releaseTimeStr:\n"+releaseTimeStr)

            #5.2, 然后获取监测站及相关信息
            print("--------------------------------------monitoringSite---------start----------------------------------------")
            monitoringSitesSoup = soup.find("tbody").children
            for monitoringSiteSoup in monitoringSitesSoup:
                print(monitoringSiteSoup)
                print("000000000")
            print("--------------------------------------monitoringSite----------end---------------------------------------")



            # tableBody = soup.tbody
            # print("tableBody:\n"+tableBody)
            return



        print("----------------------------spider-end----------------------------")
        pass
