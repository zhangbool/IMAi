#by 寒小阳(hanxiaoyang.ml@gmail.com)

import scrapy


class CnBlogSpider(scrapy.Spider):
    name = "cnblogs"
    allowed_domains = ["cnblogs.com"]
    start_urls = [
        'http://www.cnblogs.com/pick/#p2'
        ]

    def parse(self, response):
        for article in response.xpath('//div[@class="post_item"]'):
            print(article.xpath('div[@class="post_item_body"]/h3/a/text()').extract_first().strip())
            print("----------------------------------------------------------------------------------")

            yield {
                'title': article.xpath('div[@class="post_item_body"]/h3/a/text()').extract_first().strip(),
            	}

