#!/usr/bin/env python3
"""Scrape quotes, authors, and tags from a web page."""


from bs4 import BeautifulSoup

fetch_html = __import__('0-fetch_html').fetch_html


def scrape_basic(url):
    """Extract quotes, authors, and tags from the first page."""
    html = fetch_html(url)
    soup = BeautifulSoup(html, 'html.parser')

    quotes_data = []

    for quote in soup.select('div.quote'):
        text = quote.select_one('span.text').get_text()
        author = quote.select_one('small.author').get_text()
        tags = [
            tag.get_text()
            for tag in quote.select('div.tags a.tag')
        ]

        quotes_data.append({
            'text': text,
            'author': author,
            'tags': tags
        })

    return quotes_data
