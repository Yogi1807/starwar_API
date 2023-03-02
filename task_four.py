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

from resources.films import Film   # resource model
from models.datamodels.films import Film_  # pydantic model
from models.datamodels.characters import Character_
from models.datamodels.planets import Planet_
from models.datamodels.starships_ import StarShips_
from models.datamodels.vehicles import Vehicle_
from models.datamodels.species_ import Species_

from dal.db_conn_helper import get_db_conn
from dal.dml import insert_resource
from utils.fetch_data import hit_url
from utils.timing import timeit


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
    characters = film1().characters
    characters_data = []

    char_columns = [
        "name",
        "height",
        "mass",
        "hair_color"
    ]

    for character in characters:
        response = hit_url(character)
        char = response.json()
        char = Character_(**char)
        char_values = [
            char.name,
            char.height,
            char.mass,
            char.hair_color
        ]

        char_id = int(character.split("/")[-2])
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
    for planet in planets:
        response = hit_url(planet)
        pla_ = response.json()
        pla_ = Planet_(**pla_)
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

        planet_id = int(planet.split("/")[-2])
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
    starships_data = []

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

    for starship in starships:
        response = hit_url(starship)
        star = response.json()
        star = StarShips_(**star)
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

        star_id = int(starship.split("/")[-2])
        result = insert_resource(
            "starship",
            "starship_id",
            star_id,
            star_columns,
            star_values
        )
        starships_data.append(star)
    return starships_data


@timeit
def store_vehicles():
    vehicles = film1().vehicles
    vehicles_data = []

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

    for vehicle in vehicles:
        response = hit_url(vehicle)
        veh = response.json()
        veh = Vehicle_(**veh)
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

        veh_id = int(vehicle.split("/")[-2])
        result = insert_resource(
            "vehicle",
            "vehicle_id",
            veh_id,
            veh_columns,
            veh_values
        )
        vehicles_data.append(veh)
    return vehicles_data



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

    for sp in specie:
        response = hit_url(sp)
        spec = response.json()
        spec = Species_(**spec)
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

        spec_id = int(sp.split("/")[-2])
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

