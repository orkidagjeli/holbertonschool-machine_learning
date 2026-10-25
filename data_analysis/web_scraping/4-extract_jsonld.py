#!/usr/bin/env python3
"""Extract quotes from JSON-LD embedded in a webpage."""

import json
from bs4 import BeautifulSoup

fetch_html = __import__('0-fetch_html').fetch_html


def extract_jsonld(url):
    """Extract quote text, author, and tags from JSON-LD."""
    html = fetch_html(url)
    soup = BeautifulSoup(html, 'html.parser')

    results = []

    scripts = soup.find_all(
        'script',
        type='application/ld+json'
    )

    for script in scripts:
        if not script.string and not script.get_text(strip=True):
            continue

        content = script.string or script.get_text(strip=True)

        try:
            data = json.loads(content)
        except json.JSONDecodeError:
            continue

        objects = data if isinstance(data, list) else [data]

        for obj in objects:
            if not isinstance(obj, dict):
                continue

            if obj.get('@type') != 'Quote':
                continue

            tags = obj.get('keywords', [])

            if isinstance(tags, str):
                tags = [
                    tag.strip()
                    for tag in tags.split(',')
                    if tag.strip()
                ]

            results.append({
                'text': obj.get('text'),
                'author': obj.get('author', {}).get('name')
                if isinstance(obj.get('author'), dict)
                else None,
                'tags': tags if isinstance(tags, list) else []
            })

    return results
