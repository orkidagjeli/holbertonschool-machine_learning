#!/usr/bin/env python3
import json
from bs4 import BeautifulSoup
scrape_basic = __import__('1-scrape_basic').scrape_basic
data = scrape_basic("https://quotes.toscrape.com/")
print(json.dumps(data[:2], indent=2))
