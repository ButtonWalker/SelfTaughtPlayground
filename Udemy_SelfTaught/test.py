import requests
from bs4 import BeautifulSoup
import re
import pprint

url = input("Enter a website to extract the URL's from: ")
# Make a request
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

# Extract title of page
page_title = soup.title.text

# Extract body of page
page_body = soup.body

# Extract head of page
page_head = soup.head

image_data = []

images =  soup.select('img')
for images in images:
    scr = images.get('src')
    alt = images.get('alt')
    image_data.append({'src': scr, 'alt': alt})

hlinks = []
# Extracting all the <a> tags into a list.
tags = soup.find_all('a')

# Extracting URLs from the attribute href in the <a> tags.
for tag in tags:
    htag = tag.get('href')
    #desc = tag.find_all('td')
    hlinks.append({'endpoint': htag})

# print the result
pprint.pprint(hlinks)