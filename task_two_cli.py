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
import argparse
import json
import requests

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


def main() -> tuple:
    parser = argparse.ArgumentParser(description= "fetching data from swapi.api")

    parser.add_argument("-c", default= 'characters')
    parser.add_argument("-p", default= "planets")
    parser.add_argument("-v", default= "vehicles")
    argument = parser.parse_args()
    print(f"Parsed arguments are {argument}")
    obj = (argument.c, argument.p, argument.v)
    return obj


def second_task(data_: Dict) -> List:
    """pull data from swapi characters sequentially"""
    for i in main():
        characters = data_.get(i)  # returns None by default
        names = []
        for character in characters:
            character_data = hit_url(character)
            character_data = character_data.json()
            names.append(character_data.get("name"))

        pprint(names)


if __name__ == "__main__":
    second_task(first_task())