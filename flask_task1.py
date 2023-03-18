import requests
import json
from flask import Flask, Response

from utils.timing import timeit
from utils.randgen import ProduceChars
from typing import List   # required for type hinting


app = Flask(__name__)


def get_url(resource_id: int, resource: str) -> str:
    """
    Args:
        resource_id:
    Returns:
    """

    home_url = "https://swapi.dev"
    relative_url = "/api/{}/{}"
    absolute_url = home_url + relative_url.format(resource, resource_id)
    return absolute_url


@app.route("/welcome")
def welcome():
    return "hello world"


@app.route("/taskone/<resource>/<int:count>/<int:start>/<int:end>")
def task_one(resource, count, start, end):

    print("[ INFO ]")

    obj = ProduceChars(
        start,
        end,
        count
    )

    resources = [element for element in obj]
    print(f"resources - {resources}")

    print(f"[ INFO ] produced {len(resources)}"
          f" random resource ids in range({start}, {end}).")

    data = []
    for resource_id in resources:
        print(f"[ INFO ] fetching data for resource_id {resource_id}...")
        url_ = get_url(resource_id, resource)

        # `requests.get()` returns a HttpResponse
        res = requests.get(url_)
        print(f"res.status_code = {res.status_code}")

        if res.status_code == 200:
            # getting dict value from response object
            result = res.json()

            # capturing name from dict object
            data.append(result.get("name"))

    output = {
        "count": len(data),
        "names": data
    }

    return Response(json.dumps(output), status=201, mimetype="application/json")