#Web scraper

import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.geeksforgeeks.org/python-web-scraping-tutorial/')

print(r.status_code)

soup = BeautifulSoup(r.content, 'html.parser')

print(soup.prettify())