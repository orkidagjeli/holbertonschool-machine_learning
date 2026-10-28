#!/usr/bin/env python3
"""Scrape details from a single product page."""

import time
from selenium import webdriver


def scrape_product_detail(url, delay=2.0):
    """Return details for one product."""
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        time.sleep(delay)

        title = driver.find_elements(
            webdriver.common.by.By.CSS_SELECTOR,
            '.caption h4'
        )[1].text

        price = driver.find_element(
            webdriver.common.by.By.CSS_SELECTOR,
            'h4.price'
        ).text

        description = driver.find_element(
            webdriver.common.by.By.CSS_SELECTOR,
            'p.description'
        ).text

        stars = driver.find_elements(
            webdriver.common.by.By.CSS_SELECTOR,
            '.ratings p.ws-icon.ws-icon-star'
        )
        rating = len(stars)

        return {
            'title': title,
            'price': price,
            'description': description,
            'rating': rating
        }

    finally:
        driver.quit()
