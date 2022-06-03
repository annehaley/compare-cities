# Uses https://simplemaps.com/data/us-cities
import pandas
import requests
import json
from pathlib import Path

# from pprint import pprint

COST_OF_LIVING_DATA = "cost_of_living_response.json"

cities_df = pandas.read_csv("uscities.csv")
cities_df = cities_df[cities_df["source"] == "shape"]


def fetch_cost_of_living_data():
    print("FETCHING COST OF LIVING DATA")
    cost_of_living_url = (
        "https://cities-cost-of-living1.p.rapidapi.com/get_cities_details_by_name"
    )
    cost_of_living_headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Host": "cities-cost-of-living1.p.rapidapi.com",
        "X-RapidAPI-Key": "7bf9de1527mshf1894980597fa11p1655d9jsn53c1b65edec4",
    }
    cost_of_living_payload = {
        "cities": [
            {"name": city["city_ascii"], "country": "United States"}
            for index, city in cities_df.head(3).iterrows()
        ]
    }
    cost_of_living_response = requests.request(
        "POST",
        cost_of_living_url,
        data=cost_of_living_payload,
        headers=cost_of_living_headers,
    )
    json.dump(cost_of_living_response.json(), open(COST_OF_LIVING_DATA, "w"), indent=4)


if not Path(COST_OF_LIVING_DATA).exists():
    fetch_cost_of_living_data()

for index, city in cities_df.head(3).iterrows():

    print(
        city["city_ascii"],
        f'({city["lat"]}, {city["lng"]})',
        city["state_id"],
        # city["county_fips"],
        city["county_name"],
        city["population"],
        city["density"],
        bool(city["military"]),
        bool(city["incorporated"]),
        city["timezone"],
        city["ranking"],
        # city["zips"],
    )
