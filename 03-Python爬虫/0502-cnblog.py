#爬取一下博客园的数据
import scrapy

class cnBlogSpider(scrapy.Spider):
    name = "cnblog"
    start_urls = ["https://www.cnblogs.com/pick/#p2"]

    def parse(self, response):

        print("---------------------------start---------------------------")
        print(response.url)
        print("---------------------------end---------------------------")

        print("==========================start=============================")
        result = response.xpath('//div[@class="post_item"]')
        # print(result)
        for item in result:
            print("-------------------------------------------------------------------------------\n")
            # print(item.xpath('div[@class="digg"]/div/span').extract_first())
            print(item.xpath('div[@class="post_item_body"]/h3/a/text()').extract_first())
            print(item.xpath('div[@class="post_item_body"]/p/tet()').extract_first())
            print("----------------------------------------------------------------------------------------\n")


        print("==========================end=============================")


