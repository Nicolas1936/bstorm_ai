import scrapy
import pandas as pd

class TennisSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]

"""
    data = pd.read_csv('data_with_url.csv')
    wiki_url_list = list(data['wiki_url'].head(20))
    print(wiki_url_list)


    print('aaaaaaaaaaaaaaaa')

    print(wiki_url_list)

    start_urls = 'http://www.google.ch'

    def parse(self, response):
        print('bbbbbbbbbbbb')
"""
