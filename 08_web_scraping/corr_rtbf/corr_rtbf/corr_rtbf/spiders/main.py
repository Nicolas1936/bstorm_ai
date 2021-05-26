"""
Created on Wed May 26 09:02:35 2021

@author: romain
"""
import scrapy
# =============================================================================
# 
# =============================================================================
class RtbfArticles(scrapy.Spider):
    name = 'rtbf_spider_v1'
    start_urls = ['https://www.rtbf.be/info/archive_accueil?dossier=553']
    
    def __init__(self):
        self.counter = 1
    
    def parse(self, response):
        self.counter += 1
        art_types = ['article.rtbf-article-grid__item.rtbf-article-grid__item--row.col-xs-12.col-sm-4',
                     'article.rtbf-article-grid__item.rtbf-article-grid__item--row.rtbf-article-grid__item--no-border.col-xs-12.col-sm-12',
                     'article.rtbf-article-grid__item.rtbf-article-grid__item--row-text.col-xs-12']
        
        for type_ in art_types:
            articles = response.css(type_)
            for article in articles:
                item = {}
                item['time'] = article.css('header time.www-time::attr(datetime)').get()
                link = article.css('::attr(href)').get()
                yield response.follow(link, callback=self.article_parse, meta={'item':item})
        
        next_page = 'https://www.rtbf.be/info/archive_accueil?page=%s&dossier=553'%self.counter
        yield response.follow(next_page, callback=self.parse)
        
    def article_parse(self, response):
        item = response.meta['item']
        title = response.css('h1.rtbf-article-main__title::text').get()
        title = title.strip()
        item['title'] = title
        item['author'] = response.css('div.rtbf-article-main__author cite span span::text').get()
        yield item