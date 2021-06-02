import requests as rq
import cloudscraper


#headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
#headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0",
#            "Referer": "https://www.atptour.com/en/players/roger-federer/f324/overview"}
#
#r = rq.get('https://www.atptour.com/en/-/ajax/playersearch/PlayerUrlSearch?searchTerm=Gardnar%20Mulloy', 
#            headers=headers)
#print(r.status_code)
#
#print(r.status_code)
#print(r.content)

scraper = cloudscraper.create_scraper()
r = scraper.get('https://www.atptour.com/en/-/ajax/playersearch/PlayerUrlSearch?searchTerm=Gardnar%20Mulloy')
dict_ = r.json()
print(dict_)