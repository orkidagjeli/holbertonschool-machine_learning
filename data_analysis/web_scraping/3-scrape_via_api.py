#!/usr/bin/env python3
"""Scrape quotes using the site's API."""

import json

fetch_html = __import__('0-fetch_html').fetch_html


def scrape_via_api(base_url):
    """Fetch quotes from all API pages."""
    all_quotes = []
    page = 1

    while True:
        url = f"{base_url}/api/quotes?page={page}"
        response = fetch_html(url)
        data = json.loads(response)

        for quote in data['quotes']:
            all_quotes.append({
                'text': quote['text'],
                'author': quote['author']['name'],
                'tags': quote['tags']
            })

        if not data['has_next']:
            break

        page += 1

    return all_quotes
