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

# define evaluation function
_webselect = (lambda x,y:webpage.select(y[x])[0].getText().strip())
_value = (lambda x,y: float(_webselect(x,y).replace(',','')) if x in y else 'N/A')

# get interesting features
features['price']       = '#Bse_Prc_tick'
features['volume']      = '#bse_volume'
features['vwap']        = '#b_vwap_val'
features['pclose']      = '#b_prevclose'
features['buyqt']       = '#b_total_buy_qty'
features['sellqt']      = '#b_total_sell_qty'
features['openp']       = '#b_open'
features['tlow']        = '#b_low_sh'
features['thigh']       = '#b_high_sh'
features['52low']       = '#b_52low'
features['52high']      = '#b_52high'

print _value('price',features)
