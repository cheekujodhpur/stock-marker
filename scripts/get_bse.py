#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

# URL to Request
url = 'http://www.moneycontrol.com/india/stockpricequote/computers-software-training/careerpoint/CPI05'

# Downloading webpage having BSE data
res = requests.get(url)
res.raise_for_status()

# parsing webpage
webpage = BeautifulSoup(res.text, "lxml")

features = {}

# get interesting features
features['value']       = webpage.select('#Bse_Prc_tick')[0].getText().strip()
features['volume']      = webpage.select('#bse_volume')[0].getText().strip()
features['vwap']        = webpage.select('#b_vwap_val')[0].getText().strip()
features['pclose']      = webpage.select('#b_prevclose')[0].getText().strip()
features['buyqt']       = webpage.select('#b_total_buy_qty')[0].getText().strip()
features['sellqt']      = webpage.select('#b_total_sell_qty')[0].getText().strip()
features['openp']       = webpage.select('#b_open')[0].getText().strip()
features['tlow']        = webpage.select('#b_low_sh')[0].getText().strip()
features['thigh']       = webpage.select('#b_high_sh')[0].getText().strip()
features['52low']       = webpage.select('#b_52low')[0].getText().strip()
features['52high']      = webpage.select('#b_52high')[0].getText().strip()

# clean up
for feature in features:
    features[feature] = float(features[feature].replace(',',''))

print features
