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
from flask import Flask

app = Flask(__name__)


@app.route("/<resource>")
def info(resource):
    data = {
        "film":{
            "total_films": Film().get_count(),
            "urls": Film().get_resource_urls(),
            "sample_data": Film().get_sample_data(),
            "random_data": Film().pull_random_data()
        },
        "planet":{
            "total_planets": Planet().get_count(),
            "urls": Planet().get_resource_urls(),
            "sample_data": Planet().get_sample_data(),
            "random_data": Planet().pull_random_data()
        },
        "species":{
            "total_species": Species().get_count(),
            "urls": Species().get_resource_urls(),
            "sample_data": Species().get_sample_data(),
            "random_data": Species().pull_random_data()
        },
        "people":{
            "total_people": People().get_count(),
            "urls": People().get_resource_urls(),
            "sample_data": People().get_sample_data(),
            "random_data": People().pull_random_data()
        },
        "vehicle":{
            "total_vehicle": Vehicle().get_count(),
            "urls": Vehicle().get_resource_urls(),
            "sample_data": Vehicle().get_sample_data(id_=4),
            "random_data": Vehicle().pull_random_data()
        },
        "starship":{
            "total_starships": Starship().get_count(),
            "urls": Starship().get_resource_urls(),
            "sample_data": Starship().get_sample_data(id_=9),
            "random_data": Starship().pull_random_data()
        }
    }

    return data[resource]
