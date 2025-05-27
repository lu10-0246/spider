import scrapy


class TcSpider(scrapy.Spider):
    name = "tc"
    allowed_domains = ["gz.58.com"]
    start_urls = ["http://gz.58.com/"]

    def parse(self, response):
        # print('山东菏泽曹县')
        #获取网页源码
        # content=response.text
        # content=response.body
        # print("==============")
        # print(content)
        span=response.xpath('//div[@id="filter"]/div[@class="tabs"]/a/span')[0]
        print("=============")
        print(span.extract())