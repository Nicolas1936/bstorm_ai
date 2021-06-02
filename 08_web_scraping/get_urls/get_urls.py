# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 14:04:25 2021

@author: romain
"""
import numpy as np
import pandas as pd
import requests as rq
import time
# =============================================================================
# 
# =============================================================================
def get_url(data):
    time.sleep(0.1)
    search_item = data['first_name']+' '+data['last_name']
    r = rq.get('https://en.wikipedia.org/w/api.php?action=opensearch&format=json&formatversion=2&search=%s'%search_item)
    json = r.json()
    if len(json[3]) < 1:
        return np.nan
    return json[3][0]
# =============================================================================
# 
# =============================================================================
data = pd.read_csv('data.csv', header=None, names=['PK_player','first_name',
                                                     'last_name','hand','born_date','country'])
data = data.sample(500)
data['last_name'] = data['last_name'].astype(str)
data['first_name'] = data['first_name'].astype(str)

data['urls'] = data.apply(get_url, axis=1)
data = data.dropna(subset=['urls'])

data.to_csv('data_url.csv', index=False)











