# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazoncrawlItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
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
