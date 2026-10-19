
#!/usr/bin/env python3
"""List starships that can carry a given number of passengers."""

import requests


def availableShips(passengerCount):
    """Return ships that can hold at least passengerCount passengers."""
    url = "https://swapi-api.hbtn.io/api/starships/"
    ships = []

    while url:
        response = requests.get(url)
        if response.status_code != 200:
            break

        data = response.json()

        for ship in data["results"]:
            passengers = ship.get("passengers")

            if passengers is None:
                continue

            passengers = str(passengers).strip().lower()

            if passengers in ("unknown", "n/a", "null", ""):
                continue

            try:
                capacity = int(passengers.replace(",", ""))
            except ValueError:
                continue

            if capacity >= passengerCount:
                ships.append(ship["name"])

        url = data["next"]

    return ships
