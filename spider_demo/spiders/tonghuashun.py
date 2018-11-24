# -*- coding: utf-8 -*-
import scrapy


class TonghuashunSpider(scrapy.Spider):
    name = 'tonghuashun'
    allowed_domains = ['stockpage.10jqka.com.cn']
    start_urls = ['http://basic.10jqka.com.cn/000001/company.html']

    # http://basic.10jqka.com.cn/000001/company.html
    def parse(self, response):
        # /html/body/div[3]/div[3]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[1]/a
        # /html/body/div[3]/div[3]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[1]/a

        res_selector = response.xpath("//*[@class=\"turnto\"]/text()")
        name = res_selector.extract()
        print(name)
        pass
