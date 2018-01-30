# -*- coding: utf-8 -*-
import scrapy


class GetairapiSpider(scrapy.Spider):
    name = 'getAirAPI'
    allowed_domains = ['http://pm25.in/shanghai']
    start_urls = ['http://pm25.in/shanghai']

    def parse(self, response):

        print("----------------------getAirAPI---start------------------------------")



        print("----------------------getAirAPI----end------------------------------")

        pass
