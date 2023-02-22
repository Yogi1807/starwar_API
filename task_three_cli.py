"""



"""

import argparse
from pprint import pprint
from resources.films import Film
from resources.vehicle import Vehicle
from resources.people import People
from resources.species import Species
from resources.planets import Planet
from resources.starships import Starship

# pydentic classes
from models.datamodels.films import Film_
from models.datamodels.species_ import Species_
from models.datamodels.planets import Planet_
from models.datamodels.starships_ import StarShips_
from models.datamodels.vehicles import Vehicle_
from models.datamodels.characters import Character_

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description= "fetching data")

    parser.add_argument('--film', help='Call Film')
    parser.add_argument('--people',  help='Call people')
    parser.add_argument('--planets', help='Call planets')
    parser.add_argument('--species',  help='Call species')
    parser.add_argument('--vehicle',  help='Call vehicle')
    parser.add_argument('--starships',  help='Call starships')
    info = parser.parse_args()

    if info.film:
        film_object = Film()
        total_films = film_object.get_count()
        print(f"Total films: {total_films}")
        urls = film_object.get_resource_urls()
        pprint(f"film url = {urls}")
        film_data = film_object.get_sample_data()
        film_data = Film_(**film_data)
        pprint(film_object.pull_random_data())

    if info.planets:
        planet_object = Planet()
        total_planets = planet_object.get_count()
        print(f"Total planets: {total_planets}")
        pl_urls = planet_object.get_resource_urls()
        pprint(f"planet url = {pl_urls}")
        planet_data = planet_object.get_sample_data()
        planet_data = Planet_(**planet_data)
        pprint(planet_object.pull_random_data())

    if info.species:
        species_object = Species()
        total_species = species_object.get_count()
        print(f"Total species: {total_species}")
        sp_urls = species_object.get_resource_urls()
        pprint(f"species url = {sp_urls}")
        species_data = species_object.get_sample_data()
        species_data = Species_(**species_data)
        pprint(species_object.pull_random_data())

    if info.people:
        people_object = People()
        total_people = people_object.get_count()
        print(f"Total people: {total_people}")
        pe_urls = people_object.get_resource_urls()
        pprint(f"people url = {pe_urls}")
        people_data = people_object.get_sample_data()
        people_data = Character_(**people_data)
        pprint(people_object.pull_random_data())

    if info.vehicle:
        vehicle_object = Vehicle()
        total_vehicle = vehicle_object.get_count()
        print(f"Total vehicle: {total_vehicle}")
        ve_urls = vehicle_object.get_resource_urls()
        pprint(f"vehicle url = {ve_urls}")
        vehicle_data = vehicle_object.get_sample_data(id_=4)
        vehicle_data = Vehicle_(**vehicle_data)
        pprint(vehicle_object.pull_random_data())

    if info.starships:
        starships_object = Starship()
        total_starships = starships_object.get_count()
        print(f"Total starships: {total_starships}")
        st_urls = starships_object.get_resource_urls()
        pprint(f"starships url = {st_urls}")
        starships_data = starships_object.get_sample_data(id_=9)
        starships_data = StarShips_(**starships_data)
        pprint(starships_object.pull_random_data())

breakpoint()