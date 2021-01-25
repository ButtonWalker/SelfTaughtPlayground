from bs4 import BeautifulSoup
import urllib.request
import pprint as pp
import pandas as pd

source = urllib.request.urlopen('https://developers.facebook.com/docs/groups-api/reference').read()

soup = BeautifulSoup(source, 'html.parser')
rows=list()
for row in soup.findAll("tr"):
   rows.append(row)
   pp.pprint(row)