# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazoncrawlItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    page_num = 2
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/s?k=boxing+gloves&crid=DKZB67KXKHAK&sprefix=boxing%2Caps%2C347&ref=nb_sb_ss_i_1_5']

    def parse(self, response):
        items = AmazoncrawlItem()

        data = response.css('.s-include-content-margin')
        for item in data:
            name = item.css('.a-color-base.a-text-normal').css('::text').extract()
            price = item.css('.a-price-whole::text').extract()
            imagelink = item.css('.s-image::attr(src)').extract()

            items['name'] = name
            items['price'] = price
            items['imagelink'] = imagelink

            yield items

        next_page = 'https://www.amazon.com/s?k=boxing+gloves&page=' + str(AmazonSpiderSpider.page_num) + '&crid=DKZB67KXKHAK&qid=1557863534&sprefix=boxing%2Caps%2C347&ref=sr_pg_2'
        if AmazonSpiderSpider.page_num <= 3:
            AmazonSpiderSpider.page_num += 1
            yield response.follow(next_page, callback=self.parse)
