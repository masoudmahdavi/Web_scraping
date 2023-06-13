#!/usr/bin/env python

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter : ")
html = urllib.request.urlopen(url, context=ctx).read()
print(html)
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
web_address_counter = {}
for tag in tags:
    web_address_counter[tag.get('href', None)] = web_address_counter.get(tag.get('href', None),1) + 1
#print(web_address_counter)

