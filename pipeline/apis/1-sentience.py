#!/usr/bin/env python3
"""Find the home planets of all sentient species."""

import requests


def sentientPlanets():
    """Return the names of the home planets of sentient species."""
    url = "https://swapi-api.hbtn.io/api/species/"
    planets = []

    while url:
        response = requests.get(url)
        data = response.json()

        for species in data['results']:
            classification = species['classification'].lower()
            designation = species['designation'].lower()

            if 'sentient' in classification or 'sentient' in designation:
                homeworld = species['homeworld']

                if homeworld:
                    planet_response = requests.get(homeworld)
                    planet = planet_response.json()['name']

                    if planet not in planets:
                        planets.append(planet)

        url = data['next']

    return planets
