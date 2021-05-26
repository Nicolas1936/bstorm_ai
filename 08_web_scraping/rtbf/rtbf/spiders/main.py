import scrapy

class RtbfArticles(scrapy.Spider):

    #Fournir un nom
    name = 'main_v1'

    #Donner une url
    start_urls = ['https://www.rtbf.be/info/archive_accueil?dossier=553']

    def parse(self, response):
        articles = response.css('article.rtbf-article-grid__item.rtbf-article-grid__item--row.col-xs-12.col-sm-4')

        print('aaaaaaaaaaaaaaaaaaaa', len(articles))

        item = {}

        for article in articles:
            item['time'] = article.css('header time.www-time::attr(datetime)').get()
            #item['title'] = article.css('::attr(href)').get()

            link = article.css('::attr(href)').get()
            yield response.follow(link, callback=self.article_parser, meta={'item':item})

            #yield item


    def article_parser(self, response):
        item = response.meta['item']

        title = response.css('h1.rtbf-article-main__title.col-xs-12.col-md-8.www-col-full-width::text').get()
        #title = title.replace('\n', '').strip()
        title = title.strip()
        item['title'] = title

        item['authors'] = response.css('div.rtbf-article-main__author cite span span::text').get()

        yield item
