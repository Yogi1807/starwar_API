"""
TODO
1. Pull data for the first movie ("A New Hope") and save in DB.
2. Replace the data for each endpoint listed in the JSON object and insert
that data into database table
For example - "A new hope" movie has following resource endpoints -
- characters
- planets
- starships
- vehicles
- species
"""

from resources.films import Film   # resource model
from models.datamodels.films import Film_  # pydantic model


if __name__ == "__main__":
    data = Film().get_sample_data(id_=1)
    film_data = Film_(**data)

    # create DB connection
    # to create a sql query to insert data into database.
    # execute the query

