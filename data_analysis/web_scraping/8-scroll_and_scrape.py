#!/usr/bin/env python3
"""Scrape products from an infinite-scroll page."""

import time
from selenium import webdriver


def scroll_and_scrape(url, scroll_pause=2.0):
    """Scroll through the page and return unique products."""
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        time.sleep(scroll_pause)

        # Scroll until the page height stops increasing.
        previous_height = driver.execute_script(
            'return document.body.scrollHeight'
        )

        while True:
            driver.execute_script(
                'window.scrollTo(0, document.body.scrollHeight)'
            )
            time.sleep(scroll_pause)

            current_height = driver.execute_script(
                'return document.body.scrollHeight'
            )

            if current_height <= previous_height:
                break

            previous_height = current_height

        products = []
        seen = set()

        by = webdriver.common.by.By
        items = driver.find_elements(
            by.CSS_SELECTOR, 'div.thumbnail'
        )

        for item in items:
            title = item.find_element(
                by.CSS_SELECTOR, 'a.title'
            ).get_attribute('title')

            price = item.find_element(
                by.CSS_SELECTOR, 'h4.price'
            ).text

            description = item.find_element(
                by.CSS_SELECTOR, 'p.description'
            ).text

            stars = item.find_elements(
                by.CSS_SELECTOR,
                '.ratings span.ws-icon-star'
            )
            rating = len(stars)

            key = (title, price)

            if key not in seen:
                seen.add(key)
                products.append({
                    'title': title,
                    'price': price,
                    'description': description,
                    'rating': rating
                })

        return products

    finally:
        driver.quit()
