#!/usr/bin/env python3
"""Get the location of a GitHub user."""

import sys
import time
import requests


if __name__ == '__main__':
    url = sys.argv[1]

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data.get('location'))

    elif response.status_code == 404:
        print("Not found")

    elif response.status_code == 403:
        reset = int(response.headers['X-RateLimit-Reset'])
        current_time = time.time()

        minutes = int((reset - current_time) / 60)

        print("Reset in {} min".format(minutes))
