# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 09:35:48 2021

@author: arturoguizar
"""

import requests
import pandas as pd

def fetch_bbquote(n_quotes):
    url = 'https://breaking-bad-quotes.herokuapp.com/v1/quotes'
    if n_quotes > 0:
        url = f'{url}/{str(n_quotes)}'
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        return data
    else:
        return None


def transform_bbquote_data(json_response):
    columns = ['author','quote']
    bbquote_df = pd.DataFrame(columns=columns)
    
    for index, row in enumerate(json_response):
        bbquote_df.loc[index,'author'] = row['author']
        bbquote_df.loc[index,'quote'] = row['quote']
    return bbquote_df