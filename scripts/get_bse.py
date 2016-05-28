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
bse_span = webpage.select('#Bse_Prc_tick')[0]
bse_value = bse_span.getText().strip()

print bse_value
