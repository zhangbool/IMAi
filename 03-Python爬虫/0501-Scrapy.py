
#爬取一下julyEdu的数据

import scrapy
from binstar_client.inspect_package.uitls import extract_first


class JulyEduSpider(scrapy.Spider):
    name = "julyEdu"
    start_urls = ["https://www.julyedu.com/category/index"]

    def parse(self, response):
        for julyEdu_class in response.xpath('//div[@class="course_info_box"]'):
            print(julyEdu_class.xpath('a/h4/text()')).extract_first()#//*[@id="item_11"]/div[1]/div/a[1]/h4

            yield  {'title':julyEdu_class.xpath('a/h4/text()').extract_first()}


