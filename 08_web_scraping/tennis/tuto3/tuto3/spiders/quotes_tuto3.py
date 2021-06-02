import scrapy
import pandas as pd


class QuotesSpider(scrapy.Spider):
    name = "tennis"

    test = pd.read_csv('data_with_url.csv', usecols=['wiki_url'])
    url_list = test[:20]['wiki_url'].tolist()
    print('aaaaaaaaaaaaaaa')
    #print(url_list)

    start_urls = url_list

    def parse(self, response):
        dict_ = {}
        dict_['born_date'] = response.css('span.bday::text').get()
        dict_['born_city'] = response.css('table.infobox').xpath('//tr[th="Born"]').css('a::text').get()
        dict_['born_country'] = response.css('table.infobox').xpath('//tr[th="Born"]').css('td::text').getall()[1].strip(', ')

        yield dict_

"""
class QuotesSpider(scrapy.Spider):
    name = "tennis"

    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        author_page_links = response.css('.author + a')
        print('aaaaaaaaaaaaaaaaa')
        print(author_page_links)
"""