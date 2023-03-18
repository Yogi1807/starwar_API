"""
The task 2 goes like following:
Pull data for the first movie in star wars
Write the json data into a file named output.txt


SUBTASKS -
1. Output should be only list of names (first name & last name) of characters
in the movie.
2. Output should only print list of planet names used in the movie
3. Output should only print list of vehicle names used in the movie.
"""

import json
import requests

from typing import Dict, List

from utils.fetch_data import hit_url
from flask import Flask, jsonify, Response


FIRST_FILM_URL = "https://swapi.dev/api/films/1/"

app = Flask(__name__)


def write_data_into_file(data: Dict) -> None:
    """writes dict data into a file"""

    with open("output.txt", "w") as fp:
        fp.write(json.dumps(data))


def first_task() -> Dict:
    """Returns a dict object from swapi.dev/api/films/1"""

    response = requests.get(FIRST_FILM_URL)
    result_ = response.json()
    write_data_into_file(result_)
    return result_


def second_task(data_: Dict) -> List:
    """pull data from swapi characters sequentially"""

    characters = data_.get("characters")  # returns None by default

    names = []
    for character in characters:
        character_data = hit_url(character)
        character_data = character_data.json()
        names.append(character_data.get("name"))

    # names = []
    # all_characters = fetch_data(characters)
    # for character in all_characters:
    #     names.append(character.get("name"))

    return names


def third_task(data_: Dict) -> List:
    """pull data from swapi planets sequentially"""

    planets = data_.get("planets")  # returns None by default

    names = []
    for planet in planets:
        planet_data = hit_url(planet)
        planet_data = planet_data.json()
        names.append(planet_data.get("name"))

    return names


def fourth_task(data_: Dict) -> List:
    """pull data from swapi vehicles sequentially"""

    vehicles = data_.get("vehicles")  # returns None by default

    names = []
    for vehicle in vehicles:
        vehicle_data = hit_url(vehicle)
        vehicle_data = vehicle_data.json()
        names.append(vehicle_data.get("name"))

    return names


@app.route("/task2/<resource>")
def get_info(resource):

    match resource:
        case "film1":
            # first task
            data = first_task()
            data_ = json.dumps(data, indent=4)
            return Response(data_, mimetype='application/json')
        case "characters":
            # second task : capture characters
            return json.dumps(second_task(first_task()))

        case "planets":
            # third task : capture planets
            return json.dumps(third_task(first_task()))

        case "vehicles":
            # fourth task: capture vehicles
            return json.dumps(fourth_task(first_task()))

        case _:
            return "Wrong Resource Enter"


if __name__ == "__main__":
    app.run(debug=True)
