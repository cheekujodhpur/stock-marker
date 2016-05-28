#!/usr/bin/env python

from mechanize import Browser
from bs4 import BeautifulSoup

# set up mechanize header
headers = [('User-Agent', 'Mozilla/5.0 (Windows NT 5.1; rv:14.0) Gecko/20100101 Firefox/14.0.1')]

# define target URL
url = "http://www.bseindia.com/getquote.htm"

br = Browser()
br.addheaders = headers

# make request
response = br.open(url)

print response.read()

#close response
response.close()
