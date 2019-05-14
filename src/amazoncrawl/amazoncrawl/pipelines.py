# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3


class AmazoncrawlPipeline(object):
    def __init__(self):
        self.open_connection()
        self.create_table()

    def open_connection(self):
        self.conn = sqlite3.connect('items.db')
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute("DROP TABLE IF EXISTS boxing_gloves")
        self.cursor.execute("CREATE TABLE boxing_gloves (title text, price text, imagelink text)")

    def process_item(self, item, spider):
        self.store_items(item)
        return item

    def store_items(self, item):
        self.cursor.execute("INSERT INTO boxing_gloves VALUES (?,?,?)", (item['name'][0], item['price'][0], item['imagelink'][0]))
        self.conn.commit()
