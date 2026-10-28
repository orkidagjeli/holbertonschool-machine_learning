#!/usr/bin/env python3
"""Scrape product information using Selenium."""

import time
from selenium import webdriver


def scrape_products(url):
    """Return a list of products from a category page."""
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        time.sleep(2)

        products = []
        by = webdriver.common.by.By
        items = driver.find_elements(by.CSS_SELECTOR, 'div.thumbnail')

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

            rating_element = item.find_element(
                by.CSS_SELECTOR, '.ratings p[data-rating]'
            )
            rating = int(rating_element.get_attribute('data-rating'))

            products.append({
                'title': title,
                'price': price,
                'description': description,
                'rating': rating
            })

        return products

    finally:
        driver.quit()


scrape_products_list = scrape_products
