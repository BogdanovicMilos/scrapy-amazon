# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazoncrawlItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    page_num = 2
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/s?k=boxing+gloves&ref=nb_sb_noss']

    def parse(self, response):
        items = AmazoncrawlItem()

        name = response.css('.a-color-base.a-text-normal').css('::text').extract()
        price = response.css('.a-price-whole::text').extract()
        imagelink = response.css('.s-image::attr(src)').extract()

        items['name'] = name
        items['price'] = price
        items['imagelink'] = imagelink

        yield items

        next_page = 'https://www.amazon.com/s?k=boxing+gloves&page=' + str(AmazonSpiderSpider.page_num) + '&qid=1557483146&ref=sr_pg_2'
        if AmazonSpiderSpider.page_num <= 5:
            AmazonSpiderSpider.page_num += 1
            yield response.follow(next_page, callback=self.parse)
