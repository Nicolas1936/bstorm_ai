import scrapy

class QuotesAuthors(scrapy.Spider):

    #Fournir un nom
    name = 'main_v2'

    #Donner une url
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        citations = response.css('div.quote')

        print('aaaaaaaaaaaaaaaaaaaa', len(citations))

        for citation in citations:
            item = {}

            item['auteur'] = citation.css('small.author::text').get()
            item['quote'] = citation.css('span.text::text').get()
            item['tags'] = citation.css('div.tags a.tag::text').getall()

            #item['link'] = citation.css('::attr(href)').get()
            link = citation.css('span a::attr(href)').get()

            test =  response.follow(
                    link, 
                    callback=self.citation_parser, 
                    meta={'item':item},
                    dont_filter = True)

            yield test

            #print()
            #print(item['phrase'])
            #print(item['auteur'])

            #yield item


    def citation_parser(self, response):
        item = response.meta['item']

        item['born_date'] = response.css('span.author-born-date::text').get()
        item['author_born_location'] = response.css('span.author-born-location::text').get()

        print('dddddddddddddd')
        print(item)

        yield item