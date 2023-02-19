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
import argparse

from pprint import pprint
from typing import Dict, List

from utils.fetch_data import hit_url, fetch_data


FIRST_FILM_URL = "https://swapi.dev/api/films/1/"


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


# def second_task(data_: Dict) -> List:
#     """pull data from swapi characters sequentially"""
#
#     characters = data_.get(new()[0])  # returns None by default
#
#     names = []
#     for character in characters:
#         character_data = hit_url(character)
#         character_data = character_data.json()
#         names.append(character_data.get("name"))
#
#     # names = []
#     # all_characters = fetch_data(characters)
#     # for character in all_characters:
#     #     names.append(character.get("name"))
#
#     return names
#
#
# def third_task(data_: Dict) -> List:
#     """pull data from swapi planets sequentially"""
#
#     planets = data_.get(new()[1])  # returns None by default
#
#     names = []
#     for planet in planets:
#         planet_data = hit_url(planet)
#         planet_data = planet_data.json()
#         names.append(planet_data.get("name"))
#
#     return names
#
#
# def fourth_task(data_: Dict) -> List:
#     """pull data from swapi vehicles sequentially"""
#
#     vehicles = data_.get(new()[2])  # returns None by default
#
#     names = []
#     for vehicle in vehicles:
#         vehicle_data = hit_url(vehicle)
#         vehicle_data = vehicle_data.json()
#         names.append(vehicle_data.get("name"))
#
#     return names


# def new():

parser = argparse.ArgumentParser(description= "passing information")

parser.add_argument("-c", "--character" )
parser.add_argument("-p", "--planets")
parser.add_argument("-v", "--vehicle")

arguments = parser.parse_args()

ans = (arguments.character, arguments.planets, arguments.vehicle)

for i in ans:
    def second_task(data_: Dict) -> List:
        """pull data from swapi characters sequentially"""

        characters = data_.get(i)  # returns None by default

        names = []
        for character in characters:
            character_data = hit_url(character)
            character_data = character_data.json()
            names.append(character_data.get("name"))

        return names




if __name__ == "__main__":

    print(second_task(first_task))

    # # first task
    # first_result = first_task()
    # pprint(first_result)
    #
    # # second task : capture characters
    # second_result = second_task(first_result)
    # pprint(second_result)
    #
    # # third task : capture planets
    # third_result = third_task(first_result)
    # pprint(third_result)
    #
    # # fourth task: capture vehicles
    # fourth_result = fourth_task(first_result)
    # pprint(fourth_result)
    #
    # print("hello")