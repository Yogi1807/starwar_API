"""
TODO
1. Pull data for the first movie ("A New Hope") and save in DB.
2. Replace the data for each endpoint listed in the JSON object and insert
that data into database table
For example - "A new hope" movie has following resource endpoints -
- characters 15
- planets  7
- starships   10
- vehicles  5
- species  40
"""
from multiprocessing.pool import ThreadPool
from pydantic import parse_obj_as
from typing import List

from resources.films import Film   # resource model
from models.datamodels.films import Film_  # pydantic model
from models.datamodels.characters import Character_
from models.datamodels.planets import Planet_
from models.datamodels.starships_ import StarShips_
from models.datamodels.vehicles import Vehicle_
from models.datamodels.species_ import Species_

from dal.db_conn_helper import get_db_conn
from dal.dml import insert_resource
from utils.fetch_data import fetch_data_v2
from utils.timing import timeit

pool = ThreadPool(5)


def film1():
    data = Film().get_sample_data(id_=1)
    film_data = Film_(**data)

    # create DB connection
    conn = get_db_conn()

    film_columns = [
        "title",
        "opening_crawl",
        "director",
        "producer",
        "release_date",
        "created",
        "edited",
        "url",
    ]

    film_values = [
        film_data.title,
        film_data.opening_crawl,
        film_data.director,
        film_data.producer,
        film_data.release_date,
        film_data.created.strftime("%y-%m-%d"),
        film_data.edited.strftime("%y-%m-%d"),
        film_data.url,
    ]

    result = insert_resource(
        "film", "film_id", film_data.episode_id, film_columns, film_values
    )
    return film_data


@timeit
def store_characters():
    characters = film1().characters    # list of characters_url
    characters_data = []

    char_columns = [
        "name",
        "height",
        "mass",
        "hair_color"
    ]

    character = pool.map(fetch_data_v2, characters)
    characters = parse_obj_as(List[Character_], character)
    for char in characters:
        char_values = [
            char.name,
            char.height,
            char.mass,
            char.hair_color
        ]

        char_id = int(char.url.split("/")[-2])
        result = insert_resource(
            "characters",
            "char_id",
            char_id,
            char_columns,
            char_values
        )
        characters_data.append(char)
    return characters_data


@timeit
def store_planets():
    planets = film1().planets
    planet_data = []

    planets_columns = [
        "name",
        "rotation_period",
        "orbital_period",
        "diameter",
        "climate",
        "gravity",
        "terrain",
        "surface_water",
        "population"
    ]
    planet = pool.map(fetch_data_v2, planets)
    planets = parse_obj_as(List[Planet_], planet)
    for pla_ in planets:
        pla_values = [
            pla_.name,
            pla_.rotation_period,
            pla_.orbital_period,
            pla_.diameter,
            pla_.climate,
            pla_.gravity,
            pla_.terrain,
            pla_.surface_water,
            pla_.population
        ]

        planet_id = int(pla_.url.split("/")[-2])
        result = insert_resource(
            "planet",
            "planet_id",
            planet_id,
            planets_columns,
            pla_values
        )
        planet_data.append(pla_)
    return planet_data


@timeit
def store_starships():
    starships = film1().starships
    starship_data = []

    star_columns = [
        "name",
        "manufacturer",
        "cost_in_credits",
        "length",
        "max_atmosphering_speed",
        "passengers",
        "cargo_capacity",
        "consumables",
        "hyperdrive_rating",
        "MGLT",
        "starship_class",
        "model",
    ]

    starship = pool.map(fetch_data_v2, starships)
    starships = parse_obj_as(List[StarShips_], starship)
    for star in starships:
        star_values = [
            star.name,
            star.manufacturer,
            star.cost_in_credits,
            star.length,
            star.max_atmosphering_speed,
            star.passengers,
            star.cargo_capacity,
            star.consumables,
            star.hyperdrive_rating,
            star.MGLT,
            star.starship_class,
            star.model,
        ]

        star_id = int(star.url.split("/")[-2])
        result = insert_resource(
            "starship",
            "starship_id",
            star_id,
            star_columns,
            star_values
        )
        starship_data.append(star)
    return starship_data


@timeit
def store_vehicles():
    vehicles = film1().vehicles
    vehicle_data = []

    veh_columns = [
        "cargo_capacity",
        "consumables",
        "cost_in_credits",
        "crew",
        "length",
        "manufacturer",
        "max_atmosphering_speed",
        "model",
        "name",
        "vehicle_class"
    ]

    vehicle = pool.map(fetch_data_v2, vehicles)
    vehicles = parse_obj_as(List[Vehicle_], vehicle)
    for veh in vehicles:
        veh_values = [
            veh.name,
            veh.cargo_capacity,
            veh.cost_in_credits,
            veh.consumables,
            veh.max_atmosphering_speed,
            veh.crew,
            veh.vehicle_class,
            veh.model,
            veh.manufacturer,
            veh.length
        ]

        veh_id = int(veh.url.split("/")[-2])
        result = insert_resource(
            "vehicle",
            "vehicle_id",
            veh_id,
            veh_columns,
            veh_values
        )
        vehicle_data.append(veh)
    return vehicle_data


@timeit
def store_species():
    specie = film1().species
    species_data = []

    spec_columns = [
        "average_height",
        "average_lifespan",
        "classification",
        "designation",
        "eye_colors",
        "hair_colors",
        "name",
        "skin_colors"
    ]

    spe = pool.map(fetch_data_v2, specie)
    specie = parse_obj_as(List[Species_], spe)
    for spec in specie:
        spec_values = [
            spec.name,
            spec.skin_colors,
            spec.hair_colors,
            spec.eye_colors,
            spec.designation,
            spec.classification,
            spec.average_lifespan,
            spec.average_height
        ]

        spec_id = int(spec.url.split("/")[-2])
        result = insert_resource(
            "species",
            "species_id",
            spec_id,
            spec_columns,
            spec_values
        )
        species_data.append(spec)
    return species_data


if __name__ == "__main__":
    film = film1()
    character_data = store_characters()
    planets_data = store_planets()
    vehicles_data = store_vehicles()
    species_data = store_species()
    starships_data = store_starships()

