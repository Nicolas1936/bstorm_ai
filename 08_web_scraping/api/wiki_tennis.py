import requests as rq
from pprint import pprint
import time

time.sleep(0.5)
r = rq.get('https://en.wikipedia.org/w/api.php?action=opensearch&format=json&formatversion=2&search=roger%20federer')

print(r.status_code)

dict_ = r.json()
pprint(dict_[3][0])