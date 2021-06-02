# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 16:50:22 2021

@author: romain
"""

import scrapy
import pandas as pd
# =============================================================================
# 
# =============================================================================
class PlayerStats(scrapy.Spider):
    name = 'main_v1'
    start_urls = pd.read_csv('data_url.csv', usecols=['urls'])['urls'].to_list()
    
    def parse(self, response):
        print(response)