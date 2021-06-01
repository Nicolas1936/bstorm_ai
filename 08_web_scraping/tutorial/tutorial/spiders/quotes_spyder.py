import scrapy
from scrapy.http.request.form import _urlencode
from scrapy.pipelines.images import ImagesPipeline

from ..items import TutorialItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):

        quotes = response.css('div.quote')

        for quote in quotes:
            item = {}
            item['text'] = quote.css('span.text::text').get()
            item['author'] = quote.css('small.author::text').get()
            item['tags'] = quote.css('div.tags a.tag::text').getall()
            author_bio_link = quote.css('span a::attr(href)').get()

            
            yield response.follow(author_bio_link, meta={'item' : item}, callback=self.parse_author, dont_filter=True)

        quote_next_link = response.css('li.next a::attr(href)').get()
        if quote_next_link is not None:
            yield response.follow(quote_next_link, callback=self.parse)

    def parse_author(self, response):

        item = response.meta.get('item')
        
        born_date = response.css('p span.author-born-date::text').get()
        born_location  = response.css('p span.author-born-location::text').get()

        item['born_date'] = born_date
        item['born_location'] = born_location

        author_clean = "_".join(item['author'].split())

        link_picture = "https://en.wikipedia.org/wiki/" + item['author']

        yield response.follow(link_picture, meta={'item' : item}, callback=self.parse_picture, dont_filter=True)

        #yield item

    def parse_picture(self, response):
        
        item = response.meta.get('item')
            
        url_picture = response.css('div a.image img::attr(src)').get()

        if url_picture is not None:
            url_picture = 'https:' + url_picture.replace('220px', '1280px')
            item['image_urls'] = [url_picture]

        yield item
