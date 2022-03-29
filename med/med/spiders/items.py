# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MedItem(scrapy.Item):
 
    ANNONCE_LINK=scrapy.Field()
    Maladie=scrapy.Field()
    Question=scrapy.Field()
    Doctor=scrapy.Field()
    Domine=scrapy.Field()
 	 
