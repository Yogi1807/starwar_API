"""
This module defines pydantic (provides Py3 data-classes validation out of the box) models used
for validation and (de)serialization in API requests/responses.
"""


from typing import List, Optional
from models.basemodel import Base


class StarShips_(Base):

    name: str
    manufacturer: str
    cost_in_credits: str
    length: str
    max_atmosphering_speed: str
    crew: str
    passengers: str
    cargo_capacity: str
    consumables: str
    hyperdrive_rating: str
    MGLT: str
    starship_class: str
    model: str

    pilots: List[str]
    films: Optional[List[str]]


if __name__ == "__main__":
    external = {
            "name": "Star Destroyer",
            "model": "Imperial I-class Star Destroyer",
            "manufacturer": "Kuat Drive Yards",
            "cost_in_credits": "150000000",
            "length": "1,600",
            "max_atmosphering_speed": "975",
            "crew": "47,060",
            "passengers": "n/a",
            "cargo_capacity": "36000000",
            "consumables": "2 years",
            "hyperdrive_rating": "2.0",
            "MGLT": "60",
            "starship_class": "Star Destroyer",
            "pilots": [],
            "films": [
                "https://swapi.dev/api/films/1/",
                "https://swapi.dev/api/films/2/",
                "https://swapi.dev/api/films/3/"
            ],
            "created": "2014-12-10T15:08:19.848000Z",
            "edited": "2014-12-20T21:23:49.870000Z",
            "url": "https://swapi.dev/api/starships/3/"
        }

    new = StarShips_(**external)
    print(new)
    breakpoint()
