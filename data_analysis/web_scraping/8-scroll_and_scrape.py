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

        by = webdriver.common.by.By

        # Scroll until the page stops growing or 50 rounds are reached.
        last_height = driver.execute_script(
            "return document.body.scrollHeight"
        )

        for _ in range(50):
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )
            time.sleep(min(scroll_pause, 0.5))

            new_height = driver.execute_script(
                "return document.body.scrollHeight"
            )

            if new_height == last_height:
                break

            last_height = new_height

        # Extract products and skip duplicates.
        products = []
        seen = set()

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
