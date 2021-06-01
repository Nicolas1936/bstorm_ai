# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class RtbfItem(scrapy.Item):
    time = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    images = scrapy.Field()
    image_urls = scrapy.Field()
    pass
