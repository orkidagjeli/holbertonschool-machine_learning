#!/usr/bin/env python3
"""Log in and scrape quotes from a protected page."""

import requests
from bs4 import BeautifulSoup


def login_and_scrape(login_url, user, pwd):
    """Log in and return quotes from the protected page."""
    session = requests.Session()

    response = session.get(login_url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    csrf_input = soup.find('input', attrs={'name': 'csrf_token'})
    csrf_token = csrf_input['value']

    credentials = {
        'username': user,
        'password': pwd,
        'csrf_token': csrf_token
    }

    response = session.post(login_url, data=credentials)
    response.raise_for_status()

    quotes_url = 'https://quotes.toscrape.com/'
    response = session.get(quotes_url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    quotes = []

    for quote in soup.select('div.quote'):
        text = quote.select_one('span.text').get_text()
        author = quote.select_one('small.author').get_text()
        tags = [
            tag.get_text()
            for tag in quote.select('div.tags a.tag')
        ]

        quotes.append({
            'text': text,
            'author': author,
            'tags': tags
        })

    return quotes
