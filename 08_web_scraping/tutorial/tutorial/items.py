# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
    text = scrapy.Field()
    born_date = scrapy.Field()
    born_location = scrapy.Field()

    images = scrapy.Field()
    image_urls = scrapy.Field()


                    
